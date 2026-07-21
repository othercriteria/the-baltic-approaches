"""v8 robustness: which echelon's quality knob has max leverage,
world by world? Same perturbation discipline as wargame/sweep.py
(U(0.6,1.4) on 11 params), 60 worlds x 4 swings x 2 poles, 30 days,
3 seeds per cell averaged.

Run: python3 scratch/v8-echelon-sweep.py
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
)
SWINGS = [
    ("theater", "advocacy_rate", 1.0, 0.1),
    ("corps-air", "corps_alloc_lag_days", 0, 4),
    ("corps-reserve", "corps_recognition_days", 0, 4),
    ("division", "div_recognition_days", 0, 4),
]
N_WORLDS = 60
SEEDS = 3
DAYS = 30


def run(factors, seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    for k, f in factors.items():
        if k in p:
            p[k] = p[k] * f
    p.update(BASE)
    p.update(over)
    camp = Campaign(
        axes=axes, params=p, seed=seed, corps_reserve=data["corps_reserve_units"]
    )
    camp.run(DAYS)
    return sum(ax["blue"].cv for ax in axes.values())


def cell(factors, base_seed, **over):
    return statistics.mean(run(factors, base_seed + s, **over) for s in range(SEEDS))


winners = Counter()
spreads = {name: [] for name, *_ in SWINGS}
for i in range(N_WORLDS):
    prng = random.Random(10_000 + i)
    factors = {k: prng.uniform(0.6, 1.4) for k in PERTURBED}
    seed = 20_000 + 10 * i
    world = {}
    for name, key, sharp, dull in SWINGS:
        spread = abs(
            cell(factors, seed, **{key: sharp}) - cell(factors, seed, **{key: dull})
        )
        world[name] = spread
        spreads[name].append(spread)
    winners[max(world, key=world.get)] += 1

print(f"# v8 echelon sweep: {N_WORLDS} worlds x {SEEDS} seeds, {DAYS} days")
print("max-leverage echelon (count of worlds):")
for name, n in winners.most_common():
    print(f"  {name:<14} {n}/{N_WORLDS}")
print("median CV spread by echelon:")
for name in spreads:
    print(f"  {name:<14} {statistics.median(spreads[name]):.1f}")
