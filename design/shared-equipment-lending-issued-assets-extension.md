# Shared Equipment, Lending & Issued Assets Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already knows what a persistent object is, who owns or currently holds it, which workplace assigned a task, which facility can repair it and which route can transport it. This extension adds the temporary-use lifecycle between those systems.

It is intended for shared tools, field kits, loaner devices, protective equipment, event gear, research instruments, institutional keys and other reusable physical resources whose availability changes as different people use them.

It does not create a universal rental economy. It does not define property law. It does not model Pokémon as assets.

## 1. Authority boundaries

### Material Culture owns object identity

Every story-significant physical asset should reference the existing `item_instance` when one exists. Material Culture remains authoritative for owner, custodian, provenance, repairs, significance and mechanical item reference.

Pass 69 owns temporary entitlement, reservation, checkout, assignment and return state.

### Workplaces / Education own role and assignment

A job, class, expedition or training exercise may justify access to equipment. Those systems decide the assignment and qualification claim. Pass 69 records what resource was allocated to that assignment.

Receiving equipment cannot grant a role, qualification, Skill, Edge, Trainer Feature or legal authority.

### Maintenance owns readiness work

If an asset needs inspection, repair or facility support, Pass 69 changes its pool availability and references Maintenance. It does not resolve the technical work itself.

### Found Property and Case own exceptions

An item unexpectedly separated from its expected holder can hand off to Found Property. Evidence of tampering, theft, fraud or prohibited access can hand off to Case/Authority.

Overdue or missing alone is not proof of misconduct.

### Library circulation remains specialized

Books and other authored copy instances continue to use the library/publication circulation layer. Pass 69 should not duplicate their checkout state.

### Courier owns intentional transport

Moving a kit between depots can create a shipment. Pass 69 tracks whether the pool is waiting for that resource; Courier tracks its physical transit.

### Finance owns money and risk

Prices, deposits, replacement charges, insurance, fines and subsidies require established world rules. Pass 69 may reference a Finance record if one exists. It never invents those terms.

### Pokémon Agency owns Pokémon participation

A Pokémon is never an `asset_instance`, `loanable_asset`, inventory unit or equipment-pool member in this extension.

Any service involving a Pokémon routes to Pokémon Agency plus the relevant Travel, Workplace or Battle Institution layer.

## 2. Shared asset pool

```yaml
shared_asset_pool:
  pool_id: null
  owner_institution_id: null
  managing_workplace_id: null
  home_location_id: null
  supported_node_ids: []
  asset_instance_ids: []
  asset_class_refs: []
  access_policy_ref: null
  current_pool_state: ACTIVE
  availability_summary: null
  reservation_ids: []
  checkout_ids: []
  reconciliation_event_ids: []
  history_event_ids: []
```

Suggested pool states:

- ACTIVE
- LIMITED
- TEMPORARILY_UNAVAILABLE
- RECONCILING
- RELOCATING
- CLOSED_FOR_INSPECTION
- RETIRED

A pool state describes access to the collection. It does not alter the condition or ownership of every individual object.

## 3. Loanable asset reference

```yaml
loanable_asset:
  loanable_asset_id: null
  pool_id: null
  item_instance_id: null
  asset_class_ref: null
  home_node_id: null
  current_node_id: null
  availability_state: AVAILABLE
  readiness_record_ref: null
  active_reservation_id: null
  active_checkout_id: null
  restriction_refs: []
  last_reconciliation_event_id: null
```

Suggested availability states:

- AVAILABLE
- RESERVED
- CHECKOUT_PENDING
- CHECKED_OUT
- RETURN_PENDING
- INSPECTION_PENDING
- MAINTENANCE
- INCOMPLETE
- IN_TRANSIT
- UNACCOUNTED_FOR
- RETIRED

`UNACCOUNTED_FOR` means expected location or custody is unresolved. It does not mean stolen.

## 4. Access entitlement

Access should be represented separately from custody.

```yaml
asset_access_entitlement:
  entitlement_id: null
  holder_actor_id: null
  holder_group_id: null
  pool_id: null
  asset_class_refs: []
  source_assignment_id: null
  source_role_id: null
  source_institution_id: null
  valid_from: null
  valid_until: null
  location_scope_ids: []
  project_scope_ids: []
  restriction_refs: []
  state: ACTIVE
```

An entitlement can support a request or reservation. It does not itself prove that an exact item has been handed over.

Possible states:

- PLANNED
- ACTIVE
- SUSPENDED
- EXPIRED
- WITHDRAWN
- COMPLETED

The extension must preserve provenance for why the entitlement exists.

## 5. Reservation

```yaml
asset_reservation:
  reservation_id: null
  requester_id: null
  pool_id: null
  requested_asset_class_ref: null
  requested_item_instance_id: null
  source_entitlement_id: null
  needed_from: null
  needed_until: null
  pickup_node_id: null
  assignment_ref: null
  priority_claim_ref: null
  state: REQUESTED
  substitution_allowed: null
  fulfilled_item_instance_id: null
```

Suggested states:

- REQUESTED
- HELD
- WAITLISTED
- PARTIALLY_FULFILLED
- READY_FOR_PICKUP
- FULFILLED
- WITHDRAWN
- EXPIRED
- UNAVAILABLE

A reservation does not create custody. A waitlist does not imply entitlement priority unless an established policy says so.

## 6. Checkout and custody event

```yaml
asset_checkout:
  checkout_id: null
  item_instance_id: null
  pool_id: null
  issued_to_actor_id: null
  issued_to_group_id: null
  issuing_actor_id: null
  source_entitlement_id: null
  source_reservation_id: null
  assignment_ref: null
  checkout_node_id: null
  checked_out_at: null
  expected_return_window: null
  observed_condition_at_issue: null
  included_component_refs: []
  usage_scope_refs: []
  current_state: ACTIVE
  handoff_event_ids: []
```

Suggested states:

- PREPARING
- ACTIVE
- HANDED_OFF
- RETURN_DUE
- RETURN_PENDING
- RETURNED
- EXCEPTION_OPEN
- CLOSED

Checkout should update the object's current custodian through Material Culture's existing authority model.

Ownership remains unchanged unless an independently authorized transfer exists.

## 7. Handoff inside an active checkout

A team may pass one instrument between members without returning it to the institution.

```yaml
asset_handoff_event:
  handoff_id: null
  checkout_id: null
  item_instance_id: null
  from_custodian_id: null
  to_custodian_id: null
  location_id: null
  occurred_at: null
  observed_condition: null
  source_refs: []
```

This event records custody continuity. It does not infer responsibility for earlier damage.

## 8. Return lifecycle

```yaml
asset_return:
  return_id: null
  checkout_id: null
  item_instance_id: null
  returned_by_actor_id: null
  receiving_actor_id: null
  return_node_id: null
  returned_at: null
  observed_condition_at_return: null
  observed_component_refs: []
  discrepancy_claim_ids: []
  next_state: INSPECTION_PENDING
  verification_ref: null
```

Physical return and readiness are separate.

A returned asset can remain unavailable while it is:

- inspected;
- inventoried;
- cleaned;
- recharged;
- repaired;
- recalibrated where canon establishes calibration;
- moved back to another node;
- reconciled against missing components.

Pass 69 only records these dependencies. The governing technical system owns their rules.

## 9. Condition observations

Condition should be observational unless an authoritative technical record exists.

```yaml
asset_condition_observation:
  observation_id: null
  item_instance_id: null
  observer_id: null
  location_id: null
  observed_at: null
  observable_descriptors: []
  photo_or_record_refs: []
  technical_assessment_ref: null
  source_refs: []
```

Statements such as `case scratched`, `strap absent`, `indicator dark` or `seal already marked` can be observations.

They do not automatically prove:

- mechanical damage;
- who caused the condition;
- when it happened;
- whether the item is unsafe;
- whether a mechanical item effect is disabled.

## 10. Pool reconciliation

```yaml
asset_pool_reconciliation:
  reconciliation_id: null
  pool_id: null
  started_at: null
  completed_at: null
  expected_item_instance_ids: []
  observed_item_instance_ids: []
  unresolved_item_ids: []
  unexpected_item_ids: []
  record_discrepancy_ids: []
  linked_found_property_ids: []
  linked_case_ids: []
  result_state: OPEN
```

Possible outcomes:

- MATCHED
- RECORD_CORRECTION_REQUIRED
- LOCATION_UPDATE_REQUIRED
- RETURN_STILL_OPEN
- FOUND_PROPERTY_HANDOFF
- CASE_HANDOFF
- MAINTENANCE_HANDOFF
- UNRESOLVED

Reconciliation is valuable because an apparent shortage may come from a stale record, transfer between nodes, incomplete return or wrong case before it becomes a misconduct story.

## 11. Substitution

A reservation may be fulfilled by another approved asset instance or asset class when an established policy allows it.

```yaml
asset_substitution:
  substitution_id: null
  reservation_id: null
  requested_ref: null
  offered_ref: null
  decision_actor_id: null
  policy_ref: null
  accepted: null
  mechanical_equivalence_verified: false
  notes_claim_ids: []
```

Narrative similarity does not prove mechanical equivalence.

A substitute can be operationally suitable for a narrative task while still requiring separate PTU/Caelo validation if its mechanics matter.

## 12. Availability as a world-state consequence

A pool can become LIMITED because:

- several assets are already checked out;
- an upcoming event has reserved them;
- a return is waiting for inspection;
- one exact item is in Maintenance;
- resources are at another node;
- a shipment is delayed;
- the managing workplace is unstaffed;
- a facility outage prevents readiness work;
- the access policy has changed through an established authority.

The cause should be traceable to owning state. Do not invent arbitrary scarcity to force a quest.

## 13. Minecraft representation

The adapter may eventually project:

- labelled storage positions;
- empty or occupied rack slots;
- a pickup counter;
- a return bin or desk where canon supports it;
- visible cases or tool props;
- an interaction showing AVAILABLE/RESERVED/INSPECTION_PENDING;
- the exact item instance when persistence matters.

Required authority direction:

narrative/material state -> asset-pool projection -> Minecraft object/UI.

Moving a decorative prop in Minecraft must not silently change ownership or checkout records.

A player physically holding an item in Minecraft must not become its owner merely because the client inventory contains it.

## 14. Pokémon boundary

Hard prohibition:

```text
Pokemon actor -> NEVER shared_asset_pool.asset_instance_ids
```

A Ride Pokémon, working Pokémon, partner Pokémon, nursery resident, fostered Pokémon or battle participant remains an actor with its own relationship/custody/agency state.

If access to a Pokémon-assisted service is temporary, store the service entitlement under its owning system. Do not repurpose this equipment schema.

## 15. Mechanical item boundary

A narrative loan can exist even when the item's PTU implementation is incomplete.

For noncombat use, the object can remain a world-state prop with no invented bonus.

For battle use, the encounter contract must verify:

- exact mechanical item identity;
- legal holder/target semantics;
- activation timing;
- action/frequency limits;
- status/damage/move interactions;
- lifecycle hooks;
- transcript events;
- AI handling;
- adapter playback.

Until those contracts exist, keep the asset outside tactical resolution.

## 16. Compression rule

Routine checkout and return should compress when:

- the entitlement is clear;
- the asset is available;
- no meaningful discrepancy exists;
- no player decision intersects allocation;
- no mechanical execution depends on the object.

Expand the lifecycle when scarcity, conflicting assignments, condition, identity, delayed return, a route change or a meaningful relationship makes the handoff matter.

## 17. Integration handoffs

Use explicit handoffs rather than absorbing adjacent systems:

- damaged or inspection-dependent asset -> Facility Maintenance;
- unexpected lost object -> Found Property;
- suspected tampering/prohibited access -> Case/Authority;
- transfer between nodes -> Courier/Travel;
- staffing blocker -> Workplaces;
- funding/deposit/replacement-cost question -> Finance;
- event reservation -> Event Operations;
- research kit -> Science;
- expedition allocation -> Travel/Expedition;
- publication copy -> Library circulation;
- Pokémon-assisted service -> Pokémon Agency plus service owner.

## 18. Generation rules

Generated equipment hooks must originate from existing state such as a real assignment, pool shortage, reservation collision, incomplete return, maintenance hold, node transfer, record discrepancy or player request.

Do not generate a crisis merely because a shared object exists.

Do not assume a borrowing culture, rental business, fee, deposit or penalty until canon establishes one.

Do not infer negligence from lateness.

Do not infer theft from absence.

Do not infer mechanical competence from possession.

Do not infer ownership from custody.

## 19. Canon review questions

Before promoting a concrete shared-equipment service, canon review should answer:

- Which institutions own reusable pools?
- Which asset classes are normally shared?
- Which locations act as pickup/return nodes?
- What evidence establishes eligibility or qualification?
- Are reservations used, and by whom?
- Are due windows customary or formal?
- Which inspections are required before reissue?
- What records are public, internal or private?
- Do fees, deposits, fines or replacement charges exist?
- What happens when equipment is not returned?
- Which items are mechanically represented by PTU/Caelo and AutoPTU?

Until reviewed, concrete names, procedures and institutions remain PROPOSED.