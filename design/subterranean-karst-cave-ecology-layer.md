# Subterranean, karst & cave ecology layer

Status: PROPOSED SYSTEM DESIGN. Not canon.

## Purpose

This layer gives caves durable identity as ecological, hydrological, cultural and navigational systems without turning every Minecraft cave block into world truth or every underground room into a tactical hazard.

It connects Geology, Freshwater/Groundwater, Cartography, Light, Soundscapes, Decomposition, Interspecies Ecology, Conservation, Archaeology, Material Culture, Travel, Mining, Crisis, Outbreak/Health, Architecture and future Minecraft projection.

The central separation is:

```text
persistent subterranean system
        ↓
geometry + entrances + hydrology + microclimate + biological inputs
        ↓
observations / surveys / mapped knowledge / occupancy evidence
        ↓
player + institutional knowledge
        ↓
optional encounter projection
        ↓
validated AutoPTU battle snapshot
```

A chamber rendered in Minecraft does not automatically create PTU darkness, Rough Terrain, falling-rock damage, cave bonuses or legal vertical traversal.

## Core objects

### SUBTERRANEAN_SYSTEM

A durable named cave, karst, lava-tube, mine-natural-complex or other underground network.

```yaml
subterranean_system_id: null
name: null
system_type: null
surface_region_refs: []
entrance_ids: []
passage_version_ids: []
chamber_ids: []
hydrology_refs: []
microclimate_profile_id: null
biological_input_profile_id: null
known_depth_class: unknown
mapped_extent_status: PARTIAL
research_refs: []
chronicle_refs: []
canon_status: proposed
```

Suggested `system_type` values:
- KARST_CAVE
- LAVA_TUBE
- SEA_CAVE
- TALUS_CAVE
- ICE_CAVE
- MINE_NATURAL_COMPLEX
- ARTIFICIAL_TUNNEL_NETWORK
- UNKNOWN

System type must come from authored geology or evidence. The generator must not decide that every cave is limestone/karst.

### SUBTERRANEAN_GEOMETRY_REVISION

A versioned graph of known physical connectivity.

```yaml
subterranean_geometry_revision_id: null
subterranean_system_id: null
valid_from: null
valid_to: null
node_refs: []
edge_refs: []
known_open_entrances: []
known_blocked_edges: []
known_water_passages: []
uncertain_edges: []
survey_refs: []
supersedes: null
```

A new passage can be discovered without retconning old maps. A collapse can close one edge while the system identity remains unchanged.

### CAVE_ENTRANCE

A persistent connection between surface and underground spaces.

```yaml
cave_entrance_id: null
subterranean_system_id: null
surface_location_id: null
subterranean_node_id: null
entrance_type: null
physical_state: OPEN
access_state_refs: []
light_transition_class: null
airflow_observation_refs: []
water_input_refs: []
wildlife_passage_refs: []
condition_history: []
```

Possible entrance types:
- NATURAL_OPENING
- SINKHOLE
- VERTICAL_SHAFT
- SPRING_OUTFLOW
- MINE_ADIT
- CONSTRUCTED_ACCESS
- COLLAPSE_OPENING
- UNKNOWN

Access may be physically possible but institutionally restricted, ecologically sensitive or unknown to a given actor.

### SUBTERRANEAN_CHAMBER

A stable semantic location inside the network.

```yaml
subterranean_chamber_id: null
subterranean_system_id: null
name_or_label: null
geometry_revision_refs: []
depth_class: null
light_class: null
water_state_ref: null
substrate_class: null
microclimate_zone_ref: null
biological_input_refs: []
habitat_use_refs: []
archaeology_refs: []
resource_refs: []
encounter_projection_refs: []
```

A chamber can persist even when its exact Minecraft block representation changes.

### CAVE_MICROCLIMATE_PROFILE

Coarse persistent environmental state.

```yaml
cave_microclimate_profile_id: null
scope_ref: null
revision: null
temperature_class: null
humidity_class: null
airflow_class: null
surface_influence_class: null
seasonal_variability_class: null
measurement_refs: []
interpretation_refs: []
```

This profile does not automatically become PTU Weather.

### SUBTERRANEAN_WATER_LINK

Connection between cave passages and Freshwater/Groundwater state.

```yaml
subterranean_water_link_id: null
subterranean_system_id: null
source_or_recharge_ref: null
destination_ref: null
link_type: null
flow_state: UNKNOWN
seasonality_refs: []
quality_observation_refs: []
tracer_or_inference_refs: []
confidence: null
```

Possible link types:
- SINK_INPUT
- UNDERGROUND_STREAM
- SEEP
- SPRING_OUTFLOW
- FLOOD_CONNECTION
- GROUNDWATER_EXCHANGE
- UNKNOWN

A suspected connection remains a hypothesis until evidence supports it.

### CAVE_NUTRIENT_INPUT

Coarse record for material entering a low-light environment.

```yaml
cave_nutrient_input_id: null
scope_ref: null
input_type: null
source_ref: null
observed_at: null
quantity_class: null
seasonality_ref: null
evidence_refs: []
```

Possible inputs:
- GUANO
- ROOT_MATERIAL
- FLOOD_DEBRIS
- WIND_BLOWN_MATERIAL
- SEEDS
- NESTING_MATERIAL
- ANIMAL_CARCASS_OR_REMAINS
- HUMAN_VISITOR_INPUT
- UNKNOWN_ORGANIC_INPUT

The layer records observable inputs. It does not simulate calories or complete food webs.

### CAVE_OCCUPANCY_EVIDENCE

Evidence of use by an individual, collective or population.

```yaml
cave_occupancy_evidence_id: null
feature_ref: null
actor_or_population_ref: null
evidence_type: null
observed_at: null
observer_refs: []
evidence_refs: []
confidence: null
inference_status: OBSERVED_ONLY
```

Evidence types can include:
- DIRECT_SIGHTING
- CALL_OR_ULTRASOUND_RECORD
- WALL_MARKS
- TRACKS
- GUANO
- SHED_MATERIAL
- NEST_OR_ROOST_STRUCTURE
- FEEDING_REMAINS
- CAMERA_RECORD
- UNKNOWN

Evidence of use does not automatically prove current occupancy, exact abundance, nesting, kinship or ownership.

### ROOST_OR_COLONY_SITE

Persistent habitat feature for repeated aggregation.

```yaml
roost_or_colony_site_id: null
subterranean_feature_ref: null
population_or_collective_ref: null
use_window_refs: []
occupancy_observation_refs: []
disturbance_refs: []
protection_refs: []
current_status: UNKNOWN
```

A roost can be seasonal, intermittent or abandoned.

### CAVE_DISTURBANCE_EVENT

World-state change affecting cave condition.

```yaml
cave_disturbance_event_id: null
subterranean_system_id: null
event_type: null
occurred_at: null
source_event_ref: null
affected_feature_refs: []
observed_effect_refs: []
followup_required: true
```

Possible event types:
- COLLAPSE
- FLOOD
- SEDIMENT_INPUT
- ENTRANCE_MODIFICATION
- CONSTRUCTION_VIBRATION
- EXTRACTION
- VISITOR_PRESSURE
- POLLUTION_INPUT
- FIRE_SURFACE_EFFECT
- VEGETATION_CHANGE
- UNKNOWN

Cause and effect should be connected by evidence, not narrative convenience.

### CAVE_ACCESS_RECORD

World-facing access and safety state.

```yaml
cave_access_record_id: null
scope_ref: null
physical_access_state: null
institutional_access_state: null
ecological_access_state: null
known_to_actor_refs: []
valid_from: null
review_at: null
reason_refs: []
```

Physical openness, authorization and ecological advisability are separate.

## Cave-zone model

Large systems should not be represented as one uniform environment.

Useful coarse zones:
- ENTRANCE
- TWILIGHT
- DARK
- DEEP_DARK
- AQUATIC
- FLOOD_PRONE
- ROOST
- MINERAL_OR_RESOURCE
- ARCHAEOLOGICAL
- ARTIFICIAL_OR_MINED
- COLLAPSE
- UNKNOWN

These are world-state categories. They are not PTU Terrain names unless an authoritative projection maps them to a legal battle context.

## Connectivity and depth

### Cave depth is graph distance, not automatically vertical meters

A location may be “deep” because it requires many passages, not because it is directly far below the surface.

Record both when known:
- route/depth class in the cave graph;
- physical elevation/depth observations where authored or surveyed.

Do not derive tactical elevation from either one automatically.

### Multiple entrances create route choice

A cave can connect:
- two valleys;
- a town and a spring;
- a mine and a natural chamber;
- a cliff opening and river resurgence;
- surface ruins and deeper archaeological layers.

A newly discovered entrance can change Travel, Conservation, Cases, Tourism or Faction state without changing the cave’s identity.

## Surface–subsurface causal rules

### Freshwater / groundwater

Freshwater owns surface water and groundwater regime. This layer owns where that water enters, travels through or emerges from the subterranean system.

Examples:
- heavy rain activates an underground stream;
- pumping lowers a cave pool;
- a sinkhole transmits contamination;
- a cave blockage changes spring discharge;
- a collapse reroutes water.

The chain must be explicit through state references.

### Soil / erosion

Soil owns erosion and sediment production. This layer records sediment entering passages, chambers or streams.

A muddy cave floor does not prove where the sediment came from.

### Wildfire / flora / decomposition

Surface vegetation and fire can alter material and water inputs. Decomposition owns decay of organic matter; this layer records entry and cave context.

### Waste / sanitation

Waste owns pollutant/material provenance. A sinkhole or cave may become a transport path. Finding contamination underground does not prove the nearest surface actor caused it.

### Architecture / mining

Constructed tunnels, gates, supports, stairs and visitor infrastructure belong to Architecture/Infrastructure. Natural cave identity remains separate.

A mine-natural complex can contain both artificial and natural passages.

## Cave ecology rules

### Low-light energy constraint

Most deep cave habitats cannot rely on ordinary photosynthetic production.

The model should therefore support external nutrient inputs and specialized biological processes while avoiding full simulation.

### Surface dependence can be indirect

A cave population may respond to:
- fewer animals entering;
- changed plant cover over recharge zones;
- blocked entrances;
- altered water flow;
- visitor pressure;
- pollution;
- changed temperature/humidity.

The observed effect may appear far from the surface cause.

### Species behavior remains species-specific

Zubat, Woobat, Carbink, Sableye, Noibat, Aron and other cave-associated species must not share a generic cave-behavior package simply because they may occur underground.

Only authored Pokédex/species ecology or repeated observation should create specific associations.

### Roost disturbance is world state

A disturbed roost can produce:
- temporary absence;
- changed timing;
- relocation;
- increased calls/activity;
- a conservation response;
- a research question.

It does not automatically produce an Aggressive status, battle buff or swarm mechanic.

## Exploration and mapping

### Survey records

Each expedition can add:
- new nodes/edges;
- blocked routes;
- water states;
- chambers;
- feature locations;
- hazards observed in world state;
- occupancy evidence;
- samples;
- unresolved questions.

### Map editions

Cartography owns published/held maps.

A cave map should store:
- geometry revision represented;
- known uncertainty;
- survey date;
- omitted or restricted areas;
- known closures;
- vertical profile if relevant.

An old cave map may remain historically correct.

### Unknown passage rule

The generator may create the possibility of an unmapped connection only if supported by geology, incomplete survey state or authored mystery. It should not spawn secret tunnels whenever content is needed.

## Persistent cave history

The Chronicle can record:
- first known entrance;
- surveys;
- collapses;
- floods;
- rediscovered passages;
- former mines;
- closed tourist sections;
- archaeological finds;
- rescue incidents;
- wildlife recolonization;
- route opening/closure;
- changes in spring or pool state.

This allows revisiting the same cave years later with changed conditions.

## Fragile and significant features

Possible features requiring persistent identity:
- fossil context;
- archaeological layer;
- unusual mineral deposit;
- historic inscription;
- roost;
- rare formation;
- underground lake;
- spring source;
- long-running sensor station;
- memorial or historical site;
- persistent individual Pokémon den/use site.

These features are not generic loot nodes.

## Minecraft projection

Minecraft may render:
- entrances;
- stable passage versions;
- blocked/open routes;
- pools/streams;
- sediment or collapse visuals;
- light gradients;
- observation stations;
- roost presentation;
- mapped signs/markers;
- artificial supports;
- cave settlement infrastructure.

Minecraft must not be authoritative for:
- complete cave extent;
- groundwater connectivity;
- cave age;
- occupancy abundance;
- microclimate history;
- roost status;
- archaeological interpretation;
- cave map certainty;
- PTU darkness/visibility;
- PTU hazards;
- resource quantity;
- current population truth.

Loaded entities remain presentation, not ecological truth.

## Battle projection boundary

A cave world state can be projected into an immutable encounter snapshot only through validated adapter logic.

Possible future projection:

```yaml
battle_projection:
  chamber_id: null
  geometry_revision_id: null
  frozen_map_id: null
  static_blockers: []
  static_water_tiles: []
  validated_environment_tags: []
  validated_visibility_context: null
  validated_hazard_refs: []
  source_world_state_refs: []
```

Until cave visibility, hazards, water dynamics and vertical movement are authoritative in Java, reduced encounters should use one stable 2D chamber with normal battle visibility unless an exact verified rule says otherwise.

## PTU/Caelo guardrails

The Python oracle contains narrow cave/environment interactions such as recognized `cave/cavern/underground` context for named Move behavior and habitat matching.

Those mechanics do not establish a universal cave subsystem.

Do not infer from a cave visual:
- Blinded;
- Accuracy penalties;
- Darkvision activation effects beyond exact rules;
- Naturewalk;
- Burrow;
- climbing;
- Wallrunner;
- falling damage;
- difficult terrain;
- cave-in damage;
- rockfall;
- flooding;
- drowning;
- gas exposure;
- echo targeting;
- sound bonuses;
- Stealth bonuses;
- surprise;
- environmental Poison/Burn/Confusion;
- rare-spawn bonuses.

Exact PTU/Caelo rules for darkness, Darkvision, Blindsense, Glow, Naturewalk, Burrow, Wallrunner, climbing, falling, underwater passages and cave-specific effects require source validation.

## Encounter implementation contracts

### Sinking Passage Survey

Narrative premise: surveyors discover that a previously dry connecting passage is taking water after heavy rain, and wildlife is using higher ledges/side chambers.

Full version intends:
- water level changing between phases;
- route choices;
- safe/high ground;
- REACH_EXIT / WITHDRAW objectives;
- swimmers and non-swimmers using legal movement differently;
- possible current/forced movement only if authoritative rules exist;
- objective-aware AI;
- Minecraft playback of the same frozen/transition state.

Permanent capability dependencies:
- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED baseline;
- complete movement incl. push/pull/knockback/interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version: resolve water rise and route eligibility before combat. Freeze one dry or shallow-water geometry revision as the battle map. Keep surveyors and moving water outside the grid. Do not simulate currents, drowning or vertical escape.

### Roost Entrance Disturbance

Narrative premise: repeated visitor activity near an entrance coincides with changed cave-roost use, but cause and exact occupancy remain uncertain.

Full version intends:
- noncombatants near an entrance;
- wild Pokémon capable of withdrawing toward legal exits;
- protect/withdraw rather than KO-only goals;
- limited light/visibility effects only if verified;
- tactical AI that values retreat and safe routes.

Permanent dependencies:
- targeting/LoS: VERIFIED baseline; visibility-in-darkness unverified;
- base movement: VERIFIED baseline;
- complete movement/interception: BLOCKING;
- lifecycle: PARTIAL;
- statuses: PARTIAL;
- terrain/hazards/zones/reactions: BLOCKING;
- abilities/moves/features: PARTIAL as applicable;
- AI legal actions: VERIFIED;
- tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version: visitor pressure, roost evidence and evacuation happen in overworld state. If a defensive encounter occurs, use a static entrance chamber and only combatants that actually engage. Do not convert all visible roost members into enemies.

### Sinkhole Dye-Tracer Follow-Up

Narrative premise: a surface-water tracer or other investigation suggests a sinkhole is connected to a spring/cave passage, and an expedition checks the suspected route.

Full version intends:
- linked surface/subsurface objectives;
- interactable monitoring points;
- possible multi-stage travel through separate chambers;
- changing water access between scenes;
- no combat requirement unless actual world state produces one.

Permanent dependencies if combat occurs:
- base geometry and legal movement: VERIFIED baseline;
- terrain/hazards/dynamic water: BLOCKING;
- tactical AI: BLOCKING for non-KO objectives;
- adapter/playback: BLOCKING.

Reduced version: treat the tracer/survey entirely as research and world state. If a wild encounter occurs, use one static chamber after the hydrological conclusion is resolved independently.

### Collapsed Mine-Natural Junction

Narrative premise: a collapse exposes a natural chamber beside an old mine, creating rescue, archaeology, resource and ecology questions simultaneously.

Full version intends:
- unstable edges;
- protected rescue zone;
- possible falling debris only with exact rules;
- civilians/workers;
- changing access state;
- objective-aware AI.

Reduced version: resolve collapse stability and rescue corridors before battle. Freeze one safe chamber for combat, keep workers/archaeological context outside the grid and prohibit invented rockfall damage.

## Anti-exploit rules

- Digging a new Minecraft tunnel does not automatically create a canonical cave system.
- Exposing stone blocks does not create minerals, fossils or rare Pokémon.
- Placing water does not alter groundwater/cave hydrology.
- Adding torches does not automatically erase cave habitat or grant PTU visibility unless an authored lightscape rule supports the change.
- Repeatedly loading a chamber does not generate occupancy evidence.
- Breaking an entrance block does not automatically create a legal route through a persistent system.
- Players cannot farm rare spawns by opening/closing cave entrances unless a future authored ecology rule explicitly validates the causal chain.
- A sinkhole discovered by a player cannot be duplicated by terrain regeneration or chunk reload.

## Privacy / multiplayer considerations

Cave maps and discoveries may be:
- public;
- party-shared;
- institution-restricted;
- conservation-sensitive;
- personally annotated;
- intentionally redacted.

One player discovering a hidden passage does not automatically reveal it to every player.

Sensitive roost, archaeological or rare-habitat coordinates should use the same knowledge/redaction systems already defined elsewhere in Ouros.

## Open questions

- Which Ouros regions have major karst, lava-tube, sea-cave, ice-cave or mine-natural systems?
- Which cave networks are known before players arrive?
- Which named cave systems are important enough to have persistent chamber IDs?
- How much geometry can players permanently alter in Minecraft before authored topology must be protected?
- What exact PTU/Caelo rules govern darkness, Darkvision, Blindsense, Glow, Naturewalk, Burrow, Wallrunner, climbing, falling and underwater passages?
- Does AutoPTU eventually need multi-level cave battles, or should one frozen chamber remain the tactical unit?
- How should cave airflow and microclimate be represented without over-simulating temperature/humidity?
- Which surface ecological changes are allowed to affect cave occupancy automatically versus requiring research evidence?
- Which cave features are public tourism assets, protected research areas, working mines, sacred sites or private infrastructure?
