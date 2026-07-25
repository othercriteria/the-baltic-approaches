# November climatology — LANDJUT operating area

*Started 2026-07-22 from the calibration-queue research pass
("November climatology: weather + sea-state distributions"). Style
per landjut-front.md: every claim carries its source; TO-VERIFY
items are not yet fit for canon or the instrument's parameter file.
Post-period sources are for us, not for characters.*

**Reference-period note.** The primary numbers below are **1961-90
climatological standard normals** (DMI and DWD), which bracket a
mid-80s setting exactly — no 1991-2020-warming caveat applies to
them. Sources that are *measurement-era post-period* (Baltic wave
buoys from 1991, satellite fog climatologies, BSH ice reports) are
flagged inline: they describe a slightly warmer Baltic than 1986's,
so their means are a *mild floor* on period severity for anything
storm/ice-related.

Principal sources (fetched 2026-07-22):
- **DMI TR 99-5** (Laursen, Thomsen & Cappelen 1999), *Observed Air
  Temperature, Humidity, Pressure, Cloud Cover and Weather in
  Denmark — with Climatological Standard Normals, 1961-90*.
  https://www.dmi.dk/fileadmin/user_upload/Rapporter/TR/1999/tr99-5.pdf
- **DMI TR 99-13** (Cappelen & Jørgensen 1999), *Observed Wind Speed
  and Direction in Denmark — with Climatological Standard Normals,
  1961-90*.
  https://www.dmi.dk/fileadmin/user_upload/Rapporter/TR/1999/tr99-13.pdf
- **DMI TR 97-8** (Frich et al. 1997), *Observed Precipitation in
  Denmark, 1961-90*.
  https://www.dmi.dk/fileadmin/user_upload/Rapporter/TR/1997/tr97-8.pdf
- **DWD station normals 1961-90** (temperature, precipitation,
  sunshine), Klimadaten Deutschland "vieljährige Mittelwerte"
  tables, https://www.dwd.de/DE/leistungen/klimadatendeutschland/mittelwerte/
- **GAO PSAD-79-65** (11 Jun 1979), *Aerial Fire Support Weapons:
  How Useful Would They Be in a European Conflict?* — unclassified
  digest of a classified report; period-correct institutional
  judgment. https://www.gao.gov/assets/psad-79-65.pdf
- **HELCOM Baltic Sea Environment Fact Sheets**, wave climate 2020
  and 2024 editions (BSH/FMI/SMHI), and SST 2018 edition.
  https://helcom.fi/baltic-sea-trends/environment-fact-sheets/
- **BSH ice-winter report 2021/22**, German coasts.
  https://www.bsh.de/ (Ice reports and ice charts)
- **Björkqvist et al. 2018**, 41-year Baltic wave hindcast vs.
  measurements (Ocean Engineering; preprint
  https://arxiv.org/abs/1705.00559).

## 1. Air-operations weather

The 1961-90 normals describe a month in which visual air-to-ground
work is the exception:

- **Cloud cover**: November mean total cloud cover 69-72% at the
  Danish stations bracketing the corps area (Karup 69, Skrydstrup
  71, Odense 72, Copenhagen/Kastrup 71%); **13-14 days of the month
  have cloud cover >80%** (Skrydstrup 14, Kastrup 14, Karup 13).
  Only December-January are marginally worse. [DMI TR 99-5, Tables
  7.1.1, 7.3.1]
- **Fog** (visibility < 1 km, station day-count): November normals
  **9.8 days at Skrydstrup, 8.4 at Karup, 8.0 at Værløse, 5.0 at
  Kastrup**; the inland Jutland airbase stations run ~110-120 fog
  days a year. Coastal/lighthouse stations show far fewer (Kegnæs
  4.6, Gedser area ~3-5) — fog in this climate is chiefly an
  inland radiation/advection phenomenon, worst in the hours around
  dawn. [DMI TR 99-5, Table 8.3.1] Satellite climatology confirms
  the seasonal shape for Germany: fog/low-stratus maximum in
  autumn, then winter (Bendix, *A satellite-based climatology of
  fog and low-level stratus in Germany*, Atmos. Res. 2002 —
  post-period method, for us).
- **Sunshine**: November means (1961-90) **50.8 h/month at
  Schleswig, 52.0 at Kiel-Holtenau, 53.0 at Hamburg-Fuhlsbüttel** —
  about 1.7 h/day against ~8.5 h of daylight. [DWD sunshine
  normals 1961-90]
- **Period institutional judgment** (1979, i.e., in-period and in
  characters' reach): GAO's digest on aerial fire support in
  Europe — "The poor visibility generally prevalent in that
  theater, due to weather conditions and terrain obstructions,
  would limit the AH-64's standoff range"; the A-10 "can only
  perform under conditions of good visibility"; recommendation to
  "fund the development of an improved A-10 to perform close air
  support at night and in adverse weather." [GAO PSAD-79-65,
  pp. i-iii] OTA's 1987 FOFA assessment lists "inability to
  operate aircraft at night and in bad weather" as a first-order
  defect to be remedied. [OTA, *New Technology for NATO:
  Implementing Follow-On Forces Attack*, June 1987,
  https://www.princeton.edu/~ota/disk2/1987/8718/8718.PDF]
- ~~**What is still missing — the one number the sortie model
  wants**~~ **FOUND 2026-07-25 (Opus verify pass) — GATE
  DISCHARGED. PRIMARY, period-correct:** *AWS Climatic Briefs:
  Europe* (USAFETAC, Jul 1981), DTIC **AD-A118450**, free scan at
  https://archive.org/details/DTIC_ADA118450. CAV FREQ (%) panels
  = % of hourly obs with ceiling and/or visibility BELOW the
  stated floor; flyable = 100 − printed. Two in-theater stations:
  **Karup** (WMO 06060, leaf 0016; sources: Karup N-Summary Jan
  1953–Nov 1971 + DATSAV 1966–76 — POR read off the sheet image,
  verified this session) and **Hohn** (WMO 10038, near Rendsburg,
  leaves 0047–48; sources: **"Schleswig RUSSWO, POR Jan 1964–Dec
  1973"** + DATSAV — literally RUSSWO-derived, pre-1983 POR, no
  climate-drift caveat). **November, ALL HRS, flyable %
  (Karup/Hohn):** ≥3000 ft & 3 NM: 48/~46 · ≥1500 & 3: 59/55 ·
  ≥1000 & 2: 68/65 · ≥500 & 1.5: 78/78 · ≥300 & 1: 87/88. Karup
  leaf-0016 rungs (52/41/32 below) verified against the page
  image this session. Diurnal signal weak (midday only ~3–8
  points better — advective stratus, not radiation fog).
  **Recommended instrument brackets:** visual-CAS minimum
  (~1000 ft/3 sm): **63% ± 5 of hours**; conservative roll-in
  minimum (3000 ft/3 NM): **47% ± 4**. Caveats: hours not days
  (days-with-a-window higher, fully-flyable days lower); "and/or"
  semantics; the doc's 2/3 NM floors vs 3 sm interpolated.
- *The prior labeled inference* ("visual attack weather well
  under half the days") is hereby graded: **right at the high
  minimum (47%), too pessimistic at the low-level minimum
  (63%)** — the instrument's assumption flag can come off, with
  the threshold choice now the stated variable.

## 2. Daylight

Computed for Rendsburg (54.30°N, 9.66°E), November 1986, NOAA solar
equations (astronomy, not statistics; almanac cross-check is a
formality — flagged TO-VERIFY only for the minutes):

| Date | Civil dawn | Sunrise | Sunset | Civil dusk | Daylight |
|------|-----------|---------|--------|-----------|----------|
| 1 Nov | 06:44 | 07:22 | 16:48 | 17:26 | 9 h 26 m |
| 15 Nov | 07:10 | 07:50 | 16:23 | 17:02 | 8 h 32 m |
| 30 Nov | 07:35 | 08:17 | 16:04 | 16:46 | 7 h 47 m |

Daylight shrinks ~3.5 min/day through the month; civil twilight
adds ~38-42 min at each end. Kiel, Karup and Zealand are within a
few minutes of these values (54-56°N band). **By mid-month the
night is ~15.5 h long** — the majority of any 24-h combat day is
dark, and the whole month loses another 1 h 39 m end to end.

## 3. Ground conditions

- **Temperature** (Nov means, 1961-90): German side Schleswig
  4.9-5.0 °C, Kiel 5.3-5.4, Rendsburg-adjacent stations ~5,
  Lübeck 4.4-5.3, Hamburg 5.1, Fehmarn 5.6 [DWD temperature
  normals]. Danish side: Karup 4.3, Skrydstrup 4.6, Odense 5.0,
  Kastrup 5.1; mean daily max ~6.9-7.3, mean daily min 1.5-2.7.
  [DMI TR 99-5, Tables 4.1.1, 4.2.1, 4.6.1]
- **Frost**: average date of first frost is **18 Oct (Skrydstrup),
  21 Oct (Karup), 7 Nov (Kastrup)** — so November nights freeze
  routinely: 9-10 frost nights at the Jutland stations (Skrydstrup
  9.1, Karup 9.9), 6.5 at Kastrup. But **days that stay below
  freezing are rare: 0.6-1.0 November "ice days"** (Tmax < 0).
  [DMI TR 99-5, Tables 4.9.1, 4.4.1, 4.12.10] *Labeled inference*:
  with mean temps ~+5 °C, sustained ground freeze — the thing that
  would firm up soft going — does not arrive in November; that is
  a December-February phenomenon.
- **Precipitation**: **November is the wettest month of the Danish
  year** — national 1961-90 mean 79 mm (vs. 38 in Feb), and TR 97-8
  states it flatly: "The highest frequency of wet days occurs in
  November." National normals: **18 days ≥0.1 mm, 13 days ≥1 mm,
  2 days ≥10 mm**; south-central Jutland (the Skrydstrup/Toftlund
  belt) runs 20-21 wet days. [DMI TR 97-8, §5.3-5.5, Table 3]
  German side same story: November totals **104.9 mm Schleswig,
  91.4 Rendsburg, 105.3 Flensburg, 81.8 Kiel-Holtenau**, drying
  eastward to 60-64 mm at Lübeck/Fehmarn — at Schleswig November
  is the single wettest month of the year (annual 925.7 mm). [DWD
  precipitation normals 1961-90]
- **Snow**: not a November planning factor — 1.9-2.6 snowfall days
  and 1.3-2.3 snow-cover days at the Danish stations; it falls as
  rain. [DMI TR 99-5, Tables 8.1.1, 8.2.1]
- **Trafficability**: **no quantified source yet** (open item). The
  physical setup is: wet-side maximum soil moisture (wettest month,
  ~every-other-day rain) with no compensating ground freeze —
  *labeled inference*: off-road going for armor is at or near its
  annual worst, on the boulder-clay moraine of eastern Holstein
  and the drained marsh of the west coast alike; the sandy central
  Geest is the best of a bad set. Movement planning collapses onto
  roads and the road network's bridges — which couples directly to
  the 90-hour Jutland Division clock (landjut-front.md). A real
  terrain/trafficability study (Bundeswehr MilGeo series, or US
  Army terrain analysis of the North German Plain) must replace
  this inference before the advance-rate tables encode it.
- **Vegetation/concealment**: DWD's phenological calendar (1961-90
  reference) puts pedunculate-oak leaf **discoloration at ~18
  October** (long-term mean) with leaf **fall — the marker of
  phenological winter — running through November**. [DWD
  phenology pages, www.dwd.de "Phänologische Uhr"; exact regional
  1961-90 mean date for Schleswig-Holstein TO-VERIFY] *Labeled
  inference*: deciduous concealment is substantially gone by
  mid-November; woods still screen against ground observation but
  much less against air; conifer stands (minority in SH) keep
  their value.

## 4. Sea state and naval weather (western Baltic)

- **Wind — 1961-90 normals at the stations facing the landing
  water** (Kegnæs Fyr at the mouth of Flensburg Fjord; Møns Fyr and
  Røsnæs at the Zealand approaches): November mean wind **8.4-9.2
  m/s** (Kegnæs 8.5, Møn 8.4, Røsnæs 9.2 — vs. ~5.2-5.3 at inland
  Karup); **days with wind ≥10.8 m/s (Bft 6+): Kegnæs 17.7, Møn
  16.6, Røsnæs 18.0** — *more than half the days of the month*;
  days ≥20.8 m/s (Bft 9, strong gale): ~1 (Møn 1.2, Kegnæs 0.9,
  Christiansø 1.7). At nearly every exposed station November and
  December are the two windiest months of the year. [DMI TR 99-13,
  normals tables pp. 274-277]
- **Storm precedent, in-period**: "The hurricane 24-25 November
  1981 was by far the most destructive hurricane in this century
  over the Danish area. The storm 3 days before could be
  interpreted as a sort of a warning." [DMI TR 99-13, p. 282] A
  major storm inside a November campaign window is historically
  documented, not a contrivance.
- **Waves** (measurement era 1991-, post-period, for us): Darss
  Sill buoy since 1991, Arkona since 2002, Fino 2 since 2014.
  Long-term maximum significant wave height at Darss Sill and
  Arkona is **about 4 m**; Arkona's long-term December maximum is
  higher, **>5 m** (a 3.3 m event in Dec 2020 was "almost 2 metres
  below the long-term December maximum"). [HELCOM wave-climate
  fact sheets 2024 and 2020] Baltic-wide, the 41-year hindcast
  finds **84% of all events with Hs > 7 m fall in November-January**
  — open-Baltic extremes, but they date the storm season. [Björkqvist
  et al. 2018] Monthly *mean* Hs for November at Darss Sill is not
  in the fact sheets' text — open item (the data exist, Hereon/BSH).
- **SST**: no citable November number found today — the HELCOM SST
  fact sheets carry the annual cycle only in figures. Qualitative,
  sourced: surface waters cool steadily through November-December
  and stay well above freezing on the outer coasts all winter in
  mild years. [HELCOM SST 2018; BSH ice-winter 2021/22] Number
  TO-FIND (BSH MARNET / IOW station climatology).
- **Icing: none in November — verified to the extent the accessible
  record allows.** In 33 years of wave measurement, ice interrupted
  the western-Baltic stations only in Feb-Mar (1995/96 at Darss
  Sill, Feb-Mar 2010 at Arkona) [HELCOM wave 2024, Metadata]; in
  the 2021/22 cold snap, first ice formed in the sheltered Schlei
  on **21 December** [BSH ice-winter report 2021/22]; "first ice
  in November" statements in the literature refer to the Bothnian
  Bay, not here. The definitive normal is the BSH *Climatological
  Ice Atlas for the western and southern Baltic Sea (1961-2010)*
  (Schmelzer & Holfort, BSH Publ. 2338) — TO-ACQUIRE, including
  the severe-winter check (e.g., 1978/79) before "no November ice"
  is promoted from strong evidence to flat rule.
- *Labeled inference for the amphib question*: a Zealand landing
  force in November needs a multi-day window of ≤Bft 5 for the
  assault, the follow-on echelon (~100-hour spacing per
  zealand-landing.md) and the mine-clearing effort before it — and
  the wind table says Bft 6+ occurs on >50% of November days at
  the approach stations. Windows exist (storms pass in 1-2 days)
  but they are short, and forecasting them 4-6 days out with
  1980s tools is itself an operational gamble.

## 5. Consequences for the instrument

- **Air-sortie model**: November grounds or degrades visual CAS/BAI
  on most days — the deep-vs-close apportionment argument
  (reference/air-apportionment.md) changes character: sortie
  scarcity is weather-driven before it is attrition-driven.
  Suggest a daily weather state (visual / IMC / storm) drawn from
  the normals above; the visual-day fraction is currently an
  **assumption pending the RUSSWO-type table** (Open item 1) and
  must be flagged as such in the parameter file.
- **Symmetry clause**: the same weather shields the Danish
  mobilization march and the WP second echelon alike — bad
  November weather is not a blue-only or red-only modifier; it
  degrades FOFA/BAI, resupply interdiction, and reconnaissance in
  both directions. (Radar-MTI and all-weather systems are
  precisely what the period debate — GAO 1979, OTA 1987 — says
  neither side reliably had yet.)
- **Advance rates / ground model**: wettest month + no ground
  freeze → off-road degradation at its annual maximum; road and
  bridge throughput dominate; engineer effort is a first-class
  resource. Couples to the 90-hour clock and Little Belt bridge
  dependencies already in landjut-front.md.
- **Daylight**: 9.4 → 7.8 h across the month, ~15+ h nights —
  sortie-per-day counts, artillery observation, and the plausible
  concealment of night moves all key off this; the instrument's
  day-length parameter should be date-indexed, not constant.
- **Amphib window (zealand-landing.md v9/v10)**: the sea-state
  clock is real and hostile — credibility of the landing threat
  should decay on sequencing AND on the >50%-of-days-Bft 6+
  statistic; a red feint gains plausibility only inside a
  forecast calm window. November icing is a non-factor; do not
  model it.
- **Storm card**: one genuine multi-day storm in a ~3-week November
  campaign is climatologically ordinary (and the 24-25 Nov 1981
  precedent is exact) — worth an explicit scenario event that
  grounds both air forces and closes the amphib window entirely.

## 6. Open items

1. ~~Joint ceiling/visibility frequency table for a SH airfield~~
   **DISCHARGED 2026-07-25** — AD-A118450 (§1 above; Karup +
   Hohn/Schleswig-RUSSWO panels, numbers banked). Optional deeper
   pursuit only: the parent **Schleswig RUSSWO (POR Jan 1964–Dec
   1973)** as a standalone, for the full joint
   ceiling-versus-visibility cross-tabulation (the AWS brief
   gives marginal and/or thresholds); existence confirmed by
   AD-A118450's source line, no free copy surfaced — DTIC/NTIS.
2. **Darss Sill November mean/exceedance Hs** (1991- record;
   Hereon/BSH data holdings) — turns the wind-day proxy into a
   real sea-state distribution.
3. **Western Baltic November SST**, citable number (BSH MARNET
   climatology or IOW Arkona/Kiel Bight station normals).
4. **BSH Climatological Ice Atlas 1961-2010** (Schmelzer &
   Holfort) — pin the no-November-ice normal, incl. severe-winter
   1978/79 check.
5. **Trafficability study** to replace the §3 inference: Bundeswehr
   MilGeo series for Schleswig-Holstein, or US Army/BAOR terrain
   analyses of the North German Plain (globalsecurity.org carries
   a derived terrain text — fetch blocked today, TO-RETRY).
6. **DWD phenology**: exact 1961-90 mean leaf-fall
   (Stieleiche/Blattfall) date for the SH phenological region.
7. **DWD fog-day (Nebeltage) normals for Schleswig/Kiel stations**
   (DWD CDC station "KL" data) — German-side counterpart to the
   Danish Table 8.3.1 numbers.
8. Almanac cross-check of the computed §2 sun/twilight times
   (minutes-level formality).
9. ERA5-based European-airport low-visibility climatology
   (Weather & Climate Extremes, 2019; Hamburg is a station) —
   modern cross-check, paywall/403 today.
