# Ouros Urban Stormwater, Drainage & Green Infrastructure Research — Pass 90

Status: Research and provenance only. Not established Ouros canon.

## Research question

How can Ouros represent urban rainfall, runoff, drains, culverts, detention/retention systems, stormwater overflows and green infrastructure as persistent world state without duplicating Freshwater, Sanitation, Architecture, Crisis or PTU battle rules?

## Why this is a new gap

Existing layers already own:
- regional rainfall and forecasts: Meteorology;
- river/catchment hydrology: Freshwater;
- wastewater, refuse and sanitation services: Waste/Sanitation;
- buildings and physical urban form: Architecture;
- road corridors and road-stream crossings: Road Ecology;
- emergency response to flooding: Crisis;
- urban heat and shade: Urban Heat;
- tactical terrain/weather/hazards: AutoPTU-Java.

What remained missing was the causal middle layer:

rainfall on built surfaces → runoff generation → conveyance/storage/infiltration → overflow or controlled release → receiving water / street / soil consequences.

This pass treats that middle layer as infrastructure and hydrology, not as automatic combat mechanics.

## Public Pokémon references

### Castelia Sewers as infrastructure + route + habitat

Pokémon Black 2 / White 2 uses Castelia Sewers as a traversable urban sewer system connected to Sightseeing Pier, additional city access and Relic Passage. This is useful structurally because one infrastructure network can simultaneously be:
- a service space;
- a movement network;
- an ecological habitat;
- a hidden route;
- a setting for investigation or conflict.

Source:
https://www.serebii.net/black2white2/unova.shtml

Bulbapedia also records that the sewers have flooded and dry layouts and that they contain multiple Pokémon encounters. This reinforces that operational state and habitat can vary without changing the identity of the network.

Source:
https://bulbapedia.bulbagarden.net/wiki/Castelia_City_Sewers

Reusable lesson:
The underground drainage network should have persistent identity independent of whether a given reach is wet, dry, accessible, blocked or currently occupied by Pokémon.

Do not copy Castelia layout, encounter tables, Team Plasma content or specific story beats.

### Canalave sewer wildlife

In "Leading a Stray!", a Wailmer becomes stranded within a sewer while other Pokémon are already using the underground system. The story turns the sewer into an ecological corridor and rescue space rather than simple background scenery.

Source:
https://bulbapedia.bulbagarden.net/wiki/Leading_A_Stray

Reusable lesson:
Drainage infrastructure can accidentally trap, redirect or shelter Pokémon. The correct response may be rescue, route restoration or investigation rather than combat.

Do not copy Luxio's group, the exact rescue method, dialogue or episode plot.

### PTU worldbuilding principle

Public PTU worldbuilding guidance emphasizes believable ecosystems alongside enjoyable progression. Urban drainage therefore should not exist only when a quest needs a sewer dungeon; the network should have normal functions, ordinary maintenance and ecological consequences even when nothing dramatic is happening.

Source:
https://pokemontabletop.fandom.com/wiki/Populating_Your_World

This is secondary/publicly reproduced PTU guidance and not a replacement for the project's primary PTU/Caelo corpus.

### PTU flood design warning

A public PTU community discussion proposes flash-flood terrain ideas. It is useful only as evidence that GMs experiment with flooding as encounter context. Its proposed mechanics are not authoritative for Ouros.

Source:
https://www.tapatalk.com/groups/pokemon_tabletop/special-terrain-ptu-t3434.html

Reusable lesson:
Flooding can change encounter premise and access, but exact penalties, damage, movement effects and Skill checks must come from governing PTU/Caelo rules and verified engine support.

## External hydrology and urban-design research

### Impervious surfaces change runoff behavior

USGS describes roads, rooftops, parking lots, driveways and sidewalks as impervious surfaces that reduce infiltration and route rainfall rapidly into storm sewers and receiving streams. Urbanization can shorten runoff lag time and increase peak discharge.

Sources:
https://pubs.usgs.gov/pp/pp1726/pp1726.pdf
https://pubs.usgs.gov/pp/1003/report.pdf

Reusable lesson:
Ouros should not store only "rain intensity". A district's response depends on built surface, soil, drainage capacity, storage and connection to receiving waters.

### Stormwater also transports pollutants

USGS notes that urban stormflow can carry contaminants accumulated on built surfaces into streams. The important design lesson is provenance: a pollutant detected after rain may have many possible upstream sources.

Source:
https://pubs.usgs.gov/fs/2015/3056/fs20153056.pdf

Reusable lesson:
A stormwater sample should create observations and source hypotheses, not an automatic accusation against the nearest workshop, road or business.

### Green infrastructure has different functions

EPA guidance distinguishes infiltration, retention/detention, filtration and evapotranspiration. Site conditions matter: groundwater level, slopes, soils, climate, utilities and available land can change which approach is appropriate.

Source:
https://www.epa.gov/sites/default/files/2015-09/documents/massbays_handbook_combined_508-opt_1.pdf

Reusable lesson:
A rain garden, detention basin, infiltration trench, tree pit and storage tank should not all be represented as one universal "green infrastructure" upgrade. Each has a different purpose and failure mode.

## High-value design conclusions

### 1. Separate stormwater from wastewater

A storm drain primarily moves rainfall/runoff. A sanitary sewer primarily carries wastewater. Some places may have combined or linked systems only if authored canon explicitly establishes that configuration.

The generator must not infer sewage contamination merely because a drain overflowed.

### 2. Model the network as connected reaches and assets

Useful entities include:
- catchment/drainage zones;
- inlets;
- pipes;
- open channels;
- culverts;
- detention/retention basins;
- infiltration areas;
- pump stations;
- outfalls;
- overflow points;
- rain gardens / bioswales / permeable areas;
- receiving waters.

### 3. Capacity and blockage are different causes

A street can flood because:
- rainfall exceeded design capacity;
- an inlet was blocked;
- a pump failed;
- a downstream outfall was submerged;
- a basin was already full;
- soil infiltration was poor;
- construction changed flow paths;
- multiple smaller failures aligned.

Do not jump from "water in street" to "drain blocked".

### 4. Drainage infrastructure can be habitat

Pipes, culverts, channels, basins and wet outfalls can become recurring Pokémon habitat or movement corridors.

The ecological role can persist even when humans consider the asset purely technical.

### 5. Maintenance creates useful low-stakes hooks

Routine work can include:
- cleaning inlets;
- inspecting culverts;
- clearing sediment;
- checking pumps;
- verifying basin drawdown;
- replacing sensors;
- checking erosion near outfalls;
- recording unexpected Pokémon use.

Most maintenance should compress unless a meaningful decision or anomaly exists.

### 6. Green infrastructure should create tradeoffs

A retention basin may reduce peak flow but occupy land.
A bioswale may improve filtration but require maintenance.
A tree trench may support shade and runoff control but conflict with buried utilities.
A wet basin may become habitat and later create stewardship questions.

No project should grant an automatic "city resilience" score.

### 7. Flood aftermath belongs to multiple layers

Stormwater owns the runoff/conveyance event.
Crisis owns emergency response.
Freshwater owns receiving-river consequences.
Waste/Sanitation owns wastewater contamination when actually present.
Soil owns erosion/compaction.
Architecture owns building condition.
Health Surveillance owns aggregate health signals.
Conservation/Ecology own habitat response.

### 8. Underground exploration should preserve service logic

A sewer or stormwater tunnel used as a dungeon should still have:
- a reason it exists;
- upstream/downstream connections;
- maintenance access;
- operational states;
- plausible water routing;
- consequences if players alter gates, pumps or channels.

This makes exploration feel embedded in the city rather than pasted underneath it.

## Candidate research-to-Ouros patterns

- A district floods only during short intense storms despite normal annual rainfall.
- A retention basin becomes a seasonal habitat and creates a management conflict.
- An old culvert still carries water but no longer passes a migrating Pokémon population.
- A green-roof program reduces runoff in one district but maintenance failures make performance uneven.
- A storm drain conveys a pollution pulse whose source is initially unclear.
- Construction changes a curb line and silently redirects runoff toward an older neighborhood.
- A pump station outage matters only because the downstream river is simultaneously high.
- A "blocked drain" rumor is wrong; the system was operating correctly but beyond capacity.
- An underground route becomes accessible during dry weather and unsafe during storms.
- A wild Pokémon group uses a detention basin long enough that a maintenance project becomes an ecological decision.

## Copyright / originality boundary

Use only high-level structural lessons from Pokémon games, animation, public PTU material and other games.

Do not copy:
- exact dungeon layouts;
- dialogue;
- named NPCs or factions;
- distinctive plots;
- encounter tables;
- puzzle sequences;
- proprietary rules text.

## Mechanical boundary

Nothing in this research authorizes:
- flood damage;
- drowning;
- current or knockback;
- mud/rough terrain;
- Accuracy penalties;
- Poisoned from runoff;
- movement penalties in water;
- pump/gate HP;
- environmental initiative;
- rescue checks;
- sewer-gas effects;
- electrical-water interactions;
- automatic Weather or Terrain.

Those require PTU/Caelo validation plus current AutoPTU-Java implementation evidence.

## Sources used this pass

1. Serebii — Black 2 / White 2 Unova and Castelia Sewers
   https://www.serebii.net/black2white2/unova.shtml
2. Bulbapedia — Castelia Sewers
   https://bulbapedia.bulbagarden.net/wiki/Castelia_City_Sewers
3. Bulbapedia — Leading a Stray!
   https://bulbapedia.bulbagarden.net/wiki/Leading_A_Stray
4. Pokémon Tabletop community / reproduced worldbuilding guidance
   https://pokemontabletop.fandom.com/wiki/Populating_Your_World
5. PTU community special-terrain discussion
   https://www.tapatalk.com/groups/pokemon_tabletop/special-terrain-ptu-t3434.html
6. USGS — urban impervious surfaces and streamflow
   https://pubs.usgs.gov/pp/pp1726/pp1726.pdf
7. USGS — effects of urbanization on streamflow
   https://pubs.usgs.gov/pp/1003/report.pdf
8. USGS — urbanization and storm runoff contaminants
   https://pubs.usgs.gov/fs/2015/3056/fs20153056.pdf
9. EPA — coastal stormwater management through green infrastructure
   https://www.epa.gov/sites/default/files/2015-09/documents/massbays_handbook_combined_508-opt_1.pdf

## Research gaps for later passes

- exact PTU/Caelo rules for water hazards, drowning, movement and environmental effects;
- whether Ouros regions use separated, combined or mixed sewer systems;
- what stormwater assets exist in each settlement before player intervention;
- which Pokémon species have authored urban-drain habitat relationships;
- how Minecraft changes to streets/roofs should update coarse runoff state without per-block hydrology;
- how long drainage/storage state advances when chunks are unloaded;
- whether any stormwater system should ever project dynamic water into a battle rather than freezing a safe battle snapshot.
