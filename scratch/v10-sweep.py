"""v10 robustness sweep: does the feint-economics ranking survive
perturbation — and is it conditional on red's supply constraint
binding (the suspected mechanism)?

C1 hold-fat is red's best threat policy: blueCV(hold) <= min(
   blueCV(release d6/d10), blueCV(none)) + 1
C2 the thinned feint is dominated for red:
   blueCV(release d6) >= blueCV(hold) - 1 AND >= blueCV(none) - 1
C3 sharp blue G-2 (zeal_c_down 0.3 vs 0.05) moves blueCV under
   release-d10 by < 2 CV (insensitivity)

Run: python3 scratch/v10-sweep.py
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
    pin_release_c=0.25,
)
N_WORLDS = 60
SEEDS = 3
DAYS = 30


def blue_cv(factors, base_seed, **over):
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
            amphib_pool=data["amphib_units"],
        )
        camp.run(DAYS)
        vals.append(sum(ax["blue"].cv for ax in axes.values()))
    return statistics.mean(vals)


c1 = c2 = c3 = 0
c1_by_supply = {"lean": [0, 0], "rich": [0, 0]}  # [pass, total]
for i in range(N_WORLDS):
    prng = random.Random(10_000 + i)
    factors = {k: prng.uniform(0.6, 1.4) for k in PERTURBED}
    seed = 20_000 + 10 * i
    none = blue_cv(factors, seed, red_amphib="none")
    hold = blue_cv(factors, seed, red_amphib="threat")
    rel6 = blue_cv(
        factors, seed, red_amphib="threat", amphib_release_convertibles_day=6
    )
    rel10 = blue_cv(
        factors, seed, red_amphib="threat", amphib_release_convertibles_day=10
    )
    rel10_sharp = blue_cv(
        factors,
        seed,
        red_amphib="threat",
        amphib_release_convertibles_day=10,
        zeal_c_down=0.3,
    )
    p1 = hold <= min(rel6, rel10, none) + 1
    if p1:
        c1 += 1
    bucket = "lean" if factors["red_supply_points"] < 1.0 else "rich"
    c1_by_supply[bucket][0] += 1 if p1 else 0
    c1_by_supply[bucket][1] += 1
    if rel6 >= hold - 1 and rel6 >= none - 1:
        c2 += 1
    if abs(rel10_sharp - rel10) < 2:
        c3 += 1

print(f"# v10 sweep: {N_WORLDS} worlds x {SEEDS} seeds, {DAYS} days")
print(f"C1 hold-fat best for red:            {c1}/{N_WORLDS}")
for b, (p, t) in c1_by_supply.items():
    print(f"   .. red supply {b:<5}               {p}/{t}")
print(f"C2 thinned feint dominated:          {c2}/{N_WORLDS}")
print(f"C3 sharp G-2 buys < 2 CV:            {c3}/{N_WORLDS}")
