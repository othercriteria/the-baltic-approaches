# Theater transport network, November 1983 — verification round 1

*Session eb2fcb4e, 2026-07-23. Four web-research agents (Opus) run
against the atlas's criticality ranking (`atlas critical`): Danish
water crossings, roads/designations, rail, IGB crossings. This
note is the distilled record; the dataset
(atlas/data/theater-1983.toml) carries the operational values.
Source grade key: A = well-attested/official, B = encyclopedia,
B– = weakly pinned (re-verify if load-bearing), C = enthusiast
compilation. Full agent reports in this session's transcript.*

## 1. The traps caught (modern values that must NOT leak into 1983)

- **Rødby–Puttgarden crossing was ~60 min in 1983** — the famous
  45-min figure is post-1997. [de.wiki Vogelfluglinie]
- **The new Little Belt bridge carried E66** (Esbjerg–København–
  Malmö) in 1983 — E20 arrives with the 1992 Danish renumbering.
- **E3, not E45, on the Jutland corridor — until ~1992** (the AGR
  scheme was adopted ~1985 and reached Danish signs 1992; the
  CLAUDE-era "switch 1985" belief was itself too early).
  Vogelfluglinie road = **E4**, not E47.
- **M/F Karl Carstens** (the big Vogelfluglinie ferry): ordered on
  a 1983 decision, in service 1986 — does not exist in-setting.
- **Farø bridges opened 1985** — in Nov 1983 the 1937 Storstrøm
  bridge is the ONLY fixed link off Zealand southward.
- **Great Belt fixed link 1997/98** — ferries only, ~1 h crossing.
- Modern track-layout descriptions ("double except Tinglev–
  Padborg") are anachronistic — see §3.

## 2. Danish water crossings (agent 1; grades A/B unless noted)

- **Great Belt road ferry** (Halsskov–Knudshoved, DSB): ~55–60
  min; peak service ~every 15–30 min; normally 6 ferries at peak;
  vessels 200–390 cars (~1,000–1,950 lane-m). Documented actual:
  **7,007 car-units in one day on 4 of 6 ferries** (Easter 1985)
  ≈ 35,000 lane-m/day; fleet-max ≈ ~50k lane-m/day.
- **Great Belt rail ferry** (Korsør–Nyborg, DSB): ~1 h; the 1980-81
  IC ferries (Dronning Ingrid, Prins Joachim, Kronprins Frederik):
  4 tracks, ~494 m effective track, +~200 cars, 2,000 pax.
- **Vogelfluglinie** (Rødby–Puttgarden, DSB/DB, since 1963):
  half-hourly cadence; 1983 fleet ~6 vessels (Deutschland, Theodor
  Heuss, Kong Frederik IX, Danmark, Prins Henrik, Dronning
  Margrethe II); capacity class ~14 rail wagons + ~156 cars.
- **Storstrøm bridge (1937)**: single rail track + 5.6 m road,
  3,199 m, famously the bottleneck; sole Zealand→Falster link.
- **Little Belt**: old bridge (1935) two rail tracks + 5.6 m road;
  new bridge (1970) 6-lane motorway (E66).
- **Military ferry-capacity assessments: NOT FOUND in open web** —
  the CAL-3 anchor still wants Danish print sources (DSB beredskab
  planning, Landsdelskommando mobilization studies). The dataset's
  ferry capacities are therefore DERIVED, not SOURCED.

## 3. Rail (agent 3; the whole theater is DIESEL in 1983)

No line in scope was electrified in Nov 1983 (DK electrification
from 1986; DB Schleswig-Holstein 1995+; DR Mecklenburg 1985–87).

- **Fredericia–Padborg: single track south of Vamdrup in 1983**
  (Vojens–Tinglev doubled 1996, Vamdrup–Vojens 2014-15, Tinglev–
  Padborg single today). The border rail feed is single-track.
- Padborg–Flensburg–Neumünster–Hamburg: double throughout;
  crosses the canal on the **Rendsburg High Bridge + loop (1913)**.
- **Marschbahn/west coast: single-track sections including the
  Eider swing bridge at Friedrichstadt.**
- Hamburg–Lübeck double (1875-76). Lübeck–Puttgarden mostly
  single; Fehmarnsund bridge (1963) = 1 track + 2 road lanes.
- Zealand: main line double; Sydbanen double to Vordingborg,
  **single over Storstrøm** (B–); Nykøbing F–Rødby single (1963).
- East: **Lübeck–Herrnburg–Bad Kleinen single track** (2nd track
  removed as Soviet reparations), interzonal traffic incl.
  Hamburg–Rostock pair + freight, ~40 min border controls at
  Herrnburg; Bad Kleinen–Rostock double (re-doubled 1973-75),
  diesel until 1986-87. Bad Kleinen–Schwerin status B–.
- **Capacity rules of thumb, now FM-anchored where the FM
  speaks** (FM 101-10-1 Vol 2 Ch 3, 1987, on the shelf — extracted
  2026-07-23 w/ page cites): net trainload **500 STON**
  (para 3-26, p. 3-41, labeled conservative); heavy-equipment
  trains "seldom exceed 65 cars or 1,200 tons" (para 3-30);
  foreign-railway fallback 40 cars/400 t/1,000 troops (para
  3-31); net load/car 20 t US / 10 t foreign equipment. **The FM
  tabulates NO trains-per-day line density** (explicitly a local
  input) — single ≈ 20-30 / double ≈ 40-60 trains/day stays a
  grade-C rule of thumb. Dataset uses 500 STON × ~40 (double,
  class default 20k t/d) and × ~20 (single, per-edge 10k t/d).

## 3a. FM 101-10-1 highway/water factors (shelf extraction, same day)

Vol 2 **Table 3-7 (p. 3-7), "Highway Tonnage Capabilities"** —
daily tonnage forward, STON/day, by surface and zone: concrete
60,000 optimum / **36,000 COMMZ** / 8,400 combat zone;
bituminous 45,000 / **27,000** / 7,300; bituminous-treated
30,000 / 18,000 / 5,800; gravel 10,150 / 6,090 / 3,400.
Reductions: narrow (<7.2 m) −25%; rolling −10-25%; hills-with-
curves −30-60%; mountainous −60-80%; weather −20-90%. The atlas
class defaults are the COMMZ column (combat-zone degradation is
scenario logic, not edge capacity). Truck-company lift factors
and the 90-mile line-haul/2-trips-day factors extracted (Table
3-4, p. 3-4). Port/beach: NO flat tons/day default exists — the
FM computes min(reception, discharge, clearance); lighterage
craft capacities tabulated (LCU ~150-184 LT). **No inter-modal
conversion factor exists in the FM** — do not invent one.
Caveat: general planning defaults "only in the absence of
specific data on the local situation" (p. 3-2) — local research
outranks them, which is this file's whole program.

## 4. Roads (agent 2)

- **A7 complete Hamburg→Danish border since 1978** (last gap
  Schuby–Tarp); Rader Hochbrücke 1972 (1,498 m).
- **Danish E3 motorway NOT continuous in Nov 1983**: gap
  **Christiansfeld–Skovby until 1984** (through traffic on the
  old hovedvej); motorway Vejle–Christiansfeld (Vejlefjordbroen
  1980) and Skovby–Frøslev border (1978/81) either side.
- **Kiel Canal road crossings, 1983**: Rendsburg tunnel (B77,
  1961); Rader (A7, 1972); **Levensau** (B76 — old 1894 road+rail
  bridge, new road bridge 1980-83 just completing); Holtenau
  (B503): Olympiabrücke 1972 AND the 1911 Prinz-Heinrich-Brücke
  both standing; **Brunsbüttel high bridge (B5) opened 1983** —
  vehicle ferry before; plus the free small ferries (Breiholz,
  Sehestedt, Nobiskrug, Fischerhütte...).
- **Correction to the seed: B76 Kiel–Eckernförde crosses the
  canal at LEVENSAU, not Holtenau.**
- A23 Hamburg–Itzehoe open (1975/81; Halstenbek stretch still
  surface B5 until 1986); no motorway past Itzehoe until 1990.
- Eider: B5 crosses at Friedrichstadt (movable bridge); the
  **Eidersperrwerk (1973) carries a public road** at the mouth.

## 5. IGB, Lübeck sector (agent 4)

- Legal crossings in the sector, complete list: **Schlutup/
  Selmsdorf road** (GÜST, reopened 1960, Scandinavia transit +
  local traffic) and **Herrnburg rail**. Nothing else north of
  the Elbe-corner transit group (Gudow/Zarrentin A24 — opened
  Nov 1982 — Schwanheide rail, Lauenburg–Horst B5).
- **Schwerin–Gadebusch–Ratzeburg (F104/B208): SEALED and
  PHYSICALLY INTERRUPTED** — roadbeds do not meet; fence,
  control strip, and the Ratzeburg lake chain between;
  reconnected 12 Nov 1989. Wartime use = breach engineering.
  (The atlas therefore carries it as an ABSENCE, not an edge.)
- GDR roads use **F-numbers in 1983** (F104, F105); ordinary
  two-lane Fernverkehrsstraßen; **no motorway toward Lübeck**
  (A24 runs Berlin–Hamburg, south of scope; A20 is post-2000).
- Border-zone texture: 5 km Sperrzone, 500 m Schutzstreifen,
  10 m control strip; Metallgitterzaun, towers, vehicle ditches,
  SM-70s still partly fitted in 1983 (B — general-regime, not
  segment-specific).

## 6. Round 2 (same day): the B– items closed, north Jutland corrected

- **Storstrøm single rail track: grade A** (Banedanmark: "ét
  jernbanespor"; config unchanged from 1937). Bad Kleinen–Schwerin
  CORRECTED to double (on the 1973-75 rebuilt main line).
  Neumünster–Heide CONFIRMED single ("eingleisige Nebenbahn",
  never doubled). Sydbanen and Vestbanen double (1924-25 /
  1899-1900). **Rendsburg High Bridge two-track in 1983** (its
  single-track episode is 1993-2014 — a modern-value trap
  avoided).
- **North Jutland: the motorway ENDS at Vejle in Nov 1983.**
  Aalborg (1969-72) and Randers (1971) bypasses + one fragment
  south of Aarhus (1977/82) are the only motorway north of it;
  Svenstrup–Randers 1992, Vejle N gap until 1990, Aarhus–Randers
  1994. The 1982 Schlüter construction freeze corroborates.
  Domestic numbering: the spine is **hovedvej A10** (A-numbers
  until ~1985); Vejle–Fredericia = **A18** (no motorway);
  **Kolding–Fredericia motorway since 1970** (Taulov corridor,
  A1/E66, opened with the new Little Belt bridge). F106
  Schwerin–Wismar confirmed.
- **Shelf mining for the military Belt-crossing number: NOT
  FOUND on the shelf** (verdict stands: DK-browser/print tier).
  What the shelf DOES hold (diis-kk-bind3 pp. 556, 568-570;
  slks-dkka-baggrundsnotat §5.1, p. 60; cia-1989 App A):
  **East German military intelligence studied precisely this
  bottleneck question** — the Copenhagen residency mined
  Vejdirektoratet and DSB ferry-division material to find
  Denmark's "transportmæssige flaskehalse," and read Jutland
  motorway expansion as NATO reinforcement-transfer planning;
  **Danish civil defense assumed wartime BISECTION at the Great
  Belt** (separate regional command west of it); the Great Belt
  ferries were the "usual route" under standing surveillance;
  and the Zealand-raised Jutland Brigade was earmarked to
  reinforce LANDJUT (CIA 1989). Design note: red's G-2 owning
  blue's crossing arithmetic is primary-sourced — usable
  in-book.

## 7. Round 3 (same day): the density doctrine and the official chronology land

- **~~Rail line-density hard cites~~ CLOSED**: TR0603 *Rail
  Operations Planning* (1970, from DK's /bulk archive) carries
  the doctrine itself — §2.13 rule of thumb **TD 10 single / 30
  double** (trains/day each way), the passing-track formula
  (24·S·(NT+1)/(2·LD); worked example TD 17), NTL × TD = net
  division tonnage. **FM 55-20 (1974)** fetched from bits.de
  ("Railway Line Capacity Planning" section confirmed) + FM 55-15
  (1968/C3-1973) + FM 55-10 (1969) — shelf batch 9. Atlas rail
  defaults re-anchored: double 15,000 t/d (TD 30 × 500 STON),
  single-track edges 7,500 (formula-supported TD ~15 for short
  well-found divisions; doctrine floor would be 5,000).
- **~~"Det store H"~~ ACQUIRED (DK download, deposited to
  HOLDINGS — © Vejdirektoratet w/ named photographers, not
  redistributable)**: the official chronology confirms at
  Road-Directorate grade: border motorway 1978 (opened by the
  Queen with Bundespräsident Scheel attending — prose-grade
  period detail), Skovby–Christiansfeld gap closed 1984 by Prins
  Henrik ("the last piece of the Sønderjylland motorway"),
  Vejlefjordbroen 1980, Lillebæltsbro 1970 (Frederik IX), **Fyn
  motorway completed only 1985** (resolves both Funen verify
  flags: part-motorway west, hovedvej A1 east in Nov 1983), Farø
  1985, Aarhus–Randers 1994. Atlas notes upgraded to official
  grade.
- Not found free anywhere (do not re-hunt): FM 101-10-1 1976/77
  edition; 1980s Bundeswehr HDv logistics manuals (Bundesarchiv
  physical only).

## 8. Verification queue (round 4+)

1. ~~Danish military/DSB beredskab ferry-capacity planning~~ WORKED
   TO OPEN-SOURCE FLOOR 2026-07-25 — mechanism sourced, figure still
   print/archive tier; see §9 for findings + DK pursuit list.
2. OCR debt flagged by the shelf pass: cia-1984-nordic-forces,
   nie-11-14-79/81/85, ni-iim-83-10002 have NO text layer.
3. Eider secondary crossings + Kiel Canal small-ferry inventory
   if a scene needs them.
4. Remaining verify flags (3): rd-kiel-lubeck, rd-rendsburg-
   neumunster, b200-flensburg-husum road-class minutiae.

## 8. Cash-out for the outline (story-facing, non-mechanical)

What the two rounds + the v21 audit hand the Phase-1 outline:

1. **The ninety-hours arithmetic gets real furniture.** The Jyske
   Division's march runs overland down a corridor whose motorway
   ENDS at Vejle, threads the Christiansfeld–Skovby hovedvej gap
   (closed 1984 — one year too late), and whose rail feed goes
   single-track south of Vamdrup. The specimen's Little-Belt-
   chokepoint framing is dead; the real texture is a march-table
   problem on A10/E3 with two datable soft spots. (Lammers'
   "depots are not the division" scene inherits these specifics.)
2. **The Zealand brigades cross by FERRY.** Chs. 15–16's release
   is a Great Belt ferry operation (~1 h crossing, 6-vessel road
   fleet + 4-track IC rail ferries, 2–3 days for the package) —
   and Danish civil defense ASSUMED wartime bisection at the
   Belt, with a separate command west of it (primary-sourced).
   The release decision the wargame prices as zg_* was a real
   standing question. DSB's ferry division as quiet wartime
   machinery is a period-true texture layer.
3. **Red's neck is two crossings wide.** Until breach engineering
   widens it, everything red moves into the Lübeck sector rides
   one road GÜST (Schlutup) and one single-track rail line
   (Herrnburg) — the physical referent of the 200-km-column
   finding and of red's pulsed logistics. And **East German
   intelligence demonstrably studied blue's crossing arithmetic**
   (Vejdirektoratet + DSB ferry-division material, hunting
   "transportmæssige flaskehalse") — the two-confession-walls
   symmetry has a primary-sourced intelligence mirror: red's G-2
   owns blue's atlas, and vice versa is the book's question.
4. **Period signage discipline for prose:** E3/A10 (never E45),
   E4 (never E47), E66 (never E20), F-numbers east of the wire,
   A7/A1/A23 safe as-is. Rødby crossing is an HOUR. The
   Brunsbüttel high bridge is NEWS in November 1983.
5. **The G-4's rail scene has a hard fact:** the whole theater is
   diesel; the Rendsburg High Bridge carries two tracks over the
   canal on a 1913 loop; the Marschbahn crosses the Eider on a
   single-track swing bridge at Friedrichstadt — the valve
   complex's rail half.

## Sources (best URLs from the four agents)

- https://trap.lex.dk/Storebæltsforbindelsen
- https://da.wikipedia.org/wiki/Storstrømsbroen
- https://de.wikipedia.org/wiki/Vogelfluglinie
- https://da.wikipedia.org/wiki/Europavej_E66 · …/Europavej_E45
- https://da.wikipedia.org/wiki/Sønderjyske_Motorvej
- https://en.wikipedia.org/wiki/Bundesautobahn_7
- https://de.wikipedia.org/wiki/Nord-Ostsee-Kanal
- https://de.wikipedia.org/wiki/Levensauer_Hochbrücke
- https://de.wikipedia.org/wiki/Bahnstrecke_Fredericia–Flensburg
- https://en.wikipedia.org/wiki/Neumünster–Flensburg_railway
- https://de.wikipedia.org/wiki/Marschbahn
- https://en.wikipedia.org/wiki/Lübeck–Bad_Kleinen_railway
- https://de.wikipedia.org/wiki/Chronik_der_Streckenelektrifizierung_der_Deutschen_Reichsbahn_im_Gebiet_der_DDR
- https://dewiki.de/Lexikon/Bundesstraße_208
- https://de.wikipedia.org/wiki/Innerdeutsche_Grenze

## 9. Belt-ferry beredskab hunt (2026-07-25, Opus verify pass)

Queue item §8.1 worked to its open-source floor. **The discrete
military capacity figure (battalions/day, lane-m under military
control) remains UNFOUND — confirmed negative at open tier.** But
the requisition mechanism itself is now sourced and quotable:

- **DSB "Beredskabsinstruks," in force from Aug 1976** (classified
  Til Tjenestebrug; replaced station instructions of Dec 1962 /
  1 Sep 1970): governs DSB conduct at "forøgelse af fredsstyrken"
  (mobilization) — "materiel, færger, tog, perroner og andet skal
  prioriteres med forrang for indkaldt personel til forsvarets
  enheder" (ferries NAMED among assets prioritized for mobilization
  movement); point 2.6 covers denial/destruction. Source: Jensen &
  Hansen, "Kold krig på skinner — DSB og dansk infrastruktur i en
  østtysk optik," Jernbanehistorie 2019 (free PDF:
  https://tidsskrift.dk/jernbanehistorie/article/download/119240/167048/247380),
  citing the instruction's own p. 1-1. Wider legal umbrella:
  kongelig forholdsordre 6 Mar 1952; wartime fuldmagtslov
  requisition provisions.
- **Work-of-record identified:** Riis-Knudsen, "Totalforsvar på
  skinner — DSB's rolle i totalforsvaret af Danmark under den
  kolde krig" (SDU speciale 2013; article version at
  https://tidsskrift.dk/jernbanehistorie/article/view/26887) —
  the highest-probability holder of an actual capacity/timeline
  figure in print.
- **One quantified lift equivalence, WP-SIDE ONLY:** exercise
  Val-74 assumed four Danish ferries move an armored division to
  Holland (DIIS vol. 2 p. 604; ferry harbors as targets p. 619).
  Enemy planning arithmetic, not the Halsskov run — coarse
  triangulation only (~4 ferries ≈ 1 armd div).
- Ferries/harbors were registered nøglepunkter (FE key-point
  section); rail guarded by Jernbanehjemmeværnet. The
  ferries-as-minelayers legend: investigated, NOT documentable
  (Hillingsø/Nørby/Wismann consulted by the article's authors).
- Scale comparandum, red side: GDR prepared 400–448 trains + 7
  highways; ~60 trains per division (Hillingsø in Hedegaard 2008
  p. 88).
- Direction note: reachable sources foreground Jutland→south and
  Esbjerg→east flows; the manuscript's Zealand→Jutland lift is
  separately corroborated (CIA-1989 Jutland Brigade earmark, on
  shelf) and the Beredskabsinstruks mechanism is
  direction-agnostic — ch. 2's requisition premise stands.

**DK pursuit list (print/archive):** (1) Riis-Knudsen full text
(SDU repository); (2) the Beredskabsinstruks 1976 itself —
Rigsarkivet DSB fonds and/or Danmarks Jernbanemuseum; (3) DIIS
vol. 2 direct page-pull (pp. 604, 619) + vol. 3 pp. 556–558,
564–565; (4) RA FE-arkiv "V. Diverse sager (afklassificerede)"
kasse 7–11; (5) Landsdelskommando ØST/VEST staff studies via
Rigsarkivet (physical) — the natural home of a Danish Belt lift
timeline.

## 10. NEPS — the fuel line under the whole scenario (2026-07-25, DK-prompted via Bogason)

Web/museum tier (koldkrig-online.dk "NEPS-linjen"; Kystmuseet
Bangsbo Fort; nato.int NPS topic page; OSW commentary 682).
Bogason presumably carries the print-grade treatment — DK reading.

- **North European Pipeline System (NEPS):** ~650 km military
  POL pipeline, Frederikshavn (main depot; offshore tanker import
  facility ~7 km off the coast) south down Jutland to the Kiel
  Canal area — the NATO topic literature gives the southern
  terminus as **Hohn** (the Transall base; also our alternate-HQ
  woods and the AWS climate station — convergence noted, not
  engineered). Built 1952–70 under NATO infrastructure, ~15 pump
  stations, carrying **jet fuel, diesel, and gasoline to the
  Jutland and North German air bases and barracks**.
- **Period-perfect detail: the 1982–84 expansion** — branch line
  to the Fredericia refinery and enlarged import at Esbjerg
  harbor — is under construction or just complete in November
  1983. (Fredericia and Esbjerg are both already load-bearing
  addresses in the text.)
- NATO Main Air Bases fed: Karup, Skrydstrup, Aalborg;
  redeployment bases Tirstrup, Vandel, Værløse.

**Scenario relevance (assessed in-session):**
1. No contradiction on the page: ch. 2's eleven hundred
   requisitioned civilian tankers read correctly as the
   DISTRIBUTION lift (pipeline heads → formations), which
   pipelines require rather than replace; the road-competition
   claims (ch. 8) are ammunition-led, which NEPS does not carry.
2. The real gap is an absence: the corps' ambient fuel picture
   is all trucks. One clause could acknowledge the line without
   briefing it.
3. Best single candidate placement: **ch. 6, Aakjær's
   careful-fires inventory of intact things** — the pump
   stations of the fuel line belong on that list either way he
   is read (a red wanting a working peninsula spares them; a red
   strangling blue air hits them first), and the inventory is
   already the scene's engine. Candidate only — DK to rule; no
   text touched.
4. Wargame: bulk POL lives inside the CAL-3 supply abstraction;
   no recalibration implied.
