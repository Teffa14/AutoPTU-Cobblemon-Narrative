# Ouros Vertical Circulation & Lift Service Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established canon.

Date: 2026-08-28

## Purpose

This extension models the operating continuity of authored vertical conveyances inside or immediately attached to facilities: elevators, lifts, freight lifts, platform lifts and other canon-approved devices.

It deliberately does not own accessibility rights, facility repair, power networks, building ownership, inter-settlement travel or PTU tactical movement.

Existing ownership remains:

- Accessibility: whether a currently available route is usable by a specific actor and what accommodation is needed.
- Facility Maintenance: faults, assessments, work orders, repair and verification.
- Infrastructure Outage: upstream service loss and restoration handoffs.
- Travel/building graphs: physical route topology between authored spaces.
- Security/institutional owners: permission to enter a destination.
- AutoPTU: tactical movement and battle truth.

This layer preserves the operational state between those systems so a building does not collapse to `lift=true/false`.

## 1. Vertical transport system

```yaml
vertical_transport_system:
  vertical_system_id: null
  facility_id: null
  authored_kind: null
  operator_ref: null
  conveyance_unit_ids: []
  landing_ids: []
  served_connection_ids: []
  dependency_refs: []
  access_authority_refs: []
  current_service_state: unknown
  active_restriction_ids: []
  active_fault_refs: []
  active_verification_refs: []
  legacy_event_ids: []
  canon_reference_ids: []
```

`authored_kind` exists so future canon can distinguish elevator, freight lift, platform lift or another device without the generator inventing technology.

Suggested service states:

- UNKNOWN
- AVAILABLE
- LIMITED
- OUT_OF_SERVICE
- UNDER_WORK
- TESTING
- SERVICE_VERIFIED
- RETURNING_TO_SERVICE
- DECOMMISSIONED

`SERVICE_VERIFIED` can be transient evidence before `AVAILABLE`; it does not erase destination restrictions.

## 2. Landing

```yaml
vertical_landing:
  landing_id: null
  vertical_system_id: null
  location_id: null
  floor_or_level_ref: authored
  physical_access_ref: null
  destination_authority_ref: null
  current_landing_state: unknown
  alternate_route_refs: []
  accessibility_refs: []
  display_name_refs: []
  history_event_ids: []
```

Suggested landing states:

- UNKNOWN
- AVAILABLE
- RESTRICTED
- CLOSED
- BYPASSED
- UNDER_WORK

A landing can be unavailable while the rest of the system operates.

## 3. Conveyance unit

```yaml
vertical_conveyance_unit:
  unit_id: null
  vertical_system_id: null
  current_operational_state: unknown
  current_landing_id: null
  current_trip_id: null
  maintenance_asset_ref: null
  service_dependency_refs: []
  last_verified_at: null
```

Suggested operational states:

- UNKNOWN
- IDLE
- IN_SERVICE
- LIMITED
- ISOLATED
- OUT_OF_SERVICE
- UNDER_WORK
- TESTING

This is narrative operational state, not a machinery simulation.

## 4. Service request and trip

```yaml
vertical_service_request:
  request_id: null
  requester_actor_id: null
  origin_landing_id: null
  destination_landing_id: null
  requested_at: null
  authorization_ref: null
  accommodation_ref: null
  status: requested
  assigned_unit_id: null
  resulting_trip_id: null
```

Request statuses:

- REQUESTED
- AUTHORIZATION_PENDING
- ACCEPTED
- DECLINED
- CANCELLED
- UNIT_ASSIGNED
- SUPERSEDED

```yaml
vertical_service_trip:
  trip_id: null
  vertical_system_id: null
  unit_id: null
  origin_landing_id: null
  destination_landing_id: null
  passenger_actor_ids: []
  freight_or_equipment_refs: []
  boarding_started_at: null
  boarding_completed_at: null
  departure_at: null
  arrival_at: null
  exit_completed_at: null
  status: planned
  interruption_ref: null
```

Trip states:

- PLANNED
- AT_ORIGIN
- BOARDING
- BOARDED
- IN_TRANSIT
- ARRIVED
- EXITING
- COMPLETED
- INTERRUPTED
- ABORTED
- CANCELLED

The state model supports narrative continuity without requiring second-by-second motion.

## 5. Core separations

The following guards are permanent unless later canon explicitly replaces them:

`BUILDING_OPEN != EVERY_VERTICAL_ROUTE_AVAILABLE`

`POWER_AVAILABLE != VERTICAL_SERVICE_AVAILABLE`

`FAULT_REPAIRED != SERVICE_VERIFIED`

`SERVICE_AVAILABLE != ACTOR_AUTHORIZED`

`ACTOR_AUTHORIZED != DESTINATION_AUTHORIZED`

`UNIT_AT_LANDING != BOARDING_AUTHORIZED`

`DOOR_OPEN != DESTINATION_ACCESSIBLE`

`PASSENGER_BOARDED != TRIP_DEPARTED`

`UNIT_ARRIVED != PASSENGER_EXITED`

`TRIP_COMPLETED != DOWNSTREAM_ACTIVITY_COMPLETED`

These differences create useful provenance and prevent visual presentation from becoming authority.

## 6. Authorization handoff

This layer does not create security, tenancy, employment or institutional rights.

```yaml
vertical_destination_authorization:
  authorization_id: null
  actor_id: null
  landing_or_destination_id: null
  authority_owner_system: null
  authority_record_ref: null
  effective_from: null
  effective_until: null
  current_state: unknown
```

Possible states:

- UNKNOWN
- AUTHORIZED
- NOT_AUTHORIZED
- TEMPORARY
- REVIEW_REQUIRED

A key, card, badge or other presentation object may represent authorization only when connected to an authoritative record.

## 7. Accessibility handoff

Accessibility remains actor-specific.

```yaml
vertical_accessibility_handoff:
  handoff_id: null
  vertical_system_id: null
  landing_ids: []
  current_service_state: null
  alternate_route_refs: []
  effective_at: null
  accessibility_owner_action_required: true
```

The accessibility system can then decide whether the actor still has a viable route, requires assistance, must relocate an appointment, or faces a participation barrier.

This extension never infers that stairs are an acceptable substitute for a particular actor.

## 8. Maintenance lifecycle handoff

Facility Maintenance owns technical condition.

```yaml
vertical_maintenance_handoff:
  handoff_id: null
  vertical_system_id: null
  unit_id: null
  maintenance_fault_ref: null
  work_order_ref: null
  verification_ref: null
  maintenance_outcome: null
  received_at: null
  resulting_service_state: null
```

A repair can result in TESTING or SERVICE_VERIFIED rather than immediate availability.

## 9. Upstream outage handoff

Infrastructure can report loss/restoration of an authored dependency.

```yaml
vertical_dependency_handoff:
  handoff_id: null
  vertical_system_id: null
  dependency_ref: null
  availability_state: null
  effective_at: null
  verification_refs: []
  vertical_owner_action_required: true
```

Power returning does not cause an automatic trip or reopen every landing.

## 10. Service restriction

```yaml
vertical_service_restriction:
  restriction_id: null
  vertical_system_id: null
  affected_unit_ids: []
  affected_landing_ids: []
  restriction_type: authored
  reason_claim_refs: []
  authority_ref: null
  effective_from: null
  end_condition_ref: null
  current_state: active
```

Useful high-level restriction types can include:

- UNIT_UNAVAILABLE
- LANDING_UNAVAILABLE
- DESTINATION_RESTRICTED
- SERVICE_LIMITED
- TEMPORARY_ISOLATION
- FREIGHT_ONLY
- PASSENGER_ONLY

These labels do not create legal standards or technical rules.

## 11. Interruption record

```yaml
vertical_trip_interruption:
  interruption_id: null
  trip_id: null
  first_observed_at: null
  observation_refs: []
  suspected_cause_claim_refs: []
  confirmed_cause_claim_refs: []
  unit_state_after: null
  passenger_state_refs: []
  response_refs: []
  maintenance_fault_ref: null
  status: open
```

Do not infer cause from timing. A power change, nearby Pokémon, weather event or passenger action can coexist with an interruption without proving causation.

## 12. Alternate-route consequences

When vertical service changes, emit route-state changes to the building/access graph rather than teleporting actors.

Possible downstream consequences:

- a clinic moves one service to an accessible floor;
- deliveries move to a freight route;
- residents use another entrance;
- an event shifts registration downstairs;
- a public counter temporarily relocates;
- a service appointment is rescheduled;
- a previously quiet stair landing becomes a social node.

The receiving system owns each consequence.

## 13. Persistent history

```yaml
vertical_service_history_event:
  event_id: null
  vertical_system_id: null
  event_type: null
  timestamp: null
  affected_unit_ids: []
  affected_landing_ids: []
  trip_refs: []
  fault_or_work_refs: []
  state_before: null
  state_after: null
  public_record_refs: []
  player_involvement_refs: []
```

Useful event types:

- SERVICE_LIMITED
- UNIT_ISOLATED
- LANDING_CLOSED
- TRIP_INTERRUPTED
- WORK_STARTED
- TESTING_STARTED
- SERVICE_VERIFIED
- RETURNED_TO_SERVICE
- DESTINATION_POLICY_CHANGED
- UNIT_DECOMMISSIONED
- ALTERNATE_ROUTE_ESTABLISHED

History persists after signs and barriers disappear.

## 14. Floor naming and renovation continuity

A floor label is presentation metadata, not identity.

If a building is renovated, renumbered or repurposed, preserve stable `location_id` and `landing_id` values while allowing display names and route connections to change by effective date.

This supports mysteries where an old plan says “Level 4,” a current sign says “Archive,” and a maintenance record refers to the same landing by an older code.

## 15. Pokémon participation gate

Do not infer:

- lift operation from Electric typing;
- machinery repair from Steel or Electric typing;
- freight-lifting competence from size or Strength flavor;
- shaft rescue from Flying typing;
- safe carrying from Mount capability;
- access privileges from species;
- hazard immunity from Type.

Mechanically meaningful participation needs an exact governing capability, Move, Ability, Item, Trainer Feature/perk, authored trained role or setting rule.

## 16. Minecraft/Cobblemon representation

Safe presentation can include:

- lift doors and landing indicators;
- call buttons as UI triggers;
- barriers and out-of-service signs;
- alternate-route signage;
- static cars/platforms;
- maintenance props;
- changed floor labels after renovation;
- NPC queues or staff where world state supports them;
- sounds, lights and particles;
- Pokémon models/forms/poses/animations/cries;
- persistence hooks for unit/landing/service state.

Unsafe shortcuts:

- redstone proving service readiness;
- a moving platform becoming authoritative PTU movement;
- open doors proving authorization;
- teleportation proving a completed trip without authoritative state transition;
- Minecraft fall damage substituting for PTU damage;
- pistons/crushing blocks applying ungoverned PTU effects;
- chunk unload resetting a stalled trip or outage;
- Cobblemon selecting battle participants because entities share a car.

## 17. Encounter contract A — Lift Lobby Withdrawal

Narrative premise:

A vertical route is unavailable during a localized incident and several actors need to clear the lobby or reach an already verified alternate path while a hostile or distressed Pokémon blocks the space.

Full-version dependency families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle where timed withdrawal matters;
- full stateful damage pipeline;
- status lifecycle where legal effects apply;
- terrain/weather/hazards/zones/reactions if doors, shaft edges or changing restricted cells matter;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for withdrawal/protection behavior;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:

The lift is isolated before battle. Civilians complete relocation outside tactical resolution. Shaft access and moving doors are excluded from the grid. AutoPTU receives a static lobby with explicit combatants. Victory secures the immediate lobby only; it does not restore lift service or complete anyone's later journey.

## 18. Encounter contract B — Machine-Room Perimeter

Narrative premise:

Access to an isolated service area is blocked by a Pokémon incident while authorized workers need the perimeter secured before assessment can continue.

Full version can require technical hazard zones, reactions, protection objectives, forced movement and semantic playback if energized or moving equipment remains tactically active.

Reduced version:

Equipment is shut down and isolated before BattleSpec creation. Workers and machinery stay outside the grid. Resolve a static adjacent service corridor. The result can set `PERIMETER_SECURED`; Maintenance still owns assessment, repair and verification.

## 19. Encounter contract C — Split-Floor Diversion

Narrative premise:

One landing is closed and activity has shifted to another floor. A conflict at the temporary route junction threatens the diversion.

Full version can require objective-aware AI, Intercept/forced movement and generalized reactions to protect a moving withdrawal stream.

Reduced version:

Complete the civilian reroute first. Resolve the conflict in a static junction with ordinary legal combatants. Accessibility and building-route state remain authoritative outside combat.

## 20. Noncombat exploration — The Floor That Changed Names

A large public building has been renovated several times. Old plans, maintenance logs, resident memories and current signage use different names for the same vertical landings.

Playable sequence:

1. collect plan versions and effective dates;
2. map old floor labels to stable landing/location IDs;
3. separate closed landings from renamed destinations;
4. identify which vertical systems served each historical configuration;
5. verify current access independently of historical access;
6. resolve an archive, maintenance or social question using provenance.

This can run now without moving-platform combat mechanics.

## 21. Long-term narrative value

A vertical route can become part of the identity of a building without turning into a repetitive maintenance chore. Materialize scenes when service state creates a meaningful social, logistical, accessibility or historical consequence. Compress routine trips.

The important persistent unit is not “an elevator puzzle.” It is a building whose routes, users, staff, restrictions, workarounds and memories change over time.

## 22. Canon and rules safeguards

Do not infer:

- exact lift technology;
- speed, capacity, load limits or travel time;
- safety-code requirements;
- inspection jurisdiction;
- operator licensing;
- mandatory outage reporting;
- emergency procedures;
- shaft geometry or fall damage;
- door/crushing damage;
- rescue procedure;
- ownership or right of access;
- passenger fees;
- Pokémon labor legality;
- PTU bonuses from lift equipment.

All such facts require governing canon or mechanics.

## 23. Implementation value

This layer gives persistent buildings an explicit internal service graph. Accessibility can react correctly to a lift outage, Maintenance can repair the unit without directly rewriting route truth, Infrastructure can restore power without silently reopening it, and Minecraft can show intermediate states while AutoPTU remains the sole tactical authority.