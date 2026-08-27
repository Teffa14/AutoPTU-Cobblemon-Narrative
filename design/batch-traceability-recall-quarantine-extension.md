# Ouros Batch Traceability, Recall, Quarantine & Correction Extension

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already tracks physical items, material batches, supplier fulfillment, shipments, storefront state, equipment custody, care, maintenance and notices. This extension owns a narrower post-distribution lifecycle:

signal -> scope hypothesis -> containment action -> distribution trace -> notice/recovery/correction -> effectiveness review -> closure or handoff.

The goal is to make defects, counterfeit risk, mislabelling, contamination concerns, compatibility problems and other post-distribution issues persistent without inventing a universal regulator, liability system, hidden risk score or shadow implementation of PTU item effects.

## 1. Authority boundary

This layer owns:

- emerging product/batch problem records;
- affected-scope hypotheses and revisions;
- unit/batch trace state;
- temporary hold/quarantine/recovery/correction workflow;
- notification linkage;
- recovery/reconciliation state;
- effectiveness review;
- closure record and downstream handoffs.

It does not own:

- item identity, material identity or crafting — Material Culture;
- original sourcing/order/receipt/acceptance — Procurement;
- physical transit/custody legs — Courier;
- retail/service availability — Storefront;
- treatment/medical decisions — Care;
- technical repair/installation/reopening — Facility Maintenance;
- public notice rendering — Public Notices;
- formal allegations/evidence cases — Case/Authority;
- money, refund or compensation — Finance/undecided canon;
- mechanical item effects — PTU/Caelo plus AutoPTU;
- universal consumer law or regulatory power — undecided canon.

## 2. Emerging problem

```yaml
market_problem_record:
  problem_id: null
  subject_product_or_service_refs: []
  subject_batch_ids: []
  subject_item_instance_ids: []
  first_signal_time: null
  signal_refs: []
  reporting_actor_ids: []
  observation_refs: []
  claimed_problem_types: []
  known_incident_refs: []
  causal_status: UNDETERMINED
  current_scope_revision_id: null
  current_action_ids: []
  status: OPEN
```

Suggested problem types are descriptive only:

- identity/authenticity uncertainty;
- labelling/presentation mismatch;
- visible physical defect;
- compatibility uncertainty;
- unexpected performance claim;
- suspected contamination;
- packaging integrity concern;
- missing provenance;
- component-origin concern;
- instruction/documentation error;
- other authored concern.

A problem type is not a mechanical effect.

## 3. Signals

Valid signals can include:

- inspection discrepancy;
- item-instance comparison;
- repeated customer report;
- unusual care observation;
- maintenance failure linked to a component;
- counterfeit report;
- wrong label or missing marker;
- supplier notification;
- laboratory/science result if such a system exists and supports the claim;
- battle transcript evidence for an exact implemented mechanical item behavior;
- direct observation of packaging or condition.

Unsafe inference:

- one user disliked the item, therefore the batch is defective;
- one battle loss means a held item malfunctioned;
- a low price proves counterfeit;
- damaged packaging proves contamination;
- a supplier delay proves fraud;
- a Pokémon near storage caused the problem.

## 4. Scope hypothesis

```yaml
affected_scope_revision:
  scope_revision_id: null
  problem_id: null
  parent_revision_id: null
  authored_at: null
  authored_by_ids: []
  included_product_refs: []
  included_batch_ids: []
  included_serial_or_instance_refs: []
  excluded_refs: []
  date_or_production_window_refs: []
  location_or_channel_refs: []
  evidence_refs: []
  uncertainty_refs: []
  reason_for_revision_refs: []
  status: ACTIVE
```

Scope can begin broad and become narrower, or begin narrow and expand. Earlier revisions remain historical.

## 5. Traceable unit

The system should use the most specific identity already supported by world state.

```yaml
traceable_unit_ref:
  unit_ref_id: null
  product_ref: null
  material_batch_id: null
  item_instance_id: null
  serial_or_marker_ref: null
  production_episode_ref: null
  procurement_order_ref: null
  shipment_refs: []
  current_custody_ref: null
  current_location_ref: null
  disposition_state: null
```

Not every mundane object needs an item instance or serial. Trace depth should match authored significance and available evidence.

## 6. Distribution trace

```yaml
distribution_trace:
  trace_id: null
  problem_id: null
  scope_revision_id: null
  known_unit_or_batch_refs: []
  procurement_receipt_refs: []
  courier_handoff_refs: []
  storefront_distribution_refs: []
  equipment_checkout_refs: []
  care_usage_refs: []
  facility_installation_refs: []
  found_property_refs: []
  direct_observation_refs: []
  located_refs: []
  unlocated_count_or_refs: []
  irretrievable_refs: []
  uncertainty_refs: []
  last_updated_at: null
```

Distribution trace is evidence-based. It must not omnisciently reveal every downstream holder.

## 7. Unit trace states

Suggested states:

- NOT_DISTRIBUTED;
- IN_STOCK;
- IN_TRANSIT;
- INSTALLED;
- ISSUED;
- SOLD_OR_HANDED_OFF;
- LOCATED_WITH_HOLDER;
- RETURNED;
- QUARANTINED;
- CORRECTED;
- CLEARED;
- CONSUMED_OR_USED;
- DESTROYED_OR_DISPOSED_BY_OWNING_SYSTEM;
- UNLOCATED;
- UNKNOWN.

The narrative layer should prefer `UNKNOWN` over fabricated certainty.

## 8. Market action

```yaml
market_action:
  action_id: null
  problem_id: null
  scope_revision_id: null
  action_type: null
  initiated_by_ids: []
  authority_or_mandate_refs: []
  target_unit_or_batch_refs: []
  affected_location_refs: []
  initiated_at: null
  notice_refs: []
  downstream_handoff_refs: []
  status: ACTIVE
```

Useful authored action types:

- INFORMATION_ALERT;
- STOP_DISTRIBUTION;
- HOLD_PENDING_REVIEW;
- QUARANTINE;
- RECOVER_FROM_CIRCULATION;
- CORRECT_IN_PLACE;
- REPLACE_COMPONENT;
- RELABEL_OR_DOCUMENT_CORRECTION;
- CLEAR_FOR_USE_OR_DISTRIBUTION;
- OTHER_AUTHORED_ACTION.

These names are system vocabulary, not assumed Ouros legal terminology.

## 9. Hold versus quarantine

A hold is a temporary “do not release/use yet” state while evidence is incomplete.

A quarantine adds an explicit separation/location requirement authored by an institution or other valid authority.

Neither state proves the item is defective.

```yaml
containment_record:
  containment_id: null
  action_id: null
  unit_or_batch_refs: []
  containment_location_id: null
  custody_refs: []
  started_at: null
  access_restriction_refs: []
  review_trigger_refs: []
  release_or_transfer_ref: null
  status: ACTIVE
```

## 10. Authenticity review

```yaml
authenticity_review:
  review_id: null
  subject_refs: []
  expected_reference_refs: []
  provenance_refs: []
  physical_observation_refs: []
  identifier_check_refs: []
  specialist_actor_ids: []
  specialist_qualification_refs: []
  outcome: null
  uncertainty_refs: []
```

Suggested outcomes:

- AUTHENTIC_SUPPORTED;
- COUNTERFEIT_SUPPORTED;
- MISMATCH_CONFIRMED;
- INSUFFICIENT_EVIDENCE;
- FURTHER_REVIEW_REQUIRED.

Do not use a hidden authenticity percentage.

## 11. Corrective action

Correction can happen without full recovery if the unit can safely remain with its current custodian and canon supports that procedure.

```yaml
product_correction_event:
  correction_id: null
  action_id: null
  item_or_batch_refs: []
  correction_type: null
  performed_by_ids: []
  performed_at: null
  repair_work_order_refs: []
  replacement_component_refs: []
  documentation_revision_refs: []
  inspection_refs: []
  post_correction_status: null
```

Examples:

- replace a component;
- update instructions;
- relabel a container;
- correct packaging;
- apply an approved software/configuration fix if digital-system canon supports it;
- send item to Maintenance/workshop for repair.

## 12. Recovery event

```yaml
recovery_event:
  recovery_event_id: null
  action_id: null
  unit_or_batch_refs: []
  recovered_from_actor_or_location_id: null
  recovered_by_id: null
  custody_event_refs: []
  received_at_location_id: null
  observed_condition_refs: []
  disposition_handoff_refs: []
  completed_at: null
```

Recovery does not determine refund, compensation, guilt or final disposition.

## 13. User/holder notification

This layer references Communications/Public Notices rather than implementing delivery.

```yaml
affected_holder_notice_packet:
  notice_packet_id: null
  action_id: null
  intended_recipient_refs: []
  public_notice_ref: null
  direct_message_refs: []
  posted_surface_refs: []
  language_or_accessibility_refs: []
  delivery_evidence_refs: []
  acknowledgement_refs: []
  followup_refs: []
```

Sent is not received. Received is not understood. Public posting is not individual acknowledgement.

## 14. Storefront and service handoff

A market action can affect availability without this layer owning the shop.

```yaml
storefront_market_action_handoff:
  action_id: null
  storefront_id: null
  affected_stock_refs: []
  recommended_availability_state_ref: null
  replacement_stock_dependency_refs: []
  public_notice_refs: []
```

Storefront decides what remains sellable/available under its own state and approved authority.

## 15. Care handoff

Care owns health decisions.

If a medicine, food product, treatment device or care supply is affected, this layer may identify:

- exact batch/item references;
- known usage events;
- holders/locations where privacy permits;
- availability consequences;
- action notices.

It may not create diagnosis, adverse effect, healing, Injury, status, dosage, treatment or medical causation.

## 16. Maintenance handoff

For installed components or equipment:

- locate the exact affected component where possible;
- freeze further installation if warranted by valid authority;
- create or reference work orders;
- preserve pre/post-correction identity;
- require technical verification before reopening when the owning Maintenance layer says so.

A recall closure and a facility closure are related states, not the same state.

## 17. Procurement handoff

Recall can create a replacement need.

```yaml
replacement_need_handoff:
  problem_id: null
  action_id: null
  affected_need_or_service_refs: []
  removed_or_unavailable_quantity_refs: []
  replacement_specification_refs: []
  urgency_claim_refs: []
  procurement_need_ref: null
```

This extension never selects a replacement supplier or invents substitute mechanical items.

## 18. Effectiveness review

```yaml
market_action_effectiveness_review:
  review_id: null
  action_id: null
  scope_revision_id: null
  expected_trace_population_refs: []
  located_refs: []
  recovered_refs: []
  corrected_refs: []
  cleared_refs: []
  unresolved_refs: []
  notice_delivery_evidence_refs: []
  downstream_service_refs: []
  uncertainty_refs: []
  outcome: null
  reviewed_at: null
```

Suggested outcomes:

- EFFECTIVE_WITH_COMPLETE_TRACE;
- EFFECTIVE_WITH_DOCUMENTED_UNRESOLVED_UNITS;
- PARTIALLY_EFFECTIVE;
- FURTHER_ACTION_REQUIRED;
- SCOPE_REVISION_REQUIRED;
- INSUFFICIENT_EVIDENCE.

No arbitrary completion percentage is required.

## 19. Closure

```yaml
market_problem_closure:
  closure_id: null
  problem_id: null
  final_scope_revision_id: null
  final_action_ids: []
  root_cause_claim_refs: []
  root_cause_evidence_refs: []
  final_unresolved_refs: []
  correction_or_process_change_refs: []
  public_correction_refs: []
  downstream_handoff_refs: []
  closed_by_ids: []
  closed_at: null
  closure_status: null
```

Closure may state that root cause remains unknown. That is valid.

## 20. Historical persistence

After closure, the world can remember:

- a supplier changed packaging;
- a workshop added an inspection step;
- a shop keeps one old notice in an archive;
- a clinic changed where replacement stock is stored;
- a buyer changed its specification;
- a once-missing unit was found months later;
- counterfeit examples remain in a teaching collection if custody/authority permits;
- an NPC still distrusts a product based on what they personally observed.

This history cannot grant automatic social or mechanical modifiers.

## 21. Counterfeit versus defect

Counterfeit identity and product defect are separate dimensions.

An authentic unit can be defective.
A counterfeit unit can appear functional.
An uncertain unit can remain on hold without either conclusion.
A corrected authentic unit remains historically linked to its correction.

## 22. Mystery grammar

A strong investigation can begin with:

- three failures that appear to share a batch but do not;
- two differently labelled containers from one production episode;
- a counterfeit item carrying a real serial copied from an authentic unit;
- one store with affected stock and another with an older safe batch;
- an apparent recall failure that is actually forwarding/custody drift;
- a component replaced during a previous repair, breaking the assumed installation history;
- a complaint cluster generated by one repeated source rather than independent incidents.

The solution should emerge from provenance, distribution history, observations and actor knowledge.

## 23. Minecraft/Cobblemon representation

Useful visible projections include:

- taped/blocked shelf segment;
- quarantine chest or storage cage;
- changed sign/notice;
- missing product props;
- replacement component crate;
- collection bin;
- workstation inspection props;
- NPC routine changed from sales to inventory review;
- a closed service desk with redirect information.

The visible object reflects authoritative state. Breaking the sign or moving a decorative crate does not clear a recall.

## 24. Encounter: Warehouse Recovery Window

Narrative premise:

A distribution depot has several affected containers in known zones, but a Pokémon disturbance or other legitimate battle threat prevents staff from completing retrieval.

Full version wants:

- staff withdrawal while recovery zones remain protected;
- multiple item locations;
- changing access lanes;
- possible unstable shelving or hazard zones;
- interception/forced movement around exits;
- objective-aware AI for WITHDRAW/CLEAR_ROUTE/PROTECT;
- adapter/playback preserving which zones were reached before combat ended.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including forced movement/interception — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Staff first move every affected container they can safely reach into quarantined world-state storage and evacuate. Any unresolved zones stay marked `UNLOCATED_OR_INACCESSIBLE`. AutoPTU receives a static conventional arena with no recoverable products on the tactical grid. After battle, staff resume trace/recovery. Victory does not magically locate or recover remaining units.

## 25. Encounter: Counterfeit Workshop Lockdown

Narrative premise:

A workshop or storage room contains a mixture of authentic and suspect equipment while an unrelated active Pokémon threat forces evacuation.

Full version wants:

- protected evidence/storage zones;
- multiple exits;
- actors trying to withdraw rather than KO;
- possibly fragile equipment and dynamic access;
- tactical AI that understands escape/protection.

Dependencies match the rich families above, especially BLOCKING complete movement, environment/reactions, tactical AI and adapter/playback.

Reduced version:

All evidence and suspect items are sealed into world state before battle. Workers evacuate. AutoPTU resolves the threat in a static cleared room. Authenticity review happens afterward and is unaffected by who won the battle.

## 26. Non-combat encounter: Six Units, Five Locations

A trace ledger says six units left a supplier. Procurement and Courier records prove five downstream locations. The sixth may have been consolidated, redirected, installed under a component record, returned without a matching handoff, or remain genuinely unlocated.

The encounter uses:

- procurement receipts;
- courier handoffs;
- storefront issue/sale observations if available;
- equipment checkout;
- maintenance installation history;
- actor testimony;
- time and provenance.

No battle mechanics are required.

## 27. Rule-facing mechanical boundary

A mechanically defined item remains governed by PTU/Caelo and AutoPTU.

Narrative recall state can make an item unavailable in world state only when the owning inventory/service system recognizes that action. It cannot:

- weaken the item's battle effect;
- add a malfunction chance;
- change held-item timing;
- create poison/Burn/status;
- alter Accuracy or damage;
- alter initiative;
- modify movement;
- create an Ability suppression effect;
- create a fake item with custom mechanics;
- make AI avoid or prefer the item.

A mechanically distinct counterfeit/defective variant requires explicit approved rules and engine support.

## 28. Canon questions left open

- Which institutions, if any, can issue a market action in each Ouros region?
- Are recalls voluntary, contractual, professional, civic, regulatory or mixed?
- What categories of goods use lot, serial, maker or provenance marks?
- How are medicinal products governed?
- What privacy restrictions apply when tracing care usage?
- Who can order quarantine or destruction?
- Are corrections in place culturally/technically common?
- Which notices must be public versus direct?
- Are refunds, replacements or compensation customary or legally required?
- What digital tracking technology exists, if any?
- How much traceability should Minecraft materialize physically?

None of these are answered by this extension.

## 29. Canon status

Everything in this file is proposed systems design.

No Ouros regulator, recall law, product class, medicine rule, liability regime, notification duty, technology or institution is promoted to canon.
