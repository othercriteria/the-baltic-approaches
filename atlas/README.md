# Atlas — the 1983 theater transport network

*Created 2026-07-23 (session eb2fcb4e), on DK's direction, after
the critique-profile pass showed the drafting model "knows the
map's vocabulary but not the map's logic" (wrong-border opening;
the nonexistent 1983 Great Belt bridge). This package makes
geography a QUERYABLE input instead of latent prose memory.*

## What it is

A weighted multigraph of the theater's transport network as of
**November 1983**: road, rail, and ferry edges over named places,
with 1983 route designations (E3, not E45 — Danish signage
switched 1985), water-crossing tags, and capacities in a common
currency (tonnes/day) for flow questions. Plus an **absences
table**: links that must NOT exist in 1983 (Great Belt fixed
link, Fehmarn Belt link), enforced by tests so the specimen's
bridge-invention class of error fails loudly forever.

## Use

```
python3 -m atlas path koebenhavn rendsburg --profile convoy
python3 -m atlas path fredericia schleswig --metric km
python3 -m atlas flow region:SJ rendsburg          # max flow + min cut
python3 -m atlas flow koebenhavn fredericia --without gb-road-ferry,gb-rail-ferry
python3 -m atlas edges --crossing kiel_canal        # list by tag
python3 -m atlas check                              # lint + guess-rate report
make atlas                                          # = check + tests
```

`path` reports route, km, hours, the lowest-capacity edge on the
route (the chokepoint), and any verify-flagged edges used.
`flow` runs Edmonds–Karp and reports the min-cut edge set — the
"what actually limits movement from A to B" question.
`--without` models dropped bridges / closed ferries.

## Data discipline (read before editing the dataset)

The dataset (`atlas/data/theater-1983.toml`) was SEEDED FROM
MODEL MEMORY — exactly the competence boundary the critique
profile flags (notes/critique-profile.md §2.6). Accordingly:

- **Every capacity is `cap_source = "GUESS"` until researched.**
  Graduation path: GUESS → SOURCED:<shelf-ref> when the CAL-3
  road/rail/belt tonnage research lands (status.md still-open
  item). `check` reports the guess rate; it should go DOWN.
- **`verify = true` marks every fact not confidently dated.**
  Confident anchors carried in `via` notes: Ny Lillebæltsbro
  (1970), old Lillebæltsbro (1935, road+rail), Storstrømsbroen
  (1937), Vogelfluglinie ferry (1963), Fehmarnsundbrücke (1963),
  Rendsburg rail high bridge (1913), Rendsburg road tunnel
  (1961), Rader Hochbrücke (1972), Holtenau high bridge (1972).
  These too deserve a verification pass against the shelf.
- **Distances are 1:500k-atlas-from-memory tier** — good enough
  for ratios and routing, VERIFY-tier for prose. Coordinates are
  display/sanity only; the km field is authoritative.
- Speeds and default capacities live in `atlas/graph.py`
  (`SPEEDS`, `CAP_DEFAULTS_TPD`) as named planning abstractions,
  all GUESS-tier.

## Seams (the WET decision, on the record)

This package is deliberately SEPARATE from `wargame/` — DK ruling
2026-07-23: at n=2 models we are in the WET-vs-DRY valley and
premature unification would force a shared abstraction neither
model wants. Consequences, acknowledged:

- **Consistency is not free.** The wargame's movement/supply
  numbers and the atlas's capacities are calibrated
  independently and CAN disagree. Neither silently wins.
- Division of authority: the **atlas is the source of truth for
  geography and network structure** (what connects to what, by
  what, since when) — outline and prose check against it. The
  **wargame is the source of truth for dynamics** (attrition,
  tempo, the campaign's arithmetic).
- When both speak to the same quantity (e.g. a crossing's
  throughput), the discrepancy gets a line in the **Seam log**
  below — logged, dated, resolved only by research or DK ruling,
  never by auto-reconciliation.

### Seam log

- (none yet)

## Scope

Current coverage: the Jutland E3 corridor, Little Belt (both
1983 bridges), Great Belt (both ferry services), Zealand,
Storstrøm–Falster–Rødby, the Vogelfluglinie, eastern Holstein
(Lübeck–Oldenburg–Puttgarden), the Schleswig operating area
(A7/E3, B76/B201/B5, Kiel Canal and Eider crossings), Hamburg
as southern edge, and a coarse red-side approach (Rostock–
Wismar–Schwerin, with the three IGB crossing groups SE of
Lübeck — encoding the CORRECT threat geometry). Deliberately
absent for now: the West-Jutland net, Zealand's north, the GDR
interior beyond Rostock/Schwerin, Norway/Sweden. Extend when a
question needs it, with the same discipline.
