# Map implementation spec, v1

*2026-07-25, session e3137278. Authority: planning/
map-program-rfp.md (four-proposal record, synthesis, and DK's
ratification block — read it first; this spec implements that
ruling and cites forks as F1–F7). Builder: Opus agent, this
spec + the RFP are the contract. Where this spec is silent,
the RFP synthesis governs; where both are silent, decide,
record the decision in the build report, and prefer restraint.*

## 0. The program in one paragraph

Two monochrome plates of clean, timeless 1983 geography — **Plate
I "THE APPROACHES"** (theater) and **Plate II "THE NECK"**
(operating area) — for the front matter of the reading build,
before ch. 1. No front lines, arrows, unit symbols, boundaries
(other than real national frontiers), phase lines, dates,
capacities, or any mark of the war. The network layer renders
from the atlas so the absences tests guard the cartography; the
base layer is public-domain. One ink. The reader gets the plate
the staff starts from.

## 1. Deliverables (tiers; stop cleanly at a tier boundary if blocked)

- **T1 — pipeline + draft plates.** An `atlas render` subcommand
  (or `python3 -m atlas render <plate>`) emitting SVG for each
  plate from data; both plates rendered with real geometry;
  committed-quality source files. Tests: rendering must fail if
  any absences-table edge would be drawn; snapshot-test the
  feature lists (every required label present).
- **T2 — build integration.** `make maps` (data → SVG → PDF);
  plates placed in the reading build's front matter after the
  making-note page, each on its own page, no gutter crossing,
  inside the live area; `make pdf` produces a proof with both
  plates in place. Wordcount unaffected (apparatus).
- **T3 — build report.** A written report (return as final
  message text, NOT committed): every decision taken where the
  spec was silent, every deviation, every known defect (label
  collisions, geometry shortcuts), and the exact rerun commands.

**Do NOT git-commit anything.** Leave the working tree modified
for session review. Do not touch drafts/, notes/, or planning/
(except nothing — you write no planning files). New code lives
in atlas/; new data in atlas/data/; font/face is a parameter
(§5).

## 2. Data and licensing (hard constraints)

- **Network layer (roads, rail, ferries, crossings, node
  positions): atlas/data/theater-1983.toml ONLY.** Read
  atlas/README.md for the seam contract. If a node the plates
  need is missing (check: Sehestedt, Sorgbrück, Nordfeld,
  Missunde), add it to the TOML with lat/lon marked GUESS-tier
  in its note, consistent with existing conventions — that is
  the one data edit you may make.
- **Base layer (coast, water bodies, rivers, marsh): PD/CC0
  only.** First choice Natural Earth 10m (coastline, land,
  rivers+lakes) — download and commit the CLIPPED extract only
  (not the world files), with provenance noted in a README
  beside it. If downloads are blocked in this environment,
  fall back to hand-digitizing the coastline at generalized
  1:500k grain from PD sources you can reach; if nothing is
  reachable, ship T1 with an honest placeholder coast and SAY
  SO in the report. **Never invent geometry silently; never
  trace a copyrighted or scanned map.** The holdings/
  submodule is off-limits.
- **The Danevirke trace:** approximate polyline from the
  Schlei's head (Hedeby/Schleswig side) west-southwest to the
  Treene marshes, ~19 km, per reference/danevirke.md. Mark
  GUESS-tier. Rendered as an earthwork hachure (§4).
- 1983 truth is enforced by the atlas: no Great Belt fixed
  link, no Fehmarn link, E3 not E45. The layer separation is
  the anachronism guard — the modern PD base supplies ONLY
  timeless coast/water; every datable feature comes from the
  1983 network data.

## 3. Plate specifications

### Plate I — THE APPROACHES (theater)

- **Extent (F5 = A/C, full Approaches):** north ~57.2° (Aalborg
  in frame); south ~53.5° (Hamburg); west the North Sea coast
  (Husum + the Eider mouth); east ~12.6° (København and the
  Zealand coast in frame; Rostock on the Mecklenburg shore).
  Portrait if it fits the ~4.0×7.0in live area at legible
  density; landscape (reader turns the book) is permitted if
  portrait fails — state the choice in the report.
- **Required features:** the Jutland E3/A10 road spine
  (Aalborg–Aarhus–Vejle–Fredericia–Kolding–Haderslev–Aabenraa–
  Padborg) and A7/E3 south (Flensburg–Schleswig–Rendsburg–
  Neumünster–Hamburg); west-coast B5 + Marschbahn; rail with
  the double→single distinction falling at Vamdrup (honest
  drawing, no callout — F2); Little Belt bridge pair (two
  lines); Great Belt as dashed ferry routes Halsskov–Knudshoved
  and Korsør–Nyborg (no bridge); Storstrøm link; Vogelfluglinie
  ferry Rødby–Puttgarden; the Kiel Canal as a firm double line
  with its crossings (Rendsburg, Rader Hochbrücke); the Danish
  frontier (light dashed); **the IGB southeast of Lübeck as a
  plain heavier frontier line with its two real gaps, Schlutup
  (road) and Herrnburg (rail), drawn truthfully and NOT
  spotlighted (F1+F2)**.
- **Required labels (small caps waters / roman towns; 1983
  spellings):** waters — North Sea, Baltic (Ostsee acceptable),
  Little Belt, Great Belt, Fehmarn Belt, Kiel Canal, the
  Schlei, the Eider, the Trave; regions faint — Jutland, Funen,
  Zealand, Lolland-Falster, Schleswig-Holstein, Mecklenburg;
  towns — Aalborg, Aarhus, Vejle, Fredericia, Kolding, Vamdrup,
  Haderslev, Aabenraa, Padborg, Esbjerg, Flensburg, Schleswig,
  Rendsburg, Neumünster, Kiel, Eckernförde, Husum,
  Friedrichstadt, Heide, Itzehoe, Hamburg, Lübeck, Oldenburg
  (Holstein), Puttgarden, Middelfart, Odense, Nyborg, Korsør,
  Slagelse, København, Vordingborg, Nykøbing F., Rødby; past
  the wire — Ratzeburg, Schwerin, Wismar, Rostock (edge-of-
  world; no interior beyond them).
- **Rendsburg carries the plate's only distinguishing mark: a
  small quiet square (F7).** Fredericia gets NO special mark.
- Furniture: plain km bar scale, small N tick, title THE
  APPROACHES, legend ≤5 lines (road class / rail / ferry /
  frontier / HQ). No compass rose, no cartouche, no grid.

### Plate II — THE NECK (operating area)

- **Extent:** the peninsula's waist. West: Husum/Friedrichstadt
  and the Eider mouth. East: Eckernförde Bay and Schwansen.
  North: the Schlei to its head (Schleswig, Missunde in frame).
  South: the Kiel Canal with Sehestedt and Rendsburg; include
  Hohn and (corner) Neumünster if the frame allows without
  crowding — report the call.
- **Required features:** the Kiel Canal (crossings marked:
  Rendsburg, Rader Hochbrücke, the Sehestedt ferry site); the
  Schlei with the Missunde narrows; **the Danevirke as an
  earthwork hachure** running Schlei-head → Treene marshes;
  the Treene/Eider marshes as stipple; the Eider crossing
  complex — Friedrichstadt road bridge, the rail swing-bridge
  ~1 km west (Marschbahn), the Nordfeld heavy ferry — **F4: if
  the three do not separate legibly at trim scale, use a small
  titled corner inset (per A); decide on the proof and report
  it**; the Sorge rail bridge at Sorgbrück; roads/rail per the
  atlas.
- **Required labels:** Rendsburg (HQ square again), Sehestedt,
  Schleswig, Friedrichsberg (as a Schleswig district label if
  legible; drop silently if it crowds), Missunde, Eckernförde,
  Husum, Friedrichstadt, Nordfeld, Sorgbrück, Hohn, the
  Danevirke (label the rampart itself), Treene, Eider, the
  Schlei, Kiel Canal; Neumünster if in frame.
- Same furniture rules as Plate I.

## 4. Register (one ink, the clean plate)

- **One ink, pure black**, matching body text. Water: open with
  a fine coastline, plus EITHER a pale flat tint (≤10% K) OR
  fine stipple — pick one treatment for both plates.
- Line hierarchy (heaviest→lightest): canal/coast emphasis per
  plate's subject > motorway > trunk road > rail (ladder ticks;
  double vs single visible) > secondary. Ferries dashed.
  Frontiers dashed political; the IGB heavier but plain.
- The Danevirke hachure and the marsh stipple are the only two
  "relief" symbols on either plate. No hillshade, no contours.
- **No grid squares** (a grid is a staff overlay; the overlay
  is the war). Graticule ticks at the neat-line only, if at
  all.
- Hairlines ≥0.25pt at final size; labels ≥6.5pt at final size;
  nothing crosses the gutter; live area per the current build's
  margins (read the Makefile/pandoc setup for trim and
  margins rather than assuming).

## 5. Typography (F6 as amended)

The ruling is **agreement between map and text**, not a specific
font. Implement the label face as a single parameter (default:
whatever body face the current build uses — discover it from the
build configuration, do not hardcode a name in more than one
place). Towns roman, waters small caps (fake small caps
acceptable at T1), title/scale in the same face. If the book's
face changes later, `make maps` must follow it by changing one
value.

## 6. Refusals (verbatim guard — test where testable)

Never rendered, under any option or flag: front lines, FEBA/
FLOT, axes/arrows, unit symbols or echelon boxes, formation
names, corps/sector boundaries, phase lines, dates or DTGs,
guidance lines, SPERBER or any fictional operational trace,
capacities/tonnages/any atlas number, red/blue coloring, any
feature from the absences table. The renderer should not even
have the vocabulary for these.

## 7. Acceptance

- `make maps && make pdf` from clean checkout reproduces the
  proof.
- Absences test: rendering the absences edges is impossible by
  construction (test asserts).
- Feature test: every §3 required label present in the SVG.
- Visual proof at trim size (both plates) generated for DK +
  the instrument gate (doctrine auditor / veteran reader /
  period auditor run AFTER DK's first look — not the builder's
  job).
- Expected iteration: label collisions and line weights WILL
  need a hand pass; T3 must list every known defect honestly
  rather than polishing the report.

---

## Build 1 review (session e3137278, same day)

Builder's T3 report accepted; tree reviewed, tests re-run green
(21 render/atlas + 12 atlas-lint), wordcount unchanged (48,986),
plates eyeballed at trim. **Deviation ACCEPTED:** data edits
beyond add-nodes (the labeled `map-plate additions` block — 10
nodes, the Vamdrup edge split preserving the chokepoint cap, 9
GUESS-tier supporting edges, render-only `tracks` hint). The
split was the only honest way to draw double→single falling at
Vamdrup; all pre-existing atlas tests pass; connectivity clean.

**Session verdict: pipeline REAL, plates DRAFT.** Fix list for
build 2, in priority order:
1. **Plate II's water is the blocker.** The Kiel Canal and the
   Schlei must read as drawn water — the canal as the firm
   double waterway Brunsbüttel→Kiel through Rendsburg/Sehestedt,
   the Schlei as the long fjord biting in from the Baltic to
   Schleswig. Until then the plate cannot do its ch. 12 job
   (west shoulder = canal west of Sehestedt; east = the Schlei).
   The Eider likewise. Better hand-digitization (more vertices,
   GUESS-tier disclosed) or NE 10m rivers where they exist.
2. **Plate I label whitelist.** Enforce §3's per-plate label
   lists in the renderer: Sehestedt/Sorgbrück/Nordfeld/Missunde/
   Hohn/Friedrichsberg are Plate II features and must not
   render on Plate I (they caused the neck pile-up). Fix the
   Middelfart/Kolding collision; area-label collision pass
   (LITTLE BELT vs Haderslev, BALTIC vs Nykøbing F.).
3. F4 (Friedrichstadt inset) deferred again — cannot be judged
   until item 1 lands.
4. OPEN REGISTER QUESTION FOR DK: the network renders as
   straight schematic segments between node coordinates (the
   atlas has no polylines; OSM is ODbL). Is route-diagram
   honesty acceptable for the final plates, or do the major
   roads/rail need hand-bent GUESS-tier polylines to read as a
   drawn map? This is a human-diagnoses call; build 2 scope
   depends on it.
