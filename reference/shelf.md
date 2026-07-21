# Research shelf — manifest of record

Fetched documents live in `reference/pdf/` (gitignored; every item
re-fetchable via `make shelf` / `scripts/fetch-shelf.py`, sha256-
pinned there). This manifest is the shelf's catalog: what we hold,
what's queued, what must be bought. Notes distilled from these
sources go in `reference/*.md` files alongside this one, as in
white-buffalo.

## Held (fetched 2026-07-20, all US-government public domain)

| Document | Why it's on the shelf |
|---|---|
| FM 100-5 *Operations*, 1982 (188 pp) | AirLand Battle's founding statement — the doctrine the book's insight arc moves *toward* |
| FM 100-5 *Operations*, 1986 (207 pp) | The setting-year edition; canonical vocabulary for what a 1986 officer could have read |
| Romjue, *From Active Defense to AirLand Battle* (TRADOC, 1984; 144 pp) | The official history of the 1976→1982 doctrinal fight — the intellectual drama the mentor arc dramatizes; also the best map of Active Defense's named defects |
| FM 100-2-1 *The Soviet Army: Operations and Tactics* (1984; 203 pp) | What NATO *believed* about Soviet echelonment, OMGs, and norms in-period — the threat model characters reason with (right or wrong) |
| *Littoral Commander: The Baltic* rules (Bae & Wernert, Dietz Foundation 2025; 104 pp) | Wargaming baseline, NOT period doctrine: grand-tactical Baltic system to build our micro-strategic instrument against (planning/wargaming.md has the steal/skip list) |

## Local archive tier (use in place, never redistribute)

`/bulk/dlk/military` (DK's local archive) holds unclear-provenance
scans of public-domain gov docs — surveyed 2026-07-20, curated map in
`reference/bulk-survey.md`. Notables available locally: FM 100-5
1976, FM 100-2-2/-2-3, the 1969-76 theater-rail cluster, 1980s radio
procedure, the Aggressor exercise-enemy series, period map-symbol
plates. Cite by path; when a clean public copy is needed, fetch the
same document via the queue below instead.

## Fetch queue (free/PD; URLs to be hunted)

- FM 100-5 *Operations*, 1976 (Active Defense itself; local scan in
  /bulk — fetch a clean CARL/archive.org copy when citing publicly)
- FM 101-10-1 *Staff Officers' Field Manual: Organizational,
  Technical and Logistical Data* (the planning-factors bench —
  absent from /bulk, confirmed by survey)
- FM 71-100 *Division Operations* + FM 71-series maneuver doctrine
  (absent from /bulk)
- FM 55-30 *Army Motor Transport Units and Operations* (1980) — the
  period parent of the convoy procedures in /bulk
- FM 24-18 tactical single-channel radio (early-80s edition, for
  exact-period prowords)
- TRADOC Pam 525-5, *The AirLand Battle and Corps 86* (1981) — the
  transitional concept document
- Glantz's free CSI/SASO papers (his Frank Cass books are commercial —
  see purchase list): candidates include the Art of War symposium
  transcripts and CSI research surveys on Soviet operational art
- House, *Toward Combined Arms Warfare* (CSI, 1984) — free CSI classic
- Mearsheimer, "Why the Soviets Can't Win Quickly in Central Europe"
  (*International Security* 7:1, 1982) — the period net-assessment
  debate, wargaming calibration
- Posen, "Measuring the European Conventional Balance" (*IS* 9:3,
  1984-85) + the Epstein/Posen/Mearsheimer 3:1-rule exchange —
  metrics-that-mislead, argued in-period by the principals
- CIA/NIE declassified Warsaw Pact assessments (NIE 11-14 series, CIA
  FOIA reading room)
- BALTAP/LANDJUT and I (NL) Corps structure sources (front-selection
  support; likely NATO histories, Danish/German official material)
- Dupuy-adjacent free material: CAA/BDM studies on QJM validation if
  findable (the books themselves are purchases)

## Holdings (owned, not redistributable — private companion repo)

DK-owned materials that can't be freely redistributed live in the
`holdings/` submodule (`the-mission-1986-private`, always-private).
The *metadata* is public, here and in that repo's catalog — private
means "not redistributed," never "concealed." The main repo's
pre-commit guard (`make hooks`) blocks document binaries from this
repo so the only road for such files is the holdings repo.

| Holding | Status |
|---|---|
| Dupuy, *Numbers, Predictions and War* | print copy acquired 2026-07-20; PDF to be produced from the printed text or sourced. Unblocks wargame v1 calibration (QJM advance rates, daily-casualty norms) |

## Purchase list (copyrighted; DK's call)

- Goldratt, *The Goal* (structure model — mentor dialogues, metrics
  engine)
- ~~Dupuy, *Numbers, Predictions and War*~~ → acquired, see Holdings
- Epstein, *The Calculus of Conventional War* (1985; anti-Lanchester
  tempo model)
- Glantz, *Soviet Military Operational Art: In Pursuit of Deep Battle*
- Hackett, *The Third World War* (1978/82) — genre neighbor
- Coyle, *Team Yankee* — genre neighbor
- Clancy, *Red Storm Rising* — genre neighbor (vibe calibration only,
  per premise: no borrowed furniture)
- Isby, *Weapons and Tactics of the Soviet Army* — hardware auditor's
  bench reference
- Simpkin, *Red Armour* / *Race to the Swift* (1984/85) — period
  Western theorist of Soviet tempo thinking

## Shelf disciplines

- Period line: primary doctrine must predate the setting year for
  anything a character can know. The year is provisionally mid-80s
  and UNPINNED (planning/setting-time.md) — so distillations must
  tag source dates rather than assume 1986; later scholarship
  (Glantz's later work, CSI retrospectives) is for *us* — mark
  distillations accordingly so nothing anachronistic leaks into
  characters' mouths (CLAUDE.md voice rule).
- Every fetched item gets pinned (sha256) in the fetch script; a
  moved/dead URL is a fix-the-script event, not a lose-the-source
  event.
