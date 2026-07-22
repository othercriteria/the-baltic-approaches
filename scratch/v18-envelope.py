"""v18: the NBC conceit's envelope, measured (planning/nbc-conceit.md
§5-6). Two measurement-only instruments added in v18: red's
norm-shortfall against its own conventional-track rate (plan_kmd,
1967-directive-anchored) and the conceit-envelope validity check
(red exit: >= nbc_red_lag_exit days behind on even its best axis;
blue exit: an axis falls). This script reports where the canonical
scenario lives relative to the envelope, across policies and
warning values.

Run: python3 scratch/v18-envelope.py
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


def row(label, **over):
    inside, red_exits, blue_exits, lag10, lag21 = 0, [], [], [], []
    for i in range(N):
        data, axes, _ = load_scenario(SCEN)
        p = data["params"]
        p.update(over)
        camp = Campaign(
            axes=axes,
            params=p,
            seed=5000 + i,
            corps_reserve=data["corps_reserve_units"],
            amphib_pool=data["amphib_units"],
            zealand_garrison=data["zealand_garrison_units"],
        )
        state = camp.run(DAYS)
        env = camp.conceit_envelope(state)
        inside += env["inside"]
        if env["red_exit_day"]:
            red_exits.append(env["red_exit_day"])
        if env["blue_exit_day"]:
            blue_exits.append(env["blue_exit_day"])
        for day, sink in ((10, lag10), (21, lag21)):
            lags = [e.plan_lag for e in camp.logs if e.day == day]
            if lags:
                sink.append(min(lags))  # red's BEST axis
    fmt = lambda xs: f"d{statistics.mean(xs):.0f}x{len(xs)}" if xs else "--"
    print(
        f"{label:26s} inside {inside:2d}/{N}  "
        f"red-exit {fmt(red_exits):8s}  blue-exit {fmt(blue_exits):8s}  "
        f"best-axis lag d10 {statistics.mean(lag10):+5.1f}  "
        f"d21 {statistics.mean(lag21):+5.1f}"
    )


print(f"# v18 envelope: n={N}, days={DAYS}, thresh=6.0d behind best axis\n")
print("## policies (direct)")
for deep in (0.0, 0.5, 1.0):
    row(f"deep={deep}", apportionment_mode="direct", deep_fraction=deep)
print("\n## advocacy baseline x warning")
for w in (4, 2, 1, 0):
    row(f"advocacy W={w}", warning_days=w, **ADVOCACY)
