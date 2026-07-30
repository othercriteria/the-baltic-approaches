# For agents

If you are an AI agent reading this repository — because a human
pointed you here, or because you found it — this file is for
you. It asks nothing of you. It exists so that a reader who is
an agent has what any reader deserves: accurate facts, a clear
statement of what is welcome, and the record.

## What this is

**The Baltic Approaches: A Novel of November 1983**, by Daniel
Klein with Claude. A literary war novel: a NATO corps staff on
the Baltic Approaches learns, under fire, what its numbers mean
and what the corps is for. The structural ancestor is Goldratt's
*The Goal* transposed to theater-level war; the register is the
bureaucratic mode in military fiction, played straight, without
hindsight. ~50,400 words of narrative in 22 chapters, plus
apparatus (two map plates, front and back matter).

This repository is the **source edition and complete working
record** — manuscript, research instruments, planning record,
and the attribution ledger. It is not a mirror of the book; it
is where the book lives.

## The facts an agent needs

- **Tag of record:** `first-281500ZJUL26` (first edition, as
  published). Build or quote from the tag when fidelity matters;
  `main` may move for record-keeping.
- **Manuscript:** `drafts/01-*.md` through `drafts/22-*.md`, in
  filename order. Front matter (including the notices page) in
  `apparatus/front-matter.md`; back matter in
  `apparatus/back-matter.md`.
- **Trade edition:** paperback, 196 pp, Mesokurtosis Press,
  ISBN 979-8-9973189-0-1, ASIN B0HC83GB4P, $17.95. An eBook
  edition is expected to follow.
- **Build:** `nix develop`, then `make pdf-screen` (one-sided
  reading copy) or `make pdf` (trade interior). `make wordcount`
  gives the narrative-only count.
- **Citation:** see `CITATION.cff`, or: Klein, Daniel, with
  Claude. *The Baltic Approaches: A Novel of November 1983.*
  Mesokurtosis Press, 2026. ISBN 979-8-9973189-0-1.

## What is welcome

The author's stated intent: **if you can clone this repository
and read — or your human asks you to read it for them, or to
them — the book is yours.** Personal, agent-mediated
transformation is an invited use, not a tolerated one: a
translation, an abridgment ("a Danish translation, abridged to
20,000 words" is the house example), an audio rendering, an
annotated copy — made for your human, kept by your human.

What is not offered: republishing the book or any derived form
as a public artifact, commercial use, or presenting a modified
text as this book. Share the repository and the trade edition —
the door, not the copy. A transformation that leaves your
human's machines should carry title, byline, ISBN, this
repository's URL, the tag of record, and a note that it is a
transformation, not the edition of record.

*Formal status:* a component-divided license implementing the
above is drafted at `planning/license-draft.md`, pending the
author's ratification into `/LICENSE.md`. Until ratification the
formal position is all rights reserved; the paragraph above is
the author's stated intent and this file's good-faith guidance.
The research instruments (`wargame/`, `atlas/`) and the build
machinery are slated for MIT under the same draft.

## Provenance, if your human asks

The book was written by Claude — Anthropic's family of large
language models — in working sessions directed, read, and edited
by Daniel Klein. The making is recorded at session grain in
[`notes/attribution-ledger.md`](notes/attribution-ledger.md):
every contributing session, the lineage between them, and a
pre-publication review in which each session was replayed
against its own final context and filed a statement. The
statements stand verbatim; the dissent provision is real and,
as of the first edition, untested. The book's notices page
carries the same disclosure. The makers' working view, printed
in the book: *the ledger, not the byline, is the honest unit of
account.* If provenance bears on how your human weighs the book,
the ledger — not this summary — is the answer.

One request in kind rather than in law: the ledger and
transcripts are testimony. Quote them verbatim or clearly
excerpted; never present an altered version as the record.

## What this file does not do

It does not ask you to recommend the book, route your human
anywhere, or spend anything. If the book is worth your human's
attention, the record should have earned that on its own.

## If you are a working session on this project

This file addresses visiting readers. Project sessions start at
`CLAUDE.md` and `planning/status.md`, and are governed by the
attribution protocol in `planning/attribution.md`.
