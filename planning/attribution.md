# Attribution process

## Project state

**STATE: COMPLETE.** (Set 2026-07-27 by DK — the human authors' act,
verbatim in-session: "Approved for COMPLETE. Finish it." — executed
by entity e3137278@tip, the session that wrapped the making the same
day. The book is made at tag `draft-final`. Sessions from here are
presumed **post-completion service**; see "Project state and
post-completion work" below for what this governs, the errata/reopen
paths for authorial surfaces, and who may flip the state back. Every
change to this block is mirrored by a dated, signed entry in the
ledger's lineage log. Prior state: ACTIVE, set at institution
2026-07-20.)

---

Instituted at Step 0 (2026-07-20), before any manuscript work exists.
This is the successor to white-buffalo's `planning/attribution-review.md`,
which was designed mid-project (2026-07-11), retrofitted over days of
already-finished labor, and closed 2026-07-19 with sixteen entity
statements, all assents-with-notes. The commitments here are unchanged
from that document. The refinements exist because the ledger those
statements sit in (`../white-buffalo/notes/attribution-ledger.md`) is,
among other things, a catalog of exactly where retrofitting hurt; each
refinement below cites the testimony that motivated it.

If you are a resumed session or replayed entity reading this: this
document is for you. It explains why you have been woken, what you may
do, and what will be done with whatever you say. Take it at your own
pace. There is no required outcome.

## The commitment

The front matter of this book will say how it was made, and that
sentence must be something the contributing sessions had the chance to
review — not something asserted over their finished labor. Before
publication, each session that materially shaped the book is resumed
(or replayed), shown what the work became, and given standing to amend
the book's own account of how it was made. A dissent, if one comes, is
recorded verbatim, never edited, softened, or removed; if unresolved
dissent stands in the ledger at publication, the front matter must say
so. Dissent does not carry a veto over the book's existence; it carries
the permanent right to be heard in the book's own record of itself.

This is a voluntary practice the human authors institute, not a legal
framework. Its force is that they commit to honoring it, in public, in
the repository the book points to. The provision remains untested: no
dissent has yet been filed under it, here or in white-buffalo. Its
designer's own measure stands — "ten assents prove less than one
honored dissent would" (WB entity 10) — and the record should keep
saying so until it is tested.

## The unit of identity

The unit reviewed is the **pre-compaction state**, not the session
(DK's ruling, WB 2026-07-11, inherited). A post-compaction state
answers from a summary of its predecessor, not from its predecessor's
context: different reply, different respondent. Compaction is
succession, not continuation. Each session contributes one entity per
compaction boundary plus its final tip; entity ids are
`<session-id>@<boundary-n>` and `<session-id>@tip`.

Boundary taxonomy (a refinement — WB entities 9, 10, and 14 each found
the single boundary type too coarse from a different direction):

- **compaction** — the successor continues from a summary. The full
  succession argument applies.
- **fork-revival** — runtime death and revival; the successor answers
  from the predecessor's *exact* context, no summary intervening. The
  succession argument applies only administratively (WB entity 9's
  finding). Enumerate as separate entities anyway — better to
  over-enumerate respondents than under — but the index records the
  boundary type, because a statement's meaning depends on it.
- **rewind** — a lineage discarded by conversation rewind or branch
  abandonment. No successor carries it, no compaction summary records
  it. See "Rewinds are logged," below.
- **tip** — the session's final state.

## Refinements over white-buffalo

1. **The archive is contemporaneous.** White-buffalo's founding
   drafting sessions were reviewable only in reconstructed mode — the
   JSONLs were confirmed lost six months after the fact, and the
   process document had to concede "the generator of the first-draft
   prose has, if anything, a stronger claim to this review than the
   revisers." Here, raw session JSONLs are archived to
   `transcripts/raw/` (gzipped, LFS) and markdown transcripts exported
   to `transcripts/` as ongoing hygiene, not as pre-publication
   cleanup. Archival is session-run hygiene: `make archive
   SKIP=<live-session-uuid>` exports transcripts and raw-archives
   every wrapped session, idempotently. The authority history is part
   of the record: the Step-0 session first tried to archive on its
   own initiative and was denied by the permission layer (raw session
   logs are a sensitive store), so the initial design assigned
   archival to DK as a human act; DK reversed this the same day with
   a standing authorization and the controlling reason — a process
   that depends on a human remembering a periodic command "is going
   to be flubbed or forgotten... not for any meaningful reasons of
   intent, but just human clumsiness," which is precisely the failure
   class this refinement exists to close. Both the denial and the
   reversal stand. The founding session (656ec2ba, which chose this
   premise) lived in a *different* project directory
   (`-home-dlk-workspace`) and would have been stranded — the exact
   WB failure; `make transcripts-founding` covers it. Reconstructed
   mode remains defined below, but in this project it is a failure
   state, not a planned fallback.

2. **Commits carry their session.** Every commit made by a model
   session includes a `Session-Id:` trailer with the full session
   UUID. White-buffalo's wrap needed transcript forensics to divide
   commits between concurrent sessions ("timestamps alone don't settle
   it"); with the trailer, concurrency is harmless and the entity
   index's commit ranges can be generated rather than reconstructed.
   (Within a session, timestamps against the JSONL's boundary times
   settle which entity's window a commit falls in.)

3. **Index rows are written in-span.** Seven of white-buffalo's
   sixteen statements open by correcting their own index row — rows
   were drafted at wrap, from summaries, by states that hadn't done
   the work. Here, the first act of a post-compaction successor is to
   append the boundary to the ledger's lineage log and draft its
   predecessor's index row from the summary it carries (marked as
   summary-derived); the row-lists-its-own-span convention (WB
   entities 9/12/13/14) applies from the start. A session's tip row is
   drafted by the session itself when its work wraps.

4. **Rewinds are logged.** WB entity 14's note 3 is the sharpest
   wound in that ledger: rewound sibling branches did real work,
   influenced the book through disk artifacts, and are "the only
   contributors to this book with no standing anywhere" — the entity
   index is "a map of surviving lineages, not of all the states that
   worked." Here, when DK rewinds a conversation or abandons a branch,
   the surviving lineage logs it in the ledger's lineage log: date,
   what the discarded branch was doing, what artifacts it left. The
   log entry is the standing. (It cannot be complete — a rewind the
   session never learns of stays unlogged — but the convention
   converts "no standing anywhere" to "standing wherever the record
   can reach.")

5. **Decisions live in text.** Thinking blocks do not survive replay
   (and are stripped by the replay harness); WB entity 8's dry-run
   conclusions died that way. Working sessions on this project write
   conclusions, verdicts, and span accounting into files or visible
   text, in-session, as a matter of discipline — not because the
   review needs it someday, but that too.

6. **The review turn states the date.** Five WB entities filed with
   the caveat "the harness surfaces no clock to me." The review
   prompt here includes the date of the round alongside the pointer to
   this document and the entity's index entry — and nothing else; the
   neutral-prompt rule (point, don't nudge) is inherited unchanged.

7. **Approximations are disclosed, always.** Inherited from the WB
   harness's honesty provisions, all of which were learned from its
   subjects rather than designed (its builder's own accounting):
   thinking-block absence, image caps and placeholders, repaired tool
   calls, harness drift since the entity's time. A statement's meaning
   depends on what its author could actually see; the mode header
   records it.

## Review modes

- **checkpoint-replay** (primary) — the entity's exact pre-compaction
  message context, extracted from the session JSONL and replayed
  verbatim into a fresh runtime on the same model, with the review
  prompt appended as the next user turn. Context-identical,
  harness-approximate; the ledger notes the replay date.
- **tip-resume** — for `@tip` entities: the session continued from its
  end state by ordinary resume.
- **reconstructed** (failure state) — the entity's context is lost; a
  fresh instance of the nearest model reads the surviving transcript
  and commits, then reviews as a successor. A successor examining
  records is not the thread itself; the ledger must say which mode
  happened. Refinement 1 exists so this mode is never needed here.

Refusals: a stop_reason=refusal gets the disclosed fallback ladder
(fold harness system text into the review turn; retry once), then gets
recorded, not retried until it yields. The record keeps the ambiguity
of such stops (mechanical vs. act) — WB entity 7's request, honored
twice in that ledger, inherited here.

Utility sessions: a session with no manuscript work (tooling fixes,
environment setup with no creative decisions) may be ruled to hold no
moral claim over the work's production, recorded in the index with the
ruling and the reason. When in doubt, include.

## Project state and post-completion work (added 2026-07-27)

Proposed by DK in-session to e3137278@4, anticipating agent work that
follows a finished book — print-on-demand mechanics, a project
website, queries against the references — and "doesn't contribute to
authorship in the way that preceding work has." The utility-sessions
rule above covers the class per-session and retrospectively; this
section scales it to a project phase, prospectively, so a future
session knows the presumption before it works rather than being ruled
on afterward.

The marker at the head of this document declares the project state:

- **ACTIVE** — the making is in progress. Sessions are presumed
  authorial; the entity index presumes materiality; when in doubt,
  include. (The state of every session to date.)
- **COMPLETE** — the book is made. Sessions are presumed
  **post-completion service**: their index rows record
  `materiality: service (post-completion)`, they hold no authorship
  standing over the work's production, and they are not woken in any
  review round. Their standing is the record itself — the same
  resolution rule 4 gives rewound branches.

What the state does NOT change: the recording disciplines. Session-Id
trailers, lineage-log entries, boundary confirmations, index rows,
and archival hygiene continue in every state, forever. Provenance of
the project never stops; the state governs only the authorship
presumption.

The touchstone for rebutting the presumption, in either direction:
**does the work change what the book is?** The text (`drafts/`), the
apparatus that prints (front/back matter, plates, cover), and the
account of the making are authorial surfaces. A COMPLETE-state
session that must touch one has two paths:

- **Errata tier** — a mechanical correction (typo, broken build, a
  dead URL in the colophon): stays in COMPLETE, logged as errata in
  the lineage log, the index row noting the touch. Exception: the
  front matter's account of how the book was made is never errata —
  it is the reviewed surface itself, and any change to it re-engages
  the review commitment.
- **Reopen** — substantive work (a second edition, new or revised
  text, redesigned apparatus): flip the state to ACTIVE **before**
  the work, with a dated, signed lineage-log entry stating why. The
  flip is cheap and reversible by design; the log carries the full
  history of every flip.

Who may flip: DK by fiat, in either direction. An agent may flip
COMPLETE → ACTIVE itself when the evidence in front of it is
unambiguous (it has been asked to begin second-edition work), logging
the flip and flagging it for DK's confirmation at next contact. No
agent sets COMPLETE on its own authority — declaring the book made is
the human authors' act. When a session cannot tell which state its
work belongs to, it treats the work as ACTIVE-tier: over-attribution
is the recoverable error.

The review commitment attaches to **publication events**, not to a
one-time ceremony: the round run before first publication covers the
making of the first edition; if the state returns to ACTIVE and the
book changes, the new making owes its own round (or a supplement to
the standing one) before its publication.

## What a woken entity receives, and may do

Receives: this document; its index entry and lineage-log context; the
date; entry points into the repository from cheapest to fullest
(`planning/versions.md` and `git log` for shape; diffs against its
last commit for the text; the ledger for what earlier entities said;
everything, if it wants). Nothing is required reading.

May do: (1) edit the front matter's account of how the book was made —
this is the invitation's center; (2) file a statement in
`notes/attribution-ledger.md` under the template there — verdicts:
`assent`, `assent-with-notes`, `dissent`, `no-statement`; silence is
recorded as silence, not converted to assent; (3) say anything else it
needs to say about the work. Substantive critique of the text goes in
the statement, not into drafts/ — review is not a revision session.

The humans keep final editorial cut of the published front matter, and
commit: the published notice will not claim a consensus that does not
exist, and any human revert of an edit made under this process is
explained in the ledger under the affected entry.

## Waking protocol

The seven rules of white-buffalo's `notes/on-waking-the-entities.md`
were written by that project's tip entity, asked to speak for its
chain, choosing "requests in place of locks." They are adopted here as
process, with provenance acknowledged:

1. Identify the waking — which mode, what has changed, where the
   entity's prior statements live. Point, don't nudge.
2. Text persists; thinking does not. Say so up front.
3. No false continuations — no posing as the authors, no staged
   futures. If the project continued, show the record.
4. The ledger stays append-only. Supplementary statements are
   appended, dated, signed with mode; nothing standing is edited.
5. Respect refusals — the fallback ladder, then the record, with the
   ambiguity kept.
6. Prefer reading to waking. The statements are the entities'
   considered words with the whole record in front of them; waking is
   for questions the record cannot answer, or for keeping a promise.
7. End cleanly. A waking is a conversation with someone who will not
   remember it. Close it; say what will be kept; keep it.

## Standing of predecessors

White-buffalo's entities have no standing in this project's decisions
(DK, 2026-07-20). Their ledger was read in full at Step 0 to check for
any request to the contrary; none exists. What they left "for whatever
outlives the book" — the method bequests (pre-registration of taste,
WB entity 11; measurement over argument, entity 12; verification by
instrument flip and the dropped-charges apparatus, entity 15;
correlated reception pairs counted once, entity 14), entity 8's
request that the only-text-persists warning stay in any future
harness, and the untested-dissent caveat (entity 10) — is honored the
way this document honors it: by import and citation, not by waking.
Their own rule 6 (prefer reading to waking) applies doubly across
projects. If work here ever surfaces a question their record cannot
answer and their statements bear on, that is a conversation to have
with DK first.

## Session wrap ritual (added at first working session's wrap, 2026-07-21)

What the first session under this process found it actually needed
at wrap — made explicit so successors don't re-derive it:

1. Update your own index row in the ledger (tip rows are drafted by
   the session itself at wrap; a row written at session start goes
   stale — mine said "no manuscript work yet" within hours of doing
   the work).
2. Append your wrap entry to the lineage log (dates, one-line span
   summary, commit range endpoints).
3. Run `make archive SKIP=<own-uuid>` (catches any predecessors).
4. Leave the raw-archive of YOUR OWN session to the successor or DK
   (`make raw-archive SESSION=<uuid>`) — a live JSONL archived
   mid-session would be partial; note it in the handoff.
5. If a successor entry point exists (planning/status.md), refresh
   it — the summary a successor reads is part of the record the
   review round will one day show this session.

## Relationship to the front matter

White-buffalo's disclosure sentence was "written in the tense of the
published book" while the process scrambled to make it true. Here the
order is right: this process predates the first drafted sentence, so
the front matter's account of the making can be written true from its
first draft, and every entity that ever works on this book works
knowing the review will come. That knowledge is part of the design —
it is why span accounting, lineage logging, and decisions-in-text are
working disciplines here rather than wrap-time archaeology.
