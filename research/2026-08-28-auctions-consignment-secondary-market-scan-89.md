# Research Scan — Auctions, Consignment & Secondary Markets — Pass 89

Status: research/provenance only. Nothing in this file establishes Ouros canon.
Date: 2026-08-28

## Purpose

This pass investigates a narrow gap after reviewing the current Narrative repository: persistent secondary exchange of already-existing objects through consignments, public auctions, listings and collector markets.

Ouros already has:
- physical item identity and provenance;
- workshops and production;
- finance and payment records;
- recurring storefront/service continuity;
- procurement and supplier selection;
- courier handoffs;
- found-property restitution;
- batch traceability/recall;
- archives and collections;
- temporary public events.

The missing connective tissue is the lifecycle where an existing object or lot is deliberately offered to others, held by an intermediary, described publicly, viewed, bid on or offered for, withdrawn or sold, and then transferred through the existing ownership/custody/finance systems.

This pass does not create universal property law, appraisal math, stock-market behavior, hidden market prices or automatic ownership transfer.

## Internal duplication check

Files reviewed before authoring included:
- `design/material-culture-economy-crafting-layer.md`;
- `design/finance-sponsorship-risk-layer.md`;
- `design/commercial-services-storefront-continuity-extension.md`;
- `design/found-property-custody-restitution-extension.md`;
- the full current `design/` inventory;
- `design/engine-readiness-snapshot-pass-88.md`;
- `design/cobblemon-runtime-authority-boundary.md`.

The current design inventory already covers local shops, finance, procurement, credentials, public events, libraries, collections, restitution and provenance. No dedicated auction/consignment/secondary-market lifecycle was present.

## Source 1 — Porto Marinada Market, Pokémon Scarlet/Violet

Source:
https://bulbapedia.bulbagarden.net/wiki/Porto_Marinada_Market

Useful observations:
- several auctioneers operate in one recurring public market;
- auction access is gated by an in-world prerequisite;
- goods are grouped into lots;
- several bidders compete for the same lot;
- only the winner receives the lot;
- available offerings change over time;
- some offerings depend on other player state.

Reusable high-level structures:
- auction venue as a recurring location rather than a one-use menu;
- lot identity separate from the underlying item identities;
- bidder registration/access separate from winning;
- public competition over a finite offering;
- changing inventory that gives a location revisit value;
- adjudication as a discrete event after a sequence of offers.

Not imported:
- exact prices;
- random weight tables;
- item pools;
- Gym progression gates;
- NPC bidding algorithms;
- Pokémon-specific unlock conditions;
- Paldea geography or characters.

Ouros transformation:
A secondary market can expose authored objects/lots whose provenance already exists. The auction layer records who offered, who had custody, what public description was shown, what offers were made, who was selected and what transfer still remains to complete. Finance and Material Culture remain authoritative for money and object ownership.

## Source 2 — Cascarrafa Gym Test / Kofu auction sequence

Sources:
https://bulbapedia.bulbagarden.net/wiki/Cascarrafa_Gym
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Scarlet_and_Violet/Part_12

Useful pattern:
A character can be authorized to bid using another actor's funds for one exact purpose, with unused funds remaining distinguishable from the purchased object.

Reusable structure:
- principal actor;
- temporary purchasing mandate;
- authorized amount/reference;
- specific intended lot;
- bidding actor;
- final acquisition;
- reconciliation of unused funds.

Ouros transformation:
If a character acts as purchasing agent for an institution or another person, that role must be explicit. Winning a lot does not imply the bidder personally owns it when the authoritative agreement says they acted for someone else.

Not imported:
- exact amount;
- seaweed item;
- Gym Test framing;
- named characters.

## Source 3 — PTU 1.05 character creation purchasing boundary

Source:
https://pturpg.wikidot.com/character-creation

Relevant rule boundary:
PTU leaves starting money and which items are available for purchase to the GM/campaign setup.

Reusable lesson for Ouros:
The Narrative layer cannot declare that every PTU item is available at auction, cannot derive a universal fair price and cannot create mechanical item legality through market presence.

Hard transformation rule:
A lot may reference a mechanically governed item only when the governing PTU/Caelo/AutoPTU data says that item can exist in the campaign. Narrative market state controls availability of an already-approved thing; it never defines the thing's mechanical effect.

## Source 4 — Pokémon World Online persistent auction/trading feature

Source:
https://pokemon-world-online.com/

Classification:
Fan-made persistent Pokémon game. Inspiration only.

Useful high-level structure:
Auction/trading can operate as a persistent service inside a long-lived shared world alongside exploration, PvP, events and quests. The market therefore does not need to be a separate economy game; it can function as one persistent social/institutional surface among many.

Ouros transformation:
A market may develop recurring sellers, buyers, specialists, viewing habits, event days and public memory without requiring continuous simulation of every transaction.

Not imported:
- Pokémon trading rules;
- prices;
- player economy balance;
- MMO progression;
- any technical implementation.

## Source 5 — PokeOne Unofficial Marketplace

Source:
https://pokeonemarketplace.com/

Classification:
Community marketplace interface. Inspiration only.

Useful structures:
- listings carry searchable descriptors;
- identity/verification of the seller can be distinguished from claims about the listed asset;
- reference-price information is separate from the final negotiated transaction;
- listings may expire or become stale while remaining historically useful.

Ouros transformation:
A public listing is a claim packet, not truth. The seller's description may be correct, mistaken, incomplete or outdated. Provenance, inspection and authoritative item identity remain separate.

## Source 6 — PokeMMO.Trade marketplace structure

Source:
https://www.pokemmo.trade/

Classification:
Unofficial player marketplace. Inspiration only.

Useful structures:
- buy and sell requests can coexist;
- items can be grouped into lots;
- services and physical objects require different fulfillment paths;
- listings help actors find counterparties but the actual transfer occurs elsewhere.

Ouros transformation:
A notice/listing surface can create a candidate transaction without completing payment, custody or ownership transfer. This integrates naturally with Public Notices, Finance, Courier and Material Culture.

## Source 7 — Auction House Cobb / current Cobblemon ecosystem

Source:
https://www.curseforge.com/minecraft/mc-mods/auction-house-cobb

Classification:
Third-party Cobblemon addon. Technical/ecosystem reference only; not Ouros architecture authority.

Useful observations:
- persistent auction listings can survive server restarts;
- auction UIs can coexist with Cobblemon assets;
- player-to-player trade flows can reuse existing Cobblemon presentation components;
- server-authoritative listing data is possible without using Cobblemon battle logic.

Ouros transformation:
This is evidence that an adapter can reuse Cobblemon/Minecraft presentation and entity/item surfaces while Ouros keeps its own market semantics. No dependency on Cobblemon `BattleState`, participant selection or battle controllers is acceptable.

Important restriction:
Pass 89 does not adopt this addon, its currency assumptions, its Pokémon-sale model or its implementation. Pokémon are actors under the Pokémon Agency boundary and must never be reduced to generic item lots merely because a third-party addon supports Pokémon sales.

## Source 8 — Pokémon Aura / community-driven auction history

Source:
https://pokemonaura.com/

Classification:
Fan-made persistent Pokémon game. Inspiration only.

Useful structure:
Historical listings/trends can influence player expectations without becoming an authoritative valuation system.

Ouros transformation:
Past sale events may become provenance/public memory and may inform NPC expectations. They do not create a hidden global market value or force future sellers to accept a historical price.

## PTU/Caelo safety conclusions

Pass 89 establishes no new mechanical item rules.

Do not invent:
- universal appraisal Skills or DCs;
- auction-specific Features;
- bidding initiative;
- persuasion bonuses that alter mechanical currency;
- price formulas;
- automatic discounts;
- counterfeit-detection mechanics;
- rarity multipliers;
- Pokémon sale values;
- inheritance/property law;
- tax, commission or auction-house fees;
- escrow law;
- binding contract doctrine.

When an authored scene needs a PTU Skill check, Feature, item interaction or other mechanical resolution, the exact PTU/Caelo source must be reviewed first.

## Narrative design lessons

### Exchange has stages

A useful secondary-market scene can distinguish:
1. object exists;
2. consignor offers it;
3. intermediary accepts custody or representation;
4. lot/listing is described publicly;
5. actors inspect or ask questions;
6. offers/bids occur;
7. winner/buyer is selected;
8. payment may or may not complete;
9. custody changes;
10. ownership changes only when the authoritative transfer says so;
11. later provenance remembers the transaction.

This produces more story hooks than a single `BUY` action.

### Public description is evidence, not truth

A catalogue entry can be incomplete or wrong without the auctioneer being fraudulent. It may repeat prior provenance, seller claims, expert opinion or a translation later revised.

### Market competition does not require villainy

Two characters wanting the same object can produce rivalry, negotiation, cooperation, pooling of resources, withdrawal, later resale or a future relationship without a criminal subplot.

### Withdrawal matters

A consignor may withdraw before sale if the local rules allow it. A bidder may stop. A sale can fail to close. A venue can pause a lot after an authenticity concern. These outcomes create persistent history without forcing acquisition.

### Exact objects matter more than generic stock

This layer is most valuable for commissioned, personal, institutional, historical, evidence-linked or otherwise persistent objects. Routine Poké Ball shopping remains Storefront state and should compress.

### Secondary exchange can reveal history

A familiar object appearing in a new catalogue can expose:
- a prior owner change;
- an institution disposing of duplicates;
- a family archive fragment entering public circulation;
- a recovered expedition object;
- a repaired tool with old marks;
- a contested attribution;
- a former prize being sold;
- a missing item resurfacing legitimately or suspiciously.

The market is therefore also an information surface.

## Original Ouros directions produced by this scan

Promising non-canon directions:
- a recurring auction hall whose catalogue remembers previous lots;
- specialist market days attached to an existing district rather than a new settlement;
- institutional deaccession or duplicate-sale candidates, pending Archives policy;
- consignment of personal objects where seller and owner are not assumed identical;
- proxy bidding with explicit mandate;
- a lot paused because provenance branches conflict;
- a historical object whose public description changes after research;
- a familiar item reappearing years later with a legitimate new custodian;
- unsold lots returning to the consignor with public-interest consequences;
- competing institutions deciding whether acquisition is worth diverting limited resources.

## Canon status

Everything introduced in this scan remains PROPOSED/RESEARCH unless a pre-existing canon reference independently establishes it.

No auction house, market institution, pricing practice, fee, currency rule, property doctrine, collector culture or regional tradition is promoted to Ouros canon by Pass 89.
