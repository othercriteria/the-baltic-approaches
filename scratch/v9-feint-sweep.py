"""v9 robustness sweep for the feint claim.

C1: the threat-in-being has teeth — blue ends materially weaker
    under "threat" than under "none" (CV gap > 2).
C2: the feint is at least as good for red as the failed landing —
    CV_blue(threat) <= CV_blue(commit d4) + 2.
(Directions: lower blue CV = better for red. Note commit is
UNDERPRICED for red — the lost landing force is not charged — so a
C2 pass is a floor on feint dominance.)

Run: python3 scratch/v9-feint-sweep.py
"""

import random
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
    zealand_caution=0.5,
    naval_claim_frac=0.3,
    zealand_battle_claim=0.8,
    zealand_battle_days=4,
    zealand_landing_fails=True,
)
N_WORLDS = 60
SEEDS = 3
DAYS = 30


def cv(factors, base_seed, **over):
    vals = []
    for s in range(SEEDS):
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
            seed=base_seed + s,
            corps_reserve=data["corps_reserve_units"],
        )
        camp.run(DAYS)
        vals.append(sum(ax["blue"].cv for ax in axes.values()))
    return statistics.mean(vals)


c1 = c2 = 0
teeth = []
for i in range(N_WORLDS):
    prng = random.Random(10_000 + i)
    factors = {k: prng.uniform(0.6, 1.4) for k in PERTURBED}
    seed = 20_000 + 10 * i
    none = cv(factors, seed, red_amphib="none")
    threat = cv(factors, seed, red_amphib="threat")
    commit = cv(factors, seed, red_amphib="commit", red_commit_day=4)
    if none - threat > 2:
        c1 += 1
    if threat <= commit + 2:
        c2 += 1
    teeth.append(none - threat)

print(f"# v9 feint sweep: {N_WORLDS} worlds x {SEEDS} seeds, {DAYS} days")
print(f"C1 threat has teeth (none-threat > 2 CV):   {c1}/{N_WORLDS}")
print(f"C2 feint >= failed landing (for red):       {c2}/{N_WORLDS}")
print(
    f"threat's cost to blue: median {statistics.median(teeth):.1f} CV, "
    f"p10 {sorted(teeth)[len(teeth) // 10]:.1f}, "
    f"p90 {sorted(teeth)[9 * len(teeth) // 10]:.1f}"
)
