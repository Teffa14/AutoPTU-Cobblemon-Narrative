# Ouros Narrative Research — Insurance, Coverage, Claims & Loss Adjustment — Pass 143

Status: RESEARCH ONLY. Provenance and design evidence. Not Ouros canon.
Date: 2026-08-30

## Scope

This pass investigates a narrow continuity gap around optional insurance or other authored risk-transfer arrangements:

incident or loss -> notice -> claim -> evidence -> coverage review -> damage/loss assessment -> decision -> repair/recovery handoff -> settlement or closure -> later review.

The repository already contains a minimal insurance/risk-transfer guardrail in `design/finance-sponsorship-risk-layer.md`. That file deliberately leaves insurance disabled unless Ouros explicitly establishes institutions and rules. Pass 143 therefore does not introduce insurance as universal canon and does not create a second finance system.

The research goal is to provide provenance architecture and narrative patterns that can be used only if a region or institution later authors risk-transfer arrangements.

## Repository inspection before research

The complete recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected before topic selection. GitHub returned `truncated: false` at head:

`d900139983fba192b0defee738d89dbf701f3738`

The tree contained no dedicated insurance/claims/loss-adjustment continuity extension or research scan.

The gap was cross-checked against these existing owners:

- `design/finance-sponsorship-risk-layer.md`
- `design/case-authority-custody-layer.md`
- `design/facility-maintenance-repair-inspection-extension.md`
- `design/wreck-sites-salvage-recovery-preservation-extension.md`
- `design/material-culture-economy-crafting-layer.md`
- `design/found-property-custody-restitution-extension.md`
- `design/procurement-commissions-supplier-fulfillment-extension.md`
- `design/building-safety-occupancy-reentry-assessment-continuity-extension.md`
- `design/crisis-rescue-recovery-layer.md`
- `design/public-adjudication-review-compliance-continuity-extension.md`
- `design/human-identity-name-record-continuity-extension.md`
- `design/place-name-address-location-reference-continuity-extension.md`
- `research/2026-08-18-source-scan.md`
- `design/engine-readiness-snapshot-pass-142.md`

### Existing boundary that must remain authoritative

Finance already defines optional `risk_transfer_agreement` and `coverage_claim` records and explicitly states that loan, credit and insurance categories remain disabled unless Ouros establishes them.

Pass 143 therefore concentrates on continuity around those records rather than replacing them.

Finance continues to own:

- financial agreements;
- payment commitments/events;
- financial exposure;
- mechanical-money boundaries;
- settlement/payment provenance where money is actually transferred.

Other existing owners retain:

- physical damage, faults, repair and reopening: Facility Maintenance / relevant infrastructure owner;
- incident truth, evidence custody and formal investigation: Case/Authority when applicable;
- item identity and provenance: Material Culture;
- wreck-site history and recovery context: Wreck Sites;
- ownership/custody questions: their existing owners;
- emergency stabilization: Crisis/Rescue;
- adjudication or formal review authority: existing authored institutional systems.

## Public Pokémon-world research

### Pokémon Ranger: Shadows of Almia — Norward Bridge interruption

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Brook
- https://bulbapedia.bulbagarden.net/wiki/Appendix%3APok%C3%A9mon_Ranger_2_walkthrough/Section_4

Observed high-level structure:

A transport asset becomes unavailable because the operating key is lost. The disruption has a specific operational cause, a responsible operator, a recovery mission and an explicit service-restoration step after the key returns.

Reusable Ouros lesson:

Physical or operational restoration and financial recovery can be separate timelines. An asset may return to service before any claim, reimbursement, compensation, dispute or accounting record is closed. Conversely, an approved financial response cannot physically reopen the asset.

Transformation boundary:

Pass 143 does not copy Brook, Sharpedo, the key-retrieval sequence, Ranger ranks, Poké Assists or the bridge layout. The reusable structure is only:

`LOSS_OR_DISRUPTION_RECORDED -> RESOURCE_OR_ASSET_RECOVERY -> OPERATIONAL_RESTORATION`, with any financial/risk-transfer process running independently.

### Pokémon Ranger: Guardian Signs — damaged bridge and delayed repair

Public source:

- https://pokemon.fandom.com/wiki/Big_Booker_Bridge

Observed high-level structure:

A bridge can be damaged enough that ordinary passage is interrupted while an alternative traversal method exists temporarily and repairs take longer than the immediate adventure beat.

Reusable Ouros lesson:

Damage, mitigation, temporary access, repair start and full restoration should remain separate facts. A claim can therefore reference the same loss while the physical world moves through several operational states.

Source caution:

This is a community-maintained reference. It is used only for broad narrative structure. No factual detail from it becomes Ouros canon.

### Pokémon Ranger: Shadows of Almia — optional requests and field problems

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Walkthrough%3APok%C3%A9mon_Ranger%3A_Shadows_of_Almia/Part_2
- https://gamefaqs.gamespot.com/ds/944533-pokemon-ranger-shadows-of-almia/faqs/55434

Observed high-level structure:

Small field problems can originate from ordinary residents and local observations rather than central plot authorities. Some reports prove mundane, some require clearing an obstruction, and some reveal information only after direct inspection.

Reusable Ouros lesson:

A reported loss should begin as a claim about what happened, not as omniscient truth. The player may inspect a location, compare records, recover evidence or discover that the original description was incomplete without turning the claimant into a liar.

No quest text, rewards, characters or exact events are copied.

### Mystery Dungeon rescue-request communities

Sources:

- https://www.reddit.com/r/MysteryDungeon/comments/14ye7sg
- https://www.reddit.com/r/MysteryDungeon/comments/qvadaz

Observed high-level structure:

Community rescue workflows distinguish a request from the information needed to execute it and distinguish reaching the relevant location from actually satisfying the mission condition.

Reusable Ouros lesson:

Claims and loss reports benefit from explicit completeness state. A notice can be timely and genuine while still missing fields required for review. Likewise, an inspector arriving at a site does not mean evidence has been collected, the claim has been evaluated or the matter has been resolved.

These Reddit discussions are community-practice signals, not PTU rules or Pokémon canon.

### Pokémon fanfiction community — collateral damage as a worldbuilding question

Source:

- https://www.reddit.com/r/pokemonfanfiction/comments/rd79iv

Observed high-level structure:

Writers repeatedly notice that a world with powerful Pokémon raises questions about collateral damage, emergency response, responsibility, rebuilding and who bears loss. Responses disagree strongly about legal consequences, which is itself the useful evidence.

Reusable Ouros lesson:

Do not assume one universal liability regime. Different regions can plausibly have different risk-sharing customs or institutions, and some may have none. The repository should separate:

- what physically happened;
- who claims responsibility;
- whether responsibility is established;
- whether a risk-transfer agreement responds;
- who actually pays or supplies repairs.

Community opinions about imprisonment, damages, licenses or legal doctrine are not imported.

### Pokémon community discussion — speculative insurance exclusions

Source:

- https://www.reddit.com/r/MandJTV/comments/1nw6wv0

Observed high-level structure:

Fans immediately speculate that Pokémon-related damage would create complex coverage boundaries and exclusions.

Reusable Ouros lesson:

Coverage should be authored from explicit scope and exclusions rather than inferred from the dramatic importance of an incident. A catastrophic event does not automatically mean a policy responds; a denied claim does not automatically imply fraud, cruelty or corruption.

This source is treated only as a design-signal showing the question naturally arises in Pokémon-flavored worldbuilding.

## Public operational research

Operational sources are used only for provenance architecture. Real-world law, deadlines, regulators, required documents, policy wording and consumer obligations do not become Ouros rules.

### FEMA flood-claim lifecycle

Sources:

- https://www.fema.gov/sites/default/files/documents/fema_fim-appendix-e-claims_apr2021.pdf
- https://www.fema.gov/sites/default/files/2020-07/fema_nfip_claims-manual_2020.pdf
- https://emilms.fema.gov/IS1104/groups/320.html

High-level operational pattern:

A loss can generate notice to an insurer, adjuster assignment, site inspection, damage estimate, supporting documentation, a claimant statement of loss, review, payment decision and later amendments when new information appears.

Reusable Ouros structure:

Keep these events separate:

- loss observed;
- notice submitted;
- claim created;
- reviewer/adjuster assigned;
- site inspection performed;
- claimant evidence submitted;
- technical estimate produced;
- coverage scope reviewed;
- claimed amount revised;
- decision issued;
- payment/relief action authorized;
- settlement actually delivered;
- later supplemental claim or review.

A reviewer may inspect and recommend without holding final decision authority.

### NAIC consumer claim and complaint guidance

Sources:

- https://content.naic.org/es/article/lo-que-debe-saber-acerca-de-la-presentacion-de-una-reclamacion-para-un-seguro-de-auto-en-caso-de
- https://content.naic.org/consumer/how-to-file-complaint
- https://content.naic.org/consumer/insurance-department-help

High-level operational pattern:

Claims create communication records, damage inspection, adjustment and a result. A person can disagree with that result and use a distinct review/complaint channel. The review channel has its own authority and evidence rather than silently rewriting the original claim event.

Reusable Ouros structure:

`CLAIM_DECISION_ISSUED != CLAIMANT_AGREES`

`CLAIMANT_DISAGREES != DECISION_INVALID`

`COMPLAINT_FILED != ORIGINAL_DECISION_REVERSED`

`ADJUSTER_RECOMMENDATION != FINAL_COVERAGE_DECISION`

The real-world regulatory structure is not imported. Ouros may have an internal review board, guild mediator, civic office, cooperative council, insurer review desk or no appeal mechanism at all depending on authored canon.

## Design synthesis

### Primary worldbuilding value

A risk-transfer continuity layer creates stories after damage without requiring every damaged place to become a villain investigation or a generic repair quest.

Examples of useful dramatic uncertainty:

- the shop reopened before the claim was decided;
- an old photograph proves pre-loss condition but not ownership;
- a contractor estimate and an adjuster estimate describe different repair scopes;
- an event was covered, but one damaged object was excluded;
- the policy was valid but belonged to the previous operator;
- the correct asset was damaged but the wrong identifier was entered;
- a replacement was paid for while the original object was later recovered;
- a claimant reported in good faith before learning that the damage predated the incident;
- a settlement was approved but Finance has not recorded receipt;
- a claim closed without determining historical cause because coverage did not depend on it.

### Strong temporal separations

Keep the following timestamps independent:

- incident/loss time;
- discovery time;
- notice time;
- claim-open time;
- evidence-submission time;
- inspection time;
- estimate/version time;
- coverage-decision time;
- repair authorization time;
- repair completion time;
- settlement authorization time;
- payment/relief receipt time;
- closure time;
- review/reopen time.

Historical conflicts between those dates should create provenance questions rather than automatic accusations.

### Strong semantic separations

- `LOSS_OCCURRED != LOSS_REPORTED`
- `LOSS_REPORTED != LOSS_VERIFIED`
- `DAMAGE_OBSERVED != CAUSE_ESTABLISHED`
- `CAUSE_ESTABLISHED != LIABILITY_ESTABLISHED`
- `LIABILITY_ESTABLISHED != COVERAGE_CONFIRMED`
- `POLICY_ACTIVE != EVENT_COVERED`
- `EVENT_COVERED != EVERY_LOSS_ITEM_COVERED`
- `CLAIM_FILED != CLAIM_COMPLETE`
- `CLAIM_COMPLETE != CLAIM_APPROVED`
- `ADJUSTER_ASSIGNED != CLAIM_DECIDED`
- `ESTIMATE_CREATED != REPAIR_AUTHORIZED`
- `REPAIR_AUTHORIZED != REPAIR_COMPLETED`
- `REPAIR_COMPLETED != SETTLEMENT_PAID`
- `CLAIM_APPROVED != MONEY_RECEIVED`
- `CLAIM_DENIED != FRAUD`
- `CLAIM_REVISED != ORIGINAL_REPORT_FALSE`
- `COMPLAINT_FILED != CLAIM_REOPENED`
- `CLAIM_CLOSED != ALL_HISTORICAL_FACTS_KNOWN`

## PTU/Caelo cross-check

The project-supplied source scan supports campaign plots, character-centric arcs, sandbox activity, Jobs, exploration and location-specific mechanics. It does not establish a universal insurance or liability subsystem.

Pass 143 therefore keeps these mechanics UNKNOWN unless an exact source, test or future Ouros canon establishes them:

- universal insurance institutions;
- mandatory Trainer liability coverage;
- Pokémon medical insurance;
- property insurance;
- cargo insurance;
- premiums;
- deductibles/excess;
- policy limits;
- claim deadlines;
- valuation formulas;
- depreciation;
- replacement-cost formulas;
- business-interruption formulas;
- subrogation;
- generic negligence rules;
- generic liability rules;
- battle-collateral compensation rules;
- universal repair-cost tables;
- universal property HP/Armor/DR;
- Skill Checks that automatically determine claim truth;
- Technology Education as claims expertise;
- General Education as coverage interpretation authority;
- Guile as universal fraud detection;
- Perception as universal damage valuation;
- Command as institutional claim authority;
- Trainer Features that grant insurer/adjuster/legal authority;
- species, Type, Ability or Move that automatically authenticates evidence or determines causation.

If an authored investigation uses a governed Skill Check, the check may reveal or test only the exact information supported by its contract. It cannot replace institutional decision state.

## Battle implementation implications

Most claims work is noncombat world-state logic. Tactical scenes can occur around damaged property or evidence, but battle must never decide coverage, liability, valuation or settlement.

Mechanically rich scenes may depend on:

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

Reduced variants should remove adjusters, claimants, evidence packets, repair crews and controlled property from BattleSpec before combat. Battle should output only a narrow physical fact such as immediate access being safe.

## Research exclusions

This pass does not copy protected prose, dialogue, characters, exact missions, level layouts, rewards or distinctive plots.

It does not import:

- U.S. insurance law;
- FEMA deadlines;
- NAIC regulatory authority;
- policy forms;
- real-world licensing regimes;
- flood-insurance rules;
- real-world claim valuation standards;
- Reddit legal speculation.

External material supplies only high-level structures and provenance lessons.

## Candidate Ouros use

If canon later establishes risk-transfer institutions in one or more regions, Pass 143 supports:

- household/shop damage claims;
- transport-asset loss claims;
- event cancellation/interruption claims;
- cargo loss/damage claims;
- cooperative mutual-aid reimbursement;
- institutional self-insurance analogues;
- disaster recovery reimbursement;
- disputed estimate review;
- supplemental claims after hidden damage becomes visible;
- old claim files as historical evidence;
- reconstruction arcs where finance and physical repair progress on different timelines.

The same architecture also supports non-insurance compensation programs if a canon institution promises bounded reimbursement after specified events.

## Research conclusion

The repository has enough owner boundaries to add claim/loss-adjustment continuity safely as a PROPOSED extension while keeping the existence of insurance itself optional.

The most important design gain is chronology: damage, reporting, evidence, coverage, repair and payment can each be true at different times without one system silently overwriting another.