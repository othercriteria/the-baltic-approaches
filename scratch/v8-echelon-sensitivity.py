"""v8 experiment: where do the interesting decisions live?

The hostile review's attack 3: the pre-v8 instrument contained only
corps-grade decisions, so 'every lever lives at corps' was true by
construction. Now three grades exist, each with a quality number:

  theater  — advocacy_rate (how fast Karup grants the corps' ask)
  corps    — corps_alloc_lag_days (staleness of the air-allocation
             map) and corps_recognition_days (reserve dispatch)
  division — div_recognition_days (local reserve/CA)

One echelon at a time swings from sharp to dull around a common
baseline; the outcome spread is that echelon's leverage. n seeds x
30 days, toy scenario — shapes only, no canon.

Run: python3 scratch/v8-echelon-sensitivity.py
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
    corps_air_alloc="threat",
    corps_alloc_lag_days=1,
    corps_dispatch_cv=10.0,
    corps_recognition_days=1,
    corps_reserve_move_days=2,
    div_recognition_days=1,
)

SWINGS = [
    ("theater: advocacy_rate", "advocacy_rate", 1.0, 0.1),
    ("corps: air-map staleness", "corps_alloc_lag_days", 0, 4),
    ("corps: reserve recognition", "corps_recognition_days", 0, 4),
    ("division: CA recognition", "div_recognition_days", 0, 4),
]


def run(seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p.update(BASE)
    p.update(over)
    camp = Campaign(
        axes=axes,
        params=p,
        seed=seed,
        corps_reserve=data["corps_reserve_units"],
    )
    state = camp.run(DAYS)
    return {
        "held": sum(1 for st in state.values() if not st.fallen),
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
    }


def cell(**over):
    rows = [run(20_000 + i, **over) for i in range(N)]
    return {k: statistics.mean(r[k] for r in rows) for k in rows[0]}


base = cell()
print(f"# v8 echelon sensitivity: n={N}, {DAYS} days")
print(
    f"  {'baseline':<34} | held {base['held']:.2f}  "
    f"CV {base['blue_cv']:.1f}  FEBA {base['feba']:.0f}"
)
print(
    f"  {'echelon knob':<34} | {'sharp: CV/FEBA':>16} | {'dull: CV/FEBA':>16} | spread(CV)"
)
for label, key, sharp, dull in SWINGS:
    s = cell(**{key: sharp})
    d = cell(**{key: dull})
    print(
        f"  {label:<34} | {s['blue_cv']:>7.1f}/{s['feba']:>5.0f}   "
        f"| {d['blue_cv']:>7.1f}/{d['feba']:>5.0f}   "
        f"| {abs(s['blue_cv'] - d['blue_cv']):>5.1f}"
    )
