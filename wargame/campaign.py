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

v7 opens campaign 2 with the air command layer, grounded in
reference/air-apportionment.md: the deep/close split is a THEATER
decision (COMBALTAP at Karup), not the corps'. In
apportionment_mode="advocacy" the corps holds only a request;
each day (after advocacy_lag_days) the theater moves advocacy_rate
of the gap between its current apportionment and the corps request
— the persuasion tax as a first-order lag, the G-3's air-side
quality as a number beside v4's recognition lag. naval_claim_frac
models the standing maritime-strike claim (Op Hurricane pattern) on
the same deep-capable airframes while the amphib window is open;
the sea-state day that releases the beach watch releases the
Tornados too. apportionment_mode="direct" (default) reproduces v6
exactly.

v8 decomposes the decision grades (DK mandate 2; the hostile
review's attack 3 answered in the instrument's own language). Each
echelon now owns distinct decisions with its own quality number:
THEATER (Karup) — the apportionment (v7; advocacy_rate/lag).
CORPS (Rendsburg) — air sub-allocation between axes
(corps_air_alloc="threat": shares weighted by the red picture as it
stood corps_alloc_lag_days ago — the corps fights from a stale map)
and the corps reserve (role="corps-reserve" units, dispatched to a
collapsing axis after corps_recognition_days of standing trigger,
arriving corps_reserve_move_days later as DIVISIONAL withheld
reserve — commitment still chains through the lower echelon).
DIVISION — the local reserve/CA machinery (v4), its lag now
div_recognition_days (falls back to ca_recognition_days).
Defaults ("equal", no corps units passed) reproduce v7 exactly.

v9 makes LANDZEALAND explicit — as the THEATER'S OTHER CUSTOMER,
not a simulated front (the protagonist sees Zealand only as the
rival claim at Karup; the model does too). red_amphib chooses red's
operational posture: "none" (no threat: beach watch frees on day 1,
no naval skim, no theater caution), "threat" (the pin-in-being:
v7/v8 behavior — costs red nothing, ties blue down until sea state
closes the window), "commit" (the landing goes in on
red_commit_day: theater air surges to the straits for
zealand_battle_days at zealand_battle_claim, then the landing
resolves — zealand_landing_fails=true PLACEHOLDER pending real
sea-denial research — and a failed landing releases every pin AT
ONCE, ahead of the weather). zealand_caution couples the threat to
v7 advocacy: while the straits are credibly threatened the daily
conference grants the corps' request at a discounted rate — the
persuasion tax now has the theater's actual dilemma inside it.
Also v9: the CAL-1 parameter split (reference/consumption-factors
.md) — pause_consumption_frac (FM-anchored, what a paused red
burns) separates from pause_combat_frac (doctrine parameter, how
hard a paused front fights); both default to pause_intensity for
compatibility.

v10 makes the landing package REAL (DK ruling: option C of
reference/zealand-landing.md — units in, battle abstract). Units
with role="amphib" (specialists) / "amphib-convertible" (the
mechanized follow-on) form a red theater pool. Costs are now
commensurable: STAGED units consume red theater supply at
amphib_staged_intensity (FM inactive rate — the feint eats the
mainland offensive's supply); convertibles may be RELEASED to the
leading axis (amphib_release_convertibles_day, march delay,
arriving into staging under echelon discipline) — thinning the
package; COMMIT spends the package entirely (the units leave the
board win or lose — mainland never sees them again). Blue's
credibility c is now graded with the DOCUMENTED FE ratchet
(reference/zealand-landing.md §3): c tracks the staged fraction
fast upward, slowly downward (zeal_c_up >> zeal_c_down) — red's
thinning is not immediately believed, so a late release exploits
blue's institutional inertia. Hard evidence zeroes c outright
(sea-state close, a failed landing). Insurance (naval skim,
advocacy caution) and the beach-watch pin scale with c
(pin releases below pin_release_c). With no amphib units passed,
v9 behavior is reproduced exactly.
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
    deep_frac: float = 0.0  # v7: today's GRANTED apportionment (theater's)
    air_naval: float = 0.0  # v7: deep-capable points diverted to the fleet strike
    zeal_c: float = 0.0  # v10: blue's credibility in the landing threat


@dataclass
class Campaign:
    axes: dict
    params: dict
    seed: int = 1986
    logs: list = field(default_factory=list)
    # v8: corps reserve pool (Battalions; no axis until dispatched)
    corps_reserve: list = field(default_factory=list)
    # v10: the amphib landing package (Battalions; staged for the
    # landing threat until released, committed, or war's end)
    amphib_pool: list = field(default_factory=list)
    # v11: blue's Zealand garrison (Battalions; hold the island or
    # release to the mainland — COMBALTAP's insurance decision)
    zealand_garrison: list = field(default_factory=list)

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
        # v9: red's amphib posture decides what the sea-state clock
        # means. The pin releases at: day 1 (no threat), the
        # sea-state day (threat-in-being), or the landing's failure
        # day if that comes sooner (a spent threat pins nobody).
        amp = p.get("red_amphib", "threat")
        commit_day = int(p.get("red_commit_day", 0))
        self.zealand_resolve_day = None
        # v11: landing outcome and pin-release are now settled by
        # _commit_landing (outcome conditional on the garrison blue
        # actually kept, when garrison units are modeled); commit can
        # also arrive dynamically (red_amphib="opportunist" punishes
        # a garrison release). Static "commit" keeps its schedule.
        self._commit_day = None
        self._zealand_committed = False
        self._landing_fails = p.get("zealand_landing_fails", True)
        self.zealand_lost = False
        if amp == "none":
            self.pin_release_day = 1
        else:
            self.pin_release_day = self.amphib_release_day
        self._scheduled_commit = (
            commit_day
            if (
                amp == "commit"
                and self.amphib_release_day
                and commit_day >= 1
                and commit_day < self.amphib_release_day
            )
            else None
        )
        # v11: Zealand garrison state — blue's half of the ledger.
        self._zg_full_cv = sum(u.effective_cv for u in self.zealand_garrison) or None
        self._zg_released_day = None
        self._zg_standing = 0  # threshold-mode recognition counter
        # v10: amphib package state. "none" means the package never
        # formed: convertibles go straight to the mainland battle
        # (transit from day 1), specialists sit out (coastal duty).
        self._amphib_full_cv = sum(u.effective_cv for u in self.amphib_pool) or None
        self._amphib_transit = []  # (arrive_day, battalion)
        self._amphib_released = False
        if amp == "none" and self.amphib_pool:
            self._release_convertibles(1)
            self.amphib_pool = [
                u for u in self.amphib_pool if u.role != "amphib"
            ]  # specialists withdrawn from play
        # Blue's credibility in the landing threat (the G-2 estimate;
        # graded, ratcheted). Starts at the staged picture.
        self.zeal_c = self._amphib_target(1)
        # v7: the apportionment is theater state, not a blue knob.
        # "direct" reproduces v6 (deep_fraction used as-is);
        # "advocacy" starts at the theater's own prior and moves
        # toward the corps request only as fast as the daily
        # conference grants it.
        mode = p.get("apportionment_mode", "direct")
        if mode == "advocacy":
            self.deep_frac_today = p.get(
                "theater_deep_fraction", p.get("deep_fraction", 0.0)
            )
        else:
            self.deep_frac_today = p.get("deep_fraction", 0.0)
        self.naval_frac_today = 0.0
        state = {}
        for name, ax in self.axes.items():
            spec = ax["spec"]
            state[name] = AxisState(
                name=name,
                length_km=spec["length_km"],
                hold_km=spec.get("hold_km", spec["length_km"]),
            )
        # v8 corps state: threat-picture history (for the stale-map
        # air allocation), per-axis emergency-standing counters, and
        # dispatched-but-in-transit reserve units.
        self._threat_history = []
        self._corps_standing = dict.fromkeys(state, 0)
        self._in_transit = []  # (arrive_day, axis_name, battalion)
        for day in range(1, days + 1):
            wx = self._weather(rng)  # theater-wide, one draw per day
            # v10: the amphib package moves (releases arrive, commit
            # spends), then blue's graded credibility updates, then
            # the theater's insurance follows the credibility.
            self._amphib_step(day)
            self._zealand_garrison_step(day, state)
            c, skim = self._zealand_state(day)
            if mode == "advocacy" and day > p.get("advocacy_lag_days", 0):
                req = p.get("corps_request_deep", self.deep_frac_today)
                gap = req - self.deep_frac_today
                rate = p.get("advocacy_rate", 0.0)
                # The conference grants the corps' argument slower in
                # proportion to how credible the straits threat
                # stands — the persuasion tax with the theater's
                # real dilemma inside it.
                rate *= 1.0 - p.get("zealand_caution", 0.0) * c
                self.deep_frac_today = min(
                    max(self.deep_frac_today + rate * gap, 0.0), 1.0
                )
            self.naval_frac_today = skim
            # v10: the staged package eats red theater supply at the
            # FM inactive rate — the feint is a logistics customer.
            staged_cv = sum(u.effective_cv for u in self.amphib_pool)
            drain = (
                staged_cv
                * p.get("red_demand_per_cv", 0.0)
                * p.get("amphib_staged_intensity", 0.41)
            )
            self._red_supply_today = max(p.get("red_supply_points", 0.0) - drain, 0.0)
            live = [n for n, st in state.items() if not st.fallen]
            if self.aircraft > 0:
                points_today = self.aircraft * p["sorties_per_aircraft"] * wx
            else:
                points_today = p.get("blue_air_points", 0.0) * wx
            shares = self._corps_air_shares(points_today, live)
            self._corps_reserve_step(day, state)
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
                    day,
                    ax,
                    st,
                    wx,
                    shares.get(name, 0.0),
                    red_arrivals.get(name, 0),
                    len(live),
                )
        return state

    # -- theater grade (v9/v10) ----------------------------------------

    def _release_convertibles(self, day):
        """Send the convertible (mechanized) part of the package to
        the mainland: march delay, then into the leading axis's
        staging area (echelon discipline governs commitment)."""
        march = int(self.params.get("amphib_release_march_days", 3))
        for u in [x for x in self.amphib_pool if x.role == "amphib-convertible"]:
            self.amphib_pool.remove(u)
            self._amphib_transit.append((day + march, u))
        self._amphib_released = True

    def _commit_landing(self, day):
        """The landing goes in (v11). Outcome: when blue's garrison
        is modeled, success is decided by the correlation the
        research documents (reference/zealand-landing.md §1 — the
        full garrison defeats the package; a stripped one does
        not): success iff package CV at commit > zg_success_ratio x
        the garrison blue actually kept. Without garrison units the
        zealand_landing_fails param decides (v10 compat). The
        package leaves the mainland war either way."""
        p = self.params
        self._zealand_committed = True
        self._commit_day = day
        self.zealand_resolve_day = day + int(p.get("zealand_battle_days", 0))
        # v12: after the sea closes, only the AIRBORNE component can
        # be delivered — an air-only descent, hopeless against a
        # garrison, decisive against an emptied island.
        sea_open = self.amphib_release_day and day < self.amphib_release_day
        if sea_open:
            striking = list(self.amphib_pool)
        else:
            striking = [u for u in self.amphib_pool if u.role == "amphib-air"]
        package_cv = sum(u.effective_cv for u in striking)
        if self._zg_full_cv:
            # Guns can't hold ground on Zealand either: only the
            # kept garrison's maneuver CV counts against a descent.
            kept = sum(
                u.effective_cv for u in self.zealand_garrison if u.kind != "arty"
            )
            self._landing_fails = package_cv <= p.get("zg_success_ratio", 1.5) * kept
        else:
            self._landing_fails = p.get("zealand_landing_fails", True)
        self.zealand_lost = not self._landing_fails
        if self._landing_fails:
            self.pin_release_day = min(
                self.amphib_release_day or self.zealand_resolve_day,
                self.zealand_resolve_day,
            )
        else:
            self.pin_release_day = None  # Zealand falls: pinned for good
        for u in striking:  # embarked/emplaned: gone from the mainland war
            self.amphib_pool.remove(u)

    def _zealand_garrison_step(self, day, state):
        """COMBALTAP's insurance decision, executed (v11): release
        the garrison to the mainland per zg_release_mode ("never" /
        "day" / "threshold" — credibility low for long enough).
        Released units cross the Belt into the weakest axis's
        reserve queue, so red's interdiction of mobilization applies
        to the crossing. An opportunist red punishes: it commits
        red_opportunist_lag days after observing the release, sea
        window permitting."""
        p = self.params
        mode = p.get("zg_release_mode", "never")
        if self.zealand_garrison and self._zg_released_day is None:
            trigger = False
            if mode == "day" and day >= int(p.get("zg_release_day", 10_000)):
                trigger = True
            elif mode == "threshold":
                if self.zeal_c < p.get("zg_release_c", 0.0):
                    self._zg_standing += 1
                else:
                    self._zg_standing = 0
                trigger = self._zg_standing > p.get("zg_release_recognition_days", 0)
            if trigger:
                self._zg_released_day = day
                move = int(p.get("zg_move_days", 3))
                live = [n for n, st in state.items() if not st.fallen] or list(state)
                target = min(live, key=lambda n: self.axes[n]["blue"].cv)
                # v12: partial release — send the strongest N and
                # keep the rest as the island's residual insurance
                # (0 = release everything, the v11 behavior).
                count = int(p.get("zg_release_count", 0)) or len(self.zealand_garrison)
                units = sorted(self.zealand_garrison, key=lambda u: -u.effective_cv)[
                    :count
                ]
                for u in units:
                    self.zealand_garrison.remove(u)
                    u.arrival_day = day + move
                    self.axes[target]["blue"].reserve.append(u)
        if (
            p.get("red_amphib", "threat") == "opportunist"
            and self._zg_released_day is not None
            and not self._zealand_committed
            and self.amphib_pool
        ):
            strike = self._zg_released_day + int(p.get("red_opportunist_lag", 2))
            # v12: the opportunist stays armed after the sea closes —
            # the airborne component's delivery is windowless. It
            # strikes only when the strike would SUCCEED (it can see
            # the ferries; it can count the garrison it faces).
            if day >= strike and self.amphib_release_day:
                sea_open = day < self.amphib_release_day
                striking = (
                    self.amphib_pool
                    if sea_open
                    else [u for u in self.amphib_pool if u.role == "amphib-air"]
                )
                pkg = sum(u.effective_cv for u in striking)
                kept = sum(
                    u.effective_cv for u in self.zealand_garrison if u.kind != "arty"
                )
                viable = (
                    pkg > self.params.get("zg_success_ratio", 1.5) * kept
                    if self._zg_full_cv
                    else sea_open
                )
                if viable:
                    self._commit_landing(day)

    def _amphib_step(self, day):
        """Daily package bookkeeping: scheduled release of the
        convertibles; the static commit schedule; transit arrivals
        join the leading axis."""
        p = self.params
        rel = int(p.get("amphib_release_convertibles_day", 0))
        if rel and day >= rel and not self._amphib_released:
            self._release_convertibles(day)
        if (
            self._scheduled_commit
            and day >= self._scheduled_commit
            and not self._zealand_committed
        ):
            self._commit_landing(day)
        for arrive, u in list(self._amphib_transit):
            if day >= arrive:
                self._amphib_transit.remove((arrive, u))
                live = [
                    n for n, ax in self.axes.items() if ax["blue"].has_maneuver
                ] or list(self.axes)
                target = max(
                    live,
                    key=lambda n: (
                        self.axes[n]["red"].cv + self.axes[n]["red"].staging_cv
                    ),
                )
                self.axes[target]["red"].staging.append(u)

    def _amphib_target(self, day):
        """What the indicator picture supports today. v12 decomposes
        the threat: the SEALIFT component's credibility closes with
        the sea window; the AIRBORNE component's does not (the FE
        worry that outlived the fleet threat). Target = (staged air
        CV + staged sealift CV x window) / full package. Observed
        invasion is 1.0; no-threat and a failed landing are 0.0.
        Without a modeled package: v9's binary threat (sea close
        zeroes everything — legacy)."""
        p = self.params
        amp = p.get("red_amphib", "threat")
        if amp == "none" or not self.amphib_release_day:
            return 0.0
        if self._zealand_committed:
            if day >= self.zealand_resolve_day:
                return 0.0 if self._landing_fails else 1.0
            if day >= self._commit_day:
                return 1.0  # the invasion is observed fact
        window = 1.0 if day < self.amphib_release_day else 0.0
        if self._amphib_full_cv:
            air = sum(
                u.effective_cv for u in self.amphib_pool if u.role == "amphib-air"
            )
            sea = sum(
                u.effective_cv for u in self.amphib_pool if u.role != "amphib-air"
            )
            return (air + sea * window) / self._amphib_full_cv
        return window  # no package modeled: v9's binary threat

    def _zealand_state(self, day):
        """(credibility, skim). Blue's G-2 estimate of the landing
        threat follows the indicator picture through the DOCUMENTED
        FE ratchet (reference/zealand-landing.md §3): fast up, slow
        down — force-structure reassurance (a thinning package) is
        absorbed reluctantly, hard evidence (a failed landing, the
        invasion itself; and, package unmodeled, the sea close) is
        believed at once. v12: with the package modeled, the sea
        close is NOT a hard zero — the target drops to the airborne
        floor and blue's slow ratchet takes days to follow it."""
        p = self.params
        target = self._amphib_target(day)
        amp = p.get("red_amphib", "threat")
        hard = (
            amp == "none"
            or (self._zealand_committed and day >= self._commit_day)
            or (
                self._amphib_full_cv is None
                and self.amphib_release_day
                and day >= self.amphib_release_day
            )
        )
        if hard:
            self.zeal_c = target
        else:
            rate = (
                p.get("zeal_c_up", 0.5)
                if target > self.zeal_c
                else p.get("zeal_c_down", 0.05)
            )
            self.zeal_c = min(
                max(self.zeal_c + rate * (target - self.zeal_c), 0.0), 1.0
            )
        base = p.get("naval_claim_frac", 0.0)
        in_battle = (
            self._zealand_committed
            and self._commit_day <= day < self.zealand_resolve_day
        )
        if (
            not in_battle
            and self._zealand_committed
            and day >= self.zealand_resolve_day
        ):
            if not self._landing_fails:
                in_battle = True  # the straits fight persists
        skim = self.zeal_c * (
            p.get("zealand_battle_claim", base) if in_battle else base
        )
        return self.zeal_c, skim

    # -- corps grade (v8) ----------------------------------------------

    def _corps_air_shares(self, points_today, live):
        """Corps sub-allocation of the theater's air between axes —
        the lever the research says the G-3 actually holds
        (reference/air-apportionment.md). "equal" reproduces the
        pre-v8 split. "threat" weights by red combat power per axis,
        but through the picture as it stood corps_alloc_lag_days
        ago: the corps allocates against a stale map, and its
        staleness is a quality number."""
        p = self.params
        if not live:
            return {}
        threat = {
            n: self.axes[n]["red"].cv + self.axes[n]["red"].staging_cv for n in live
        }
        self._threat_history.append(threat)
        if p.get("corps_air_alloc", "equal") != "threat":
            return dict.fromkeys(live, points_today / len(live))
        lag = int(p.get("corps_alloc_lag_days", 0))
        idx = max(len(self._threat_history) - 1 - lag, 0)
        pic = self._threat_history[idx]
        # Fallen-axis weights vanish; a picture with no live weight
        # degenerates to the equal split.
        weights = {n: max(pic.get(n, 0.0), 0.0) for n in live}
        total = sum(weights.values())
        if total <= 0:
            return dict.fromkeys(live, points_today / len(live))
        return {n: points_today * w / total for n, w in weights.items()}

    def _corps_reserve_step(self, day, state):
        """Corps reserve: dispatched to an axis whose line has stood
        below the trigger for corps_recognition_days, arriving
        corps_reserve_move_days later as DIVISIONAL withheld reserve
        (the division still decides commitment — echelons chain)."""
        p = self.params
        for arrive, name, bn in list(self._in_transit):
            if day >= arrive and not state[name].fallen:
                self.axes[name]["blue"].withheld.append(bn)
                self._in_transit.remove((arrive, name, bn))
        if not self.corps_reserve:
            return
        trigger = p.get("corps_dispatch_cv", 0.0)
        if trigger <= 0:
            return
        for name, st in state.items():
            if st.fallen:
                self._corps_standing[name] = 0
                continue
            if self.axes[name]["blue"].cv < trigger:
                self._corps_standing[name] += 1
            else:
                self._corps_standing[name] = 0
            if (
                self._corps_standing[name] > p.get("corps_recognition_days", 0)
                and self.corps_reserve
            ):
                bn = max(self.corps_reserve, key=lambda u: u.effective_cv)
                self.corps_reserve.remove(bn)
                self._in_transit.append(
                    (day + int(p.get("corps_reserve_move_days", 1)), name, bn)
                )
                self._corps_standing[name] = 0

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
                # THREAT releases them — sea state, a landing's
                # failure, or its absence (v9 pin_release_day).
                if (self.pin_release_day and day >= self.pin_release_day) or (
                    self.zeal_c < p.get("pin_release_c", 0.0)
                ):
                    blue.reserve.remove(u)
                    blue.units.append(u)
                    blue_arrivals += 1
            elif day >= u.arrival_day + st.blue_delay_days:
                blue.reserve.remove(u)
                blue.units.append(u)
                blue_arrivals += 1
        air_close, air_deep, air_naval = self._air(red, st, wx, air_share)
        self._naval_log = air_naval  # picked up by _log for this axis-day

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
            # v10: theater supply net of the staged amphib package's
            # draw (set daily in run; falls back to the raw param).
            supply = getattr(self, "_red_supply_today", p["red_supply_points"])
            cap = (supply / n_live) * max(stretch, 0.0)
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
            # A paused front consumes at pause-consumption intensity
            # (patrols and fires), which is what lets the stockpile
            # actually build. v9 CAL-1 split: the consumption face is
            # FM-anchorable (inactive situation ≈ 0.41 of defense-
            # day-1); the combat face below is a doctrine parameter.
            demand_today = demand * (
                p.get("pause_consumption_frac", p.get("pause_intensity", 0.25))
                if st.red_paused
                else 1.0
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
        # v8: the local reserve/CA decision is DIVISION grade; its
        # recognition lag is the division's quality number
        # (div_recognition_days; falls back to the pre-v8 name).
        div_lag = p.get("div_recognition_days", p.get("ca_recognition_days", 0))
        ca_today = (
            p.get("ca_enabled", True)
            and window
            and can_mass
            and st.window_days > div_lag
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
            # v9 CAL-1 split: this is the COMBAT face of the pause.
            scale *= p.get("pause_combat_frac", p.get("pause_intensity", 0.25))
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
        and cost more than close support over friendly lines.
        v7: the deep fraction is the THEATER's granted apportionment
        (self.deep_frac_today), and the maritime-strike claim skims
        the deep-capable share first — those sorties fly against the
        invasion fleet, pay the deep airframe price, and give the
        land battle nothing."""
        p = self.params
        deep = points * self.deep_frac_today
        naval = deep * self.naval_frac_today
        deep -= naval
        close = points - deep - naval
        if deep > 0 and red.reserve:
            red.attrit_reserve(deep * p["deep_attrition_per_point"])
            st.red_delay_days += min(
                deep * p["deep_delay_per_point"], p["deep_delay_cap_dpd"]
            )
        else:
            # No echelon left to interdict: land-deep effort reverts
            # to close support (the naval claim does not — the fleet
            # is still there).
            close += deep
            deep = 0.0
        if getattr(self, "aircraft", 0.0) > 0:
            losses = close * p.get("loss_per_close_point", 0.0) + (
                deep + naval
            ) * p.get("loss_per_deep_point", 0.0)
            self.aircraft = max(self.aircraft - losses, 0.0)
        return close, deep, naval

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
                deep_frac=round(getattr(self, "deep_frac_today", 0.0), 3),
                air_naval=round(getattr(self, "_naval_log", 0.0), 1),
                zeal_c=round(getattr(self, "zeal_c", 0.0), 2),
            )
        )
