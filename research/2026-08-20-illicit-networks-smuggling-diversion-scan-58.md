# Ouros Research Scan — Pass 58

Status: research and provenance only. Not canon. Not a PTU rules source.

Date: 2026-08-20

## Scope

This pass studies fictional criminal logistics in Pokémon settings: theft, poaching, black markets, front businesses, diversion of legitimate goods, client-driven capture, smuggling across routes or jurisdictions, false accusations, recovery of stolen Pokémon and evidence chains.

The repository already has systems for cases, custody, antagonists, factions, conservation, finance, transport, digital records, credentials and Pokémon agency. The missing layer is the network that connects acquisition, concealment, movement, brokerage and demand.

The design goal is not to create a universal crime simulation. It is to create persistent world state that can explain how an illicit operation survives, changes or collapses without reducing every offender to a generic villain.

## Repository cross-check

Existing systems already cover important adjacent concerns:

- `case-authority-custody-layer.md` keeps allegations, evidence, authority and custody separate.
- `antagonist-agency-defection-escalation-layer.md` models adversaries as actors with goals, resources and internal fault lines rather than `villain=true`.
- `material-culture-economy-crafting-layer.md` tracks item provenance and persistent item instances.
- `conservation-protected-areas-stewardship-layer.md` covers ecological protection and wildlife pressure.
- `pokemon-agency-partnership-release-layer.md` separates Pokémon identity, custody, partnership and ownership claims.
- `travel-transport-expedition-layer.md`, `maritime-coasts-depths-layer.md` and `interregional-mobility-recognition-layer.md` already provide legal movement infrastructure.
- `finance-sponsorship-risk-layer.md` separates money promised, transferred and restricted.
- `digital-systems-cyberspace-data-layer.md` covers logs, versions and access without making digital records infallible.

No existing layer models the complete illicit flow from source to buyer. Pass 58 fills that gap.

## Public sources inspected

### 1. Official Pokémon: Johto retrospective — Team Rocket and the Slowpoke Tail black market

Source:
https://www.pokemon.com/us/pokemon-news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-johto-region

The official retrospective explicitly describes Team Rocket stealing Slowpoke and harvesting tails for sale on the black market. It also connects later operations to a hideout and control of a communications facility.

Reusable structure:

- wildlife exploitation can feed a market rather than exist only as random cruelty;
- acquisition, processing, sales and organization can be different operational layers;
- a local ecological incident can expose a larger network;
- a network can use ordinary infrastructure and communications as part of its operations.

Do not copy Team Rocket, Slowpoke Tail trafficking or Mahogany Town into Ouros.

### 2. Official Pokémon animation — Pokémon Hunter J

Source:
https://www.pokemon.com/us/animation/seasons/10/episode-20-mutiny-in-the-bounty

Hunter J operates as a thief for hire. The episode frames the theft of Pokémon as client-driven work performed by a mobile specialist with transport, staff and powerful Pokémon.

Reusable structure:

- demand can originate from a buyer/client who is not present at the capture site;
- a hunter cell may be mobile and contract-driven rather than territorially rooted;
- recovering the Pokémon does not automatically identify the buyer;
- transport vehicles, temporary holding areas and transfer points become investigative nodes.

Do not copy J, her equipment, crew, targets or story beats.

### 3. Official Pokémon animation — fraudulent breeding center as front operation

Source:
https://www.pokemon.com/uk/animation/seasons/1/episode-52-the-breeding-center-secret

A legitimate-looking breeding center is used as cover for Pokémon theft. Photographic evidence later matters to the investigation.

Reusable structure:

- a front business can provide legitimate services and still conceal an illicit operation;
- custody can change for an apparently valid reason before the diversion occurs;
- public reputation of the front and actual internal activity must remain separate;
- visual evidence needs provenance and interpretation, connecting directly with Pass 46.

Do not copy the breeding center, Butch, Cassidy or the episode plot.

### 4. Official Pokémon animation — theft from a Pokémon Center repository

Source:
https://www.pokemon.com/us/animation/seasons/11/episode-40-a-lean-mean-team-rocket-machine

The episode includes theft of stored Poké Balls from a Pokémon Center repository.

Reusable structure:

- institutional storage creates custody and inventory risks separate from personal theft;
- a missing asset can be detected through operational state, witnesses or logs;
- recovery must preserve item/Pokémon identity rather than replacing the missing entity with a generic equivalent.

### 5. PTU campaign retrospective — Wakino Privateers

Source:
https://pokemontabletop.com/wakino-privateers-a-game-of-love-extreme-power-levels-and-actually-not-that-much-piracy/

The campaign uses an archipelago where piracy is difficult to prosecute because crimes and jurisdictions span different islands. The PCs investigate criminal activity and eventually connect apparently local operations to a larger organizer.

Reusable structure:

- jurisdiction gaps can create operational space for networks;
- local incidents may be independent, connected or only partially connected;
- network discovery should emerge through evidence rather than a global `crime faction` flag;
- dismantling one cell does not automatically dismantle the organization.

This source was previously useful for maritime design. Pass 58 uses a different aspect: distributed criminal organization and cross-jurisdiction investigation.

### 6. Public Pokémon Ranger RP — Almia Goes Old School

Sources:
https://forums.pokecharms.com/threads/pokemon-ranger-almia-goes-old-school-discussion-thread.19702/
https://forums.pokecharms.com/threads/pokemon-ranger-almia-goes-old-school-rp-thread.19789/

The RP explicitly places Rangers among traders, prospectors, smugglers and poachers in a frontier setting. The design distributes plot-hook creation among players rather than relying on a single scripted villain.

Reusable structure:

- ordinary economic activity and illicit activity can coexist on the same routes;
- a transporter, trader or prospector is not suspicious merely because criminals use the same infrastructure;
- player-created local incidents can feed a larger network only when evidence supports the connection.

Do not copy characters, setting history or specific RP scenes.

### 7. Eevee Expo fangame — Pokémon Adventure Chapter 1

Source:
https://www.eeveeexpo.com/threads/9445/

The public project description presents a criminal organization built around stealing Pokémon and selling them onward to other organizations, producing an expanding underground market.

Reusable structure:

- sellers, brokers and buyers can be different actors;
- criminal revenue can increase capacity over time;
- a network can have both routine profit motives and a separate strategic objective.

Do not copy Team Nebula, its region, targets, characters or Legendary plot.

### 8. Pokémon Adventures publisher summary — stolen museum fossil

Source:
https://www.simonandschuster.com.au/books/Pokemon-Adventures-Black-and-White-Vol-3/Hidenori-Kusaka/Pokemon-Adventures-Black-and-White/9781421561783

The official publisher summary includes theft of a fossil from a museum.

Reusable structure:

- cultural/scientific objects can enter illicit flows without becoming generic loot;
- museum provenance, custody and evidence layers remain relevant after theft;
- the downstream motive may be scientific, political, monetary or strategic and should remain unknown until supported.

Do not copy the manga plot or characters.

## Structural findings

### A. Model flows, not a single black-market container

A useful network may contain:

source/acquisition → temporary holding → aggregation → concealment → transport → broker → buyer/client → reuse/resale.

Any leg may be absent.

The same legal route, warehouse or ferry may be used by legitimate traffic and illicit traffic. The location itself must not become `criminal=true`.

### B. Acquisition methods should remain distinct

Possible high-level categories:

- theft from a Trainer;
- poaching/capture from the wild;
- diversion while in institutional custody;
- fraudulent transfer;
- theft of items, fossils, research samples or equipment;
- misappropriation of legitimate shipments;
- voluntary sale later alleged to be improper;
- unknown provenance.

These categories are narrative facts only when evidence supports them.

### C. Demand matters

The actor who physically takes an asset may not be the actor who benefits.

A network should be able to represent:

- end buyers;
- commissioning clients;
- brokers;
- transporters;
- storage providers;
- corrupt or coerced insiders;
- legitimate service providers unknowingly used by the network.

This prevents every investigation from ending when the visible thief is defeated.

### D. Front businesses need mixed truth

A front may perform real legitimate work.

Useful state distinctions:

- legitimate services provided;
- illicit activity suspected;
- illicit activity verified;
- which staff know;
- which assets/accounts are involved;
- whether the institution itself is complicit or only infiltrated.

Do not convert every employee into a member of the network.

### E. Recovery and prosecution are separate

Ouros may allow players to recover a Pokémon, fossil, shipment or item even when:

- the buyer remains unknown;
- the theft cannot yet be proved;
- the network remains active;
- jurisdiction is disputed;
- a case later closes incomplete.

This produces satisfying local closure without requiring total network destruction.

### F. Illegality is authored state, not rarity or secrecy

A rare Pokémon, private sale, unusual route, cash payment, masked buyer or unregistered item is not automatically illegal.

Until Ouros canon defines the relevant rules, the system should store:

- authorization state;
- provenance state;
- custody state;
- claims;
- evidence;
- institutional assessment;
- legal-status claim if authored.

It should not infer a universal criminal code.

## PTU/Caelo mechanical boundary

This pass does not create new rules for capture, theft, ownership, restraint, pursuit, surrender, confiscation, search, surveillance, tracking or evidence.

The supplied project research already treats capture, item ownership, custody and mechanically consequential changes as server-authoritative state. The full primary Caelo PDFs were not reliably recoverable in this runtime, so no new Caelo-specific legality or enforcement rule is asserted.

PTU/Caelo must remain authoritative for:

- capture legality and rolls;
- any Skill checks involving Guile, Stealth, Perception, Survival, Command or related Features;
- Pokémon capabilities used in pursuit or concealment;
- battle mechanics during interception;
- Trainer Features/perks;
- item behavior;
- movement, restraint, escape or pursuit effects.

Narrative legality remains a separate canon decision.

## Engine implications

The richest illicit-network encounters tend to need objective-aware movement rather than only defeat-all battles.

Examples:

- stop a carrier from reaching an exit;
- protect a recovered Pokémon while withdrawing;
- prevent a transfer between two actors;
- hold a gate while a shipment is secured;
- intercept without damaging protected evidence;
- allow surrender or retreat as a meaningful outcome.

These depend on exact permanent capability families and must not be approximated by Minecraft-side scripts that recreate missing PTU rules.

Reduced versions can keep cargo, victims, evidence and handoffs in overworld state and use a static legal battle only if combat actually begins.

## Design direction for Ouros

Pass 58 should add:

- illicit operation objects;
- asset-flow legs;
- front-business state;
- diversion events;
- broker/client relationships;
- concealment and transfer records;
- network cells and knowledge boundaries;
- recovery/disposition state;
- integration with cases, custody, conservation, finance and transport;
- no automatic criminal labels without authored rules/evidence.

## Source-use limits

All copyrighted source material is used only for high-level structural analysis. No protected prose, dialogue, distinctive characters, gadgets, organizations, plots or scenes are imported into Ouros.
