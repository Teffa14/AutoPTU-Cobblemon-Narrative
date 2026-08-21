# Ouros Urban Stormwater, Drainage & Green Infrastructure Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

This layer models how rainfall interacts with built surfaces, drains, storage, infiltration systems and receiving waters inside settlements.

It exists to connect Meteorology, Architecture, Freshwater, Waste/Sanitation, Road Ecology, Soil, Crisis, Urban Heat and Conservation without allowing Minecraft blocks or narrative prose to invent PTU environmental mechanics.

It does not define flood damage, drowning, currents, movement penalties, contaminated-water statuses, drainage engineering formulas, sewer legality, maintenance Skill DCs, pump statistics or Minecraft fluid simulation.

## 1. Responsibility boundary

This layer owns:
- urban drainage catchments;
- impervious/pervious surface summaries;
- stormwater asset identity and connectivity;
- inlet/outfall state;
- storage/infiltration state;
- runoff-routing revisions;
- blockage/maintenance records;
- overflow observations;
- green-infrastructure projects;
- stormwater monitoring;
- stormwater-to-receiving-water handoff records.

Other layers remain authoritative for:
- rainfall and forecast: Meteorology;
- rivers, lakes and downstream hydrology: Freshwater;
- wastewater and refuse: Waste/Sanitation;
- roads/culverts as transport corridors: Road Ecology;
- buildings and streets: Architecture;
- soil infiltration observations: Soil;
- emergencies and evacuation: Crisis;
- urban vegetation/shade: Flora / Urban Heat;
- habitat response: Conservation / Wild Ecology;
- tactical environmental effects: AutoPTU-Java.

## 2. Stormwater district

```yaml
stormwater_district:
  district_id: null
  settlement_id: null
  drainage_zone_ids: []
  receiving_water_ids: []
  surface_summary_revision_id: null
  network_id: null
  monitoring_station_ids: []
  maintenance_program_ids: []
  public_map_ids: []
  last_review_event_id: null
```

A stormwater district is a hydrologic/service coordination object. It does not imply one political district, one utility, one watershed or one legal authority.

## 3. Drainage zone

```yaml
drainage_zone:
  drainage_zone_id: null
  district_id: null
  footprint_ref: null
  surface_summary_revision_id: null
  inlet_ids: []
  storage_asset_ids: []
  infiltration_asset_ids: []
  pump_asset_ids: []
  outfall_ids: []
  upstream_zone_ids: []
  downstream_zone_ids: []
  receiving_water_id: null
  known_overflow_points: []
  confidence_notes: null
```

The footprint is coarse. The system should not calculate runoff for every Minecraft block.

## 4. Surface summary

```yaml
surface_summary_revision:
  revision_id: null
  drainage_zone_id: null
  effective_from: null
  impervious_fraction_class: null
  connected_impervious_class: null
  vegetated_storage_class: null
  open_water_refs: []
  soil_unit_refs: []
  roof_area_class: null
  road_area_class: null
  parking_area_class: null
  major_recent_change_refs: []
  source_ids: []
```

Candidate qualitative classes:
- VERY_LOW
- LOW
- MODERATE
- HIGH
- VERY_HIGH
- UNKNOWN

These classes do not directly produce liters/second or flood depth.

## 5. Stormwater network

```yaml
stormwater_network:
  network_id: null
  node_ids: []
  edge_ids: []
  network_type: null
  operator_actor_ids: []
  record_system_ids: []
  inspection_program_ids: []
  known_interconnection_ids: []
```

Candidate network types:
- SEPARATE_STORMWATER
- OPEN_DRAINAGE
- MIXED_OPEN_CLOSED
- COMBINED_ONLY_IF_AUTHORED
- UNKNOWN

Never infer combined sewer behavior because a pipe is underground.

## 6. Network node

```yaml
stormwater_node:
  node_id: null
  node_type: null
  location_ref: null
  operational_state: null
  capacity_class: null
  current_blockage_assessment: null
  maintenance_refs: []
  wildlife_use_refs: []
  inspection_access_ref: null
```

Candidate node types:
- INLET
- JUNCTION
- MANHOLE
- OPEN_CHANNEL
- DETENTION_BASIN
- RETENTION_BASIN
- INFILTRATION_BASIN
- BIOSWALE
- RAIN_GARDEN
- PUMP_STATION
- OUTFALL
- OVERFLOW_POINT
- SENSOR_SITE

Candidate operational states:
- NORMAL
- DEGRADED
- RESTRICTED
- BLOCKED_CONFIRMED
- OUT_OF_SERVICE
- UNDER_MAINTENANCE
- UNKNOWN

## 7. Network edge

```yaml
stormwater_edge:
  edge_id: null
  from_node_id: null
  to_node_id: null
  edge_type: null
  flow_direction_state: null
  operational_state: null
  access_state: null
  inspection_refs: []
  sediment_state_ref: null
  wildlife_use_refs: []
```

Candidate edge types:
- PIPE
- CULVERT
- OPEN_DITCH
- LINED_CHANNEL
- OVERLAND_RELIEF_PATH
- PUMPED_LINK
- UNKNOWN

## 8. Rainfall-to-runoff episode

```yaml
stormwater_episode:
  episode_id: null
  meteorology_event_id: null
  district_id: null
  start_time: null
  end_time: null
  rainfall_observation_ids: []
  pre_event_storage_state_ids: []
  runoff_response_observation_ids: []
  overflow_observation_ids: []
  pump_operation_ids: []
  receiving_water_handoff_ids: []
  incident_ids: []
  review_status: null
```

The stormwater layer records what happened. It does not fabricate exact discharge from rainfall alone.

## 9. Runoff-response observation

```yaml
runoff_response_observation:
  observation_id: null
  episode_id: null
  location_ref: null
  observer_id: null
  observed_at: null
  observation_type: null
  value_or_class: null
  instrument_ref: null
  confidence: null
  media_refs: []
  provenance_ids: []
```

Candidate observation types:
- STREET_PONDING
- INLET_SURCHARGE
- CHANNEL_FLOW
- BASIN_LEVEL
- OUTFALL_FLOW
- SEDIMENT_PLUME
- EROSION
- FLOATING_DEBRIS
- PUMP_OPERATION
- INFILTRATION_FAILURE_SUSPECTED
- UNKNOWN

Observation is not diagnosis.

## 10. Overflow assessment

```yaml
overflow_assessment:
  assessment_id: null
  episode_id: null
  affected_zone_ids: []
  observed_overflow_ids: []
  candidate_cause_ids: []
  reviewed_cause_state: null
  severity_class: null
  downstream_effect_refs: []
  infrastructure_damage_refs: []
  confidence: null
```

Candidate causes:
- CAPACITY_EXCEEDED
- BLOCKAGE_CONFIRMED
- PUMP_FAILURE
- DOWNSTREAM_BACKWATER
- STORAGE_ALREADY_FULL
- CONSTRUCTION_FLOW_PATH_CHANGE
- INFILTRATION_LIMITED
- MULTIPLE_FACTORS
- UNKNOWN

Never set `BLOCKAGE_CONFIRMED` from street flooding alone.

## 11. Green-infrastructure asset

```yaml
green_infrastructure_asset:
  asset_id: null
  asset_type: null
  site_id: null
  drainage_zone_id: null
  primary_function_refs: []
  supporting_function_refs: []
  vegetation_unit_refs: []
  soil_unit_refs: []
  maintenance_owner_ref: null
  current_condition: null
  commissioning_event_id: null
  monitoring_program_ids: []
  ecological_use_refs: []
```

Candidate functions:
- INFILTRATION
- DETENTION
- RETENTION
- FILTRATION
- EVAPOTRANSPIRATION
- SHADE_SUPPORT
- HABITAT_SUPPORT
- PUBLIC_SPACE

A rain garden does not automatically improve all functions equally.

## 12. Green-infrastructure project

```yaml
green_infrastructure_project:
  project_id: null
  proposal_id: null
  site_ids: []
  baseline_observation_ids: []
  intended_function_refs: []
  construction_state: null
  maintenance_plan_ref: null
  monitoring_plan_ref: null
  completed_event_id: null
  followup_assessment_ids: []
```

Completion does not equal success.

## 13. Stormwater monitoring

Monitoring can include:
- rainfall;
- basin level;
- inlet condition;
- pump operation;
- outfall flow;
- water-quality samples;
- sediment observations;
- photo points;
- wildlife use.

Each observation needs provenance and timing.

A sample collected during one storm cannot describe every storm.

## 14. Stormwater contamination claim

```yaml
stormwater_quality_observation:
  observation_id: null
  episode_id: null
  sample_site_ref: null
  sample_time: null
  analyte_or_indicator_ref: null
  observed_value: null
  method_ref: null
  chain_of_custody_ref: null
  source_hypothesis_ids: []
  public_claim_ids: []
```

The nearest visible business is not automatically the source.

Use the Science, Case, Evidence and Waste/Sanitation layers when source attribution becomes important.

## 15. Underground drainage as explorable space

An explorable drain/tunnel should preserve:
- infrastructure function;
- upstream/downstream context;
- maintenance access;
- active/inactive state;
- known dry-weather accessibility;
- rainfall-sensitive access state;
- wildlife-use observations;
- safety review state;
- historical modifications.

It should not exist only as a dungeon skin.

## 16. Access state

```yaml
stormwater_access_state:
  access_state_id: null
  site_id: null
  effective_from: null
  access_class: null
  cause_refs: []
  weather_dependency_ref: null
  credential_requirement_ref: null
  safety_review_ref: null
```

Candidate access classes:
- OPEN_PUBLIC
- STAFF_ONLY
- GUIDED_ACCESS
- TEMPORARILY_CLOSED
- DRY_WEATHER_ONLY
- EMERGENCY_ONLY
- INACCESSIBLE
- UNKNOWN

## 17. Pokémon use of stormwater infrastructure

```yaml
stormwater_pokemon_use_observation:
  observation_id: null
  pokemon_or_population_ref: null
  asset_or_reach_id: null
  observed_behavior: null
  observed_at: null
  season_ref: null
  water_state_ref: null
  provenance_ids: []
  interpretation_ids: []
```

Valid observations can include:
- sheltering;
- crossing;
- feeding;
- nesting;
- trapped/stranded;
- repeated presence;
- avoidance;
- unknown use.

Do not infer ownership, friendship, territorial bonuses or battle mechanics.

## 18. Causal integration examples

### Example A: short intense storm

high-intensity rainfall
→ street runoff rises quickly
→ one basin reaches storage limit
→ controlled overflow reaches creek
→ Freshwater records downstream pulse
→ Road Ecology records one culvert crossing issue
→ no automatic crisis if people/services remain safe.

### Example B: blocked inlet

routine rain
→ street ponding appears at one corner
→ inspection finds leaf/debris blockage
→ maintenance clears inlet
→ future storms no longer reproduce the same symptom
→ no citywide drainage upgrade required.

### Example C: redevelopment

new roofs + pavement
→ surface-summary revision
→ higher runoff-response concern
→ civic proposal adds tree trenches / detention
→ monitoring after completion
→ results remain mixed or uncertain until evidence accumulates.

## 19. Minecraft projection

Minecraft may render:
- drains;
- grates;
- pipes;
- channels;
- basins;
- rain gardens;
- wet/dry visual variants;
- maintenance barriers;
- sensor stations;
- debris;
- temporary ponding as presentation if safely implemented.

Minecraft must not decide:
- authoritative runoff quantity;
- contamination source;
- downstream hydrology;
- whether a combatant is Slowed/Tripped/Poisoned;
- whether water is mechanically dangerous;
- whether a gate/pump interaction succeeds under PTU rules.

## 20. Battle snapshot projection

Battle projection must be explicit and conservative.

```yaml
stormwater_battle_projection:
  projection_id: null
  source_episode_id: null
  source_site_id: null
  frozen_geometry_revision: null
  verified_environment_contract_refs: []
  excluded_world_effects: []
  encounter_contract_id: null
```

Default behavior:
1. Resolve rainfall/runoff and infrastructure state in world state.
2. Select a safe/frozen battle geometry.
3. Exclude unimplemented dynamic flow, civilians and machinery.
4. Send only mechanically verified environment state to AutoPTU-Java.

## 21. Encounter implementation contracts

### A. Underpass Intake Blockage

Narrative premise:
A short storm produces unexpected flooding around an underpass. A maintenance crew discovers that part of the inlet system is blocked while Pokémon are using the dry edge as shelter.

Full version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including forced movement/interception: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Full version:
Water advances through selected low cells, some Pokémon attempt withdrawal, and clearing/protecting the intake is an objective.

Reduced version:
World state resolves the water level and crew evacuation first. The battle occurs on a fixed dry platform with only combatants. Clearing the blockage happens before or after battle through overworld interaction.

### B. Detention Basin Wildlife Conflict

Narrative premise:
A detention basin that usually drains after storms has retained water longer than expected and is now being used by wild Pokémon when a maintenance inspection is scheduled.

Full version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING if withdrawal/crossing objectives are active
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior / abilities / items / Features: PARTIAL as relevant
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:
Inspectors delay work; the server records the ecological use. If conflict occurs, AutoPTU receives a fixed shoreline arena. No basin-water effects are mechanical.

### C. Outfall Plume Investigation

Narrative premise:
After a storm, a visible sediment/discoloration plume appears below an outfall. Investigators need samples while local Pokémon are active nearby.

Full version dependencies:
- targeting/LoS: VERIFIED
- base movement: VERIFIED
- complete movement: potentially BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic water/plume effects
- move/ability/item/Feature behavior: PARTIAL as applicable
- AI legal actions: VERIFIED
- AI policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:
Sampling and plume interpretation stay outside battle. If a battle occurs, use a static bank/platform and do not apply pollution or current mechanics.

## 22. Permanent mechanical guardrails

Do not infer:
- rain = battlefield Weather;
- puddle = Water Terrain;
- flooded street = Slow/Rough Terrain;
- overflow = Poisoned;
- storm drain = drowning hazard;
- current = forced movement;
- culvert = cover;
- grate = trap;
- pump failure = electrical hazard;
- bioswale = healing or Grass Terrain;
- detention basin = encounter bonus;
- wet Pokémon = Water-type bonus.

## 23. Overworld implementation blockers

Explicit blockers outside the battle core:
- `OVERWORLD_STORMWATER_DISTRICT_GRAPH`
- `OVERWORLD_DRAINAGE_NETWORK_STATE`
- `OVERWORLD_SURFACE_SUMMARY_REVISIONS`
- `OVERWORLD_STORMWATER_EPISODES`
- `OVERWORLD_OVERFLOW_ASSESSMENTS`
- `OVERWORLD_GREEN_INFRASTRUCTURE_STATE`
- `OVERWORLD_STORMWATER_MONITORING`
- `OVERWORLD_STORMWATER_WILDLIFE_USE`
- `STORMWATER_TO_FRESHWATER_HANDOFF`
- `STORMWATER_TO_SANITATION_HANDOFF`
- `STORMWATER_TO_BATTLE_SNAPSHOT`
- `STORMWATER_TO_MINECRAFT_PROJECTION`

## 24. Questions requiring canon decisions

- Which settlements have formal stormwater networks?
- Which use open drains, separated pipes or mixed systems?
- Which assets predate the players?
- Who maintains the systems?
- What historical floods or drainage failures are established canon?
- Which underground networks are accessible?
- Which Pokémon have authored relationships with drains, channels or basins?
- Which green-infrastructure practices are regionally normal?
- How much drainage state advances while chunks are unloaded?
- Can players physically alter runoff routes through construction?
- Which PTU/Caelo rules, if any, govern flooding, currents, drowning or contaminated environments?

## 25. Promotion gate

A stormwater concept can enter canon only after:
1. narrative/settlement fit review;
2. infrastructure ownership and access review;
3. source/provenance review;
4. ecological consistency review;
5. PTU/Caelo mechanical review when mechanics are involved;
6. AutoPTU-Java capability review for tactical projection;
7. Minecraft implementation review if physical world changes are required.
