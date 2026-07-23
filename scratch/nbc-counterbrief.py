"""NBC counter-brief probe (2026-07-23, DK question): would LATE
escalation be operationally effective for red?

NOT canon, NOT a mechanic — a scratch what-if per the conceit's
escape-clause analysis (planning/nbc-conceit.md §5). The canonical
instrument never simulates NBC as fires; this probe brackets what
a day-13 strike could buy red AT ITS MOST GENEROUS, to test the
"frustration act" hypothesis: red's binding constraint at day 13
is throughput (supply/LOC), so destroying blue CV should buy
little ground.

Shock model, deliberately red-favorable (variant A):
  on shock day, every axis's blue LINE and WITHHELD lose frac F;
  blue's air stock is halved; red pays NOTHING (no contamination,
  no infrastructure loss, no MOPP tax, no blue retaliation).
Variant B adds the minimal self-tax the sources insist on (strike
zones + WMD-blasted infrastructure worsen red's own throughput:
red_loc_penalty 0.55 -> 0.80; the 1961/1967 directives want the
Kiel Canal locks and ports INTACT — reference/php-maritime-front.md).

Run: python3 scratch/nbc-counterbrief.py
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
DAYS = 28
SHOCK_DAY = 13
ADVOCACY = dict(
    apportionment_mode="advocacy",
    theater_deep_fraction=0.2,
    corps_request_deep=1.0,
    advocacy_rate=0.3,
    advocacy_lag_days=1,
    zealand_caution=0.5,
    naval_claim_frac=0.3,
)


class ShockCampaign(Campaign):
    shock_frac = 0.0
    red_tax = None  # post-strike red_loc_penalty, or None

    def _axis_day(self, day, ax, st, wx, air_share, arrivals, n_live):
        if day == SHOCK_DAY and not getattr(self, "_shocked", set()):
            pass
        if day >= SHOCK_DAY and st.name not in getattr(self, "_shocked", set()):
            self._shocked = getattr(self, "_shocked", set())
            self._shocked.add(st.name)
            blue = ax["blue"]
            if self.shock_frac > 0:
                blue.distribute_losses(self.shock_frac * blue.cv)
                for u in blue.withheld:
                    u.apply_loss_fraction(self.shock_frac)
                self.aircraft *= 0.5
            if self.red_tax is not None:
                self.params["red_loc_penalty"] = self.red_tax
        super()._axis_day(day, ax, st, wx, air_share, arrivals, n_live)


def row(label, frac, tax):
    feba21, feba28, held, bcv = [], [], [], []
    for i in range(N):
        data, axes, _ = load_scenario(SCEN)
        p = data["params"]
        p.update(ADVOCACY)
        camp = ShockCampaign(
            axes=axes,
            params=p,
            seed=5000 + i,
            corps_reserve=data["corps_reserve_units"],
            amphib_pool=data["amphib_units"],
            zealand_garrison=data["zealand_garrison_units"],
        )
        camp.shock_frac = frac
        camp.red_tax = tax
        state = camp.run(DAYS)
        f21 = sum(
            e.feba_km
            for e in camp.logs
            if e.day == 21 or (e.day < 21 and state[e.axis].fallen_day == e.day)
        )
        # simpler: reconstruct day-21 FEBA per axis from logs
        per = {}
        for e in camp.logs:
            if e.day <= 21:
                per[e.axis] = e.feba_km
        feba21.append(sum(per.values()))
        feba28.append(sum(st.feba_km for st in state.values()))
        held.append(sum(1 for st in state.values() if not st.fallen))
        bcv.append(sum(ax["blue"].cv for ax in axes.values()))
    print(
        f"{label:34s} FEBA d21 {statistics.mean(feba21):5.0f}  "
        f"d28 {statistics.mean(feba28):5.0f}  "
        f"held {statistics.mean(held):.2f}  blue CV {statistics.mean(bcv):5.1f}"
    )


print(f"# NBC counter-brief probe: shock day {SHOCK_DAY}, n={N}, days={DAYS}\n")
row("baseline (no strike)", 0.0, None)
row("A: strike 40% blue, free", 0.4, None)
row("A: strike 60% blue, free", 0.6, None)
row("B: strike 60% + red LOC tax .80", 0.6, 0.80)
