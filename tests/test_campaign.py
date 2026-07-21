from pathlib import Path

from wargame.campaign import Campaign
from wargame.models import epstein
from wargame.oob import Battalion, load_scenario

SCEN = Path(__file__).parent.parent / "wargame" / "scenarios" / "toy-landjut.toml"


def run(days=18, deep=None, hold=True):
    data, axes, dropped = load_scenario(SCEN)
    if deep is not None:
        data["params"]["deep_fraction"] = deep
    if not hold:
        for ax in axes.values():
            ax["spec"]["hold_km"] = ax["spec"]["length_km"]
    camp = Campaign(axes=axes, params=data["params"])
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


def test_year_parameterization_mechanism():
    data, axes, dropped = load_scenario(SCEN, year=1955)
    assert dropped == []  # toy units carry no in_service dates
    bn = Battalion(name="x", side="red", kind="armor", cv=10, in_service=1985)
    assert bn.in_service > 1955
