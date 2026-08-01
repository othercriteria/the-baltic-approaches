"""Site apparatus guards (book-site.md §6.1).

Three disciplines under test: the site's pull-quote is verbatim
ch. 22 (the drift rule of tests/test_excerpt.py, applied to the
new quoting surface); the PRINT render path stays annotation-free
(the locked plates carry no web attributes); the web mode carries
its annotations and entries.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import build_site  # noqa: E402
from test_excerpt import chapter_text, normalize  # noqa: E402


def test_deal_pull_quote_matches_ch22():
    lines = build_site.deal_quote_lines()
    assert lines, "deal.md carries no pull-quote"
    ch22 = chapter_text("22-december.md")
    for ln in lines:
        assert normalize(ln) in ch22, f"pull-quote drifted from ch. 22: {ln!r}"


def test_print_render_carries_no_web_annotation():
    from atlas.render import render_plate

    for plate in ("approaches", "neck"):
        svg, _ = render_plate(plate)
        assert "data-a" not in svg, f"print path annotated: {plate}"
        assert 'tabindex="0"' not in svg


def test_web_render_annotated_and_entries_cover_it():
    from atlas.render import render_plate, web_entries

    svg, _ = render_plate("approaches", web=True)
    keys = set(re.findall(r'data-a="([^"]+)"', svg))
    assert len(keys) > 80, "web annotation unexpectedly sparse"
    entries = web_entries()
    missing = keys - set(entries)
    assert not missing, f"annotated elements without entries: {sorted(missing)[:5]}"
    sample = entries[next(k for k in keys if k.startswith("e:"))]
    assert "provenance" in sample and "cap_t_d" in sample


def test_tag_of_record_wellformed():
    tag = build_site.read_tag()
    assert re.fullmatch(r"(first|ebook)-\d{6}Z[A-Z]{3}\d{2}", tag), tag
