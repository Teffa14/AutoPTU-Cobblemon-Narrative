# After-Sale Return, Warranty, Repair & Replacement Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon.

## Purpose

This extension preserves the history of non-living goods after acquisition when an item later enters a provider-facing service episode: return request, exchange, warranty/guarantee review, diagnosis, repair, replacement, temporary loan, reissue or refund handoff.

It fills the gap between an original sale/procurement event and existing technical, logistical and financial owners. It does not create universal consumer law or a second item/repair/economy system.

Pokémon and other living actors are excluded. They remain governed by Pokémon Agency, care, custody and relationship systems. A Pokémon can never be a returnable product, warranty unit, replacement asset or loaner under this extension.

## 1. Authority boundary

This extension owns:

- the after-sale service case;
- the customer's/provider's recorded claims about the problem;
- return/exchange request chronology;
- reference to the promise/policy/agreement being invoked;
- remedy eligibility decision provenance when an authored provider has such a process;
- linkage among diagnosis, repair, replacement, loaner and refund handoffs;
- reopen/repeat-failure history;
- closure reason.

It does not own:

- item identity, physical condition or repair provenance — Material Culture;
- storefront opening or service availability — Commercial Services;
- original institutional sourcing/acceptance — Procurement;
- shipment movement/custody legs — Courier;
- money, refund settlement or credit — Finance;
- negotiated obligations/disputes — Agreements/Mediation;
- batch recall/quarantine — Batch Traceability/Recall;
- insurance/risk-transfer claims — Insurance extension, when canon-enabled;
- temporary shared-asset ownership — Shared Equipment or another authored asset owner;
- evidence custody — Case/Authority/Custody;
- mechanical Item effects, crafting or repair legality — PTU/Caelo/AutoPTU;
- legal rights or regulatory authority — unresolved canon unless explicitly authored.

## 2. After-sale service case

```yaml
after_sale_case:
  case_id: null
  requester_actor_or_institution_id: null
  provider_actor_or_institution_id: null
  service_node_id: null
  item_instance_ids: []
  item_type_refs: []
  acquisition_event_refs: []
  procurement_order_refs: []
  invoked_promise_or_policy_refs: []
  service_contract_refs: []
  symptom_report_ids: []
  intake_event_ids: []
  inspection_or_diagnosis_refs: []
  remedy_decision_ids: []
  repair_refs: []
  replacement_refs: []
  exchange_refs: []
  loaner_refs: []
  finance_handoff_refs: []
  courier_handoff_refs: []
  recall_refs: []
  dispute_refs: []
  status: OPEN
  opened_at: null
  closed_at: null
  closure_reason: null
  canon_refs: []
```

Suggested states:

- OPEN
- CLARIFICATION_REQUIRED
- RETURN_REQUESTED
- RETURN_AUTHORIZED
- AWAITING_ITEM
- ITEM_RECEIVED
- ASSESSMENT_PENDING
- REMEDY_REVIEW
- REPAIR_IN_PROGRESS
- REPLACEMENT_PENDING
- EXCHANGE_PENDING
- REFUND_HANDOFF
- AWAITING_CUSTOMER_PICKUP
- AWAITING_RETURN_SHIPMENT
- RESOLVED
- CLOSED_WITHOUT_REMEDY
- DISPUTED
- REOPENED

These labels describe world-state workflow only. They grant no PTU mechanical effect.

## 3. Service promise / policy reference

No provider receives a warranty policy by default.

```yaml
after_sale_promise_reference:
  promise_ref_id: null
  provider_id: null
  source_type: authored_policy|transaction_term|agreement|service_contract|spoken_claim_record|institution_rule|other
  source_record_id: null
  effective_from: null
  effective_until: null
  covered_item_or_service_refs: []
  scope_claim_refs: []
  limitation_claim_refs: []
  available_remedy_refs: []
  evidence_requirement_refs: []
  transferability_claim_ref: null
  superseded_by_ref: null
  status: ACTIVE
```

A policy version must remain historically inspectable after supersession.

`CURRENT_POLICY != POLICY_GOVERNING_OLD_TRANSACTION`.

This object records what a source says. It does not create legal enforceability.

## 4. Problem report

```yaml
after_sale_problem_report:
  report_id: null
  case_id: null
  reporter_id: null
  reported_item_instance_id: null
  reported_symptoms: []
  reported_failure_time: null
  first_observed_time: null
  use_context_claim_refs: []
  prior_repair_refs: []
  supporting_evidence_refs: []
  uncertainty_refs: []
  recorded_at: null
```

A report can be sincere and inaccurate.

`SYMPTOM_REPORTED != DEFECT_CONFIRMED`.

Do not infer misuse, deception or negligence from a mismatch.

## 5. Return request and authorization

```yaml
return_request:
  return_request_id: null
  case_id: null
  requester_id: null
  requested_item_instance_ids: []
  requested_remedy_refs: []
  stated_reason_refs: []
  request_time: null
  provider_response_ref: null
  status: REQUESTED
```

```yaml
return_authorization:
  authorization_id: null
  return_request_id: null
  authorizing_actor_or_institution_id: null
  authority_basis_ref: null
  accepted_item_instance_ids: []
  handoff_location_ref: null
  courier_arrangement_refs: []
  effective_window: null
  limitations: []
  status: AUTHORIZED
```

Authorization permits an authored return process to proceed. It does not prove physical handoff.

`RETURN_REQUESTED != RETURN_AUTHORIZED`.

`RETURN_AUTHORIZED != ITEM_HANDED_OVER`.

## 6. Intake event

```yaml
after_sale_intake:
  intake_id: null
  case_id: null
  item_instance_id: null
  receiving_actor_or_institution_id: null
  custody_event_ref: null
  received_at: null
  observed_condition_refs: []
  included_component_refs: []
  missing_component_claims: []
  packaging_observation_refs: []
  evidence_packet_refs: []
  intake_status: RECEIVED_PENDING_ASSESSMENT
```

The intake record reflects what was received and observed at that time.

`ITEM_HANDED_OVER != PROVIDER_RECEIPT_PROCESSED`.

`ITEM_RECEIVED != DEFECT_CONFIRMED`.

## 7. Diagnosis / assessment reference

Material Culture or another exact technical owner controls actual repair/condition semantics.

```yaml
after_sale_assessment_link:
  assessment_link_id: null
  case_id: null
  item_instance_id: null
  assessor_id: null
  assessor_authorization_refs: []
  technical_record_refs: []
  symptom_confirmed: null
  defect_claim_refs: []
  cause_claim_refs: []
  confirmed_cause_refs: []
  repairability_claim_ref: null
  mechanics_validation_refs: []
  assessed_at: null
```

The after-sale layer only links the technical result into the customer-service chronology.

`DEFECT_CONFIRMED != CAUSE_ESTABLISHED`.

`CAUSE_ESTABLISHED != PROVIDER_RESPONSIBILITY_ESTABLISHED`.

## 8. Remedy eligibility decision

```yaml
remedy_eligibility_decision:
  decision_id: null
  case_id: null
  decision_actor_ids: []
  authority_basis_refs: []
  promise_or_policy_revision_refs: []
  transaction_refs: []
  evidence_considered_refs: []
  technical_assessment_refs: []
  uncertainty_refs: []
  eligible_remedy_refs: []
  excluded_remedy_refs: []
  decision_state: null
  decision_time: null
  explanation_claim_ref: null
```

Possible descriptive states:

- ELIGIBLE
- PARTIALLY_ELIGIBLE
- INELIGIBLE_UNDER_REFERENCED_PROMISE
- MORE_INFORMATION_REQUIRED
- OUTSIDE_PROVIDER_SCOPE
- REFER_TO_OTHER_PROVIDER
- DISPUTED

No state is a legal judgment unless a separate canon-approved authority owns that judgment.

`DEFECT_CONFIRMED != REMEDY_ELIGIBLE`.

`REMEDY_ELIGIBLE != REMEDY_SELECTED`.

## 9. Remedy selection

```yaml
remedy_selection:
  remedy_selection_id: null
  case_id: null
  offered_remedy_refs: []
  requester_preference_refs: []
  provider_selection_ref: null
  governing_promise_refs: []
  selected_remedy: repair|replacement|exchange|refund_handoff|reissue|return_without_work|other
  selection_time: null
  downstream_owner_refs: []
```

If the applicable promise does not define who chooses among alternatives, the narrative generator must not invent that authority.

## 10. Repair episode linkage

```yaml
after_sale_repair_link:
  case_id: null
  item_instance_id: null
  material_culture_repair_record_ids: []
  workshop_id: null
  started_at: null
  technical_completion_ref: null
  verification_ref: null
  release_ref: null
  customer_notification_ref: null
```

`REPAIR_STARTED != REPAIR_COMPLETED`.

`REPAIR_COMPLETED != QUALITY_CHECK_PASSED`.

`QUALITY_CHECK_PASSED != ITEM_RETURNED_TO_HOLDER`.

No new repair formula exists here.

## 11. Replacement episode

```yaml
replacement_episode:
  replacement_id: null
  case_id: null
  original_item_instance_id: null
  replacement_item_type_ref: null
  replacement_item_instance_id: null
  allocation_event_ref: null
  availability_state: null
  issue_event_ref: null
  original_return_requirement_ref: null
  original_return_event_ref: null
  ownership_handoff_refs: []
  courier_refs: []
  status: PENDING
```

Possible states:

- APPROVED_PENDING_ALLOCATION
- ALLOCATED
- AWAITING_STOCK
- READY_FOR_ISSUE
- ISSUED
- ORIGINAL_RETURN_PENDING
- COMPLETE
- CANCELLED

`REPLACEMENT_APPROVED != REPLACEMENT_AVAILABLE`.

`REPLACEMENT_AVAILABLE != REPLACEMENT_ISSUED`.

`REPLACEMENT_ISSUED != ORIGINAL_RETURNED`.

A replacement is a distinct item instance unless the underlying owner explicitly models a repaired original.

## 12. Exchange episode

```yaml
exchange_episode:
  exchange_id: null
  case_id: null
  surrendered_item_instance_id: null
  surrendered_custody_event_ref: null
  issued_item_instance_id: null
  issued_custody_or_ownership_event_ref: null
  exchange_basis_ref: null
  functional_difference_refs: []
  mechanical_validation_refs: []
  completed_at: null
```

Rydel-like exchange is an optional authored service pattern, never a universal rule.

`EXCHANGE_ACCEPTED != EXCHANGE_COMPLETED`.

`SAME_PROVIDER != SAME_ITEM_INSTANCE`.

## 13. Temporary loaner

```yaml
temporary_loaner_episode:
  loaner_episode_id: null
  case_id: null
  loaner_asset_id: null
  provider_owner_ref: null
  recipient_id: null
  custody_issue_ref: null
  expected_return_trigger_ref: null
  actual_return_ref: null
  condition_observation_refs: []
  status: ACTIVE
```

`LOANER_ISSUED != OWNERSHIP_TRANSFERRED`.

A loaner must use an existing asset/custody owner. This extension only links it to the service case.

## 14. Refund handoff

```yaml
refund_handoff:
  refund_handoff_id: null
  case_id: null
  authorization_ref: null
  finance_transaction_ref: null
  reason_ref: null
  requested_at: null
  authorized_at: null
  settled_at: null
```

Finance remains authoritative for money.

`REFUND_AUTHORIZED != REFUND_SETTLED`.

`ITEM_RETURNED != REFUND_SETTLED`.

## 15. Recall interaction

An individual case can intersect a batch recall, but the states remain separate.

```yaml
after_sale_recall_link:
  case_id: null
  item_instance_id: null
  recall_event_ref: null
  inclusion_evidence_refs: []
  recall_remedy_handoff_refs: []
```

`RECALL_ACTIVE != THIS_UNIT_DEFECTIVE`.

`RECALL_CASE != WARRANTY_CASE`.

`ITEM_FROM_AFFECTED_BATCH != ITEM_CAUSED_REPORTED_SYMPTOM`.

## 16. Insurance interaction

If and only if insurance/risk transfer is later canon-enabled, one incident may have both an after-sale service case and a coverage claim.

They remain separate.

A seller repairing an item does not prove insurance coverage. An insurer paying a claim does not prove the seller admitted a defect.

## 17. Repeat failure and reopening

```yaml
case_reopen_event:
  reopen_event_id: null
  prior_case_id: null
  new_or_reopened_case_id: null
  item_instance_id: null
  new_report_id: null
  prior_repair_refs: []
  relationship_to_prior_issue: unknown|same_symptom_claimed|same_cause_confirmed|different_issue|undetermined
  reopened_at: null
```

A later symptom must not silently rewrite the earlier repair as unsuccessful.

`REPEAT_SYMPTOM != SAME_CAUSE`.

`NEW_CASE != PRIOR_CASE_ERASED`.

## 18. Lost records and uncertainty

Possible evidence may include:

- transaction record;
- procurement receipt;
- item-instance provenance;
- provider's historic policy version;
- customer-held representation;
- repair record;
- workshop mark;
- serial/identifier record where canon supports one;
- correspondence;
- courier handoff;
- witness statement.

Missing evidence may justify `INSUFFICIENT_EVIDENCE` or `ACCEPTED_AMBIGUITY` when the world genuinely cannot resolve the old state.

`MISSING_RECEIPT != FALSE_CLAIM`.

`RECORD_MISMATCH != FRAUD`.

## 19. Provider succession

A shop or workshop can change operators while old obligations or promises remain historically relevant.

```yaml
after_sale_provider_succession:
  service_node_id: null
  former_provider_id: null
  successor_provider_id: null
  transition_event_ref: null
  inherited_case_refs: []
  noninherited_case_refs: []
  governing_agreement_refs: []
  unresolved_scope_questions: []
```

The system records what was actually transferred. It never assumes a successor inherited every promise.

## 20. Customer-facing visibility

Safe visible states can include:

- service intake open/closed;
- item awaiting assessment;
- repair underway;
- replacement delayed;
- ready for pickup;
- temporary loaner in use;
- provider relocation;
- public recall notice where separately authorized.

Private evidence, diagnosis details, financial settlement and dispute records remain subject to their owners' visibility rules.

## 21. Minecraft/Cobblemon/Craftics boundary

Minecraft/Cobblemon may render authored state through:

- repair counters;
- tagged shelves;
- boxed returned goods;
- workshop props;
- a repaired cosmetic variant;
- an alternate/replacement item model;
- pickup notices;
- temporary loaner props;
- provider signage;
- courier parcels.

Presentation never determines:

- whether a return is authorized;
- whether a defect exists;
- who caused damage;
- whether a promise applies;
- remedy eligibility;
- ownership;
- refund completion;
- repair legality;
- item mechanical state;
- combatants or battle legality.

Cobblemon BattleState remains non-authoritative for combatants, legality, HP/status, tactical position and world consequences.

## 22. Encounter contract — Repair Counter Withdrawal

Narrative premise:

A provider has accepted a story-significant non-living item for assessment. An unrelated tactical threat reaches the public service area before staff can finish moving customers and controlled property away.

Full intended version may require:

- staged withdrawal;
- narrow-space movement;
- Intercept/forced movement;
- protected counters or controlled-property zones;
- generalized reactions;
- objective-aware AI that protects exits rather than simply attacking;
- semantic playback of closed counter / resumed service.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Staff, customers, service records and the serviced item leave BattleSpec.
2. Existing owners freeze custody and case state.
3. Ouros explicitly selects legitimate combatants.
4. AutoPTU receives static reviewed geometry in the emptied public area or adjacent corridor.
5. No destructible counter, item HP, pickup, theft or custody rule is invented.
6. Tactical success may create only `IMMEDIATE_SERVICE_AREA_CLEAR`.
7. The after-sale case resumes afterward under world-state authority.

`TACTICAL_VICTORY != RETURN_AUTHORIZED`.

`TACTICAL_VICTORY != REPAIR_COMPLETED`.

## 23. Encounter contract — Replacement Handoff Chokepoint

Narrative premise:

A replacement unit has been allocated and is awaiting a later controlled handoff. An unrelated threat blocks the approach between safe storage and the public pickup point.

Rich version dependencies are identical to the permanent map above when escort, object protection, Intercept, changing zones or objective-aware policy matter.

Reduced version status: READY.

Reduced contract:

- replacement asset stays outside BattleSpec;
- staff/couriers withdraw;
- custody remains frozen;
- battle occurs on static adjacent geometry;
- success creates `IMMEDIATE_HANDOFF_APPROACH_CLEAR` only;
- later world events perform issue/custody/ownership handoffs.

`APPROACH_CLEAR != REPLACEMENT_ISSUED`.

`REPLACEMENT_ISSUED != ORIGINAL_RETURNED`.

## 24. Encounter contract — Workshop Retrieval Perimeter

Narrative premise:

A repaired item is technically ready but cannot yet be collected because a tactical threat occupies the exterior approach.

Full version may require weather/hazard state, staged movement, reaction ordering, escort and tactical policy.

Reduced version:

- repaired item and workshop staff remain outside BattleSpec;
- repair/verification/release state is frozen before combat;
- AutoPTU resolves a conventional static encounter;
- victory creates only `IMMEDIATE_WORKSHOP_APPROACH_CLEAR`;
- pickup and custody transfer occur later.

`REPAIR_COMPLETE != PICKUP_COMPLETE`.

`APPROACH_CLEAR != OWNERSHIP_CHANGED`.

## 25. Noncombat contract — Three Repairs, One Instrument

A field instrument has three repair records and a new reported symptom. Players compare:

- item identity;
- earlier symptoms;
- replaced components;
- workshop records;
- provider policy versions;
- courier dates;
- current observation.

Valid conclusions may include:

- new unrelated defect;
- recurrence of prior cause;
- prior repair completed correctly but another component later failed;
- records attached to another same-model unit;
- evidence insufficient.

The scene should not force fraud or incompetence as the answer.

## 26. Generation guardrails

1. Never apply this extension to Pokémon or other living actors.
2. Never invent universal warranties or consumer rights.
3. Preserve the exact authored promise/policy version used by a case.
4. Keep item model/type and item instance separate.
5. Keep custody and ownership separate.
6. Keep symptom, defect, cause and responsibility separate.
7. Keep remedy eligibility, selection and fulfillment separate.
8. Route repair mechanics to exact PTU/Caelo/AutoPTU authority.
9. Route money to Finance.
10. Route shipments to Courier.
11. Route recall state to Recall.
12. Route disputes/obligations to Agreements or appropriate authority.
13. Missing records create uncertainty before they create accusations.
14. Preserve failed, superseded and reopened episodes instead of rewriting history.
15. Rich tactical scenes must declare permanent capability dependencies.
16. Reduced encounters must remove controlled items and administrative semantics from BattleSpec.

## 27. Promotion questions

Before any after-sale practice becomes canon, establish:

- which region/provider/institution uses it;
- which non-living goods qualify;
- whether the practice is a seller promise, maker guarantee, service contract, cooperative custom, institutional rule or something else;
- whether coverage follows buyer, item, institution or transaction;
- what evidence is normally requested;
- who may authorize a remedy;
- available remedies;
- whether exchange/replacement requires original return;
- whether temporary loaners exist;
- how private records are handled;
- how policy changes affect old transactions;
- whether successor providers inherit cases;
- which exact PTU/Caelo mechanics govern any repair effect.

Until promotion, all such practices remain local PROPOSED worldbuilding.