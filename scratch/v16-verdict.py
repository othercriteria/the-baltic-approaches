"""v16 verdict runs: does the flagship claim survive the re-baseline?

Three questions, one script:
1. The v15 comparison, re-run: deep vs close at the toy point
   (direct mode, n seeds) on the RE-BASELINED scenario (posture
   demand on, supply re-tuned). v15 found flat-demand deep-dominance
   INVERTED under raw posture demand; this is the tuned answer.
2. The 90-hour table, re-run: W in {4,2,1,0} on the advocacy
   baseline — now with the delaying screen, so the uncovered-axis
   collapse path is no longer a free march (the flattered middle
   rows of the original table).
3. The advocacy-baseline sanity row (campaign-2's canonical policy
   point) for the findings entry.

Run: python3 scratch/v16-verdict.py
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
    / "toy-landjut-v16.toml"
)
N = 30
DAYS = 21
ADVOCACY = dict(
    apportionment_mode="advocacy",
    theater_deep_fraction=0.2,
    corps_request_deep=1.0,
    advocacy_rate=0.3,
    advocacy_lag_days=1,
    zealand_caution=0.5,
    naval_claim_frac=0.3,
)


def run(seed, **over):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p.update(over)
    camp = Campaign(
        axes=axes,
        params=p,
        seed=seed,
        corps_reserve=data["corps_reserve_units"],
        amphib_pool=data["amphib_units"],
        zealand_garrison=data["zealand_garrison_units"],
    )
    state = camp.run(DAYS)
    return camp, state, axes


def row(label, **over):
    held, cv, feba, ca = [], [], [], []
    for i in range(N):
        camp, state, axes = run(5000 + i, **over)
        held.append(sum(1 for st in state.values() if not st.fallen))
        cv.append(sum(ax["blue"].cv for ax in axes.values()))
        feba.append(sum(st.feba_km for st in state.values()))
        ca.append(sum(1 for e in camp.logs if e.ca))
    print(
        f"{label:28s} held {statistics.mean(held):.2f}  "
        f"blue CV {statistics.mean(cv):5.1f}  "
        f"FEBA sum {statistics.mean(feba):5.0f} km  "
        f"CA days {statistics.mean(ca):.1f}"
    )
    return statistics.mean(held), statistics.mean(cv)


print(f"# v16 verdict: n={N}, days={DAYS}, re-baselined scenario\n")
print("## 1. deep vs close, direct mode (the v15 comparison, re-tuned)")
r0 = row("close (deep=0.0)", apportionment_mode="direct", deep_fraction=0.0)
r5 = row("split (deep=0.5)", apportionment_mode="direct", deep_fraction=0.5)
r1 = row("deep  (deep=1.0)", apportionment_mode="direct", deep_fraction=1.0)
verdict = "DEEP" if (r1[0], r1[1]) > (r0[0], r0[1]) else "CLOSE"
print(f"-> ranking at the toy point: {verdict} wins (held, then CV)\n")

print("## 2. the 90-hour table, re-run with the screen (advocacy baseline)")
for w in (4, 2, 1, 0):
    row(f"W={w} warning days", warning_days=w, **ADVOCACY)
print()

print("## 3. canonical advocacy baseline (W=4)")
row("advocacy baseline", **ADVOCACY)
