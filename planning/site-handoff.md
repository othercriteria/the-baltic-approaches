# Site deployment hand-off — the valueof.info side's contract

*2026-08-01, session 372bd078. The repo side of the site is DONE
(book-site.md §6/§6.1): `make site` assembles a complete static
page into `build/site/`. This document is the interface the
serving system builds against. It is written agnostically of that
system; where a concrete shape is suggested, it is a suggestion.*

## What is being served

One static page for the book at the ruled path:

    https://valueof.info/the-baltic-approaches/

`build/site/` after a build contains exactly:

| file | role |
|---|---|
| `index.html` | the main page (plate SVG + atlas entries inline) |
| `making/index.html` | the making subpage (full account, record links, editions) |
| `site.css` | dress (system font stacks; nothing fetched) |
| `site.js` | the plate's hover panel (vanilla, no requests) |
| `cover.jpg` | masthead cover, 825×1275 |
| `llms.txt` | the reader-who-is-an-agent file |

*(Correction 2026-08-01: `making/index.html` was missing from this
table — it landed with the subpage split after the table was
written. A deploy-side completeness check built from this table
should include it.)*

All internal references are relative (`./…`), so the directory is
mountable at any path — the page is portable to a future
mesokurtosis.com home behind a redirect (the §5.2 ruling).

## Build interface

From a checkout of `othercriteria/the-baltic-approaches`, branch
`main`:

    nix develop -c make test site

- `nix develop` is the supported environment (the repo flake
  carries every build dependency: pandoc, TeX Live, poppler,
  librsvg, python, and — since 2026-08-01 — the TeX Gyre fonts,
  with `FONTCONFIG_FILE` pinned to the declared set so a headless
  host builds identically; the deploy sandbox's finding, absorbed
  upstream with a rendered-output byte-identity check). Transcript
  LFS objects are not needed for the site:
  `GIT_LFS_SKIP_SMUDGE=1` clones are fine.
- `make test` is the deploy gate (117 tests; includes the
  quote-drift and plate-annotation guards). **A failing suite must
  not deploy.**
- `make site` writes `build/site/` (it renders the cover via
  xelatex on the way; first build takes ~a minute, warm rebuilds
  are seconds).

The build is deterministic: no timestamps or commit hashes are
stamped into the output, and the tag of record is read from
AGENTS.md text, not from git. Identical inputs → identical output,
so "deploy only if the output differs" is a valid optimization and
double-builds are harmless.

## Update discipline

- **Trigger:** new commits on `main` (poll or webhook — either is
  fine; the page has no freshness requirement tighter than "soon
  after an errata lands").
- **Sequence:** fetch → `nix develop -c make test site` → on
  success, atomically swap `build/site/` into the docroot (build
  into a staging dir, then rename/rsync). On ANY failure, keep
  serving the last good build — a broken `main` must never take
  the page down.
- Most commits on `main` are record-keeping and will rebuild to
  byte-identical output; that is expected and fine.

## Serving details

- UTF-8 everywhere (`charset=utf-8` on text/html, text/plain,
  text/css, application/javascript).
- `llms.txt` is served at the book path
  (`/the-baltic-approaches/llms.txt`). The domain root's
  `/llms.txt` is the domain's own file, outside this contract — a
  pointer line there to the book path is welcome but optional.
- No server-side execution of any kind. If a CSP is wanted:
  `default-src 'none'; img-src 'self'; style-src 'self';
  script-src 'self'` passes — the page's inline JSON rides in a
  `type="application/json"` data block, which is not executable
  content.
- Caching: default ETag behavior is fine; content changes only on
  errata-grade commits.

## Verification after deploy

1. The page renders; the masthead shows the cover; the plate
   responds to hover/tap (highlight + atlas entry in the panel).
2. The tag shown in door 3 matches AGENTS.md's "Tag of record" on
   `main` — if they differ, the deploy is stale.
3. `llms.txt` resolves at the book path.

## Who owns what

- **This repo:** page content, design, atlas data, the build, the
  tests. Content changes follow the project's attribution protocol
  (post-completion service; fresh prose is DK-ratified).
- **The serving system:** hosting, TLS, the watch-build-swap
  service, domain-root files, redirects (including the eventual
  mesokurtosis.com move).
- **Not served:** book files (PDF/EPUB). The absence is a ruled
  position (book-site.md §0) stated on the page itself; do not
  "fix" it at the server layer.

## Suggested concrete shape (nonbinding)

A systemd timer (or webhook-triggered unit) on the serving host:
clone/fetch the repo to a working dir, run the gate+build in
`nix develop`, rsync `build/site/` → the vhost's
`/the-baltic-approaches/` docroot on success. The nginx-vhost +
module-per-property pattern already in use fits; the book is a
path under the existing `valueof.info` vhost, not a new service.
