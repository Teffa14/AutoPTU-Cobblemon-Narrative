# Research Scan 160 — Remote Sensing, Aerial Imagery & Change Detection

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-08-25

## Why this gap is worth adding

The repository already has strong authorities for individual photographs and image provenance, scientific observations, metrology, maps, environmental state and historical revisions. It does not yet have a dedicated authority for repeated remote acquisition over an area: what footprint was actually observed, what was obscured, which product revision was compared, what changed between dates, and what still requires field validation.

This scan therefore targets a narrow systems gap rather than creating a second Photography or Cartography layer.

Authority boundary proposed for Pass 160:

`physical world -> remote acquisition -> coverage/quality -> derived spatial product -> change-detection claim -> field validation -> scoped interpretation`

Visual Records remains authoritative for individual image artifacts and derivative provenance. Metrology remains authoritative for calibration/reference traceability. Cartography remains authoritative for maps and route products. Science remains authoritative for hypotheses, datasets and scientific interpretation. The owning environmental layer remains authoritative for the underlying world state.

## Source 1 — USGS Landsat: repeated observation as historical evidence

USGS describes Landsat as a long-running Earth-observation record used for time-series analysis and environmental change detection. Landsat 8 and Landsat 9 together provide an eight-day interval for coverage of the same area, while Collection 2 applies standardized radiometric, geometric and environmental corrections intended to improve comparison across time.

Reusable lesson for Ouros:

- a remote observation should have an acquisition date and coverage footprint;
- revisits create a history rather than a live omniscient map;
- products from different processing revisions can be compared only when provenance is retained;
- a later corrected product does not erase the raw acquisition or the historical product people used at the time.

Useful Ouros applications include shoreline revision review, wildfire scars, marsh extent, snow persistence, urban expansion, quarry reclamation, reservoir change, river migration and forest recovery.

Sources:

- USGS, Landsat 9: https://www.usgs.gov/landsat-missions/landsat-9
- USGS, Landsat Collection 2: https://www.usgs.gov/landsat-missions/landsat-collection-2
- USGS, Landsat Applications: https://www.usgs.gov/landsat-missions/landsat-applications

## Source 2 — USGS surface-water and change products

USGS Dynamic Surface Water Extent products derive per-pixel surface-water presence from standardized Landsat observations. USGS has also published long temporal histories of surface-water and land-condition change.

The important design lesson is not the pixel formula. It is the separation between:

1. an observed signal;
2. a derived classification product;
3. comparison across dates;
4. an interpretation of why the change occurred.

A water-classification change does not by itself prove drought, diversion, drainage, dam operation, tidal phase or mapping error. Those causal questions belong to Freshwater, Groundwater, Estuaries, Irrigation, Climate, Infrastructure or Science as appropriate.

Sources:

- USGS Dynamic Surface Water Extent: https://www.usgs.gov/landsat-missions/landsat-dynamic-surface-water-extent-science-products
- USGS Landsat change products and applications: https://www.usgs.gov/landsat-missions/landsat-science-products

## Source 3 — NASA ground truth and validation

NASA remote-sensing education and field-validation material repeatedly distinguishes remotely sensed observations from ground truth / field observations used to calibrate or validate interpretation. Remote sensing can provide broad spatial coverage, while field work can resolve local ambiguity that a distant sensor cannot.

Reusable lesson for Ouros:

A remote product should be allowed to say `candidate change detected` long before the world says `cause confirmed`.

This creates an exploration loop that fits Ouros particularly well:

`remote anomaly -> prioritize field visit -> local observation/sample -> reconcile disagreement -> revise spatial claim -> update future monitoring`

The loop produces useful adventures without making every anomaly a villain plot.

Sources:

- NASA, Ground Truth Studies + Satellite Imagery: https://www.nasa.gov/stem-content/ground-truth-studies-satellite-imagery/
- NASA, Earth Day Connections: NASA Investigates Vegetation: https://www.nasa.gov/stem-content/earth-day-connections-nasa-investigates-vegetation/
- NASA ARSET, burn-scar and land-cover-change training resources: https://appliedsciences.nasa.gov/get-involved/training/english/arset-using-earth-observations-mapping-and-monitoring-burn-scars

## Source 4 — Pokémon Legends: Arceus: institutional survey loop

The official Legends: Arceus site presents the Galaxy Expedition Team Survey Corps as an institution that studies how Pokémon live. Survey missions leave Jubilife Village, investigate specific regions, and return to the base for subsequent work. The official gameplay material also describes Hisuian Braviary as giving the rider a high vantage point from which Pokémon and items below can be observed during surveys.

Reusable Ouros structures:

- a survey institution can maintain repeatable field campaigns instead of one-off quests;
- broad observation can determine where investigators should go next;
- elevated observation changes what can be seen without granting perfect identification or causation;
- survey work can alternate between remote reconnaissance and ground investigation.

Guardrail:

Hisuian Braviary lore does not grant aerial-photography equipment, mapping precision, carrying capacity, Sensor capabilities or survey Skills. It is a narrative precedent for elevated reconnaissance only.

Sources:

- Pokémon Legends: Arceus — Story / Survey Corps: https://legends.arceus.pokemon.com/en-ca/story/
- Pokémon Legends: Arceus — Gameplay / surveys and Hisuian Braviary: https://legends.arceus.pokemon.com/en-gb/gameplay/

## Source 5 — Pokémon technology: cameras and remote viewing are setting-dependent

Current Pokémon media contains camera-equipped and remote-viewing technology, including widespread Rotom Phone cameras and Drone Rotom / Rotom Drone concepts in different contexts. These are useful precedents for the possibility of small remote platforms in a Pokémon world, but their existence does not establish what technology Caelo/Ouros has.

Pass 160 therefore keeps platform type authored and setting-dependent. A future Ouros acquisition platform could be a fixed high point, balloon, airship, crewed aircraft, small remote craft, Pokémon-assisted survey platform or another canon-approved technology. Orbital sensing must not be assumed merely because real-world Landsat is used as research inspiration.

Sources:

- Pokémon official TCG database, Drone Rotom: https://www.pokemon.com/uk/pokemon-tcg/pokemon-cards/series/swsh4/151/
- Pokémon Horizons official material showing extensive Rotom Phone camera use: https://www.pokemon.com/us/features/pokemon-horizons-season-2-the-search-for-laqua-part-1-quiz

## Source 6 — PTU campaign-structure guidance

Public PTU campaign guidance emphasizes that the system can support organization-based or exploration-team campaigns, not only League travel. It also recommends allowing calm phases where players pursue their own interests alongside larger plot phases.

Remote sensing fits that structure because it can produce low-intensity research hooks, recurring institutional work and optional field investigations between larger arcs. A change-detection result can remain background evidence until players decide it matters.

The PTU mapping community also repeatedly notes that regional maps become meaningful when spatial differences change player choices rather than serving only as decorative backgrounds. Pass 160 follows that principle by turning spatial revisions into route, conservation, infrastructure or research consequences only through owning systems.

Sources:

- PTU Campaign Structure: https://pokemontabletop.fandom.com/wiki/Campaign_Structure
- Pokémon Tabletop community, regional-map discussion: https://www.reddit.com/r/PokemonTabletop/comments/j2v13u

## Design lessons extracted

### A. Coverage is evidence, not omniscience

Every acquisition needs a footprint and quality state. Clouds, smoke, canopy, shadow, terrain, platform failure, resolution, timing and missing passes can create real gaps.

`NOT_OBSERVED` and `NOT_DETECTED` must stay distinct from `ABSENT`.

### B. Spatial resolution matters

A broad product may reliably show that a marsh boundary changed while being unable to identify which Pokémon used the new habitat. A detailed low-altitude image may show an individual object while covering too little area to support a regional claim.

Do not invent a single universal `sensor_quality` score.

### C. Change detection does not explain cause

Useful claim states:

- NO_CHANGE_DETECTED_FOR_SCOPE
- CANDIDATE_CHANGE
- CHANGE_SUPPORTED
- CHANGE_CONFIRMED_FOR_SCOPE
- ARTIFACT_OR_PROCESSING_DIFFERENCE
- INSUFFICIENT_COMPARABILITY
- UNRESOLVED

A changed pixel or polygon never writes directly into the owning environmental layer.

### D. Revisit history creates Chronicle value

The same site can be acquired repeatedly for decades. Old products can later answer questions nobody originally intended to ask.

Examples:

- a bridge approach existed before a flood;
- a wetland was already expanding before a restoration project;
- a quarry face moved over several years;
- a forest opening predates a suspected disturbance;
- a coastal breach appeared between two acquisitions but not necessarily at a known exact hour.

### E. Processing versions must remain visible

Raw acquisition, corrected/georeferenced product, classification product and public map are not one object.

A new processing method can revise a historical interpretation while preserving the original product that informed past decisions.

### F. Field validation creates adventure without mandatory combat

A remote anomaly is an excellent reason to visit a location, but the visit can end with:

- a confirmed change;
- a harmless seasonal explanation;
- a data artifact;
- an inaccessible site;
- two competing explanations;
- a new question rather than an answer.

### G. Remote observation can itself affect the world

Low-altitude platforms, repeated flights, lights, noise or close approaches can disturb wildlife. Research Ethics, Airspace, Wildlife, Working Pokémon and local access authorities should own those consequences.

A passive distant acquisition should not be treated as identical to a low-flying close survey.

## Explicit no-inferences for Ouros

Do not infer:

- remote image -> authoritative ecological truth;
- image classification -> species identity;
- visible animal count -> population size;
- no visible Pokémon -> population absence;
- change detected -> cause known;
- image color -> toxic contamination;
- burn-like patch -> confirmed wildfire;
- water-like pixels -> safe or potable water;
- vegetation index -> Grassy Terrain;
- snow/ice signature -> Ice-type habitat bonus;
- heat signature -> Fire-type presence;
- aerial platform -> legal access to every property or protected site;
- Rotom/Rotom Phone -> remote-sensing capability;
- Minecraft chunk render -> authoritative remote acquisition;
- Minecraft map item -> Cartography/Science truth;
- client render distance -> survey coverage;
- unloaded chunk -> missing landscape.

## PTU/Caelo mechanical cross-check

No generic PTU mechanic was verified in this scan that authorizes aerial imagery, remote classification, sensor-derived encounter bonuses, automated identification or map-based combat modifiers.

PTU campaign guidance supports exploration/research structures, but that is narrative guidance rather than a mechanical remote-sensing subsystem.

The complete Caelo source corpus was not reliably available in the current runtime for a dedicated remote-sensing rule check. Super PTU Online Helper was not exposed as an invocable capability. No output is attributed to either source.

Any later use of Technology Education, Perception, Pokémon Education, Chronicler/Researcher-like Features, special equipment, flight capabilities or Pokémon-assisted sensing must be validated against the project’s actual PTU/Caelo material before it becomes mechanical.

## Candidate Ouros conclusion

Remote sensing is best treated as an evidence-producing spatial-history layer. Its strongest contribution is not technological spectacle. It is the ability to preserve what an institution could see from a distance at a particular date, expose uncertainty honestly, and send players into the field when interpretation matters.