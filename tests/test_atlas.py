"""Atlas tests. The absence tests are the permanent guard against
the specimen's bridge-invention class of error (critique-profile
2.6): geography claims fail loudly here, not silently in prose."""

from pathlib import Path

import pytest
import tomllib

from atlas import Atlas

_RAW = tomllib.loads(
    (
        Path(__file__).resolve().parent.parent / "atlas" / "data" / "theater-1983.toml"
    ).read_text()
)


@pytest.fixture(scope="module")
def atlas():
    return Atlas.load()


def test_every_rail_edge_asserts_a_track_count():
    """Build 2 fix 4: no drawn rail line without a track assertion. Every
    mode=rail edge must declare `tracks` (single|double) and carry a
    graded `tracks_src` (SOURCED:... | GUESS:...), so the plate can never
    render an un-asserted third rail class."""
    for e in _RAW["edge"]:
        if e["class"] != "rail":
            continue
        assert e.get("tracks") in ("single", "double"), (
            f"{e['id']}: missing/invalid tracks"
        )
        src = e.get("tracks_src", "")
        assert src.startswith("SOURCED") or src.startswith("GUESS"), (
            f"{e['id']}: tracks_src not graded ({src!r})"
        )


def test_loads_clean(atlas):
    issues, stats = atlas.check()
    assert issues == []
    assert stats["nodes"] > 30
    assert stats["edges"] > 50


def test_no_great_belt_fixed_link(atlas):
    """In Nov 1983 nothing but ferries crosses the Great Belt."""
    for e in atlas.edges:
        if {e.a, e.b} == {"nyborg", "korsor"}:
            assert e.mode == "ferry", f"{e.id} fixed-links the Great Belt"


def test_no_fehmarn_belt_fixed_link(atlas):
    for e in atlas.edges:
        if {e.a, e.b} == {"rodby", "puttgarden"}:
            assert e.mode == "ferry"


def test_jutland_division_route_is_overland(atlas):
    """The Jyske Division's march to Schleswig needs no water
    crossing at all — the specimen's Little-Belt-chokepoint
    framing was wrong (critique-profile 2.7)."""
    cost, path = atlas.shortest_path("fredericia", "schleswig")
    modes = {e.mode for e in path}
    assert "ferry" not in modes
    crossings = {e.crossing for e in path if e.crossing}
    assert "little_belt" not in crossings
    assert "great_belt" not in crossings


def test_zealand_exits_cut_at_water(atlas):
    """Every tonne leaving Zealand westward crosses water: by ferry
    (Great Belt, Rødby) or over the narrow Storstrøm bridge. The
    min cut must consist only of water crossings — never an inland
    road or rail edge."""
    flow, cut = atlas.max_flow(["koebenhavn"], ["rendsburg"])
    assert flow > 0
    assert cut, "expected a nonempty min cut"
    for e in cut:
        assert e.mode == "ferry" or e.crossing == "storstrom", (
            f"inland edge in Zealand exit cut: {e.id}"
        )


def test_zealand_isolated_without_ferries(atlas):
    ferries = {e.id for e in atlas.edges if e.mode == "ferry"}
    flow, _ = atlas.max_flow(["koebenhavn"], ["rendsburg"], without=ferries)
    assert flow == 0


def test_kiel_canal_crossings_present(atlas):
    ids = {e.id for e in atlas.edges if e.crossing == "kiel_canal"}
    # A7 at Rader, B76 at Holtenau, the Rendsburg rail high bridge
    assert len(ids) >= 3


def test_igb_crossings_connect_red_to_sh(atlas):
    """The war comes from the southeast: every IGB edge joins
    Mecklenburg to Schleswig-Holstein. Encodes the corrected
    threat geometry (critique-profile 2.7)."""
    igb = [e for e in atlas.edges if e.crossing == "igb"]
    # exactly two legal crossings in the Lübeck sector in 1983:
    # Schlutup/Selmsdorf road + Herrnburg rail (transport-1983 §5)
    assert len(igb) == 2
    assert {e.mode for e in igb} == {"road", "rail"}
    for e in igb:
        regions = {atlas.nodes[e.a].region, atlas.nodes[e.b].region}
        assert regions == {"ME", "SH"}, f"{e.id} joins {regions}"


def test_dk_border_is_not_the_igb(atlas):
    """No edge at the Danish border carries the igb tag — the
    specimen's wrong-border opening becomes untypable here."""
    for e in atlas.edges:
        if e.crossing == "dk_de_border":
            regions = {atlas.nodes[e.a].region, atlas.nodes[e.b].region}
            assert regions == {"JY", "SH"}


def test_bridge_drop_what_if(atlas):
    """Dropping the Rader Hochbrücke still leaves a canal crossing
    (the B76/Holtenau and the rail bridge), so Schleswig-Rendsburg
    reroutes rather than disconnects."""
    res = atlas.shortest_path(
        "schleswig", "rendsburg", without={"a7-schleswig-rendsburg"}
    )
    assert res is not None
    cost, path = res
    assert cost > 0


def test_region_flow_resolution(atlas):
    flow, cut = atlas.max_flow(atlas.resolve("region:SJ"), atlas.resolve("region:JY"))
    assert flow > 0


def test_critical_ranking(atlas):
    """The named story flows load and produce a nonempty knockout
    ranking whose top tier includes at least one water crossing.
    (The exact order legitimately shifts as capacities graduate —
    do not pin it.)"""
    assert len(atlas.flows) >= 5
    ranked, base = atlas.critical()
    assert all(b > 0 for b in base.values())
    assert ranked
    top5 = [e for _, e in ranked[:5]]
    assert any(e.mode == "ferry" or e.crossing for e in top5)
