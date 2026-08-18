# Ouros Travel, Transport & Expedition Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models locations, settlements, factions, supply routes, cases, clocks, dungeons, mobile actors and world-state consequences. This layer defines how characters move between those states without turning every journey into either a loading screen or a mandatory random battle.

The core principle is selective significance: routine movement compresses, while travel expands when geography, information, relationships, risk, logistics or changing world state creates a meaningful decision.

## 1. Connection graph

The world should model travel as explicit connections between locations.

```yaml
travel_connection:
  connection_id: null
  endpoint_a: null
  endpoint_b: null
  connection_type: null
  physical_state: OPEN
  supported_mode_refs: []
  environment_tags: []
  route_segment_ids: []
  infrastructure_ids: []
  transport_service_ids: []
  access_policy_ids: []
  active_hazard_ids: []
  active_clock_ids: []
  faction_presence_ids: []
  ecology_state_ids: []
  alternate_connection_ids: []
  world_truth_refs: []
```

Candidate connection types:
- ROAD
- TRAIL
- WATERWAY
- SEA_LANE
- RAIL_OR_TRANSIT if canon supports it
- AIR_ROUTE if canon supports it
- CAVE_PASSAGE
- DUNGEON_LINK
- URBAN_TRANSIT
- TEMPORARY_ROUTE
- SERVICE_ONLY_CONNECTION

The type is descriptive. Exact movement mechanics remain external.

## 2. Physical route state and service state are separate

A road can be physically open while the bus/ferry/carrier serving it is unavailable.
A harbor service can run while one coastal trail is closed.

```yaml
route_state:
  connection_id: null
  physical_state: OPEN
  state_reasons: []
  last_changed_event_id: null
  traversal_conditions: []
  known_bypass_ids: []
```

Suggested physical states:
- OPEN
- DEGRADED
- RESTRICTED
- BLOCKED
- DESTROYED
- SEASONAL_CLOSED
- UNKNOWN

Do not conflate `player cannot use current service` with `there is no physical route`.

## 3. Actor route knowledge

The actor's map can be wrong or stale without changing world truth.

```yaml
route_knowledge:
  holder_id: null
  connection_id: null
  known_state: null
  last_confirmed_event_id: null
  freshness_band: null
  source_ids: []
  known_landmark_ids: []
  known_hazard_ids: []
  known_rest_site_ids: []
  known_bypass_ids: []
  confidence: null
```

Potential sources:
- direct travel;
- local guide;
- public map;
- transport operator;
- field report;
- faction intel;
- rumor;
- previous expedition;
- infrastructure notice.

The UI should distinguish confirmed recent information from rumor where practical.

## 4. Travel mode

A route may support several ways to cross it.

```yaml
travel_mode:
  mode_id: null
  mode_type: null
  provider_type: null
  governing_refs: []
  world_requirements: []
  participant_requirements: []
  asset_requirements: []
  current_implementation_state: unknown
```

Candidate orchestration types:
- ON_FOOT
- OWNED_POKEMON_ASSISTED
- PUBLIC_POKEMON_SERVICE
- PUBLIC_TRANSPORT
- CHARTER
- CONVOY
- EXPEDITION_VEHICLE
- TEMPORARY_ASSISTANCE

No mode should be executable until the relevant PTU/Caelo and Minecraft/AutoPTU requirements are validated.

## 5. Public transport service

Transport is a world actor/service rather than universal fast travel.

```yaml
transport_service:
  service_id: null
  operator_ids: []
  institution_id: null
  home_base_ids: []
  stop_ids: []
  connection_ids: []
  staff_ids: []
  pokemon_asset_ids: []
  vehicle_asset_ids: []
  service_state: OPERATING
  dependency_ids: []
  current_disruption_ids: []
  passenger_policy_ids: []
  cargo_policy_ids: []
  public_information_ids: []
  last_service_event_id: null
```

Suggested service states:
- OPERATING
- LIMITED
- DELAYED
- REROUTED
- SUSPENDED
- EMERGENCY_ONLY
- CLOSED
- RESTORING

Service state must have a causal reason.

## 6. Access without ownership

A player may gain mobility because a service, institution or community grants access to capable assets.

This supports:
- public transport;
- ride programs;
- rescue deployment;
- research expeditions;
- institutional field teams;
- temporary guides;
- chartered services.

The narrative engine should never require owning a specific species when the world already provides a plausible public route.

Likewise, a public service should not override a genuine authored wilderness access challenge when the service does not operate there.

## 7. Owned Pokémon traversal boundary

When a player wants to use a Pokémon partner for travel, the narrative layer asks the authoritative system whether the exact individual has the required legal state.

Validation can include:
- movement capability;
- Mountable or equivalent governing capability where applicable;
- environment compatibility;
- current injury/status/state where implementation tracks it;
- party ownership/availability;
- route-specific constraints;
- current bridge/mod support.

Do not infer `large bird = can carry Trainer` or `Water type = can cross ocean`.

## 8. Journey object

A trip can persist when it is important enough to deserve state.

```yaml
journey:
  journey_id: null
  participant_ids: []
  origin_id: null
  destination_id: null
  purpose_ids: []
  planned_segment_ids: []
  current_segment_id: null
  selected_modes: []
  departure_event_id: null
  current_state: PLANNED
  cargo_ids: []
  commitment_ids: []
  clock_ids: []
  incident_ids: []
  discoveries: []
  reroute_history: []
  arrival_event_id: null
```

Suggested journey states:
- PLANNED
- PREPARING
- DEPARTED
- IN_TRANSIT
- PAUSED
- REROUTING
- STRANDED
- RETURNING
- ARRIVED
- ABANDONED

Do not instantiate a persistent journey for every five-minute walk through town.

## 9. Journey significance test

Before expanding transit into gameplay, evaluate whether it currently contains meaningful state.

```yaml
journey_significance:
  route_changed: false
  navigation_uncertain: false
  active_clock_intersection: false
  active_case_intersection: false
  faction_intersection: false
  ecological_anomaly: false
  transport_disruption: false
  relationship_callback: false
  player_exploration_intent: false
  resource_or_cargo_choice: false
  unique_discovery_possible: false
  score: 0
```

If significance remains low, compress the trip.

This is a pacing heuristic, not a game mechanic.

## 10. Travel compression

A routine trip can produce a concise state transition:

```text
verified route
+ functioning service or legal traversal
+ no meaningful intersecting state
-> update time/location
-> emit arrival event
```

Compression may still surface one short summary of:
- weather;
- visible route condition;
- ordinary traffic;
- known settlement changes;
- time elapsed.

Do not generate filler conversations or battles solely to justify travel time.

## 11. When travel becomes a scene

Expand when players need to decide something.

Possible scene triggers:
- route fork;
- uncertain landmark;
- bridge/ferry/service failure;
- severe weather change;
- injured traveler/Pokémon;
- ecological anomaly;
- pursuit intersection;
- faction action;
- cargo problem;
- social disagreement with consequence;
- optional discovery;
- player chooses to leave known route;
- clock requires prioritization.

Travel is then composed from existing Mission Grammar action blocks rather than a separate mini-game.

## 12. Route incident object

```yaml
travel_incident:
  incident_id: null
  journey_id: null
  connection_id: null
  source_state_ids: []
  incident_type: null
  visible_evidence_ids: []
  actor_ids: []
  immediate_options: []
  optional: false
  resolution_event_ids: []
  persistent_outputs: []
  mechanics_review_required: false
```

Candidate types:
- WEATHER_DELAY
- INFRASTRUCTURE_FAILURE
- SERVICE_DISRUPTION
- NAVIGATION_UNCERTAINTY
- WILDLIFE_EVENT
- RESCUE_OPPORTUNITY
- FACTION_INTERSECTION
- CASE_INTERSECTION
- CARGO_PROBLEM
- SOCIAL_SCENE
- DISCOVERY
- PUBLIC_EVENT_TRAFFIC
- ROUTE_CLOSURE

Selection must come from current state or authored randomness appropriate to the route.

## 13. Incident budget

Do not force a dramatic encounter every leg.

A route may explicitly support:
- no incident;
- one meaningful incident;
- several incidents during a high-stakes expedition.

Repeated routine routes should become more compressible as players learn them, unless state actually changes.

## 14. Navigation decision model

Navigation should create choices when uncertainty exists, not constant dice rolling.

```yaml
navigation_problem:
  connection_id: null
  known_destination_direction: null
  landmark_ids: []
  map_or_report_ids: []
  visibility_state: null
  route_options: []
  wrong_route_outputs: []
  recovery_options: []
  rules_validation_required: true
```

Possible resolutions may involve valid PTU Skills, capabilities, maps, local knowledge, guides or physical landmarks.

Exact checks and DCs are not defined here.

## 15. Rest and staging sites

Routes can contain persistent intermediate nodes.

```yaml
staging_site:
  site_id: null
  connection_ids: []
  shelter_state: null
  service_ids: []
  water_or_supply_refs: []
  communications_state: null
  caretaker_ids: []
  hazard_ids: []
  public_access_state: null
  last_maintenance_event_id: null
```

Possible forms:
- roadside shelter;
- harbor;
- field station;
- expedition camp;
- caravan stop;
- ranger/rescue post;
- mountain hut;
- temporary event checkpoint.

Availability must be authored from world state. This layer does not create camping/rest mechanics.

## 16. Expedition object

An expedition is a journey with planned field objectives and stronger logistics state.

```yaml
expedition:
  expedition_id: null
  sponsor_ids: []
  participant_ids: []
  objective_ids: []
  destination_ids: []
  route_plan_ids: []
  staging_site_ids: []
  role_assignments: []
  cargo_ids: []
  transport_service_ids: []
  communications_plan_ids: []
  extraction_plan_ids: []
  contingency_ids: []
  active_clock_ids: []
  current_state: PLANNING
```

Suggested states:
- PLANNING
- ASSEMBLING
- DEPLOYED
- FIELDWORK
- RETURNING
- COMPLETE
- ABORTED
- OVERDUE

## 17. Expedition roles

Roles organize responsibility, not progression.

Possible roles:
- NAVIGATION
- SCOUTING
- LOGISTICS
- MEDICAL_SUPPORT
- POKEMON_CARE
- RESEARCH
- LIAISON
- TECHNICAL_SUPPORT
- SECURITY
- COMMUNICATIONS
- LOCAL_GUIDE

A participant may hold several roles.

No role grants PTU modifiers by itself.

## 18. Expedition preparation

The existing `Expedition Loadout as Story Choice` seed remains valid. This layer formalizes the state behind it.

```yaml
expedition_preparation:
  expedition_id: null
  known_conditions: []
  uncertain_conditions: []
  selected_assets: []
  selected_services: []
  selected_information_sources: []
  omitted_options: []
  dependency_checks: []
  preparation_complete: false
```

Preparation should change options, not create arbitrary gotcha failures.

## 19. Extraction and return planning

Remote missions should consider how people get back.

```yaml
extraction_plan:
  expedition_id: null
  primary_route_id: null
  alternate_route_ids: []
  service_ids: []
  rendezvous_location_ids: []
  communication_dependencies: []
  trigger_conditions: []
  current_viability: unknown
```

A failed extraction plan may create a return journey, rescue request or temporary base scenario.

It should not automatically kill or strand characters off-screen.

## 20. Mobile base

A mobile base is both transport and persistent location.

```yaml
mobile_base:
  mobile_base_id: null
  asset_type: null
  current_location_id: null
  operator_ids: []
  crew_ids: []
  service_ids: []
  cargo_capacity_state: null
  maintenance_state_id: null
  upgrade_event_ids: []
  route_constraints: []
  dock_or_land_requirements: []
  communication_state: null
  active_journey_id: null
```

Candidate forms are canon-dependent. The schema does not imply Ouros has airships, trains or advanced vehicles.

## 21. Crew state

Named crew should remain characters rather than equipment slots.

```yaml
crew_assignment:
  actor_id: null
  mobile_base_id: null
  operational_roles: []
  current_availability: null
  personal_goal_ids: []
  relationship_ids: []
  current_constraints: []
```

A service can become limited if the relevant person or Pokémon is unavailable, consistent with the Settlement and Material Culture layers.

## 22. Transport disruption

```yaml
transport_disruption:
  disruption_id: null
  service_id: null
  affected_connection_ids: []
  cause_state_ids: []
  visible_evidence_ids: []
  severity: null
  alternate_service_ids: []
  alternate_route_ids: []
  repair_or_resolution_paths: []
  expected_review_event_id: null
```

Useful causes:
- weather;
- mechanical/infrastructure damage;
- ecological pressure;
- staff/Pokémon unavailability;
- supply interruption;
- faction action;
- event congestion;
- scheduled seasonal closure.

Disruption should create choices, not arbitrary dead time.

## 23. Route restoration

Opening a connection can change several systems simultaneously.

Potential outputs:
- settlement accessibility;
- supply-route state;
- transport-service reach;
- visitor traffic;
- faction influence;
- emergency response times;
- ecological disturbance;
- public-event feasibility;
- new job access;
- migration pressure;
- public memory.

This extends existing bridge/road seeds without duplicating Settlement or Economy ownership of those effects.

## 24. Route ecology

Travel infrastructure and Pokémon ecology interact both ways.

Possible route/ecology relationships:
- migration corridor crosses road;
- ferry noise affects coastal behavior;
- night lighting alters local activity;
- abandoned road becomes habitat;
- traffic increases scavenger presence;
- seasonal nesting causes temporary closure;
- a disturbed population makes one service unsafe.

The Observation layer owns ecological claims. Travel consumes validated state.

## 25. Route social life

Transport spaces can generate recurring relationships:
- crew;
- conductors/operators;
- guides;
- regular passengers;
- merchants;
- traveling performers;
- researchers;
- couriers;
- seasonal workers.

A route can therefore become a social location with its own recurring cast.

Do not create filler NPC interactions on every trip; callbacks should be relevant and bounded.

## 26. Cargo and convoy integration

The Material Culture layer owns item provenance and supply routes. Travel adds the operational journey state.

```yaml
convoy:
  convoy_id: null
  journey_id: null
  carrier_ids: []
  cargo_instance_ids: []
  cargo_batch_ids: []
  escort_ids: []
  origin_id: null
  destination_id: null
  service_or_faction_ids: []
  current_state: null
```

Exact carrying capacity, vehicle inventory and transport costs remain mechanics/economy decisions.

## 27. Pursuit integration

The Case layer already owns target pursuit state.

Travel contributes:
- reachable connection graph;
- service schedules/availability;
- route knowledge;
- travel time bands if authored;
- closures and alternatives.

A target cannot teleport between locations merely because the plot needs them elsewhere.

## 28. Fast travel policy

Fast travel is a presentation choice over validated connectivity.

Recommended rule:
A destination becomes compressible when the player knows a viable connection and current state supports the selected travel mode.

Fast travel should be blocked or modified when:
- route changed significantly;
- selected service is unavailable;
- an active high-priority state requires a decision;
- player deliberately chooses exploration;
- destination access policy changed;
- current party cannot legally execute the selected personal traversal mode.

Do not disable fast travel merely to inflate playtime.

## 29. Multiplayer travel

Players traveling together may have different purposes and knowledge.

Potential structure:
- common journey state;
- player-specific objectives;
- private route knowledge where appropriate;
- shared cargo/service dependencies;
- explicit split/leave/rejoin events;
- individual arrival when party members take different connections.

A multiplayer server should not force everyone online to wait through another player's long transit scene.

## 30. Offline/world pulse behavior

Transport services and routes may change through World Pulse, but changes need bounded causality.

Safe candidates:
- scheduled service state transitions;
- repair completion backed by a prior project;
- seasonal closure/opening;
- faction-supported reroute;
- public-event service increase;
- documented weather/event disruption.

Do not simulate arbitrary accidents off-screen solely for novelty.

## 31. Minecraft / Cobblemon representation

Potential world-facing objects:
- terminals/stops;
- signs and route boards;
- docks;
- gates;
- bridges and trailheads;
- staging camps;
- service NPCs/Pokémon;
- mobile-base interiors;
- cargo staging areas;
- route closure barriers;
- repair crews;
- updated maps/notices;
- alternate trail markers;
- rendezvous points.

The overworld should show why a route or service changed where feasible.

## 32. AutoPTU boundary

AutoPTU tactical movement must not be treated as overworld transport authority automatically.

Before execution, validate relevant rules and implementation for:
- Overland/Swim/Sky/Burrow/Levitate or other movement values;
- Naturewalk;
- Mountable or equivalent capabilities;
- Trainer/Pokémon movement interaction;
- weight/carrying constraints if applicable;
- environmental effects;
- movement-affecting status;
- Features/Edges relevant to wilderness travel;
- item/tool requirements;
- any Caelo-specific travel rules;
- Cobblemon entity/riding support;
- server-side ownership and capability state.

This document defines orchestration only.

## 33. Generation guardrails

1. Do not generate a travel battle merely because time passes.
2. Routine known transit should become faster with familiarity and infrastructure.
3. A route incident needs a causal source or authored encounter policy.
4. Route knowledge and route truth remain separate.
5. Public services prevent traversal from becoming ownership-gated by default.
6. Personal Pokémon travel requires exact individual capability validation.
7. Transport failure should offer understandable alternatives where plausible.
8. Distance matters only when it changes an actual decision or consequence.
9. Opening a route can create costs as well as benefits, but progress should not be punished automatically.
10. Mobile-base crew remain characters with goals and availability.
11. Expedition preparation should reward foresight without using hidden gotchas.
12. Avoid universal survival meters unless a dedicated authored scenario requires them.
13. Do not invent ticket prices, schedules, speeds or capacities.
14. A route may be peaceful; peace does not require filler content.

## 34. Implementation priority

Recommended order:
1. connection graph and route state;
2. actor route knowledge;
3. transport service state;
4. travel-mode authority interface;
5. journey significance/compression;
6. route incident selection;
7. expedition object and roles;
8. disruption/reroute state;
9. extraction plan;
10. mobile base support;
11. multiplayer journey views;
12. World Pulse route/service integration.

## Open implementation questions

- Which PTU/Caelo movement and Mountable rules will govern overworld traversal in Ouros?
- Which Caelo boat/Surf/Fly travel conventions, if any, carry forward?
- Does Cobblemon currently expose rideable state for every Pokémon Ouros would need, or must the bridge provide custom mounts?
- Should public transport use real schedules, event-phase schedules, or simple availability states?
- How does server time advance during compressed journeys?
- Which route changes must physically alter Minecraft blocks versus metadata only?
- How should a journey crossing unloaded chunks be validated?
- What constitutes enough route familiarity to allow compression/fast travel?
- How should personal Pokémon injury/status affect overworld mobility without duplicating battle-state logic?
- Can AutoPTU query a Pokémon's authoritative movement/capability state outside combat?
- How should transport NPCs and persistent transport Pokémon be represented across chunk unload/reload?
- Which mobile-base technologies, if any, belong in Ouros canon?