# Inland waterways, canals, locks and navigation research — Pass 154

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is established Ouros canon.
Date: 2026-08-24

## Scope

This pass investigates inland navigation as a persistent world system: navigable rivers, canals, locks, maintained channels, ferries, barges, lock queues, temporary restrictions, operating windows, wildlife conflicts and multi-use water decisions.

The repository already has authoritative proposed layers for Freshwater/Hydrology, Travel, Maritime, Rail, Road Transit, Supply Chains, Emergency Services and wildlife ecology. The missing boundary is operational navigation between physical water state and journey/cargo state.

The target separation is:

physical water regime -> navigability assessment -> navigation asset state -> operating decision -> vessel/service movement -> passenger/cargo consequence -> historical record.

A river being wet does not prove it is navigable. A lock being mechanically healthy does not prove a vessel can reach it. A ferry suspension does not mean the waterway is physically closed.

## Repository overlap review

### Freshwater, Watersheds & Hydrology

`design/freshwater-watersheds-hydrology-layer.md` already owns rivers, streams, lakes, canals, flow/level state, reservoirs, water-control assets and multi-use water dependencies. It explicitly keeps physical water, infrastructure operation, observation and tactical PTU state separate.

Pass 154 therefore must not duplicate discharge, flood, groundwater or reservoir simulation. It reads those states when navigation needs them.

### Maritime, Coasts & Underwater Depths

`design/maritime-coasts-depths-layer.md` already owns harbors, sea lanes, coastal maritime assets and submerged sites. Pass 154 is limited to inland navigation and inland interfaces. A river port may link both layers where appropriate.

### Travel, Transport & Expedition

`design/travel-transport-expedition-layer.md` already owns travel connections, route availability, journeys and generic public transport services. Pass 154 supplies inland-waterway operating context to those journeys rather than replacing Travel.

### Supply Chains / Markets / Postal

Those layers own inventory, consignments, commercial offers and parcels. A barge delay may change their states, but navigation never creates or destroys cargo by implication.

## Pokémon official material

### Leading a Stray — Canalave operational blockage

Source: Pokémon.com, “Leading a Stray,” Season 12 Episode 5.
https://www.pokemon.com/us/animation/seasons/12/episode-5-leading-a-stray

Reusable structure:

- a group of Wailord physically blocks Canalave Harbor;
- boats remain present but cannot depart;
- a scheduled ferry becomes unavailable;
- the visible transport disruption is connected to a separate wildlife rescue problem in the drainage/sewer network;
- a drawbridge becomes another independent navigation constraint later in the episode.

Design lesson for Ouros:

A water transport failure can be caused by ecology, infrastructure or geometry without any of those systems becoming equivalent. `service_suspended`, `navigation_passage_blocked`, `wildlife_group_present` and `bridge_state` should be separate records.

Do not copy the Wailmer/Luxio plot or solution. The reusable grammar is `operational blockage -> stranded travelers/cargo -> investigate connected infrastructure/ecology -> resolve each constraint separately`.

### Type Casting — missing bridge creates ferry dependency

Source: Pokémon.com, “Type Casting,” Season 4 Episode 5.
https://www.pokemon.com/us/animation/seasons/4/episode-5-type-casting

Reusable structure:

A river crossing becomes unavailable because there is no bridge. An existing boat operator can provide an alternative crossing, and access to that service becomes part of the local adventure.

Design lesson:

Ferry, bridge and ford are alternate connection services over the same geographic barrier. The disappearance of one crossing can increase the significance of another without changing the river itself.

## Fan-game material

### Pokémon Uranium — freshwater ferry as a persistent route service

Sources:
- Pokémon Uranium Wiki, “Tandor Luxury Cruise.”
  https://pokemon-uranium.fandom.com/wiki/Tandor_Luxury_Cruise
- Pokémon Uranium Wiki, “Route 7.”
  https://pokemon-uranium.fandom.com/wiki/Route_7

The former Vinoville Lake Ferry becomes a persistent freshwater transport link across a large inland body of water. It connects several locations and can also become a contained adventure location while still serving a transport function.

Reusable structure:

- a transport asset can be both movement infrastructure and a temporary playable location;
- route service can persist before and after a crisis;
- access rules, crew state and passenger state can change without changing the underlying water body;
- a ferry can create a natural chapter boundary because departure and arrival are explicit transitions.

Ouros adaptation:

Use inland vessels as persistent assets with operating history, crew/service links and journey records. Do not import Uranium’s ticket prices, plot, characters, Nuclear mechanics or encounter design.

## PTU community / campaign-design material

### Open-ended campaign advice

Source: r/PokemonTabletop, “First time DM thinking of making a PTU campaign,” 17 Nov 2025.
https://www.reddit.com/r/PokemonTabletop/comments/1oz4e7w/first_time_dm_thinking_of_making_a_ptu_campaign/

A useful community recommendation is to maintain multiple lightly specified hooks in an open world and develop the ones players engage with rather than fully scripting every possibility.

Application to inland navigation:

A canal network can accumulate operational hooks — delayed ferry, lock inspection, wildlife crossing, cargo backlog, towpath detour, survey discrepancy — without turning each one into a mandatory quest. Routine lockages should compress. Only a lockage with a meaningful decision, conflict or consequence should expand into playable content.

### Road-trip campaign warning

Source: r/PokemonTabletop, “Asking out of curiousity,” 17 Mar 2022.
https://www.reddit.com/r/PokemonTabletop/comments/tglxnl

A GM reports that long undifferentiated travel stretches can become barren session material.

Application:

Inland waterways should have named operational nodes: locks, junctions, ferry landings, maintenance reaches, old towpaths, ports, spillways and transfer points. These create reusable context without forcing random encounters every few minutes.

## Navigation operations research

### USACE navigation lock operation

Source: U.S. Army Corps of Engineers, “Navigation Locks — Locking Through.”
https://www.usace.army.mil/Missions/Civil-Works/Navigation-Locks/

Source: Tulsa District, “How Navigation Locks Operate.”
https://www.swt.usace.army.mil/Missions/Navigation/Locking.aspx

Reusable system principles:

- a lock chamber is an intermediate controlled space between two water levels;
- vessels enter only when the relevant gate/chamber state permits it;
- water level is changed before the opposite gate opens;
- vessel movement and water-control state therefore occur in an ordered sequence;
- procedures vary between facilities.

Ouros should represent lockage as an operational event, not an animation shortcut.

No real-world safety regulation or US institutional authority is imported into Ouros.

### 2025 USACE hydraulic structures manual

Source: USACE EM 1110-2-2610, published 18 March 2025.
https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM%201110-2-2610_FINAL_18Mar2025.pdf

The manual notes that lock gates/valves can fill and empty chambers, serve as guard gates, pass debris or ice and permit dewatering. A navigation lock requires closure at both ends so chamber level can be varied between upper and lower approaches.

Reusable design lesson:

An asset can be physically present while one subcomponent is unavailable, under inspection, dewatered or configured for another function. Avoid a single `lock_open=true` field.

### Multi-use water management

Source: USACE EM 1110-2-3600, “Management of Water Control Systems.”
https://www.publications.usace.army.mil/portals/76/publications/engineermanuals/em_1110-2-3600.pdf

Navigation may rely on canals, locks, dams, reservoirs, maintained channels and releases that maintain navigation depth. The same stored water may also support water supply, water quality, hydropower, fish/wildlife and recreation.

Reusable design lesson:

A navigation request can conflict with another valid water use without either side being an antagonist. Ouros should record the operational decision and its dependencies rather than generate a morality score.

### Infrastructure resilience

Sources:
- USACE Civil Works Navigation overview.
  https://www.usace.army.mil/Missions/Civil-Works/Navigation/Remote-Lock-and-Dam-Operations/
- USACE Resilient Lock and Dam Operations.
  https://www.usace.army.mil/Missions/Civil-Works/Navigation/Resilient-Lock-and-Dam-Operations/

Reusable structure:

Lock-and-dam systems are long-lived infrastructure with maintenance, modernization, sensors, controls and operating staff. A modernization can change how a facility is operated while the navigation function persists.

Ouros can therefore preserve several generations of lock controls, operator practice and maintenance history without creating a new location every time the equipment changes.

## High-value Ouros design lessons

1. Keep water state, navigation clearance, asset state, service state and journey state independent.
2. A temporary closure can produce consequences in Travel, Supply Chains, Postal, Workplaces, Markets and Crisis without changing those systems’ authority.
3. Wildlife blockage is an ecology event first and an operational restriction second; it does not imply hostility or capture eligibility.
4. A lockage is a sequence with history. Failed, aborted and delayed lockages should remain records rather than disappear.
5. Routine navigation should compress. Operational detail appears when a decision or consequence matters.
6. Water allocated for navigation can create legitimate trade-offs with other uses. Do not make every conflict sabotage or corruption.
7. Alternate modes create resilience: bridge, ferry, rail transfer, road haulage, portage or another lock route can take over temporarily.
8. Infrastructure upgrades should preserve old revisions and operational memory.
9. Minecraft water blocks, gates, pistons or boats are presentation, never authority for navigation truth.
10. No lock, current, vessel or debris mechanic should become PTU tactical state unless exact PTU/Caelo and engine evidence supports it.

## PTU/Caelo boundary

This research establishes no PTU rules.

Before any tactical use, verify exact project-source rules for:

- Swim and underwater movement;
- currents or forced movement;
- falling/drowning if applicable;
- vehicle/vessel rules if any;
- Trainer/Pokémon carrying;
- movement on moving platforms;
- water Terrain or Weather;
- hazards;
- interception/reactions;
- relevant Moves, Abilities, Items or Trainer Features.

The project’s PTU/Caelo material remains the rules authority. External navigation sources are world-system inspiration only.

Super PTU Online Helper was not available as an invocable capability in this run. No result is invented or attributed to it.
