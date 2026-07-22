"""v9 experiment: what is the threat-in-being worth?

Red's amphib posture choice, priced from blue's side, with the
Zealand coupling ON (caution 0.5 — the conference hedges while the
straits are threatened). Blue baseline: advocacy rate 0.3, request
1.0, prior 0.2, naval skim 0.3 while threatened.

  none       — no amphib threat at all (counterfactual)
  threat     — the pin-in-being, until the sea state closes
  commit d4  — early landing: air surge d4-7, fails, all pins
               release on d8 (ahead of the weather)
  commit d8  — later landing, same shape

Run: python3 scratch/v9-feint-experiment.py
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
N = 60
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
    zealand_landing_fails=True,
)
POSTURES = [
    ("none", dict(red_amphib="none")),
    ("threat", dict(red_amphib="threat")),
    ("commit d4", dict(red_amphib="commit", red_commit_day=4)),
    ("commit d8", dict(red_amphib="commit", red_commit_day=8)),
]


def run(seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p.update(BASE)
    p.update(over)
    camp = Campaign(
        axes=axes, params=p, seed=seed, corps_reserve=data["corps_reserve_units"]
    )
    state = camp.run(DAYS)
    return {
        "held": sum(1 for st in state.values() if not st.fallen),
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
        "release": camp.pin_release_day or DAYS + 1,
    }


print(f"# v9 feint pricing: n={N}, {DAYS} days, caution=0.5, skim=0.3")
print(f"  {'red posture':<12} | {'held':>4} {'blueCV':>7} {'FEBA':>5} {'meanRel':>7}")
for label, over in POSTURES:
    rows = [run(20_000 + i, **over) for i in range(N)]
    m = {k: statistics.mean(r[k] for r in rows) for k in rows[0]}
    print(
        f"  {label:<12} | {m['held']:>4.2f} {m['blue_cv']:>7.1f} "
        f"{m['feba']:>5.0f} {m['release']:>7.1f}"
    )
