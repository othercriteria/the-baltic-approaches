# Soviet operational art — the Glantz/CSI distillation

*Extracted 2026-07-22 (session 3845eb93) from the held Glantz/CSI cluster,
flagged as a standing debt in the session brief ("held but undistilled").
Method: `pdftotext -layout` + `grep` navigation across all five documents
(the primary target's cover/front matter defeats plain extraction — scanned
title page — but body text extracts cleanly with `-layout`); no page images
were needed. This is a **targeted mining pass, not an exhaustive read** —
461 + 260 + 215 + 36 + 72 = 1,044 pages across the cluster; what follows is
what a grep-and-read pass on echelonment/rates/logistics/deception terms
surfaced, prioritized as DK specified. Every claim below carries a page
citation; see "Open items" for what wasn't reached.

**Page citation convention.** Where the document's own printed pagination
is visible in the extracted text and I confirmed the PDF-page-to-printed-page
offset directly (not computed blind), I cite the printed page ("p. 123").
Where the offset was inconsistent on inspection (the two *August Storm*
papers — front-matter/plate pages drift the count), I cite the PDF page
count instead, flagged as such ("PDF p. 89", i.e., page 89 of
`pdftotext -layout`'s output, reproducible by anyone re-running the same
command). Confirmed offsets: Symposium PDF page − 9 = printed page (checked
at six separate points, zero exceptions); Kursk PDF page − 2 = printed page
(checked three points); 1930s PDF page − 3 = printed page (checked twice).

**Period discipline.** All five items are *our* reference, not a
mid-80s NATO officer's shelf. The 1984 Art of War Symposium transcript
and the 1986-dated Kursk CSI report sit at or past the Nov-1983 setting
line; the two *August Storm* Leavenworth Papers (Feb/June 1983) are
right at the edge — a real staff officer could conceivably have read
them by a very-late-1983 setting, but the *symposium itself* (a 1984
event) could not have happened yet. One line for the book's texture: a
1983 LANDJUT G-2's actual bench on Soviet operational art was thin —
FM 100-2-1 (1984, held) and this whole CSI/Leavenworth Papers program
were still being written; the protagonist's real-world contemporaries
worked from NIE assessments, Dupuy-lineage empirical work (ORALFORE,
1972, reference/advance-rates.md), and translated Soviet field
regulations, not from retrospective American scholarship that hadn't
been published yet. This file is red-side modeling material and
authorial background — not something to put in a 1983 character's hands
or mouth.

**Documents** (shelf entries, reference/shelf.md lines 40-43):
- **Symposium** = Glantz (ed.), *1984 Art of War Symposium: From the Don
  to the Dnepr* (transcript of a CSI-hosted event with US and West
  German officers/historians, including Balck/Mellenthin-generation
  German veterans, discussing the winter 1942-43 Soviet campaign from
  Stalingrad through the Donbas/Kharkov counteroffensive-and-counterstroke
  cycle). 461 pp.
- **Storm-Strategic** = Glantz, *August Storm: The Soviet 1945 Strategic
  Offensive in Manchuria*, Leavenworth Paper No. 7 (Feb 1983). 260 pp.
- **Storm-Tactical** = Glantz, *August Storm: Soviet Tactical and
  Operational Combat in Manchuria, 1945*, Leavenworth Paper No. 8 (June
  1983). 215 pp.
- **1930s** = Glantz, *Soviet Operational Art and Tactics in the 1930s*
  (SASO/CSI, scanned OCR, badly garbled on Cyrillic-transliteration
  passages but the English prose extracts cleanly). 36 pp.
- **Kursk** = Glantz, *Soviet Defensive Tactics at Kursk, July 1943*,
  CSI Report No. 11 (Sept 1986). 72 pp.

---

## 1. Echelonment in practice: when and why second echelons commit

The symposium's case material (the Feb-Mar 1943 Donbas/Kharkov cycle) gives
a spread of real commitment windows, not a single doctrinal number — the
wargame's `ca_window_days` mechanic (echelon "spent" + a "gap" before the
next echelon/reserve arrives, `wargame/campaign.py:1194-1204`) should treat
commitment timing as **mission- and echelon-depth-dependent**, not fixed.

- **Day-3 commitment as a deliberate plan.** General Moskalenko's 40th
  Army (Kharkov operation) deployed four rifle divisions first echelon,
  one rifle division + one tank brigade second echelon, with the *plan*
  explicitly stating: "On the third day of the attack he would commit his
  second echelon forces as a mobile group to lead the army advance on
  Belgorod" (Symposium p. 241-242). This is second-echelon-as-scheduled-
  exploitation-force, not emergency reinforcement.
- **Day-1 commitment when the sector is narrow enough.** At Belgorod-
  Kharkov (Aug 1943), the Soviets used their new TOE tank armies "for
  the first time... at Belgorod-Khar'kov they used two such armies in
  tandem, committed to action on day one of the offensive in an
  extremely narrow sector (6 kilometers). This massive use of armor so
  early in the attack caught German commanders by surprise" (Symposium
  p. 394). Commitment window collapses to zero when the front is willing
  to mass on a very narrow frontage.
- **Mobile groups committed already under-strength.** Mobile Group Popov
  (Donbas, Feb 1943) — a corps-command-headquarters-controlled grouping
  of four tank corps, the direct WWII ancestor of the 1980s OMG concept
  (the term "operational maneuver group" itself does not appear in this
  WWII-focused symposium; "mobile group" is the period term) — "although
  hindered by shortages of fuel and ammunition, supported the... assaults.
  Popov's forces numbered 180 tanks at the time of their commitment to
  combat, thus each corps attacked in understrength condition" (Symposium
  p. 143). Commitment did not wait for full resupply; the group fought its
  way into the gap on what it had.
- **Directed minimum rates as a commitment condition, not just a march
  order.** 3d Tank Army's front commander's order specified the *rate of
  advance be maintained at at least 20-25 kilometers per day* (Symposium
  p. 244) as a condition of the plan succeeding — the commitment decision
  and the rate requirement were bound together, not separable knobs.
- **STAVKA-level echelon-depth doctrine, codified from failure.** Order
  #306 (Oct 1942) is cited in the symposium as the STAVKA's correction of
  the 1936 regulation's default two-echelon formation: commanders were
  "using too rigidly the pattern recommended in the 1936 regulation... in
  a rifle division only 9 companies of 27 would bring their firepower to
  bear." The order mandated single-echelon formation at every level from
  army through battalion "in order to generate maximum firepower forward"
  — in the rifle division, 18 of 27 companies forward instead of 9
  (Symposium p. 30). **Echelon depth is itself a doctrine variable the
  Soviets tuned by directive, not a fixed structural feature** — worth
  noting against the instrument's static echelon table.
- **Full deep-echelon architecture by 1943-45**, contrasted with the
  thin 1930/1941 formations (§5 below): by the Manchurian operation the
  Trans-Baikal Front ran tank formations in first echelon *and*
  tank-heavy forward detachments at every level of command down to
  division, "so the 6th Guards Tank Army would spearhead the front
  effort" (Storm-Strategic, PDF p. 89) — echelon and forward-detachment
  structure nested at every level simultaneously, not a single second
  echelon waiting in the rear.
- **Forward detachments as a distinct, graduated echelon-leading
  device**, distinct from the main second echelon: "One brigade led the
  advance of each corps as a forward detachment... [that] tank brigade
  was led by a forward detachment of battalion strength... itself a
  forward detachment of its parent corps and so on" (Symposium p. 367) —
  a *fractal* structure, each level fielding its own lead element, not
  one echelon "committing" at one moment. By 1943 this was doctrine:
  "the Soviets increased their use of forward detachments... to increase
  attack and pursuit tempos. Forward detachments would race ahead of
  main forces and secure key terrain features, river crossings, and road
  junctions, and hold them until the arrival of the main force" — but
  the technique's failure mode is named explicitly: at Belgorod-Kharkov
  "forward detachments tended to become overextended... the Germans
  smashed the relatively isolated forward detachments of 1st Tank Army"
  (Symposium p. 409-410).
- **The counterstroke's real-world "gap":** von Manstein's counterthrust
  against Vatutin's overextended 6th Army began 19 February 1943; "only
  by 28 February did the scope of the Soviet disaster finally become
  apparent to Vatutin and the STAVKA alike" (Symposium p. 262). A
  **nine-day recognition lag** between the counterstroke's start and the
  attacker's own high command grasping what had happened — the request
  for help (21 Feb) drew only a single division transfer, because the
  neighboring front had nothing to spare (p. 263). This is the best
  real-world analog in the set for the wargame's spent+gap mechanic: the
  gap that matters is not just red's reserve-arrival gap but the
  *defender's exploitation window before red's own command recognizes
  culmination* — a second clock the instrument doesn't currently run.

## 2. Rates and norms: planned vs. achieved

Cross-referencing reference/advance-rates.md (ORALFORE, WWII Western-Front
data: Category I "determined/intense" opposition averages 2.80 km/day
normalized, 1.32-4.04 range; FM 100-2-1's mid-80s planning norms cited
there as "up to 50 km/day anticipated... up to 30 km/day fighting through
defensive positions"). The Glantz cluster supplies the missing
**Soviet-attacker** data ORALFORE lacked (advance-rates.md §7, "no
Soviet-attacker operations... data unavailable"):

| Case | Planned/directed | Achieved | Source |
|---|---|---|---|
| Middle Don op, Jan 1943 | 30 km/day rifle, 70 km/day mechanized | "the latter figure was not inaccurate. However, the former... had to be revised downward" | Symposium p. 63-64 |
| 3d Tank Army, Feb 1943 (Kharkov) | ≥20-25 km/day (front commander's order) | slowed by German resistance at Veliki Burluk/Ol'khovatka within days | Symposium p. 244 |
| Belgorod-Kharkov counteroffensive, Aug 1943 (6th Gds Army sector, hard fighting) | — | **0.5 km/day** ("gains were measured by a half kilometer per day") | Symposium p. 374 |
| Trans-Baikal Front, Manchuria 1945 | 23 km/day combined arms, 70 km/day tank | (fast-collapsing Japanese resistance; see caveat below) | Storm-Strategic PDF p. 89 |
| 1st Far Eastern Front, Manchuria 1945 (dense fortified zone) | 8-10 km/day | — | Storm-Strategic PDF p. 92 |
| 1st Red Banner Army, Manchuria 1945 | 8-10 km/day (150-180 km / 18 days), "up to 100 km/day in good terrain" per note | achieved on schedule per plan | Storm-Tactical PDF p. 48 |
| 39th Army, Manchuria 1945 (Grand Khingan crossing) | 50-60 km/day | **40 km/day** sustained ("the audacity of the plan itself" strained C2 but the rate held); tank/tractor elements 50-80 km/day | Storm-Tactical PDF p. 142, 154-155, 159 |
| 15th Army + Amur Flotilla, Manchuria 1945 | — | 210 km / 7 days = **30 km/day**, "over appalling terrain" | Storm-Tactical PDF p. 190 |

**Reading across the table**: the Manchuria numbers (achieved rates near
or even exceeding plan, 30-40 km/day sustained over multiple days against
difficult terrain) are the historical ceiling *because Japanese resistance
had functionally collapsed* — this is ORALFORE's Category II-B/III
territory (negligible/administrative, 35-70+ km/day), not a NATO-caliber
defended-zone case. The Belgorod-Kharkov 0.5 km/day figure, by contrast,
sits below even ORALFORE's Category I-A floor (1.32 km/day) — determined
German defense in 1943 could stop a directed Soviet advance cold. **The
same Soviet army, in the same war, produced both numbers depending
entirely on what the defender did** — exactly ORALFORE's threshold-not-
ratio finding (advance-rates.md §1), now confirmed from the attacker's
own side and against a real WWII opponent, not the German 1940 or 1944
cases ORALFORE used. A red planning cell writing "50 km/day" into a plan
and a red army achieving "0.5 km/day" against determined defense are both
period-authentic — the gap between them is the scene, as advance-rates.md
already flagged for FM 100-2-1's norms (open items, "a red plan written
at 30 meeting ground that pays 10 is a scene, not just a parameter" — the
Glantz cluster shows the gap can run two orders of magnitude wider still).

## 3. Logistics coupling: operational pauses, culmination, resupply

- **The deliberate no-pause gamble, STAVKA-directed.** The Donbas
  operation ("Skachok"/Gallop) was planned under explicit STAVKA guidance
  that "the operations be conducted without an operational pause in order
  to deny the enemy time to erect fortified defensive positions" (Symposium
  p. 123) — the pause/no-pause decision is presented as a conscious
  trade of logistics risk against denying the defender recovery time, made
  at STAVKA level, not emergent. The follow-on Voronezh Front offensive
  repeated the choice against already-attrited forces: STAVKA "planned to
  continue the offensive westward virtually without an operational pause...
  willing to undertake a calculated risk that its forces, already worn
  down by a month of fighting" could still produce a "final inexorable
  collapse" (Symposium p. 230).
- **The bill for skipping the pause.** The subsequent Kharkov operation
  (Feb-Mar 1943) "began with virtually no operational pause and with the
  absence of any systematic regrouping or thorough resupply of forces.
  Moreover, supply bases remained 250-300 kilometers to the rear, making
  logistical support throughout the operation tenuous at best. Front
  mobile units were well below full strength (3d Tank Army — 165 tanks)"
  (Symposium p. 287-288). This is the historical basis for the model's
  pulse/pause supply logic under stress: skipping the pause is a real,
  named doctrinal choice with a documented cost (understrength mobile
  formations, tenuous resupply at 250-300 km), not a modeling artifact.
- **The pause, when taken, is credited with real command development.**
  "The four month operational pause after March of 1943" is cited as one
  reason Soviet operational leadership matured — tank brigade commanders
  of 1941-42 becoming tank army commanders by war's end (Symposium
  p. 411). An operational pause is not pure loss in this material; it
  buys leadership consolidation the model doesn't represent.
- **Logistics as the explicit strategic risk accepted at the top**, in
  the Manchurian case: "the operation relied heavily on the ability of
  logistical units to supply the fast moving columns deep in Manchuria.
  The Soviets confidently took both risks [Japanese reaction speed and
  logistics]" (Storm-Strategic PDF p. 89) — a front-level plan that
  named its own logistics gamble in writing, matching consumption-
  factors.md §5's framing of Soviet resupply as a "quota, not a demand
  forecast": the plan assigns risk, it doesn't forecast a shortfall and
  hedge against it.
- **Even under-supplied, mobile groups fought rather than waited**: Popov's
  group committed "hindered by shortages of fuel and ammunition" rather
  than delaying for a full refill (Symposium p. 143, §1 above) — a data
  point against treating `red_resume_fill = 1.0` (consumption-factors.md
  §5, CAL-4) as a hard gate; historically the threshold bent when the
  operational timetable demanded it.

## 4. Deception/maskirovka and warning

The strongest material in the cluster on this axis is Storm-Strategic's
treatment of the Manchurian operation's strategic surprise — directly
useful for calibrating the wargame's warning-time `W` parameter
(notes/wargaming-findings.md, 90-hour-clock entry) with a case where
warning approached **zero** despite a large, detectable buildup:

- **Compartmentation by written order, not just practice.** The
  planning directive itself specified: "The Front commander, the member
  of the Military Council, the Front chief of staff, and the chief of the
  Front staff operations department are to be allowed to take full part
  in working out the plan... Chiefs of the branches and services may be
  allowed to take part in working out their special sections... without
  being informed of the Front's general objectives. The army commanders
  are to be told their objectives orally without passing on written Front
  directives... All documents... shall be kept in the personal safes of
  the commander of the Front and the commanders of armies" (Storm-
  Strategic PDF p. 168-169). Deception here is procedural/administrative,
  not camouflage.
- **Movement discipline as deception**: "Unit after unit deployed for
  attack from assembly areas twenty to eighty kilometers to the rear and
  entered from the march. The 6th Guards Tank Army conducted a major
  march and crossed the border without halting in final assembly areas"
  (PDF p. 168) — no forward staging pause for units to be detected in;
  the approach march *was* the attack.
- **A tight, late go/no-go decision cycle**: "On 2 August the Far East
  Command assigned frontal designations to force groupings and told all
  forces to achieve full combat readiness by 9 August. At 1630 on 7
  August, Far East Command made the final decision on timing for an
  attack that would occur less than two days later" (PDF p. 169) — under
  48 hours between final decision and H-hour, on top of a compartmented
  plan.
- **The defender's own analysts had the right instinct and were
  overruled by institutional complacency**: "Most Kwantung Army
  intelligence agencies assessed the Soviets would not conduct major
  operations until the fall of 1945... Among the few relatively accurate
  assessments was that of the Japanese 4th Army commander, General
  Uemura, who warned of a Soviet attack occurring as early as August 1945
  and had his subordinate units prepare for that eventuality. Japanese
  complacency, however, smothered most warnings" (PDF p. 169). This is a
  clean W-parameter case: one correct forecast existed in the system and
  was outvoted; on the night of the attack, senior Japanese commanders
  (including the Kwantung Army commander himself) were away from their
  posts at a planning conference or on travel (PDF p. 169-170) — command
  presence, not just intelligence, collapsed at H-hour.
- **A separate, tactical-surprise mechanism from the German side of the
  ledger**: Mellenthin's own symposium commentary (he co-wrote *NATO
  Under Attack* with Stolfi) makes a doctrinal claim directly relevant to
  the counterstroke-window mechanic: "Russian commanders and soldiers
  appeared incapable of coping with surprise during World War II... Of
  greatest importance for NATO, the Russians tended toward dissolution
  and panic when confronted with unexpected counterattacks" (Symposium
  p. 417) — offered as a lesson *for NATO*, i.e., this is the period's
  own doctrinal argument for why a small, well-timed counterstroke should
  outperform its force ratio against a culminated Soviet echelon. He
  illustrates it with a 12-hour action: a "childishly small" German
  battlegroup (20 tanks, one recon company, one mechanized infantry
  battalion, one SP-artillery troop) restored a broken sector at Akhtyrka
  (Aug 1943) "due primarily to surprise... the Russians had thought
  [the corps] was tied down... the appearance of our tanks... came as a
  complete surprise. Initial resistance was negligible... the Russians
  withdrew in panic" (Symposium p. 417-419). Treat with the same caution
  the project already applies to German-authored source material generally:
  this is a German veteran's self-assessment of his own war-winning
  technique, at a US Army-hosted symposium in the AirLand Battle era,
  audience of NATO officers looking for exactly this lesson — the
  incentive to overstate is structural, not just anecdotal. It is real
  evidence of a real 1943 action; it is also a data point selected and
  narrated for a receptive audience.
- **On the offense side, deliberate deception paid off in the same theater
  the symposium centers on**: at Belgorod-Kharkov, "during the preparation
  phase, the Soviets made widespread use of deception. Careful Soviet
  planning of the initial penetration operation paid dividends" (Symposium
  p. 394) and separately, before Kursk, "the Soviets claimed to have
  created near the Suzhda area by dummy radio communications a fake tank
  army and a concentration of rifle forces... that concentration drew the
  attention of the Germans away from this area" (Symposium p. 366) — a
  named maskirovka technique (radio-deception order of battle spoofing),
  offered with the caveat that the transcript speaker only has "German
  sources that confirm it," i.e., corroborated but not from the Soviet
  archival side.

## 5. Brief: two lineage sections

### 5a. Deep-operations origins (1930s)

- Tukhachevsky and Triandafillov's 1929 theoretical baseline: "only
  successive operations over a month's time to a depth of 150 to 200
  kilometers could produce victory" (1930s p. 5) — deep battle/deep
  operations as the answer to WWI-style attrition, built around using
  tanks-with-air-support to punch through the tactical zone into
  operational depth.
- The 1929 numbers that matter for calibrating "what a Soviet planner
  thought was realistic" a full half-century before the setting: a front
  attacking on a 300-400 km sector to 200 km depth; an army on a 50-80 km
  sector to 25-30 km depth; each operation lasting 5-6 days at a
  **planned 5-6 km/day** rate of advance in 1929, which the theorists
  explicitly intended to raise to **25-30 km/day** once tanks and
  mechanized vehicles were fielded (1930s p. 5-6). This is the
  doctrinal ancestor of every later "30-50 km/day" planning-norm figure
  in the cluster (§2 table) — the number moved from horse-cavalry-era
  5-6 km/day to mechanized 25-30 km/day within the same decade, on paper,
  before most of the hardware existed to test it.
- The theory (deep battle/deep operations) preceded the practice by
  years: "By 1929 the theory... was fully developed" but "deep battle was
  but a promise whose realization depended on economic reform and
  industrialization" (1930s p. 6) — a caution about reading any Soviet
  planning-norm number as demonstrated capability rather than aspiration,
  a caution that generalizes forward to the 1980s FM 100-2-1 norms
  advance-rates.md already flags.

### 5b. Echeloned defense at Kursk (brief)

- **The mature (1943) multi-belt architecture**, at the point the Soviets
  had learned the lessons of 1941-42: tactical defense zone = combat
  security belt (1-2 km forward of the main belt) + main defensive belt
  (6 km deep, division sector 8-12 km wide, two-echelon regiments) + rear
  defensive belt (12-15 km deep) — the *1930-vintage* formal doctrine
  (Kursk p. 2), which by summer 1943 had evolved into something deeper
  still: rifle corps deployed two divisions in the first tactical belt,
  one in the second; a first-echelon division defended 8-15 km wide to
  5-6 km deep, backed by antitank strongpoints/regions "throughout the
  entire depth of the defense" and mobile obstacle detachments (Kursk
  p. 12-13).
- **The full operational-to-strategic depth actually built for Kursk**:
  Central and Voronezh Fronts each ran three army defensive belts,
  *plus* two additional front defensive belts behind those, backed by
  the Steppe Front as strategic reserve (five combined-arms armies, one
  tank army, three tank corps, three mechanized corps, three cavalry
  corps, 1,600+ tanks) explicitly to "ensure that no German operational
  penetration would occur and... provide strength for planned Soviet
  counterattacks" (Kursk p. 26). This is the historical maximum case for
  "defense in depth defeating a set-piece attacker" — worth remembering
  as the ceiling, not the norm, when the book or the model reaches for a
  Soviet-defense analog (LANDJUT's actual defense is nothing like this
  scale; the contrast is the point).
- **The pre-1943 baseline it replaced** was thin by comparison: in
  1941, forces were "forced... to deploy in single-echelon defensive
  formation with a depth of only 3 to [a few] kilometers... dictated by
  the limited forces available and wide defensive zones. This resulted
  in inadequate tactical... depth of the defense" (Kursk p. 4-5) — the
  1943 Kursk system is the corrective, built over eighteen months of
  costly single-echelon failure, not a doctrine the Soviets started the
  war already holding.

## Consequences for the instrument

1. **`ca_window_days` (spent + gap counterstroke window) is under-specified
   against the historical range.** The Manstein counterthrust case gives
   a real gap of at least 9 days between an attacker's culmination
   (overextension began ~19 Feb) and the *defender's own high command*
   recognizing it (28 Feb) — during which period the counterstroke was
   already running. If the model's window represents only "time before
   red's next echelon plugs the gap," it is answering a narrower question
   than the historical case, which also includes a command-recognition
   lag on red's own side. Consider whether the mechanic should separate
   "reserve arrival gap" from "red command recognizes the gap" — two
   different clocks in the Manstein case, currently one in the model.
2. **Echelon commitment timing is not one number; it is mission-shaped.**
   The symposium shows day-1 (narrow-sector massed armor), day-3
   (scheduled exploitation force), and immediate-but-understrength
   (Popov, committed short on fuel/ammo rather than waiting) all as real
   plans within the same six-week campaign. If the wargame ever
   parameterizes "which day does red's second echelon commit," it should
   be a distribution or a scenario input, not a constant — and forward
   detachments commit *earlier and more granularly* (fractal, down to
   battalion) than the second echelon proper, a distinct entity the
   current echelon table may be collapsing together.
3. **The rates table (§2) sharpens, rather than resolves, the CAL-A/CAL-C
   tension already logged in advance-rates.md.** The Manchuria data shows
   Soviet-planned rates (50-60 km/day) achieved almost exactly (40 km/day)
   under *negligible* opposition — supporting the existing high end of
   the model's unopposed rate. The Belgorod-Kharkov 0.5 km/day figure is
   lower than any ORALFORE cell and confirms CAL-B's `pressure_kmd = 4.0`
   is, if anything, generous against truly determined defense — the
   resistance-intensity ladder (advance-rates.md CAL-C) should treat "0.5
   km/day" as a real, citable floor for the "screened/determined" band,
   not just a modeling extreme.
4. **The no-operational-pause gamble is a named, top-directed choice with
   a documented logistics bill** (250-300 km supply-base distance,
   understrength mobile formations) — this strengthens consumption-
   factors.md CAL-4's framing of red's demand as "a quota system" whose
   starvation "should bite between assigned efforts": here it bit
   *because* the STAVKA chose to skip the gap between efforts, which is
   exactly the pulse/pause mechanic's decision point, now with a named
   historical instance on both sides of the choice (Skachok = pause
   skipped, deliberately, twice in one winter; the four-month 1943 pause
   afterward = the recovery the model's resume logic represents).
5. **Warning-time (`W`) calibration gets a near-zero-warning anchor with
   named mechanism**, not just a number: written compartmentation orders,
   march-to-contact without forward staging, and a correct warning
   overruled by institutional complacency (Kwantung Army). This is a
   different *kind* of warning failure than the 90-hour-clock finding's
   political-warning-band framing (FE doctrine's 48h-8-day political
   window) — it is a case where the warning signal existed inside the
   defender's own system and was suppressed by institutional bias, not a
   case of no signal at all. Worth a distinct W-scenario: "warning existed,
   was disbelieved" vs. "no signal reached anyone," since the wargame's W
   sweep currently treats warning as a single scalar.

## Open items

- **Most of the symposium's 461 pages are unmined.** This pass followed
  echelonment/rate/pause/deception grep hits; the discussion-and-Q&A
  sections (where symposium principals debated each other directly,
  likely the richest "operational art argued by the principals" material
  per the task brief) were not systematically read — only the passages
  the keyword search surfaced. A second pass reading the introductory
  and closing synthesis remarks in full (not yet located precisely) is
  the natural next increment if more is wanted.
- **Storm-Strategic and Storm-Tactical**: read for echelonment/rates/
  logistics/warning terms only. Neither paper's treatment of the Kuril
  Islands/southern Sakhalin amphibious operations, nor the bulk of the
  Trans-Baikal Front's own advance (as opposed to 39th Army and 1st Red
  Banner Army, which is what the grep hits surfaced), was read.
- **1930s document**: only pp. 2-15 of 36 were read (the deep-operations
  theoretical baseline). The back half — mechanized corps disbandment
  (1939-40), the Nomonhan/Khalkhin-Gol experience, and the doctrinal
  effect of the officer purges — is directly relevant to "why 1941 forces
  fought in the thin single-echelon formation Kursk's opening section
  describes" but was left unmined per the "brief section only"
  instruction.
- **Kursk document**: only pp. 2-15 and 26 of 72 were read (the belt
  architecture and the overall Kursk order of battle). The tactical
  narrative of the actual German penetration attempt, the Prokhorovka
  battle, and the report's concluding lessons-learned chapter are unread.
- **PDF-page-vs-printed-page offset for the two Storm papers was found
  inconsistent** (11 at one point, 8 at another in Storm-Tactical) —
  likely photo-plate/map pages breaking the printed sequence without a
  PDF-page match. All Storm citations above are therefore given as PDF
  page numbers (reproducible via `pdftotext -layout`), not the documents'
  own pagination; a future pass wanting the "true" printed page for a
  specific citation should check the nearest embedded page-number string
  directly rather than trust a computed offset.
- **No cross-check yet against Bogason or the CIA WP-planning papers**
  (already on the shelf, reference/oob-verification.md,
  reference/zealand-landing.md) for whether the GDR 5th Army / Polish
  Küstenfront axis this project actually uses would have run WWII-style
  forward-detachment/mobile-group echelonment or the later, more
  OMG-explicit 1980s construct — that synthesis (does this file's WWII
  material actually describe LANDJUT's opposing axis, or a different
  echelonment culture) is not attempted here and is the natural next
  question for whoever picks this up.
