# Railways, Stations & Rail Operations Layer

Status: PROPOSED SYSTEM DESIGN. Not canon. Not a PTU rules replacement.
Pass: 97

## Purpose

This layer gives Ouros a persistent model for rail corridors, stations, trains, yards, service patterns, dispatch constraints and rail incidents.

The existing Travel layer remains the owner of generic journeys and connections. Technology remains the owner of machinery, signals, power and technical faults. This layer adds the rail-specific topology and operational state that sits between them.

The design goal is causal transportation rather than a railroad simulator.

A train can be late because another movement occupies the only usable segment, because a signal asset is degraded, because a platform is unavailable or because a storm damaged a bridge. It should not be late because the narrative generator wants an encounter.

## Core separations

Ouros must keep these facts independent:

- physical track exists;
- track is operational;
- a route path is available;
- a movement slot is available;
- a specific service is scheduled;
- a specific train is assigned;
- the train is physically present;
- a platform is usable;
- a passenger has permission/ticket state if canon requires it;
- a passenger knows the current service state;
- public information says the service is running;
- a tactical battle can legally occur there.

A train on a map is not universal fast travel.

A Minecraft minecart moving on rails is not proof that a canonical Ouros railway service exists.

## 1. RAIL_NETWORK

```yaml
rail_network:
  rail_network_id: null
  name_ref: null
  geographic_scope_ids: []
  operator_institution_ids: []
  corridor_ids: []
  station_ids: []
  yard_ids: []
  junction_ids: []
  service_pattern_ids: []
  infrastructure_network_refs: []
  public_information_refs: []
  historical_revision_ids: []
  canon_refs: []
```

A region may have several independent networks.

Do not assume interoperability, common fares, common gauges, government ownership or reciprocal access until authored canon establishes them.

## 2. RAIL_CORRIDOR

A corridor is the persistent physical connection along which rail movements can occur.

```yaml
rail_corridor:
  corridor_id: null
  endpoint_station_ids: []
  segment_ids: []
  junction_ids: []
  crossing_ids: []
  bridge_tunnel_asset_refs: []
  environment_refs: []
  current_operational_state: UNKNOWN
  active_restriction_ids: []
  historical_revision_ids: []
```

Suggested corridor states:
- OPEN
- DEGRADED
- RESTRICTED
- MAINTENANCE
- BLOCKED
- ISOLATED
- CLOSED
- DECOMMISSIONED
- UNKNOWN

This layer never derives movement speed or battle Terrain from those labels.

## 3. TRACK_SEGMENT

```yaml
track_segment:
  segment_id: null
  corridor_id: null
  endpoint_node_ids: []
  topology_type: SINGLE | DOUBLE | YARD | SIDING | TERMINAL_APPROACH | OTHER
  adjacent_segment_ids: []
  technical_asset_refs: []
  current_state: OPEN
  occupancy_state: CLEAR
  occupancy_ref: null
  restriction_refs: []
  inspection_refs: []
  maintenance_refs: []
  physical_revision_ref: null
```

`SINGLE` and `DOUBLE` are topology descriptions only.

They do not import real-world capacity formulas.

## 4. JUNCTION_AND_ROUTE_AUTHORITY

Junctions create incompatible possible movements.

```yaml
rail_junction:
  junction_id: null
  connected_segment_ids: []
  control_asset_refs: []
  possible_route_ids: []
  current_route_state: null
  current_fault_refs: []
```

```yaml
rail_route_slot:
  slot_id: null
  movement_path_ids: []
  requested_by_service_id: null
  train_id: null
  time_window_ref: null
  state: AVAILABLE
  conflict_ref_ids: []
  dispatch_decision_ref: null
```

Suggested states:
- AVAILABLE
- REQUESTED
- RESERVED
- OCCUPIED
- RELEASED
- BLOCKED
- MAINTENANCE
- UNKNOWN

This is coarse world-state orchestration, not a simulation of signal blocks.

## 5. RAIL_STATION

A station is a persistent location, not just a travel menu.

```yaml
rail_station:
  station_id: null
  settlement_id: null
  location_id: null
  operator_ids: []
  platform_ids: []
  concourse_public_space_id: null
  station_forecourt_id: null
  interchange_service_ids: []
  staff_role_ids: []
  passenger_information_channel_ids: []
  access_policy_refs: []
  accessibility_refs: []
  freight_facility_refs: []
  current_operational_state: OPEN
  historical_revision_ids: []
```

Station state can be:
- OPEN
- PARTIAL
- PLATFORM_RESTRICTED
- TRANSFER_ONLY
- EMERGENCY_ONLY
- CLOSED_TEMPORARY
- CLOSED_LONG_TERM
- DECOMMISSIONED

The station can remain a social landmark after rail service ends.

## 6. PLATFORM

```yaml
rail_platform:
  platform_id: null
  station_id: null
  served_segment_ids: []
  supported_service_refs: []
  current_state: AVAILABLE
  current_train_ref: null
  access_state_ref: null
  crowd_state_ref: null
  accessibility_state_ref: null
  information_display_ref: null
```

A platform being unavailable should cause a routing or service consequence, not a random battle modifier.

## 7. RAIL_SERVICE_PATTERN

A service pattern is the advertised recurring relationship between stops.

```yaml
rail_service_pattern:
  service_id: null
  operator_id: null
  service_type: PASSENGER | FREIGHT | MIXED | MAINTENANCE | RESEARCH | EMERGENCY | SPECIAL
  stop_sequence: []
  normal_corridor_ids: []
  schedule_version_ref: null
  assigned_train_pool_ids: []
  dependency_refs: []
  current_service_state: OPERATING
  current_disruption_ids: []
```

Suggested service states:
- OPERATING
- LIMITED
- DELAYED
- SHORT_TURNED
- REROUTED
- REPLACEMENT_SERVICE
- SUSPENDED
- EMERGENCY_ONLY
- CLOSED

A service can be delayed even when every track remains physically intact.

## 8. TIMETABLE_VERSION

```yaml
rail_timetable_version:
  timetable_id: null
  service_id: null
  effective_from: null
  effective_to: null
  planned_stop_times: []
  planned_connection_refs: []
  planned_frequency_band: null
  source_ref: null
  supersedes_id: null
```

Timetables are plans.

They do not prove that a train actually ran.

Historic timetables should remain in archives and public memory.

## 9. TRAIN_INSTANCE

A train can be a persistent asset or a temporary world location when narratively important.

```yaml
train_instance:
  train_id: null
  operator_id: null
  vehicle_asset_refs: []
  consist_revision_id: null
  assigned_service_id: null
  current_location_ref: null
  current_segment_ref: null
  current_station_ref: null
  current_state: OUT_OF_SERVICE
  onboard_staff_ids: []
  passenger_manifest_policy_ref: null
  cargo_refs: []
  maintenance_refs: []
  incident_refs: []
```

Suggested states:
- OUT_OF_SERVICE
- PREPARING
- BOARDING
- IN_SERVICE
- HELD
- TURNING
- TERMINATED
- MAINTENANCE
- STRANDED
- EVACUATING

Do not simulate every passenger as an individual entity.

## 10. TEMPORARY_MOVING_LOCATION

When a train matters as a scene, it can expose an authored interior graph.

```yaml
moving_location_projection:
  projection_id: null
  train_id: null
  carriage_node_ids: []
  connection_edges: []
  public_area_ids: []
  restricted_area_ids: []
  current_stop_ref: null
  movement_state: null
  world_clock_ref: null
```

The train's movement through the overworld and the interior scene do not need frame-by-frame synchronization.

For most narrative scenes, a service can advance between station milestones while the interior remains a stable local instance.

## 11. RAIL_YARD

```yaml
rail_yard:
  yard_id: null
  location_id: null
  operator_ids: []
  track_segment_ids: []
  storage_track_ids: []
  maintenance_asset_refs: []
  freight_transfer_refs: []
  staff_role_ids: []
  access_policy_refs: []
  current_state: NORMAL
```

Yards can support:
- vehicle inspection;
- freight transfer;
- train assembly;
- maintenance;
- storage;
- emergency staging;
- investigations;
- illicit diversion cases.

Yards are not generic combat arenas.

## 12. FREIGHT_MOVEMENT

Cargo state belongs to provenance/custody systems. Rail only records the transport leg.

```yaml
rail_freight_leg:
  freight_leg_id: null
  cargo_ref_ids: []
  custody_refs: []
  origin_facility_id: null
  destination_facility_id: null
  train_id: null
  planned_service_ref: null
  loaded_event_ref: null
  unloaded_event_ref: null
  current_state: PLANNED
  disruption_ids: []
```

A train carrying a missing shipment does not prove rail staff diverted it.

## 13. TRANSFER_AND_CONNECTION

A transfer is a dependency between journeys or services.

```yaml
transfer_connection:
  transfer_id: null
  inbound_service_ref: null
  outbound_service_ref: null
  station_id: null
  planned_window_ref: null
  accessibility_requirements: []
  luggage_or_cargo_requirements: []
  actual_outcome: UNKNOWN
  disruption_refs: []
```

Suggested outcomes:
- MADE
- MISSED
- HELD_FOR_CONNECTION
- REBOOKED
- STRANDED
- CANCELLED
- UNKNOWN

A missed connection can create a social scene or information gap without needing a quest.

## 14. RAIL_INCIDENT

```yaml
rail_incident:
  incident_id: null
  incident_type: null
  location_refs: []
  first_observed_at: null
  affected_segment_ids: []
  affected_service_ids: []
  observed_facts: []
  hypothesis_refs: []
  case_ref: null
  crisis_ref: null
  operational_response_refs: []
  recovery_refs: []
  current_state: OPEN
```

Candidate incident families:
- OBSTRUCTION
- SIGNAL_OR_CONTROL_FAULT
- TRACK_DAMAGE
- POWER_FAILURE
- PLATFORM_UNAVAILABLE
- TRAIN_FAILURE
- WEATHER_IMPACT
- WILDLIFE_INTERACTION
- FREIGHT_PROBLEM
- ACCESS_PROBLEM
- INFORMATION_FAILURE
- UNKNOWN

`OBSTRUCTION` never means hostile Pokémon by default.

## 15. GRADE_CROSSING

A grade crossing is an interface between rail and road/pedestrian systems.

```yaml
grade_crossing:
  crossing_id: null
  rail_segment_ids: []
  road_or_path_refs: []
  control_asset_refs: []
  current_rail_priority_state: null
  current_road_access_state: null
  incident_history_ids: []
  emergency_contact_ref: null
  wildlife_connectivity_ref: null
```

A crossing closure can affect:
- commuters;
- emergency services;
- wildlife movement;
- deliveries;
- school/work schedules;
- public events;
- alternative routes.

## 16. RAIL_AND_ECOLOGY

Rail corridors interact with existing ecological systems through explicit observations.

Possible evidence-backed states:
- population repeatedly crosses at one culvert;
- group avoids a busy segment;
- abandoned track bed becomes a travel corridor;
- nesting occurs near a low-use siding;
- freight yard lighting changes nocturnal activity;
- maintenance changes vegetation along a right-of-way.

Forbidden inference:

```text
railway exists -> habitat fragmented
```

The effect must be local and evidence-backed.

## 17. STATION_AS_PUBLIC_SPACE

Station interiors and forecourts reuse Urban Public Space rather than creating a second crowd model.

Possible station-specific rhythms:
- first departures;
- commuter peak;
- school arrival window;
- market-day surge;
- match-day surge;
- overnight quiet;
- disrupted-service crowding;
- emergency shelter or staging use.

A crowd state does not create tactical penalties.

## 18. INFORMATION_AND_SERVICE_TRUTH

Keep these separate:

```text
actual train movement
-> operator operational record
-> passenger-information packet
-> station display / announcement
-> passenger receipt
-> passenger belief
```

A stale display can be wrong without changing the train's actual position.

A rumor that a line is closed does not close it.

## 19. MINECRAFT_PROJECTION

Minecraft may render:
- tracks;
- signals;
- platforms;
- station clocks;
- departure boards;
- trains or simplified vehicle entities;
- barriers;
- yards;
- freight objects;
- damaged infrastructure;
- decommissioned alignments.

Minecraft must not own:
- route authority;
- timetable truth;
- service eligibility;
- cargo provenance;
- rail safety rules;
- vehicle collision rules;
- PTU battle outcomes.

Recommended server flow:

```text
rail world state
-> derive visible operational projection
-> Minecraft renders current revision
-> player requests travel/access/action
-> server validates route/service/access
-> journey state updates
-> if battle occurs, freeze a separate BattleSpec
```

## 20. BATTLE BOUNDARY

Rail scenes often tempt the adapter to invent mechanics. Do not do that.

A narrative rail scene does not automatically imply:
- moving platforms;
- train collision damage;
- forced movement;
- vehicle initiative;
- pursuit speed;
- electrified rails;
- platform-edge falling;
- moving cover;
- carriage coupling mechanics;
- track hazards;
- signal-based battlefield effects.

Each requires an explicit PTU/Caelo rule and verified engine support where applicable.

## 21. PERMANENT CAPABILITY DEPENDENCIES

The project-wide permanent categories remain:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Pass 97 does not promote any category.

The current Java evidence strengthens lifecycle/Trainer resource state but does not implement rail mechanics.

## 22. ENCOUNTER CONTRACT — Grade Crossing Obstruction

Narrative premise:
A recurring Pokémon presence blocks a rail-road crossing shortly before a critical service movement. Players must determine why the location is being used and reopen safe passage without assuming hostility.

FULL version:
- moving rail deadline represented inside the encounter;
- objective `CLEAR_CROSSING` or `WITHDRAW_FROM_ZONE`;
- Pokémon AI able to retreat toward safe habitat;
- road/rail protected zones;
- possible interception without mandatory KO;
- semantic playback of barrier/service state.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:
- dispatch holds the train outside the tactical scene;
- overworld state closes road/rail movements;
- players investigate the Pokémon use of the crossing;
- if conflict occurs, battle uses one static arena with the track represented only as geometry;
- after a legal resolution, world state updates the crossing and dispatch releases or reroutes service.

The narrative premise remains intact.

## 23. ENCOUNTER CONTRACT — Yard Transfer Interruption

Narrative premise:
A freight transfer stops when a Pokémon, equipment problem or human incident makes one yard throat unavailable. Cargo custody matters because several shipments are moving simultaneously.

FULL version:
- multiple route lanes;
- cargo/protect objectives;
- moving equipment or train sections;
- AI aware of escape/protection goals;
- interactable switches or gates only if mechanically supported;
- tactical consequences for changing route availability.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception — BLOCKING;
- full lifecycle — PARTIAL;
- terrain/hazards/zones/reactions — BLOCKING;
- items — PARTIAL if any mechanical item is used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:
- yard dispatcher isolates a safe static section;
- all train/cargo movements pause before battle;
- cargo remains world-state/custody objects outside the grid;
- AutoPTU resolves only combatants in the isolated area;
- transfer resumes, reroutes or remains suspended based on the result and technical investigation.

## 24. ENCOUNTER CONTRACT — Onboard Investigation Escalation

Narrative premise:
A passenger service develops a mystery while between stations. Players move through carriages, interview passengers and inspect evidence. A confrontation may occur before arrival.

FULL version:
- train as moving world location;
- carriage graph changes when cars are coupled/isolated;
- time-to-arrival clock;
- protected passengers;
- objective-aware AI;
- possible multi-car pursuit;
- deterministic playback of doors/couplers where supported.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED within a frozen carriage map;
- base movement legality — VERIFIED within static geometry;
- complete movement/interception — BLOCKING for pursuit/forced interactions;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- terrain/hazards/zones/reactions — BLOCKING if carriage state changes tactically;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:
- moving train remains an overworld/instance clock;
- investigation occurs carriage by carriage outside battle;
- if confrontation begins, the current carriage set is frozen as one static BattleSpec;
- civilians are removed to safe world-state positions before tactical resolution;
- arrival occurs after the battle or after a separate noncombat clock decision.

## 25. OUT-OF-BATTLE BLOCKERS

Pass 97 adds these implementation contracts outside the battle core:

- `RAIL_NETWORK_STATE`;
- `TRACK_SEGMENT_TOPOLOGY_AND_REVISION`;
- `RAIL_ROUTE_SLOT_STATE`;
- `STATION_PLATFORM_STATE`;
- `TIMETABLE_VERSIONING`;
- `TRAIN_INSTANCE_LOCATION`;
- `TRANSFER_CONNECTION_STATE`;
- `RAIL_FREIGHT_LEG`;
- `GRADE_CROSSING_STATE`;
- `RAIL_INCIDENT_AND_RECOVERY`;
- `RAIL_TO_TRAVEL_HANDOFF`;
- `RAIL_TO_TECHNOLOGY_HANDOFF`;
- `RAIL_TO_MINECRAFT_PROJECTION`;
- `RAIL_TO_BATTLE_SNAPSHOT`.

These belong to the world/server integration layer, not AutoPTU-Java.

## 26. CANON QUESTIONS

Before rail becomes canon, Ouros needs authored decisions on:
- whether railways exist at launch;
- which regions have them;
- passenger, freight or mixed roles;
- technology level and power source;
- whether separate operators exist;
- whether any line crosses regional boundaries;
- whether abandoned alignments predate the players;
- whether Pokémon are institutional rail workers/partners and under what relationship;
- how tickets/permissions work, if used at all;
- which yards and stations are major landmarks;
- how much service state advances while players are offline;
- how the Minecraft adapter represents trains without becoming rules authority.

Until those decisions exist, all examples remain proposals.
