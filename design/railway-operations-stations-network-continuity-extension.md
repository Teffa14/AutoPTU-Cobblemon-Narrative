# Ouros Railway Operations, Stations & Network Continuity Extension

Status: proposed systems design extension. Not established Ouros canon.

Parent systems:
- `design/travel-transport-expedition-layer.md`
- `design/transit-hubs-passenger-cohorts-extension.md`
- `design/technology-energy-infrastructure-layer.md`
- `design/facility-maintenance-repair-inspection-extension.md`
- `design/infrastructure-outage-restoration-extension.md`
- `design/public-notices-signage-world-information-extension.md`
- `design/interregional-mobility-recognition-layer.md`
- `design/workplaces-professions-staffing-layer.md`
- `design/pokemon-work-role-participation-extension.md`
- `design/cobblemon-runtime-authority-boundary.md`

## Purpose

Travel already supports rail/transit as a possible connection type if canon later establishes it. Transit Hubs already supports passengers and onboard social scenes. This extension adds the missing rail-specific continuity layer: persistent track topology, station/line operational state, planned service patterns, junction history, partial operation, control indications, decommissioned alignments and network revisions.

The goal is to make a railway behave like an institution and piece of geography that can accumulate history rather than a teleport menu.

This file establishes no railway in Ouros.

## Authority boundary

Travel owns:
- physical inter-location connections at the general route level;
- journeys;
- transport service identity;
- route viability consumed by travel planning.

Transit Hubs owns:
- passenger cohorts;
- recurring journey contacts;
- in-transit social scenes;
- aggregate passenger pressure.

Technology owns:
- traction/power systems;
- signalling/control technical assets;
- monitoring equipment;
- technical faults;
- operator interfaces.

Maintenance owns:
- asset condition;
- inspections;
- work orders;
- repairs;
- technical verification.

Infrastructure Outage owns:
- cross-service cascades;
- backup continuity;
- staged restoration across networks.

Public Notices owns:
- platform boards;
- closures;
- revised timetables;
- passenger-facing physical information.

Workplaces owns human staffing. Pokémon Work owns individual Pokémon assignments. Conservation owns ecological interpretation. Crisis owns derailment/emergency response. Material Culture/Courier own cargo and item provenance.

This extension owns the rail-specific operational topology and its revision history.

## Rail network

```yaml
rail_network:
  rail_network_id: null
  display_name_ref: null
  operator_refs: []
  corridor_ids: []
  station_ids: []
  junction_ids: []
  depot_or_yard_ids: []
  service_pattern_ids: []
  technology_network_refs: []
  travel_connection_refs: []
  current_revision_id: null
  historical_revision_ids: []
  status: proposed
```

A network is a coordination object. It does not imply ownership, a monopoly, a public authority or a particular technology.

## Rail corridor and sections

```yaml
rail_corridor:
  corridor_id: null
  endpoint_station_ids: []
  section_ids: []
  travel_connection_refs: []
  current_operating_band: unknown
  active_restriction_ids: []
  current_service_pattern_ids: []
  decommissioned_section_ids: []
  ecology_link_ids: []
  last_revision_event_id: null
```

```yaml
rail_section:
  section_id: null
  corridor_id: null
  endpoint_refs: []
  physical_state: unknown
  operational_access_state: unknown
  technical_asset_refs: []
  maintenance_refs: []
  active_restriction_refs: []
  direct_observation_refs: []
  control_indication_refs: []
  last_verified_at: null
```

Suggested physical states:
- OPEN_GEOMETRY
- DEGRADED
- BLOCKED
- DAMAGED
- UNDER_WORKS
- DECOMMISSIONED
- REMOVED
- UNKNOWN

The descriptive state does not create tactical terrain.

## Physical state, control state and service state remain separate

A section can be physically unobstructed while service is suspended because:
- power is unavailable;
- signalling/control is unavailable;
- rolling stock is unavailable;
- staffing is unavailable;
- a downstream section is blocked;
- inspection/testing is pending;
- a station needed for the service remains closed.

A train-control display can indicate occupancy or protection while direct inspection later finds a different physical situation.

Never collapse these into `rail_open=true`.

## Junction / switch state

```yaml
rail_junction:
  junction_id: null
  connected_section_ids: []
  current_alignment_ref: null
  permitted_alignment_refs: []
  indication_refs: []
  command_history_refs: []
  maintenance_refs: []
  lockout_ref: null
  last_directly_verified_at: null
```

The extension stores authored persistent alignment only when it matters to world state. It does not simulate every switch continuously.

A Minecraft lever or redstone state can present an alignment, but the persistent semantic state remains server-owned.

## Station state

```yaml
rail_station:
  station_id: null
  location_id: null
  network_refs: []
  corridor_refs: []
  platform_or_boarding_area_refs: []
  entrance_refs: []
  accessibility_route_refs: []
  staff_workspace_refs: []
  service_node_refs: []
  public_information_surface_refs: []
  active_service_pattern_ids: []
  operating_band: unknown
  maintenance_refs: []
  historical_use_refs: []
  current_revision_id: null
```

Station shops, queues, found property, credentials and announcements belong to their existing systems even when physically located inside the station.

Suggested station operating bands:
- FULL_SERVICE
- LIMITED_SERVICE
- BYPASS_ONLY
- TERMINATING_ONLY
- BOARDING_CLOSED
- BUILDING_OPEN_NO_TRAINS
- UNDER_WORKS
- DECOMMISSIONED
- REPURPOSED
- UNKNOWN

This allows “station reopened” and “line reopened” to be separate events.

## Service pattern

```yaml
rail_service_pattern:
  service_pattern_id: null
  transport_service_ref: null
  network_revision_ref: null
  ordered_stop_refs: []
  corridor_section_refs: []
  turnback_refs: []
  operating_window_refs: []
  active_restriction_refs: []
  public_timetable_projection_refs: []
  current_state: proposed
```

Possible service states:
- NORMAL
- SHORT_TURN
- SHUTTLE
- STATION_BYPASS
- SINGLE_CORRIDOR_LIMITED
- TEST_RUNS
- RESTORING
- SUSPENDED

These are narrative/operational states. This layer does not invent frequency, speed or capacity math.

## Train run

A particular journey can reference a rail run without turning the layer into a real-time dispatch simulator.

```yaml
train_run:
  run_id: null
  service_pattern_id: null
  journey_ref: null
  consist_or_vehicle_asset_refs: []
  crew_assignment_refs: []
  planned_stop_refs: []
  actual_stop_event_refs: []
  departure_event_ref: null
  current_operational_state: planned
  active_disruption_refs: []
  arrival_event_ref: null
```

Use only when an exact run matters. Routine service can remain aggregate.

## Rolling stock boundary

Rolling stock can be a persistent technical/material asset when exact identity matters:
- a named heritage vehicle;
- a recurring train used by a known crew;
- a unit under repair;
- a vehicle involved in a case or incident;
- a mobile service with recurring interior spaces.

Its condition belongs to Maintenance/Technology. Its item provenance belongs to Material Culture where relevant. This extension only references it in service operation.

Do not instantiate every carriage in the database solely for realism.

## Operational indication

```yaml
rail_operational_indication:
  indication_id: null
  source_asset_or_actor_ref: null
  observed_at: null
  indication_kind: null
  indicated_section_ref: null
  indicated_state: null
  observer_refs: []
  confidence_band: unknown
  later_reconciliation_refs: []
```

Candidate indications:
- SIGNAL_ASPECT
- CONTROL_BOARD_OCCUPANCY
- PLATFORM_DISPLAY
- STAFF_RADIO_REPORT
- TRAIN_POSITION_REPORT
- SENSOR_ALERT
- MANUAL_BLOCK_NOTICE

An indication is evidence. It is not world truth by itself.

## Operational reconciliation

```yaml
rail_reconciliation:
  reconciliation_id: null
  subject_section_or_run_ref: null
  indication_refs: []
  direct_observation_refs: []
  maintenance_log_refs: []
  staff_claim_refs: []
  confirmed_fact_refs: []
  unresolved_conflicts: []
  completed_at: null
```

This supports mysteries where apparent “ghost trains,” wrong-platform reports or contradictory staff accounts resolve into stale data, duplicated run IDs, clock drift, a manual override, incomplete records or genuinely unresolved evidence.

No paranormal answer is required or excluded automatically.

## Restrictions and partial operation

```yaml
rail_operating_restriction:
  restriction_id: null
  affected_section_or_station_refs: []
  cause_refs: []
  effective_from: null
  expected_review_at: null
  allowed_operation_refs: []
  prohibited_operation_refs: []
  alternate_service_refs: []
  public_notice_refs: []
  release_condition_refs: []
  current_state: active
```

Useful narrative forms:
- one section closed while both ends remain served;
- trains terminate early and turn back;
- one station is bypassed;
- passenger service stops while maintenance/test movements continue;
- a replacement surface service uses an already valid Travel connection;
- a freight or institutional movement remains possible while public service is suspended, if canon explicitly supports that distinction.

No replacement mode appears merely for convenience; Travel must contain a viable connection/service.

## Network revision history

```yaml
rail_network_revision:
  revision_id: null
  rail_network_id: null
  effective_at: null
  added_section_ids: []
  removed_or_decommissioned_section_ids: []
  added_station_ids: []
  bypassed_station_ids: []
  changed_junction_refs: []
  new_service_pattern_ids: []
  superseded_pattern_ids: []
  project_or_event_refs: []
  public_map_refs: []
```

Old maps and memories remain historically valid for their dates. A later branch extension never rewrites what a passenger knew before it existed.

## Commissioning / reopening chain

A rebuilt section should normally pass through explicit handoffs:

```text
public/project decision
-> procurement/work authorization
-> physical repair/construction
-> technical inspection
-> controlled test state
-> station readiness review
-> service commissioning decision
-> public information update
-> ordinary operation
```

Not every step needs a playable scene. The chain prevents “funding complete” from becoming “train running” in one silent mutation.

## Decommissioned and repurposed rail

A decommissioned alignment may become:
- maintenance access;
- walking/cycling route if canon permits;
- public space;
- industrial heritage;
- archive/museum asset;
- workshop/storage;
- wildlife corridor or habitat;
- abandoned infrastructure under survey;
- candidate for future reopening.

Those outcomes are owned by the appropriate parent systems. Rail continuity preserves the old transport identity and its relationship to the present use.

Reopening later must inspect current ecology, occupancy, maintenance and public-space state. The system cannot erase years of new use because a historical map says “railway.”

## Working Pokémon

Railway operations may reference an individual Pokémon work assignment when canon establishes one.

Requirements:
- exact Pokémon identity;
- exact task;
- capability/Move/Ability evidence where mechanically relevant;
- supervision/role state;
- work availability;
- welfare/agency boundaries;
- handoff if the individual is unavailable.

Never use `Electric type = traction power`, `large Pokémon = shunting`, or similar species-level inference.

A Pokémon entity present on a platform is not working unless Ouros work state says so.

## Passenger information

Passenger-facing state is projected through Public Notices:
- platform change;
- station bypass;
- short-turn destination;
- closure;
- delayed opening;
- test operation;
- replacement route;
- corrected timetable.

A stale board can create actor misinformation without changing the actual service pattern.

## Route ecology

Rail ecology can include observed relationships such as:
- old cuttings used as travel corridors by wild Pokémon;
- embankments used for nesting or shelter;
- noise/light changing observed activity;
- station food waste changing scavenger presence;
- maintenance vegetation clearance altering access;
- a closed line becoming habitat during prolonged disuse.

Conservation/Science owns causal interpretation. This extension records where rail operation and ecological state intersect.

Wild Pokémon near tracks do not become tactical participants automatically.

## Minecraft / Cobblemon reuse

Prefer reuse of Minecraft/Cobblemon presentation wherever technically appropriate:
- rails, minecart-like visual language or custom vehicle assets when reviewed;
- stations, platforms, doors, barriers, lamps and signs;
- redstone-like visual controls when they faithfully mirror semantic state;
- NPC/Pokémon entities, models, forms, poses, animations and cries;
- sounds/particles;
- UI/network synchronization;
- timetable boards and service notices;
- persistent structures and changed world geometry.

Potential adapter-required surfaces:
- starting/ending a semantic train run;
- station arrival/departure events;
- authoritative switch/control interaction;
- network revision projection;
- working-Pokémon assignment presentation;
- battle transition and semantic playback.

Minecraft minecart physics, redstone, entity proximity or Cobblemon BattleState never decide:
- whether the rail service is canonically operating;
- which route a persistent service uses;
- who is a combatant;
- train collision damage;
- tactical movement;
- HP/status/results.

Required combat direction remains:
`Ouros rail/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

## Encounter contract — Trackside Withdrawal

Status: proposed encounter pattern.

Narrative premise:
A rail work or inspection team must withdraw from a bounded corridor after an unexpected Pokémon conflict or other encounter blocks the safe access route.

Full intended version:
- multiple withdrawal routes;
- protected noncombatants;
- narrow trackside geometry;
- Intercept/forced movement when legally supported;
- active exclusion/hazard zones only if PTU/Caelo and runtime support them;
- objective-aware AI capable of territorial defense, withdrawal or route denial;
- exact semantic playback.

Permanent capability dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
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

Reduced version:
The operator fully isolates the rail section before battle. Workers withdraw in overworld state and never become tactical tokens. No train moves through the arena. Ouros selects the exact combatants and AutoPTU resolves a static encounter beside an inert line. Reopening/inspection happens afterward.

## Encounter contract — Station Concourse Evacuation

Narrative premise:
A station is cleared after an encounter develops in or near the passenger circulation area.

Full intended version:
- civilians moving toward multiple exits;
- access gates changing route options;
- PROTECT/CLEAR_ROUTE/WITHDRAW objectives;
- possible Intercept and reaction windows;
- objective-aware AI;
- synchronized station-state playback.

Dependencies use the same readiness profile as Trackside Withdrawal, with terrain/zones/reactions, tactical AI and adapter support remaining major blockers.

Reduced version:
Transit Hubs evacuates all passengers before tactical resolution. Shops, ticketing, luggage and important assets remain outside targeting. The battle runs in a reviewed static concourse/perimeter. Passenger service remains suspended until the owning systems perform reopening review.

## Encounter contract — Decommissioned Cutting Wildlife Conflict

Narrative premise:
A disused alignment now functions as a wildlife route. A survey or proposed reopening causes a temporary conflict at the same physical site.

Full intended version:
- route-control or withdrawal objective;
- territorial/escape AI;
- possible constrained geometry;
- environment effects only when authoritative mechanics exist;
- exact distinction between observed background Pokémon and tactical participants.

Reduced version:
Surveyors leave first. Conservation state keeps the wildlife-use claim separate from battle. Ouros instantiates only the reviewed opposing subgroup on static terrain. Victory cannot approve reopening or disprove ecological use of the corridor.

## Noncombat pattern — Control Log Reconciliation

Inputs:
- control-board indications;
- station/departure records;
- direct platform observations;
- staff claims;
- maintenance logs;
- clocks/timestamps;
- network revision history.

Possible result:
- duplicated run identity;
- stale indication;
- display clock mismatch;
- manual override;
- a train terminating before the observed section;
- physical evidence inconsistent with control data;
- unresolved conflict.

No battle dependency is required.

## Generation guardrails

1. Do not invent a railway merely because a route needs faster travel.
2. Do not generate a dramatic incident on every trip.
3. Do not equate signal/control indication with physical truth.
4. Do not infer sabotage from an operational anomaly.
5. Do not invent speeds, capacities, fares, headways or safety margins.
6. Do not turn a station into customs or immigration control without separate canon.
7. Do not model every switch, carriage or passenger persistently.
8. Do not convert moving trains, electrified track or platform edges into tactical hazards without verified mechanics.
9. Do not allow Minecraft/Cobblemon physics to decide canonical service or combat results.
10. Preserve decommissioned alignments and old service patterns as historical state.
11. A reopening must account for intervening habitat, public-space and occupancy state.
12. Working Pokémon need individual task evidence, never species inference.

## Canon boundary

This extension establishes reusable data and encounter grammar only. It establishes no Ouros rail network, technology, operator, station, pass, fare, timetable, gauge, electrification system, ownership model, worker practice or historic line.