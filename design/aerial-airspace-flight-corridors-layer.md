# Ouros Aerial Airspace, Flight Corridors & Sky Ecology Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

Ouros already knows how to represent roads, ferries, public transport, weather, seasonal migration, forests, visibility, communication infrastructure and wild collectives. It needs a dedicated aerial layer so the sky does not collapse into one of two bad abstractions:

- `Flying Pokémon = unrestricted fast travel`, or
- `sky = empty visual space with no persistent state`.

This layer models aerial movement, aerial services, migration corridors, observation, closures and incidents as world state while keeping PTU tactical Sky movement under AutoPTU authority.

## Core separation

Ouros should preserve the following boundary:

```text
physical airspace state
→ route/service state
→ ecological use
→ actor knowledge
→ eligibility to travel
→ actual journey
→ optional tactical encounter snapshot
```

A Pokémon having Sky movement in PTU does not answer every step above.

## 1. Airspace regions

Airspace is represented in coarse 3D regions rather than per-block simulation.

```yaml
airspace_region:
  airspace_id: null
  horizontal_footprint_ref: null
  altitude_band_ids: []
  connected_airspace_ids: []
  terrain_below_refs: []
  settlement_refs: []
  weather_region_refs: []
  lightscape_refs: []
  migration_corridor_refs: []
  infrastructure_refs: []
  current_restriction_refs: []
  current_incident_refs: []
  last_revision_event_id: null
```

An airspace region may cover:

- a valley;
- a harbor approach;
- an urban district;
- a mountain pass;
- a wetland flyway;
- a coastal corridor;
- a research area;
- an elevated settlement;
- a route around a protected habitat.

Airspace identity should survive changes in services and temporary closures.

## 2. Altitude bands are coarse world state

Do not simulate every vertical meter.

```yaml
altitude_band:
  band_id: null
  airspace_id: null
  authored_label: null
  approximate_lower_bound: null
  approximate_upper_bound: null
  use_tags: []
  known_visibility_constraints: []
  known_weather_constraints: []
  ecological_use_refs: []
  infrastructure_intersection_refs: []
```

Candidate authored labels:

- GROUND_APPROACH
- LOW_TRANSIT
- RIDGE_LEVEL
- HIGH_TRANSIT
- ABOVE_CLOUD_REFERENCE

Those labels are narrative/world-state concepts. They do not imply PTU elevation mechanics.

## 3. Air corridors

An air corridor is a known route through airspace.

```yaml
air_corridor:
  corridor_id: null
  endpoint_refs: []
  airspace_segment_refs: []
  preferred_altitude_band_refs: []
  operator_refs: []
  intended_use_tags: []
  state: OPEN
  active_restriction_refs: []
  weather_dependency_refs: []
  ecological_conflict_refs: []
  navigation_aid_refs: []
  alternate_corridor_refs: []
  route_history_refs: []
  public_information_refs: []
```

Suggested states:

- OPEN
- LIMITED
- TEMPORARY_REROUTE
- WEATHER_RESTRICTED
- ECOLOGY_RESTRICTED
- EMERGENCY_ONLY
- CLOSED
- UNKNOWN

An air corridor can remain physically possible while a passenger service is suspended.

## 4. Aerial transport services

Aerial services extend the existing `transport_service` model.

```yaml
aerial_transport_service:
  service_id: null
  institution_id: null
  operator_ids: []
  route_ids: []
  stop_or_pad_ids: []
  pokemon_asset_ids: []
  vehicle_asset_ids: []
  staff_ids: []
  service_state: OPERATING
  passenger_policy_refs: []
  cargo_policy_refs: []
  weather_operating_refs: []
  wildlife_operating_refs: []
  maintenance_refs: []
  current_disruption_refs: []
  public_schedule_refs: []
```

No specific transport technology is canon by default.

Possible authored implementations include:

- Pokémon-assisted taxi;
- institutional survey flight;
- rescue deployment;
- courier service;
- airship or mechanical aircraft if canon later supports it;
- special event transport.

## 5. Individual Pokémon service state

A service Pokémon remains a persistent Pokémon entity.

```yaml
aerial_service_pokemon_assignment:
  pokemon_entity_id: null
  institution_id: null
  service_id: null
  assignment_state: null
  assignment_start_event_id: null
  assignment_end_event_id: null
  approved_route_refs: []
  handler_refs: []
  care_refs: []
  mechanical_validation_ref: null
```

Narrative assignment never grants Sky speed, Mountable, carrying capacity or endurance.

Those require authoritative rules/data.

## 6. Passenger-flight eligibility

The server must validate aerial travel separately from combat movement.

```yaml
aerial_access_assessment:
  assessment_id: null
  journey_id: null
  corridor_id: null
  service_id: null
  participant_ids: []
  pokemon_entity_ids: []
  world_requirements_checked: []
  permission_refs: []
  mechanical_capability_refs: []
  weather_state_ref: null
  service_state_ref: null
  result: UNKNOWN
  unresolved_requirements: []
```

Possible results:

- ELIGIBLE
- ELIGIBLE_WITH_SERVICE
- REQUIRES_GUIDE
- REQUIRES_AUTHORIZATION
- TEMPORARILY_UNAVAILABLE
- MECHANICALLY_UNRESOLVED
- NOT_ELIGIBLE

A large Flying Pokémon must not pass this gate merely from species appearance.

## 7. Aerial migration corridors

Wild Pokémon use the sky independently of transport routes.

```yaml
aerial_migration_corridor:
  migration_id: null
  species_or_collective_refs: []
  broad_footprint_ref: null
  typical_altitude_band_refs: []
  seasonal_window_refs: []
  stopover_site_refs: []
  route_confidence: null
  observation_refs: []
  weather_sensitivity_refs: []
  light_sensitivity_refs: []
  disturbance_refs: []
  current_state: EXPECTED
```

Suggested states:

- EXPECTED
- OBSERVED_ACTIVE
- DELAYED
- EARLY
- DIVERTED
- PARTIALLY_OBSERVED
- NOT_OBSERVED
- UNKNOWN

A migration corridor is broad and probabilistic. It is not a rail that every individual follows.

## 8. Stopover sites

Aerial migration can depend on places on the ground.

```yaml
aerial_stopover_site:
  site_id: null
  location_ref: null
  habitat_refs: []
  known_user_refs: []
  seasonal_use_refs: []
  resource_dependency_refs: []
  disturbance_refs: []
  conservation_refs: []
  last_observation_event_id: null
```

Stopover sites may include:

- wetlands;
- cliffs;
- forest canopy;
- coastal islands;
- towers;
- open fields;
- reservoirs;
- urban roofs where authored ecology supports it.

## 9. Aerial observation

Aerial surveys can reveal information unavailable from the ground, but they are not omniscient.

```yaml
aerial_observation:
  observation_id: null
  observer_ids: []
  platform_ref: null
  route_ref: null
  time_ref: null
  altitude_band_ref: null
  observed_area_ref: null
  visibility_conditions: []
  observed_fact_refs: []
  uncertain_claim_refs: []
  photography_refs: []
  map_update_refs: []
  coverage_quality: null
```

Occlusion sources can include:

- cloud;
- canopy;
- terrain relief;
- darkness;
- glare;
- smoke;
- fog;
- distance;
- observer attention.

Exact visual mechanics remain outside this layer.

## 10. Aerial incidents

Aerial incidents should preserve uncertainty.

```yaml
aerial_incident:
  incident_id: null
  airspace_ref: null
  corridor_ref: null
  time_ref: null
  report_refs: []
  involved_actor_refs: []
  involved_pokemon_refs: []
  physical_observation_refs: []
  possible_cause_refs: []
  confirmed_cause_refs: []
  service_impact_refs: []
  ecological_impact_refs: []
  case_ref: null
  resolution_state: OPEN
```

Examples:

- unexpected flock concentration;
- communication-light conflict;
- route lost in fog;
- service Pokémon refuses an approach;
- navigation beacon outage;
- survey craft returns early;
- reported collision or near miss;
- unusual migration altitude;
- aerial courier missing a scheduled arrival.

An incident is not proof of sabotage, aggression or mechanical injury.

## 11. Wildlife/transport conflict

Conflicts between aerial services and Pokémon need a causal workflow.

```text
observed conflict
→ establish where/when it occurs
→ identify species/collective if possible
→ establish behavior and route use
→ compare service route/timing
→ test mitigations
→ monitor consequences
```

Potential mitigations can include:

- schedule change;
- route shift;
- temporary seasonal closure;
- light change;
- habitat restoration elsewhere;
- public warning;
- altered approach route;
- remote observation;
- no intervention if evidence does not justify one.

No mitigation should grant an unsupported PTU modifier.

## 12. Navigation aids and landmarks

Aerial travel can use persistent landmarks.

```yaml
aerial_navigation_aid:
  aid_id: null
  type: null
  physical_asset_ref: null
  service_area_refs: []
  operating_state: null
  operator_ref: null
  maintenance_ref: null
  public_information_ref: null
  visual_signal_ref: null
  acoustic_signal_ref: null
```

Possible types:

- beacon;
- tower;
- signal light;
- radio relay if canon supports it;
- painted marker;
- natural landmark;
- route station.

A lighthouse or beacon can serve maritime and aerial navigation at the same time.

## 13. Weather and airspace

Meteorology owns weather truth and forecasts.

This layer consumes that state.

Examples:

- cloud may reduce survey visibility;
- wind may cause service restrictions;
- storms may close routes;
- unusual seasonal conditions may shift migration;
- smoke may change both visibility and route policy.

None of these automatically create PTU Weather.

## 14. Light and airspace

Light can create navigation and ecological interactions.

Examples:

- beacons;
- city glow;
- stadium lighting;
- migrating Pokémon attracted, confused or unaffected depending on authored evidence;
- biological signals;
- nighttime service restrictions.

Never generalize one species' response to every Flying Pokémon.

## 15. Communications

An air route can have incomplete information.

```text
incident occurs
→ operator receives report
→ verification
→ route notice published
→ passengers receive or miss notice
```

A route closure should not become universal player knowledge until the information travels through an existing channel.

## 16. Cartography

Aerial maps and charts should be versioned.

A route edition can become obsolete because of:

- new towers/buildings;
- habitat change;
- altered settlement boundaries;
- a new service hub;
- migration research;
- changed weather policy;
- temporary hazards;
- changed access permissions.

Historical charts remain valid records of past world state.

## 17. Airspace and elevated settlements

If Ouros later authors sky islands, cliff cities, floating structures or elevated research stations, they remain normal persistent locations.

They need:

- access graph;
- residence/services;
- infrastructure;
- ecology;
- emergency routes;
- supply dependencies;
- route permissions;
- world-state history.

Being physically elevated does not exempt them from Travel, Demography, Infrastructure or Governance systems.

## 18. Battle projection boundary

World airspace must not be projected directly into PTU combat.

```yaml
battle_aerial_projection_request:
  encounter_id: null
  source_airspace_ref: null
  selected_static_geometry_ref: null
  requested_altitude_features: []
  requested_weather_features: []
  requested_forced_movement_features: []
  requested_falling_features: []
  required_capability_families: []
  reduced_version_ref: null
```

Until verified, the safe reduced pattern is:

1. resolve route/altitude/landing world state before battle;
2. choose a stable tactical slice;
3. place only actual combatants;
4. run a standard legal encounter;
5. write results back to world state.

## 19. Permanent capability dependency map

Aerial concepts may depend on the engine categories as follows.

`targeting/footprints/range/LoS` — VERIFIED as a category, but LoS is not altitude-aware vision by default.

`base movement legality` — VERIFIED for current Shift/Jump/Sky primitives. This does not prove long-range flight or passenger transport.

`complete movement including push/pull/knockback/interception/forced movement` — BLOCKING for true aerial displacement, interception or falling interactions.

`core calculations` — VERIFIED.

`action economy/initiative` — VERIFIED.

`full turn/round lifecycle` — PARTIAL.

`full stateful damage pipeline` — PARTIAL.

`status lifecycle` — PARTIAL.

`terrain/weather/hazards/zones/reactions` — BLOCKING as a complete family. Semantic Weather/Terrain state exists, but full execution is not verified.

`move-specific behavior` — PARTIAL.

`abilities` — PARTIAL.

`items` — PARTIAL.

`Trainer Features/perks` — PARTIAL.

`AI legal-action infrastructure` — VERIFIED.

`AI tactical policy` — BLOCKING.

`Minecraft/Cobblemon/Craftics adapter/playback` — BLOCKING.

## 20. Aerial-specific blockers outside the battle core

The overworld/server layer still needs explicit contracts for:

- `AIRSPACE_REGION_STATE`
- `AIR_CORRIDOR_GRAPH`
- `AERIAL_SERVICE_OPERATION`
- `AERIAL_PASSENGER_ELIGIBILITY`
- `MIGRATION_FLYWAY_STATE`
- `AERIAL_STOPOVER_STATE`
- `AERIAL_OBSERVATION_COVERAGE`
- `AERIAL_INCIDENT_HISTORY`
- `AERIAL_NAVIGATION_AIDS`
- `AIRSPACE_TO_COBBLEMON_PROJECTION`
- `AIRSPACE_TO_BATTLE_SNAPSHOT`

## 21. Guardrails

Do not infer:

- Flying type → can carry people;
- Sky speed → safe long-distance travel;
- Levitate → aviation;
- large body → Mountable;
- migration corridor → every individual follows it;
- flock → hostile group;
- route deviation → weather cause;
- near miss → wild Pokémon aggression;
- service refusal → Injury or fear;
- cloud/fog → Accuracy penalty;
- high altitude → damage;
- strong wind → forced movement;
- airborne combat → 3D tactical support;
- visible Flying Pokémon → legal participant in an air service.

## 22. Implementation sequence

A safe implementation order is:

1. persistent airspace/corridor records;
2. aerial service schedules and route state;
3. migration corridor observations;
4. aerial observation/map updates;
5. incident/closure integration;
6. Minecraft presentation of routes/services;
7. capability validation for personal Pokémon-assisted travel;
8. static aerial encounter projection;
9. only later, real vertical tactical mechanics.

## 23. Canon questions

Before promotion, human authors should decide:

- which regions have formal aerial services;
- whether mechanical aircraft/airships exist;
- which routes existed before players;
- which migration corridors are known at campaign start;
- whether any elevated settlements are canon;
- who manages public air-route information;
- which institutions can temporarily close routes;
- what passenger/cargo rules exist;
- which PTU/Caelo flight capabilities govern personal travel;
- whether long-range flight has fatigue/endurance constraints;
- whether AutoPTU will ever support explicit altitude layers.
