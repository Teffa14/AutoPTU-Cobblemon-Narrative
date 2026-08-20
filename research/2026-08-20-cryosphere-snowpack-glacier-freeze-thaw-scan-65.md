# Cryosphere, Snowpack, Glaciers & Freeze-Thaw — Research Scan

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. No PTU mechanic is established by this document.

Pass: 65
Date: 2026-08-20

## Why this pass exists

The repository already has dedicated layers for seasonality, meteorology, freshwater hydrology, geology, crisis response, conservation, travel, cartography, architecture and wildfire recovery.

Those systems can say that winter exists, snow is falling, a river receives meltwater or a route is closed. They do not yet provide one persistent contract for the cold landscape itself.

The missing distinctions are:

- current weather versus accumulated snowpack;
- snowfall depth versus snow-layer structure;
- seasonal snow versus perennial ice;
- glacier identity versus the visible ice surface of one year;
- frozen water surface versus safe route eligibility;
- freeze-thaw change versus generic weather variation;
- avalanche observation versus avalanche forecast or cause;
- glacier retreat versus deglaciated successor habitat;
- meltwater contribution versus rainfall contribution;
- cold-region ecology versus invented Ice-type battle effects.

This pass researches that missing layer without replacing Seasonality, Meteorology, Freshwater, Crisis or Conservation.

## Source findings

### Pokémon winter routes can combine transport, wildlife and care

The official episode “Over the Mountain of Snow!” places a journey across a large snowy mountain behind a transport decision. The travelers use Mamoswine for the crossing. Their route changes when the Pokémon lead them toward Frost Cavern, where an Abomasnow is guarding a sick Snover.

Source:
https://www.pokemon.com/us/animation/seasons/18/episode-17-over-the-mountain-of-snow

Reusable structures:

- winter travel can depend on a service or suitable partner rather than a universal movement ability;
- a route deviation can expose an ecological or care problem instead of an ambush;
- a cold crossing may require staging, route knowledge and shelter;
- the Pokémon providing transport can notice information that the travelers did not have.

Do not copy the episode sequence, characters or specific resolution.

### Heavy snow can create shelter and timing pressure without requiring combat damage

The official Pokémon Horizons episode “Roy and Fuecoco's First Snow!” uses heavy snowfall, a mountain cabin, firewood gathering, temporary separation and the approach of night as the main pressure.

Source:
https://www.pokemon.com/us/animation/horizons/2/roy-and-fuecocos-first-snow

Reusable structures:

- shelter can be meaningful world infrastructure;
- cold-route scenes can create decisions through time, visibility and separation;
- preparation can matter before a battle exists;
- a safe cabin can become a persistent route asset.

Mechanical boundary:

The episode does not establish PTU cold damage, hypothermia, visibility penalties, movement costs or survival DCs.

### A winter storm can change resource competition between wild groups

“The Beartic Mountain Feud!” presents a storm that damages local food resources and contributes to competition between groups of Beartic.

Source:
https://www.pokemon.com/us/animation/seasons/25/episode-54-the-beartic-mountain-feud

Reusable structure:

storm → resource loss → changed movement/competition → investigation → alternative resource or route response.

This is stronger for Ouros than treating every post-storm wild encounter as random aggression.

Do not copy the groups, characters or episode resolution.

### Snow quality can itself be ecological information

The official Pokédex states that Snom eats snow and prefers soft, freshly fallen snow while climbing toward mountain peaks.

Source:
https://www.pokemon.com/us/pokedex/snom

Reusable structure:

- snow age and condition can matter to local observations;
- fresh-snow zones can shift animal presence without altering species stats;
- a change in snow quality can generate research before any population change is declared.

Species-specific behavior must remain species-specific.

### Snowline movement can be part of seasonal Pokémon movement

The official Pokédex states that Snover gathers around footprints on snowy mountains and moves to lower elevations during colder seasons before returning toward snow-covered summits in spring.

Source:
https://www.pokemon.com/us/pokedex/snover

Reusable structure:

- snowline and elevation can interact with seasonal movement;
- the same route can host different observations as snow retreats or accumulates;
- a lower-than-usual observation is evidence, not immediate proof of climate change or population decline.

### Ice can preserve paleontological context

“Coming Back into the Cold!” uses Amaura and Aurorus revived from fossils discovered in ice and establishes their need for a cold environment after revival.

Source:
https://www.pokemon.com/us/animation/seasons/17/episode-23-coming-back-into-the-cold

Reusable structure:

- glacier or perennial ice can preserve material that links Geology, Archives, Science and Care;
- exposure by melt can create a discovery window;
- recovery from ice should preserve provenance before extraction;
- revival, custody and care remain separate systems.

Do not infer a universal preservation timer, temperature requirement or fossil-revival rule.

### Ice can be cultural space, not only hazard

The official Alolan Sandshrew Pokédex describes a local tradition of sliding Sandshrew across ice.

Source:
https://www.pokemon.com/us/pokedex/sandshrew

Reusable structure:

- frozen surfaces can support seasonal recreation and public events;
- a winter route can have cultural value independent of transport;
- changing ice conditions can alter an event without requiring a crisis.

Do not copy the exact tradition into Ouros. Create original regional practices if this theme becomes canon.

### Seasonal Pokémon folklore must remain separate from observation

The official Cryogonal Pokédex includes seasonal behavior and also a folklore claim about people who died on snowy mountains.

Source:
https://www.pokemon.com/us/pokedex/cryogonal

Design lesson:

Keep biological observation, local belief and supernatural truth separate. A seasonal Cryogonal sighting can be recorded without validating the folklore attached to it.

### Public fangame work reinforces the value and risks of cold exploration

Pokémon Glacial Chronicles presents a harsh cold-region journey with survival, exploration and puzzles. Public player feedback also notes visual overload during storms and navigation/soft-lock concerns in difficult terrain.

Source:
https://eeveeexpo.com/threads/12569/

Pokémon Glacier Shards uses a winter island, an exploration guild, quests, caves and mining. Public discussion includes route-state issues where checkpoints or travel systems can undermine a landslide gate.

Source:
https://eeveeexpo.com/threads/9594/

Reusable structures:

- cold-region exploration can support professional guilds and repeated expeditions;
- severe-weather presentation needs accessibility alternatives;
- route state must be authoritative so fast travel cannot bypass a closure accidentally;
- recovery routes and reset logic matter in snow/ice puzzles.

Do not copy regions, factions, characters, stories or mechanics from either project.

## Cryosphere research outside Pokémon

### Snowpack is layered history, not a single depth value

Avalanche.org describes snowpack as layered and spatially variable. Individual layers preserve evidence of storms, wind, warming and dry periods, and continue to change after deposition.

Sources:
https://avalanche.org/avalanche-encyclopedia/snowpack
https://avalanche.org/avalanche-encyclopedia/snowpack/snow-layer

Reusable structure:

- store coarse snowpack versions rather than only `snow=true`;
- a snow pit or field observation can reveal history without revealing the entire regional truth;
- two nearby slopes can legitimately have different snow states;
- earlier weather can matter after the storm has ended.

Ouros should not simulate individual snow crystals or import avalanche thresholds.

### Avalanche hazard is spatial and time-scoped

Avalanche.org separates terrain, current snowpack, observations and forecast products. Hazard varies by place and time; terrain remains comparatively stable while snow conditions change.

Sources:
https://avalanche.org/avalanche-encyclopedia/avalanche-basics
https://avalanche.org/avalanche-encyclopedia/terrain
https://avalanche.org/avalanche-encyclopedia/avalanche-forecast
https://avalanche.org/avalanche-encyclopedia/snowpack/snowpack-observations

Reusable structure:

terrain + current snowpack + observations → scoped hazard assessment → route decision.

The assessment must remain a forecast, not canonical certainty.

Do not import danger scales, slope thresholds, trigger probabilities or real-world travel instructions as game mechanics.

### Glaciers connect climate, freshwater and new terrain

USGS describes glaciers as gaining snow and ice during accumulation periods and losing mass through melting and other processes. Glacier melt contributes to streams and lakes, while retreat can alter water supply, habitat and landscape stability.

Source:
https://www.usgs.gov/programs/water-resources/science/snow-ice-and-permafrost

Reusable structure:

- glacier body identity persists across yearly geometry changes;
- accumulation and loss can be coarse world-state trends;
- meltwater should connect into the existing catchment graph;
- retreat can expose new land, rock, artifacts or habitats;
- a disappearing ice edge is not the same as the glacier entity ceasing to exist.

### Deglaciation can create succession, not empty terrain

National Park Service research documents wildlife and ecosystem colonization as glaciers retreat and new surfaces become available.

Source:
https://www.nps.gov/articles/000/wildlife-colonization-following-glacier-retreat.htm

Reusable structure:

freshly exposed substrate → pioneer observations → developing habitat → later established ecological patch.

This can connect the Geology, Conservation, Science and Wild Collective layers over many world years.

### Avalanche paths can also function as habitat

National Park Service research on avalanche cycles describes recurring avalanche paths as landscape features that can maintain open habitat used by wildlife.

Source:
https://www.nps.gov/articles/000/avalanche-cycles-and-wildlife.htm

Reusable structure:

An avalanche path can be simultaneously:

- a hazard corridor under some conditions;
- an ecological opening;
- a route constraint;
- a survey site;
- a historical landscape feature.

Do not reduce it to `dangerous tile`.

### Glacier retreat can create new lake hazards

USGS work on glacial lake outburst floods shows that retreating ice and moraines can create or destabilize lakes. Sudden drainage can send water, sediment and debris downstream.

Sources:
https://www.usgs.gov/programs/water-resources/science/glacier-related-outburst-floods
https://www.usgs.gov/observatories/cvo/science/glacial-outburst-flood-hazards

Reusable structure:

glacier retreat → lake formation/change → observation and monitoring → possible downstream crisis.

This should connect to Freshwater and Crisis. It should not produce a random flood because the story needs one.

### Snow and glacier melt can matter late in the dry season

National Park Service hydrologic material notes that mountain snowpack and glacier melt can sustain streamflow after seasonal precipitation has declined.

Source:
https://www.nps.gov/articles/000/glacier-hydrologic-activity.htm

Reusable structure:

- a low snowpack can matter months later;
- irrigation, wetlands, fisheries and settlements can experience delayed consequences;
- water-state changes should flow through the catchment graph rather than spawn independent quests.

### Permafrost needs its own ground-state boundary

USGS describes permafrost with an active layer that thaws and refreezes, influencing water movement, soil and nutrients.

Source:
https://www.usgs.gov/programs/water-resources/science/snow-ice-and-permafrost

Reusable structure:

- frozen ground can have seasonal versions;
- thaw can affect foundations, drainage and habitat;
- permafrost change should connect Architecture, Infrastructure and Freshwater;
- Minecraft block appearance cannot become the authority for whether ground is frozen.

## Cross-system lessons for Ouros

### Cryosphere state should sit between weather and hydrology

Recommended causal chain:

weather observations → snowfall / temperature history → snowpack state → melt/freeze event → route/ecology/infrastructure impacts → freshwater contribution → later recovery or seasonal reset.

Weather does not directly rewrite a river or route unless the intermediate state supports it.

### Glacier state needs long memory

A glacier can have:

- stable identity;
- mapped terminus versions;
- accumulation/ablation trend;
- exposed sites;
- meltwater connections;
- adjacent lakes;
- observation history;
- public interpretation.

The visible ice geometry is one version, not the whole object.

### Forecast and observation must remain separate

A forecast can say a pass is likely unsafe. A field party can observe different local conditions. Neither automatically rewrites the other.

A later review can compare forecast, actual conditions and route outcome.

### Cold routes need anti-softlock policy

If a winter path becomes invalid after a player enters it, the server needs one of:

- safe return route;
- shelter/checkpoint;
- extraction service;
- explicit temporary instance policy;
- rollback to last valid route state.

Fast travel must not silently bypass a closed pass unless the travel system explicitly authorizes that bypass.

### Accessibility applies to snowstorms too

Whiteout, blowing snow and particle-heavy storms should not make critical navigation dependent only on low-contrast visual cues. Route markers, subtitles, map state, sound cues or UI information should provide equivalent information where appropriate.

## PTU / AutoPTU mechanical evidence

Project evidence from Python AutoPTU contains specific cold-environment logic:

- terrain labels such as tundra, snow and ice can map to a tundra environment for selected Move/Feature behavior;
- hail/snow weather has specific damage/immunity handling;
- `Frozen Domain` exists as one explicit hazard with an Acrobatics check and possible Tripped result;
- selected Trainer Features reference Ice Moves, `Naturewalk (Tundra)` and tundra-specific effects.

These are narrow implementation examples.

They do not prove:

- general ice-slip rules;
- snow depth movement penalties;
- avalanche mechanics;
- glacier collapse;
- hypothermia;
- snow blindness;
- crevasse damage;
- frozen-water load limits;
- general cold exposure;
- Java parity for every listed Python behavior.

AutoPTU-Java remains incomplete for terrain, hazards, reactions and broad environmental execution.

## Copyright and transformation boundary

External Pokémon stories, fangames and RP material are used only to identify high-level structures. Ouros material must use original locations, institutions, characters, conflicts and resolutions.

Do not copy episode plots, dialogue, distinctive NPCs, region names, quest text, custom fangame mechanics or proprietary maps.

## Research gaps for later passes

- exact PTU/Caelo text for Snow, Hail, Frozen, tundra terrain and cold-environment effects;
- exact treatment of Naturewalk (Tundra), Heater and relevant Ice capabilities;
- whether any PTU/Caelo rule covers exposure, thin ice, avalanche or crevasse hazards;
- Cobblemon hooks for snow layers, freezing, weather and biome state;
- safe world-state projection for snowpack without simulating every snow block;
- how much glacier geometry should change in Minecraft over long world times;
- whether any region-specific winter culture becomes canon in Ouros.
