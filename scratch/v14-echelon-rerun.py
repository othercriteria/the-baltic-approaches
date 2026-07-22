"""v14 experiment: the echelon-leverage table, re-run with a real
division grade (demolition timing + obstacle siting added to the
v8-era reserve/CA lag).

The hostile review's caveat on the v8 answer was that the division
layer was too thin for the comparison to count. Now the division
owns: local reserve/CA timing, the demolition trigger and lag, and
obstacle siting. Baseline runs with a middling engineer policy;
each echelon swings sharp<->dull around it.

Run: python3 scratch/v14-echelon-rerun.py
"""

import random
import statistics
import sys
from collections import Counter
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
PERTURBED = [
    "alpha",
    "beta",
    "blue_tolerance",
    "deep_attrition_per_point",
    "deep_delay_per_point",
    "close_support_cv_per_point",
    "sorties_per_aircraft",
    "red_deep_points",
    "red_loc_penalty",
    "red_supply_points",
    "blue_supply_points",
]
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
    div_demo_trigger_km=8.0,
    div_demo_lag_days=1,
    div_obstacle_pos="hold",
    obstacle_ready_day=4,
)
SWINGS = [
    ("theater: advocacy_rate", dict(advocacy_rate=1.0), dict(advocacy_rate=0.1)),
    (
        "corps: reserve recognition",
        dict(corps_recognition_days=0),
        dict(corps_recognition_days=4),
    ),
    (
        "division: CA recognition",
        dict(div_recognition_days=0),
        dict(div_recognition_days=4),
    ),
    (
        "division: engineer quality",
        dict(div_demo_trigger_km=12.0, div_demo_lag_days=0, obstacle_ready_day=3),
        dict(div_demo_trigger_km=4.0, div_demo_lag_days=2, div_obstacle_pos="none"),
    ),
]


def run(factors, seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    for k, f in factors.items():
        if k in p:
            p[k] = p[k] * f
    p.update(BASE)
    p.update(over)
    camp = Campaign(
        axes=axes,
        params=p,
        seed=seed,
        corps_reserve=data["corps_reserve_units"],
        amphib_pool=data["amphib_units"],
        zealand_garrison=data["zealand_garrison_units"],
    )
    state = camp.run(30)
    return sum(ax["blue"].cv for ax in axes.values()), sum(
        st.feba_km for st in state.values()
    )


def cell(factors, base_seed, **over):
    rows = [run(factors, base_seed + s, **over) for s in range(2)]
    return statistics.mean(r[0] for r in rows), statistics.mean(r[1] for r in rows)


# Point table (unperturbed), n=40 seeds
print("# v14 echelon re-run | point (n=40): sharp CV/FEBA vs dull CV/FEBA")
for label, sharp, dull in SWINGS:
    s = [run({}, 20_000 + i, **sharp) for i in range(40)]
    d = [run({}, 20_000 + i, **dull) for i in range(40)]
    scv = statistics.mean(x[0] for x in s)
    dcv = statistics.mean(x[0] for x in d)
    sf = statistics.mean(x[1] for x in s)
    df = statistics.mean(x[1] for x in d)
    print(
        f"  {label:<28} {scv:>6.1f}/{sf:>4.0f}  vs {dcv:>6.1f}/{df:>4.0f}"
        f"  | spread CV {abs(scv - dcv):>5.1f}  km {abs(sf - df):>4.0f}"
    )

# Sweep: winners per world
winners = Counter()
spreads = {label: [] for label, *_ in SWINGS}
for i in range(60):
    prng = random.Random(10_000 + i)
    factors = {k: prng.uniform(0.6, 1.4) for k in PERTURBED}
    seed = 40_000 + 10 * i
    world = {}
    for label, sharp, dull in SWINGS:
        scv, _ = cell(factors, seed, **sharp)
        dcv, _ = cell(factors, seed, **dull)
        world[label] = abs(scv - dcv)
        spreads[label].append(abs(scv - dcv))
    winners[max(world, key=world.get)] += 1
print("# sweep: 60 worlds x 2 seeds — max-leverage echelon counts")
for label, n in winners.most_common():
    print(
        f"  {label:<28} {n}/60   (median spread {statistics.median(spreads[label]):.1f} CV)"
    )
