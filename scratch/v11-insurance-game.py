"""v11 experiment: COMBALTAP's insurance decision as a game.

Blue chooses a garrison policy without knowing red's type; red's
type ranges from no-threat to the opportunist who punishes a
release. Payoffs refuse to collapse: blue CV, FEBA, and Zealand
lost are reported side by side (which one is "the goal" is the
book's question, not the model's).

Release-d18 sits past every sea-close draw (10-17): the "wait for
the weather to free you" policy.

Run: python3 scratch/v11-insurance-game.py
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
    ("hold always", dict(zg_release_mode="never")),
    ("release d8", dict(zg_release_mode="day", zg_release_day=8)),
    ("release d12", dict(zg_release_mode="day", zg_release_day=12)),
    ("release d18 (post-sea)", dict(zg_release_mode="day", zg_release_day=18)),
    (
        "threshold c<0.2",
        dict(
            zg_release_mode="threshold", zg_release_c=0.2, zg_release_recognition_days=2
        ),
    ),
]
RED = [
    ("none", dict(red_amphib="none")),
    ("threat", dict(red_amphib="threat")),
    ("commit d6", dict(red_amphib="commit", red_commit_day=6)),
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


print(f"# v11 insurance game: n={N}, {DAYS} days | cell = blueCV / FEBA / Z-lost%")
header = "  " + f"{'blue \\\\ red':<24}" + "".join(f"{r[0]:>22}" for r in RED)
print(header)
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
    print(f"  {blabel:<24} worst-case blueCV {worst:>5.1f} | max Z-lost {zmax:>4.0%}")
for rlabel, _ in RED:
    best = max(BLUE, key=lambda b: matrix[(b[0], rlabel)]["blue_cv"])
    print(
        f"  best blue vs {rlabel:<12} -> {best[0]} ({matrix[(best[0], rlabel)]['blue_cv']:.1f})"
    )
