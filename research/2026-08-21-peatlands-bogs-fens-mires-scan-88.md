# Peatlands, Bogs, Fens & Mires Research Scan — Pass 88

Status: RESEARCH ONLY. Not Ouros canon. Not a PTU/Caelo rules source.

Date: 2026-08-21

## Why this pass exists

The repository already models wetlands through Freshwater, Estuaries, Soil, Conservation, Wildfire, Road Ecology and Aridity. It did not yet have a dedicated persistent model for peat-forming wetlands.

That gap matters because peatlands preserve slow history through water table, organic-soil accumulation, drainage, subsidence, decomposition, fire, rewetting and vegetation change. A bog, fen, wooded peatland or other mire can remain the same place while its hydrology and ecological function change for decades.

The research goal for this pass is therefore not “make a swamp biome.” It is to extract structures for persistent wetland history without inventing PTU terrain, status, environmental damage or Cobblemon spawn rules.

## Source boundaries

This scan uses public Pokémon material for species/worldbuilding patterns and public scientific sources for hydrology/restoration structure.

No protected dialogue, distinctive fan characters or plots are copied.

Scientific institutions and real restoration programs are design references only. Their names, governance and culturally specific practices are not imported into Ouros.

The available PTU/Caelo corpus was checked again. Full primary Caelo source text was not reliably recoverable during this runtime. Therefore no new Caelo rule is asserted here.

AutoPTU and AutoPTU-Java were inspected read-only for implementation boundaries.

## Pokémon material

### Wooper — wetlands can support repeated group movement

Official Pokédex source:
https://www.pokemon.com/us/pokedex/wooper

The official material describes Wooper travelling in groups through wetlands. The reusable structure is not a universal Wooper “swamp mechanic.” It is that a wetland route may contain repeated, observable movement by a collective whose timing and path can become part of a regional baseline.

Useful Ouros translation:

- group passage can be observed over several seasons;
- a missing route can become a research question;
- a boardwalk, ditch or road can intersect the same path;
- one observation does not prove population size or ownership of the site.

Do not infer Swim, Naturewalk, herd AI, capture behavior or terrain bonuses from the Pokédex description.

### Ducklett — bog-associated resources can be part of foraging behavior

Official Pokédex source:
https://www.pokemon.com/us/pokedex/ducklett

The official material includes Ducklett searching ponds for bog moss. The useful design lesson is that a plant/resource patch can matter because of repeated Pokémon use, not because it is a magical pickup node.

Useful Ouros translation:

- a moss patch can have observation history;
- disappearance of the patch can alter a known foraging route;
- several explanations can remain open: water level, trampling, seasonal timing, disturbance or survey error;
- collecting material for research must preserve provenance and stewardship rules.

Do not convert “bog moss” into healing, Food Buffs, crafting yield or spawn bonuses without an authored rule.

### Stunfisk — “mud” has context and should not be treated as one universal substrate

Official Pokédex source:
https://www.pokemon.com/us/pokedex/stunfisk

The official material associates Stunfisk with muddy environments and its Galarian form with iron-rich mud. The reusable lesson is classification discipline: dark mud, mineral-rich mud, peat soil and ordinary wet sediment should remain different observations until evidence supports a stronger interpretation.

Do not use Stunfisk presence to prove peat, iron, hazards or Ground-type terrain.

## Pokémon roleplay / campaign structure

### Expedition reporting works well for remote wetland exploration

Public Pokécharms source:
https://forums.pokecharms.com/threads/exploration-of-the-froena-region-sign-ups.17832/

This public Pokémon RP sets up a dangerous regional expedition with supplies, field reports, waterproof communication and distinct biomes including swamp. The reusable structure is expedition reporting: a remote wetland becomes more interesting when players return observations, update maps, compare routes and trigger follow-up work instead of clearing the area once.

For Ouros this supports:

- field stations or temporary boardwalk camps;
- survey reports with provenance;
- SOS/rescue contingencies;
- conflicting maps from different dates;
- exploration that creates knowledge rather than permanent conquest.

No names, characters, region geography or plot are imported.

### PTU module culture supports portable, bounded field problems

Public PTU community source:
https://www.reddit.com/r/PokemonTabletop/comments/itlrso

The community module collection demonstrates a recurring PTU practice: bounded adventures can be transplanted into a larger campaign if mechanics and Pokémon are regenerated for the local setting. The useful lesson for peatlands is to create portable field-problem structures — survey, rescue, restoration inspection, route reopening, missing-observation investigation — while leaving species, mechanics and local history authored per region.

No community module text is copied into Ouros.

## Peatland hydrology and classification

### Fen and bog are hydrologically different concepts

NPS source:
https://home.nps.gov/romo/peatlands.htm

NPS describes peat as organic-rich soil formed where waterlogging and/or cold limits decomposition, and distinguishes peatland types by water source. It describes fens as receiving water and nutrients from groundwater/soil/rock as well as precipitation.

Additional NPS fen source:
https://www.nps.gov/places/the-fen.htm

This page describes a fen as a peat-forming wetland fed by groundwater and notes that seasonal flooding can still occur.

Reusable Ouros lesson:

- visible wetness does not establish peatland type;
- water source matters;
- two similar-looking sites may have different hydrologic dependencies;
- a map label can remain provisional until field evidence improves.

The world model should therefore store `peatland_type_assessment`, not bake BOG/FEN truth into a block palette.

### Water table is a core state variable, not a universal health score

USGS source:
https://www.usgs.gov/publications/hydrologic-restoration-decreases-greenhouse-gas-emissions-shrub-bog-peatlands

The study found that hydrologic restoration raised water levels and changed multiple greenhouse-gas fluxes in different directions while lowering overall greenhouse-gas emissions in that study. Water-table depth and soil temperature explained substantial parts of observed variation.

Reusable Ouros lesson:

- one intervention can improve one metric while another moves in the opposite direction;
- restoration should not use a single “health +20” result;
- monitoring should preserve several observations and interpretations;
- rewetting outcomes should be reviewed after implementation.

Ouros does not need to simulate greenhouse gases numerically. Scientific claims can exist as research records without becoming a gameplay stat.

### Drainage networks can reshape a peatland for decades

USGS source:
https://www.usgs.gov/publications/hydrology-and-water-quality-great-dismal-swamp-virginia-and-north-carolina-and

The Great Dismal Swamp study links historic timber drainage ditches with altered wetland forests, peat subsidence/decomposition and increased fire risk. It also shows how roads, ditches, water-control structures, peat layers and groundwater sources interact in complex ways.

Reusable Ouros lesson:

- an old ditch can remain causally important long after its original industry disappears;
- roads and spoil banks can change water movement;
- a restoration structure can affect several adjacent zones differently;
- the same peatland can contain zones with different hydrologic behavior;
- management requires observations, not merely placing a weir and declaring success.

This links directly to Road Ecology, Freshwater, Infrastructure, Soil and Wildfire.

### Climate stress can alter peat accumulation and physical structure

USGS 2025 source:
https://www.usgs.gov/publications/effects-climate-change-midwestern-ecosystems-north-american-bog-and-fen

This report describes bog/fen vulnerability to water deficits and warming, including lower water tables, faster aerobic decomposition, reduced moss/sedge productivity, subsidence and compaction.

Reusable Ouros lesson:

- a peatland can change slowly during several “normal” seasons;
- a drought year can matter even without a crisis event;
- physical ground elevation/structure may change after repeated drying;
- old boardwalk elevations or survey markers can become historical evidence.

### Peatland recovery has long time horizons

USGS and related public-source synthesis show that hydrology, vegetation, peat structure and fire risk may respond on different schedules. Rewetting is an intervention, not a reset button.

This is ideal for the Ouros Chronicle because a site can retain visible consequences of decisions made years earlier.

## Design structures worth carrying forward

### 1. Water-source provenance

A peatland should record whether its wetness is currently interpreted as precipitation-fed, groundwater-fed, surface-flow-supported or mixed. That interpretation can be revised.

### 2. Water-table revision history

A coarse water-table state can change through seasons, drought, drainage, restoration and infrastructure failure.

It should not produce PTU terrain automatically.

### 3. Drainage legacy graph

Historic ditches, roads, culverts, extraction cuts and control structures can remain causal edges in the world graph even if they look minor in Minecraft.

### 4. Subsidence/decomposition observations

Repeated benchmarks can reveal slow physical change. One low survey marker does not prove cause.

### 5. Rewetting project with monitoring

A restoration project needs baseline, intervention, expected mechanisms, observation schedule and review. Success may be partial or spatially uneven.

### 6. Peat-fire distinction

Wildfire owns active fire/crisis state. The peatland layer can record verified below-surface peat involvement, persistent burn footprint and hydrologic consequence. Smoke alone does not prove a peat fire.

### 7. Boardwalk and access history

Wetland access can change with water table, frost, maintenance, restoration policy or ecological sensitivity. The same route may be open to researchers but closed to ordinary visitors.

### 8. Long-memory archaeology

Peat can preserve long environmental and cultural histories. Any artifact discovery must route through Archaeology/Custody/Collections. Peat preservation does not justify inventing spectacular intact finds on demand.

## Anti-copying / copyright guardrail

No distinctive campaign plot, named fan character, dialogue, fan region or module text is imported.

The public RP and PTU community material is used only to identify high-level expedition/reporting structures.

Pokémon species are referenced only for public factual behavior descriptions and potential Ouros hooks.

## Mechanical boundary

No source inspected in this pass authorizes these automatic effects:

- bog/mire = Rough Terrain;
- peat = Slow Terrain;
- dark water = Poisoned;
- floating mat = falling hazard;
- drainage ditch = movement penalty;
- smoke = Accuracy penalty;
- saturated soil = Stuck;
- bog moss = healing;
- peat fire = Burned;
- Wooper/Ducklett/Stunfisk presence = terrain bonus or spawn modifier.

Exact PTU/Caelo mechanics must be validated separately.

## Engine-relevant implications

The permanent capability map should remain conservative.

The Java head inspected for this pass is `f4a5232b406fe0c80137e4d1d2f8408771ab4ba0`. It now runs canonical field progression through `ROUND_START`, but current evidence still does not prove a complete environmental rules family.

Python AutoPTU remains at `e4bb0ca38b7018710af476ce365d515a387de4e7`; its latest visible changes are Career-related.

A peatland encounter that requires unstable ground, spreading underground fire, changing water levels, forced movement, entry/exit reactions or AI that deliberately finds safe hummocks remains dependent on blocking capability families.

## Source register

1. Pokémon — Wooper Pokédex
   https://www.pokemon.com/us/pokedex/wooper
2. Pokémon — Ducklett Pokédex
   https://www.pokemon.com/us/pokedex/ducklett
3. Pokémon — Stunfisk Pokédex
   https://www.pokemon.com/us/pokedex/stunfisk
4. Pokécharms — Exploration of the Froena Region Sign Ups
   https://forums.pokecharms.com/threads/exploration-of-the-froena-region-sign-ups.17832/
5. PokémonTabletop community — PTU Module Collection
   https://www.reddit.com/r/PokemonTabletop/comments/itlrso
6. National Park Service — Mired in Peatlands
   https://home.nps.gov/romo/peatlands.htm
7. National Park Service — The Fen
   https://www.nps.gov/places/the-fen.htm
8. USGS — Hydrologic restoration decreases greenhouse gas emissions from shrub bog peatlands
   https://www.usgs.gov/publications/hydrologic-restoration-decreases-greenhouse-gas-emissions-shrub-bog-peatlands
9. USGS — Hydrology and water quality of the Great Dismal Swamp
   https://www.usgs.gov/publications/hydrology-and-water-quality-great-dismal-swamp-virginia-and-north-carolina-and
10. USGS — Effects of climate change on midwestern ecosystems: North American bog and fen
    https://www.usgs.gov/publications/effects-climate-change-midwestern-ecosystems-north-american-bog-and-fen

## Next research directions

Future passes can deepen this system by locating reliable primary PTU/Caelo text for Wetland/Naturewalk/Survival interactions, checking exact Python habitat labels, and researching peat extraction/cultural history only when Ouros has an authored region where that material is relevant.

No claim in this file is promoted to canon.