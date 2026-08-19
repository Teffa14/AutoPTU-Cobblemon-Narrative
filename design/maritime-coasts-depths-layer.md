# Ouros Maritime, Coasts & Underwater Depths Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

This layer models maritime space as persistent world state across travel, ecology, settlements, salvage, infrastructure, research, crisis response and tactical encounters.

It does not define Swim rules, underwater visibility, drowning, currents, vessel movement, fishing, salvage ownership, Dive behavior, weather damage or Minecraft fluid physics.

Those remain under PTU/Caelo authority and current implementation evidence.

## 1. Maritime region

```yaml
maritime_region:
  maritime_region_id: null
  parent_region_ids: []
  coastal_location_ids: []
  island_ids: []
  harbor_ids: []
  sea_lane_ids: []
  marine_habitat_ids: []
  submerged_location_ids: []
  stewardship_ids: []
  jurisdiction_refs: []
  weather_region_ids: []
  seasonal_cycle_ids: []
  public_map_ids: []
  active_incident_ids: []
```

A maritime region is a coordination object. It does not imply a single government, culture or League authority.

## 2. Water-space classification

The narrative layer may label water spaces without assigning mechanics.

Candidate labels:
- COASTAL_EDGE
- HARBOR_WATER
- ESTUARY
- SURFACE_WATER
- OPEN_SEA
- REEF
- SUBMERGED_SHALLOWS
- DEEP_WATER
- SEAFLOOR
- SUBMERGED_STRUCTURE
- UNDERWATER_SETTLEMENT
- UNDERWATER_CAVE

These labels help connect content systems. They must not grant movement costs, cover, pressure damage or visibility rules.

## 3. Sea lane

A sea lane is not equivalent to a body of water.

```yaml
sea_lane:
  sea_lane_id: null
  endpoint_ids: []
  connection_ref: null
  lane_type: null
  operator_ids: []
  service_ids: []
  traffic_state: normal
  known_navigation_refs: []
  hazard_state_ids: []
  current_state: OPEN
  seasonal_constraints: []
  ecology_overlap_ids: []
  stewardship_overlap_ids: []
  jurisdiction_overlap_ids: []
  emergency_alternative_ids: []
  last_verified_event_id: null
```

Candidate states:
- OPEN
- LIMITED
- REROUTED
- RESTRICTED
- CLOSED
- WEATHER_SUSPENDED
- INFRASTRUCTURE_SUSPENDED
- EMERGENCY_ONLY
- UNKNOWN

The travel layer remains authoritative for journeys and transport services. This object adds maritime-specific context.

## 4. Harbor

```yaml
harbor:
  harbor_id: null
  settlement_id: null
  berth_ids: []
  service_ids: []
  operator_ids: []
  cargo_facility_ids: []
  passenger_facility_ids: []
  rescue_facility_ids: []
  maintenance_asset_ids: []
  fuel_or_energy_dependency_ids: []
  navigation_asset_ids: []
  weather_exposure_refs: []
  ecology_overlap_ids: []
  current_capacity_state: normal
  current_access_state: open
```

Harbors should integrate with workplaces, transport, infrastructure, economy, crisis and communications layers.

A harbor can be operational while one berth, ferry service or lane is unavailable.

## 5. Vessel or maritime service asset

```yaml
maritime_asset:
  asset_id: null
  asset_type: null
  owner_claim_ids: []
  operator_ids: []
  home_harbor_id: null
  service_role: null
  capacity_state: unknown
  maintenance_state: unknown
  current_location_id: null
  current_journey_id: null
  cargo_record_ids: []
  passenger_record_ids: []
  crew_assignment_ids: []
  incident_ids: []
```

Candidate types:
- FERRY
- RESEARCH_VESSEL
- FISHING_VESSEL
- RESCUE_CRAFT
- CARGO_VESSEL
- SMALL_BOAT
- DIVE_SUPPORT_VESSEL
- FLOATING_BASE

Exact vehicle physics and speeds remain out of scope.

## 6. Surface and submerged locations are separate nodes

An underwater site should not be represented only as metadata on the surface tile.

```yaml
submerged_location:
  submerged_location_id: null
  surface_access_ref: null
  depth_band: null
  location_type: null
  access_state: unknown
  environment_refs: []
  structural_asset_ids: []
  marine_habitat_ids: []
  archaeological_refs: []
  geological_refs: []
  infrastructure_ids: []
  known_entry_ids: []
  known_exit_ids: []
  observation_ids: []
  current_condition: unknown
```

Possible location types:
- REEF_SITE
- WRECK
- CAVE
- RUIN
- RESEARCH_SITE
- SETTLEMENT
- UTILITY_SITE
- TUNNEL
- HABITAT_SITE
- SEAFLOOR_ROUTE

## 7. Access contract

Narrative access must request validation from authoritative systems.

Potential requirements include:
- valid route/service;
- individual Pokémon movement capability;
- exact breathing capability;
- equipment;
- escort/service access;
- current health state;
- environment restrictions;
- institutional permission;
- implementation support.

Do not infer:
- Water type means Swim eligibility;
- large aquatic Pokémon means mountable;
- Gilled means passenger transport;
- Dive Move means overworld underwater access;
- Cobblemon model means PTU capability.

## 8. Tides, currents and sea state

```yaml
marine_condition:
  condition_id: null
  maritime_region_id: null
  condition_type: null
  observed_state: null
  expected_state: null
  source_ids: []
  affected_location_ids: []
  affected_lane_ids: []
  start_event_id: null
  expected_end_ref: null
  confidence: null
```

Candidate condition types:
- TIDE
- CURRENT
- SWELL
- VISIBILITY
- SURFACE_WEATHER
- WATER_QUALITY
- DEBRIS_FIELD

The seasonality/weather layer may own timing. This layer records maritime consequences.

A condition may alter world access without creating a tactical modifier.

## 9. Tidal access

```yaml
tidal_access_window:
  window_id: null
  target_location_id: null
  enabling_condition_refs: []
  disabling_condition_refs: []
  expected_window_ref: null
  observed_open_state: unknown
  verification_event_id: null
```

Examples:
- cave mouth exposed at low water;
- temporary sandbar route;
- shallow wreck reachable during a calm window;
- harbor berth unusable at an extreme condition.

No movement/DC effect is implied.

## 10. Marine habitat

```yaml
marine_habitat:
  habitat_id: null
  location_ids: []
  habitat_type: null
  species_population_refs: []
  collective_ids: []
  seasonal_presence_refs: []
  resource_dependency_ids: []
  vessel_disturbance_refs: []
  water_quality_refs: []
  stewardship_ids: []
  observation_ids: []
  current_state: unknown
```

Candidate habitat types:
- REEF
- KELP_OR_SEAGRASS
- ESTUARY
- OPEN_WATER_FEEDING_AREA
- NESTING_OR_ROOSTING_SITE
- WRECK_HABITAT
- HARBOR_ADAPTED_HABITAT
- DEEP_WATER_SITE

Encounter ecology remains linked to the conservation and wild-collective layers.

## 11. Marine behavior memory

Observed behaviors may include:
- following a regular ferry;
- avoiding a noisy lane;
- feeding near a current boundary;
- resting near a wreck;
- appearing after storms;
- gathering near seasonal food;
- returning to a harbor;
- changing routes after construction.

Record observation and confidence.

Do not infer emotion, ownership or mechanical capability.

## 12. Wreck site

```yaml
wreck_site:
  wreck_id: null
  submerged_location_id: null
  vessel_or_structure_ref: null
  wreck_date_claims: []
  cause_claims: []
  historical_record_ids: []
  memorial_refs: []
  hazard_refs: []
  habitat_refs: []
  cargo_claim_ids: []
  salvage_event_ids: []
  custody_record_ids: []
  archaeological_refs: []
  access_state: unknown
```

A wreck may simultaneously be a habitat, hazard, historical site and salvage location.

## 13. Salvage event

Recovery and ownership must remain separate.

```yaml
salvage_event:
  salvage_event_id: null
  recovery_location_id: null
  recoverer_ids: []
  recovered_object_ids: []
  recovered_batch_ids: []
  discovery_context_ids: []
  immediate_custodian_id: null
  ownership_claim_ids: []
  evidence_ids: []
  archaeological_context_ids: []
  hazard_observation_ids: []
  disposition_state: unresolved
```

Candidate dispositions:
- RETURNED
- HELD_FOR_IDENTIFICATION
- TRANSFERRED_TO_AUTHORITY
- TRANSFERRED_TO_INSTITUTION
- SCIENTIFIC_CUSTODY
- HERITAGE_CUSTODY
- CLAIM_DISPUTE
- ABANDONED_BY_AUTHORITY
- UNRESOLVED

The generator cannot invent salvage law.

## 14. Cargo and lost property

Cargo should use provenance and custody links.

Possible consequences of lost cargo:
- supply shortages;
- environmental contamination;
- ownership disputes;
- insurance/compensation questions if canon later supports them;
- salvage expeditions;
- evidence in a case;
- unexpected habitat effects.

Do not assume every lost crate is loot.

## 15. Fishing boundary

Fishing can exist as:
- food production;
- sport;
- research;
- cultural practice;
- tourism;
- capture opportunity;
- stewardship issue.

This layer may schedule or contextualize fishing activity.

It may not define:
- encounter rolls;
- catch tables;
- bait bonuses;
- capture legality;
- yields;
- damage;
- species eligibility.

Those require PTU/Caelo and ecosystem rules.

## 16. Underwater settlement

```yaml
underwater_settlement_profile:
  settlement_id: null
  submerged_location_id: null
  access_system_ids: []
  breathable_space_refs: []
  power_dependency_ids: []
  communication_dependency_ids: []
  food_supply_refs: []
  water_or_environment_system_refs: []
  emergency_exit_ids: []
  rescue_plan_ids: []
  resident_ids: []
  visitor_policy_ids: []
  maintenance_project_ids: []
  habitat_overlap_ids: []
```

The system must not invent technology to justify an underwater settlement. Canon must define how it functions.

## 17. Marine rescue

Marine rescue extends the crisis/rescue layer with location-specific state.

Useful states:
- LAST_CONFIRMED_POSITION
- LAST_CONTACT
- DRIFT_ESTIMATE_CLAIM
- SEARCH_AREA
- VESSEL_CONDITION_UNKNOWN
- PERSON_OR_POKEMON_STATUS_UNKNOWN
- RESCUE_RESOURCE_ASSIGNMENT

Do not convert missing into injured/dead/stranded without evidence.

## 18. Navigation knowledge

Actors can know different versions of a route.

```yaml
marine_navigation_knowledge:
  holder_id: null
  sea_lane_id: null
  chart_ref: null
  known_markers: []
  known_hazard_refs: []
  known_current_refs: []
  freshness: null
  confidence: null
  source_ids: []
```

Old charts can be historically valid and currently wrong.

## 19. Maritime institutions

Potential institution roles:
- harbor authority or equivalent;
- ferry cooperative;
- rescue service;
- marine research station;
- fishery group;
- conservation/stewardship body;
- salvage operator;
- shipyard;
- lighthouse/navigation service;
- island council or local civic actor.

These are design categories, not automatic canon institutions.

## 20. Maritime world events

Examples:
- lane closure;
- unusual migration;
- harbor congestion;
- missing vessel;
- reef damage;
- wreck discovery;
- salvage dispute;
- service strike/shortage only if workplace canon supports it;
- communication outage;
- extreme tide window;
- floating debris field;
- underwater infrastructure failure;
- festival/sport event;
- marine research expedition.

Each event must point to causal state.

## 21. Minecraft representation

Possible presentation state:
- docks and berth occupancy;
- service signs;
- boat/vessel entities where supported;
- buoys/navigation markers;
- lighthouses;
- temporary barriers;
- wreck models;
- submerged structures;
- bubbles/lighting/visual effects;
- selected marine Pokémon entities;
- harbor workers;
- updated notice boards.

The adapter must not implement PTU rules itself.

## 22. Performance policy

Marine ecosystems should not require every fish or school to exist as a loaded entity.

Use coarse state for:
- migration;
- vessel journeys;
- deep-water populations;
- drift;
- off-screen search operations.

Materialize entities only when players enter an interaction bubble or when implementation requires it.

## 23. Encounter contract — Reef Passage Disturbance

Narrative premise: a normal passage through a reef becomes unsafe because a recent disturbance has changed where wild Pokémon gather.

FULL version:
- spatial reef channels;
- water terrain and movement legality;
- dynamic hazards or zones if supported;
- objectives such as REACH_EXIT or WITHDRAW;
- tactical AI aware of passage/territory;
- possible forced movement/current interaction only if authoritative.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED for Swim slice
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if current displacement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:
- fixed arena with legal Swim movement;
- reef walls represented as static blockers;
- no current, dynamic hazard or moving objective;
- battle resolves normally;
- route consequence handled in world state after combat/withdrawal.

## 24. Encounter contract — Wreck Interior Search

Narrative premise: players enter a partially submerged wreck while another actor or wild group contests access.

FULL version:
- mixed land/water spaces;
- changing access doors;
- interactable evidence/cargo;
- protect/search/escape objectives;
- environmental zones;
- tactical AI using chokepoints.

Required families beyond basic combat:
- terrain/weather/hazards/zones/reactions: BLOCKING
- complete movement/forced movement/interception: BLOCKING if water flow or chokepoint interception matters
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

REDUCED version:
- evidence/cargo remains outside battle state;
- one static room or deck becomes the legal battle arena;
- objects are non-interactive blockers;
- search/custody occurs before or after combat.

## 25. Encounter contract — Harbor Evacuation Chokepoint

Narrative premise: a harbor incident requires clearing a safe route while workers and passengers withdraw.

FULL version:
- PROTECT / CLEAR_ZONE / REACH_EXIT objectives;
- civilians/noncombatants;
- objective-aware AI;
- possible hazards and interactables;
- interception/forced movement only if authoritative.

REDUCED version:
- civilians remain off-grid;
- players clear one static chokepoint through normal battle;
- evacuation progress is resolved as world state after a legal result.

## 26. PTU/Caelo mechanical boundary

Before promotion to executable content, validate:
- Swim movement;
- Gilled and breathing capabilities;
- Mountable/travel eligibility;
- water terrain costs;
- underwater visibility/LoS;
- semi-invulnerable/Dive behavior;
- drowning/suffocation if present;
- weather at sea;
- fishing/capture interactions;
- boat/island travel rules in Caelo;
- water encounter tables;
- any Trainer Features that alter aquatic movement or survival.

Python AutoPTU contains aquatic movement and ocean-linked rule logic, but representative code does not prove Java parity or complete subsystem coverage.

## 27. Canon promotion checklist

Before a maritime proposal becomes canon:
1. Region/island geography is approved.
2. Harbors/services/institutions are approved.
3. Technology level is consistent with Ouros.
4. Marine ecology is consistent with species data.
5. Access mechanics are validated against PTU/Caelo.
6. Wreck/salvage ownership assumptions are reviewed.
7. Encounter implementation contract is feasible or reduced version is selected.
8. Minecraft representation does not duplicate PTU logic.
9. No external plot, characters or distinctive location has been transplanted.
