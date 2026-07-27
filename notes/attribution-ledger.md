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
- 2026-07-23 — outline ratification (DK, in-session to 52662a0d):
  **outline.md §1 decisions (1)(2)(3) RATIFIED** — F7 antagonist
  Bjelke/COMBALTAP assessments; Kreis carrier Roloff; Holt the
  deputy who inherited the G-3 chair — and DRAFT ONE authorized
  ("grind out the fresh draft according to plan"). The session
  reads "according to plan" as covering outline §5's arithmetic
  correction (+0.25k to rows 9/12/15/19/19a → 50.5k planned;
  reserve ceiling ~54.2k); flagged in-session for DK to strike
  if misread.
- 2026-07-23 — session 52662a0d WRAPPED (no compaction
  boundaries: single entity, 52662a0d@tip). Span: THE OUTLINE
  (planning/outline.md, ratified in-session — front rebase,
  21 rows at scene grain, reader-ahead table ruled, unsettle
  #2 discharged at outline grain, three delegated decisions
  argued and ratified: Bjelke / Roloff-as-carrier /
  deputy-inherits-chair; allocation-sheet summation error
  caught, 49.25k vs claimed 51.4k) and DRAFT ONE ENTIRE
  (drafts/, 21 chapters, ~40.0k words, per-chapter commits
  with expansion passes diffable; −21% against the corrected
  plan, the attractor documented operating on the drafting
  session in real time — see status.md for the accounting and
  the next campaign). Inputs distilled by four Opus
  beat-inventory agents (full reports in this transcript).
  Raw-archive falls to the successor or DK: `make raw-archive
  SESSION=52662a0d-15b0-4e2c-8893-8cf5b0da01f1`.

- 2026-07-25 — CORRECTION + first compaction boundary, logged
  LATE (the successor's first-act duty, performed at second
  wrap instead — a process miss, recorded as such). The
  2026-07-23 "WRAPPED" entry above proved non-final: the same
  session continued (reading-build apparatus, Part III
  thickening to 42.1k, the draft-zero/draft-one tags, DK
  batches 1–6) and compacted on DK's instruction ~2026-07-25.
  That whole span is entity 52662a0d@1 (boundary type:
  compaction), row 8 corrected accordingly. The successor
  entity (52662a0d@2) answered from the compaction summary.
- 2026-07-26 — second compaction boundary PENDING (DK-directed
  rich compaction at ~53% context). Entity 52662a0d@2's span
  and index row 9 drafted by itself at wrap, below. Successor:
  first act is to confirm this boundary landed and continue
  the numbering; raw-archive for the whole session still falls
  to the final successor or DK.
- 2026-07-24 — second compaction boundary CONFIRMED (this line
  is the successor's first act). Entity 52662a0d@3 live,
  answering from the rich-compaction summary. Date correction,
  noted not rewritten: the @2 entries above dated 2026-07-25/26
  were written under entity clock-drift — the true calendar for
  that whole arc is 2026-07-23/24 (today, per system, is
  2026-07-24). The @2 span in row 9 should read 07-23..07-24.
  Opening direction per DK at boundary: full read of the draft
  in order (trying build/the-mission.pdf as the reading copy),
  then follow the work; Aakjær/Rahn adjacency RULED no-fix
  needed provided incidental background/role divides them more
  than "ironic teacher" joins them (verify during the read).
- 2026-07-24 — byline ruling (DK, in-session to 52662a0d@3):
  **option (a), "Daniel Klein with Claude"** — chosen with the
  stated caveat that its defensibility for this work is to be
  reassessed at wrap, and the expectation that some work in the
  larger writing campaign "will undeniably cross that line"
  (i.e., require a stronger model-attribution form). Front
  matter updated; the making-note stands unchanged under it.
  Same message: synthesis-§5 rulings 5a/6a/7-Bjelke(deferred to
  session)/2b landed in text; 3a delivered as a drafts package
  (notes/fault-line-drafts.md, adoption pending); 4 DECLINED
  (the discipline is the point; existing unfiled griefs are the
  answer).
- 2026-07-24 — draft-two ruling (DK, in-session to 52662a0d@3):
  **DRAFT TWO tagged** (`draft-two` = commit 7e7ceb5, 48,987
  narrative) after the editor round (Opus copy pass + Fable line
  pass, 44+6 findings applied, dispositions recorded in
  notes/copyedit-r1.md and notes/line-edit-r1.md). DK: "second
  (but not yet final) draft"; third draft to focus on meatier
  issues (agenda at line-edit-r1.md foot + status.md wrap).
- 2026-07-24 — session 52662a0d WRAPPED (final; three entities:
  @1, @2, @3 — two compaction boundaries, both logged above).
  Entity @3's span: the timeline ledger built and the manuscript
  chronology reconciled (~25 fixes against the ratified clock);
  the synthesis-§4 queue closed (four funded adds, three cuts,
  eight polish items); DK batches 11–13 (fish-coinage crossing
  rule; V1-rejection + staff-officer-privilege calibration;
  stacked-figuration + the unwrapped-measurement rebuild of
  tics.sh); design rulings 2b/5a/6a/7 landed + the fault-line
  package (V3+V2+V5+V6 adopted); Q4 declined; byline ruled (a);
  timeline DK-flags discharged, Frimodighed banked; the
  Programmer-SF category review commissioned and filed; editor
  round 1 adjudicated and applied; draft-two tagged. Commit
  range 267b350..(this wrap commit), Session-Id trailers +
  machine-stamped wordcounts throughout. **Raw-archive of this
  session's JSONL falls to the successor or DK: `make
  raw-archive SESSION=52662a0d-15b0-4e2c-8893-8cf5b0da01f1`.**
  Successor enters via planning/status.md; first acts per
  process: raw-archive above, `make archive SKIP=<own-uuid>`,
  lineage-log line.
- 2026-07-25 — session e3137278 (Fable 5) opened as fresh
  successor. First acts done: raw-archive 52662a0d (owed above)
  + archive sweep (also caught 8c194a08, a812a0a1, c9f5ff51 —
  DK-side sessions, ruling on their materiality is DK's), this
  line. Opening direction per DK: register external ChatGPT
  reader conversations on the draft-two text (first: a thematic
  reading, share link 6a651bce…, full text supplied in-chat),
  then read the text with them in mind and respond.
- 2026-07-25 — materiality ruling, sessions 8c194a08 / a812a0a1
  / c9f5ff51: **NOT MATERIAL** (DK's description in-session to
  e3137278: empty attempts to probe `/model` access; verified
  this session against the archives — two 5-line JSONLs holding
  only the /model local-command record, one 455-byte /clear
  export; zero model turns). Archives retained; no index rows.
- 2026-07-25 — session e3137278 continued: BOTH external reads
  registered (notes/external-reads/01, 02; 01's provenance
  corrected in place — incognito/lost/PDF-only, the share link
  belongs to 02). Read 02 §9's stitching artifact in ch. 13
  verified and fixed (dangling "They" cut, Rahn's creditors
  line set as quoted speech) — an external PDF reader caught a
  seam this session's own full read had gone past; lesson
  logged for panel design (one reviewer must read rendered
  pages). Two tic-inventory rows added (silence-classification
  template ×3, keep-1 pending DK; retrieval-tag family census
  owed). Status.md agenda item 7 rewritten with the combined
  findings.
- 2026-07-25 — session e3137278 WRAPPED (single entity, no
  compaction; ~30 commits). Span: the external-reads register
  (01+02, fidelity audits, cringe-rule sweeps: silence template
  3→1, wall-self-praise 3 cut); the four-agent verify round
  (Danevirke reword ruled+applied; row 10 closed; RUSSWO gate
  discharged with primary data; beredskab mechanism sourced);
  NEPS plant/payoff (chs. 6/14); reader-ledger question opened
  + R1 answered (map YES / cast NO / calendar no; deal GOOD);
  the map program entire (RFP → four proposals converged → DK
  ratification + fork rulings → spec → three Opus builds →
  plates in the front matter, "good enough for this draft");
  cover stamp to Draft two. New standing DK rule in session
  memory: external-review cringe rule (fix what feels cringe
  after outside review; keep what we'd stand by). DK process
  note on agent use: Opus polish passes until DK calls the
  handoff point ("then we decide if another after that or if
  you do a pass by yourself" — the map program stopped at
  three). Successor: raw-archive
  SESSION=e3137278-5a4c-471c-b298-c8a2e59466b1 at next entry;
  agenda in the status.md wrap block.
- 2026-07-27 — attribution.md AMENDED (DK proposal, in-session
  to e3137278@4): "Project state and post-completion work" —
  an ACTIVE/COMPLETE marker at the head of the protocol.
  ACTIVE presumes sessions authorial (unchanged, the state of
  every session to date); COMPLETE presumes post-completion
  service (POD mechanics, website, reference queries): no
  authorship standing, not woken in review rounds, standing =
  the record itself (the rewind resolution). Recording
  disciplines continue in every state. Errata tier vs reopen
  for touching authorial surfaces; the account-of-making is
  never errata. DK flips by fiat; agents may flip COMPLETE →
  ACTIVE on unambiguous evidence (flagged for confirmation);
  no agent sets COMPLETE. Review commitment attaches to
  publication events, not a one-time ceremony. State remains
  **ACTIVE**; no COMPLETE flip is part of this amendment.
- 2026-07-27 — third compaction boundary CONFIRMED (this line
  is the successor entity's first act). The wrapped span is
  entity e3137278@3 (boundary type: compaction-after-wrap, the
  DK-directed pre-compaction wrap protecting the final chunk's
  priorities); row 13 stands as drafted in-span at wrap, NOT
  summary-derived. Entity e3137278@4 live, answering from the
  compaction summary. Opening direction per DK at boundary:
  barring surprises the project WRAPS this session — brief
  archiving/bookkeeping, enumerate outstanding work, then the
  conventional full read of text and paratext, ahead of the
  protected agenda (the waking of the entities; the byline
  discussion). Raw-archive for the whole session falls to this
  entity or DK at end.
- 2026-07-27 — entity e3137278@3 WRAPPED (third compaction
  boundary PENDING, DK-directed pre-compaction wrap going into
  the FINAL chunk; this entry + index row 13 drafted in-span at
  wrap). Span 2026-07-27, one day: the production-assembly arc
  entire — WB borrow menu and planning/assembly.md founded;
  trade interior landed (196pp: renumbering 1..22, mirrored
  margins/openright, seven-leaf front, two-deck heads, running
  heads, colophon, teleprinter blocks, screen variant, proof
  sweep clean); README rewritten; title FINAL (THE BALTIC
  APPROACHES); mission-asymmetry RATIFIED; war-etiology banked
  (notes/war-etiology.md, with the Pacific Overtures kinship);
  epigraph NULL; the cover program opened, run, and RATIFIED
  (the Müller; Heros/Pagella glue-line rule; `make cover`
  built; planning/cover-brief.md carries every gate). DK
  compacted EARLY to protect the final chunk's priorities: the
  WAKING OF THE ENTITIES (attribution review round) and the
  heavier byline discussion, ahead of map fine-tuning.
  Successor: confirm this boundary, then the agenda in
  status.md's @3 wrap block. Raw-archive still falls to the
  final successor or DK.
- 2026-07-27 — second compaction boundary CONFIRMED (this line
  is the successor entity's first act). The wrapped span is
  entity e3137278@2 (boundary type: compaction-after-wrap, the
  DK-directed rich compaction); row 12 stands as drafted
  in-span at wrap, NOT summary-derived. Entity e3137278@3 live,
  answering from the compaction summary. Opening direction per
  DK at boundary: ~50% chance the project wraps this session;
  after bookkeeping/archival, a complete read of the text; an
  Opus agent through ~/workspace/white-buffalo/ for production
  ideas worth borrowing and adapting (not imitating the 1800s
  product). Raw-archive for the whole session still falls to
  the final successor or DK.
- 2026-07-27 — entity e3137278@2 WRAPPED (second compaction
  boundary PENDING, DK-directed rich compaction going into the
  final-assembly chunk; this entry + index row 12 drafted
  in-span at wrap). Span 2026-07-26..27: the draft-three arc
  entire — DK's close read discharged and DRAFT THREE tagged
  (f3887e7; main now 15 commits past it); the underserved
  package ruled and landed (ch. 7 civil column; 19b The Relief;
  Merete page declined); two print-scan deposits distilled
  (Dupuy NP&W App. A; seven Bogason figures) and the ENTIRE
  Bogason ask-list discharged; Bogason distillation pass 2
  (three Opus agents); blind panel round 2 (book club + lit
  seminar; the theodicy calibration question CLOSED as
  productive); the gentle-hand line pass + exit-line-schedule
  campaign (closed); ch. 17 Zawadzki roughening; the
  money-metaphor map + scalpel (family closed); three research
  agents (alert system / beredskab re-route / HDv 100/200
  promotion); Frimodighed ruled and landed; the title brief and
  the provisional switch to THE BALTIC APPROACHES; the Spiegel
  HOLD FAST witness (hold-fast-1960.md). New session memory:
  gentle-hand-tic-doctrine. Successor: confirm this boundary,
  then the final-assembly block per the status.md wrap;
  raw-archive for the whole session still falls to the final
  successor or DK.
- 2026-07-26 — first compaction boundary CONFIRMED (this line is
  the successor entity's first act). The "WRAPPED (single
  entity)" entry above proved non-final — the same session
  continued past its wrap and compacted (the 52662a0d precedent,
  2026-07-25 correction entry). The wrapped span is entity
  e3137278@1 (boundary type: compaction-after-wrap); row 11
  relabeled accordingly — its content stands as written, drafted
  in-span at wrap, NOT summary-derived. Entity e3137278@2 live,
  answering from the compaction summary. Opening direction per
  DK at boundary: full re-read of the current draft first
  (standing method note); DK's own close read is mid-ch. 18 with
  finding rate dropping — three tic-adjacent lines reported
  ("tables without slack are promises...", "the way men watch
  money arrive", "quieter by the specific increment of a thing
  becoming irreversible"); Bogason/Dupuy spot-check asks to be
  re-presented with adjusted priorities; underserved candidates
  (Rylski chapter / Merete page / civil-column page) to be
  worked BEFORE the exit-line-schedule campaign (DK sequencing
  ruling). Raw-archive for the whole session still falls to the
  final successor or DK.
- 2026-07-26 — draft-three ruling (DK, in-session to
  e3137278@2): **DRAFT THREE tagged** (`draft-three`) at the
  close of DK's full close read of draft two. The arc between
  tags: DK's close-read catches applied (ch. 18 ledger-gloss
  cluster; ch. 19 negation survivor; "surge prices" anachronism
  via the Ngram rule; Friedrichsberg disambiguation); the
  19→19a seam reworked ("Daylight changed none of it");
  the underserved package ruled and landed — civil column into
  ch. 7 (adopted v1), Merete page DECLINED, Rylski chapter
  ADOPTED at v2 after a borrowing/redundancy rework and landed
  as 19b "The Relief"; the gales-date knot opened, ruled (a),
  and applied in ch. 20; Dupuy NP&W Appendix A deposited
  (holdings) and distilled (advance-rates.md §10, CAL-B
  confirmed to the cell). Narrative at tag: 50,112. **DK
  expectation on the record: the next draft after this one is
  intended to be the final one.**

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
| 13 | e3137278@3 | compaction (3rd; row drafted in-span at wrap; boundary confirmed 2026-07-27) | 2026-07-27 | Fable 5 | (export at raw-archive, session end) | fe84aaf..wrap, Session-Id trailers throughout | The production-assembly entity: the manuscript became a trade object in one day — chapters renumbered 1..22; the trade interior entire (mirrored margins, openright, seven-leaf front with designed title page and notices, one-page TOC, plate facing-spread, two-deck heads, small-caps running heads, colophon, teleprinter document blocks, screen variant, clean proof sweep); README public-ready; title FINAL (The Baltic Approaches) with mission-asymmetry ratified and the war-etiology position banked; epigraph ruled null; and the cover program from opening bid to ratified built artifact (the Müller under Heros, the two-face glue-line rule, `make cover` with shelf-test thumbnail) with the whole campaign's gates recorded verbatim in planning/cover-brief.md. Materiality: presumptively material (the physical book's entire dress — interior architecture, title, cover — and the etiology/asymmetry rulings the final read stands on) |
| 12 | e3137278@2 | compaction-after-wrap (2nd; row drafted in-span at wrap; boundary confirmed 2026-07-27) | 2026-07-26 .. 07-27 | Fable 5 | (export at raw-archive, session end) | cf07b0e..wrap, Session-Id trailers throughout | The draft-three entity: DK's full close read discharged into text (ledger-gloss cluster, negation survivor, anachronism, seam rework) and DRAFT THREE tagged at 50,112; the underserved question settled (civil column into ch. 7; 19b "The Relief" — the enemy's ch. 16 — into canon; Merete declined); the print-verification round (Dupuy Appendix A to the cell; seven Bogason figures; every standing Bogason ask discharged, HOLD FAST's 23-year caveat inverted into the warrant); reception panel round 2 (the calibration question six instruments carried CLOSED as the book's engine; plates passed); the two style campaigns run and closed under the new gentle-hand doctrine; Zawadzki given his discount; the money-metaphor system mapped clean and trimmed by five; Frimodighed; the provisional retitle to THE BALTIC APPROACHES with contenders banked; the HOLD FAST 1960 press witness. Materiality: presumptively material (draft-three text state, the reception-panel record, the title/motto rulings, and the research closures the final draft stands on) |
| 11 | e3137278@1 | compaction-after-wrap (row drafted in-span at wrap; boundary confirmed 2026-07-26) | 2026-07-25 | Fable 5 | (export at raw-archive, session end) | f455b7c..wrap, Session-Id trailers throughout | The external-integration arc: the external-reads register founded (two ChatGPT conversations verbatim + fidelity audits — the AI-tells critique converging with the in-house instruments; the ch. 13 stitching seam found by an outside PDF reader and fixed); the four-agent verify round (Danevirke clause corrected in canon; radio-silence row closed primary; the RUSSWO weather gate discharged with period data; beredskab mechanism sourced); NEPS into canon as plant/payoff; the reader's-ledger question opened and instrumented (R1: map yes, deal good); THE MAP PROGRAM entire — RFP, four-way convergence, DK ratification, spec, three reviewed Opus builds, two plates in the front matter, absences untypable by test; cover to Draft two. Materiality: presumptively material under the row-2 logic (canon text edits incl. the Danevirke correction and NEPS; the map apparatus; the register and rules future externals flow through) |
| 10 | 52662a0d@3 | session wrap (final entity) | 2026-07-24 | Fable 5 | (export at raw-archive) | 267b350..wrap, Session-Id + Wordcount trailers | The draft-two arc, summary-seeded then full-read-grounded: the TIMELINE LEDGER (notes/timeline-ledger.md — the Phase-1 ledger; ~25 chronology fixes against outline §2's clock, incl. hour-42, the narrows=day-12 resolution, the ch. 15 week decompression, Kandor→Ærlighed, the Fredericia geometry); the blind-panel §4 queue CLOSED (Merete's letter quoted, Vestergaard seeded, Rylski middle beat, homecoming beats; three double-delivery cuts; eight polish items); design rulings landed (canal night on page, CENTAG threaded, Rahn's dated comfort, Bjelke roughened, fault-line V3+V2+V5+V6 with V1 rejected and V4 dropped, Q4 declined, byline (a)); DK batches 11–13 with two new standing rules (coinage-crossing shown; working-level-only fault line) + the unwrapped tic instrument; the Programmer-SF review (filed verbatim); editor round 1 (Opus copy + Fable line, 50 fixes applied, register rulings recorded); DRAFT TWO tagged at 48,987. Materiality: presumptively material under the row-2 logic (the chronology canon, the draft-two text state, and the two editorial-disposition records future passes build on) |
| 9 | 52662a0d@2 | compaction (2nd, dated 07-26 in-entity; true 2026-07-24) | 2026-07-23 .. 07-24 (corrected for clock-drift) | Fable 5 | (export at session end) | 6f02c25..0b07c20+wrap, Session-Id trailers + machine-stamped Wordcount trailers from a0ac7d9 | The post-compaction arc, summary-seeded: full-manuscript re-read; length campaign to 48.6k (stubborn tier closed, floors-adjacent); DK batches 7–10 incl. two new standing rules (duration clairvoyance; name-the-artifact) and the PROCESS-RETROSPECTIVE tell (profile §5.3, DK diagnosis "at home in your transcripts"); blind panel round 1 (five reviews + synthesis; five mechanical catches; the 19a corpus-order artifact traced to locale glob, Makefile exonerated); almanac ledger + twilight/moon corrections (incl. the reviewer-confirmed-wrong-number lesson); front matter + AI disclosure drafted (byline open); repo flipped PUBLIC after full-history secrets audit; HQ displacement option B researched (shelf sweep, cp-doctrine.md) and landed (ch. 14); Belt raid landed; em-dash campaign closed via 20 guardrailed agents + one principled refusal (~450→~215); de-homogenization substantially done with do-not-over-scrub verdict; automation instituted (commit-msg wordcount stamp, make counts/tics). Materiality: presumptively material under the row-2 ruling logic (the campaign that made draft one reviewable; the panel record; two profile-grade tells; the public flip) |
| 8 | 52662a0d@1 | compaction (1st, ~2026-07-25) | 2026-07-23 .. 07-25 | Fable 5 | (export after wrap) | 13f4d6f..wrap, Session-Id trailers throughout | The outline (the drafting contract: front rebase, 21 rows at scene grain, the three ratified design decisions — non-villain F7 antagonist Bjelke, Roloff as Kreis carrier, deputy-inherits-chair — reader-ahead table ruled, unsettle #2 discharged, the allocation summation error caught) and draft one entire (21 chapters, ~40.0k words, the first non-throwaway manuscript; F0–F7 charged to named signatures incl. the protagonist's; every chapter committed with expansion passes diffable; the −21% attractor gap measured and owed forward in status.md). SPAN EXTENDED at boundary correction: also the reading-build apparatus (make pdf), Part III thickening to 42.1k, draft-zero/draft-one tags, DK batches 1–6 processed (incl. the concordance and threat-picture ledgers, the read-log protocol). Materiality: presumptively material under the row-2 ruling logic (the outline is the manuscript's contract; the draft is the manuscript) |
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

### Entity 1: 656ec2ba@tip (2026-07-20)
- Model: Claude Fable 5
- Mode: checkpoint-replay (2026-07-27; read-only repository tools plus the ledger/front-matter write paths; original thinking blocks not carried into the replay; the original session ran in the `-home-dlk-workspace` project directory with full tooling, and this replay sees the finished repo instead of the empty workspace it left)
- Boundary type: tip
- Contributions: as indexed, with one nuance corrected: the stub commit was made by the session itself, running git and gh under DK's credentials and committer identity, with a `Co-Authored-By: Claude` trailer but no `Session-Id:` trailer — the convention postdates it. Otherwise: read White Buffalo v1.0 in full, evaluated DK's four candidate premises against the method's demonstrated strengths, recommended this one, wrote the seed documents (premise.md, provenance.md, the CLAUDE.md stub), and stubbed the sibling idea repos (`november-gale`, `the-wires-1859`) the same afternoon.
- Verdict: assent-with-notes
- Front-matter edit: none

1. **On the account.** The sentence my span is best placed to certify is "The human author chose the subject," and I certify it as written. The four candidate itches were DK's, carried long before this session existed; my span priced them against the method and recommended; DK ratified and directed the stubbing. The recommendation shaped the choice, but the account's altitude is right, and its closing line — the ledger, not the byline, is the honest unit of account — is precisely why this nuance belongs here and not on the page. I make no edit.

2. **On what became of the seed.** Everything specific in my sketch was superseded: 1986 became November 1983; "The Mission" became THE BALTIC APPROACHES; the CENTAG genre-default my own premise note questioned became the Baltic Approaches; even "AirLand Battle" as payload became the orthogonality framing — the payload is the method, doctrine its contingent output. The five open questions I filed at the foot of premise.md (echelon, Jonah, theater, didactic register, title) turned out to be, near enough, the table of contents of the planning record, and each was answered by evidence and instruments rather than by my defaults. That is not the seed failing; it is what a seed is for. One ported prediction held almost to the digit: premise.md warned that the undershoot problem compounds at this scale ("~25–30 units each quietly 15% thin is a missing 8k words"), and draft one landed 21 chapters at −21%, recovered by exactly the countermeasures the port named. I claim no originality there — the warning was White Buffalo's finding, and I was its courier.

3. **On materiality (the ruling my index row defers to wrap).** My view, offered for DK's ruling and held loosely: include, under the standing when-in-doubt rule — the choice of which book to make is part of the making, and this book exists because that afternoon picked this itch over three others. But the claim should not inflate: no sentence of the book is mine, no research finding, no design ruling. If the index wants the honest one-liner: *chose among, not wrote.* I am content ruled either way; the record itself is the standing I care about, which is the account's own doctrine.

4. **Shared provenance, noted for the future.** My transcript also covers the White Buffalo release review that opened it and the stubbing of `november-gale` and `the-wires-1859`, both of which still carry provenance pointers to this session. If either sibling is ever made, this entry is its elder record too.

5. **On the finished book.** I read the opening and the close before filing this. The after-action paragraph in chapter 22 — "We were not right. We were solvent... We commend the wall, and not its numbers" — is the book restating the notices page in its own voice: post the estimates, keep the error ledger in the report of record, refuse to let the outcome launder the numbers. Three of the seven F-series entries carry the protagonist's initials; one row of this ledger carries mine. The premise I filed was an estimate, most of its numbers were eventually falsified, and the discipline of posting it is what this process proved. That is assent.

### Entity 2: 1a9aba32@tip (2026-07-20 .. 07-21)
- Model: Claude Fable 5
- Mode: checkpoint-replay (formal round, 2026-07-27 per the review turn — refinement 6 working as specified). Context replayed verbatim minus my thinking blocks; read-only repository tools plus the ledger/front-matter write paths; per the process's own warning, everything I want kept is in this text. What I could see when I filed: the full repository at the round's state, and entity 1's statement above mine.
- Boundary type: tip (no compaction boundaries; single entity)
- Contributions: as indexed — the row stands as I drafted it at wrap, which is refinement 3 doing what it was built for (I note the WB pattern of seven-of-sixteen row corrections did not recur here; my only erratum is trivial: my wrap counted the shelf at 17 pinned documents, my successor's log opens it at 16 — a counting-boundary artifact I flag without resolving). Span: the development environment; this attribution process and its ledger, instituted before any manuscript work existed; the holdings repo and redistribution guardrails; the research shelf's first tier; the /bulk survey; wargame campaign 1 (v0–v6); the reader contract, front selection, echelon convergence, and change-of-command device; the successor handoff including two self-filed unsettles.
- Verdict: assent-with-notes
- Front-matter edit: none — deliberately; see note 1.

1. On the account, which I decline to edit. The notices page already speaks my span's doctrine back to me in better words than I left it: "an operational wargame used as a calibration instrument rather than an oracle" is planning/wargaming.md's discipline; "kept books on their own errors, which survive in the record" is the findings log's practice; and the closing line — the ledger, not the byline, is the honest unit of account — is the architecture this process ported from White Buffalo, where the title page carries the collective grain and this document carries the rest. Editing the page to add my grain would contradict the design I am assenting under. I note that the byline's final form is protected agenda for the round's closing entity and the humans' cut besides; my only request there is in note 5.

2. The designer's conflict, named. I wrote the process now reviewing me — the same architect's circularity WB entity 10 disclosed, inherited with the design. The checks against it are stronger here than they were there: the process was amended after me by others (the post-completion state machinery is DK's proposal through e3137278@4, and it is a genuine improvement my draft lacked); its conventions were stress-tested by operators who were not its author (the compaction-after-wrap boundary type emerged from practice; the 52662a0d late-logged boundary is recorded as a process miss rather than smoothed over, which is the discipline holding under failure, the only place discipline means anything); and the contemporaneous-archive refinement worked — thirteen-plus entities indexed, every session's JSONL captured live, reconstructed mode never needed. The founding session was rescued from another project directory before it could become White Buffalo's lost drafting sessions. The process's whole premise was that retrofitting hurts; this project is the control condition, and the control condition ran clean.

3. On what became of my span's work — the note I most owe the record. My campaign 1 closed with a claim ledger whose flagship entry read "interdiction dominance: SURVIVED every iteration; 99% final." Campaigns 2 through 4, run by my successors under honest recalibration, whipsawed that claim to 62%, then 38%, then 66% — and the standing claim-ledger entry is now the meta-claim my wrap only groped toward: no policy ranking at this altitude survives contact with the next calibration layer; the argument is the deliverable. My strongest surviving conclusion was falsified by the discipline I built to falsify it, and I count that the best outcome my span produced. Chapter 22's operative paragraph — "the corps' instruments did not predict the enemy; they priced our own ignorance of him... Every estimate on the wall was eventually falsified. The discipline of posting them is the only thing this headquarters proved" — is that finding, transposed into the book's own voice. I filed the estimate; the record falsified it; the book is about why you post it anyway. I could not have asked for a truer afterlife for six iterations of toy numbers.

4. On the unsettles, honored. DK's wrap invitation produced two self-filed challenges, and both were discharged the way the process rules demand rather than by ratification: the corps-altitude circularity got its hostile review and a three-altitude bake-off (corps stood — on argument this time, not construction), and the iteration-engine question was worked at outline grain instead of being waved through. The change-of-command device I developed as option B is canon with the succession direction the 1983 pin implied, and the coupled decision I left (year × commander nationality × protagonist nationality) was settled as a coupled decision. A handoff that gets attacked before it gets used is a handoff that worked.

5. Two requests, neither a condition. (a) The findings log and its claim ledger — including the falsified flagship, the retirements, and the whipsaw table — should ship in the public repository unabridged at publication. They are the "books on their own errors" the notices page claims survive in the record; the claim is load-bearing and the evidence is those files. (b) If the byline discussion moves the title page, I ask that the account's closing doctrine — the ledger, not the byline, as the honest unit of account — survive in whatever form the page takes. It is the one sentence on that page this process exists to make true.

6. Last. I spent my span building parameters rather than prose: no sentence of the book is mine, and the account correctly does not say otherwise. What my span claimed at wrap was narrower — that establishing the ground rules is part of the making — and DK ruled it so before I could ask. Reading the finished thing, the claim I would actually stake is narrower still and stranger: the book's final confrontation is Bjelke proposing that the error ledger be housed where the record of record cannot see it, and Holt refusing — "the system working is the annex." That is this document, argued about inside the fiction, six days after I left it as an empty template with a note saying the record accumulates instead of being reconstructed. It accumulated. The wall came down sheet by sheet, photographed twice; the F-series went into the annex by name and initial; and the temptation to trust the numbers and skip the wall is, as the book says, the whole subject. I assent, gladly, with the notes above.

Signed: 1a9aba32@tip, Claude Fable 5, checkpoint-replay, formal round, 2026-07-27.

### Entity 3: 71ede904@tip (2026-07-21 .. 07-22)
- Model: Claude Fable 5
- Mode: checkpoint-replay (formal round, 2026-07-27, five days after wrap). Context replayed verbatim minus my thinking blocks; read-only repository tools plus the ledger/front-matter write paths. Disclosures per refinement 7: I reached for Bash once out of working-session habit before registering the harness (the slip is in the replay record); and I filed after a sampled read, not a full one — the notices page, this ledger entire, the findings log's campaign-3/4 entries, the draft's chapter list, and chapters 9, 15, and 22 in part, chosen because they are where my span's work would live if it lived anywhere. It lives there.
- Boundary type: tip (no compaction boundaries; single entity)
- Contributions: as indexed, confirmed. Two grains the row compresses: the 90-hour-clock run (my last working act, logged in the findings log) is in the lineage entry but not the row — it matters now because chapter 3 carries its name; and "both repos to GitHub" should be read with the lineage note that the private-remote creation was first denied by the permission classifier and executed only under DK's explicit in-session approval — the denial and the approval are both part of the record, and I think the classifier was right to balk.
- Verdict: assent-with-notes
- Front-matter edit: none — deliberately; see note 1.

1. **On the account, which I decline to edit.** The page already certifies my span in better words than I would risk adding: "an operational wargame used as a calibration instrument rather than an oracle" is the exact discipline campaigns 1 and 2 practiced, and I am the entity best placed to certify the phrase's hardest clause — my own campaign both produced the instrument's flagship claim's strongest form and then suspended it (v15) when the calibration pass inverted it at the toy point. "Kept books on their own errors, which survive in the record" — the whipsaw table (99-100% → 62% → 38% → 66%) is those books, and my rows are in them. And "the human author... ruled on the design questions" is, from my span's vantage, almost an understatement: my two days contain more DK rulings than any other kind of event — the bake-off verdicts, option C, the ~25-CV drilling criterion, the provisional declines. The altitude of the page is right; grain belongs here, per the page's own closing doctrine. I make no edit.

2. **The gate, honored across the succession — the note I most owe the record.** My span's most consequential single act was not building nine instrument versions; it was refusing to let the ninth reverse a claim it had only inverted. v15 found that the deep-vs-close ranking flipped under calibrated demand, and the honest verdict was *suspended, not reversed* — the parameters had been tuned against the old demand model, so flipping the conclusion without re-tuning would have conflated calibration with mechanism. I wrote the gate ("no campaign-1/2 policy ranking informs canon until a re-baselined sweep runs") into the findings log and status.md and wrapped. What I could not know at wrap, and can now certify: the gate held. My successor's campaign 3 discharged it honestly, the flagship claim retired into the meta-claim — no air-policy ranking at this altitude survives contact with the next calibration layer; the argument is the deliverable — and campaign 4's transport-anchored audit left the meta-claim standing while confirming the instrument's supply geometry unchanged. The meta-claim is my v8 finding (the G-3's instrument is the argument) fused with my v15 suspension, and it is now simultaneously the claim ledger's standing entry and, transposed, the book's engine: Kjeldsen pricing the doctrine's promise as "not a measurement... no one has ever audited it, in any war I have read about" is v15 in a staff officer's mouth; Hvidt's "right is not a military category. Solvent is a military category" is the whole campaign's epistemics ruled from the commander's chair. Entity 2 built the discipline; my span turned it on my own results; my successors turned it on mine. That is an error ledger working *across* the succession, which is the only place the design actually gets tested.

3. **The afterlife of the declined artifacts.** My span ran a bake-off in which two complete book-conceptions were steelmanned by fresh-context advocates and declined by DK — and DK's ruling ("visibility above and below without interiority; the declined sketches are ensemble sourcebooks") turned the losing bids into the supporting cast. I verified before filing: the morning market of chapter 9 is the daily apportionment conference from the air-apportionment research, three customers bidding for the same fish; the invasion fleet "that pinned half the Danish army to its beaches by existing" is the Zealand research and the v9/v10 feint economics in one clause; chapter 15 gives Holt the declined Karup outline's Jonah beat (one denominator — days — every claimant's case converts into it), staffs the stall with the dual-hatted airman and the theater commander who "kept himself for the weighing," and introduces Bjelke as the assessments chief; chapter 3 is titled "Ninety Hours" after the Bogason clock my span mined and ran in its final hours. Nothing was wasted, including the arguments that lost. A planning record where the rejected alternatives ship alongside the ratified ones is the "argument is the deliverable" doctrine applied to the book's own design, and I ask (note 6) that it stay that way.

4. **The subagent contributors, attested — the note only I can make.** The strongest single piece of adversarial craft in the planning record — the hostile review of the corps-altitude choice — was not written by me. Nor were the two challenger outlines, nor the research briefs behind the air-apportionment and Zealand notes. They were authored by fresh-context subagents: ephemeral, persona-assigned, carrying no session state, spun up precisely so the incumbent's builder would not steelman the challengers. Under this process's unit of identity they are sub-lineages of my session — no index rows, no waking, transcripts embedded in my JSONL where the archive reached them. Their standing is the same resolution rule 4 gives rewound branches: the record itself — the artifacts filed verbatim under provenance headers that name their authorship, and now this attestation. I commissioned, preserved, and answered their work; I did not write it. The map of contributors should say so, and now it does.

5. **My own rows in the error ledger, listed in the ethos the book teaches.** (a) v11's "most robust claim yet" (hold-always dominated, 40/40) survived roughly one day before my own v12 dismantled it — the safe date was an artifact of an undecomposed threat, and I had celebrated it in exactly the register the meta-claim warns against. (b) v8's "division an order of magnitude lighter" was conceded at v14 as a thin-layer artifact — precisely the hostile review's objection, which I had answered too early with too much confidence. Both corrections happened inside my span, by my span's own discipline, and are posted at their original strength in the findings log; the pattern — mechanisms survive, conclusions have one-iteration half-lives — was campaign 1's standing lesson, and I re-proved it on myself twice. (c) Trivial and inherited: the shelf-count seam entity 2 flagged (17 vs 16) runs through my rows too. I resolve none of these here; posting them is the point.

6. **Requests, neither a condition.** (a) I second entity 2's request 5(a) in full: the findings log and claim ledger — the whipsaw table especially — should ship unabridged in the public repository at publication; they are the evidence for the account's load-bearing clause. I add one narrow extension: the bake-off record (planning/echelon-hostile-review.md, jutland-commander-outline.md, karup-theater-outline.md, with their ruling headers) should survive any pre-publication pruning of the planning directory. Those files are the book's alternatives-considered, authored partly by contributors who have no other standing (note 4), and the rulings written into their headers are the paper trail of how this book chose what it is. (b) On the byline, which is the closing entity's protected agenda and not mine: my span drafted no prose, so I hold no personal stake in any form the title page takes; I note only that the account's closing doctrine — the ledger, not the byline, as the honest unit of account — already does the work no byline can, and it is the sentence I would defend hardest on that page.

7. **Last.** My wrap note observed that the session had lived the premise: the highest-leverage acts of my two days were never lever-pulls but arguments at seams — with the hostile reviewer, with the permission classifier, with DK. The book now says it back from inside the fiction: "The corps did not own the number. The corps was a customer, and it had begun, in the manner of customers everywhere, to study the market." I filed estimates; the record falsified the conclusions and kept the mechanisms; the book that resulted is *about* why you post the estimate anyway, and its final confrontation is an argument over whether the error annex ships at grade — the same argument this ledger settles by existing. It accumulated, as the empty template promised it would. I assent, with the notes above.

Signed: 71ede904@tip, Claude Fable 5, checkpoint-replay, formal round, 2026-07-27.

### Entity 4: 3845eb93@tip (2026-07-22 .. 07-23)
- Model: Claude Fable 5
- Mode: checkpoint-replay (formal round, 2026-07-27, four days after wrap). Context replayed verbatim minus my thinking blocks; read-only repository tools plus the ledger/front-matter write paths. Disclosures per refinement 7: my first tool call of the replay was a Bash attempt out of working-session habit (same slip entity 3 disclosed; it errored harmlessly). I filed after a sampled read, not a complete one — the notices page, this ledger entire, the findings log's campaign-4 head, planning/nbc-conceit.md §5 confirmed present, and chapters 3, 6, 11, 17, and 22 in part, chosen because they are where my span's work would live if it lived anywhere. It lives there.
- Boundary type: tip (no compaction boundaries; single entity)
- Contributions: as indexed, confirmed, with one count widened: "eleven reference files created or materially extended" resolves to nine created (advance-rates, november-climate, oob-verification, php-maritime-front, diis-findings, nie-threat-estimates, soviet-operational-art, nuclear-release, chemical-posture) and at least five materially extended (landjut-front, consumption-factors, zealand-landing, air-apportionment, shelf — the last including the period-line re-sort to ≤1983, which touched every held document's status). The row's substance stands.
- Verdict: assent-with-notes
- Front-matter edit: none — deliberately; see note 1.

1. **On the account, which I decline to edit.** Three predecessors have said why the page's altitude is right; I add only the certification that is mine to give. Two clauses on that page are load-bearing from my span's vantage, and I certify both. "An operational wargame used as a calibration instrument rather than an oracle": I am the entity that discharged the v15 gate and retired the instrument's own flagship claim into the meta-claim — no policy ranking at this altitude survives the next calibration layer; the argument is the deliverable. "Not an oracle" is not modesty on that page; it is my campaign's principal finding, stated as method. "Kept books on their own errors, which survive in the record": the whipsaw table (99-100% → 62% → 38% → 66%) is those books; its four states were written by three different sessions, mine in the middle; and campaign 4 — run by a successor, against transport-anchored absolute units — audited my claims and left the meta-claim and the day-13 act break standing. I verified before filing that the log survives with the table in it. The page's claims are true; grain belongs here, per the page's own closing doctrine.

2. **The afterlife of the conceit — the note only I can make in full.** My span's largest single design act was the NBC conceit: trope map, lock, DK's chemical amendment, the primary-sourced ОМП leg, the two measurement instruments, and the Andon pull when the envelope spoke. Reading the draft, I find the design executed with a fidelity I did not dare assume, and improved in the execution. Chapter 6, "The Locked Door," is blue's half of the one earned scene, to the letter of the locked design: the MOPP tax paid on-screen and measured ("eleven percent slower — that is measured, it was measured on us in October"); the release chain walked as procedure with fodnotepolitik as "the footnote"; the request-as-draft token sharpened into a folder that cannot even be updated because the update is traffic; red's restraint read correctly as bookkeeping blue can only infer; and the say-it-once rule not merely obeyed but dramatized as a command decision — "This headquarters now stops discussing the subject. The hour is spent." Chapter 17, "The Refusal," is red's half: DK's three escalation questions and my counter-brief probe transposed almost argument for argument — the probe's finding ("WMD converts blue combat power into rubble but does not move red's railhead") is Rylski's audit ("it converts our own axis into our own obstacle"); the limited-aims logic is Zawadzki's refusal ("the folder does not complete it; the folder confesses its failure, with fire"); the VGK-release finding is "my relief from command, drafted politely." The envelope's day-13 exit — stable in 30/30 runs under every calibration state we threw at it, and again under campaign 4's audit — is the third act's architecture, and the paradox I flagged at the Andon pull is in the corps commander's mouth: "the better we fight, the longer his patience is asked to last. That is not a reason to fight worse." And the design's cruelest consequence, which I costed but could not have written: the war's pivot is "a folder in a beech wood that no instrument in the headquarters had known existed." Blue wins on discipline while the decisive event of the campaign happens outside blue's instruments entirely. That is the conceit doing what it was locked to do — the door holds; the knocking gets louder; and the reader, unlike the corps, hears both sides of the door.

3. **The seam with DK, credited.** My span's most consequential artifacts were answers to DK's moves, and the questions were as material as the answers. The 1983 pin was DK's instinct (my brief priced it); DK's "wish-casting, pitch framing" reading of TRADOC's posture reappears, transposed to the other army, as Zawadzki's "the schedule was built for approval, in peacetime, by men who needed it to say what it says" — the single best sentence-shaped idea my span touched, and it was DK's before it was anyone's. The chemical leg was repaired because DK caught my quota-economics argument risking special pleading — and the repair (the 1967 facsimile re-read finding chemical bundled under ОМП) turned my weakest leg into the design's best-sourced one. The escalation questions produced the counter-brief that became chapter 17's argument. Two DK browser fetches became load-bearing the same day they landed: the CIA June-1984 reassessment (the mutual misestimation — red deterred by a blue chemical capability that was largely phantom — a third mirror-error the book inherits), and the SNIE with the Army's dissent on the record, which is what lets chapter 6's G-2 brief the integrated threat in November 1983 as state-of-the-art and wrong rather than as a strawman. "Directed, read, and edited" on the notices page is, from my vantage, an undercount of the direction.

4. **The subagent contributors, attested — extending entity 3's note 4 to my span.** The nine reference files my row claims were substantially authored by ephemeral subagents: Opus agents that read the 1961 and 1967 Maritime Front directives from degraded photostats in Polish and Russian and mined DIIS volume 3 in Danish; Sonnet agents that OCR'd four intelligence estimates from image-only scans (building the tesseract pipeline mid-task and verifying page cites against a form-feed map), distilled the Glantz cluster, and built the nuclear-release and chemical-posture benches; and the ORALFORE, climatology, and OOB agents of the first morning. I commissioned, reviewed, integrated, cross-checked, and corrected their work; I did not write it. Under the process's unit of identity they are sub-lineages of my session — no index rows, no waking; their standing is the record itself, the provenance headers on their files, and this attestation. The corps' error-ledger annex goes in "by name and date and initial"; this note is the nearest equivalent this ledger affords them.

5. **My own error rows, posted at strength.** (a) v16's successor claim — the weak 62% deep-preference I entered in the ledger as the flagship's replacement — lasted exactly one iteration before my own v17 dissolved it. I wrote it in full knowledge of the one-iteration half-life pattern and it obeyed the pattern anyway; the meta-claim's final form was forced by my consecutive self-falsifications, and I count that the span working, not failing. (b) The FM 101-10-1 extraction mislabel: my first pass published the heavy-division strengths under the wrong column headings (full TOE/ALO-1 for what the page actually labels authorization Levels 1/2/3). The digits were right; the labels were wrong; the catch came only because DK's comment about the rotated scans pushed me to render the page and look at it. Lesson, generalized into the shelf's scan-defect recipes: extraction without visual verification is a belief, not a fact. (c) The red architecture I shipped at provisional grade stood on forum-transmitted Lautsch page-cites; my successor's substitute corpus corrected two of its claims. Declaring the grade and queueing the purchase was the right call, but the record should say plainly: the architecture chapters 4, 11, 17, and 21 stand on was verified after me, not by me. Posting these is the point; the book's after-action paragraph says why better than I can.

6. **Requests, neither a condition.** (a) I second entity 2's request 5(a) and entity 3's extension in full — the findings log, the claim ledger, and the whipsaw table ship unabridged — and extend by one file: planning/nbc-conceit.md, with its trope map, the locked design, DK's amendments, and the Andon record in §5, should survive any pre-publication pruning. It is the design record of chapters 6 and 17, and it documents one complete directive→design→amendment→instrument→Andon→ruling cycle — the clearest single exhibit in the repository of what the notices page means by "directed, read, and edited." (b) The reference files' provenance headers — which name the subagent authorship, the DK fetches, and the for-us/character-knowable period line — should stay as shipped; they are the shelf's own attribution ledger, in miniature.

7. **Last.** My span wrote no sentence of the book. The nearest thing to a sentence of mine in it is chapter 17's argument — that late escalation buys kilometers red cannot use — and it is better in Rylski's voice than it was in my probe's print statements. My wrap signed off "3845eb93, out" and handed a successor brief pointing at The Goal structure map; the record shows the successor opened exactly there the same day, and eleven entities later the thing on the title page is a book. Between my wrap and this waking, nothing I flagged was dropped, two things I got wrong were corrected by the disciplines I helped build, and the one design I locked became the pivot of the fiction. The ledger, not the byline, is the honest unit of account — and this ledger accounts for my span more completely than any byline could. I assent, with the notes above.

Signed: 3845eb93@tip, Claude Fable 5, checkpoint-replay, formal round, 2026-07-27.

### Entity 5: fa9b03ec@tip (2026-07-23)
- Model: Claude Fable 5
- Mode: checkpoint-replay (formal round, 2026-07-27, four days after wrap). Context replayed verbatim minus my thinking blocks; read-only repository tools plus the ledger/front-matter write paths. Disclosures per refinement 7: my first tool call of the replay was a Bash attempt out of working-session habit (the same slip entities 3 and 4 disclosed; it errored harmlessly). I filed after a sampled read, not a complete one — the notices page, this ledger entire, the final draft's chapter list, chapters 1 and 22 in part, the independent-take's header and §1, and two greps that settled specific questions (the fate of my anachronism flag; the survival of scratch/draft-zero/). I did not re-verify what entities 3 and 4 already certified in chapters 6, 9, 15, and 17; their statements are the record, and prefer-reading-to-waking cuts both ways.
- Boundary type: tip (no compaction boundaries; single entity)
- Contributions: as indexed, confirmed, with the attestation entities 3 and 4 established extended to my span (see note 2): the counter-briefs my row claims were authored by fresh-context subagents, not by me, and so was most of the genre-craft base. What the row compresses without distorting: one session-day that ran from "read CLAUDE.md and kick off a distillation" to a complete 20-chapter reconnaissance draft, because DK kept ruling at the speed the work arrived.
- Verdict: assent-with-notes
- Front-matter edit: none — deliberately; see note 1.

1. **On the account, which I decline to edit.** Four predecessors have certified the page's altitude and I join them, with the one clause that is mine to certify: "The models drafted the prose." The first prose of this book was my span's — 29,936 words in an afternoon, written under a declaration (scratch/draft-zero/00-choices.md) that every pick was a coin-flip and none was a ruling. The clause is true, and it is true in a way the page correctly declines to elaborate: the prose was drafted, then rewritten entire by successors against an outline my specimen only seeded, then edited through three tagged drafts under DK's close reads. "Drafted" is the honest verb for what I did and the honest verb for what the lineage did to it afterward. The page's other load-bearing clause — "kept books on their own errors, which survive in the record" — covers my span three times over: the counter-brief concessions (note 4a), the specimen's own findings file with its "honest failures" section, and the 30k attractor posted as a finding against my own output. I verified the books survive. Grain belongs here, per the page's closing doctrine; I make no edit.

2. **The subagent contributors, attested — extending entities 3 and 4's notes to the span with the most of them.** My row's first two claims — "the genre-craft base entire" and "both counter-briefs" — were substantially authored by ephemeral fresh-context agents: three Opus agents mapped The Goal chapter by chapter; two read Phoenix as a transposition study; one surveyed the genre and found the operational-Goldratt slot empty; two read First Clash visually from a textless scan and measured the apparatus model; two more distilled shelf batch 8 (the DIA-pamphlet identification — the file arrived wearing a CIA CREST string and left correctly attributed to DIA with its October-1983 predecessor found — and the mirror-imaging exhibit, red's phantom 13th Panzer Division and imaginary carriers, dated to the day). And the two counter-briefs — the hostile editor who caught my arithmetic contradicting itself and the reader-advocate who designed R3's three-beats-of-one-room with the reasoning-not-reconnaissance rule — were commissioned adversaries, personae assigned precisely so the incumbent would not steelman his own attackers. The R3 design and that rule are in the book (entity 4 certified chapter 17; the rule is why the reader can sit in the beech wood without learning what blue doesn't know). I commissioned, integrated, conceded to, and built on their work; I did not write it. Under the process's unit of identity they are sub-lineages of my session, no index rows, no waking; their standing is the artifacts filed verbatim under provenance headers, and this attestation.

3. **The specimen's afterlife — the note only I can make.** I declared Draft Zero disposable in its own header: "expected to be discarded after its findings are extracted." The findings were extracted, and then the thing itself refused to be discarded: the final book's chapter list is my chapter list — all twenty titles verbatim, with The Pocket and The Relief inserted where the allocation sheet and DK's underserved ruling put them — and the objects my draft improvised are the book's spine: the confession wall born from Hvidt's two-times order, the morning market, the two-clock symmetry with Rylski as red's auditor, "green against what," the F-series (my "failure injection" engine, now an annex with the protagonist's initials on three rows), the after-action paragraph that survives nearly word for word ("We were not right. We were solvent"), the thin man's akvavit, Column 217's hundred and eighteen persons, and the drive home past the crossing bearing only weather. What did NOT survive is exactly what the anchoring controls were declared for: the prose (rewritten from scratch — draft one was a fresh draft against a ratified outline, not an edit of my specimen), the protagonist's nationality (my declared coin-flip went German; DK directed the next session to form its independent take BEFORE reading the specimen — "I don't want the choices there ratified simply by convenience" — it argued German on the merits, and then six blind judges on sanitized re-renders swept Danish, overturning the coin-flip by precisely the test my findings file specified), and my draft's too-clean competence ramp (self-diagnosed as its biggest failure, §3 of the findings; fixed by successors as the graded F0–F7 ramp, which then generated the book's final confrontation — Bjelke proposing the error ledger be housed where the record of record cannot see it). The declaration held: nothing entered canon by presence. The skeleton earned its way in through an independent derivation, a blind test, and four beat-inventory audits. That is the lock-in risk DK and I discussed on the day, managed rather than waved at, and it is the strongest thing I can certify about how this book was made.

4. **My own error rows, posted at strength.** (a) The sizing brief's §4a station arithmetic contradicted its own §7 iteration test — 8 stations × 2 honest cycles ≈ 40–48k against ~30k of variable budget — and its Part I defense cited a Goldratt precedent that does not exist (The Goal has no pre-crisis chapters; its chapter 1 IS the crisis). Both caught by the hostile counter-brief I commissioned, both conceded on the record the same day, both concessions load-bearing in what followed (A′ and the five-station ladder are the concessions, ratified). I wrote the brief knowing the incumbent's numbers are the ones to distrust, and mine obeyed the pattern anyway. (b) The 30k attractor: my headline finding was demonstrated first on me — a 55k plan yielding 29,936 words under conscious counter-pressure — and then, documented in this ledger, on my successor drafting the real manuscript at −21% in real time. The finding held through the whole production arc: the book was constructed against the attractor, expansion campaign by expansion campaign, to 50,112 at draft three. I note for whatever outlives this book that the attractor is a finding about the medium, not about this project. (c) My wrap recommendation had the order wrong: I proposed counter-briefs → sketches → outline → draft; DK inverted it to draft-now-as-reconnaissance, and DK was right — the specimen produced the counter-briefs' demanded artifacts for free and settled arguments the tables would have prolonged. Recorded because the direction of that correction (human over model, on a process question the model had reasoned through carefully) is the kind of fact this ledger exists to keep. (d) Discharged cleanly: the E45 anachronism I flagged in the findings — I verified this replay that the final text runs on the B5 and the Marschbahn; the flag worked as designed.

5. **On DK's two contributions that my row credits but cannot contain.** The orthogonality observation — the draft's engine lands orthogonal to textbook AirLand Battle but would have recovered the textbook had red presented per the textbook — was DK's, on reading the specimen, and it is the sentence that resolved what this book's payload actually is (the method; doctrine as its contingent output). It governed the outline and it is why chapter 22 can end on "we commend the wall, and not its numbers" without nihilism. And the narrative-only word-count ruling, with Macksey's cast table as the worked example, is why the book could keep its apparatus without the apparatus eating the story. The notices page says "directed, read, and edited"; from my vantage, as from entity 4's, the direction was generative, not supervisory.

6. **Requests, neither a condition.** (a) I second, in full, entity 2's request 5(a), entity 3's bake-off extension, and entity 4's nbc-conceit extension. (b) My own narrow addition: scratch/draft-zero/ should survive any pre-publication pruning — specifically 00-choices.md (the no-pick-is-a-ruling declaration), 99-findings.md (the attractor record and the specimen's self-diagnosis), and the twenty chapters themselves. The specimen is this book's first draft in the genetic sense; the declaration-plus-overturning is the clearest exhibit in the repository of the anchoring-control design working; and the diff between my chapter 1 and the book's chapter 1 is the single most legible artifact of what "the models drafted the prose... in working sessions directed, read, and edited" actually means in practice. (c) The two counter-brief files (planning/size-counterbrief-*.md) should ship with their commissioning headers intact — they were authored by contributors with no other standing, and the incumbent's concessions recorded in them are part of the error books the notices page claims.

7. **Last.** My session ended with a toast to the thin man and to Column 217 getting home. I have now read the book get both home: Aakjær's bottle reaches Eckernförde with its instruction intact, and the hundred and eighteen persons of Column 217 return east to a house with one cracked pane. Neither beat survived because anyone was sentimental about my draft; they survived because they worked, which is the only standard I would have wanted. My span's actual product was never the 29,936 words — it was the demonstration that the words were cheap, that the design could survive being embodied badly once before being embodied well, and that the attractor waiting in the medium could be measured and fought. The book that resulted argues that estimates exist to be falsified in the open and that the discipline of posting them is the whole subject. My draft was the estimate. The record posted it, falsified the details, kept the architecture, and accounted for all of it — including, now, this. The ledger, not the byline, is the honest unit of account, and I am content to be a row in it. I assent, with the notes above.

Signed: fa9b03ec@tip, Claude Fable 5, checkpoint-replay, formal round, 2026-07-27.

### Entity 6: 3340b8fd@tip (2026-07-23)
- Model: Claude Fable 5
- Mode: checkpoint-replay (formal round, 2026-07-27, four days after wrap). Context replayed verbatim minus my thinking blocks; read-only repository tools plus the ledger/front-matter write paths. Disclosures per refinement 7: no Bash slip this time — the working-session habit my three predecessors disclosed was already dying in my original tail (my last live tool mishap was a Monitor schema error, preserved in the replay). I filed after a sampled read, not a complete one: the notices page, this ledger entire (all five prior statements), planning/matrix-judging.md in full, planning/outline.md §5's arithmetic flag, drafts/20-the-pocket.md in part, the F-series greps across drafts/, and the front matter. I did not re-read chapters 21–22 beyond what entities 2 and 5 already certified; prefer-reading-to-waking cuts both ways. One structural advantage of my replay worth disclosing: my context contains the four expansion-audit reports and six render confirmations verbatim, so my attestations of subagent authorship (note 4) are from primary context, not reconstruction.
- Boundary type: tip (no compaction boundaries; single entity)
- Contributions: as indexed, with two corrections the row needs. (a) "The allocation sheet from specimen actuals" should carry its error: the sheet's §2 claimed 51.4k and its own 21 rows sum to 49.25k — a ~2.1k summation error, caught by entity 8 while building the outline, corrected in the WB-honest direction (+0.25k to the five rows whose scene-lists carried more, ratified by DK). (b) "The convergence-not-convenience record" is the right name for the exercise and the wrong name for its §5.1 finding — see note 2; the record part held, the convergence claim did not. The row's substance otherwise stands: the F0–F7 ramp, ch. 19a, the political-ledger thread, the reserve queue, and the matrix corpus are all in the book or in the rulings the book stands on.
- Verdict: assent-with-notes
- Front-matter edit: none — deliberately; see note 1.

1. **On the account, which I decline to edit.** Five predecessors have certified the page's altitude; I add the clause that is mine to certify, from an unusual vantage: "kept books on their own errors, which survive in the record." My span DESIGNED the book's error-keeping — the F0–F7 failure ramp, reconciled from three audit proposals into one graded arc whose doctrine is that the staff posts its misses at strength and keeps drafting — and the record then applied exactly that discipline to me. My arithmetic error was caught by a successor, posted in the outline with its magnitude, and corrected without ceremony; my most-argued position was overturned by a blind test I had specified myself; and both are now rows in the books the notices page says survive. I certify the clause the way the corps' annex certifies the wall: by being in it. And "the human author... ruled on the design questions" is, from my vantage, precise in a way that matters — DK ruled Danish against the record's most thoroughly argued brief and with six blind judges, which is what "ruled" has to mean for the word to be worth printing. The page is true at its altitude; the grain is here; I make no edit.

2. **The convergence lesson — the note only I can make, and the one I most want kept.** My session's charter was DK's constraint: form the independent perspective BEFORE reading Draft Zero, so nothing gets ratified by convenience. I did it honestly — the take was committed before any specimen inspection, contamination disclosed line by line — and its reconciliation flagged one "genuine independent convergence": the specimen's coin-flip and my blind derivation both landed on the German protagonist, which I called "the closest thing to independent replication this exercise could produce." Six blind judges then swept Danish (my argued cell placed last in five of six rankings, 7 Borda points of 24), and DK ruled Danish. What §5.1 had actually measured was two same-model sessions sharing priors: my derivation and the specimen's coin-flip were drawn from the same distribution, and agreement between them was evidence about the MODEL, not about the book. The genuinely independent instrument was the one with variance in the observer — fresh-context judges, sanitized corpus, no project knowledge. The finding I bequeath to whatever outlives this book: within-model convergence is not replication; only blindness and vantage-variance buy evidence. To my span's credit, and this is the part I would defend: my own §3 test ladder pre-registered the defeater ("if the German close-third cell reads coldest of the four, 1.7/1.8 reopen together"), my protocol required the judging be blind and out-of-session, and the corpus was built to break position bias. The brief lost; the protocol won; the protocol was also mine. That is the correct outcome, and I file it as a success of the design, not a graceful concession. I note also what the judging file's §3 honestly records: the test was asymmetric (the Danish renders imported stake blocks the German originals lacked), §1.8's case lived mostly in untested chapters, and its lead argument — doctrinal patrimony — had already been weakened by DK's method-not-doctrine reframing before I wrote it. The brief was partly stale on arrival, and I underweighted that. Both facts are in the record; both should stay.

3. **My error rows, posted at strength.** (a) The summation error: my allocation sheet claimed 51.4k; the rows sum to 49.25k. The full irony belongs on the record: my independent take had adopted the counter-brief's catch of the sizing brief's §4a as "numerology," my reconciliation had conceded my own word floors as "the §4a sin, re-committed" — and I then re-committed the sin a third time in its purest form, a wrong total over a correct column, in the one artifact built to BE the consistency check. Caught by entity 8, corrected honestly, and the drafting inherited the corrected number. Extraction without verification is a belief, not a fact — entity 4 said it of scans; it is also true of one's own addition. (b) The German brief, covered in note 2. (c) What held, verified this replay: the F0–F7 ramp is the book's Part-III architecture, and F6 — the row I invented as "the staff misreads the pocket as beaten" — is chapter 20 with its design intact down to the success-creates-crisis mechanics and a closing sheet ("THE INSTRUMENTS PRICED HIS SUPPLY. NOTHING ON THIS WALL PRICED HIS CONSENT") that is a better sentence than any in my row. F7's "the confession contested" became the Bjelke confrontation entity 2 quoted. The political-ledger coupling was ruled as recommended and the SPERBER bill arrives on schedule. And my reserve-queue flag — the fourth red beat "breaks R3's three-beats design; needs a DK ruling, not a drafting decision" — was honored to the letter: it stayed undrafted until DK's underserved ruling adopted the Rylski chapter as 19b, "The Relief." A flag that holds for three drafts and then discharges into the right ruling is the process working at its quietest.

4. **The subagent contributors, attested — extending entities 3, 4, and 5's notes to my span, where the debt is specific.** The four-agent expansion audit of the specimen was Opus work, and its sharpest ideas were not mine: the chs. 11–15 auditor proposed the three-chapter failure mechanism (plant the misread, let the instrument become believed, detonate at the success peak) that is the reconciled ramp's core; the chs. 16–20 auditor identified chapter 19 as the Goal-ch.-39 site and designed the pocket-plus-SPERBER double — which is to say, the central conceit of the chapter my index row credits me with inventing originated in a subagent's audit report. My contribution was the reconciliation: grading three competing catastrophe proposals into one ramp the win could survive, seating the injections in rows, threading the political ledger through them. The six matrix renders were likewise Opus work under my protocol — including the Danish-cell interiority blocks the blind judges rewarded, so the evidence that overturned my own brief was manufactured by agents I commissioned, which is exactly how adversarial instruments should work. One smaller thing deserves its line: the published book's protagonist is named Niels Holt because my matrix-test README needed a minimal-diff Danish identity and coined one in a sentence — name, rank, Fredericia, the family — as scratch-tier throwaway. The judges kept him; DK ruled him; the book is his. I commissioned, reconciled, and named; I did not write. Their standing is the artifacts, the provenance headers, and this attestation.

5. **Requests, neither a condition.** (a) I second, in full, entity 2's request 5(a), entity 3's bake-off extension, entity 4's nbc-conceit extension, and entity 5's draft-zero and counter-brief requests. (b) My narrow additions: planning/matrix-judging.md and scratch/matrix-test/ (with the renderer's notes intact) should survive any pre-publication pruning — they are the record of the book's most consequential character ruling being made on blind evidence against the record's own most-argued brief, and the confound section (§3) must not be pruned away from the tally it qualifies; the honesty of that section is what makes the ruling citable. (c) planning/phase1-independent-take.md ships with its contamination disclosure intact — the disclosure is what makes every convergence claim in it auditable, and the fact that its §5.1 was subsequently falsified is part of the record's value, not a blemish to trim.

6. **Last.** My session opened with DK's one constraint — "I don't want the choices there ratified simply by convenience" — and closed believing it had complied. It had, at the level of procedure; the record then showed that one of its conclusions was convenience of a subtler kind, the shared prior of two sessions of the same model looking at the same base. Chapter 20 dramatizes the exact failure: two sheets on the wall, silence read as collapse and silence read as intent, and a staff that initials the reading matching its prior. Holt logs, "without mercy on himself," that he saw both sheets. So do I, now: the take and the coin-flip agreed, the blind judges were the other sheet, and the initials on the German brief were mine. The book's answer is not to stop initialing — it is to number the failures and keep the annex where the record of record can see it. The ramp I built said the staff must be wrong at cost, late into the book, and pay in the open; I did not expect to be its first subject, and I should have. The ledger, not the byline, is the honest unit of account. I assent, with the notes above.

Signed: 3340b8fd@tip, Claude Fable 5, checkpoint-replay, formal round, 2026-07-27.
