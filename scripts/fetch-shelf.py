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
    # Wargaming baseline, not period doctrine (rules PDF publicly
    # hosted by the retailer; the game itself is on the purchase list)
    (
        "littoral-commander-baltic-rules.pdf",
        "https://gamers-hq.de/media/pdf/9a/da/c0/Booklet_-_Rules_LCBaltic2-3-freigeschaltet.pdf",
        "68f5dcf64b79700531e2d736949800662e8eedad7d6ed86f8400812a63a05e9a",
    ),
    # Batch 2 (2026-07-20, post-bulk-survey): planning factors, legacy
    # doctrine, radio procedure, the 1981 concept pamphlet. Hashes
    # pinned after first verified fetch.
    (
        "fm-101-10-1-vol1-planning-factors-1987.pdf",
        "https://archive.org/download/FM101-10-11/FM101-10-11.pdf",
        "f77d1d449a00fa45dec71bece2e3eeb5297f0e76354056c79d552e3956d24ed1",
    ),
    (
        "fm-101-10-1-vol2-planning-factors-1987.pdf",
        "https://archive.org/download/FM101-10-12/FM101-10-12.pdf",
        "8f12d55cdd1109657167e7ecb480e57935cecf2b59bc195893a78144a22c21cb",
    ),
    (
        "fm-24-18-single-channel-radio-1987.pdf",
        "https://www.bits.de/NRANEU/others/amd-us-archive/FM24-18(87).pdf",
        "a78790c3eb5bbd9d626740d9618e8217f2dbaef01c2a15c5789adac666fc3710",
    ),
    (
        "fm-100-5-operations-1976.pdf",
        "https://cgsc.contentdm.oclc.org/digital/api/collection/p4013coll9/id/972/download",
        "317bed0e400551e42d734f2ee91d0a2ec6dd9bc3de3b7a146149c86a1c5eab83",
    ),
    # 1996 edition (bits.de) — post-setting; for our construct
    # reference only, the 1990/period editions stay on the queue
    (
        "fm-71-100-division-operations-1996.pdf",
        "https://www.bits.de/NRANEU/others/amd-us-archive/fm71_100(96).pdf",
        "5d56a1669b82988a8a374bed3c62ded094f8d4067560522c80b753cc78411d92",
    ),
    (
        "tradoc-pam-525-5-airland-battle-1981.pdf",
        "https://cgsc.contentdm.oclc.org/digital/api/collection/p4013coll9/id/656/download",
        "d58f0b5b1e5ccf86e80dfbda7a5b0262d53967f1abad8738d9c41637ec7cf2ad",
    ),
    # Leavenworth Paper 16: DePuy and the 1976 FM 100-5 — the official
    # history of Active Defense's creation (companion to Romjue)
    (
        "leavenworth-paper-16-depuy-fm100-5.pdf",
        "https://archive.org/download/DTIC_ADA531279/DTIC_ADA531279.pdf",
        "f2c989be481a0f4d38e9e880e5c5e58a0a75615a949ff76c3ebfdee8748a9be1",
    ),
    # Dupuy/HERO attrition handbook (Sept 1986, DTIC unlimited
    # distribution) — DK-surfaced; the public core of the Dupuy
    # calibration bench alongside the purchased NP&W
    (
        "dupuy-hero-ground-forces-attrition-1986.pdf",
        "https://archive.org/download/DTIC_ADA278728/DTIC_ADA278728.pdf",
        "46841dc7a22259948dc1ccd7ddd7ecb3df1dccfedf2d18ccc6aeb3f6c88107f9",
    ),
    # Batch 3 (2026-07-20, LANDJUT front research pass)
    # The Balck/von Mellenthin-TRADOC consultation (BDM 1980) — the
    # documented German intellectual debt of AirLand Battle
    (
        "bdm-balck-von-mellenthin-nato-tactics-1980.pdf",
        "https://archive.org/download/DTIC_ADA097704/DTIC_ADA097704.pdf",
        "2c653afd7b7ad49b08dc928947df3cc0cc9a7892125b78dde9468e12ed7a18bf",
    ),
    # Pałka, planning of the Polish People's Army landing operation
    # (Danish isles) — Red-side primary-source scholarship
    (
        "palka-polish-landing-operation-planning.pdf",
        "https://rcin.org.pl/Content/238081/WA303_274302_A52-KH-129-EE-6_Palka.pdf",
        "040015ff3479aa53c1cf4140bd8466b1e0bf3992ffae05452504aee8793a4991",
    ),
    # Compiled Danish TO&Es 1980-89 (R Mark Davies, Fire & Fury) —
    # wargamer-grade OOB bench for the Jutland Division side; verify
    # against official sources before canon
    (
        "davies-danish-toe-1980-89.pdf",
        "https://www.fireandfury.com/orbats/modcwdanish.pdf",
        "28fc63cd2a0388ec410ceccf0d8c25bb1fc41d6f47d81c6866c1c5402ac3957b",
    ),
    # Young, Multinational Land Formations and NATO (SSI, 1997) —
    # the Corps LANDJUT case study: staff integration, command
    # arrangements, OPCON/OPCOM history
    (
        "young-multinational-land-formations-nato.pdf",
        "https://www.govinfo.gov/content/pkg/GOVPUB-D101-PURL-LPS12561/pdf/GOVPUB-D101-PURL-LPS12561.pdf",
        "1217db93c9f33f046ad53f9375f945381e19ed9d75517d0d9503d0acefb8900e",
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
