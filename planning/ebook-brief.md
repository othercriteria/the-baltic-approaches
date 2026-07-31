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

## DK-side (the KDP form)

- Entry sheet fields (description, categories, keywords,
  AI-disclosure) carry over from the paperback sheet in
  cover-brief.md. Pricing is DK's call — the 70% royalty band is
  $2.99–$9.99; NO Select enrollment (banked).
- Upload artifacts: `build/the-baltic-approaches.epub` +
  `build/epub/cover-ebook.jpg` (KDP asks for the marketing cover
  separately).
- **At submission: tag it** — propose `ebook-<DTG>` in the
  edition-tag convention, with the EPUB rebuilt at the tag so the
  stamp slug matches (the paperback precedent, both times).
  Rebuild is one `make epub`.
