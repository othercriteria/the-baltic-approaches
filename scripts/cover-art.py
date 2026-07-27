#!/usr/bin/env python3
"""Recompose the cover raster for bleed geometry.

Crops apparatus/cover-art/muller-hall-of-antiquities.jpg to the
full-bleed cover aspect (5.75x8.75in) at 300dpi (1725x2625 px)
and writes build/cover/cover-art.jpg for apparatus/cover.tex to
place full-bleed. Recomposes from the museum source every build
(design pass 2 rule: never upscale a comp).
"""

from pathlib import Path

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
