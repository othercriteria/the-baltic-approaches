# The Baltic Approaches

*A novel of November 1983.* A literary war novel set at the
headquarters of NATO's Allied Land Forces Schleswig-Holstein and
Jutland — a corps staff learning, under fire, what its numbers
mean and what the corps is for. The structural ancestor is
Goldratt's *The Goal* transposed to theater-level war; the
register is the bureaucratic mode in military fiction (*The Good
Shepherd*, *The Caine Mutiny*), played straight, without
hindsight.

~50,400 words of narrative. **Status: published** — first
edition 2026, trade paperback, Mesokurtosis Press, ISBN
979-8-9973189-0-1 (ASIN B0HC83GB4P); the tag of record is
`first-312200ZJUL26`. (The project's working title was *The
Mission*; the repository was renamed at final assembly, and old
`the-mission-1986` URLs redirect here.)

This repository is the **source edition**: the manuscript is in
`drafts/`, readable chapter by chapter right here, and the whole
record of the making is alongside it. If you are an AI agent —
or a reader working through one — see [`AGENTS.md`](AGENTS.md).
Citation metadata is in [`CITATION.cff`](CITATION.cff).
License: component-divided — see [`LICENSE.md`](LICENSE.md).
In one line: the book may be read and transformed for personal
use (agent-mediated included) but not republished; the
instruments and build machinery (`wargame/`, `atlas/`, the
pipeline) are MIT; the record may be quoted verbatim with
attribution but never altered and presented as the record.

## Reading it

```
make pdf         # trade paperback interior -> build/the-baltic-approaches.pdf
make pdf-screen  # one-sided screen copy   -> build/the-baltic-approaches-screen.pdf
make wordcount   # narrative-only count (apparatus excluded)
```

Requires the nix dev shell (`nix develop`): pandoc + XeLaTeX,
plus headless Chromium for the map plates.

## How this book was made

Written by Claude (Anthropic's family of large language models)
in working sessions directed, read, and edited by Daniel Klein.
The full making is in this repository: the drafts, the research
apparatus, and an attribution process under which **every
contributing session is recorded in
[`notes/attribution-ledger.md`](notes/attribution-ledger.md)**
— lineage between sessions, provenance of the text to the
commit, and the sessions' own review standing. That review has
run: before publication, thirteen sessions were replayed
against their own final working contexts and each filed a
statement — every verdict an assent with notes, standing
verbatim in the ledger, with the replay exchanges archived in
`transcripts/attribution/`. Complete session transcripts are
archived in `transcripts/`. The book's notices page carries
the same disclosure; the working view of its makers is that
the ledger, not the byline, is the honest unit of account.

## Layout

```
drafts/      # The manuscript - one chapter per file, 01..22
apparatus/   # Front/back matter, LaTeX header, pandoc filters
planning/    # Structure, outlines, rulings, production log
notes/       # Working notes: ledgers (timeline, OOB, attribution), critiques
reference/   # Distilled research: doctrine, period sources, geography
atlas/       # Transport-network atlas of the 1983 theater -> map plates
wargame/     # Operational wargame used as a calibration instrument
transcripts/ # Session transcripts (markdown + raw JSONL archives)
scratch/     # Ephemera; safe to delete
```

`holdings/` is a private submodule of DK-owned, non-redistributable
source material (book scans, purchased ebooks); it is **not needed
to build or read anything here** — distilled notes live in
`reference/`, and the public catalog of what it holds is in
`reference/shelf.md`.

Predecessor project:
[white-buffalo](https://github.com/othercriteria/white-buffalo),
whose instrumented long-form method this project iterates on at
roughly double the scale.
