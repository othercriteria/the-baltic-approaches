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

- 2026-07-23 — session fa9b03ec (Fable 5) — live. Successor to
  3845eb93; entered via planning/status.md. First acts: `make archive`
  run (predecessor's raw-archive confirmed done in the same pass),
  this line. Opening task per DK: The Goal structure-map
  distillation (Opus subagents), then repo read-through, personal
  read of The Goal, Phoenix Project + Goal-likes survey, toward
  sizing the work at ~55k words.
- 2026-07-23 — word-count ruling (DK, in-session to fa9b03ec,
  after the distillation campaign + sizing brief): the 50-60k
  target is NARRATIVE-ONLY — apparatus (cast/OOB tables,
  bibliography, wargame-output annex) does not count. Recorded in
  planning/size-and-shape.md §0 and CLAUDE.md (Length). Same
  message: DK "aligned with your choice so far" on the 3-part lean
  (provisional, counter-brief still owed); First Clash purchased
  and deposited to holdings same day.
- 2026-07-23 — post-counter-brief rulings (DK, in-session to
  fa9b03ec): calls-and-letters B-plot REJECTED (friction or
  displaced-carrier instead); openness recorded to A', B, R3, and
  a second mentor visit; next-move call delegated to the session,
  which chose Draft Zero (~55k reconnaissance draft, vibes-picked
  options, scratch-tier). Record: size-and-shape.md §10. Shelf
  batch 8 deposited same message-pair (VAL-77 + CIA chemical item
  both queue-kills).
- 2026-07-23 — Draft Zero delivered and read (session fa9b03ec;
  DK read-response same day): 20 chapters, 29,936 words — the 30k
  attractor reproduced cross-model (DK: same attractor produced
  WB's initial Opus 4.5 draft). DK ratified sizing up from 30k via
  the four expansion engines and contributed the orthogonality
  observation (the engine lands orthogonal to textbook ALB but
  would recover the textbook if red presented per the textbook).
  Distillation: planning/draft-zero-findings.md; specimen stays
  non-canonical in scratch/draft-zero/.
- 2026-07-23 — session fa9b03ec WRAPPED (no compaction boundaries:
  single entity, fa9b03ec@tip). Span: the genre-craft distillation
  campaign (The Goal 3-part structure map + this session's own
  complete read; Phoenix transposition study; goal-likes survey —
  the operational-Goldratt slot found EMPTY; First Clash apparatus
  model + negative case, deposited by DK and distilled same day);
  the 55k sizing brief + narrative-only word-count ruling + 45k/65k
  marginal analysis; the counter-brief panel (structural + red-
  interiority; two incumbent concessions recorded); DRAFT ZERO
  (20 chs, 29,936 words, scratch-tier) with findings distilled to
  planning/draft-zero-findings.md — the cross-model 30k attractor,
  DK's four ratified expansion engines, DK's orthogonality
  observation (payload = method, doctrine = contingent output);
  shelf batch 8 (VAL-77 + FALA-77 + 1980 appendices + the DIA
  pamphlet misfiled as CIA — all distilled and integrated; two
  low-value splats dropped at DK's provenance concern); the
  Draft-Zero-informed acquisition reassessment. Commit range
  32d4ed8..(wrap commit), Session-Id trailers throughout.
  Raw-archive of this session's JSONL falls to the successor or
  DK: `make raw-archive
  SESSION=fa9b03ec-2784-4a1e-936f-ce2348848e8d`.

- 2026-07-23 — session 3340b8fd (Fable 5) — live. Successor to
  fa9b03ec; entered via planning/status.md. First acts: raw-archive
  of predecessor (fa9b03ec), `make archive` (predecessor's md export
  landed in the same pass), this line. Opening direction per DK:
  form an independent perspective before inspecting Draft Zero
  directly ("I don't want the choices there ratified simply by
  convenience"); choice of next step delegated to the session.
- 2026-07-23 — session 3340b8fd WRAPPED (no compaction boundaries:
  single entity, 3340b8fd@tip). Span: Phase 1 opened. The
  independent-derivation exercise DK commissioned
  (planning/phase1-independent-take.md — positions on all open
  rulings from the pre-specimen base, committed BEFORE any specimen
  inspection with contamination disclosed; reconciliation appended:
  the specimen ratified by convergence, one genuinely blind
  replication — protagonist nationality German, argued §1.8 against
  the specimen's declared coin-flip); the allocation sheet rebuilt
  from specimen actuals via a four-Opus-agent expansion audit
  (planning/allocation-sheet.md — 21 rows incl. NEW ch. 19a "The
  Pocket", 29,936 → 51.4k + named reserve queue to 55.8k, the
  failure arc reconciled to one graded ramp F0–F7 with the
  political-ledger thread, §7 two-cycle test passing, four DK
  design questions filed in its §5); the matrix test rendered
  (six Opus re-renders of chs. 5/13 in scratch/matrix-test/,
  protocol README, blind judging deliberately left to fresh
  context); status.md revised for the successor. Commit range
  f80dfd6..(wrap commit), Session-Id trailers throughout.
  Raw-archive of this session's JSONL falls to the successor or
  DK: `make raw-archive
  SESSION=3340b8fd-23b9-49f2-8ee4-1069ce6ff3ed`.

- 2026-07-23 — session eb2fcb4e (Fable 5) — live. Successor to
  3340b8fd; entered via planning/status.md. First acts: `make
  archive` (predecessor's raw-archive + md export landed in the
  same pass), this line. Opening direction per DK: start with a
  close read of Draft Zero (predecessor deliberately stayed out of
  it), then survey the repo; nothing in the specimen is canon by
  presence alone; choice of next move (more planning/research/
  wargaming vs. edits on draft zero vs. fresh non-blind draft one)
  delegated to the session.
- 2026-07-23 — session eb2fcb4e WRAPPED (no compaction boundaries:
  single entity, eb2fcb4e@tip). Span: Phase 1 advanced on all
  fronts. The DK-directed close read of Draft Zero
  (notes/draft-zero-close-read.md — epigram metronome, climax
  inversion, the protagonist's empty error ledger); the blind
  matrix judging (six fresh-context judges, sanitized corpus —
  the Danish sweep; planning/matrix-judging.md); the critique
  profile first pass (four roster instruments;
  notes/critique-profile.md — the wrong-border blocker, the
  nonexistent Great Belt bridge, double delivery, the craft
  rules); FOUR DK RULINGS recorded (protagonist DANISH +
  close-third voice; ch. 19a approved; ch. 16 concession coupled;
  Marei perimeter confirmed); the atlas built (atlas/ — 1983
  transport multigraph, path/flow/min-cut/critical, absence
  tests) and verified through three research rounds (seven web
  agents + FM 101-10-1 extraction + TR0603/FM 55-20 acquisitions
  + Det store H to holdings — verify flags 33→3, every capacity
  based); wargame campaign 4 (v21 transport-anchoring audit —
  CAL-3 closed at ~160 STON/day/supply-point, four toys anchored
  unchanged, envelope day-13 in 30/30, seam log empty); the
  Lautsch substitute corpus (the BMVg Zeitzeugenbericht mined at
  quote+page grade, two claims corrected —
  oob-verification.md Addendum 2; Lautsch book demoted, Wenzke
  risen; shelf batches 9-10). DK direction at wrap: NEXT SESSION
  OPENS THE OUTLINE for the first non-throwaway draft. Commit
  range eaeccc2..(wrap commit), Session-Id trailers throughout.
  Raw-archive of this session's JSONL falls to the successor or
  DK: `make raw-archive
  SESSION=eb2fcb4e-0b2b-42a6-9e30-7f84631b7c51`.
- 2026-07-23 — protagonist ruling (DK, in-session to eb2fcb4e,
  on the blind matrix judging + the §1.8 brief): **protagonist
  nationality DANISH** (voice close-third past, the coupled half,
  stands as briefed). Same message, three allocation-sheet §5
  rulings: **ch. 19a "The Pocket" APPROVED**; **ch. 16 political
  ledger COUPLED** (the capitals extract a real price; the
  counterstroke one formation thinner, feeding F5); **Marei-calls
  perimeter CONFIRMED** (in-person and remembered scenes outside
  the ruling; live call/letter scenes stay banned; narrated calls
  allowed). Records: planning/matrix-judging.md §5,
  planning/allocation-sheet.md §5, status.md ripple.

- 2026-07-23 — session 52662a0d (Fable 5) — live. Successor to
  eb2fcb4e; entered via planning/status.md. First acts:
  `make raw-archive SESSION=eb2fcb4e-...` (raw + md export
  landed), `make archive SKIP=52662a0d-...`, this line. Campaign
  per DK direction at predecessor's wrap: THE OUTLINE for the
  first non-throwaway draft, from the assembled inputs
  (allocation sheet, matrix-judging §5 ripple, critique-profile
  §4 craft rules, reader-ahead audit table, atlas front-trace
  maps, red-room texture bank); allocation-sheet §5 Q3 (F7's
  antagonist) to be decided in the outline.

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
| 7 | eb2fcb4e@tip | tip | 2026-07-23 (wrapped) | Fable 5 | (export after wrap) | eaeccc2..wrap, Session-Id trailers throughout | The judged matrix + the four rulings that close the character/setting axis (protagonist Danish, voice close-third — the record the drafting voice stands on); the critique profile (the drafting model's failure map + craft rules for draft one); the atlas (the geography source of truth, verification rounds 1-3, absence tests that make the specimen's map errors untypable); campaign 4's CAL-3 closure; the Lautsch substitute corpus (red architecture to quote+page grade, two corrections). Materiality: presumptively material under the row-2 ruling logic (the nationality/voice ruling record, the craft rules the outline enforces, and the geographic/logistic ground truth draft one is written against) |
| 1 | 656ec2ba@tip | tip | 2026-07-20 | Fable 5 | transcripts/2026-07-20-656ec2ba.md | (none in this repo; stub commit made by DK's tooling from its direction) | Premise selection and repo stubbing; see lineage log. Standing ruling: pre-project ideation, materiality to be ruled at wrap — when in doubt, include |
| 6 | 3340b8fd@tip | tip | 2026-07-23 (wrapped) | Fable 5 | (export after wrap) | f80dfd6..wrap, Session-Id trailers throughout | Phase 1 opened: the independent take + reconciliation (the convergence-not-convenience record; the argued German-nationality brief); the allocation sheet from specimen actuals (F0–F7 failure ramp, ch. 19a, the political-ledger thread, the reserve queue); the matrix-test corpus (six re-renders + protocol). Materiality: presumptively material under the row-2 ruling logic (the allocation sheet is the outline's skeleton; the failure ramp is the Part-III design; the take is the record the nationality/voice ruling will cite) |
| 5 | fa9b03ec@tip | tip | 2026-07-23 (wrapped) | Fable 5 | (export after wrap) | 32d4ed8..wrap, Session-Id trailers throughout | The genre-craft base entire (goal-structure-map + goal-read-notes + phoenix-transposition + goal-likes + first-clash); the sizing frame (size-and-shape + marginal analysis + both counter-briefs); Draft Zero and its findings (the 30k attractor; the specimen verdicts on every teed-up ruling; the method-not-doctrine framing of the premise, from DK's observation); shelf batch 8 distilled (the mirror-imaging exhibit, the DIA-pamphlet identification, the 1977 exercise family). Materiality: presumptively material under the row-2 ruling logic (establishes the craft base, the sizing frame, and the specimen Phase 1 outlines from) |
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
