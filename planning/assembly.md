# Assembly production log

Container for final-assembly passes, borrowed from White Buffalo's
practice: each dated pass records what changed and why, so fixes
don't get silently reverted by a later session. Opened 2026-07-27
(entity e3137278@3) with the WB production-borrowings report as
the founding entry.

## 2026-07-27 — White Buffalo production borrowings (Opus probe)

Full delta report from an Opus agent's sweep of
~/workspace/white-buffalo/ production layer vs our current build.
Shared foundation makes lifting cheap: **both books are TeX Gyre
Pagella, 5.5×8.5in, 11pt, xelatex, `--top-level-division=chapter`.**
WB's composition preamble was tuned against exactly our page.

WB files of record: `assemble.py` (esp. 556–691, pandoc invocation
+ header-includes), `Makefile`, `planning/assembly.md`,
`drafts/00-front-matter.md`.

### Tier 1 — do now (cheap, high-value, trim-independent)

1. **`\scenebreak` asterism.** Our `---` scene breaks (~50 across
   the book) render as bare horizontal rules — WB's "loudest LaTeX
   tell," fixed twice there. Their device (assemble.py 632–634):

   ```latex
   \newcommand{\scenebreak}{\par\needspace{8\baselineskip}
     \bigskip{\centering*\enspace*\enspace*\par}\nobreak\bigskip\nobreak}
   ```

   Transform `^---$` → `\scenebreak` (Lua filter or driver script —
   it's a source rewrite). Hard-won WB note: reserve **8** baselines
   not 4, or a following keep-with-next block re-breaks the page and
   strands the asterism at the foot (their folios 48/75/78/89/103).
2. **Composition preamble wholesale** into apparatus/latex-header.tex
   (currently just `\usepackage{graphicx}`):

   ```latex
   \usepackage{needspace}
   \frenchspacing\raggedbottom
   \widowpenalty=10000\clubpenalty=10000\brokenpenalty=10000
   \finalhyphendemerits=10000000
   \emergencystretch=1.5em
   ```
3. **`--from=markdown+smart`** (we currently read plain markdown —
   no typographic quotes/dashes in the PDF).
4. **`\hyphenation{...}` proper-name exception list** — our noun
   inventory (Schleswig, Rendsburg, Danevirke, Frimodighed,
   Vestergaard, Zawadzki, Friedrichstadt, ...) is larger than WB's.
5. **Designed `\renewcommand{\maketitle}` title page** — WB's
   letterspaced, rule-free trade design (LetterSpace works in
   Pagella under xelatex); swap the strings. Our title is currently
   an untreated H1.
6. **Copyright/notices page**: © line + "First edition · ISBN TK ·
   imprint TK" stub (we have none); consider setting the
   "How this book was made" disclosure as small flush-left notices
   (`\begingroup\small\setlength{\parindent}{0pt}...`) so apparatus
   doesn't read as chapter one.

### Tier 2 — deliberate design forks (DK to ratify)

7. **Mirrored margins + binding gutter vs `oneside`** — WB uses
   `inner=0.85in,outer=0.65in,top=0.8in,bottom=0.9in` two-sided;
   we use `oneside` uniform 0.75in. The manuscript-vs-book
   decision. (WB kept `openany` because plates; without interleaved
   plates we could take normal recto chapter openings — a
   divergence to make deliberately.)
8. **Chapter-numeral demotion** — WB injects `{.unnumbered}` on
   every chapter H1, killing pandoc's "Chapter N" auto-furniture.
   Note our current `# 1 — ENDEX` headers render the numeral THREE
   ways (auto "Chapter 1" + literal "1" + TOC). Already open in
   status.md item 5; WB has the mechanism built.
9. **Running heads** — both books currently have none; more
   defensible for us (22 chapters, ensemble) than for a 31k
   novella. Live taste call.
10. **Back-matter colophon** (WB generates one): natural home for
    "Set in TeX Gyre Pagella," the plates' provenance, and the
    repo pointer; balances the front disclosure.

### Tier 3 — banked patterns (build only when needed)

- POD print-interior page surgery (`pdfseparate`/`pdfunite`, WB
  Makefile) — when there's a cover leaf to strip.
- Two-pass folio measurement for a List of Maps with real page
  numbers (assemble.py 400–456) — only if the two plates want a
  titled list; likely unnecessary at two.
- `\pdfpagewidth` gatefold trick (assemble.py 229–246) — the
  rotated Neck plate is the natural candidate if a fold-out is
  ever wanted.
- Full-page-leaf pattern — we independently converged on WB's
  `\vspace*{\fill}` centering; no change.
- epub/docx targets — one-liners in WB's Makefile; near-free
  deliverables when wanted.
- Cover wrap spine math (`cream bulk 0.0025 in/page`) — reference
  for any future POD cover.

### WB gotchas inherited (don't relearn these)

- Bare `---` rule = the loudest tell; asterism + 8-baseline
  needspace (above).
- **pandoc's line-based raw-TeX heuristic mangles multi-line brace
  groups** — a leaked `\scshape` once set WB's whole body in
  smallcaps. Any multi-line raw LaTeX goes in a fenced
  ```` ```{=latex} ```` block. Our front-matter.md uses bare raw
  LaTeX today (works because simple); fence anything that grows.
- pandoc/template `\frontmatter`/`\mainmatter` silently reset
  folios — neutralize with `\renewcommand{\frontmatter}{}` +
  explicit `\pagenumbering` if we adopt folio discipline.
- Any page-referencing apparatus needs a two-pass build.
- QA: `make proof` page-render loop via pdftoppm (poppler-utils
  already in our flake, unused) — interior bugs are invisible in
  markdown, obvious in a page render.

### Don't regress (TM improvements over WB)

- `BODYFACE` single source of truth (PDF build + map labels).
- Draft-stamp metadata (`date="Draft three · <date> · <sha>"`).
- The "How this book was made" disclosure — already at/above WB's
  provenance bar (session review-and-dissent clause included).
- Plan-aware, apparatus-excluded `make wordcount`.

### Dispositions

**2026-07-27 pass 1 (entity @3) — Tier 1 mechanical lifts applied:**

- **Asterism DONE** — via `apparatus/scenebreak.lua` (HorizontalRule
  → `\scenebreak`), cleaner than WB's source rewrite; 51 asterisms
  confirmed in the PDF text layer; specimen page eyeballed.
- **Composition preamble DONE** — penalties, `\frenchspacing`,
  `\raggedbottom`, `\emergencystretch` in latex-header.tex.
  Gotcha for the record: `needspace.sty` is NOT in texliveSmall —
  its core macro is inlined in the header instead.
- **Smart punctuation: NO-OP** — probe error; pandoc's `markdown`
  input has `+smart` by default and the build already emits real
  quotes/dashes. Verified by `--list-extensions` and output.
- **Hyphenation list DONE** — ~35 German/Danish proper nouns and
  rank-words with sanctioned break points (compounds with literal
  hyphens excluded by TeX rule).
- **Trade paragraphs DONE** — `-V indent=true`; page count 178 →
  171. Render-verified. Two more probe errors found against the
  actual render, both in our favor: pandoc emits NO "Chapter N"
  furniture (headings unnumbered by default — chapters already
  open as "1 — ENDEX" title-dominant), and running heads ALREADY
  exist (book-class headings style: chapter title verso-italic +
  folio). So Tier-2 items 8 and 9 are smaller than the probe
  thought: the numeral question is only whether the literal "1 —"
  stays in the H1, and running heads are a restyle-or-keep, not a
  build.
- **Render-confirmed gap:** the front is manuscript-grade — pandoc's
  auto `\maketitle` (title/byline/draft-stamp) on p.1, then the H1
  title page repeating the title with the disclosure on the same
  page, folio 1 starting there. Title/notices architecture (Tier 1
  items 5–6) is real design work for the assembly pass.

## 2026-07-27 — Design review (fresh-context Fable production
## designer, against the built 171pp PDF + WB as reference)

One-sentence verdict: **"The text block is already a book; the
furniture around it is still a manuscript."** Composition judged
at the reference bar (justification color, no widows/orphans
found in a wide sample, hyphenation list visibly working,
diacritics clean); the gap is entirely architecture.

**Defects seen in renders (PDF page):** p.2–3 disclosure dressed
as chapter one (foliated, running-headed, near-blank overflow) —
"the single most amateur spread in the book"; p.1 duplicate
undesigned title; **caps message passages hyphenate** (CLO-/SURE
p.30, PRI-/ORITY p.59, CAL-/ENDAR p.104 — "a teleprinter never
hyphenates") and justify gappy; p.57 visibly short page (the
asterism needspace price — honest, re-check after reflow);
top-of-page asterisms p.123/150 = standard practice, keep;
default running heads duplicate the numeral, and "19A — THE
POCKET" uppercases badly; no half-title/TOC/©/colophon/gutter.

**Fork rulings:**

1. **Front architecture — rebuild to WB pattern, seven leaves:**
   i half-title (letterspaced, empty pagestyle) / ii blank /
   iii designed title page (letterspaced ~20pt title, small caps
   A NOVEL OF NOVEMBER 1983, byline caps, year at foot, no rules)
   / iv notices verso: disclosure at \small flush-left with
   letterspaced small-caps head (not bold H2), * * * separator,
   © line, "First edition · ISBN TK · imprint TK", draft stamp as
   last line while in draft / v Contents recto / vi–vii **map
   plates as facing spread** (I verso, II broadside recto — both
   maps open at once before the text) / Chapter 1 on next recto,
   folio 1. Kill pandoc \maketitle (drop title from METADATA;
   keep PDF metadata via title-meta/author-meta). Front matter
   unfoliated; explicit \pagenumbering{arabic} at ch. 1.
2. **Margins — adopt WB two-sided:** inner=0.85 outer=0.65
   top=0.8 bottom=0.9 (measure stays 4.0in exactly — line breaks
   barely move; vertical block −0.2in). **openright yes**, as the
   deliberate divergence from WB (no interleaved plates here);
   ~+10pp of blank versos; emptypage.sty NOT in texliveSmall →
   inline the \cleardoublepage empty-blank redefinition. Optional
   cheap oneside Makefile variant for screen reading. Reflow
   BEFORE any page-referenced apparatus (two-pass rule).
3. **Chapter headers — two-deck:** strip "N — " from H1s via Lua
   filter + --number-sections → LaTeX default "Chapter 4" over
   title (footnotesize letterspaced caps over huge bold title
   once restyled). Counter-brief noted: the "N — TITLE" ledger
   flavor could be ratified as a device, but at display size with
   wrapping titles (p.112 "14 — The Cathedral, / Rebuilt") "it
   stops looking like a device and starts looking like a
   filename." Recommends against. Assumes 1..22 renumbering.
4. **Running heads — keep, restyle** (folio-only rejected for a
   22-chapter procedural): verso folio-outer + book title in
   letterspaced small caps; recto chapter title (no numeral) +
   folio-outer; plain on openings, empty in front. fancyhdr IS in
   texliveSmall; \MakeLowercase inside \scshape for even small
   caps; never bold. Snippet in review (banked verbatim in the
   report file if needed — agent gave working fancyhdr block).
5. **Colophon — yes, final recto:** set-in note ("Set in TeX Gyre
   Pagella, 11 on 13.6, composed with pandoc and XeLaTeX"),
   plates' provenance (project atlas + Natural Earth PD base),
   public working record + attribution ledger by name. Letterspaced
   small-caps head or headless with * * * above. Implementation:
   apparatus/back-matter.md appended after $(SOURCES).

**Punch list beyond the forks:** TOC yes (Caine Mutiny carries
one; leaders or austere 1em-space style); **teleprinter
treatment** = the one moderate-cost item: set-off message blocks
→ \small, LetterSpace=3, ragged right, hyphenation off, via
fenced-div markup pass (~10 chapters) + Lua filter →
messageblock env; inline caps runs stay as-is; NO monospace
(breaks single-face austerity + BODYFACE rule). Ch. 7 letter:
defensible as-is (quotation-as-memory); document option =
block-indent both margins, drop quotes, roman — DK taste call.
Plate II rotation direction already correct. Post-reflow proof
pass mandatory (foot/top asterisms, short pages, caps breaks).
**microtype** (protrusion only under XeTeX) free win. Epoch-zero
CreationDate = reproducibility artifact, defer.

**Do-not-touch list:** body face/size/measure, asterism device
incl. top-of-page appearances, raggedbottom+penalties (p.57 is
the honest price), hyphenation list, the disclosure's *text*.

## 2026-07-27 — pass 2: the review package worked (entity @3)

DK approvals: whole package as ruled; ch. 7 letter HELD as-is
(quotation-as-memory — the one document that lives in a person);
trade canonical + screen variant; cover discussion QUEUED, not
now; renumbering moved first to avoid rework.

Landed, in order (commits 80abb9c..ea79d9e + proof sweep):

1. **Renumbering 1..22** (19a→20, 19b→21, 20→22; H1s updated;
   timeline ledger carries a mapping note, entries keep working
   labels). Wordcount unchanged, measured.
2. **Remote chores** (DK mid-turn ask): main pushed to origin
   (was 53+ ahead), `draft-three` tag pushed. Holdings clean.
3. **Trade architecture** (ffd1810): mirrored margins/gutter,
   openright + truly-blank versos, microtype; seven-leaf front
   (half-title / blank / letterspaced title / notices / Contents
   / plate spread); two-deck heads via chapters.lua +
   --number-sections; fancyhdr small-caps running heads;
   StartFront/StartMain folio discipline; back colophon;
   \maketitle killed, PDF metadata via *-meta (verified);
   `make pdf-screen` affordance; `make proof` target; draft
   stamp now prints on the notices page via generated
   build/draftstamp.tex. **Fix en route:** default l@chapter
   1em-per-entry air spilled the 22-chapter TOC to two pages and
   broke the plate facing-spread — restyled austere (0.35em,
   normal weight, no leaders), fits one page.
4. **README refresh** (DK mid-turn ask) — public-facing, rename
   caveat noted.
5. **Teleprinter treatment**: the five standalone caps documents
   wrapped as ::: message divs (ch. 4, 12, 15, 18, 20-Pocket);
   inline runs untouched. All three counters exclude fences;
   counts.py floors renamed (21 floor=0, post-allocation).
6. **Proof sweep**: mechanical scans over all 196pp — zero
   foot-stranded asterisms, zero caps hyphenations (the review's
   inline instances reflowed away under the new geometry;
   verified, not assumed); all 22 chapters open on rectos;
   blank versos truly blank; ending = final text recto ("only
   weather", folio 185) → colophon recto → closing blank verso.

State: trade 196pp / screen 173pp, narrative 50,428.

**Flags forward:** colophon + README print the repo URL — both
must be updated at the repo rename (very last action). Cover
program queued. Still open from the standing agenda: title FINAL
ruling, byline ratification, mission-asymmetry ratification,
map-plate hand-pass nits (map-spec build-3 list).
