# Ouros Insurance, Risk Pooling, Claims & Recovery Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Finance already anticipates `INSURANCE_OR_RISK_TRANSFER` but intentionally leaves it disabled until Ouros establishes institutions and rules.

This layer defines the minimum narrative architecture required if canon later enables commercial insurance, mutual-aid pools, recovery funds or another form of risk transfer.

It does not create a universal insurance market, property law, liability regime, actuarial model or Pokémon valuation system.

Its core question is:

When an already-authoritative loss occurs, what agreement says who may bear part of the resulting financial/resource consequence, how is that claim reviewed, and what happens next?

## 1. Hard separations

The generator must preserve these distinctions:

- physical loss != insurance claim;
- damage report != verified damage;
- verified damage != covered loss;
- covered loss != approved amount;
- approved amount != payment sent;
- payment sent != payment received;
- payment received != recovery complete;
- replacement cost != historical/cultural/ecological value;
- maintenance record != guaranteed coverage;
- poor maintenance != fraud;
- denied claim != wrongdoing;
- disputed claim != bad faith;
- duplicate notice != duplicate loss;
- claim error != deception;
- deception allegation != proven fraud;
- insured interest != ownership proof;
- custody != ownership;
- sponsor support != insurance;
- relief grant != insurance;
- emergency reserve != insurance;
- mutual aid != commercial insurance;
- risk pool membership != authority over member institutions;
- one paid claim != precedent for every later event;
- business interruption != physical destruction;
- battle victory != claim approval;
- AutoPTU damage != world-property valuation;
- Minecraft block damage != authoritative loss unless the relevant world layer records it;
- Pokémon capture/custody != insurable property valuation;
- Pokémon injury != replacement-value claim.

## 2. Authority boundaries

This layer references facts owned elsewhere.

Crisis owns hazard events and response phases.

Architecture/Infrastructure/Technology/Manufacturing/Maritime/Rail/Fisheries/other domain layers own physical and operational state.

Material Culture owns persistent item identity and provenance.

Supply Chains owns replacement procurement and logistics.

Finance owns mechanical/narrative payment handoffs.

Agreements owns negotiated commitments outside formal claim handling.

Institutional Review owns bounded appeals/reviews when an authored institution has mandate.

Cases owns suspicious-cause/fraud investigations when evidence justifies opening one.

Pokémon Agency owns Pokémon identity, custody, ownership claims, release/transfer and agency.

Care owns treatment/welfare state.

This layer never overwrites those authorities.

## 3. Risk-transfer institution

```yaml
risk_transfer_institution:
  institution_id: null
  institution_type: null
  public_identity_ref: null
  geographic_scope_refs: []
  eligible_participant_classes: []
  supported_risk_categories: []
  reserve_pool_refs: []
  claim_process_ref: null
  review_body_ref: null
  current_status: ACTIVE
  canon_status: proposed
```

Possible authored institution types:

- COMMERCIAL_INSURER
- MUTUAL_AID_POOL
- CIVIC_RECOVERY_POOL
- PROFESSIONAL_ASSOCIATION_FUND
- LEAGUE_RECOVERY_FUND
- COOPERATIVE_RESERVE
- DISASTER_RECONSTRUCTION_FUND
- OTHER_AUTHORED

These labels create no legal powers by themselves.

## 4. Risk-transfer agreement

```yaml
risk_transfer_agreement:
  agreement_id: null
  institution_id: null
  participant_ids: []
  beneficiary_ids: []
  effective_from: null
  effective_until: null
  current_version_id: null
  covered_interest_refs: []
  covered_event_categories: []
  excluded_event_categories: []
  coverage_scope_refs: []
  limit_refs: []
  participant_obligation_refs: []
  reserve_pool_ref: null
  payment_rule_ref: null
  review_rule_ref: null
  status: PROPOSED
  canon_status: proposed
```

Suggested states:

- PROPOSED
- OFFERED
- ACTIVE
- SUSPENDED
- EXPIRED
- TERMINATED
- SUPERSEDED
- DISPUTED

A risk-transfer agreement is versioned.

A new version does not rewrite what was covered during an older event.

## 5. Covered interest is a reference, not ownership truth

```yaml
covered_interest:
  covered_interest_id: null
  agreement_id: null
  subject_ref: null
  interest_type: null
  ownership_claim_refs: []
  custody_refs: []
  operator_refs: []
  dependency_refs: []
  valuation_method_ref: null
  active_from: null
  active_until: null
```

Possible interest types:

- STRUCTURE
- INFRASTRUCTURE_ASSET
- EQUIPMENT
- INVENTORY_BATCH
- VESSEL
- SERVICE_OPERATION
- EVENT_OPERATION
- BUSINESS_INTERRUPTION
- RESEARCH_EQUIPMENT
- EXHIBIT_OR_COLLECTION_OBJECT
- OTHER_AUTHORED

A covered interest may be legitimate even when the participant does not own the underlying object, for example a lessee with responsibility for equipment. That fact still does not establish legal ownership outside the relevant domain.

Pokémon are excluded from generic asset valuation.

If future canon creates care-cost or institutional service coverage involving Pokémon, those records must reference Pokémon Agency/Care without assigning replacement value to the individual.

## 6. Versioned coverage

```yaml
risk_transfer_agreement_version:
  agreement_version_id: null
  agreement_id: null
  version_number: 1
  effective_from: null
  effective_until: null
  coverage_scope_refs: []
  exclusion_refs: []
  limit_refs: []
  participant_obligation_refs: []
  claim_requirements: []
  supersedes_version_id: null
  change_reason_refs: []
```

Examples of authored scope differences:

- storm damage covered, flood excluded;
- equipment replacement covered, business interruption not covered;
- harbor vessels covered only while operating within a region;
- mutual fund supports emergency repairs but not upgrades;
- museum reserve covers conservation stabilization but not speculative restoration.

No scope is universal.

## 7. Loss event reference

The underlying loss belongs to another domain.

```yaml
claim_loss_reference:
  loss_ref_id: null
  domain_owner: null
  source_event_ref: null
  affected_asset_refs: []
  service_disruption_refs: []
  first_observed_at: null
  verification_refs: []
  current_loss_state_ref: null
```

A claim cannot create or revise the source event.

Example:

A warehouse roof condition is owned by Architecture. A claim references that condition and its evidence.

## 8. Loss notice

```yaml
loss_notice:
  notice_id: null
  agreement_id: null
  reported_by_actor_id: null
  reported_at: null
  claimed_loss_refs: []
  initial_event_description_ref: null
  supporting_evidence_ids: []
  current_status: RECEIVED
```

Suggested states:

- RECEIVED
- INCOMPLETE
- ACKNOWLEDGED
- WITHDRAWN
- MERGED_WITH_OTHER_NOTICE
- CLOSED_NO_CLAIM

A notice is not yet an approved claim.

## 9. Claim file

```yaml
claim_file:
  claim_id: null
  notice_ids: []
  agreement_id: null
  agreement_version_id: null
  claimant_ids: []
  beneficiary_ids: []
  loss_ref_ids: []
  evidence_ids: []
  requested_support_refs: []
  current_assessment_id: null
  decision_id: null
  dispute_refs: []
  payment_commitment_refs: []
  recovery_project_refs: []
  status: OPEN
```

Suggested states:

- OPEN
- EVIDENCE_NEEDED
- ASSESSMENT_PENDING
- UNDER_REVIEW
- DECIDED
- PARTIALLY_DECIDED
- DISPUTED
- PAYMENT_PENDING
- PAID
- CLOSED
- WITHDRAWN

## 10. Claim evidence

Evidence should be domain-grounded.

Possible sources:

- crisis event record;
- structure inspection;
- maintenance history;
- inventory ledger;
- photograph/video with provenance;
- sensor logs;
- shipping/custody records;
- repair estimate;
- service timetable/outage record;
- witness statement;
- public notice;
- weather observation;
- manufacturing lot record;
- battle transcript only when a battle actually caused a relevant world event and that handoff is authored.

A screenshot alone does not override Chronicle or authoritative domain state.

## 11. Claim assessment

```yaml
claim_assessment:
  assessment_id: null
  claim_id: null
  assessor_id: null
  assessed_at: null
  coverage_findings: []
  loss_findings: []
  evidence_gap_refs: []
  valuation_refs: []
  causation_scope_refs: []
  recommended_support_ref: null
  unresolved_questions: []
  confidence_note_ref: null
```

The assessment may legitimately conclude:

- covered;
- partially covered;
- outside scope;
- evidence insufficient;
- duplicate/overlapping claim;
- another institution must determine a prerequisite fact first.

It does not automatically determine fraud or liability.

## 12. Claim decision

```yaml
claim_decision:
  decision_id: null
  claim_id: null
  deciding_authority_ref: null
  decided_at: null
  decision_type: null
  approved_support_ref: null
  denied_component_refs: []
  condition_refs: []
  reasoning_document_ref: null
  review_available: false
  review_deadline: null
  supersedes_decision_id: null
```

Possible decision types:

- APPROVED
- PARTIALLY_APPROVED
- DENIED_OUTSIDE_SCOPE
- DENIED_INSUFFICIENT_EVIDENCE
- DEFERRED_PENDING_EXTERNAL_FACT
- CLOSED_DUPLICATE
- WITHDRAWN
- OTHER_AUTHORED

No denial reason implies moral judgment by default.

## 13. Payment handoff

Finance owns payment state.

```yaml
claim_payment_handoff:
  handoff_id: null
  claim_decision_id: null
  finance_commitment_ref: null
  intended_recipient_ref: null
  approved_amount_or_resource_ref: null
  restricted_use_refs: []
  sent_event_ref: null
  received_event_ref: null
```

Claim approval does not mutate mechanical currency directly.

## 14. Recovery handoff

```yaml
recovery_funding_handoff:
  handoff_id: null
  claim_id: null
  recovery_project_ref: null
  authorized_support_ref: null
  supply_chain_request_refs: []
  finance_refs: []
  project_status_ref: null
```

Examples:

An approved bridge claim may fund replacement materials. Architecture/Public Works still owns the bridge project.

An approved museum claim may fund conservation work. Archives/Collections still owns treatment and custody.

## 15. Mutual-aid pool

```yaml
mutual_aid_pool:
  pool_id: null
  institution_id: null
  member_ids: []
  contribution_rule_ref: null
  eligible_loss_categories: []
  reserve_ref: null
  allocation_rule_ref: null
  emergency_priority_ref: null
  last_review_at: null
  current_status: ACTIVE
```

The pool can remember:

- contributions;
- reserve depletion;
- unresolved claims;
- emergency allocations;
- members joining/leaving;
- rules changing after a catastrophe;
- loans of equipment handled by Supply Chains rather than money;
- regional mutual aid when one settlement cannot respond alone.

Do not model actuarial mathematics unless future gameplay needs it.

## 16. Correlated-loss pressure

A pool can be healthy during isolated events and strained when many members suffer losses simultaneously.

```yaml
pool_stress_event:
  pool_stress_id: null
  pool_id: null
  triggering_crisis_refs: []
  simultaneous_claim_ids: []
  reserve_before_ref: null
  reserve_after_ref: null
  deferred_claim_ids: []
  emergency_action_refs: []
```

This creates stories about prioritization and resilience without inventing bankruptcy mechanics.

## 17. Business interruption

```yaml
service_interruption_claim_component:
  component_id: null
  claim_id: null
  service_or_business_ref: null
  interruption_start: null
  interruption_end: null
  cause_ref: null
  physical_damage_required: false
  dependency_failure_refs: []
  requested_support_ref: null
  assessment_ref: null
```

Possible causes may include route closure, utility outage, evacuation, supplier failure or temporary access restriction.

Whether the agreement covers that cause remains authored contract state.

## 18. Fraud allegation boundary

Fraud is not inferred from discrepancy alone.

```yaml
claim_discrepancy:
  discrepancy_id: null
  claim_id: null
  discrepancy_type: null
  conflicting_record_refs: []
  benign_explanation_refs: []
  investigation_case_ref: null
  current_interpretation: UNRESOLVED
```

Possible discrepancy types:

- DUPLICATE_RECORD
- VERSION_MISMATCH
- QUANTITY_MISMATCH
- DATE_MISMATCH
- OWNERSHIP_CLAIM_MISMATCH
- PRIOR_DAMAGE_MISMATCH
- CAUSE_MISMATCH
- PAYMENT_MISMATCH

Only Cases/Institutional Review should escalate when mandate and evidence justify it.

## 19. Review and dispute

A claim may be reviewed without creating a universal court.

```yaml
claim_review:
  review_id: null
  claim_id: null
  previous_decision_ref: null
  reviewing_body_ref: null
  mandate_ref: null
  new_evidence_refs: []
  review_scope: null
  outcome_ref: null
  status: PENDING
```

A corrected decision does not erase the earlier decision from Chronicle.

## 20. Repair versus upgrade

If a recovery project changes the asset rather than restoring it exactly, track the difference.

Example:

A storm destroys an old footbridge.

The claim supports equivalent replacement.

The town chooses a larger accessible bridge and funds the improvement separately.

Architecture records the new structure version. Finance records both funding sources. Insurance does not become the owner of the bridge design.

## 21. Historical and cultural loss

Replacement cost cannot fully represent:

- a unique archive object;
- memorial fabric;
- historical architecture;
- an old instrument with documented provenance;
- a tree/landscape landmark;
- ecological habitat;
- social continuity.

The claim may support stabilization or reconstruction while other layers record non-financial loss.

## 22. Pokémon-related boundary

Never use this layer to calculate Pokémon replacement value.

Do not infer:

- captured Pokémon = insurable inventory;
- missing Pokémon = asset loss;
- injured Pokémon = depreciated asset;
- released Pokémon = disposal;
- transferred Pokémon = sale;
- wild Pokémon damage = liability automatically;
- Trainer ownership claim = absolute property right.

Any future coverage of care costs, transport incidents or institutional services must hand off to Pokémon Agency/Care and remain bounded by authored canon.

## 23. Minecraft projection

Minecraft may present:

- damaged insured structures already established by world state;
- claim notices;
- assessor NPC visits;
- inspection markers;
- repair staging;
- mutual-aid depots;
- public recovery notices;
- reopened sites;
- historical claim records.

Minecraft does not decide:

- whether the loss is covered;
- asset value;
- fraud;
- ownership;
- liability;
- payout;
- repair completeness.

## 24. Encounter implementation boundary

Claim work is primarily overworld/institutional.

If a claim survey becomes dangerous, the battle should remain separate from claim truth.

Winning combat may allow inspectors to continue. It never proves coverage, causation or valuation.

Mechanically rich versions of evacuation, escort, protected survey lanes or moving cargo depend on the same permanent capability map used elsewhere.

## 25. Reduced-version principle

When complete movement, hazards, tactical AI or Minecraft playback are unavailable:

1. establish the authoritative loss and claim state outside battle;
2. move civilians/workers/cargo outside the grid where possible;
3. freeze one safe tactical geometry;
4. run a conventional battle only for combatants actually involved;
5. return to the claim/recovery workflow afterward.

The narrative premise survives without duplicating missing PTU rules in Minecraft.

## 26. Suggested initial implementation order

If canon enables this layer later:

1. `RISK_TRANSFER_INSTITUTION`
2. versioned `RISK_TRANSFER_AGREEMENT`
3. `LOSS_NOTICE`
4. `CLAIM_FILE`
5. evidence references
6. assessment
7. decision
8. Finance payment handoff
9. recovery-project handoff
10. mutual-aid pool state
11. dispute/review integration
12. Minecraft UI/projection

No pricing engine is required for an initial implementation.

## 27. Hard non-inferences

Never infer:

- storm happened -> insurance payout;
- structure damaged -> claim covered;
- claim denied -> insurer corrupt;
- claim disputed -> claimant deceptive;
- evidence missing -> fraud;
- duplicated invoice -> theft;
- old damage -> current claim invalid;
- maintenance failure -> negligence;
- payout -> recovery complete;
- repair complete -> history erased;
- mutual pool depleted -> institution bankrupt;
- insurer paid -> insurer owns the asset;
- wild Pokémon involvement -> Trainer liability;
- battle transcript -> property valuation;
- mechanical Injury -> monetary value;
- captured Pokémon -> insurable inventory;
- insurance -> guaranteed replacement;
- insured venue -> reduced battle damage;
- Minecraft repair animation -> claim settled.

## 28. Canon status

Everything in this layer remains PROPOSED.

The existing Finance rule that insurance/risk transfer remains disabled continues to control until Ouros canon explicitly establishes one or more institutions and their scope.

This document supplies architecture so later canon can enable the concept without improvising inconsistent rules.