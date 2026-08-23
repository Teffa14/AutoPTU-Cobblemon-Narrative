# Research Scan — Currency, Accounts, Payments & Settlement — Pass 120

Status: research/provenance only. Not Ouros canon. Not PTU/Caelo rules authority.

## Why this pass exists

The repository already has strong financial and commercial layers, but they deliberately stop short of defining the operational money system.

Internal review found the following boundaries:

- `design/finance-sponsorship-risk-layer.md` owns funding agreements, payment commitments, restricted funds, budgets and financial exposure, while explicitly avoiding a full banking simulator;
- `design/retail-markets-auctions-merchant-networks-layer.md` owns listings, agreed terms and market transactions, but delegates authoritative money balances/transfers to Finance;
- `design/digital-systems-cyberspace-data-layer.md` owns digital accounts, records, access and logs, but not monetary value;
- `design/insurance-risk-pooling-claims-recovery-layer.md` owns claims and recovery finance rather than payment infrastructure;
- `design/supply-chains-procurement-inventory-layer.md` owns physical stock, not money;
- PTU/Caelo remains the authority for actual mechanical money values and item prices where supplied.

The missing layer is the operational path between an obligation or purchase and a completed transfer of value: currency/point systems, wallet/account state, payment instruments, merchant acceptance, authorization, holds/reservations, transfer instructions, settlement, receipts, reversals and reconciliation.

The design goal is narrative legibility and persistence, not modern-bank simulation.

## Source 1 — Pokémon Mystery Dungeon Rescue Team DX: safekeeping and carried money are separate states

Source: official Pokémon Mystery Dungeon: Rescue Team DX world guide, Felicity Bank.
https://mysterydungeon.pokemon.com/en-us/world/

The official guide distinguishes money carried into a dungeon from Poké deposited at Felicity Bank. Deposited money remains safe even if carried money is lost after defeat.

Reusable Ouros structure:

- physical/on-person money and deposited/account money can be separate balances;
- a deposit event is not merely a UI label: it changes where value is held;
- loss exposure can depend on where value is held without changing the currency itself;
- a financial institution can provide a narrow service such as safekeeping without implying loans, investments or a complete banking sector.

Ouros should therefore avoid one universal `money` integer if narrative consequences depend on custody/location of funds.

## Source 2 — Mystery Dungeon settlements: banking can be one service among many

Sources: Bulbapedia pages for Treasure Town / Explorers of Sky and related Mystery Dungeon settlements.
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Mystery_Dungeon:_Explorers_of_Sky

Treasure Town contains separate institutions for shops, item storage, appraisal and banking. Duskull Bank holds money while Kangaskhan Storage separately holds items.

Reusable Ouros structure:

A settlement may expose financial services without collapsing inventory, item custody, appraisal, payments and money storage into the same institution.

This supports small-region designs such as:

- a market with no local deposit institution;
- a rail station with a payment kiosk but no savings service;
- a village cooperative that holds community funds but does not serve individuals;
- a League venue that accepts a particular payment rail without operating the rail itself.

## Source 3 — League Points: a second medium can coexist with Poké Dollars and have selective acceptance

Source: Bulbapedia, League Point.
https://bulbapedia.bulbagarden.net/wiki/League_Point

Scarlet/Violet uses League Points alongside Pokémon Dollars. Most shops can accept LP in place of Pokémon Dollars, while some contexts such as Porto Marinada auctions do not. One Kitakami shop can change its acceptance behavior after repeated player interaction.

Reusable Ouros structure:

- denomination/value and acceptance are separate;
- a merchant may accept one medium and reject another;
- payment acceptance can be institution- or venue-specific;
- secondary institutional points can coexist with ordinary currency;
- acceptance rules can change historically.

Ouros must not infer that any institutional point system is universally exchangeable or legally equivalent to cash.

## Source 4 — Pokémon HOME Points: conversion can exist between institutional point systems without implying a universal exchange market

Source: official Pokémon HOME page.
https://www.pokemon.com/us/pokemon-video-games/pokemon-home

Pokémon HOME Points can be converted into Battle Points in Sword/Shield or League Points in Scarlet/Violet. The conversion is product/system-specific.

Reusable Ouros structure:

- a conversion rule can be scoped to a service;
- conversion may be directional;
- conversion may depend on account/system eligibility;
- a conversion table does not prove free exchange elsewhere;
- old conversion rules should be versioned if they change.

The Ouros analogue can support League credits, academy credits, transit tokens, festival scrip or club points later if canon establishes them, without inventing a universal floating exchange rate.

## Source 5 — PTU Core: mechanical cash and purchase availability are GM/rules concerns

Source: publicly accessible PTU 1.05 Core Rulebook, Character Creation, Step 9: Money and Items.
https://peda.net/p/josajoki/fista/ohjeet/ptu/pokemon-tabletop-united-1.05-core%3Afile/download/c109e0ecc0ac41065575a4a324183b80189a2c70/Pokemon%20Tabletop%20United%201.05%20Core.pdf

The rulebook states that starting money and what is available to purchase are ultimately campaign/GM decisions and gives a recommended starting amount for level-1 Trainers.

Reusable Ouros boundary:

- the narrative repository should not redefine PTU prices or starting wealth;
- account/payment architecture may reference a mechanical balance but must not silently alter it;
- whether an item is available remains distinct from whether a player can pay for it;
- worldbuilding can explain institutions and payment pathways while PTU/Caelo/implementation remain authoritative for mechanical costs.

No PTU rule for banking, interest, credit scoring or payment-network behavior is inferred from this section.

## Source 6 — PTU GM discussion: desired campaign wealth level is a design choice

Source: Pokémon Tabletop forum discussion, “Money in PTU — need advice as a GM.”
https://www.tapatalk.com/groups/pokemon_tabletop/money-in-ptu-need-advice-as-a-gm-t4756.html

Community discussion explicitly treats campaign wealth level and money availability as GM-facing tuning questions rather than universal setting facts.

Reusable Ouros lesson:

The new layer should make money state traceable without introducing an autonomous economy that undermines campaign tuning. Detailed monetary state should expand only when a meaningful decision depends on it.

Routine purchases should compress.

## Source 7 — payment processing: authorization, acceptance and final settlement are distinct states

Source: BIS Innovation Hub, Nexus payment-processing key points and settlement process documentation.
https://docs.bis.org/nexus/payment-processing/key-points
https://docs.bis.org/nexus/payment-processing/annex-4-step-vs-5-step-processes-in-domestic-clearing-and-settlement

The material separates payment instruction, validation, funds reservation, recipient acceptance/rejection, settlement and confirmation. Different systems can implement these stages differently.

Reusable Ouros architecture:

A payment can have states such as:

- initiated;
- authorized;
- reserved/held;
- accepted;
- rejected;
- settled;
- returned/reversed;
- reconciled.

The exact sequence is authored per payment rail. Ouros should not assume every transfer becomes final the moment a UI says “sent.”

## Source 8 — settlement finality: a payment message is not automatically final transfer of value

Sources: BIS annual-report chapter on payments and BIS Core Principles material.
https://www.bis.org/publ/arpdf/ar2020e3.htm
https://www.bis.org/publ/cpss43.pdf

These sources distinguish submitted, validated, accepted-for-settlement and finally settled states. They also explain finality as the point at which the transfer becomes unconditional/irrevocable under the system’s rules.

Reusable Ouros structure:

- a receipt can say “submitted” without meaning “settled”;
- a merchant confirmation can occur before or after final settlement depending on the rail;
- a payment can fail because of authorization, acceptance, system availability or settlement state without implying fraud;
- a later reconciliation can correct records without deleting the original event trail.

No real-world banking regulation, central-bank structure or legal doctrine is imported into Ouros.

## Source 9 — contemporary payment-system research: account updates can be the economic event even when no physical object moves

Source: BIS Annual Economic Report 2025, chapter on the next-generation monetary and financial system.
https://www.bis.org/publ/arpdf/ar2025e3.htm

The source emphasizes that many payments are implemented as coordinated account updates rather than physical money moving from one place to another.

Reusable Ouros lesson:

Minecraft does not need to spawn a physical coin entity for every payment. A server-authoritative ledger can change balances while Minecraft renders an optional receipt, terminal, till or animation.

Physical cash, tokens or vouchers can still exist where canon wants them; they simply use a different settlement path.

## Source 10 — recent payment-system work reinforces that multiple currencies/rails can interoperate without becoming identical

Source: BIS press release, Project Agorá, 27 May 2026.
https://www.bis.org/press/p260527.htm

The project explores multi-currency settlement across different institutions while preserving distinct currencies and settlement structures.

Reusable Ouros lesson:

If Ouros eventually has multiple regional or institutional media of exchange, interoperability should be represented as an explicit conversion/settlement service. It should not be assumed merely because two balances are numerically denominated.

This is an architectural inspiration only. No tokenisation, central-bank money or real-world institutional model is being imported.

## Reusable narrative structures

### The payment was authorized but never settled

A procurement terminal shows a successful authorization, but the receiving institution never records settlement because a rail outage occurred during the handoff. The mystery is reconciliation, not theft by default.

### The merchant accepts one medium, not another

A market stall accepts ordinary currency and a local market token but not League-issued credits. Another venue has the opposite policy. The difference comes from explicit acceptance agreements.

### The same amount exists in two records for legitimate reasons

One system records a reservation while another already displays a pending debit. The apparent duplicate disappears after settlement/reconciliation.

### The old voucher is still historically real but no longer redeemable

A festival, railway or institution once issued stored-value tokens. Old examples survive in archives and collections even after redemption ends.

### The rural branch only provides narrow services

A small settlement may support deposits/withdrawals or basic transfers without credit, investment, insurance or foreign exchange.

### The emergency payment rail matters because the normal rail is down

A storm, power failure or communication outage can disable one payment method while cash, signed institutional vouchers or offline-authorized relief tokens remain usable.

### A transfer is correct but the public story is wrong

A sponsor promised funds, Finance records the obligation, the payment system settles it, and the recipient later allocates the money differently within the permitted scope. Media/public belief may still report that “the money never arrived.”

## Design guardrails derived from this scan

Do not infer:

- displayed balance -> funds available for every purpose;
- account holder -> beneficial owner of every balance;
- payment initiated -> payment settled;
- payment settled -> goods delivered;
- receipt -> underlying transaction was authorized correctly;
- failed payment -> insufficient funds;
- reversed payment -> fraud;
- bank-like institution -> loans/interest/investment services;
- points -> cash;
- one shop accepting a medium -> universal acceptance;
- digital balance -> internet connectivity currently available;
- physical coin/token -> universally valid currency;
- market price -> PTU mechanical item price unless rules/canon say so;
- high wealth -> social authority, friendship, Trainer Level, Skills or Features;
- payment outage -> economic collapse;
- Pokémon species flavor -> monetary or payment-processing Ability.

## PTU/Caelo validation state

The publicly accessible PTU Core confirms mechanical money/purchase context but does not, from the material used in this pass, establish a complete banking/payment system.

The project’s complete primary Caelo Core/Player/encounter/character-creation corpus was not recoverable through the repository sources inspected in this run.

Super PTU Online Helper was not exposed as an invocable capability.

Therefore Pass 120 does not establish:

- account fees;
- interest;
- lending/credit;
- overdrafts;
- currency conversion rates;
- taxation;
- banking law;
- payment-network rules;
- theft/fraud rules;
- payment-related Skill checks;
- merchant discounts;
- mechanical reward conversion;
- new currencies as canon.

## Originality note

External sources were used only for abstract structural lessons. No protected dialogue, named original Ouros-equivalent institutions, distinctive plots or copyrighted prose are reproduced. All Ouros candidates produced from this research are original and remain non-canon until reviewed.