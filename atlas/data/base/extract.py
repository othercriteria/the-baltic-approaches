#!/usr/bin/env python3
"""Clip Natural Earth 10m physical layers to the two plate extents.

Dev tool, run once to regenerate the committed base extracts. Reads
the world shapefiles from src/ (gitignored — not redistributed) and
writes small GeoJSON extracts (approaches.json, neck.json) that ARE
committed, with provenance in README.md beside them. Pure stdlib +
the shapefile format parsed by hand (no gdal/ogr/shapely present).

    python3 atlas/data/base/extract.py

Natural Earth is public domain (CC0); see README.md for the exact
files, version, and licence text.
"""

from __future__ import annotations

import json
import struct
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "src"

# Plate extents (lon_min, lat_min, lon_max, lat_max). A small margin
# beyond the drawn neat-line lets clipped coastline run to the edge
# cleanly rather than stopping short.
PLATES = {
    "approaches": (7.6, 53.3, 12.8, 57.35),
    "neck": (8.55, 53.98, 10.25, 54.65),
}

# Which NE layers feed which geometry role.
LAYERS = {
    "coastline": ("ne_10m_coastline", "line"),
    "land": ("ne_10m_land", "polygon"),
    "rivers": ("ne_10m_rivers_lake_centerlines", "line"),
    "lakes": ("ne_10m_lakes", "polygon"),
}


# ---------------------------------------------------------------- shapefile


def read_shapes(shp_path: Path):
    """Yield (shape_type, parts, points) for each record. points is a
    flat list of (lon, lat); parts indexes ring/part starts."""
    data = shp_path.read_bytes()
    n = len(data)
    off = 100  # skip the 100-byte header
    while off < n:
        # record header: number (BE), content length in 16-bit words (BE)
        _num, clen = struct.unpack_from(">ii", data, off)
        off += 8
        content = off
        shape_type = struct.unpack_from("<i", data, content)[0]
        if shape_type in (3, 5):  # polyline / polygon
            nparts, npoints = struct.unpack_from("<ii", data, content + 36)
            p = content + 44
            parts = list(struct.unpack_from(f"<{nparts}i", data, p))
            p += 4 * nparts
            coords = struct.unpack_from(f"<{2 * npoints}d", data, p)
            pts = [(coords[2 * i], coords[2 * i + 1]) for i in range(npoints)]
            yield shape_type, parts, pts
        # else: skip (no other types in these layers)
        off = content + clen * 2


def split_parts(parts, pts):
    rings = []
    for i, start in enumerate(parts):
        end = parts[i + 1] if i + 1 < len(parts) else len(pts)
        rings.append(pts[start:end])
    return rings


# ---------------------------------------------------------------- clipping


def bbox_overlaps(pts, bbox):
    x0, y0, x1, y1 = bbox
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return not (max(xs) < x0 or min(xs) > x1 or max(ys) < y0 or min(ys) > y1)


def clip_polygon(ring, bbox):
    """Sutherland-Hodgman clip of a ring against the bbox rectangle."""
    x0, y0, x1, y1 = bbox

    def clip_edge(poly, inside, intersect):
        out = []
        if not poly:
            return out
        prev = poly[-1]
        prev_in = inside(prev)
        for cur in poly:
            cur_in = inside(cur)
            if cur_in:
                if not prev_in:
                    out.append(intersect(prev, cur))
                out.append(cur)
            elif prev_in:
                out.append(intersect(prev, cur))
            prev, prev_in = cur, cur_in
        return out

    def isect(a, b, t):
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

    poly = ring
    # left
    poly = clip_edge(
        poly,
        lambda p: p[0] >= x0,
        lambda a, b: isect(a, b, (x0 - a[0]) / (b[0] - a[0])),
    )
    # right
    poly = clip_edge(
        poly,
        lambda p: p[0] <= x1,
        lambda a, b: isect(a, b, (x1 - a[0]) / (b[0] - a[0])),
    )
    # bottom
    poly = clip_edge(
        poly,
        lambda p: p[1] >= y0,
        lambda a, b: isect(a, b, (y0 - a[1]) / (b[1] - a[1])),
    )
    # top
    poly = clip_edge(
        poly,
        lambda p: p[1] <= y1,
        lambda a, b: isect(a, b, (y1 - a[1]) / (b[1] - a[1])),
    )
    return poly


def clip_line(pts, bbox):
    """Liang-Barsky per segment; stitch consecutive in-segments into
    polylines. Returns a list of polylines (each a list of points)."""
    x0, y0, x1, y1 = bbox
    out = []
    cur = []
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        seg = _clip_segment(a, b, x0, y0, x1, y1)
        if seg is None:
            if len(cur) >= 2:
                out.append(cur)
            cur = []
            continue
        s, e = seg
        if not cur:
            cur = [s, e]
        elif cur[-1] == s:
            cur.append(e)
        else:
            if len(cur) >= 2:
                out.append(cur)
            cur = [s, e]
    if len(cur) >= 2:
        out.append(cur)
    return out


def _clip_segment(a, b, x0, y0, x1, y1):
    dx, dy = b[0] - a[0], b[1] - a[1]
    p = [-dx, dx, -dy, dy]
    q = [a[0] - x0, x1 - a[0], a[1] - y0, y1 - a[1]]
    u0, u1 = 0.0, 1.0
    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return None
        else:
            t = qi / pi
            if pi < 0:
                u0 = max(u0, t)
            else:
                u1 = min(u1, t)
    if u0 > u1:
        return None
    return ((a[0] + u0 * dx, a[1] + u0 * dy), (a[0] + u1 * dx, a[1] + u1 * dy))


def round_pts(pts, nd=4):
    return [[round(x, nd), round(y, nd)] for x, y in pts]


# ---------------------------------------------------------------- driver


def build(plate: str, bbox):
    features = []
    for role, (fname, kind) in LAYERS.items():
        shp = SRC / f"{fname}.shp"
        if not shp.exists():
            print(f"  WARN: {shp} absent, skipping {role}")
            continue
        count = 0
        for shape_type, parts, pts in read_shapes(shp):
            if not bbox_overlaps(pts, bbox):
                continue
            for ring in split_parts(parts, pts):
                if not bbox_overlaps(ring, bbox):
                    continue
                if kind == "polygon":
                    clipped = clip_polygon(ring, bbox)
                    if len(clipped) >= 3:
                        features.append(
                            {
                                "type": "Feature",
                                "properties": {"layer": role},
                                "geometry": {
                                    "type": "Polygon",
                                    "coordinates": [round_pts(clipped)],
                                },
                            }
                        )
                        count += 1
                else:
                    for line in clip_line(ring, bbox):
                        features.append(
                            {
                                "type": "Feature",
                                "properties": {"layer": role},
                                "geometry": {
                                    "type": "LineString",
                                    "coordinates": round_pts(line),
                                },
                            }
                        )
                        count += 1
        print(f"  {role}: {count} features")
    fc = {"type": "FeatureCollection", "bbox": list(bbox), "features": features}
    out = HERE / f"{plate}.json"
    out.write_text(json.dumps(fc, separators=(",", ":")))
    print(f"  wrote {out} ({out.stat().st_size // 1024} KB)")


def main():
    for plate, bbox in PLATES.items():
        print(f"[{plate}] bbox={bbox}")
        build(plate, bbox)


if __name__ == "__main__":
    main()
