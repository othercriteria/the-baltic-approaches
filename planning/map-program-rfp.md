# Map program RFP — four independent proposals + synthesis

*2026-07-25, session e3137278. DK commissioned: "a slightly
underspecified RFP on maps, throw it at 4 Opus agents." Identical
brief to four independent fresh-context Opus respondents (A–D):
the book's vantage/register, the reader-ledger R1 page-located
evidence (map wanted at chs. 3/7/12, fades after 13), standing
constraints (apparatus = reference/record only; nothing
forecloses the war's shape; register extends to apparatus).
Permission, not obligation, to read the text, mine reference/
planning/atlas, and search the web. Each required to COMMIT to
one philosophy. Proposals verbatim below (§A–§D); synthesis
first.*

## RATIFIED (DK, 2026-07-25, in-session to e3137278)

The convergent program (§Synthesis items 1–5) is RATIFIED. Fork
rulings: **F1 = A/C/D** — draw the IGB and its real crossings
(DK: "Per-war border is territory, not map, so to speak, as
common knowledge"). **F2 = D** — no chokepoint emphasis; the
network drawn honestly, discoverable not briefed. **F3 = no
reprint. F4 = decide at trim proof. F5 = A/C** — full Approaches
including Zealand/København (DK: "Zealand, etc., shouldn't be
let to feel like abstractions, while the construction of the
book works (not unproblematically) to make the Fulda Gap, etc.,
an abstraction"). **F6 AMENDED** — the ruling is agreement
between map and text face, NOT a pin to Pagella specifically
(the book's face is not finally pinned); implement as a
parameter that follows the build. **F7 = one quiet Rendsburg
mark.** Implementation spec: planning/map-spec.md; Opus build
agent commissioned same session.

## Synthesis

### The convergence (all four, independently)

1. **TWO maps** — a theater plate (the Approaches / "the board")
   and a neck plate (the narrows / the waist). All four
   independently rejected both the single sheet (scale conflict:
   a plate wide enough for Lammers' six chokepoints cannot
   resolve Friedrichstadt's three crossings) and the per-Part
   series (a per-Part program leaks the campaign's shape).
2. **Front matter, before ch. 1** — findable from every crisis;
   the ch. 3 debt falls due before any part-opener could pay it.
   All four rejected endpapers on production reality (perfect
   bound = no pastedowns) and in-chapter figures on register
   (textbook plates).
3. **Pure, timeless geography — the clean plate.** No front
   line, no arrows, no units, no dates, no phase lines, ever.
   All four derived this from the book itself: ch. 1's razor
   scene reveals exactly this object, and the reader should hold
   the same clean instrument the staff starts from and draw the
   war on it mentally. The suspense constraint and the
   apparatus rule are satisfied *by construction*.
4. **Monochrome, restrained, period-truthful register** — one
   ink, black as the text; period truth (no Great Belt bridge,
   E3 not E45, Vamdrup double→single) without period pastiche.
5. **Atlas-driven production**: render the network layer from
   atlas/data/theater-1983.toml (small in-repo SVG generator,
   `make maps`), coast/water from a public-domain base (Natural
   Earth) — so the absences tests make the specimen's map-error
   class untypable in the cartography, and the repo stays
   redistributable. Human hand finishes label placement and
   line weights; vector to print.

The convergence is strong enough to treat items 1–5 as the
program, pending DK ratification.

### The forks (real divergences; DK to rule)

| # | Question | Positions | Session recommendation |
|---|---|---|---|
| F1 | Does red's geography appear? | B: red never appears — no IGB crossings, no Rostock ("blue's back garden"; protects the two-crossing-straw reveal of ch. 14). A/C/D: the IGB and its real crossings + edge-of-world Mecklenburg names are period map fact; omitting Lübeck makes chs. 2–4 unreadable | A/C/D — draw it, but plainly (see F2). The IGB was on every 1983 sheet; the *reveal* is the arithmetic, not the geography |
| F2 | Chokepoint emphasis | C: draw the six throats as the sheet's most legible features. D: emphasize nothing — draw the network honestly and let the reader count Lammers' six off the map himself ("annotate the constraints and you've briefed the reader"). B: one graphic event only (the Vamdrup tick) | D's discipline. Emphasis is a didactic seam; an honest drawing of double-track going single IS visible. This also resolves F1: the IGB's two gaps drawn truthfully, not spotlighted |
| F3 | Map 2 reprint at Part III opener? | C: yes (free art, thumb-span refund at 19a). A: no (reprints invite "updating" = drift toward the forbidden trace). B/D: shown once | No reprint (3–1, and A's anti-drift argument is principled). Revisit only if the next panel asks |
| F4 | Friedrichstadt resolution | A: corner inset on Map 2 (three crossings within ~1 km collapse at neck scale). B/C/D: inside Map 2's main frame | Decide at the trim proof: if the three crossings don't separate at 5.5in, A's inset. Production detail, not philosophy |
| F5 | Theater extent | A/C: Aalborg→Hamburg/Rostock INCLUDING Zealand + København (the beach-watch, Korsør, the Belt lift are a full subplot). B: west coast→Great Belt only (loses Zealand/Vogelfluglinie). D: Little Belt→Hamburg (loses Aalborg–Aarhus — half the ninety-hours corridor) | A/C's full Approaches. Ch. 3 needs the whole corridor; ch. 15 needs the Belt run and Korsør; Aakjær's island needs to exist |
| F6 | Label face | B/D: the book's own body face (TeX Gyre Pagella) — "a map lettered in the body font is felt as continuous with the prose." A: plain period cartographic face. C: period face + hand-lettered accents for staff additions | B/D. Also cheaper. C's hand-lettered accents contradict the clean-plate thesis (a pre-chinagraph base carries no staff hand) |
| F7 | HQ mark | A/C/D: one quiet Rendsburg mark (tick/ring/square) — the vantage is record. B: none singled out | One quiet square. The book is the view from that room |

### Other adoptables (single-respondent ideas worth keeping)

- B: frames overlap at Rendsburg-on-the-canal so the sheets
  register on a shared landmark like two overlays; the
  theater→neck zoom mirrors the campaign's own contraction.
- C: the atlas absences tests as the map's proofreader, stated
  as gate; `atlas render` as a tested in-repo command.
- D: no art across the gutter (perfect-binding eats it);
  labels ≥6.5–7pt at trim; "the map is as blind to red's rear
  as the corps is" — usable as the one-line design brief.
- A: proof gate — run the plates past the doctrine/veteran/
  period instruments before lock, like any other apparatus.
- B: for a future case-bound edition the same vectors promote
  to true endpapers unchanged.

### Next steps (pending DK ratification of the program + forks)

1. Prototype `atlas render` (SVG from TOML; nodes/edges styled
   by class; absences enforced by construction) + `make maps`.
2. Pull PD base geometry (Natural Earth coast/water; hand-trace
   Schlei/Eider/canal/Treene at neck scale; Danevirke trace from
   reference/danevirke.md).
3. First trim-size proofs of both plates in the reading build;
   F4 decided on the proof.
4. Label/line-weight hand pass; instrument proof gate; lock.

---

## §A — Respondent A (verbatim)

The book already contains its own map. Chapter 1 opens with a German captain on a chair, taking nine days of chinagraph off the operations board with a razor blade until "the map of the Baltic Approaches emerged at 1:250,000, clean, the peninsula hanging down into Germany like something anatomical." **The map program is that base sheet, undressed** — the ground the corps fights over, with every mark the staff made on it withheld. The reader is handed the clean plexiglass and made to draw the war on it in their own head, chapter by chapter. That is the book's method (the wall shows inputs, not conclusions; the reader does the subtraction) turned onto its own apparatus. It is also, not coincidentally, the design that cannot spoil a single suspense mechanic, because it shows no war at all.

I commit to **two maps, both pure static geography, no front, no arrows, no dates, no enemy** — placed in the front matter as a findable pair.

**(1)** Two. Not one, not per-Part. The reviewer's instinct ("a single front-map would have refunded hours") is right about *timing* and wrong about *count*, because the pain occurs at two irreconcilable scales: **Map 1 — THE APPROACHES** (theater, ~1:1,000,000), the whole LANDJUT geography Aalborg→Rostock, serving ch. 3; **Map 2 — THE NECK** (operating area, ~1:250,000 — the ch.-1 scale), the waist of the peninsula, serving chs. 7 and 12. A theater sheet physically cannot show that the Eider has three separate crossings a kilometre apart; a neck sheet cannot show a 400-km march corridor. Two sheets, doing a **coarse→fine handoff**, is the honest minimum — and it stops there. Map 2 carries one small titled **detail-inset** in a corner: the Friedrichstadt / Sorgbrück / Nordfeld cluster — three dots that collapse to one at neck scale but are the whole confusion of ch. 7.

**(2)** Both in the front matter, as a facing/sequential pair before chapter 1. Findability (the reader thumbs to the front by reflex; a part-opener buried at ch. 9 is invisible at ch. 7); the ch.-1 rhyme (the reader has already held what the captain uncovers); no reprints (every reprint is a temptation to "update" the map with where the front now is — which is the spoiler; static maps, printed once, cannot drift). Reject in-chapter maps (a snapshot of the front = spoiler) and endpapers (a hardcover feature).

**(3)** A period NATO/German staff base sheet at ~1:250,000 — the JOG/TK-series look of the early 1980s — rendered monochrome and clean. Water open; land plain; relief only where load-bearing — the **Danevirke as a hachured earthwork**, the **Treene/Eider marshes** as marsh stipple. Roads by line-weight and dash encoding the atlas's own classes; rail with double vs. single tick (Vamdrup, the Marschbahn); ferries as dashed sea-routes; the IGB as a plain national frontier. Plain period cartographic face, 1983 spellings. Bar scale, north tick, graticule ticks. No compass rose, no cartouche, no unit symbology. The register should *be the object the characters work on*, stripped of their chinagraph.

**(4)** Refusals: the front line, ever (the suspense guarantee and the thematic engine); arrows/axes; formations/unit boxes/OOB symbology (the cast/OOB table's job); time (no dates, phase lines, DTGs); the enemy as enemy (Mecklenburg, the IGB, Rostock, Schlutup, Herrnburg appear as geography and real infrastructure — nothing colored, nothing arrowed). The refusal is the point: *why* the pinch matters stays in Lammers' mouth; the map only lets the reader put a finger on each noun.

**(5)** Worked Map 1: portrait plate, graticule ticks at 54–57°N/9–12°E, title block THE APPROACHES · NOVEMBER 1983, four-line legend. Extent Aalborg to Hamburg/Rostock, North Sea to København — never the GDR interior. Full E3 chain named; **Rendsburg carries a single quiet HQ tick**; the Little Belt bridge pair as the only fixed pinch; the Great Belt as a dashed ferry route (no 1983 bridge, atlas-enforced); Storstrøm; Vogelfluglinie; the double→single change at Vamdrup; the IGB with Schlutup and Herrnburg as real crossings. At ch. 3 the eye runs the E3 down Jutland and lays the pinch points onto the route itself — the list becomes a road. At ch. 12 the eye returns for a different job: sea on both flanks, nowhere left to give; coarse fix here, then drop to Map 2 for Sehestedt, the Danevirke, the exact crossings.

**(6)** Production: geography from atlas/data/theater-1983.toml (authoritative, period-verified, absences enforced); PD-only base (Natural Earth CC0; hand-digitized canal/Danevirke/marshes) — no purchased or scanned basemap touches the build. Add `python3 -m atlas geojson` (~40 lines) so the map *regenerates from corrected data*; style in QGIS or scripted render; a cartographer/designer does the period-register pass; export press-ready vector. Proof gate: doctrine auditor / veteran reader / period auditor before lock. Print spec: 1-color black from the first stroke; pure vector; full page inside the existing live area; theater plate rotated to landscape if width demands.

## §B — Respondent B (verbatim)

The book's first chapter opens on a map **razored clean** — the acetate the corps starts each morning with, before anyone grease-pencils the war onto it. That clean base overlay is not a metaphor to decorate; it is the whole program. **The reader gets the same blank instrument the staff gets, and fills it from the prose exactly as the staff fills theirs from reports.** No front line, no unit, no arrow, no date. This is not timidity about spoilers — it is the book's epistemology made physical. The apparatus rule and the suspense constraint are the same rule, and the clean overlay satisfies both by construction.

**(1)** TWO. Not the per-Part maps the outline drafted (rightly rejected: three operational fronts *are* a campaign trace), and not the single sheet (the reviewer's floor, not the prescription). **Map 1 — THE APPROACHES** (the ninety-hours corridor): Aalborg down to Hamburg, the two Belts to the east; every one of Lammers' six places sits on this sheet. **Map 2 — THE NECK**: Husum to Eckernförde, the Kiel Canal up to Schleswig and the Danevirke; serves ch. 7 and ch. 12, carries four of ch. 3's six chokepoints, and keeps paying off silently through chs. 13–19. The two frames **overlap deliberately at Rendsburg-on-the-canal** — the southern margin of Map 1 is the middle of Map 2 — so a reader hands off on a shared landmark, the way you register two staff overlays by a common tick. The theater→neck zoom **mirrors the campaign's own contraction** — achieving thematically what a front-trace would achieve literally, at zero spoiler cost.

**(2)** Front matter, recto plates, shown once; Map 2 facing the opening of Chapter 1. Not endpapers (perfect-bound paperbacks have none — call the thing by its true production home). Not in-chapter (would repeat at 7 and 12; textbook plates; fragile under pandoc float placement).

**(3)** The clean base overlay, inked by the headquarters' own hand. Not a period NATO staff map (that path needs APP-6 symbology we're refusing), not modern GIS (tourist-atlas register). Monochrome, printed in the same black as the text; water as pale tint or fine stipple; fine single-weight coastlines; the canal a firm double line; rail as ladder-hatch; the **Danevirke as period earthwork hachure** — the single antique flourish, earned. Place names in small caps in the book's own face (TeX Gyre Pagella). Plain N, plain scale bar, **no grid squares** — a grid is a staff overlay, and an overlay is the war. Period stance: drawn now, for the reader, obeying **1983 truth** — period-truthful, not period-pastiche.

**(4)** Refusals: any front line/FLOT; unit symbols/OOB; axes/arrows (one arrow spoils chs. 15–19); **red — entirely** (no IGB crossings, no Schlutup/Herrnburg, no Rostock/Wismar: red's approach and the two-crossing neck are late reveals; the maps are blue's own ground and back garden); dates/phase lines/the political guidance lines; capacities/tonnages/any atlas number (the map says *where*; the prose says *why it meters the corps*).

**(5)** Worked Map 1: portrait at the 4.0in live width; ~57.1°N to 53.5°N, 8.5°E to 11.3°E. The E3/A10 spine with the Christiansfeld–Skovby gap shown open (period truth); the rail hatch changing double→single at Vamdrup — **the one deliberate graphic event, nothing else emphasised**; the Little Belt bridge-pair; the Great Belt ferry berths with no bridge; ~14 place names; Fredericia carries no special mark — but a reader who reaches ch. 16 will come back and find it. At ch. 3 the eye physically counts the constrictions — orientation, not instruction. At ch. 12, Map 1 honestly **runs out at the top of the fight and hands off**: the eye finds Rendsburg at the bottom margin, recognises it as the middle of Map 2, turns the page. On Map 2 the ambiguity dissolves into fixed geography — the reader now knows which shoulder is which, and still has to learn from the prose that Holt weighted the wrong one. Position resolved; suspense intact.

**(6)** Production: atlas-driven and de-risked — `python3 -m atlas path aalborg rendsburg --profile convoy` already returns the Vamdrup chokepoint machine-verified against canon. Base from PD/open vectors (Natural Earth coast; OSM-derived centrelines filtered through transport-1983.md; the Danevirke line from reference/danevirke.md). In-repo generator → SVG; human cartographic pass for ink weights, label collisions, the hachure; SVG → PDF vector; source lives in apparatus/ behind `make maps`. Print: black only (pure K), hairlines ≥0.25pt, labels ≥6.5–7pt Pagella; full-width figures in the existing front-matter hook (already excluded from narrative wordcount). For a future cover-bearing edition the same vector prints on the inside cover.

## §C — Respondent C (verbatim)

This book's whole method is a wall that shows inputs and refuses to show movement. **The map program must be built of the same refusal.** Two maps, both pure terrain-and-network, showing the ground the corps holds and *nothing the corps decides*. The reader is handed the same base sheet Roloff pinned up before he started inking, and told: here is the ground; the war is what you can't yet see on it. That is the two-columns ledger made spatial.

**(1)** **Map 1 — "The Baltic Approaches."** North Jutland to the Elbe, the North Sea across to Zealand and the Mecklenburg shore. Its subject is *the transport network*, drawn so that the six chokepoints of Lammers' speech are the map's most legible features, **as geometry, never as numbers**: the Little Belt pair as a visible pinch; the Great Belt as a *gap* crossed only by a dashed ferry line; the rail double north of Vamdrup, single south; the Storstrøm thread; the bold canal; the IGB with exactly two gaps — Schlutup road, Herrnburg rail — red's two-crossing neck as a fact of the drawing. **Map 2 — "The Neck."** The waist: canal, Rendsburg, Sehestedt, the Schlei and its head, the Danevirke, Schleswig, the Eider–Treene–Friedrichstadt valve, the marshes, Eckernförde, Neumünster — the west and east shoulders legible *as ground*, so that when ch. 12's fires go the wrong way the reader can see which way was wrong.

**(2)** Front matter as a **facing pair** (Map 1 verso, Map 2 recto — the open book shows both). **Map 2 reprints once, as the Part III opener** (by the pocket breakout the reader is a long thumb-span from the front matter; a reprint is free art and pure refund; Map 1 does not reprint — its job is the first half, and it ends there honestly). Not endpapers (format-illiterate for a paperback; a future hardback promotes the spread unchanged). Never in-chapter (a figure mid-scene is a textbook; and it invites the one annotation the program forbids).

**(3)** A restrained 1983 staff base map — **the clean printed base the wall's overlays were inked onto** — monochrome line on cream. Rahn arrives carrying "one folded map, 1:250,000, Baltic Approaches, 1961 printing, privately annotated." The reader's map should be that base — the sheet before the grease pencil. It is literally the thing the corps cannot annotate its way out of: the ground is knowable and fixed; the war is not. On Map 2 the Danevirke goes in as an antiquarian dashed-rampart symbol — the thousand-year wall already on the sheet, facing south, before anyone alive drew a line near it. [Map 2's few annotated features get hand-lettered accents against a machine-clean base — the overlay/base distinction made visible.]

**(4)** Refusals: no front lines, phase lines, arrows, boundaries, unit symbols, or dates (a map with arrows would be the book betraying its own instrument; the reader draws the arrow in his own head — which is the method); no capacities or tonnages printed on the sheet (the chokepoint shown *as a pinch in the line*); no fictional operational furniture (guidance lines, SPERBER, the salient); no red interior beyond start-state geography. Everything the maps won't draw is the book.

**(5)** Worked Map 1: north up, Aalborg to the Elbe, Husum to Rostock; km scale bar; black on cream (optional muted second ink for water if the build supports duotone, degrades gracefully to one). Regions faint; ~40 dots hand-set; **RENDSBURG the one distinguishing mark on the whole sheet — a ringed dot, the HQ**. At ch. 3 the six places *are already the sheet's most legible features* — the speech stops being a list and becomes a route with visible throats, and the reader supplies the motion himself. At ch. 12 the same untouched sheet reads inside-out: the neck is the narrowest point on the entire board, and *behind it there is nothing but Jutland and the belts, i.e. everything*. The terrain held still; the reader's knowledge moved — the book's two-columns idea, delivered by the apparatus without the apparatus ever teaching.

**(6)** Production: **the map is a rendering of the atlas, not a fresh drawing** — the absences table is enforced by tests, so the Great Belt fixed link *cannot* appear; **the atlas's tests become the map's proofreader.** Extend atlas/ with a `render` command emitting SVG from the TOML (equirectangular at 54°N, or a light conic); coast/marsh from Natural Earth (PD) with the neck-scale detail hand-traced from open sources (redistributability named, not assumed); one styling pass by an illustrator or disciplined Inkscape/QGIS operator; add Sehestedt to the node set; trace the Danevirke from reference/danevirke.md. Print: trade 5.5×8.5, 1-color, vector (SVG→PDF placed as full-page figures); **line hierarchy tuned for the reduction, proofed at trim, not on screen**; front-matter pair may bleed; the Part III reprint sits in the live area.

## §D — Respondent D (verbatim)

The book opens (ch. 1, ENDEX) and closes (ch. 20, coda) on **the same object: a clean map, razored clean.** The book's whole discipline is that the *clean map is reference and record*; the marks on it are the argument, and the argument lives in the prose. **The apparatus gives the reader the clean plate the staff starts from; the war happens on it in the reader's head — and gets wiped, exactly as on the wall.** This single idea resolves all four standing constraints at once.

**(1)** Two maps, one geography at two scales — **a nested reference pair, not a per-Part series**. Map 1 ("The Board"): the full operating area, the canal as its spine, ~24 named places, the transport skeleton, the Danish border at Padborg, the IGB SE of Lübeck. Map 2 ("The Narrows"): the waist only — Rendsburg, Sehestedt, the Schlei, the Treene marshes and the Eider, the Danevirke, and at *this* scale only, Friedrichstadt resolved into its three real crossings. There is a hard scale conflict the single-plate answer can't survive; R1 was right that the answer is not per-Part, under-specified in calling for one plate. If production economics force exactly one, the theater plate survives and the neck degrades to a boxed inset in its lower corner — but the committed recommendation is the pair.

**(2)** Front matter, facing reference spread, immediately before Chapter 1 — after the title and the "How this book was made" page. Not endpapers (perfect-bound production reality, stated rather than wished away). Not part-openers (where a per-Part program would live, and that program is refused). Not in-chapter (tied to a scene = illustration/didactic aid; and the *first* want is ch. 3, so the map must be in hand before ch. 3). Each map on its own page inside the ~4×7in live area; **neither crosses the gutter** (perfect-binding eats gutter-crossing detail).

**(3)** The book's own idiom — which resolves to the period staff base-map, because the book already made that its central object. The map is drawn clean — **the plate before the grease pencil.** One ink (no red/blue: colour-coding the sides is doing the chinagraph's job). **Labels set in the book's own face (TeX Gyre Pagella)** — towns roman, waters small caps; the map must read as a *page of the book*, not a bolt-on plate; a map lettered in the body font is felt as continuous with the prose that venerates it. Hand-feel, machine-truth: generalised coastline, geometrically faithful — a competent staff officer's base map, not a satellite tile and not a decorative antique. We are not choosing an aesthetic *for* the book; we are printing the book's own recurring image.

**(4)** Refusals: no front line, FEBA/FLOT, arrows, phase lines, dates (the load-bearing refusal — the campaign's *shape* is the book's engine); no red/blue, unit symbols, strengths, OOB; no corps boundaries — only Rendsburg marked, a small square, because the reader must know where they are standing; **the map is as blind to red's rear as the corps is** (Rostock, Wismar, Schwerin as edge-of-world names past the IGB; the corps only ever sees red through handsets, and the cartography honours that vantage); **the map does not label its own chokepoints** — it shows the network truthfully (the bridge *pair* as two lines, the rail double-then-single with the tick at Vamdrup, ferries as dashes) and lets the reader *count Lammers' six off the map as he counts them off in speech*. Annotate the constraints and you've briefed the reader; draw the network honestly and the constraints are *discoverable*, which is the book's entire method. No time on the map.

**(5)** Worked Map 1: portrait, 4×7in live area; Little Belt at the top with a corner of Funen and the Great Belt ferry track to Korsør; Hamburg at the south; Husum and the Marschbahn west; Kieler Bucht, the Schlei, Fehmarn east; the IGB SE of Lübeck as the one heavier fortified line (period-honest — it *was* a physical fact on every 1983 map); Rostock/Wismar/Schwerin as terminal names. **The Kiel Canal drawn boldest of all lines** — the peninsula's structural fact and the book's recurring hinge. At ch. 3 the eye traces the march down the plate and counts the six off the map as Lammers counts them off in speech — the ninety-hours arithmetic stops being assertion and becomes a chain the reader can *see* is only as strong as its links. At ch. 12 the same plate is used the opposite way: the eye finds Rendsburg on the canal, Sehestedt east, the Schlei reaching in from the Baltic (the eastern shoulder — the main effort), the Treene marshes west (where the fires get wrongly weighted). **The reader uses the identical clean plate first as a schedule and then as a battlefield — which is precisely the book's own move, the same wall read first as intake curves and then as a war.**

**(6)** Production: the map is the atlas made visible, inheriting the absence tests, so the specimen's error class is *untypable in the cartography* exactly as in the prose. Base from Natural Earth 10m (PD) — and the layer separation is the anachronism guard: the modern PD tile supplies only timeless coast and water; the *network* is drawn from 1983 edges only, so a 1998 bridge can never reach the plate. Purpose-built SVG writer in atlas/ (not matplotlib); the one thing that can't be automated is label collision — a hand pass; **DK rules the aesthetic** (the project's own "human diagnoses, instrument executes" discipline). `make maps` (atlas → SVG → PDF) into the pandoc FRONT_MATTER sequence, already excluded from narrative wordcount. Print: vector, 1-colour black, water as open/hatched field, no bleed, no gutter-crossing art; supply vector PDF (fallback 1200 dpi); ordinary interior-line-art cost tier — the register-honest choice as well as the cheap one.
