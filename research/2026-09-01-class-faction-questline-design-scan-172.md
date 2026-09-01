# Class & Faction Questline Design Scan — Pass 172

Status: RESEARCH / PROVENANCE. Nothing in this file is canon by itself.

Date: 2026-09-01

## Research question

How should Ouros turn its broad world-state research into long-form PTU class questlines and faction questlines while supporting up to four current classes, future respecs, cross-class convergence and strict separation between narrative history and mechanical authority?

## Internal baseline inspected

- Narrative repository main at Pass 171.
- Existing campaign convergence architecture.
- Existing world-state layers and proposals through Pass 171.
- Read-only PTU oracle catalog: 69 Trainer Classes.
- Read-only Trainer Class Validation: 61 classes currently listed with missing mechanics, 23 ambiguous unlockable OR branches, and no explicit multi-class mentions in that validation artifact.
- Current AutoPTU-Java main and recent movement-parity commits.

The class catalog is therefore treated as the complete class-coverage backlog, while implementation readiness must be evaluated separately from narrative coverage.

## Source pattern 1 — World of Warcraft Legion Class Hall campaigns

Source: Wowhead, Class Hall Campaign and Class Hall Mission Guide.

Reusable high-level lessons:

- each class receives a distinct identity-focused campaign;
- a class campaign can share a global world threat without becoming a duplicate of the global campaign;
- the class has a recognizable institutional/home-base context;
- recurring champions and class-linked NPCs create continuity;
- class progression is expressed through a sequence of responsibilities, relationships and escalating access;
- later global content can reconnect to class infrastructure without requiring the class campaign to own the whole world plot.

Do not copy:

- Legion, Order Hall names, artifacts, champions, quests, titles, locations, reward structures or class-specific plots.

Ouros transformation:

- use each PTU class as a perspective on shared world pressures;
- give each class recurring mentor/rival/peer networks and institutions where appropriate;
- allow a class line to intersect a global arc but retain class-specific stakes and methods;
- avoid making a dedicated physical headquarters mandatory for classes that are better represented by itinerant, informal, spiritual, ecological or personal networks.

## Source pattern 2 — Pokémon Ranger: Shadows of Almia

Sources: Bulbapedia Ranger Mission, Ranger Quest, Ranger Union and walkthrough material.

Reusable high-level lessons:

- an institution can combine formal missions with optional local quests;
- player status inside the organization changes which responsibilities become available;
- local citizen problems can coexist with a larger institutional threat;
- ordinary service work, rescue, investigation, study and crisis response can all reinforce one professional identity;
- recurring staff and headquarters meetings create continuity between field episodes;
- class/profession identity is reinforced by what the organization asks the player to do, not only by combat rewards.

Do not copy:

- Ranger Union plot, Team Dim Sun, named characters, specific missions, gems, bosses or captures.

Ouros transformation:

- class arcs should mix major authored episodes with smaller local requests when the class fantasy supports service work;
- profession-like PTU classes can have institutions that react to prior missions and trust the player with different kinds of work;
- faction progression should change access and responsibility without automatically changing PTU mechanics.

## Source pattern 3 — Pokémon Mystery Dungeon guild/exploration teams

Sources: Bulbapedia Mystery Dungeon Explorers material, team/guild descriptions and explorer guide.

Reusable high-level lessons:

- a guild can give a repeatable activity loop while a personal mystery advances in parallel;
- team identity can have a personal goal distinct from the guild's institutional goals;
- everyday assignments build relationships and familiarity before major plot convergence;
- recurring guild members can become a social ensemble with their own pressures and reactions;
- a personal artifact/question can stay relevant across many unrelated assignments before converging with the main arc.

Do not copy:

- Wigglytuff's Guild, Relic Fragment, Time Gears, Team Skull, temporal crisis, named characters or dungeon plots.

Ouros transformation:

- faction membership and class identity should generate repeatable but stateful activity while longer personal threads mature;
- recurring minor assignments should feed relationships, reputation, knowledge or world state rather than serve as filler;
- class questlines need not be linear chains. They can be persistent thread networks with prerequisites and convergence points.

## PTU class-catalog implications

The current oracle catalog explicitly contains 69 Trainer Classes. The catalog includes very different fantasies:

- trainer-development classes such as Ace Trainer and Mentor;
- profession/social classes such as Chef, Chronicler and Fashionista;
- capture/exploration classes such as Capture Specialist and Backpacker;
- performance classes such as Coordinator and Dancer;
- command/tactical classes such as Commander and Duelist;
- supernatural/elemental classes such as Channeler, Druid, Fire Bringer, Frost Touched and others;
- direct-combat classes such as Athlete, Berserker, Fortress, Marksman and related branches.

This diversity means a single universal quest grammar would flatten class identity.

Each class needs its own narrative fantasy, but all class lines should compile into the same shared world-state architecture.

## Multi-class/respec design lesson

The narrative system must not equate identity history with the current build.

Required separation:

- what classes the character currently owns mechanically;
- what classes they owned historically;
- which class-linked institutions know them;
- which class arcs they entered;
- which quest decisions already happened;
- which class-specific knowledge they acquired;
- which mechanical actions remain legal after a respec.

A respec changes current mechanical authority. It does not erase causal history.

This supports characters with up to four simultaneous classes and later class reorganization without retconning NPC memory or world consequences.

## Questline topology recommendation

Use five connected layers:

1. WORLD ARC — persistent regional/global pressure.
2. FACTION ARC — how an organization responds to that pressure and its own internal problems.
3. CLASS ARC — how a discipline/profession/fantasy intersects the world.
4. CHARACTER THREAD — the specific player's relationships, choices and history.
5. QUEST EPISODE — the playable local unit.

A quest episode may advance more than one layer.

Example abstract pattern:

A watershed becomes unstable.

- a Druid line investigates ecological relationships;
- a Researcher line studies evidence and competing explanations;
- a Survivalist line maps safe access and field logistics;
- a Chef line deals with ingredient scarcity and replacement traditions;
- a Commander line coordinates a multi-settlement response;
- a Chronicler line finds earlier records of similar change;
- relevant factions disagree about intervention.

These should reference one watershed state, not six parallel copies.

## Class questline content requirements

For each class, future research should produce:

- fantasy statement;
- class-specific moral/technical tensions;
- natural institutions/factions;
- mentor archetypes;
- peer archetypes;
- rival archetypes;
- novice-stage hooks;
- competence-stage responsibilities;
- advanced-stage dilemmas;
- long-term legacy question;
- recurring activity lanes;
- shared-world intersection tags;
- at least one faction conflict;
- at least one cross-class cooperation edge;
- at least one cross-class tension edge;
- possible noncombat episodes;
- possible combat episodes;
- exact engine dependencies for combat episodes;
- reduced versions where full mechanics are unavailable.

## Faction questline content requirements

Major factions should have:

- public mandate;
- internal constituencies;
- resource dependencies;
- institutional memory;
- succession/change pressure;
- allies and rivals;
- class affinities;
- class tensions;
- membership and non-membership participation lanes;
- defection/exit/outsider paths where appropriate;
- consequences that continue if the player ignores them.

A player should not need to permanently join a faction to experience all meaningful interactions with it.

## Anti-patterns

Avoid:

- one isolated quest chain per class with no shared world impact;
- class quests that are only mechanical tutorials;
- every class receiving the same five quests with renamed NPCs;
- class completion permanently granting mechanics after respec;
- NPCs forgetting completed events because the class left the build;
- faction arcs frozen until the player engages;
- every faction having a headquarters, rank ladder and uniform by default;
- every class being forced into battle content;
- Minecraft/Cobblemon deciding class membership or quest outcome;
- class-specific world copies that diverge from canonical shared state.

## Research backlog generated by this scan

High priority:

1. Build the complete 69-class narrative matrix from the authoritative catalog.
2. Map each class against all existing Ouros research/design layers.
3. Identify which classes already have rich source support and which are under-researched.
4. Group classes into overlapping narrative clusters without merging their identities.
5. Build faction archetypes that create multi-class intersections.
6. Start authored class questlines from the strongest-supported clusters while continuing research for weak classes.
7. Track narrative coverage independently from engine implementation coverage.

## Engine note

Class quest research does not imply engine readiness.

A class quest may need any of the permanent capability families. For example:

- Channeler stories may eventually touch Intercept, Features, abilities and stateful communication assumptions;
- Commander stories may require Orders, lifecycle and tactical policy;
- Druid/elemental stories may require terrain/weather/hazards/zones/reactions;
- Marksman or Fortress stories may require move/feature-specific behavior and reactions;
- Capture Specialist stories may depend on exact capture mechanics and movement legality;
- Chef stories may depend on exact Item/Feature behavior if food mechanics enter battle.

Every encounter must therefore retain explicit capability classification and reduced variants.

## Provenance summary

External inspiration sources used this pass:

- Wowhead — Legion Class Hall Campaign / Mission Guide.
- Bulbapedia — Pokémon Ranger: Shadows of Almia missions, quests and Ranger Union structure.
- Bulbapedia — Pokémon Mystery Dungeon Explorers guild/exploration-team structures.

Project-authoritative mechanics source:

- Teffa14/AutoPTU `TRAINER_CLASS_CATALOG.md` and `TRAINER_CLASS_VALIDATION.md` at pinned oracle head `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

All external story material is used only for high-level design patterns.