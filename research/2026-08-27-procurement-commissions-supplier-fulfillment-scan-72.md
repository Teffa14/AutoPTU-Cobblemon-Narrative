# Procurement, commissions & supplier fulfillment research — Pass 72

Status: research/provenance only. Nothing in this file is canon.

## Research question

Ouros already has material provenance, workshops and commissions, market/storefront state, finance/sponsorship, agreements/mediation, staffing, courier logistics, maintenance, public works and service access. The missing operational question is narrower:

How does a persistent world represent a need for goods or work moving through request, sourcing, comparison, selection, order, fulfillment, receipt, verification and closeout without inventing a universal legal/procurement regime or duplicating the systems that own money, production, delivery and ownership?

## Repository gap confirmed before external research

The full repository tree was inspected before this pass. Relevant existing layers include:

- `material-culture-economy-crafting-layer.md`: physical item instances, material batches, workshops, commissions, market state and supply routes;
- `finance-sponsorship-risk-layer.md`: funding agreements, commitments, payment events, budget envelopes and a procurement linkage, but not physical acquisition workflow;
- `commercial-services-storefront-continuity-extension.md`: storefront availability and service continuity;
- `courier-parcel-last-mile-logistics-extension.md`: shipment/custody/delivery after a shipment exists;
- `facility-maintenance-repair-inspection-extension.md`: work orders and repair verification;
- `civic-governance-public-works-layer.md`: collective decisions and projects;
- `agreements-mediation-repair-layer.md`: explicit commitments, amendment, compliance events and dispute repair;
- `workplaces-professions-staffing-layer.md`: roles, shifts and professional continuity;
- `credentials-authorizations-recognition-extension.md`: qualification/authorization evidence.

No existing file owns a general requisition → sourcing → supplier response → selection → order → receipt/acceptance lifecycle.

## Source 1 — Pokémon Legends: Arceus, recurring General Store / Supply Corps relationship

Sources:

- Serebii, “Getting Ahold of New Wares”: https://www.serebii.net/legendsarceus/requests/gettingaholdofnewwares.shtml
- Serebii, “Even More New Wares”: https://www.serebii.net/legendsarceus/requests/evenmorenewwares.shtml
- Bulbapedia walkthrough, Requests 1–30: https://bulbapedia.bulbagarden.net/wiki/Appendix%3ALegends%3A_Arceus_walkthrough/Requests_1-30

Observed structure:

- the General Store has a concrete supply problem rather than an abstract “shop level”;
- the store operator and Supply Corps are distinct actors with a persistent relationship;
- the player intervenes between those actors;
- several later requests revisit the same dependency instead of replacing it with an unrelated fetch quest;
- successful resolution changes the store’s future visible offering.

Reusable Ouros lesson:

A procurement problem should preserve the actors and dependency that caused it. Repeated sourcing episodes can deepen the same supplier relationship, reveal new blockers, or change what a service can offer. The permanent output should be changed world/service state, not merely currency or XP.

Transformation rule:

Do not copy Choy, Tao Hua, Galaxy Team, Supply Corps, gifts, requested materials, exact inventory unlocks or dialogue. Ouros should use original institutions and relationships. The reusable structure is recurring supplier dependency + intervention + persistent service consequence.

## Source 2 — Legends: Arceus quest-chain escalation

Source:

- Game8, General Store Wares quest line: https://game8.co/games/Pokemon-Legends-Arceus/archives/355493

Observed structure:

The same commercial relationship is revisited through four requests, each gated by previous progress and broader world progression. The later requests do not erase prior history.

Reusable Ouros lesson:

An acquisition relationship can have a history. A supplier who fulfilled one order may later have different capacity, constraints or willingness. A recurring buyer may become predictable. Procurement therefore benefits from stable `buyer_id`, `supplier_id`, request history and fulfillment history rather than one-shot quest flags.

## Source 3 — Pokémon Reborn restoration projects

Sources:

- Grand Hall donation/restoration overview: https://pokemon-reborn.fandom.com/wiki/Grand_Hall
- Railnet Reconstruction Project: https://pokemon-reborn.fandom.com/wiki/Railnet_Reconstruction_Project

Observed structure:

- restoration projects are discrete, named commitments;
- resources can be committed to one project before others;
- completion changes physical access and later content;
- infrastructure state persists after the decision.

Reusable Ouros lesson:

Large acquisitions or contracted work should terminate in world-state verification, not at “money spent.” A funded/ordered project may still require supplier, delivery, compatibility, installation, inspection and reopening before downstream systems change.

Transformation rule:

Do not import Reborn’s costs, badge gates, city projects, locations or rewards. Reuse only the high-level pattern of finite project selection producing durable world-state change.

## Source 4 — PTU item availability boundary

Source:

- PTU character-creation reference, money and items: https://pturpg.wikidot.com/character-creation

Observed rule-facing lesson:

The reference explicitly leaves starting money and what items are available for purchase to the GM, while PTU provides item/mechanical definitions.

Ouros implication:

The narrative layer cannot infer that every mechanical item is purchasable everywhere, manufacture a price, or treat a supplier response as mechanically valid inventory. Procurement may request a `mechanical_item_ref`, but availability, price, crafting legality and mechanical item behavior remain governed by PTU/Caelo plus approved implementation/world data.

## Source 5 — PTU/PTR automation context

Sources:

- Pokémon Tabletop official blog/about: https://pokemontabletop.com/about/
- Pokémon Tabletop Reunited Foundry system: https://github.com/pokemon-tabletop-reunited/ptr1e

These sources are not used to define Ouros rules. They reinforce two implementation lessons already central to this project:

1. PTU is mechanically dense enough that narrative systems should avoid shadow implementations of rules.
2. Workflow/state around battles can be modeled independently while combat legality remains in the authoritative engine.

## High-level structures extracted

### Need before vendor

A world actor first has a need, specification or service gap. The generator should not pick a vendor and reverse-engineer a reason to use them.

### Sourcing as information gathering

Possible suppliers can differ by availability, timing, route, technical compatibility, proven track record, material provenance or authored terms. The system can present meaningful choice without inventing hidden “best vendor” scores.

### Offer is not order

A quote, proposal, estimate, sample or promise is information. Selection and authorization remain separate events.

### Order is not fulfillment

An accepted order can be waiting for materials, production, staff, route access or another dependency.

### Delivery is not acceptance

A shipment can arrive while still needing count, condition, compatibility, provenance or work-quality verification.

### Payment is not teleportation

This follows the existing Finance layer directly. A paid invoice cannot instantiate a physical object or mark a facility complete.

### Failure should preserve causality

Late fulfillment does not imply fraud. Possible causes include weather, route closure, supplier capacity, missing input, damaged equipment, staffing, revised specification, inspection failure or buyer-side delay.

### Closeout can produce future memory

A supplier relationship can remember:

- reliable delivery under difficult conditions;
- a corrected mistake;
- a substitution that worked;
- a dispute that was resolved;
- recurring demand;
- a specification that repeatedly causes problems.

This memory is narrative/provenance state and must not become an unsupported commerce bonus.

## Patterns deliberately rejected

Do not add by default:

- universal competitive bidding;
- government tender law;
- procurement thresholds;
- taxes;
- licenses required to sell;
- warranties with assumed legal force;
- penalties/liquidated damages;
- automatic lowest-price selection;
- credit scores;
- supplier reputation math;
- corruption probability;
- exclusivity rules;
- standardized invoices;
- arbitrary item prices;
- hidden supply/demand equations.

Any of these may exist later only through reviewed Ouros canon and/or mechanics.

## Encounter-design implications

Procurement itself normally needs no AutoPTU battle mechanics. Rich encounters appear when acquisition intersects physical retrieval, protected delivery, active work sites or supplier facilities.

Example full-version dependency risks:

- moving cargo or escort targets → complete movement/interception/forced movement;
- unstable warehouse/worksite → terrain/hazards/zones/reactions;
- defend/withdraw/clear-route goals → AI tactical policy;
- battle result changing physical shipment/work status in Minecraft → adapter/playback;
- item-specific tactical effect → items + full relevant hooks, not merely one held-item representative effect.

Reduced versions should keep goods, workers, transfer/acceptance state and dynamic site controls outside the tactical grid, then use a conventional static battle only for the threat that genuinely requires battle resolution.

## Canon status

All Ouros-specific institutions, procurement practices, supplier categories, documents, selection methods, payment customs and dispute procedures remain UNDECIDED unless already established elsewhere.

This pass proposes a system vocabulary and original story candidates only. It does not promote any external story element to canon.
