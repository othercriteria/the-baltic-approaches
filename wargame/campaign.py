"""Axis-based campaign frame: day steps, battalion atoms.

The frame is micro-strategic (planning/wargaming.md): each axis is a
1-D corridor with a FEBA position in km from the start line. Each
day, forces in contact fight (Lanchester square, scaled to daily
attrition); the defender withdraws Epstein-style when its daily loss
fraction exceeds tolerance; the attacker advances into ground given
or won. Advance rates are PLACEHOLDER values pending QJM's tables
(reference/shelf.md).

Deterministic: no dice in v0. The seed parameter is reserved for the
engagement-variance layer (planned; see findings).
"""

from dataclasses import dataclass, field

from .models import epstein, lanchester


@dataclass
class AxisState:
    name: str
    length_km: float
    feba_km: float = 0.0
    contact: bool = True
    fallen: bool = False


@dataclass
class DayLog:
    day: int
    axis: str
    ratio: float
    red_loss_frac: float
    blue_loss_frac: float
    withdrawal_km: float
    advance_km: float
    feba_km: float


@dataclass
class Campaign:
    axes: dict
    params: dict
    logs: list = field(default_factory=list)

    def run(self, days):
        state = {
            name: AxisState(name=name, length_km=ax["spec"]["length_km"])
            for name, ax in self.axes.items()
        }
        for day in range(1, days + 1):
            for name, ax in self.axes.items():
                st = state[name]
                if st.fallen:
                    continue
                self._axis_day(day, ax, st)
        return state

    def _axis_day(self, day, ax, st):
        red, blue = ax["red"], ax["blue"]
        p = self.params
        r_cv, b_cv = red.cv, blue.cv
        if b_cv <= 0.5:  # defense collapsed: road-march advance
            adv = p["march_kmd"]
            st.feba_km += adv
            self._log(day, st, r_cv, b_cv, 0, 0, 0, adv)
            self._check_fallen(st)
            return
        if r_cv <= 0.5:
            self._log(day, st, r_cv, b_cv, 0, 0, 0, 0.0)
            return

        # Engagement: square law scaled to daily loss coefficients.
        alpha = p["alpha"]  # red fire effect on blue, per red CV per day
        beta = p["beta"]  # blue fire effect on red
        # square_step(a, d, alpha, beta): alpha = A's fire on D. Here
        # A=red, so alpha = red-on-blue, beta = blue-on-red.
        r_after, b_after = lanchester.square_step(r_cv, b_cv, alpha, beta)
        red_loss = r_cv - r_after
        blue_loss = b_cv - b_after
        blue_frac = blue_loss / b_cv

        # Defender's Epstein-style reaction, then dilution of the day.
        w = epstein.withdrawal_rate_kmd(blue_frac, p["blue_tolerance"], p["w_max_kmd"])
        scale = epstein.contact_attrition_scale(w, p["w_max_kmd"])
        red_loss *= scale
        blue_loss *= scale
        red.distribute_losses(red_loss)
        blue.distribute_losses(blue_loss)

        # Attacker advance: pushes into ground given, plus pressure
        # advance by force ratio (PLACEHOLDER thresholds).
        ratio = red.cv / max(blue.cv, 0.1)
        adv = min(w, p["march_kmd"])
        if ratio >= p["advance_ratio"]:
            adv += p["pressure_kmd"]
        st.feba_km += adv
        self._log(
            day,
            st,
            red.cv,
            blue.cv,
            red_loss / max(r_cv, 0.1),
            blue_loss / max(b_cv, 0.1),
            w,
            adv,
        )
        self._check_fallen(st)

    def _check_fallen(self, st):
        if st.feba_km >= st.length_km:
            st.feba_km = st.length_km
            st.fallen = True

    def _log(self, day, st, r_cv, b_cv, r_frac, b_frac, w, adv):
        self.logs.append(
            DayLog(
                day=day,
                axis=st.name,
                ratio=round(r_cv / max(b_cv, 0.1), 2),
                red_loss_frac=round(r_frac, 3),
                blue_loss_frac=round(b_frac, 3),
                withdrawal_km=round(w, 1),
                advance_km=round(adv, 1),
                feba_km=round(st.feba_km, 1),
            )
        )
