# Ouros Road Passenger Transit, Taxis & Shuttles Layer

Status: Proposed systems design. Not established Ouros canon.
Date: 2026-08-23

## Purpose

This layer owns persistent road-based passenger transport inside and between settlements: buses, minibuses, taxis, shuttles, demand-responsive services, route stops, passenger queues, transfers and service disruptions.

It does not replace the generic Travel layer. Travel continues to own the world connection graph and journeys. This layer owns the operational state of road passenger services that use those connections.

It also does not replace Road Ecology, Infrastructure, Accessibility, Payments, Working Pokémon, Emergency Services or Demography.

Core principle:

A road can be open while the passenger service is unavailable. A service can be running while unreliable. A vehicle can exist while unavailable. A stop can exist while temporarily unusable. A passenger can hold a valid reservation while still failing to board because the assigned trip never arrived.

## 1. Service identity

```yaml
road_transit_service:
  service_id: null
  operator_id: null
  service_type: FIXED_ROUTE
  public_name: null
  route_pattern_ids: []
  service_area_ids: []
  vehicle_pool_ids: []
  working_pokemon_role_ids: []
  fare_policy_id: null
  accessibility_profile_id: null
  operating_calendar_id: null
  current_service_state: OPERATING
  public_information_ref: null
  history_refs: []
```

Candidate `service_type` values:

- FIXED_ROUTE
- CIRCULATOR
- SHUTTLE
- TAXI
- DEMAND_RESPONSIVE
- SCHOOL_OR_INSTITUTIONAL
- EVENT_ONLY
- REPLACEMENT_SERVICE
- EMERGENCY_ONLY

Service type does not define a mechanical vehicle class.

## 2. Route patterns and stops

```yaml
road_transit_route_pattern:
  pattern_id: null
  service_id: null
  revision_id: null
  stop_sequence: []
  connection_ids: []
  direction_label: null
  operating_window_ids: []
  schedule_mode: SCHEDULED
  planned_headway_band: null
  published_timetable_ref: null
  detour_policy_ref: null
  active_from: null
  active_until: null
```

A route pattern is versioned. If a bridge closure sends a bus through another district, create a detour revision instead of rewriting the historical route.

```yaml
road_transit_stop:
  stop_id: null
  location_id: null
  public_name: null
  boarding_area_ids: []
  accessibility_state_ref: null
  shelter_asset_ids: []
  signage_refs: []
  passenger_information_refs: []
  current_stop_state: OPEN
  service_pattern_ids: []
```

Candidate stop states:

- OPEN
- LIMITED
- TEMPORARILY_RELOCATED
- SKIPPED
- CLOSED
- DAMAGED
- ACCESS_RESTRICTED
- UNKNOWN

A stop being physically present in Minecraft does not prove it is currently served.

## 3. Trip instances

A published route is not the same as one actual run.

```yaml
road_transit_trip:
  trip_id: null
  service_id: null
  pattern_revision_id: null
  planned_start_time: null
  actual_start_time: null
  assigned_vehicle_id: null
  assigned_operator_ids: []
  assigned_working_pokemon_ids: []
  trip_state: PLANNED
  stop_event_ids: []
  disruption_ids: []
  passenger_load_band: null
  capacity_state: NORMAL
```

Suggested trip states:

- PLANNED
- BOARDING
- IN_SERVICE
- DELAYED
- SHORT_TURNED
- REROUTED
- TERMINATED_EARLY
- COMPLETED
- CANCELLED
- UNKNOWN

Historical trips should remain queryable when relevant to a case, missed connection, commute pattern or public-memory event.

## 4. Stops need actual events

```yaml
transit_stop_event:
  stop_event_id: null
  trip_id: null
  stop_id: null
  scheduled_arrival: null
  observed_arrival: null
  scheduled_departure: null
  observed_departure: null
  boarding_band: null
  alighting_band: null
  pass_up_count_band: null
  stop_skipped: false
  observation_sources: []
```

The system does not need exact passenger counts for routine background traffic. Use qualitative bands unless a specific story, capacity decision or research project needs exact measurement.

## 5. Service reliability

A service-state revision can summarize delivered performance without turning the world into a transit-management simulator.

```yaml
transit_reliability_revision:
  revision_id: null
  service_id: null
  scope: null
  time_window: null
  planned_service_band: null
  delivered_service_band: null
  spacing_state: NORMAL
  crowding_state: NORMAL
  missed_trip_refs: []
  disruption_refs: []
  observation_sources: []
  interpretation_refs: []
```

Candidate `spacing_state`:

- EVEN
- IRREGULAR
- BUNCHING_OBSERVED
- LARGE_GAPS
- UNKNOWN

Candidate `crowding_state`:

- LIGHT
- NORMAL
- BUSY
- CAPACITY_PRESSURE
- PASS_UPS_OBSERVED
- UNKNOWN

Do not infer one from the other automatically.

## 6. Passenger request and taxi/demand-responsive state

```yaml
road_trip_request:
  request_id: null
  requester_id: null
  service_id: null
  requested_origin: null
  requested_destination: null
  requested_time_window: null
  accommodation_refs: []
  party_size_band: null
  request_state: REQUESTED
  assignment_id: null
  price_quote_ref: null
  payment_ref: null
```

Suggested states:

- REQUESTED
- ACCEPTED
- WAITLISTED
- ASSIGNED
- VEHICLE_EN_ROUTE
- PICKUP_READY
- BOARDED
- COMPLETED
- CANCELLED
- NO_SHOW
- UNFULFILLED

A taxi request being accepted does not mean the passenger has boarded. A vehicle being nearby in Minecraft does not prove it is assigned to that request.

## 7. Transfers

```yaml
transit_transfer:
  transfer_id: null
  actor_ids: []
  inbound_trip_id: null
  outbound_trip_id: null
  transfer_location_id: null
  planned_connection_window: null
  actual_connection_state: UNKNOWN
  accommodation_refs: []
  reroute_option_refs: []
```

Suggested connection states:

- MADE
- MISSED
- HELD_CONNECTION
- REBOOKED
- ALTERNATE_ROUTE_USED
- STRANDED
- UNKNOWN

A missed transfer can create downstream consequences without combat: late arrival, missed appointment, changed hotel reservation, cargo mismatch, missed ceremony or lost observation window.

## 8. Disruptions

```yaml
road_transit_disruption:
  disruption_id: null
  service_id: null
  affected_pattern_ids: []
  affected_stop_ids: []
  start_event_id: null
  cause_refs: []
  verified_cause_state: null
  operational_effects: []
  public_notice_refs: []
  mitigation_refs: []
  recovery_state: ACTIVE
```

Potential causes belong to other authoritative layers:

- Road Infrastructure / Road Ecology: closure or crossing issue;
- Meteorology / Crisis: storm, flooding or fire response;
- Working Pokémon: assigned service partner unavailable;
- Workplaces: staffing gap;
- Technology/Energy: charging, fueling or power issue;
- Supply Chains: spare-parts shortage;
- Public Events: temporary street use;
- Urban Wildlife: animals occupying a boarding area;
- Payments: fare system unavailable while service continues through fallback policy.

A disruption record links those facts. It does not invent them.

## 9. Vehicle state

Vehicle physics remain outside narrative authority, but vehicle identity can persist.

```yaml
road_transit_vehicle:
  vehicle_id: null
  operator_id: null
  vehicle_class_label: null
  passenger_capacity_band: null
  accessibility_features: []
  assigned_service_ids: []
  current_operational_state: AVAILABLE
  maintenance_refs: []
  location_ref: null
  history_refs: []
```

Possible states:

- AVAILABLE
- ASSIGNED
- IN_SERVICE
- OUT_OF_SERVICE
- MAINTENANCE
- INSPECTION
- RESERVE
- RETIRED

Do not derive collision damage, speed, armor, initiative or tactical cover from this record.

## 10. Pokémon-operated or Pokémon-assisted transport

Any Pokémon involved in a passenger service must retain its persistent Pokémon identity and route through Working Pokémon + Pokémon Agency.

Possible narrative roles:

- pulling a licensed carriage where canon supports it;
- carrying passengers in a specifically authored service where capability is validated;
- assisting boarding or route operations;
- navigation support;
- station assistance;
- emergency replacement service.

Never infer from species alone:

- carrying capacity;
- Mountable legality;
- working hours;
- willingness;
- battle command authority;
- immunity to traffic or weather;
- passenger safety.

A service partner can be resting, reassigned, refusing, retired or unavailable while the service institution persists.

## 11. Accessibility boundary

Accessibility remains owned by the Accessibility layer.

Transit can reference:

- boarding accessibility;
- stop access route;
- vehicle feature availability;
- demand-responsive accommodation;
- temporary relocated-stop impact;
- communication/support needs.

Do not infer disability or private health information from use of an accessible service.

## 12. Passenger knowledge

```yaml
transit_information_state:
  actor_id: null
  service_id: null
  known_route_revision_id: null
  known_disruption_ids: []
  source_refs: []
  observed_at: null
  confidence: null
```

A detour can exist before every actor learns it. Public information, delivery and actor knowledge remain separate.

## 13. Routine compression

Routine trips should normally compress into a result such as:

- trip completed;
- expected duration band;
- fare/payment result if relevant;
- notable co-presence only when meaningful;
- transfer result;
- service disruption encountered if any.

Expand a journey only when it creates a meaningful decision:

- route closes;
- connection is at risk;
- capacity prevents boarding;
- player chooses whether to wait or reroute;
- a recurring NPC is encountered;
- a service worker needs help;
- wildlife or a case intersects the route;
- an accessibility accommodation changes the viable options;
- the player is investigating the transit system itself.

## 14. Minecraft projection

Minecraft may render:

- buses/taxis/shuttles or abstract stand-ins;
- stops, shelters, signs and ranks;
- queues and passenger cohorts;
- detours;
- closed stops;
- service notices;
- working Pokémon associated with a service;
- parked reserve vehicles.

Minecraft must not decide:

- trip legality;
- who is assigned to a vehicle;
- fare settlement;
- passenger eligibility;
- service reliability;
- capacity truth;
- whether a stop is officially served;
- whether a Pokémon can legally carry a passenger;
- mechanical collision or traffic rules.

## 15. Battle handoff

Road transit should normally resolve outside battle.

If conflict occurs, the world state should first freeze or evacuate noncombat vehicles/passengers when possible.

FULL encounter versions may eventually require:

- moving passengers or vehicles;
- protected boarding lanes;
- intercepting an actor before departure;
- clearing a route under pressure;
- timed connection objectives;
- moving service assets.

Those depend on complete movement, tactical AI and adapter/playback. Any road hazard also depends on exact terrain/hazard support.

REDUCED versions preserve the premise by stopping the service, evacuating passengers, freezing the vehicle and opening a static legal battle arena.

## 16. Anti-inference rules

Never infer:

- road open -> bus running;
- bus visible -> trip available;
- stop sign -> current service;
- timetable -> trip actually ran;
- delayed trip -> negligence;
- crowded stop -> population growth;
- driver -> Trainer Feature;
- vehicle -> tactical Item;
- taxi ride -> private relationship with driver;
- ride with another NPC -> friendship/romance;
- service animal/Pokémon -> ownership by operator;
- route used frequently -> public right-of-way unless Land Tenure says so;
- battle victory -> route restored.

## 17. Canon questions

Before promotion to canon, decide:

- which settlements have road passenger transport;
- whether services are public, cooperative, private or mixed;
- which cities have taxis versus fixed-route services;
- whether Pokémon-assisted urban transport exists and under what validated capabilities;
- how fares interact with the Ouros currency system;
- what accessibility guarantees institutions promise;
- whether player organizations can operate services;
- how exact schedules need to be;
- which data is stored exactly and which remains qualitative;
- whether vehicles themselves ever enter tactical battle space.
