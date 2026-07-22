# Advance rates — the ORALFORE calibration bench

*Extracted 2026-07-22 (session 3845eb93) from
reference/pdf/hero-oralfore-opposed-rates-of-advance-1972.pdf: HERO,
"Opposed Rates of Advance of Large Forces in Europe (ORALFORE)," Final
Report, 28 August 1972, prepared for ODCSOPS (DAMO-PLW) under contract
DAHC19-72-C-0015; DTIC AD902830, 377 pp. scan. This is the wargame's
missing advance-rate bench — the current movement parameters are
self-declared placeholders (wargame/scenarios/toy-landjut.toml:24-27,
"PLACEHOLDER thresholds pending QJM advance rates,"
wargame/campaign.py:20). Every number carries its page; derived or
arithmetic-reconstructed values are marked DERIVED; deltas against the
wargame are CAL-A…-F.*

**Standing caveats.** (1) **Dated 1972 — pre-setting.** Usable without
anachronism worry for the instrument, and it is *in-period knowledge*:
this study is the seed of Dupuy's QJM lineage (Appendix E is the QJM's
first full published statement; *Numbers, Predictions and War* 1979
descends from it), so a mid-80s NATO staff officer could plausibly know
these categories. The official critique (CHASE, 1986 — §8) is
period-*edge*: contemporaneous with the setting, not yet folklore.
(2) **The data base is six WWII operations** (1940 France, 1941 and
1942 Eastern Front, three 1944 NW-Europe US operations), all
*attacker-side* documented; no Soviet-attacker cases (data
unavailable, p. 2). The study itself calls every cell's sample "very
small" (p. III-1). (3) **Scan quality**: the daily matrix analysis
sheets (the per-day data tables for all six operations) are defeated
by OCR — headings and legends extract, the numeric grids do not. The
summary tables in Section III/IV and Appendix E extract cleanly, and
the "Normalized Rates of Advance" chart (p. III-10) was read from the
page image with arithmetic cross-checks. Anything from the daily
matrices is TO-VERIFY against the page images.

## 1. The factor structure: resistance intensity, not force ratio

ORALFORE's central structural finding (pp. III-4, III-6, IV-1): rates
of advance are **not a function of force ratio**. Force ratio acts as
a *threshold* — "sustained advances are probably not possible unless a
threshold force ratio superiority has been achieved" (General
Conclusion 2, p. IV-1) — and above the threshold the rate is governed
by the **intensity of the defender's opposition** plus environment.
The categories (p. III-6):

| Category | Opposition | Force-ratio threshold |
|---|---|---|
| I | Determined opposition (defender able and intent on stopping/severely limiting the advance) | attacker superiority ~**1.1–1.3** |
| I-A | …intense resistance | |
| I-B | …moderate resistance | |
| II | Light opposition (defender lacks capability or intent; occasional delay and harassment) | ~**1.3 or more** |
| II-A | …slight resistance | |
| II-B | …negligible resistance | |
| III | Administrative move, no substantial resistance expected | — |

The worked evidence for the threshold thesis (pp. III-3–III-4): US XX
Corps crossed northern France at **5:1–7:1 raw** force ratio; at
defended obstacles the QJM-refined ratio still ≥ **2:1** and the
advance continued; when the refined ratio shifted to ~**2:1 in the
Germans' favor** in the Metz fortified zone, "the American advance
abruptly stopped." The study is explicit that six operations cannot
*prove* threshold-over-ratio, only that the method could with more
data (p. III-4).

A proposed refinement the data hinted at but could not support
(pp. III-9, IV-2): splitting Category I into **determined *sustained*
opposition** (XL Pz Corps in the Caucasus, XX Corps at Metz, XII Corps
in the Saar — slow) vs **serious *intermittent* opposition** —
i.e., the delaying-defense case is suspected to be a *different rate
regime*, not a milder version of the same one (§6).

## 2. The core numbers: normalized rates of advance (km/day)

Conclusions, p. IV-2 (identical statement pp. III-8–III-9). These are
*normalized* rates — actual rates divided by composite environmental
and operational factors (§3) to estimate the rate "in a comparable
tactical situation under 'normal' … circumstances" (p. III-8):

| Category / resistance | Overall range | avg | Corps avg | Armd Div avg |
|---|---|---|---|---|
| I-A Intense | 1.32–4.04 | **2.80** | 2.76 | 2.89 |
| I-B Moderate | 4.18–15.87 | **10.10** | 9.48 | 10.40 |
| II-A Slight | 5.15–36.72 | **23.34** | 20.75 | 25.69 |
| II-B Negligible | 34.55–78.22 | **54.79** | 48.66 | 63.30 |
| III Administrative | — | **69.78** | 45.00 | 120.00 (inf div 55.60) |

Sustained tactical administrative march: **55–60 km/day** was
sustainable for weeks by VII Corps divisions "despite necessary
security measures," and "major obstacles do not appear to affect
tactical administrative march rates" (VII Corps analysis, comments 4–5,
p. D-47ff).

The shape to keep: each resistance step is roughly a **2–4x rate
jump** (2.8 → 10.1 → 23.3 → 54.8), against which force-ratio
differences above threshold do almost nothing.

## 3. Actual (un-normalized) rates, US 1944 operations

From the "Normalized Rates of Advance" chart, p. III-10 (PDF p. 326),
read from the page image; DERIVED arithmetic check: potential = actual
÷ (env factor x op factor) reproduces the chart's printed potential in
every cell below. Actual km/day by resistance met:

| Unit (operation) | Intense | Moderate | Slight | Negligible | Admin |
|---|---|---|---|---|---|
| XX Corps (E, Aug–Sep 44) | 2.2 | 8.3 | 23.0 | 26.7 | — |
| 7th Armd Div (E) | 1.0 | 12.0 | 23.8 | **51.6** | — |
| VII Corps (D, Aug–Sep 44) | — | 6.6 | 22.9 | ~34 | 48.0 |
| 3d Armd Div (D) | 2.3 | 6.7 | 20.3 | 36.9 | **120** |
| XII Corps (F, Nov–Dec 44, Saar) | **1.3** | 2.6 | 3.2 | — | — |
| 4th Armd Div (F) | 1.2 | 4.9 | 8.7 | — | — |

(Composite factors: Op E env 0.84, op 0.90–0.92; Op F env 0.74, op
0.84–0.86; Op D env ~0.88, op ~0.94 — Op F's low environmental factor
is the November mud and cold, which is why its *normalized* rates
join the common ranges while its actuals sit far below Op E's.)
Second-decimal cells in this chart are TO-VERIFY against the page
image; the row/column structure and the checked cells are solid.

The normalization recipe (pp. III-7–III-8), tagged by the study itself
as "arbitrary" and "tentative": composite environmental factor =
mean of (weather factor², terrain factor, roadnet factor,
obstacle/logistics-inhibited-days factor); composite operational
factor = mean of (√(combat-effectiveness ratio), an opposition
intensity value (minimum on pause/negligible days, +0.1 slight, +0.3
moderate, +0.5 intense), and (1 − daily casualty rate)).

## 4. Methodology, and what "resistance" means operationally

- **Derivation** (pp. 1–4): daily reconstruction of six WWII
  operations of 2–5 weeks' sustained movement, from primary records
  (US corps/division G-1/2/3/4 files; German unit Kriegstagebücher on
  National Archives microfilm — Bibliographical Note). QJM force
  ratios could be completed only for **Operations E and F** (XX and
  XII Corps); A–D use estimated ratios, "no attempt … on a daily
  basis" (pp. 3–4, A-22, B-36, C-61).
- **Intensity of opposition to advance** is "the historian's estimate
  from the narrative, and from an assessment of relative casualties …
  of the tenacity of the defender's resistance … on any given day. It
  bears no relationship to force ratio" and reflects only the
  *engaged* elements, "frequently only a relatively small fraction of
  the total forces available" (p. 4). Coded I/M/S/N (Intense /
  Moderate / Slight / Negligible) plus P (pause) in the daily
  matrices. The study flags this as its weakest link and wants it
  replaced by a casualties-per-distance formula (pp. III-8–III-9).
- **Attacker's casualties, not defender's, track the rate**: "rates of
  advance appear to be rather closely related to casualties sustained
  by the advancing force … the defender's casualties appear to have
  little or no close relation" (General Observation 1, p. III-4).
- **Order of significance, operational** (Specific Conclusion 1,
  p. IV-1): attacker's mission → adjacent forces' missions/locations →
  defender's mission → relative combat effectiveness → perceived
  intensity of opposition. Note force ratio is *not on the list*.
- **Order of significance, environmental** (Specific Conclusion 3,
  p. IV-2): terrain configuration → weather → exceptional obstacles
  (rivers, urban areas) → roadnet/road conditions.
- **Surge-decay**: "overall rates of advance … tend to be greatest in
  the first few days and to decline gradually but steadily" (General
  Observation 7, p. III-5); within Op E, each between-pauses movement
  series showed an initial surge then decline (E-42, comment 5).
- **Logistics**: the only firm finding — "the advance rate falls
  rapidly down to zero when fuel supply is interrupted" (General
  Observation 3, p. III-5; XX Corps went static when out of gasoline,
  E-41). Limited-vs-interrupted fuel effects: explicitly unanswered.
- **Night**: no night factor exists; all rates are per-day averages at
  daily grain (matches the wargame's daily tick — no separate
  day/night split to import).

## 5. Degradation factors (QJM tables, Appendix E)

The study *assumed* terrain/weather effects on advance rates equal
their QJM effects on combat capability, and says "this assumption
needs to be tested" (General Observation 5, p. III-5). The factors, as
used to refine force ratios:

**Terrain (Table 2, p. App-E10)** — mobility factor rm: rugged wooded
0.4, rugged mixed 0.5, rugged bare / rolling wooded 0.6, rolling mixed
0.8, rolling bare / flat 1.0-ish (flat wooded 0.7, flat mixed 0.9).
Defense-position multiplier ru (defender only): rugged 1.35–1.5,
rolling 1.3–1.45, flat 1.05–1.2. LANDJUT's rolling-mixed/flat terrain
sits at the mobility-friendly end: rm 0.8–1.0, defender ru 1.2–1.45.

**Weather (Table 3, pp. App-E10–E11)** — attack factor ha: dry 1.0
(0.9 extreme heat/cold-overcast cells); wet-light 0.7–0.9; **wet-heavy
0.5–0.6**. (Column alignment in the OCR is imperfect; band structure
is solid, individual cells TO-VERIFY.)

**Roadnet mobility (matrix key, p. A-23 and repeated)** — unlimited
cross-country 1.0; good roadnet 0.8 (0.7–0.9); fair 0.5; poor 0.2;
impassable 0.0.

**Posture (Table 6, p. App-E12)** — force-strength multiplier us:
attack 1.0; **hasty defense 1.3; prepared defense 1.5; fortified
defense 1.6; withdrawal 1.15; delay 1.4**.

**Obstacles and demolitions**: tracked daily by code (R river, FZ
fortified zone, Ur urban, Fl flooded, **Dn "exceptionally effective
demolitions"**, Sa sabotage — matrix key, p. A-23) but **never
quantified**: "obstacles tended to reduce advance rates, although the
extent of this reduction is not calculable from the data" (A-22; same
verdict E-42 comment 6, and Conclusion 6a wants the research done).
Qualitative anchors: major obstacles slow even an *undefended*
combat advance (VII Corps analysis, comment 1, p. D-47ff) but not an
administrative march (ibid., comment 5); rates were lowest during
river crossings and mountain movement (XL Pz Corps, C-61); a coup de
main at an unblown bridge (Verdun) erased the obstacle entirely (E-42,
comment 6). One demolition data point in the narrative: a 130-man
Allied demolition party blew the Canal du Nord bridge at Marquion
ahead of 7th Panzer (20 May 40) — cost: about two hours, the division
crossing elsewhere by 0500 and engineers bridging (16-ton) the same
day (p. A-12ff — narrative, not a factor; a demolition *without a
defender behind it* bought almost nothing, which is the
delaying-screen point in miniature).

## 6. Delaying screens vs prepared defense

What the bench offers the re-baseline's missing delaying-screen
representation (notes/wargaming-findings.md, 90-hour-clock entry):

- The QJM prices a **delaying posture at 1.4** — nearly a prepared
  defender (1.5), far above a withdrawing one (1.15) (Table 6,
  p. App-E12). A competent screen is not a speed bump; it multiplies
  its force strength almost as much as a dug-in defender while giving
  ground.
- Operationally, the 1944 narratives code German delaying detachments
  as *slight-to-moderate* resistance: VII Corps "moved forward quickly
  against light German delaying forces" (D narrative) but a "resolute
  delaying action" by 9th Panzer limited a day's advance outright
  (D narrative, Ranes fighting). So a screened axis lives in the
  **~10–23 km/day** band (I-B/II-A), an unscreened one in the
  **~45–60+ km/day** band (II-B/III) — a factor of 2–4, which is the
  delaying screen's entire military value at this grain.
- The suspected fourth regime — "determined, *sustained* opposition"
  as rate-distinct from "serious, *intermittent* opposition"
  (pp. III-9, IV-2) — maps exactly onto prepared-defense-with-depth vs
  successive-delay-lines, but ORALFORE could not populate it.

## 7. The study's own stated limitations

- Feasibility study only; "the analysis initiated in this feasibility
  study cannot be completed without a larger data base" (General
  Conclusion 3, p. IV-1); category boundaries themselves "too small
  [a sample] to permit firm conclusions" (Gen. Obs. 10, p. III-6).
- Time/budget forced triage: full QJM analysis only for Ops E and F;
  Ops A–C lack opposing-side statistics entirely (pp. 3–4).
- Logistical constraints on rates: not assessable beyond the
  fuel-interruption finding (p. III-5, Specific Conclusion 2, IV-1).
- The normalization factors are "arbitrarily-determined … quite
  tentative" and not offered as definitive (p. III-8).
- No Soviet-attacker operations; WWII armies only, with a hand-waved
  Napoleon-1812 comparison suggesting motorization roughly doubled
  Cat-II and tripled Cat-III rates but left **Cat-I rates unchanged
  since the pre-20th century** (Gen. Obs. 11, pp. III-6–III-7) — the
  claim most worth remembering when tempted to let 1980s mechanization
  inflate opposed rates.

## 8. Counter-brief: the CHASE critique (1986, period-edge)

Per "evaluations are briefs, not verdicts" — the official 1986 reading
of the HERO empirical program
(reference/pdf/caa-chase-combat-history-analysis-1986.pdf, CAA-TP-86-2,
on the later 601-battle HERO database that grew from this lineage):

- The database "is still not large enough to support adequately all of
  the statistical analyses" and contains "typographical mistakes,
  omissions, ambiguities and ill-defined data categories" (Limitations
  2–3, p. vi). HERO's intangible tables are "frankly judgmental, and
  hence almost impossible to objectify" (p. 2-1/2-2) — the same
  critique lands on ORALFORE's historian-estimated intensity codes.
- Battle durations recorded "only to the nearest day … too coarse a
  time resolution to provide rate values suitable for analysis"
  (p. 1-5/1-6) — a direct caution against over-trusting km/*day*
  precision.
- But CHASE *supports* ORALFORE's headline: "force ratio is an
  unsatisfactory and inadequate predictor of victory in battle"
  (Key Finding f, p. 1-6). The threshold-not-rate-ratio structure
  survives its own hostile audit; the specific cell values are what
  carry wide error bars.

## 9. Calibration deltas against the current instrument

Current parameters (wargame/scenarios/toy-landjut.toml:24-27, 68,
203-214; mechanics in wargame/campaign.py:1074-1082, 903):

- **CAL-A — `march_kmd = 25.0` conflates two ORALFORE regimes and is
  low for both.** The model uses it as the unopposed/collapse rate and
  the cap on following up withdrawals. ORALFORE: negligible-resistance
  advance ≈ **49–55 km/day** normalized (26–52 actual), admin march
  **45–60 sustained**. An uncovered axis at 25 km/day is charitable to
  blue by ~2x — which flatters exactly the middle rows of the
  90-hour-clock table (the collapse path) that the findings log
  already flags as flattered. Honest fix is CAL-C's split, not just a
  bigger number.
- **CAL-B — `pressure_kmd = 4.0` sits in the right band.** Against
  determined opposition ORALFORE gives intense 2.80 / moderate 10.10
  normalized; 4.0 is a defensible single value for
  determined-opposition pressure on a corps frontage (XII Corps
  actuals against Vorneverteidigung-like defense: 1.3–3.2). Keep,
  cite, stop calling it a placeholder.
- **CAL-C — `advance_ratio = 3.0` gates the wrong variable.**
  ORALFORE's force-ratio threshold for *any* sustained advance is
  **1.1–1.3**, and above it the rate is set by *resistance intensity*,
  not ratio ("the contested 3:1!" comment in the scenario file is
  self-aware). The ORALFORE-shaped mechanic is a resistance-intensity
  ladder — screened / determined / negligible — selecting the rate
  band (≈2.8 / ≈10 / ≈50), with the ratio appearing only as a ~1.3
  threshold. This is the delaying-screen representation the
  re-baseline queued: a screen's effect is precisely "axis moves one
  band down" (§6), not a CV contest.
- **CAL-D — engineer/obstacle parameters are ahead of the source.**
  `obstacle_adv_factor = 0.5`, `demo_crossing_days = 2`,
  `demo_crossing_loss_mult = 1.5` have *no ORALFORE numbers behind
  them* — the study explicitly could not quantify obstacle effects
  (§5). Directionally everything matches (obstacles slow contested
  advance; demolitions coded as exceptional events; blown Meuse
  bridges ≈ 1 day). Keep values as declared free parameters; the
  quantified obstacle bench must come from elsewhere (FM 90-13 /
  engineer doctrine — open item).
- **CAL-E — `w_max_kmd = 12.0` is consistent** with the II-A band: a
  withdrawing-but-fighting defender concedes ~10–23 km/day to a
  pursuing corps; 12 as *blue's chosen* maximum inside that band is
  fine, and the delay-posture factor 1.4 supports the model's choice
  to keep a withdrawing blue lethal.
- **CAL-F — surge-decay is unmodeled.** ORALFORE: advances open fast
  and decay steadily (Gen. Obs. 7); red's pulse mechanic captures the
  pause-resume cycle but each pulse advances at a flat rate. A
  within-pulse decay factor is a candidate campaign-3 mechanic, not a
  number to tune now.

## Open items

- Read the daily matrix sheets from page images (per-operation daily
  rate + intensity series; the six "Cumulative Rate by opposition"
  blocks) — OCR-defeated, needed before any distribution-level claims.
- Overall Matrix Comparison chart (p. III-2 area, PDF p. 318) —
  rendered but not yet mined; contains the per-operation composite
  factor averages and the Napoleon-1941 comparison data.
- A quantified obstacle/demolition bench (ORALFORE names the gap;
  Conclusion 6a assigns the research nobody then funded) — engineer
  doctrine pubs, front research queue.
- Dupuy's later *Numbers, Predictions and War* (1979) / HERO's 1980s
  advance-rate work updates these categories with the larger database
  ORALFORE asked for — in-period for the setting, not yet on the
  shelf.
- Soviet-attacker rates: ORALFORE has none; FM 100-2-1 (1984, held)
  gives the *planning norms* red staffs would use — "approximately 50
  kilometers per day" anticipated over weeks, "up to 30 kilometers per
  day" while fighting through defensive positions (FM 100-2-1 ch. 4,
  "Rapid Advance," p. 4-3). ORALFORE's history says determined
  opposition yields 3–10. A red plan written at 30 meeting ground that
  pays 10 is a scene, not just a parameter.
