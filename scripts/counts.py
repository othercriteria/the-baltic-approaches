#!/usr/bin/env python3
"""Per-chapter word counts against the ratified floors (corrected
plan, 50.5k). Run: make counts. Floors from the allocation sheet
as corrected at ratification; apparatus excluded per DK ruling
2026-07-23."""

import subprocess
import sys
from pathlib import Path

FLOORS = {
    "01-endex.md": 3000,
    "02-handover.md": 2600,
    "03-ninety-hours.md": 2200,
    "04-norms.md": 2450,
    "05-green-against-what.md": 2650,
    "06-the-locked-door.md": 2100,
    "07-the-roads.md": 2600,
    "08-the-crossing.md": 2700,
    "09-the-morning-market.md": 3050,
    "10-his-ledger.md": 2100,
    "11-days-behind.md": 2300,
    "12-the-narrows.md": 3050,
    "13-the-visitor.md": 2300,
    "14-the-cathedral-rebuilt.md": 2100,
    "15-sequencing.md": 2650,
    "16-the-bank.md": 1900,
    "17-the-refusal.md": 1850,
    "18-the-crest.md": 2350,
    "19-the-door.md": 2250,
    "19a-the-pocket.md": 2350,
    "20-december.md": 2200,
}

drafts = Path(__file__).resolve().parent.parent / "drafts"
total = floor_total = 0
rows = []
for name, floor in FLOORS.items():
    p = drafts / name
    if not p.exists():
        rows.append((name, None, floor))
        continue
    n = len(p.read_text().split())
    rows.append((name, n, floor))
    total += n
    floor_total += floor

print(f"{'chapter':<28}{'words':>7}{'floor':>7}{'delta':>7}")
for name, n, floor in rows:
    if n is None:
        print(f"{name:<28}{'MISSING':>7}{floor:>7}")
        continue
    d = n - floor
    mark = "" if d >= 0 else "  <-- under"
    print(f"{name:<28}{n:>7}{floor:>7}{d:>+7}{mark}")
print("-" * 49)
print(f"{'TOTAL':<28}{total:>7}{floor_total:>7}{total - floor_total:>+7}")
print(f"plan 50.5k / ceiling 54.2k; narrative only (no apparatus)")
