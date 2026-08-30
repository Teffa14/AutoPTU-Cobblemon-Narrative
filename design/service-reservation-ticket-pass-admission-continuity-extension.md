# Service Reservation, Ticket, Pass & Admission Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension models bounded rights to use a service, attend an activity or enter a controlled service scope when an authored institution uses reservations, tickets, passes or comparable records.

It provides continuity between issuance and use without replacing payment, queues, credentials, transport operations, event operations, identity, Material Culture or PTU mechanics.

The extension is intentionally optional. A village ferry may board people without tickets. A public event may use open admission. A local shuttle may require only a recurring pass. Another service may use reservations without any visible ticket. The owning institution decides which model exists.

## 1. Authority boundaries

### Service owners retain operational authority

Transport decides whether a train, ferry, flight, road service, ropeway or other service operates.

Event Operations decides whether an event or activity is active, delayed, relocated, restricted or canceled.

Battle Institutions decides challenge eligibility, battle format, roster legality and battle authority.

Education decides course/session eligibility and instructional completion.

Libraries retain copy-level circulation and library-specific reservations.

Shared Equipment retains exact-asset reservation and checkout.

Hospitality retains room/stay allocation when its own specialized model applies.

This extension may reference those states. It cannot create them.

### Service Access owns queues and appointments

A reservation can produce or reference a Service Access slot allocation. Queue position, appointment check-in and entitlement validity remain separate.

### Credentials owns institutional authority

A professional badge, permit, certification or role authorization belongs to Credentials. An admission ticket does not grant professional authority.

A service can require both.

### Finance owns money movement

Purchase, deposit, refund, credit, reversal and other monetary events remain Finance or the relevant mechanical-money implementation.

This layer can record the commercial reason for an entitlement and reference a payment event.

It must not silently mutate balances.

### Human Identity owns actor linkage

If an entitlement is identity-bound, Human Identity supplies the actor reference. This layer does not create universal identity documents or identity-verification rules.

### Material Culture owns physical carriers

Paper tickets, cards, tokens, wristbands and devices can be physical artifacts. Material Culture owns their object provenance and custody. This layer owns only the service-entitlement relationship represented by them.

## 2. Core service entitlement

```yaml
service_entitlement:
  entitlement_id: null
  issuer_id: null
  owning_layer: null
  owning_service_ref: null
  entitlement_type: null
  issued_at: null
  effective_from: null
  effective_until: null
  holder_actor_ids: []
  holder_group_ref: null
  bearer_mode: NAMED_OR_REGISTERED
  scope_ref: null
  use_policy_ref: null
  transfer_policy_ref: null
  prerequisite_refs: []
  financial_event_refs: []
  reservation_refs: []
  representation_ids: []
  validation_event_ids: []
  use_event_ids: []
  supersedes_entitlement_id: null
  superseded_by_entitlement_id: null
  current_state: ISSUED
  history_event_ids: []
```

Candidate `entitlement_type` values are descriptive only:

- SINGLE_USE_TICKET
- MULTI_USE_PASS
- NETWORK_PASS
- DAY_PASS
- SESSION_ADMISSION
- EVENT_ADMISSION
- JOURNEY_ENTITLEMENT
- SPECIAL_DESTINATION_TICKET
- COMP_ACCESS
- INVITATION_ENTITLEMENT
- SERVICE_VOUCHER

No type implies a universal price, transfer rule or identity requirement.

## 3. Entitlement state

Candidate lifecycle states:

- DRAFT
- PENDING_ISSUANCE
- ISSUED
- ACTIVE
- FUTURE_VALIDITY
- VALIDATION_REQUIRED
- PARTIALLY_USED
- FULLY_USED
- EXPIRED
- SUSPENDED
- DISRUPTED
- REBOOKING_REQUIRED
- CANCELLED_BY_HOLDER
- CANCELLED_BY_ISSUER
- VOIDED_BY_POLICY
- SUPERSEDED
- REISSUED
- ARCHIVED
- VALIDITY_UNRESOLVED

State transitions require a governing event or policy reference.

`DISRUPTED` should be preferred over immediate cancellation when the underlying service disruption does not itself determine what happens to the entitlement.

## 4. Entitlement scope

```yaml
entitlement_scope:
  scope_id: null
  service_refs: []
  network_ref: null
  origin_place_refs: []
  destination_place_refs: []
  zone_refs: []
  event_ref: null
  activity_ref: null
  departure_refs: []
  session_refs: []
  service_class_ref: null
  valid_time_window_refs: []
  allowed_use_count: null
  party_size_limit: null
  allocation_refs: []
  exclusion_refs: []
  authored_rule_ref: null
```

Scope must be explicit enough that two superficially similar tickets can be distinguished.

A network pass and a departure-specific reservation can coexist.

A special-destination ticket can require a broader network pass without either record becoming the other.

## 5. Reservation record

A reservation reserves bounded capacity or service opportunity when the owning service supports reservations.

```yaml
service_reservation:
  reservation_id: null
  owning_service_ref: null
  service_access_request_ref: null
  entitlement_id: null
  actor_ids: []
  group_ref: null
  requested_scope_ref: null
  confirmed_scope_ref: null
  capacity_allocation_ref: null
  created_at: null
  confirmed_at: null
  check_in_window_ref: null
  current_state: REQUESTED
  history_event_ids: []
```

Candidate states:

- REQUESTED
- HELD
- CONFIRMED
- WAITLISTED
- CHANGE_REQUESTED
- CHANGED
- CHECK_IN_OPEN
- CHECKED_IN
- NO_SHOW_RECORDED
- CANCELLED_BY_HOLDER
- CANCELLED_BY_SERVICE
- EXPIRED
- COMPLETED
- DISRUPTED

Reservation identity persists through ordinary changes when the policy treats them as changes rather than cancellation plus new booking.

## 6. Representation

An entitlement may have zero, one or many representations.

```yaml
entitlement_representation:
  representation_id: null
  entitlement_id: null
  representation_type: null
  material_object_ref: null
  issuer_serial_ref: null
  displayed_scope_snapshot_ref: null
  generated_at: null
  replaced_at: null
  replacement_reason_ref: null
  current_state: CURRENT
```

Candidate forms:

- PAPER
- CARD
- TOKEN
- WRIST_MARK
- STAMP
- PRINTED_CODE
- DEVICE_RECORD
- REGISTRY_ONLY
- MANIFEST_ENTRY
- INVITATION_NOTE

Representation does not determine whether the entitlement is transferable.

A replacement can supersede a lost representation while the entitlement itself remains continuous.

## 7. Bearer and identity modes

Candidate modes:

- BEARER
- NAMED_OR_REGISTERED
- GROUP_BOUND
- INVITEE_BOUND
- VEHICLE_OR_PARTY_BOUND
- POLICY_DEFINED

The mode must come from the issuer policy.

`PHYSICAL_POSSESSION != IDENTITY_CONFIRMED`.

`IDENTITY_CONFIRMED != ENTITLEMENT_VALID`.

For a bearer instrument, physical possession may be sufficient only because the authored policy says so.

## 8. Prerequisite composition

```yaml
entitlement_prerequisite:
  prerequisite_id: null
  entitlement_id: null
  requirement_type: null
  required_ref: null
  evaluated_at: null
  evaluation_state: UNKNOWN
  decision_event_ref: null
```

Possible requirements include:

- another entitlement;
- eligibility decision from Battle Institutions;
- credential authorization;
- identity match;
- minimum or maximum party size;
- service-access registration;
- owning-service state;
- authored invitation;
- financial settlement reference when required by policy.

The system should preserve each requirement separately instead of synthesizing an unexplained access score.

## 9. Validation event

```yaml
entitlement_validation_event:
  validation_event_id: null
  entitlement_id: null
  representation_id: null
  presented_by_actor_id: null
  validator_actor_or_system_ref: null
  service_boundary_ref: null
  observed_at: null
  rule_version_ref: null
  checked_prerequisite_refs: []
  decision: null
  reason_refs: []
  resulting_state_event_ref: null
```

Candidate decisions:

- VALID_FOR_SCOPE
- VALID_BUT_WRONG_SERVICE
- VALID_BUT_WRONG_TIME
- VALID_BUT_PREREQUISITE_MISSING
- EXPIRED
- ALREADY_USED
- SUSPENDED
- CANCELLED
- SUPERSEDED
- HOLDER_MISMATCH
- REPRESENTATION_REPLACED
- CANNOT_DETERMINE

`CANNOT_DETERMINE` is legitimate. A damaged old ticket need not become fraudulent simply because current systems cannot resolve it.

## 10. Use and consumption

```yaml
entitlement_use_event:
  use_event_id: null
  entitlement_id: null
  validation_event_id: null
  owning_service_event_ref: null
  actor_ids: []
  service_scope_used_ref: null
  started_at: null
  completed_at: null
  use_units_consumed: null
  resulting_entitlement_state: null
```

The owning service remains authoritative for the actual journey, event, session or service completion.

This layer records that the entitlement was used for a particular scope.

A validation can occur without successful service use if the service fails immediately afterward.

## 11. Assignment is distinct from entitlement

Seat, room, cabin, berth, platform slot, table, challenge station or similar allocations should remain specialized references.

```yaml
entitlement_allocation_link:
  entitlement_id: null
  allocation_owner: null
  allocation_ref: null
  effective_at: null
  ended_at: null
```

`ENTITLEMENT_VALID != SEAT_ASSIGNED`.

`SEAT_ASSIGNED != HOLDER_BOARDED`.

`HOLDER_BOARDED != JOURNEY_COMPLETED`.

## 12. Issuance and payment

Possible issuance triggers include:

- purchase;
- institutional invitation;
- compensation;
- public-service allocation;
- membership benefit;
- challenge/event registration;
- replacement;
- progression decision from another owner;
- emergency or relief allocation if canon establishes it.

The issuance event records its trigger.

`PAYMENT_AUTHORIZED != PAYMENT_RECEIVED`.

`PAYMENT_RECEIVED != ENTITLEMENT_ISSUED`.

`ENTITLEMENT_ISSUED != REPRESENTATION_DELIVERED`.

## 13. Reissue, replacement and supersession

```yaml
entitlement_reissue_event:
  reissue_event_id: null
  entitlement_id: null
  reason_ref: null
  old_representation_ids: []
  new_representation_ids: []
  entitlement_scope_changed: false
  replacement_entitlement_id: null
  created_at: null
```

A representation replacement normally preserves entitlement identity.

A scope expansion or contractually distinct rebooking may instead create a successor entitlement with explicit lineage.

`NEW_TOKEN != NEW_RIGHT`.

`NEW_RIGHT != OLD_HISTORY_ERASED`.

## 14. Cancellation, disruption and financial settlement

Cancellation of the entitlement and cancellation of the underlying service are distinct events.

A service disruption can create a follow-up state:

- STILL_VALID_FOR_ALTERNATIVE_SERVICE
- REBOOKING_REQUIRED
- HOLDER_ACTION_REQUIRED
- ISSUER_REVIEW_REQUIRED
- REFUND_ELIGIBILITY_PENDING
- REPLACEMENT_ENTITLEMENT_PENDING
- EXPIRED_BY_AUTHORED_RULE

Any refund, credit or reversal belongs to Finance.

`ENTITLEMENT_CANCELLED != REFUND_SENT`.

`REFUND_SENT != REFUND_RECEIVED`.

`SERVICE_CANCELLED != ENTITLEMENT_CANCELLED`.

## 15. Network and layered passes

A pass can grant a broad scope while another reservation or ticket grants a narrow use within it.

Example structure:

```yaml
network_pass:
  grants: COASTAL_FERRY_NETWORK
special_ticket:
  grants: LANTERN_ISLE_EVENT_SAILING
  prerequisite_refs:
    - COASTAL_FERRY_NETWORK_PASS
```

This mirrors a common real and Pokémon-world pattern without imposing a universal fare hierarchy.

## 16. Group entitlements

One entitlement can cover a group if the issuer policy permits it.

Keep these fields separate:

- reservation party;
- covered actor list;
- current group membership;
- number of remaining uses;
- identity-verification requirement;
- physical representation count.

One printed ticket does not imply one traveler.

## 17. Partial use

A multi-segment or multi-use entitlement can be partially consumed.

```yaml
entitlement_use_balance:
  entitlement_id: null
  original_use_scope_ref: null
  completed_use_refs: []
  remaining_use_scope_ref: null
  last_recalculated_at: null
```

Never infer that the entire itinerary completed because the first boundary was validated.

## 18. Historical and expired artifacts

A physical ticket can remain culturally or historically meaningful after expiry.

Archive/Museum/Material Culture can preserve the object.

This layer preserves:

- original issuer;
- original scope;
- original validity;
- known validation/use events;
- later expiry or supersession.

`HISTORICALLY_AUTHENTIC != CURRENTLY_VALID`.

## 19. Notification and published information

Communications owns delivery of confirmation, cancellation and change messages.

Public Notices owns physical or public-facing displays.

This layer stores the authoritative entitlement event that those systems report.

`NOTICE_SENT != NOTICE_RECEIVED`.

`DISPLAY_UPDATED != HOLDER_INFORMED`.

`HOLDER_NOT_INFORMED != ENTITLEMENT_UNCHANGED`.

## 20. Cross-system handoffs

### Travel / Transit

Reads entitlement validity for boarding decisions if the service uses ticketing. Owns actual departure, boarding, route, vehicle and arrival state.

### Maritime / Rail / Road / Aviation / Ropeway

May provide service-specific scope and allocations. Do not let this common layer erase specialized operational states.

### Event Operations

Provides event identity, venue state, activity scope and cancellation/relocation facts.

### Battle Institutions

Provides challenge eligibility and battle authority. Spectator admission and competitor eligibility can require separate records.

### Service Access

Owns queue, appointment, call and check-in coordination. Can reference a confirmed reservation.

### Finance

Owns payment/refund provenance.

### Human Identity

Resolves actor linkage when a record is named.

### Place Reference

Resolves venue, terminal, entrance or service-point identity. Correct ticket scope does not prove that the actor reached the correct entrance.

## 21. Strong invariants

`RESERVATION_REQUESTED != RESERVATION_CONFIRMED`

`RESERVATION_CONFIRMED != ENTITLEMENT_ISSUED`

`ENTITLEMENT_ISSUED != PAYMENT_RECEIVED`

`ENTITLEMENT_ISSUED != REPRESENTATION_RECEIVED`

`VALID_REPRESENTATION != VALID_ENTITLEMENT`

`VALID_ENTITLEMENT != SERVICE_OPERATING`

`SERVICE_OPERATING != CAPACITY_AVAILABLE`

`VALID_ENTITLEMENT != ENTRY_COMPLETED`

`VALIDATION_SUCCESS != SERVICE_COMPLETED`

`NETWORK_PASS_VALID != SPECIFIC_DEPARTURE_RESERVED`

`SEAT_ASSIGNED != PASSENGER_BOARDED`

`BOOKING_EXISTS != HOLDER_PRESENT`

`TICKET_NAME_MATCH != ISSUER_MATCH`

`TOKEN_LOST != ENTITLEMENT_CANCELLED`

`TOKEN_FOUND != ENTITLEMENT_TRANSFERRED`

`SERVICE_CANCELLED != REFUND_COMPLETED`

`REISSUED_REPRESENTATION != DUPLICATE_VALID_ACCESS`

`SUPERSEDED_PASS != HISTORY_DELETED`

`QUEUE_POSITION != RESERVED_CAPACITY`

`PROFESSIONAL_CREDENTIAL != ADMISSION_ENTITLEMENT`

`BATTLE_VICTORY != ADMISSION_GRANTED`

## 22. Encounter boundary

Ticketing and admission disputes should rarely be battles by themselves.

When an independent tactical threat occurs near an admission boundary, the narrative entitlement state is frozen before BattleSpec creation.

The battle can determine immediate physical access or safety only.

It cannot validate a ticket, assign a seat, settle a refund, decide identity, issue a pass, consume an entitlement, waive a prerequisite or authorize service operation.

## 23. Encounter template: Boarding Gate Withdrawal

Full intended version:

A service boundary is processing passengers when an independent tactical threat appears. Staff pause validation and withdraw passengers through a protected route while combatants hold the approach.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic protected lanes or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version: READY.

Reduced contract:

1. Validation and boarding pause.
2. Passengers, validators, records and noncombatant Pokémon leave BattleSpec.
3. Ouros selects explicit combatants.
4. Static reviewed geometry is sent to AutoPTU.
5. Victory can create only `IMMEDIATE_GATE_APPROACH_CLEAR`.
6. The service owner later decides whether validation or boarding resumes.

`APPROACH_CLEAR != BOARDING_AUTHORIZED`.

## 24. Encounter template: Ticket Office Access Chokepoint

Full intended version:

A replacement/rebooking counter contains no tactical objective itself, but an independent threat blocks safe public access while the underlying service is disrupted.

Reduced version: READY.

All private records, staff and customers remain outside BattleSpec. Combat resolves only the static approach.

`TACTICAL_VICTORY != REBOOKING_COMPLETED`.

`TACTICAL_VICTORY != REFUND_APPROVED`.

## 25. Encounter template: Special-Admission Perimeter

Full intended version:

A special event or remote destination requires both a broad network pass and a specific entitlement. An unrelated encounter occurs outside the controlled perimeter.

Reduced version: READY.

The prerequisite decision is made before combat. AutoPTU never decides whether either entitlement is valid.

`BATTLE_RESULT != PREREQUISITE_SATISFIED`.

## 26. Minecraft / Cobblemon projection rules

Minecraft can represent:

- ticket counters;
- gates;
- turnstile-like scenery;
- waiting areas;
- route boards;
- paper/card/token props;
- changed departure boards;
- closed entrances;
- staff/NPC positions;
- temporary rebooking counters;
- festival wristband or stamp visuals if canon establishes them.

These are projections.

A player holding an item stack does not prove entitlement validity.

An open gate does not prove admission.

A redstone pulse does not consume an entitlement.

A scoreboard tag does not become a diegetic ticket.

Cobblemon BattleState must not decide access rights, holder identity, service state, payment, seat allocation, ticket consumption or narrative consequences.

## 27. PTU / Caelo guardrails

Remain source-governed and UNKNOWN unless verified:

- ticket prices;
- generic pass Items;
- validation Skill Checks;
- forgery detection;
- transferability;
- admission penalties;
- no-show rules;
- discounts;
- fare evasion mechanics;
- automatic access from Badges or League rank;
- species/Type-based free travel;
- Moves or Abilities that authenticate or duplicate tickets;
- Trainer Features that waive institutional requirements;
- battle victory as payment, ticket validation or service admission.

No narrative entitlement should alter HP, status, initiative, movement, damage, accuracy or legality unless an exact PTU/Caelo rule independently establishes that effect.

## 28. Canon questions deliberately left open

- Which Ouros institutions use tickets or reservations at all?
- Which services are free, paid, invitation-only or open access?
- Do any regions use network passes?
- Are entitlements transferable anywhere?
- Which systems are bearer-based versus identity-bound?
- What physical or digital representations exist?
- Which services support reissue after loss?
- What are local refund/rebooking practices?
- Which institutions maintain centralized records, if any?
- Are there recurring commuter, student, League, festival or civic passes?
- How are children, groups and Pokémon companions represented in capacity or admission rules?
- Which historical tickets or passes already exist in Ouros canon?

All answers remain PROPOSED/UNKNOWN until authored elsewhere.
