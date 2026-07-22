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
    # Batch 4 (2026-07-21, fetch-queue hunt, session 71ede904).
    # CSI/Leavenworth/SASO cluster — Soviet operational art and the
    # combined-arms survey that was on the queue from Step 0
    (
        "house-toward-combined-arms-warfare-1984.pdf",
        "https://archive.org/download/DTIC_ADA528264/DTIC_ADA528264.pdf",
        "fdc57c95c1d067a5924ec130ad6adf39c7e7a21e09b9abc8c9e9849b2f6abbd6",
    ),
    # 1984 Art of War Symposium transcript (Glantz, Carlisle) — Soviet
    # offensive operational art argued by the principals; CARL-only
    (
        "glantz-1984-art-of-war-symposium-don-to-dnepr.pdf",
        "https://cgsc.contentdm.oclc.org/digital/api/collection/p4013coll8/id/4111/download",
        "83335fa8ede45ad8dfc56d6f54c63bb564db0be02954333dd07b0dab0dc5bb59",
    ),
    (
        "glantz-soviet-operational-art-tactics-1930s.pdf",
        "https://archive.org/download/DTIC_ADA232954/DTIC_ADA232954.pdf",
        "94b07300332375df51426bfed9d1e59f3dbccb4cf9f5ac307abee505ff57e09d",
    ),
    # CSI Report 11 (1986) — echeloned defense at Kursk
    (
        "glantz-soviet-defensive-tactics-kursk-csi-report-11.pdf",
        "https://archive.org/download/soviet-defensive-tactics-at-kursk-russia-july-1943-david-m-glantz-1986/Soviet_defensive_tactics_at_Kursk_russia_July_1943_-_David_M_Glantz_1986.pdf",
        "23fda93501b131e34a48ff72959ee5a3b03cf990230706c22ae3c9227ae63f90",
    ),
    # Leavenworth Papers 7+8: August Storm — front-level operational
    # art and its tactical execution (forward detachments, echelons)
    (
        "glantz-august-storm-strategic-leavenworth-paper-7.pdf",
        "https://archive.org/download/DTIC_ADA144378/DTIC_ADA144378.pdf",
        "13674a9bc02a723c4e07786b32125f0ac1dd3f5ae430f6284ba4b9de8d22a06e",
    ),
    (
        "glantz-august-storm-tactical-leavenworth-paper-8.pdf",
        "https://archive.org/download/DTIC_ADA143942/DTIC_ADA143942.pdf",
        "986c482b3ad832459149c585a9d30e8eee6bbcc0fa04a68d2d3b04faaf624e06",
    ),
    # Dupuy/QJM methodology cluster — advance rates (ORALFORE), the
    # official CAA evaluation of the HERO database (CHASE), and the
    # clearest free exposition of QJM internals (NPS thesis)
    (
        "hero-oralfore-opposed-rates-of-advance-1972.pdf",
        "https://archive.org/download/DTIC_AD0902830/DTIC_AD0902830.pdf",
        "f1e90358ced5ebb6d175019124a936faa23eb74e123b2afe44c06b7e0dc499d8",
    ),
    (
        "caa-chase-combat-history-analysis-1986.pdf",
        "https://archive.org/download/DTIC_ADA179734/DTIC_ADA179734.pdf",
        "7c9414f0a10403c637b56066da0fe15b8b9deef949521ddc174545495abad2b4",
    ),
    (
        "nps-thesis-qjm-historic-ground-combat.pdf",
        "https://archive.org/download/quantifiedjudgme00cianpdf/quantifiedjudgme00cian.pdf",
        "712fdf4fc2d8c713399e35001b1e8b056b3f7c6479e45eafb3624b566b6f2dbb",
    ),
    # Period net-assessment debate — Mearsheimer self-archived copies
    # (MIT Press copyright; author's own site; personal research use,
    # never redistribute). Posen 1984-85 and Epstein's two articles
    # have no legitimate open host — purchase/library list.
    (
        "mearsheimer-1982-why-soviets-cant-win-quickly.pdf",
        "https://www.mearsheimer.com/wp-content/uploads/2019/07/A0006.pdf",
        "18a0927b0c3da661b61f90f3e5850318b0411e20831ef6eb56ccbdb26a2cc5d8",
    ),
    (
        "mearsheimer-1988-numbers-strategy-european-balance.pdf",
        "https://www.mearsheimer.com/wp-content/uploads/2019/07/A0011.pdf",
        "f6d2ee8668330caf54922ccd62bff2c561bc1c8d1462beb33d119a7402542c79",
    ),
    (
        "mearsheimer-1989-assessing-conventional-balance-3-1-rule.pdf",
        "https://www.mearsheimer.com/wp-content/uploads/2019/07/A0013.pdf",
        "69212eca594ed77aada0ac4a2db3af9158ce93b45e8f231bfad315c6c3acbadf",
    ),
    # IS 13:4 correspondence section (52 pp) — the Epstein side of the
    # 3:1 exchange lives here in open form
    (
        "is-13-4-1989-correspondence-reassessing-net-assessment.pdf",
        "https://www.mearsheimer.com/wp-content/uploads/2019/07/A0012.pdf",
        "b98fc4f36e33790024b8d5da2ca0c1d83f8dff70c357bb8bf2b466a353eb2336",
    ),
    # Declassified WP assessments (CIA FOIA reading room via
    # archive.org mirrors; cia.gov blocks non-browser fetches from
    # here). Image-only scans, no text layer. Public domain.
    (
        "nie-11-14-85-warsaw-pact-theater-forces-1985-2000.pdf",
        "https://archive.org/download/cia-readingroom-document-0000802732/0000802732.pdf",
        "22f6da18ca6666a0957ea96371e59e3b6b595eca8246b7e4e8484c6d88c7049a",
    ),
    (
        "nie-11-14-81-warsaw-pact-forces-opposite-nato.pdf",
        "https://archive.org/download/cia-readingroom-document-0000281660/0000281660.pdf",
        "8307ded3f659684f85580085418a28f4380c0c966325cdadbae9723f0308676e",
    ),
    (
        "nie-11-14-79-warsaw-pact-forces-opposite-nato.pdf",
        "https://archive.org/download/cia-readingroom-document-0000278537/0000278537.pdf",
        "34fcab699eafc256211377a36b904536f9fa0e68ae90d842d668525f75246d25",
    ),
    # NI IIM 83-10002 — the sanitized 1983 interagency memo on WP
    # campaign employment against NATO (Baltic axis coverage)
    (
        "ni-iim-83-10002-employment-warsaw-pact-forces-against-nato.pdf",
        "https://archive.org/download/cia-readingroom-document-0000261340/0000261340.pdf",
        "70fec1a2c4c2509a0c5e6c4b4baf2e86e9a3489a81cdce81710b981ff4865222",
    ),
    # Batch 5 (2026-07-21, Baltic/LANDJUT hunt, session 71ede904).
    # PHP (ETH Zurich) — WP war-planning primary sources for the
    # Danish axis: the 1964 plan dossier and two Polish Maritime
    # Front exercise directives in facsimile (the enemy's clock)
    (
        "php-warsaw-pact-war-plans-1964-dossier.pdf",
        "https://www.files.ethz.ch/isn/108642/warplan_dossier.pdf",
        "f0241f5423dbcace69a5811f1f1d6f76f3084e9b9ebec6f4a454a336ecaa6ac6",
    ),
    (
        "php-maritime-front-directive-1961.pdf",
        "https://phpisn.ethz.ch/kms2.isn.ethz.ch/serviceengine/Files/PHP/20316/ipublicationdocument_singledocument/5bc8ce55-ee20-44c5-a30c-632f879be2b2/pl/OperationalDirective_041061.pdf",
        "7c9ce212db0d845fb73ca08425643ce25bd611c0762c7c1d18e44334a5d30c67",
    ),
    (
        "php-maritime-front-directive-1967.pdf",
        "https://phpisn.ethz.ch/kms2.isn.ethz.ch/serviceengine/Files/PHP/20318/ipublicationdocument_singledocument/61cd99c8-8388-466c-bbd5-f454fda05a53/ru/OperationalDirective_310567.pdf",
        "a970ff094f1efc0bb73a3e5b641a87fa7dc3f490709dc058c32b32a43f88a605",
    ),
    (
        "wilson-bange-soyuz75-shchit88.pdf",
        "https://www.wilsoncenter.org/sites/default/files/media/documents/publication/Bange%20Commentary.pdf",
        "506921d585e5e45fa25357b2ac56809006cab0ead09a359b167c8170cbc42550",
    ),
    # DIIS, Danmark under den kolde krig (2005): the 7-pp English
    # summary is the only English release (no full English volume
    # exists); vol 3 (1979-91) carries the WP-threat material
    (
        "diis-denmark-cold-war-english-summary.pdf",
        "https://phpisn.ethz.ch/lory1.ethz.ch/documents/Denmark_English_summary.pdf",
        "1f29a5b2446bfcb9204f364700c8e098f9c2fdcc439d13732a7bc6f58190cc03",
    ),
    (
        "diis-kk-bind1-1945-62.pdf",
        "https://pure.diis.dk/ws/files/27984/KKBind1.pdf",
        "7d868600543f7ee650523b7fe7174af7bfd7134bc3312a4dd113b913e7f8bdc4",
    ),
    (
        "diis-kk-bind2-1963-78.pdf",
        "https://pure.diis.dk/ws/files/27985/KKBind2.pdf",
        "86218035290679936fec8949ee00e2dd323c1220efae671bac3b86c8e2b90ba8",
    ),
    (
        "diis-kk-bind3-1979-91.pdf",
        "https://pure.diis.dk/ws/files/27986/KKBind3.pdf",
        "f5a354434392a9712fec478e4b89376e48b1cac11c22e092cef1e5d323faec05",
    ),
    (
        "diis-kk-bind4-konklusioner.pdf",
        "https://pure.diis.dk/ws/files/27987/KKBind4.pdf",
        "5b5eed35ccb1739b256b59591d14c9b335916220081dc2fc1561063e504af948",
    ),
    # NATO Archives Online — BALTAP activation cluster (1962,
    # declassified); the archive holds 600+ more BALTAP/LANDJUT items
    (
        "nato-sgm-0694-62-baltap-activation.pdf",
        "https://archives.nato.int/uploads/r/nato-archives-online/f/4/6/f46dde450ec17987210b1e9e41ddcb9751a465ff5a38db6ebd81a5252b7a1176/SGM-0694-62_ENG_NHQO62000582E.pdf",
        "f46dde450ec17987210b1e9e41ddcb9751a465ff5a38db6ebd81a5252b7a1176",
    ),
    (
        "nato-ipt-020-244-baltap-activation.pdf",
        "https://archives.nato.int/uploads/r/nato-archives-online/1/5/3/1538e3ef2a537ff9e62afd1aee2032145bd294611cd87fd92042c7afa58a54d5/IPT_020_244_ENG_NHQO62001054E.pdf",
        "1538e3ef2a537ff9e62afd1aee2032145bd294611cd87fd92042c7afa58a54d5",
    ),
    (
        "nato-sglp-0433-62-baltap-hq.pdf",
        "https://archives.nato.int/uploads/r/nato-archives-online/e/7/7/e77138f6aa0a1aa78b054e19ab4433531189672148f7b5b227d69f8d4129df95/SGLP_0433_62_ENG_NHQI62000832E.pdf",
        "e77138f6aa0a1aa78b054e19ab4433531189672148f7b5b227d69f8d4129df95",
    ),
    # Dragoner, Die Bundeswehr 1989, Teil 2.2 (Territorialheer) —
    # answers the TerrKdo Schleswig-Holstein OOB question. CAVEAT:
    # author-released research compendium on a hobbyist mirror, not
    # an institutional publication — treat as Davies-grade (verify
    # before canon)
    (
        "dragoner-bundeswehr-1989-territorialheer.pdf",
        "https://www.microarmormayhem.com/BW_Territorials.pdf",
        "1f38e698d672b159e4798bef342dea314246fcd0fd5b5d619ace597cff9df20c",
    ),
    # Danish Agency for Culture — Cold War installations (official):
    # 33-site survey (78 MB) and the systematic registration note
    (
        "slks-kold-krig-33-fortaellinger-2014.pdf",
        "https://slks.dk/fileadmin/publikationer/Kulturarv/Kold_Krig_2014.pdf",
        "581f67dc10f07fdef8d2b84ced66cfdab08a8cb017304f61013e6e674fd0e85b",
    ),
    (
        "slks-dkka-baggrundsnotat.pdf",
        "https://slks.dk/fileadmin/user_upload/kulturarv/fysisk_planlaegning/DKKA_baggrundsnotat_v8.pdf",
        "813240fb27e7e67dea4285a49f4243e4dc907d4d2a8ebbc2681b1a2ef488abe5",
    ),
    # Batch 7 (2026-07-22, DK browser fetches — cia.gov bot-blocks
    # this network; these URLs work from a normal browser. Both US
    # Government works, public domain; image scans, no text layer).
    # DI/SOVA research paper, Apr 1989: THE document on red's
    # Denmark operation and its constraints
    (
        "cia-1989-wp-planning-operations-against-denmark.pdf",
        "https://www.cia.gov/readingroom/docs/1989-04-01.pdf",
        "86c2fa3485b72152e83cf7b61c0bb1a8ddfb51f7f10e747cd33cba8ff3e8f525",
    ),
    # DI research paper EUR 84-10207, Nov 1984: Nordic defense
    # capabilities — blue's readiness/stocks/reinforcement clocks
    (
        "cia-1984-nordic-forces-in-the-1980s.pdf",
        "https://www.cia.gov/readingroom/docs/CIA-RDP85S00316R000300040006-9.pdf",
        "fafba67273869f9257916eef7df327906fe845447d62bd773002e4b68114dc0a",
    ),
    # DI intelligence assessment, June 1984 (sanitized, released
    # 2012): Soviet Doctrine for Offensive Chemical Warfare Against
    # NATO — the IC's classified picture to test against
    # FM 100-2-1's public belief (reference/chemical-posture.md).
    # DK browser fetch 2026-07-22 (filename 1984-06-01b.pdf).
    (
        "cia-1984-soviet-offensive-chemical-warfare-nato.pdf",
        "https://www.cia.gov/readingroom/docs/1984-06-01b.pdf",
        "c1b396b73f72a27407d4f603bfab4e7ecf1cf0e82b020391032ebe9038c8177e",
    ),
    # SNIE 11/17-2-84/L (late 1984, sanitized): the COORDINATED
    # community position on Soviet chemical warfare — adopts the
    # 'selective'/WMD-gated view over NIE 11-14-81's 'massive',
    # with the Army's dissent on the record. DK browser fetch
    # 2026-07-22 (reading-room DOC_0000284028).
    (
        "cia-snie-11-17-2-84-soviet-chemical-threat-nato.pdf",
        "https://www.cia.gov/readingroom/docs/DOC_0000284028.pdf",
        "1ec0306c09559ddd3c9c35bb2c0f1e06cbd6dfba63c4b3bbd63686cba853f4f0",
    ),
    # Batch 6 (2026-07-21, period FM 71-series hunt, session 71ede904).
    # FM 71-100 1990 was never webbed (CARL bibliography lists it,
    # links no file); the 1978+C1 edition below is the manual actually
    # in force mid-80s — period-superior for character knowledge
    (
        "fm-71-100-armored-mechanized-division-operations-1978-c1.pdf",
        "https://archive.org/download/FM_71_100_A_D_O_1979/FM%2071-100%20Army%20and%20mechanized%20Divisions%20Operations%20%281979%29.pdf",
        "5c944bb2602ca16483487c33917cab6ecb75697ae2e226378bc0d7fba353cbae",
    ),
    (
        "fm-71-2-tank-mech-infantry-battalion-task-force-1977.pdf",
        "https://www.bits.de/NRANEU/others/amd-us-archive/FM71-2%2877%29.pdf",
        "b51abf3de172d69303b2954d8f4235346d37c25398e5451b21084f806948c634",
    ),
    # 1988 editions (the period 1977/1980 HTF editions are not
    # public): post-provisional-setting — OUR reference, not the
    # characters'. US-government works, public domain; the scans
    # carry period distribution-restriction covers, long moot
    # (superseded twice over, publicly hosted)
    (
        "fm-71-1-tank-mech-infantry-company-team-1988.pdf",
        "https://archive.org/download/fm-71-1-1988/FM%2071-1%201988.pdf",
        "5f987be109c342080d45368140ace32a938f9439f5b5353e073d6512c66847c9",
    ),
    (
        "fm-71-3-armored-mech-infantry-brigade-1988.pdf",
        "https://archive.org/download/fm-71-3-1988/FM%2071-3%201988.pdf",
        "533789e81f82166327f882d04cc39fe3adc6eed74fde8638bd62134ab185e7d6",
    ),
    # FM 55-30 1980 exists only on paper; 1969 edition is the
    # nearest public predecessor (convoy-procedure texture)
    (
        "fm-55-30-army-motor-transport-operations-1969.pdf",
        "https://archive.org/download/FM55-30/FM55-30.pdf",
        "f8e8ac06422c0637d86eda238ea06577a942664e921c3b72bc846afafb8d9d2c",
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
