# Ouros Aerial Ropeway / Cable-Car Service Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until approved.
Date: 2026-08-29

## Purpose

This extension models the operating continuity of authored exterior cable-supported passenger transport connecting separately authored destinations. Candidate technologies such as cable cars, gondolas, aerial trams or other ropeways exist only when future canon explicitly chooses them.

Travel keeps authority over journeys and connection graphs. Transit Hubs keeps passenger-group continuity. Vertical Circulation keeps building lifts. Facility Maintenance owns faults, repair and verification. Infrastructure Outage owns upstream dependencies. Weather owns weather observations and forecasts. Crisis/Rescue owns rescue and evacuation. Accessibility owns actor-specific route viability. AutoPTU owns battle truth. Minecraft/Cobblemon/Craftics presents and replays authoritative state.

## Core records

```yaml
aerial_ropeway_system:
  system_id: null
  authored_kind: null
  operator_ref: null
  line_ids: []
  station_ids: []
  dependency_refs: []
  maintenance_refs: []
  public_information_refs: []
  legacy_event_ids: []
  canon_reference_ids: []
```

```yaml
aerial_ropeway_line:
  line_id: null
  system_id: null
  endpoint_station_ids: []
  served_connection_ids: []
  authored_span_refs: []
  carrier_ids: []
  current_service_state: UNKNOWN
  active_restriction_ids: []
  active_interruption_ids: []
  alternate_route_refs: []
  last_verified_service_event_id: null
```

Suggested narrative service states are UNKNOWN, OPERATING, LIMITED, SUSPENDED, UNDER_WORK, TESTING, RETURNING_TO_SERVICE and DECOMMISSIONED. These are operational labels, not engineering certifications.

```yaml
aerial_ropeway_station:
  station_id: null
  line_id: null
  location_id: null
  access_route_refs: []
  boarding_area_ref: null
  destination_access_ref: null
  accessibility_refs: []
  current_station_state: UNKNOWN
  display_name_refs: []
  history_event_ids: []
```

A station may be open as a place while boarding is unavailable. A line may operate while the area beyond one station has its own restriction.

```yaml
aerial_ropeway_carrier:
  carrier_id: null
  line_id: null
  authored_carrier_kind: null
  operational_state: UNKNOWN
  current_trip_id: null
  current_station_ref: null
  maintenance_asset_ref: null
  last_verified_at: null
```

No continuous position, speed or cable simulation is implied.

## Trip continuity

```yaml
aerial_ropeway_trip:
  trip_id: null
  line_id: null
  carrier_id: null
  origin_station_id: null
  destination_station_id: null
  passenger_cohort_refs: []
  journey_refs: []
  boarding_started_at: null
  boarding_completed_at: null
  departure_at: null
  arrival_at: null
  alighting_completed_at: null
  current_state: PLANNED
  interruption_ref: null
```

Useful narrative states are PLANNED, AT_ORIGIN, BOARDING, BOARDED, IN_TRANSIT, ARRIVED, ALIGHTING, COMPLETED, INTERRUPTED, ABORTED and CANCELLED.

`PASSENGER_BOARDED` and `TRIP_DEPARTED` remain separate facts. `CARRIER_ARRIVED` and `PASSENGER_ALIGHTED` remain separate facts.

## Permanent state separations

`STATION_OPEN != LINE_OPERATING`

`POWER_AVAILABLE != LINE_OPERATING`

`WEATHER_OBSERVED != SERVICE_SUSPENDED`

`FAULT_REPAIRED != SERVICE_VERIFIED`

`SERVICE_VERIFIED != FULL_SERVICE_RESTORED`

`CARRIER_AT_STATION != BOARDING_AUTHORIZED`

`PASSENGER_BOARDED != TRIP_DEPARTED`

`TRIP_INTERRUPTED != RESCUE_REQUIRED`

`RESCUE_REQUESTED != EVACUATION_STARTED`

`EVACUATION_COMPLETE != LINE_REOPENED`

`UPPER_STATION_OPEN != SUMMIT_ROUTE_OPEN`

`LINE_REOPENED != ALTERNATE_ROUTE_CLOSED`

`PUBLIC_NOTICE_ISSUED != NOTICE_RECEIVED_BY_EVERY_ACTOR`

These distinctions prevent presentation, rumor or one subsystem from silently deciding another subsystem's truth.

## Service restriction

```yaml
aerial_ropeway_service_restriction:
  restriction_id: null
  line_id: null
  affected_station_ids: []
  affected_carrier_ids: []
  restriction_scope: authored
  reason_claim_refs: []
  authority_ref: null
  effective_from: null
  expected_review_ref: null
  ended_at: null
  status: ACTIVE
```

Possible scopes include whole-line suspension, reduced carrier availability, station boarding restriction, destination restriction and scheduled limited service. Exact triggers remain authored or supplied by governing systems.

Weather can provide observations and forecasts. The ropeway operator or other approved authority records the service decision. Weather state never flips ropeway state automatically unless future canon defines that explicit automation.

## Trip interruption and stranded state

```yaml
aerial_ropeway_trip_interruption:
  interruption_id: null
  trip_id: null
  first_observed_at: null
  observation_refs: []
  suspected_cause_claim_refs: []
  confirmed_cause_claim_refs: []
  carrier_state_ref: null
  passenger_state_refs: []
  operator_response_refs: []
  rescue_handoff_ref: null
  maintenance_handoff_ref: null
  current_status: OPEN
```

A stopped carrier does not automatically mean passengers are injured, exposed, falling, trapped in a mechanically meaningful sense or in need of evacuation. Those facts need separate evidence.

Crisis/Rescue owns any rescue operation. Facility Maintenance owns technical diagnosis and repair. Care owns medical state. This extension only preserves the interruption and the handoffs.

## Restart verification

```yaml
aerial_ropeway_restart_record:
  restart_id: null
  line_id: null
  dependency_restoration_refs: []
  maintenance_verification_refs: []
  operator_review_refs: []
  service_test_refs: []
  resulting_service_state: null
  effective_at: null
```

Returning an upstream dependency or finishing a repair may lead to TESTING or LIMITED service rather than immediate normal operation.

## Alternate-route handoff

```yaml
aerial_ropeway_alternate_route_handoff:
  handoff_id: null
  line_id: null
  affected_connection_ids: []
  alternate_connection_refs: []
  travel_owner_action_required: true
  accessibility_owner_action_required: true
  effective_from: null
  ended_at: null
```

Travel decides which alternatives are viable. Accessibility decides whether those alternatives work for a specific actor. A steep trail does not become an acceptable replacement simply because it exists.

Temporary shuttles, walking routes, service roads or other modes require separate canon support and their own operating owners.

## Public information and knowledge

```yaml
aerial_ropeway_notice:
  notice_id: null
  line_id: null
  issuer_ref: null
  issued_at: null
  effective_scope: null
  source_state_refs: []
  message_version: null
  supersedes_notice_ref: null
```

Actor knowledge should track source, timestamp and freshness. A traveler may remember the morning closure while another has a later reopening notice. Neither memory changes world truth.

## Persistent history and renamed infrastructure

Stable line, station and location IDs survive display-name changes, operator changes, renovation or decommissioning. Old tickets, photographs, trail maps and maintenance records can therefore refer to the same infrastructure under different names.

A retired lower station can remain a social landmark. An alternate trail created during a long suspension can remain popular after the line returns. A temporary shuttle stop can become a market corner. Recovery need not reset the region to its previous social graph.

## Pokémon participation boundary

Do not infer line operation from Electric typing, cable repair from Steel typing, wind prediction from Flying typing, safe aerial rescue from Levitate, passenger carrying from body size, or fall immunity from species flavor.

An individual Pokémon can have an authored trained role, history or observed behavior. Mechanically relevant effects require an exact governing capability, Move, Ability, Item, Trainer Feature/perk or setting rule.

## Minecraft/Cobblemon/Craftics boundary

Safe presentation includes stations, cabins, cables/support structures, ticket or notice UI, barriers, queues, operator NPCs, individual Pokémon, sounds, particles, lighting, static or cinematic carrier movement and persistent closed/limited/open visual states.

Minecraft movement never becomes PTU movement authority. A moving entity does not prove trip completion. Redstone does not prove service readiness. Native fall damage does not substitute for AutoPTU damage. Wind particles do not create forced movement. Entity collision does not create cable-car collision rules. Cobblemon BattleState never chooses combatants, legality, HP/status, tactical positions or outcomes.

## Encounter contract: Lower Station Withdrawal

Narrative premise: a localized conflict threatens a station while travelers need to clear the boarding area or reach an already verified alternate route.

Full version dependencies: targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle if departure or withdrawal windows matter; full stateful damage pipeline; status lifecycle when legal effects apply; terrain/weather/hazards/zones/reactions if gates or protected corridors change; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy for PROTECT/WITHDRAW; Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version: all civilians complete withdrawal before BattleSpec creation. The carrier, cable and boarding machinery are inert or outside the grid. AutoPTU receives a static station apron with explicit combatants. Victory can record `IMMEDIATE_STATION_PERIMETER_SECURED`; it cannot reopen service or complete a journey.

## Encounter contract: Interrupted-Line Rescue Staging

Narrative premise: a service interruption has already occurred and a conflict threatens a stable rescue-staging area used by responders.

Full version becomes highly demanding if combat occurs on or around a moving/suspended carrier: complete movement, generalized reactions, moving hazards/zones, fall or environmental damage, phased lifecycle, rescue/protection policy and semantic playback all become direct dependencies.

Reduced version: passengers have already been moved by authoritative world-state resolution to a stable authored platform, station or cleared staging area before battle. The suspended carrier remains scenery outside tactical reach. Resolve a conventional static encounter protecting the staging perimeter. Crisis/Rescue continues to own the rescue outcome.

## Encounter contract: Summit Diversion Junction

Narrative premise: the line is suspended and travelers are using a verified alternate connection near the upper station when a conflict blocks the junction.

Full version may need objective-aware protection/withdrawal, Intercept/forced movement, generalized reactions, weather/environmental zones and semantic playback.

Reduced version: complete civilian rerouting first. Resolve the conflict on a static junction. Travel and Accessibility remain authoritative for whether the alternate route actually works for each actor.

## Noncombat exploration: The Station Above the Old Road

A mountain transport line was rebuilt, renamed or partially relocated. Historical route maps, old station photographs, operator records, retired signs and resident memories describe apparently different systems. Players map historical names to stable station/connection IDs and discover how an older walking road became socially important during a long closure.

This can run with current capabilities because all relevant geometry is static and the puzzle is provenance-based.

## Long-term arc: A Mountain Learns Two Ways Up

Begin with ordinary commuters, hikers, workers, vendors and visitors using both the ropeway and older ground routes. A limited suspension changes traffic and creates temporary practices. Recovery proceeds through repair, verification and staged service. Some temporary routes, businesses and relationships persist. A later interruption or historical investigation reuses those accumulated facts rather than resetting the mountain.

No scalar `ropeway_recovery_level` is required.

## Canon safeguards

Remain UNKNOWN until approved or sourced: exact ropeway technology; engineering layout; travel time; capacity; fares; operating schedule; weather limits; inspection jurisdiction; emergency procedure; rescue equipment; fall rules; cabin combat; passenger carrying; cable traversal; maintenance standards; occupational roles; species-specific advantages; Move/Ability/Item/Trainer Feature interactions.

The architecture is ready to preserve such facts later without inventing them now.