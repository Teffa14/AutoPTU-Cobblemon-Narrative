# Ouros Narrative Research — After-Sale Return, Warranty, Repair & Replacement Continuity — Pass 144

Status: RESEARCH / PROVENANCE ONLY. This file does not establish Ouros canon.
Date: 2026-08-30

## Scope

This pass investigates a gap between existing commercial, material, procurement, maintenance, finance, recall and insurance systems: what happens after a non-living good has already been acquired and later returns to a seller, maker, workshop or service provider for exchange, diagnosis, repair, replacement, reissue or refund handling.

The pass deliberately does not establish a universal consumer-rights regime, mandatory warranties, standard return windows, manufacturer obligations, prices, refund formulas, defect rules or legal liability.

Pokémon are living actors under Pokémon Agency and related layers. They must never be modeled as warranty goods, replaceable products or returnable inventory.

## Existing-repository inspection

The complete recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected before topic selection and returned `truncated: false` at narrative head `993adcc0e6e955c7eafc7c2de14257d326721a8f`.

Relevant existing owners were checked before writing:

- Commercial Services / Storefront Continuity owns the continuing customer-facing service surface and visible availability.
- Procurement / Supplier Fulfillment owns need, sourcing, order, receipt, discrepancy and initial acceptance.
- Material Culture owns physical item-instance identity, provenance, workshops, crafting and repair records.
- Facility Maintenance owns technical work orders and operational release for facilities.
- Finance owns money, payment and refund settlement.
- Batch Traceability / Recall owns batch-level recall and quarantine state.
- Insurance / Claims owns optional risk-transfer claim chronology and remains disabled unless explicitly canonized.
- Agreements / Mediation owns authored promises, negotiated obligations and disputes.
- Courier owns shipment legs and custody handoffs.
- Shared Equipment owns temporary issue/checkout of shared assets.
- Case / Authority / Custody owns evidence when an object becomes part of an investigation.

No dedicated after-sale lifecycle was found for an acquired non-living item that later enters return authorization, intake, diagnosis, remedy selection, repair/replacement, reissue and owner handback.

## Pokémon source: Rydel's Cycles

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Rydel%27s_Cycles
- https://bulbapedia.bulbagarden.net/wiki/Bicycle_Shop

High-level observation:

Rydel's Cycles allows the player to hold one of two bicycle models and exchange it for the other repeatedly. The two models support different traversal functions. In later material the player can eventually retain both after separate conditions are met.

Reusable structure:

- possession of one asset can be exchanged for another without treating both as simultaneously possessed;
- exchange can change functional configuration while preserving the continuing relationship with a provider;
- a later entitlement can alter the previous one-at-a-time constraint;
- customer/provider history can matter without needing a generic reputation score.

Ouros transformation:

An authored shop, workshop or institution may support an exchange program where a specific item instance is handed back and a different instance is issued. The world must record both custody events. `EXCHANGE_ACCEPTED` does not mean the old object vanished, and `REPLACEMENT_ISSUED` does not prove ownership of both assets.

No Rydel character, dialogue, bicycle rules, advertising quest or Hoenn plot is copied.

## Pokémon source: recurring bicycle shops and variant policies

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Bicycle_Shop
- https://bulbapedia.bulbagarden.net/wiki/Rydel

High-level observation:

Pokémon games present different bicycle-shop policies across regions and generations. Some choices can be changed later; other cosmetic choices cannot. Similar-looking retail/service surfaces therefore need not share one universal exchange rule.

Reusable structure:

Provider policy is local state. One shop allowing exchanges does not establish that every seller in the world accepts returns or exchanges.

Ouros transformation:

Return/exchange eligibility must reference an authored provider policy, agreement, transaction condition or explicit institutional rule. The generator may never infer a universal right from another region or provider.

## PTU community signal

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/r9f6k6/how_can_i_make_a_scavenger_character/

A public PTU discussion mentions crafting and repairing equipment through PTU crafting-related character options and Scrap. The discussion is community guidance rather than rules authority.

Reusable lesson:

The existence of repair-oriented character options does not imply a universal after-sale warranty system. Narrative continuity should reference exact PTU/Caelo mechanics for any mechanical repair effect and keep customer-service promises separate from crafting legality.

## Internal PTU/Caelo cross-check

Internal source-scan evidence already establishes:

- PTU supports campaign plots, character arcs and sandbox activities;
- Caelo supports Jobs and other activity containers that need not become combat;
- exact mechanical effects must come from governing source material;
- location-specific mechanics exist when explicitly defined.

Existing Material Culture architecture already requires rules references for mechanical crafting and repair. No project source reviewed in this pass establishes a universal warranty, return, exchange, refund, service-contract, repair-guarantee or replacement subsystem.

Therefore the following remain UNKNOWN until exact PTU/Caelo text or implementation contracts establish them:

- universal return windows;
- universal warranty periods;
- automatic right to exchange an Item;
- automatic refund rights;
- generic defect diagnosis checks;
- generic repair success checks beyond exact governed mechanics;
- generic replacement entitlement;
- service contracts as PTU Items;
- warranty cards or receipts as mechanical Items;
- Technology Education as universal warranty/repair authority;
- General Education as universal contract interpretation;
- Guile as automatic false-claim detection;
- Perception as automatic defect diagnosis;
- Trainer Features granting seller/manufacturer authority;
- species, Type, Move or Ability as automatic repair, authentication or warranty competence.

## Operational provenance source: GS1 traceability

Source:
- https://www.gs1.org/standards/gs1-global-traceability-standard/current-standard

GS1 describes traceability across the lifetime of a traceable object, including maintenance, repair and overhaul across multiple usage/service cycles.

Reusable structure:

Physical identity can persist through repair cycles. A repaired object can remain the same tracked object while components, condition and custody change.

Ouros transformation:

Use stable `item_instance_id` or another existing asset identity where narrative identity matters. Do not replace identity merely because a component was repaired, cosmetically altered or serviced.

Do not import GS1 identifiers, standards, membership systems or commercial requirements into canon.

## Operational provenance source: Cisco service replacement / RMA

Sources:
- https://www.cisco.com/c/en/us/buy/logistics-support-center.html
- https://www.cisco.com/c/en/us/products/warranties/warr-eltd-life-hw.html

Cisco publicly separates several events:

- opening a support case;
- obtaining return authorization;
- checking replacement status;
- receiving replacement hardware;
- returning replaced material;
- tracking the returned part.

Reusable structure:

A replacement workflow can have two physical objects moving in opposite directions. The replacement arriving does not itself prove the original has been returned. The original being authorized for return does not prove it has entered custody.

Ouros transformation:

Preserve authorization, handoff, shipment, receipt and replacement allocation as distinct events. Courier owns physical shipment/custody legs. After-sale continuity links those events to the service case.

No Cisco contract terms, deadlines, serial-number scheme, logistics SLA or geographic rule becomes Ouros canon.

## Operational provenance source: FTC warranty guidance

Sources:
- https://consumer.ftc.gov/articles/warranties
- https://www.ftc.gov/business-guidance/resources/businesspersons-guide-federal-warranty-law
- https://consumer.ftc.gov/articles/extended-warranties-and-service-contracts

Public FTC guidance distinguishes:

- warranty from separately purchased service contracts;
- scope and duration of coverage;
- repair, replacement and refund as different possible remedies;
- records/proof associated with a purchase;
- claims/service process;
- promises made by different parties.

Reusable structure:

A purchase, warranty promise, service contract, defect report, coverage decision and chosen remedy answer different questions. They should not collapse into one `RETURNABLE=true` flag.

Ouros transformation:

If a region/provider is later canonized to use warranties or guarantees, preserve the actual authored promise and its version. A separate service arrangement can coexist with or outlast another promise. The remedy chosen in one case should be recorded explicitly.

No U.S. law, implied-warranty doctrine, statutory remedy, disclosure requirement, regulator, deadline or mandatory right becomes Ouros canon.

## Operational provenance source: returnable assets

Source:
- https://www.gs1.org/standards/id-keys/grai

GS1 distinguishes returnable assets that may circulate through repeated issue/return cycles and, when needed, can be individually identified.

Reusable structure:

A temporary replacement or loaner can remain the provider's asset while being held by a customer. Custody and ownership must remain separate.

Ouros transformation:

Temporary loaners should reference Shared Equipment or an equivalent authored custody owner rather than silently transferring ownership.

## Design lessons extracted

The following are safe high-level structures for Ouros:

1. Keep the physical item instance separate from its model/type and from any service case.
2. Keep purchase/receipt provenance separate from later remedy eligibility.
3. Record a customer's report as a claim until inspection or exact evidence confirms the condition.
4. Preserve what the provider promised at the time; later policy changes do not rewrite earlier terms.
5. Separate return request, authorization, physical handoff and receipt.
6. Separate observed symptom, diagnosis and cause.
7. Separate remedy eligibility from remedy selection.
8. Separate repair completion from verification/release and final handback.
9. Separate replacement allocation from replacement availability and issue.
10. Separate refund authorization from Finance settlement.
11. Keep recall state separate from an individual after-sale case.
12. Keep insurance claim state separate from warranty/service handling.
13. A missing receipt or incomplete record may produce uncertainty; it does not prove deception.
14. A repeat failure may reopen or create a new episode without deleting the earlier repair history.
15. A temporary loaner remains a separate asset with its own custody history.
16. Never apply product-return semantics to Pokémon or other living actors.

## Candidate boundaries for design

- `PURCHASE_RECORDED != REMEDY_ELIGIBLE`
- `RETURN_REQUESTED != RETURN_AUTHORIZED`
- `RETURN_AUTHORIZED != ITEM_HANDED_OVER`
- `ITEM_HANDED_OVER != PROVIDER_RECEIPT_PROCESSED`
- `SYMPTOM_REPORTED != DEFECT_CONFIRMED`
- `DEFECT_CONFIRMED != CAUSE_ESTABLISHED`
- `DEFECT_CONFIRMED != COVERAGE_CONFIRMED`
- `COVERAGE_CONFIRMED != REPAIR_SELECTED`
- `REPAIR_COMPLETED != QUALITY_CHECK_PASSED`
- `QUALITY_CHECK_PASSED != ITEM_RETURNED_TO_HOLDER`
- `REPLACEMENT_APPROVED != REPLACEMENT_AVAILABLE`
- `REPLACEMENT_AVAILABLE != REPLACEMENT_ISSUED`
- `REPLACEMENT_ISSUED != ORIGINAL_RETURNED`
- `REFUND_APPROVED != REFUND_SETTLED`
- `RECALL_ACTIVE != THIS_UNIT_DEFECTIVE`
- `RECALL_CASE != WARRANTY_CASE`
- `SAME_MODEL != SAME_ITEM_INSTANCE`
- `LOANER_ISSUED != OWNERSHIP_TRANSFERRED`
- `CASE_CLOSED != FUTURE_FAILURE_IMPOSSIBLE`

## Narrative opportunity

After-sale state is useful because it turns ordinary objects into persistent world history without requiring combat or a market simulator. A repaired camera can retain a replaced casing. A workshop can remember that the same field instrument returned three times for unrelated faults. A shop can have a policy that changed after a storm. A temporary loaner can become familiar to a neighborhood before returning to its provider.

Disagreements can remain mundane and evidence-based rather than becoming fraud plots by default.

## Exclusions

This pass does not copy protected prose, dialogue, characters or plots.

This pass does not establish:

- consumer law;
- universal warranties;
- legal liability;
- standardized refund policy;
- manufacturer obligations;
- exact prices;
- repair recipes;
- item durability rules;
- destructible-object combat rules;
- Pokémon sale/return/replacement mechanics;
- insurance coverage;
- universal serial-number technology.

## Proposed next step

Create a PROPOSED after-sale continuity extension that acts as an orchestration layer across Storefront, Procurement, Material Culture, Courier, Finance, Shared Equipment, Recall, Agreements and optional Insurance. It should include mechanically rich encounters only through explicit permanent capability contracts, with reduced static variants available now.