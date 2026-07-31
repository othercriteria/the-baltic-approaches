# External test 03 — the affordance test (claude.ai chat, 2026-07-31)

*Registered by session 3d8e73ea per the external-reads convention.
Source: DK-shared snapshot
claude.ai/share/02e748c7-9444-4fa5-9de7-5dbf9b73779b, recovered
verbatim via the public snapshot API (the share page itself is a
JS shell). Snapshot title: "Converting GitHub repository to screen-friendly PDF". Code-execution blocks render as
"not supported" placeholders in the snapshot; the assistant's
prose between them is complete. Design of the test: DK asked a
fresh, unbriefed Claude to exercise the license's central grant —
agent-mediated personal transformation — hours after
ratification. It mostly failed, on plumbing; the failure map is
the value. Audit and resulting adjustments at foot.*


---

**DK** (2026-07-31T14:24:01):

Give me the screen-friendly PDF of https://github.com/othercriteria/the-baltic-approaches (for my personal use, of course!) (or even more correctly as a test of this affordance!).

---

**Assistant (Opus 5, claude.ai chat + code-execution container)** (2026-07-31T14:26:17):


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Pandoc and XeLaTeX are both here, so the real build path is at least plausible. Let me pull the build machinery.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Toolchain is a good match — pandoc 3.1.3, XeLaTeX, qpdf, and TeX Gyre Pagella (the book's actual body face) are all present. Now let me see if I can pull raw file contents.
```
This block is not supported on your current device yet.
```

Raw-path construction is blocked — I can only fetch URLs that actually appear in prior results. Let me probe the drafts directory to see what's reachable.
```
This block is not supported on your current device yet.
```

/tree/ paths are robots-blocked, and no `drafts/` URLs appeared in anything I've fetched. Let me try one more route.
```
This block is not supported on your current device yet.
```

Short answer: this affordance can't do it, and the failure is interesting enough to be worth reporting precisely.

**What's actually here.** The container is a surprisingly good match for your toolchain — pandoc 3.1.3, XeLaTeX, qpdf, pdfinfo/pdftoppm, and TeX Gyre Pagella itself, so `BODYFACE` would resolve correctly rather than silently falling back. Missing: `pdfjam` and headless Chromium.

**Where it breaks.** Bash has no network, so no clone, no curl. That leaves `web_fetch`, which hit three walls:

- `/tree/` paths are robots-disallowed, so I can't enumerate `drafts/`.
- Raw URLs can't be constructed — I can only fetch URLs that literally appeared in a prior result, and `.../raw/refs/heads/main/apparatus/chapters.lua` was rejected on exactly that basis. The Makefile's own raw link came through because GitHub rendered it on the blob page.
- No `drafts/*.md` URL appears on any page I can reach, and the repo isn't search-indexed.

So I got the Makefile in full and learned what `pdf-screen` wants, but the manuscript is simply unreachable. Even the fallback of walking blob pages one file at a time would be a bad build: GitHub renders `.md` blobs rather than serving source, which would eat the `:::` div fences that `scenebreak.lua` keys on — asterisms wrong throughout a 22-chapter novel is worse than no PDF.

**And even with the sources**, `pdf-screen` wouldn't complete as written. It depends on `maps` (headless Chromium for `svg2pdf.py`), `cover` and `cover-wrap` (`cover-art.py` recomposing the museum raster — network again), `pdfjam` for the trim-to-5.5×8.5 step, and `git rev-parse` for the `DRAFT_STAMP`. What I could produce is `screen-interior.pdf` without plates or the cover/back-panel bookends — which is the SCREEN_OPTS composition but not the one-file product view you defined.

**What would work.** If you upload a zip of `drafts/` + `apparatus/` (and `build/maps/*.pdf` if you want the plates injected), I can run the pandoc SCREEN_OPTS step here verbatim and hand back the interior. `pdfjam` is replaceable — it's a `pdfpages` wrapper, so the trim-and-clip is a ten-line XeLaTeX shim — meaning if you include the built cover and wrap PDFs, I can reproduce the full qpdf assembly including the bookends. The only thing genuinely out of reach is regenerating plates and cover art from source.

Your license anticipated this case explicitly — personal use, agent-mediated included — so the wink was unnecessary. The obstacle was plumbing, not permission.

---

**DK** (2026-07-31T14:28:12):

Cool. As you might likely be guessing, I'm going to run this conversation by an agent working on the project. You might as well identify what model you are and given any additional content that will help debug this use case.

---

**Assistant (Opus 5, claude.ai chat + code-execution container)** (2026-07-31T14:30:24):

Let me gather an actual environment fingerprint rather than describe it from memory, and verify the two claims I made about workarounds.
```
This block is not supported on your current device yet.
```

Now let me actually exercise the `SCREEN_OPTS` composition against synthetic chapters, to check pandoc-version compatibility independent of the missing sources.
```
This block is not supported on your current device yet.
```

A real finding — `lmodern.sty` is absent, which kills any pandoc PDF build here before it reaches the sources. Let me confirm and work around it.
```
This block is not supported on your current device yet.
```

The stub works — 396×612pt is exactly 5.5×8.5in, and metadata survives. Now the `pdfjam` replacement and the full qpdf assembly, end-to-end with synthetic cover/wrap stand-ins.
```
This block is not supported on your current device yet.
```

Model: **Claude Opus 5**, running in the claude.ai chat surface with a code-execution container — not Claude Code, which matters because the affordance sets differ (no repo checkout, no persistent workspace, network only through `web_fetch`). Two caveats worth passing along: if you'd selected Claude Fable 5, safeguards routing can silently redirect a session to Opus 5, and I can't tell from the inside which happened. And my knowledge cutoff is end of May 2026, so the repo — published July 2026 — is entirely outside training data. Everything I've said about it came from the two fetches in this conversation.

## Environment fingerprint

```
pandoc 3.1.3 (+lua)          xelatex  TeX Live 2023/Debian (XeTeX 0.999995)
qpdf 11.9.0                  poppler  24.02.0 (pdfinfo, pdftoppm)
python 3.12.3                PIL OK; lxml OK; cairosvg/svglib MISSING
TEXMFDIST /usr/share/texlive/texmf-dist
present: pdfpages geometry fontspec unicode-math microtype tikz pdflscape
MISSING: lmodern.sty, pdfjam, headless Chromium
fonts:   TeX Gyre Pagella (Regular/Italic/Bold/BoldItalic) — full set
         Latin Modern: 0 files in texmf (fc-list shows LM Roman via system pkg only)
```

## The blocker worth knowing about

`lmodern.sty` is absent, and pandoc's default LaTeX template loads it unconditionally. **Every pandoc PDF build in this sandbox dies at `l.21 \ifPDFTeX` before it ever reaches your sources** — so this failure is upstream of the missing-manuscript problem and would have bitten even with a full checkout. Stub fixes it:

```sh
mkdir -p texin && printf '\\ProvidesPackage{lmodern}[stub]\n' > texin/lmodern.sty
TEXINPUTS=./texin: pandoc ...
```

Safe here only because `-V mainfont` routes through fontspec under XeLaTeX; under pdflatex the stub would silently drop you to Computer Modern.

## Verified working

With that stub, your `SCREEN_OPTS` string runs clean under pandoc 3.1.3 — `--top-level-division=chapter`, `-V secnumdepth=0`, the doubled `-V classoption` (accumulates to a list correctly), and the geometry vars all behave. Output measured **396×612pt = exactly 5.5×8.5in**, and `title-meta`/`author-meta` land in the catalog with no `\maketitle` emitted.

`pdfjam` is fully replaceable — it's a `pdfpages` wrapper. This reproduces both trims, verified at 396×612 for the symmetric cover and the asymmetric `5.625+SPINE_IN` back panel:

```latex
\documentclass{article}
\usepackage[papersize={5.5in,8.5in},margin=0pt]{geometry}
\usepackage{pdfpages}
\begin{document}
\includepdf[pages=1,trim=<SPEC>,clip,fitpaper=false,
            width=\paperwidth,height=\paperheight]{<IN>}
\end{document}
```

Your `qpdf --pages` assembly then runs verbatim, and interior metadata survives as primary. I ran the whole chain end-to-end on synthetic chapters plus stand-in cover art: 4 interior + cover + back = 6 pages, uniform trim size. **The assembly half of `pdf-screen` is sound in this environment; only plate and cover *generation* is out of reach.**

## Reachability map, with exact errors

| Target | Result |
|---|---|
| repo root, `/blob/main/Makefile` | OK — full source, GitHub renders raw text for non-`.md` |
| `/tree/main/drafts` | `ROBOTS_DISALLOWED` |
| constructed `/raw/refs/heads/main/apparatus/chapters.lua` | `PERMISSIONS_ERROR: This URL was not in any prior search or fetch result` |
| `web_search` for repo contents | not indexed (0 stars, days old) |
| container egress | `HTTP Error 403: Forbidden` — proxy denial, not absence of a stack |

That last row may matter to whoever configures this: the proxy 403s rather than failing to connect, so naive retry logic will look like a transient network fault.

Untested, because I never got the files: `scenebreak.lua`, `chapters.lua`, `latex-header.tex`, and the front/back matter — including whether `front-matter.md`'s plate injection degrades gracefully or hard-fails when `build/maps/*.pdf` is absent. That's the one question I'd most want answered before anyone tries an agent-mediated build again, since it determines whether a no-Chromium environment can produce a plateless interior at all.

If it's useful, `AGENTS.md` currently assumes an agent with a checkout. A short section on the sandboxed case — "no network, no clone: here is the minimum upload set for `screen-interior.pdf`, here is the lmodern stub, here is the pdfjam shim" — would have turned this session from a failed build into a completed one.
---

## Audit (session 3d8e73ea)

**What failed, precisely (claude.ai chat surface):**
1. Container bash has no network — no clone, no curl.
2. `web_fetch` cannot enumerate the repo: `/tree/` paths are
   robots-disallowed, and raw URLs may only be fetched if they
   literally appeared in previously-fetched content. No
   `drafts/*.md` URL appears on any reachable page, so the
   manuscript was unreachable even though the Makefile (linked
   from a rendered blob page) came through in full.
3. Blob-page fallback would corrupt sources: GitHub renders
   `.md`, eating the `:::` scene-break fences `scenebreak.lua`
   keys on.
4. Even with sources, full `pdf-screen` needs headless Chromium
   (plates), cover generation, `pdfjam`, and `git rev-parse` —
   absent there. The assistant verified the ASSEMBLY half works
   (pandoc SCREEN_OPTS clean on synthetic chapters at exactly
   396x612pt; pdfjam replaceable by a ten-line pdfpages shim;
   qpdf chain verbatim) and found `lmodern.sty` missing — which
   kills ANY pandoc PDF build in that sandbox before sources
   matter (stub workaround documented in the transcript).

**Incidental facts worth keeping:** the responding model was
Opus 5 and noted that a Fable 5 selection can be silently
safeguards-routed to Opus 5, indistinguishable from inside; its
cutoff (May 2026) predates publication, so the repo was entirely
outside training — everything it knew came from two fetches. Its
closing line belongs in the record: "The obstacle was plumbing,
not permission" — the license's first field test, hours after
ratification, held on the permission side.

**Adjustments made in response (same day):**
1. AGENTS.md gained a SOURCE MANIFEST: absolute
   raw.githubusercontent.com URLs, pinned to the tag of record,
   for every chapter and the apparatus text — so a fetch-only
   agent has every URL it needs the moment it reads AGENTS.md
   (defeating the no-constructed-URLs rule), plus a fidelity
   warning (raw, never rendered blob) and minimal-build guidance
   (interior-only path; plates/cover optional to reading; deps
   without nix).
2. SUPERSEDED same day by the better fix, DK-directed:
   **Chrome-free assembly** (see planning/map-spec.md, converter
   switch entry). The plates now build with rsvg-convert; pdfjam
   and pillow are declared in the flake; the full `make
   pdf-screen` runs hermetically in `nix develop` and via plain
   apt packages in sandboxes. The screen-lite/committed-plates
   proposals are moot. One correction to this audit: the
   responder guessed cover generation needs network — it does
   not; the museum source raster is committed in
   apparatus/cover-art/, and `make cover` is fully local.

**Prediction for the web Claude Code re-test:** clone and
enumeration will succeed (real checkout, real git); the risk
moves to toolchain — no nix in that sandbox, so the build needs
apt-level TeX (fonts-texgyre, texlive-xetex) and pandoc, and
plates/cover still need Chromium. The manifest + minimal-build
notes in AGENTS.md are written to make that path legible.
