"""Axis-based campaign frame: day steps, battalion atoms. v1.

The frame is micro-strategic (planning/wargaming.md): each axis is a
1-D corridor with a FEBA position in km from the start line. Each
day, per axis:

1. Red follow-on echelons arrive (arrival_day + accumulated
   interdiction delay) — echelonment is the FOFA payload.
2. Blue allocates air: `deep_fraction` of blue_air_points goes to
   interdiction (attrits and delays the *unarrived* echelon; delay
   rate capped — you cannot stop the second echelon, only make it
   arrive late and weaker), the rest to close support (adds CV to
   today's engagement without absorbing ground losses).
3. Forces in contact fight (Lanchester square scaled to daily
   attrition); the defender withdraws Epstein-style when projected
   full-contact losses exceed tolerance — but not past the axis
   hold line (forward-defense politics as geometry). Standing at a
   hold line means eating full-contact attrition.
4. The attacker advances into ground given, plus a pressure advance
   at high force ratio (PLACEHOLDER thresholds pending QJM advance
   rates — NP&W, holdings pipeline).

Attrition calibration anchors: HERO Handbook on Ground Forces
Attrition (Sept 1986, on the shelf): division engagement casualty
norm ~1.0%/day (Fig 48 discussion, p.~120); terrain/weather TBC
matrix 1.6-3.6%/day for rolling terrain, temperate/cold cells
(Fig 47); battalion-level ceiling ~3.5%/day short of catastrophe.
CV-points-to-personnel mapping remains abstract; parameters should
keep daily loss fractions inside that band.

Logging discipline (findings item 6): the log records BOTH the
defender's decision input (projected full-contact loss fraction)
and the realized outcome — staffs see estimates and results
disagree, and so should readers of this log.

Deterministic: no dice in v1; seed reserved for the variance layer.
"""

from dataclasses import dataclass, field

from .models import epstein, lanchester


@dataclass
class AxisState:
    name: str
    length_km: float
    hold_km: float  # withdrawal may not take the FEBA past this
    feba_km: float = 0.0
    red_delay_days: float = 0.0  # accumulated interdiction delay
    fallen: bool = False


@dataclass
class DayLog:
    day: int
    axis: str
    ratio: float
    proj_blue_frac: float  # decision input: full-contact projection
    red_loss_frac: float  # realized
    blue_loss_frac: float  # realized
    withdrawal_km: float
    standing: bool  # wanted to withdraw, hold line said no
    advance_km: float
    feba_km: float
    arrivals: int
    red_reserve_cv: float
    air_close: float
    air_deep: float


@dataclass
class Campaign:
    axes: dict
    params: dict
    logs: list = field(default_factory=list)

    def run(self, days):
        state = {}
        for name, ax in self.axes.items():
            spec = ax["spec"]
            state[name] = AxisState(
                name=name,
                length_km=spec["length_km"],
                hold_km=spec.get("hold_km", spec["length_km"]),
            )
        for day in range(1, days + 1):
            for name, ax in self.axes.items():
                st = state[name]
                if st.fallen:
                    continue
                self._axis_day(day, ax, st)
        return state

    # -- one axis-day ------------------------------------------------

    def _axis_day(self, day, ax, st):
        red, blue = ax["red"], ax["blue"]
        p = self.params

        arrivals = self._arrivals(day, red, st)
        air_close, air_deep = self._air(red, st)

        r_cv, b_cv = red.cv, blue.cv
        if b_cv <= 0.5:  # defense collapsed: road-march advance
            adv = p["march_kmd"]
            st.feba_km += adv
            self._log(
                day, st, red, 0, 0, 0, 0, 0, False, adv, arrivals, air_close, air_deep
            )
            self._check_fallen(st)
            return
        if r_cv <= 0.5:
            self._log(
                day, st, red, 0, 0, 0, 0, 0, False, 0.0, arrivals, air_close, air_deep
            )
            return

        # Close support fights today without absorbing ground losses.
        b_cv_eff = b_cv + air_close * p["close_support_cv_per_point"]

        # Projected full-contact engagement (the G3's decision input).
        # square_step(a, d, alpha, beta): alpha = A's fire on D. A=red.
        r_after, b_after = lanchester.square_step(r_cv, b_cv_eff, p["alpha"], p["beta"])
        red_loss = r_cv - r_after
        blue_loss = max(b_cv - (b_after - (b_cv_eff - b_cv)), 0.0)
        proj_blue_frac = blue_loss / b_cv

        # Epstein-style withdrawal, capped by the political hold line.
        w_wanted = epstein.withdrawal_rate_kmd(
            proj_blue_frac, p["blue_tolerance"], p["w_max_kmd"]
        )
        w = min(w_wanted, max(st.hold_km - st.feba_km, 0.0))
        standing = w_wanted > 0 and w < w_wanted
        scale = epstein.contact_attrition_scale(w, p["w_max_kmd"])
        red_loss *= scale
        blue_loss *= scale
        red.distribute_losses(red_loss)
        blue.distribute_losses(blue_loss)

        ratio = red.cv / max(blue.cv, 0.1)
        adv = min(w, p["march_kmd"])
        if ratio >= p["advance_ratio"]:
            adv += p["pressure_kmd"]
        st.feba_km += adv
        self._log(
            day,
            st,
            red,
            round(red.cv / max(blue.cv, 0.1), 2),
            proj_blue_frac,
            red_loss / max(r_cv, 0.1),
            blue_loss / max(b_cv, 0.1),
            w,
            standing,
            adv,
            arrivals,
            air_close,
            air_deep,
            ratio_known=True,
        )
        self._check_fallen(st)

    # -- helpers -----------------------------------------------------

    def _arrivals(self, day, red, st):
        arrived = 0
        for u in list(red.reserve):
            if day >= u.arrival_day + st.red_delay_days:
                red.reserve.remove(u)
                red.units.append(u)
                arrived += 1
        return arrived

    def _air(self, red, st):
        p = self.params
        points = p.get("blue_air_points", 0.0)
        deep_frac = p.get("deep_fraction", 0.0)
        deep = points * deep_frac
        close = points - deep
        if deep > 0 and red.reserve:
            red.attrit_reserve(deep * p["deep_attrition_per_point"])
            st.red_delay_days += min(
                deep * p["deep_delay_per_point"], p["deep_delay_cap_dpd"]
            )
        else:
            deep = 0.0
            close = points
        return close, deep

    def _check_fallen(self, st):
        if st.feba_km >= st.length_km:
            st.feba_km = st.length_km
            st.fallen = True

    def _log(
        self,
        day,
        st,
        red,
        ratio,
        proj,
        r_frac,
        b_frac,
        w,
        standing,
        adv,
        arrivals,
        air_close,
        air_deep,
        ratio_known=False,
    ):
        self.logs.append(
            DayLog(
                day=day,
                axis=st.name,
                ratio=ratio if ratio_known else 0.0,
                proj_blue_frac=round(proj, 3),
                red_loss_frac=round(r_frac, 3),
                blue_loss_frac=round(b_frac, 3),
                withdrawal_km=round(w, 1),
                standing=standing,
                advance_km=round(adv, 1),
                feba_km=round(st.feba_km, 1),
                arrivals=arrivals,
                red_reserve_cv=round(red.reserve_cv, 1),
                air_close=round(air_close, 1),
                air_deep=round(air_deep, 1),
            )
        )
