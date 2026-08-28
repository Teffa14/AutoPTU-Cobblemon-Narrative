# Ouros Hospitality, Lodging & Guest-Stay Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until explicitly approved.

## Purpose

This extension models temporary accommodation as persistent world state without turning beds, buildings or Pokémon Centers into hidden rule engines.

It answers:
- who is actually staying where;
- whether a reservation became a real stay;
- what space was assigned and whether it remained usable;
- which amenities or services were available;
- what interruptions occurred;
- what staff and guests knew at the time;
- what history remains after checkout.

## 1. Authority boundary

Hospitality owns temporary guest-stay continuity, reservation state, accommodation allocation, guest-facing availability, check-in/check-out history and establishment-level service availability.

Travel owns journeys, arrivals and onward-route viability.

Commercial Services owns charges, purchases and payment records.

Care/Recovery owns treatment and clinical recovery.

Facility Maintenance owns asset faults, repair and verification.

Crisis owns evacuation, emergency shelter activation and incident response.

Public Notices owns published information objects.

Accessibility owns accommodation requirements and participation support.

PTU/AutoPTU owns mechanical rest/healing consequences.

Hospitality never grants HP, removes Status Conditions, restores Daily Moves or refreshes AP merely because a guest has a room.

## 2. Establishment identity

```yaml
hospitality_establishment:
  establishment_id: null
  location_ref: null
  establishment_kind: authored
  operator_ref: null
  guest_scope_policy_ref: null
  accommodation_unit_refs: []
  service_area_refs: []
  accessibility_profile_ref: null
  current_operational_state: UNKNOWN
  history_event_ids: []
  canon_status: proposed
```

Candidate kinds are descriptive only: INN, HOTEL, LODGE, HOSTEL, GUESTHOUSE, CAMPGROUND, RESORT, PILGRIM_LODGING, COMMUNITY_GUEST_SPACE, OTHER_AUTHORED.

No kind implies pricing, legality, Pokémon access, medical capability or PTU recovery.

## 3. Accommodation units

```yaml
accommodation_unit:
  unit_id: null
  establishment_id: null
  unit_kind: authored
  capacity_claim: null
  accessibility_refs: []
  current_serviceability: UNKNOWN
  maintenance_refs: []
  allocation_refs: []
  history_event_ids: []
```

A unit may be a room, bunk space, cabin, campsite, suite or other authored temporary accommodation.

`SERVICEABLE` does not mean `AVAILABLE`.

`AVAILABLE` does not mean `RESERVED`.

`RESERVED` does not mean `OCCUPIED`.

## 4. Reservation record

```yaml
lodging_reservation:
  reservation_id: null
  establishment_id: null
  guest_party_ref: null
  requested_window: null
  confirmed_window: null
  requested_unit_profile_refs: []
  allocated_unit_refs: []
  reservation_state: REQUESTED
  source_channel_ref: null
  payment_or_deposit_refs: []
  accessibility_request_refs: []
  change_event_ids: []
  provenance_refs: []
```

Candidate states:
- REQUESTED
- WAITLISTED
- CONFIRMED
- MODIFIED
- CANCELLED_BY_GUEST
- CANCELLED_BY_OPERATOR
- NO_SHOW
- CONVERTED_TO_STAY
- EXPIRED

A booking record is information, not proof of physical presence.

## 5. Guest party and privacy

```yaml
guest_party:
  guest_party_id: null
  actor_refs: []
  pokemon_refs: []
  declared_relationship_refs: []
  responsible_actor_refs: []
  privacy_classification_ref: null
  accessibility_refs: []
  provenance_refs: []
```

Presence in one party does not establish ownership, custody, employment or Trainer-Pokémon relationship.

Pokémon may only be treated as independent guests if canon and the relevant legal/custody systems permit it.

Guest lists are not world-omniscient public data.

## 6. Stay record

```yaml
lodging_stay:
  stay_id: null
  reservation_ref: null
  establishment_id: null
  guest_party_ref: null
  check_in_at: null
  checkout_due_at: null
  actual_checkout_at: null
  allocated_unit_refs: []
  occupancy_state: CHECKED_IN
  service_entitlement_refs: []
  interruption_event_ids: []
  rest_event_refs: []
  incident_refs: []
  history_event_id: null
```

Candidate occupancy states:
- CHECKED_IN
- PRESENT
- TEMPORARILY_AWAY
- RELOCATED_WITHIN_PROPERTY
- EVACUATED
- DEPARTED
- CHECKED_OUT
- ABANDONED_STAY_UNKNOWN

Hospitality records the stay. It does not infer exact sleep, recovery or battle readiness.

## 7. Guest-facing service availability

```yaml
hospitality_service_state:
  service_state_id: null
  establishment_id: null
  service_ref: null
  effective_from: null
  effective_until: null
  state: UNKNOWN
  cause_ref: null
  maintenance_or_external_dependency_refs: []
  notice_refs: []
  verification_ref: null
```

Candidate states:
- AVAILABLE
- LIMITED
- RESERVATION_ONLY
- STAFFING_LIMITED
- TEMPORARILY_UNAVAILABLE
- CLOSED_FOR_MAINTENANCE
- CLOSED_BY_AUTHORITY
- UNKNOWN

A hot spring, meal service, laundry, transport desk, lounge or care area can fail independently of room occupancy.

## 8. Staffing and operational capacity

```yaml
hospitality_staffing_snapshot:
  snapshot_id: null
  establishment_id: null
  observed_at: null
  role_assignments: []
  unavailable_staff_refs: []
  service_capacity_claims: []
  verification_state: null
  provenance_refs: []
```

Staff absence may reduce services without closing accommodation.

Never infer competence from species or Type. A Pokémon performs a hospitality task only when an individual assignment and governing capability support it.

## 9. Check-in sequence

Recommended chain:

```text
arrival or local presence
-> reservation/availability check
-> identity/custody/access requirements if applicable
-> unit allocation
-> check-in
-> physical occupancy
-> optional guest services
-> independently evaluated PTU rest/recovery
```

Each step may fail without erasing prior history.

## 10. Checkout and departure

Checkout can record:
- planned versus actual departure;
- early departure;
- extension;
- relocation;
- outstanding property/custody issue;
- emergency evacuation;
- unresolved lost-property record;
- guest feedback or follow-up when canon supports it.

Checkout never proves the traveler departed the settlement. Travel owns onward movement.

## 11. Capacity and overflow

```yaml
hospitality_capacity_snapshot:
  snapshot_id: null
  establishment_id: null
  valid_at: null
  serviceable_unit_count_ref: null
  allocated_unit_count_ref: null
  held_unit_count_ref: null
  overflow_state: NONE
  alternate_accommodation_refs: []
  provenance_refs: []
```

Narrative states can remain coarse:
- NONE
- BUSY
- NEAR_CAPACITY
- FULL
- OVERFLOW_ACTIVE
- UNKNOWN

Do not create exact bed counts unless authored.

Overflow may redirect guests toward another establishment, community shelter, camping, transit delay or a changed itinerary.

## 12. Interruption records

```yaml
lodging_interruption:
  interruption_id: null
  establishment_or_unit_ref: null
  started_at: null
  ended_at: null
  interruption_type: authored
  affected_stay_refs: []
  affected_service_refs: []
  authority_or_cause_ref: null
  relocation_refs: []
  verification_refs: []
  notice_refs: []
```

Candidate descriptive types:
- ACCESS_RESTRICTED
- UNIT_UNSERVICEABLE
- UTILITY_LOSS
- STAFFING_SHORTAGE
- WEATHER_DELAY
- EVACUATION
- CROWDING
- SECURITY_PERIMETER
- SERVICE_OUTAGE
- INFORMATION_ERROR

These labels have no tactical effect by themselves.

## 13. Rest boundary

A `rest_event_ref` may point to a PTU/AutoPTU-owned nonbattle recovery event when such an interface is verified.

Hospitality may provide circumstances compatible with rest, such as a quiet room or protected shelter. The governing PTU conditions still decide whether rest occurred.

Hard rules:
- room assignment != rest;
- bed interaction != rest;
- four hours elapsed on a reservation != Extended Rest;
- visual sleep != PTU Sleep status;
- hotel service != Pokémon Center healing;
- interruption semantics remain UNKNOWN until the governing nonbattle rest contract exists.

## 14. Recurring guest continuity

Recurring travelers can retain:
- prior establishment/stay references;
- staff familiarity;
- unresolved promises or disputes;
- preference claims;
- earlier observations;
- social relationships;
- past incidents.

This enables regional continuity without deterministic NPC rotation.

## 15. Establishment history

Recommended history events:

```text
ESTABLISHMENT_OPENED
SERVICE_ADDED
SERVICE_SUSPENDED
SERVICE_RESTORED
CAPACITY_REACHED
OVERFLOW_ACTIVATED
RESERVATION_CREATED
RESERVATION_CHANGED
CHECK_IN
UNIT_REASSIGNED
STAY_INTERRUPTED
GUEST_EVACUATED
CHECKOUT
ACCESS_RESTORED
ESTABLISHMENT_REPURPOSED
ESTABLISHMENT_CLOSED
```

No abstract `hospitality_level` is required.

## 16. Information and belief

Staff systems, booking records, signs and guest assumptions may disagree.

A guest may possess an old confirmation. Reception may have a revised allocation. A room may be visually empty but still held. A property may advertise a service that is temporarily unavailable.

Preserve timestamps and provenance instead of collapsing disagreement into a hidden truth score.

## 17. Encounter contract — Guest Wing Withdrawal

Narrative premise:

A conflict threatens one part of an occupied lodging property while staff are already moving uninvolved guests toward safe exits.

Full intended version may require:
- multiple withdrawal routes;
- Intercept/forced movement;
- route-protection objectives;
- reactions;
- AI that understands evacuation and separation;
- authoritative adapter playback.

Permanent capability requirements:

```yaml
requirements:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Current authoring profile: REDUCED.

Reduced version:
- evacuate every uninvolved guest before battle;
- lock or exclude occupied/private rooms from the grid;
- move staff and luggage away;
- explicitly select combatants;
- use a static lobby, courtyard or service corridor;
- winning secures the immediate area only;
- Hospitality/Crisis decides later re-entry and stay continuation.

## 18. Encounter contract — Overflow Camp Perimeter

Narrative premise:

A full establishment has redirected travelers to an authorized temporary camp or overflow area. A separate territorial conflict occurs at the perimeter.

Full version may want route-control, protection objectives, reactions, terrain/hazard support and tactical AI.

Reduced version:
- occupants remain in a protected noncombat zone;
- tents, personal property and resting Pokémon are outside the BattleSpec;
- combat occurs on a reviewed static edge;
- no battle result grants lodging, ejects guests or completes rest.

## 19. Encounter contract — Service Courtyard Interruption

Narrative premise:

A maintenance/service area is interrupted while the guest property remains partly operational.

Full version may want object protection, workers withdrawing, complete reactions and objective-aware AI.

Reduced version:
- Maintenance suspends work first;
- equipment and workers leave the tactical area;
- AutoPTU receives a static courtyard or access lane;
- battle cannot repair the failed service or restore availability.

## 20. Noncombat investigation — Four Bookings, Three Actual Stays

Four records appear to show four guest visits. Reconciliation may reveal that one reservation was modified, one guest changed properties, or one booking never converted into check-in.

Useful evidence:
- reservation timestamps;
- check-in records;
- room allocation history;
- public notices;
- travel arrival/departure evidence;
- staff testimony;
- guest consent where privacy permits.

The result may remain provisional.

## 21. Cobblemon/Minecraft boundary

Safe reuse candidates:
- building geometry;
- rooms and furniture;
- doors, signs and lighting;
- Pokémon models/forms/poses/animations/cries;
- decorative beds and camps;
- UI and interaction presentation;
- networking, entity tracking and persistence hooks;
- day/night and weather presentation.

Adapter-required:
- stable establishment/unit/stay bindings;
- authoritative access projection;
- explicit battle arena conversion;
- stable actor identity across load/unload;
- semantic playback.

Minecraft/Cobblemon must never decide:
- who is a guest from entity proximity;
- reservation or occupancy from a bed block;
- PTU rest from sleeping animation;
- healing from a Pokémon Center model;
- combatants from occupants of the same building;
- eviction/re-entry from KO outcome;
- ownership/custody from room sharing;
- battle result.

Binding flow remains:

`Ouros hospitality/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

## 22. Canon status discipline

Everything in this extension remains PROPOSED until explicitly approved.

A future canon file should reference approved establishment types, institutions and local practices rather than silently promoting this entire schema.