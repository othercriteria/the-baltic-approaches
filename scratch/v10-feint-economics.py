"""v10 experiment: the feint's economics, now commensurable.

Red's amphib package is real units: staged it eats red theater
supply (FM inactive rate) and withholds 26 CV of convertible mech
from the mainland; released it thins the threat (but blue's ratchet
lags); committed it is spent. What is red's best policy — and what
does a blue G-2 that believes reassurance faster buy?

Blue baseline: advocacy 0.3, caution 0.5, skim 0.3.
Run: python3 scratch/v10-feint-economics.py
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
    pin_release_c=0.25,
)
POLICIES = [
    ("none (no feint formed)", dict(red_amphib="none")),
    ("threat: hold fat", dict(red_amphib="threat")),
    (
        "threat: release d6",
        dict(red_amphib="threat", amphib_release_convertibles_day=6),
    ),
    (
        "threat: release d10",
        dict(red_amphib="threat", amphib_release_convertibles_day=10),
    ),
    (
        "threat: release d14",
        dict(red_amphib="threat", amphib_release_convertibles_day=14),
    ),
    ("commit d6", dict(red_amphib="commit", red_commit_day=6)),
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
        amphib_pool=data["amphib_units"],
    )
    state = camp.run(DAYS)
    cs = {}
    for e in camp.logs:
        cs.setdefault(e.day, e.zeal_c)
    return {
        "held": sum(1 for st in state.values() if not st.fallen),
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "red_cv": sum(ax["red"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
        "mean_c": statistics.mean(cs.values()),
    }


def block(title, extra):
    print(f"## {title}")
    print(
        f"  {'red policy':<24} | {'held':>4} {'blueCV':>7} {'redCV':>6} "
        f"{'FEBA':>5} {'meanC':>5}"
    )
    for label, over in POLICIES:
        rows = [run(20_000 + i, **over, **extra) for i in range(N)]
        m = {k: statistics.mean(r[k] for r in rows) for k in rows[0]}
        print(
            f"  {label:<24} | {m['held']:>4.2f} {m['blue_cv']:>7.1f} "
            f"{m['red_cv']:>6.1f} {m['feba']:>5.0f} {m['mean_c']:>5.2f}"
        )


print(f"# v10 feint economics: n={N}, {DAYS} days")
block("blue G-2 ratcheted (zeal_c_down=0.05, the FE record)", dict(zeal_c_down=0.05))
block("blue G-2 sharp (zeal_c_down=0.3 — believes reassurance)", dict(zeal_c_down=0.3))
