# Wargaming findings log

Running log, newest at top within each session block. The instrument's
version of imagegen/findings.md from white-buffalo: what the builds
and runs taught, what they broke, what research they forced.

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
