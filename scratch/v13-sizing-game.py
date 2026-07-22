"""v13 experiment: sizing the garrison against a moving threat.

Red can expand the airborne pool mid-campaign (2 air-capable
regiments, 16 CV, diverted OFF the mainland march tables —
commensurable). Release is irreversible, so blue must size its
kept core against red's POTENTIAL, not its current pool. The v12
rational core (keep one battalion) is now a bet; sizing against
potential (keep four) is the worst-case answer that looks like
v12's over-insurance. Red's bluff: divert the regiments, never
strike — pure scare, paid in mainland strength.

Run: python3 scratch/v13-sizing-game.py
"""

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from wargame.campaign import Campaign
from wargame.oob import load_scenario

SCEN = (
    Path(__file__).resolve().parent.parent
    / "wargame"
    / "scenarios"
    / "toy-landjut.toml"
)
N = 40
DAYS = 30
BASE = dict(
    apportionment_mode="advocacy",
    theater_deep_fraction=0.2,
    corps_request_deep=1.0,
    advocacy_rate=0.3,
    advocacy_lag_days=1,
    zealand_caution=0.5,
    naval_claim_frac=0.3,
    zealand_battle_claim=0.8,
    zealand_battle_days=4,
    pin_release_c=0.25,
    red_opportunist_lag=2,
)
BLUE = [
    ("hold always (the pin)", dict(zg_release_mode="never")),
    (
        "d18 keep 2 (v12 core)",
        dict(zg_release_mode="day", zg_release_day=18, zg_release_count=4),
    ),
    (
        "d18 keep 4 (vs potential)",
        dict(zg_release_mode="day", zg_release_day=18, zg_release_count=2),
    ),
    ("d18 release all", dict(zg_release_mode="day", zg_release_day=18)),
]
RED = [
    ("threat", dict(red_amphib="threat")),
    ("opportunist", dict(red_amphib="opportunist")),
    ("opp + reinforce d12", dict(red_amphib="opportunist", red_air_reinforce_day=12)),
    ("bluff (reinf, no strike)", dict(red_amphib="threat", red_air_reinforce_day=12)),
]


def run(seed, over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p.update(BASE)
    p.update(over)
    camp = Campaign(
        axes=axes,
        params=p,
        seed=seed,
        amphib_pool=data["amphib_units"],
        zealand_garrison=data["zealand_garrison_units"],
    )
    state = camp.run(DAYS)
    return {
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "red_cv": sum(ax["red"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
        "zlost": 1.0 if camp.zealand_lost else 0.0,
    }


print(f"# v13 sizing game: n={N}, {DAYS} days | cell = blueCV / redCV / Z-lost%")
print("  " + f"{'blue \\\\ red':<28}" + "".join(f"{r[0]:>26}" for r in RED))
matrix = {}
for blabel, bover in BLUE:
    cells = []
    for rlabel, rover in RED:
        rows = [run(20_000 + i, {**bover, **rover}) for i in range(N)]
        m = {k: statistics.mean(r[k] for r in rows) for k in rows[0]}
        matrix[(blabel, rlabel)] = m
        cells.append(f"{m['blue_cv']:>6.1f}/{m['red_cv']:>5.1f}/{m['zlost']:>4.0%}")
    print("  " + f"{blabel:<28}" + "".join(f"{c:>26}" for c in cells))
print()
for blabel, _ in BLUE:
    worst = min(matrix[(blabel, r)]["blue_cv"] for r, _ in RED)
    zmax = max(matrix[(blabel, r)]["zlost"] for r, _ in RED)
    print(f"  {blabel:<28} worst blueCV {worst:>5.1f} | max Z-lost {zmax:>4.0%}")
