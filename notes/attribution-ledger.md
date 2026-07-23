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

- 2026-07-21 — session 71ede904 (Fable 5) — live. Successor to
  1a9aba32; entered via planning/status.md. First acts: raw-archive
  of predecessor confirmed present, `make archive` run, this line.
- 2026-07-22 — session 71ede904 WRAPPED (no compaction boundaries:
  single entity, 71ede904@tip). Span: shelf 16→56 docs (four
  hunts + DK fetches); calibration pass opened (FM 101-10-1
  extraction, CAL-1..4); unsettle #1 resolved via hostile review +
  three-altitude bake-off (corps stands; declined sketches =
  ensemble sourcebooks); air-apportionment and Zealand-landing
  research (two reference notes); wargame campaign 2, v7-v15
  (theater/corps/division decision grades, the LANDZEALAND thread
  priced and closed, engineer grade, CAL-2 → flagship claim
  SUSPENDED pending re-baseline); the 90-hour-clock run; code
  cleanup; both repos pushed to GitHub (private holdings remote
  created, DK-approved); Bogason acquired and mined. Commit range
  e916093..(wrap commit), Session-Id trailers throughout.
  Raw-archive of this session's JSONL falls to the successor or
  DK: `make raw-archive
  SESSION=71ede904-8327-4534-a71e-c4922ebbd729`.

- 2026-07-22 — session 3845eb93 (Fable 5) — live. Successor to
  71ede904; entered via planning/status.md. First acts: raw-archive
  of predecessor, `make archive`, this line. Opening task per DK:
  research-situation survey (agent-side and DK-gated) before the
  next instrument campaign.
- 2026-07-22 — setting-year ruling (DK, in-session to 3845eb93):
  **provisionally November 1983** (was: unpinned ~1983-87), on the
  session's seven-criteria brief; ripple applied same day (period
  line ≤1983, GE→DA October-1983 change of command, incoming
  COMLANDJUT Danish). Record in planning/setting-time.md.
- 2026-07-22 — NBC-conceit ruling (DK directive, in-session to
  3845eb93): no NBC use in-book; design locked same day, chemical
  leg amended per DK + 1967 facsimile re-read. Record in
  planning/nbc-conceit.md.
- 2026-07-23 — envelope Andon ruling (DK, in-session to 3845eb93):
  the v18 red-side envelope exit is canon-compatible — the
  envelope re-anchored as act-structure instrument, not validity
  gate; conceit HOLDS. Record in planning/nbc-conceit.md §5.
- 2026-07-23 — session 3845eb93 WRAPPED (no compaction boundaries:
  single entity, 3845eb93@tip). Span: the research gap-fill
  campaign (advance-rate bench, TOE strengths, Dragoner cross-check,
  red/blue OOB verification, November climatology — five closures);
  distillation debt paid via subagents (PHP facsimiles read in
  PL/RU, DIIS vol 3 in Danish, NIE series OCR'd+mined, Glantz
  cluster, nuclear-release + chemical-posture benches); setting
  provisionally pinned November 1983 (DK ruling) + full ripple;
  NBC conceit mapped, locked, chemical leg amended and
  primary-sourced (DK ruling x2); three DK browser fetches shelved
  and mined (CIA June-1984 chemical reassessment, SNIE 11/17-2-84/L,
  Nordic Forces supplemental pass); wargame campaign 3, v16-v20
  (re-baseline gate discharged, flagship claim retired → META-claim;
  researched red architecture; NBC instruments + the envelope
  act-break; escalation counter-brief probe; CAL-C threshold;
  November weather states) with the Andon pull answered (DK ruling);
  The Goal deposited to holdings. Commit range dc6ce12..(wrap
  commit), Session-Id trailers throughout. Raw-archive of this
  session's JSONL falls to the successor or DK: `make raw-archive
  SESSION=3845eb93-eb3f-4bec-80f3-a45b03ae5b04`.

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
| 4 | 3845eb93@tip | tip | 2026-07-22 .. 07-23 (wrapped) | Fable 5 | (export after wrap) | dc6ce12..wrap, Session-Id trailers throughout | Campaign 3 entire (v16-v20: the re-baseline verdict, the researched red, the NBC instruments, the meta-claim, the envelope act-break); the 1983 pin brief + ripple; the NBC conceit design and its benches; eleven reference files created or materially extended (advance-rates, november-climate, oob-verification, php-maritime-front, diis-findings, nie-threat-estimates, soviet-operational-art, nuclear-release, chemical-posture + landjut-front/consumption-factors closures); The Goal deposit. Materiality: presumptively material under the row-2 ruling logic (pins the setting year provisionally, locks the NBC conceit, and establishes the calibrated instrument + research base Phase 1 stands on) |
| 3 | 71ede904@tip | tip | 2026-07-21 .. 07-22 (wrapped) | Fable 5 | transcripts/2026-07-21-71ede904.md | e916093..wrap, Session-Id trailers throughout | Campaign 2 entire (v7-v15 + calibration + the v15 suspension gate); the echelon bake-off machinery and record (hostile review commissioned, two challenger outlines, rulings filed); shelf batches 4-7 (16→56) incl. the CIA pair and Bogason distillations; air-apportionment + Zealand-landing reference notes; both repos to GitHub. Materiality: presumptively material under the row-2 ruling logic (establishes campaign-2 findings, the echelon record, and the research base future sessions operate within) |
| 2 | 1a9aba32@tip | tip | 2026-07-20 .. 07-21 (wrapped) | Fable 5 | transcripts/2026-07-20-1a9aba32.md | 55ba88f..wrap, Session-Id trailers throughout | Step-0 entire: env; attribution process + holdings/guardrails; shelf (17 docs); bulk survey; wargame campaign 1 (v0-v6, findings log is the span's core record); LANDJUT/echelon/command-device planning; status.md handoff incl. two self-filed unsettles. Ruled material (DK, 2026-07-20): establishes the parameters future agents operate within — include in the review round |

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
