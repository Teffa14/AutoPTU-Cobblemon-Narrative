# Ouros Library Circulation, Borrowing & Interlibrary Loan Continuity Extension

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Date: 2026-08-31

## Purpose

This extension adds persistent circulation state for libraries and related collections. It is intentionally narrower than the existing Archives, Museums, Collections & Preservation layer.

Archives/Museums remains authoritative for holdings, cataloging, preservation, access policies, stewardship and institutional collection loans. This layer models temporary patron access to circulating material and networked borrowing between institutions.

It is dormant by default. No institution lends materials unless canon or an authored institutional policy says that it does.

## 1. Circulation policy

```yaml
circulation_policy:
  policy_id: null
  institution_id: null
  version_id: null
  effective_from: null
  effective_until: null
  eligible_patron_scope_refs: []
  circulating_collection_refs: []
  noncirculating_collection_refs: []
  renewal_rule_ref: null
  hold_rule_ref: null
  return_location_rule_ref: null
  lost_or_damage_rule_ref: null
  privacy_retention_rule_ref: null
  interlibrary_rule_ref: null
  authored_source_refs: []
  status: ACTIVE
```

The policy describes what the institution claims it will do. It does not itself prove that a specific loan was legal, returned, lost or paid for.

## 2. Patron account

```yaml
library_patron_account:
  patron_account_id: null
  institution_or_network_id: null
  actor_id: null
  eligibility_basis_refs: []
  opened_at: null
  expires_at: null
  current_service_state: ACTIVE
  active_loan_ids: []
  active_hold_ids: []
  notice_channel_refs: []
  privacy_profile_ref: null
  record_revision_ids: []
```

Possible service states:
- ACTIVE
- LIMITED
- SUSPENDED
- EXPIRED
- CLOSED
- UNKNOWN

A patron account is a service relationship. It is not citizenship, residence, student status, identity proof outside its mandate, or evidence of what the actor knows.

## 3. Circulating copy

```yaml
circulating_copy:
  circulating_copy_id: null
  collection_object_ref: null
  owning_institution_id: null
  current_custodian_ref: null
  current_location_ref: null
  circulation_class_ref: null
  condition_record_ref: null
  availability_state: AVAILABLE
  active_loan_id: null
  active_transfer_id: null
```

Availability states can include:
- AVAILABLE
- ON_HOLD_SHELF
- CHECKED_OUT
- IN_TRANSIT
- IN_PROCESSING
- REPAIR_OR_CONSERVATION
- MISSING
- LOST_DECLARED
- NONCIRCULATING
- WITHDRAWN

A title may have several copies with different availability and condition histories.

## 4. Hold or reservation

```yaml
circulation_hold:
  hold_id: null
  patron_account_id: null
  title_or_copy_scope_ref: null
  requested_at: null
  pickup_location_ref: null
  queue_position_claim: null
  availability_notice_id: null
  pickup_deadline: null
  fulfilled_by_copy_id: null
  status: REQUESTED
```

States:
REQUESTED → QUEUED → AVAILABLE_FOR_PICKUP → FULFILLED

Alternative terminals:
CANCELLED, EXPIRED, UNSATISFIABLE, POLICY_BLOCKED.

Queue position is an institutional operational claim and may change when priorities, copy scope or policy change.

## 5. Patron loan

```yaml
patron_loan:
  loan_id: null
  copy_id: null
  patron_account_id: null
  checkout_location_ref: null
  checkout_time: null
  due_time: null
  renewal_episode_ids: []
  return_episode_id: null
  condition_at_checkout_ref: null
  condition_at_return_ref: null
  status: CHECKED_OUT
```

States can include:
CHECKED_OUT, DUE_SOON, OVERDUE, RETURN_INITIATED, RETURNED, LOST_REPORTED, LOST_DECLARED, DAMAGED_REPORTED, CLOSED.

`OVERDUE` is operational timing state. It does not prove theft, intent, negligence or permanent loss.

## 6. Renewal episode

```yaml
loan_renewal_episode:
  renewal_id: null
  loan_id: null
  requested_at: null
  evaluated_policy_version_ref: null
  blocking_hold_refs: []
  decision: PENDING
  decided_at: null
  prior_due_time: null
  resulting_due_time: null
  decision_reason_refs: []
```

Possible decisions:
GRANTED, DENIED, PARTIAL_OR_MODIFIED, CANCELLED, UNKNOWN.

Renewal request and renewed due date must remain separate facts.

## 7. Return episode

```yaml
loan_return_episode:
  return_episode_id: null
  loan_id: null
  copy_id: null
  return_location_ref: null
  deposited_at: null
  received_by_institution_at: null
  checked_in_at: null
  condition_observation_ref: null
  routing_after_return_ref: null
  status: DEPOSITED
```

Important distinction:
DEPOSITED != RECEIVED != CHECKED_IN != RESHELVED.

This prevents a book placed in a return chute from teleporting into available inventory.

## 8. Loss and damage review

```yaml
circulation_loss_or_damage_case:
  case_id: null
  loan_id: null
  copy_id: null
  report_ids: []
  condition_evidence_refs: []
  institution_review_refs: []
  responsibility_claim_refs: []
  finance_link_refs: []
  replacement_copy_ref: null
  recovery_episode_refs: []
  status: OPEN
```

This layer records the operational case only.

Finance owns actual charges or payments. Risk-sharing owns coverage/claim consequences. Archives/Material Culture owns object identity, condition history and stewardship.

Lost then later recovered must preserve both episodes. A replacement copy does not retroactively become the original copy.

## 9. Interlibrary request

```yaml
interlibrary_request:
  request_id: null
  requesting_institution_id: null
  patron_or_project_ref: null
  requested_work_or_item_ref: null
  requested_at: null
  candidate_supplier_ids: []
  supplier_decision_refs: []
  selected_supplier_id: null
  fulfillment_mode: null
  status: REQUESTED
```

Possible states:
REQUESTED, SEARCHING, SUPPLIER_FOUND, APPROVED, DECLINED, UNSATISFIABLE, CANCELLED, FULFILLED.

A request does not create availability.

## 10. Interlibrary transfer

```yaml
interlibrary_transfer:
  transfer_id: null
  request_id: null
  supplying_institution_id: null
  borrowing_institution_id: null
  copy_id: null
  dispatch_event_ref: null
  logistics_shipment_ref: null
  received_event_ref: null
  patron_access_episode_ref: null
  return_dispatch_ref: null
  return_received_ref: null
  condition_before_ref: null
  condition_after_ref: null
  status: PREPARING
```

Logistics/Courier controls physical shipment and custody in transit. This layer controls the library-service relationship around that shipment.

Ownership remains with the supplying institution unless a separate authoritative transfer says otherwise.

## 11. Reading and knowledge boundary

A loan can optionally link to an observed reading episode:

```yaml
reading_access_episode:
  episode_id: null
  actor_id: null
  copy_or_content_ref: null
  access_start: null
  access_end: null
  observed_scope: null
  knowledge_update_refs: []
  interpretation_refs: []
```

The generator must not create knowledge merely because the actor possessed the book.

Permanent boundaries:
- CHECKED_OUT != READ
- READ != UNDERSTOOD
- UNDERSTOOD != BELIEVED
- BELIEVED != TRUE
- CONTENT_TRUE != ACTOR_KNOWS_IT

Actor knowledge changes only through the existing knowledge/observation authority with explicit provenance.

## 12. Privacy and retention

Circulation history can be sensitive world state.

The default recommended design is minimal retention:
- active loans and holds are operationally visible to the governing institution;
- completed circulation may compress or purge borrower-content linkage according to authored policy;
- aggregate demand can survive without exposing individual reading histories;
- lost/damaged cases may retain limited operational linkage when canon authorizes it.

Do not create a permanent omniscient list of every text every NPC ever borrowed.

## 13. Notices

Notices such as hold-available, due-soon, overdue or recall messages must use Communications.

`NOTICE_SENT != NOTICE_DELIVERED != NOTICE_READ`.

A failed message cannot silently update actor knowledge.

## 14. Minecraft representation

Minecraft/Cobblemon may render:
- a public library desk;
- shelves and reading areas;
- return chutes;
- pickup shelves;
- a small number of visible circulating books;
- book crates moving between branches;
- librarians and patrons;
- signs showing service state;
- closed stacks or conservation work;
- a rotating mobile-library stop.

Presentation remains non-authoritative.

A Minecraft book item in an inventory is not automatically a canonical library checkout.
A chest full of books is not the catalog.
An NPC standing near a shelf is not proof they borrowed or read anything.

## 15. Encounter contracts

### A. Mobile Library Route Interruption

Narrative premise: a scheduled mobile-library stop is delayed because a route segment becomes unsafe while patrons in a remote settlement are waiting for returns and holds.

FULL version requirements:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL and blocking if vehicle protection, escort, route breakthrough or displacement matter;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL for selected combat content;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if weather, road hazards or reaction windows alter the encounter;
- move-specific behavior: PARTIAL, audit exact Moves;
- abilities: PARTIAL, audit exact Abilities;
- items: PARTIAL, audit exact Items;
- Trainer Features/perks: PARTIAL, audit exact Features;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for escort/protect/breakthrough objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version: the vehicle, driver, patrons and book crates remain outside BattleSpec. AutoPTU resolves a static audited encounter blocking the route. Permitted result: `IMMEDIATE_MOBILE_LIBRARY_ROUTE_CLEAR`. World state separately decides whether service resumes and which materials arrive.

### B. Interlibrary Transfer Chokepoint

Narrative premise: a shipment carrying one or more temporary library loans is stopped by an unrelated threat.

FULL version: BLOCKED by protected-object carrying, escort, complete movement, objective-aware AI, possible hazards/reactions and semantic playback.

REDUCED version: shipment and copies remain outside BattleSpec. AutoPTU can only establish `IMMEDIATE_INTERLIBRARY_TRANSFER_ROUTE_CLEAR`. It cannot mark the transfer received or alter custody/ownership.

### C. Flooded Return Room Access

Narrative premise: returned books are physically deposited but the return-processing room becomes unsafe before staff can check them in.

FULL version: BLOCKED if rising water, hazard zones, timed rescue or protected-object recovery occur tactically.

REDUCED version: books remain world-state objects outside combat. An ordinary audited encounter may clear access and output `IMMEDIATE_RETURN_PROCESSING_ACCESS_CLEAR`. Check-in, condition assessment and conservation happen afterward.

### D. Reading Room Evacuation

Narrative premise: a public reading room must be cleared during an incident while borrowed and reference materials are still present.

FULL version: BLOCKED by civilian escort/protection, crowd movement, reactions, lifecycle and tactical policy.

REDUCED version: civilians and collection objects leave BattleSpec before initiative. AutoPTU resolves only the conventional threat and may output `IMMEDIATE_READING_ROOM_PERIMETER_CLEAR`.

## 16. PTU/Caelo boundary

Do not infer:
- General or Occult Education increases from reading;
- Scholar, Researcher, Chronicler or other Feature effects from library use;
- automatic Pokédex or identification bonuses;
- Move learning from a manual;
- Tutor effects from possession of a text;
- Skill checks for every search or checkout;
- supernatural properties of old books;
- progression from overdue returns, donations or reading volume;
- combat effects from library membership.

Exact mechanical texts, Items, Features and moves remain governed by PTU/Caelo and live AutoPTU evidence.

## 17. Generation guardrails

1. Holdings authority remains in Archives/Museums.
2. Checkout does not establish knowledge.
3. Knowledge does not establish truth.
4. Overdue does not mean stolen.
5. Lost does not mean destroyed.
6. Returned does not mean checked in.
7. Checked in does not mean available.
8. Hold requested does not mean copy reserved yet.
9. Interlibrary request does not mean supplier approval.
10. Dispatch does not mean receipt.
11. Custody does not mean ownership.
12. A replacement does not erase the original copy's history.
13. Reader history should not become omniscient surveillance by default.
14. A restricted book needs an authored access-policy reason.
15. Do not invent fees or sanctions merely to generate conflict.
16. Do not put civilians or fragile books into BattleSpec until the engine explicitly supports those tactical semantics.

## 18. Implementation priority

1. circulating copy availability state;
2. patron loan lifecycle;
3. return/check-in separation;
4. holds and renewal episodes;
5. circulation-policy versioning;
6. interlibrary request and transfer links;
7. loss/damage integration with existing object and finance layers;
8. privacy-retention policy;
9. communications notices;
10. Minecraft coarse visible state;
11. richer tactical objectives only after the missing engine capability families are verified.