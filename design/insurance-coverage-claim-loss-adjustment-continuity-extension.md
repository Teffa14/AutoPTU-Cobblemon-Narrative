# Ouros Insurance, Coverage, Claim & Loss-Adjustment Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Pass: 143
Date: 2026-08-30

## Purpose

This extension gives Ouros a durable lifecycle for an optional authored risk-transfer or compensation arrangement after an incident causes a claimed loss.

It exists because `finance-sponsorship-risk-layer.md` already defines a minimal `risk_transfer_agreement` and `coverage_claim`, but does not yet preserve the full chronology between loss, notice, evidence, review, adjustment, repair/recovery and settlement.

This extension does not make insurance universal. It activates only where canon has explicitly established an institution, cooperative, guild, civic fund, carrier, mutual-aid pool or other body with authored risk-transfer rules.

## Authority boundaries

Finance owns the agreement and money.

Facility Maintenance and relevant infrastructure owners own physical damage, repairs, verification and reopening.

Case/Authority owns formal incident investigation and evidence custody when an actual case exists.

Material Culture owns object identity and provenance.

Found Property owns ordinary found-object custody/restitution.

Wreck Sites owns wreck context and recovery history.

Crisis/Rescue owns immediate stabilization, rescue and life safety.

Public Adjudication or other authored institutions own any formal review powers established by canon.

This extension owns only the continuity of a coverage/compensation claim and its claim-specific evidence/decision history.

## Activation gate

No claim system appears merely because something was damaged.

Before creating a `risk_claim_case`, world state must establish:

```yaml
risk_transfer_activation:
  agreement_ref: null
  provider_ref: null
  claimant_or_beneficiary_refs: []
  covered_subject_refs: []
  effective_period_ref: null
  authored_scope_ref: null
  authored_exclusion_ref: null
  claim_process_ref: null
  canon_reference_ids: []
```

If these facts do not exist, the world may still have:

- ordinary repair;
- aid;
- donation;
- civic relief;
- private compensation;
- a dispute;
- no financial response.

Do not synthesize an insurer to make a quest work.

## Persistent claim case

```yaml
risk_claim_case:
  risk_claim_id: null
  agreement_ref: null
  provider_ref: null
  claimant_refs: []
  beneficiary_refs: []
  incident_refs: []
  claimed_loss_item_refs: []
  notice_event_ref: null
  completeness_state: RECEIVED_UNREVIEWED
  review_state: NOT_STARTED
  coverage_decision_refs: []
  adjustment_refs: []
  settlement_ref: null
  review_or_appeal_refs: []
  linked_repair_refs: []
  linked_recovery_refs: []
  linked_finance_refs: []
  public_visibility: PRIVATE
  provenance_refs: []
  status: OPEN
```

Candidate claim statuses:

- OPEN
- INFORMATION_REQUIRED
- EVIDENCE_COLLECTION
- UNDER_REVIEW
- ADJUSTMENT_ACTIVE
- DECISION_ISSUED
- SETTLEMENT_PENDING
- SETTLED
- DENIED
- WITHDRAWN
- CLOSED
- REOPENED

These are claim-process states. They do not alter the physical condition of the subject.

## Loss notice

A loss notice records what someone reported at a specific time.

```yaml
loss_notice:
  notice_id: null
  submitted_at: null
  submitted_by_ref: null
  receiving_actor_or_institution_ref: null
  agreement_ref: null
  incident_time_claim: null
  discovery_time_claim: null
  subject_refs: []
  location_refs: []
  cause_claim_refs: []
  damage_or_loss_claim_refs: []
  immediate_action_claim_refs: []
  evidence_refs: []
  completeness_state: RECEIVED_UNREVIEWED
```

Candidate completeness states:

- RECEIVED_UNREVIEWED
- SUFFICIENT_FOR_OPENING
- CLARIFICATION_REQUIRED
- DOCUMENTATION_REQUIRED
- WRONG_PROCESS
- DUPLICATE_SUSPECTED
- COMPLETE_FOR_CURRENT_STAGE

A notice can be genuine and incomplete.

A later correction does not rewrite the original report. Append a revision or clarification event.

## Claim item

One incident can produce several claimed losses with different dispositions.

```yaml
claim_loss_item:
  claim_loss_item_id: null
  risk_claim_id: null
  subject_ref: null
  loss_type: authored
  observed_damage_refs: []
  claimed_cause_refs: []
  claimed_value_ref: null
  valuation_basis_ref: null
  ownership_or_interest_ref: null
  pre_loss_condition_refs: []
  post_loss_condition_refs: []
  recovery_status_ref: null
  repair_status_ref: null
  coverage_component_ref: null
  current_disposition: PENDING
```

Possible dispositions:

- PENDING
- INFORMATION_REQUIRED
- COVERED
- PARTIALLY_COVERED
- EXCLUDED
- OUTSIDE_SCOPE
- WITHDRAWN
- DUPLICATE
- RECOVERED_BEFORE_SETTLEMENT
- REFERRED_TO_OTHER_PROCESS

A whole claim can therefore be partly accepted and partly rejected without contradiction.

## Evidence packet

Claim evidence should preserve source and purpose.

```yaml
claim_evidence_packet:
  packet_id: null
  risk_claim_id: null
  submitted_by_ref: null
  received_at: null
  evidence_refs: []
  asserted_purpose: null
  integrity_notes: []
  completeness_claim: null
  verification_refs: []
  supersedes_packet_ref: null
```

Examples of evidence refs can include:

- photographs already governed by Photography/Visual Evidence;
- maintenance histories;
- inventories;
- receipts or transaction provenance;
- prior condition surveys;
- transport manifests;
- witness statements;
- incident reports;
- repair estimates;
- recovery records;
- identity or entitlement records.

This extension does not duplicate any evidence object's owner.

## Claim-specific review role

```yaml
claim_review_assignment:
  assignment_id: null
  risk_claim_id: null
  reviewer_ref: null
  role_type: authored
  assigned_at: null
  authority_scope_ref: null
  permitted_evidence_refs: []
  decision_authority: false
  completed_at: null
```

Candidate authored roles may include:

- intake reviewer;
- field assessor;
- loss adjuster;
- technical specialist;
- coverage reviewer;
- settlement approver;
- internal review officer;
- community mutual-aid assessor.

Role labels create no authority by themselves. Canon must establish the institution and mandate.

`ASSIGNED_REVIEWER != FINAL_DECISION_AUTHORITY`.

## Inspection and assessment

A claim inspection is an observation event, not a verdict.

```yaml
claim_site_inspection:
  inspection_id: null
  risk_claim_id: null
  inspector_refs: []
  performed_at: null
  location_refs: []
  subject_refs: []
  observed_condition_refs: []
  inaccessible_area_refs: []
  evidence_created_refs: []
  technical_referrals: []
  uncertainty_notes: []
```

Claim inspection must link to the authoritative physical-condition owner rather than rewriting it.

If Facility Maintenance already has a condition observation, the claim can consume that observation.

If the claim inspector notices a new physical fault, it should emit a candidate observation to Maintenance rather than privately changing facility truth.

## Loss adjustment

Adjustment records how the claim process interprets scope and value. It must remain distinct from the underlying physical facts.

```yaml
loss_adjustment_revision:
  adjustment_id: null
  risk_claim_id: null
  revision_number: 1
  created_at: null
  created_by_refs: []
  claim_item_assessments: []
  valuation_input_refs: []
  covered_scope_claims: []
  excluded_scope_claims: []
  uncertainty_notes: []
  prior_revision_ref: null
  recommendation: null
```

Revisions are append-only.

A later estimate can supersede an earlier recommendation without declaring the earlier observer dishonest.

## Coverage review

Coverage answers a narrower question than causation or liability.

```yaml
coverage_review:
  coverage_review_id: null
  risk_claim_id: null
  agreement_ref: null
  reviewed_scope_refs: []
  prerequisite_results: []
  exclusion_results: []
  incident_fact_refs_used: []
  unresolved_fact_refs: []
  reasoning_claim_refs: []
  decision_authority_ref: null
  outcome: PENDING
  issued_at: null
```

Candidate outcomes:

- PENDING
- INFORMATION_REQUIRED
- COVERED
- PARTIALLY_COVERED
- NOT_COVERED
- OUTSIDE_EFFECTIVE_PERIOD
- WRONG_SUBJECT
- WRONG_BENEFICIARY
- REFERRED
- WITHDRAWN

A coverage review must evaluate authored agreement conditions only.

It cannot invent an exclusion after the event.

## Coverage and liability remain separate

Preserve these boundaries:

```text
CAUSE_ESTABLISHED != LIABILITY_ESTABLISHED
LIABILITY_ESTABLISHED != COVERAGE_CONFIRMED
COVERAGE_CONFIRMED != LIABILITY_ESTABLISHED
```

An agreement may respond regardless of fault.

Another may require a specific event category.

A region may have no liability rules authored at all.

Do not create criminality, negligence or civil liability because a claim requires drama.

## Repair and recovery handoff

Claims can consume repair/recovery state but cannot own it.

```yaml
claim_repair_link:
  risk_claim_id: null
  claim_loss_item_id: null
  facility_or_asset_ref: null
  work_order_refs: []
  repair_estimate_refs: []
  repair_authorization_ref: null
  completion_refs: []
  verification_refs: []
```

```yaml
claim_recovery_link:
  risk_claim_id: null
  claim_loss_item_id: null
  lost_object_ref: null
  recovery_event_ref: null
  recovery_condition_ref: null
  recovery_time: null
  settlement_reassessment_required: false
```

`REPAIR_AUTHORIZED != REPAIR_COMPLETED`.

`OBJECT_RECOVERED != CLAIM_AUTOMATICALLY_VOID`.

The claim owner decides whether recovery changes settlement only according to authored agreement terms.

## Temporary mitigation

Emergency mitigation can occur before claim review finishes.

Examples:

- boarding a broken window;
- moving inventory away from water;
- temporary service relocation;
- towing an asset out of an unsafe location;
- securing a damaged roof;
- isolating a utility fault.

These actions belong to their physical/service owners.

The claim records them as evidence/provenance where relevant.

`MITIGATION_COMPLETED != CLAIM_APPROVED`.

## Settlement instruction

Settlement is an authorized response, not proof of receipt.

```yaml
claim_settlement_instruction:
  settlement_id: null
  risk_claim_id: null
  issued_at: null
  authorized_by_ref: null
  covered_claim_item_refs: []
  excluded_claim_item_refs: []
  financial_commitment_refs: []
  replacement_or_service_refs: []
  conditions_remaining: []
  status: AUTHORIZED
```

Possible settlement forms if canon supports them:

- monetary payment;
- direct repair funding;
- replacement asset procurement;
- service credit;
- material reimbursement;
- cooperative resource allocation;
- mixed settlement.

Finance owns the actual payment event.

Procurement owns physical replacement acquisition.

Maintenance owns repair completion.

`SETTLEMENT_AUTHORIZED != SETTLEMENT_RECEIVED`.

## Claim closure

```yaml
claim_closure:
  closure_id: null
  risk_claim_id: null
  closed_at: null
  closure_reason: null
  resolved_claim_item_refs: []
  unresolved_historical_question_refs: []
  outstanding_finance_refs: []
  outstanding_repair_refs: []
  reopen_conditions: []
```

Candidate closure reasons:

- SETTLED
- DENIED_FINAL_FOR_CURRENT_PROCESS
- WITHDRAWN
- DUPLICATE_MERGED
- WRONG_PROCESS
- NO_RESPONSE
- REFERRED
- CLOSED_WITH_UNRESOLVED_HISTORY

A claim can be closed while a repair remains underway if the authored process allows it.

A repair can be complete while settlement remains pending.

## Supplemental claim / amendment

New damage may become visible later.

```yaml
claim_supplement:
  supplement_id: null
  risk_claim_id: null
  submitted_at: null
  submitted_by_ref: null
  new_claim_item_refs: []
  revised_value_refs: []
  new_evidence_refs: []
  relation_to_prior_adjustment_ref: null
  review_state: PENDING
```

Supplement does not erase the original decision chronology.

## Review, complaint or appeal

Only create a review mechanism if canon establishes one.

```yaml
claim_review_request:
  review_request_id: null
  risk_claim_id: null
  requested_by_ref: null
  requested_at: null
  disputed_decision_refs: []
  stated_issue_refs: []
  new_evidence_refs: []
  reviewing_body_ref: null
  authority_basis_ref: null
  outcome: PENDING
```

Possible outcomes:

- UPHOLD
- MODIFY
- RETURN_FOR_MORE_INFORMATION
- REOPEN_CLAIM
- REFER_TO_OTHER_PROCESS
- NO_AUTHORITY

`REVIEW_REQUESTED != ORIGINAL_DECISION_VOID`.

`REVIEW_GRANTED != CLAIMANT_WINS`.

## Duplicate and related claims

One incident may create multiple legitimate claims.

```yaml
claim_relationship:
  relationship_id: null
  claim_a_ref: null
  claim_b_ref: null
  relation_type: null
  evidence_refs: []
  confidence: null
```

Candidate relations:

- SAME_INCIDENT_DIFFERENT_SUBJECT
- SAME_SUBJECT_DIFFERENT_AGREEMENT
- POSSIBLE_DUPLICATE
- CONFIRMED_DUPLICATE
- SUPPLEMENT_TO
- REPLACEMENT_FOR
- RELATED_ONLY

Do not merge claims solely because they share an address, claimant or storm.

## Historical agreement versioning

A claim must resolve against the agreement version effective at the relevant authored time.

```yaml
risk_transfer_version_ref:
  agreement_ref: null
  version_ref: null
  effective_from: null
  effective_to: null
  scope_refs: []
  exclusion_refs: []
  beneficiary_refs: []
  subject_refs: []
```

A later amendment must not retroactively rewrite earlier coverage unless canon explicitly says it does.

## Information visibility

Claims are private by default.

Potentially private:

- claimant identity;
- exact claimed amount;
- private property inventory;
- medical/care costs;
- internal assessment notes;
- denial reasoning;
- settlement details;
- historical names/addresses linked through evidence.

Potentially public only when world state supports it:

- a public relief program exists;
- a civic facility has received reconstruction funding;
- a cooperative announces aggregate support;
- a public review decision is published.

NPCs may know that a shop is closed without knowing whether a claim exists.

## Environmental storytelling

Claim continuity should appear through world consequences rather than paperwork walls.

Examples:

- temporary boarding remains while repair funding is reviewed;
- an old inspection chalk mark survives after the storefront reopens;
- a replacement delivery arrives before the original damaged object is removed;
- a repair crew returns after a supplemental inspection;
- a public facility displays a restoration notice without exposing private claim details;
- an old archive box contains multiple estimate versions;
- a business keeps operating from a temporary counter while its premises claim is unresolved;
- a recovered cargo crate changes a pending claim but remains under separate custody.

## Mystery grammar

Claims can support evidence puzzles without treating every discrepancy as fraud.

Useful ambiguity classes:

- different timestamps describe different process stages;
- two estimates use different scopes;
- one photograph predates a renovation;
- a policy identifier belongs to the correct agreement but wrong version;
- a building address changed while the place remained the same;
- a claimant changed name while identity remained the same;
- an item was reported missing and later recovered elsewhere;
- repair work revealed older pre-incident damage;
- one claim item was duplicated while the rest of the claim was valid;
- the report was accurate when made but later evidence changed the assessment.

Allow `ACCEPTED_AMBIGUITY` where surviving evidence cannot settle historical fact.

## Quest hooks

Possible authored hooks include:

- retrieve a pre-loss condition record from an archive;
- escort no one: simply clear access so an inspection can occur later;
- compare two nonmatching but legitimate estimate scopes;
- locate a recovered object before settlement is finalized;
- trace which version of a notice reached a remote branch;
- inspect an old repair that may explain present damage;
- deliver an evidence packet without granting access to its contents;
- confirm whether a temporary location and permanent address refer to the same place;
- help a community fund distinguish duplicate requests after a storm;
- document a reopened facility whose financial recovery remains incomplete.

The player should not be forced to act as an insurer, judge or lawyer unless canon gives that role explicitly.

## Long-term arc pattern — A Street Rebuilds on Different Clocks

Stage 1: establish normal businesses, homes, services and recurring residents.

Stage 2: a bounded storm, accident, Pokémon incident or infrastructure event causes several different losses.

Stage 3: Crisis stabilizes immediate danger. Maintenance records faults. Businesses adapt through temporary spaces.

Stage 4: only some actors have authored risk-transfer or compensation arrangements. Others use savings, mutual aid, civic relief or deferred repair.

Stage 5: claims diverge. One needs clarification, one is partly covered, one settles quickly, one remains under review and one does not exist at all.

Stage 6: physical rebuilding progresses on its own dependencies. A reopened shop can still have a pending claim. A paid claim can still wait on materials.

Stage 7: months later, the street remembers the event through changed facades, temporary habits that became permanent, archived notices, relationships between institutions and differing stories about when recovery was 'finished'.

The arc does not require fraud, corruption or a villain.

## Encounter contract A — Damage Survey Access Perimeter

Status: PROPOSED.

Narrative premise:

A field assessor needs access to a damaged exterior after the acute emergency has ended. An unrelated tactical threat occupies the immediate approach.

### Intended full version

Potentially uses:

- protected withdrawal paths;
- escort/interception if the assessor remains present;
- fragile or restricted areas;
- dynamic hazard zones if physical owner has established them;
- objective-aware `CLEAR_ROUTE` / `PROTECT` tactical policy;
- exact adapter playback around the damaged site.

Permanent capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

### Reduced version — READY

1. Assessor, claimant, records and controlled property leave the tactical space before BattleSpec creation.
2. The physical owner freezes damaged areas and access restrictions.
3. Ouros selects explicit legitimate combatants.
4. AutoPTU receives a static reviewed safe-area geometry.
5. No destructible-property, fragile-evidence or dynamic-hazard mechanic is invented.
6. Tactical victory may create only `IMMEDIATE_SURVEY_APPROACH_CLEAR`.
7. Inspection occurs afterward as a noncombat world-state event.

`TACTICAL_VICTORY != INSPECTION_COMPLETED`.

`INSPECTION_COMPLETED != COVERAGE_CONFIRMED`.

`SURVEY_APPROACH_CLEAR != CLAIM_APPROVED`.

## Encounter contract B — Recovered Cargo Handoff Chokepoint

Status: PROPOSED.

Narrative premise:

A lost or damaged cargo object has been physically recovered and is awaiting handoff while an unrelated threat blocks the controlled approach.

### Intended full version

Could require:

- protected-object zones;
- withdrawal/escort;
- Intercept and forced movement;
- terrain/hazards where the recovery site genuinely has them;
- AI policy that protects/withdraws rather than purely seeking KOs;
- adapter synchronization between battle outcome and later custody event.

### Reduced version — READY

1. Recovered cargo leaves BattleSpec and remains under its current world-state custody.
2. Couriers, adjusters and other noncombatants withdraw.
3. AutoPTU receives only explicit combatants and static geometry.
4. Victory creates `IMMEDIATE_HANDOFF_APPROACH_CLEAR` only.
5. Material Culture / Wreck / Found Property / Case then performs the custody event.
6. Claim review consumes the recovery fact afterward.

`TACTICAL_VICTORY != CUSTODY_TRANSFERRED`.

`CARGO_RECOVERED != CLAIM_SETTLED`.

`CARGO_RECOVERED != OWNERSHIP_ESTABLISHED`.

## Encounter contract C — Temporary Repair Site Withdrawal

Status: PROPOSED.

Narrative premise:

Temporary mitigation or repairs are underway at a covered or potentially covered loss site when a separate tactical threat appears.

### Intended full version

May need:

- staged worker withdrawal;
- protected exit zones;
- active worksite hazards;
- changing access geometry;
- complete movement/interception;
- full round lifecycle;
- objective-aware policy;
- semantic adapter playback.

### Reduced version — READY

1. Workers and claim actors withdraw before combat.
2. Work pauses in Facility Maintenance state.
3. Tools, evidence and repair materials remain noninteractive world objects.
4. Battle occurs in a reviewed static adjacent area.
5. Victory yields `IMMEDIATE_REPAIR_WORK_AREA_CLEAR` only.
6. Maintenance decides whether work resumes.
7. The claim process records no coverage or settlement conclusion from battle.

`WORK_AREA_CLEAR != REPAIR_RESUMED`.

`REPAIR_RESUMED != CLAIM_APPROVED`.

`REPAIR_COMPLETE != PAYMENT_RECEIVED`.

## PTU/Caelo guardrails

This extension does not define or infer:

- premiums;
- deductibles/excess;
- policy limits;
- standard policy forms;
- claim deadlines;
- universal valuation methods;
- depreciation/replacement-cost formulas;
- mandatory insurance;
- liability law;
- negligence;
- subrogation;
- universal property damage rules;
- universal repair costs;
- generic adjuster Skills;
- fraud-detection Skill checks;
- legal authority from Trainer Classes;
- insurer authority from General Education or Technology Education;
- species/Type/Move/Ability competence for valuation, authentication or causation.

Mechanical money remains governed by PTU/Caelo and explicit project implementation.

## Minecraft/Cobblemon/Craftics boundary

SAFE_REUSE can display authored consequences:

- damaged and repaired building states;
- temporary barriers;
- inspection appointments represented by NPC presence after Ouros schedules them;
- claim-office counters if canon has them;
- delivery or repair crews;
- archived documents as interactable representations;
- recovered cargo props;
- replacement objects after authoritative procurement/settlement state.

ADAPTER_REQUIRED for:

- projecting claim-state-specific NPC schedules;
- hiding private claim details from unauthorized players;
- representing work pauses/resumptions;
- linking a tactical access result to a later noncombat inspection;
- reconciling persistent site state after restart.

FORBIDDEN_AUTHORITY:

Minecraft/Cobblemon/Craftics may not decide:

- whether a claim exists;
- whether the claimant is eligible;
- coverage;
- exclusions;
- causation;
- liability;
- loss value;
- ownership;
- evidence authenticity;
- repair completion;
- payment;
- settlement;
- battle participants or PTU legality.

A broken Minecraft block is not automatically a covered loss.

A repaired visual model is not settlement evidence.

A chest pickup is not custody transfer or proof of ownership.

Cobblemon BattleState remains non-authoritative for all combatant, legality, HP/status, position and narrative consequence decisions.

## Core invariants

`LOSS_OCCURRED != LOSS_REPORTED`

`LOSS_REPORTED != LOSS_VERIFIED`

`DAMAGE_OBSERVED != CAUSE_ESTABLISHED`

`CAUSE_ESTABLISHED != LIABILITY_ESTABLISHED`

`LIABILITY_ESTABLISHED != COVERAGE_CONFIRMED`

`POLICY_ACTIVE != EVENT_COVERED`

`EVENT_COVERED != EVERY_LOSS_ITEM_COVERED`

`CLAIM_FILED != CLAIM_COMPLETE`

`CLAIM_COMPLETE != CLAIM_APPROVED`

`ADJUSTER_ASSIGNED != CLAIM_DECIDED`

`ADJUSTER_RECOMMENDATION != FINAL_DECISION`

`ESTIMATE_CREATED != REPAIR_AUTHORIZED`

`REPAIR_AUTHORIZED != REPAIR_COMPLETED`

`REPAIR_COMPLETED != SETTLEMENT_PAID`

`CLAIM_APPROVED != MONEY_RECEIVED`

`CLAIM_DENIED != FRAUD`

`CLAIM_REVISED != ORIGINAL_REPORT_FALSE`

`COMPLAINT_FILED != ORIGINAL_DECISION_VOID`

`CLAIM_CLOSED != ALL_HISTORICAL_FACTS_KNOWN`

## Canon questions deliberately left open

- whether insurance exists anywhere in Ouros;
- whether it is private, cooperative, guild-based, civic, League-linked or another form;
- which assets/activities can be covered;
- which regions use mutual aid instead;
- whether Pokémon-related damage is covered, excluded or handled case-by-case;
- who can make a claim;
- whether claims are named, bearer-like, household-based, business-based or institution-based;
- how coverage scopes are authored;
- what evidence is normally requested;
- who may inspect or adjust;
- what review/appeal paths exist;
- what privacy applies;
- how repair vendors or replacements are chosen;
- whether compensation can be nonmonetary;
- what historical claim files exist;
- which named institutions or recurring NPCs participate.

## Conclusion

Pass 143 can safely deepen the existing optional Finance guardrail into a claim-continuity architecture without canonizing insurance or importing real-world law.

The practical value is persistent aftermath. Ouros can remember that a loss was reported, revised, inspected, partly covered, repaired and eventually settled on different dates while the physical world, institutional records and player knowledge remain internally consistent.