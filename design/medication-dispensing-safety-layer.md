# Ouros Medication Use, Dispensing, Reconciliation & Safety Layer

Status: proposed systems design. NON-CANON. Does not establish clinical rules, medicine lists, dosing, prices or PTU mechanics.

## Purpose

This layer gives Ouros persistent operational state for medicine after a care decision exists: what was ordered, what was dispensed, what was actually administered, what records followed the patient through a transfer, what discrepancies were found, and what suspected medication-related events were investigated later.

It exists to prevent medication from collapsing into a binary `has_medicine=true` or a magical healing inventory.

Routine healthy use should compress into Chronicle. Detailed state becomes visible when a handoff, shortage, recall, discrepancy, adverse-event investigation, consent issue or persistent historical consequence matters.

## 1. Authority boundaries

This layer owns:

- medication-order identity and revision history after Care authorizes a treatment intent;
- dispensing events and recipient handoffs;
- possession/use-course history when narratively relevant;
- administration observations;
- medication-list reconciliation across transitions;
- discrepancy records;
- suspected adverse medication events as operational cases;
- allergy/intolerance labels as provenance-bearing records, not diagnoses;
- medication transition handoffs;
- returns and disposal handoffs;
- recall-to-care matching and acknowledgement;
- longitudinal medication-safety process history.

It does not own:

- diagnosis, clinical appropriateness, treatment plan or recovery -> Care/Recovery/Welfare;
- toxicological causation/exposure science -> Toxicology;
- disease/outbreak clusters -> Health Surveillance;
- manufacturing formula, production run, quality release or production recall -> Manufacturing;
- procurement, stock, storage availability or freight -> Supply Chains;
- payment -> Finance/Payments;
- professional credentials -> Credentials/Workplaces;
- physical item mechanics -> Material Culture/PTU/Caelo;
- consent/custody/partnership truth for Pokémon -> Pokémon Agency;
- battle healing, Restorative Item use, Status cure or medical Trainer Features -> PTU/Caelo + AutoPTU evidence;
- Minecraft inventory/container state as authority -> never.

## 2. Core separation

Never collapse these states:

```text
CARE_DECISION
ORDER_AUTHORED
ORDER_ACTIVE
STOCK_AVAILABLE
DISPENSED
HANDED_OVER
POSSESSED
ADMINISTRATION_DUE
ADMINISTERED_OR_USED
OBSERVED_RESPONSE
COURSE_REVIEWED
RECONCILED_AT_TRANSITION
COMPLETED_OR_STOPPED
```

Important no-inferences:

```text
ordered != dispensed
dispensed != possessed
possessed != administered
administered != effective
improved_after_use != caused_by_medicine
symptom_after_use != adverse reaction caused by medicine
adverse reaction != allergy
allergy label != verified mechanism
recall != patient exposure
recall != patient harm
medication discrepancy != medication error
medication error != intentional misconduct
stock shortage != inappropriate care
closed treatment course != biological recovery
```

## 3. MEDICATION_ORDER

A medication order is a persistent operational representation of an already-authorized care intent.

```yaml
medication_order:
  medication_order_id: null
  subject_actor_id: null
  care_plan_ref: null
  medication_or_item_ref: null
  authored_indication_ref: null
  authored_by_actor_or_role_id: null
  authored_at: null
  effective_from: null
  intended_end_or_review_window: null
  route_or_use_method_ref: null
  schedule_ref: null
  mechanical_rule_ref: null
  order_revision_id: null
  supersedes_order_revision_id: null
  status: DRAFT
  canon_state: PROPOSED
```

Suggested states:

- DRAFT
- ACTIVE
- ON_HOLD
- SUPERSEDED
- STOPPED
- COMPLETED
- CANCELLED_BEFORE_USE
- UNKNOWN_CURRENT_STATE

This file intentionally does not define dose, route vocabulary, clinical indication, frequency or duration. Those require authored Care/PTU/Caelo rules.

## 4. DISPENSING_EVENT

Dispensing records a medicine leaving an authorized stock context for an intended recipient/use context.

```yaml
dispensing_event:
  dispensing_event_id: null
  medication_order_id: null
  source_inventory_pool_id: null
  stock_batch_or_item_instance_ref: null
  dispensed_by_actor_or_role_id: null
  dispensed_at: null
  intended_recipient_actor_id: null
  handoff_actor_id: null
  quantity_ref_or_band: null
  instructions_artifact_ref: null
  mechanical_item_ref: null
  status: DISPENSED
  evidence_ids: []
```

Possible states:

- PREPARED
- DISPENSED
- HANDED_OVER
- RETURNED_UNOPENED
- CANCELLED_BEFORE_HANDOFF
- DISCREPANCY_OPEN

A dispensing event does not prove administration.

## 5. MEDICATION_COURSE

Use a course when multiple administrations or observations need persistent continuity.

```yaml
medication_course:
  medication_course_id: null
  subject_actor_id: null
  medication_order_id: null
  started_at_estimate: null
  ended_at_estimate: null
  administration_event_ids: []
  missed_or_unknown_event_ids: []
  response_observation_ids: []
  suspected_adverse_event_ids: []
  reconciliation_event_ids: []
  current_status: PLANNED
```

Suggested states:

- PLANNED
- ACTIVE
- PAUSED
- COMPLETED
- STOPPED_EARLY
- UNKNOWN

No adherence percentage is required unless a specific authored system needs it.

## 6. ADMINISTRATION_EVENT

Administration/use is an observation or authorized record, not an inferred fact from inventory loss.

```yaml
administration_event:
  administration_event_id: null
  medication_course_id: null
  subject_actor_id: null
  medication_or_item_ref: null
  stock_batch_or_item_instance_ref: null
  occurred_at: null
  observed_by_ids: []
  administered_by_actor_id: null
  self_administered: null
  cooperation_or_consent_observation_ref: null
  mechanical_execution_ref: null
  evidence_ids: []
  certainty: CONFIRMED
```

Certainty may be:

- CONFIRMED
- REPORTED
- PARTIAL_RECORD
- UNCERTAIN
- DISPUTED

An inventory decrement may support an investigation but is not sufficient by itself to create an administration event.

## 7. MEDICATION_RECONCILIATION

Reconciliation compares multiple legitimate records during a transition instead of silently choosing one.

```yaml
medication_reconciliation:
  reconciliation_id: null
  subject_actor_id: null
  transition_event_id: null
  source_record_refs: []
  compared_at: null
  compared_by_ids: []
  discrepancy_ids: []
  resulting_active_order_refs: []
  unresolved_question_ids: []
  participant_confirmation_ref: null
  status: OPEN
```

Possible transition contexts:

- HOME_TO_CLINIC
- CLINIC_TO_HOSPITAL
- HOSPITAL_TO_HOME
- FIELD_TEAM_TO_CLINIC
- TRAINER_TO_INSTITUTIONAL_CARE
- TEMPORARY_CUSTODY_TRANSFER
- REGIONAL_TRANSFER
- EVACUATION_HANDOFF

These labels are world orchestration only.

## 8. MEDICATION_DISCREPANCY

```yaml
medication_discrepancy:
  medication_discrepancy_id: null
  reconciliation_id: null
  medication_or_item_ref: null
  record_a_ref: null
  record_b_ref: null
  discrepancy_type_claim: null
  evidence_ids: []
  clinical_significance_ref: null
  cause_hypothesis_ids: []
  resolution_event_id: null
  status: OPEN
```

Candidate discrepancy labels:

- ITEM_MISSING_FROM_ONE_LIST
- DUPLICATE_ENTRY
- ORDER_STATUS_MISMATCH
- TIMING_MISMATCH
- BATCH_OR_ITEM_ID_MISMATCH
- INSTRUCTIONS_VERSION_MISMATCH
- ADMINISTRATION_RECORD_MISSING
- UNKNOWN

These are descriptive. They do not assign fault.

## 9. SUSPECTED_ADVERSE_MEDICATION_EVENT

This object records a question, not causation.

```yaml
suspected_adverse_medication_event:
  adverse_event_id: null
  subject_actor_id: null
  medication_course_ids: []
  symptom_or_change_observation_ids: []
  first_observed_at: null
  temporal_relation_notes: []
  care_case_ref: null
  toxicology_case_ref: null
  manufacturing_lot_refs: []
  alternate_hypothesis_ids: []
  causality_assessment_ref: null
  current_status: UNDER_REVIEW
```

Suggested states:

- UNDER_REVIEW
- POSSIBLY_RELATED
- UNLIKELY_RELATED
- UNRESOLVED
- REFERRED_TO_TOXICOLOGY
- REFERRED_TO_MANUFACTURING
- CLOSED_WITHOUT_CAUSAL_FINDING

The medication layer never creates a diagnosis or PTU Status from this object.

## 10. ALLERGY_OR_INTOLERANCE_LABEL

Historical labels need provenance because old records may be incomplete.

```yaml
allergy_or_intolerance_label:
  label_id: null
  subject_actor_id: null
  substance_or_item_ref: null
  label_type_claim: ALLERGY|INTOLERANCE|ADVERSE_HISTORY|UNKNOWN
  recorded_at: null
  recorded_by_ref: null
  source_event_or_document_ref: null
  reaction_description_ref: null
  verification_state: HISTORICAL_LABEL
  supersedes_label_id: null
  restriction_ref: null
```

Possible verification states:

- HISTORICAL_LABEL
- REPORTED_BY_SUBJECT_OR_CAREGIVER
- REVIEWED
- VERIFIED_BY_AUTHORED_CARE_RULE
- DISPUTED
- SUPERSEDED
- UNKNOWN

No real-world allergy testing or diagnostic logic is defined here.

## 11. RECALL_TO_CARE_HANDOFF

Manufacturing/Supply Chains own the recall and affected stock. This layer records whether an affected subject/order/course was identified and acknowledged.

```yaml
recall_to_care_handoff:
  recall_handoff_id: null
  recall_ref: null
  affected_batch_refs: []
  possible_subject_refs: []
  matching_method_ref: null
  matched_course_ids: []
  contacted_actor_ids: []
  acknowledgement_event_ids: []
  care_review_refs: []
  status: SCREENING
```

Suggested states:

- SCREENING
- NO_MATCH_FOUND
- POSSIBLE_MATCH
- MATCH_CONFIRMED
- CONTACT_PENDING
- ACKNOWLEDGED
- CARE_REVIEWED
- CLOSED

A confirmed batch match proves only that the recorded course used/received that batch when evidence supports it. It does not prove harm.

## 12. RETURN_OR_DISPOSAL_EVENT

Unused medicine can leave active possession without implying consumption.

```yaml
return_or_disposal_event:
  return_or_disposal_event_id: null
  medication_or_item_ref: null
  stock_batch_or_item_instance_ref: null
  previous_holder_id: null
  receiving_node_or_actor_id: null
  occurred_at: null
  condition_claim_ref: null
  disposition_ref: RETURNED|DISPOSED|QUARANTINED|UNKNOWN
  evidence_ids: []
  supply_chain_handoff_ref: null
```

## 13. Pokémon-specific agency safeguards

A Trainer, clinic, researcher or custodian does not obtain unlimited treatment authority merely because a Pokémon is captured, partnered, working or temporarily housed there.

When a care action can be meaningfully accepted/refused, record behavioral/communication evidence through Pokémon Agency and Care. Do not invent a numeric consent stat.

Important no-inferences:

```text
captured != blanket medical consent
custody != blanket medical consent
working role != blanket medical consent
prior cooperation != permanent cooperation
refusal != Loyalty loss
wild Pokémon accepting food/medicine once != capture eligibility
healing behavior by Chansey != institutional ownership or employment
```

Emergency exceptions, guardian authority and any incapacity rules remain canon questions, not assumptions.

## 14. Regional and technological variation

Ouros may eventually support:

- full Pokémon Centers with standardized inventory;
- small rural clinics;
- mobile field teams;
- pharmacies attached to workshops;
- berry/herbal preparation traditions;
- institutional field kits;
- emergency caches;
- remote resupply.

No option becomes canon through this file. Different systems can coexist if their mechanics and institutions are authored later.

## 15. Chronicle compression

Routine successful medication use should normally compress.

Detailed events are worth retaining when:

- a handoff creates a discrepancy;
- a recall intersects a real course;
- a patient refuses or withdraws cooperation;
- a persistent Pokémon has longitudinal care history;
- an adverse event triggers investigation;
- a shortage changes allocation;
- a delivery delay affects treatment timing;
- the same institution improves its process over years;
- a batch/provenance question connects Manufacturing to Care;
- an old record becomes relevant much later.

## 16. Minecraft projection

Allowed direction:

```text
medication world state -> coarse Minecraft presentation
```

Never:

```text
Minecraft chest contents -> medication inventory truth
bottle item in hand -> administration event
consumed animation -> clinical success
health particles -> recovery truth
NPC uniform -> prescribing authority
```

When a mechanical PTU Item exists, the adapter may project an already-authorized item action only after the battle core owns legality and effect.

## 17. Battle handoff

### In-battle medicine

Any in-battle use that heals HP, removes Status, affects Injuries, changes turn cost or invokes a Medic/Nurse/Feature depends on exact PTU implementation.

Current project evidence marks Items and Trainer Features/perks PARTIAL, and AutoPTU runtime coverage reports multiple medical Edges/Features as missing runtime mappings. Therefore this layer does not execute those effects.

### Safe reduced pattern

1. Care/Medication Use resolves legitimate treatment outside combat.
2. The world freezes the post-treatment state.
3. If an independent hostile encounter remains, create a conventional static AutoPTU battle from validated state.
4. AutoPTU returns battle results.
5. Care/Medication Use resumes afterward.

This prevents the Minecraft adapter from implementing missing healing/item/Feature rules.

## 18. Canon gates

Before enabling canonical medication systems, define:

- which care institutions exist;
- which roles can authorize/dispense/administer which authored treatments;
- which PTU Restorative Items exist in the final ruleset;
- whether humans and Pokémon use identical or different items;
- which herbal/berry preparations have mechanics;
- how Pokémon consent/cooperation is represented;
- how emergencies alter ordinary authorization;
- what medication information is private;
- what recall/quality institutions exist;
- whether any regional formulary/standard exists;
- how multiplayer custody and care decisions work.

Until then, every medication-specific worldbuilding element remains PROPOSED.