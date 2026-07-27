# The Mission (1986) - Writing Project

**Status: pre-Phase-1, Step-0 complete.** Structure and process ported from
[white-buffalo](https://github.com/othercriteria/white-buffalo); the
Phase-1-pending sections below remain non-binding until Phase 1 runs.
**Successor sessions start at `planning/status.md`** (broad outline, open
decisions, standing unsettles); founding context in `planning/premise.md`
and `planning/provenance.md`.

## Project Structure

```
drafts/      # Chapter drafts - the actual manuscript
notes/       # Working notes: characters, scenes, research, worldbuilding
planning/    # Story structure, outlines, arc tracking, ledgers
reference/   # External sources: doctrine pubs, genre neighbors, style guides
scratch/     # Ephemera - safe to delete anytime
```

## Workflow

- Commit frequently. Small, meaningful commits. Be fearless about deleting
  material that no longer serves the work.
- **drafts/** contains canonical text. Number chapters for ordering:
  `01-chapter-name.md`
- **notes/** is for thinking. **scratch/** is throwaway.
- All prose in Markdown; one chapter per file.

## Length

Target 50–60k words — the deliberate increment over White Buffalo's ~31k.
The premise was chosen because its natural size is this target; if drafting
reveals otherwise, that is an Andon Cord conversation, not a silent drift.
The count is **narrative-only** (DK ruling 2026-07-23): apparatus — cast/OOB
tables, maps, bibliography, wargame-output annex — does not count against
the target, and carries reference/record only, never the didactic payload
(planning/size-and-shape.md §0).

## Ledgers (build in Phase 1, not as retrofit)

- timeline ledger (multi-axis: political, operational, protagonist)
- geography/map ledger
- order-of-battle ledger (formations, equipment, attrition state by chapter)
- continuity notes per Part

## Provenance (binding from Step 0, unlike the Phase-1-pending sections)

The attribution process (`planning/attribution.md`) exists *before* the
work, so its disciplines apply to every session from the first:

- **Every commit carries a `Session-Id:` trailer** with the session's
  full UUID (alongside the Co-Authored-By line).
- **After a compaction**, the successor's first act: append the boundary
  to the lineage log in `notes/attribution-ledger.md` and draft its
  predecessor's index row (marked summary-derived).
- **Rewinds and discarded branches get logged** in the lineage log by
  the surviving lineage when DK reports them.
- **Decisions live in text**, not thinking — conclusions and span
  accounting go into files or visible output in-session.
- **Sessions run archival themselves**: `make archive SKIP=<own-session-uuid>`
  at wrap (and opportunistically at start, to catch predecessors).
  Standing authorization from DK, 2026-07-20 — recurring hygiene must
  not depend on a human remembering a command (attribution.md,
  refinement 1, has the history).
- The ledger's Statements section is append-only, forever.

## Holdings (private companion repo)

This repo may become public; it must stay freely redistributable.
DK-owned materials that can't be (book scans, purchased ebooks) live
in the `holdings/` submodule → `the-baltic-approaches-private`,
**always-private**. Metadata stays public (reference/shelf.md
Holdings table + the holdings catalog). Never copy holdings content
into this repo, its build outputs, or transcripts — distilled notes
about the material belong in reference/*.md, the material itself
does not. `make hooks` installs the pre-commit guard that enforces
the file side of this.

## Process rules (presumed to apply to any model on this project)

Inherited from White Buffalo's model-author findings; a fresh critique profile
of the actual drafting model must be built early in drafting.

- **Self-review is not clearance.** Critique requires fresh context plus an
  assigned critical persona and a specific lens.
- **Evaluations are briefs, not verdicts.** Get the counter-brief before
  acting on a recommendation.
- **Alternatives must be forced.** Reopen decisions explicitly; ask for
  multiple options with tradeoffs.
- **Length/texture reports are unreliable.** Per-unit word floors; thinness
  is diagnosed by the human and named specifically.

## Instrument roster (to re-cast at revision time)

doctrine auditor · hardware/material auditor · veteran reader ·
Clancy-pastiche detector · "PowerPoint-in-prose" reader (didactic seams) ·
blind truncated readers · hostile + regression certification rounds

## Quality criteria (draft; revise in Phase 1)

- **Voice:** ensemble members distinct; no anachronistic concepts (nothing
  post-setting-year in characters' mouths or frames; the year is
  provisionally November 1983, pinned provisionally 2026-07-22 —
  planning/setting-time.md).
- **Didactic honesty:** each chapter's doctrinal payload earned in-scene, not
  briefed at the reader. The Goal's seminar unapologetically committed to its
  form — decide our register and hold it.
- **Consistency:** OOB, geography, timeline, attrition all internally
  coherent; characters don't know what they haven't learned.
- **Authenticity:** period-accurate hardware, staff procedure, radio
  discipline, and the texture of 1980s NATO service.
- **Restraint:** play it straight. No winking at the genre, no 2020s
  hindsight smuggled into the setting.
