# Public Notices, Signage & Physical Information Research — Pass 68

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Scope

This pass investigates how Pokémon games and public Pokémon tabletop material use blackboards, bulletin boards, visible quest markers, posted notices and other physical information surfaces to make world state legible.

The design target is deliberately narrower than the existing Media/Communications layer. Ouros already has information packets, publications, public bulletins, maps, route state, access restrictions, event notices and settlement memory. The missing implementation-facing question is how one of those facts or claims becomes a persistent object in an explorable Minecraft/Cobblemon location, how it becomes stale, and how later corrections remain historically traceable.

## Existing-repository boundary

The repository tree was inspected before research. Relevant existing owners include:

- `design/media-communications-information-layer.md` — information packets, publications and channel reach;
- `design/cartography-survey-wayfinding-layer.md` — authored maps, map editions, route knowledge and map corrections;
- `design/public-space-parks-commons-continuity-extension.md` — entrances, restrictions and public-space rule provenance;
- `design/temporary-public-event-operations-extension.md` — temporary event overlays and notices;
- `design/weather-forecast-preparedness-operational-extension.md` — forecasts and warnings;
- `design/facility-maintenance-repair-inspection-extension.md` — closures and technical reopening;
- `design/courier-parcel-last-mile-logistics-extension.md` — physical delivery;
- `design/libraries-publications-editions-circulation-extension.md` — authored works, editions and copies.

Pass 68 therefore does not create another media system, quest log, map system or access-policy system. It focuses on physical presentation and revision of already-owned information.

## Source 1 — Pokémon Legends: Arceus request blackboard

Source: Bulbapedia walkthrough, Requests 1–30.
https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30

Observed pattern:

Professor Laventon's office contains a blackboard that exposes some requests after their prerequisites are met. Interacting with the board gives a summary and directs the player toward the actual requester for details. The board is therefore an intake/discovery surface rather than an omniscient quest resolver.

Reusable design lesson:

A physical board can reveal that a request exists while keeping the authoritative details with the requester, institution or underlying case record. Availability can depend on world state. A board entry does not need to contain the entire task state.

Transformation for Ouros:

Use a posted notice as a projection of an existing `information_packet`, request record, event instance, restriction or service state. The surface stores where and how it was displayed. The source object keeps authority.

## Source 2 — Pokémon Mystery Dungeon job boards and mailbox

Sources:

Bulbapedia, Pokémon News / Rescue Team Basics:
https://bulbapedia.bulbagarden.net/wiki/PKMN_News

Bulbapedia, Job (Mystery Dungeon):
https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)

Bulbapedia walkthrough intro:
https://bulbapedia.bulbagarden.net/wiki/Appendix:Mystery_Dungeon_walkthrough/Intro

Observed pattern:

Jobs can arrive through multiple surfaces: a bulletin board, mailbox, codes and later other channels. Seeing a job and accepting it are distinct states. Board capacity and accepted-job capacity are also distinct. Special jobs can disappear from the board after they have served their purpose.

Reusable design lesson:

Discovery, acknowledgement, acceptance, active execution and removal from public display should not collapse into one boolean. A notice can be visible without being accepted. A task can remain active after its public notice disappears. Different channels can carry the same underlying request.

Transformation for Ouros:

A notice surface should store display state and observation history. A quest/case/request system should own acceptance and completion. Removing a sign must never delete the underlying request record unless the owning system explicitly resolves or withdraws it.

## Source 3 — Pokémon Ranger: Shadows of Almia quests

Sources:

Serebii quest catalogue:
https://www.serebii.net/ranger2/quests.shtml

Bulbapedia Ranger Quest overview:
https://bulbapedia.bulbagarden.net/wiki/Ranger_Quest

Observed pattern:

Optional requests become available after specific progression points. The player identifies available requesters through a visible icon state, speaks to the citizen, accepts the request and then sees a changed visual marker. The interface externalizes a change in relationship between world actor and player.

Reusable design lesson:

A visible marker should project a real state transition rather than create it. Availability, accepted state and completion can each have different visual representation. The icon is an affordance, not the source of truth.

Transformation for Ouros:

Minecraft signs, particles, icons or NPC indicators may be adapter projections of authoritative narrative records. If an icon fails to render, the quest should still exist. If an unauthorized sign is placed, the underlying authority does not change.

## Source 4 — Pokémon Rejuvenation Help Center pattern

Sources:

Community guide describing Help Center quest boards and revisits:
https://pokuniverse.com/video-games/pokemon-rejuvenation-game/

Community discussion distinguishing Help Center board quests from quests discovered through exploration/NPCs:
https://www.reddit.com/r/PokemonRejuvenation/comments/1gn5dya

Provenance note: these are fan/community sources. They are inspiration only, never rules or Ouros canon.

Observed pattern:

A centralized help board makes a subset of optional work legible, but the world also contains tasks discovered by revisiting places, speaking to characters or entering locations. Players explicitly distinguish board-listed work from ambiently discovered work.

Reusable design lesson:

Do not make every story hook depend on a single universal quest board. Central boards are useful for institutional or public requests; private, emergent, ecological and place-specific problems should still arise through world observation.

Transformation for Ouros:

`notice_visibility` should be optional. A request can be PUBLICLY_POSTED, DIRECT_ONLY, LOCATION_TRIGGERED, INSTITUTION_INTERNAL or otherwise undisplayed. The presence of public signage should reflect the source actor's plausible publication route and privacy constraints.

## Source 5 — PTU campaign structure guidance

Source: Pokémon Tabletop campaign structure guidance mirrored on the Pokémon Tabletop Wiki.
https://pokemontabletop.fandom.com/wiki/Campaign_Structure

Observed pattern:

Pokémon tabletop campaigns benefit from alternating calm periods where players pursue gyms and personal interests with periods where larger plot pressure intrudes. Routine activities remain useful even in long campaigns.

Reusable design lesson:

Physical information surfaces can support low-pressure self-directed play between major arcs. A board showing repair work, club meetings, route notices or requests gives the player grounded options without inventing a crisis every session.

Transformation for Ouros:

Noticeboards should surface already-generated world opportunities from institutions, services, public spaces and local actors. They should not randomly create disconnected filler quests.

## Source 6 — Public PTU session log with environmental response

Source: r/PokemonTabletop campaign log #24.
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Observed pattern:

A mundane action in the environment creates a response from a local Pokémon, and the scene can be resolved by understanding the cause and repairing the situation rather than only by combat.

Reusable design lesson:

Posted warnings and later corrections can become environmental storytelling when they refer to a place that players can physically inspect. A sign saying that an area is closed should point to real closure state, evidence, maintenance or ecology; it should not exist only as decoration.

Transformation for Ouros:

A trail warning can reference an actual ecology observation, maintenance record or temporary restriction. If the cause later changes, the old notice can become stale evidence rather than silently rewriting history.

## Cross-source patterns

### Physical display is a projection

The underlying request, restriction, schedule, map or warning remains owned by its source system. The board, sign or poster is a visible representation of that state.

### Visibility and authority differ

A highly visible notice can be wrong, stale, copied without authorization or superseded. A correct rule can exist even when its sign is damaged. Presence in the world does not create policy.

### Revision history matters

Signs and notices should be replaceable without deleting prior public history. A player who read an old closure notice yesterday may plausibly act on outdated information today.

### Public boards should not become universal quest vending machines

They work best for requests that actors plausibly choose to publish. Sensitive cases, private relationships, wild ecology and emergent events need other discovery paths.

### World change should update visible surfaces

If a gate closes, a ferry schedule changes, a shop reopens, an event is delayed or a trail reroutes, nearby informational props are high-value places to show that persistence inside Minecraft.

## Anti-copy / transformation rules

Do not copy source text, dialogue, named NPCs, exact quest lists, reward structures, proprietary UI layouts or distinctive plots.

Do not import Mystery Dungeon job limits, Ranger reward systems, Rejuvenation morality systems or Legends: Arceus request prerequisites.

Do not infer that Ouros has one universal bulletin network, municipal signage standards, permit law or magical updating boards.

Do not convert a notice into canonical truth. Every displayed statement must retain provenance to an owning claim or state object.

## PTU/Caelo mechanical boundary

No researched source establishes PTU tactical rules for signs, notices or quest markers.

A physical notice can influence player knowledge and overworld navigation. It does not grant Accuracy, Evasion, movement, Skills, Edges, Features, Orders, morale, initiative, damage, status or other combat effects.

If a notice-related encounter later uses civilians, escort movement, dynamic barriers, forced displacement, weather, hazards, reactions or objective-aware opponents, those mechanics must be separately verified against PTU/Caelo and AutoPTU.

## Pass 68 design target

Create a narrow physical-information extension with:

- `information_surface` for boards, signs, posters, schedule panels and map boards;
- `posted_notice` that references an authoritative information/state object;
- display lifecycle and revision history;
- readable-condition state separate from content truth;
- provenance and authorization refs;
- acknowledgement/observation records;
- stale/superseded notice handling;
- Minecraft projection rules;
- noncombat mysteries built from conflicting displayed information;
- battle-adjacent encounters with explicit full/reduced capability contracts.
