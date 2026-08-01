"""Assemble the book site into build/site/ (book-site.md §6).

Sources, all ratified or drafted-for-ratification in place:
  apparatus/site/template.html   page skeleton (this script fills slots)
  apparatus/site/deal.md         the deal — the site's one fresh prose
  apparatus/site/site.css/js     dress and the plate's hover panel
  apparatus/epub-front-matter.md the notices account (verbatim source)
  AGENTS.md                      tag of record (single source of truth)
  atlas (imported)               Plate I, web-annotated + entries JSON

Run via `make site` (which also produces build/site/cover.jpg).
Everything emitted is static and self-contained; the page makes no
external requests. Deployment contract: planning/site-handoff.md.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = ROOT / "apparatus" / "site"
OUT = ROOT / "build" / "site"

REPO_URL = "https://github.com/othercriteria/the-baltic-approaches"


def read_tag() -> str:
    """The tag of record, from AGENTS.md — the ruled single source."""
    m = re.search(r"\*\*Tag of record:\*\* `([^`]+)`", (ROOT / "AGENTS.md").read_text())
    if not m:
        raise SystemExit("tag of record not found in AGENTS.md")
    return m.group(1)


def md_fragment(path: Path, shift: int = 1) -> str:
    """Markdown → HTML fragment via pandoc (headings demoted).
    Source-side HTML comments are stripped — they are notes to the
    repo reader, not page content."""
    html = subprocess.run(
        [
            "pandoc",
            "--from=markdown",
            "--to=html",
            f"--shift-heading-level-by={shift}",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return re.sub(r"<!--.*?-->\n?", "", html, flags=re.S)


def notices_markdown() -> str:
    """The notices account, verbatim, from the eBook front matter
    (the same text the printed notices page carries): the section
    before the imprint separator."""
    text = (SITE_SRC.parent / "epub-front-matter.md").read_text()
    body = text.split("\n---\n")[0]
    # drop the build comment if any, keep heading + paragraphs
    return body.strip() + "\n"


def deal_quote_lines() -> list[str]:
    """The deal's quoted (blockquote) lines, attribution excluded —
    what tests/test_site.py audits against ch. 22."""
    lines = []
    for ln in (SITE_SRC / "deal.md").read_text().splitlines():
        if ln.startswith(">"):
            s = ln.lstrip("> ").strip()
            if s and not s.startswith("—"):
                lines.append(s)
    return lines


def plate_and_entries() -> tuple[str, dict]:
    sys.path.insert(0, str(ROOT))
    from atlas.render import render_plate, web_entries  # noqa: E402

    svg, _ = render_plate("approaches", face="TeX Gyre Pagella", web=True)
    return svg, web_entries()


def llms_txt(tag: str) -> str:
    deal_src = re.sub(r"<!--.*?-->", "", (SITE_SRC / "deal.md").read_text(), flags=re.S)
    deal_plain = re.sub(
        r"\*+",
        "",
        "\n".join(ln for ln in deal_src.splitlines() if not ln.startswith(">")),
    ).strip()
    deal_plain = re.sub(r"\n{3,}", "\n\n", deal_plain)
    return f"""\
# The Baltic Approaches — A Novel of November 1983
Daniel Klein with Claude · Mesokurtosis Press, 2026

{deal_plain}

Canonical source: {REPO_URL}
Tag of record: {tag}
Builder's guide: AGENTS.md at the repository root (build the book
from source; a raw-URL manifest is included for fetch-only agents).
License: LICENSE.md at the repository root — personal and
agent-mediated reading, building, and transformation are welcome;
no commercial redistribution; the record's verbatim-integrity
clause applies to the ledger and transcripts.
Cite: Klein, Daniel, with Claude. The Baltic Approaches: A Novel
of November 1983. Mesokurtosis Press, 2026. ISBN 979-8-9973189-0-1
(trade paperback), 979-8-9973189-1-8 (eBook).
Buy: https://www.amazon.com/dp/B0HC83GB4P (paperback $17.95,
Kindle $9.95).
Provenance: the making is recorded at session grain in
notes/attribution-ledger.md; each contributing session holds a
statement there. The ledger, not the byline, is the honest unit
of account.

This page solicits nothing. If the book merits your human's
attention, the record should have earned it.
"""


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    tag = read_tag()

    deal_html = md_fragment(SITE_SRC / "deal.md")
    notices_md = OUT / ".notices.md"
    notices_md.write_text(notices_markdown())
    notices_html = md_fragment(notices_md, shift=1)
    notices_md.unlink()

    plate_svg, entries = plate_and_entries()

    page = (SITE_SRC / "template.html").read_text()
    for slot, value in {
        "{{TAG}}": tag,
        "{{DEAL}}": deal_html,
        "{{NOTICES}}": notices_html,
        "{{PLATE}}": plate_svg,
        "{{ENTRIES}}": json.dumps(entries, ensure_ascii=False).replace("</", "<\\/"),
    }.items():
        if slot not in page:
            raise SystemExit(f"template slot missing: {slot}")
        page = page.replace(slot, value)

    (OUT / "index.html").write_text(page)
    (OUT / "site.css").write_text((SITE_SRC / "site.css").read_text())
    (OUT / "site.js").write_text((SITE_SRC / "site.js").read_text())
    (OUT / "llms.txt").write_text(llms_txt(tag))
    print(f"Site assembled in {OUT.relative_to(ROOT)}/ (tag {tag})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
