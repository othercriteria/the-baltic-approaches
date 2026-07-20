#!/usr/bin/env python3
"""Fetch the research shelf's public-domain documents.

reference/pdf/ is gitignored (large scans, all re-fetchable); this
script plus reference/shelf.md ARE the shelf's reproducibility. Add
new items here and describe them in the manifest. Idempotent: skips
files already present; verifies sha256 when pinned (pin after first
fetch by copying the printed hash into ITEMS).

Run: python3 scripts/fetch-shelf.py   (or `make shelf`)
"""

import hashlib
import subprocess
import sys
from pathlib import Path

DEST = Path(__file__).resolve().parent.parent / "reference" / "pdf"

# (filename, url, sha256-or-None)
ITEMS = [
    (
        "fm-100-5-operations-1982.pdf",
        "https://upload.wikimedia.org/wikipedia/commons/7/70/US_Army_Field_Manual_100-5,_1982.pdf",
        "b8dd3f0e653fa493573bd024dcfcbe02e8d0fe7f29479cadb1c6316e38cfb905",
    ),
    (
        "fm-100-5-operations-1986.pdf",
        "https://cgsc.contentdm.oclc.org/digital/api/collection/p4013coll9/id/893/download",
        "bce6d10808f0c82afae084bda7bbe4517df537449866b6036df6bf595fda1a0e",
    ),
    # tradoc.army.mil hosts the canonical copy but .mil doesn't resolve
    # from this network; CGSC/CARL mirror used instead.
    (
        "romjue-active-defense-to-airland-battle-1984.pdf",
        "https://cgsc.contentdm.oclc.org/digital/api/collection/p4013coll11/id/1662/download",
        "060827577e8a135aaabfb72a786ec002e0d0c00c25cf583b63bf362cdb15e65d",
    ),
    (
        "fm-100-2-1-soviet-army-operations-tactics-1984.pdf",
        "https://www.bits.de/NRANEU/others/amd-us-archive/FM%20100-2-1(84).pdf",
        "8b42a298ca15b562770b7aa026fe6aa987368487ac0c5cce295cc8dccd78380e",
    ),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    failures = 0
    for filename, url, pinned in ITEMS:
        out = DEST / filename
        if out.exists():
            print(f"have    {filename}")
        else:
            print(f"fetch   {filename}")
            r = subprocess.run(["curl", "-fsSL", "--retry", "2", "-o", str(out), url])
            if r.returncode != 0:
                print(f"FAILED  {filename}  ({url})", file=sys.stderr)
                out.unlink(missing_ok=True)
                failures += 1
                continue
        digest = sha256(out)
        if pinned and digest != pinned:
            print(f"HASH MISMATCH  {filename}: {digest}", file=sys.stderr)
            failures += 1
        else:
            print(f"        sha256 {digest}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
