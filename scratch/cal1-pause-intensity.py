"""CAL-1 sensitivity: pause_intensity 0.25 (v6 placeholder) vs 0.41
(FM 101-10-1 'inactive situation' = 80% of protracted, normalized to
defense-day-1 — reference/consumption-factors.md §2, CAL-1).

Note the conflation being tested: the parameter scales BOTH paused
consumption and paused contact intensity; the FM number calibrates
only the consumption face.

Run: python3 scratch/cal1-pause-intensity.py
"""

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from wargame.campaign import Campaign
from wargame.oob import load_scenario

SCENARIO = (
    Path(__file__).resolve().parent.parent
    / "wargame"
    / "scenarios"
    / "toy-landjut.toml"
)
N = 40
DAYS = 30  # longer than the 24-day v6 horizon: pulses need room


def run(pause_intensity, deep, target, seed):
    data, axes, _ = load_scenario(SCENARIO)
    p = data["params"]
    p["pause_intensity"] = pause_intensity
    p["deep_fraction"] = deep
    p["deep_target"] = target
    camp = Campaign(axes=axes, params=p, seed=seed)
    state = camp.run(DAYS)
    return {
        "held": sum(1 for st in state.values() if not st.fallen),
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "red_cv": sum(ax["red"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
        "pause_days": sum(1 for e in camp.logs if e.pause),
    }


def cell(pi, deep, target):
    rows = [run(pi, deep, target, 20_000 + i) for i in range(N)]
    return {k: statistics.mean(r[k] for r in rows) for k in rows[0]}


print(f"# CAL-1: n={N} seeds, {DAYS} days, toy-landjut")
print(
    f"# {'pi':>4} {'deep':>4} {'target':>10} | {'held':>4} {'blueCV':>6} {'redCV':>6} {'FEBA':>5} {'pauseD':>6}"
)
for target in ("echelon", "throughput"):
    for deep in (0.0, 1.0):
        for pi in (0.25, 0.41):
            c = cell(pi, deep, target)
            print(
                f"  {pi:>4} {deep:>4} {target:>10} | {c['held']:>4.2f} "
                f"{c['blue_cv']:>6.1f} {c['red_cv']:>6.1f} {c['feba']:>5.0f} {c['pause_days']:>6.1f}"
            )
