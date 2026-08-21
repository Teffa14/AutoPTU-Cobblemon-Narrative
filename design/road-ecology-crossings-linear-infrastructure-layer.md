# Ouros Road Ecology, Crossings & Linear Infrastructure Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Travel already models roads as human connections. Conservation already models habitat corridors. Public Works already models proposals and implementation. Freshwater already models water movement. This layer defines the ecological interface between those systems.

The key idea is that linear infrastructure can change movement without changing the underlying identity of a population or location. A road can remain physically open while becoming a barrier for a wild collective. A culvert can pass water while failing as animal passage. A wildlife crossing can exist but remain poorly used. A fence can reduce one conflict and create another at its endpoint.

## Core separations

Keep these truths independent:

- physical infrastructure state;
- transport-service state;
- traffic/use intensity;
- habitat connectivity;
- observed crossing behavior;
- collision or near-miss evidence;
- management policy;
- public belief;
- Pokémon population/collective state;
- tactical AutoPTU state.

A road sign does not create a corridor. A road closure does not prove wildlife recovery. A crossing used once does not prove success. An encounter on a road does not prove the road caused it.

## Persistent schema

```yaml
linear_infrastructure_system:
  linear_system_id: null
  route_connection_ids: []
  segment_ids: []
  infrastructure_asset_ids: []
  operating_actor_ids: []
  stewardship_area_ids: []
  freshwater_reach_ids: []
  settlement_ids: []
  public_works_project_ids: []
  canon_status: proposed
```

```yaml
linear_segment:
  segment_id: null
  linear_system_id: null
  segment_type: ROAD
  endpoint_location_ids: []
  physical_state: OPEN
  surface_descriptor: null
  traffic_use_band: unknown
  lighting_asset_ids: []
  drainage_asset_ids: []
  fence_asset_ids: []
  crossing_asset_ids: []
  adjacent_habitat_ids: []
  intersected_corridor_ids: []
  observation_ids: []
  incident_ids: []
  current_management_ids: []
```

Candidate segment types are descriptive only:

ROAD, TRAIL, RAIL, BRIDGE_APPROACH, CAUSEWAY, UTILITY_CORRIDOR, SERVICE_TRACK, CANAL_EDGE, URBAN_ARTERIAL, RURAL_LINK, OTHER_AUTHORED_LINEAR_ASSET.

No segment type creates PTU Terrain by itself.

## Connectivity state

Habitat connectivity should be evaluated for a specific movement need or population, not as a universal score.

```yaml
connectivity_assessment:
  assessment_id: null
  segment_id: null
  population_or_collective_ids: []
  movement_purpose_claims: []
  evidence_ids: []
  known_barriers: []
  known_passage_options: []
  seasonal_conditions: []
  avoidance_observations: []
  crossing_observations: []
  confidence: null
  assessment_date_or_clock: null
  interpretation_status: proposed
```

Movement purposes can include seasonal migration, daily foraging, access to water, nesting, dispersal, refuge movement, spawning access or an authored species-specific need.

Do not infer purpose from route geometry alone.

## Crossing assets

```yaml
wildlife_crossing_asset:
  crossing_id: null
  segment_id: null
  crossing_type: null
  linked_habitat_ids: []
  target_population_claim_ids: []
  physical_condition: null
  approach_condition_ids: []
  guidance_fence_ids: []
  water_passage_refs: []
  monitoring_point_ids: []
  opened_event_id: null
  retrofit_history_ids: []
  maintenance_history_ids: []
```

Candidate types:

- OVERPASS
- UNDERPASS
- CULVERT_PASSAGE
- BRIDGE_UNDERCROSSING
- RIPARIAN_SPAN
- AMPHIBIAN_PASSAGE
- FISH_PASSAGE_RETROFIT
- AT_GRADE_SEASONAL_CROSSING
- AUTHORED_OTHER

A crossing should not receive a generic `works=true` flag.

## Crossing adoption and monitoring

Some animals may need time before regularly using a new crossing. That makes longitudinal monitoring useful worldbuilding.

```yaml
crossing_use_observation:
  observation_id: null
  crossing_id: null
  timestamp_or_window: null
  source_type: CAMERA_TRAP
  observed_species_or_entity_ids: []
  observed_count_or_band: null
  direction: null
  successful_passage_observed: unknown
  approach_without_crossing: unknown
  provenance_id: null
  observer_interpretation_ids: []
```

Possible sources include camera traps, field observation, tracks, acoustic observations, telemetry if canon supports it, resident reports and maintenance logs.

Connect visual evidence to the Photography layer. Do not merge two Pokémon entities from blurry imagery without corroboration.

## Collision and near-miss records

```yaml
linear_conflict_incident:
  incident_id: null
  segment_id: null
  timestamp: null
  involved_actor_ids: []
  involved_pokemon_entity_ids: []
  involved_population_claim_ids: []
  incident_type: null
  observation_ids: []
  injury_or_damage_claim_ids: []
  confirmed_outcome_ids: []
  traffic_state_ids: []
  weather_state_ids: []
  public_report_ids: []
  investigation_case_id: null
```

Possible incident types:

CROSSING_OBSTRUCTION, NEAR_MISS, VEHICLE_COLLISION, RAIL_OBSTRUCTION, FENCE_ENTRAPMENT, CULVERT_TRAP, SERVICE_DISRUPTION, UNKNOWN_LINEAR_CONFLICT.

Narrative generation cannot create mechanical Injuries or death from a road incident unless authoritative rules/world resolution support that result.

## Fencing and guidance state

Fences are directional infrastructure, not invisible walls.

```yaml
movement_guidance_asset:
  guidance_asset_id: null
  segment_id: null
  geometry_ref: null
  intended_function: null
  linked_crossing_ids: []
  condition: null
  known_gap_ids: []
  endpoint_ids: []
  monitoring_ids: []
  maintenance_ids: []
```

A fence can:
- reduce access to a road segment;
- guide movement toward a crossing;
- shift pressure toward an endpoint;
- create entrapment risk if damaged;
- fail differently for different species or movement modes.

No fence applies forced movement inside battle unless that exact geometry and mechanic are implemented.

## Road-stream crossings

Road Ecology must connect directly to Freshwater.

```yaml
road_stream_crossing:
  crossing_id: null
  linear_segment_id: null
  freshwater_reach_id: null
  hydraulic_asset_id: null
  water_conveyance_state: null
  aquatic_passage_assessment_ids: []
  terrestrial_bank_passage_assessment_ids: []
  flood_capacity_refs: []
  sediment_refs: []
  maintenance_ids: []
```

`water passes` and `wildlife passes` are different claims.

A culvert can be hydraulically adequate but ecologically poor. A large bridge can preserve bank movement while still generating noise or lighting disturbance.

## Traffic/use intensity

Avoid detailed vehicle simulation by default.

Use coarse state:

- VERY_LOW
- LOW
- MODERATE
- HIGH
- EVENT_SURGE
- SERVICE_ONLY
- CLOSED
- UNKNOWN

Traffic/use bands should be derived from route schedules, settlement activity, event state, construction, diversions and observations.

They should not be recomputed from loaded Minecraft entities.

## Temporal patterns

Connectivity can vary by:

- season;
- time of day;
- school/work commute windows;
- migration periods;
- weather;
- festival surges;
- construction phases;
- emergency detours;
- road closure windows;
- maintenance cycles.

This should connect to Seasonality and Demography rather than create duplicate clocks.

## Mitigation projects

```yaml
linear_mitigation_project:
  project_id: null
  affected_segment_ids: []
  problem_statement_ids: []
  evidence_ids: []
  target_population_claim_ids: []
  proposed_measures: []
  alternative_ids: []
  public_works_proposal_id: null
  implementation_events: []
  monitoring_plan_ids: []
  review_ids: []
  status: PROPOSED
```

Measures can include:

- overpass/underpass construction;
- culvert retrofit;
- longer bridge span;
- fencing/guidance changes;
- seasonal closure;
- speed/use management where canon supports it;
- lighting change;
- route realignment;
- habitat restoration near approaches;
- decommissioning;
- monitoring only.

The generator must not assume the most expensive intervention is best.

## Learning and unintended consequences

A mitigation project can partially fail.

Examples:

- target animals avoid the structure;
- another species begins using it unexpectedly;
- fencing shifts crossings toward an unprotected endpoint;
- flood debris blocks a culvert;
- improved human access increases visitor pressure nearby;
- a crossing becomes a useful route for a predator;
- a road closure harms a transport-dependent settlement more than expected.

Preserve those results as history. Do not retcon the original decision into stupidity or sabotage.

## Minecraft projection

Minecraft may render:

- road/rail geometry;
- culverts and bridges;
- underpasses/overpasses;
- fencing;
- crossing signs;
- camera traps;
- maintenance crews;
- seasonal gates;
- roadkill-free incident markers or investigation props;
- changed vegetation around approaches;
- temporary detours.

The server-owned world graph remains authoritative.

Loaded Pokémon entities are presentation/sample state, not population truth.

## Cobblemon projection

Possible future projection inputs:

- corridor status;
- crossing adoption band;
- adjacent habitat state;
- time/season;
- disturbance history;
- road closure state.

Anti-exploit rule:

Players cannot farm rare spawns by rapidly opening/closing gates, placing fences or repeatedly crossing a trigger. Ecological changes require validated state transitions and coarse time.

## Narrative hooks

Road Ecology can create:

- wildlife-crossing surveys;
- camera-trap retrieval;
- culvert inspection;
- missing migration observations;
- bridge retrofit debates;
- seasonal closure logistics;
- route reopening after mitigation;
- historical road alignment research;
- settlement tradeoff stories;
- construction-stage encounters;
- stranded individual rescue;
- misinformation about a supposed problem species;
- monitoring projects lasting several years.

## PTU/Caelo guardrails

This layer creates no battle rule by itself.

Do not infer:

- collision damage;
- vehicle knockback;
- road Rough/Slow Terrain;
- fence forced movement;
- interception;
- reaction attacks;
- road-crossing Skill DCs;
- herd morale;
- automatic Run Away;
- Pack Mon;
- water-current penalties;
- bridge-fall mechanics;
- traffic initiative slots.

Exact capabilities must come from validated PTU/Caelo rules and implementation evidence.

## Encounter contract A — Crossing Retrofit Survey

Narrative premise: researchers and maintenance workers inspect a newly opened underpass because target Pokémon still appear to cross elsewhere.

FULL version:
- moving wild actors with CROSS/WITHDRAW goals;
- road boundary or dangerous lane represented tactically;
- fencing/gaps as meaningful movement constraints;
- objective-aware AI;
- possible interception/rescue;
- dynamic traffic/service windows if canon supports them.

Required capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement where used;
- action economy/initiative;
- full turn/round lifecycle;
- terrain/weather/hazards/zones/reactions if the road itself becomes a tactical zone;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED version:
- crossing observations and traffic are resolved in overworld state;
- the server identifies a safe static inspection area;
- any actual conflict becomes a conventional AutoPTU encounter on static geometry;
- target population movement remains outside the grid unless those Pokémon truly join the encounter.

## Encounter contract B — Culvert After the Storm

Narrative premise: a storm leaves a road open to people but potentially blocks aquatic and terrestrial passage beneath it.

FULL version:
- dynamic water or debris state;
- multiple movement routes;
- interactable obstruction;
- protected inspection objective;
- wildlife withdrawal/reach-exit behavior;
- hazard/reaction support if water or debris matters mechanically.

REDUCED version:
- Freshwater resolves hydraulic state before battle;
- inspection/debris clearing occurs in overworld;
- AutoPTU receives a dry/static or otherwise prevalidated arena if combat occurs;
- no current, flooding or debris damage is simulated tactically.

## Encounter contract C — Fence-End Bottleneck

Narrative premise: mitigation reduced crossings along most of a road but concentrated movement near the end of a fence.

FULL version:
- mobile non-hostile Pokémon attempting to cross;
- actors able to block, redirect or protect routes;
- objective-aware AI;
- interception and zone control;
- possibly civilians/service vehicles kept as noncombatants.

REDUCED version:
- movement pressure is represented by world-state observations;
- service is paused or rerouted before combat;
- only hostile/engaged combatants enter a static arena;
- later narrative resolution updates the mitigation design.

## Promotion gate

No Road Ecology encounter may use road collision, moving traffic, forced movement, wildlife crossing AI, current effects, dynamic barriers or objective-aware withdrawal until the exact required capability families are verified or the encounter contract explicitly uses the reduced version.