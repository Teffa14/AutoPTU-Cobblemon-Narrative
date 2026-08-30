# Engine Readiness Snapshot — Pass 143

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-30

This snapshot records repository inspection, live engine evidence and permanent capability dependencies checked while adding optional insurance, coverage-claim and loss-adjustment continuity.

AutoPTU-Java and AutoPTU were inspected read-only. Pass 143 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 143:

`d900139983fba192b0defee738d89dbf701f3738`

The complete recursive narrative tree was inspected before topic selection and returned `truncated: false`.

No dedicated insurance/claim/loss-adjustment continuity extension existed.

The selected gap was checked against:

- Finance, Sponsorship, Patronage & Risk;
- Case, Authority & Custody;
- Facility Maintenance, Repair & Inspection;
- Wreck Sites, Salvage, Recovery & Preservation;
- Material Culture;
- Found Property;
- Procurement;
- Building Safety;
- Crisis/Rescue;
- Public Adjudication/Review;
- Human Identity;
- Place Reference;
- PTU/Caelo source scan;
- Pass 142 engine snapshot.

Finance already contains a minimal optional `risk_transfer_agreement` and `coverage_claim` guardrail and says insurance remains disabled unless explicitly authored. Pass 143 therefore deepens chronology only. It does not establish insurance as canon or create a parallel financial owner.

## Research relevance

Public Pokémon material supplied high-level story structures:

- Pokémon Ranger bridge disruptions show that physical restoration can have its own operational chronology independent from any later financial response.
- Ranger optional requests show that reports can be genuine, incomplete and clarified through field inspection.
- Mystery Dungeon rescue communities reinforce the separation between request creation, sufficient information, arrival and actual completion.
- Pokémon fanfiction/community discussions about collateral damage show that writers naturally ask who bears losses in a world with powerful Pokémon, while disagreeing strongly on legal answers. The disagreement supports regional variation rather than one universal liability regime.

Operational public sources from FEMA and NAIC supplied provenance architecture only:

- notice of loss;
- claim opening;
- reviewer/adjuster assignment;
- inspection;
- evidence submission;
- estimate/adjustment;
- coverage decision;
- amendment/supplement;
- settlement/payment;
- complaint/review.

No external law, deadline, policy form, regulator, valuation standard or licensing regime becomes Ouros canon.

## AutoPTU-Java live evidence

Current head inspected:

`aef04061c27b9c7611e96d7287fc7d9ce98afb0e`

Commit:

`Add server-owned terrain context label resolver (#283)`

This is newer than the Pass 142 head `5f8c23950e5689a771b9c9d0772e7cc60e9a8197`.

The commit adds `TerrainContextLabelResolver` and tests. The resolver derives terrain-context labels from authoritative battle state rather than Minecraft/Cobblemon presentation. Live code inspected in the commit shows inputs including:

- active field terrain / legacy terrain name;
- combatant position;
- movement-grid tile type;
- temporary terrain aliases.

The resolver normalizes labels and is wired into the Intercept parity workflow together with the previously added `TerrainSkillCheckBonusResolver`.

This is meaningful progress in server-owned terrain-context derivation for the exact covered Intercept/Naturewalk-related path.

It does not verify the complete permanent terrain family.

It does not establish:

- generalized terrain object lifecycle;
- arbitrary terrain creation/removal;
- weather lifecycle;
- hazards;
- dynamic zones;
- generalized reactions;
- competing-reaction ordering;
- environmental forced movement;
- broad Push/Pull/Knockback;
- every Intercept/forced-movement case;
- escort semantics;
- fragile-property tactical interactions;
- destructible-object rules;
- worksite collapse rules;
- claim/evidence semantics;
- tactical policy;
- Minecraft/Cobblemon/Craftics semantic claim playback.

No permanent capability category is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 143.

The change remains presentation-only. It synchronizes cached Pixi screen dimensions after viewport resize so sprite destinations use live renderer geometry and explicitly does not alter battle rules or outcomes.

It provides no semantic support for:

- claim state;
- coverage decisions;
- evidence custody;
- damage valuation;
- repair completion;
- settlement;
- private information visibility;
- world-state handoffs after battle.

## Permanent capability map — Pass 143

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Static reviewed BattleSpecs can rely on the established spatial targeting baseline. This does not make damaged property or claim evidence targetable tactical objects.

`base movement legality`

Conventional static movement remains verified. It does not establish unstable worksite movement, moving debris, escort movement or special inspection zones.

`core calculations`

The established parity-backed baseline remains verified. It does not provide property valuation, repair costing, collateral-damage accounting or destructible-building calculations.

`action economy/initiative`

Conventional combatant action economy remains verified. It does not define claim workflow timing or worker/assessor evacuation stages.

`AI legal-action infrastructure`

Legal action enumeration/validation remains verified. It does not provide objective-aware policy for protecting a survey approach, clearing a handoff route or withdrawing from a repair site.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

Specific Intercept paths have increasingly strong evidence, now including server-owned terrain labels and terrain skill-check inputs. The combined family remains partial. Broad Push, Pull, Knockback, all forced-movement sources, escort semantics and fragile-edge/worksite movement remain unverified.

`full turn/round lifecycle`

Ordinary tactical progression exists. Staged withdrawal, timed evacuation and multi-phase worksite objectives have not been verified as a complete family.

`full stateful damage pipeline`

Substantial implementation exists, but family completeness has not been established. It must not be repurposed into generic property HP, structural damage or claim valuation.

`status lifecycle`

Use only exact implemented combat statuses. Pass 143 does not create tactical `CLAIM_PENDING`, `EVIDENCE_SECURED`, `DAMAGED_PROPERTY`, `UNDER_REPAIR` or `COVERED` statuses.

`move-specific behavior`

Representative coverage does not establish interactions with buildings, claim evidence, repair materials or controlled cargo.

`abilities`

Representative Ability coverage remains partial. No Ability automatically determines causation, evidence authenticity, loss value or institutional authority.

`items`

Items remain partial. A claim file, estimate, policy representation, repair invoice or recovered cargo record is not automatically a PTU combat Item.

`Trainer Features/perks`

Server-owned Naturewalk/terrain-context evidence is localized. The family remains partial. No Feature creates universal adjuster, insurer, investigator, lawyer, appraiser or repair authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The new terrain label resolver strengthens a narrow exact path but does not complete this family. Rich damage-site scenes can require unstable zones, protected evidence areas, active worksite hazards, changing geometry, weather phases or generalized reactions.

`AI tactical policy`

Rich variants may require `PROTECT`, `WITHDRAW`, `CLEAR_ROUTE`, `HOLD_POSITION`, `AVOID_HAZARD` or escort-aware behavior. Legal-action infrastructure alone does not provide those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

No live evidence establishes semantic projection of claim state, coverage, inspection, evidence visibility, repair handoff or settlement. Minecraft/Cobblemon remains presentation only for authored world state.

## PTU/Caelo mechanical guardrails

The project source scan supports campaign plots, character arcs, sandbox activities, Jobs, exploration and exact location mechanics when the governing source defines them. It does not establish a universal insurance/liability/property-damage subsystem.

Remain UNKNOWN until exact source/tests/contracts establish them:

- universal insurance institutions;
- mandatory Trainer liability coverage;
- Pokémon medical insurance;
- property/cargo/event insurance;
- premiums;
- deductibles;
- policy limits;
- claim deadlines;
- valuation/depreciation/replacement-cost formulas;
- business-interruption formulas;
- subrogation;
- generic negligence/liability rules;
- battle-collateral compensation;
- universal property HP/Armor/DR;
- universal structural-damage rules;
- generic claim/adjustment Skill Checks;
- generic fraud-detection checks;
- Technology Education as adjustment authority;
- General Education as policy interpretation authority;
- Guile as automatic deception/fraud detection;
- Perception as automatic loss valuation;
- Command as institutional decision authority;
- Trainer Classes/Features as insurer/adjuster/legal licenses;
- species/Type/Move/Ability as automatic valuation, authentication, causation or repair competence.

No narrative scene may invent these semantics.

## Encounter review — Damage Survey Access Perimeter

Narrative premise:

An assessor needs later access to a damaged exterior after the acute emergency has ended. An unrelated tactical threat occupies the immediate approach.

Full intended dependencies:

- targeting/footprints/range/LoS — VERIFIED for static reviewed geometry;
- base movement legality — VERIFIED for conventional static movement;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for unstable/protected zones/generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Assessor, claimant, private records and controlled property leave the tactical space before BattleSpec creation.
2. Facility/physical owners freeze damaged areas and restrictions.
3. Ouros selects explicit legitimate combatants.
4. AutoPTU receives static reviewed geometry in a safe adjacent area.
5. No destructible-property, evidence-integrity or dynamic-hazard rule is invented.
6. Tactical victory may create only `IMMEDIATE_SURVEY_APPROACH_CLEAR`.
7. The claim inspection happens afterward as a separate noncombat event.

`TACTICAL_VICTORY != CLAIM_APPROVED`.

`TACTICAL_VICTORY != INSPECTION_COMPLETED`.

`INSPECTION_COMPLETED != COVERAGE_CONFIRMED`.

## Encounter review — Recovered Cargo Handoff Chokepoint

Narrative premise:

A lost/damaged cargo object has been physically recovered and awaits a later controlled handoff while an unrelated threat blocks the approach.

Full intended dependencies use the same permanent families. Rich protection/withdrawal, object zones, Intercept/forced movement, objective policy and semantic playback remain PARTIAL/BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Cargo remains outside BattleSpec under existing world-state custody.
2. Couriers, reviewers and other noncombatants withdraw.
3. No cargo HP, destructible-object or pickup-as-custody mechanic is invented.
4. Ouros selects explicit combatants.
5. AutoPTU resolves a conventional static encounter.
6. Victory creates `IMMEDIATE_HANDOFF_APPROACH_CLEAR` only.
7. Existing custody owners perform any later transfer.
8. Pass 143 consumes the recovery/custody fact without inventing ownership or settlement.

`TACTICAL_VICTORY != CUSTODY_TRANSFERRED`.

`CARGO_RECOVERED != OWNERSHIP_ESTABLISHED`.

`CARGO_RECOVERED != CLAIM_SETTLED`.

## Encounter review — Temporary Repair Site Withdrawal

Narrative premise:

Temporary mitigation or repair work is underway when an independent tactical threat makes the immediate work area unsafe.

Full intended dependencies:

Rich staged worker withdrawal, active hazards, changing geometry, Intercept/forced movement and objective-aware policy depend on the same PARTIAL/BLOCKING families.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Maintenance pauses the work order in world state.
2. Workers, claim actors, records, tools and controlled materials withdraw before BattleSpec creation.
3. AutoPTU receives reviewed static adjacent geometry.
4. No worksite hazard/damage mechanic is invented.
5. Victory creates `IMMEDIATE_REPAIR_WORK_AREA_CLEAR` only.
6. Maintenance separately decides whether work resumes.
7. Finance/claim state remains unchanged unless later world events justify change.

`WORK_AREA_CLEAR != REPAIR_RESUMED`.

`REPAIR_RESUMED != REPAIR_COMPLETE`.

`REPAIR_COMPLETE != CLAIM_SETTLED`.

## Reduced-version implementation rule

The claim-continuity layer can advance now because claims are primarily world-state records and reduced tactical scenes remove administrative/physical semantics from BattleSpec.

Before battle, world owners resolve or freeze:

- claim existence;
- agreement/coverage scope;
- claimant/beneficiary identity;
- evidence custody;
- physical damage state;
- repair state;
- cargo/property custody;
- private information visibility;
- noncombatants;
- site restrictions.

Battle receives explicit combatants and static reviewed geometry.

Battle returns only a narrow physical access/perimeter fact.

World owners resume afterward.

## Minecraft/Cobblemon/Craftics boundary

Presentation may display authored consequences such as damaged facades, temporary barriers, reopened shops, repair overlays, claim-office/service counters where canon supports them, archive boxes, recovered cargo or replacement objects.

It may not infer:

- a claim from visible damage;
- coverage from an NPC's presence;
- claim approval from a document prop;
- causation from block damage;
- ownership from chest contents;
- repair completion from a visual swap;
- settlement from a repaired building;
- battle participants from proximity;
- evidence authenticity from an item entity.

Cobblemon BattleState remains non-authoritative for combatants, legality, HP/status, tactical position and world consequences.

## Canon questions left open

Pass 143 deliberately does not decide:

- whether insurance exists anywhere in Ouros;
- regional risk-sharing models;
- private/cooperative/civic/guild/League-linked providers;
- covered subjects/events;
- Pokémon-related damage treatment;
- claim eligibility;
- scope/exclusions;
- premiums/deductibles/limits;
- intake/evidence customs;
- assessor/reviewer authority;
- valuation methods;
- settlement forms;
- review/appeal paths;
- privacy;
- named claim institutions or recurring NPCs;
- historic claims that belong to canon.

## Pass 143 conclusion

The narrative repository can safely add optional claim/loss-adjustment continuity as PROPOSED world-state architecture because it extends the existing Finance guardrail without enabling insurance by default.

AutoPTU-Java gained meaningful server-owned terrain-context evidence in `aef04061...`, but that work remains localized to the covered terrain/Intercept path. Permanent capability status remains unchanged from Pass 142.

Rich claim-site tactical scenes remain blocked by exact missing movement, hazard/reaction, policy and adapter families. Reduced static variants are READY and keep coverage, evidence, repair and settlement under their proper world-state owners.