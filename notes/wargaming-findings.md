# Wargaming findings log

Running log, newest at top within each session block. The instrument's
version of imagegen/findings.md from white-buffalo: what the builds
and runs taught, what they broke, what research they forced.

## 2026-07-21 — calibration pass opens (session 71ede904; research, no mechanics)

FM 101-10-1 consumption extraction done →
reference/consumption-factors.md (division Class V by posture, the
intensity ladder, theater per-capita, Soviet unit-of-fire/refill
frame, deltas CAL-1..4). Per the campaign-1 handoff this is
research-before-model; no instrument code changed.

**CAL-1 sensitivity run** (scratch/cal1-pause-intensity.py; n=40,
30 days, pause_intensity 0.25 vs FM-derived 0.41): at deep=1.0 the
v6 conclusions are insensitive (held 1.00/1.00, blue CV 36.6/35.9);
at deep=0.0 the calibrated pause makes the pulsed red HARDER (held
0.65→0.23, blue CV 11.1→5.3). **v6's "deep re-dominates vs the
pulsed red" strengthens under calibration** — the first v6 claim to
face new data and survive it, with margin. Mechanism note: the gain
to red comes through the parameter's *contact-intensity* face
(a 0.41-intensity pause still grinds blue), not its consumption
face; `pause_intensity` conflates the two, and the FM calibrates
only consumption. Queued for campaign 2: split into
pause_consumption_frac (≈0.41, FM-anchored) and pause_combat_frac
(doctrine parameter, likely lower) — until then the pulsed red at
0.25 is the *conservative* setting for blue-favorable claims.

Also confirmed at 30 days (past the 24-day horizon artifact):
throughput-targeting still forces more pauses than
echelon-targeting at deep=1.0 (17.0 vs 11.7 pause days) — v6
finding 3 survives the longer horizon.

Mechanics: **red operational pauses** (a starved red stops, drops to
patrol-intensity consumption, builds a stockpile forward, resumes on
a full tank — the pulsed offensive, with hysteresis); **deep-target
choice** (blue's deep fires attack either arrival schedules or
supply flow); **pursuit** (counterattacks into a starved red bite
2x); **the OOB ledger bridge** (wargame/ledger.py renders any run
into the ledger format — game state and the manuscript's continuity
bookkeeping now share one spine; example committed under
wargame/examples/; regenerate, don't hand-edit). 35 tests green.

**Finding 1: the grinding red was flattering blue enormously.**
Against the pulsed red under all-close support, blue ends at 20.8
CV instead of 55.4 — an honest red that fights only at full supply
hits nearly three times harder over the campaign. The 24-day
"theater holds 30/30" under pulses is a horizon artifact: the
pulsed campaign is a longer war entered with a worn-out defense and
a 168-CV red poised on a stockpile. Every prior blue-favorable
number deserves a mental haircut for this.

**Finding 2: v5's ground-vs-force bifurcation was itself
conditional on the dishonest red.** Against the pulsed red, deep
re-dominates BOTH criteria (final sweep: 99% axes-held dominance,
71% strictly better, blue CV 49.3 vs 42.9). Fourth consecutive
iteration to revise a certified claim, which is now the point:

> **The policy ranking is hostage to the enemy model.** Deep vs
> close flipped or bifurcated at v3 (red counter-interdiction), v5
> (red grinding at the supply floor), and v6 (red pulsing) — same
> blue, same theater, different theory of the enemy. You cannot
> rank your own policies without a theory of the enemy's
> operational method: the G-2 question precedes the G-3 question.
> The instrument's two staged questions are now the book's two
> hinges — *what is the goal?* and *what does the enemy think the
> goal is?* Any chapter where the staff argues policy is secretly
> arguing enemy models, and the book can stage that with receipts.

**Finding 3: throughput-targeting edges echelon-targeting** against
the pulsed red (FEBA 125 vs 131, blue CV 46.7 vs 39.3) and works by
FORCING pauses (15.4 vs 10.0 pause days) — tempo denial made
mechanical. Attacking the enemy's supply flow doesn't destroy him;
it makes him fight on your clock instead of his.

**Claim ledger at campaign close (survival across 6 iterations +
final n=150 sweep):**

| Claim | Status |
|---|---|
| Interdiction dominance (axes held) | SURVIVED every iteration; 99% final |
| Monotone in deep fraction | survived; 99% final |
| All-deep strictly better | criterion- and enemy-model-dependent (71% vs pulsed red); report conditionally, never flatly |
| CA requires deep | dead (v4); 52% final — window also opens by massing and red starvation |
| Split is worst | dead (v2); 33% final |
| Counterstroke window is contested/fragile | survived v3-v6 in varying forms |
| Guns can't hold ground | closure guard, tested |

**Campaign 1 handoff (research before model):**
- FM 101-10-1 consumption-factor extraction → real demand_per_cv
- OOB verification: Davies vs official sources; GDR 5th Army/Polish
  axis from PHP/CWIHP; mobilization timelines (the covering-force
  clock in real days)
- November Baltic climatology (weather + sea-state distributions)
- Parked model work: longer horizons for pulsed campaigns; red axis
  reallocation during pauses; red fires against blue supply (not
  just mobilization); LANDZEALAND as a real axis; QJM advance rates
  when NP&W lands in holdings

**Process verdict on the six iterations:** the instrument's chief
products are (1) a mechanism inventory that composes honestly, (2)
calibrated humility — every confident conclusion died or
conditionalized within one iteration, while every *mechanism*
survived, exactly the epistemics the book's staff should live; and
(3) the two staged questions above. The numbers were never the
point; the shape of how the numbers betray you is the point.

## 2026-07-21 — v5 (logistics layer, culmination, red discipline, sea state)

Mechanics: **supply throughput as the constraint** — blue draws on
short interior lines (flat theater capacity); red pays for every
kilometer gained, its axis throughput falling as the LOC stretches
(culmination as a supply phenomenon); fulfillment scales combat
OUTPUT through an effectiveness floor. Red whole-echelon commitment
discipline (the v4 piecemeal finding handed to red as doctrine:
mass ≥ red_commit_min_cv or timeout — arrivals now land in
staging and commit in bursts). Counterattack culmination (a CA run
exhausts itself after ca_culminate_days until the window closes and
reopens). Sea state: the amphib window now closes on a seeded drawn
day, releasing the beach watch. 31 tests green. FM 101-10-1 (on the
shelf) is flagged as the calibration bench for real consumption
factors — demand_per_cv is where its planning data plugs in.

**Headline: the logistics layer forced the Goldratt question into
the policy space.** At default parameters, all-close now beats
all-deep on force preserved (55.4 vs 48.3 blue CV) — because red's
own LOC stretch does interdiction's job for free (red fill bottoms
at ~0.17: the theater's geometry starves the attacker without a
single deep sortie). But the sweep (n=150, supply params perturbed
too) shows deep=1.0 is the ONLY policy that ever holds the whole
theater (41/150 vs 0/150 for all-close), and axes-held dominance
survives at 100%/94% monotone. So the certified v3 claim did not
invert — it BIFURCATED by criterion:

> **Deep buys ground; close buys the force.** Which policy is
> "better" now depends on what the commander is maximizing —
> terrain integrity or force preservation — and the model cannot
> answer that, because it is not a modeling question. It is the
> book's title question: *what is the goal?* The instrument has
> reproduced The Goal's central move — the metrics argument
> dissolves into a purpose argument — from supply arithmetic alone.

Claim ledger after v5's sweep: interdiction dominance on axes held
100% (survives all five iterations); monotone 94%; all-deep
strictly better 41% (criterion-dependent, correctly so);
CA-needs-deep 3% (dead, stays dead — massing + a supply-starved
red opens windows everywhere); split-worst 23% (dead, stays dead).

**Also confirmed in-model:** red commitment now arrives in echelon
bursts (max burst ≥3 bns, tested); CA runs bounded by culmination
(tested); the deeper red drives the weaker it hits — which
retroactively justifies Epstein against Lanchester with mechanisms
Epstein didn't have to assume.

**v6 queue:** red operational pauses (a real red at 0.17 fill
PAUSES to build supply forward — the pulsed Soviet offensive;
currently red grinds on, which flatters blue); symmetric supply
interdiction (blue deep fires should be able to target red
throughput, not just echelon arrival — and red ours); researched
consumption factors from FM 101-10-1 and researched OOB strengths
(the calibration pass that retires "toy"); CA pursuit/exploitation
beyond the fixed ca_kmd; the OOB ledger proper (game state and
ledger unification — CLAUDE.md's Phase-1 obligation).

## 2026-07-21 — v4 (command-decision layer: reserves, recognition, red choice)

Mechanics: withheld tactical reserves (present, not in contact, no
losses and no line CV until committed — protective capacity bought
with a thinner line); counterattack now requires MASSING (window
evaluated against line+reserve strength; a CA cancelled on risk
grounds keeps its committed reserve defensively); emergency commit
when the line nears collapse; **recognition lag** — the window must
stand open `ca_recognition_days` before command acts, i.e. the
G-3's quality is now a number; red reinforce-success (arriving
echelons divert to the leading axis); amphib pin encoded (two
beach-watch units released ~day 13 when the November sea state
closes the Pałka landing window — placeholder, dynamic version
queued). 27 tests green.

**Experiment results (30 seeds, deep=1.0, 24 days):**

1. *Recognition ladder* — monotone and quantified: each day of G-3
   lag costs ~2-4 km of theater and ~0.5-1.5 counterattack days
   (lag 0: 130 km ceded, 6.4 CA days; lag 4: 144 km, 3.7). The
   difference between a sharp operations officer and a mediocre one
   is now a measurable campaign quantity — and the protagonist's
   growth curve has a parameter name.
2. *The reserve tradeoff is real and neither side dominates*:
   withholding reserves retakes ground (134 vs 165 km ceded) but
   spends force (32.9 vs 42.0 blue CV); everything-on-line preserves
   the force and cedes ground (and never counterattacks at all —
   no massed reserve, no window). Ground versus force as a genuine
   command decision, cleanly rendered.
3. *Naive reinforce-success HURTS red* (FEBA 134 adaptive vs 205
   scripted; blue survives 3.5x better against the adaptive rule).
   Diagnosis: the rule commits arriving battalions piecemeal into
   the leading axis, and square-law engagement math punishes
   piecemeal commitment brutally. Partly artifact (red has no
   mass-before-committing discipline — v5 item), but the underlying
   phenomenon is real doctrine: Soviet norms required committing
   echelons WHOLE for exactly this reason. The artifact and the
   doctrine point the same direction; fix red's discipline before
   drawing any canon from red behavior.

**Sweep re-run under v4 (n=150, ±40% perturbation) — a certified
claim died, on schedule:**

- interdiction dominance (all-deep ≥ all-close): 99% — SURVIVES
- monotone in deep: 95% — survives
- all-deep strictly better: 57% (was 79%) — weakened by the
  command layer; reserves give close-support configs survivability
- **"counterattack requires deep>0": 11% (was 100%) — DEAD.**
  With a reserve system, massing alone can open the window that v3
  thought only interdiction could buy. v3's claim was conditional
  on blue having no reserves — every layer of added realism has so
  far killed one confident claim. The standing meta-lesson
  (structural claims have one-iteration half-lives) is now 3-for-3
  and belongs in the book's own epistemology: the staff's models
  keep being right about mechanisms and wrong about conclusions.

**v5 queue:** red commitment discipline (mass echelons before
committing — unblocks honest red-behavior findings); CA termination
(counterattacks currently run until the window shuts; culmination
needs modeling); dynamic sea-state for the amphib window; the
logistics layer (ammo/supply throughput — the artillery closure's
deferred obligation); researched strengths + mobilization timelines
(research queue).

## 2026-07-21 — Artillery item CLOSED by argument (one guard added)

The v0 finding "artillery is wrong: modeled as direct-fire CV"
is resolved as a bookkeeping confusion, not a missing subsystem,
on three grounds:

1. **The coefficients are all-arms.** Alpha/beta are anchored to
   HERO total-battle-casualty rates, which already include
   artillery — historically the dominant casualty producer in them.
   A separate artillery attrition mechanism at daily/battalion/
   theater grain would double-count what the calibration data
   embodies. This is the aggregation logic that ruled out bottom-up
   modeling, applied consistently: QJM and Epstein also weight
   artillery into aggregate combat power at this grain. Arty CV in
   the stack is a composition weight, and that is legitimate.
2. **Ammo-as-throughput belongs to the logistics layer.** The
   NATO-shell-shortage problem is maximally Goal-shaped and WILL be
   modeled — as supply throughput throttling all combat power, with
   artillery as its biggest customer. Deferred-to, not denied;
   tracked as the logistics layer's requirement.
3. **Counterbattery/fires texture is prose**, per decompose-on-
   demand doctrine (FM 6-20-30 family is in /bulk for that).

Counter-brief, kept live: this closure fails only if campaign
logic (not scene texture) ever hinges on a counterbattery duel or
gun-specific ammo starvation. The first is implausible at our
altitude; the second re-opens inside the logistics layer, where it
belongs.

One real defect fixed in code (~20 lines + test): pro-rata loss
distribution could leave an axis "held" or "taken" by surviving
artillery battalions alone. Guns neither hold nor take ground:
`Force.has_maneuver` now gates both collapse and advance.

## 2026-07-21 — v3 (airframe stock, red counter-interdiction, sweep harness)

Mechanics: sortie generation is now a STOCK (air points come from
surviving airframes; sorties cost airframes; deep costs ~2x close —
the sortie-generation payload made real: an air force can spend
itself); red air against blue mobilization (grounded in the front
research — the documented Baltic threat to Danish roads/bridges/
ports — same capped late-and-weaker logic as blue's FOFA, in
reverse); scenario upgraded to researched STRUCTURE with toy
strengths (UKMF brigade per Davies/BALTAP sources, Soviet third
echelon TO-VERIFY); and the REQUIRED sensitivity sweep harness
(wargame/sweep.py). 22 tests green.

**Headline: the counterattack window is contested ground.** v2's
window (15 CA days, FEBA driven to 4 km) exists only while red's
deep fight is absent. Turn on red interdiction of blue mobilization
plus the third echelon, and the window narrows to a single dawn —
day 10, ratio 0.93, one day below the threshold — which the
campaign then loses forever when the next echelon lands. The
counterstroke is not a blue capability; it is a prize the two deep
fights compete for. For the book: the enemy has a G-3 too, and the
protagonist's applied insight must beat the mirror-image insight —
which is both truer doctrine (FOFA existed precisely because Soviet
echelons existed) and better drama than v2's solvable puzzle.

**Sweep results (n=150, all key params perturbed U(0.6, 1.4),
21 days):** the first claims robust enough to survive their own
counter-brief — still conditional on the toy scenario's shape, but
no longer on its numbers:

- all-deep holds ≥ as many axes as all-close: **100%**
- monotone in deep fraction: **100%**
- all-deep strictly better (held, then force): 79%
- counterattack requires deep>0: **100%**
- v1's "split is strictly worst": 13% — the dead claim stays dead
  (parameter-dependent artifact, confirmed at ensemble scale)

**Airframe economics note:** with the stock model, sustained
all-deep spends the air force — points decline as airframes attrit,
so late-campaign interdiction fades exactly when the third echelon
arrives. Sortie-generation-as-throughput now interacts with the
echelon clock; nobody tuned this, the mechanisms composed.

**v4 queue:** the missed-dawn problem (CA evaluates at dawn against
a hard ratio threshold; day 10's 0.93 was a real window the rule
family may be too coarse to seize — consider commander-judgment
variance or multi-day window detection; this is ALSO a
characterization question: who notices the window is the book's
protagonist); blue reserve massing (whole-force CA is wrong —
counterattacks are massed from withheld reserves); red operational
choice between axes; amphib axis (LANDZEALAND pressure); artillery
(v0 item, still open); researched strengths + mobilization
timelines into the scenario (research queue items feed directly).

## 2026-07-20 — v2 (counterattack windows, mobilization, weather, saturation)

Mechanics: blue mobilization inflow (Danish/FRG reserve battalions on
arrival schedules — the covering-force clock); counterattack windows
(fires only when red's in-contact echelon is spent, the follow-on is
≥2 days out, and blue accepts attacker-grade risk; FEBA moves back,
spent echelon pays a cohesion premium); weather-gated air (seeded
November placeholder: stand-down days + degraded factor); close-
support saturation; political hold release (`hold_release_day`).
18 tests green.

**The arc exists in the machine now.** Single-seed run, deep=1.0:
inland axis annihilates red's first echelon and drives the FEBA from
65 km back to 2 km — interdiction delays echelon 2 (~5 days), the
mobilizing defense grinds echelon 1 to the spent threshold, and nine
consecutive counterattack days do the rest — while the coastal axis
survives at 83/95 km with blue's covering force effectively
destroyed. Failing defense → doctrinal insight applied → local
counterstroke, with the cost showing on the other axis: the book's
shape, from the instrument, unprompted.

**30-seed robustness (weather variance), 21 days:**

| deep | axes held (2/1/0 of 30) | mean blue CV | mean CA days |
|---|---|---|---|
| 0.0 | 0 / 30 / 0 | 6.6 | 0.0 |
| 0.5 | 0 / 30 / 0 | 16.0 | 0.3 |
| 1.0 | **26** / 4 / 0 | 30.5 | 9.4 |

**Correction to a v1 finding, on the record:** v1's "the 50/50 hedge
is the worst belligerent policy" did NOT survive v2 — with
mobilization inflow and close-support saturation the payoff is
monotone in deep_fraction, and split is simply intermediate. The
concave-payoff shape was an artifact of a defense with no
reinforcement clock. (The metrics-mislead point survives in weaker
form: close support still *looks* better daily than its campaign
value, but the trap is drift, not a cliff.) Lesson for the
instrument's own epistemics: v1 structural claims have roughly
one-iteration half-lives; nothing informs canon before the parameter
sensitivity sweep, which is STILL REQUIRED and still pending.

**New mechanism finding:** the counterattack window is
mobilization-dependent, not just interdiction-dependent. With no
blue inflow (v1 scenario), red's ratio advantage never dips below
the spent threshold — no amount of interdiction opens the window,
because the covering force shrinks as fast as red's first echelon.
The counterstroke needs BOTH the delayed second echelon AND arriving
fresh battalions. Thematically: tempo advantage is created by the
interaction of the enemy's constraint with your own throughput —
which is a cleaner statement of the book's thesis than either lever
alone.

**v3 queue:** parameter sensitivity sweep harness (REQUIRED,
promoted); red operational choice (red currently never reallocates
between axes or pauses to mass — a live opponent would); blue air
attrition (air points are currently a free resource — sorties should
cost aircraft, which is the sortie-generation payload); interdiction
of blue mobilization (red air exists too); artillery still wrong
(v0 item, still open); naval/amphib flank (still open).

## 2026-07-20 — v1 (echelonment, close-vs-deep air, hold lines)

Mechanics added per the v0 tension list: red follow-on echelons on
arrival schedules; a blue air-allocation lever (`deep_fraction`:
close support adds CV to today's fight, interdiction attrits and
delays the *unarrived* echelon, delay rate capped — you cannot stop
the second echelon, only make it late and weaker); political hold
lines per axis (forward defense as geometry — withdrawal stops
there, standing means full-contact attrition); logs now carry the
G3's decision input (projected full-contact loss) alongside the
realized outcome. Attrition parameters re-anchored to the HERO
handbook's bands (division engagement norm ~1.0%/day; terrain/
weather cells 1.6-3.6%/day; Figs 47-48). 13 tests green.

**The four-corner experiment** (toy numbers — mechanism
demonstration, NOT a finding about LANDJUT; sensitivity sweep is
queued before anything here informs canon):

| policy | coastal | inland | blue force |
|---|---|---|---|
| close air + hold lines | FALLEN d12 | FALLEN d14 | annihilated |
| ALL-DEEP air + hold lines | FALLEN | **HOLDING d18** (85/110 km, red 2nd ech delayed ~9 days) | 2.5 CV — held by a thread |
| split 50/50 + hold lines | FALLEN | FALLEN | annihilated |
| split 50/50, free withdrawal | FALLEN | FALLEN | preserved (4 bns/axis) |

Three structural results, all thesis-shaped:

1. **The constraint is the arrival rate, not today's firepower.**
   All-deep beats all-close *even though blue gives up every point
   of close support while being ground down at its hold line* —
   because the second echelon's arrival schedule, not the current
   force ratio, is what kills the defense. Subordinating today's
   fight to the system's constraint is The Goal's move, emerging
   from the machinery unprompted.
2. **Splitting the effort is the worst belligerent policy.** 50/50
   loses both axes AND the force — half-interdiction doesn't delay
   the echelon enough to matter, and half-close-support doesn't
   stop the grinding. The intuitive compromise is the trap. (Toy-
   number caveat applies at full strength here; but the shape —
   concave payoff punishing hedges — is exactly the metrics-
   mislead engine the book needs, because a staff measuring "sorties
   supporting troops in contact" will always drift toward close.)
3. **The standing dilemma sharpened.** v0 showed rational
   withdrawal loses the theater; v1 shows forward defense loses the
   *army* (hold + close = annihilation by day 12-14, projected
   daily losses climbing past 20-40% while the log's "S" column
   marks the days the hold line forbade the withdrawal the model
   wanted). The book's opening act lives in that S column.

**New tensions / v2 queue:**
- No blue counterattack: the arc's payoff (applied counterstroke)
  has no mechanism yet — blue can only delay, bleed, or die. A
  counterattack window (when red's in-contact echelon is spent and
  the next is delayed) is the natural v2 feature and IS the tempo
  payload.
- Interdiction is weather/night-blind: November's short days
  (setting-time.md) should gate air points daily; currently air is
  a constant. Variance layer (the reserved seed) belongs here.
- Close support scales linearly and never saturates; needs
  diminishing returns before any policy conclusion survives.
- Hold lines are static; political release of a hold line mid-
  campaign (the Andon Cord moment upward) would let the model stage
  the book's command-relationship drama.
- Loss-fraction log columns divide by a floored denominator and
  read >100% on annihilation days — cosmetic, fix with the
  logging-clarity pass.
- Sensitivity sweep harness (vary alpha/beta/delay params, report
  which structural results survive) — REQUIRED before any of
  today's shapes inform canon; the counter-brief discipline applied
  to our own instrument.

## 2026-07-20 — v0 build (Lanchester core + axis frame + toy LANDJUT)

**Headline: the toy model already stages the book's argument.**
First run, placeholder numbers: blue plays the Epstein-rational
defender — trades space whenever full-contact losses would exceed
tolerance — and *preserves its force beautifully* (4 of 4 battalion
groups alive on each axis at the end) while **losing the entire
theater in 8-11 days**, because Schleswig-Holstein is 95-110 km deep
and a casualty-minimizing withdrawal eats ~10 km/day. The
attrition-rational defense loses LANDJUT with its army intact; the
stand-and-fight defense keeps the ground and loses the army. The
doctrinal escape from that dilemma — counterstroke, deep attack on
the follow-on echelon, tempo — is exactly what attrition models
can't represent, which is to say: the toy model's failure mode IS
the protagonist's problem. Active Defense's forward-defense politics
(you may not trade German ground) plus the periphery's actual
geography (there is no ground to trade) make the tension
geographically forced, not doctrinally optional. This deserves to
survive into the book's spine.

**Tensions / v1 needs surfaced:**

1. **No echelonment.** Red fights as one echelon; the whole FOFA/
   deep-battle payload needs red's second echelon arriving on a
   schedule the blue player can attack (the constraint is the
   *arrival rate*, not the force in contact). This is v1's core
   feature, not an option.
2. **No depth/politics constraint on withdrawal.** Need hold-lines
   (forward defense as a political input) and terminal depth (the
   Kiel Canal as the geometry's actual wall). The model must be able
   to say "you cannot Epstein your way out of a 95 km theater."
3. **3:1 pressure-advance never fired** (ratios ran 1.4-2.1); all
   red advance came from blue's withdrawal. Real advance-rate tables
   (QJM: Dupuy purchase) are load-bearing, not decoration.
4. **Artillery is wrong**: modeled as direct-fire CV in the stack.
   Needs its own treatment (fire support multiplying engaged units,
   counterbattery, ammo as throughput — the logistics payload).
5. **Withdrawal has no cost or end state**: no rally, no breaking of
   contact, no exhaustion of march capacity, no bridge demolitions.
   Delay operations need their actual grammar.
6. **Logging conflates decision inputs and outcomes**: the defender
   decides on full-contact projected losses, the log shows scaled
   actual losses — a reader of the log can't see the decision. Log
   both (the model should generate what a staff sees — and staffs
   see estimates AND results disagreeing, which is on-theme).
7. **Naval/amphib flank absent**: the coastal axis needs the LC
   naval-zone pattern (off-map pressure, threatened landings pinning
   blue reserves) before LANDJUT runs mean anything.

**Research provoked (queue into reference/shelf.md work):**

- Actual LANDJUT geography and depth geometry: where NATO planned to
  stand (Trave? the Segeberg line? the Canal?), bridge/canal
  demolition doctrine, Hamburg's political shadow on the western
  flank.
- Forward-defense politics for Schleswig-Holstein specifically
  (FRG's Vorneverteidigung obligation vs Danish government posture).
- GDR 5th Army / Polish Pomeranian axis OOB and the WP amphibious
  order of battle for the Baltic (real echelon timings).
- Danish and 6th Panzergrenadier Division mobilization timelines
  (the covering-force period is where the book's opening lives).
- Dupuy advance rates and daily-casualty norms (purchase list —
  now blocking v1 calibration).
- Epstein's actual equations (purchase list — our withdrawal shape
  is flagged UNVERIFIED in wargame/models/epstein.py).

**Mechanics banked:** Lanchester square/linear with closed-form
verification (invariant conserved to 1e-9; Euler converges); the
square law's concentration claim and the linear law's absence of it
now live in tests as executable definitions — useful when the book
needs a character to *explain* the 3:1 debate. Year-parameterized
OOB loading works (in_service filter). 9 tests green; deterministic
runs verified.
