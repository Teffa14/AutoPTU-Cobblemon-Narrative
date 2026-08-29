# Public Library Circulation, Access & Service Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not canon.
Date: 2026-08-29
Pass: 135

## Purpose

This layer models ordinary public-library service continuity across branches, reading rooms, circulating copies, holds, pickups, returns, transfers, mobile stops and temporary service changes.

It does not replace Archives/Museums/Collections. That layer remains authoritative for accession, preservation, archival provenance, restricted holdings, institutional loans, authenticity and conservation.

The central rule is scope separation.

A building can be open while a reading room is closed. A branch can be open while inter-branch transfer is paused. A title can exist in the catalog while no local copy is present. A returned copy can be inside the building but not yet available. A hold can survive a service interruption. A user can access information without ever receiving the original object.

## 1. Library service institution

```yaml
library_service:
  library_service_id: null
  institution_ref: null
  mandate_ref: null
  branch_ids: []
  mobile_service_ids: []
  shared_catalog_id: null
  circulation_policy_id: null
  access_policy_ref: null
  notification_channel_refs: []
  current_service_incident_ids: []
  status: ACTIVE
```

No service mandate is inferred from the word library. Canon must establish each institution and its authority.

## 2. Branch

```yaml
library_branch:
  branch_id: null
  library_service_id: null
  location_id: null
  current_name: null
  former_name_ids: []
  opening_schedule_ref: null
  service_scope_ids: []
  reading_room_ids: []
  circulating_collection_scope_ids: []
  local_history_collection_ref: null
  pickup_point_ids: []
  return_point_ids: []
  temporary_service_point_ids: []
  predecessor_site_ids: []
  successor_site_ids: []
  service_state: OPEN
```

Candidate service states:

OPEN
PARTIAL
TEMPORARY_LOCATION
RENOVATION_SERVICE
CLOSED_TEMPORARILY
CLOSED_PERMANENTLY
MOVED
UNKNOWN

A branch state never changes an Archives collection object's provenance by itself.

## 3. Service scope

```yaml
library_service_scope:
  service_scope_id: null
  branch_id: null
  service_kind: null
  spatial_scope_ids: []
  audience_scope_ref: null
  schedule_ref: null
  policy_ref: null
  dependency_ids: []
  state: AVAILABLE
  state_reason_ids: []
  effective_from: null
  effective_until: null
```

Candidate service kinds:

READING_ROOM
CIRCULATION
HOLDS_PICKUP
RETURNS
LOCAL_BRANCH_TRANSFER
NETWORK_RESOURCE_SHARING
REFERENCE_HELP
PUBLIC_TERMINAL
LOCAL_HISTORY_ACCESS
MOBILE_STOP
COMMUNITY_ROOM_ACCESS

The repository should not treat these as one OPEN/CLOSED flag.

## 4. Bibliographic work and copy identity

The intellectual work and the physical or authorized access copy are different records.

```yaml
library_work_record:
  work_id: null
  title_claim: null
  creator_claim_ids: []
  edition_or_version_ids: []
  subject_tags: []
  language_tags: []
  source_catalog_refs: []
  related_archive_object_refs: []
  status: CURRENT
```

```yaml
library_copy:
  copy_id: null
  work_id: null
  copy_kind: PHYSICAL
  owner_or_custodian_ref: null
  home_branch_id: null
  current_location_ref: null
  shelving_location_ref: null
  condition_ref: null
  circulation_class_ref: null
  restriction_ref: null
  current_transaction_ref: null
  availability_state: AVAILABLE
```

Candidate copy kinds:

PHYSICAL
AUTHORIZED_REPRODUCTION
DIGITAL_ACCESS_REFERENCE
READING_ROOM_COPY
LOCAL_HISTORY_COPY

`WORK_EXISTS != COPY_EXISTS_LOCALLY`

`CATALOG_RECORD_EXISTS != COPY_AVAILABLE`

`AUTHORIZED_REPRODUCTION != ORIGINAL_OBJECT`

## 5. Catalog availability snapshot

```yaml
catalog_availability_snapshot:
  snapshot_id: null
  catalog_id: null
  work_id: null
  observed_at: null
  branch_availability: []
  requestable: null
  source_record_refs: []
  freshness_state: null
```

Catalog availability is an observation, not omniscient world truth.

A snapshot can be stale.

A copy can be in transit while an old screen still says AVAILABLE.

A returned copy can be physically present while the catalog still says CHECKED_OUT.

## 6. Patron/access identity

If Ouros canonizes library membership, keep it narrow.

```yaml
library_access_account:
  account_id: null
  actor_ref: null
  library_service_id: null
  access_basis_ref: null
  current_state: ACTIVE
  created_at: null
  restriction_event_ids: []
  accommodation_refs: []
  privacy_policy_ref: null
```

Do not infer:

- legal identity systems;
- age thresholds;
- residency requirements;
- fines;
- fees;
- credit-like consequences;
- household authority;
- guardianship;
- professional credentials.

Those require canon.

## 7. Hold request

```yaml
library_hold_request:
  hold_id: null
  requester_account_id: null
  work_id: null
  acceptable_copy_scope: null
  requested_at: null
  pickup_branch_id: null
  queue_position_claim: null
  assigned_copy_id: null
  ready_at: null
  pickup_deadline_ref: null
  cancellation_event_id: null
  fulfillment_event_id: null
  state: REQUESTED
```

Candidate states:

REQUESTED
QUEUED
SEARCHING
ASSIGNED
IN_TRANSFER
READY_FOR_PICKUP
PICKED_UP
FULFILLED_BY_ACCESS_COPY
CANCELLED
EXPIRED
UNFULFILLABLE
PAUSED

Important boundaries:

`REQUESTED != ASSIGNED`

`ASSIGNED != IN_TRANSFER`

`IN_TRANSFER != READY_FOR_PICKUP`

`READY_FOR_PICKUP != PICKED_UP`

`QUEUE_POSITION_RECORDED != FUTURE_POSITION_GUARANTEED` unless policy explicitly says otherwise.

## 8. Checkout

```yaml
library_checkout:
  checkout_id: null
  copy_id: null
  account_id: null
  checkout_branch_id: null
  checked_out_at: null
  due_at: null
  renewal_event_ids: []
  return_event_id: null
  state: ACTIVE
```

A checkout records circulation custody for the service. It does not change ownership by default.

`CHECKED_OUT_TO_ACTOR != OWNED_BY_ACTOR`

## 9. Renewal

```yaml
library_renewal_event:
  renewal_id: null
  checkout_id: null
  requested_at: null
  policy_version_ref: null
  blocking_hold_ref: null
  decision: PENDING
  new_due_at: null
  reason_ref: null
```

No universal renewal count or duration is assumed.

## 10. Return and reshelving

```yaml
library_return_event:
  return_id: null
  copy_id: null
  accepted_at: null
  accepted_location_ref: null
  receiving_branch_id: null
  condition_observation_ref: null
  routing_decision_ref: null
  reshelved_at: null
  next_hold_id: null
  state: ACCEPTED
```

Candidate states:

ACCEPTED
IN_CHECKIN
ROUTING
HELD_FOR_NEXT_REQUEST
IN_TRANSFER
RESHELVING
AVAILABLE
CONDITION_REVIEW

Strong boundaries:

`RETURN_ACCEPTED != CHECKIN_COMPLETE`

`CHECKIN_COMPLETE != AVAILABLE`

`PHYSICALLY_IN_BRANCH != RESHELVED`

`RESHELVED != CATALOG_SNAPSHOT_REFRESHED`

## 11. Branch transfer

```yaml
library_transfer:
  transfer_id: null
  copy_ids: []
  origin_branch_id: null
  destination_branch_id: null
  reason_ref: null
  shipment_ref: null
  dispatched_at: null
  received_at: null
  receiving_check_ref: null
  state: PLANNED
```

Courier/Logistics owns physical shipment execution where appropriate.

Library service owns why the copy is moving and the service consequence.

`TRANSFER_CREATED != SHIPMENT_DISPATCHED`

`SHIPMENT_DELIVERED != LIBRARY_RECEIPT_PROCESSED`

## 12. Interlibrary/resource-sharing request

```yaml
resource_sharing_request:
  request_id: null
  requesting_service_id: null
  supplying_service_id: null
  work_id: null
  requested_format_scope: null
  accepted_method: null
  source_object_ref: null
  supplied_copy_ref: null
  shipment_ref: null
  state: REQUESTED
```

Candidate fulfillment methods:

PHYSICAL_COPY_LOAN
AUTHORIZED_REPRODUCTION
READING_ROOM_ACCESS
REFERENCE_RESPONSE
DECLINED
UNKNOWN

The original collection owner retains provenance authority.

## 13. Reading-room access

```yaml
reading_room_visit:
  visit_id: null
  room_id: null
  actor_ref: null
  access_policy_ref: null
  requested_material_refs: []
  material_delivery_refs: []
  started_at: null
  ended_at: null
  notes_ref: null
```

Reading a source does not automatically establish the source's claim as fact.

Reading does not automatically grant a Skill Rank, Edge, Feature, Move or Trainer Level.

## 14. Reference question

```yaml
reference_question:
  reference_question_id: null
  requester_ref: null
  received_at: null
  question_summary: null
  search_record_refs: []
  candidate_source_refs: []
  response_claim_ids: []
  uncertainty_notes: []
  state: OPEN
```

This supports investigation gameplay without making librarians omniscient.

A response can be:

ANSWERED_WITH_SOURCES
PARTIALLY_ANSWERED
REFERRED
NO_SOURCE_FOUND
QUESTION_REFRAMED
CLOSED_WITHOUT_ANSWER

## 15. Mobile library / temporary stop

```yaml
mobile_library_stop:
  stop_id: null
  service_id: null
  vehicle_or_unit_ref: null
  location_id: null
  schedule_ref: null
  offered_service_scope_ids: []
  weather_or_route_dependency_ids: []
  current_state: SCHEDULED
```

A mobile stop can become narratively important after a branch closure, construction project, evacuation or route disruption.

The mobile unit does not inherit every service of a full branch automatically.

## 16. Service incident

```yaml
library_service_incident:
  incident_id: null
  service_id: null
  branch_scope_ids: []
  affected_service_scope_ids: []
  started_at: null
  cause_claim_ids: []
  dependency_refs: []
  temporary_measure_ids: []
  recovery_checkpoint_ids: []
  closed_at: null
  state: ACTIVE
```

Examples:

- building renovation;
- water intrusion;
- communications outage;
- route disruption;
- staffing shortfall;
- catalog migration;
- temporary relocation;
- shared-transfer suspension;
- local closure while returns remain accepted elsewhere.

No cause is inferred from coincidence.

## 17. Service recovery checkpoint

```yaml
library_recovery_checkpoint:
  checkpoint_id: null
  incident_id: null
  service_scope_id: null
  observed_at: null
  observed_state: null
  evidence_refs: []
  next_review_at: null
```

Recovery can be staggered.

`BUILDING_REOPENED != ALL_SERVICES_RESTORED`

`CATALOG_ONLINE != TRANSFERS_RESUMED`

`TRANSFERS_RESUMED != QUEUE_CAUGHT_UP`

`QUEUE_CAUGHT_UP != COMMUNITY_ROUTINE_RESET`

## 18. Historical continuity

A library should retain evidence of service change.

Possible persistent traces:

- former branch name carved over a doorway;
- old bookplates or branch stamps;
- two call-number systems on the same shelf labels;
- a mobile-library stop that became permanent;
- a temporary pickup counter that residents still use as a meeting place;
- former Gym or school space reused as stacks;
- old routing stickers on copies;
- a branch closed years ago whose return slot remains visible;
- local-history material still referencing the predecessor institution.

## 19. Mystery structures

Prefer chronology, routing and metadata over arbitrary locked-room puzzles.

Strong patterns:

- returned but not reshelved;
- catalog says one branch, routing label says another;
- hold assigned before a branch closure;
- two copies with different edition notes;
- a source cited under a former title;
- a mobile stop used as an emergency pickup point;
- an old shelving map preserved in a photo;
- an interlibrary copy mistaken for a local holding;
- a reproduction mistaken for the original source object;
- a queue preserved across an outage while notifications fail.

## 20. Agency and privacy guardrails

A library record may contain sensitive reading or request history if canon chooses to retain such data.

Do not assume:

- universal retention;
- public access to patron history;
- police access;
- parental access;
- employer access;
- school access;
- household access;
- permanent borrowing history.

Privacy scope must be authored.

## 21. Pokémon agency guardrails

A Pokémon present in a library may be:

- a partner accompanying a visitor;
- a known resident individual;
- an accessibility/service participant if canon establishes that role;
- a wild visitor;
- a trained worker;
- a recurring local character.

Presence does not establish ownership, employment, literacy, research competence or custody.

Species does not automatically grant librarian capability.

Psychic or telepathic flavor does not automatically reveal source contents or authenticate claims.

## 22. Minecraft/Cobblemon representation

Minecraft/Cobblemon can present:

- open/closed branch doors;
- public reading areas;
- stacks as coarse world geometry;
- a pickup shelf or service desk;
- routing crates;
- returned-book carts;
- mobile-library vehicles or stalls;
- old branch signage;
- renovation barriers;
- a visible temporary service counter;
- NPC routines that change with opening hours;
- Pokémon routines already established by Ouros world state.

It must not decide:

- who may borrow;
- whether a hold exists;
- whether a return completed;
- whether a source is authentic;
- whether a person read or understood a source;
- whether a catalog claim is true;
- whether a Pokémon owns or authored anything;
- battle-state legality or narrative consequence.

## 23. PTU/Caelo boundary

Keep mechanical knowledge acquisition rule-governed.

Do not invent universal:

- General Education DCs for library searches;
- Perception DCs for finding a shelved book;
- Researcher/Scholar bonuses outside exact source text;
- reading-time rules;
- automatic Skill Rank increase from study;
- automatic Edge/Feature gain from a course or reading list;
- translation success from a single Skill without source support;
- Move learning from a manual unless the governing rule says so;
- memory checks;
- misinformation detection bonuses;
- library-card Items;
- archive protection reactions;
- shelf-cover combat bonuses.

## 24. Encounter implementation contracts

### A. Branch Closing-Time Withdrawal

Narrative premise:

A routine closing is interrupted by a separate tactical incident outside or near an exit. Staff need to finish withdrawal and secure service areas.

Full intended dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for escort/Intercept/forced displacement
- core calculations — VERIFIED baseline
- action economy/initiative — VERIFIED baseline
- full turn/round lifecycle — PARTIAL for staged withdrawal timing
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for ordinary implemented statuses only
- terrain/weather/hazards/zones/reactions — BLOCKING for protected exits, falling shelving, smoke, live hazards or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for semantic withdrawal/service-state projection

Reduced version — READY:

1. Library service ends public access in world state.
2. Visitors, staff, carts, records, fragile material and noncombatant Pokémon leave BattleSpec.
3. Ouros selects explicit combatants.
4. Static geometry is supplied to AutoPTU.
5. The fight determines immediate access only.
6. Library service separately records whether closing completed.

Forbidden automatic transitions:

victory => BRANCH_SECURED
victory => ALL_VISITORS_ACCOUNTED_FOR
victory => RETURNS_PROCESSED
victory => HOLD_READY
victory => COLLECTION_SAFE

### B. Transfer Crate Chokepoint

Narrative premise:

A branch-transfer shipment is paused because an unrelated encounter blocks the route to or from the loading point.

Full intended dependencies:

Movement/reactions, objective-aware AI and semantic adapter support remain limiting families.

Reduced version — READY:

The crate, courier, receiving staff and transfer records remain outside BattleSpec. The shipment is stopped. AutoPTU resolves a conventional static encounter. Courier/Library service decides dispatch or receipt only after the tactical transcript is complete.

Victory never proves:

- copy identity;
- ownership;
- authenticity;
- successful delivery;
- successful check-in;
- fulfillment of a hold.

### C. Temporary Reading-Room Access Perimeter

Narrative premise:

A temporary service point operating during renovation or closure must suspend access while a nearby tactical threat is cleared.

Full intended dependencies:

Escort, protected-zone reactions, timed withdrawal, tactical AI and semantic playback are not fully verified.

Reduced version — READY:

The room closes first. Readers, staff and requested materials leave the tactical grid. Combat occurs in an adjacent static space. Reopening requires a separate world-state decision.

Victory never establishes:

- access permission;
- source authenticity;
- research success;
- knowledge gain;
- branch reopening;
- service restoration.

## 25. Capability-family implications

This layer does not require any capability promotion.

Its reduced encounters fit the existing VERIFIED baseline when conventional combat is isolated from service-state transitions.

Rich versions continue to depend on the exact permanent families named above.

## 26. Generation guardrails

1. Catalog data is not omniscient truth.
2. Work identity and copy identity stay separate.
3. Checkout is not ownership.
4. Return acceptance is not immediate availability.
5. Branch open does not mean every service is available.
6. Network transfer pause does not mean every branch is closed.
7. A queue can survive a disruption without all positions being known perfectly.
8. A librarian can be mistaken without being corrupt.
9. A missing copy can be routing error, delayed check-in, repair, hold assignment, loss or genuine theft; do not choose theft automatically.
10. A reproduction is not the original object.
11. Public reading access does not grant unrestricted archive access.
12. A source can contain a false claim and still be catalogued correctly.
13. Reading does not automatically grant mechanics.
14. Pokémon presence does not establish ownership, authorship or professional role.
15. Battles resolve tactical facts only.
16. Preserve predecessor branch names, labels and routing history when facilities change.
17. Keep provenance/research separate from canon.
18. Any membership, fines, fees, privacy, age or eligibility rule must be authored locally.

## 27. Implementation priority

1. branch + service-scope state;
2. work/copy separation;
3. hold lifecycle;
4. checkout/return/reshelving lifecycle;
5. branch transfer handoff to Courier;
6. service incidents and staggered recovery;
7. reading-room/reference records;
8. mobile/temporary service points;
9. local-history linkage to Archives;
10. Minecraft visible-state projection;
11. richer tactical variants only after required engine families are verified.