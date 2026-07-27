"""Map-plate render tests (planning/map-spec.md §7).

Two guards, both "by construction":

  * the absences guard — the cartography can only draw edges that
    exist in the atlas, so the specimen's bridge-invention error class
    (a Great Belt fixed link, etc.) is untypable on the plate exactly
    as it is in the network data; and the renderer has no vocabulary
    for the §6 refusals (front lines, arrows, unit symbols, dates,
    capacities, red/blue);
  * the feature snapshot — every label §3 requires is present in the
    emitted SVG, so a dropped town fails loudly here.
"""

import re
from pathlib import Path

import pytest
import tomllib

from atlas import Atlas
from atlas.render import LABEL_AUDIT, LABEL_WHITELIST, PLATES, render_plate

PLATE_NAMES = list(PLATES)

_RAW = tomllib.loads(
    (
        Path(__file__).resolve().parent.parent / "atlas" / "data" / "theater-1983.toml"
    ).read_text()
)
SHAPE_NAMES = [n["name"] for n in _RAW["node"] if n.get("kind") == "shape"]


@pytest.fixture(scope="module")
def atlas():
    return Atlas.load()


@pytest.fixture(scope="module")
def rendered():
    return {name: render_plate(name) for name in PLATE_NAMES}


def _texts(svg):
    return "\n".join(re.findall(r"<text[^>]*>(.*?)</text>", svg))


# ---------------------------------------------------------------- absences


def test_renderer_draws_only_atlas_edges(atlas, rendered):
    ids = {e.id for e in atlas.edges}
    for name in PLATE_NAMES:
        _, drawn = rendered[name]
        assert set(drawn) <= ids, f"{name}: drew non-atlas edges"


def test_absence_links_are_untypable(atlas, rendered):
    """No plate may draw a fixed link across a forbidden pair. This
    holds because the plate draws only atlas edges and the atlas
    enforces the absence table — but assert it on the CARTOGRAPHY too."""
    by_id = {e.id: e for e in atlas.edges}
    for a in atlas.absences:
        x, y = a["would_connect"]
        allowed = set(a.get("allowed", []))
        for name in PLATE_NAMES:
            _, drawn = rendered[name]
            for eid in drawn:
                e = by_id[eid]
                if {e.a, e.b} == {x, y} and e.mode != "ferry" and eid not in allowed:
                    pytest.fail(f"{name}: {eid} draws forbidden link {x}-{y}")


def test_great_belt_only_ferry_on_plate(atlas, rendered):
    by_id = {e.id: e for e in atlas.edges}
    for name in PLATE_NAMES:
        _, drawn = rendered[name]
        for eid in drawn:
            e = by_id[eid]
            if {e.a, e.b} == {"nyborg", "korsor"}:
                assert e.mode == "ferry", f"{name}: {eid} bridges the Great Belt"


def test_no_war_marks_vocabulary(rendered):
    """The §6 refusals must not appear as text anywhere on either
    plate: front lines, arrows, unit symbols, dates, DTGs, phase
    lines, capacities/tonnages, the fictional operational trace."""
    forbidden = [
        "FEBA",
        "FLOT",
        "FLET",
        "phase line",
        "phaseline",
        "PL ",
        "SPERBER",
        "arrow",
        "axis of",
        "boundary",
        "tonnes",
        "t/d",
        # NB: the bare year "1983" is deliberately NOT forbidden — build 3
        # item 8 adds a restrained "NOVEMBER 1983" subtitle that dates the
        # geography. The no-time refusal (§6) is about operational time
        # (DTGs, H-hour, phase lines), which the tokens below still guard.
        "DTG",
        "H-hour",
        "H+",
        "corps",
        "brigade",
        "division",
        "regiment",
        "objective",
        "obj ",
    ]
    for name in PLATE_NAMES:
        svg, _ = rendered[name]
        low = svg.lower()
        for tok in forbidden:
            assert tok.lower() not in low, f"{name}: forbidden token {tok!r} present"


def test_one_ink_no_red_blue(rendered):
    """One ink only. No color-coded sides — the refusal that a plate
    must not do the chinagraph's job."""
    allowed = {"#111111", "#ffffff", "#e9edf0", "none"}
    for name in PLATE_NAMES:
        svg, _ = rendered[name]
        used = set(re.findall(r'(?:fill|stroke)="([^"]*)"', svg))
        stray = {c for c in used if c.lower() not in allowed}
        assert not stray, f"{name}: non-ink colours present: {stray}"


# ---------------------------------------------------------------- features

REQUIRED = {
    "approaches": {
        "waters": [
            "NORTH SEA",
            "BALTIC",
            "LITTLE BELT",
            "GREAT BELT",
            "FEHMARN BELT",
            "KIEL CANAL",
            "SCHLEI",
            "EIDER",
            "TRAVE",
        ],
        "regions": [
            "JUTLAND",
            "FUNEN",
            "ZEALAND",
            "LOLLAND-FALSTER",
            # Hand-pass 2026-07-27: the composite name is set as the two
            # duchies — no placement of the ~2°-wide tracked single line
            # cleared the road net (map-spec.md hand-pass entry, item 5).
            "SCHLESWIG",
            "HOLSTEIN",
            "MECKLENBURG",
        ],
        "towns": [
            "Aalborg",
            "Aarhus",
            "Vejle",
            "Fredericia",
            "Kolding",
            "Vamdrup",
            "Haderslev",
            "Aabenraa",
            "Padborg",
            "Esbjerg",
            "Flensburg",
            "Schleswig",
            "Rendsburg",
            "Neumünster",
            "Kiel",
            "Eckernförde",
            "Husum",
            "Friedrichstadt",
            "Heide",
            "Itzehoe",
            "Hamburg",
            "Lübeck",
            "Oldenburg",
            "Puttgarden",
            "Middelfart",
            "Odense",
            "Nyborg",
            "Korsør",
            "Slagelse",
            "København",
            "Vordingborg",
            "Nykøbing",
            "Rødby",
            "Ratzeburg",
            "Schwerin",
            "Wismar",
            "Rostock",
        ],
    },
    "neck": {
        "waters": ["KIEL CANAL", "SCHLEI", "EIDER", "TREENE", "DANEVIRKE"],
        "regions": [],
        "towns": [
            "Rendsburg",
            "Sehestedt",
            "Schleswig",
            "Missunde",
            "Eckernförde",
            "Husum",
            "Friedrichstadt",
            "Nordfeld",
            "Sorgbrück",
            "Hohn",
            "Neumünster",
        ],
    },
}


@pytest.mark.parametrize("name", PLATE_NAMES)
def test_required_labels_present(rendered, name):
    text = _texts(rendered[name][0])
    up = text.upper()
    missing = []
    for w in REQUIRED[name]["waters"] + REQUIRED[name]["regions"]:
        if w.upper() not in up:
            missing.append(w)
    for t in REQUIRED[name]["towns"]:
        if t not in text:
            missing.append(t)
    assert not missing, f"{name}: missing required labels {missing}"


def test_rendsburg_has_the_only_hq_mark(rendered):
    """Rendsburg carries the plate's one distinguishing mark (F7); no
    other node is singled out. The HQ mark is the small square."""
    for name in PLATE_NAMES:
        svg, _ = rendered[name]
        # exactly one small filled-white square of side HQ_SQUARE-ish in
        # the map body (the legend swatch lives after </g>, i.e. the
        # clip group holds exactly one).
        body = svg.split("</g>")[0]
        squares = re.findall(r'<rect[^>]*width="3.20"[^>]*height="3.20"', body)
        assert len(squares) == 1, f"{name}: expected 1 HQ square, got {len(squares)}"


# ---------------------------------------------------------------- typography


def test_label_face_is_a_parameter():
    svg, _ = render_plate("neck", face="Sentinel Test Face")
    assert "Sentinel Test Face" in svg


# ---------------------------------------------------------------- build 2 invariants


def test_shape_nodes_are_never_labelled(rendered):
    """A `kind="shape"` node renders as an unlabelled path vertex (spec
    build-2 work order). Its name must appear nowhere in either plate's
    text."""
    assert SHAPE_NAMES, "expected shape nodes in the atlas"
    for name in PLATE_NAMES:
        text = _texts(rendered[name][0])
        for sn in SHAPE_NAMES:
            assert sn not in text, f"{name}: shape node {sn!r} was labelled"


def test_plate1_excludes_plate2_only_towns(rendered):
    """The Plate II-only neck features must not letter on Plate I (build
    2 fix 2 / the theater pile-up). Names that are in the neck whitelist
    but NOT the approaches whitelist must be absent from Plate I text."""
    atlas = Atlas.load()
    plate2_only = LABEL_WHITELIST["neck"] - LABEL_WHITELIST["approaches"]
    text = _texts(rendered["approaches"][0])
    for nid in plate2_only:
        disp = atlas.nodes[nid].name.split(" (")[0]
        assert disp not in text, (
            f"approaches: {disp!r} (Plate II-only) leaked onto Plate I"
        )


def test_labels_stay_inside_the_neatline(rendered):
    """No town/water/region/country label escapes the neat-line (build 2
    fix 6). Checked against the render's own placement audit."""
    for name in PLATE_NAMES:
        rendered[name]  # ensure rendered + audit populated
        audit = LABEL_AUDIT[name]
        fx0, fy0, fx1, fy1 = audit["frame"]
        tol = 1.0
        for bx0, by0, bx1, by1 in audit["boxes"]:
            assert (
                bx0 >= fx0 - tol
                and bx1 <= fx1 + tol
                and by0 >= fy0 - tol
                and by1 <= fy1 + tol
            ), (
                f"{name}: label box {(bx0, by0, bx1, by1)} escapes frame {audit['frame']}"
            )
