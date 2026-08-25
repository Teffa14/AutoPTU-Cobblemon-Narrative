# Seismicity, Earthquakes, Aftershocks and Ground Failure — Research Scan 164

Status: RESEARCH / PROVENANCE ONLY. NON-CANON. This file records external sources and reusable design lessons. It does not establish Ouros geography, event history, technology, Pokémon behavior, hazards or PTU mechanics.

Date researched: 2026-08-25

## Deduplication and authority audit

The current repository inventory was inspected before writing. Ouros already has authorities for geology, volcanism/geothermal unrest, slope instability, crisis/disaster response, architecture/infrastructure damage, groundwater, metrology, timekeeping and remote sensing. No dedicated seismic-event authority was found.

Pass 164 therefore should not create a competing geology system. The useful missing layer is a subordinate seismic monitoring and event-revision protocol that records earthquakes, local shaking, aftershock relationships and observed ground failure, then hands consequences to the existing authorities.

Key separation:

`geologic structure / fault interpretation -> seismic event estimate -> local shaking observations -> scoped ground-failure observations -> cross-system consequences`

Geology owns the regional geologic interpretation. Crisis owns emergency operations. Slope Instability owns earthquake-triggered landslides/rockfall/debris-flow state. Architecture/Public Works own structural damage and repair. Groundwater owns wells/springs and subsurface-water response. Metrology owns instrument calibration. Timekeeping owns corrected timestamps. Remote Sensing owns derived aerial change products.

## Scientific sources and reusable lessons

### USGS — magnitude and intensity are different questions

Source: U.S. Geological Survey, “Earthquake Magnitude, Energy Release, and Shaking Intensity.”
https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity

Reusable lesson: an earthquake can have one source-size estimate while producing many local intensity observations. Effects vary by distance, rupture geometry and local geology. Ouros should never store one global `earthquake_severity` and apply it to every settlement.

Design use:
- preserve event/source estimates separately from local shaking observations;
- allow two towns to experience materially different effects from the same event;
- allow intensity maps to be revised as observations arrive without changing the original event identity.

### USGS — observed effects are site-specific

Source: U.S. Geological Survey, “The Modified Mercalli Intensity Scale.”
https://www.usgs.gov/programs/earthquake-hazards/modified-mercalli-intensity-scale

Reusable lesson: felt/effect-based intensity is a local observation/assessment, not the same property as magnitude. Ouros may use its own setting-appropriate qualitative vocabulary unless canon explicitly adopts a numerical scale.

Do not import the Modified Mercalli scale as Ouros canon merely because it was useful research.

### USGS — site conditions matter

Sources:
- U.S. Geological Survey, “How do earthquakes affect buildings?”
  https://www.usgs.gov/faqs/how-do-earthquakes-affect-buildings
- U.S. Geological Survey, “Earthquake Processes and Effects — Ground Shaking.”
  https://earthquake.usgs.gov/research/eqproc/grdshaking.php

Reusable lesson: local shaking and damage depend on source characteristics, distance, soil/geology and the structure itself. This is useful for Chronicle because one earthquake can expose different vulnerabilities without requiring separate causes.

Guardrail: a building that suffers more damage than a nearby building does not prove corruption, sabotage or a stronger local earthquake. Architecture must assess its own condition.

### USGS — liquefaction is conditional, not synonymous with wet ground

Sources:
- U.S. Geological Survey, “What is liquefaction?”
  https://www.usgs.gov/faqs/what-liquefaction
- U.S. Geological Survey, “What are the Effects of Earthquakes?”
  https://www.usgs.gov/programs/earthquake-hazards/what-are-effects-earthquakes

Reusable lesson: liquefaction requires susceptible loose/water-saturated sediment plus strong shaking. It can produce settlement, lateral spreading and other ground failures.

Ouros design rule: `wet ground`, `riverbank`, `filled land` or `high groundwater` alone never creates liquefaction. A post-event sand boil or lateral-spread observation can open an assessment; it cannot be inferred from biome labels or Minecraft blocks.

### USGS — after-event activity has its own history

Sources:
- U.S. Geological Survey, “Earthquake Processes and Effects — Post-Earthquake Motions.”
  https://earthquake.usgs.gov/research/eqproc/posteqmotions.php
- U.S. Geological Survey, Loma Prieta aftershocks and postseismic effects.
  https://www.usgs.gov/publications/loma-prieta-california-earthquake-october-17-1989-aftershocks-and-postseismic-effects

Reusable lesson: a major event can be followed by many later earthquakes and other post-event deformation. Those later observations matter because already-damaged infrastructure and disrupted services may face renewed risk.

Ouros should store aftershock association as an assessment. A later nearby tremor is not automatically an aftershock merely because it occurred after the first event.

### USGS — shaking maps are derived products

Source: U.S. Geological Survey, ShakeMap.
https://earthquake.usgs.gov/data/shakemap/

Reusable lesson: near-real-time shaking maps combine observations/models into a spatial product used for response and later analysis. That fits Ouros well if the setting has sufficient instrumentation, but the product must keep its method/revision provenance. It is not raw world truth.

## Pokémon sources and reusable structures

### Pokémon Mystery Dungeon: Rescue Team DX — disasters can sustain an institution and recurring rescue loop

Sources:
- The Pokémon Company International, Pokémon Mystery Dungeon: Rescue Team DX.
  https://www.pokemon.com/us/pokemon-video-games/pokemon-mystery-dungeon-rescue-team-dx/
- Official game site, world overview.
  https://mysterydungeon.pokemon.com/en-us/world/

The official premise states that natural disasters are occurring across the land and causing problems, while rescue requests create recurring work for rescue teams.

Reusable structure for Ouros:
`physical event -> immediate local needs -> response institution -> recovery/research -> later callbacks`

Do not copy its cosmological mystery, characters, dungeon plots or disaster cause. The useful lesson is that disaster response can be recurring civic work rather than one apocalyptic quest.

### Whiscash — visible Pokémon behavior is not reliable earthquake attribution

Secondary Pokédex compilation used to compare multiple official game entries:
https://bulbapedia.bulbagarden.net/wiki/Whiscash_(Pok%C3%A9mon)

Especially useful is the Legends: Arceus entry summarized there: Whiscash creates local shaking to startle prey, and people historically mistook that behavior for the cause of earthquakes. Other game entries also associate the species with tremors or earthquake prediction folklore.

Reusable Ouros pattern:
`unusual Pokémon behavior -> public causal claim -> instrument/geology evidence -> possibly corrected interpretation`

Guardrails:
- Whiscash presence does not prove a tectonic event.
- Whiscash absence does not rule one out.
- species lore does not create a regional earthquake-warning system;
- a Pokémon can create local tremors without being the source of a regional seismic event;
- any authored predictive behavior needs explicit canon and evidence.

This is particularly compatible with Ouros’ existing anti-scapegoat design patterns.

## PTU and project mechanics cross-check

Project source search confirms that `Earthquake` exists as a concrete Move concept in available material. A project source summary describes it as a damaging Ground Move rather than a general environmental-event system.

Therefore:
- environmental earthquake state must never call the battle Move by name as an implementation shortcut;
- an earthquake does not inherit the Move’s range, targeting, damage, Frequency or special interactions;
- a Pokémon using the Move does not automatically create a persistent regional seismic event;
- a persistent regional event does not prove a Pokémon used the Move.

Available AutoPTU Python evidence also contains `Groundshaper`/`Mold the Earth` battle behavior. That is another exact mechanic and does not grant geologic authority, fault manipulation, earthquake prediction or regional ground deformation.

No reliable complete Caelo source defining earthquake hazards, seismic damage, structural collapse, liquefaction, aftershocks or environmental tremor mechanics was recovered in this run. Super PTU Online Helper was not exposed as an invocable capability.

## PTU community / campaign design lesson

A public PTU GM report describes an earthquake exposing a cave and the GM then improvising unstable-roof consequences during exploration. This is useful mainly as a warning: it is narratively effective to let a disaster reveal previously inaccessible space, but improvised falling-rock damage can quickly become an unverified subsystem.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/onnt2p/

Ouros adaptation:
- an event may revise a cave entrance, roadcut or ruin access in world state;
- Slope Instability/Geology decides whether instability exists;
- a battle inside that site uses static reduced geometry until falling debris/collapse rules are actually verified;
- do not invent damage dice because “earthquake cave” sounds dangerous.

## Fan-game structural reference

Pokémon Prism’s public premise begins with an earthquake separating the protagonist from home and placing them in a new region. This is useful only as a high-level transition pattern: a physical event can alter access and personal geography without needing to remain the central antagonist for the entire story.

Reference overview:
https://en.wikipedia.org/wiki/Pok%C3%A9mon_Prism

Ouros should not copy its protagonist, regions, league route or plot.

## Original Ouros design directions derived from the research

1. A single event should accumulate several revisions: initial automatic detection, felt reports, instrument review, geologic interpretation and later historical reanalysis.
2. The same event can produce different local stories without contradiction.
3. Damage is downstream evidence, not a magnitude meter.
4. Post-event sequences should create repeated small operational decisions rather than endlessly escalating spectacle.
5. A later aftershock can matter because of prior damage or disrupted services even when it is much less dramatic than the first event.
6. Ground failure should be typed and handed off. Liquefaction, landslide, settlement and surface rupture are not interchangeable.
7. Monitoring outages and bad clocks can create uncertainty that Metrology/Timekeeping later resolve.
8. A quarry blast, mine operation, Pokémon-generated tremor or machinery event can become a competing signal hypothesis without automatically becoming deception.
9. A quiet monitoring year is valuable Chronicle evidence.
10. Earthquake history can alter maps, route planning, archives, memorials, building practice and public memory for decades.

## Explicit non-canon / no-inference rules

Do not infer a fault from a crack in Minecraft terrain.
Do not infer an earthquake from block destruction.
Do not infer magnitude from damage.
Do not infer intensity at one settlement from another settlement’s experience.
Do not infer liquefaction from wet ground, sand, river proximity or groundwater alone.
Do not infer landslide state inside this protocol; hand it to Slope Instability.
Do not infer structural safety from a low local shaking assessment; hand condition to Architecture/Public Works.
Do not infer earthquake cause from Whiscash or any Ground-type Pokémon.
Do not infer prediction capability from unusual Pokémon behavior unless authored and verified.
Do not map environmental earthquakes to the PTU Move `Earthquake`.
Do not map `Groundshaper`, `Mold the Earth`, Ground typing or Ground Moves to tectonic authority.
Do not invent falling-rock damage, knockback, Tripped, Rough Terrain, Accuracy penalties or Status effects from shaking.

## Open questions for canon

- Does Ouros have known active faults before the player arrives?
- Which regions possess instrumental seismic monitoring, and how advanced is it?
- What historical earthquakes are already part of public memory?
- Which event data are public, restricted or uncertain?
- Does the setting use numerical magnitude/intensity language, or qualitative regional terminology?
- Which settlements or infrastructures were designed around known seismic history?
- Are any Pokémon behaviors authored as seismic precursors, local tremor sources or folklore, and how reliable are those claims?
- How much event catalog revision should occur offline?
- What Caelo rules, if any, govern environmental shaking, collapse, falling debris or ground failure?
