# Wargaming approach

*Status: instrument campaign 1 CLOSED (2026-07-21, v6). Mechanism
inventory, claim ledger, and research handoff live in
notes/wargaming-findings.md; resume model work after the
calibration research pass.*

*Step-0 sketch (2026-07-20). Purpose and options; system choice is a
Phase-1 decision after the echelon/front question narrows.*

## What the wargaming is for

Following the Red Storm Rising / Convoy-84 precedent (Clancy & Bond
gamed the convoy battles; the book's operational spine came out of
the game), but scoped to our needs:

1. **Plot logistics integrity.** Time-space-attrition honesty at
   50-60k words of sustained operations: can that brigade actually
   reach that river line by that chapter; what does a week of
   defensive combat leave of a division. Feeds and is fed by the
   order-of-battle ledger (CLAUDE.md) — the game state IS the ledger's
   attrition column.
2. **Honest surprise.** A gamed campaign produces the unplanned
   reverses and ugly tradeoffs that invented campaigns lack; the
   Convoy-84 lesson is that the dice write better operational irony
   than the author does.
3. **Doctrinal demonstration.** The book's thesis (tempo as
   throughput, echelonment as constraint) should be *checkable* in
   the model: if the counterstroke works in the narrative but not in
   the game, that is an Andon Cord moment for the thesis itself.

## Options

**1. Ad hoc, period-published models in Python (current lean).**
Implement the models the period itself argued with — which makes the
tooling double as research and even as diegetic texture (a 1986
staff officer can plausibly have met Dupuy's numbers or the
Lanchester debate):

- Lanchester square/linear laws — the baseline everyone attacks;
- Dupuy's QJM (Numbers, Predictions and War, 1979/1985) — the
  attrition-and-advance-rate framework actually used in 1980s
  NATO/WP net assessments;
- Epstein's adaptive dynamic model (The Calculus of Conventional
  War, 1985) — built *against* Lanchester precisely to model
  withdrawal and tempo decisions;
- the Posen/Mearsheimer attrition-FEBA exchange (International
  Security, 1984-88) — the 3:1 rule debate, i.e., the period's own
  fight about whether these models mislead (thematically on the
  nose: metrics that mislead is the book's engine).

Deterministic + seeded, inspectable, pytest-covered, outputs writing
directly into the OOB ledger. Hex/area map as plain data files.

**2. Semi-COTS: open engines.** Survey before committing (forced
alternatives; queue a proper look in Phase 1):

- **VASSAL** (open-source board-wargame engine) — we'd build a tiny
  module over our own map/counters; buys a real map UI and manual
  play with DK, costs module-building time and gives no automation;
- open-source hex-wargame codebases (candidates to survey: any
  maintained operational-level engines with data-driven scenarios);
- commercial period sims (Flashpoint Campaigns, the Tiller corpus)
  are out per the free/open constraint, but their documentation and
  scenario research are legitimate shelf material.

**3. Hybrid (likely landing zone).** Python models for attrition/
tempo arithmetic and ledger integration; a VASSAL-or-paper map for
the human-visible operational picture when DK and the session game a
campaign move-by-move. Decide after the front is chosen — LANDJUT
needs naval/amphib representation that none of the land models
carry natively, which would push more weight onto the ad hoc side.

## Baseline to build against: Littoral Commander: The Baltic

DK's pointer (2026-07-20) for the non-model-based part; rules PDF on
the shelf (`reference/pdf/littoral-commander-baltic-rules.pdf`, 104
pp, Bae & Wernert, Dietz Foundation 2025). Deltas first: LC is
**grand tactical** (20 km hexes, company-battalion counters, hours-
scale turns) with a 2030+ unit set; we are closer to
**micro-strategic** (DK's term — a whole small theater held in one
frame, days-scale, division/brigade counters, mid-80s kit). So it is
a baseline, not a chassis. What's worth stealing:

- **Capability cards bought from a command-point budget** (LC's
  JCCs): a clean way to represent theater-level enablers (a FOFA
  strike package, a sortie surge, an OMG commitment) as discrete,
  priced decisions rather than continuous modifiers — and priced
  decision-making under a budget is literally the book's subject.
- **Deception counters and concealment as first-class units**
  (MILDECs): cheap fog-of-war that produces honest surprise without
  hidden bookkeeping — the recon-strike payload needs exactly this
  (what you kill may be a decoy; what you didn't find kills you).
- **Logistics units with explicit resupply values**, targetable and
  capturable: throughput made visible on the map.
- **Naval zone abstraction** (off-map areas at 700/1,200 km with
  range/CV penalties): the pattern for LANDJUT's Baltic dimension —
  represent the sea fight's *pressure* on the land campaign without
  simulating it.
- **Initiative from results** (last turn's destruction decides who
  moves first): tempo advantage as an earned, visible state — close
  to the book's thesis in mechanism form.
- **Scenario = narrative + OOB + CP allocation + victory conditions**,
  and the rulebook's own ethos ("adapted to fit the educational
  objective and not as a straitjacket") — the right spirit for an
  instrument that serves a manuscript.

What we would *not* inherit: card-driven near-future kill-chain
content, the 2030 unit set, and the tactical turn grain — our
attrition/advance arithmetic comes from the period models (option 1),
with LC-style structures carrying the parts models don't
(deception, discrete enabler decisions, the sea's shadow).

## Resolution structure (ratified by DK, 2026-07-20)

Top-down, not bottom-up. The honest quantities are aggregate
(division/corps: movement, daily attrition, throughput, decision
lag), the period models and their calibration data live at that
grain, and bottom-up aggregation has no validation ground truth —
it compounds error toward being confidently wrong about exactly what
the book is about. Structure:

- **Top of frame = the theater command owning the front** (BALTAP/
  AFNORTH for LANDJUT), *not* ACE/SACEUR. Higher echelons enter as
  boundary conditions — air apportionment, withheld releases —
  scripted or stochastic, never played. (The reader contract in
  mechanism form: the top of the model is weather.)
- **Battalion is the atomic counter** (~50-80 maneuver battalions
  both sides at LANDJUT scale). Campaign frame moves counters;
  engagement layer (the period models) adjudicates contacts.
- **Decompose on demand only:** a named engagement can be zoomed to
  companies by hand for a chapter, informed by the model's outcome,
  not generated below battalion. Below battalion is prose.
- **Verify top-down:** calibrate against Dupuy's historical rates
  and the 3:1-debate worked cases; run identical scenarios through
  Lanchester/QJM/Epstein and treat divergence as a sensitivity
  brief, not a contest to pick a winner.
- Emergent surprise comes from deception counters, priced enabler
  decisions, and engagement dice — not from simulated fire teams.

## Disciplines (from the project's process rules)

- The model is an instrument, not an oracle: its outputs are briefs;
  the counter-brief (does this result survive contact with the
  research shelf?) precedes canon.
- Every gamed campaign gets committed: inputs, seed, outputs, and
  the narrative deltas it forced — same provenance discipline as
  everything else.
- Calibration comes from the shelf (Dupuy's historical rates, CSI/
  Leavenworth case studies), not from genre fiction.
