# Wargaming findings log

Running log, newest at top within each session block. The instrument's
version of imagegen/findings.md from white-buffalo: what the builds
and runs taught, what they broke, what research they forced.

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
