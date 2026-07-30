# License draft — option (c), component-divided

*Session 3d8e73ea, 2026-07-30. **DRAFT — NOT IN FORCE.** A license
is the copyright holder's act: this file becomes operative only
when DK ratifies it and moves the license text to `/LICENSE.md`
at the repo root. Until then the formal position is unchanged:
© 2026 Daniel Klein, all rights reserved. Drafted per DK
direction (book-site.md §5.1, option (c)): plain language,
divided by component, permissive on the ready-made machinery,
stringent on the record.*

*Design intent, for the ratification read: the repo is the
edition of record. The license's job is to make DK's stated
invitation legally legible — "if you can clone a repo and read,
the book is yours," including agent-mediated transformation for
personal use — without creating a free competing artifact, and
without ever permitting the record to be altered and still
called the record.*

---

## Proposed `/LICENSE.md` text begins here

# License

This repository is the working record and source edition of
**The Baltic Approaches: A Novel of November 1983**, by Daniel
Klein with Claude (Mesokurtosis Press, 2026; ISBN
979-8-9973189-0-1). Different parts of the record are different
kinds of thing, and they carry different grants. Three tiers:

## 1. The book (read it, transform it for yourself; don't republish it)

**Covers:** `drafts/`; the book-text and book-dress parts of
`apparatus/` (`front-matter.md`, `back-matter.md`, `cover.tex`,
`cover-wrap.tex`, `cover-art/`); the rendered map plates; and
any artifact built from these (the PDFs `make` produces).

**You may, free of charge:**

- **Read it**, by any means, human or machine — in the repo
  browser, from a clone, or through an AI agent.
- **Build it**: clone the repository and run the build for your
  own reading copy.
- **Transform it for personal use**: you, or an agent acting on
  your behalf, may produce any derived form for yourself — a
  translation, an abridgment, an audio rendering, a reformatted
  copy, an annotated edition. This is an invited use, not a
  tolerated one.
- **Share the door**: link to this repository, fork or mirror it
  whole (record intact) on a public code host, quote reasonable
  excerpts with attribution.

**You may not, without written permission:**

- **Republish the book or any derived form as a public
  artifact** — no posting the PDF, an EPUB, a translation, or an
  audio version for others to take. Share the repository and the
  trade edition, not extracted copies. (This is the deliberate
  asymmetry: transformation is personal; distribution is the
  edition's.)
- **Use it commercially** in any form.
- **Present a modified text as this book.** A transformation
  that leaves your own machines must carry: title, byline, ISBN,
  this repository's URL, the tag of record
  (`first-281500ZJUL26`), and a statement that it is a
  transformation and not the edition of record.

## 2. The instruments and machinery (MIT)

**Covers:** `wargame/`, `atlas/` (code and data files, including
their tests), `scripts/`, `Makefile`, `flake.nix`, and the
typesetting machinery in `apparatus/` (`latex-header.tex`,
`chapters.lua`, `scenebreak.lua`).

These are ready-made tools — a calibration wargame, a period
transport atlas, a book-production pipeline — and they are
offered as tools, under the **MIT License**:

> Copyright (c) 2026 Daniel Klein and the contributing Claude
> sessions recorded in `notes/attribution-ledger.md`.
>
> Permission is hereby granted, free of charge, to any person
> obtaining a copy of this software and associated documentation
> files (the "Software"), to deal in the Software without
> restriction, including without limitation the rights to use,
> copy, modify, merge, publish, distribute, sublicense, and/or
> sell copies of the Software, and to permit persons to whom the
> Software is furnished to do so, subject to the following
> conditions: The above copyright notice and this permission
> notice shall be included in all copies or substantial portions
> of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT
> WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
> LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
> PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
> OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
> OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
> SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Note: the atlas's base geography is Natural Earth (public
domain); the cover's source painting is a CC0 image from the
Metropolitan Museum of Art (see `planning/cover-brief.md`).
Public-domain inputs stay public domain.

## 3. The record (read it, quote it, never alter it and call it the record)

**Covers:** `notes/` (including the attribution ledger),
`transcripts/` (including `transcripts/raw/` and
`transcripts/attribution/`), `planning/`, `reference/`.

This is the project's testimony: how the book was made, who made
it, what they said, and what it cost. The grant is accordingly
narrow:

- **Read and search freely**, by any means.
- **Quote with attribution**, at fair-use scale or beyond, for
  any noncommercial purpose (scholarship, criticism, journalism,
  process comparison), provided quotations are verbatim or
  clearly marked as excerpted.
- **No modified versions.** You may not publish an altered
  ledger, altered session statements, or altered transcripts,
  or present any modified version of these files as the record.
  The entity statements in the ledger stand verbatim by the
  project's own commitments; this clause extends that commitment
  to downstream copies.
- **No commercial use** without written permission.

Third-party material quoted within `reference/` and
`transcripts/` (doctrine publications, period sources, cited
works) remains its owners'; this license covers only what this
project made.

## Boundaries and notes

- **`holdings/`** is a private submodule of non-redistributable
  source material. It is not covered by this license, is not
  needed to build or read anything here, and is not offered.
- **Non-exclusive.** Nothing here limits the trade edition or
  the copyright holder's other arrangements.
- **No warranty.** The book, instruments, and record are offered
  as-is.
- **Questions and permissions:** open an issue on this
  repository.

## Proposed `/LICENSE.md` text ends here

---

## Open questions for DK at ratification

1. **Machine-learning training use.** The draft is deliberately
   silent: tier 1's "read by any means" plausibly includes
   ingestion, and the project's own provenance (and the
   Checkpoint credits-crowd kinship) cut both ways. Options:
   stay silent; explicitly permit noncommercial training with
   provenance; explicitly reserve it. Needs a ruling before
   ratification, even if the ruling is "stay silent knowingly."
2. **Public verbatim mirrors of built PDFs.** Draft says no
   (share the door, not the copy). Confirm — this is the clause
   that protects both the pricing signal and the KDP channel.
3. **KDP interaction.** Standard KDP is non-exclusive and
   compatible with all of this. **KDP Select is NOT** — it
   requires digital exclusivity and would conflict with the repo
   carrying the full text. Flag for the eBook decision
   (~2026-08-04): do not enroll in Select.
4. **Tier 3 scope.** `planning/` and `reference/` are grouped
   with the record for simplicity; if DK wants the research
   distillations more reusable (they'd serve other Cold War
   projects), `reference/` could move to a CC BY-NC tier. Lean:
   keep tier 3 as drafted; revisit on request.
5. **Tooling legibility.** A bespoke license won't be
   machine-recognized (GitHub will show "custom license"). The
   MIT tier could alternatively live as per-directory LICENSE
   files for SPDX visibility. Cosmetic; decide at ratification.
