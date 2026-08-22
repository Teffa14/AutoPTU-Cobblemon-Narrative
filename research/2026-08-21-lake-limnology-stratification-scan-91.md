# Pass 91 Research — Lake Limnology, Stratification & Inland-Water Ecology

Status: RESEARCH / PROVENANCE ONLY. Not canon. Not a PTU rules source.

Date: 2026-08-21

## Why this pass exists

The repository already has a broad freshwater/watershed layer. That layer correctly owns catchments, reaches, flow classes, floodplain connections, groundwater links, reservoirs and water-control assets.

What it does not yet model in depth is the internal state of a lake itself.

A lake can have stable surface conditions while temperature, oxygen, clarity and biological activity differ sharply with depth. Seasonal mixing can reorganize the whole water column without changing the lake's identity. A visible bloom can be real while its cause remains uncertain. A shoreline survey can describe the littoral zone accurately while missing a deep-water problem entirely.

This pass therefore studies limnology as a distinct but linked layer rather than expanding the watershed layer until it owns every freshwater process.

## Source set inspected

### Official Pokémon — Lake of Rage / Johto retrospective

Sources:
- https://www.pokemon.com/uk/pokemon-news/remember-the-region-johto-spotlight
- https://www.pokemon.com/us/pokemon-news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-johto-region

Reusable structure:
A lake can be the visible location where a wider technological or institutional action produces a behavioral anomaly in Pokémon. The important structure for Ouros is not the specific Team Rocket plot. It is the separation between:

- unusual Pokémon behavior observed at the lake;
- a cause located elsewhere;
- public interpretation of the lake event;
- investigation that connects the observation to an external actor or signal.

Design lesson:
Do not let a lake anomaly prove its own cause. A large behavioral event may be local evidence of a remote driver.

Copyright boundary:
Do not reproduce the Red Gyarados plot, Team Rocket operation, dialogue or sequence of events.

### Official Pokémon — Wooper / wetland group behavior

Source:
- https://www.pokemon.com/us/pokedex/wooper

Reusable structure:
Pokémon associated with inland waters can have travel and group behavior that is specific to wetlands or shore transitions. That supports repeated observations of route use and shallow-water access without converting every Water-type into a generic lake indicator.

Design lesson:
Species lore can justify a candidate observation protocol. It does not justify a universal ecological mechanic.

### Official Pokémon — Pokécology announcement

Source:
- https://www.pokemon.com/us/news/pokecology-an-illustrated-guide-to-pokemon-ecology-is-available-now

Reusable structure:
Pokémon ecology can be treated as a legitimate field of comparative observation: similarities, differences, relationships and environmental context rather than only species lists.

Design lesson:
A lake should support multi-year ecological records and comparison between sites, not just encounter tables.

### PTU public campaign log — lake as a multi-purpose encounter space

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

High-level observation:
A public PTU campaign log uses a lake/forest area for capture, foraging, environmental interaction, wild-Pokémon behavior and a later conflict. The lake is part of an explorable ecological scene rather than a battle room.

Reusable structure:
One visit can produce several independent opportunities:

- observation;
- capture;
- resource collection;
- travel;
- social interpretation;
- later battle.

Copyright boundary:
No player characters, dialogue, named Pokémon or campaign plot are copied into Ouros.

### USGS — dissolved oxygen and depth stratification

Source:
- https://pubs.usgs.gov/wsp/2382/report.pdf

Key finding:
Dissolved oxygen can vary strongly with depth. Thermal stratification can isolate deeper water from atmospheric mixing, while decomposition continues consuming oxygen near the bottom.

Reusable structure:
A lake may need depth-specific observations. A surface reading cannot establish conditions at depth.

### EPA — dissolved oxygen seasonal cycles

Source:
- https://www.epa.gov/system/files/documents/2021-07/parameter-factsheet_do.pdf

Key finding:
Seasonal cycles can include spring mixing, summer stratification, fall mixing and winter stratification under ice. Temperature and dissolved oxygen profiles change across these phases.

Reusable structure:
Lake state should be versioned by season and observation date. `lake_state = NORMAL` is too coarse.

### EPA — harmful algal bloom overview

Source:
- https://www.epa.gov/sites/default/files/documents/hab-overview.pdf

Key finding:
Bloom occurrence can depend on nutrients, clarity/sediment, circulation, hydrology, climate/weather and biological interactions.

Reusable structure:
A bloom should create an investigation with multiple hypotheses rather than selecting one cause automatically.

### EPA — climate and harmful algal blooms

Source:
- https://www.epa.gov/sites/default/files/documents/climatehabs.pdf

Key finding:
Warmer surface water can strengthen or extend stratification. Some bloom-forming organisms can exploit stratified conditions and vertically position themselves.

Reusable structure:
Meteorology can influence lake internal state through a causal handoff rather than directly creating a bloom flag.

### NOAA / Great Lakes hypoxia synthesis

Source:
- https://cdn.coastalscience.noaa.gov/page-attachments/research/Harmful%20Algal%20Blooms%20Report%20FINAL%20August.2017.pdf

Key finding:
Layering can limit vertical oxygen movement while decomposition consumes oxygen in deeper water. Added nutrient loads can worsen the process by increasing organic material that later decomposes.

Reusable structure:
A deep-water oxygen problem may be delayed relative to the event that contributed nutrients or organic matter.

### USGS — littoral-zone definition

Source:
- https://pubs.usgs.gov/circ/1381/pdf/circ1381.pdf

Key finding:
The littoral zone can be defined by depth, light availability or rooted vegetation. Its width varies greatly with shoreline slope.

Reusable structure:
A lake should not use a fixed-width littoral ring. Mapping requires observations and local morphology.

## High-level reusable design patterns

### 1. Vertical profiles, not one lake number

Track coarse depth layers or sampled stations instead of a single `temperature`, `oxygen` or `clarity` value.

Possible distinction:

- surface / epilimnetic observation;
- transition / thermocline observation;
- deep / hypolimnetic observation;
- bottom-water observation.

These are world-state observations. They do not create battle penalties.

### 2. Mixing regime as persistent seasonal state

A lake can move through:

- mixed;
- developing stratification;
- stratified;
- partial mixing;
- turnover/mixing event;
- ice-covered stratification;
- unknown.

The state should come from authored model logic plus observations, not from Minecraft water blocks.

### 3. Shoreline and deep-water ecology can disagree

A healthy-looking littoral zone does not prove healthy deep water.

A deep-water problem does not prove that the whole shoreline is unsafe.

This allows players with different roles to discover different pieces of the same event.

### 4. Bloom investigation must remain hypothesis-driven

Potential contributors can include:

- nutrient input;
- warmer conditions;
- long residence time;
- reduced mixing;
- sediment interaction;
- biological-community changes;
- altered inflow;
- measurement error.

No single observation should silently pick one.

### 5. Surface appearance is evidence, not diagnosis

Examples:

- unusual color;
- surface scum;
- low transparency;
- odor;
- dead vegetation;
- changed Pokémon activity;
- unusual shoreline congregation.

Each becomes an observation with provenance.

### 6. Turnover can be a world event without being a crisis

Seasonal mixing can:

- change measured oxygen profiles;
- redistribute temperature;
- alter where Pokémon are observed;
- change fishing/survey success;
- move material within the water column;
- create new research windows.

It does not automatically create damage, Weather or hazards.

### 7. Lake anomalies can originate outside the lake

Potential upstream or external drivers can be handed in from existing layers:

- watershed inflow;
- stormwater runoff;
- sanitation failure;
- wildfire ash/sediment;
- agricultural runoff;
- air-quality deposition;
- unusual technological signal;
- drought/heat conditions.

The lake layer should consume evidence and state from those systems without taking ownership of their causes.

## Ouros opportunities created by this research

A lake can support:

- seasonal survey programs;
- depth-profile expeditions;
- littoral habitat restoration;
- bloom investigations;
- fisheries closures based on evidence;
- nighttime oxygen surveys;
- winter under-ice observation;
- public-health advisories without revealing private case data;
- conflicting scientific interpretations;
- historical comparison between old and current bathymetric maps;
- deep-water mysteries that do not require a Legendary cause;
- recurring NPC researchers and local guides;
- long-term consequences from upstream decisions.

## PTU / AutoPTU boundary

The available project evidence includes a specific Python `Secret Power` environment mapping where freshwater/pond/creek/river/lake context can produce a Speed-drop-style effect when that Move is legally resolved.

That is narrow evidence for one Move-specific rule. It does not establish:

- lake-wide Speed penalties;
- deep-water penalties;
- oxygen mechanics;
- algal-bloom status effects;
- toxic-water mechanics;
- turnover effects;
- visibility penalties;
- pressure/depth damage;
- currents;
- diving rules.

Likewise, `Swim` capability confirms only the capability or movement contract that actually uses it. It does not prove limnological simulation.

## Copyright / transformation record

No protected prose, dialogue, named fan characters or distinctive fan-campaign plots are copied.

Pokémon sources are used for broad ecological or narrative structures. PTU community logs are used only for abstract encounter-design lessons. Scientific sources are used to inform system architecture and causal separation.

## Research gaps for later passes

- Exact PTU/Caelo rules for Swim, underwater activity, drowning/suffocation and water terrain.
- Whether Caelo contains lake-specific encounter or environmental modifiers.
- Exact Cobblemon hooks for water depth, biome, temperature and species presence.
- Whether Java will expose an authoritative visibility/depth context.
- Whether lake turnover should be purely world-state or optionally feed a future field-effect system when a PTU rule explicitly supports it.
- How detailed bathymetry should be without simulating every Minecraft block.
