from pathlib import Path

from wargame.campaign import Campaign
from wargame.models import epstein
from wargame.oob import Battalion, load_scenario

SCEN = Path(__file__).parent.parent / "wargame" / "scenarios" / "toy-landjut.toml"


def run(days=18, deep=None, hold=True, seed=1986, wx=False, ca=False, red_air=None):
    data, axes, dropped = load_scenario(SCEN)
    if deep is not None:
        data["params"]["deep_fraction"] = deep
    if not hold:
        for ax in axes.values():
            ax["spec"]["hold_km"] = ax["spec"]["length_km"]
    if not wx:
        data["params"]["wx_standdown_prob"] = 0.0
        data["params"]["wx_min"] = 1.0
        data["params"]["wx_max"] = 1.0
    if red_air is not None:
        data["params"]["red_deep_points"] = red_air
    data["params"]["ca_enabled"] = ca
    camp = Campaign(axes=axes, params=data["params"], seed=seed)
    state = camp.run(days)
    return camp, state, axes


def test_scenario_loads_and_runs_deterministically():
    camp1, _, _ = run()
    camp2, _, _ = run()
    assert [vars(e) for e in camp1.logs] == [vars(e) for e in camp2.logs]
    assert len(camp1.logs) > 0


def test_defender_trades_space_under_pressure():
    camp, state, _ = run(hold=False)
    withdrawals = [e.withdrawal_km for e in camp.logs]
    assert any(w > 0 for w in withdrawals), "blue never withdrew: tune scenario"
    for st in state.values():
        assert st.feba_km > 0, "red never advanced at all"


def test_losses_nonnegative_and_strengths_bounded():
    camp, _, axes = run()
    for log in camp.logs:
        assert log.red_loss_frac >= 0
        assert log.blue_loss_frac >= 0
    for ax in axes.values():
        for force in (ax["blue"], ax["red"]):
            for u in force.units + force.reserve:
                assert 0.0 <= u.strength <= 1.0


def test_second_echelon_arrives_and_ratio_jumps():
    camp, _, _ = run(deep=0.0)
    arrival_days = [e.day for e in camp.logs if e.arrivals > 0]
    assert arrival_days, "no follow-on echelon ever arrived"
    assert min(arrival_days) >= 5  # scenario schedules echelon 2 at day 5+


def test_interdiction_delays_and_attrits_echelon():
    camp_close, _, axes_close = run(deep=0.0)
    camp_deep, _, axes_deep = run(deep=1.0)
    first_close = min(e.day for e in camp_close.logs if e.arrivals > 0)
    deep_arrivals = [e.day for e in camp_deep.logs if e.arrivals > 0]
    if deep_arrivals:  # interdiction may hold them out entirely in-window
        assert min(deep_arrivals) > first_close

    # march-column attrition: total red CV (contact+reserve) lower under deep
    def red_total(axes):
        return sum(ax["red"].cv + ax["red"].reserve_cv for ax in axes.values())

    assert red_total(axes_deep) < red_total(axes_close)


def test_hold_line_pins_defender_earlier():
    """Political hold lines pin the defender; without them the only
    'hold line' is the theater's rear edge (the sea), so standing
    still happens — but later."""
    camp_hold, _, _ = run(deep=0.0, hold=True)
    camp_free, _, _ = run(deep=0.0, hold=False)
    first_hold = min(e.day for e in camp_hold.logs if e.standing)
    free_standing = [e.day for e in camp_free.logs if e.standing]
    assert not free_standing or min(free_standing) > first_hold


def test_decision_input_logged_separately_from_outcome():
    camp, _, _ = run()
    diverging = [
        e
        for e in camp.logs
        if e.withdrawal_km > 0 and e.proj_blue_frac > e.blue_loss_frac
    ]
    assert diverging, "delaying action should realize less than projection"


def test_withdrawal_rate_shape():
    assert epstein.withdrawal_rate_kmd(0.02, 0.05, 12) == 0.0
    assert epstein.withdrawal_rate_kmd(0.05, 0.05, 12) == 0.0
    assert 0 < epstein.withdrawal_rate_kmd(0.07, 0.05, 12) < 12
    assert epstein.withdrawal_rate_kmd(0.30, 0.05, 12) == 12


def test_weather_seeded_and_reproducible():
    a, _, _ = run(wx=True, seed=7)
    b, _, _ = run(wx=True, seed=7)
    c, _, _ = run(wx=True, seed=8)
    assert [e.wx for e in a.logs] == [e.wx for e in b.logs]
    assert [e.wx for e in a.logs] != [e.wx for e in c.logs]
    assert all(0.0 < e.wx <= 1.0 for e in a.logs)


def test_close_support_saturates():
    """Effective close-support CV must stay below the saturation
    ceiling regardless of points thrown at it."""
    import math

    sat, per_point = 9.0, 1.2
    added = [
        sat * (1.0 - math.exp(-(pts * per_point) / sat)) for pts in (1, 6, 60, 600)
    ]
    assert added == sorted(added)  # monotone
    assert added[-1] <= sat  # never exceeds ceiling (== at float limit)
    assert added[1] < 6 * added[0]  # sublinear already at 6 points


def test_counterattack_fires_in_the_window():
    """Mechanism test: with blue interdiction stretching the echelon
    gap and NO red counter-interdiction, blue counterattacks and CA
    days move the FEBA backward. (With red interdiction on, the
    window can legitimately close — that is a scenario finding, not
    a mechanism defect; see notes/wargaming-findings.md v3.)"""
    camp, _, _ = run(deep=1.0, ca=True, red_air=0.0, days=24)
    ca_days = [e for e in camp.logs if e.ca]
    assert ca_days, "no counterattack ever fired"
    assert all(e.advance_km < 0 for e in ca_days)


def test_counterattack_never_fires_when_disabled():
    camp, _, _ = run(deep=1.0, ca=False)
    assert not any(e.ca for e in camp.logs)


def test_hold_release_frees_withdrawal():
    data, axes, dropped = load_scenario(SCEN)
    data["params"]["wx_standdown_prob"] = 0.0
    data["params"]["wx_min"] = 1.0
    data["params"]["wx_max"] = 1.0
    data["params"]["ca_enabled"] = False
    for ax in axes.values():
        ax["spec"]["hold_release_day"] = 8
    camp = Campaign(axes=axes, params=data["params"], seed=1)
    camp.run(18)
    standing_days = [e.day for e in camp.logs if e.standing]
    resumed = [e for e in camp.logs if e.day > 8 and e.withdrawal_km > 0]
    assert standing_days and min(standing_days) < 8, "hold line never bound"
    assert resumed, "withdrawal never resumed after hold release"


def test_airframe_stock_depletes_and_floors_at_zero():
    camp, _, _ = run(deep=1.0, days=21)
    assert camp.aircraft >= 0.0
    data, _, _ = load_scenario(SCEN)
    assert camp.aircraft < data["params"]["blue_aircraft"]


def test_deep_costs_more_airframes_than_close():
    camp_deep, _, _ = run(deep=1.0, days=10)
    camp_close, _, _ = run(deep=0.0, days=10)
    assert camp_deep.aircraft < camp_close.aircraft


def test_red_interdiction_delays_blue_mobilization():
    data, axes, _ = load_scenario(SCEN)
    data["params"]["wx_standdown_prob"] = 0.0
    data["params"]["wx_min"] = 1.0
    data["params"]["wx_max"] = 1.0
    data["params"]["ca_enabled"] = False
    camp = Campaign(axes=axes, params=data["params"], seed=1)
    camp.run(18)
    with_red = min(e.day for e in camp.logs if e.blue_arrivals > 0)

    data2, axes2, _ = load_scenario(SCEN)
    data2["params"]["wx_standdown_prob"] = 0.0
    data2["params"]["wx_min"] = 1.0
    data2["params"]["wx_max"] = 1.0
    data2["params"]["ca_enabled"] = False
    data2["params"]["red_deep_points"] = 0.0
    camp2 = Campaign(axes=axes2, params=data2["params"], seed=1)
    camp2.run(18)
    without_red = min(e.day for e in camp2.logs if e.blue_arrivals > 0)
    assert with_red > without_red


def test_sweep_smoke():
    from wargame.sweep import run_sample

    outcomes = run_sample(SCEN, 0, days=8, lo=0.8, hi=1.2)
    assert set(outcomes) == {0.0, 0.5, 1.0}
    for o in outcomes.values():
        assert 0 <= o["held"] <= 2
        assert o["blue_cv"] >= 0


def test_artillery_cannot_hold_or_take_ground():
    """Guns alone neither hold nor advance (the v3 artillery
    closure's one code guard)."""
    from wargame.oob import Force

    data, _, _ = load_scenario(SCEN)
    p = dict(data["params"])
    p.update(
        wx_standdown_prob=0.0,
        wx_min=1.0,
        wx_max=1.0,
        ca_enabled=False,
        red_deep_points=0.0,
    )

    def mini(blue_units, red_units):
        axes = {
            "x": {
                "spec": {"name": "x", "length_km": 50, "hold_km": 50},
                "blue": Force("blue", units=blue_units),
                "red": Force("red", units=red_units),
            }
        }
        camp = Campaign(axes=axes, params=p, seed=1)
        state = camp.run(3)
        return camp, state["x"]

    def arty(side, n):
        return [
            Battalion(name=f"{side}-a{i}", side=side, kind="arty", cv=6)
            for i in range(n)
        ]

    def mech(side, n):
        return [
            Battalion(name=f"{side}-m{i}", side=side, kind="mech", cv=8)
            for i in range(n)
        ]

    # Blue holds only artillery: treated as collapsed, red road-marches.
    _, st = mini(arty("b", 3), mech("r", 3))
    assert st.feba_km == 3 * p["march_kmd"] or st.fallen

    # Red holds only artillery: no engagement, no advance.
    _, st = mini(mech("b", 3), arty("r", 3))
    assert st.feba_km == 0.0


def _mini_params(base):
    p = dict(base)
    p.update(
        wx_standdown_prob=0.0,
        wx_min=1.0,
        wx_max=1.0,
        red_deep_points=0.0,
        red_reinforces_success=False,
    )
    return p


def test_withheld_reserve_takes_no_losses_until_committed():
    from wargame.oob import Force

    data, _, _ = load_scenario(SCEN)
    p = _mini_params(data["params"])
    p["ca_enabled"] = False
    p["emergency_commit_cv"] = 0.0  # never emergency-commit in this test
    line = [Battalion(name=f"b-m{i}", side="blue", kind="mech", cv=8) for i in range(4)]
    res = Battalion(name="b-res", side="blue", kind="armor", cv=10, role="reserve")
    red = [Battalion(name=f"r-m{i}", side="red", kind="mech", cv=8) for i in range(5)]
    axes = {
        "x": {
            "spec": {"name": "x", "length_km": 200, "hold_km": 200},
            "blue": Force("blue", units=line, withheld=[res]),
            "red": Force("red", units=red),
        }
    }
    camp = Campaign(axes=axes, params=p, seed=1)
    camp.run(6)
    assert res.strength == 1.0, "withheld reserve took losses"
    assert any(u.strength < 1.0 for u in line), "line never attrited"


def test_recognition_lag_delays_or_forfeits_counterattack():
    def first_ca(lag):
        data, axes, _ = load_scenario(SCEN)
        p = _mini_params(data["params"])
        p["ca_enabled"] = True
        p["deep_fraction"] = 1.0
        p["ca_recognition_days"] = lag
        camp = Campaign(axes=axes, params=p, seed=1986)
        camp.run(24)
        days = [e.day for e in camp.logs if e.ca]
        return min(days) if days else None

    fast, slow = first_ca(0), first_ca(4)
    assert fast is not None, "sharp G-3 never counterattacked"
    assert slow is None or slow > fast


def test_red_reinforces_success_diverts_arrivals():
    from wargame.oob import Force

    data, _, _ = load_scenario(SCEN)
    p = _mini_params(data["params"])
    p.update(ca_enabled=False, red_reinforces_success=True, deep_fraction=0.0)
    # Axis "a": no blue at all -> red races ahead. Axis "b": solid
    # blue defense. The echelon scripted for "b" should divert to "a".
    red_a = [Battalion(name="ra", side="red", kind="mech", cv=8)]
    red_b = [Battalion(name="rb", side="red", kind="mech", cv=8)]
    follow_b = Battalion(
        name="rb-follow", side="red", kind="armor", cv=10, arrival_day=3
    )
    blue_b = [
        Battalion(name=f"bb{i}", side="blue", kind="mech", cv=8) for i in range(6)
    ]
    axes = {
        "a": {
            "spec": {"name": "a", "length_km": 300, "hold_km": 300},
            "blue": Force("blue"),
            "red": Force("red", units=red_a),
        },
        "b": {
            "spec": {"name": "b", "length_km": 300, "hold_km": 300},
            "blue": Force("blue", units=blue_b),
            "red": Force("red", units=red_b, reserve=[follow_b]),
        },
    }
    camp = Campaign(axes=axes, params=p, seed=1)
    camp.run(6)
    assert follow_b in axes["a"]["red"].units, "echelon did not reinforce success"


def test_commit_logged_on_counterattack_day():
    data, axes, _ = load_scenario(SCEN)
    p = _mini_params(data["params"])
    p.update(ca_enabled=True, deep_fraction=1.0, ca_recognition_days=0)
    camp = Campaign(axes=axes, params=p, seed=1986)
    camp.run(24)
    ca_days = [e for e in camp.logs if e.ca]
    assert ca_days
    axis_first_ca = {}
    for e in camp.logs:
        if e.ca and e.axis not in axis_first_ca:
            axis_first_ca[e.axis] = e
    assert any(e.commit > 0 for e in axis_first_ca.values()), (
        "first counterattack day never committed the reserve"
    )


def test_red_fill_declines_as_loc_stretches():
    """Culmination as supply: red fulfillment must fall as the FEBA
    advances into the theater."""
    camp, _, _ = run(deep=0.0, days=14)
    by_axis = {}
    for e in camp.logs:
        if e.rfill > 0 and e.ratio > 0:
            by_axis.setdefault(e.axis, []).append((e.feba_km, e.rfill))
    assert by_axis
    strictly_declined = 0
    for pts in by_axis.values():
        deep_pts = [f for km, f in pts if km > 50]
        shallow_pts = [f for km, f in pts if km < 20]
        if deep_pts and shallow_pts:
            # Never higher when stretched; an unconstrained axis may
            # sit at 1.0 throughout.
            assert max(deep_pts) <= max(shallow_pts)
            if max(deep_pts) < max(shallow_pts):
                strictly_declined += 1
    assert strictly_declined >= 1, "no axis ever felt the LOC stretch"


def test_red_commits_echelons_in_mass():
    """Whole-echelon discipline: red arrivals appear in committed
    masses (>= red_commit_min_cv worth, or the timeout batch), not
    single battalions every day."""
    camp, _, _ = run(deep=0.0, days=14)
    bursts = [e.arrivals for e in camp.logs if e.arrivals > 0]
    assert bursts, "no red commitment ever happened"
    assert max(bursts) >= 3, "echelons never committed as a mass"


def test_ca_culminates():
    """A counterattack run cannot exceed ca_culminate_days without
    the window closing in between."""
    data, axes, _ = load_scenario(SCEN)
    p = _mini_params(data["params"])
    p.update(ca_enabled=True, deep_fraction=1.0, ca_recognition_days=0)
    limit = p["ca_culminate_days"]
    camp = Campaign(axes=axes, params=p, seed=1986)
    camp.run(24)
    runs = {}
    best = 0
    prev = {}
    for e in camp.logs:
        if e.ca:
            runs[e.axis] = runs.get(e.axis, 0) + 1 if prev.get(e.axis) else 1
            best = max(best, runs[e.axis])
        else:
            runs[e.axis] = 0
        prev[e.axis] = e.ca
    assert best <= limit


def test_sea_state_release_is_seeded_and_in_range():
    data, axes, _ = load_scenario(SCEN)
    lo = data["params"]["amphib_close_min"]
    hi = data["params"]["amphib_close_max"]
    days_by_seed = {}
    for seed in (1, 2, 3):
        data_i, axes_i, _ = load_scenario(SCEN)
        camp = Campaign(axes=axes_i, params=data_i["params"], seed=seed)
        camp.run(2)
        days_by_seed[seed] = camp.amphib_release_day
        assert lo <= camp.amphib_release_day <= hi
    camp2 = Campaign(*[], **{"axes": axes, "params": data["params"], "seed": 1})
    camp2.run(2)
    assert camp2.amphib_release_day == days_by_seed[1]


def test_year_parameterization_mechanism():
    data, axes, dropped = load_scenario(SCEN, year=1955)
    assert dropped == []  # toy units carry no in_service dates
    bn = Battalion(name="x", side="red", kind="armor", cv=10, in_service=1985)
    assert bn.in_service > 1955
