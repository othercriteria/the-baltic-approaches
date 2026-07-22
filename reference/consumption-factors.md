# Consumption factors — the FM 101-10-1 calibration bench

*Extracted 2026-07-21 (session 71ede904) from the held shelf copies:
FM 101-10-1 (Oct 1987) Vols 1-2, FM 100-2-1 (1984), and the /bulk
scan of FM 100-2-2 (1984). This is the "FM 101-10-1
consumption-factor extraction" item from the campaign-1 handoff
(notes/wargaming-findings.md) — the research pass that gates model
work. Every number carries its table; derived ratios are marked
DERIVED; deltas against the current wargame parameters are marked
CAL-n.*

**Standing caveats.** (1) FM 101-10-1 is the *US* staff officers'
bench; LANDJUT's divisions are German and Danish. These factors
calibrate the model's *shape* (posture ratios, intensity ladder,
orders of magnitude); absolute values are US-division stand-ins
until Bundeswehr/Danish norms are found (front research queue).
(2) The held edition is dated October 1987 — usable for our
instrument without restriction, but for anything in a *character's
hands* the period edition (FM 101-10-1, 1976/earlier-80s printing)
must be verified against the setting year once pinned
(shelf discipline, planning/setting-time.md). (3) ~~US per-capita derivations assume a J-series heavy division
of ~16,000-17,000 — TO-VERIFY~~ → VERIFIED 2026-07-22 (session
3845eb93): `pdftotext -layout` defeats the scan where plain
extraction failed, and the page was verified VISUALLY (render +
counter-rotate; the held copies are scanned 90° CW — see the
recipe in reference/shelf.md). Vol 1 p. 1-152, Section II
Personnel Summary, heavy-division rows [TOE 87000J410-440],
aggregate strength at authorization Level 1 / 2 / 3:
AR DIV (6xM60/4xM113) **16,993** / 16,027 / 14,246;
MX DIV (5xM60/5xM113) **17,278** / 16,247 / 14,463;
AR DIV (M1/BFV) **17,027** / 15,860 / 14,165;
MX DIV (M1/BFV) **17,330** / 16,115 / 14,390.
The ~16.5k working figure stands; per-capita derivations below
are good to ±3% at Level 1-2.

## 1. Division Class V (ammunition) consumption by posture

FM 101-10-1 Vol 2, Table 2-16 ("Ammunition Per Type Unit Per Weapon
Per Day... Rounds and STON"), division roll-up rows, short tons/day.
Rates are for a division "heavily committed and firing at high
rates" — surge rates, not theater averages (see §3).

| Division type | Defense day 1 | Defense succ. | Attack day 1 | Attack succ. | Protracted (d6-15) |
|---|---|---|---|---|---|
| Armored | 2,432.6 | 1,902.8 | 1,911.5 | 1,424.3 | 1,163.4 |
| Mechanized | 2,156.8 | 1,742.3 | 1,680.4 | 1,295.4 | 1,094.1 |
| Infantry | 1,896.3 | 1,722.0 | 1,579.6 | 1,350.9 | 864.2 |
| Air assault | 1,825.1 | 1,653.1 | 1,572.2 | 1,297.8 | 808.9 |
| Airborne | 1,373.4 | 1,277.9 | 1,180.7 | 1,018.7 | 552.2 |

"Succeeding days" = days 2-4; day 5 = mean of succeeding and
protracted (table footnote). **Note the direction: defense of
position out-consumes attack** in Class V, in every division type,
both time bins. The defender's guns are the theater's biggest ammo
customer — on-theme, and counter to the intuition that the attacker
buys tempo with tonnage (he buys it with *fuel*, §4).

## 2. Situation multipliers (para 2-15d)

Applied against Table 2-16 columns:

| Situation | Multiplier |
|---|---|
| Attack of fortification / hasty attack | 100% of attack (deliberate) |
| Covering force | 100% of defense of position |
| Inactive situation | 80% of protracted |
| Meeting engagement | 200% of protracted |
| Pursuit | 40% of protracted |
| Retrograde | 59% of defense (succeeding) |

DERIVED — the intensity ladder normalized to defense-day-1 = 1.00
(mechanized division):

| State | Fraction |
|---|---|
| Defense, first day | 1.00 |
| Defense, succeeding / attack, first day | 0.78-0.81 |
| Attack, succeeding | 0.60 |
| Protracted | 0.51 |
| Inactive | 0.41 |
| Retrograde | 0.46 |
| Meeting engagement | 1.01 |
| Pursuit | 0.20 |

## 3. Theater-level average rates (Vol 2, Table 2-3)

Pounds per person per day, temperate zone, all echelons averaged:

Class I 4.03 · II 3.67 · III bulk 53.7 · III pkg 0.59 · IV 8.50 ·
V 31.29 ("moderate level of combat", TAA 92) · VI 3.20 · VII 15.00 ·
VIII 1.22 · IX 2.50 — **total ≈ 123.7 lb ≈ 0.056 STON/person/day.**

DERIVED — the surge-vs-average gap: a committed mech division's
Table 2-16 Class V rate (~2,157 STON/day ÷ ~16.5k men ≈ 260
lb/man/day) is **~8x the theater-average Class V planning factor**
(31.29). Both numbers are official; they answer different questions
(committed division-slice at surge vs. all theater troops averaged).
A staff that plans the theater on Table 2-3 and fights a corps that
consumes at Table 2-16 has a bottleneck it built itself — this is
maximally Goal-shaped and belongs in the book's argument, not just
the model.

## 4. Class III (POL)

Vol 2, Table 2-15 computes fuel bottom-up (per equipment-hour; wheels
per-km) via usage profiles — too granular for our grain. Usable
anchors: the manual's own worked example runs **one M60 tank
battalion ≈ 21,600 gal diesel/day** on the European profile;
theater-average bulk POL is 53.7 lb/person/day (Table 2-3), the
largest single class. Direction of asymmetry: fuel is the *mover's*
class — attack and pursuit spend Class III where defense spends
Class V. The model's single "supply" scalar hides this; fine at
current altitude, but deep fires against "throughput" would in
reality choose between starving red's movement (fuel) and red's
firepower (ammo) — parked as texture until a mechanism needs it.

## 5. The Soviet accounting frame (FM 100-2-1 §ammunition; FM 100-2-2 rear services)

- Planning unit is the **unit of fire** (boekomplekt): fixed rounds
  per weapon (122-mm howitzer = 80 rds; BMP 73-mm = 40; full weights
  table in FM 100-2-2, scan partially garbled — TO-VERIFY against a
  cleaner copy). Expenditure for an operation is *assigned* as a
  multiple of units of fire per phase — a push system quota, not a
  demand forecast.
- POL unit is the **refill** (tracked: integral tanks; wheeled:
  500-km range). "Motorized rifle and tank divisions normally carry
  sufficient reserves to refuel their units twice."
- Consequence for the model: red's pulse-resume threshold
  (`red_resume_fill = 1.0` — resume on a full tank) is a fair cartoon
  of assigned-refill logic; red demand between operations is a quota
  choice, which supports modeling red pause consumption as a *doctrine
  parameter* rather than mirroring blue's.

## 6. Calibration deltas against the current instrument (queue for campaign 2)

- **CAL-1 — `pause_intensity = 0.25` is likely too low.** The FM's
  closest analog to a paused-but-forward red is the *inactive
  situation* at 0.41 of defense-day-1 (§2); 0.25 sits nearer
  *pursuit* (0.20). Sensitivity run DONE (scratch/
  cal1-pause-intensity.py, n=40 x 30 days): at deep=1.0 the v6
  conclusions are insensitive (held 1.00 both, blue CV 36.6 vs
  35.9); at deep=0.0 the FM value makes the pulsed red *harder*
  (held 0.65 -> 0.23, blue CV 11.1 -> 5.3) — deep-dominance
  *strengthens* under calibration. Caveat: the parameter conflates
  paused consumption with paused contact intensity; the FM number
  calibrates only the consumption face, so the honest fix is a
  parameter split (campaign-2 mechanics, queued).
- **CAL-2 — posture-dependent demand is real and one-sided.** Current
  model: flat `demand_per_cv` both sides. FM: defense-day-1 : 
  protracted ≈ 2:1, and *defense out-draws attack* in Class V. A
  posture multiplier on demand (attacking/defending/paused/pursuing,
  §2 ladder) is the honest upgrade — mechanics change, so it belongs
  to campaign 2, gated behind the rest of the calibration pass.
- **CAL-3 — absolute unit conversion now possible.** One committed
  heavy division ≈ 2,900 STON/day all classes (Table 2-16 Class V +
  Table 2-3 non-V per-capita ≈ 760 STON at 16.5k men); LANDJUT at ~3
  division-equivalents ≈ 8-9,000 STON/day at surge. When the Danish
  road/rail/Little Belt capacity research lands (front queue), supply
  points can become short tons and the theater-capacity number stops
  being a free parameter.
- **CAL-4 — blue/red demand symmetry is defensible at first order**
  (both sides' surge tonnage is same order of magnitude), but red's
  is a quota system (§5): red starvation should bite *between*
  assigned efforts, not continuously. v6's pause/hysteresis already
  approximates this; note kept for the enemy-model ledger.

## Open items

- Bundeswehr (HDv-series) and Danish consumption norms — the actual
  blue force's numbers (front research queue; this whole bench is a
  US stand-in until then).
- ~~FM 101-10-1 Vol 1 TOE strengths for clean per-capita math~~ →
  ANSWERED 2026-07-22, see standing caveat (3): heavy division
  16,993-17,330 full TOE / 15,860-16,247 ALO-1 (`pdftotext
  -layout` on the held copy).
- Soviet unit-of-fire weight table from a cleaner FM 100-2-2 copy.
- ~~NATO days-of-supply stock policy~~ → ANSWERED for Denmark
  2026-07-22 (cia-1984-nordic-forces-in-the-1980s.pdf, Table 5 +
  p.13): NATO requirement 30 combat days; Danish stocks 1983:
  105 mm **10.0 days**, 155 mm **8.8**, 203 mm **9.4**, mortars
  17.3, TOW 15.0 (1988 projections: 8.9/11.0/8.4/14.9/30.0-if-
  funded); "the most critical shortfall ... is in the army's
  artillery ammunition"; Denmark met only 50% of its NATO TOW
  requirement in 1982. → Blue's supply constraint is DOCUMENTED at
  roughly ONE-THIRD of the planning requirement in exactly the
  class the FM's own tables say dominates a defender's
  consumption. The re-baseline task (v15 gate) should anchor
  blue_supply_points against this: a blue that fights at Table
  2-16 defense rates exhausts national artillery stocks in ~9
  days — the campaign's second week is fought on whatever NATO
  resupply arrives, which is its own throughput story.
