# Ouros Road Passenger Transport Services Continuity Extension

Status: PROPOSED systems architecture. Not established Ouros canon.

Parent systems:
- `design/travel-transport-expedition-layer.md`
- `design/roads-bridges-detours-operational-continuity-extension.md`
- `design/transit-hubs-passenger-cohorts-extension.md`
- `design/interregional-mobility-recognition-layer.md`
- `design/public-notices-signage-operational-information-extension.md`
- `design/commercial-services-access-queues-bookings-continuity-extension.md`

## Purpose

This extension specializes the operational state of road passenger services: taxis, buses, shuttles, hired rides and canon-approved Pokémon-assisted public transport.

Travel remains authoritative for journeys and route viability. Roads remains authoritative for physical road/crossing access. Transit Hubs owns passenger cohorts and expanded co-presence scenes. Finance owns payment/obligation state. This layer owns service pattern, stop identity, dispatch/run state, pickup/dropoff and road-service history.

## Core separations

Keep these facts independent:
- road open;
- service operating;
- stop active;
- run scheduled;
- vehicle/transport asset available;
- operator/assigned Pokémon available;
- passenger accepted;
- passenger boarded;
- run departed;
- stop served;
- passenger alighted;
- journey arrived.

A single visible vehicle or Pokémon proves none of the later states.

## Road passenger service

```yaml
road_passenger_service:
  service_id: null
  operator_id: null
  service_type: TAXI | FIXED_ROUTE | SHUTTLE | LOCAL_CARRIER | CHARTER | POKEMON_ASSISTED_PUBLIC_SERVICE | OTHER
  home_location_ids: []
  road_connection_ids: []
  stop_ids: []
  service_pattern_id: null
  staff_actor_ids: []
  pokemon_asset_ids: []
  vehicle_asset_ids: []
  service_state: OPERATING
  dependency_ids: []
  active_disruption_ids: []
  public_information_refs: []
  history_event_ids: []
```

Service types are descriptive, not mechanics.

## Stop identity

```yaml
road_service_stop:
  stop_id: null
  location_id: null
  service_ids: []
  access_state: ACTIVE
  pickup_allowed: true
  dropoff_allowed: true
  shelter_asset_id: null
  sign_or_board_refs: []
  road_segment_refs: []
  accessibility_refs: []
  temporary_relocation_ref: null
  history_event_ids: []
```

Possible access states: ACTIVE, LIMITED, RELOCATED, SKIPPED_TEMPORARILY, CLOSED, UNKNOWN.

A stop can move temporarily while the service continues. The old stop remains historical state instead of vanishing.

## Service pattern

```yaml
road_service_pattern:
  pattern_id: null
  service_id: null
  pattern_type: POINT_TO_POINT | ORDERED_STOPS | LOOP | REQUEST_BASED | LIMITED_ROUTE
  ordered_stop_ids: []
  allowed_destination_ids: []
  directionality: null
  published_schedule_ref: null
  frequency_band: null
  active_window_ref: null
  version: 1
  effective_from: null
  supersedes_pattern_id: null
```

Do not derive travel time or capacity unless an authoritative system provides it.

## Individual run / dispatch

```yaml
road_service_run:
  run_id: null
  service_id: null
  pattern_id: null
  planned_start: null
  actual_start: null
  assigned_operator_ids: []
  assigned_pokemon_ids: []
  assigned_vehicle_ids: []
  state: PLANNED
  expected_stop_ids: []
  served_stop_events: []
  skipped_stop_ids: []
  passenger_cohort_ref: null
  disruption_refs: []
  actual_end: null
  provenance_refs: []
```

Suggested lifecycle:
PLANNED → READY → BOARDING → DEPARTED → IN_SERVICE → COMPLETED.

Alternate states: DELAYED, REROUTED, SHORT_TURNED, SUSPENDED, CANCELLED, ABORTED.

`VEHICLE_PRESENT != READY` and `READY != BOARDING`.

## Taxi / request-based dispatch

Point-to-point services need a dispatch record rather than pretending every trip is a fixed route.

```yaml
road_dispatch:
  dispatch_id: null
  service_id: null
  request_actor_id: null
  requested_pickup_id: null
  requested_destination_id: null
  accepted_at: null
  assigned_asset_refs: []
  state: REQUESTED | ACCEPTED | EN_ROUTE_TO_PICKUP | AT_PICKUP | BOARDED | IN_TRIP | DROPPED_OFF | CANCELLED
  journey_ref: null
  payment_or_agreement_ref: null
```

Finance owns fare/payment truth. A failed payment never authorizes Narrative to invent a battle.

## Passenger handoff

Boarding and alighting are world-state transitions.

```yaml
road_passenger_event:
  event_id: null
  run_or_dispatch_id: null
  actor_or_cohort_ref: null
  event_type: ACCEPTED | BOARDED | ALIGHTED | DENIED | MISSED | TRANSFERRED
  stop_or_location_id: null
  occurred_at: null
  source_refs: []
```

Transit Hubs decides whether a cohort deserves a playable social scene.

## Dependency-driven suspension

A service can suspend while roads remain open because of:
- staff unavailability;
- individual assigned-Pokémon unavailability;
- maintenance state;
- power/communications failure;
- wildlife/ecology restriction;
- weather decision;
- event congestion;
- accessibility failure;
- institutional decision;
- other explicitly sourced state.

The cause must point to the owning system. Road Passenger Operations records the operational consequence.

## Pokémon-operated public services

A Pokémon can participate only when the exact individual and assignment are explicit.

Required distinctions:
- species identity;
- individual Pokémon identity;
- governing movement/mount capability if mechanically relevant;
- work-role assignment;
- current availability;
- service asset relationship;
- passenger relationship.

No Type, body shape, animation or species precedent automatically grants passenger-carrying capability, work consent, legal qualification or ownership transfer.

## Service restoration

Restoration should expose stages:

cause addressed → operator reviews service → test/verification if required → limited service → normal pattern restored or revised.

A road reopening does not automatically restart a service. A Pokémon returning to a depot does not prove it is ready for work. A test trip does not prove public boarding has resumed.

## Information versus truth

Public notices may say a run is expected, delayed, rerouted or cancelled. Observed assets may support or contradict that information.

Store:
- publication time;
- effective window;
- service/pattern/run scope;
- supersession;
- observation provenance.

Do not make outdated signage overwrite authoritative service state.

## Long-term service memory

Useful persistent history includes:
- route extensions or contractions;
- recurring drivers/operators;
- retired or transferred Pokémon workers;
- temporary stops that became permanent;
- closed stops still used as landmarks;
- a service suspended by ecological change;
- a restored service using a revised pattern;
- recurring commuters or visitors promoted to persistent actors.

## Encounter contract — Stop Evacuation Withdrawal

Narrative premise: a road-service stop must be cleared while a bounded hostile or frightened subgroup threatens the immediate approach.

Full intended dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL, required for protective Intercept/withdrawal behavior;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for live traffic/work zones or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal/protection priorities;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced form: suspend the run first, remove passengers, staff, vehicles and nonparticipant Pokémon, then instantiate a static roadside arena. Battle can secure the immediate stop area; Road Passenger Operations separately decides whether service resumes.

## Encounter contract — Disabled Shuttle Perimeter

Narrative premise: a disabled service asset creates a roadside operational interruption while a separate combat threat prevents safe access.

Full version may require protected-route objectives, reactions, forced movement, traffic/work hazards, tactical AI and playback.

Reduced form: Maintenance isolates the asset and workers before battle. The vehicle/Pokémon service asset is not a target or combatant. AutoPTU receives a nearby static arena. Victory grants access to continue diagnosis; it does not repair or restart the service.

## Encounter contract — Rerouted Pickup Conflict

Narrative premise: a temporary pickup is moved because the normal stop is unavailable, and an unrelated territorial encounter threatens the alternate approach.

Full version may need reviewed terrain, withdrawal/route protection, reactions and tactical AI.

Reduced form: passengers wait outside the tactical area; Ouros explicitly selects combatants; the battle occurs on a cleared static section. A win does not prove the temporary stop is safe for public operation until Road/Road Passenger authorities review it.

## Minecraft/Cobblemon boundary

Safe presentation reuse:
- roads, curbs, stops, signs, shelters and barriers;
- vehicles or decorative assets where available;
- Pokémon models/forms/poses/animations/cries;
- operator/passenger NPCs;
- sounds, particles, UI, maps, networking, tracking and persistence hooks.

Adapter-required:
- stable service/stop/run identity;
- authoritative boarding/alighting intent;
- service-state projection into signs/barriers;
- entity-to-world-record binding;
- reviewed static arena conversion;
- semantic battle playback.

Forbidden authority:
- Minecraft pathfinding cannot decide a run completed;
- redstone cannot restart a service;
- vehicle/entity proximity cannot board a passenger automatically;
- Cobblemon nearby-entity or BattleState logic cannot select combatants;
- Minecraft collision cannot resolve PTU push/knockback/damage;
- a visible riding animation cannot prove PTU Mount legality.

## Canon boundary

This extension establishes no Ouros operator, road service, vehicle technology, fare system, stop, species labor role, driving law or public-transport institution. All concrete instantiations require canon review.