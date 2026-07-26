# Map base geometry — provenance

*Created 2026-07-25 (session e3137278) for the front-matter map
plates (planning/map-spec.md). This directory holds the **base
layer** (timeless coast / water / rivers / marsh) that the plates
draw under the atlas network layer. Kept strictly separate from the
1983 network: the base supplies only geography that has not changed,
so no datable feature can leak in through it (spec §2).*

## What is committed here

| File | Contents | Tier / licence |
|---|---|---|
| `approaches.json` | Plate I extent, clipped: coastline, land polygons, rivers, lakes | Natural Earth, **CC0 / public domain** |
| `neck.json` | Plate II extent, clipped: same layers | Natural Earth, **CC0 / public domain** |
| `handdigitized.json` | Kiel Canal, the Schlei, Eider, Treene, Sorge, Trave, the **Danevirke**, and the Treene–Eider marsh polygon | **hand-digitized, GUESS-tier** (see below) |
| `extract.py` | The clipper that regenerates the two `*.json` extracts from the world downloads | — |

The world Natural Earth downloads live in `src/` and are
**git-ignored** (26 MB, re-fetchable). Only the small clipped
extracts above are committed, per the spec's redistributability rule.

## Natural Earth source (public domain)

Downloaded 2026-07-25 from `https://naciscdn.org/naturalearth/10m/physical/`:

- `ne_10m_coastline` (v5.0.0-pre9)
- `ne_10m_land` (v5.1.1)
- `ne_10m_rivers_lake_centerlines` (v5.0.0)
- `ne_10m_lakes` (v5.0.0)

Datum WGS84 (unprojected lon/lat). Natural Earth is released into the
**public domain** ("no permission needed … crediting is unnecessary");
we credit it anyway. Nothing purchased, scanned, or copyrighted was
used; `holdings/` was not touched.

### Clip extents (lon_min, lat_min, lon_max, lat_max)

- approaches: `(7.6, 53.3, 12.8, 57.35)`
- neck: `(8.55, 53.98, 10.25, 54.65)`

(A small margin beyond each drawn neat-line, so clipped coastline runs
to the edge.) Regenerate with:

```
python3 atlas/data/base/extract.py      # needs src/*.shp present
```

## Hand-digitized supplements (`handdigitized.json`) — GUESS-tier

Natural Earth 10m returns **zero** river features inside the neck
extent: no Kiel Canal, Schlei, Eider, or Treene at plate grain. The
spec's sanctioned fallback is to hand-digitize these at generalized
~1:500k grain from public geographic knowledge, marked GUESS and
disclosed — which is what these are. Endpoints are anchored to atlas
node coordinates where a node exists (Rendsburg, Schleswig,
Friedrichstadt, Lübeck …). Each is a coarse handful of vertices; **no
copyrighted or scanned map was traced.** Treat as display geometry
only, never as survey data.

- **Kiel Canal** — Brunsbüttel → Rendsburg → Holtenau, generalized.
- **the Schlei** — Baltic (Schleimünde) → Missunde narrows → Schleswig.
- **the Eider / Treene / Sorge** — the neck's valve waters.

**Build-2 densification (2026-07-25):** the canal, Schlei, and Eider
were given more vertices and a GUESS-tier `half_km` half-width (a scalar,
or a per-vertex list tapering the Schlei fjord), so the renderer can draw
them as FILLED water ribbons rather than thin lines — the fix for the
Plate II "the water is the blocker" acceptance item. `half_km` is coarse
public-knowledge geography (the canal is drawn a touch wider than true
scale so it does not vanish); the renderer scales it to points per plate,
so the same feature is a thin line on the theater plate and a legible
water body on the neck plate. Still no copyrighted or scanned map traced.
- **the Trave** — Lübeck → Travemünde (Plate I).
- **the Danevirke** — Schlei-head WSW to the Treene marshes, ~19 km,
  facing south, per `reference/danevirke.md`. Rendered as an earthwork
  hachure (the plate's one antiquarian relief symbol).
- **Treene–Eider marsh** — a coarse polygon, rendered as stipple.

The two political frontiers the plates draw — the **Danish frontier**
(light dashed, near Padborg) and the **inner-German border** (heavier,
plain, with its two real gaps at Schlutup and Herrnburg) — are
likewise hand-digitized generalized traces; they are defined inline in
`atlas/render.py` (`_draw_frontiers`) rather than here, and are equally
GUESS-tier. Modern PD admin boundaries carry no 1983 IGB, so it could
not be sourced from Natural Earth.

### Build-3 frontier research (2026-07-25)

The two frontier traces were re-shaped in build 3 from the real
courses (still GUESS-tier generalized polylines; no map image traced):

- **Danish frontier — western terminus.** The 1983 land border reaches
  the Wadden-Sea coast just west of **Siltoft** (the *Siltoftvej*
  road crossing is at 54°54′41″N 8°40′11″E), runs east past **Rudbøl**,
  and ends at the **Flensburg Firth** at ≈54°50′22″N 9°24′16″E. The
  drawn western vertex is placed on this directory's NE mainland dike
  coastline (~8.665°E, ~54.912°N) so the dashed line meets the coast —
  neither short of it nor out to sea. Source: Wikipedia,
  *Denmark–Germany border* (en.wikipedia.org/wiki/German-Danish_border),
  crossing-table and Flensburg-Firth terminus coordinates.
- **Inner-German border — Ratzeburg reach.** From the Baltic at
  **Priwall** (east of Travemünde) the border ran south past the
  **Schlutup** (road) and **Herrnburg** (rail) gaps, then along the
  **north-eastern / eastern shore of the Ratzeburger See** (between
  Rothenhusen / Groß Sarau and Römnitz) — so **Ratzeburg itself (FRG,
  ~10.76°E) lies just WEST of the line**, not on a straight tangent —
  then south-east toward the **Schaalsee** and on south. Sources:
  Wikipedia, *Ratzeburger See* (en.wikipedia.org/wiki/Ratzeburger_See),
  which records the NE lakeshore as the inner-German border between
  Hohenleuchte/Römnitz and Rothenhusen/Groß Sarau; and the Schaalsee
  reserve description confirming the border divided the Schaalsee to the
  south-east.
