"""Parameter sensitivity sweep: which structural claims survive?

The counter-brief discipline applied to our own instrument
(notes/wargaming-findings.md): before any run's shape informs canon,
perturb the placeholder parameters and report which qualitative
results hold across the perturbed ensemble, not just at the
hand-picked point.

Each sample multiplies the key parameters by independent U(lo, hi)
draws, then runs the scenario under each air policy with its own
weather seed. Reported per policy: axes held, blue CV, counter-
attack days — and the survival rates of the standing structural
claims.

Run: python -m wargame.sweep wargame/scenarios/toy-landjut.toml
"""

import argparse
import random
from pathlib import Path

from .campaign import Campaign
from .oob import load_scenario

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
    # v16: warning is a first-class scenario parameter (the 90-hour
    # clock finding) — scenarios that declare warning_days get it
    # perturbed like everything else (x U(lo,hi): W 4 -> ~2.4-5.6)
    "warning_days",
]

POLICIES = (0.0, 0.5, 1.0)


def run_sample(scenario, i, days, lo, hi):
    prng = random.Random(10_000 + i)
    factors = {k: prng.uniform(lo, hi) for k in PERTURBED}
    outcomes = {}
    for deep in POLICIES:
        data, axes, _ = load_scenario(scenario)
        p = data["params"]
        for k, f in factors.items():
            if k in p:
                p[k] = p[k] * f
        p["deep_fraction"] = deep
        camp = Campaign(axes=axes, params=p, seed=20_000 + i)
        state = camp.run(days)
        outcomes[deep] = {
            "held": sum(1 for st in state.values() if not st.fallen),
            "blue_cv": round(sum(ax["blue"].cv for ax in axes.values()), 1),
            "ca_days": sum(1 for e in camp.logs if e.ca),
        }
    return outcomes


def main():
    ap = argparse.ArgumentParser(prog="wargame.sweep")
    ap.add_argument("scenario", type=Path)
    ap.add_argument("--n", type=int, default=150)
    ap.add_argument("--days", type=int, default=21)
    ap.add_argument("--lo", type=float, default=0.6)
    ap.add_argument("--hi", type=float, default=1.4)
    args = ap.parse_args()

    samples = [
        run_sample(args.scenario, i, args.days, args.lo, args.hi) for i in range(args.n)
    ]

    print(f"# sweep: n={args.n}, days={args.days}, U({args.lo},{args.hi}) on:")
    print(f"#   {', '.join(PERTURBED)}")
    print()
    for deep in POLICIES:
        held = [s[deep]["held"] for s in samples]
        cv = [s[deep]["blue_cv"] for s in samples]
        ca = [s[deep]["ca_days"] for s in samples]
        print(
            f"deep={deep}: held 2/1/0 = {held.count(2)}/{held.count(1)}/"
            f"{held.count(0)} | mean blue CV {sum(cv) / len(cv):.1f} "
            f"| mean CA days {sum(ca) / len(ca):.1f}"
        )
    print()

    def claim(name, pred):
        k = sum(1 for s in samples if pred(s))
        print(f"{name}: {k}/{len(samples)} ({100 * k / len(samples):.0f}%)")

    claim(
        "all-deep holds at least as many axes as all-close",
        lambda s: s[1.0]["held"] >= s[0.0]["held"],
    )
    claim(
        "all-deep strictly better (held, then blue CV)",
        lambda s: (
            (s[1.0]["held"], s[1.0]["blue_cv"]) > (s[0.0]["held"], s[0.0]["blue_cv"])
        ),
    )
    claim(
        "monotone in deep fraction (held)",
        lambda s: s[1.0]["held"] >= s[0.5]["held"] >= s[0.0]["held"],
    )
    claim(
        "counterattack window needs deep (CA only when deep>0)",
        lambda s: s[0.0]["ca_days"] == 0,
    )
    claim(
        "split is strictly worst (the dead v1 claim, tracked)",
        lambda s: (
            (s[0.5]["held"], s[0.5]["blue_cv"])
            < min(
                (s[0.0]["held"], s[0.0]["blue_cv"]),
                (s[1.0]["held"], s[1.0]["blue_cv"]),
            )
        ),
    )


if __name__ == "__main__":
    main()
