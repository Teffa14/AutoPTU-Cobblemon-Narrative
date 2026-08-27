# Service Access, Queues & Appointments Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already has persistent services, facilities, transport, events, battle institutions, libraries, shared equipment, workplaces and public notices. Those systems can say that a service exists and whether it is operating. This extension models the access lifecycle between that service and the actor trying to use it.

It covers requests, registrations, appointment windows, walk-ins, waiting, check-in, calls, service start, completion, cancellation, rescheduling, no-shows, referral and capacity handoffs.

It does not create a universal ticketing system, bureaucracy, triage algorithm, identity document, fee schedule or right of access.

## 1. Authority boundaries

### The owning service keeps domain authority

Pass 70 coordinates access. It never decides the underlying service result.

Examples:

- Care decides medical urgency, treatment legality, readiness and clinical capacity.
- Travel/Transit decides departures, vehicle/service capacity, boarding and route state.
- Storefront decides whether a commercial service is offered and currently available.
- Battle Institutions decides challenge eligibility, format, roster legality and battle authority.
- Event Operations decides event/activity state and site readiness.
- Workplaces decides staffing, shifts, qualifications and assignments.
- Education decides instructional eligibility and course/session content.
- Science decides research access requirements where established.
- Civic Governance decides public-service policy where established.

Pass 70 may read an owning state and record its effect on access. It cannot manufacture that state.

### Specialized reservations remain specialized

- Shared Equipment owns exact-asset reservations and checkout.
- Libraries owns copy reservations and circulation.
- Housing owns residential occupancy.
- Courier owns intentional shipments.

A service appointment may reference one of those records. It does not replace it.

### Public Notices and Communications project information

Pass 70 can produce schedule/cancellation/ready-for-service events. Public Notices decides how a published schedule appears physically. Communications owns messages and delivery state.

### Observation/Time owns the clock

Waiting, appointment windows and deadlines must use the existing world clock. Pass 70 must not invent a second timeline.

## 2. Service access channel

One underlying service may expose several access channels.

```yaml
service_access_channel:
  channel_id: null
  owning_layer: null
  owning_service_ref: null
  location_id: null
  service_point_ref: null
  channel_type: WALK_IN
  access_policy_ref: null
  eligibility_policy_ref: null
  capacity_state_ref: null
  schedule_ref: null
  published_schedule_ref: null
  current_state: OPEN
  temporary_relocation_ref: null
  queue_model: NONE
  notes: null
```

Candidate `channel_type` values:

- WALK_IN
- APPOINTMENT
- REGISTRATION
- CALLBACK
- REFERRAL
- SESSION
- REMOTE_REQUEST
- CHECK_IN_ONLY

Candidate channel states:

- PLANNED
- OPEN
- LIMITED
- PAUSED
- CLOSED
- RELOCATED
- SUSPENDED
- RETIRED

`OPEN` means the access channel is operating. It does not guarantee that a requested service can start immediately.

## 3. Service access request

A request says that an actor or group wants access to a service.

```yaml
service_access_request:
  request_id: null
  channel_id: null
  requester_actor_id: null
  requester_group_id: null
  requested_for_actor_ids: []
  purpose_ref: null
  requested_window_ref: null
  submitted_at: null
  eligibility_check_ref: null
  eligibility_state: UNKNOWN
  priority_claim_ref: null
  priority_decision_ref: null
  assigned_slot_id: null
  queue_entry_id: null
  referral_ref: null
  current_state: REQUESTED
  history_event_ids: []
```

Suggested states:

- REQUESTED
- NEEDS_INFORMATION
- ELIGIBILITY_PENDING
- ELIGIBLE
- INELIGIBLE
- WAITLISTED
- OFFERED_SLOT
- CONFIRMED
- CHECKED_IN
- CALLED
- IN_SERVICE
- COMPLETED
- REFERRED
- RESCHEDULE_REQUIRED
- CANCELLED_BY_REQUESTER
- CANCELLED_BY_SERVICE
- NO_SHOW_RECORDED
- EXPIRED
- WITHDRAWN

An `INELIGIBLE` state must point to an owning rule or decision. Pass 70 cannot create one.

## 4. Service slot

A slot is a bounded opportunity for a service to begin or run.

```yaml
service_slot:
  slot_id: null
  channel_id: null
  start_at: null
  end_at: null
  service_capacity_ref: null
  capacity_units: null
  allocation_ids: []
  location_id: null
  service_point_ref: null
  staff_assignment_refs: []
  dependency_refs: []
  state: PLANNED
  history_event_ids: []
```

Suggested states:

- PLANNED
- OPEN_FOR_REQUESTS
- HELD
- PARTIALLY_ALLOCATED
- FULL
- CHECK_IN_OPEN
- ACTIVE
- COMPLETED
- DELAYED
- PAUSED
- CANCELLED
- RELOCATED

`capacity_units` should exist only when the owning system defines a meaningful unit. Never assume that one person always equals one unit.

## 5. Slot allocation

```yaml
service_slot_allocation:
  allocation_id: null
  slot_id: null
  request_id: null
  actor_ids: []
  group_id: null
  allocated_at: null
  allocation_source: null
  priority_decision_ref: null
  confirmation_state: OFFERED
  confirmed_at: null
  released_at: null
```

Candidate confirmation states:

- OFFERED
- CONFIRMED
- DECLINED
- EXPIRED
- RELEASED
- TRANSFERRED_BY_POLICY

A slot allocation does not authorize transfer to another actor unless an owning policy explicitly allows it.

## 6. Walk-in queue entry

Queues should model access demand, not ownership of people.

```yaml
service_queue_entry:
  queue_entry_id: null
  request_id: null
  channel_id: null
  actor_ids: []
  group_id: null
  joined_at: null
  checked_in_at: null
  queue_class_ref: null
  priority_claim_ref: null
  priority_decision_ref: null
  current_position_band: null
  wait_estimate_id: null
  current_state: WAITING
  left_queue_at: null
  history_event_ids: []
```

Suggested states:

- WAITING
- TEMPORARILY_AWAY
- READY_TO_CALL
- CALLED
- SERVING
- COMPLETED
- LEFT
- REFERRED
- CANCELLED
- INVALIDATED

Avoid persisting exact numeric position unless the real access process exposes it. A qualitative band can often be enough:

- NEXT
- SOON
- MIDDLE
- LATER
- UNKNOWN

## 7. Priority provenance

Priority must never come from a hidden narrative score.

```yaml
service_priority_decision:
  priority_decision_id: null
  request_id: null
  channel_id: null
  policy_ref: null
  decision_actor_id: null
  decision_institution_id: null
  source_facts_refs: []
  resulting_queue_class_ref: null
  resulting_slot_ref: null
  decided_at: null
  public_explanation_ref: null
```

Pass 70 may store a result supplied by Care, an institution or an explicit policy.

It may not infer priority from:

- protagonist status;
- wealth;
- reputation;
- Trainer class;
- Pokémon species or rarity;
- friendship with staff;
- quest importance;
- player impatience.

If observers believe a priority choice was unfair, that belief belongs in Rumor/Testimony or Social state. It does not rewrite the actual decision provenance.

## 8. Wait estimate

An estimate is a forecast.

```yaml
service_wait_estimate:
  estimate_id: null
  channel_id: null
  queue_entry_id: null
  request_id: null
  generated_at: null
  estimated_start_window: null
  basis_refs: []
  confidence: null
  supersedes_estimate_id: null
  current_state: CURRENT
```

Candidate states:

- CURRENT
- SUPERSEDED
- INVALIDATED
- FULFILLED

A later estimate must not erase the earlier one. Actor knowledge may depend on which estimate the actor actually saw.

## 9. Check-in and service events

```yaml
service_access_event:
  access_event_id: null
  channel_id: null
  request_id: null
  slot_id: null
  queue_entry_id: null
  event_type: CHECKED_IN
  occurred_at: null
  actor_ids: []
  operator_actor_id: null
  location_id: null
  source_state_refs: []
  notes: null
```

Useful event types:

- REQUEST_SUBMITTED
- INFORMATION_REQUESTED
- ELIGIBILITY_CONFIRMED
- ELIGIBILITY_DENIED
- WAITLISTED
- SLOT_OFFERED
- SLOT_CONFIRMED
- QUEUE_JOINED
- CHECKED_IN
- CALLED
- SERVICE_STARTED
- SERVICE_PAUSED
- SERVICE_RESUMED
- SERVICE_COMPLETED
- REFERRAL_CREATED
- RESCHEDULE_REQUESTED
- RESCHEDULED
- CANCELLED_BY_REQUESTER
- CANCELLED_BY_SERVICE
- NO_SHOW_RECORDED
- TEMPORARY_RELOCATION

Use timestamps from world time, not real-world UI time.

## 10. No-shows and missed access

A missed slot is an observation about the access event, not a moral judgment.

A no-show record may coexist with:

- route closure;
- incorrect published schedule;
- care emergency;
- communications failure;
- actor misunderstanding;
- deliberate withdrawal;
- unknown cause.

Do not infer negligence, disrespect or unreliability from `NO_SHOW_RECORDED` alone.

If the owning service has a consequence policy, reference it explicitly.

## 11. Cancellation and rescheduling

A cancellation needs provenance.

Possible causes may reference:

- staff unavailable;
- service dependency unavailable;
- room/facility issue;
- transport interruption;
- weather preparedness decision;
- event pause;
- actor withdrawal;
- unknown or private reason.

Pass 70 records the access consequence. It does not invent the underlying reason.

Rescheduling should create a new slot/allocation relation while preserving the old event history.

## 12. Referral and callback

A referral is not a completed service.

```yaml
service_referral:
  referral_id: null
  source_service_ref: null
  source_request_id: null
  target_service_ref: null
  target_channel_id: null
  created_at: null
  reason_ref: null
  owning_decision_ref: null
  information_packet_ref: null
  state: CREATED
```

Candidate states:

- CREATED
- SENT
- RECEIVED
- REQUESTED
- ACCEPTED
- DECLINED
- EXPIRED
- COMPLETED

Clinical referrals remain under Care for medical meaning. Pass 70 only supports the access handoff.

## 13. Capacity handoff

The access layer should consume capacity rather than calculate it.

```yaml
service_capacity_handoff:
  handoff_id: null
  channel_id: null
  owning_layer: null
  owning_capacity_ref: null
  observed_at: null
  access_effect: NORMAL
  max_new_allocations_ref: null
  pause_new_requests: false
  expected_review_at: null
```

Candidate access effects:

- NORMAL
- REDUCED
- WALK_INS_PAUSED
- APPOINTMENTS_ONLY
- REFERRAL_ONLY
- CHECK_IN_PAUSED
- NO_NEW_ACCESS
- UNKNOWN

The owning layer remains authoritative for why capacity changed.

## 14. Group and cohort handling

Large waiting populations should be represented economically.

Use persistent individual actors only when they matter as:

- rivals;
- contacts;
- witnesses;
- specialists;
- recurring regulars;
- parties tied to another persistent record.

Everyone else can remain in aggregate queue/cohort state.

Minecraft should not need one entity per waiting person to preserve demand.

## 15. Waiting as world time

Waiting can be compressed when no meaningful decision exists.

When the player chooses to wait, other systems may advance through the existing world clock:

- a departure leaves;
- weather changes;
- a shop closes;
- a rival arrives or departs;
- a public notice updates;
- a staff shift changes;
- an event phase advances;
- a request expires if an established rule says so.

Pass 70 does not invent those consequences. It allows their existing clocks to continue.

## 16. Player-facing information

Useful visible states can include:

- request received;
- eligibility pending;
- waitlisted;
- confirmed window;
- checked in;
- estimated wait;
- delayed;
- called;
- relocated;
- cancelled;
- referral available.

Avoid exposing hidden priority logic, private diagnoses, staff-only reasons or other actors' private records unless an information system grants access.

## 17. Minecraft materialization

Near-term safe representation:

- a service desk or interaction point;
- a small set of story-relevant waiting NPCs;
- aggregate demand in UI/world state;
- signage projected from Public Notices;
- location/room overlays from the owning service;
- explicit check-in/call interactions.

The final adapter must preserve separation between:

1. visual presence;
2. access state;
3. service authority;
4. tactical battle state.

Moving an NPC in Minecraft must not silently reorder a queue. Breaking a sign must not cancel appointments. Entering a room must not count as check-in unless the authoritative interaction occurs.

## 18. Battle handoff

Some services lead directly into battle, such as formal challenges. The access layer ends where the battle contract begins.

Safe sequence:

`request -> eligibility result -> slot/queue -> check-in -> called -> owning battle institution creates legal BattleSpec -> AutoPTU -> BattleTranscript -> owning institution records result -> Pass 70 records service completion/next access state`

Pass 70 must never construct PTU legality from appointment data alone.

## 19. Encounter pattern — Registration Hall Evacuation

Narrative premise:

A venue has several challengers or participants checked in when a battle-capable threat makes the public registration area unsafe.

Intended full version may require:

- moving noncombatants;
- multiple exits;
- PROTECT/WITHDRAW/CLEAR_ROUTE objectives;
- interception or forced displacement;
- changing safe zones;
- hazards or reactions if rules-mapped;
- AI that values evacuation/access rather than KO only;
- synchronized playback between queue state and world positions.

Permanent capability dependencies:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate all queued noncombatants through world state first. Preserve requests, check-ins and allocations. Freeze a static reviewed arena away from desks and access controls. Run a standard encounter using only individually verified mechanics. After the authoritative result, the venue owner decides reopening; Pass 70 then reschedules or restores access from that owning state.

Battle victory cannot automatically mark every appointment completed, restore capacity or decide who receives priority afterward.

## 20. Encounter pattern — Mobile Service Stop Interrupted

Narrative premise:

A recurring mobile service has a small set of appointments plus walk-ins when a local threat interrupts access before the session finishes.

Intended full version may require:

- civilians/clients withdrawing;
- a mobile facility or service point;
- protection or clear-route objectives;
- terrain/weather if governing mapping exists;
- interception/forced movement;
- objective-aware opponents;
- adapter playback preserving who had started service and who was still waiting.

Capability state is the same permanent map as above. Any active weather, terrain, hazards, forced movement, reactions or tactical objective policy remains BLOCKING.

Reduced version:

Move all clients and staff out of the tactical grid first. Preserve `IN_SERVICE`, `CHECKED_IN` and `WAITING` records separately. Resolve a static battle. The owning service then decides whether unfinished sessions resume, refer or reschedule. Pass 70 only records the resulting access transitions.

For a care service, the battle result cannot determine treatment priority or medical readiness.

## 21. Noncombat pattern — Two Names, One Slot

Two records appear to occupy the same appointment window. Investigation uses:

- request timestamps;
- allocation history;
- reschedule events;
- group/proxy relationships if canon supports them;
- communications receipts;
- staff handoff notes;
- published versus internal schedule versions.

Possible resolution may be clerical duplication, a stale allocation, legitimate group booking, an unrecorded reschedule or insufficient evidence. Fraud is never the default explanation.

This can run entirely in narrative state before new tactical capabilities exist.

## 22. Persistent arc — A Service Learns Its Regulars

A recurring service develops continuity across visits:

1. baseline channel, schedule and demand become legible;
2. several actors become recurring users because they matter to stories;
3. a capacity change causes visible but policy-grounded adjustments;
4. one temporary workaround creates a different waiting pattern;
5. the service later restores or changes its routine;
6. prior appointments, delays and corrections remain in history.

Regular use does not create hidden reputation priority. Any preferential access must have explicit canon policy or decision provenance.

## 23. Canon questions left open

Pass 70 does not decide:

- which Ouros services accept appointments;
- which allow walk-ins;
- whether numbered tickets exist;
- whether booking is paper, phone, digital or in-person;
- what identity verification exists;
- whether transfers/proxies are allowed;
- what cancellation/no-show consequences exist;
- whether wait estimates are publicly shown;
- what services use formal priority rules;
- what privacy applies to waiting lists;
- how much queue state should appear physically in Cobblemon.

All of those require canon or owning-system decisions.