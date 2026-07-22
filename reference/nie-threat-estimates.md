# NIE threat estimates mined: the Baltic/northern-flank picture as the US IC held it

*Mining pass 2026-07-22. Four declassified estimates, held as scans with no
text layer (`pdftotext` returned nothing — `pdffonts` confirms zero embedded
fonts, i.e. pure image PDFs). OCR'd via `ocrmypdf --force-ocr` + tesseract
5.5.2 (not previously on this box; pulled through `nix-shell -p tesseract`)
to produce searchable sidecars; quality is good but not perfect (a scattering
of misread characters, tracked below where they touch a load-bearing word).
Every claim below cites the document, its own paragraph number (¶, the
estimate's internal numbering — reliable across editions), and a PDF page
number computed from the scanned page count (labeled "PDF p." throughout,
since the scan's page 1 is the cover and does not match any printed
pagination the document itself carries in places). Redacted passages are
marked **[REDACTED]** where the OCR shows a bracketed gap in running text;
these are the sanitization gaps and are not filled in.*

*Companion files: `reference/landjut-front.md` (the front's command
architecture and blue OOB), `reference/oob-verification.md` (the
archive-era ground truth — Lautsch's Küstenfront/covering-force
architecture), `reference/zealand-landing.md` (the amphibious/Zealand
story in full, already mined from these same four documents for that
narrower question — this file does not re-derive the amphibious material,
it cross-references it). Post-1990 scholarship is for us, not for
characters (shelf discipline) — none of what follows was available to a
1983 LANDJUT staff officer; see "Epistemic chain" below.*

## The documents

| Document | Date / info-as-of | Held scope | PDF pages |
|---|---|---|---|
| NIE 11-14-79, *Warsaw Pact Forces Opposite NATO* | 31 Jan 1979 | **Volume I — Summary Estimate only** (title page states this explicitly); Volume II, the detailed doctrine/OOB/trends volume, is not held | 97 |
| NIE 11-14-81, *Warsaw Pact Forces Opposite NATO* | 7 Jul 1981; info as of 30 Jun 1981 | Appears self-contained (no "Volume I/II" language anywhere in the text) — the fullest single-document estimate we hold | 38 |
| NI IIM 83-10002, *Employment of Warsaw Pact Forces Against NATO* | "est. pub. date" on cover; info as of 1 Apr 1983 — internally dated **July 1983** by a cross-reference in NIE 11-14-85 ¶185 fn.7 | Drafted as a would-be third volume to NIE 11-14-81 to cover front-level employment concepts in the detail Volume II would have carried; issued instead as its own IIM. Sanitized — several bracketed redactions in running text | 19 |
| NIE 11-14-85/D, *Trends and Developments in Warsaw Pact Theater Forces, 1985-2000* | September 1985 | **Not an employment estimate.** Its own Scope Note (PDF p.7) disclaims doing a "traditional multivolume NIE" and names sibling documents — NIE 11-19-85 (*Soviet Capabilities for Multitheater War*) and NIE 11-15-85 (*Soviet Naval Strategy and Programs*) — as carrying the operational/naval detail. We hold none of those siblings. This is a force-trends/projections document; its Baltic/Denmark content is what leaks through incidentally | 110 |

**Setting note.** The setting is provisionally Nov 1983 (per CLAUDE.md /
planning/setting-time.md). NIE 11-14-81 and NI IIM 83-10002 are the
**setting-adjacent pair** — the picture the IC held in the setting year (81
current to mid-1981, the IIM current to spring/summer 1983, i.e. months
before/around the setting). NIE 11-14-79 shows where the picture was
drifting from. NIE 11-14-85 is **post-setting — "for us," not for
characters** — but shows where the picture kept drifting *to*, which is
useful for grading how far ahead of the IC the archive-era ground truth
(Lautsch, writing the actual plan 1983-86) really was.

## 1. NIE 11-14-79 (Vol I, 31 Jan 1979)

### The Baltic/northern axis picture

The Northern (Polish) Front appears by name in the TVD organization
chart (Figure 15, PDF p.59) and gets a dedicated description at ¶127
(PDF p.66): *"The Polish Front, upon breaking through initial defenses
in its area, would be responsible for advancing both into Denmark and
across northern Germany into the Netherlands."* The naval section is
explicit that the front, "composed primarily of Polish forces, but with
the support of the Combined Baltic Fleet, would be responsible initially
for capturing northern West Germany and Denmark" (¶137, PDF p.69).

Employment concept, land axis: air superiority and sea control first
(¶138-141, PDF pp.69-70), then "Pact forces in the Baltic would then
concentrate on supporting the Polish (Northern) Front's offensive across
northern West Germany and into Jutland" (¶142, PDF p.70). Amphibious/
airborne landings against the Danish islands, especially Zealand, are
described as necessary to deny NATO Baltic naval use and enable a
subsequent move on southern Norway; Bornholm gets an early, separate
airborne/amphibious neutralization operation against its SIGINT
facilities (¶142, PDF p.70) — see `zealand-landing.md` for the full
amphibious distillation, not repeated here.

Assault composition named at ¶143 (PDF p.70): Soviet Baltic Fleet naval
infantry regiment, the Polish sea-landing division, a specially-trained
regiment of an East German motorized rifle division for the initial
wave; a Polish mechanized division (partially amphib-trained) and
Soviet motorized rifle divisions from the USSR for follow-on; a Polish
airborne division (and "perhaps Soviet airborne troops") coordinated
with the amphibious landings. Note: **no distinction is drawn here
between a thin covering force and the Polish front's main striking
echelon** — the document reads as if the Polish front itself is the
first-echelon attacking formation on the axis, arriving and breaking
through in one continuous action, not as a follow-on echelon passing
through a prior GDR/Soviet screen. See the ledger below.

### Warning-time judgments (verbatim-ish)

This volume does not carry its own numeric NATO-warning-time estimate;
it repeatedly points to a sibling document for that judgment — **NIE
4-1-78**, *Warsaw Pact Concepts and Capabilities for Going to War in
Europe: Implications for NATO Warning of War* (cited in the preface,
PDF p.9: *"assesses Pact attack options in Central Europe and the
intelligence basis for our estimate of NATO's warning time there"*) —
which we do not hold. Flagged as an open item below.

What this volume does give, quantified: Pact division readiness
categories. ¶25 (PDF p.35): divisions in the Soviet Groups of Forces in
Eastern Europe plus eight NSWP divisions "are manned close to wartime
strength... and can be brought up to strength and ready to move within
**24 hours**. Other active Soviet and NSWP divisions have lower
manpower and equipment levels, and can be mobilized and begin movement
for combat within **72 hours**." ¶26 (PDF p.36) adds that army/front-
level and especially rear-service formations "require longer to
mobilize than the combat units which they support," and that
significant portions of wartime rear services "do not exist in
peacetime" and would have to be mobilized from the civilian economy —
a structural reason NATO's warning would come disproportionately from
watching support and logistics generation, not front-line divisions.

### Non-Soviet reliability judgment

¶102 (PDF p.58, pre-Solidarity — this is a 1979 document): *"We have
considered the question of whether the Soviets could rely on their
Warsaw Pact allies to participate willingly and effectively in
hostilities against NATO and have concluded that no categorical answer
is possible... In sum, the East Europeans would feel they had little
choice but to fight on behalf of the Pact."* ¶119 (PDF p.63) is blunter
about the stakes riding on this judgment: *"While the Soviets regard
most of their allies with habitual distrust... the Soviets have
nevertheless entrusted their allies to carry out wartime functions
potentially critical to the Pact's prospects... the Soviets count on
attacks by Polish units in the north and Czechoslovak units in the south
to tie down large NATO forces."* No Solidarity-era doubt yet — this is
the baseline the 1981 document visibly reacts against.

## 2. NIE 11-14-81 (7 Jul 1981, info as of 30 Jun 1981)

The setting-adjacent document, and the sharpest of the four on the
question the book needs: **what happens to the Polish-front plan when
Poland itself looks unreliable.** Written five months before martial
law (13 Dec 1981) but squarely inside the Solidarity crisis (August
1980 strikes, the free trade union's legalization, an entire year of
Polish political crisis by the estimate's date).

### The Baltic/northern axis picture

¶57 (PDF p.29-31) restates the three-front architecture (Soviet-East
German, Polish, Czechoslovak-Soviet) and gives the clearest **warning-
time-linked force-generation judgment in the whole set**: *"Although a
war between NATO and the Pact could begin in any number of ways, it
probably would be preceded by an extended period of rising tension
during which both sides would take steps to improve their forces. How
long this period would extend is not possible to predict, but **if it
lasted as long as two weeks, the Pact would have time to prepare the
five fronts noted above and move them into Eastern Europe**. This would
provide a force of 80 to 90 ground divisions plus support and tactical
air units."* This is the clearest headline warning-time judgment across
the four documents: a **two-week** period of tension is what the IC
credited as sufficient for the Pact to fully form its opening-campaign
force structure (not the launch trigger, the *build-out* clock).

¶58 (PDF p.31): *"The Polish front would attempt to defeat NATO forces
in northern West Germany with an ultimate objective of seizing Denmark
and the Netherlands."* ¶60 (PDF p.32): naval operations in the Baltic
"conducted in the context of the overall campaign... particularly the
ground and air operations of the Polish front," with the Baltic Sea
force concentrating on "supporting the Polish front's offensive across
northern West Germany and into Denmark" once sea control/air
superiority is won.

### Warning-time judgments

Beyond the two-week force-generation figure above (¶57), ¶20 (PDF p.17)
gives the standing force base against which that build-out happens: 163
active Pact divisions arrayed against NATO in peacetime, with "18
additional divisions" drawable from the active forces in the western
USSR and "27 reserve divisions — 16 Soviet and 11 NSWP" mobilizable on
top of that. The two-week judgment is thus specifically about closing
the gap from 163 standing divisions to the full 80-90-division,
five-front opening array — not about detecting the war's first move,
which (per the readiness-category logic inherited from 1979) would
already be visible in as little as 24-72 hours at the division level.

### Non-Soviet / Polish reliability judgment — the direct hit

This is the document's most important passage for the book. Key
Judgments front matter (PDF p.7): *"Greater uncertainty about the
reliability of their East European partners, a perennial issue made
more pressing by **recent developments in Poland**."* ¶59 (PDF p.31),
in full: *"The success of the Pact's apparent planning for a campaign
in Central Europe depends to a considerable degree on the performance
of the NSWP forces involved in these fronts. **Recent events in Poland
have provided new reasons to question the potential reliability of
these forces** and we expect that the Soviets could be planning to
shoulder a larger portion of the burden in a Central European
offensive, particularly in the northern part of Germany. Poland
continues to bear the principal responsibility for prosecuting the
northern axis of advance and for facilitating the movement of Soviet
reinforcements toward West Germany. We have no evidence that the
Soviets have decided to relieve the Poles of these responsibilities, but
we believe that alternative plans must have been considered. **One
option that has been tested in Pact exercises is to bring forces forward
from the USSR's Baltic Military District to conduct operations in
conjunction with the Polish armed forces.**"*

The closing Conclusions section (¶70, PDF p.35) generalizes this to a
strategic-level worry: *"Potentially the most threatening problems for
the USSR, however, are political. The question of the reliability of
the non-Soviet Warsaw Pact countries in a war with the West has always
been present; recent events in Poland have made it even more pressing...
The validity of this strategy has been made doubtful as a result of the
current situation in Poland and whether the course of political
liberalization in that country continues or **Moscow finally intervenes
to suppress it**, the outlook for the reliability of its East European
cohorts cannot be comforting to the leadership of the Soviet Union."*

This is a document watching martial law arrive in real time (five
months out) and reasoning explicitly about the specific axis this book
is set on — the axis's striking force being exactly the ally whose
reliability is collapsing. Note what the IC does *not* do here: it
floats a hedge (Baltic MD reinforcement of the Poles) but never
reaches for the actual mid-80s fix (a thin GDR/Soviet covering force
holding the border while the Polish front approaches and the front's
own composition shifts toward more Soviet weight over time, per
Lautsch — see the ledger).

## 3. NI IIM 83-10002 (info as of 1 Apr 1983; "July 1983" per NIE 11-14-85 cross-ref)

The other setting-adjacent document — closest in date to a Nov 1983
setting of anything held. Short (19 pp.), written explicitly to supply
the front-level employment detail NIE 11-14-81 lacked (having been
issued as a single volume rather than the planned two).

### The Baltic/northern axis picture

The Polish Front section (PDF p.12, immediately following the
Soviet-East German Front description in the Summary's Western TVD
walkthrough) contains a
**redaction directly in the load-bearing sentence**: *"The Polish
Front[REDACTED]in the northern part of West Germany. [REDACTED],
however, Polish armies have been used as exploitation forces in the
central part of West Germany. In its more common role, this front most
likely would consist at least of **two — and probably three — Polish
armies plus an East German army**. It would be responsible for moving
along the northern coast, up the Jutland Peninsula, and west toward the
Netherlands. This front most likely would be reinforced by the Soviet
Baltic Front."* The redaction sits exactly where the source/method for
the "sometimes used as exploitation forces in the central sector"
claim would have been — flagged, not filled in.

This is the most precise numeric Polish-front composition the four
documents give: **two-to-three Polish armies + one East German army**,
reinforced (unclear timing) by a "Soviet Baltic Front." Compare directly
against the archive-era finding in `oob-verification.md`: Lautsch's
Küstenfront (Coastal Front) was **three Polish armies plus one air
army** — the IIM's "two-to-three armies" band brackets the true figure
correctly, and its "Soviet Baltic Front" reinforcement guess is a
plausible if unconfirmed proxy for what turned out to be the attached
94th Guards Motor-Rifle Division plus (from 1985) the Soviet 16th
Army/Unified Baltic Fleet taking the Zealand mission. First-echelon
composition (PDF p.12): "About half of the first echelon would be
composed of East European forces" across all three fronts, i.e. this
document has the Polish front's ground force *as the first echelon on
the axis*, not as a second wave behind a covering screen.

Naval (PDF p.13): "The Combined Baltic Fleet also would support
amphibious assault operations in support of ground force operations
against Denmark and West Germany" — brief, deferring detail to the
naval discussion; see `zealand-landing.md`.

### Warning-time judgment

The only quantified figure in this document is nuclear-readiness, not
general-force warning, and it is short: *"With two days' preparation,
probably taking place during the prehostilities phase, a front's
nuclear strike assets could achieve states of readiness that would
permit the launching of a maximum number of strikes**[REDACTED]**in a
minimum amount of time**[REDACTED]**after receiving the order"* (PDF
p.11). Two redacted quantities sit exactly where the strike-count and
timing figures would be — flagged. This is a **2-day** readiness clock
for nuclear forces specifically, materially shorter than the 1981
document's 2-week force-generation figure for the conventional
build-out — the two numbers describe different things (nuclear alert
posture vs. full theater force assembly) and should not be conflated.

### Non-Soviet reliability judgment

No dedicated Polish-reliability discussion survives in this short
document at all — it is focused on employment mechanics, not the
political judgment, and Poland's reliability specifically is not named
anywhere in the 19 pages. The closest the document comes is a hedge on
Romania (PDF p.14, Southwestern TVD): *"It is not clear what role
Romanian forces would have in wartime. Generally, the Romanians have
balked at any participation other than homeland defense... The role
depicted for Romanian forces [REDACTED] is that of a second-echelon
front responsible for rear area security behind the Soviet and
Bulgarian fronts."* This is thinner than 1979's parallel passage on the
same ally (NIE 11-14-79 ¶165, PDF p.75: *"Romanian reliability is thus
a key to sustained Pact offensive operations in the area"*) — the IIM
doesn't even use the word "reliability." Given the IIM's date (spring/
1983, past the worst of martial law's initial shock, Solidarity banned,
Jaruzelski's government installed), the complete silence on Poland
specifically may itself be a data point — either the reliability
question had been "answered" for planning purposes by the imposition of
martial law, or this document's narrower scope (employment mechanics,
not political risk assessment) simply never carried it. Flagged as an
open item; do not read this silence as an IC judgment that the Polish
reliability question had gone away — the 1985 document (below) shows
it hadn't, just reframed.

## 4. NIE 11-14-85/D (Sept 1985) — post-setting, "for us"

### The Baltic/northern axis picture

Much thinner than the earlier three, consistent with the Scope Note's
disclaimer that this is a trends/projections document, not an
employment estimate. The Küstenfront/Polish-front architecture is not
walked through as a named front at all in the material we hold; the
Baltic axis appears mainly through force-generation and naval-force
tables. ¶211 (PDF p.72): *"The NSWP navies also would contribute
amphibious forces for landings on the **Jutland Peninsula** and the
Turkish Straits"* — the Jutland target survives unchanged from 1979,
but there is markedly less land-axis employment narrative than the
earlier documents carried. ¶185 (PDF p.63) footnotes NI IIM 83-10002
directly for "a complete discussion" of Baltic naval operations —
i.e., the 1985 document is explicitly deferring to the *setting-year*
document rather than updating it, which is itself informative: the
land-axis employment concept the IC held in 1985 was, per its own
footnote, still the 1983 picture.

### Warning-time judgments — the clearest drift in the set

This is where 1985 earns its "for us" status: the warning-time picture
has visibly lengthened relative to 1979/81. ¶131 (PDF p.52): *"the
Soviets do not have any 'full-strength ready' (NATO category A1) tank
and motorized rifle divisions opposite NATO. Such divisions would
require no mobilization and would be ready for offensive operations
within 24 to 48 hours after an alert. Instead, even opposite NATO's
Central Region, the Soviets would need to mobilize over 40,000
reservists to man their ready combat divisions alone... The most ready
Soviet divisions in Eastern Europe now fall into the second readiness
category (NATO category A2) and... would probably need **five to seven
days** to achieve full strength and combat readiness."* The paragraph's
conclusion is explicit and IC-confidence-raising: *"these adverse
readiness trends make it increasingly less likely that the Soviets
would plan to mount a sudden attack without warning against NATO... Growing
requirements to augment forward-area Soviet forces with reservists also
should provide NATO with early strategic warning of increased combat
readiness in Eastern Europe."*

¶59 (PDF p.22) makes the same point at the command-architecture level:
new peacetime TMO high commands ease the Pact's wartime transition, but
*"Our ability to warn of a major military move... depends primarily on
observation of the many steps required to prepare large combat
forces... Consequently, the activation of the permanent TMO high
commands does not, by itself, reduce our confidence in our overall
ability to provide warning of war."*

Read against 1979's 24hr/72hr per-division figures and 1981's two-week
full-force-generation figure, 1985 shows the IC's warning-time
confidence **increasing**, not eroding, over the period — driven by a
judgment that Soviet manpower/readiness trends (declining active-duty
category-A1 strength, growing reliance on reservist call-up) were
making a short-notice attack structurally harder for the Pact to
mount, not by any specific new collection source. This is the single
clearest piece of estimate *drift* across the four documents and feeds
the instrument's W parameter directly (see below).

### Non-Soviet reliability judgment — the softening

The Solidarity-era alarm of 1981 is not repeated in the same key. ¶40
(PDF p.20): *"The Soviets apparently have in place with most East
European forces a system that effectively places the NSWP forces under
Soviet control from the outset of hostilities... the East Europeans can
generally be relied on to play roles that they have been assigned and
have trained for, at least early in any NATO-Pact conflict."* ¶41
immediately following: *"Soviet fiat, however, cannot close the widening
gap between modern Soviet forces in Eastern Europe and those of Soviet
allies. This disparity in combat potential is **most pronounced in
Eastern Europe's southern tier and in Poland**. It will probably lead to
operational adjustments in Soviet plans against NATO in the years
ahead."* Poland is still named, but reframed from a *political-
reliability crisis* (1981's language: "Moscow finally intervenes to
suppress it") to a routinized *combat-potential/equipment gap* alongside
the Balkan allies — a return to the pre-Solidarity framing of 1979,
just with Poland now specifically flagged rather than East Europe as an
undifferentiated bloc. Whether this reflects a real Polish military
recovery post-martial-law, an IC judgment that the crisis was
"resolved" by the imposition of martial law itself, or simply this
document's different scope (trends, not political risk) is not
resolvable from the text held — flagged as an open item.

## Right/wrong ledger against the archive-era ground truth

*Baseline: `reference/oob-verification.md` (Lautsch, MB V operations
chief 1983-86 — the man who wrote the plan in our exact setting window)
and `reference/zealand-landing.md` (Pałka, the Polish General Staff
archives on the amphibious side).*

**Right — the target and the ultimate objective.** All four documents
agree, from 1979 through 1985, that the Schleswig-Holstein/Jutland axis
is a **Polish-force-led** front with Denmark (mainland and islands) as
the objective, coordinated with a Baltic naval campaign. This matches
the archive-era finding exactly: the Küstenfront *was* Polish (three
armies + an air army), and its mission *was* Schleswig-Holstein plus
the Danish mainland, bypassing Hamburg. The IC never lost this thread
across six years and three authors — a real hit, not a lucky guess.

**Right — the direction of travel on reliability, wrong on the fix.**
The 1981 document correctly identifies, in real time, that Polish
reliability is the single most exposed assumption underpinning the
whole axis, and floats the actual mitigation lever the Soviets would
eventually reach for (more Soviet weight on the axis — ¶59's "Baltic
Military District" hedge anticipates, in shape if not detail, the
94th Guards MRD attachment and the post-1985 Soviet takeover of the
Zealand mission via 16th Army/UBF). But the IC's own follow-on
document (1985) *softens* the reliability worry back toward routine
combat-potential-gap language just as the real plan was actually moving
away from reliance on the Poles for the axis's most exposed mission
(Zealand passes to the Soviets, May 1985/Nov 1986 per `zealand-landing.md`).
The estimate's alarm and the real fix are chronologically staggered —
right worry, but the IC's confidence in it faded exactly as the
worry was being validated by events it wasn't tracking.

**Wrong — the covering-force architecture, in all four documents.**
This is the sharpest miss. None of the four estimates describes
anything resembling Lautsch's actual mid-80s architecture: a thin
**two-division GDR/Soviet covering force** (8. MSD + 94. Gds MSD)
holding the border for ~2 days while the Polish Küstenfront completes
its approach march from Poland and deploys through Mecklenburg. Every
document instead describes the Polish front itself as the axis's
first-echelon, breakthrough-conducting formation (1979 ¶127: the front
itself "breaking through initial defenses in its area"; 1983 IIM: "About
half of the first echelon would be composed of East European forces,"
with the Polish front counted as first-echelon, full stop). **The IC
counted the Polish front's divisions and armies but never modeled the
two-phase covering-force-then-front architecture** — it saw the
building blocks (Polish Pomeranian MD, GSFG's northern army, Baltic MD
as a reinforcement pool) without ever assembling them into the actual
sequence. This is exactly the theme `oob-verification.md` names for the
NVA/GDR side of the ledger ("both G-2s count the other side's divisions
and miss the other side's plan") — now confirmed true of the US
estimates as well, not just of a hypothetical Soviet mirror-image error.

**Wrong (or at least: not caught in what we hold) — the 1985 defensive
turn.** `oob-verification.md` documents a 1985 Warsaw Pact plan
revision that turned the whole Western TVD defensive-first (hold a
Dassow-Lenzen line, restore the status quo ante, offensive action
reduced to counterstrokes) — a change contemporaneous with NIE
11-14-85 itself. Nothing in the held NIE 11-14-85 text reflects this;
if anything, the document's ground-offensive framing (¶127-class
material is absent from what we hold, but the naval/force-posture
material treats the Polish-front offensive mission as unchanged from
1979/81/83) suggests either the IC hadn't picked up the shift by
September 1985, or the signal lived in a sibling document we don't
hold (NIE 11-19-85, *Soviet Capabilities for Multitheater War*, is the
likelier home for a plan-posture judgment like this). Genuinely open —
flagged below, not resolved.

**Right, with real texture — warning time got longer, correctly, for a
reason the Pact's own planners would recognize.** The 1985 document's
5-7-day A2-readiness figure and its explicit "increasingly less likely
[the Soviets] would plan to mount a sudden attack without warning"
judgment (¶131) is consistent with everything the archive era shows
about the direction of Warsaw Pact readiness in the mid-80s (manpower
strain, the 1985 defensive-first turn itself implying reduced appetite
for a short-warning offensive). The IC's warning-time confidence grew
for the right underlying reason (Soviet manpower/readiness trends) even
though it never connected that trend to the plan-level defensive turn
it was a symptom of.

## Epistemic chain for the book

A corps G-2 at Rendsburg in Nov 1983 does not read National Intelligence
Estimates. NIEs are DCI-level, NFIB-coordinated, TOP SECRET-RUFF/codeword
products disseminated to national policymakers and the senior military
intelligence staffs named on their covers (ACSI Army, DNI Navy, ACS/I Air
Force, DIA, NSA, State/INR) — paragraph 1 of the 1981 document's
dissemination notice runs through exactly this list, and a corps-level
staff officer three command echelons below AFNORTH is not on it. What
LANDJUT's own G-2 would actually see is a **derived, sanitized,
theater-level product** — the equivalent of what BALTAP or AFNORTH staff
would push down as intelligence estimates, threat briefings, or
Order-of-Battle handbooks built *from* NIE-class material but stripped
of sourcing, dissemination-controlled at a lower level, and filtered
through whatever caveats the theater command chose to keep or drop.

The NIE layer matters to the book anyway, for one reason: **it is the
ceiling of what blue's side could know, institutionally, at all.** If
the DCI-level estimate itself never modeled the covering-force
architecture, no derived corps-level product could have modeled it
either — a derived product cannot know more than its source. The gap
this file documents (Polish-front-as-first-echelon vs. the real
covering-force-then-front sequence) is therefore not just a curiosity
about Langley's paperwork; it is a hard ceiling on what any character
in this book, however well-briefed, could have believed about the
axis's actual shape. A LANDJUT G-2 who briefed his commander that "the
Poles hit us on day one" would have been repeating, in good faith, the
best available synthesis of what the US intelligence community itself
believed in 1981-83 — and would have been wrong in exactly the way the
real NVA operations chief's own memoir shows the plan actually worked.

## Consequences for the instrument

- **Warning-time parameter (W):** the four documents do not converge on
  a single number, and that spread is itself usable. Read as a
  progression: 1979's per-division readiness bands (24h Cat-I / 72h
  other-active) describe how fast standing divisions could move, not
  how much *notice* NATO gets; 1981's explicit two-week judgment is the
  best available headline figure for full theater-force generation
  (163 standing → 80-90 division, five-front array); 1985's 5-7-day
  A2-readiness figure plus its "early strategic warning" judgment
  shows the estimate lengthening over time. For a Nov 1983 setting, the
  defensible instrument default is the **1981 two-week figure for full
  Pact force generation**, with the caveat that first-contact forces
  (the covering-force divisions in the real plan, which the IC didn't
  know were a distinct category) could be moving within the 1979-vintage
  24-72 hour band. This bifurcation — long warning for the *full*
  offensive, short warning for whatever hits the border first — is
  itself period-accurate and dramatically useful: blue's mobilization
  clock and blue's *contact* clock are different clocks, and the
  estimates never quite say so out loud.
- **Polish reliability as a plot lever, correctly dated:** the 1981
  document's alarm (five months before martial law) and the 1985
  document's softening (Poland now filed with the "southern tier" as a
  routine capability gap) bracket a real, dateable arc. A Nov 1983
  setting sits about a year and a half after martial law was imposed
  (Dec 1981) and roughly two years after the 1981 NIE's live alarm —
  i.e., in the setting year, a corps-level G-2's derived product would
  most plausibly still be running on 1981-vintage reliability doubt,
  not yet on 1985's routinized language. This licenses a book-internal
  choice: blue characters worried about Polish reliability are reading
  their own moment correctly; blue characters no longer worried would
  be ahead of the documented curve.
- **The covering-force miss is dramatically load-bearing, not just a
  footnote.** Any blue staff officer working from NIE-derived material
  would expect the Polish front's arrival to *be* first contact on the
  axis. The real architecture (GDR 8. MSD + Soviet 94. Gds MSD holding
  for ~2 days first) means blue's own doctrine-informed expectation of
  "the Poles hit us and the Poles are the reliability question" would
  be answered, in the field, by two days of GDR/Soviet troops who
  aren't the reliability question at all — a legitimate surprise built
  entirely out of documented intelligence gaps, no authorial invention
  required.
- **The 1985 defensive turn is a live unknown for characters set after
  it**, per the ledger above — the held NIE material doesn't show the
  IC catching it. Any post-1985-set material (out of scope for this
  project's Nov 1983 pin, but worth flagging for the ledger) should not
  assume blue intelligence had caught up to the Pact's own defensive
  turn.

## Open items

- **NIE 4-1-78** (*Warsaw Pact Concepts and Capabilities for Going to
  War in Europe: Implications for NATO Warning of War*) is the actual
  home of the IC's NATO-warning-time methodology per NIE 11-14-79's own
  preface citation (PDF p.9) — not held. Highest-value acquisition for
  tightening the W-parameter case above; would let the two-week/24-72h
  bifurcation above be replaced with the IC's own explicit warning
  model instead of an inference from readiness-category language.
- **NIE 11-14-79 Volume II** (detailed doctrine/theater-forces/trends) —
  not held; Volume I's citations to "(IV, 86-111)"-style cross-references
  throughout point at OOB and doctrine detail we don't have for the 1979
  baseline.
- **NIE 11-19-85** (*Soviet Capabilities for Multitheater War*, Jun 1985)
  and **NIE 11-15-85** (*Soviet Naval Strategy and Programs Through the
  1990s*, Jan 1985) — both named as siblings by NIE 11-14-85's own Scope
  Note as carrying the operational/naval detail this trends volume
  disclaims; NIE 11-19-85 in particular is the likeliest home for
  whether the IC had picked up the 1985 defensive-plan turn by the
  document's date — currently an open question in the ledger above.
  Not held; not identified as available in the CIA reading room search
  already run for the 1989 Denmark paper (a further pass is owed).
- **NI IIM 83-10002's redactions**: two bracketed gaps (PDF pp.11, 12 —
  the nuclear-strike-count/timing figures and the Polish-front
  exploitation-role source) are sanitization, not retrievable without a
  formal re-review request.
- **Why 1983's IIM carries no Polish-reliability discussion** at all
  (vs. 1981's alarm and 1985's softened version) is unresolved from the
  text — could be scope (employment mechanics only) or could reflect a
  real IC view that martial law had "settled" the question for planning
  purposes; a second setting-adjacent source (a 1982-84 NIE on Poland
  itself, if one exists and is findable) would settle this.
- **OCR fidelity**: sidecar text was produced by `ocrmypdf --force-ocr`
  and is generally good but not proofread word-by-word beyond the
  passages quoted above; any future direct quotation from these
  documents beyond what's excerpted here should be checked against the
  scan images, not just the OCR sidecar (`ocrmypdf` output PDFs +
  `.txt` sidecars left in the session scratchpad, not checked into the
  repo).
