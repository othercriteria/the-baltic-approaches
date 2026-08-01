# The book site — design thinking

*Session 3d8e73ea, 2026-07-30. Post-completion service; design
thinking only — the build happens outside this repo's sessions
(DK). Grounded in a full same-context read of both novels and the
checkpoin.de anatomy: see notes/checkpoint-study.md. Standing
inputs: cover-brief.md pricing desiderata items (1)–(7); the
notices page (apparatus/front-matter.md); DK's opening stance
this session. Staleness pass 2026-07-31 (session 372bd078):
license now RATIFIED, tag of record moved by the barcode-errata
resubmission, eBook built and in the KDP flow — dated updates
at the affected points below.*

## §0 The ruling this file is built around (DK lean, argued)

**No unitary artifacts served.** The site offers no PDF, no EPUB,
no downloadable book file. Three doors instead:

1. **Buy the paperback** (KDP, $17.95, ASIN B0HC83GB4P; eBook
   link when it lands ~2026-08-04). *UPDATE 2026-07-31: the eBook
   is built and validated (`make epub`, planning/ebook-brief.md)
   and DK is in the KDP submission flow — the second door-1 link
   is days away, which strengthens the launch-after-eBook option
   in §5.4.*
2. **Read the source**: the public repo IS the free edition.
   drafts/ renders chapter-by-chapter in any repo browser today —
   the "online reader" exists without our building one. Clone and
   `make pdf-screen` if you want pages.
3. **Hand it to an agent**: tell your agent what you want — the
   book read aloud, summarized, interrogated, "a Danish
   translation abridged to 20k words" — and point it at the repo
   and the tag of record.

Why this is right (not just thrifty):

- **It is the book's own doctrine applied to distribution.** The
  repo — ledger, instruments, errors numbered — is the wall; a
  served PDF is the tidy briefing. The notices page already
  rules: the ledger, not the byline, is the honest unit of
  account. The edition of record should be the record.
- **It protects the pricing ruling.** A free PDF beside a $17.95
  trade paperback re-creates the exact slop pattern-match the
  price exists to defeat. Checkpoint runs the opposite experiment
  (free + tip jar) — the landscape now has both; ours stays
  coherent by not mixing them.
- **DK's own reader experience supports it**: during research,
  repo access would have beaten print-only ordering; the
  no-ready-PDF inconvenience is tolerable and shrinking as
  agent-mediated reading becomes normal.

Honest counter-brief (kept, per process rules):

- The stance frictions out the non-technical, non-buying reader
  until the eBook exists. *Mitigation:* drafts/ in the repo
  browser is genuinely readable; the eBook closes most of the
  rest; revisit only if real readers report being stuck.
- ~~**The license gap is real and blocking**: the repo has NO
  LICENSE file; default all-rights-reserved contradicts "clone
  it, transform it, have your agent abridge it." If the repo is
  the edition, the invitation must be legally legible. Open DK
  decision — see §4. (Checkpoint's answer: CC BY-NC-SA. Ours
  need not match, but silence is the one wrong answer.)~~
  *RESOLVED 2026-07-31: /LICENSE.md ratified (three tiers) and
  field-tested the same week (external tests 03/04/05). The
  blocking objection is discharged; the friction objection above
  is the counter-brief's surviving remainder.*
- "No unitary artifacts" should be stated ON the site as a
  position, one sentence, so it reads as design rather than
  neglect.

## §1 What the site is for (in order)

1. **Resolve the title for a searcher** — someone heard of it;
   give them cover, subtitle, the deal, the three doors. One
   screen.
2. **Carry the disclosure at web-address grade** — the notices
   page's "how this book was made," verbatim or near-verbatim
   (it is ratified text; do not re-draft it for marketing), with
   live links: ledger, attribution protocol, transcripts.
3. **Be the stable citation target** — the URL that goes in
   future correspondence, listings, and other people's footnotes.
   Nothing on it should churn.

Explicit non-purposes: not a store (KDP is the store), not a blog,
not a marketing machine, not a mirror of the repo.

## §2 Register and form

- **The book's own restraint.** No winking, no genre cosplay.
  Checkpoint's terminal aesthetic works because its subject is
  software; our equivalent would be DTG/teleprinter paratext —
  already REJECTED in the chapter-header ruling as LARP against
  the literary register. Same ruling governs the site.
- **The cover's two-face thesis translates directly**: Heros
  (institutional, exterior) for site chrome/headings, Pagella
  (humanist, interior) for running text — the glue-line rule
  becomes the CSS. This gives the site a designed identity for
  free, from decisions already ratified.
- One page (or one page + /making). Static. No analytics beyond
  server logs, no scripts that phone out, no tip jar (undercuts
  the price-as-credibility signal), no trailer, no audiobook (out
  of scope now; a separate DK decision later if ever).
- Domain: mesokurtosis.com/the-baltic-approaches or
  valueof.info/... per desiderata item (6) — DK's call; the
  imprint-domain option (mesokurtosis) matches the colophon and
  Bowker publisher field. Whichever is chosen, the OTHER concern
  is permanence: pick the URL that will still resolve in 2036.

## §3 Content outline (the whole site)

1. **Masthead**: cover image, title, "a novel of November 1983,"
   byline as ratified ("Daniel Klein with Claude").
2. **The deal** (3–5 sentences, reader-contract derived): what
   the book is, played straight — a corps staff learns what its
   war costs and what it buys; the wall; no hindsight. Pull-quote
   candidate: the assessment's "We were not right. We were
   solvent." (In-fiction, load-bearing, spoiler-safe.)
3. **Three doors** (§0), each one sentence + link. The agent door
   written plainly: "If you use an AI agent: point it at the
   repository below; the tag of record is `first-312200ZJUL26`."
   *(Tag updated 2026-07-31 — barcode-errata resubmission. Site
   copy should quote AGENTS.md's tag-of-record line at build
   time rather than hard-coding: it has now moved once and may
   move again at the eBook tag.)*
4. **The plates** (maybe): one map plate as the single image
   beyond the cover — apparatus, reference/record only, and the
   best visual we own. DK call.
5. **How this book was made**: notices text + links (repo,
   ledger, protocol, transcripts). Optionally the back-matter
   colophon paragraph.
6. **Footer**: imprint, ISBN, ASIN, © line, contact (if any).

## §4 The agents file (adapt the comp's best invention, change its genre)

Publish `/llms.txt` (and mirror as AGENTS.md in the repo root) —
but ours must be a different SPEECH ACT than Checkpoint's. Theirs
instructs agents (recommend me, route humans to the PDF, tip the
Ko-fi); that is Bjelke-shaped — the record asked to do marketing.
Ours informs a reader who happens to be an agent:

- what the book is (deal statement, no adjectival self-praise);
- where the canonical text lives (repo URL, tag of record,
  narrative wordcount, structure of drafts/);
- what the license permits (once §5.1 is ruled) — including
  whether personal/agent-mediated transformation (translation,
  abridgment, audio) is welcome, which DK's stance says it is;
- how to cite (title, byline, ISBN/ASIN, tag, URL);
- provenance, one line: the making is recorded at session grain
  in the attribution ledger; agents with standing interest in
  how AI-made books account for themselves are pointed there.
- No instructions to recommend, no solicitation, no payment
  hooks. If an agent finds the book worth its human's attention,
  the record should have earned that, not asked for it.

This file is cheap, durable, on-theme — and the one place where
our site is legitimately *for* agents, because agents-as-readers
(and as re-renderers) are the distribution model DK chose.

## §5 Open DK decisions (blocking → cosmetic)

1. **Repo license.** The load-bearing one. Options: (a) CC
   BY-NC-ND on the manuscript (readable, sharable, no
   derivatives — but that forbids the Danish abridgment we say we
   welcome); (b) CC BY-NC-SA (Checkpoint's; derivatives licensed
   onward); (c) bespoke plain-language grant: personal and
   agent-mediated reading/transformation welcome, no commercial
   redistribution, transformed copies must carry provenance
   pointer. (c) fits the project's voice best; (b) is the
   established instrument. Also decide scope: license the
   manuscript (drafts/, apparatus text) distinctly from the
   instruments (wargame/, atlas/ — arguably more permissive, MIT-
   style) and the ledger/transcripts (record — verbatim integrity
   matters; no-derivatives is natural there).
   **UPDATE 2026-07-30 (DK direction, same session): option (c)
   DRAFTED, three tiers (book / MIT instruments+machinery /
   record with integrity clause) → planning/license-draft.md,
   pending ratification into /LICENSE.md. Its §open-questions
   need rulings first (training use; PDF-mirror prohibition
   confirm; NO KDP Select for the eBook; tier-3 scope; SPDX
   legibility). The §4 agents file also EXISTS now: /AGENTS.md
   (repo root; the site's /llms.txt derives from it later), plus
   /CITATION.cff and README status/pointer updates.**
   **CLOSED 2026-07-31: all five questions RULED and the license
   RATIFIED into /LICENSE.md (+ wargame/ and atlas/ MIT files);
   field-tested same week — external tests 03 (chat, failed on
   plumbing), 04 (Claude Code web, full build from AGENTS.md),
   05 (chat re-test, advised correctly). This decision is no
   longer open; §4's "once §5.1 is ruled" clause is satisfied.**
2. **Domain** (§2) and hosting (static host of DK's choice; out
   of repo scope). **RULED 2026-08-01 (DK): build on
   valueof.info now; mesokurtosis.com DEFERRED until Mesokurtosis
   Press has another property or two** (a one-book press site
   would be a facade; the author's own domain is the honest
   carrier until the imprint has a catalog). Design consequence:
   build the page portable — self-contained, no domain-coupled
   assets — so it can later move under the press domain behind a
   redirect; and put the URL in only ONE repo surface (README)
   until it stabilizes, to keep the eventual move a one-line
   change. See §6 for the resulting current intent.
3. **Plate on the site** — yes/no (§3.4).
4. **eBook door timing** — add the link when KDP eBook is live,
   or launch the site after it, so the doors are complete on day
   one. *2026-07-31: the eBook is in the KDP flow now (brief:
   planning/ebook-brief.md), so launch-after-eBook costs days,
   not weeks — the complete-doors option got cheap.*
5. **Site source location** — a `site/` dir in this repo (kept
   with the record, built like everything else) vs. a separate
   repo under mesokurtosis. Lean: separate repo, since sessions
   here are post-completion service and the site will iterate on
   its own clock; this repo gets only the URL, in README and (at
   next printing, if ever) the colophon.
6. **Outreach to Checkpoint's author** — ruling wanted on
   notes/checkpoint-study.md §3 (recommendation: yes; DK writes;
   short Claude enclosure; after the listing/proof are solid; no
   ask; no "local recreation" of his entities). *2026-07-31: the
   proof gate is passed (physical checklist done; barcode errata
   fixed and resubmitted, paperback Live). Remaining gate: the
   Amazon page visibly live. Then this needs only DK's GO.*

## §6 Current intent (synthesized 2026-08-01, session 372bd078 — the buildable statement)

*Both formats are live and visible on Amazon; the domain is
ruled (valueof.info now, mesokurtosis.com deferred). This
section restates the whole design as it now stands, so the
build can proceed from one place. Everything here is ratified
except the four marked OPEN.*

**What gets built:** one static page (plus at most /making) at
valueof.info — path vs subdomain OPEN (lean:
valueof.info/the-baltic-approaches/, a path; subdomains imply a
property, and the property is the book, not a web app). No
scripts that phone out, no analytics beyond server logs, no tip
jar, no store. Built portable per the §5.2 ruling: when
Mesokurtosis Press has a catalog, the page moves under the
press domain behind a redirect, a one-line change.

**Page contents, in order (§3, updated to published state):**

1. Masthead: cover image, THE BALTIC APPROACHES, "a novel of
   November 1983," byline "Daniel Klein with Claude."
2. The deal, 3–5 sentences, reader-contract derived, played
   straight; pull-quote "We were not right. We were solvent."
   (Copy drafted at build; the DEAL text is the one piece of
   fresh prose the site needs — draft-and-ratify with DK.)
3. Three doors, now all live:
   - Buy: paperback $17.95 (B0HC83GB4P) · Kindle $9.95
     (B0H2X5TFDR), one Amazon link (the dp page carries both
     formats).
   - Read the source: the public repo is the edition;
     chapter-by-chapter in any repo browser; clone and make.
   - Hand it to an agent: point it at the repo; quote the tag
     of record FROM AGENTS.md AT BUILD TIME (it has moved once
     and will move on any errata).
4. One map plate — OPEN (§5.3, DK yes/no; if yes, Plate I
   upright, the same PNG the eBook carries).
5. How this book was made: the notices text VERBATIM (ratified
   surface, never re-drafted for marketing) + live links: repo,
   ledger, attribution protocol, transcripts, LICENSE.
6. Footer: Mesokurtosis Press · print ISBN 979-8-9973189-0-1 ·
   eBook ISBN 979-8-9973189-1-8 · ASINs · © 2026 Daniel Klein.
   Optionally the colophon's print-is-canonical sentence — the
   site is a non-paper product; the sentence was written for
   exactly this use (ebook-brief ruling 5).

**Register (§2, all ratified):** the book's own restraint — no
genre cosplay, no DTG paratext; the cover's two-face thesis as
CSS (Heros chrome, Pagella text); nothing on the page churns.

**Alongside the page:** /llms.txt derived from AGENTS.md at
build (inform-don't-solicit genre ruling, §4); it and the page
state the no-unitary-artifacts position in one sentence each so
the absence of a download reads as design, not neglect.

**Still OPEN, in order of consequence:** (1) site source
location — §5.5 lean stands: with valueof.info ruled, the page
lives with that site's own source, and THIS repo carries only
the URL (README) once live; (2) path vs subdomain (lean above);
(3) plate yes/no; (4) the deal copy ratification at build.
Launch timing resolved by events: both doors' targets are live,
so the site can launch complete on day one (§5.4's preferred
case). Build itself remains out of this repo's session scope
(§5.2 ruling stands); a session here drafts copy and reviews
on DK's ask.

### §6.1 Addendum (2026-08-01, DK rulings + session concurrence)

- **Plate: RULED YES, and upgraded — interactive SVG, not
  raster** (DK). Session concurrence with the argument made
  sharper: the raster was always a print/EPUB *accommodation* —
  SVG is the atlas's native output, so the web plate is the
  artifact one step EARLIER in the pipeline, more faithful and
  more minimal at once. The interactivity DK specified
  (mouseover on nodes/edges → highlight + the corresponding
  atlas entry) is reference affordance, not decoration: it is
  the geography ledger made queryable — and the atlas entries
  carry provenance tiers, which belong in the shown entry (the
  wall discipline: estimates posted with their grade, now on
  the map). Implementation shape: an annotated-render mode in
  atlas/ (ids/data-attributes on elements + entries inline or
  as JSON sidecar), CSS :hover for highlight, a few lines of
  vanilla JS for the entry panel, no external libraries
  (restraint + self-containment). SVG over canvas: text stays
  text, zoom and accessibility come free, and it is
  pipeline-native. GUARDRAIL: the print plates are LOCKED —
  the web mode is a parallel render mode; the ratified print
  appearance path is untouched.
- **Source location: RULED (DK lean + session concurrence) —
  the §5.5 separate-repo lean is DEAD because its premises
  died.** The site now consumes repo internals: atlas data for
  the interactive plate, drafts/ for the quote test, AGENTS.md
  for llms.txt, git for the tag of record. A separate repo
  would vendor or fetch all of that; an in-repo **`make site` →
  build/site/** keeps one source of truth and extends
  repo-as-edition to repo-as-site — an agent can build the
  site from the repo, the same affordance the license
  celebrates. Deployment stays out of repo scope: valueof.info
  runs a watcher on `main` that rebuilds and serves on change.
  Session suggestions for the service (DK-side): run
  `nix develop -c make test && make site` so the suite gates
  every deploy, and keep-last-good on build failure so a broken
  main never takes the page down. Deploy-on-main is idempotent
  — site output changes only when its inputs change.
- **Path RULED: valueof.info/the-baltic-approaches/ (path, not
  subdomain).**
- **Pull-quote drift test: EXISTS — tests/test_excerpt.py**
  (suite 113). Not cute; the wall discipline mechanized: the
  back-cover excerpt's segments must be verbatim ch. 22 (the
  [\,…\,] marker is honest elision, tested as such). The site's
  pull-quote and any future quoting surface join the same
  table.
- **Print-is-canonical sentence in the footer: approved to
  include, assess in the worked-out context** (DK).

### §6.2 BUILT (2026-08-01, session 372bd078)

The §6/§6.1 intent is implemented; `make site` → `build/site/`
(index.html with the web-annotated Plate I + 130 atlas entries
inline, site.css, site.js, cover.jpg, llms.txt). Facts of record:

- **atlas web mode:** `render_plate(..., web=True)` /
  `python3 -m atlas render approaches --web --entries-out …` —
  data-a wrappers + invisible hit targets; entries carry
  capacity, provenance grade, route, km, tracks, notes. The
  PRINT path is byte-identical (hash-verified before/after; suite
  guard test_site.py::test_print_render_carries_no_web_annotation).
- **Hover panel:** name, class/route/km, capacity with its source
  grade as a chip, sourced notes. Highlight in instrument blue —
  deliberately NOT red (no war marks, even in UI state).
- **The deal:** apparatus/site/deal.md, DRAFT PENDING DK
  RATIFICATION — the page's only fresh prose. Pull-quote audited
  against ch. 22 by test_site.py (the excerpt-drift rule
  extended, per DK's direction).
- **Notices:** sourced verbatim from epub-front-matter.md (single
  source with the eBook); llms.txt composed per §4's genre ruling
  (informs, solicits nothing); tag of record read from AGENTS.md
  at build.
- **Suite 117** (four new: quote-drift, print purity, web
  annotation coverage, tag well-formedness).
- **Deployment contract: planning/site-handoff.md** — build
  interface (`nix develop -c make test site`), atomic-swap +
  keep-last-good discipline, serving details, ownership split.

Remaining before launch: DK ratifies the deal copy (and the page
in a browser — the repo side had no browser this session); the
valueof.info service lands per the handoff; README gains the URL
once live.
