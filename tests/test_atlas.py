"""Atlas tests. The absence tests are the permanent guard against
the specimen's bridge-invention class of error (critique-profile
2.6): geography claims fail loudly here, not silently in prose."""

import pytest

from atlas import Atlas


@pytest.fixture(scope="module")
def atlas():
    return Atlas.load()


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


def test_zealand_exits_are_all_ferries(atlas):
    """Every tonne leaving Zealand westward crosses water by ferry
    (Great Belt) or by the island chain ending in the Rødby ferry.
    The min cut must therefore be pure ferry edges."""
    flow, cut = atlas.max_flow(["koebenhavn"], ["rendsburg"])
    assert flow > 0
    assert cut, "expected a nonempty min cut"
    assert all(e.mode == "ferry" for e in cut), (
        f"non-ferry edge in Zealand exit cut: "
        f"{[e.id for e in cut if e.mode != 'ferry']}"
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
    assert len(igb) >= 3
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
