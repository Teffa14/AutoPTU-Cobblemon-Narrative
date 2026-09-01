# Service Dispatch & Request-Board Research — Pass 173

Status: EXTERNAL RESEARCH / NON-CANON
Date: 2026-09-01

This file records provenance and high-level design extraction only. It does not establish Ouros canon, PTU mechanics, rewards, ranks or legal field actions.

## Research question

How can Ouros support many small resident problems, field requests and institution-generated jobs without turning every incident into a main quest, a random encounter or a disconnected checklist?

The useful gap is dispatch structure: who knows a problem exists, where it is posted, why the player can see it, when it expires or changes, what other work can be combined with it, and how completion feeds durable world state.

## Source 1 — Pokémon Ranger: Shadows of Almia optional Quests

Source:
https://bulbapedia.bulbagarden.net/wiki/Ranger_Quest

Related game overview:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Ranger:_Shadows_of_Almia

Observed structure:
- optional quests are requested by ordinary citizens rather than only central command;
- availability is gated by story progress and prerequisites;
- the player can carry only one active Ranger Quest at a time in Shadows of Almia;
- requests remain geographically grounded in settlements and nearby routes;
- rewards often strengthen the player's existing tool or create a new long-term partner option rather than only paying currency;
- many requests reveal ordinary life in the region between major villain missions.

Reusable lesson for Ouros:
Resident requests should appear because an actor or institution has both a problem and a plausible communication path to the player. Small jobs can be strong worldbuilding when they expose work routines, local dependencies and recurring people. Availability gates should come from explicit world facts, relationship state, route access, institutional standing or prior observations rather than arbitrary player level.

Do not copy:
Almia locations, quest text, named characters, capture-styler progression, partner rewards or specific quest plots.

## Source 2 — Pokémon Ranger: Guardian Signs mission/quest separation

Sources:
https://bulbapedia.bulbagarden.net/wiki/Ranger_Mission
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Ranger:_Guardian_Signs

Observed structure:
- major Missions carry the central story while shorter Quests help citizens;
- optional work can coexist with escalating regional threats;
- mission objectives are usually concrete verbs such as investigate, retrieve, rescue, drive out, salvage or reach;
- some missions alter traversal context rather than merely asking for battle victory;
- multiplayer missions are separate from the main-story progression state.

Reusable lesson for Ouros:
The world needs a visible distinction between narrative-critical assignments and service work. A local dispatch layer should never obscure MAIN or REGION questlines. It should create concise operational contracts whose consequences can still feed settlement, faction, character and ecology state.

## Source 3 — Pokémon Ranger field-move obstacle model

Source:
https://bulbapedia.bulbagarden.net/wiki/Field_Move_(Ranger)

Observed structure:
- traversal problems are represented as explicit environmental obstacles;
- an obstacle asks for a capability family rather than a particular story solution;
- different Pokémon can supply different kinds of field assistance;
- some area moves change access to a larger space instead of only removing one object.

Reusable lesson for Ouros:
A service request should point at world-state objects such as `blocked_route`, `damaged_fixture`, `missing_manifest`, `stranded_actor`, `unverified_report` or `equipment_fault`. The narrative layer may describe the problem and record its resolution, but it must not invent a PTU field capability or infer that a species can solve it. Exact player/Pokémon actions remain governed by PTU/Caelo and live AutoPTU evidence.

## Source 4 — Pokémon Mystery Dungeon job boards

Source:
https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)

Official Rescue Team description:
https://www.spike-chunsoft.co.jp/pages/games/pokedun_i/rescue01.html

Observed structure:
- jobs arrive through mailbox and public boards;
- the player explicitly accepts work before it becomes active;
- request type, destination and difficulty are visible before departure;
- multiple jobs can sometimes be completed during one dungeon trip when their destinations are compatible;
- some special jobs unlock locations or story content, while routine requests remain repeatable;
- board inventory changes over time instead of acting as a permanent dump of every possible task.

Reusable lesson for Ouros:
The most valuable pattern is trip bundling. If Lia needs a ferry manifest delivered to Tideglass, Pia has archive copies for Mirador and Nerea needs an instrument returned, the player should be able to combine compatible work into one plausible route. This makes ordinary travel feel economically and socially connected instead of producing three separate fast-travel errands.

Ouros should not import Mystery Dungeon rank math, random job generation rules, floor restrictions or rewards.

## Source 5 — Mystery Dungeon community rescue-request etiquette

Public community example:
https://www.reddit.com/r/MysteryDungeon/comments/nh1rd4/

Observed structure:
Community rescue requests become actionable when they include a compact contract: game/context, dungeon, floor, identifier and optional notes/reward. Other players can quickly decide whether they can help.

Reusable lesson for Ouros:
A request surface benefits from a compact schema. A player should be able to understand the issuer, location, current problem, urgency, access constraints and known evidence without opening a long narrative transcript.

This is a community-practice observation only. No Reddit user content, phrasing or identifiers should be copied into Ouros.

## Cross-source synthesis

The combined pattern is not "procedural quests." It is a dispatch network.

A useful Ouros request should have:
- issuer identity;
- posting channel;
- affected site or route;
- concise operational need;
- known facts separated from claims;
- prerequisites or access state;
- urgency/expiry when the world state actually supports one;
- compatibility tags for bundling travel;
- consequence targets such as settlement service state, actor knowledge, relationship history, supply continuity, ecology evidence or repair state;
- mechanical dependency declaration when tactical action is possible.

The board is a view over world state. It should not be an independent quest generator that invents emergencies.

## Marea Interior fit

Marea already has the right institutions for a first dispatch network:
- Marea Field Office: field reports, route checks and incident coordination;
- Bruma Market Hall: supply/service requests;
- ferry landing: arrival, manifest and passenger issues;
- Tideglass Archive: document/copy/source requests;
- clinic: privacy-safe logistical requests, never public patient details;
- repair row: equipment intake/return;
- Loma cooperative: lot, dispatch and storage coordination;
- Estación Mirador: observation/equipment requests;
- Battle Yard: maintenance, scheduling and formal challenge notices kept separate from ordinary service work.

This reuses existing residents and sites instead of creating a new guild solely to host a quest board.

## Engine capability implications

The dispatch system itself is narrative/world-state infrastructure and does not require tactical battle support.

Requests that compile into combat must declare exact dependency families.

Current live evidence, based on AutoPTU-Java head `cc5522b72f63ad283153251db5fef4502b860db9` and the latest Narrative engine snapshot, remains:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support as a complete capability family.

Recent Java work strengthens forced-movement geometry and prevention contracts but does not justify promoting complete movement.

## Originality boundary

Ouros may use the high-level ideas of local requests, explicit acceptance, prerequisites, compact job contracts, routing/bundling and changing board inventory.

Ouros must not copy Ranger Quest plots, Mystery Dungeon mission text, rank ladders, named institutions, reward tables, dungeon-job generation formulas or distinctive story content.
