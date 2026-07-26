"""Render the two front-matter map plates as SVG from atlas data.

    python3 -m atlas render approaches > plate1.svg
    python3 -m atlas render neck --face "TeX Gyre Pagella" > plate2.svg

Contract: planning/map-spec.md. One ink, pure geography. The network
layer (roads, rail, ferries, node positions) comes ONLY from
atlas/data/theater-1983.toml; the base layer (coast/water/rivers,
marsh, canal, firths, the Danevirke) from PD/CC0 geometry in
atlas/data/base/. The renderer has NO vocabulary for war marks
(front lines, arrows, unit symbols, dates, capacities) — see §6 of
the spec and test_render.py, which assert the refusals hold by
construction.

Pure stdlib. Style constants live at the top for the hand pass the
spec expects (label collisions, line weights).
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from .graph import Atlas

BASE = Path(__file__).parent / "data" / "base"

# The label face is a single parameter. Its authoritative default is
# the build's body face, passed in by `make maps` (Makefile BODYFACE);
# this fallback is used only when the renderer is run by hand.
DEFAULT_FACE = "TeX Gyre Pagella"

# ---- register (one ink; weights in pt at final size) -------------
INK = "#111111"
WATER_TINT = "#e9edf0"  # pale flat tint, <10% K (chosen over stipple)
LAND = "#ffffff"
W_COAST = 0.5
W_RIVER = 0.5
W_FIRTH = 0.9
W_CANAL = 0.7  # each of the two parallel canal lines
CANAL_GAP = 1.6  # centre-to-centre of the double canal line
W_MOTORWAY = 1.15
W_TRUNK = 0.85
W_FEDERAL = 0.62
W_SECONDARY = 0.42
W_RAIL = 0.5
RAIL_TICK = 1.4  # half-length of a rail cross-tick
RAIL_TICK_STEP = 6.5  # spacing of rail ticks along the line
RAIL_DOUBLE_GAP = 1.4  # centre-to-centre for double track
W_FRONTIER = 0.7  # national frontier (Danish): light dashed
W_IGB = 1.1  # inner-German border: heavier, plain
W_DANEVIRKE = 0.6
DOT_R = 1.5
HQ_SQUARE = 3.2  # Rendsburg's side
FS_TOWN = 6.6
FS_WATER = 6.8
FS_REGION = 7.2
FS_TITLE = 12.0
FS_LEGEND = 6.2
FS_SCALE = 6.0

# Deep red-side interior: names/edges suppressed (spec: edge-of-world
# names only, "no interior beyond them"). Rostock/Wismar/Schwerin are
# kept as edge labels; these three carry no label and no drawn edge.
SUPPRESS_NODES = {"bad_kleinen", "gadebusch", "selmsdorf"}
# Unlabeled far-bank ferry landings.
NO_LABEL = {"sehestedt_s", "nordfeld_s", "missunde_s"}
# København is drawn (labelled) but carries NO town dot (DK ruling,
# build 2 fix 10: "København stays unmarked").
NO_DOT = {"koebenhavn"}

# Per-plate label whitelist (build 2 fix 2 / Plate II item b): a node
# is labelled AND dotted only if its id is in that plate's whitelist.
# Everything else in frame — non-required towns, the Plate II-only
# neck features (Sehestedt/Missunde/Nordfeld/Sorgbrück/Hohn) on Plate
# I, the `_s` ferry landings, and every `kind="shape"` vertex — draws
# as neither dot nor label (it still exists for edge routing). This is
# what stops the theater plate's neck pile-up. The sets are the §3
# required-town lists, by node id.
LABEL_WHITELIST = {
    "approaches": {
        "aalborg",
        "aarhus",
        "vejle",
        "fredericia",
        "kolding",
        "vamdrup",
        "haderslev",
        "aabenraa",
        "padborg",
        "esbjerg",
        "flensburg",
        "schleswig",
        "rendsburg",
        "neumunster",
        "kiel",
        "eckernforde",
        "husum",
        "friedrichstadt",
        "heide",
        "itzehoe",
        "hamburg",
        "lubeck",
        "oldenburg_h",
        "puttgarden",
        "middelfart",
        "odense",
        "nyborg",
        "korsor",
        "slagelse",
        "koebenhavn",
        "vordingborg",
        "nykobing_f",
        "rodby",
        "ratzeburg",
        "schwerin",
        "wismar",
        "rostock",
    },
    "neck": {
        "rendsburg",
        "sehestedt",
        "schleswig",
        "missunde",
        "eckernforde",
        "husum",
        "friedrichstadt",
        "nordfeld",
        "sorgbruck",
        "hohn",
        "neumunster",
    },
}

# ---- per-plate configuration -------------------------------------
# extent = (lon_min, lat_min, lon_max, lat_max) of the drawn neat-line.
# water/region labels are area labels, hand-anchored at (lon, lat).

PLATES = {
    "approaches": {
        "title": "THE APPROACHES",
        # Extent nudged east a hair vs build 1 (12.70->12.80) so
        # København has room to letter INSIDE the neat-line; edge labels
        # are kept in frame by the label clamp (build 2 fix 6).
        "extent": (8.00, 53.44, 12.80, 57.28),
        "target_w": 288.0,  # 4.0in live width, portrait
        "landscape": False,
        "waters": [
            ("North Sea", 8.30, 55.45),
            ("Baltic", 11.85, 55.00),
            ("Little Belt", 9.85, 55.18),
            ("Great Belt", 10.98, 55.64),
            ("Fehmarn Belt", 11.30, 54.40),
            ("Kiel Canal", 9.24, 54.05),
            ("the Schlei", 10.02, 54.66),
            ("the Eider", 8.62, 54.26),
            ("the Trave", 10.82, 53.90),
        ],
        "regions": [
            ("JUTLAND", 9.10, 56.30),
            ("FUNEN", 10.45, 55.20),
            ("ZEALAND", 11.98, 55.44),
            ("LOLLAND-FALSTER", 11.42, 54.70),
            ("SCHLESWIG-HOLSTEIN", 9.72, 53.92),
            ("MECKLENBURG", 12.10, 53.88),
        ],
        # Country labels (build 2 fix 8): faint, tracked, even lighter
        # than the region subdivisions, placed in the emptiest land
        # zones and clamped inside the neat-line. The two Germanys carry
        # the compact period Anglophone convention (Times/Nat-Geo 1983
        # sheets: WEST GERMANY / EAST GERMANY) — the full formal names
        # run ~150pt wide and smear across a 4in plate (work order
        # permits abbreviation).
        "countries": [
            ("DENMARK", 9.00, 56.92),
            ("WEST GERMANY", 9.52, 53.62),
            ("EAST GERMANY", 11.66, 53.62),
        ],
        "scale_km": 50,
    },
    "neck": {
        "title": "THE NECK",
        "extent": (8.80, 54.03, 10.18, 54.63),
        # Landscape (reader turns the book). Sized so that, rotated 90
        # and placed at NATURAL size in the portrait live area, the
        # plate's short side stays under the 4.0in live width and the
        # labels sit at their rendered 6.6pt (no scaling, above floor).
        "target_w": 348.0,
        "landscape": True,
        "legend_corner": "bl",
        "waters": [
            ("Kiel Canal", 9.45, 54.155),
            ("the Schlei", 9.80, 54.575),
            ("the Eider", 8.86, 54.24),
            ("the Treene", 9.05, 54.55),
            ("the Danevirke", 9.42, 54.463),
        ],
        "regions": [],
        "scale_km": 10,
    },
}


# Label placement audit, populated by render_plate for the tests: per
# plate, the neat-line frame and the bounding boxes of every placed
# town / water / region / country label. The invariant (build 2 fix 6):
# every one of these boxes lies inside the frame.
LABEL_AUDIT = {}
_AREA_ACC = None


# ================================================================ geometry


def load_base(name):
    p = BASE / f"{name}.json"
    return json.loads(p.read_text()) if p.exists() else {"features": []}


class Projection:
    """Equirectangular, longitude compressed by cos(lat0). North up.
    1 SVG user unit = 1 pt. Fits the extent to target content width."""

    def __init__(self, extent, target_w, pad):
        self.lon0, self.lat0, self.lon1, self.lat1 = extent
        self.latc = 0.5 * (self.lat0 + self.lat1)
        self.k = math.cos(math.radians(self.latc))
        self.pad = pad
        world_w = (self.lon1 - self.lon0) * self.k
        world_h = self.lat1 - self.lat0
        self.scale = (target_w - 2 * pad) / world_w
        self.cw = target_w
        self.ch = world_h * self.scale + 2 * pad
        self.deg_lat_pt = self.scale  # pt per degree latitude

    def xy(self, lon, lat):
        x = self.pad + (lon - self.lon0) * self.k * self.scale
        y = self.pad + (self.lat1 - lat) * self.scale
        return x, y

    def inside(self, lon, lat, margin=0.0):
        return (
            self.lon0 - margin <= lon <= self.lon1 + margin
            and self.lat0 - margin <= lat <= self.lat1 + margin
        )


# ================================================================ svg helpers


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path_d(pts):
    if not pts:
        return ""
    d = f"M{pts[0][0]:.2f},{pts[0][1]:.2f}"
    for x, y in pts[1:]:
        d += f"L{x:.2f},{y:.2f}"
    return d


def offset_line(pts, off):
    """Offset a polyline sideways by `off` pt (for double canal/rail).
    Simple per-segment normal average; adequate at this grain."""
    if len(pts) < 2:
        return pts
    out = []
    n = len(pts)
    for i in range(n):
        if i == 0:
            ax, ay = pts[0]
            bx, by = pts[1]
        elif i == n - 1:
            ax, ay = pts[i - 1]
            bx, by = pts[i]
        else:
            ax, ay = pts[i - 1]
            bx, by = pts[i + 1]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        out.append((pts[i][0] + nx * off, pts[i][1] + ny * off))
    return out


def offset_var(pts, halfs, sign):
    """Like offset_line but with a per-vertex offset (points), signed.
    Used to build tapering water ribbons (wide fjord mouth, narrow head)."""
    if len(pts) < 2:
        return pts
    out = []
    n = len(pts)
    for i in range(n):
        if i == 0:
            ax, ay = pts[0]
            bx, by = pts[1]
        elif i == n - 1:
            ax, ay = pts[i - 1]
            bx, by = pts[i]
        else:
            ax, ay = pts[i - 1]
            bx, by = pts[i + 1]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        h = halfs[i] * sign
        out.append((pts[i][0] + nx * h, pts[i][1] + ny * h))
    return out


class SVG:
    def __init__(self, w, h, face):
        self.w, self.h, self.face = w, h, face
        self.body = []
        self.clip = None  # (x, y, w, h) neat-line clip for map layers

    def add(self, s):
        self.body.append(s)

    def poly(
        self,
        pts,
        stroke=INK,
        width=0.5,
        fill="none",
        dash=None,
        opacity=None,
        cap="round",
        join="round",
    ):
        if len(pts) < 2 and fill == "none":
            return
        d = path_d(pts)
        if fill != "none" and pts and pts[0] != pts[-1]:
            d += "Z"
        a = [
            f'd="{d}"',
            f'stroke="{stroke}"' if stroke else 'stroke="none"',
            f'stroke-width="{width}"' if stroke else "",
            f'fill="{fill}"',
            f'stroke-linecap="{cap}"',
            f'stroke-linejoin="{join}"',
        ]
        if dash:
            a.append(f'stroke-dasharray="{dash}"')
        if opacity is not None:
            a.append(f'opacity="{opacity}"')
        self.add(f"<path {' '.join(x for x in a if x)}/>")

    def line(self, x1, y1, x2, y2, stroke=INK, width=0.5, dash=None, cap="round"):
        a = [
            f'x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"',
            f'stroke="{stroke}"',
            f'stroke-width="{width}"',
            f'stroke-linecap="{cap}"',
        ]
        if dash:
            a.append(f'stroke-dasharray="{dash}"')
        self.add(f"<line {' '.join(a)}/>")

    def rect(self, x, y, w, h, stroke="none", width=0.5, fill="none", opacity=None):
        a = [
            f'x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}"',
            f'stroke="{stroke}"',
            f'stroke-width="{width}"',
            f'fill="{fill}"',
        ]
        if opacity is not None:
            a.append(f'opacity="{opacity}"')
        self.add(f"<rect {' '.join(a)}/>")

    def dot(self, x, y, r=DOT_R):
        self.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{INK}"/>')

    def text(
        self, x, y, s, size, anchor="start", italic=False, tracking=0.0, opacity=None
    ):
        a = [
            f'x="{x:.2f}" y="{y:.2f}"',
            f'font-family="{esc(self.face)}, serif"',
            f'font-size="{size}"',
            f'fill="{INK}"',
            f'text-anchor="{anchor}"',
        ]
        if italic:
            a.append('font-style="italic"')
        if tracking:
            a.append(f'letter-spacing="{tracking}"')
        if opacity is not None:
            a.append(f'opacity="{opacity}"')
        self.add(f"<text {' '.join(a)}>{esc(s)}</text>")

    def render(self):
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{self.w:.2f}pt" height="{self.h:.2f}pt" '
            f'viewBox="0 0 {self.w:.2f} {self.h:.2f}">'
        )
        defs = ""
        if self.clip:
            x, y, w, h = self.clip
            defs = (
                f'<defs><clipPath id="nl">'
                f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" '
                f'height="{h:.2f}"/></clipPath></defs>'
            )
        return head + "\n" + defs + "\n" + "\n".join(self.body) + "\n</svg>\n"


# ================================================================ label placement


class Labeller:
    """Greedy collision-avoiding placement. Candidate offsets tried in
    order; first non-overlapping box wins. Boxes accumulate."""

    OFFSETS = [
        (1, 0, "start"),
        (-1, 0, "end"),
        (0, -1, "mid"),
        (0, 1, "mid"),
        (1, -1, "start"),
        (-1, -1, "end"),
        (1, 1, "start"),
        (-1, 1, "end"),
    ]

    def __init__(self, proj):
        self.boxes = []
        self.proj = proj
        self.collisions = 0
        # the neat-line frame; every placed label box is kept inside it
        # (build 2 fix 6: no label escapes the bounding box).
        self.frame = (proj.pad, proj.pad, proj.cw - proj.pad, proj.ch - proj.pad)

    def _box_free(self, box):
        x0, y0, x1, y1 = box
        for bx in self.boxes:
            if not (x1 < bx[0] or x0 > bx[2] or y1 < bx[1] or y0 > bx[3]):
                return False
        return True

    def _in_frame(self, box, m=1.5):
        fx0, fy0, fx1, fy1 = self.frame
        return (
            box[0] >= fx0 + m
            and box[2] <= fx1 - m
            and box[1] >= fy0 + m
            and box[3] <= fy1 - m
        )

    def place(
        self, svg, x, y, text, size, italic=False, force=True, pad=3.0, tracking=0.0
    ):
        w = len(text) * size * 0.52 + (len(text) * tracking)
        h = size * 0.9
        chosen = None
        for ox, oy, anchor in self.OFFSETS:
            tx = x + ox * pad
            ty = y + oy * pad + (h * 0.32 if oy >= 0 else -h * 0.12)
            if anchor == "start":
                bx0, bx1 = tx, tx + w
            elif anchor == "end":
                bx0, bx1 = tx - w, tx
            else:
                bx0, bx1 = tx - w / 2, tx + w / 2
            box = (bx0, ty - h, bx1, ty)
            if self._in_frame(box) and self._box_free(box):
                chosen = (tx, ty, anchor, box)
                break
        if chosen is None:
            if not force:
                self.collisions += 1
                return False
            # fallback: point the label inward from the node and clamp the
            # box fully inside the frame (accept a possible overlap — logged
            # as a collision — but NEVER an out-of-frame escape).
            fx0, fy0, fx1, fy1 = self.frame
            anchor = "start" if x < (fx0 + fx1) / 2 else "end"
            ty = y + h * 0.32
            if anchor == "start":
                tx = x + pad
                bx0, bx1 = tx, tx + w
            else:
                tx = x - pad
                bx0, bx1 = tx - w, tx
            # clamp horizontally
            if bx0 < fx0 + 1.5:
                dx = (fx0 + 1.5) - bx0
                tx += dx
                bx0 += dx
                bx1 += dx
            if bx1 > fx1 - 1.5:
                dx = bx1 - (fx1 - 1.5)
                tx -= dx
                bx0 -= dx
                bx1 -= dx
            # clamp vertically
            top, bot = ty - h, ty
            if top < fy0 + 1.5:
                dy = (fy0 + 1.5) - top
                ty += dy
                top += dy
                bot += dy
            if bot > fy1 - 1.5:
                dy = bot - (fy1 - 1.5)
                ty -= dy
                top -= dy
                bot -= dy
            box = (bx0, top, bx1, bot)
            chosen = (tx, ty, anchor, box)
            self.collisions += 1
        tx, ty, anchor, box = chosen
        self.boxes.append(box)
        sa = {"start": "start", "end": "end", "mid": "middle"}[anchor]
        svg.text(tx, ty, text, size, anchor=sa, italic=italic, tracking=tracking)
        return True

    def reserve(self, box):
        self.boxes.append(box)


# ================================================================ the renderer


def render_plate(name, face=DEFAULT_FACE):
    global _AREA_ACC
    _AREA_ACC = []
    cfg = PLATES[name]
    atlas = Atlas.load()
    raw = _raw_toml()
    tracks = {e["id"]: e.get("tracks") for e in raw.get("edge", [])}
    # shape nodes: real, named intermediate places that render as
    # unlabelled, undotted path vertices (spec build-2 work order). Their
    # `kind="shape"` classification lives in the atlas TOML; graph.py
    # ignores it, the renderer reads it from the raw table.
    shape = {n["id"] for n in raw.get("node", []) if n.get("kind") == "shape"}
    whitelist = LABEL_WHITELIST[name]

    def labelled(nid):
        """A node is labelled iff it is in this plate's whitelist and is
        not a shape vertex, a far-bank landing, or a suppressed red node."""
        return (
            nid in whitelist
            and nid not in shape
            and nid not in NO_LABEL
            and nid not in SUPPRESS_NODES
        )

    pad = 34.0
    proj = Projection(cfg["extent"], cfg["target_w"], pad)
    svg = SVG(proj.cw, proj.ch, face)
    lab = Labeller(proj)

    x0, y0 = proj.pad, proj.pad
    nlx, nly = proj.cw - proj.pad, proj.ch - proj.pad  # neat-line far corner

    def project_line(coords):
        return [proj.xy(lon, lat) for lon, lat in coords]

    # clip every map layer to the neat-line; labels/furniture draw over.
    svg.clip = (x0, y0, nlx - x0, nly - y0)
    svg.add('<g clip-path="url(#nl)">')

    # --- water background -----------------------------------------
    svg.add("<!-- water -->")
    svg.rect(x0, y0, nlx - x0, nly - y0, fill=WATER_TINT)

    base = load_base(name)
    hand = load_base("handdigitized")

    # land polygons knock the water tint back to white
    svg.add("<!-- land -->")
    for f in base["features"]:
        if f["properties"]["layer"] == "land":
            pts = project_line(f["geometry"]["coordinates"][0])
            svg.poly(pts, stroke="none", fill=LAND)
    # lakes: water tint inside land
    for f in base["features"]:
        if f["properties"]["layer"] == "lakes":
            pts = project_line(f["geometry"]["coordinates"][0])
            svg.poly(pts, stroke=INK, width=W_COAST, fill=WATER_TINT)

    # marsh stipple (neck only) — the one relief symbol besides the hachure
    for f in hand["features"]:
        if f["properties"]["layer"] == "marsh" and _in_extent_poly(
            f["geometry"]["coordinates"][0], proj
        ):
            pts = project_line(f["geometry"]["coordinates"][0])
            _stipple(svg, pts, proj)

    # --- coastline (fine) -----------------------------------------
    svg.add("<!-- coastline -->")
    for f in base["features"]:
        if f["properties"]["layer"] == "coastline":
            svg.poly(
                project_line(f["geometry"]["coordinates"]), stroke=INK, width=W_COAST
            )

    # --- rivers / firths (hand-digitized base) --------------------
    # Drawn as FILLED water ribbons (tint fill + fine bank lines) so the
    # Schlei reads as a fjord and the Eider as a river, not as thin
    # lines (build 2 Plate II acceptance blocker). Widths come from each
    # feature's GUESS-tier `half_km`, converted to points at this
    # plate's scale — so they are thin on the theater plate and legible
    # water bodies on the neck plate.
    svg.add("<!-- hand water (ribbons) -->")
    for f in hand["features"]:
        layer = f["properties"]["layer"]
        if layer in ("river", "firth"):
            coords = f["geometry"]["coordinates"]
            if not _touches_extent(coords, proj):
                continue
            _water_ribbon(svg, project_line(coords), _halfs_pt(f, proj, coords))
    # NE rivers (e.g. the Elbe) as thin lines
    for f in base["features"]:
        if f["properties"]["layer"] == "rivers":
            svg.poly(
                project_line(f["geometry"]["coordinates"]), stroke=INK, width=W_RIVER
            )
    # the Kiel Canal: firm engineered waterway — a filled ribbon with two
    # parallel bank lines, the heaviest water feature (spec §4).
    for f in hand["features"]:
        if f["properties"]["layer"] == "canal":
            coords = f["geometry"]["coordinates"]
            if not _touches_extent(coords, proj):
                continue
            _water_ribbon(
                svg, project_line(coords), _halfs_pt(f, proj, coords), bank=W_CANAL
            )

    # --- frontiers (real national only) ---------------------------
    svg.add("<!-- frontiers -->")
    _draw_frontiers(svg, proj, name)

    # --- network layer (atlas ONLY) -------------------------------
    svg.add("<!-- network (from atlas) -->")
    drawn_edges = []
    for e in atlas.edges:
        if e.a in SUPPRESS_NODES or e.b in SUPPRESS_NODES:
            continue
        na, nb = atlas.nodes[e.a], atlas.nodes[e.b]
        if not (proj.inside(na.lon, na.lat, 0.05) or proj.inside(nb.lon, nb.lat, 0.05)):
            continue
        p1 = proj.xy(na.lon, na.lat)
        p2 = proj.xy(nb.lon, nb.lat)
        drawn_edges.append(e.id)
        if e.mode == "ferry":
            svg.poly([p1, p2], stroke=INK, width=0.6, dash="3.2,2.4")
        elif e.mode == "rail":
            _draw_rail(svg, [p1, p2], double=(tracks.get(e.id) == "double"))
        else:
            svg.poly([p1, p2], stroke=INK, width=_road_w(e.cls))

    # --- the Danevirke: earthwork hachure (over the network so the
    #     rampart reads; it is the plate's subject relief) -----------
    for f in hand["features"]:
        if f["properties"]["layer"] == "danevirke" and _touches_extent(
            f["geometry"]["coordinates"], proj
        ):
            _hachure(svg, project_line(f["geometry"]["coordinates"]))

    # --- nodes + HQ mark ------------------------------------------
    # A node gets a dot only if it is labelled on this plate (so shape
    # vertices, ferry landings, and non-whitelisted towns carry no dot);
    # Rendsburg gets the HQ square; København is labelled but unmarked.
    svg.add("<!-- nodes -->")
    for nid, n in atlas.nodes.items():
        if not proj.inside(n.lon, n.lat):
            continue
        if nid == "rendsburg":
            x, y = proj.xy(n.lon, n.lat)
            s = HQ_SQUARE
            svg.rect(x - s / 2, y - s / 2, s, s, stroke=INK, width=0.7, fill=LAND)
        elif labelled(nid) and nid not in NO_DOT:
            x, y = proj.xy(n.lon, n.lat)
            svg.dot(x, y)

    svg.add("</g>")  # end neat-line clip

    # --- labels ----------------------------------------------------
    # countries first (faintest; the ground beneath the subdivisions)
    svg.add("<!-- labels: countries (faintest) -->")
    for txt, lon, lat in cfg.get("countries", []):
        if not proj.inside(lon, lat, 0.1):
            continue
        x, y = proj.xy(lon, lat)
        _clamp_text(svg, proj, x, y, txt, FS_REGION, tracking=1.8, opacity=0.24)

    svg.add("<!-- labels: regions (faint) -->")
    for txt, lon, lat in cfg["regions"]:
        if not proj.inside(lon, lat, 0.1):
            continue
        x, y = proj.xy(lon, lat)
        _clamp_text(svg, proj, x, y, txt, FS_REGION, tracking=1.4, opacity=0.32)

    svg.add("<!-- labels: waters (small caps) -->")
    for txt, lon, lat in cfg["waters"]:
        if not proj.inside(lon, lat, 0.1):
            continue
        x, y = proj.xy(lon, lat)
        _clamp_text(
            svg,
            proj,
            x,
            y,
            txt.upper(),
            FS_WATER * 0.9,
            italic=True,
            tracking=0.8,
            opacity=0.85,
        )

    svg.add("<!-- labels: towns (roman, greedy, whitelist only) -->")
    # reserve title / furniture zones so labels avoid them
    _reserve_furniture(lab, proj, cfg)
    town_start = len(lab.boxes)
    ordered = sorted(
        (
            n
            for nid, n in atlas.nodes.items()
            if labelled(nid) and proj.inside(n.lon, n.lat)
        ),
        key=lambda n: n.lat,
        reverse=True,
    )
    for n in ordered:
        x, y = proj.xy(n.lon, n.lat)
        lab.place(svg, x, y, _display_name(n.name), FS_TOWN)

    # record the placed label boxes for the in-frame invariant test
    LABEL_AUDIT[name] = {
        "frame": lab.frame,
        "boxes": list(lab.boxes[town_start:]) + list(_AREA_ACC),
    }

    # --- furniture -------------------------------------------------
    svg.add("<!-- furniture -->")
    _draw_furniture(svg, proj, cfg, face)

    return svg.render(), drawn_edges


# ---------------------------------------------------------------- sub-draws


def _km_to_pt(proj, km):
    return km * (proj.deg_lat_pt / 111.2)


def _halfs_pt(feature, proj, coords):
    """Per-vertex half-widths in points for a water feature, from its
    GUESS-tier `half_km` (a scalar or a per-vertex list), with a floor so
    nothing vanishes at theater scale."""
    hk = feature["properties"].get("half_km", 0.25)
    floor = 0.9  # pt, each side
    if isinstance(hk, list):
        vals = hk + [hk[-1]] * (len(coords) - len(hk))
        return [max(floor, _km_to_pt(proj, v)) for v in vals[: len(coords)]]
    return [max(floor, _km_to_pt(proj, hk))] * len(coords)


def _water_ribbon(svg, pts, halfs, bank=W_COAST):
    """A filled water ribbon: tint fill bounded by two fine bank lines.
    This is what makes a hand-digitized centreline read as WATER (a fjord
    or a canal) rather than as a stroked line."""
    if len(pts) < 2:
        return
    left = offset_var(pts, halfs, +1)
    right = offset_var(pts, halfs, -1)
    svg.poly(left + right[::-1], stroke="none", fill=WATER_TINT)
    svg.poly(left, stroke=INK, width=bank)
    svg.poly(right, stroke=INK, width=bank)


def _clamp_text(svg, proj, x, y, text, size, italic=False, tracking=0.0, opacity=None):
    """Draw a middle-anchored area label (water/region/country), shifting
    it so its box stays inside the neat-line (build 2 fix 6)."""
    w = len(text) * size * 0.52 + len(text) * tracking
    h = size * 0.9
    fx0, fy0 = proj.pad, proj.pad
    fx1, fy1 = proj.cw - proj.pad, proj.ch - proj.pad
    x = min(max(x, fx0 + 1.5 + w / 2), fx1 - 1.5 - w / 2)
    y = min(max(y, fy0 + 1.5 + h), fy1 - 1.5)
    if _AREA_ACC is not None:
        _AREA_ACC.append((x - w / 2, y - h, x + w / 2, y))
    svg.text(
        x,
        y,
        text,
        size,
        anchor="middle",
        italic=italic,
        tracking=tracking,
        opacity=opacity,
    )


def _road_w(cls):
    return {
        "motorway": W_MOTORWAY,
        "trunk": W_TRUNK,
        "federal": W_FEDERAL,
        "secondary": W_SECONDARY,
    }.get(cls, W_TRUNK)


def _draw_rail(svg, pts, double=False):
    if double:
        a = offset_line(pts, RAIL_DOUBLE_GAP / 2)
        b = offset_line(pts, -RAIL_DOUBLE_GAP / 2)
        svg.poly(a, stroke=INK, width=W_RAIL)
        svg.poly(b, stroke=INK, width=W_RAIL)
    else:
        svg.poly(pts, stroke=INK, width=W_RAIL)
    # cross ticks along the (centre) line
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    L = math.hypot(x2 - x1, y2 - y1)
    if L < 1:
        return
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    d = RAIL_TICK_STEP
    while d < L:
        cx, cy = x1 + ux * d, y1 + uy * d
        svg.line(
            cx - nx * RAIL_TICK,
            cy - ny * RAIL_TICK,
            cx + nx * RAIL_TICK,
            cy + ny * RAIL_TICK,
            stroke=INK,
            width=0.4,
        )
        d += RAIL_TICK_STEP


def _hachure(svg, pts):
    """Earthwork hachure: a line with short ticks on the south face."""
    svg.poly(pts, stroke=INK, width=0.85)
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        L = math.hypot(x2 - x1, y2 - y1)
        if L < 1:
            continue
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        # south = +y in svg; pick the downward normal
        nx, ny = (-uy, ux) if ux >= 0 else (uy, -ux)
        if ny < 0:
            nx, ny = -nx, -ny
        d = 1.5
        while d < L:
            cx, cy = x1 + ux * d, y1 + uy * d
            svg.line(cx, cy, cx + nx * 2.8, cy + ny * 2.8, stroke=INK, width=0.45)
            d += 3.2


def _stipple(svg, pts, proj):
    """Marsh stipple: a scatter of tiny dots inside the polygon."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    step = 4.6
    row = 0
    y = y0 + 2
    while y < y1:
        x = x0 + 2 + (step / 2 if row % 2 else 0)
        while x < x1:
            if _pt_in_poly(x, y, pts):
                svg.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.35" fill="{INK}"/>')
            x += step
        y += step
        row += 1


def _draw_frontiers(svg, proj, name):
    """The Danish frontier (light dashed) and the IGB (heavier, plain,
    with its two real gaps). Hand-digitized generalized traces —
    GUESS-tier, disclosed in the base README. Real national frontiers
    only; no other boundary is ever drawn."""
    # Danish frontier: from the Wadden coast east to Flensburg Fjord,
    # ~lat 54.83. Western end trimmed to the coastline (build 2 fix 9:
    # no dashed protrusion into the North Sea; it started at 8.60 before).
    dk = [(8.84, 54.905), (9.05, 54.89), (9.25, 54.85), (9.43, 54.83)]
    if _touches_extent(dk, proj):
        svg.poly(
            [proj.xy(lo, la) for lo, la in dk],
            stroke=INK,
            width=W_FRONTIER,
            dash="4,2.5",
        )
    # IGB SE of Lubeck: Baltic (Priwall) south past the Ratzeburg lakes,
    # with gaps at Schlutup (road ~53.90) and Herrnburg (rail ~53.79).
    igb = [
        (10.87, 53.96),
        (10.84, 53.90),
        (10.82, 53.83),
        (10.80, 53.76),
        (10.78, 53.69),
        (10.76, 53.62),
        (10.74, 53.56),
    ]
    if _touches_extent(igb, proj):
        pts = [proj.xy(lo, la) for lo, la in igb]
        gaps = [proj.xy(10.83, 53.90), proj.xy(10.805, 53.79)]  # Schlutup, Herrnburg
        _line_with_gaps(svg, pts, gaps, W_IGB)


def _line_with_gaps(svg, pts, gap_pts, width, gap=3.0):
    """Draw a polyline broken by small gaps near given points."""
    seg = [pts[0]]
    for p in pts[1:]:
        seg.append(p)
    # split by proximity to gap points
    out = []
    cur = [pts[0]]
    for i in range(1, len(pts)):
        a, b = pts[i - 1], pts[i]
        broke = False
        for g in gap_pts:
            if _seg_near(a, b, g, gap):
                # break here
                cur.append(_toward(a, b, g, -gap))
                out.append(cur)
                cur = [_toward(a, b, g, gap)]
                broke = True
                break
        if not broke:
            cur.append(b)
    out.append(cur)
    for s in out:
        if len(s) >= 2:
            svg.poly(s, stroke=INK, width=width)


def _toward(a, b, g, d):
    L = math.hypot(b[0] - a[0], b[1] - a[1]) or 1
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    # project g onto segment param, offset by d
    t = (g[0] - a[0]) * ux + (g[1] - a[1]) * uy
    t = max(0, min(L, t + d))
    return (a[0] + ux * t, a[1] + uy * t)


def _seg_near(a, b, g, tol):
    L2 = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 or 1
    t = ((g[0] - a[0]) * (b[0] - a[0]) + (g[1] - a[1]) * (b[1] - a[1])) / L2
    if t < 0 or t > 1:
        return False
    px, py = a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])
    return math.hypot(px - g[0], py - g[1]) < tol


# ---------------------------------------------------------------- furniture


def _reserve_furniture(lab, proj, cfg):
    # title band (top), legend box (a corner), scale bar (bottom) —
    # keep town labels out of them.
    lab.reserve((proj.pad, 0, proj.cw - proj.pad, proj.pad))  # title
    # scale bar zone (bottom-left, inside the neat-line)
    lab.reserve((proj.pad, proj.ch - proj.pad - 22, proj.pad + 110, proj.ch - proj.pad))
    # N-tick zone (top-left, inside)
    lab.reserve((proj.pad, proj.pad, proj.pad + 24, proj.pad + 30))
    lab.reserve(_legend_box(proj, cfg))


def _legend_box(proj, cfg):
    """Legend rectangle. Corner is per-plate: top-right by default; the
    neck uses bottom-left (stacked above the scale bar) because its
    top-right corner is owned by the Schlei/Eckernforde-Bay water and
    label."""
    w, h = 104, 66
    if cfg.get("legend_corner") == "bl":
        x = proj.pad + 4
        y = proj.ch - proj.pad - h - 17  # above the scale bar
    else:
        x = proj.cw - proj.pad - w - 4
        y = proj.pad + 4
    return (x, y, x + w, y + h)


def _draw_furniture(svg, proj, cfg, face):
    # neat-line
    svg.rect(
        proj.pad,
        proj.pad,
        proj.cw - 2 * proj.pad,
        proj.ch - 2 * proj.pad,
        stroke=INK,
        width=0.6,
        fill="none",
    )
    # title (small caps, tracked), above the neat-line
    svg.text(
        proj.cw / 2,
        proj.pad - 12,
        cfg["title"],
        FS_TITLE,
        anchor="middle",
        tracking=2.2,
    )
    # N tick, top-left inside
    nx, ny = proj.pad + 12, proj.pad + 20
    svg.line(nx, ny, nx, ny - 12, stroke=INK, width=0.8)
    svg.add(
        f'<path d="M{nx:.1f},{ny - 12:.1f} l-1.7,4 l1.7,-1.6 l1.7,1.6 z" fill="{INK}"/>'
    )
    svg.text(nx, ny + 7, "N", 6.5, anchor="middle")
    # scale bar (bottom-left inside)
    _scale_bar(svg, proj, cfg["scale_km"])
    # legend (<=5 lines)
    _legend(svg, proj, cfg)


def _scale_bar(svg, proj, km):
    pt_per_km = proj.deg_lat_pt / 111.2
    length = km * pt_per_km
    x = proj.pad + 10
    y = proj.ch - proj.pad - 12
    svg.line(x, y, x + length, y, stroke=INK, width=0.9, cap="butt")
    for xx in (x, x + length / 2, x + length):
        svg.line(xx, y, xx, y - 3, stroke=INK, width=0.9, cap="butt")
    svg.text(x, y - 5, "0", FS_SCALE, anchor="middle")
    svg.text(x + length, y - 5, f"{km} km", FS_SCALE, anchor="middle")


def _legend(svg, proj, cfg):
    box = _legend_box(proj, cfg)
    x0, y0, x1, y1 = box
    svg.rect(x0, y0, x1 - x0, y1 - y0, stroke=INK, width=0.4, fill="#ffffff")
    # Every drawn line class is legended, including the rail double/single
    # distinction (build 2 fix 4) and the canal waterway symbol (fix 5).
    rows = [
        ("motorway", "road", W_MOTORWAY, None),
        ("rail (double)", "rail2", None, None),
        ("rail (single)", "rail1", None, None),
        ("canal", "canal", None, None),
        ("ferry", "ferry", 0.6, "3.2,2.4"),
        ("frontier", "road", W_FRONTIER, "4,2.5"),
        ("HQ", "hq", None, None),
    ]
    lx = x0 + 6
    ty = y0 + 10
    for label, kind, w, dash in rows:
        sx = lx
        cy = ty - 2
        if kind in ("rail1", "rail2"):
            if kind == "rail2":
                svg.line(
                    sx,
                    cy - RAIL_DOUBLE_GAP / 2,
                    sx + 16,
                    cy - RAIL_DOUBLE_GAP / 2,
                    stroke=INK,
                    width=W_RAIL,
                )
                svg.line(
                    sx,
                    cy + RAIL_DOUBLE_GAP / 2,
                    sx + 16,
                    cy + RAIL_DOUBLE_GAP / 2,
                    stroke=INK,
                    width=W_RAIL,
                )
            else:
                svg.line(sx, cy, sx + 16, cy, stroke=INK, width=W_RAIL)
            for t in (4, 8, 12):
                svg.line(sx + t, cy - 2.2, sx + t, cy + 2.2, stroke=INK, width=0.4)
        elif kind == "canal":
            # a short filled waterway ribbon with two bank lines
            g = CANAL_GAP / 2 + 0.4
            svg.rect(sx, cy - g, 16, 2 * g, stroke="none", fill=WATER_TINT)
            svg.line(sx, cy - g, sx + 16, cy - g, stroke=INK, width=W_CANAL)
            svg.line(sx, cy + g, sx + 16, cy + g, stroke=INK, width=W_CANAL)
        elif kind == "hq":
            svg.rect(
                sx + 5,
                cy - 1.6,
                HQ_SQUARE,
                HQ_SQUARE,
                stroke=INK,
                width=0.7,
                fill="#ffffff",
            )
        else:
            svg.line(sx, cy, sx + 16, cy, stroke=INK, width=w, dash=dash)
        svg.text(lx + 22, ty, label, FS_LEGEND, anchor="start")
        ty += 8


# ---------------------------------------------------------------- misc utils

_RAW = None


def _raw_toml():
    global _RAW
    if _RAW is None:
        import tomllib

        _RAW = tomllib.loads(
            (Path(__file__).parent / "data" / "theater-1983.toml").read_text()
        )
    return _RAW


def _display_name(name):
    # trim parentheticals for a cleaner plate; the atlas keeps the full name
    return name.split(" (")[0]


def _touches_extent(coords, proj):
    return any(proj.inside(lo, la, 0.02) for lo, la in coords)


def _in_extent_poly(coords, proj):
    return any(proj.inside(lo, la, 0.1) for lo, la in coords)


def _pt_in_poly(x, y, pts):
    inside = False
    n = len(pts)
    j = n - 1
    for i in range(n):
        xi, yi = pts[i]
        xj, yj = pts[j]
        if ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
        ):
            inside = not inside
        j = i
    return inside


# ---------------------------------------------------------------- CLI


def cmd_render(args):
    face = args.face or DEFAULT_FACE
    svg, _ = render_plate(args.plate, face=face)
    if args.out:
        Path(args.out).write_text(svg)
    else:
        import sys

        sys.stdout.write(svg)
    return 0


def add_subparser(sub):
    pr = sub.add_parser("render", help="render a map plate to SVG")
    pr.add_argument("plate", choices=list(PLATES.keys()))
    pr.add_argument("--face", default="", help="label face (default: build body face)")
    pr.add_argument("--out", default="", help="output path (default: stdout)")
    return pr
