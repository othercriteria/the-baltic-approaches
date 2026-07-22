"""v16 re-baseline supply re-tune (the v15 gate's core demand).

The pre-v15 supply points were placeholder-tuned against FLAT
demand: every day billed at defense-day-1 rates. Posture demand
bills days at the FM ladder (<= 1.0), so the same supply points buy
systematically higher fills — flipping demand_posture without
re-tuning conflates calibration with mechanism (v15 finding).

Re-tune rule: scale each side's supply points by that side's mean
realized demand multiplier, so the campaign-average bill stays
comparable and fills are driven back toward the flat baseline's.
red_pause_buildup scales with red's factor (stockpile economy
stays commensurate). Then verify: posture fills at the scaled
points vs flat fills at the original points.

Run: python3 scratch/v16-retune.py
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
POLICIES = (0.0, 0.5, 1.0)


def run(seed, deep, posture, bscale=1.0, rscale=1.0):
    data, axes, _ = load_scenario(SCEN)
    p = data["params"]
    p["apportionment_mode"] = "direct"
    p["deep_fraction"] = deep
    p["demand_posture"] = posture
    p["blue_supply_points"] *= bscale
    p["red_supply_points"] *= rscale
    p["red_pause_buildup"] *= rscale
    camp = Campaign(
        axes=axes,
        params=p,
        seed=seed,
        corps_reserve=data["corps_reserve_units"],
        amphib_pool=data["amphib_units"],
        zealand_garrison=data["zealand_garrison_units"],
    )
    camp.run(DAYS)
    logs = camp.logs
    return {
        "bfill": statistics.mean(e.bfill for e in logs),
        "rfill": statistics.mean(e.rfill for e in logs),
        "bmult": statistics.mean(e.bmult for e in logs),
        "rmult": statistics.mean(e.rmult for e in logs),
    }


def ensemble(posture, bscale=1.0, rscale=1.0):
    rows = [
        run(3000 + i, deep, posture, bscale, rscale)
        for i in range(N)
        for deep in POLICIES
    ]
    return {k: statistics.mean(r[k] for r in rows) for k in rows[0]}


flat = ensemble(False)
raw = ensemble(True)
print(f"flat    : bfill {flat['bfill']:.3f}  rfill {flat['rfill']:.3f}")
print(
    f"posture : bfill {raw['bfill']:.3f}  rfill {raw['rfill']:.3f}"
    f"  (mults b {raw['bmult']:.3f} r {raw['rmult']:.3f})"
)
bs, rs = raw["bmult"], raw["rmult"]
tuned = ensemble(True, bs, rs)
print(
    f"retuned : bfill {tuned['bfill']:.3f}  rfill {tuned['rfill']:.3f}"
    f"  at bscale {bs:.3f} rscale {rs:.3f}"
)
# one refinement pass on the measured post-scale multipliers
bs2, rs2 = bs * tuned["bmult"] / raw["bmult"], rs * tuned["rmult"] / raw["rmult"]
tuned2 = ensemble(True, bs2, rs2)
print(
    f"pass 2  : bfill {tuned2['bfill']:.3f}  rfill {tuned2['rfill']:.3f}"
    f"  at bscale {bs2:.3f} rscale {rs2:.3f}"
)
data, _, _ = load_scenario(SCEN)
p = data["params"]
for label, scale in (("pass1", (bs, rs)), ("pass2", (bs2, rs2))):
    print(
        f"{label}: blue_supply_points {p['blue_supply_points'] * scale[0]:.1f}  "
        f"red_supply_points {p['red_supply_points'] * scale[1]:.1f}  "
        f"red_pause_buildup {p['red_pause_buildup'] * scale[1]:.1f}"
    )
