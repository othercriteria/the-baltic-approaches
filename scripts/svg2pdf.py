#!/usr/bin/env python3
"""SVG -> single-page vector PDF, sized exactly to the SVG's pt box.

    python3 scripts/svg2pdf.py in.svg out.pdf

Converter choice (recorded in the map build report): this environment
has no rsvg-convert / cairosvg / inkscape / resvg. It DOES have a
headless Chromium (`google-chrome`), which rasterises nothing — it
prints the SVG to a vector PDF and, because the label face (TeX Gyre
Pagella) is on fontconfig, sets the text in the same font the book's
xelatex run uses. We wrap the SVG in an HTML page whose @page size
equals the SVG box with zero margin, so the PDF is one tight page.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "google-chrome"


def svg_size_pt(svg: str) -> tuple[float, float]:
    m = re.search(r'width="([\d.]+)pt"\s+height="([\d.]+)pt"', svg)
    if not m:
        raise SystemExit("svg2pdf: could not read width/height in pt from SVG")
    return float(m.group(1)), float(m.group(2))


def convert(svg_path: Path, pdf_path: Path) -> None:
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
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={pdf_path}",
            str(htmlf),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if not pdf_path.exists():
            sys.stderr.write(r.stderr)
            raise SystemExit(f"svg2pdf: chrome produced no PDF for {svg_path}")
    print(f"svg2pdf: {svg_path.name} -> {pdf_path} ({win:.2f}x{hin:.2f}in)")


def main(argv):
    if len(argv) != 3:
        raise SystemExit("usage: svg2pdf.py in.svg out.pdf")
    convert(Path(argv[1]), Path(argv[2]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
