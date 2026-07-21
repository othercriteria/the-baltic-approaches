"""Axis-based campaign frame: day steps, battalion atoms. v2.

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

v2 adds:
- Weather-gated air (the variance layer; seeded, reproducible):
  November Baltic placeholder — stand-down days and a daily factor,
  pending real climatology (planning/setting-time.md).
- Close-support saturation (diminishing returns; a policy conclusion
  that only holds under linear close support is worthless).
- Counterattack windows: when red's in-contact echelon is spent and
  the follow-on echelon is still distant, blue attacks — FEBA moves
  back, the spent echelon pays a cohesion premium, blue pays the
  attacker's price. This is the tempo payload: the counterstroke
  exists only inside the window that interdiction buys.
- Political hold release (axis spec `hold_release_day`): the upward
  Andon Cord — command frees the hold line mid-campaign.
"""

import math
import random
from dataclasses import dataclass, field

from .models import epstein, lanchester


@dataclass
class AxisState:
    name: str
    length_km: float
    hold_km: float  # withdrawal may not take the FEBA past this
    feba_km: float = 0.0
    red_delay_days: float = 0.0  # accumulated blue-interdiction delay
    blue_delay_days: float = 0.0  # accumulated red-interdiction delay
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
    advance_km: float  # negative = blue counterattack gains
    feba_km: float
    arrivals: int  # red follow-on echelon units arrived today
    blue_arrivals: int  # blue mobilization units arrived today
    red_reserve_cv: float
    air_close: float
    air_deep: float
    wx: float = 1.0  # weather factor applied to today's air
    ca: bool = False  # blue counterattacked today


@dataclass
class Campaign:
    axes: dict
    params: dict
    seed: int = 1986
    logs: list = field(default_factory=list)

    def run(self, days):
        rng = random.Random(self.seed)
        p = self.params
        # Sortie generation is a stock, not a faucet: air points come
        # from surviving airframes, and sorties cost airframes.
        self.aircraft = p.get("blue_aircraft", 0.0)
        state = {}
        for name, ax in self.axes.items():
            spec = ax["spec"]
            state[name] = AxisState(
                name=name,
                length_km=spec["length_km"],
                hold_km=spec.get("hold_km", spec["length_km"]),
            )
        for day in range(1, days + 1):
            wx = self._weather(rng)  # theater-wide, one draw per day
            live = [n for n, st in state.items() if not st.fallen]
            if self.aircraft > 0:
                points_today = self.aircraft * p["sorties_per_aircraft"] * wx
            else:
                points_today = p.get("blue_air_points", 0.0) * wx
            share = points_today / len(live) if live else 0.0
            for name, ax in self.axes.items():
                st = state[name]
                if st.fallen:
                    continue
                spec = ax["spec"]
                release = spec.get("hold_release_day")
                if release and day >= release:
                    st.hold_km = st.length_km
                self._axis_day(day, ax, st, wx, share)
        return state

    # -- one axis-day ------------------------------------------------

    def _axis_day(self, day, ax, st, wx, air_share):
        red, blue = ax["red"], ax["blue"]
        p = self.params

        arrivals = self._arrivals(day, red, st)
        # Blue mobilization: red interdiction (Baltic air/missile
        # threat to Danish roads, bridges, ports — the Pałka-
        # documented axis) delays and attrits it, same capped
        # late-and-weaker logic as blue's FOFA in reverse.
        red_deep = p.get("red_deep_points", 0.0) * wx
        if red_deep > 0 and blue.reserve:
            blue.attrit_reserve(red_deep * p["red_deep_attrition_per_point"])
            st.blue_delay_days += min(
                red_deep * p["red_deep_delay_per_point"],
                p["red_delay_cap_dpd"],
            )
        blue_arrivals = 0
        for u in list(blue.reserve):
            if day >= u.arrival_day + st.blue_delay_days:
                blue.reserve.remove(u)
                blue.units.append(u)
                blue_arrivals += 1
        air_close, air_deep = self._air(red, st, wx, air_share)

        r_cv, b_cv = red.cv, blue.cv
        if b_cv <= 0.5 or not blue.has_maneuver:  # defense collapsed
            adv = p["march_kmd"]
            st.feba_km += adv
            self._log(
                day,
                st,
                red,
                0,
                0,
                0,
                0,
                0,
                False,
                adv,
                arrivals,
                blue_arrivals,
                air_close,
                air_deep,
                wx,
                False,
            )
            self._check_fallen(st)
            return
        if r_cv <= 0.5 or not red.has_maneuver:
            self._log(
                day,
                st,
                red,
                0,
                0,
                0,
                0,
                0,
                False,
                0.0,
                arrivals,
                blue_arrivals,
                air_close,
                air_deep,
                wx,
                False,
            )
            return

        # Close support fights today without absorbing ground losses;
        # saturating (diminishing returns beyond what the engaged
        # force can absorb/direct).
        sat = p.get("close_sat_cv", 0.0)
        raw = air_close * p["close_support_cv_per_point"]
        cs_cv = sat * (1.0 - math.exp(-raw / sat)) if sat > 0 else raw
        b_cv_eff = b_cv + cs_cv

        # Projected full-contact engagement (the G3's decision input).
        # square_step(a, d, alpha, beta): alpha = A's fire on D. A=red.
        r_after, b_after = lanchester.square_step(r_cv, b_cv_eff, p["alpha"], p["beta"])
        red_loss = r_cv - r_after
        blue_loss = max(b_cv - (b_after - cs_cv), 0.0)
        proj_blue_frac = blue_loss / b_cv

        if self._ca_ready(day, red, blue, st, proj_blue_frac):
            # Counterattack: full contact, no withdrawal; the spent
            # echelon pays a cohesion premium, blue pays the
            # attacker's price; FEBA moves back.
            red_loss *= p["ca_exploit"]
            blue_loss *= p["ca_blue_cost"]
            red.distribute_losses(red_loss)
            blue.distribute_losses(blue_loss)
            gain = min(p["ca_kmd"], st.feba_km)
            st.feba_km -= gain
            self._log(
                day,
                st,
                red,
                round(red.cv / max(blue.cv, 1e-9), 2),
                proj_blue_frac,
                min(red_loss / max(r_cv, 1e-9), 1.0),
                min(blue_loss / max(b_cv, 1e-9), 1.0),
                0,
                False,
                -gain,
                arrivals,
                blue_arrivals,
                air_close,
                air_deep,
                wx,
                True,
                ratio_known=True,
            )
            return

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

        ratio = red.cv / max(blue.cv, 1e-9)
        adv = min(w, p["march_kmd"])
        if ratio >= p["advance_ratio"]:
            adv += p["pressure_kmd"]
        st.feba_km += adv
        self._log(
            day,
            st,
            red,
            round(ratio, 2),
            proj_blue_frac,
            min(red_loss / max(r_cv, 1e-9), 1.0),
            min(blue_loss / max(b_cv, 1e-9), 1.0),
            w,
            standing,
            adv,
            arrivals,
            blue_arrivals,
            air_close,
            air_deep,
            wx,
            False,
            ratio_known=True,
        )
        self._check_fallen(st)

    # -- helpers -----------------------------------------------------

    def _weather(self, rng):
        """Daily air-weather factor. November-Baltic PLACEHOLDER
        (stand-down probability + degraded range) pending real
        climatology; see planning/setting-time.md."""
        p = self.params
        prob = p.get("wx_standdown_prob", 0.0)
        if prob <= 0:
            return 1.0
        if rng.random() < prob:
            return p.get("wx_standdown_factor", 0.15)
        return rng.uniform(p.get("wx_min", 0.5), p.get("wx_max", 1.0))

    def _ca_ready(self, day, red, blue, st, proj_blue_frac):
        """Counterattack window: red's in-contact echelon spent
        (ratio below threshold), the follow-on echelon at least
        ca_window_days away, ground to retake, and blue not itself
        being shredded."""
        p = self.params
        if not p.get("ca_enabled", True) or st.feba_km <= 0:
            return False
        # Attacking means accepting more risk than defending — but
        # not annihilation-level risk.
        if proj_blue_frac > p["blue_tolerance"] * p.get("ca_proj_mult", 2.5):
            return False
        if red.cv / max(blue.cv, 1e-9) >= p["ca_at_ratio"]:
            return False
        if red.reserve:
            gap = min(u.arrival_day + st.red_delay_days - day for u in red.reserve)
            if gap < p["ca_window_days"]:
                return False
        return True

    def _arrivals(self, day, red, st):
        arrived = 0
        for u in list(red.reserve):
            if day >= u.arrival_day + st.red_delay_days:
                red.reserve.remove(u)
                red.units.append(u)
                arrived += 1
        return arrived

    def _air(self, red, st, wx, points):
        """Allocate this axis's air share; pay the airframe bill.
        Deep sorties fly into the follow-on echelon's air defense
        and cost more than close support over friendly lines."""
        p = self.params
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
        if getattr(self, "aircraft", 0.0) > 0:
            losses = close * p.get("loss_per_close_point", 0.0) + deep * p.get(
                "loss_per_deep_point", 0.0
            )
            self.aircraft = max(self.aircraft - losses, 0.0)
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
        blue_arrivals,
        air_close,
        air_deep,
        wx,
        ca,
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
                blue_arrivals=blue_arrivals,
                red_reserve_cv=round(red.reserve_cv, 1),
                air_close=round(air_close, 1),
                air_deep=round(air_deep, 1),
                wx=round(wx, 2),
                ca=ca,
            )
        )
