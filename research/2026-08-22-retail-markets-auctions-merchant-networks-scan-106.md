# Research Scan — Retail Markets, Auctions & Merchant Networks — Pass 106

Status: external research and provenance only. Nothing in this file is established Ouros canon or a rules source.

Date: 2026-08-22

## Why this pass

The narrative repository already has strong systems for material provenance, workshops, production, finance, supply chains, public space, tourism, postal delivery, transport and illicit diversion. Pass 105 added the upstream logistics authority: what an institution needs, what stock exists, what is reserved, what was shipped, what was received and what was accepted for use.

A different gap remains on the public-facing side of the economy.

Ouros still needs a common contract for questions such as:

- which vendors are actually present at a market today;
- which offers are currently visible to a player;
- whether an offer is fixed, negotiated, exchanged, consigned or auctioned;
- whether the seller has custody, ownership authority or merely possession;
- whether the listed object is the same physical instance later transferred;
- whether a market is permanent, weekly, seasonal, mobile or event-linked;
- whether an auction was announced, opened, cancelled, completed or disputed;
- whether a buyer and seller agreed to a transfer;
- whether payment was authorized versus actually transferred;
- whether the purchased object was delivered or remained in storage;
- whether a secondhand object retained provenance after resale;
- whether an advertised item is still available after supply or staffing changed;
- how a merchant route changes when rail, ferry or road infrastructure changes;
- how routine shopping can compress without making markets feel like static menus.

The existing Material Culture layer already has a coarse `market_state`. Pass 106 does not replace it. It expands the player-facing market institution and transaction lifecycle while leaving item definitions, inventory truth, money truth and transport under their existing authorities.

## Internal repository overlap reviewed

Before external research, the branch inventory, README and relevant systems were inspected.

Key boundaries:

- `design/material-culture-economy-crafting-layer.md` owns item instances, material batches, provenance, workshops, commissions and the coarse idea of a market. It already records `TRADED`, `SOLD` and `GIFTED` provenance events. Pass 106 should orchestrate offers and transactions, not redefine those objects.
- `design/supply-chains-procurement-inventory-layer.md` owns sourcing, stock, reservations, allocations, storage, freight, receiving and availability. A market listing must consume supply truth rather than manufacture stock.
- `design/finance-sponsorship-risk-layer.md` owns authorized money movement, funding, restricted funds and financial claims. A bid or quoted price is not itself proof that money changed hands.
- `design/urban-public-space-street-life-layer.md` owns public-space use, crowd pressure and temporary programming. A market can occupy a square without owning the square.
- `design/festivals-ceremonies-observances-layer.md` owns recurring cultural events. A festival can host vendors, but the market system should own the resulting commercial offers.
- `design/tourism-visitors-destination-pressure-layer.md` owns visitor pressure. Increased visitors can change market demand or vendor attendance without the market layer deciding tourism truth.
- `design/postal-courier-parcel-logistics-layer.md` owns addressed delivery and last-mile parcel movement. A market purchase can hand off to postal delivery without turning the marketplace into the postal authority.
- `design/illicit-networks-smuggling-diversion-layer.md` owns evidence-backed illicit trade and diversion. A cheap, private or undocumented offer is not automatically illicit.
- `design/case-authority-custody-layer.md` owns evidence, allegations and custody disputes. A questioned transaction can generate a case without the market itself determining guilt.
- `design/pokemon-agency-partnership-release-layer.md` owns Pokémon identity, custody, partnership and transfer concerns. Pass 106 must not reduce Pokémon to generic merchandise.

The branch comparison before writing showed `agent/pass-53-evolution-life-stage` 212 commits ahead of `main` and 0 behind.

## Source 1 — Porto Marinada as a visible market institution

Source: Pokémon.com, “Reminisce on Pokémon Scarlet and Pokémon Violet with the Pokémon TCG”, September 22, 2025.

URL: https://www.pokemon.com/us/features/reminisce-on-pokemon-scarlet-and-pokemon-violet-with-the-pokemon-tcg

Related official Pokémon.com camera feature describing Porto Marinada as a marketplace with auctioneers and bidders:

URL: https://www.pokemon.com/uk/news/using-the-camera-app-in-the-hidden-treasure-of-area-zero-part-1-the-teal-mask

Observed structure:

- Porto Marinada is remembered specifically through its bustling market identity;
- the market is a recognizable place within the town rather than an abstract global shop menu;
- auctioneers, bidders, stalls and bargaining are part of the visible social environment;
- the market can be a location used for another objective before a Gym challenge.

Reusable Ouros pattern:

A market can be a persistent civic place with its own routine even when the player is not shopping. It may produce foot traffic, merchant arrivals, public information, tourism, jobs and occasional adventures while still allowing routine purchases to compress.

A market venue should therefore have physical identity and operating state separate from individual offers.

What is not imported:

- Porto Marinada itself;
- Kofu, the Gym Test or its scripted errand;
- Paldea’s economy;
- bargaining emotes;
- prices, currencies or auction formulas.

## Source 2 — Porto Marinada’s ordinary vendors and auction lots are different market modes

Source: Bulbapedia, “Porto Marinada Market”.

URL: https://bulbapedia.bulbagarden.net/wiki/Porto_Marinada_Market

Observed structure:

- ordinary food vendors and auctioneers coexist inside one market;
- auction participation is gated in the game while ordinary vendors remain accessible;
- auctioned offers are presented as lots;
- offers can change from one in-game day to another;
- several bidders can compete for one lot;
- a winning outcome produces a specific transfer rather than granting every participant the item.

Reusable Ouros pattern:

One physical market can host multiple exchange modes simultaneously:

- ordinary fixed offers;
- negotiated offers;
- temporary lots;
- public auctions;
- consignment;
- barter/exchange;
- service commissions.

The `offer_listing` and `auction_lot` should be objects with their own validity windows and provenance references.

The important abstraction is not Paldea’s exact bidding math. It is the state machine:

`ANNOUNCED -> OPEN -> BIDDING -> WON/NO_SALE/CANCELLED -> PAYMENT_PENDING -> TRANSFERRED`

What is not imported:

- starting-price formulas;
- NPC budget formulas;
- fixed bid increments;
- probability weights;
- specific item pools;
- Gym-based eligibility as a universal market rule;
- Paldean prices.

These are Scarlet/Violet mechanics, not PTU/Caelo rules.

## Source 3 — Pokémon Mystery Dungeon: shops inside a service hub

Source: Nintendo official manual, Pokémon Mystery Dungeon: Explorers of Sky.

URL: https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_ds_21/Manual_NintendoDS_PokemonMysteryDungeonExplorersOfSky_EN.pdf

Related Nintendo official Blue Rescue Team manual:

URL: https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_ds_21/Manual_NintendoDS_PokemonMysteryDungeonBlueRescueTeam_EN.pdf

Observed structure:

- Treasure Town/Pokémon Square places shops alongside storage, banking, appraisal, training and other services;
- Kecleon Shop and Kecleon Wares specialize in different goods;
- buying, selling and storage remain distinct operations;
- the settlement hub remains socially useful even when the player does not need every service on every visit.

Reusable Ouros pattern:

Commerce should sit inside an institutional/service ecology rather than become the entire settlement.

A market district can contain:

- general merchants;
- specialist vendors;
- repair or appraisal services;
- storage handoffs;
- food stalls;
- postal collection;
- transport links;
- noticeboards;
- temporary traders.

The actual stock and mechanical item definitions remain external authorities.

What is not imported:

- Mystery Dungeon currencies;
- shop inventories;
- dungeon-loss mechanics;
- Move-linking services;
- Friend Area systems;
- Mystery Dungeon item prices or effects.

## Source 4 — PTU Game of Throhs: a recurring harbor trader market

Sources:

- Publicly accessible copy of Pokémon Tabletop United: Game of Throhs, campaign-setting section.
  https://anyflip.com/tcye/kdwk/basic/101-121
- PTU public mirror/searchable copy:
  https://www.scribd.com/document/785005535/Pokemon-Tabletop-United-Game-of-Throhs

Observed structure:

The Visiwa setting includes a Trader’s Market held every Saturday. Ships and local groups arrive in port and exchange outside goods, and trade is linked to the economic identity of the settlement.

Reusable Ouros pattern:

A market does not need to be permanently open to be persistent.

A weekly or seasonal market can have:

- a stable venue identity;
- recurring calendar windows;
- a changing merchant roster;
- transport dependencies;
- goods that reflect which routes arrived;
- local sellers whose participation varies;
- a historical record of editions/sessions;
- knock-on effects on lodging, public space, staffing and tourism.

This is useful for Minecraft because the server can project a denser market only during the active session instead of keeping every trader loaded all week.

What is not imported:

- Visiwa;
- named factions, settlements or NPCs;
- fantasy classes;
- supernatural economics;
- any prices or trade rules from Game of Throhs.

The source is used as campaign-setting inspiration, not as the project’s governing PTU/Caelo rules authority.

## Source 5 — Eevee Expo Free Market: listings as explicit data objects

Source: Eevee Expo, Pokémon Essentials resource “Free Market 2.0.3”.

URL: https://eeveeexpo.com/resources/1692/

Observed structure:

- sellers can expose discrete lots rather than one universal shop inventory;
- lots can be defined with seller-specific context;
- the resource supports item listings and also player-facing marketplace-style interfaces;
- later versions track personal lots and buyer validity.

Reusable Ouros pattern:

A marketplace benefits from treating an offer as an object:

`who is offering -> what exact object/batch -> under which terms -> during which window -> to whom -> current state`

This makes it possible to preserve secondhand provenance, cancel stale listings and display different offers to players who have different access permissions without duplicating the underlying item.

Strong non-import rule:

The plugin also supports Pokémon sale/trade lots. Ouros must not copy this as a generic Pokémon marketplace. Pokémon transfer requires the project’s Pokémon-agency, custody, ownership/registration and multiplayer-consent rules. No species-based or stat-based monetary valuation is introduced here.

What is not imported:

- plugin code;
- UI;
- prices;
- Pokémon sale mechanics;
- trade formulas;
- restock logic;
- seller classes.

## Source 6 — Auction-house research: temporal markets create distinct participation patterns

Source: Anders Drachen, Joseph Riley, Shawna Baskin and Diego Klabjan, “Going Out of Business: Auction House Behavior in the Massively Multi-Player Online Game Glitch”, 2016.

Public paper:

https://arxiv.org/abs/1603.07610

Observed high-level lesson:

The study analyzes millions of auction-house records across the lifetime of a multiplayer game and finds that participation changes over time. The auction house is not simply a static catalog; players move between behavioral patterns and market participation changes as the world changes.

Reusable Ouros pattern:

Ouros does not need a full MMO economy, but market sessions should have history.

A market can remember:

- participation bands;
- vendor turnover;
- recurring buyers without inferring private motives;
- categories becoming more or less common;
- periods of unusual activity;
- the appearance/disappearance of specialist merchants;
- effects of transport openings, festivals or crises.

This should remain coarse narrative state unless an authored economy requires more detail.

What is not imported:

- Glitch’s economy;
- clustering algorithms;
- price optimization;
- player-value scoring;
- auction analytics as a gameplay requirement.

## Source 7 — PTU adventure structure: routine resources should support decisions, not become grind

Source: Pokémon Tabletop Wiki, “A Song of Ice and Ire”.

URL: https://pokemontabletop.com/wiki/index.php/Quest%3AA_Song_of_Ice_and_Ire

Observed structure:

The adventure uses bounded resource pressure and priority tradeoffs to make supplies matter during an unusual crisis. The point is not permanent shopping simulation. Resources matter because the environment and time pressure make specific decisions consequential.

Reusable Ouros pattern:

Routine commerce should normally compress.

A shopping scene deserves expansion when at least one of these applies:

- the exact object has story provenance;
- the vendor relationship matters;
- the offer is temporary or contested;
- several legitimate buyers compete;
- a shortage has a causal source;
- a purchase affects institutional capacity;
- a secondhand object raises custody/provenance questions;
- the player deliberately wants merchant/professional gameplay;
- the market session itself is a social/cultural event;
- the transaction changes a route, project, collection or public record.

A normal Potion purchase should not become a quest.

## Source 8 — Markets as a design choice between convenience and social interaction

Source: public game-market research and design literature, including the Glitch auction-house study above and public GDC material discussing different market structures.

Reusable Ouros lesson:

Different exchange structures serve different goals.

A fixed shop is good for routine availability.

A specialist merchant is good for identity and knowledge.

A weekly market is good for recurring social rhythms.

An auction is good for scarce, unique or provenance-rich objects when competition itself is meaningful.

A player-to-player exchange is good for negotiated ownership when both sides consent.

A commission is good when creation and relationships matter more than browsing stock.

Ouros should choose the structure based on the world state and narrative purpose rather than force everything through one universal marketplace UI.

## Design synthesis for Ouros

The core market pipeline should be:

`SUPPLY/OWNERSHIP STATE -> VENDOR PRESENCE -> OFFER LISTING -> NEGOTIATION/AUCTION/ACCEPTANCE -> PAYMENT AUTHORIZATION -> TRANSFER AUTHORIZATION -> PHYSICAL HANDOFF -> PROVENANCE UPDATE`

Each arrow can fail independently.

Examples:

- stock exists but is reserved, so no offer appears;
- a vendor is scheduled but cannot reach the market because the ferry is suspended;
- an offer remains visible after the item was put on quality hold;
- an auction opens but provenance is questioned before transfer;
- a buyer wins but payment remains pending;
- payment succeeds but the object remains with a museum until a handoff is scheduled;
- an item is resold and keeps the same persistent instance ID;
- a market session is cancelled but the merchants remain in town and trade privately where allowed;
- a listing is public while its seller identity is intentionally limited by an institution without becoming automatically illicit.

## Important anti-inference rules

Pass 106 should preserve these distinctions:

- listed does not mean available forever;
- displayed does not mean owned by the vendor;
- possession does not prove legal authority to sell;
- low price does not prove stolen goods;
- high price does not prove rarity or quality;
- no sale does not prove lack of demand;
- auction loss does not create rivalry;
- repeated buyer does not prove friendship or obsession;
- market fame does not create a mechanical reputation bonus;
- vendor uniform does not prove institution membership;
- seller absence does not prove closure of the market;
- crowding does not create PTU penalties;
- stall layout does not create tactical cover automatically;
- a visible item does not enter battle inventory;
- a Pokémon helping at a stall is not merchandise;
- a Pokémon appearing in a trade conversation cannot be transferred without authoritative ownership/custody/consent rules;
- a secondhand mechanical Item keeps its mechanical definition; narrative provenance cannot add stats;
- an auctioneer cannot create an item that Supply Chain/Material Culture does not say exists.

## Copyright and originality boundary

External Pokémon, PTU and fan-game material is used only for abstract structures and design lessons.

Do not copy:

- dialogue;
- named NPCs into Ouros;
- locations wholesale;
- scripted auction scenarios;
- distinctive plots;
- item lists;
- proprietary art/UI;
- pricing formulas;
- trade algorithms.

Ouros proposals must use original places, institutions, merchants, conflicts and histories.

## PTU/Caelo mechanics boundary

No new PTU rule is asserted by this research pass.

Questions requiring project-source validation include:

- exact money rules;
- selling/buying prices;
- item availability;
- Haggling/Charm/Guile interactions, if any;
- Merchant-style Trainer Features, if any;
- appraisal/identification rules;
- carrying/encumbrance;
- item transfer timing in battle;
- Pokémon ownership/registration/transfer;
- capture versus sale/trade rights;
- services that can legally alter mechanical Items;
- any Caelo-specific economy or access rules.

The full primary Caelo corpus was not reliably retrievable during this runtime. No Caelo-specific economy rule is invented here.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No result is attributed to it.

## Canon questions opened by this pass

- Which settlements have permanent markets versus weekly/seasonal ones?
- Does Ouros use one regional currency, several currencies, barter, or a simpler authored economy?
- Are exact prices universal or institution/vendor specific?
- Which categories of goods are normally resellable?
- Can institutions run public auctions?
- Who can consign an object for sale?
- What proof of custody/ownership is required for provenance-rich objects?
- Are player-owned shops or stalls possible?
- Can clubs operate shared vendor tables?
- How are player-to-player item trades confirmed in multiplayer?
- How are irreversible Pokémon transfers handled and consented to?
- How does a market advertise stale/changed offers without becoming omniscient?
- How much market state advances while chunks are unloaded?
- Which merchant routes exist before the players arrive?
- What market records are public and which are private?