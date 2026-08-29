# Ouros Interregional Arrival, Inspection, Hold & Release Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already models travel, ports, stations, courier custody, interregional visits, institutional recognition, credentials, conservation, care, product traceability and public decisions. This extension preserves the continuity of a scoped arrival inspection episode only when an existing authored institution or rule already requires one.

It does not create passports, visas, customs law, immigration law, tariffs, national borders, universal biosecurity powers, automatic quarantine, contraband categories, inspection Skill DCs or sovereign authority.

The core continuity chain is:

physical arrival or transfer -> inspection requirement reference -> scoped intake -> observations and document/identity checks -> clear, hold, refer or request evidence -> release from this inspection scope -> downstream destination decision.

## Authority boundary

Interregional Mobility owns visits, regional association, host context and recognition of portable records.

Travel, Port, Aviation, Rail, Road and Transit Hub systems own physical journeys, calls, arrivals, departures and service state.

Courier owns shipment legs and custody transfers. Storage owns storage state. Procurement owns order/receipt/acceptance history. Material Culture owns item identity and provenance.

Credentials owns individual authorizations and their scope.

Conservation, Wildlife, Science and Interspecies Ecology own ecological interpretation. Regional origin alone never produces an ecological-risk conclusion.

Care and Pokémon welfare systems own health observations, diagnosis and treatment. This layer cannot create disease, status conditions or treatment requirements.

Batch Traceability owns post-distribution holds, recall, correction and recovery for affected products or batches.

Case Authority owns allegations, investigative evidence and custody when a real case exists.

Civic Governance and Public Adjudication may own mandate, review or contested institutional decisions only where canon has established those powers.

Public Notices owns what is displayed or distributed publicly.

This extension owns the persistent inspection episode linking those systems.

## 1. Inspection gateway

```yaml
arrival_inspection_gateway:
  gateway_id: null
  location_id: null
  host_region_id: null
  operating_institution_ids: []
  mandate_refs: []
  supported_arrival_mode_refs: []
  supported_subject_classes: []
  current_operating_state: UNKNOWN
  temporary_location_refs: []
  public_information_refs: []
  history_event_ids: []
  canon_status: proposed
```

A gateway can be a desk, room, station, laboratory receiving area, conservation access point, port facility or other authored site. Its existence does not imply a national border.

Candidate operating states are descriptive only: OPEN, LIMITED, RELOCATED, TEMPORARY, CLOSED, UNKNOWN.

## 2. Inspection requirement reference

```yaml
inspection_requirement_ref:
  requirement_ref_id: null
  source_authority_or_rule_ref: null
  institution_id: null
  subject_class_scope: []
  geographic_or_facility_scope: []
  trigger_conditions_refs: []
  effective_from: null
  effective_until: null
  public_notice_refs: []
  canon_reference_refs: []
```

Hard rule: the narrative generator may consume this object but may not manufacture it merely because an arrival would be more interesting with a checkpoint.

`ARRIVAL_RECORDED != INSPECTION_REQUIRED`

`INSPECTION_DESIRED_BY_NPC != AUTHORITY_EXISTS`

## 3. Arrival inspection episode

```yaml
arrival_inspection_episode:
  inspection_id: null
  gateway_id: null
  requirement_ref_id: null
  inspecting_institution_id: null
  inspector_actor_ids: []
  subject_ref: null
  subject_class: actor|pokemon|shipment|item_group|vehicle|equipment|sample|other
  source_region_or_location_ref: null
  destination_ref: null
  arrival_event_ref: null
  intake_time: null
  scope_revision_ids: []
  document_check_ids: []
  identity_check_ids: []
  condition_observation_ids: []
  finding_ids: []
  hold_ids: []
  referral_ids: []
  release_event_id: null
  current_state: INTAKE_PENDING
  provenance_refs: []
```

Suggested episode states:
- INTAKE_PENDING
- INTAKE_RECORDED
- REVIEW_PENDING
- INSPECTION_ACTIVE
- EVIDENCE_REQUESTED
- HOLD_ACTIVE
- REFERRED
- CLEARED_WITHIN_SCOPE
- RELEASED_FROM_INSPECTION
- CLOSED_WITHOUT_RELEASE
- CANCELLED
- UNKNOWN

These are continuity labels, not legal categories.

## 4. Scope revision

```yaml
inspection_scope_revision:
  scope_revision_id: null
  inspection_id: null
  parent_revision_id: null
  subject_refs: []
  container_or_package_refs: []
  document_refs: []
  identity_questions: []
  condition_questions: []
  excluded_scope_refs: []
  reason_for_revision_refs: []
  authored_at: null
  authored_by_ids: []
```

A later inspection can expand or narrow scope without pretending the earlier scope included information that was never examined.

Examples:
- exterior container only;
- listed equipment only;
- one transferred Pokémon, not every Pokémon traveling with the Trainer;
- manifest identity check, not ecological assessment;
- facility-access credential, not ownership verification.

## 5. Documentary check

```yaml
document_check:
  check_id: null
  inspection_id: null
  document_ref: null
  claimed_purpose_or_scope: null
  issuer_ref: null
  authenticity_state: UNKNOWN
  scope_match_state: UNKNOWN
  current_version_state: UNKNOWN
  discrepancy_refs: []
  checked_at: null
  checker_ids: []
  evidence_refs: []
```

Possible descriptive states:
- VERIFIED_FOR_THIS_SCOPE
- AUTHENTIC_BUT_SCOPE_MISMATCH
- AUTHENTIC_BUT_SUPERSEDED
- INCOMPLETE
- UNVERIFIED
- CONFLICTING_RECORDS
- NOT_APPLICABLE

An authentic record can still be irrelevant or too narrow.

`DOCUMENT_AUTHENTIC != REQUEST_AUTHORIZED`

## 6. Identity check

```yaml
inspection_identity_check:
  check_id: null
  inspection_id: null
  subject_ref: null
  expected_identity_refs: []
  observed_identity_refs: []
  marker_or_record_refs: []
  match_state: UNKNOWN
  uncertainty_refs: []
  checked_at: null
```

Identity checks must use existing persistent IDs and provenance. They do not create ownership.

`IDENTITY_MATCHED != OWNERSHIP_ESTABLISHED`

For Pokémon, use the persistent Pokémon identity and existing relationship/custody state. Species, nickname, ball appearance or proximity to a Trainer cannot replace identity evidence.

## 7. Condition observation

```yaml
inspection_condition_observation:
  observation_id: null
  inspection_id: null
  subject_ref: null
  observation_scope: null
  observed_at: null
  observer_ids: []
  observable_claims: []
  media_or_measurement_refs: []
  uncertainty_refs: []
  downstream_interpretation_owner_refs: []
```

This record stores direct observations only.

Examples of safe observations:
- seal visibly broken;
- listed count does not match visible count;
- container exterior wet;
- Pokémon individual appears lethargic;
- plant material visible where manifest listed equipment;
- identifier unreadable.

Unsafe conclusions for this layer:
- disease confirmed;
- invasive species confirmed;
- deliberate smuggling confirmed;
- item mechanically defective;
- dangerous Ability confirmed;
- ownership fraud confirmed.

Those require their governing systems.

## 8. Finding

```yaml
inspection_finding:
  finding_id: null
  inspection_id: null
  scope_revision_id: null
  finding_type: null
  supporting_observation_refs: []
  supporting_document_refs: []
  interpretation_owner_ref: null
  confidence_or_resolution_state: null
  created_at: null
  superseded_by_ref: null
```

Useful neutral finding types:
- NO_DISCREPANCY_FOUND_WITHIN_SCOPE
- DOCUMENT_INCOMPLETE
- IDENTITY_UNRESOLVED
- SCOPE_MISMATCH
- CONDITION_REQUIRES_OWNER_REVIEW
- UNLISTED_SUBJECT_OBSERVED
- EVIDENCE_CONFLICT
- INSPECTION_NOT_COMPLETABLE

A finding remains bounded by the inspected scope.

`NO_DISCREPANCY_FOUND_WITHIN_SCOPE != EVERYTHING_PROVEN_SAFE`

## 9. Inspection hold

```yaml
inspection_hold:
  hold_id: null
  inspection_id: null
  subject_refs: []
  hold_scope: null
  reason_state: AWAITING_REVIEW
  initiated_at: null
  initiated_by_ref: null
  mandate_ref: null
  custody_owner_ref: null
  permitted_actions_refs: []
  pending_evidence_refs: []
  referral_refs: []
  released_at: null
  release_reason_ref: null
  status: ACTIVE
```

Candidate reason states:
- AWAITING_REVIEW
- AWAITING_DOCUMENT
- AWAITING_IDENTITY_RESOLUTION
- AWAITING_OWNER_SYSTEM_INTERPRETATION
- AWAITING_DESTINATION_DECISION
- CONDITION_OBSERVATION_REQUIRES_REVIEW
- OTHER_AUTHORED_REASON

Hard rules:

`HOLD_ACTIVE != VIOLATION_CONFIRMED`

`HOLD_ACTIVE != GUILT`

`HOLD_RELEASED != DELIVERY_COMPLETE`

`HOLD_RELEASED != DESTINATION_ACCESS_GRANTED`

## 10. Referral

```yaml
inspection_referral:
  referral_id: null
  inspection_id: null
  referred_subject_refs: []
  target_owner_system: null
  target_institution_ref: null
  question_or_reason_refs: []
  evidence_bundle_refs: []
  referred_at: null
  accepted_at: null
  result_ref: null
  status: SENT
```

Examples:
- Care reviews a health observation;
- Conservation reviews ecological significance;
- Batch Traceability opens a product problem;
- Credentials reviews a scope mismatch;
- Case Authority receives a formally authorized investigative handoff;
- Maintenance reviews damaged transport equipment.

This layer does not predict the result.

## 11. Release event

```yaml
inspection_release_event:
  release_event_id: null
  inspection_id: null
  released_subject_refs: []
  released_scope: null
  release_basis_refs: []
  remaining_restriction_refs: []
  downstream_destination_refs: []
  released_at: null
  authorized_by_ref: null
```

Release means the inspection episode no longer holds the specified subject within that scope.

It does not mean:
- the destination accepted the subject;
- a reserve authorized ecological release;
- Courier completed delivery;
- a port call completed;
- a Trainer gained ownership;
- Care declared health normal;
- a credential gained broader scope.

## 12. Pokémon-specific guardrails

For a transferred or visiting Pokémon preserve separate state for:
- persistent Pokémon identity;
- current partner/ownership/custody relationships;
- origin and prior-region provenance;
- transport/transfer episode;
- inspection episode if one is actually required;
- care state;
- ecological placement or release decision;
- public knowledge.

Hard separations:

`FROM_ANOTHER_REGION != NONNATIVE_POPULATION`

`NONLOCAL_INDIVIDUAL != INVASIVE`

`TRANSFERRED != RELEASED_TO_WILD`

`FACILITY_INTAKE != OWNERSHIP_TRANSFER`

`HEALTH_OBSERVATION != PTU_STATUS`

A Pokémon may simply be traveling with its established partner. The generator must not convert ordinary interregional travel into ecological suspicion.

## 13. Temporary gateways and continuity

A temporary inspection desk or receiving site can become narratively important without becoming permanent law.

Preserve:
- opening/closing dates;
- reason for activation;
- which mandate applied;
- staff and facility history;
- later relocation;
- aliases used in records;
- local businesses/routes that adapted;
- notices that became outdated;
- whether the temporary site later gained another function.

This enables callbacks without implying every future arrival uses the same process.

## 14. Provenance mysteries

Good mysteries come from scope and time differences.

Possible structures:
- planned manifest versus actual loading record versus inspection intake record;
- authentic credential with a narrower scope than people remember;
- facility moved but retained its old public name;
- one shipment split before inspection, producing two legitimate records;
- hold ended before Courier resumed delivery;
- later ecological evidence changes interpretation without making the original inspection fraudulent.

Do not default to corrupt inspectors, smugglers or malicious Pokémon.

## 15. Integration with world simulation

A completed inspection should emit explicit handoffs only.

Possible handoffs:
- `INSPECTION_SCOPE_CLEARED`
- `SUBJECT_RELEASED_FROM_INSPECTION`
- `DOCUMENT_SCOPE_REVIEW_REQUESTED`
- `CARE_REVIEW_REQUESTED`
- `ECOLOGY_REVIEW_REQUESTED`
- `BATCH_PROBLEM_REVIEW_REQUESTED`
- `CASE_REVIEW_REQUESTED`
- `DESTINATION_DECISION_PENDING`

Owner systems decide their own resulting state.

## 16. Encounter boundary

Inspection itself is not a combat check.

A battle near an inspection facility can affect physical access, immediate safety or route control. It cannot authenticate records, establish ecological harm, clear a hold, prove ownership or grant destination admission.

Mechanically rich versions must classify their dependencies using the permanent engine categories. Reduced variants should remove inspected subjects, civilians and controlled evidence from BattleSpec before tactical resolution whenever the missing capability families would otherwise become authoritative.

## 17. Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render:
- arrival halls;
- receiving desks;
- inspection rooms;
- waiting areas;
- sealed containers;
- signage;
- temporary tents;
- staff;
- individual Pokémon;
- gates opening after an Ouros decision;
- visual/sound cues for intake or release.

Presentation cannot decide:
- whether inspection is required;
- whether an institution has authority;
- identity/authenticity conclusions;
- ecological risk;
- health state;
- ownership;
- hold/release state;
- destination access;
- combatants, legality, HP/status, tactical positions or battle outcomes.

Cobblemon BattleState remains outside Ouros/AutoPTU authority.

## 18. Canon questions intentionally left open

Pass 124 does not answer:
- whether any Ouros region has routine interregional inspection at all;
- which institutions possess any such mandate;
- which subjects can be inspected;
- whether ecological transfer controls exist;
- whether there are health-related entry procedures;
- whether any port, station, laboratory or reserve serves as a formal gateway;
- what records are required;
- what review/appeal route exists;
- what privacy protections apply;
- what happens after a serious finding.

Those require explicit canon decisions. Until then, this layer is reusable infrastructure for authored, scoped inspection episodes only.