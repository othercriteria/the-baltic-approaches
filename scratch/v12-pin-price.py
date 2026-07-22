"""v12 experiment: the pin's rational core.

The threat is decomposed: sealift closes with the sea, the
airborne component does not. The v11 safe date is gone — an
emptied island can be taken by the airborne echelon in any
weather. Blue's ladder of policies runs from the historical pin
(hold everything, forever) through partial releases (keep k
battalions as residual insurance) to v11's now-suspect full
release. Against the opportunist, how much garrison must stay —
and what does every battalion of over-insurance cost on the
mainland?

Run: python3 scratch/v12-pin-price.py
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
    ("d18 keep 3", dict(zg_release_mode="day", zg_release_day=18, zg_release_count=3)),
    ("d18 keep 2", dict(zg_release_mode="day", zg_release_day=18, zg_release_count=4)),
    (
        "d18 keep arty only",
        dict(zg_release_mode="day", zg_release_day=18, zg_release_count=5),
    ),
    ("d18 release all (v11)", dict(zg_release_mode="day", zg_release_day=18)),
    ("d8 keep 2", dict(zg_release_mode="day", zg_release_day=8, zg_release_count=4)),
]
RED = [
    ("threat", dict(red_amphib="threat")),
    ("opportunist", dict(red_amphib="opportunist")),
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
        "feba": sum(st.feba_km for st in state.values()),
        "zlost": 1.0 if camp.zealand_lost else 0.0,
    }


print(f"# v12 pin price: n={N}, {DAYS} days | cell = blueCV / FEBA / Z-lost%")
print("  " + f"{'blue policy':<24}" + "".join(f"{r[0]:>22}" for r in RED))
matrix = {}
for blabel, bover in BLUE:
    cells = []
    for rlabel, rover in RED:
        rows = [run(20_000 + i, {**bover, **rover}) for i in range(N)]
        m = {k: statistics.mean(r[k] for r in rows) for k in rows[0]}
        matrix[(blabel, rlabel)] = m
        cells.append(f"{m['blue_cv']:>6.1f}/{m['feba']:>4.0f}/{m['zlost']:>4.0%}")
    print("  " + f"{blabel:<24}" + "".join(f"{c:>22}" for c in cells))
print()
for blabel, _ in BLUE:
    worst = min(matrix[(blabel, r)]["blue_cv"] for r, _ in RED)
    zmax = max(matrix[(blabel, r)]["zlost"] for r, _ in RED)
    print(f"  {blabel:<24} worst blueCV {worst:>5.1f} | max Z-lost {zmax:>4.0%}")
