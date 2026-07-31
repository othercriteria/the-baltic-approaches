#!/usr/bin/env python3
"""SVG -> single-page vector PDF, sized exactly to the SVG's pt box.

    python3 scripts/svg2pdf.py in.svg out.pdf

Converter chain (Chrome-free assembly, 2026-07-31; the switch and
its pixel-diff audit are in the map build record):

1. rsvg-convert (librsvg — declared in flake.nix; `librsvg2-bin`
   on Debian/Ubuntu). Vector output; plate labels (TeX Gyre
   Pagella) resolve through fontconfig exactly as xelatex's do,
   and the page box honors the SVG's pt dimensions exactly.
2. cairosvg (pip-installable), for python-only environments.
3. Headless Chromium (`google-chrome`) — the original converter,
   kept as a legacy fallback. Note it rounds the printed page box
   to whole points (e.g. 377.28pt -> 378pt), which rsvg does not;
   rsvg output is the more faithful of the two.

The atlas emits plain SVG 1.1 (paths, strokes, dashes, <text>
with font-family/size/anchor/style/letter-spacing) — deliberately
inside every converter's comfort zone.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def svg_size_pt(svg: str) -> tuple[float, float]:
    m = re.search(r'width="([\d.]+)pt"\s+height="([\d.]+)pt"', svg)
    if not m:
        raise SystemExit("svg2pdf: could not read width/height in pt from SVG")
    return float(m.group(1)), float(m.group(2))


def via_rsvg(svg_path: Path, pdf_path: Path) -> bool:
    if not shutil.which("rsvg-convert"):
        return False
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["rsvg-convert", "-f", "pdf", "-o", str(pdf_path), str(svg_path)],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if r.returncode != 0 or not pdf_path.exists():
        sys.stderr.write(r.stderr)
        return False
    return True


def via_cairosvg(svg_path: Path, pdf_path: Path) -> bool:
    try:
        import cairosvg  # type: ignore
    except ImportError:
        return False
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2pdf(url=str(svg_path), write_to=str(pdf_path))
    return pdf_path.exists()


def via_chrome(svg_path: Path, pdf_path: Path) -> bool:
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    if not chrome:
        return False
    svg = svg_path.read_text()
    wpt, hpt = svg_size_pt(svg)
    win, hin = wpt / 72.0, hpt / 72.0
    html = (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        f"@page{{size:{win:.4f}in {hin:.4f}in;margin:0}}"
        "html,body{margin:0;padding:0}svg{display:block}"
        f"</style></head><body>{svg}</body></html>"
    )
    with tempfile.TemporaryDirectory() as td:
        htmlf = Path(td) / "wrap.html"
        htmlf.write_text(html)
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            str(htmlf),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if not pdf_path.exists():
            sys.stderr.write(r.stderr)
            return False
    return True


def convert(svg_path: Path, pdf_path: Path) -> None:
    for name, fn in (
        ("rsvg-convert", via_rsvg),
        ("cairosvg", via_cairosvg),
        ("chrome", via_chrome),
    ):
        if fn(svg_path, pdf_path):
            wpt, hpt = svg_size_pt(svg_path.read_text())
            print(
                f"svg2pdf[{name}]: {svg_path.name} -> {pdf_path} "
                f"({wpt / 72.0:.2f}x{hpt / 72.0:.2f}in)"
            )
            return
    raise SystemExit(
        "svg2pdf: no converter available. Install one of: "
        "rsvg-convert (nix: librsvg; apt: librsvg2-bin), "
        "cairosvg (pip), or Chromium."
    )


def main(argv):
    if len(argv) != 3:
        raise SystemExit("usage: svg2pdf.py in.svg out.pdf")
    convert(Path(argv[1]), Path(argv[2]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
