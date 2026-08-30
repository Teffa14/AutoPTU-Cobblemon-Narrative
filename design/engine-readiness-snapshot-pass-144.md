# Engine Readiness Snapshot — Pass 144

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-30

This snapshot records repository inspection, live engine evidence and permanent capability dependencies checked while adding proposed after-sale return, warranty, repair, replacement and reissue continuity.

AutoPTU-Java and AutoPTU were inspected read-only. Pass 144 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 144:

`993adcc0e6e955c7eafc7c2de14257d326721a8f`

The complete recursive narrative tree was inspected before topic selection and returned `truncated: false`.

The selected gap was checked against:

- Commercial Services / Storefront Continuity;
- Procurement / Supplier Fulfillment;
- Material Culture / Crafting / Repair;
- Facility Maintenance;
- Finance;
- Agreements / Mediation;
- Batch Traceability / Recall;
- Insurance / Claims;
- Courier;
- Shared Equipment;
- Case / Authority / Custody;
- PTU/Caelo source scan;
- Pass 143 engine snapshot.

Existing owners already cover sale/service surfaces, receipt, initial discrepancies, physical item identity, technical repair records, money, shipments, recall and optional insurance. No dedicated layer preserved the customer/provider lifecycle from later return request through authorization, intake, diagnosis linkage, remedy selection, repair/replacement/exchange, reissue and final handback.

GitHub code search for `warranty guarantee return exchange replacement after-sales RMA` in the narrative repository returned no matching dedicated implementation before Pass 144.

## Research relevance

Public Pokémon material supplied a useful local-policy pattern:

- Rydel's Cycles allows repeated exchange between two bicycle configurations while other bicycle-shop choices elsewhere can behave differently.
- The reusable lesson is that provider-specific exchange practice can exist without creating a universal return rule.

Public operational sources supplied provenance architecture only:

- GS1 supports stable traceability across maintenance, repair and overhaul cycles;
- Cisco separates support case, return authorization, replacement status, replacement shipment and return of replaced material;
- FTC guidance distinguishes warranty, separately purchased service arrangements and different remedies such as repair, replacement and refund.

No external consumer law, mandatory remedy, return window, warranty duration, disclosure rule, serial-number standard or regulator becomes Ouros canon.

## PTU/Caelo guardrail

Internal project source-scan evidence supports campaign plots, character arcs, sandbox activities, Jobs and exact mechanical location/item interactions when a governing source defines them.

Material Culture already requires exact rules references for crafting and repair effects.

No reviewed source establishes a universal after-sale subsystem.

Remain UNKNOWN until exact source/tests/contracts establish them:

- universal return windows;
- universal warranties/guarantees;
- automatic exchange rights;
- automatic replacement rights;
- generic refund rights;
- generic defect or misuse checks;
- universal item durability or breakage;
- generic repair success rules beyond exact implemented mechanics;
- service contracts as PTU Items;
- receipts/warranty cards as combat Items;
- Technology Education as universal repair/service authority;
- General Education as universal warranty interpretation;
- Guile as automatic false-claim detection;
- Perception as automatic technical diagnosis;
- Trainer Features/perks as seller, maker or warranty authority;
- species/Type/Move/Ability as automatic item repair, authentication or remedy eligibility.

No narrative scene may invent these mechanics.

Pokémon are living actors and are excluded from product return, replacement, warranty and loaner semantics.

## AutoPTU-Java live evidence

Current head inspected:

`aef04061c27b9c7611e96d7287fc7d9ce98afb0e`

Commit:

`Add server-owned terrain context label resolver (#283)`

No newer AutoPTU-Java commit was present during Pass 144.

The live commit remains the same evidence recorded in Pass 143. `TerrainContextLabelResolver` derives normalized terrain-context labels from authoritative battle state using active field terrain, combatant position, movement-grid tile type and temporary terrain aliases, and is gated through the Intercept parity workflow.

This strengthens one exact server-owned terrain-context path associated with the covered Intercept/Naturewalk behavior.

It does not establish:

- generalized terrain-object lifecycle;
- arbitrary terrain creation/removal;
- weather lifecycle;
- hazards;
- dynamic zones;
- generalized reactions;
- competing-reaction ordering;
- environmental forced movement;
- broad Push/Pull/Knockback;
- every Intercept case;
- escort semantics;
- object pickup/carry/drop semantics;
- destructible service counters;
- generic item HP/durability;
- repair/warranty/customer-service mechanics;
- tactical policy;
- Minecraft/Cobblemon/Craftics semantic after-sale playback.

No permanent capability family is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 144.

The change remains presentation-only. It keeps cached Pixi dimensions synchronized after viewport resize and explicitly does not change battle rules or outcomes.

It provides no semantic support for return authorization, item custody, defect diagnosis, remedy selection, repair completion, replacement issue, refund settlement or service-case state.

## Permanent capability map — Pass 144

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Static reviewed BattleSpecs can rely on the established spatial baseline. This does not make serviced objects, parcels, repair counters or replacement units tactical targets by default.

`base movement legality`

Conventional static movement remains verified. It does not establish moving carts, escort movement, restricted service zones or object-carry movement.

`core calculations`

The parity-backed baseline remains verified. It does not provide defect diagnosis, item valuation, durability, repair cost or refund calculation.

`action economy/initiative`

Conventional combatant action economy remains verified. It does not define customer evacuation stages, item handoff timing or repair workflow.

`AI legal-action infrastructure`

Legal action enumeration/validation remains verified. It does not provide policy for protecting exits, withdrawing from a counter, guarding a handoff approach or avoiding controlled property.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

Specific Intercept evidence is strong for covered paths, including server-owned terrain context and skill-check inputs. The family remains partial. Broad Push/Pull/Knockback, every forced-movement source, escort/object-carry movement and fragile-edge behavior remain unverified.

`full turn/round lifecycle`

Ordinary tactical progression exists. Staged staff withdrawal, timed handoffs and multi-phase service-area objectives are not verified as a complete family.

`full stateful damage pipeline`

Substantial implementation exists, but family completeness remains unproven. It must not be repurposed into generic product durability, property HP or repair accounting.

`status lifecycle`

Use only exact implemented combat statuses. Pass 144 does not create combat statuses such as `UNDER_WARRANTY`, `RETURN_AUTHORIZED`, `REPAIR_PENDING`, `LOANER`, `REPLACEMENT_ALLOCATED` or `REFUND_APPROVED`.

`move-specific behavior`

Representative coverage does not establish effects on controlled goods, service counters, stored replacements or repair equipment.

`abilities`

Representative Ability coverage remains partial. No Ability automatically diagnoses a defect, authenticates a claim, grants provider authority or repairs an item unless exact governing rules say so.

`items`

Mechanical Item coverage remains partial. A receipt, warranty representation, service ticket, repair tag, RMA-like authorization or replacement box is not automatically a combat Item.

`Trainer Features/perks`

Server-owned terrain/Naturewalk evidence remains localized. No Feature creates universal repair, warranty, merchant, customer-service or adjudication authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich service/workshop encounters may need protected zones, moving obstructions, weather residue, active shop hazards or generalized reactions. The localized terrain resolver does not complete this family.

`AI tactical policy`

Rich variants may require `PROTECT_EXIT`, `WITHDRAW`, `CLEAR_ROUTE`, `HOLD_POSITION`, `AVOID_CONTROLLED_AREA` or escort-aware behavior. Legal-action infrastructure alone does not provide these policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

No live evidence establishes semantic projection of service-case state, return authorization, repair status, replacement allocation, custody, refund settlement or customer notification. Minecraft/Cobblemon remains presentation for facts already decided by Ouros.

## Encounter review — Repair Counter Withdrawal

Narrative premise:

A provider has accepted a story-significant non-living item for later assessment. An unrelated tactical threat reaches the public service area while staff and customers are withdrawing.

Full dependencies:

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

1. Staff, customers, private records and serviced objects leave BattleSpec.
2. Material Culture/Courier/after-sale owners freeze custody and case state.
3. Ouros selects explicit combatants.
4. AutoPTU receives reviewed static geometry.
5. No destructible-counter, item-HP, theft, pickup or custody mechanic is invented.
6. Victory may create only `IMMEDIATE_SERVICE_AREA_CLEAR`.
7. World-state owners resume the service case afterward.

`TACTICAL_VICTORY != RETURN_AUTHORIZED`.

`TACTICAL_VICTORY != DEFECT_CONFIRMED`.

`TACTICAL_VICTORY != REPAIR_COMPLETED`.

## Encounter review — Replacement Handoff Chokepoint

Narrative premise:

A replacement has been allocated and is waiting for a later controlled handoff while an unrelated threat blocks the approach.

Full rich semantics remain dependent on the same PARTIAL/BLOCKING movement, lifecycle, terrain/reaction, tactical-policy and adapter families.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Replacement asset remains outside BattleSpec.
2. Original-item custody state remains frozen.
3. Staff/couriers/noncombatants withdraw.
4. Ouros selects legitimate combatants.
5. AutoPTU resolves a static encounter on adjacent geometry.
6. Victory creates `IMMEDIATE_HANDOFF_APPROACH_CLEAR` only.
7. Existing world-state owners perform later custody/ownership/issue events.

`APPROACH_CLEAR != REPLACEMENT_ISSUED`.

`REPLACEMENT_ISSUED != ORIGINAL_RETURNED`.

`REPLACEMENT_ISSUED != REFUND_SETTLED`.

## Encounter review — Workshop Retrieval Perimeter

Narrative premise:

A technically completed repair waits for pickup while an unrelated tactical threat occupies the workshop approach.

If the intended version uses weather phases, active hazards, changing zones, generalized reactions, escort movement or forced displacement, those exact capability families remain required.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Workshop staff and repaired item remain outside BattleSpec.
2. Technical completion, verification and release state is frozen before combat.
3. AutoPTU receives reviewed static nearby geometry.
4. Victory creates only `IMMEDIATE_WORKSHOP_APPROACH_CLEAR`.
5. Pickup and custody transfer occur afterward.

`REPAIR_COMPLETED != ITEM_RELEASED`.

`ITEM_RELEASED != PICKUP_COMPLETE`.

`APPROACH_CLEAR != OWNERSHIP_CHANGED`.

## Reduced-version implementation rule

Pass 144 can advance before rich tactical support because its primary state is administrative/provenance continuity.

Before battle, world owners resolve or freeze:

- item identity;
- item custody/ownership;
- after-sale case state;
- provider policy/promise version;
- technical repair/condition state;
- replacement allocation;
- loaner custody;
- refund/finance state;
- shipment state;
- private evidence visibility;
- noncombatants.

Battle receives explicit combatants and static reviewed geometry.

Battle returns only a narrow physical-access fact.

World-state owners resume afterward.

## Minecraft/Cobblemon/Craftics boundary

Presentation may display authored consequences such as repair counters, intake shelves, boxed returns, alternate item models, cosmetic repair patches, pickup notices, loaner props and changed storefront signage.

It may not infer:

- return authorization from an item being dropped on a counter;
- ownership from inventory or chest contents;
- a defect from a damaged model;
- repair completion from a texture/model swap;
- replacement entitlement from identical item models;
- refund completion from removal of an item;
- customer deception from missing records;
- combatants from proximity.

Minecraft physics cannot become PTU item durability, collision, theft or object-damage authority.

Cobblemon BattleState remains non-authoritative for combatants, legality, HP/status, tactical position and world consequences.

## Canon questions left open

Pass 144 deliberately does not decide:

- whether any region recognizes warranties or guarantees;
- which sellers/makers/institutions offer returns or exchanges;
- return windows;
- proof requirements;
- whether promises follow buyer, item or transaction;
- whether service contracts exist;
- available remedies;
- who chooses among remedies;
- whether original return is required for replacement;
- whether temporary loaners exist;
- refurbishment/pre-owned practices;
- provider succession of old service cases;
- privacy rules;
- legal enforcement;
- named providers or recurring service NPCs;
- exact PTU/Caelo repair mechanics beyond already governed rules.

## Pass 144 conclusion

The narrative repository can safely add proposed after-sale continuity as an orchestration layer because existing owners already control physical items, repair mechanics, custody, shipments and money.

The live engine heads remain unchanged from Pass 143. Permanent capability status therefore remains unchanged.

Rich service/workshop tactical variants remain blocked by exact movement, terrain/reaction, tactical-policy and adapter families. Reduced static variants are READY and keep after-sale semantics outside BattleSpec.