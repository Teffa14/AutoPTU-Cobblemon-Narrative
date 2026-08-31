# Ouros Narrative Research — Clandestine Trade, Smuggling, Provenance & Interdiction — Pass 155

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-30

## Why this pass exists

The repository already models material provenance, cargo movements, courier custody, arrival inspection, covert operations, organizations, investigations, wildlife stewardship, protected areas, ports, transit hubs and institutional decisions. What is still missing is a continuity layer for clandestine supply chains themselves: where a restricted or disputed object or living subject came from, how it moved through intermediaries, where provenance was obscured or relabeled, who actually knew what, where a chain was interrupted, and what remained unresolved afterward.

This pass therefore researches narrative structures for smuggling, poaching, illicit resale, concealed cargo, laundering of provenance and interdiction. It does not create universal criminal law, customs law, contraband categories, police powers, search authority, arrest mechanics or guilt rules.

A shipment can be suspicious without being illicit. An item can have a broken provenance chain without being stolen. A person can possess restricted goods without knowing their origin. An inspection can find a discrepancy without proving intent. Those distinctions are central.

## Existing repository boundaries inspected

The recursive repository tree at narrative head `edf6ffd83cb48ae41089f83d5808dd62f216fdcb` was inspected before writing. The tree was complete (`truncated: false`). Relevant existing layers include:

- `design/material-culture-economy-crafting-layer.md`: item identity, ownership, custody, provenance events and material batches;
- `design/port-harbor-berth-cargo-passenger-operations-continuity-extension.md`: berth, port-call and cargo-operation continuity;
- `design/interregional-arrival-inspection-hold-release-continuity-extension.md`: scoped arrival inspection when an authored requirement already exists;
- `design/covert-operation-infiltration-access-extraction-continuity-extension.md`: cover, access, exposure and extraction for covert missions;
- `design/case-authority-custody-layer.md`: allegations, evidence and case custody;
- `design/organization-faction-identity-lineage-continuity-extension.md`: organization identity and lineage;
- `design/conservation-protected-areas-stewardship-layer.md` and `design/wildlife-monitoring-tagging-telemetry-extension.md`: ecological stewardship and wildlife observation;
- `design/courier-parcel-last-mile-logistics-extension.md`, `design/storage-warehousing-inventory-operations-continuity-extension.md` and `design/batch-traceability-recall-quarantine-extension.md`: ordinary movement, storage and traceability.

Repository-wide search for `smuggling contraband illicit market trafficking poaching black market` returned no dedicated implementation layer. This pass fills that gap without taking ownership away from those systems.

## Pokémon source: Slowpoke Well and Team Rocket's resale scheme

Primary franchise summary:
https://www.pokemon.com/uk/news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-johto-region

Secondary location reference:
https://bulbapedia.bulbagarden.net/wiki/Slowpoke_Well

Reusable structure:

The Johto story connects a local extraction site, harmed Pokémon, an organization performing the extraction, a sale motive and a broader criminal network. The important reusable pattern is not the exact item or villain group. It is the chain:

local source -> extraction -> controlled access -> transfer -> resale outlet/network -> local ecological and social consequence.

For Ouros, a clandestine market becomes more interesting when the source location matters. Removing something from a wetland, nursery, mine, archive, protected area or workshop can create consequences at the source even when the item itself moves far away.

Do not import Slowpoke tails, Team Rocket, Johto locations or the plot wholesale.

## Pokémon source: Hunter J and theft-for-hire

Source:
https://www.pokemon.com/us/animation/seasons/10/episode-20-mutiny-in-the-bounty

Reusable structure:

A professional thief can operate as a contractor rather than as a member of the buyer's organization. The capture site, transporter, holding platform, client and final destination can therefore be separate actors with separate knowledge.

Ouros use:

- do not collapse `captor`, `carrier`, `broker`, `buyer` and `beneficiary` into one faction;
- allow one participant to know only the next handoff;
- allow a recovered Pokémon or item to reveal only one segment of the route;
- preserve partial network disruption when one cell is removed.

Do not import Hunter J, her equipment, aircraft, petrification technology or episode plot.

## Pokémon source: Decolore supply theft

Source:
https://www.pokemon.com/us/animation/seasons/16/episode-32-the-pirates-of-decolore

Reusable structure:

Repeated theft around transport routes can create a recognizable pattern before the actors are understood. A series of missing supplies can initially look like unrelated petty incidents and later become a route-level problem.

Ouros use:

A recurring theft arc can begin from inventory discrepancies, witness reports and route timing rather than from an omniscient villain reveal. The world should preserve each incident independently so investigators can later discover common locations, cargo classes, timing or intermediaries.

## Public PTU community source: fossil black market campaign concept

Source:
https://www.reddit.com/r/PokemonTabletop/comments/fh59h2

This is community material, not PTU rules authority.

Reusable lesson:

A public PTU campaign pitch uses fossil resale as the ordinary economic motive that later intersects with a much larger regional threat. The useful pattern is that a villainous network can start with understandable material incentives and only later expose a more ambitious agenda. The player may first encounter damaged sites, missing specimens, buyers or intermediaries before understanding the organizer's true objective.

Ouros use:

- give clandestine actors ordinary logistics and incentives;
- avoid making every illegal market a single monolithic conspiracy;
- permit a mundane resale operation to intersect with archaeology, ecology, faction politics or myth without requiring those domains to have been secretly controlled by one villain from the start.

No distinctive characters, legendary concepts or plot resolution are imported.

## Wildlife-trafficking research: source, transit, destination and laundering

Sources:
https://sherloc.unodc.org/cld/en/education/tertiary/wildlife-crime/module-1/key-issues/locations-and-activities-relating-to-wildlife-trafficking.html
https://cites.org/sites/default/files/ICCWC%20Vision/ICCWC/ICCWC%20Wildlife%20and%20Forest%20Crime%20Analytic%20Toolkit%202022.pdf
https://www.canr.msu.edu/news/the-hidden-hubs-driving-the-global-illegal-wildlife-trade

Reusable structural lessons only:

- illicit supply chains can have source, transit and destination stages;
- transit hubs can matter independently of the source and final buyer;
- goods can be repackaged or relabeled during transit;
- illicit origin can be concealed inside ordinary lawful trade flows;
- documents, markings and declarations can conflict with physical provenance;
- a seizure point shows where something was found, not necessarily where it originated or where it was ultimately going;
- understanding intermediaries often matters more than assuming a direct source-to-buyer path.

Ouros use:

Represent clandestine chains as event-sourced handoffs. Keep source claims, observed route segments, custody transfers, declarations and later interpretations separate. Never infer a universal legal regime from real-world CITES or UNODC material.

## Design lesson: illicit origin can be laundered through ordinary systems

The ICCWC toolkit emphasizes that goods from illicit sources can enter apparently legitimate supply chains. This is especially useful for Ouros because the repository already has ordinary stores, couriers, warehouses, workshops, ports, auctions and institutions.

The stronger narrative pattern is not a separate glowing `BLACK MARKET` map node. It is a legitimate-looking network containing some compromised, deceived or opportunistic participants.

Possible high-level forms:

- a broker mixes disputed-origin material into ordinary consignments;
- an old credential remains technically genuine but does not authorize the current shipment;
- a specimen is relabeled after a custody gap;
- a buyer receives an object without knowing the source claim is false;
- a workshop processes material whose provenance was already broken upstream;
- a transport operator carries a sealed shipment without knowing its contents;
- a retailer discovers later that one supplier record cannot be reconciled.

This allows moral and investigative complexity without assigning guilt by association.

## PTU / Caelo cross-check

The existing internal source scan confirms that PTU supports central plots, character-centered arcs and sandbox activity, and that Caelo already provides multiple activity containers such as Social, Wild Encounter, Job, Raid, Contest, Gym and Dojo. This supports clandestine-trade stories as campaign content, but it does not establish a universal smuggling subsystem.

Keep UNKNOWN unless explicit project-approved source evidence establishes otherwise:

- universal contraband categories;
- universal criminal law or customs law;
- generic search/seizure authority;
- arrest and detention procedure;
- bribery mechanics;
- fencing or black-market price tables;
- concealment checks;
- smuggling DCs;
- automatic suspicion or Heat meters;
- poaching mechanics;
- universal wildlife-trade permits;
- generic forged-document mechanics;
- automatic guilt from possession;
- automatic faction reputation changes;
- automatic Pokémon ownership transfer after recovery;
- species-based inference that a Pokémon is stolen or illegally captured;
- Move, Ability, Skill or Trainer Feature effects on evidence/provenance unless exact rules say so.

## Engine implications

Most clandestine-trade continuity is narrative and can progress before richer battle support exists. Combat becomes relevant only when a handoff, withdrawal, recovery, convoy or holding site is contested.

Mechanically rich scenes commonly depend on:

- complete movement including push/pull/knockback/interception/forced movement when routes, interception, carrying or withdrawal matter;
- full turn/round lifecycle for timed arrivals or staged escape;
- terrain/weather/hazards/zones/reactions for dynamic loading areas, environmental hazards or reaction windows;
- AI tactical policy when opponents must decide whether to flee, delay, protect, seize or abandon cargo;
- adapter/playback when vehicles, doors, containers or moving platforms must be shown authoritatively.

Reduced versions can keep cargo, evidence and noncombatants outside BattleSpec, freeze geometry and permit only narrow physical outcomes such as `IMMEDIATE_HANDOFF_APPROACH_CLEAR` or `IMMEDIATE_STORAGE_EXIT_ROUTE_CLEAR`.

## Provenance safeguards

This research must not silently establish any specific Ouros criminal organization, protected species list, contraband class, border, police force, customs office, legal penalty, black-market price, smuggling route or enforcement mandate.

Every concrete proposal derived from this scan remains NON-CANON until separately approved.

A battle result cannot prove:

- illicit origin;
- ownership;
- intent;
- guilt;
- buyer identity;
- network membership;
- legality of a search;
- validity of a seizure;
- provenance authenticity;
- future custody disposition.

Those conclusions require the systems that actually own them.

## Research conclusion

The strongest reusable pattern is a chain of partial knowledge rather than a single criminal flag. Source actors, carriers, brokers, processors, buyers and beneficiaries can be different people. Legal-looking infrastructure can carry disputed-origin goods. One interdiction can expose one segment while leaving the rest intact. A successful Ouros arc should therefore preserve route evidence, custody gaps, provenance claims, intermediary knowledge and downstream consequences instead of collapsing the story into `contraband found -> faction defeated`.