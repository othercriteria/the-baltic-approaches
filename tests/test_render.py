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

import pytest

from atlas import Atlas
from atlas.render import PLATES, render_plate

PLATE_NAMES = list(PLATES)


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
        "1983",
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
            "SCHLESWIG-HOLSTEIN",
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
