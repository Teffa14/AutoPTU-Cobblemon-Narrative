# Ranches, Managed Pokémon Groups & Pasture Continuity Research — Pass 85

Status: research/provenance only. Nothing in this file is automatically Ouros canon.

Date: 2026-08-27

## Why this pass exists

The repository already has broad agriculture, food production, breeding/nursery, Pokémon work assignments, ecology, conservation, seasonality, travel, care, housing, material provenance and settlement systems. The full repository inventory through Pass 84 was inspected before writing this pass.

The remaining gap is narrower: a persistent rural site may contain a managed group of Pokémon, several paddocks or grazing zones, recurring movement between those zones, individual welfare cases, production/service dependencies, working Pokémon with exact assignments, neighboring wild populations and route links. Existing layers can represent each fact separately, but they do not yet provide one continuity model for the managed group and its land-use history.

This pass researches that gap without creating new PTU breeding rules, ownership law, species productivity scores, hunger simulation, Rancher mechanics or Cobblemon battle authority.

## Existing Ouros boundaries preserved

`design/food-agriculture-hospitality-layer.md` already owns agricultural sites, food batches, cultivation cycles, venue/service state and generic food-production provenance. It explicitly rejects species stereotypes as evidence of work capability.

`design/breeding-eggs-nursery-lineage-layer.md` owns Egg provenance, nursery services, hatching continuity and lineage records. A ranch does not become a breeding institution merely because several Pokémon of the same species share a paddock.

`design/pokemon-work-role-participation-extension.md` owns the exact assignment of one persistent Pokémon to one bounded task, including suitability evidence, supervision and withdrawal. A managed group record therefore should not duplicate an individual working Pokémon's assignment.

`design/conservation-protected-areas-stewardship-layer.md` owns ecological management designations and policy. A ranch's pasture rotation or wildlife overlap does not create conservation authority by itself.

`design/seasonality-calendar-phenology-layer.md` owns regional cycles, phenology and calendar state. Pasture-use windows should reference that substrate instead of inventing a separate season clock.

`design/cobblemon-runtime-authority-boundary.md` remains binding. Cobblemon can materialize Pokémon entities, models, animation, sounds, fences, blocks, UI and networking. Ouros decides world facts and encounter composition. AutoPTU decides tactical participants, legality and results.

## New public sources inspected

### Moomoo Farm — production continuity linked to one individual's welfare

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Moomoo_Farm
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Gold_and_Silver/Part_8

The Johto location presents a small working farm with a paddock, barn, owners, several Miltank and one specifically sick individual. The farm's milk service becomes available after that individual's recovery.

Reusable structures:
- a managed group can contain individually important members without requiring every background member to receive full narrative identity;
- an individual welfare case may create a real production/service consequence;
- care, production and storefront state should remain separate records connected by explicit handoffs;
- recovery of one individual can change availability without turning health into a hidden productivity stat.

Transformation boundary:
Do not copy the named farm, exact Berry requirement, reward, price, species roster or healing procedure. Ouros must use Care and governing PTU/Caelo mechanics for actual health state.

### Paniola Ranch — mixed-use rural landscape

Source:
- https://bulbapedia.bulbagarden.net/wiki/Paniola_Ranch

Paniola Ranch is positioned between routes and a town, contains multiple fenced zones, a paddock for tended Pokémon, farm equipment, a nursery, roads and areas where wild Pokémon appear separately from the tended group.

Reusable structures:
- a ranch can be a landscape rather than one building;
- managed paddocks, public/transit routes, nursery services, work yards and wild-use areas can coexist while retaining separate authority;
- co-location does not collapse managed Pokémon and wild populations into one state;
- road access makes rural production part of regional travel/logistics rather than an isolated minigame.

Transformation boundary:
Do not copy Paniola's geography, named facilities, Ride unlocks, species composition or Alola institutions.

### Baa de Mer Ranch / Kalos Route 12 — trained individuals as mobility resources

Source:
- https://bulbapedia.bulbagarden.net/wiki/Kalos_Route_12

The ranch places several Skiddo beside a major route and allows riding them to reach terrain otherwise inaccessible to the player.

Reusable structures:
- a ranch may maintain individuals trained or accustomed to a particular route or service;
- public or institutional mobility can intersect a rural site;
- access to a particular Pokémon does not imply ownership of that Pokémon;
- route suitability must be a property of the exact individual/service relationship, not an automatic species tag.

Transformation boundary:
Ouros must not infer ride eligibility from species or reproduce game-HM gating. Personal or service traversal requires authoritative capability and world-state validation.

### Floccesy Ranch — managed group plus exact working Pokémon

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Floccesy_Ranch
- https://bulbapedia.bulbagarden.net/wiki/Sangi_Ranch

The animated depiction uses a tame Mareep group supervised by people and an Ampharos whose job is to keep that group within the ranch limits. The working Pokémon struggles with the assignment, and the group repeatedly wanders beyond the intended boundary.

Reusable structures:
- managed-group continuity and individual work-assignment continuity are different systems;
- a boundary failure can be operational without making the group hostile or criminalizing the working Pokémon;
- a specific working partner can require training, reassessment or a changed procedure;
- failures should produce observed facts such as `group_outside_planned_zone`, not inferred personality labels.

Transformation boundary:
Do not copy the characters, Team Rocket plot, Thunder Punch solution, species requirement or confidence arc. In Ouros, the work layer must justify any exact Pokémon assignment from evidence.

### PTU community module — Trouble on the Farm

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/ptu-module-trouble-on-the-farm-t3323.html

The author describes a leisurely novice-trainer scenario on a small rural farm. Community feedback highlights varied encounters and multiple ways players may handle them. When asked about encounter tables, the author explains an ecology-first process: consider the whole ecosystem and habitats, then choose Pokémon that fit those conditions and environmental details.

Reusable structures:
- a farm/ranch can sustain a complete low-intensity adventure without becoming a combat gauntlet;
- rural encounters should begin with ecology, habitat and current world conditions rather than a random list detached from the site;
- several response paths can coexist: observation, rerouting, repair, care, negotiation, capture when legal, or battle;
- early-game content can be locally dense and consequential without world-threatening stakes.

Authority warning:
This is community-authored PTU material and inspiration only. Its encounter construction and any unstated mechanics do not establish Ouros rules.

### PTU module collections — farm scenarios as reusable local shells

Sources:
- https://www.tapatalk.com/groups/pokemon_tabletop/premade-adventures-t7173.html
- https://www.tapatalk.com/groups/pokemon_tabletop/mini-module-collection-t7231.html
- https://www.reddit.com/r/PokemonTabletop/comments/itlrso

Public module indexes repeatedly preserve farm/rural scenarios among useful early-game content. One collection describes a scalable farm-help one-shot, while another explicitly treats Trouble on the Farm as a reusable novice adventure.

Reusable lesson:
A rural institution can repeatedly host unrelated stories because the stable site provides residents, animals/Pokémon, routes, production, weather exposure, fences, equipment and neighboring ecology. The location should accumulate history rather than being consumed after one incident.

Do not copy module twists, villains, characters, encounters or maps.

## High-level structures extracted

1. Managed group identity and individual Pokémon identity must coexist. A background cohort may be aggregate while recurring or mechanically important individuals receive persistent IDs.
2. Group membership must be evidence-based and time-bounded. Being physically inside the same fence once does not establish permanent membership.
3. Managed-group state does not settle ownership, custody, breeding status, kinship or willingness to work.
4. A ranch should be zoned: paddock, barn/shelter, handling/staging area, storage, road connection, seasonal pasture, service area and wild-overlap zone may have different use state.
5. Pasture movement should reference calendar, route, habitat and actual access state. It should not be a hidden optimal-grazing formula.
6. Individual welfare can affect a service or production process through explicit dependencies, but health must remain owned by Care.
7. Production output belongs to Food/Material/Storefront systems. The ranch layer should record source group/site and operational context, not invent yields or PTU item effects.
8. Exact herding, guarding, carrying, search or mobility work by a Pokémon belongs to the work-assignment layer and requires individual evidence.
9. Wild Pokémon sharing a ranch landscape remain ecologically and narratively distinct from the managed group.
10. Boundary crossings should be world events with causes and consequences. They should not automatically trigger combat.
11. Group counts can be uncertain. `EXPECTED`, `OBSERVED`, `CONFIRMED_PRESENT`, `UNLOCATED` and `TEMPORARILY_OFF_SITE` are more useful than silently spawning missing members.
12. Rural sites benefit from calm baseline scenes. Routine work should compress until a meaningful decision, discrepancy or ecological interaction appears.
13. A managed group can temporarily shelter elsewhere during weather, crisis, maintenance or habitat conflict without changing ownership or permanent membership.
14. The same pasture may change meaning over time: active grazing, resting/recovery, temporary refuge, research observation, restoration or public access can be different windows of one persistent place.
15. Encounter design should preserve the site's ecology and work history. A battle result should never automatically repair fences, verify animal/Pokémon counts, diagnose illness or establish route rights.

## Proposed implementation vocabulary for later design

Useful concepts to formalize:
- `rural_managed_site`
- `managed_pokemon_group`
- `group_membership_observation`
- `managed_zone`
- `pasture_use_window`
- `group_movement_plan`
- `group_movement_event`
- `count_reconciliation`
- `individual_exception_ref`
- `production_dependency_handoff`
- `wild_overlap_observation`
- `temporary_refuge_event`
- `managed_group_history`

These are world-state concepts, not PTU mechanics.

## Cobblemon reuse opportunities

Potential SAFE_REUSE or ADAPTER_REQUIRED surfaces to inspect at implementation time:
- persistent Pokémon entity projection;
- species/forms/models/textures;
- idle, movement, grazing/resting-looking poses where available;
- cries and ambient sound;
- entity tracking and client/server synchronization;
- fences, gates, hay/storage props, paths, water and vegetation blocks;
- particles/sounds for work presentation;
- UI for group counts, paddock status and service availability;
- persistence hooks mapping an Ouros individual/group member to overworld embodiment;
- world geometry observation through a reviewed adapter.

BattleState, participant/controller logic and any Cobblemon path that decides tactical combatants, HP, status, positions or outcomes remains BATTLE_AUTHORITY_FORBIDDEN.

## Mechanical questions exposed

PTU/Caelo and runtime review remains required before any scenario relies on:
- exact carrying/dragging capacity;
- mounted or assisted traversal;
- Command/Loyalty consequences;
- breeding eligibility or reproductive timing;
- Egg production;
- milk/food item effects or yields;
- weather penalties;
- stampede-style forced movement;
- interception/protection reactions;
- terrain movement effects;
- environmental damage/status;
- Trainer Features affecting ranch work;
- Moves/Abilities used to manage groups or alter pasture/weather;
- wild capture legality in managed-use areas.

## Canon questions left open

- Do any approved Ouros regions use ranches, pastoral systems or managed grazing at meaningful scale?
- Which Pokémon species, if any, are commonly managed in each region?
- What language do local cultures use for managed groups and caretaking relationships?
- What ownership/custody norms apply to managed Pokémon?
- Are products such as milk, fiber, eggs or transport services common, rare or institution-specific?
- How are seasonal pasture routes coordinated with wild habitat and public routes?
- What role do nurseries and care facilities play in rural regions?
- Which Pokémon may work alongside handlers, and what evidence/credentials are required?
- How much of a large managed group should Minecraft materialize at once?

No answer is promoted to canon by this research file.
