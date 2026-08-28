# Ouros Aviation, Airfields & Flight Operations Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Parent systems:
- `design/travel-transport-expedition-layer.md`
- `design/transit-hubs-passenger-cohorts-extension.md`
- `design/interregional-mobility-recognition-layer.md`
- `design/weather-forecast-preparedness-operational-extension.md`
- `design/technology-energy-infrastructure-layer.md`
- `design/material-culture-economy-crafting-layer.md`
- `design/workplaces-professions-staffing-layer.md`
- `design/pokemon-work-role-participation-extension.md`
- `design/cobblemon-runtime-authority-boundary.md`

Research provenance:
- `research/2026-08-28-aviation-airfields-flight-operations-scan-93.md`

## Purpose

Travel already permits `AIR_ROUTE` if canon supports it. Transit Hubs already owns temporary passenger co-presence. Interregional Mobility owns arrival context. Weather owns forecasts and observed conditions. This extension fills the operational continuity between them.

It models an airfield or landing site as a persistent location whose physical availability, service availability, exact movements, cargo handoffs, notices and historical reuse can change independently.

The schema does not establish that Ouros has airplanes, airships, airports, commercial aviation or any particular aviation technology.

## 1. Authority boundary

Aviation owns:
- airfield/landing-site operational identity;
- landing-area availability state;
- flight-service patterns when canonized;
- exact flight-operation records when narratively significant;
- ground-operation state relevant to departure/arrival;
- holds, diversions, cancellations and return-to-origin events as world facts;
- operational notices and verification history;
- airfield reuse history.

Travel owns:
- route connectivity;
- journeys;
- transport services at the general network level;
- route compression and rerouting.

Transit Hubs owns:
- passenger cohorts;
- terminal social scenes;
- representative crowd state.

Material Culture/Courier/Batch systems own:
- cargo identity;
- parcel/batch provenance;
- delivery/transfer consequences.

Weather owns:
- observations;
- forecasts;
- forecast revisions.

Technology/Maintenance owns:
- technical assets;
- faults;
- repair state.

Interregional Mobility owns:
- visitor/arrival context;
- regional recognition.

Pokémon Work and Pokémon Agency own any working-Pokémon assignment or association.

AutoPTU owns every tactical battle fact.

## 2. Airfield site

```yaml
airfield_site:
  airfield_id: null
  location_id: null
  operator_refs: []
  travel_connection_refs: []
  landing_area_ids: []
  terminal_or_hub_refs: []
  cargo_area_refs: []
  maintenance_asset_refs: []
  public_access_refs: []
  active_service_pattern_ids: []
  current_operational_band: UNKNOWN
  active_notice_ids: []
  ecology_observation_refs: []
  reuse_history_refs: []
  provenance_refs: []
  canon_status: proposed
```

Candidate operational bands:
- NORMAL
- LIMITED
- ARRIVALS_ONLY
- DEPARTURES_ONLY
- EMERGENCY_ONLY
- TEST_OR_POSITIONING_ONLY
- SUSPENDED
- CLOSED
- RESTORING
- DECOMMISSIONED
- UNKNOWN

These are orchestration states, not legal aviation categories.

## 3. Landing area state

An airfield may contain one or more authored landing areas.

```yaml
landing_area_state:
  landing_area_id: null
  airfield_id: null
  physical_condition_ref: null
  current_availability: UNKNOWN
  restriction_reason_refs: []
  inspection_refs: []
  active_work_refs: []
  weather_observation_refs: []
  ecology_observation_refs: []
  public_information_refs: []
  last_verified_event_id: null
```

Candidate availability states:
- AVAILABLE
- LIMITED
- OCCUPIED
- INSPECTION_REQUIRED
- WORK_IN_PROGRESS
- WEATHER_HOLD
- ECOLOGY_HOLD
- CLOSED
- STATUS_UNKNOWN

A landing area status does not define required length, surface, obstacle clearance, wind limits or aircraft performance. Those remain unresolved until canon and mechanics review.

## 4. Air service pattern

```yaml
air_service_pattern:
  service_pattern_id: null
  transport_service_ref: null
  operator_ref: null
  origin_airfield_id: null
  destination_airfield_ids: []
  service_role: passenger|cargo|mixed|research|medical|emergency|charter|other
  published_schedule_ref: null
  recurring_window_refs: []
  asset_requirement_refs: []
  staffing_requirement_refs: []
  dependency_refs: []
  current_state: PROPOSED
  public_information_refs: []
  canon_status: proposed
```

The role is descriptive. It does not create fares, capacity, access rights or vehicle statistics.

## 5. Exact flight operation

Do not instantiate one for every compressed background movement. Create an exact operation when it matters to story state, cargo, passengers, a case, a deadline, a disruption or a recurring service history.

```yaml
flight_operation:
  flight_operation_id: null
  service_pattern_ref: null
  vehicle_or_transport_asset_ref: null
  origin_airfield_id: null
  planned_destination_airfield_id: null
  actual_destination_airfield_id: null
  planned_departure_time: null
  actual_departure_time: null
  planned_arrival_time: null
  actual_arrival_time: null
  operational_state: PLANNED
  passenger_cohort_refs: []
  cargo_refs: []
  crew_assignment_refs: []
  weather_information_refs: []
  notice_refs: []
  diversion_or_hold_refs: []
  journey_ref: null
  provenance_refs: []
```

Suggested states:
- PLANNED
- BOARDING_OR_LOADING
- HELD
- READY
- DEPARTED
- IN_TRANSIT
- DIVERTING
- RETURNING
- ARRIVED
- CANCELLED
- ABORTED_BEFORE_DEPARTURE
- STATUS_UNKNOWN

A departure-board entry is not proof of departure. An announced arrival is not proof that the operation landed.

## 6. Operational hold

```yaml
flight_hold:
  hold_id: null
  flight_operation_ids: []
  airfield_or_landing_area_refs: []
  reason_class: weather|technical|staffing|access|ecology|traffic|cargo|information_gap|other
  triggering_evidence_refs: []
  decision_actor_refs: []
  started_at: null
  review_condition_refs: []
  ended_at: null
  outcome: null
```

A forecast can trigger a review or precaution, but Weather does not automatically close an airfield.

## 7. Diversion and return

```yaml
flight_diversion_event:
  event_id: null
  flight_operation_id: null
  prior_destination_id: null
  selected_destination_id: null
  decision_time: null
  cause_refs: []
  available_information_refs: []
  passenger_handoff_refs: []
  cargo_handoff_refs: []
  onward_journey_refs: []
  public_notice_refs: []
```

A diverted arrival does not automatically add a scheduled route. It can create temporary passenger, cargo and service pressure through existing systems.

## 8. Cargo handoff

Aviation records movement context only.

```yaml
air_cargo_handoff:
  handoff_id: null
  flight_operation_id: null
  cargo_instance_or_batch_refs: []
  from_custody_ref: null
  to_custody_ref: null
  observed_time: null
  observed_location_ref: null
  discrepancy_refs: []
  parent_system_event_refs: []
```

Material Culture, Batch Traceability and Courier decide provenance, condition, custody and delivery completion.

## 9. Passenger and privacy boundary

Exact passenger identity should be persisted only when another system has a reason.

Transit Hubs may keep an aggregate cohort. Individual actors are promoted when they become a witness, contact, worker, client, rival, care case or other persistent participant.

A passenger list, booking record or crew assignment can carry privacy constraints. Aviation does not make travel history universally public.

## 10. Weather information boundary

Keep these separate:
- forecast product;
- actual observation;
- what the operator received;
- what the decision actor believed;
- operational decision;
- later verification.

A forecast that turns out wrong may still have been reasonable information at departure. A visually rainy Minecraft sky cannot impose a flight hold by itself.

## 11. Ecology at an airfield

An airfield can overlap wildlife activity without treating every Pokémon as a hazard.

```yaml
airfield_ecology_observation:
  observation_id: null
  airfield_id: null
  landing_area_or_zone_ref: null
  observed_actor_or_collective_refs: []
  observed_behavior_refs: []
  time_ref: null
  source_ref: null
  interpretation_refs: []
  operational_review_ref: null
```

Conservation/Science own ecological interpretation. Aviation may consume a reviewed operational consequence.

A flying Pokémon near a landing area does not automatically create a closure, work assignment or combat encounter.

## 12. Pokémon-assisted aviation work

If an individual Pokémon participates in signalling, observation, cargo movement, passenger assistance or another task, the assignment must go through Pokémon Work.

Do not infer eligibility from:
- Flying type;
- visible ability to fly in Cobblemon;
- species reputation;
- size alone;
- proximity to the airfield.

Any mechanically meaningful carrying or mounted role requires PTU/Caelo validation of the exact individual and current implementation support.

## 13. Decommissioned and repurposed fields

Aviation infrastructure can persist after service ends.

Candidate later uses:
- emergency landing site;
- logistics yard;
- market/event ground;
- research staging area;
- heritage site;
- public open space;
- agriculture;
- wildlife habitat/corridor;
- partial redevelopment;
- unknown/contested use.

The same `airfield_id` may retain history while physical subareas change use. Reopening must account for those later states rather than resetting the site to its old configuration.

## 14. Flight record reconciliation

Operational records can disagree.

Possible evidence:
- departure board revision;
- staff log;
- cargo handoff timestamp;
- passenger testimony;
- weather notice;
- photograph;
- observed aircraft position;
- destination arrival record;
- maintenance record;
- public announcement.

No single source automatically becomes truth because it is official-looking.

## 15. Scene grammar

Useful noncombat patterns:

```text
planned movement
-> new evidence or dependency change
-> hold/reroute/cancel decision
-> passenger/cargo/service consequences
-> public information update
-> later verification
```

```text
old landing site
-> current-world survey
-> discover later use/ecology/infrastructure changes
-> competing restoration/reuse proposals
-> decision by owning systems
-> persistent physical consequence
```

## 16. Encounter contract — Runway Perimeter Withdrawal

Status: proposed, not canon.

Narrative premise:
Workers or surveyors must clear the perimeter after a wild or hostile group creates an immediate access problem near an inactive section of the field.

Intended full version:
The tactical objective supports withdrawal/route clearance, Intercept and forced movement where legal, distinct access lanes, objective-aware opponent behavior and accurate Minecraft playback. If weather or moving operational equipment matters mechanically, those effects are represented only through authoritative AutoPTU systems.

Capability dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
All aircraft movements are stopped before battle. Workers leave through world-state resolution and are not tactical units. The active landing area is excluded from the arena. Ouros selects the exact combatants and AutoPTU runs a static legal encounter. Wind, rain, lights, vehicles and machinery are visual only. Afterward, Aviation/Safety/Conservation decide whether the field can resume use.

## 17. Encounter contract — Diverted Cargo Apron Interruption

Status: proposed, not canon.

Narrative premise:
An unexpected diverted arrival creates a temporary cargo backlog. A separate conflict blocks safe access to one part of the staging area.

Intended full version:
Eventually supports CLEAR_ROUTE/WITHDRAW/PROTECT-like objective awareness, multiple access lanes, reactions/Intercept where governing rules allow them, and AI that values access and withdrawal rather than only KO.

Reduced version:
Cargo, vehicles and workers remain outside the tactical grid. The affected transport asset is shut down and static. One reviewed nearby arena resolves only the immediate opposing group. Winning creates a safe-access input; it does not deliver cargo or complete custody transfer.

## 18. Encounter contract — Old Airstrip Wildlife Conflict

Status: proposed, not canon.

Narrative premise:
A former landing strip has become part of a recurring wildlife route. A proposed temporary reopening creates a conflict between current habitat use and operational access.

Full version:
Could eventually use territorial/withdrawal-aware AI, changing access zones and environmental state.

Reduced version:
Survey and consultation establish the habitat conflict first. Any battle occurs away from active works on a static arena with explicitly selected participants. A victory never proves the strip can reopen and never erases ecological state.

## 19. Noncombat pattern — Five Reports, Three Flights

A reconciliation scene compares several records that apparently describe five operations. Two records may be revised versions, a positioning movement may have been mistaken for scheduled service, or one announced departure may have been cancelled.

Useful inputs:
- timestamps;
- board revisions;
- cargo handoffs;
- arrival observations;
- staff reports;
- photographs;
- weather products.

The result can remain unresolved if provenance is insufficient.

## 20. Cobblemon/Minecraft representation

Prefer deep reuse for presentation:
- runway/apron/terminal geometry;
- lights, signs, doors, barriers and display boards;
- sounds and particles;
- day/night and weather visuals;
- Pokémon entities, models, forms, poses, animations and cries;
- UI, networking and synchronization;
- world coordinates and persistent entity references where reviewed.

Use adapters for semantic state projection and player intent.

Never let Minecraft entity physics, Elytra logic, redstone, visible weather, vehicle mods or Cobblemon BattleState determine PTU movement, collisions, damage, participants, tactical weather or results.

Required direction:
`Ouros aviation/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

## 21. Mechanical guardrails

This extension establishes no:
- aircraft performance model;
- flight speed or capacity;
- fuel system;
- pilot Skill/DC;
- takeoff or landing roll;
- collision/fall/crash damage;
- aerial grid altitude rules;
- turbulence/crosswind modifiers;
- moving-platform battle rule;
- vehicle HP;
- weather threshold;
- passenger-carrying species permission;
- Flying-type work bonus;
- automatic use of Fly as public transport.

PTU Sky/Power/Mount rules remain authoritative only where they actually apply to an individual actor.

## 22. Canon questions

Open questions include:
- whether Ouros contains aircraft, airships, airports or small landing fields at all;
- which regions, settlements and institutions use them;
- passenger versus cargo prevalence;
- operator structures;
- technology level and maintenance practices;
- public versus restricted areas;
- emergency/diversion practices;
- how weather information reaches operators;
- whether any former strips have been repurposed;
- whether Pokémon participate in specific aviation tasks.

None is answered by this extension.