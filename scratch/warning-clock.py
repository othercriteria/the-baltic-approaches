"""Pre-campaign-3 calibration run: the 90-hour clock.

Bogason Ch 6 (Helms 1975): the Jutland Division needs ~90 hours
from mobilization to its Schleswig battle positions. The toy
scenario has its battalions in place on day 1 — implicitly ~4 days
of acted-upon warning. FE doctrine bounds warning: political 48h-8
days, tactical worst-case none (reference/zealand-landing.md §2).

So: warning W days => JDiv main body (line + withheld, inland
axis) arrives day max(1, 4-W). W=4+ reproduces the current
scenario; W=0 is the no-warning nightmare. What is a day of
warning worth? Parameter arithmetic only — no mechanics; feeds the
v15 re-baseline's choice of canonical opening.

Note: a late-arriving withheld battalion enters the LINE on
arrival (reserve queue semantics) — the massing subtlety is lost
at W<4; flagged, acceptable for a shape run.

Run: python3 scratch/warning-clock.py
"""

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from wargame.campaign import Campaign
from wargame.oob import load_scenario

SCEN = Path(__file__).resolve().parent.parent / "wargame" / "scenarios" / "toy-landjut.toml"
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
)


def run(seed, warning):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p.update(BASE)
    arrive = max(1, 4 - warning)
    if arrive > 1:
        blue = axes["inland-bad-segeberg"]["blue"]
        movers = [u for u in blue.units if u.name.startswith("B-JDiv")] + [
            u for u in blue.withheld if u.name.startswith("B-JDiv")
        ]
        for u in movers:
            if u in blue.units:
                blue.units.remove(u)
            else:
                blue.withheld.remove(u)
            u.arrival_day = arrive
            blue.reserve.append(u)
    camp = Campaign(
        axes=axes, params=p, seed=seed,
        amphib_pool=data["amphib_units"],
        zealand_garrison=data["zealand_garrison_units"],
    )
    state = camp.run(DAYS)
    return {
        "held": sum(1 for st in state.values() if not st.fallen),
        "blue_cv": sum(ax["blue"].cv for ax in axes.values()),
        "feba": sum(st.feba_km for st in state.values()),
    }


print(f"# The 90-hour clock: n={N}, {DAYS} days | JDiv arrives day max(1, 4-W)")
print(f"  {'warning W':>9} {'arrive':>6} | {'held':>4} {'blueCV':>7} {'FEBA':>5}")
prev = None
for w in (4, 2, 1, 0):
    rows = [run(20_000 + i, w) for i in range(N)]
    m = {k: statistics.mean(r[k] for r in rows) for k in rows[0]}
    delta = f"  (day worth {prev - m['blue_cv']:+.1f} CV)" if prev is not None and w < 4 else ""
    print(
        f"  {w:>9} {max(1, 4 - w):>6} | {m['held']:>4.2f} {m['blue_cv']:>7.1f} "
        f"{m['feba']:>5.0f}{delta}"
    )
    prev = m["blue_cv"]
