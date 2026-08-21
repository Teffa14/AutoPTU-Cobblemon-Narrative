# Research Scan — Alpine Mountains, Elevation Zonation & Pass Ecology

Status: research/provenance only. Not Ouros canon.

Pass: 84.

Inspected: 2026-08-21.

## Why this pass exists

The repository already has dedicated systems for Cryosphere, Aerial corridors, Canopy/vertical forest, Travel, Cartography, Geology, Weather, Soil, Freshwater, Wildfire and public infrastructure. None of those layers owns the mountain as a connected elevation system.

This pass focuses on how the same mountain can change with elevation, slope aspect, exposure, treeline, pass geometry, rest/staging sites, alpine meadows, talus, ridges and summit conditions.

The design target is a mountain that can remain one persistent place while different elevation bands support different ecology, access, institutions, observations and adventure structures.

## Source findings

### Pokémon — Gogoat

Official Pokédex material describes Gogoat as living in herds in mountainous places, with leadership contests among herd members. It also says the species has assisted people with work for thousands of years.

Reusable structure:

- mountain species can have authored herd behavior;
- a species can have long-standing human work relationships without becoming universal transport infrastructure;
- observing a group on one elevation band does not prove the whole mountain population is there.

Source:
https://www.pokemon.com/uk/pokedex/gogoat

### Pokémon — Avalugg

Official Pokédex material describes Hisuian Avalugg moving along steep mountain paths through deep snow and encountering Cetitan groups without automatically fighting them.

Reusable structure:

- steep mountain travel can be species-specific behavior;
- two large wild groups meeting can resolve through avoidance rather than combat;
- observed route use is useful ecological knowledge but does not grant traversal capability to Trainers.

Source:
https://www.pokemon.com/us/pokedex/avalugg

### Pokémon Mystery Dungeon — Sky Peak

Sky Peak is structured as a long ascent broken into successive passes and stations, with rest/transport points between stages rather than one uninterrupted dungeon. Different portions of the climb use different encounter populations.

Reusable structure:

- mountain ascent can be segmented into staging bands;
- rest stations create social, supply and callback nodes;
- higher elevation can change encounter context gradually instead of through a single biome switch;
- a known mountain can still feel different depending on which station or band the player is traversing.

Sources:
https://bulbapedia.bulbagarden.net/wiki/Sky_Peak
https://bulbapedia.bulbagarden.net/wiki/Sky_Peak_Mountain_Path

Copyright boundary:

Do not copy Sky Peak's station count, bosses, Shaymin plot, gondola implementation, dungeon floors or progression requirements.

### PTU public adventure — A Song of Ice and Ire

The public Pokémon Tabletop adventure catalogue describes A Song of Ice and Ire as a mountain-resort scenario in an unusually strong blizzard with time management, environmental hazards and triage of side-quest priorities. The adventure profile describes a small sandbox where helping with side problems can provide resources or enable further exploration.

Reusable structure:

- a mountain can support a compact regional sandbox rather than a linear climb;
- route access, shelter, supplies and local problems can influence which portions of the mountain are practical to explore;
- mountain logistics can matter narratively without every obstacle becoming a battle;
- solving optional local problems can change future access without becoming arbitrary quest gating.

Sources:
https://pokemontabletop.com/wiki/index.php/Quest%3AAdventures
https://pokemontabletop.com/wiki/index.php/Quest%3AA_Song_of_Ice_and_Ire

### NPS — alpine treeline is an ecotone, not a fixed line

National Park Service material describes alpine treeline as a transition zone. Its position and structure vary with temperature, snowpack, wind, soil moisture, slope and aspect. Trees become shorter, patchier and wind-shaped near the upper edge rather than ending at a single universal elevation.

Reusable structure:

- Ouros should model treeline as a spatial band/revision, not one hard Y-coordinate;
- two slopes of the same mountain can have different treeline elevations;
- boulders and wind shelters can create local exceptions;
- long-term change can move treeline without changing mountain identity.

Sources:
https://www.nps.gov/articles/000/alpine-vegetation-resource-brief.htm
https://www.nps.gov/articles/denali-treeline-shifts.htm
https://www.nps.gov/teachers/classrooms/aspect-treeline-climate.htm

### NPS — elevation alone does not define alpine habitat

Mount Rainier and Olympic National Park material separates alpine/subalpine environments into different combinations of talus, snowbeds, meadows, ridges and wind-exposed terrain. Slope and aspect change growing season and snow persistence.

Reusable structure:

- elevation band should not equal one uniform biome;
- one altitude can contain wind-scoured ridges, late snowbeds, talus and sheltered vegetation;
- route state and ecology can differ on opposite aspects of the same massif;
- a summit route can cross multiple microhabitats without loading a different region.

Sources:
https://www.nps.gov/mora/learn/nature/plants.htm
https://www.nps.gov/olym/learn/nature/alpine.htm
https://www.nps.gov/olym/learn/nature/subalpine.htm

### North Cascades — mountain life zones

NPS describes mountain habitats as elevation-linked life zones with distinct conditions and communities.

Reusable structure:

Ouros can use coarse vertical ecological bands for simulation and authoring while avoiding per-block ecology.

Source:
https://www.nps.gov/noca/learn/nature/life-zones.htm

## Cross-system lessons for Ouros

### 1. Elevation band is world state, not PTU Terrain

A location can be ALPINE, SUBALPINE or MONTANE for ecology and travel without automatically applying Rough Terrain, Slow Terrain, Weather, Accuracy, damage or movement penalties.

### 2. Aspect matters

North/south/east/west exposure can alter snow persistence, vegetation, wind, visibility and route timing. Aspect belongs in mountain physical state and observations. It does not create tactical modifiers by itself.

### 3. Treeline needs history

Treeline should support revisions over years. The old treeline can remain useful to research, cartography, historical photos and public memory.

### 4. Mountain passes are conditional connections

A pass is a persistent route edge whose practical state can depend on snow, slope failure, maintenance, transport service, fire, wildlife activity or closures. Travel remains authoritative for route/service status.

### 5. Staging sites are high-value narrative nodes

Mountain huts, shelters, survey stations, cable stations, ranger cabins or informal camps can combine:

- weather reports;
- field observations;
- rescue staging;
- rumors;
- supplies;
- social callbacks;
- route decisions;
- scientific monitoring;
- expedition handoffs.

They should not automatically become healing stations or fast-travel nodes.

### 6. Mountain ecology should be cross-layered

Mountain state can feed:

- Cryosphere for snow/ice;
- Meteorology for exposure and forecast;
- Soil for thin/unstable substrates;
- Freshwater for headwaters;
- Flora for treeline/meadows;
- Wild Collectives for seasonal group use;
- Travel for passes/staging;
- Cartography for route editions;
- Aerial for ridge/flight corridors;
- Crisis for rescue/closure;
- Architecture for huts/cable stations;
- Tourism for summit pressure.

No single mountain layer should silently own those systems.

## PTU / AutoPTU evidence boundary

The available Python AutoPTU snapshot contains a concrete Wilderness Guide branch for `mountain`/`cave` that grants a specific temporary hazard-immunity effect when that Trainer Feature is actually used. This is narrow rule evidence.

It does not establish:

- generic mountain hazard immunity;
- climbing rules;
- altitude penalties;
- falling rules;
- exposure damage;
- cliff cover;
- summit bonuses;
- high-altitude Weather;
- mountain movement bonuses for Gogoat/Avalugg;
- automatic Naturewalk;
- free Mountable traversal.

Available evidence reference:

Project file-library `battle_state.py` snapshot, where Wilderness Guide has an authored `mountain`/`cave` branch.

Primary Caelo PDFs were not reliably recoverable in this runtime. No new Caelo-specific mountain rule is claimed here.

## Sources retained for future authoring

- https://www.pokemon.com/uk/pokedex/gogoat
- https://www.pokemon.com/us/pokedex/avalugg
- https://bulbapedia.bulbagarden.net/wiki/Sky_Peak
- https://bulbapedia.bulbagarden.net/wiki/Sky_Peak_Mountain_Path
- https://pokemontabletop.com/wiki/index.php/Quest%3AAdventures
- https://pokemontabletop.com/wiki/index.php/Quest%3AA_Song_of_Ice_and_Ire
- https://www.nps.gov/articles/000/alpine-vegetation-resource-brief.htm
- https://www.nps.gov/articles/denali-treeline-shifts.htm
- https://www.nps.gov/teachers/classrooms/aspect-treeline-climate.htm
- https://www.nps.gov/mora/learn/nature/plants.htm
- https://www.nps.gov/olym/learn/nature/alpine.htm
- https://www.nps.gov/olym/learn/nature/subalpine.htm
- https://www.nps.gov/noca/learn/nature/life-zones.htm

## Promotion boundary

Nothing in this scan is canon.

Before promotion, authored Ouros mountains still need explicit decisions about regional geography, long-term treeline history, settlements, trails, huts, transport, cultural meaning, stewardship, named species relationships and any PTU/Caelo mechanical interaction.