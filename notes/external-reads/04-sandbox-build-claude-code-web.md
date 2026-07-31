# External test 04 — sandbox build succeeds (web Claude Code, 2026-07-31)

*Registered by session 3d8e73ea. The re-test of the affordance
that test 03 mostly-failed: DK asked web Claude Code
(claude.ai/code, ephemeral Ubuntu 24.04 sandbox, no owner-side
access) to produce the screen PDF. It SUCCEEDED, first try, from
AGENTS.md's public instructions alone. DK relayed the builder's
own wrap-up verbatim below; no full transcript was shared.*

## The builder's report (verbatim, relayed by DK)

> **What I did** (entirely from the public instructions in
> `AGENTS.md`, no owner-side access — the `holdings/` submodule
> was never needed):
>
> 1. Bare Ubuntu 24.04 sandbox, nothing installed. Took the
>    no-nix route: `apt-get install pandoc texlive-xetex
>    fonts-texgyre qpdf librsvg2-bin texlive-extra-utils
>    python3-pil python3-numpy`, plus `poppler-utils`.
> 2. `make pdf-screen` — ran clean, first try. Plates went
>    through `rsvg-convert` (no browser), cover and wrap
>    composed from the Met CC0 Müller source, `qpdf` assembled
>    cover + interior + back panel.
>
> **Result:** `build/the-baltic-approaches-screen.pdf`, 175
> pages, 5.5×8.5in, one-sided, no blank versos. Pagella/Heros
> fully embedded and subset, 3.2 MB. Notices page stamps
> `Final · 2026-07-31 · 99f420e`. 51,452 words of extracted
> text; both plates render with legible labels; contents, title
> page, chapter openings, and the back panel all proofed
> visually.
>
> **Fidelity:** `git diff first-281500ZJUL26..HEAD -- drafts
> apparatus` is empty, so the text and apparatus are identical
> to the tag of record. I built from `main` rather than the tag
> because `main` carries the Chrome-free plate path (99f420e),
> which is what makes this buildable in a sandbox without
> headless Chromium.
>
> **Two small gaps in the no-nix guidance**, not worth an issue
> but worth knowing:
>
> - `poppler-utils` is missing from the `AGENTS.md` package
>   list. `make cover` calls `pdftoppm` for the proof PNGs and
>   the 120px shelf-test thumbnail, so `pdf-screen` fails
>   without it. (`pdfinfo` is guarded by `|| true`; `pdftoppm`
>   isn't.)
> - `python3-pil`/`python3-numpy` install against the *system*
>   interpreter. If `python3` on PATH is a different build —
>   here `/usr/local/bin/python3` at 3.11 vs. the system 3.12 —
>   the apt numpy is on the path but ABI-mismatched, and
>   `scripts/cover-art.py` dies on an import error that reads
>   like a numpy source-tree problem rather than a version
>   mismatch. `pip install --ignore-installed pillow numpy` for
>   whichever interpreter `make` will actually use is the fix.
>
> Nothing was committed; `build/` is gitignored and the working
> tree is unchanged.

## Audit (session 3d8e73ea)

The tests 03→04 pair is the before/after of the Chrome-free
assembly work: same request, same day, chat surface failed on
reachability + toolchain; the Claude Code surface with a real
checkout and the revised AGENTS.md built the complete product
view — plates, cover, back panel — with zero owner intervention.
The builder independently verified tag-fidelity (empty diff to
`first-281500ZJUL26` over drafts+apparatus) and correctly chose
main for the plate path, exactly the tradeoff AGENTS.md
describes. Extracted-text count (51,452) exceeds the narrative
count (50,428) by front/back matter and running text, as
expected; not a discrepancy.

Both reported gaps folded into AGENTS.md the same day
(poppler-utils added to the apt list with the pdftoppm reason;
interpreter-mismatch trap documented with the pip fix). Next:
DK re-runs the chat-surface experiment (test 03's ground) with
the manifest + guidance now in place; expected outcome there
remains an interior-only build unless that container gains a
converter, which AGENTS.md frames as a faithful copy.
