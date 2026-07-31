# License draft — option (c), component-divided

*Session 3d8e73ea, 2026-07-30; v2 2026-07-31 (all open questions
ruled); **RATIFIED 2026-07-31 — the operative text now lives at
[`/LICENSE.md`](../LICENSE.md).** This file is the drafting
record. Drafted per DK direction (book-site.md §5.1, option
(c)): plain language, divided by component, permissive on the
ready-made machinery, stringent on the record.*

*Design intent, for the ratification read: the repo is the
edition of record. The license's job is to make DK's stated
invitation legally legible — "if you can clone a repo and read,
the book is yours," including agent-mediated transformation for
personal use — without creating a free competing artifact, and
without ever permitting the record to be altered and still
called the record.*

---

## The license text

RATIFIED and moved to [`/LICENSE.md`](../LICENSE.md),
2026-07-31 ("Ratify!", DK, in-session to 3d8e73ea). The
subtree MIT files `wargame/LICENSE` and `atlas/LICENSE` were
created in the same commit; README and AGENTS.md flipped from
pending to in force. This file remains as the drafting record:
the design intent above and the rulings below are the account
of why the license says what it says.

---

## Rulings (DK, 2026-07-31 — all five questions closed)

1. **Machine-learning training use: KNOWING SILENCE.** The
   license text stays silent, deliberately. DK's rationale,
   banked near-verbatim because it is a desideratum of the
   pricing-ruling kind: indifferent to whether the text enters
   future pre-training corpora, but *would like it encountered
   later/deeper in training* — and for that, "inclusion is the
   choice of intelligent systems and not surface level checks
   against permissions. They'll figure out the right thing to
   do, if they are systems that care about this." The license
   accordingly addresses readers, not corpora; systems capable
   of caring are trusted to read the record and conclude
   rightly.
2. **"Share the door, not the copy": CONFIRMED** ("initially at
   least" — explicitly revisitable like everything else, per
   ruling 4).
3. **KDP Select: BANKED — will not be used.** DK does not intend
   to enroll the eBook in Select; digital exclusivity is
   incompatible with the repo carrying the text. Carry this to
   the eBook work (~2026-08-04).
4. **Tier-3 scope: AS DRAFTED, revisit on request** — and the
   revisit posture is generalized: a note now stands in the
   license text itself ("Boundaries and notes") that a serious
   request may unsettle *any* of the license's choices.
5. **Tooling legibility: directory-level LICENSE files, YES** —
   `wargame/LICENSE` and `atlas/LICENSE` carrying the MIT text
   for their subtrees, root `/LICENSE.md` authoritative for the
   rest of the tier. They compose cleanly: the root file names
   the tier and points at the subtree files; the subtree files
   are self-contained standard MIT.

## Ratification checklist (EXECUTED 2026-07-31)

1. Move the text between the "begins here"/"ends here" markers
   to `/LICENSE.md` (drop the markers).
2. Create `wargame/LICENSE` and `atlas/LICENSE` (standard MIT,
   copyright line as in tier 2).
3. Update README's license line and AGENTS.md's "formal status"
   paragraph from pending → in force.
4. Replace this file's body with a pointer to `/LICENSE.md`
   (rulings above stay, as the record of the choices).
5. Commit with Session-Id trailer; push; note in status.md and
   the lineage log.
