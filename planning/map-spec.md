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

---

## Build 2 work order (DK plate review, 2026-07-25)

**Register ruling (answers build 1's open question):** the
water-crossing howlers force shape; straight segments remain
acceptable for land-only edges. **Mechanism (DK's): SHAPE
NODES** — add real, named intermediate places (stations,
junctions that actually lie on the route) as path vertices that
render WITHOUT labels or town dots. Honest by construction:
every vertex is a fact; no fine polylines needed. Renderer
gains an unlabeled `shape` node class; atlas conventions apply
(GUESS-tier notes).

### Plate I fixes (all from DK's review)

1. **Schleswig–Esbjerg rail crosses the North Sea.** Also wrong
   topology: the west-coast rail is the Marschbahn,
   Itzehoe–Heide–Husum–Niebüll–(Ribe)–Esbjerg. Reroute along
   real stations (Niebüll, Ribe as shape nodes; Husum/Heide
   already labeled).
2. **Lübeck–Puttgarden rail crosses the Baltic.** Route the
   Vogelfluglinie honestly: Lübeck–(Neustadt in
   Holstein)–Oldenburg in Holstein–(Burg auf Fehmarn)–
   Puttgarden, with the Fehmarnsund crossing (1963 bridge —
   real, permitted).
3. **Kiel–Lübeck road crosses the Großer Plöner See.** Route
   B76 via Plön and Eutin as shape nodes (Eutin is a ch. 4
   place — labeling it is permitted if it doesn't crowd).
4. **Rail classes:** legend entries for double vs single track;
   ELIMINATE the unasserted third class to the extent possible —
   research each drawn line's 1983 track count (grade sources;
   where genuinely unfindable, assert single and note the
   choice in the TOML). Every drawn rail line ends up double or
   single, legended.
5. **Canal gets a legend entry** (waterway symbol).
6. **Labels inside the neat-line.** København, Nykøbing
   Falster, Esbjerg, North Sea (and any others) currently
   escape the bounding box — clip/pad, and check whether the
   escape is costing plate size (the frame should use the full
   live area).
7. **Missing edges east of Lübeck:** add Lübeck–Ratzeburg
   (real road/rail, GUESS-tier) so the IGB corner isn't empty
   and the two real gaps read against actual infrastructure.
8. **Country labels:** DENMARK; and the two Germanys
   "appropriately" — builder picks the period Anglophone map
   convention (e.g., FEDERAL REPUBLIC OF GERMANY / GERMAN
   DEMOCRATIC REPUBLIC, abbreviated if needed), faint like
   region labels, and reports the choice.
9. **Danish frontier trimmed to the coastline** (no protrusion
   into the North Sea).
10. **København stays unmarked** (DK: liked — now a ruling).

### Plate II fixes

Port all of the above conventions, plus the standing build-1
items: (a) **the water is still the blocker** — Kiel Canal and
the Schlei drawn as real water (canal as firm waterway
Brunsbüttel→Kiel through Rendsburg/Sehestedt; the Schlei as the
long fjord Baltic→Schleswig; Eider likewise), more vertices,
GUESS-tier disclosed; (b) Plate I label whitelist enforced per
§3 (the Plate II-only features off Plate I); (c) F4
(Friedrichstadt inset) judged on the new proof and reported.

---

## Build 2 review (session e3137278, same day)

Report accepted; suite re-run green (112), atlas check clean
(56 nodes/89 edges), wordcount unchanged, both plates eyeballed
at trim. All ten Plate I fixes verified on the plate: coasts
respected (Marschbahn inland, Vogelfluglinie via Fehmarn, B76
south of the lakes), rail all asserted double/single with legend
(19+14, one honest GUESS: Itzehoe–Heide), canal legended, labels
in-frame, IGB corner populated, DENMARK/WEST GERMANY/EAST
GERMANY at region-faintness, frontier trimmed, København
unmarked. Plate II water blocker CLEARED — canal/Schlei/Eider
read as ribbons. F4 call accepted: NO INSET — the three Eider
crossings separate on the main frame, and a finer bridge
coordinate would have to be invented, which the rules forbid.
Rail-track sourcing table stands in the TOML notes (three of the
builder's own guesses corrected by its sources: Heide–Husum
double, Vogelfluglinie single, Sydbanen double).

**Verdict: plates are now HAND-PASS TIER.** Build 3 (small)
polish list:
1. Plate II legend box is oversized and covers the lower-left
   (part of the Eider ribbon + a clipped water label + scale
   bar crowding). Shrink/relocate (top-right is open water).
2. The Danevirke hachure's EAST end should anchor at the Schlei
   head by Schleswig/Hedeby (currently ends short, floating);
   west end into the Treene marshes. Improve the GUESS trace
   per reference/danevirke.md.
3. Plate II: Hohn label sits on the Rendsburg–Sorgbrück rail;
   nudge.
4. Plate I: Middelfart/Kolding label collision persists; faint
   area-label overlaps (LITTLE BELT/FUNEN cluster, BALTIC/
   Vordingborg, THE TRAVE/Lübeck) worth one greedy-pass
   improvement or hand anchors.
5. Then: DK look at the full proof → instrument gate (doctrine/
   veteran/period readers) per spec §7 → lock for the panel
   PDF.

---

## Build 3 work order (DK review of build 2, 2026-07-25)

Process note: one more Opus polish pass now; afterwards DK
decides whether a further pass runs or the session does a hand
pass itself.

**Amendment:** the København ruling was over-read — "no special
treatment" means no capital styling, NOT dotless. København
gets an ordinary dot + label like any town.

### Plate I
1. København: ordinary dot restored.
2. Aarhus label to the LEFT of its dot; Vejle likewise.
3. Middelfart/Kolding collision (carryover) — resolve.
4. Faint area-label overlaps (carryover): LITTLE BELT/FUNEN
   cluster, BALTIC/Vordingborg, THE TRAVE/Lübeck, KIEL
   CANAL/SCHLESWIG-HOLSTEIN graze.
5. Danish frontier west end: build 2 over-corrected. Split the
   difference and RESEARCH the actual 1983 land-border west
   terminus (the frontier meets the Wadden coast near
   Siltoft/Rudbøl); end the drawn line at the researched
   coast point, not short of it and not at sea.
6. **IGB at Ratzeburg is wrong** — DK sees a line segment
   tangent to Ratzeburg. Research the actual border course
   (Priwall/Travemünde down past the Schlutup and Herrnburg
   gaps, then EAST of Ratzeburg along the Ratzeburger See and
   Schaalsee) and re-trace, GUESS-tier but shaped from the
   real course. Ratzeburg is FRG, near but not on a straight
   tangent.

### Both plates
7. Legend boxes are oversized for contents — size to content
   with tight padding.
8. Year annotation: add NOVEMBER 1983 as a restrained subtitle
   (or title-integrated) on both plates, consistent placement;
   this dates the GEOGRAPHY and does not breach the no-time
   refusal (which concerns campaign time).

### Plate II (carryover from build-2 review)
9. Legend relocated (top-right open water is available) and
   resized per item 7; scale bar uncrowded; nothing covering
   the Eider ribbon or water labels.
10. Danevirke hachure east end anchored at the Schlei head by
    Schleswig/Hedeby (per reference/danevirke.md); west end
    into the Treene marshes.
11. Hohn label off the Rendsburg–Sorgbrück rail line.

---

## Build 3 review (session e3137278, wrap)

Accepted: all 11 items landed (112 tests green; the one test
change — "1983" removed from the forbidden-vocabulary list — is
sanctioned by item 8). Item-9 deviation accepted with its
measured reasoning (Eckernförde occupies the top-right; legend
stays bottom-left, shrunk, scale bar opposite). Research sources
recorded (frontier terminus Siltoft/Rudbøl; IGB along the
Ratzeburger See NE shore — Ratzeburg now ~3–4 km west of the
line). DK verdict: **"Good enough for this draft."** Cover stamp
bumped Draft one → Draft two same commit.

Remaining defects list stands in the build-3 report (transcript)
+ honest-list above: THE TRAVE/infrastructure graze,
SCHLESWIG-HOLSTEIN span, FUNEN graze, neck scale-bar tightness,
FS_LEGEND 6.2pt vs the 6.5 floor. These are HAND-PASS items for
final assembly, not another agent round. Instrument gate
(doctrine/veteran/period readers over the plates) still owed
before lock — run it with the next blind panel round.

---

## Hand-pass (entity e3137278@4, 2026-07-27)

All five residuals discharged, plus two convention changes DK
proposed mid-pass:

1. **FS_LEGEND 6.2 → 6.5** (the floor); legend boxes auto-size.
2. **FUNEN** → (10.45, 55.15), the island's empty south interior
   (was under the cross-island road and Nyborg's label).
3. **Neck scale bar** → 110pt in from the right: flush-right had
   its zero end on the Neumünster junction; 56pt put it on the
   town label; the clear band lies between the Neumünster rail
   approach and the canal/rail bottom exits.
4. **THE TRAVE** → (10.15, 53.845), the clear triangle north of
   the Hamburg–Lübeck corridor, on the river's real (undrawn)
   upstream course toward Bad Oldesloe; crossed once by the A7
   bundle at a word gap. The old spot at the drawn trace's head
   sat ON the motorway/rail pair.
5. **SCHLESWIG-HOLSTEIN → SCHLESWIG + HOLSTEIN** (the duchies,
   separately placed). An obstacle audit (all edges, coasts,
   rivers, town-label boxes) found NO placement of the composite
   ~2°-wide tracked name — single or stacked — clearing the road
   net and the Elbe-estuary coast; minimum anywhere was 5–7
   collisions. The halves each sit with exactly one
   near-perpendicular route-bundle crossing: SCHLESWIG (9.38,
   54.68), HOLSTEIN (10.05, 53.97). This is also the text's own
   working vocabulary (the covering force trades Holstein; the
   corps holds Schleswig). **PROVISIONAL — DK ratification
   owed.** Knock-on: THE SCHLEI moved onto its own firth
   (10.01, 54.575), out of SCHLESWIG's band.

Convention changes (DK proposals in-pass, both **provisional**):

6. **Rail**: single centreline for both classes; ticks one side
   for single track, both sides for double (the period topo
   convention; the old double-line + through-ticks distinction
   was subtle at plate scale). Tick side for singles is keyed to
   compass (north side; east for near-vertical runs), not vertex
   order, so adjacent runs digitized in opposite directions agree
   — DK's stated counter-brief. Legend swatches match.
7. **Frontiers dotted, not dashed**: Danish frontier 0.8pt fine
   dots; IGB 1.1pt heavier dots (keeps its two crossing gaps).
   Differentiates the border class from ferry dashes at a glance
   — and a border held in dots is the right philosophical weight
   for plates that carry clean prewar geography (DK). Watch item:
   the neck plate's marsh stipple is also dots; at proof scale
   they read differently (area vs line), but the instrument gate
   should confirm.

---

## Instrument gate (§7) — RUN AND CLOSED, 2026-07-27

One combined Opus pass (doctrine auditor + veteran reader +
period-accuracy reader), howlers-only remit, over both plates at
full resolution with the atlas data and build history as ground
truth. **Verdict: CLEAN — zero blockers on all three lenses.**
Specific clearances: LANDJUT HQ at Rendsburg; Danevirke corridor;
all five crossing sites real and correctly typed; Great Belt
ferry-only (no fixed link, verified in data and stroke); Little
Belt two-bridge pair; Storstrøm solid with no Farø (1985);
Fehmarnsund solid vs Vogelfluglinie ferry; E3 period gaps drawn
as trunk; no post-1983 E-numbering; double→single rail change at
Vamdrup; native Danish spellings internally consistent; IGB east
of Ratzeburg with its two legal gaps; marsh stipple reads as area
texture, distinct from the dotted frontier line class.

Two NOTEs, neither a howler, dispositions:
1. Nordfeld ferry node: the TOML note said "NW of
   Friedrichstadt" while the GUESS coordinate sits upstream
   (ESE) — self-contradiction. FIXED: note rewritten to record
   the contradiction and the more-plausible coordinate half
   (Gut Nordfeld/Drage), still GUESS-tier, site unverified.
2. Legend carries "motorway" as its only road class while
   trunk/federal/secondary draw unlegended — composition
   matter, outside the howler remit, ACCEPTED under the
   officer-from-memory ruling.

With this, every gate the spec owes is discharged; the plates
are LOCKED for the first edition.

## Converter switch — Chrome-free assembly (2026-07-31, session 3d8e73ea; DK-directed)

The plate SVG→PDF step moved from an undeclared host
`google-chrome` to `rsvg-convert` (librsvg, now declared in
flake.nix; chain in scripts/svg2pdf.py: rsvg → cairosvg →
chrome-legacy). Measurement findings, for the record:

- Geometry was pixel-exact under both converters (100-unit ruler:
  416px vs 416px at 300dpi). But **Chromium had been rendering
  `<text>` ~12% below the spec'd font-size** (controlled test,
  20pt Pagella "Hxg": FreeType ground truth 158×81px @300dpi;
  rsvg 155×80; Chrome 138×71). The plates were designed,
  hand-passed, and ratified around Chrome's shrunken labels.
- Since the plates are LOCKED, the ratified *appearance* is the
  target, not the SVG's nominal spec: `TEXT_SCALE = 0.88` (env
  `ATLAS_TEXT_SCALE` to override) now compensates in
  atlas/render.py, chosen by sweep — untracked labels (the
  collision-relevant class the hand-pass tuned) match the
  ratified renders glyph-for-glyph (Haderslev span 122px ↔
  122px; Odense/Korsør gap preserved).
- Residual, quantified NON-MATERIAL: (a) letterspaced display
  text (title/subtitle/region ghosts) runs 3–6% narrower — the
  engines disagree on letter-spacing units; narrower is
  collision-safe and all such text is center-anchored; (b)
  antialiasing halos on dense line art (aligned mean|d| ≈
  4.9/255; 2.7% of pixels >64/255 — ±1px stroke-edge effects);
  (c) the page box is now EXACT to the SVG (377.63pt where
  Chrome rounded to 378pt) — the new output is the more faithful
  one. No layout, content, or face changes. Comparison crops in
  the session record.
- The published first-edition artifacts at `first-281500ZJUL26`
  remain the edition of record (built with the Chrome plates);
  rebuilds from main reproduce them within the tolerance above.
  *UPDATE 2026-07-31 (372bd078): superseded by the barcode-errata
  resubmission at `first-312200ZJUL26`, whose artifacts are built
  with the rsvg plates — the tolerance above is now the published
  state, not a divergence from it. The eBook plates (make epub,
  PNG) come off the same chain.*
- Same commit closed the other two host leaks: pdfjam (now via
  texliveSmall.withPackages) and pillow (flake python). The full
  `make pdf-screen` — plates, cover, wrap, trims, assembly — now
  runs hermetically in `nix develop`, and in plain sandboxes via
  apt packages alone.
