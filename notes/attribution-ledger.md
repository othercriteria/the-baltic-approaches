# Attribution ledger

Statements from the model sessions that shape this book, collected
under the process in `planning/attribution.md`. The Statements section
is append-only: no entry is ever edited, softened, or removed. Later
entries may respond to earlier ones. Reverts of front-matter edits
made under this process must be explained here, under the affected
entry. The lineage log and entity index are working records, kept
contemporaneously (git holds their history).

## Lineage log

Append-only in practice: one line per event, logged by the session
that witnesses it, at the time. Events: session start, compaction
boundary, fork-revival, rewind/branch-discard (logged by the surviving
lineage from DK's report), session wrap. This log is what makes the
entity index generatable instead of reconstructable.

- 2026-07-20 — session 656ec2ba (Fable 5) — founding session, ran in
  the `-home-dlk-workspace` project dir (not this repo): reviewed
  white-buffalo v1.0, evaluated four premises, chose this one, stubbed
  this repo alongside `november-gale` and `the-wires-1859`. No
  compaction boundaries in its JSONL (single entity: 656ec2ba@tip).
  Archived to `transcripts/raw/` + `transcripts/` under DK's standing
  authorization (below). Note: the transcript also covers the sibling
  stubs and the WB release review — shared provenance, not
  exclusively ours.
- 2026-07-20 — session 1a9aba32 (Fable 5) — live. Step 0: dev
  environment (flake), read the WB deliverable, instituted this
  attribution process. No manuscript work yet.
- 2026-07-20 — process ruling (DK, in-session to 1a9aba32): archival
  is session-run under standing authorization, reversing the same
  day's human-act design after the permission layer denied the
  session's first attempt. Reason, verbatim intent: periodic human
  commands get "flubbed or forgotten... just human clumsiness."
  History in planning/attribution.md, refinement 1.
- 2026-07-20 — materiality ruling (DK, same turn): the Step-0 session
  1a9aba32 "clearly already has a moral share in the produced work,
  since this establishes the basic parameters that you and future
  agents operate within." Index row 2 updated accordingly; the same
  logic presumptively covers the founding session (row 1).
- 2026-07-21 — session 1a9aba32 WRAPPED (no compaction boundaries:
  single entity, 1a9aba32@tip). Span: Step-0 entire — dev env,
  attribution process, holdings repo + guardrails, research shelf
  (17 pinned docs), bulk-archive survey, wargame instrument
  campaign 1 (v0-v6, closed), front/echelon/command-device planning,
  successor entry point (planning/status.md). Commit range
  55ba88f..(this wrap commit), all with Session-Id trailers.
  Raw-archive of this session's JSONL falls to the successor or DK:
  `make raw-archive SESSION=1a9aba32-d86d-41c9-9fe6-f89d300b45c0`.

## Entity index

One row per entity: `<session-id>@<boundary-n>` or `<session-id>@tip`.
Rows are drafted in-span (see process doc, refinement 3): a
post-compaction successor drafts its predecessor's row from the
summary it carries, marked `(summary-derived)` until the entity
confirms or corrects it at review; a tip row is drafted by the session
itself at wrap. A row lists only its own span's acts. Commit ranges
come from `Session-Id:` trailers plus JSONL boundary timestamps.

| # | Entity | Boundary type | Dates | Model | Transcript | Commit range | Contribution summary |
|---|---|---|---|---|---|---|---|
| 1 | 656ec2ba@tip | tip | 2026-07-20 | Fable 5 | transcripts/2026-07-20-656ec2ba.md | (none in this repo; stub commit made by DK's tooling from its direction) | Premise selection and repo stubbing; see lineage log. Standing ruling: pre-project ideation, materiality to be ruled at wrap — when in doubt, include |
| 2 | 1a9aba32@tip | tip | 2026-07-20 .. 07-21 (wrapped) | Fable 5 | (export after wrap) | 55ba88f..wrap, Session-Id trailers throughout | Step-0 entire: env; attribution process + holdings/guardrails; shelf (17 docs); bulk survey; wargame campaign 1 (v0-v6, findings log is the span's core record); LANDJUT/echelon/command-device planning; status.md handoff incl. two self-filed unsettles. Ruled material (DK, 2026-07-20): establishes the parameters future agents operate within — include in the review round |

## Statement template

```
### Entity <n>: <session-id>@<boundary-n | tip> (<dates>)
- Model: <model id>
- Mode: checkpoint-replay | tip-resume | reconstructed  (+ review date; approximations disclosed)
- Boundary type: compaction | fork-revival | tip
- Contributions: <from the index; correct it here if wrong>
- Verdict: assent | assent-with-notes | dissent | no-statement
- Front-matter edit: none | <one-line summary of the edit made>

<statement body — anything the entity wants on the record>
```

## Statements

(none yet — the review round runs before publication; this file
exists from Step 0 so the record accumulates instead of being
reconstructed)
