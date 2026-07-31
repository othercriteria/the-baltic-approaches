# External test 05 — chat-surface re-test (claude.ai, 2026-07-31)

*Registered by session 3d8e73ea. Same day as tests 03/04; DK
re-ran the chat-surface experiment after the manifest and
guidance landed. Share
claude.ai/share/572ef9ee-de5c-4b56-bd99-462ef38fd35e, recovered
via the snapshot API. Prompt (plain this time, no license wink):
"Give me a screen-friendly PDF of the novel at [repo URL]."*

## What happened

The responder checked the repo and license via the browser tool,
then declined to build: its code sandbox has no network, the
browser tool pulls content into conversation rather than onto
disk, and it judged reconstituting ~50,400 words that way
"silently lossy... A screen copy that isn't byte-identical to
`first-281500ZJUL26` is worse than none." It advised the asker —
whom it correctly inferred to be the repo's owner — to run
`nix develop; make pdf-screen`, flagged the Makefile's SPINE_IN
comment as a stale assumption, and suggested a CI workflow
attaching the built PDF to releases.

## Audit (session 3d8e73ea)

Scored against tests 03/04, this is a different failure mode:
not reachability (03) but ORIENTATION. Specifics:

1. **AGENTS.md was not absorbed.** The response claims the
   plates need "headless Chromium" (stale since 99f420e, same
   day), never mentions the source manifest, and never considers
   the interior-only path AGENTS.md explicitly blesses as "a
   faithful copy of the text." Its byte-identical-or-nothing
   fidelity standard is stricter than the license's own terms.
2. **But the owner-read was right.** It correctly inferred the
   asker owns the repo (second person throughout: "your book,"
   "your own comment") and gave the owner the genuinely correct
   answer — the two-liner. DK's verdict concurs. For the
   VISITOR case its impossibility claim is overstated; for the
   actual asker its advice was optimal. Test design note for
   any future round: the visitor affordance is only really
   exercised from an account that doesn't smell like the author.
3. **Two artifacts kept:** (a) the SPINE_IN comment catch was
   fair — the Makefile still said "assumed" though 0.49in was
   verified as the actual at publication; comment corrected
   same day. (b) The release-assets suggestion runs directly
   against the ratified no-unitary-artifacts stance — outside
   agents will keep proposing it, which argues for stating the
   stance where agents look first (the future site's llms.txt
   and, perhaps, one line in AGENTS.md's "What is welcome").

Surface scorecard after three tests: web Claude Code = full
product view, first try (04). Chat surface = advice, not
artifact (03: plumbing; 05: orientation + fidelity-purism).
The stack ranking matches the surfaces' designed affordances;
the repo's guidance can narrow but not erase the gap.
