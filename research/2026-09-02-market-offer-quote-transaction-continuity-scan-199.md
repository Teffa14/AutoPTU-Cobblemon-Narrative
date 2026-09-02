# Ouros Narrative Research — Market Offer, Quote & Transaction Continuity — Pass 199

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is automatically Ouros canon.
Date: 2026-09-02

## Scope

This pass examines a narrow continuity gap left after the broader material-culture/economy work in pass 07 and the service-request/capacity work in pass 198.

Pass 07 already established workshops, market state, supply routes, item provenance, commissions and causal scarcity. Pass 198 established request, routing, capacity, appointment and work-order continuity. Neither layer fully records the transactional path between a concrete offer and a completed exchange.

The seam for this pass is therefore:

`available or claimed stock -> offer/quote -> revision or expiry -> reservation -> agreement -> governed payment/consideration -> custody/ownership claim transfer -> pickup/delivery -> later provenance`

This pass does not create a regional macroeconomy, dynamic inflation model, universal haggling system, tax code, currency standard, ownership law or new PTU prices.

## Existing Ouros constraints checked before research

### Canon-approved Marea facts

The current playable foundation establishes Puerto Bruma as a service hub with Bruma Market Hall, kitchens and repair stalls. Loma Clara producers supply food and specialist ingredients to Puerto Bruma. The Producers Cooperative coordinates storage, shared deliveries and market representation while individual producers retain their holdings and decisions.

The same canon establishes Thin Delivery Season. Several deliveries are smaller and less predictable than the previous local season, while vendors disagree over production, route reliability, purchasing behavior or coincidence. No canonical cause exists yet.

Ivo Serrat is canonically the purchasing lead at Bruma Market Hall communal kitchen. His role makes him a legitimate anchor for purchase records, substitutions and supplier observations. His observations do not grant him omniscient knowledge of regional supply.

### Existing non-canon design overlap

Pass 07 already contains:
- physical item instances and material batches;
- owner/custodian fields;
- provenance events including TRADED, SOLD and GIFTED;
- workshops and service offers;
- commissions;
- supply routes;
- ordinal market state;
- scarcity events;
- a hard rule against invented prices.

Pass 198 already contains service requests, queue/capacity state and work-order completion.

Pass 199 extends these systems. It should not replace them.

## Public-source research

### 1. Porto Marinada Market — an offer can be a time-bounded lot, not a permanent shelf entry

Source:
https://bulbapedia.bulbagarden.net/wiki/Porto_Marinada_Market

Observed structure:
- the market combines ordinary vendors with auctions;
- auction offerings are lots rather than single permanent catalog entries;
- offered lots change with the in-game day;
- several buyers can compete for one lot;
- participation, bidding, winning, payment and receiving the lot are separate steps.

Reusable structure for Ouros:
A market record can have a finite validity window and a specific quantity. Seeing an offer should not reserve it. Entering negotiation should not guarantee acquisition. A completed agreement should point to the exact lot or stock record that was actually transferred.

Transformation rule:
Ouros does not import Porto Marinada vendors, auction formulas, bid increments, access requirements or item lists. The useful abstraction is only the lifecycle of a temporary offer.

### 2. Ginkgo Guild — merchant identity can travel while stock comes from changing provenance

Official source:
https://legends.arceus.pokemon.com/en-us/story/
Equivalent official localized pages also describe the Ginkgo Guild merchants traveling Hisui and selling rare or special findings acquired in different places.

Observed structure:
- a merchant organization has a persistent identity;
- individual merchants travel;
- wares can reflect what has been obtained elsewhere;
- meeting the same merchant again does not imply identical stock.

Reusable structure for Ouros:
Vendor identity, location, stock provenance and current offer should be separate records. A repeat visitor can bring different goods on a later visit while remaining the same social actor.

Transformation rule:
No Ginkgo characters, stock tables or Hisui trade routes are imported.

### 3. Join Avenue — shop capability can change through the actor operating it

Source:
https://bulbapedia.bulbagarden.net/wiki/Join_Avenue

Observed structure:
- different shop operators create different service/product selections;
- the avenue can gain businesses through visitors;
- shop development changes what becomes available;
- market-type facilities can sell batches rather than only single items.

Reusable structure for Ouros:
A shop should not be represented only as a global item menu. Current operator, current inventory source and current world state can all matter to what is offered.

Transformation rule:
Ouros does not import Join Avenue ranks, popularity points, shop types, unlock tables or discounts.

### 4. Poké Marts — stock availability can be contextual instead of universal

Source:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Mart

Observed structure:
Across the series, shops can share common stock while also having location-specific stock or stock gated by progression state.

Reusable structure for Ouros:
The existence of an item definition does not prove that every vendor has the item. Availability needs an actual market/shop record.

Transformation rule:
Badge gates and main-series prices are not adopted into Ouros.

### 5. Mystery Dungeon Rescue Team DX — purchase, carried cash and storage are different states

Official source:
https://mysterydungeon.pokemon.com/en-us/world/

Observed structure:
- Kecleon shops sell defined categories of goods;
- money held by the party is distinct from money placed in a bank;
- items carried by the party are distinct from items stored elsewhere;
- shops can also appear inside dungeons.

Reusable structure for Ouros:
Transaction completion should not flatten physical location, custody and accessible inventory into one flag. An item can be owned, stored, reserved, in transit or physically carried by different actors.

Transformation rule:
Ouros does not import Mystery Dungeon loss-on-defeat, banking rules, dungeon shop behavior or currency values.

### 6. PTU 1.05 — availability and campaign economy remain GM/setting decisions

Public reference:
https://pturpg.wikidot.com/character-creation

The character-creation reference states that the GM determines how much starting money Trainers receive and what items are available for purchase, while giving a recommended starting amount and example purchases.

Public mirror for NPC services:
https://anyflip.com/gqibw/ifqm/basic/451-500

The PTU Core material also gives example service availability and price guidance for tutors, chefs and other providers, with frequency depending on place/provider.

Reusable structure for Ouros:
Narrative can represent a vendor or service provider as world state, but it must not infer universal availability or invent executable price/effect rules. Exact mechanical purchases should use the governing PTU/Caelo/AutoPTU data chosen for the project.

### 7. PTU community experience — campaign reward economies vary substantially

Community discussion:
https://www.reddit.com/r/PokemonTabletop/comments/11zxota/

Observed signal:
GMs describe materially different approaches to money and rewards depending on campaign structure: sponsorships, quest rewards, crafting materials, cash awards and direct item access all appear. Contributors explicitly adjust money around what items players need access to and what their campaign already provides.

Reusable lesson:
A single economy model should not be inferred from PTU community practice. Ouros should preserve concrete transactions and authored access rules while keeping macroeconomic assumptions configurable.

This Reddit source is community practice, not rules authority.

## AutoPTU live cross-check

Read-only repository checked at:
`Teffa14/AutoPTU @ 729bae2d424963ff9bb3f4159c9a7ac9152128a7`

`auto_ptu/rules/campaign_commands.py` already contains deterministic campaign commands for:
- `shop.create`;
- `shop.buy`;
- `shop.sell`.

The current Python implementation stores a shop id, location and stock entries with price and quantity. `shop.buy` checks shop location, stock quantity and Trainer currency, then subtracts currency, adds inventory and reduces stock. `shop.sell` checks Trainer inventory, calculates a value from shop price, removes inventory, adds currency and increases shop stock.

Important limitation:
This is evidence for a concrete campaign-shop command path in AutoPTU Python. It does not prove a complete economic simulation, unique physical-item provenance, reservations, quote expiry, negotiated terms, delivery, taxes, credit, auctions, legal ownership or Java parity.

Search of AutoPTU-Java for shop/buy/sell/currency/inventory/price did not return indexed implementation evidence in this run. Therefore no Java transaction capability is declared.

## PTU/Caelo cross-check status

### PTU

Verified from public PTU references:
- money and purchasable items exist;
- the GM controls starting money and availability;
- PTU publishes item/service price guidance in its own rules corpus.

Pass 199 therefore must not create alternate mechanical prices for PTU items by narrative inference.

### Caelo

The Narrative README identifies the Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as authoritative project sources. Pass 07 also recorded that supplied Caelo material included shop/market/buy/recipe/crafting surfaces.

However, a fresh literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed source files in this run. Pass 199 therefore treats Caelo-specific currency, shop commands, prices, resale rules, bargaining, taxes and ownership doctrine as UNVERIFIED in live evidence.

No Caelo-specific transaction rule is promoted from the older research note alone.

## Reusable design conclusions

1. Preserve an offer as a dated/versioned claim made by a specific seller or institution.
2. Preserve the stock or lot referenced by that offer separately from the advertisement itself.
3. A displayed price is local evidence with a time/provider/scope, not a regional economic truth.
4. Reservation and completed purchase need distinct states.
5. Payment/consideration and physical handoff can occur at different times.
6. Custody transfer and ownership claim transfer should be separately auditable until Ouros ownership doctrine is canonical.
7. Delivery/pickup should connect to existing correspondence, transport and custody layers rather than being hidden inside a shop UI.
8. A substitution needs explicit agreement or governing institutional procedure; it should not silently rewrite the original order.
9. A changed quote should supersede the old quote without erasing it.
10. Market observations can become evidence for Thin Delivery Season but cannot prove its cause by themselves.
11. Ordinary off-screen transactions may proceed when actual actors, stock and world rules support them; player absence should not freeze the market.
12. Minecraft display entities, containers and shop screens are projections of authoritative transaction/world state, not the authority themselves.

## Proposed vocabulary boundary

These labels are implementation-facing proposals, not Caelo legal terminology:
- MARKET_OFFER
- PRICE_QUOTE
- STOCK_CLAIM
- LOT
- RESERVATION
- AGREEMENT
- CONSIDERATION_RECORD
- TRANSFER_EVENT
- PICKUP
- DELIVERY
- SUBSTITUTION
- REFUND_OR_REVERSAL_CANDIDATE
- PRICE_OBSERVATION

The project should rename them if Caelo source material establishes authoritative terminology.

## Explicit exclusions

Pass 199 does not establish:
- the name or denomination of Ouros currency;
- exchange rates;
- taxes;
- credit or interest;
- debt enforcement;
- auction law;
- consumer-protection law;
- regional resale percentages;
- universal haggling;
- dynamic inflation;
- wage scales;
- ownership law;
- stolen-property doctrine;
- scarcity-to-price formulas;
- PTU item prices different from authoritative rules;
- automated market-making;
- a canonical cause for Thin Delivery Season.

## Recommended first implementation slice

`Ivo's Quote, Tomorrow's Delivery`

Ivo records a supplier quote for a defined ingredient lot that is expected on a later delivery. Before arrival, a revised message changes either quantity or available substitute. The player can see both versions, ask Ivo what he currently plans to buy and later observe which lot actually arrives.

Required continuity:
- original quote;
- revision;
- supplier identity or institutional source;
- validity/expected-delivery context;
- requested quantity;
- substitution status;
- actual received lot;
- Ivo's purchasing decision;
- provenance link into kitchen stock.

No battle is required. No price formula is invented. The slice strengthens Thin Delivery Season evidence without deciding its cause.

## Source provenance summary

Primary/official Pokémon sources are preferred where they contain the needed structure. Bulbapedia is used for system details that official marketing pages do not document. PTU public references are mechanics discovery/cross-check sources. Reddit is explicitly community practice only.

No protected prose, dialogue, characters, plots, bespoke item tables or distinctive quest sequences are imported. Only high-level transactional structures are transformed into original Ouros design.