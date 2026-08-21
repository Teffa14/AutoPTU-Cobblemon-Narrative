# Estuaries, Tidal Wetlands & Salinity Research Scan — Pass 78

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-21

## Why this pass exists

The repository already has dedicated layers for maritime space, freshwater catchments, fisheries, conservation, meteorology, soil, pollution, tourism and infrastructure. Those layers intentionally touch the coast, but none currently owns the transition system where river water, seawater, tide, sediment, groundwater and coastal wetlands interact.

This pass investigates estuaries, tidal marshes, mudflats, brackish gradients, saltwater intrusion and coastal wetland migration as a new connective layer rather than another generic water biome.

## Internal overlap check

Inspected before writing:

- `design/maritime-coasts-depths-layer.md`
- `design/freshwater-watersheds-hydrology-layer.md`
- `design/fisheries-angling-aquaculture-layer.md`
- `design/conservation-protected-areas-stewardship-layer.md`
- `design/soil-health-erosion-land-restoration-layer.md`
- `design/meteorology-forecasting-weather-layer.md`
- `design/air-quality-aerosols-atmospheric-exposure-layer.md`
- `design/engine-readiness-snapshot-pass-77.md`

The maritime layer already permits an `ESTUARY` label and has a generic `marine_condition` concept for tides/currents. Freshwater already models wetlands and downstream reaches. Pass 78 therefore focuses on the coupled interface: salinity gradients, tidal wetland hydroperiod, sediment/accretion, estuary mouth state, freshwater inflow, groundwater salinization and landward marsh migration.

## Pokémon sources

### Shellos and Gastrodon — changing distribution can be world evidence

Official Pokédex entries describe Shellos as a seashore species with regional forms and state that one form is decreasing in number. Gastrodon entries describe shallow beaches, changing relative abundance and occasional appearances far from the sea during prolonged rain.

Reusable structure:

- coastal populations can have long-term distribution records;
- fishers, researchers and residents may notice different trends;
- heavy rain may temporarily move normally coastal Pokémon outside the expected coastal band;
- observations should be stored by location/date/form rather than turned immediately into causal conclusions.

Do not infer:

- a Shellos/Gastrodon form is caused by salinity;
- a form change happens dynamically to an individual;
- rainfall creates a spawn bonus;
- Storm Drain models estuary hydrology.

Sources:
- https://www.pokemon.com/us/pokedex/shellos
- https://www.pokemon.com/us/pokedex/gastrodon
- https://www.pokemon.com/uk/pokemon-news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-sinnoh-region

### Stunfisk — mudflat occupation can be behavior, not terrain mechanics

The official Pokédex states that Stunfisk conceals itself in seashore mud and waits for prey. Galarian Stunfisk is associated with iron-rich mud.

Reusable structure:

- a mudflat can contain concealed wildlife that is observable through tracks, depressions, feeding signs or direct survey;
- sediment chemistry can be part of habitat interpretation;
- exposure of a mudflat at low water may change what can be observed without automatically changing battle terrain rules.

Do not infer:

- every mud tile conceals Stunfisk;
- mud creates Static/Paralysis;
- iron-rich sediment creates Steel typing;
- tidal exposure automatically grants ambush mechanics.

Source:
- https://www.pokemon.com/us/pokedex/stunfisk

### Wooper — wetlands can support group movement without universal social rules

The official Wooper Pokédex describes groups helping each other while moving through wetlands. Paldean Wooper is described as having changed after losing an aquatic territorial struggle and moving onto land.

Reusable structure:

- wetlands can be a meaningful movement and social context for a species;
- habitat history can help explain regional forms at a high narrative level;
- a local group observation can generate follow-up ecology research.

Do not infer:

- every Wooper collective uses the same formation;
- a territorial conflict is known merely because a Paldean Wooper is present;
- wetland group movement grants pack bonuses or shared initiative.

Source:
- https://www.pokemon.com/uk/pokedex/wooper

### Great Marsh — wetland exploration can foreground observation and access rather than battle

The official Brilliant Diamond/Shining Pearl guide presents the Great Marsh as multiple swampy areas where daily Pokémon appearances can be previewed through binoculars and the main loop differs from normal battling.

Reusable structure:

- wetlands can support observation infrastructure;
- daily or seasonal occupancy can matter;
- access rules can be institutional and activity-specific;
- not every Pokémon-contact activity should be expressed as a standard battle.

Do not import the Safari Game's step limits, balls, bait/mud rules or capture balance into PTU.

Sources:
- https://diamondpearl.pokemon.com/en-us/trainersguide/fundamentals/
- https://diamondpearl.pokemon.com/en-au/trainersguide/fundamentals/

## Public PTU/community material

A public PTU campaign log shows a useful structural pattern where Pokémon behavior, a damaged tree and water stress become one ecological problem; players investigate rather than treating the first visible Pokémon as the sole problem. Another log shows the party respecting eggs after learning that a large Pokémon was responding to disturbance.

Reusable structure for Pass 78:

- wetland encounters should allow the visible organism to be a signal rather than the root cause;
- nesting, water level, vegetation and access can be connected without forcing combat;
- resolving a local conflict may require changing player behavior or restoring habitat.

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t
- https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Reddit campaign reports are anecdotal community evidence only. They do not define PTU rules or Ouros canon.

## Estuary science sources

### Estuaries are coupled transition systems

NOAA defines estuaries as places where rivers meet the sea. Freshwater and seawater mix, and tides continuously alter water depth and chemistry. Estuaries can include marshes, mangroves, seagrass, tidal creeks, mudflats and shallow subtidal zones.

Design lesson:

Do not represent an estuary as a static `water_type = brackish` flag. The important state is the changing relationship between freshwater inflow, seawater, tidal stage, sediment and habitat zones.

Sources:
- https://www.fisheries.noaa.gov/national/habitat-conservation/estuary-habitat
- https://oceanservice.noaa.gov/education/tutorial_estuaries/est01_whatis.html
- https://www.fisheries.noaa.gov/west-coast/habitat-conservation/estuary-habitat-west-coast

### Salinity is spatial and temporal

NOAA notes that salinity normally varies by position, tidal stage, rainfall/snowmelt and freshwater inflow. Fresh and salt water may also stratify vertically depending on circulation.

Design lesson:

A single estuary-wide salinity number is often too coarse. Ouros should store coarse salinity zones or observations with time/depth context where it matters. Most gameplay should still use simple qualitative states unless a scientific quest requires more detail.

Sources:
- https://oceanservice.noaa.gov/education/tutorial_estuaries/est10_monitor.html
- https://oceanservice.noaa.gov/education/tutorial_estuaries/est05_circulation.html

### Tidal wetlands move and change

NOAA and NPS materials describe coastal wetland change under sea-level rise, including inundation, altered salinity, sediment accretion and landward marsh migration where space permits.

Design lesson:

A marsh boundary can move over years of world time. Protecting today's polygon while blocking all inland transition space can produce future problems. A restoration should therefore have geometry/history rather than a permanent `restored=true` flag.

Sources:
- https://www.coast.noaa.gov/digitalcoast/data/slr-wetland.html
- https://www.nps.gov/articles/000/saving-salt-marsh.htm
- https://www.nps.gov/articles/coastal-processes-changes-in-sea-level.htm

### Saltwater can move underground too

USGS documents saltwater intrusion into coastal aquifers through multiple mechanisms. Pumping can reduce freshwater pressure and move the freshwater/saltwater interface landward; intrusion can be local or regional.

Design lesson:

A coastal well becoming saline should not automatically mean seawater visibly flooded the surface. Groundwater and surface-water observations remain distinct linked evidence streams.

Sources:
- https://www.usgs.gov/mission-areas/water-resources/science/saltwater-intrusion
- https://www.usgs.gov/publications/saltwater-intrusion-coastal-regions-north-america
- https://water.usgs.gov/ogw/gwrp/saltwater/salt.html

## PTU/AutoPTU evidence available in this runtime

The available Python AutoPTU evidence recognizes `swamp`, `wetland`, `marsh` and `mud` as a wetlands context for selected behavior such as Nature Power, and has explicit Swim/Naturewalk capability handling.

This proves only narrow authored mechanics when their rule contracts apply.

It does not prove:

- tidal movement;
- brackish-water penalties;
- salinity damage;
- sinking mud;
- mudflat hazards;
- estuary currents;
- changing water depth;
- saltwater intrusion;
- wetland visibility;
- dynamic spawning;
- environmental Poisoned/Slowed/Tripped effects.

Caelo primary documents were not reliably retrieved for a dedicated salinity/tide rule during this run. No Caelo-specific estuary mechanic is claimed here.

## Reusable Ouros structures

1. Salinity-front mystery: two stations report different conditions because they sampled different tidal stages or depths.
2. Tidal access window: a route, wreck, mudflat or observation site exists physically at all times but is accessible only in some world states.
3. Marsh migration conflict: a wetland restoration succeeds ecologically but begins moving toward land already designated for another future use.
4. Estuary nursery season: a shallow habitat becomes temporarily important for juvenile Pokémon without creating a rare-spawn switch.
5. Saltwater-intrusion investigation: wells change before the surface marsh visibly changes.
6. Sediment story: upstream works change deposition downstream and slowly alter a channel or mudflat.
7. Estuary-mouth shift: a storm or sediment event changes circulation and therefore access, salinity and habitat.
8. Mixed-use estuary: port, fishery, research, tourism, conservation and settlement actors all depend on the same place in different ways.
9. Historical charts: old maps remain correct for their date because channels and marsh edges genuinely moved.
10. Wildlife observation conflict: a population shift is noticed by fishers before instruments or researchers agree on the cause.

## Copyright/provenance boundary

Only high-level structures, factual ecological principles and source metadata are retained. No protected dialogue, prose, distinctive fan characters or source plots should be copied into Ouros.

## Questions for future validation

- Which Ouros regions contain estuaries, tidal marshes, mangroves, lagoons or deltas?
- Does Ouros need numeric salinity at all, or only qualitative bands plus measurements during research scenarios?
- Which PTU/Caelo terrain labels and Naturewalk capabilities apply to marsh/mud/wetland contexts?
- How should battle initialization freeze a tide/water state without Minecraft deciding PTU mechanics?
- How should Cobblemon receive estuary population projections without letting players exploit tide manipulation for rare spawns?
- How should saltwater intrusion connect to Freshwater groundwater objects and settlement water supply?
