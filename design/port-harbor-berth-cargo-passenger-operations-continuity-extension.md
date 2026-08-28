# Ouros Port, Harbor, Berth, Cargo & Passenger Operations Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon.

Parent systems:
- `design/maritime-coasts-depths-layer.md`
- `design/travel-transport-expedition-layer.md`
- `design/transit-hubs-passenger-cohorts-extension.md`
- `design/courier-parcel-last-mile-logistics-extension.md`
- `design/material-culture-economy-crafting-layer.md`
- `design/batch-traceability-recall-quarantine-extension.md`
- `design/facility-maintenance-repair-inspection-extension.md`
- `design/public-notices-signage-world-information-extension.md`
- `design/workplaces-professions-staffing-layer.md`
- `design/coastal-navigation-aids-lighthouses-beacon-continuity-extension.md`
- `design/cobblemon-runtime-authority-boundary.md`

## Purpose

This extension gives ports selective operational memory.

It answers questions such as:

- which exact berth can be used right now;
- which vessel call is planned, active, delayed, diverted or complete;
- whether passengers may board even when the vessel is present;
- whether cargo has physically crossed a custody boundary;
- whether a manifest describes the current load or an older plan;
- whether one waterfront function can continue while another is restricted;
- what a temporary operational workaround changes elsewhere in the world.

It does not create maritime physics, legal customs regimes, cargo mechanics, vessel combat rules or a second transport system.

## 1. Authority boundary

Maritime owns harbor identity, sea lanes, maritime assets and marine context.

Travel owns route viability, journeys, schedules and transport-service state.

Transit Hubs owns passenger cohorts, temporary co-presence and scene expansion.

Courier owns shipments, delivery legs and custody transfers.

Material Culture owns item identity, ownership/provenance and material batches.

Batch Traceability owns recall/hold/correction state after distribution.

Facility Maintenance owns technical diagnosis, work, repair and verification.

Public Notices owns displayed service/closure information.

Credentials owns individual authorizations when canon requires them.

Workplaces owns staffing and professional assignments.

Crisis owns emergency state and recovery.

Conservation/Wildlife owns ecological interpretation.

This extension owns berth-level operating state, exact port-call records and the coordination episode that connects those parent systems.

## 2. Port operating state

```yaml
port_operating_state:
  port_id: null
  harbor_id: null
  active_berth_ids: []
  restricted_berth_ids: []
  active_call_ids: []
  current_pressure_band: NORMAL
  passenger_processing_state: NORMAL
  cargo_processing_state: NORMAL
  active_operational_notice_ids: []
  active_disruption_ids: []
  active_mitigation_ids: []
  last_verified_event_id: null
```

Candidate pressure bands:

- LOW
- NORMAL
- BUSY
- CONGESTED
- SEVERE
- UNKNOWN

Pressure is descriptive world state. It creates no initiative, movement, crowd or Accuracy modifier.

## 3. Berth or landing point

```yaml
port_berth:
  berth_id: null
  port_id: null
  location_id: null
  berth_type: null
  supported_service_refs: []
  supported_asset_refs: []
  access_profile_refs: []
  maintenance_asset_refs: []
  navigation_asset_refs: []
  public_access_state: null
  operational_state: AVAILABLE
  active_call_id: null
  reservation_or_allocation_refs: []
  ecology_overlap_refs: []
  history_event_ids: []
  last_verified_event_id: null
```

Candidate operational states:

- AVAILABLE
- RESERVED
- OCCUPIED
- TURNAROUND
- RESTRICTED
- MAINTENANCE
- INSPECTION
- TESTING
- TEMPORARY_USE
- CLOSED
- DISUSED
- UNKNOWN

These are operating labels, not legal categories.

A berth may remain physically present while `DISUSED`. A harbor may remain open while one berth is `CLOSED`.

## 4. Exact port call

```yaml
port_call:
  call_id: null
  port_id: null
  maritime_asset_id: null
  service_id: null
  journey_ids: []
  call_purpose_tags: []
  planned_arrival_window_ref: null
  actual_arrival_time: null
  planned_berth_id: null
  actual_berth_id: null
  current_call_state: PLANNED
  planned_departure_window_ref: null
  actual_departure_time: null
  passenger_operation_ids: []
  cargo_operation_ids: []
  support_service_refs: []
  notice_refs: []
  exception_ids: []
  provenance_refs: []
  completion_event_id: null
```

Candidate call states:

- PLANNED
- CONFIRMED
- APPROACHING
- WAITING
- BERTHING
- ALONGSIDE
- OPERATING
- DEPARTURE_HELD
- DEPARTING
- COMPLETED
- DIVERTED
- CANCELLED
- UNKNOWN

A call record persists after departure.

## 5. Port-call purpose

Purpose tags can include:

- PASSENGER
- CARGO
- MIXED
- FISHERIES_LANDING
- RESEARCH
- RESCUE
- MAINTENANCE
- EVENT
- TEST
- EMERGENCY
- OTHER_AUTHORED_PURPOSE

A purpose tag does not define cargo content, passenger identity or authority.

## 6. Berth allocation

```yaml
berth_allocation:
  allocation_id: null
  call_id: null
  requested_berth_ids: []
  assigned_berth_id: null
  assigned_at: null
  valid_window_ref: null
  allocation_basis_refs: []
  supersedes_allocation_id: null
  status: ACTIVE
```

A changed allocation is normal operational history. It is not evidence of sabotage, corruption or error by itself.

The assigned berth does not physically teleport the vessel. Actual arrival requires an observed/authoritative event.

## 7. Passenger operation

```yaml
port_passenger_operation:
  passenger_operation_id: null
  call_id: null
  journey_ids: []
  hub_or_terminal_ref: null
  operation_type: EMBARKATION
  authorization_profile_refs: []
  current_state: NOT_STARTED
  passenger_cohort_refs: []
  representative_actor_ids: []
  exception_ids: []
  started_at: null
  completed_at: null
```

Candidate operation types:

- EMBARKATION
- DISEMBARKATION
- TRANSFER
- EVACUATION
- OTHER

Candidate states:

- NOT_STARTED
- READY
- PAUSED
- IN_PROGRESS
- COMPLETE
- CANCELLED
- UNKNOWN

Important separations:

- vessel presence does not prove boarding permission;
- valid credential does not prove the sailing will depart;
- boarding complete does not prove the journey has departed;
- arriving at the port does not prove the actor reached their final destination.

Exact passenger identity should be persisted only when another system makes it meaningful. Otherwise use Transit Hub cohorts.

## 8. Cargo operation

```yaml
port_cargo_operation:
  cargo_operation_id: null
  call_id: null
  operation_type: LOAD
  shipment_refs: []
  material_batch_refs: []
  item_instance_refs: []
  declared_manifest_ref: null
  observed_transfer_refs: []
  source_custody_refs: []
  destination_custody_refs: []
  staging_location_ref: null
  current_state: NOT_STARTED
  exception_ids: []
  started_at: null
  completed_at: null
```

Candidate operation types:

- LOAD
- DISCHARGE
- TRANSSHIP
- RETURN
- HOLD
- OTHER

Candidate states:

- NOT_STARTED
- STAGED
- IN_PROGRESS
- PAUSED
- PHYSICALLY_COMPLETE
- CUSTODY_PENDING
- COMPLETE
- CANCELLED
- UNKNOWN

The port layer references existing shipment/items/batches. It never duplicates them.

`PHYSICALLY_COMPLETE` means the transfer movement ended. `COMPLETE` additionally requires the appropriate custody/operational handoff record when one is expected.

## 9. Manifest and declared record

```yaml
port_manifest_record:
  manifest_id: null
  call_id: null
  record_type: null
  revision_id: null
  declared_entry_refs: []
  issuer_ref: null
  authored_at: null
  effective_for_window_ref: null
  supersedes_manifest_id: null
  evidence_refs: []
  verification_state: UNVERIFIED
  access_or_privacy_refs: []
```

Candidate verification states:

- UNVERIFIED
- PARTIALLY_RECONCILED
- RECONCILED
- DISPUTED
- SUPERSEDED
- UNKNOWN

A manifest is an information artifact. It does not reveal hidden contents, ownership or canonical truth.

## 10. Transfer observation

```yaml
port_transfer_observation:
  observation_id: null
  port_id: null
  berth_id: null
  call_id: null
  observed_at: null
  observer_ref: null
  observation_type: null
  subject_refs: []
  observed_quantity_or_band: null
  observed_condition: null
  media_refs: []
  confidence_band: null
  interpretation_refs: []
```

Observation types can include:

- VESSEL_PRESENT
- VESSEL_ABSENT
- GANGWAY_STATE
- PASSENGER_FLOW
- CARGO_UNIT_MOVEMENT
- STORAGE_BACKLOG
- BERTH_OCCUPANCY
- EQUIPMENT_STATE
- WILDLIFE_ACTIVITY
- OTHER

Observation and interpretation remain separate.

## 11. Port exception

```yaml
port_operation_exception:
  exception_id: null
  port_id: null
  call_id: null
  berth_id: null
  exception_type: null
  detected_at: null
  evidence_refs: []
  affected_operation_refs: []
  current_mitigation_refs: []
  responsible_system_refs: []
  status: OPEN
```

Useful authored exception types:

- BERTH_UNAVAILABLE
- CALL_DELAY
- CALL_DIVERSION
- PASSENGER_HOLD
- CARGO_HOLD
- MANIFEST_DISCREPANCY
- CUSTODY_DISCREPANCY
- EQUIPMENT_UNAVAILABLE
- STAFFING_LIMITATION
- ROUTE_OR_WEATHER_RESTRICTION
- NAVIGATION_AID_RESTRICTION
- EVENT_PRESSURE
- ECOLOGY_CONSTRAINT
- UNKNOWN_CAUSE

These labels do not establish fault.

## 12. Waiting and diversion

A vessel waiting for a berth is not the same as a cancelled service.

```yaml
call_wait_state:
  call_id: null
  waiting_location_ref: null
  waiting_since: null
  reason_refs: []
  expected_next_review_ref: null
  passenger_consequence_refs: []
  cargo_consequence_refs: []
  travel_consequence_refs: []
```

If a different port/landing receives the call, Travel/Maritime must author that route/call consequence. The port layer cannot invent a safe alternative destination.

## 13. Congestion and backlog

Congestion must be derived from actual state such as:

- overlapping active calls;
- unavailable berth capacity;
- delayed departure occupying a berth;
- cargo staging backlog;
- passenger event pressure;
- maintenance restriction;
- route/weather disruption;
- staffing limitation;
- crisis activity.

A `CONGESTED` label is an aggregate consequence. It does not create tactical crowd rules.

## 14. Temporary operational workaround

```yaml
port_mitigation:
  mitigation_id: null
  port_id: null
  affected_call_or_berth_refs: []
  mitigation_type: null
  started_at: null
  expected_end_ref: null
  service_consequence_refs: []
  notice_refs: []
  verification_refs: []
  status: ACTIVE
```

Possible descriptive patterns:

- alternate berth;
- temporary passenger landing;
- cargo staged elsewhere;
- reduced call pattern;
- delayed transfer window;
- temporary shuttle connection;
- manual information procedure.

A temporary berth cannot appear merely because the story needs one. Geometry, access and governing world state must support it.

## 15. Partial reopening

A repaired waterfront should reopen by evidence, not by quest completion.

Possible sequence:

```text
fault/restriction
-> maintenance or other intervention
-> technical verification
-> berth-level operating decision
-> service rescheduling/allocation
-> passenger/cargo operations resume
-> public information updates
-> follow-up review
```

Passenger and cargo functions may resume at different times.

## 16. Disused and repurposed waterfront

```yaml
waterfront_use_episode:
  use_episode_id: null
  berth_or_facility_ref: null
  use_type: null
  started_at: null
  ended_at: null
  operator_or_steward_refs: []
  infrastructure_change_refs: []
  ecology_overlap_refs: []
  public_access_refs: []
  history_refs: []
```

Potential non-canon use types include transport, fisheries, warehousing, market, public space, heritage, maintenance, emergency use, research access and habitat stewardship.

A future reopening inherits those episodes.

## 17. Actor knowledge

Actors should know port state through evidence channels:

- current service notice;
- timetable or booking;
- direct observation;
- worker statement;
- prior journey experience;
- local rumor;
- map/guide;
- institutional message;
- public display.

Do not synchronize every actor to authoritative state instantly.

## 18. Pokémon agency and work boundary

A Pokémon present at a waterfront can be:

- wild;
- partnered with a traveler;
- a resident/regular visitor;
- participating in approved work;
- receiving care;
- part of a research observation;
- completely unrelated to port operations.

Species, Type, size or proximity never establishes a work assignment.

Pokémon Work plus PTU/Caelo capability evidence must authorize any functional task. Nearby entities never determine battle participants.

## 19. Non-combat playable patterns

Port play can include:

- reconcile a manifest against observed transfers and custody events;
- find why a shipment stopped at `CUSTODY_PENDING`;
- compare old and current berth allocations;
- coordinate a passenger connection after a delayed call;
- document a temporary berth before a festival;
- investigate why one service remains suspended after another resumes;
- trace effects of changed waterfront traffic on businesses or wildlife;
- recover the operational history of a disused landing.

These can ship without tactical adapter support.

## 20. Mechanically rich encounter contracts

### Berth Evacuation Withdrawal

Narrative premise:

An immediate conflict near an active waterfront requires people to clear the berth while operations are suspended.

Intended full version wants:

- multiple withdrawal routes;
- Intercept and forced movement;
- route protection/denial;
- meaningful dock-edge or restricted-work zones if exact rules support them;
- objective-aware AI that values evacuation/withdrawal over KO;
- authoritative Minecraft playback.

Safe reduced version:

- suspend vessel/cargo movement before BattleSpec;
- evacuate passengers, workers and nonparticipant Pokémon in world state;
- move significant cargo/equipment outside tactical targeting;
- choose a static quay/yard arena away from water edge and machinery;
- select combatants explicitly in Ouros;
- AutoPTU resolves combat only;
- Port/Travel/Maintenance decide whether operations resume afterward.

### Cargo Transfer Interruption

Narrative premise:

A conflict occurs during an important handoff, but the cargo itself must remain governed by custody/provenance systems.

Intended full version wants:

- CLEAR_ROUTE/PROTECT/WITHDRAW-like objectives;
- complete movement/reaction handling;
- possible static zones around staging areas;
- AI that understands route control and protection;
- item/Feature/Ability interactions only where exact implementations exist;
- authoritative playback.

Safe reduced version:

- pause the transfer before combat;
- freeze custody state at the last verified handoff;
- remove cranes, vehicles and cargo units from tactical interaction;
- use a nearby static arena;
- no battle result moves ownership or custody;
- resume/cancel/reconcile transfer through port and courier systems afterward.

### Harbor Entrance Diversion

Narrative premise:

A conflict near a harbor entrance forces traffic to remain outside while a safe route is restored.

Intended full version wants:

- route-control/withdrawal objectives;
- water/shore terrain only if exact rules support it;
- weather/current/hazard interaction only if verified;
- objective-aware AI;
- adapter/playback.

Safe reduced version:

- hold all vessels outside the encounter before combat;
- choose a static shore/breakwater/land approach arena;
- do not simulate moving craft, current, drowning or collision;
- AutoPTU resolves selected combatants only;
- Maritime/Port/Travel determine later whether calls remain waiting, divert or resume.

## 21. Capability dependency classification

The intended rich versions may depend on the permanent engine categories as follows:

- targeting/footprints/range/LoS — required; currently VERIFIED at family level;
- base movement legality — required; VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — required for evacuation/route-control richness; PARTIAL;
- core calculations — required for ordinary combat; VERIFIED;
- action economy/initiative — required; VERIFIED;
- full turn/round lifecycle — required for production-complete battle flow; PARTIAL;
- full stateful damage pipeline — required for production-complete combat; PARTIAL;
- status lifecycle — required whenever encounter content applies statuses; PARTIAL;
- terrain/weather/hazards/zones/reactions — required for mechanically active dock edges, water, machinery, weather or reaction zones; BLOCKING;
- move-specific behavior — required only for selected Moves and cannot be generalized; PARTIAL;
- abilities — required only for selected Abilities and cannot be generalized; PARTIAL;
- items — required if a chosen battle uses relevant Items; PARTIAL;
- Trainer Features/perks — required when Intercept/Feature hooks participate; PARTIAL;
- AI legal-action infrastructure — required and VERIFIED as infrastructure;
- AI tactical policy — required for evacuation, protection, territorial and route-control objectives; BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — required for authoritative in-world battle presentation; BLOCKING.

Reduced versions intentionally avoid depending on mechanically active port infrastructure.

## 22. Minecraft/Cobblemon projection boundary

Strong SAFE_REUSE candidates, subject to concrete API inspection:

- water/shore/wharf geometry;
- blocks, slabs, stairs, fences, gates and doors;
- lamps, signs, boards and decorative terminal displays;
- particles, sounds and ambient weather presentation;
- boats/ship-like visual assets where available and appropriate;
- Pokémon entities, models, forms, poses, cries and overworld animations;
- UI surfaces;
- entity tracking, networking and synchronization hooks.

ADAPTER_REQUIRED examples:

- stable mapping from an Ouros `berth_id` or `port_id` to world geometry;
- projecting an authoritative berth closure into barriers/signage;
- turning reviewed world geometry into AutoPTU cells;
- linking an Ouros maritime asset to a visual vessel entity without letting that entity own operational truth;
- maintaining identity across chunk unload/reload.

Minecraft/Cobblemon must never decide:

- who is a combatant because they are nearby;
- which berth is operational because a block exists;
- whether a vessel call completed because a boat moved;
- cargo ownership or custody because an item entity crossed a line;
- passenger authorization;
- PTU HP/status/position;
- collision, fall, current or machinery damage;
- Push/Pull/Intercept outcomes;
- weather mechanics;
- battle result;
- whether the port reopens.

Authority remains:

`Ouros port/world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## 23. Canon questions this extension does not answer

- which Ouros regions possess formal ports, harbors or ferry landings;
- whether formal berth allocation exists everywhere or only at larger facilities;
- what cargo documentation practices exist;
- whether passenger manifests/registers exist and who may access them;
- whether Ouros has customs, immigration, pilotage, tug services or harbor-master institutions;
- what credentials are required for particular sailings;
- what technologies move cargo;
- what working roles Pokémon may perform;
- what privacy, labor, safety or maritime-law traditions exist;
- which historic waterfronts were abandoned or repurposed.

All remain UNKNOWN until canon or governing source material establishes them.