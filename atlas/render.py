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
RAIL_TICK = 1.6  # length of a rail tick (per side)
RAIL_TICK_STEP = 6.5  # spacing of rail ticks along the line
W_FRONTIER = 0.8  # national frontier (Danish): light dotted
W_IGB = 1.1  # inner-German border: heavier dotted
# Frontiers are DOTTED (hand-pass, DK 2026-07-27): dots read lighter
# than the ferry dashes at equal ink, so the two classes stop competing
# — and a border held in dots rather than a drawn wall is the right
# philosophical weight for this map (the text's war does not treat the
# line as permanent; the plates carry clean prewar geography).
DOT_FRONTIER = "0.1,1.7"
DOT_IGB = "0.1,2.1"
W_DANEVIRKE = 0.6
DOT_R = 1.5
HQ_SQUARE = 3.2  # Rendsburg's side
FS_TOWN = 6.6
FS_WATER = 6.8
FS_REGION = 7.2
FS_TITLE = 12.0
FS_LEGEND = 6.5  # hand-pass: raised to the spec's 6.5 floor
FS_SCALE = 6.0

# Deep red-side interior: names/edges suppressed (spec: edge-of-world
# names only, "no interior beyond them"). Rostock/Wismar/Schwerin are
# kept as edge labels; these three carry no label and no drawn edge.
SUPPRESS_NODES = {"bad_kleinen", "gadebusch", "selmsdorf"}
# Unlabeled far-bank ferry landings.
NO_LABEL = {"sehestedt_s", "nordfeld_s", "missunde_s"}
# Build-3 amendment (DK): the build-2 "København stays unmarked" ruling
# was over-read — "no special treatment" means no capital styling, NOT
# dotless. København carries an ordinary dot + label like any town, so
# nothing is dot-suppressed.
NO_DOT: set[str] = set()

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

# Per-node label-side hints (build 3, DK review). A hint names the side
# the labeller should TRY FIRST for that town's dot; it still falls back
# to the ordinary greedy order if that side collides, so a hint never
# forces an out-of-frame or overlapping box. Used only for the handful of
# labels DK called out:
#   - Aarhus / Vejle labels to the LEFT of their dots (item 2);
#   - Middelfart / Kolding pushed apart (item 3);
#   - Hohn off the Rendsburg-Sorgbrück rail, which runs just north of it
#     (item 11) — nudged south.
LABEL_HINTS = {
    "approaches": {
        "aarhus": "left",
        "vejle": "left",
        # Fredericia / Middelfart / Kolding are packed at the Little Belt
        # narrows (Fredericia and Middelfart dots nearly coincide); fan
        # them into distinct directions so they read (item 3): Fredericia
        # NE over the belt, Middelfart E, Kolding W into Jutland.
        "fredericia": "above-right",
        "middelfart": "right",
        "kolding": "left",
    },
    "neck": {
        "hohn": "below",
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
        # Water area labels. Several were nudged in build 3 (item 4) to
        # clear town labels: BALTIC out into open sea SE of Falster (was
        # on top of Vordingborg); LITTLE BELT south into the strait (was
        # grazing Haderslev/FUNEN). THE TRAVE (hand-pass) moved further
        # up the river's real course (toward Bad Oldesloe), into the
        # clear triangle north of the Hamburg–Lübeck corridor — the old
        # spot at the drawn trace's head sat ON the motorway/rail pair.
        "waters": [
            ("North Sea", 8.30, 55.45),
            ("Baltic", 12.28, 54.80),
            ("Little Belt", 9.78, 55.08),
            ("Great Belt", 10.98, 55.64),
            ("Fehmarn Belt", 11.30, 54.40),
            ("Kiel Canal", 9.22, 54.02),
            # Hand-pass: onto the firth's own water at its mouth — the old
            # spot NE of it sat in the band SCHLESWIG now occupies.
            ("the Schlei", 10.01, 54.575),
            ("the Eider", 8.62, 54.26),
            ("the Trave", 10.15, 53.845),
        ],
        # FUNEN (hand-pass) into the island's empty south interior — at
        # 55.26 it sat under the cross-island road and Nyborg's label.
        # SCHLESWIG-HOLSTEIN (hand-pass): the composite tracked name
        # spanned ~2° of longitude and an obstacle audit found NO
        # placement (single or stacked) clearing the road net and the
        # Elbe-estuary coast. Set instead as the two duchies, SCHLESWIG
        # north of the Schlei and HOLSTEIN south — each crossed exactly
        # once, near-perpendicular, by one route bundle — which is also
        # the text's own working vocabulary for the ground (the covering
        # force trades Holstein; the corps holds Schleswig).
        # PROVISIONAL pending DK ratification (hand-pass, 2026-07-27).
        "regions": [
            ("JUTLAND", 9.10, 56.30),
            ("FUNEN", 10.45, 55.15),
            ("ZEALAND", 11.98, 55.44),
            ("LOLLAND-FALSTER", 11.42, 54.70),
            ("SCHLESWIG", 9.38, 54.68),
            ("HOLSTEIN", 10.05, 53.97),
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
        # Build 3 item 9: the legend was oversized (104x66) and, bottom-
        # left, reached up over the Eider ribbon + a water label while
        # crowding the scale bar. It stays bottom-left (the emptiest open
        # water on this plate — the top-right the review imagined is in
        # fact occupied by the Eckernforde node and the Schlei/Missunde/
        # Schleswig cluster, see build report) but is now content-sized
        # and flush to the bottom neat-line, CLEARING the Eider ribbon and
        # THE EIDER label; the scale bar moves to the opposite (bottom-
        # right) corner so the two no longer crowd.
        "legend_corner": "bl",
        "waters": [
            ("Kiel Canal", 9.45, 54.155),
            ("the Schlei", 9.82, 54.58),
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

    # side-hint -> the (ox, oy, anchor) candidate to try first
    _PREFER = {
        "right": (1, 0, "start"),
        "left": (-1, 0, "end"),
        "above": (0, -1, "mid"),
        "below": (0, 1, "mid"),
        "above-right": (1, -1, "start"),
        "below-right": (1, 1, "start"),
        "above-left": (-1, -1, "end"),
        "below-left": (-1, 1, "end"),
    }

    def place(
        self,
        svg,
        x,
        y,
        text,
        size,
        italic=False,
        force=True,
        pad=3.0,
        tracking=0.0,
        prefer=None,
    ):
        w = len(text) * size * 0.52 + (len(text) * tracking)
        h = size * 0.9
        chosen = None
        offsets = self.OFFSETS
        if prefer in self._PREFER:
            p = self._PREFER[prefer]
            offsets = [p] + [o for o in self.OFFSETS if o != p]
        for ox, oy, anchor in offsets:
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
    hints = LABEL_HINTS.get(name, {})
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
        lab.place(svg, x, y, _display_name(n.name), FS_TOWN, prefer=hints.get(n.id))

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


def _rail_tick_side(ux, uy):
    """Deterministic tick side for single track: the NORTH side of the
    run (falling back to EAST for near-vertical runs). Keyed to compass
    direction, not vertex order, so adjacent edges digitized in opposite
    directions still tick the same side (the hand-pass counter-brief)."""
    nx, ny = -uy, ux
    if abs(ny) > 0.05:
        if ny > 0:  # svg +y is south; keep the upward normal
            nx, ny = -nx, -ny
    elif nx < 0:
        nx, ny = -nx, -ny
    return nx, ny


def _draw_rail(svg, pts, double=False):
    """One centreline for both classes; the track count is carried by the
    ticks — one side for single, both sides for double (the period topo
    convention; hand-pass, DK 2026-07-27)."""
    svg.poly(pts, stroke=INK, width=W_RAIL)
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    L = math.hypot(x2 - x1, y2 - y1)
    if L < 1:
        return
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = _rail_tick_side(ux, uy)
    d = RAIL_TICK_STEP
    while d < L:
        cx, cy = x1 + ux * d, y1 + uy * d
        if double:
            svg.line(
                cx - nx * RAIL_TICK,
                cy - ny * RAIL_TICK,
                cx + nx * RAIL_TICK,
                cy + ny * RAIL_TICK,
                stroke=INK,
                width=0.4,
            )
        else:
            svg.line(
                cx,
                cy,
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
    """The Danish frontier (light dotted) and the IGB (heavier dotted,
    with its two real gaps). Hand-digitized generalized traces —
    GUESS-tier, disclosed in the base README. Real national frontiers
    only; no other boundary is ever drawn."""
    # Danish frontier: Wadden-Sea coast (west) to Flensburg Fjord (east),
    # light dashed. Build 3 item 5 RESEARCHED terminus: the 1983 land
    # border reaches the Wadden coast just west of Siltoft (the Siltoftvej
    # crossing is 54°54'41"N 8°40'11"E; the drawn NE mainland dike here
    # runs at ~8.665E, ~54.912N), then runs E past Rudbøl and on to the
    # Flensburg-Firth terminus at ~54°50'22"N 9°24'16"E. The western
    # vertex is set ON the drawn coastline (not short of it — build 2 had
    # over-corrected it inland to 8.84 — and not out to sea). Sources in
    # atlas/data/base/README.md. GUESS-tier generalized trace.
    dk = [
        (8.665, 54.912),
        (8.70, 54.910),
        (8.78, 54.906),
        (8.90, 54.900),
        (9.05, 54.892),
        (9.20, 54.868),
        (9.32, 54.850),
        (9.43, 54.837),
    ]
    if _touches_extent(dk, proj):
        svg.poly(
            [proj.xy(lo, la) for lo, la in dk],
            stroke=INK,
            width=W_FRONTIER,
            dash=DOT_FRONTIER,
        )
    # IGB SE of Lubeck. Build 3 item 6 RESEARCHED course: from the Baltic
    # at Priwall (E of Travemunde) south past the Schlutup (road) and
    # Herrnburg (rail) gaps, then EAST of Ratzeburg — the border ran along
    # the NE/E shore of the Ratzeburger See (between Rothenhusen/Gross
    # Sarau and Romnitz), so Ratzeburg (FRG, ~10.76E) sits just WEST of
    # the line, not on a straight tangent — then SE toward the Schaalsee
    # and on south. GUESS-tier, shaped from the real course. Sources in
    # atlas/data/base/README.md.
    igb = [
        (10.90, 53.955),  # Priwall / Baltic shore
        (10.87, 53.925),
        (10.845, 53.905),  # approaching Schlutup
        (10.82, 53.875),
        (10.80, 53.845),
        (10.785, 53.815),  # approaching Herrnburg
        (10.78, 53.785),
        (10.795, 53.755),  # NE shore, Ratzeburger See (Rothenhusen/Gross Sarau)
        (10.81, 53.720),  # E shore — Ratzeburg (10.76) lies WEST of here
        (10.82, 53.685),  # S of the lake
        (10.865, 53.640),  # bending SE toward the Schaalsee
        (10.92, 53.595),  # Schaalsee
        (10.95, 53.540),
        (10.96, 53.470),  # on south to the neat-line
    ]
    if _touches_extent(igb, proj):
        pts = [proj.xy(lo, la) for lo, la in igb]
        # gaps: Schlutup (road) and Herrnburg (rail)
        gaps = [proj.xy(10.833, 53.895), proj.xy(10.783, 53.800)]
        _line_with_gaps(svg, pts, gaps, W_IGB, dash=DOT_IGB)


def _line_with_gaps(svg, pts, gap_pts, width, gap=3.0, dash=None):
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
            svg.poly(s, stroke=INK, width=width, dash=dash)


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
    # scale bar zone (bottom corner opposite the legend)
    sx, sy, slen = _scale_pos(proj, cfg)
    lab.reserve((sx - 6, sy - 10, sx + slen + 12, sy + 4))
    # N-tick zone (top-left, inside)
    lab.reserve((proj.pad, proj.pad, proj.pad + 24, proj.pad + 30))
    lab.reserve(_legend_box(proj, cfg))


# Legend rows (every drawn line class, incl. the rail double/single
# distinction and the canal waterway symbol). One source of truth so the
# box can be sized to its contents (build 3 item 7).
LEGEND_ROWS = [
    ("motorway", "road", W_MOTORWAY, None),
    ("rail (double)", "rail2", None, None),
    ("rail (single)", "rail1", None, None),
    ("canal", "canal", None, None),
    ("ferry", "ferry", 0.6, "3.2,2.4"),
    ("frontier", "road", W_FRONTIER, DOT_FRONTIER),
    ("HQ", "hq", None, None),
]
_LEGEND_TEXTGAP = 22  # swatch-to-text offset (lx+22 in _legend)
_LEGEND_ROW_STEP = 8


def _legend_dims():
    """Legend box size, sized to its contents with tight padding (build 3
    item 7 — the box was a fixed 104x66, far wider than the text)."""
    text_w = max(len(lbl) * FS_LEGEND * 0.52 for lbl, *_ in LEGEND_ROWS)
    w = 6 + _LEGEND_TEXTGAP + text_w + 6
    h = 10 + len(LEGEND_ROWS) * _LEGEND_ROW_STEP - 4
    return w, h


def _legend_box(proj, cfg):
    """Legend rectangle, sized to content. Corner is per-plate: top-right
    by default (open water on both plates after the build-3 relocation of
    the neck legend, item 9); a plate may still request another corner."""
    w, h = _legend_dims()
    corner = cfg.get("legend_corner", "tr")
    if corner == "bl":
        x = proj.pad + 4
        y = proj.ch - proj.pad - h - 4  # flush to the bottom neat-line
    else:  # top-right
        x = proj.cw - proj.pad - w - 4
        y = proj.pad + 4
    return (x, y, x + w, y + h)


def _scale_pos(proj, cfg):
    """Left end + baseline of the scale bar. It sits opposite the legend
    corner: bottom-right when the legend owns bottom-left, else the
    default bottom-left. Keeps the two furniture pieces from crowding
    (build 3 items 7/9)."""
    length = cfg["scale_km"] * (proj.deg_lat_pt / 111.2)
    y = proj.ch - proj.pad - 12
    if cfg.get("legend_corner") == "bl":
        # Hand-pass: 110pt in from the right, not 10 — flush right put
        # the bar's zero end on the Neumünster junction, and 56 put it on
        # the town's own label; the truly clear bottom band lies between
        # the Neumünster rail approach and the canal/rail exits at left.
        x = proj.cw - proj.pad - 110 - length
    else:
        x = proj.pad + 10
    return x, y, length


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
        proj.pad - 15,
        cfg["title"],
        FS_TITLE,
        anchor="middle",
        tracking=2.2,
    )
    # Year subtitle (build 3 item 8): dates the GEOGRAPHY, restrained and
    # subordinate to the title, consistent on both plates. This is not a
    # campaign timestamp — the no-time refusal (§6) is about operational
    # DTGs, not the shelf-date of the map — so it sits with the title
    # furniture, plain and small.
    svg.text(
        proj.cw / 2,
        proj.pad - 4.5,
        "NOVEMBER 1983",
        FS_SCALE,
        anchor="middle",
        tracking=2.0,
        opacity=0.72,
    )
    # N tick, top-left inside
    nx, ny = proj.pad + 12, proj.pad + 20
    svg.line(nx, ny, nx, ny - 12, stroke=INK, width=0.8)
    svg.add(
        f'<path d="M{nx:.1f},{ny - 12:.1f} l-1.7,4 l1.7,-1.6 l1.7,1.6 z" fill="{INK}"/>'
    )
    svg.text(nx, ny + 7, "N", 6.5, anchor="middle")
    # scale bar (bottom corner opposite the legend)
    _scale_bar(svg, proj, cfg)
    # legend (<=5 lines)
    _legend(svg, proj, cfg)


def _scale_bar(svg, proj, cfg):
    km = cfg["scale_km"]
    x, y, length = _scale_pos(proj, cfg)
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
    lx = x0 + 6
    ty = y0 + 10
    for label, kind, w, dash in LEGEND_ROWS:
        sx = lx
        cy = ty - 2
        if kind in ("rail1", "rail2"):
            # single centreline; ticks one side (single) / both (double),
            # matching _draw_rail's convention
            svg.line(sx, cy, sx + 16, cy, stroke=INK, width=W_RAIL)
            for t in (4, 8, 12):
                y_far = cy - RAIL_TICK
                y_near = cy + RAIL_TICK if kind == "rail2" else cy
                svg.line(sx + t, y_far, sx + t, y_near, stroke=INK, width=0.4)
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
