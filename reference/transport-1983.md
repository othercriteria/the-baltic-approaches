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

## 6. Verification queue (what round 2 chases)

1. Danish military/DSB beredskab ferry-capacity planning (the
   CAL-3 anchor proper) — print sources, DK browser tier.
2. Storstrøm single-rail-track (B–) and Bad Kleinen–Schwerin
   track status (B–).
3. Neumünster–Heide single/double in 1983.
4. Hard cites for rail capacity norms (FM 55-20; HDv logistics).
5. North-Jutland (Aalborg–Vejle) motorway extents 1983.
6. F106 designation (Schwerin–Wismar) — assumed, unverified.

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
