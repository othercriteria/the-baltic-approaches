# Project status — successor entry point

*Written 2026-07-21 at the wrap of the Step-0/instrument session
(1a9aba32). Read this first; everything cites its source doc. The
lineage log is in notes/attribution-ledger.md — log your session
start there before working (CLAUDE.md, Provenance).*

## The broad outline as it stands (DK: "broad outline is set")

- **Premise:** The Goal transposed to a NATO corps; tempo as
  throughput. planning/premise.md (founding), planning/
  reader-contract.md (the deal: adrift / confused / earnest — test
  every structural choice against it).
- **Front: LANDJUT / Baltic Approaches** — chosen through three
  ratchets (planning/protagonist-echelon.md): reader-contract
  screen, front reassessment (Bagnall problem, opened GDR archives,
  doctrine-returns-home), and six wargame iterations that kept
  independently generating the theater's dilemmas.
- **Protagonist: G-3 operations at LANDJUT HQ Rendsburg**,
  Oberstleutnant-equivalent, one year in post; arc = discovering
  the G-3's questions need the G-2's and G-4's answers. Corps =
  composite binational staff, working language English, 95-110 km
  from the war. Open: nationality (pure voice decision), exact
  post. Same doc.
- **Command device (lean):** October change of command — new
  commander of the other nation, three weeks in post, missed the
  autumn exercise. Deviations register opened
  (reference/landjut-front.md).
- **Time:** year unpinned within ~1983-87 (now coupled to commander
  nationality — planning/setting-time.md criterion 5); season
  provisionally November.
- **Instrument:** wargame/ campaign 1 CLOSED at v6 — mechanism
  inventory, claim ledger, and the two staged questions (what is
  the goal / what does the enemy think it is) in
  notes/wargaming-findings.md. Research-first handoff there;
  don't resume model work before the calibration pass.
- **Research shelf:** reference/shelf.md (manifest of record; 16
  pinned documents), reference/landjut-front.md (front facts,
  sourced, TO-VERIFY flags), reference/bulk-survey.md (/bulk map).
  Holdings (non-redistributable) in the always-private companion
  repo via holdings/ submodule.

## Two deliberate unsettlings (from the departing session)

DK offered the chance to unsettle the converged choices. Taking it
seriously, two flags — not reversals, but things the fresh eyes
should attack before drafting:

1. **The corps-convergence has a circularity hazard.** The wargame
   "discovered" that every decision lives at corps level — but I
   built the instrument top-down with the corps as its frame (the
   ratified resolution structure). An instrument framed at corps
   altitude will hand its levers to the corps by construction. I
   believe the convergence anyway (the reader-contract and staff-
   structure arguments are independent of the model), but per
   self-review-is-not-clearance, the LANDJUT-HQ-G-3 choice deserves
   one hostile fresh-context review that asks: *what would a
   division-altitude or Danish-brigade book see that Rendsburg
   can't?* Cheap to run, and the answer strengthens whichever way
   it goes.
   **RUN 2026-07-21** (session 71ede904) →
   planning/echelon-hostile-review.md. The review concedes the
   front and the ensemble but lands three real attacks (Rogo has
   authority, the G-3 has a grease pencil; the feedback engine is
   weakest at corps; the instrument contains no non-corps decision
   grades, so the convergence was unfalsifiable as run). It asks
   for two cheap artifacts before the choice is clean: a
   division-framed wargame sketch and a one-page
   Jutland-Division-commander outline. Ruling is DK's; the brief
   is filed, not acted on.
   **UPDATE, same day:** the air-apportionment research
   (reference/air-apportionment.md) CONFIRMED attack 2's premise —
   the deep/close split is COMBALTAP's at Karup — and wargame v8
   answered attack 3's method demand: the instrument now contains
   theater/corps/division decision grades, and across 60 perturbed
   worlds the leverage concentrates at the corps-theater seam
   (advocacy 11.8 CV median spread vs division 1.8), with the
   G-3's one owned air lever (sub-allocation) nearly weightless.
   The division-framed-sketch request is thereby partially
   delivered inside the shared instrument (caveat: division layer
   models only reserve/CA timing so far). The
   Jutland-commander-outline request stands open. Ruling still
   DK's.

2. **The Goal's engine assumes iteration; a three-week war may not
   provide it.** Rogo learns because the plant runs every day —
   experiment, feedback, revise. Nobody has pressure-tested where
   the protagonist's feedback CYCLES come from in a campaign this
   short. Candidates visible from here: the pre-war autumn exercise
   as laboratory (rehearsal chapters = the plant before the crisis),
   the daily air-allocation decision (genuinely iterated, and the
   instrument priced it), and the estimate-vs-outcome log the staff
   keeps (the model's proj-vs-realized columns are this). But if
   Phase-1 outlining can't find honest iteration, the didactic form
   itself needs rethinking — that's an Andon Cord conversation, not
   a drafting problem. This is the unexamined assumption I'd
   examine first.

## Immediate next steps (in rough order)

1. Phase 1 planning proper: outline, parts structure, the ledgers
   (CLAUDE.md lists them; the wargame ledger bridge exists —
   wargame/ledger.py).
2. The coupled character/setting decision: year x commander
   nationality x protagonist nationality x succession direction —
   settle via character sketches (one pass; all four move together).
3. Calibration research pass (blocking model work, not writing):
   ~~FM 101-10-1 consumption extraction~~ (done 2026-07-21 →
   reference/consumption-factors.md, CAL-1..4; CAL-1 sensitivity
   run strengthened v6's deep-dominance), OOB verification and
   PHP/DIIS documents (sources now ON THE SHELF, reading/
   distillation owed — batches 4-6 in reference/shelf.md, incl.
   ORALFORE for the advance-rate bench), mobilization timelines,
   November climatology (both still open).
4. The fresh critique profile of the drafting model (CLAUDE.md
   process rules) — before any prose is drafted.
5. ~~Unsettle-review #1 above, early and cheap.~~ Done 2026-07-21;
   awaiting DK ruling (see the unsettling's entry above).

## Standing DK reminders (loose ends outside the repo)

- Create the private GitHub remote (othercriteria/
  the-mission-1986-private) and push the holdings repo; the
  submodule's relative URL then resolves for fresh clones.
- Main repo has unpushed commits (push at your pleasure).
- After this session ends: `make raw-archive
  SESSION=1a9aba32-d86d-41c9-9fe6-f89d300b45c0` (a session cannot
  archive its own live JSONL; the successor or DK does it).
- Dupuy NP&W scan into holdings when convenient (QJM advance rates
  still the missing calibration piece).
