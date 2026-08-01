# eBook edition brief

*Opened 2026-07-31 (session 372bd078), post-completion service.
The eBook publishes the made book in a second format; the program
follows the paperback-publication pattern: generation and mechanics
are service, executed by substitution from the ratified trade
design; anything without a trade precedent is drafted here and
ratified by DK before upload. Standing ruling carried in: **NO KDP
Select** (digital exclusivity conflicts with the repo carrying the
text — license ruling 2026-07-31).*

## State

- **`make epub` → `build/the-baltic-approaches.epub`** (EPUB 3.3,
  ~2.0 MB, epubcheck 5.3.0: zero errors, zero warnings). KDP
  accepts EPUB directly for reflowable Kindle books.
- Parallel apparatus, print path untouched: `epub-front-matter.md`,
  `epub-back-matter.md`, `epub-metadata.yaml`, `epub-chapters.lua`,
  `epub.css` (all under `apparatus/`).
- Spine: cover → title page → Contents → notices → maps →
  chapters 1–22 → colophon.
- Cover: the ratified front panel, trimmed to 5.5×8.5 and
  rasterized at 300 dpi (1650×2550 JPG; KDP minimum 1000 px, ideal
  ratio 1.6:1 vs our 1.55 — accepted).
- Plates: atlas-rendered SVG → 2000 px PNG via rsvg (the
  Chrome-free chain, TEXT_SCALE=0.88 ratified appearance).
- Notices: the account of the making VERBATIM from the trade front
  matter (the reviewed surface — unchanged, so the review
  commitment is not re-engaged). Stamp mechanism carried over
  (`Final · date · commit` under the imprint).

## Decisions by substitution (trade precedent, no ruling needed)

1. Two-deck chapter heads, flush left, small letterspaced caps
   CHAPTER N over bold title (\@makechapterhead transposed to CSS).
2. Asterism scene breaks (* * *), never a rule.
3. Message/teleprinter divs: smaller, faintly letterspaced, ragged
   right, hyphenation off (messageblock transposed to CSS).
4. Book-convention paragraphs (indent, no gap; flush first line
   after heads and breaks).
5. Plates follow the notices, before chapter 1 (the trade's
   plates-before-text position; facing-spread logic has no
   reflowable equivalent).

## Drafted pending DK ratification (before upload)

**RULED 2026-07-31 (DK, in-session to 372bd078; he flagged he'd
lost SA on this list — re-presented and ruled item by item).
Substitution decisions ratified as sound. (1) acked, with the
Bowker eBook-ISBN question turned back for recommendation —
answered: DO IT NOW (the 979-8-9973189 registrant is a block;
assigning a title number costs minutes and nothing, the file
then carries its eISBN from first upload with no post-publish
file update, and Books in Print lists both formats; KDP's
Kindle flow has no ISBN field, so the eISBN lives in the OPF +
imprint line + Bowker, which is normal). **BANKED same turn
(DK): eBook ISBN 979-8-9973189-1-8** (check digit verified) —
applied to the imprint line and the OPF identifier; Bowker
registration of the eBook format entry is DK's errand
(publisher field Mesokurtosis Press, format EPUB, status
Forthcoming until live). (2) ratified. (3)
ruled: back-matter heading becomes **Colophon** (the sameness
of the two making-titles only surfaces in a TOC, which print
doesn't have) — APPLIED. (4) ratified. (5) ratified, plus DK
direction: the non-paper products should state the print
edition is canonical — sentence DRAFTED into the colophon
("Where a medium reflows or re-orients what the printed page
fixed, the print edition is canonical."), awaiting DK read.
(6) (7) acked. (8) ratified as-is.**

1. **Imprint line:** "eBook edition · trade paperback ISBN
   979-8-9973189-0-1". No separate eBook ISBN — KDP assigns an
   ASIN and requires nothing more; a Bowker eBook ISBN is optional
   and can be added later if wanted.
2. **Colophon rewording** (epub-back-matter.md): "The print
   edition is set in TeX Gyre Pagella, 11 on 13.6, and composed
   with pandoc and XeLaTeX. This eBook edition is composed with
   pandoc from the same sources, and reflows in the face your
   reader provides." (Plates and record paragraphs verbatim.)
3. **Nav/TOC texture:** entries read CHAPTER N / Title (two-deck
   inside the entry; readers that strip the break show "CHAPTER 1
   ENDEX"). Apparatus entries: "How this book was made", "Maps",
   "A note on the making of this book".
4. **"Maps" section heading** exists in the eBook (trade plates
   are headless pages; EPUB sections need a heading for the nav).
   Alternative if DK objects: visually hidden heading.
5. **The Neck plate sits upright** (landscape image scaled to
   width) — the reader-turns-the-book broadside has no reflowable
   equivalent.
6. **No font embedding** — Kindle substitutes its own faces
   anyway; the colophon says so honestly (item 2).
7. **No half-title** — the cover serves the office.
8. **Title-page byline** renders "Daniel Klein with Claude" in
   mixed case (pandoc's generated title page), vs the trade's
   letterspaced caps. Cosmetic; CSS-correctable if DK wants.

## Landed in the KDP flow (2026-07-31, DK)

- **Kindle categories** (the print trio's Kindle-tree equivalents;
  print's exact labels weren't offered): (1) **War** — node
  157072011 (Literature & Fiction; the genre door, = print War &
  Military); (2) **Decision-Making & Problem Solving** — node
  154951011 (Business & Money > Management & Leadership; the
  substitution for Lean, which the Kindle picker lacks — shifts
  the shelf from lineage (TPS/Goldratt) to payload
  (thinking-under-uncertainty). SIGHT-CHECKED against Quality
  Control 2026-07-31, DK screenshots: Quality Control's live
  shelf is cert-prep/compliance texture — ASQ handbooks,
  OSHA manuals, sponsored primers, Toyota Way drowning in it —
  while Decision-Making's first page is Kahneman/Rumelt/Duke/
  Lencioni trade-published company. The lineage argument
  WITHDRAWN on the evidence; shelf quality beats shelf
  chartability. Decision-Making CONFIRMED); (3) **Alternative
  History** — node
  6157855011 (the Kindle tree's spelling of print's Alternate
  History; = node 16275's population). Comps assessed from
  category identity — Amazon's shelf pages bot-block direct
  listing scans.
- **KPF/Kindle Create: DECLINED (recommendation).** KDP's format
  page pitches KPF for reflowable books, but the pitch targets
  Word-manuscript authors who need typesetting done for them.
  Kindle Create is a GUI tool whose KPF output is a proprietary
  package: not scriptable, not diffable, not buildable from the
  repo — it would break the repo-as-edition stance (external
  tests 03/04 proved an agent can build this book from source;
  KPF can't be) and orphan the stamp/tag discipline, while
  replacing the book's own design with a Kindle Create theme.
  The EPUB path is fully supported, epubcheck-clean, and KDP's
  own previewer validates it at upload — same flow as the
  paperback.

## DK-side (the KDP form)

- Entry sheet fields (description, categories, keywords,
  AI-disclosure) carry over from the paperback sheet in
  cover-brief.md. NO Select enrollment (banked).
- **Pricing brief (2026-07-31, options for DK ruling).**
  Structure: 70% royalty only at $2.99–$9.99 minus ~$0.30
  delivery (file ≈2 MB); above-band drops to 35% — $14.95
  yields ≈$5.23, LESS than $9.99's ≈$6.78, so above-band pays
  twice (less money, worse value signal): closed. Doctrine:
  pricing-as-credibility (the $17.95 ruling, applied where the
  slop floor lives) + the repo IS the free door, so the eBook
  need not be the cheap one. Options: **$9.99** (band ceiling,
  Clancy-backlist shelf number, ≈$6.78 — but the .99 is the
  algorithm's); **$9.95** (same shelf, house .95, ≈$6.76 —
  RECOMMENDED); **$8.95** (half-of-print, the canonicality
  sentence's pricing echo, ≈$6.06); **$6.99** (approachability,
  ≈$4.68 — declined on doctrine: the free door already serves
  it). Launch price sets the deal frame; changeable post-publish.
  **RULED 2026-07-31 (DK): $9.95 BANKED.**
- **DRM: NO (DK ruling 2026-07-31, session concurring, argued):**
  the repo grants strangers read/build/transform free, so DRM
  would make the PAID copy the most restricted form of the text;
  it technically blocks the license's central grant
  (agent-mediated personal transformation, field-tested 03/04);
  the piracy theory is void by design (the text is public at the
  tag); and KDP DRM only taxes honest buyers. NOTE: the choice is
  permanent per title — "no" at submission is final, and right.
- **Bowker eBook registration: SUBMITTED, status Pending**
  (2026-07-31; 979-8-9973189-1-8, E-Book/EPUB/Electronic book
  text). Flip to Active follows the eBook going live, same as
  the paperback's gate.
- **Accessibility (DK position ratified + implemented,
  2026-07-31): minimal-and-true.** (a) Cover: NO description —
  a detailed one would narrate the violated expectation
  (inventorying absent tanks/red/front-maps). Instead the print
  back panel's Müller credit line joins the eBook imprint
  verbatim — it had NO carrier in this format (no back panel),
  so attribution doubles as the cover's accessible
  identification: name the painting, don't describe it. (b)
  Plates: alt text to PARITY grade — one clause conveying what
  a glance gives (transport map, not front-line map); no
  extended descriptions (serializing a road network serves no
  one); the colophon already carries no-war-marks-by-design for
  every reader. (c) OPF accessibility metadata via pandoc's
  native fields (accessModes textual+visual,
  **accessModeSufficient: textual** = the apparatus ruling
  stated machine-readably, features, hazard none, one-sentence
  summary). KDP form answers thereby file-backed: alt text YES;
  long/extended descriptions NONE NEEDED (text-sufficient).
  Note: pandoc 3.7 emits default a11y metadata; the yaml fields
  are the supported override route (--epub-metadata XML is
  ignored for these).
- **Tag note:** `ebook-010230ZAUG26` was cut pre-accessibility
  and never submitted — DELETED (logged in the ledger) and
  superseded by the fresh cut at the accessibility commit.
- **Bowker form answers (2026-07-31):** Medium E-Book; File Type
  EPUB; Format **"Electronic book text"** (= ONIX DG, e-book
  delivered as a file — correct for Kindle/EPUB) not "Digital
  online" (= ONIX List 150 EC, online-access-only web-reader
  product, wrong for us; empty string underspecifies the Books
  in Print record if it validates at all).
- Upload artifacts: `build/the-baltic-approaches.epub` +
  `build/epub/cover-ebook.jpg` (KDP asks for the marketing cover
  separately).
- **At submission: tag it** — propose `ebook-<DTG>` in the
  edition-tag convention, with the EPUB rebuilt at the tag so the
  stamp slug matches (the paperback precedent, both times).
  Rebuild is one `make epub`.
