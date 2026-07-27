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
