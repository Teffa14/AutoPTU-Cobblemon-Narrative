# Pass 130 — Libraries, Lending, and Public Knowledge Research Scan

Status: RESEARCH / NON-CANON
Date: 2026-08-23
Writable repository: `Teffa14/AutoPTU-Cobblemon-Narrative`
Read-only evidence: `Teffa14/AutoPTU-Java`, `Teffa14/AutoPTU`

## Why this scan exists

The repository already has strong owners for archives, museums, languages and translation, education, digital systems, postal logistics, identity, public memory, science, and material provenance. What it did not yet have was a dedicated owner for ordinary public knowledge access: circulating copies, reading rooms, library holdings, lending, editions, holds, reference service, mobile branches, and resource sharing between institutions.

This matters because a persistent world needs to distinguish a work from a translation, an edition from a specific copy, and possession from access. A book can be replaced without replacing the work. A damaged copy can become historically important. An old edition can remain useful for understanding what people knew at the time. A returned volume does not prove that the borrower read it. A library holding a text does not mean the institution endorses every claim inside it.

This scan keeps provenance separate from Ouros canon. Pokémon examples are used for high-level worldbuilding patterns. External library science is used only for abstract data-model lessons. No real-world law, lending period, fee, privacy statute, copyright regime, or professional standard is imported into Ouros.

## Repository overlap review

Before research, the branch inventory and README were inspected to avoid duplicating existing systems.

Existing authorities that remain separate:

- Archives / institutional memory: records kept because they document actions, decisions, evidence, or institutional history.
- Museums / collections: stewardship, accession, condition, conservation, loans, display, and interpretation of collection objects.
- Languages / translation: source expression, writing system, transcription, translation, interpretation, and terminology versions.
- Education: curriculum, learning activity, assessment, and institutional teaching.
- Digital systems: files, versions, data stores, backups, access grants, and digital incidents.
- Postal / courier logistics: physical movement and handoff of letters, parcels, samples, and other items.
- Identity / aliases: persistent actor identity and record linkage.
- Science: observation, method, evidence, hypothesis, dataset, and interpretation.
- Public memory: attention, remembrance, reception, and what communities believe or remember.
- Material culture: persistent physical-object identity and provenance.

Pass 130 should own public-access knowledge resources and their circulation. A unique manuscript used principally as evidence belongs primarily to Archives. A historically significant physical copy may be handed to Museums or Archives for preservation even if it once circulated in a library.

## Pokémon source patterns

### Canalave Library — library as regional knowledge infrastructure

Source: Bulbapedia, Canalave Library
https://bulbapedia.bulbagarden.net/wiki/Canalave_Library

Source: Bulbapedia, Canalave City
https://bulbapedia.bulbagarden.net/wiki/Canalave_City

Reusable pattern:

Canalave Library is a public place where Sinnoh myths and historical ideas are available for reading, and it is also used as a meeting point for active research discussion. The useful structure is not the individual myths. It is that a library can simultaneously be a civic place, a research resource, and a repository of multiple claims about regional history.

Ouros adaptation:

A regional library can hold old field guides, folklore collections, route maps, scientific monographs, tournament histories, newspapers, translated works, and public records without any single shelf becoming authoritative world truth. Researchers can meet there because the institution provides access and comparison, not because the building itself knows which source is correct.

Guardrail:

`LIBRARY_HOLDS(text)` does not imply `TEXT_CLAIM == WORLD_TRUTH`.

### Malie Library — public access plus old regional knowledge

Source: Bulbapedia, Malie City / Malie Library
https://bulbapedia.bulbagarden.net/wiki/Malie_Library

Reusable pattern:

Malie Library is explicitly public and contains older material about Alola's history, guardian deities, kahunas, and Legendary Pokémon. In the games, characters use the library to pursue an existing research question rather than receiving an automatic quest from the institution.

Ouros adaptation:

Libraries can be places where players answer questions they already care about. A useful library visit may prevent an unnecessary expedition, reveal that two names refer to the same place, show that a route description belongs to an older edition, or surface several incompatible interpretations that require fieldwork.

Guardrail:

Access to a book does not equal comprehension, acceptance, or completed research.

### Pokémon Reborn — library as layered urban place, not just lore kiosk

Source: Pokémon Reborn Wiki, Beryl Library
https://pokemon-reborn.fandom.com/wiki/Beryl_Library

Source: Pokémon Reborn Wiki, Sanctum Key Sidequest
https://pokemon-reborn.fandom.com/wiki/Sanctum_Key_Sidequest

Reusable pattern:

The Beryl Library participates in multiple urban systems across the game: sidequests, employment, hidden rooms, books, cleanup, Pokémon presence, and later discoveries. The useful design lesson is recurrence. A library can be revisited for different reasons as the city changes.

Ouros adaptation:

A branch library can be a workplace, public-space node, mobile-service hub, research stop, weather shelter, community notice point, and later a historically significant place. Those functions should remain separate records rather than becoming one permanent quest marker.

Anti-pattern to avoid:

Do not make every suspicious shelf a secret door or every rare book a dungeon key. Hidden-room puzzles can exist when authored, but ordinary circulation and reference work should carry most library stories.

### Pokémon Insurgence — library as settlement-scale institution

Source: Pokémon Insurgence Wiki, Utira Library
https://wiki.p-insurgence.com/Utira_Library

Reusable pattern:

Utira Town is identified in part through its large library, while the library also contains an abandoned wing used by the game's plot. The reusable high-level lesson is that knowledge institutions can be part of why a settlement exists or grows.

Ouros adaptation:

A library may affect settlement identity, student housing, research travel, postal demand, printing, cafés, secondhand book markets, mobile routes, or rail schedules without becoming an omniscient lore vault.

Copyright transformation note:

No prophecy, cult plot, named room, puzzle order, or distinctive Insurgence story element is imported.

## PTU and project-mechanics boundary

### Public PTU resource status

Source: official Pokémon Tabletop downloads and resources
https://pokemontabletop.com/downloads-and-resources/

The public PTU resource page identifies PTU 1.05 as the core downloadable system and warns users to learn the rules rather than treating automated tools as infallible. This supports the project's existing policy that PTU/Caelo source material and the designated Python oracle remain authoritative for mechanics.

Library operations are primarily overworld/institutional state. They do not need a new PTU mechanic merely because books contain information about Pokémon.

Do not infer:

- Pokémon Education rank from owning or borrowing books.
- Occult Education from reading folklore.
- General Education from library membership.
- Researcher Features from employment as a librarian.
- Skill Ranks from repeated visits.
- mechanical identification success from possession of a field guide.
- automatic translation from holding a multilingual edition.
- a combat bonus from consulting a battle manual.

### Caelo source check

A File Library search for the named PTU/Caelo corpus did not return the primary Caelo Player's Guide, Caelo rulebook/errata, character-creation documents, or Caelo Region Location & Encounter List in a reliably identifiable form during this run. The result set instead returned a prior research package and unrelated files.

Therefore Pass 130 does not claim any Caelo-specific rule about libraries, books, research access, education, literacy, reference work, or knowledge checks.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output is attributed to it.

## Library-science patterns worth transforming

### Work, expression, manifestation, item

Source: IFLA Library Reference Model
https://repository.ifla.org/rest/api/core/bitstreams/7d23aa55-1f85-490f-b500-6170285585a6/content

Source: earlier IFLA LRM PDF
https://www.ifla.org/wp-content/uploads/2019/05/assets/cataloguing/frbr-lrm/ifla-lrm-august-2017.pdf

IFLA distinguishes a conceptual work, its expressions, manifestations, and individual items. Ouros should not copy the terminology mechanically, but the separation is extremely useful.

Transformed Ouros model:

- `KNOWLEDGE_WORK`: the intellectual/content identity that persists across editions.
- `CONTENT_EXPRESSION`: a language, revision, adaptation, transcription, or other content-level realization.
- `PUBLICATION_EDITION`: a publishable/issued version with a particular date and production context.
- `LIBRARY_COPY`: one physical or controlled digital copy with its own condition, annotations, circulation, and provenance.

Why it matters:

A field guide published in Year 12 can be replaced by a Year 18 edition without deleting what Year 12 researchers believed. The same translation may appear in several printings. One copy can carry handwritten route notes while another clean copy of the same edition does not.

### Resource sharing

Source: IFLA overview of resource sharing systems
https://repository.ifla.org/bitstreams/6d621497-96df-444f-becf-e31ca96ee9dd/download

Reusable pattern:

Libraries can extend access by locating holdings elsewhere, making requests, routing physical or digital resources, and agreeing on what can be shared. The important system is request/fulfillment state, not any particular real-world code.

Ouros adaptation:

A small mountain branch can satisfy a research need by borrowing a field atlas from a coastal institute. The request can be approved while the copy is still elsewhere. Postal/Rail/Travel then move the actual item. The borrowing library does not become owner.

Guardrail:

`RESOURCE_SHARE_APPROVED` does not imply `COPY_RECEIVED`.

## Proposed systems derived from research

### Persistent bibliographic identity

The content hierarchy should survive reprints, translations, revised terminology, corrections, and damaged/lost copies.

Example:

`WORK: Birds of Meridian Basin`

- expression A: original Meridian-language text
- expression B: later translation
- edition 1: pre-rail route names
- edition 2: corrected taxonomy and new map
- copy 17: annotated by a field team, later returned water-damaged

The annotations belong to copy 17 unless deliberately published into a new content version.

### Holdings and availability are different

A library can own or steward five copies and have zero currently available because copies are loaned, under conservation, reserved, missing, or restricted.

Possible copy states:

`AVAILABLE`, `ON_LOAN`, `ON_HOLD_SHELF`, `IN_TRANSIT`, `REFERENCE_ONLY`, `REPAIR`, `CONSERVATION_HANDOFF`, `MISSING`, `WITHDRAWN`, `LOST`, `DIGITIZATION`, `RESTRICTED_BY_SCOPE`.

None of these states implies anything about the truth of the contents.

### Circulation should preserve history without becoming surveillance

A circulation event can record that a copy was loaned, renewed, returned, declared missing, found, or transferred between sites. Patron-level history should be private by default and retained only where the world design needs it.

Narrative principle:

A library can remember that copy 17 was water-damaged during a flood without exposing a lifelong public reading history for the person who had borrowed it.

### Reference service as a non-quest resolution engine

An important use of libraries is reducing unnecessary action.

Examples:

- a rumor about a closed road is shown to originate in an old guide;
- two apparently different ruins are revealed to be variant names for one site;
- a rare-species claim turns out to quote an obsolete classification;
- a festival route appears contradictory because one map predates a bridge;
- a supposed new prophecy is identified as a modern retelling of an older text.

Sometimes the best library outcome is that no expedition, fight, or crisis is needed.

### Mobile and small-branch libraries

A persistent world benefits from access outside major cities.

Possible forms:

- mobile road library;
- ferry library shelf or scheduled service;
- rail-linked deposit collection;
- seasonal mountain branch;
- school/community shared reading room;
- research-station deposit collection;
- traveling language/translation collection.

These create recurrent routes and schedules without requiring a giant building in every settlement.

### Access scopes

Public access need not mean every copy is freely circulating.

Possible scopes:

- `PUBLIC_STACKS`
- `REFERENCE_ROOM`
- `SUPERVISED_SPECIAL_COLLECTION`
- `INSTITUTIONAL_MEMBER`
- `RESEARCH_REQUEST`
- `TEMPORARY_EVENT_DISPLAY`
- `SENSITIVE_LOCATION_REDACTED`

Access scopes must connect to Credentials/Permissions where authority is actually required. Restricted access does not imply conspiracy or dangerous knowledge.

## Design guardrails

1. A book on a shelf does not create world truth.
2. A library owning a copy does not imply endorsement.
3. An old edition can remain historically useful after a new edition appears.
4. A missing checkout scan does not prove theft.
5. A returned copy does not prove it was read.
6. A borrowed copy does not prove the patron agreed with it.
7. A damaged copy does not mean the work is lost.
8. An annotation is not part of the authored text unless separately published.
9. Public availability does not imply language proficiency or literacy.
10. A library card does not imply citizenship, residency, age, class, faction, or ideology.
11. A sealed/restricted collection does not imply supernatural danger.
12. A copy transferred by interlibrary loan does not transfer ownership.
13. Minecraft bookshelves do not define authoritative holdings.
14. Destroying Minecraft blocks does not erase a work, catalog record, or circulation history.
15. Restoring a backup does not duplicate unique physical copies.
16. A digital scan is a derivative/access object, not the physical original.
17. A historical field guide cannot change current Pokémon mechanics.
18. A battle manual cannot grant a Move, Feature, Skill Rank, Ability, or tactical modifier without a verified PTU rule.

## Engine boundary for library-related encounters

Ordinary library use needs no AutoPTU dependency.

Mechanically rich incidents can depend on battle families, but only when those mechanics actually appear.

### Flooded Reading Annex Evacuation — intended full version

Premise:

A stormwater/freshwater incident threatens a lower reading annex. Patrons, staff, circulation carts, and a small number of wild Pokémon need safe routes while an unrelated confrontation complicates the evacuation.

Dependencies:

- targeting / footprints / range / LoS: VERIFIED when ordinary attacks occur.
- base movement legality: VERIFIED for static legal shifts.
- complete movement including interception / forced movement: BLOCKING for moving civilians, protection lanes, route interception, or displacement.
- action economy / initiative: VERIFIED.
- full turn / round lifecycle: PARTIAL if delayed or phase-specific effects are used.
- terrain / weather / hazards / zones / reactions: BLOCKING if water rises or creates tactical zones during battle.
- AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `PROTECT_ROUTE`, `REACH_EXIT`.
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for semantic civilian/collection movement and dynamic environmental presentation.

Reduced version:

Resolve flood progression and patron evacuation in world state first. Move unique books and carts out of the combat space. Freeze a dry legal arena. AutoPTU resolves only the actual combatants. After battle, world state resolves condition, circulation, and recovery.

### Mobile Library Chokepoint — intended full version

Premise:

A traveling library is stranded on a route during a regional service day. The narrative objective is to restore passage without treating the vehicle or its books as combatants.

Full dependencies:

- complete movement / interception: BLOCKING for escort and route-clearing movement.
- AI tactical policy: BLOCKING for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT_VEHICLE`.
- adapter/playback: BLOCKING for moving route objectives.
- environment family: only required if the authored version includes mechanically real weather/terrain/hazard behavior.

Reduced version:

Park and secure the vehicle outside the grid. Staff remain in world state. If confrontation remains, run a static battle at the chokepoint, then reopen the route through Travel/Road/Rail state afterward.

### Reading Courtyard Wildlife Intrusion — intended full version

Premise:

A recurring urban-wildlife group enters a library courtyard during a crowded period. The preferred outcome may be withdrawal rather than KO.

Full dependencies:

- complete movement: BLOCKING for withdrawal paths and crowd separation.
- AI tactical policy: BLOCKING for `WITHDRAW`, `REACH_EXIT`, `AVOID_CIVILIANS`.
- adapter/playback: BLOCKING for civilians and semantic withdrawal.

Reduced version:

Evacuate patrons in world state. Give the wild Pokémon an out-of-combat withdrawal opportunity. Only if an independent combat conflict remains does AutoPTU open a static arena.

### Reference Desk Misinformation Case — no combat dependency

A public rumor points toward a supposedly new dangerous site. Reference work shows that the location name changed decades ago and the warning describes an already-resolved event. The correct resolution can be updating public information and closing the case without a battle or field expedition.

## Live engine evidence inspected for Pass 130

### AutoPTU-Java

Inspected head: `7de79dcd30b241d439724050fb24ee893a7c5c63`

Latest relevant commit: `Freeze forced movement instruction contract (#160)`.

The Java contract recognizes a language-neutral Push/Pull instruction and distance extracted from Move metadata. The code explicitly states that the contract does not move a combatant; later spatial resolution must execute the displacement.

Therefore complete movement remains BLOCKING. This is exactly the kind of representative-mechanic boundary the narrative repository must not overstate.

### AutoPTU Python

Inspected head: `99ba07ea47b8896d96bd37f6c06cffb8695f69bb`

Latest visible change is Career regression coverage proving that a seventh owned Pokémon overflows to PC instead of replacing the active six. This is useful Career/persistence evidence but does not change the permanent tactical capability map.

## Source register

- Canalave Library, Bulbapedia: https://bulbapedia.bulbagarden.net/wiki/Canalave_Library
- Canalave City, Bulbapedia: https://bulbapedia.bulbagarden.net/wiki/Canalave_City
- Malie Library / Malie City, Bulbapedia: https://bulbapedia.bulbagarden.net/wiki/Malie_Library
- Pokémon Reborn Beryl Library: https://pokemon-reborn.fandom.com/wiki/Beryl_Library
- Pokémon Reborn Sanctum Key Sidequest: https://pokemon-reborn.fandom.com/wiki/Sanctum_Key_Sidequest
- Pokémon Insurgence Utira Library: https://wiki.p-insurgence.com/Utira_Library
- Official Pokémon Tabletop downloads/resources: https://pokemontabletop.com/downloads-and-resources/
- IFLA Library Reference Model: https://repository.ifla.org/rest/api/core/bitstreams/7d23aa55-1f85-490f-b500-6170285585a6/content
- IFLA resource-sharing overview: https://repository.ifla.org/bitstreams/6d621497-96df-444f-becf-e31ca96ee9dd/download
- AutoPTU-Java inspected read-only at `7de79dcd30b241d439724050fb24ee893a7c5c63`.
- AutoPTU inspected read-only at `99ba07ea47b8896d96bd37f6c06cffb8695f69bb`.

## Open questions left intentionally unresolved

- Which Ouros settlements begin with public libraries, reading rooms, deposit collections, or mobile service?
- Is there a regional/national catalog, or only local catalogs that become interoperable later?
- Which materials circulate and which remain reference-only?
- How private is borrowing history in each institution?
- Can clubs or player-founded settlements establish libraries?
- Who can impose access restrictions on sensitive ecological maps, clinical materials, or sacred/restricted texts?
- How do physical and digital library services coexist at the chosen technology level?
- Which languages and translations are available at campaign start?
- When does a specific copy become historically important enough to hand off to Archives or Museums?
- Does the project want exact copy counts for all resources, or exact identity only for rare/significant copies?
- What PTU/Caelo text, if any, governs research through books, general education, Pokémon Education, or library-related checks?

No answer above is promoted to canon by this pass.