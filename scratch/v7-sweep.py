"""v7 robustness sweep: do the advocacy findings survive parameter
perturbation? Same discipline and perturbation set as wargame/sweep.py
(U(0.6,1.4) on the key params), 30 days.

Claims under test:
  C1: blue CV is monotone nondecreasing in advocacy_rate
      (owning the lever faster is never worse for the force).
  C2: the tax is earliness, not average effort — rate 0.15 reaches
      mean granted deep >= 0.7 yet delivers < 60% of direct-1.0's
      blue CV.
  C3: rate 0.0 == direct at the theater prior (sanity identity).

Run: python3 scratch/v7-sweep.py
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
N = 100
DAYS = 30
RATES = (0.0, 0.15, 0.3, 1.0)


def run(factors, seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    for k, f in factors.items():
        if k in p:
            p[k] = p[k] * f
    p.update(over)
    camp = Campaign(axes=axes, params=p, seed=seed)
    state = camp.run(DAYS)
    grants = {}
    for e in camp.logs:
        grants.setdefault(e.day, e.deep_frac)
    return {
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "mean_deep": statistics.mean(grants.values()) if grants else 0.0,
    }


c1 = c2 = c3 = 0
taxes = []
for i in range(N):
    prng = random.Random(10_000 + i)
    factors = {k: prng.uniform(0.6, 1.4) for k in PERTURBED}
    seed = 20_000 + i
    adv = {
        r: run(
            factors,
            seed,
            apportionment_mode="advocacy",
            theater_deep_fraction=0.2,
            corps_request_deep=1.0,
            advocacy_rate=r,
            advocacy_lag_days=1,
        )
        for r in RATES
    }
    ideal = run(factors, seed, apportionment_mode="direct", deep_fraction=1.0)
    floor = run(factors, seed, apportionment_mode="direct", deep_fraction=0.2)
    seq = [adv[r]["blue_cv"] for r in RATES]
    if all(b >= a - 0.5 for a, b in zip(seq, seq[1:])):
        c1 += 1
    if adv[0.15]["mean_deep"] >= 0.7 and adv[0.15]["blue_cv"] < 0.6 * max(
        ideal["blue_cv"], 1e-9
    ):
        c2 += 1
    if abs(adv[0.0]["blue_cv"] - floor["blue_cv"]) < 0.01:
        c3 += 1
    if ideal["blue_cv"] > 1:
        taxes.append(1.0 - adv[0.3]["blue_cv"] / ideal["blue_cv"])

print(f"# v7 sweep: n={N}, days={DAYS}, U(0.6,1.4) on {len(PERTURBED)} params")
print(f"C1 monotone in advocacy_rate:            {c1}/{N}")
print(f"C2 earliness-not-average (rate 0.15):    {c2}/{N}")
print(f"C3 rate-0 identity with direct prior:    {c3}/{N}")
print(
    f"persuasion tax at rate 0.3 (CV lost vs ideal): "
    f"median {statistics.median(taxes):.0%}, "
    f"p10 {sorted(taxes)[len(taxes) // 10]:.0%}, "
    f"p90 {sorted(taxes)[9 * len(taxes) // 10]:.0%}"
)
