# Ouros Maritime Ferry, Port & Passenger-Service Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension specializes the existing Travel/Transport layer for recurring maritime passenger service. It covers terminal operations, sailing identity, boarding, intermediate calls, arrival, disembarkation, service disruption, passenger reconciliation and operational handoffs.

It does not define ship combat, ocean physics, weather effects, legal port authority, navigation checks, vessel engineering, cargo economy, rescue law or ownership rules.

## Owner boundary

Travel/Transport remains owner of connection graphs, route knowledge, generic service state and journey orchestration.

This extension owns maritime-service continuity records.

Weather owns observations, forecasts and weather episodes.

Coastal Navigation Aids owns beacons, lighthouses and navigation-aid continuity.

Maintenance and Construction own vessel/facility repair and physical project state where applicable.

Crisis/Rescue owns emergency search, rescue and evacuation operations.

Courier/Logistics and Material Culture own cargo or item custody chains.

Pokémon Agency owns persistent Pokémon identity, partnership, custody and ownership state.

No handoff is automatic merely because two records share a location or timestamp.

## Maritime network node

A port or ferry terminal can participate in several services without collapsing into one state.

```yaml
maritime_terminal:
  terminal_id: null
  place_id: null
  berth_ids: []
  service_ids: []
  operator_ids: []
  public_area_refs: []
  access_state: null
  passenger_service_state: null
  cargo_service_refs: []
  maintenance_refs: []
  construction_refs: []
  active_disruption_ids: []
  public_information_refs: []
  last_review_event_id: null
```

Useful passenger-service states may include:

- OPERATING
- LIMITED
- BOARDING_ONLY
- ARRIVALS_ONLY
- TEMPORARY_LOCATION
- SUSPENDED
- RESTORING
- CLOSED
- UNKNOWN

These are narrative service states, not mechanics.

## Berth state

```yaml
berth_state:
  berth_id: null
  terminal_id: null
  physical_state: null
  operational_state: null
  assigned_sailing_ids: []
  restriction_refs: []
  maintenance_refs: []
  construction_refs: []
  weather_dependency_refs: []
  last_verified_event_id: null
```

A berth may be physically intact but operationally unavailable. A terminal may remain open while one berth is unavailable.

## Service identity

```yaml
maritime_service:
  service_id: null
  operator_ids: []
  public_name: null
  connection_ids: []
  terminal_ids: []
  normal_stop_pattern_ids: []
  vessel_pool_refs: []
  passenger_policy_refs: []
  cargo_policy_refs: []
  booking_or_access_policy_refs: []
  current_service_state: OPERATING
  disruption_ids: []
  public_information_refs: []
  last_service_event_id: null
```

A service is not a vessel. A vessel is not a sailing.

## Sailing identity

```yaml
maritime_sailing:
  sailing_id: null
  service_id: null
  planned_origin_terminal_id: null
  planned_destination_terminal_id: null
  planned_stop_call_ids: []
  planned_departure_time: null
  planned_arrival_time: null
  assigned_vessel_ref: null
  actual_origin_terminal_id: null
  actual_stop_call_ids: []
  actual_departure_event_id: null
  actual_arrival_event_id: null
  current_phase: PLANNED
  disruption_ids: []
  passenger_reconciliation_ids: []
  cargo_handoff_refs: []
  world_truth_refs: []
```

Suggested phases:

- PLANNED
- CHECK_IN_OR_ASSEMBLY
- BOARDING
- BOARDING_PAUSED
- READY_TO_DEPART
- DEPARTED
- UNDERWAY
- INTERMEDIATE_CALL
- REROUTING
- RETURNING_TO_ORIGIN
- ARRIVED_AT_BERTH
- DISEMBARKING
- COMPLETE
- CANCELLED
- ABORTED

Do not infer skipped phases. A compressed routine journey may store only the events that matter while preserving the same semantic order.

## Stop calls

```yaml
maritime_stop_call:
  stop_call_id: null
  sailing_id: null
  terminal_id: null
  planned_sequence: null
  planned_arrival_time: null
  planned_departure_time: null
  actual_arrival_event_id: null
  actual_departure_event_id: null
  call_state: PLANNED
  embarkation_record_refs: []
  disembarkation_record_refs: []
  passenger_count_refs: []
  cargo_handoff_refs: []
  berth_ref: null
  disruption_refs: []
```

Suggested call states:

- PLANNED
- APPROACHING
- BERTHED
- BOARDING
- DISEMBARKING
- COMPLETE
- SKIPPED
- DIVERTED
- CANCELLED

A skip-stop can leave the overall service operating.

## Passenger journey record

This layer must avoid inventing a universal ticket or legal manifest system. A region may use bookings, passes, walk-up boarding, institutional travel or another authored system.

```yaml
maritime_passenger_journey:
  passenger_journey_id: null
  actor_id: null
  sailing_id: null
  intended_origin_terminal_id: null
  intended_destination_terminal_id: null
  access_or_booking_refs: []
  assembly_or_checkin_event_id: null
  boarding_event_id: null
  current_presence_state: null
  disembarkation_event_id: null
  completed_destination_terminal_id: null
  reconciliation_refs: []
  privacy_refs: []
```

Possible presence states:

- EXPECTED
- PRESENT_AT_TERMINAL
- BOARDED
- CONFIRMED_ONBOARD
- DISEMBARKED_AT_INTERMEDIATE_STOP
- DISEMBARKED_AT_DESTINATION
- NO_SHOW
- CANCELLED
- TRANSFERRED
- UNKNOWN

No state grants ownership, citizenship, identity certainty or custody authority.

## Count and reconciliation records

```yaml
passenger_count_record:
  count_record_id: null
  sailing_id: null
  stop_call_id: null
  count_type: null
  observed_count: null
  method_ref: null
  timestamp: null
  observer_or_system_ref: null
  confidence: null
  source_refs: []
  supersedes_record_id: null
```

Count types can include:

- EXPECTED_OR_BOOKED
- ASSEMBLED
- BOARDED
- CURRENT_ONBOARD
- ARRIVAL
- DISEMBARKED

Exact procedures are canon-dependent.

```yaml
passenger_reconciliation:
  reconciliation_id: null
  sailing_id: null
  trigger_record_refs: []
  discrepancy_type: null
  evidence_refs: []
  inquiry_event_refs: []
  current_state: OPEN
  resolution_ref: null
  external_handoff_refs: []
```

Suggested states:

- OPEN
- RECOUNTING
- CHECKING_RECORDS
- CONTACTING_PARTIES
- HANDOFF_REQUIRED
- RESOLVED
- CLOSED_UNRESOLVED

A discrepancy may resolve to duplicate count, late boarding, early disembarkation, stale booking, recording error, transfer, wrong stop assumption or another authored cause.

Do not default to person overboard, crime or deception.

## Boarding and disembarkation events

```yaml
maritime_boarding_event:
  event_id: null
  sailing_id: null
  terminal_id: null
  actor_ids: []
  event_type: null
  timestamp: null
  source_refs: []
  world_truth_refs: []
```

Candidate event types:

- BOARDING_STARTED
- PASSENGER_BOARDED
- BOARDING_PAUSED
- BOARDING_RESUMED
- BOARDING_CLOSED
- PASSENGER_DISEMBARKED
- DISEMBARKATION_STARTED
- DISEMBARKATION_COMPLETE

Presence must come from world truth, not Minecraft entity position alone.

## Disruption record

```yaml
maritime_service_disruption:
  disruption_id: null
  service_id: null
  sailing_ids: []
  terminal_ids: []
  berth_ids: []
  cause_refs: []
  observed_effects: []
  operational_decision_refs: []
  public_information_refs: []
  alternative_service_refs: []
  current_state: ACTIVE
  review_event_id: null
  resolved_event_id: null
```

Possible operational effects:

- DELAY
- BERTH_CHANGE
- BOARDING_PAUSE
- SKIP_STOP
- SHORT_TURN
- SUBSTITUTE_VESSEL
- TRANSFER_TO_OTHER_SERVICE
- RETURN_TO_ORIGIN
- SAILING_CANCELLED
- SERVICE_SUSPENDED
- TEMPORARY_TERMINAL

These are options for canon authors, not universal operator powers.

## Vessel substitution

```yaml
vessel_assignment_event:
  event_id: null
  sailing_id: null
  previous_vessel_ref: null
  new_vessel_ref: null
  reason_refs: []
  effective_time: null
```

`VESSEL_CHANGED != SERVICE_CANCELLED`

`VESSEL_ASSIGNED != VESSEL_READY`

`VESSEL_READY != BERTH_READY`

`BERTH_READY != BOARDING_STARTED`

## Public information

Passenger knowledge should remain separate from operator truth.

```yaml
maritime_service_notice:
  notice_id: null
  service_id: null
  sailing_ids: []
  terminal_ids: []
  published_time: null
  valid_from: null
  valid_until: null
  stated_status: null
  source_refs: []
  correction_notice_ids: []
```

A notice can become stale without becoming fraudulent.

`NOTICE_PUBLISHED != PASSENGER_RECEIVED_NOTICE`

`NOTICE_SAYS_ON_TIME != SAILING_DEPARTED_ON_TIME`

`CORRECTION_PUBLISHED != EARLIER_NOTICE_ERASED`

## Maritime social continuity

Recurring ferries can become social places through:

- regular crew;
- commuters;
- island residents;
- merchants;
- researchers;
- couriers;
- students;
- performers;
- seasonal workers;
- known wild Pokémon near terminals;
- named partner Pokémon with authored work roles.

A recurring passenger can become recognizable without requiring a persistent journey object for every ordinary crossing.

## Port district continuity

A port district can contain independent systems:

- passenger terminal;
- cargo handling;
- market activity;
- shipyard/maintenance;
- public waterfront;
- transport interchange;
- coastal navigation aids;
- emergency/rescue facilities;
- warehouses;
- research or conservation access points.

A disruption in one scope should not automatically close the others.

## Ecology boundary

Maritime service can consume ecology facts such as nesting periods, recurring migration observations or habitat disturbance reports.

The service owner may alter operations when canon supports that decision.

It may not infer `species present => hazard`, `Water type => safe vessel escort`, `wild Pokémon nearby => service closure` or `successful crossing => no ecological impact`.

## Weather boundary

Weather can create operational dependencies and disruption causes.

This layer does not implement PTU Weather, waves, currents, wind push, visibility penalties or ship stability.

`WEATHER_WARNING != SAILING_CANCELLED`

`SAILING_CANCELLED_FOR_WEATHER != TERMINAL_CLOSED`

`WEATHER_ENDED != SERVICE_RESTORED`

## Search/rescue handoff

A passenger reconciliation may create an external handoff when world facts justify it.

This layer records:

- last confirmed service phase;
- last confirmed terminal/stop;
- count evidence;
- boarding/disembarkation evidence;
- known travel intention when privacy rules allow;
- handoff timestamp;
- receiving owner.

Crisis/Rescue decides search or rescue state.

## Strong invariants

`SEA_LANE_OPEN != FERRY_SERVICE_OPERATING`

`FERRY_SERVICE_OPERATING != EVERY_SAILING_OPERATING`

`TERMINAL_OPEN != EVERY_BERTH_AVAILABLE`

`BERTH_AVAILABLE != BOARDING_OPEN`

`BOOKING_EXISTS != PASSENGER_PRESENT`

`PASSENGER_PRESENT_AT_TERMINAL != BOARDED`

`BOARDED != DEPARTED`

`DEPARTED != ARRIVED`

`ARRIVED_AT_BERTH != DISEMBARKED`

`DISEMBARKED != REACHED_FINAL_NONMARITIME_DESTINATION`

`COUNT_MISMATCH != PERSON_MISSING`

`PERSON_UNACCOUNTED_FOR != PERSON_OVERBOARD`

`VESSEL_SUBSTITUTED != SERVICE_IDENTITY_CHANGED`

`DELAYED != CANCELLED`

`SKIP_STOP != WHOLE_ROUTE_CANCELLED`

`WEATHER_IMPROVED != SERVICE_RESTORED`

`BATTLE_WON != SAILING_SAFE`

`BATTLE_WON != PASSENGERS_ACCOUNTED_FOR`

`BATTLE_WON != VESSEL_DEPARTED`

## Battle integration rule

Routine transport state remains outside AutoPTU.

When a tactical incident intersects a maritime location, Ouros must select combatants and define the BattleSpec. Noncombatant passengers, crew not selected as combatants, operational records, controlled cargo and vessel-control semantics should remain outside the tactical engine unless exact contracts exist.

A battle result can feed a narrow world fact such as `immediate access to gangway restored` or `nearby threat defeated`.

The maritime owner separately evaluates whether boarding resumes, a sailing departs, a terminal reopens or reconciliation completes.

## Reduced encounter pattern

If rich maritime semantics are unavailable:

1. pause boarding, disembarkation or terminal service in world state;
2. remove ordinary passengers and noncombatant crew from BattleSpec;
3. secure or relocate records/cargo through nonbattle world state;
4. keep vessel-control state static;
5. provide AutoPTU with reviewed static geometry and explicit combatants;
6. resolve conventional combat;
7. hand the tactical outcome back to the maritime owner;
8. let that owner decide service continuation from world facts.

## Canon questions deliberately left open

Which Ouros regions use scheduled ferries?

Which ports and islands are connected?

Which institutions or businesses operate passenger services?

Which services carry cargo as well as passengers?

Which regions use tickets, passes, bookings, manifests or walk-up boarding?

What passenger information, if any, is retained?

What privacy rules apply?

Who may cancel, divert, short-turn or substitute a sailing?

How are vessel inspections and maintenance governed?

Which coastal communities depend heavily on maritime service?

Which crossings are routine enough to compress?

Which recurring crew, passengers and Pokémon are canon characters?

What historical route closures, shipyard changes, terminal relocations or service substitutions remain visible?

No answer is established by this extension.