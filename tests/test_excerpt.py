"""Quoted-surface drift tests (DK direction 2026-08-01).

The book quotes itself in its dress: the back-cover excerpt
(apparatus/cover-wrap.tex) abridges the ch. 22 after-action
assessment. These tests fail if a quoting surface and the
canonical text drift apart. When the site target lands
(book-site.md §6), its pull-quote and any other quoting
surfaces join this table.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def chapter_text(name: str) -> str:
    return normalize((ROOT / "drafts" / name).read_text(encoding="utf-8"))


def test_back_cover_excerpt_matches_ch22():
    tex = (ROOT / "apparatus" / "cover-wrap.tex").read_text(encoding="utf-8")
    m = re.search(r"\\raggedright (.*?)\\par\}", tex, re.S)
    assert m, "excerpt block not found in cover-wrap.tex"
    # The abridgment marker [\,…\,] is honest elision, not text;
    # every segment around it must be verbatim ch. 22.
    segments = re.split(r"\[\\,…\\,\]", m.group(1))
    assert len(segments) == 2, "expected exactly one abridgment marker"
    ch22 = chapter_text("22-december.md")
    for seg in segments:
        seg = normalize(seg)
        assert seg, "empty excerpt segment"
        assert seg in ch22, f"excerpt drifted from ch. 22: {seg!r}"
