"""v7 experiment: the persuasion tax and the naval claim, priced.

Baseline: direct deep=1.0 (v6's ideal — the corps owns the lever).
Advocacy: theater prior 0.2, corps request 1.0, granted at
advocacy_rate per day after a 1-day lag. The gap to baseline is the
campaign cost of not owning the lever — the memo trail in km and CV.
Naval claim: Op Hurricane's share of deep-capable sorties while the
amphib window is open.

Run: python3 scratch/v7-advocacy-experiment.py
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


def run(seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p.update(over)
    camp = Campaign(axes=axes, params=p, seed=seed)
    state = camp.run(DAYS)
    grants = {}
    for e in camp.logs:
        grants.setdefault(e.day, e.deep_frac)
    return {
        "held": sum(1 for st in state.values() if not st.fallen),
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
        "mean_deep": statistics.mean(grants.values()) if grants else 0.0,
    }


def cell(label, **over):
    rows = [run(20_000 + i, **over) for i in range(N)]
    m = {k: statistics.mean(r[k] for r in rows) for k in rows[0]}
    print(
        f"  {label:<34} | {m['held']:>4.2f} {m['blue_cv']:>6.1f} "
        f"{m['feba']:>5.0f} {m['mean_deep']:>5.2f}"
    )
    return m


print(f"# v7: n={N} seeds, {DAYS} days | held blueCV FEBA meanDeep")
print("## The persuasion tax (corps request 1.0, theater prior 0.2)")
cell(
    "direct 1.0 (v6 ideal: corps owns it)",
    apportionment_mode="direct",
    deep_fraction=1.0,
)
for rate in (1.0, 0.6, 0.3, 0.15, 0.0):
    cell(
        f"advocacy rate={rate}",
        apportionment_mode="advocacy",
        theater_deep_fraction=0.2,
        corps_request_deep=1.0,
        advocacy_rate=rate,
        advocacy_lag_days=1,
    )
cell("direct 0.2 (voiceless floor)", apportionment_mode="direct", deep_fraction=0.2)

print("## The naval claim (advocacy rate=0.3, request 1.0)")
for claim in (0.0, 0.3, 0.6):
    cell(
        f"naval_claim_frac={claim}",
        apportionment_mode="advocacy",
        theater_deep_fraction=0.2,
        corps_request_deep=1.0,
        advocacy_rate=0.3,
        advocacy_lag_days=1,
        naval_claim_frac=claim,
    )
