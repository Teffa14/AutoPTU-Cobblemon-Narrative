# Ouros Finance, Sponsorship, Patronage & Risk Layer

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already models physical goods, workshops, jobs, institutions, staffing, public works, media, crises and reputation. This layer adds the financial relationships that can connect those systems: who provides resources, what the support is for, whether payment actually occurred, what obligations accompany the support, who carries financial risk and how funding decisions leave persistent world consequences.

The goal is narrative finance. The default design is not a full banking, investment, tax or macroeconomic simulator.

## 1. Mechanical money versus narrative finance

Mechanical money remains governed by PTU/Caelo and the eventual game implementation.

Narrative finance tracks facts around money without redefining its mechanical value.

```yaml
financial_state_reference:
  account_or_holder_id: null
  mechanical_balance_ref: null
  pending_commitment_ids: []
  restricted_fund_ids: []
  receivable_ids: []
  payable_ids: []
  public_disclosure_ids: []
  last_verified_event_id: null
```

A narrative record must never silently change a mechanical balance.

A mechanical balance change should generate a provenance event when the transaction is narratively significant.

## 2. Funding source

A funding source is an actor or institution capable of offering resources.

```yaml
funding_source:
  funding_source_id: null
  actor_or_institution_id: null
  source_type: null
  public_identity_id: null
  known_program_ids: []
  known_priority_tags: []
  geographic_scope_ids: []
  disclosure_policy_ref: null
  active: true
```

Possible authored source types:
- individual patron;
- business;
- cooperative;
- civic body;
- League-linked institution;
- university or laboratory;
- club or association;
- charitable or relief institution;
- competition organizer;
- community fund.

These labels describe world roles. They do not create legal powers.

## 3. Funding agreement

```yaml
funding_agreement:
  agreement_id: null
  agreement_type: null
  provider_id: null
  recipient_ids: []
  beneficiary_ids: []
  purpose_ids: []
  total_authorized_amount_ref: null
  restricted_fund_ids: []
  payment_commitment_ids: []
  milestone_ids: []
  visibility_right_ids: []
  reporting_requirement_ids: []
  termination_conditions: []
  amendment_ids: []
  governing_document_ids: []
  public_status: null
  internal_status: PROPOSED
```

Possible authored agreement types:
- SPONSORSHIP
- GRANT
- DONATION
- PRIZE
- SCHOLARSHIP
- RELIEF_SUPPORT
- PROCUREMENT_ADVANCE
- LOAN_OR_CREDIT
- INSURANCE_OR_RISK_TRANSFER

Loan, credit and insurance categories remain disabled unless Ouros explicitly establishes institutions and rules for them.

Suggested states:
- PROPOSED
- UNDER_REVIEW
- OFFERED
- ACCEPTED
- ACTIVE
- PAUSED
- AT_RISK
- COMPLETED
- TERMINATED
- EXPIRED
- DISPUTED

## 4. Provider role is separate from control

Keep these concepts independent:

```text
funds an institution
owns an institution
operates an institution
sets competition rules
holds public authority
employs staff
controls property
has naming/visibility rights
```

A sponsor can provide money and receive public visibility without controlling a Gym, Contest, research program or settlement.

A donor can fund a building without owning it.

A grant provider can require a report without controlling the research conclusion.

Do not infer hidden control merely because funding exists.

## 5. Restricted funds

Some support may be authorized for a specific purpose.

```yaml
restricted_fund:
  restricted_fund_id: null
  agreement_id: null
  purpose_ids: []
  eligible_cost_categories: []
  prohibited_use_claim_ids: []
  released_amount_ref: null
  remaining_amount_ref: null
  expiration_time: null
  review_required: false
  current_status: AVAILABLE
```

Possible states:
- PLEDGED
- AVAILABLE
- PARTIALLY_USED
- EXHAUSTED
- FROZEN
- EXPIRED
- RETURN_PENDING
- CLOSED

A restricted fund is not free general-purpose money.

If Ouros never implements restricted mechanical balances, this object may remain a narrative authorization state and transactions can be validated by authored scripts.

## 6. Promise, transfer and receipt are different events

```yaml
payment_commitment:
  commitment_id: null
  agreement_id: null
  payer_id: null
  intended_recipient_id: null
  amount_ref: null
  due_time: null
  condition_ids: []
  status: PROMISED
```

```yaml
payment_event:
  payment_event_id: null
  commitment_id: null
  payer_id: null
  recipient_id: null
  amount_ref: null
  event_type: null
  world_time: null
  evidence_ids: []
  mechanical_transaction_ref: null
```

Possible event types:
- AUTHORIZED
- SENT
- RECEIVED
- PARTIALLY_RECEIVED
- RETURNED
- REFUNDED
- WITHHELD
- CANCELLED
- REVERSED

A public announcement that money was promised does not prove it was transferred.

A transfer record does not prove the recipient could legally spend it for every purpose.

## 7. Sponsorship

```yaml
sponsorship_agreement:
  agreement_id: null
  sponsor_id: null
  sponsored_actor_or_institution_ids: []
  supported_activity_ids: []
  visibility_right_ids: []
  deliverable_ids: []
  performance_condition_ids: []
  exclusivity_claim_ids: []
  renewal_review_id: null
  public_disclosure_id: null
  current_status: ACTIVE
```

Examples of visibility rights:
- venue banner;
- uniform or equipment mark;
- program acknowledgement;
- named scholarship;
- event signage;
- sponsored equipment plaque;
- media acknowledgement.

Visibility rights do not create PTU combat bonuses.

## 8. Sponsorship pressure

A sponsor may create pressure without being an antagonist.

Track pressure through explicit expectations:

```yaml
sponsor_expectation:
  expectation_id: null
  agreement_id: null
  expected_outcome_or_behavior: null
  measurement_source_ids: []
  current_assessment: null
  consequence_if_unmet_ids: []
```

Possible consequences should come from the authored agreement:
- reduced renewal likelihood;
- loss of future funding;
- public criticism;
- amendment request;
- contract termination;
- no consequence.

Do not invent penalties after the fact because a story needs conflict.

## 9. Grants and research support

```yaml
grant_award:
  agreement_id: null
  program_id: null
  recipient_institution_id: null
  project_id: null
  approved_scope_ids: []
  milestone_ids: []
  reporting_due_ids: []
  publication_requirement_ids: []
  sensitive_data_exception_ids: []
  renewal_review_id: null
```

A null result can still satisfy a legitimate research grant.

The funding source cannot force the science layer to mark a preferred conclusion as true.

Research truth, publication, institutional position and funding remain separate.

## 10. Prizes and awards

```yaml
prize_pool:
  prize_pool_id: null
  event_id: null
  funding_source_ids: []
  eligibility_rule_ref: null
  mechanical_reward_ref: null
  public_amount_ref: null
  payout_commitment_ids: []
  verification_requirement_ids: []
```

The official event result should determine eligibility according to authored rules.

Narrative generation cannot fabricate prize values or pay a prize before the authoritative result is known.

Winning a prize can create attention and sponsor interest. It does not create political authority, friendship or mechanical stat growth.

## 11. Scholarships and development support

A scholarship can support training, travel, research, education or equipment without becoming a combat buff.

```yaml
scholarship_award:
  award_id: null
  provider_id: null
  recipient_id: null
  purpose_ids: []
  eligible_expense_categories: []
  term_start: null
  term_end: null
  review_ids: []
  public_or_private: private
```

For PCs, acceptance must be an explicit player decision when the award creates obligations.

## 12. Donations and patronage

Donations can carry provenance, public acknowledgement and purpose restrictions.

```yaml
donation_record:
  donation_id: null
  donor_id: null
  recipient_id: null
  asset_or_amount_ref: null
  purpose_claim_ids: []
  anonymity_state: null
  acknowledgement_ids: []
  ownership_transfer_ref: null
  custody_transfer_ref: null
```

Donation does not automatically mean unconditional ownership transfer unless that transfer is authored and valid.

## 13. Debt and credit guardrail

Debt can easily become coercive and tedious.

Default rule:
- do not generate routine consumer debt;
- do not use debt to seize core player progression;
- do not create interest rates dynamically;
- do not infer legal enforcement powers;
- do not make a player accept a loan to continue the main story.

If Ouros later establishes loans, use explicit agreements with clear scope and player consent.

```yaml
financial_claim:
  claim_id: null
  claimant_id: null
  counterparty_id: null
  claim_type: null
  claimed_amount_ref: null
  evidence_ids: []
  agreement_id: null
  status: ASSERTED
```

Claimed debt and verified debt are separate.

## 14. Insurance and risk-transfer guardrail

Insurance is optional worldbuilding. Do not assume it exists everywhere.

If authored:

```yaml
risk_transfer_agreement:
  agreement_id: null
  provider_id: null
  covered_asset_or_activity_ids: []
  covered_event_types: []
  excluded_event_types: []
  valid_from: null
  valid_to: null
  claim_process_ref: null
```

```yaml
coverage_claim:
  claim_id: null
  agreement_id: null
  incident_id: null
  claimant_id: null
  claimed_loss_ids: []
  evidence_ids: []
  status: FILED
```

Possible states:
- FILED
- INFORMATION_REQUIRED
- UNDER_REVIEW
- APPROVED
- PARTIALLY_APPROVED
- DENIED
- WITHDRAWN
- PAID

A denied claim does not imply fraud or bad faith.

## 15. Financial exposure

Narrative risk can be coarse and legible.

```yaml
financial_exposure:
  exposure_id: null
  actor_or_institution_id: null
  source_event_or_agreement_id: null
  exposure_type: null
  severity_band: null
  affected_service_ids: []
  mitigation_ids: []
  known_to_actor_ids: []
```

Suggested qualitative bands:
- LOW
- MODERATE
- HIGH
- CRITICAL

This is narrative state, not a hidden probability formula.

## 16. Budget envelope

Large institutions may have authored budget priorities without simulating every coin.

```yaml
budget_envelope:
  budget_id: null
  institution_id: null
  period_ref: null
  priority_ids: []
  committed_project_ids: []
  protected_service_ids: []
  flexible_capacity_band: null
  funding_source_ids: []
  review_event_ids: []
```

This supports choices such as:
- repair an old bridge;
- expand clinic capacity;
- fund a research expedition;
- increase transport frequency;
- defer a museum renovation.

The game can represent the choice without calculating municipal accounting.

## 17. Funding review

```yaml
funding_review:
  review_id: null
  agreement_or_program_id: null
  reviewer_ids: []
  evidence_ids: []
  milestone_assessments: []
  compliance_findings: []
  outcome: null
  next_review_time: null
```

Possible outcomes:
- CONTINUE
- CONTINUE_WITH_CHANGES
- PAUSE
- EXTEND
- REDUCE_SCOPE
- COMPLETE
- END

Reviews must assess authored conditions. They cannot rewrite history to justify a desired outcome.

## 18. Procurement linkage

Procurement is connected to workshops, infrastructure and institutions.

A financial agreement may authorize acquisition of an asset, but physical procurement still needs:
- an actual supplier;
- an available route;
- item/material provenance;
- delivery;
- custody/ownership transfer;
- technical compatibility;
- implementation support when mechanical items are involved.

A paid invoice does not teleport an object into inventory.

## 19. Economic shock

```yaml
economic_shock:
  shock_id: null
  source_event_ids: []
  affected_region_ids: []
  affected_service_ids: []
  affected_funding_program_ids: []
  severity_band: null
  start_time: null
  recovery_state_id: null
```

Potential causes:
- route closure;
- harvest failure;
- disaster;
- major discovery boom;
- major employer closure;
- tournament/festival influx;
- infrastructure failure;
- ecological restriction;
- loss of a funding source.

Do not create random recessions merely to generate quests.

## 20. Relief funds

Relief support should connect directly to the crisis/recovery layer.

```yaml
relief_fund:
  fund_id: null
  crisis_id: null
  provider_ids: []
  eligible_need_categories: []
  supported_location_ids: []
  distribution_actor_ids: []
  remaining_capacity_band: null
  transparency_record_ids: []
```

A relief fund can run short without implying theft.

A local group can disagree with allocation priorities without either side becoming villainous.

## 21. Player consent and multiplayer

A player's financial agreement binds only actors who explicitly accepted it or institutions they are authorized to represent.

One player cannot:
- take a loan on behalf of another PC;
- pledge another player's property;
- accept sponsorship obligations for another player's club;
- spend another player's restricted funding;
- make another PC responsible for a penalty.

Shared clubs/institutions need explicit governance/authorization state.

## 22. Privacy

Financial details are private by default unless world state says otherwise.

Possible public facts:
- a sponsor relationship;
- an announced grant;
- a publicly funded project;
- a published prize pool;
- a donor plaque.

Possible private facts:
- exact balance;
- rejected applications;
- private scholarship terms;
- unpaid commitments;
- insurance or debt claims;
- internal budget pressure.

Media and rumor layers may report claims, but publication does not make them true.

## 23. Minecraft representation

Financial state should appear through understandable physical consequences rather than spreadsheets everywhere.

Examples:
- sponsor banners at a venue;
- donated equipment with provenance plaque;
- construction that starts only after funding is secured;
- an unfinished expansion when funding pauses;
- a research board showing project status;
- a relief distribution station;
- a closed service window caused by budget/staff limits;
- a renovated facility after a successful funding cycle;
- fewer services during a funding gap.

Do not display exact private balances above NPC heads.

## 24. Routine finance compression

Compress ordinary transactions when they do not create a meaningful decision.

Examples that usually compress:
- buying routine food;
- ordinary lodging;
- normal transit fares;
- incidental supplies;
- small household expenses.

Expand finance when it changes:
- access;
- obligations;
- ownership/custody;
- institutional capacity;
- project timing;
- risk;
- public reputation;
- future opportunities;
- relationships between institutions.

## 25. No-inference rules

Do not infer:
- corruption from wealth;
- criminality from unpaid money;
- poverty from one missed payment;
- ownership from sponsorship;
- control from donation;
- political authority from economic influence;
- friendship from patronage;
- exploitation from every commercial relationship;
- consent from silence;
- mechanical reward from narrative funding;
- bankruptcy, taxes or legal enforcement without authored rules.

## 26. PTU/Caelo boundary

This layer does not define:
- money values;
- starting funds;
- prices;
- Job payouts;
- Trainer battle payouts;
- Contest or tournament prizes;
- salaries;
- crafting costs;
- item resale rules;
- grants;
- interest;
- insurance premiums;
- taxes;
- fines;
- debt collection;
- shop inventory formulas;
- sponsor combat bonuses.

Exact mechanics remain governed by the project-supplied PTU/Caelo corpus and explicit Ouros implementation decisions.

## 27. AutoPTU boundary

Financial state normally does not require AutoPTU.

A sponsorship agreement, grant, prize or payment record must never modify battle rules directly.

If a funded scenario creates a tactical encounter, the encounter must use the normal implementation contract and capability map.

## 28. Encounter contract — Grant Shipment Chokepoint

Narrative premise:
A research grant purchased legitimate field equipment. The shipment reaches a blocked route during an unrelated conflict. The equipment is cargo, not a combatant.

FULL version dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — BLOCKING if cargo movement and interception occur inside battle
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if relevant
- terrain/weather/hazards/zones/reactions — BLOCKING if the route has tactical hazards
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL family; any exact required Feature needs direct parity evidence
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Keep the shipment and driver outside the tactical grid. Players clear a static legal chokepoint battle. Delivery, custody and grant inventory update in world state after the battle.

## 29. Encounter contract — Sponsored Exhibition Interruption

Narrative premise:
A public sponsored exhibition is interrupted by a genuine safety incident. Sponsor branding and financial state are background context only.

FULL version dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception — BLOCKING for live crowd protection
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage/status/moves/abilities/items — PARTIAL as used
- terrain/hazards/zones/reactions — BLOCKING for dynamic venue conditions
- Trainer Features/perks — PARTIAL family; exact Feature proof required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protection/evacuation objectives
- adapter/playback — BLOCKING

REDUCED version:
Pause the exhibition. Resolve audience evacuation in overworld state. Run a conventional static battle in a cleared arena. Resume or cancel the event afterward based on world state.

## 30. Encounter contract — Claims Survey at the Warehouse

Narrative premise:
After a warehouse incident, staff document damage for an authored coverage or funding review. A wild Pokémon disturbance occurs during the survey.

FULL version dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — BLOCKING if rubble or moving machinery forces movement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage/status/moves/abilities/items — PARTIAL as used
- terrain/weather/hazards/zones/reactions — BLOCKING for unstable floor, smoke, machinery or protected survey zones
- Trainer Features/perks — PARTIAL family; exact technical/support Feature proof required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING if the encounter uses protect-objective logic
- adapter/playback — BLOCKING

REDUCED version:
Complete the damage survey before combat starts. Move people and documents to a safe area. Run a normal static encounter. The financial claim is resolved later from agreement/evidence state, never from the battle outcome alone.

## 31. Promotion checklist

Before any finance candidate becomes canon:
1. Confirm the relevant institution exists.
2. Confirm the funding relationship is culturally and politically plausible.
3. Confirm whether the amount needs an actual mechanical value.
4. Validate any PTU/Caelo money/reward rule involved.
5. Confirm ownership and authority are not inferred from funding.
6. Confirm multiplayer consent for shared obligations.
7. Confirm privacy/public disclosure rules.
8. Confirm no sponsor condition grants an unsupported battle bonus.
9. Confirm any tactical scenario has FULL/REDUCED capability contracts.
10. Record provenance and final human approval.
