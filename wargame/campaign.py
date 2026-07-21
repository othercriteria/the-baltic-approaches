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

v4 adds the command-decision layer: withheld tactical reserves
(massing gates the counterattack; emergency commit guards collapse),
recognition lag (the G-3's quality as a number), theater-level red
arrivals with reinforce-success, and the amphib pin via arrival-day
release.

v5 adds the logistics layer: supply throughput scales combat output
(red's fill falls as its LOC stretches — culmination as supply);
red whole-echelon commitment via staging; counterattack culmination;
seeded sea-state closure of the amphib window.

v6 adds the pulsed offensive (red operational pauses with stockpile
hysteresis), deep-target choice (echelon vs throughput), pursuit
into a starved enemy, and the OOB-ledger export (wargame/ledger.py).
Campaign 1 closes here; notes/wargaming-findings.md carries the
claim ledger and handoff.
"""

import math
import random
from dataclasses import dataclass, field

from .models import epstein


@dataclass
class AxisState:
    name: str
    length_km: float
    hold_km: float  # withdrawal may not take the FEBA past this
    feba_km: float = 0.0
    red_delay_days: float = 0.0  # accumulated blue-interdiction delay
    blue_delay_days: float = 0.0  # accumulated red-interdiction delay
    window_days: int = 0  # consecutive days the CA window has stood open
    ca_committed: bool = False  # reserve already committed to the attack
    ca_run_days: int = 0  # consecutive CA days this run (culmination clock)
    stage_since: int | None = None  # day red's staging area last went occupied
    red_paused: bool = False  # operational pause: building supply forward
    red_stockpile: float = 0.0  # supply accumulated during pauses
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
    commit: int = 0  # withheld-reserve units committed today (CA or emergency)
    bfill: float = 1.0  # blue supply fulfillment (effectiveness input)
    rfill: float = 1.0  # red supply fulfillment (falls as its LOC stretches)
    pause: bool = False  # red operational pause (building supply forward)


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
        # Sea state: the WP landing window closes for the season on a
        # drawn day (November climatology PLACEHOLDER); beach-watch
        # units release to their axes that day.
        self.amphib_release_day = (
            rng.randint(
                int(p.get("amphib_close_min", 0)), int(p.get("amphib_close_max", 0))
            )
            if p.get("amphib_close_max", 0)
            else None
        )
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
            red_arrivals = self._red_arrivals(day, state)
            for name, ax in self.axes.items():
                st = state[name]
                if st.fallen:
                    continue
                spec = ax["spec"]
                release = spec.get("hold_release_day")
                if release and day >= release:
                    st.hold_km = st.length_km
                self._axis_day(
                    day, ax, st, wx, share, red_arrivals.get(name, 0), len(live)
                )
        return state

    def _red_arrivals(self, day, state):
        """Theater-level red echelon arrivals. Units arrive into the
        target axis's STAGING area and commit to the line only as a
        mass (whole-echelon discipline: >= red_commit_min_cv, or
        after red_commit_max_wait days) — the v4 finding was that
        piecemeal commitment is suicide, and red knows it too. With
        red_reinforces_success, arrivals stage on the most
        successful live axis."""
        p = self.params
        counts = {}
        reinforce = p.get("red_reinforces_success", False)
        live = [n for n, st in state.items() if not st.fallen]
        for name, ax in self.axes.items():
            st = state[name]
            red = ax["red"]
            for u in list(red.reserve):
                if day >= u.arrival_day + st.red_delay_days:
                    red.reserve.remove(u)
                    target = name
                    if reinforce and live:
                        target = max(
                            live,
                            key=lambda n: state[n].feba_km / state[n].length_km,
                        )
                    self.axes[target]["red"].staging.append(u)
                    if state[target].stage_since is None:
                        state[target].stage_since = day
        # Commitment pass: mass or timeout.
        min_cv = p.get("red_commit_min_cv", 0.0)
        max_wait = p.get("red_commit_max_wait", 0)
        for name, ax in self.axes.items():
            st = state[name]
            red = ax["red"]
            if not red.staging:
                st.stage_since = None
                continue
            waited = day - st.stage_since if st.stage_since is not None else 0
            no_more_coming = not red.reserve
            if (
                red.staging_cv >= min_cv
                or waited >= max_wait
                or (no_more_coming and red.staging)
            ):
                counts[name] = counts.get(name, 0) + red.commit_staging()
                st.stage_since = None
        return counts

    # -- one axis-day ------------------------------------------------

    def _axis_day(self, day, ax, st, wx, air_share, arrivals, n_live):
        red, blue = ax["red"], ax["blue"]
        p = self.params

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
            if u.role == "beach-watch":
                # Already in theater, pinned watching the coast; the
                # sea state, not the rail net, releases them.
                if self.amphib_release_day and day >= self.amphib_release_day:
                    blue.reserve.remove(u)
                    blue.units.append(u)
                    blue_arrivals += 1
            elif day >= u.arrival_day + st.blue_delay_days:
                blue.reserve.remove(u)
                blue.units.append(u)
                blue_arrivals += 1
        air_close, air_deep = self._air(red, st, wx, air_share)

        # Supply fulfillment: throughput is the constraint. Blue
        # draws on short interior lines (flat theater capacity); red
        # pays for every kilometer gained — its axis throughput
        # falls as the LOC stretches (culmination as a supply
        # phenomenon). Fulfillment scales combat OUTPUT, not
        # resilience, through an effectiveness floor.
        bfill, rfill = 1.0, 1.0
        floor = p.get("supply_floor", 1.0)
        if p.get("blue_supply_points", 0.0) > 0:
            cap = p["blue_supply_points"] / n_live
            demand = p["blue_demand_per_cv"] * max(blue.cv, 1e-9)
            bfill = min(1.0, cap / demand) if demand > 0 else 1.0
        if p.get("red_supply_points", 0.0) > 0:
            stretch = 1.0 - p.get("red_loc_penalty", 0.0) * (st.feba_km / st.length_km)
            cap = (p["red_supply_points"] / n_live) * max(stretch, 0.0)
            # Deep fires against THROUGHPUT (deep_target="throughput"):
            # today's flow interrupted instead of the echelon delayed.
            if air_deep > 0 and p.get("deep_target", "echelon") == "throughput":
                cap = max(cap - air_deep * p.get("deep_supply_per_point", 0.0), 0.0)
            demand = p["red_demand_per_cv"] * max(red.cv, 1e-9)
            # Operational pause with hysteresis: a starved red stops
            # to build supply forward (the pulsed offensive) instead
            # of grinding at the floor; it resumes on a stockpile.
            flow_fill = cap / demand if demand > 0 else 1.0
            if st.red_paused:
                st.red_stockpile += p.get("red_pause_buildup", 0.0)
                if (cap + st.red_stockpile) / max(demand, 1e-9) >= p.get(
                    "red_resume_fill", 1.0
                ):
                    st.red_paused = False
            elif flow_fill < p.get("red_pause_fill", 0.0) and st.red_stockpile <= 0:
                st.red_paused = True
            # A paused front consumes at pause intensity (patrols and
            # fires), which is what lets the stockpile actually build.
            demand_today = demand * (
                p.get("pause_intensity", 0.25) if st.red_paused else 1.0
            )
            use = min(demand_today, cap + st.red_stockpile)
            st.red_stockpile = max(st.red_stockpile - max(use - cap, 0.0), 0.0)
            rfill = min(1.0, use / demand_today) if demand_today > 0 else 1.0
        b_eff = floor + (1.0 - floor) * bfill
        r_eff = floor + (1.0 - floor) * rfill

        r_cv, b_cv = red.cv, blue.cv
        committed = 0

        # Emergency commit: the line is about to break and a reserve
        # exists — protective capacity spent to avoid collapse.
        if b_cv <= p.get("emergency_commit_cv", 0.0) and blue.withheld:
            committed += blue.commit_withheld()
            b_cv = blue.cv

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
                commit=committed,
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
                commit=committed,
            )
            return

        # Counterattack window: evaluated against MASSED strength
        # (line + withheld reserve) at dawn. Recognition lag models
        # the G-3: the window must stand open for more than
        # ca_recognition_days before the command acts on it. Who
        # notices the window, and how fast, is the book.
        window = self._window_open(day, red, b_cv + blue.withheld_cv, st)
        st.window_days = st.window_days + 1 if window else 0
        can_mass = (
            blue.withheld_cv >= p.get("ca_min_reserve_cv", 0.0) or st.ca_committed
        )
        if not window:
            st.ca_run_days = 0  # window closed: culmination clock resets
        ca_today = (
            p.get("ca_enabled", True)
            and window
            and can_mass
            and st.window_days > p.get("ca_recognition_days", 0)
            and st.ca_run_days < p.get("ca_culminate_days", 10_000)
        )
        if ca_today and blue.withheld:
            committed += blue.commit_withheld()
            st.ca_committed = True
            b_cv = blue.cv

        # Close support fights today without absorbing ground losses;
        # saturating (diminishing returns beyond what the engaged
        # force can absorb/direct).
        sat = p.get("close_sat_cv", 0.0)
        raw = air_close * p["close_support_cv_per_point"]
        cs_cv = sat * (1.0 - math.exp(-raw / sat)) if sat > 0 else raw
        b_cv_eff = b_cv + cs_cv

        # Projected full-contact engagement (the G3's decision
        # input). Square-law daily fire with supply-scaled OUTPUT:
        # each side's losses come from the other's effective fire
        # (lanchester.square_step's Euler step, unrolled so the
        # shooters can be efficiency-scaled).
        red_loss = min(p["beta"] * b_cv_eff * b_eff, r_cv)
        blue_loss = min(p["alpha"] * r_cv * r_eff, b_cv)
        proj_blue_frac = blue_loss / b_cv

        # Attacking means accepting more risk than defending — but
        # not annihilation-level risk. (A cancelled CA still keeps
        # its committed reserve in the line, defensively.)
        if ca_today and proj_blue_frac > p["blue_tolerance"] * p.get(
            "ca_proj_mult", 2.5
        ):
            ca_today = False

        if ca_today:
            # Counterattack: full contact, no withdrawal; the spent
            # echelon pays a cohesion premium, blue pays the
            # attacker's price; FEBA moves back. Culmination: a run
            # of CA days exhausts itself (supply, fatigue) until the
            # window closes and reopens.
            st.ca_run_days += 1
            red_loss *= p["ca_exploit"]
            blue_loss *= p["ca_blue_cost"]
            red.distribute_losses(red_loss)
            blue.distribute_losses(blue_loss)
            gain = p["ca_kmd"]
            if rfill < p.get("ca_pursuit_fill", 0.0):
                gain *= p.get("ca_pursuit_mult", 1.0)  # pursuit
            gain = min(gain, st.feba_km)
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
                commit=committed,
                bfill=bfill,
                rfill=rfill,
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
        if st.red_paused:
            # Quiet front: patrols and fires only, while red builds
            # supply. Blue may still counterattack into a pause (the
            # CA path above bypasses this scaling deliberately).
            scale *= p.get("pause_intensity", 0.25)
        red_loss *= scale
        blue_loss *= scale
        red.distribute_losses(red_loss)
        blue.distribute_losses(blue_loss)

        ratio = red.cv / max(blue.cv, 1e-9)
        if st.red_paused:
            adv = 0.0  # a paused red does not follow up withdrawals
        else:
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
            commit=committed,
            bfill=bfill,
            rfill=rfill,
            pause=st.red_paused,
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

    def _window_open(self, day, red, blue_massed_cv, st):
        """Is the counterattack window open at dawn? Red's in-contact
        echelon spent relative to blue's MASSED strength, the
        follow-on echelon at least ca_window_days away, and ground
        to retake. (Risk and recognition are judged separately.)"""
        p = self.params
        if st.feba_km <= 0:
            return False
        if red.cv / max(blue_massed_cv, 1e-9) >= p["ca_at_ratio"]:
            return False
        if red.reserve:
            gap = min(u.arrival_day + st.red_delay_days - day for u in red.reserve)
            if gap < p["ca_window_days"]:
                return False
        return True

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
        commit=0,
        bfill=1.0,
        rfill=1.0,
        pause=False,
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
                commit=commit,
                bfill=round(bfill, 2),
                rfill=round(rfill, 2),
                pause=pause,
            )
        )
