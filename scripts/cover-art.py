#!/usr/bin/env python3
"""Recompose the cover raster for bleed geometry.

Crops apparatus/cover-art/muller-hall-of-antiquities.jpg to the
full-bleed cover aspect (5.75x8.75in) at 300dpi (1725x2625 px)
and writes build/cover/cover-art.jpg for apparatus/cover.tex to
place full-bleed. Recomposes from the museum source every build
(design pass 2 rule: never upscale a comp).
"""

from pathlib import Path

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "apparatus/cover-art/muller-hall-of-antiquities.jpg"
OUT_DIR = ROOT / "build/cover"
OUT = OUT_DIR / "cover-art.jpg"

BLEED_W_IN, BLEED_H_IN = 5.75, 8.75
DPI = 300
W, H = int(BLEED_W_IN * DPI), int(BLEED_H_IN * DPI)  # 1725x2625

im = Image.open(SRC).convert("RGB")
sw, sh = im.size
ar = W / H
# Source is taller-aspected than the cover: full height, centered width.
if sw / sh > ar:
    ch = sh
    cw = ch * ar
else:
    cw = sw
    ch = cw / ar
x0 = (sw - cw) / 2
y0 = (sh - ch) / 2
crop = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))
eff_dpi = crop.height / BLEED_H_IN
crop = crop.resize((W, H), Image.LANCZOS)

OUT_DIR.mkdir(parents=True, exist_ok=True)
crop.save(OUT, quality=95)
print(f"{OUT}  {W}x{H} @300dpi (effective source {eff_dpi:.0f}dpi)")

# --- Wrap support (cover-brief.md, wrap program items 1 and 3) ---

# Front panel for the wrap: the same recomposition minus its left
# bleed (the art meets the field at the front hinge). 0.125in @300dpi
# = 37.5px; the half-pixel rounding shifts the art 1/600in, below
# any visible threshold.
WRAP_OUT = OUT_DIR / "cover-art-wrap.jpg"
wrap = crop.crop((round(0.125 * DPI), 0, W, H))
wrap.save(WRAP_OUT, quality=95)

# Back/spine field: solid color SAMPLED from the dark floor band the
# byline sits in (x 10-90%, y 90-97% of the bleed crop) — median
# channel values, no eyeballed hex. Written as a LaTeX color def for
# apparatus/cover-wrap.tex; the RGB is recorded in build output.
band = np.asarray(
    crop.crop((int(W * 0.10), int(H * 0.90), int(W * 0.90), int(H * 0.97)))
)
r, g, b = (int(np.median(band[..., c])) for c in range(3))
(OUT_DIR / "field.tex").write_text(
    f"\\definecolor{{coverfield}}{{RGB}}{{{r},{g},{b}}}\n"
)
# Reverse-check datum (item 8): the art column that meets the field
# at the front hinge, for the proof-time comparison.
hinge_col = np.asarray(wrap)[:, 0:8, :].reshape(-1, 3)
hr, hg, hb = (int(np.median(hinge_col[:, c])) for c in range(3))
print(
    f"field sampled from floor band (x 10-90%, y 90-97%): RGB({r},{g},{b}); "
    f"art at front hinge: RGB({hr},{hg},{hb})"
)
