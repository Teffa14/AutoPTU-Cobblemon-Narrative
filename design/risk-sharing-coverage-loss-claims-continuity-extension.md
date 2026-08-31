# Risk-sharing, coverage, loss, and claims continuity extension

Status: PROPOSED / DORMANT BY DEFAULT
Pass: 168

## Purpose

Provide a continuity layer for authored mutual-aid arrangements, guarantees, risk pools, protection contracts, disaster reserves, transport guarantees, or other systems that respond to loss. This layer records procedure and history. It does not create modern insurance as universal Ouros canon.

Activation requires an authoritative `coverage_rule_ref`, institution rule, contract, custom, or explicit canon statement. If the applicable rule is unknown, preserve `RULE_UNKNOWN`; do not fabricate a decision framework.

## Authority boundaries

Finance remains authoritative for money balances, commitments, transfers, and payment facts.
Material Culture/property continuity remains authoritative for object identity, provenance, ownership, condition, repair, replacement, and custody where applicable.
Logistics/courier continuity remains authoritative for transport and shipment custody.
Health/Care remains authoritative for injury and treatment.
Disaster/event continuity remains authoritative for the underlying incident.
Archives/records remain authoritative for preserved documentary artifacts.
AutoPTU remains authoritative for tactical battle facts.
Minecraft/Cobblemon/Craftics remain presentation/adaptation layers and cannot infer economic outcomes.

## Core records

`risk_sharing_arrangement`
- arrangement_id
- arrangement_kind
- authority_ref
- institution_or_participants
- start_time
- end_time_or_open
- status
- provenance

`coverage_version`
- arrangement_id
- version_id
- effective_interval
- coverage_rule_ref
- covered_risk_refs
- exclusion_or_limit_refs when authored
- contribution_commitment_refs when authored
- supersedes_version_id

`covered_subject_link`
- coverage_version_id
- subject_ref
- subject_kind
- relationship_to_participant
- effective_interval
- provenance

`loss_report`
- report_id
- reported_subject_ref
- alleged_loss_event_ref
- reporter_ref
- report_time
- reported_damage_or_loss
- confidence
- provenance

`claim_case`
- claim_id
- arrangement_id
- coverage_version_claimed
- claimant_ref
- loss_report_ref
- opened_time
- current_status
- rule_authority_ref

`claim_evidence_bundle`
- claim_id
- evidence_refs
- missing_evidence_refs
- version_time
- provenance

`claim_review_episode`
- claim_id
- reviewer_or_process_ref
- inputs_considered
- rule_version_used
- started_time
- completed_time
- result_ref

`coverage_decision`
- decision_id
- claim_id
- decision_kind
- scope
- reasoning_summary_ref
- authority_ref
- effective_time
- reviewable_status

`compensation_link`
- claim_id
- approved_commitment_ref
- finance_transfer_refs
- material_replacement_refs
- service_or_repair_refs
- completion_status

`claim_dispute_or_review`
- claim_id
- challenged_decision_ref
- grounds_as_asserted
- review_authority_ref
- status
- outcome_ref

`coverage_renewal_or_lapse`
- arrangement_id
- prior_version
- new_version_or_none
- effective_time
- reason_ref if known

`coverage_record_revision`
- target_record
- prior_assertion
- revised_assertion
- reason
- authority
- timestamp

## Permanent separations

COVERAGE_EXISTS != LOSS_COVERED
LOSS_OCCURRED != CLAIM_FILED
CLAIM_FILED != CLAIM_ACCEPTED
CLAIM_ACCEPTED != PAYMENT_COMPLETED
CLAIM_REJECTED != FRAUD_PROVEN
CLAIM_APPROVED != FULL_COMPENSATION
PAYMENT_COMPLETED != OBJECT_REPAIRED
COMPENSATION != RESTORATION
DAMAGE_REPORTED != DAMAGE_CONFIRMED
OWNERSHIP != COVERAGE
CUSTODY != COVERAGE
CONTRIBUTION_PAID != CLAIM_AUTOMATICALLY_APPROVED
COVERAGE_EXPIRED != PAST_CLAIMS_ERASED
REPAIR_COMPLETED != ORIGINAL_STATE_RESTORED
MUTUAL_AID_MEMBER != AUTOMATIC_BENEFICIARY
BATTLE_VICTORY != CLAIM_VALIDATED
ITEM_LOST_IN_BATTLE != AUTOMATIC_COVERAGE_OUTCOME
MINECRAFT_BLOCK_DAMAGE != CANONICAL_LOSS

## Generator restrictions

Do not invent a loss merely to create a claim plot.
Do not infer ownership from possession, custody, coverage, payment, or Minecraft container state.
Do not infer fraud because evidence conflicts or a claim is rejected.
Do not turn a Skill Check into automatic legal/economic entitlement unless an authored PTU/Caelo rule explicitly says so.
Do not grant Trainer XP, Features, Items, money, Loyalty, reputation, or civic authority merely because a claim was filed or accepted.
Do not create premiums, deductibles, limitation periods, exclusions, liability rules, or compulsory coverage unless canon authors them.
Do not treat Pokémon companions as insurable property by default. Any care, guardianship, medical-cost, partnership, or related arrangement must use explicit canon and preserve Pokémon agency.

## Encounter contracts

### Claims Archive Recovery Perimeter

Narrative premise: an authored claims or mutual-aid archive becomes temporarily inaccessible during an incident.

Full version: BLOCKED.
Dependencies: complete movement including push/pull/knockback/interception/forced movement if route control or displacement matters; full turn/round lifecycle; terrain/weather/hazards/zones/reactions when the site itself remains dangerous; move-specific behavior; abilities/items/Trainer Features used by the encounter; AI legal-action infrastructure; AI tactical policy for protect/withdraw/objective behavior; Minecraft/Cobblemon/Craftics adapter/playback for semantic presentation.

Reduced version: READY at narrative-contract level after individual tactical content audit. Records and archivists remain outside BattleSpec before initiative. Static geometry only. Allowed output: `IMMEDIATE_CLAIMS_ARCHIVE_APPROACH_CLEAR`. This never means evidence recovered, claim validated, records complete, or decision changed.

### Damaged Workshop Assessment Perimeter

Narrative premise: an assessor or mutual-aid representative needs safe later access to inspect a damaged workshop.

Full version: BLOCKED when active hazards, unstable terrain, environmental phases, protected escort, or objective-aware AI are required.

Reduced version: keep assessor, owners, tools, damaged property, and evidence objects outside BattleSpec. AutoPTU resolves only a conventional audited conflict on static geometry. Allowed output: `IMMEDIATE_DAMAGE_ASSESSMENT_SITE_CLEAR`. Narrative separately determines whether inspection occurs and what it establishes.

### Mutual Aid Treasury Transfer Chokepoint

Narrative premise: an authored reserve or physical transfer must move between two institutional locations.

Full version: BLOCKED. Dependencies can include protected-object carrying, escort semantics, complete movement, Intercept/displacement, lifecycle, reactions, tactical policy, and adapter playback. Existing representative forced-movement mechanics do not verify this family.

Reduced version: transfer objects and couriers are outside BattleSpec. Combat may clear a static immediate route. Allowed output: `IMMEDIATE_MUTUAL_AID_TRANSFER_ROUTE_CLEAR`. This does not transfer money, change Finance, establish custody, or fulfill a compensation commitment.

### Relief or Compensation Distribution Access Incident

Narrative premise: access to a distribution point is contested after a canon-authored loss event.

Full version: BLOCKED when crowd movement, queues, escort, hazards, reactions, or objective-aware AI are required.

Reduced version: recipients, staff, supplies, funds, and queues remain outside BattleSpec. Allowed output: `IMMEDIATE_DISTRIBUTION_POINT_ACCESS_CLEAR`. Distribution, eligibility, quantity, and receipt are later Narrative/Finance/logistics facts.

## Long-term continuity value

The same claim can matter years later without being re-litigated as a new world fact. A repaired building may retain a loss history. A replaced heirloom can preserve the provenance of the lost original and the distinct story of the replacement. A community reserve can survive several disasters, revise its authored rules, run short of resources, merge with another institution, or dissolve while preserving past obligations and decisions.

The design intentionally supports uncertainty: `RULE_UNKNOWN`, `EVIDENCE_INCOMPLETE`, `DECISION_PENDING`, `PAYMENT_PENDING`, and `DISPUTED` are stable states, not errors the generator must automatically resolve.