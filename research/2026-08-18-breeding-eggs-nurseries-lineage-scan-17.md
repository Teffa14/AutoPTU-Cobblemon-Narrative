# Breeding, Eggs, Nurseries & Lineage — Research Pass 17

Status: research/provenance only. Nothing in this file is Ouros canon.

## Purpose

The existing Ouros research already covers care, welfare, social bonds, institutions, ecology, crafting, cases, travel, public memory and encounter implementation contracts. A repository-wide inspection found no dedicated treatment of breeding, Eggs, nurseries, hatcheries, juvenile care or lineage state.

This pass studies those subjects as worldbuilding systems rather than as a competitive-stat optimization loop.

The primary design question is:

How can an Egg or nursery create persistent stories about care, custody, ecology, mentorship, family history and community infrastructure without letting narrative generation invent PTU breeding outcomes?

## Sources inspected

### Pokémon Day Care / Nursery history

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Day_Care
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_breeding

Across the core games, Day Care and Nursery facilities have served different functions. Earlier Day Cares can raise deposited Pokémon and may produce Eggs when compatible Pokémon are left together. Later Nursery implementations separate breeding from passive leveling, while Scarlet/Violet moves Egg generation into the picnic system.

Reusable lesson:
- breeding does not need to be tied to one universal facility;
- care, training, Egg production and hatching can be different services;
- regions can express different cultural or institutional approaches to raising Pokémon;
- a world simulation should represent the purpose of a facility explicitly instead of assuming every ranch or clinic is also a breeding center.

Do not import game-specific fees, step counters, breeding percentages, IV systems or generation-specific inheritance mechanics into Ouros.

### Day Care as a social institution in animation and manga

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Day-Care_Couple
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Day_Care

Pokémon media repeatedly depicts Day Cares as staffed places with caretakers, families, specialist roles and links to local communities. Some animated examples care for Eggs before they become first partners; others care for Trainers' Pokémon. Pokémon Adventures also uses a Day Care as a place with history, labor and personal relationships rather than only a menu service.

Reusable lesson:
- nursery staff can be recurring NPCs with expertise and institutional memory;
- a nursery can be a civic node connected to first-partner programs, research, welfare, adoption, transport and education;
- the facility can have obligations to both Pokémon and people.

Do not copy named caretakers, locations, plot events or distinctive character histories.

### Pokémon Tabletop United public material

Sources:
- https://pokemontabletop.com/basic-ptu-tools-and-utilities/
- https://forums.giantitp.com/showsinglepost.php?p=17012904&postcount=1
- https://forums.giantitp.com/archive/index.php/t-400537.html

The official PTU site notes breeder-oriented utilities for Egg Moves. Public PTU release discussions identify Hatcher as a supported Trainer specialization. This confirms that breeding and raising young Pokémon are intended character-facing activities in PTU rather than purely off-screen setting flavor.

Secondary rule mirrors consulted for discovery only:
- https://pturpg.wikidot.com/104%3Ahatcher
- https://pokemontabletop.fandom.com/wiki/Pok%C3%A9mon
- https://pokemontabletop.fandom.com/wiki/Pokemon_Tabletop_United_Pokedex
- https://anyflip.com/tcye/paot/basic/251-300

These mirrors describe PTU concepts such as Egg Groups, species Hatch Rates, inheritance lists, Hatcher features and Egg Warmers. They are not promoted as authoritative over the project's supplied PTU/Caelo files. Exact numbers, prerequisites, inheritance behavior and effects must be verified against those project files before implementation.

Reusable lesson:
- an Egg is mechanically meaningful state in PTU;
- parentage and species data can affect later legal move/inheritance state;
- hatching time can be a real campaign clock;
- a Trainer may specialize in raising Eggs and young Pokémon;
- narrative generation therefore must preserve provenance instead of inventing an Egg result after the fact.

### PTU community campaign evidence

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/valleytown-t6190-s310.html

A public PTU play thread shows Eggs being carried through ordinary campaign time and an Egg Warmer changing when one hatches. The Egg is not a disconnected crafting result; it travels with the party and can mature while other adventures continue.

Reusable lesson:
- hatching can be a background clock that intersects travel, downtime and future scenes;
- players can prepare for an expected hatch without turning every elapsed day into a dedicated quest;
- an Egg may become meaningful because of where it was carried and who cared for it before hatching.

Do not copy characters, dialogue or campaign events.

### Pokémon roleplay communities

Sources:
- https://www.gaiaonline.com/guilds/viewtopic.php?page=1&t=24629583
- https://www.gaiaonline.com/guilds/viewtopic.php?page=1&t=24629593
- https://forums.pokecharms.com/threads/the-everstone-daycare-discussion.21727/

Public roleplay communities have treated Day Cares as playable social spaces where Trainers leave Pokémon, caretakers interact with them, and breeding or adoption is coordinated between participants.

Reusable lesson:
- nurseries can support asynchronous multiplayer activity;
- responsibility for an Egg can involve more than one player or NPC;
- deposit, pickup, temporary care and adoption are different relationships and should not be collapsed into ownership;
- a Pokémon left at a facility can remain a character rather than disappearing into storage state.

Community-specific rules are not imported.

### Fangame and fan-system experiments

Sources:
- https://eeveeexpo.com/threads/2275/
- https://eeveeexpo.com/threads/6989/
- https://eeveeexpo.com/resources/662/
- https://eeveeexpo.com/threads/3081/

Pokémon Daycare, a fangame centered on operating a daycare, makes facility capacity, opening hours, staff/player attention, individual Pokémon preferences and expansion part of the game loop. Other fan projects separate breeding, hatching, training and storage or experiment with Egg generation to create more variety.

Reusable lesson:
- nursery capacity can be world state rather than an invisible infinite service;
- operating hours and staffing can create believable constraints without arbitrary gating;
- individual care preferences can add characterization when they are observed rather than procedurally invented as hidden mechanics;
- facility growth can connect directly to settlement progression.

Do not import hidden-ability chances, shiny rates, commercial prices, random generation rules, unique species, code or project-specific mechanics.

### Main-series breeding as long-term planning

Source:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_breeding

The main games use compatibility, Egg Groups, parent species and inherited properties to make breeding a planning activity. The exact implementation changes significantly across generations.

Reusable lesson:
The narrative layer should record inputs and provenance but must not calculate output using a homemade universal breeding algorithm. PTU/Caelo is the rules authority for Ouros.

## Internal project files inspected

The repository tree and README were reviewed before writing. Existing systems already cover:
- care facilities and medical privacy;
- custody and ownership uncertainty;
- social bonds and consent boundaries;
- wild populations and collective ecology;
- material provenance;
- travel clocks;
- settlement services;
- mentoring and clubs;
- public records and legacy;
- encounter capability contracts.

This pass therefore does not duplicate those systems. It introduces Egg/nursery-specific state that references them.

Repository search for `egg breeding nursery lineage hatch inheritance family daycare` returned no existing matching file content.

## Mechanical source boundary

The project's supplied PTU/Caelo corpus remains authoritative for:
- Egg Groups;
- breeding eligibility;
- parent contribution;
- offspring species determination;
- gender determination;
- Nature and Ability rules;
- inheritance lists and Egg Moves;
- hatch timing;
- Egg Warmer behavior;
- Hatcher/Breeder features;
- Tutor interactions;
- any Caelo changes or banned/limited options.

No narrative system may infer these mechanics from the main-series games or secondary PTU mirrors.

## Proposed information separation

Ouros should keep the following independent:

1. `egg_mechanical_state`
   - authoritative PTU/Caelo result or unresolved placeholder;

2. `egg_provenance`
   - where the Egg came from, known parent identifiers when legally established, source institution and creation/handoff events;

3. `egg_custody`
   - who is currently responsible for physically caring for it;

4. `egg_ownership_claim`
   - legal/social claim if the world has one; unresolved when law/canon has not established it;

5. `egg_care_history`
   - caregivers, facilities, travel and meaningful care events;

6. `public_story`
   - what other actors believe about the Egg;

7. `hatched_entity_id`
   - persistent Pokémon identity after authoritative hatching.

Custody must never silently become ownership. Parentage must never silently create an owner. Caring for an Egg must never guarantee a social bond after hatching.

## Nursery as world infrastructure

A nursery can expose state such as:

```yaml
nursery_id: null
location_id: null
service_profile: []
staff_ids: []
capacity_state: null
occupied_slots: []
egg_slots: []
young_pokemon_slots: []
care_specialties: []
operating_state: null
supply_dependencies: []
referral_links: []
public_programs: []
known_constraints: []
world_state_refs: []
```

Possible service profiles include care, hatching support, rehabilitation of juveniles, Trainer education, first-partner programs, temporary boarding and rules-authorized breeding support. These are not automatically bundled together.

## Juvenile Pokémon state

A recently hatched Pokémon can have persistent narrative state without receiving invented mechanical bonuses.

Useful state:
- hatch location;
- caregivers present;
- known parentage;
- first observed behaviors;
- first trusted locations;
- exposure to particular environments;
- social introductions;
- first battle only when/if that happens;
- training milestones generated from actual events.

Do not infer personality, loyalty, affection or battle aptitude from parentage.

## Lineage as provenance, not power ranking

Lineage can be useful for:
- identifying parent/offspring relationships when canonically known;
- tracking nursery records;
- recognizing historical breeding programs;
- tracing endangered or restored populations;
- understanding inheritance mechanics after PTU validation;
- public memory around notable Pokémon families;
- resolving custody or research questions.

Lineage should not become an automatic rarity hierarchy, purity score, value score or moral status.

## Ecological boundary

Wild reproduction is different from Trainer-directed breeding.

A nesting or nursery ground can support ecology stories about:
- seasonal arrival;
- nesting protection;
- food supply;
- predator pressure;
- habitat disturbance;
- juvenile dispersal;
- conservation or research.

The system should not generate explicit parentage for wild individuals unless observed or authored. A cluster of juveniles does not prove a family structure.

## Live AutoPTU-Java evidence inspected

Current Java evidence was re-checked after Pass 16 because the engine has advanced.

Recent commits inspected:
- `6570d95` — authoritative lifecycle hook registry;
- `046cc9f` — authoritative pre-damage move hooks and Mega Launcher parity slice;
- `1757163` — canonical held-item battle state and Pink Pearl parity-backed damage hook;
- `7b0fac3` — ordered authoritative damage hook registry;
- `63110d0` — authoritative round lifecycle;
- `1a75257` — authoritative move-frequency state;
- `b9a59a9` — authoritative movesets.

Important consequence:
The engine now has useful hook seams and representative ability/item slices, but a representative implementation does not prove the whole family.

## Current capability readiness for Pass 17 encounters

| Capability family | Readiness | Live evidence |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | Java README and action-space/runtime tests. |
| base movement legality | VERIFIED | Shift/Jump and movement-mode legality documented complete. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Still listed as unported; lifecycle hooks do not implement forced movement. |
| core calculations | VERIFIED | Core tables/stages/accuracy/stat resolution implemented. |
| action economy/initiative | VERIFIED | Typed phases, budgets and initiative variants exist. |
| full turn/round lifecycle | PARTIAL | Authoritative round controller and lifecycle registry exist; full status/terrain/temporary-effect population remains incomplete. |
| full stateful damage pipeline | PARTIAL | Ordered damage hooks and representative parity slices exist; full pipeline remains broader. |
| status lifecycle | PARTIAL | Burn/status-skip slices exist; full controller is not proven. |
| terrain/weather/hazards/zones/reactions | BLOCKING | Registry seams exist, but this capability family is not implemented as a complete battlefield system. |
| move-specific behavior | PARTIAL | Move execution/frequency and selected hooks exist; complete move library is not proven. |
| abilities | PARTIAL | Ability identity plus Mega Launcher is parity-backed; one ability family slice does not prove the registry/library. |
| items | PARTIAL | Pink Pearl and held-item state are parity-backed; one item does not prove general item behavior. |
| Trainer Features/perks | BLOCKING | Event/hook seams do not prove the Feature registry or rules. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action enumeration exists. |
| AI tactical policy | BLOCKING | Scoring/policy remains unfinished. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | Architecture/playback event seams exist, but target adapter remains unimplemented. |

## Encounter-design consequences

Breeding itself does not need to become a battle mechanic. When Egg/nursery stories intersect combat, the Egg should usually remain outside the tactical resolution unless PTU rules explicitly model the needed interaction.

Examples:
- protect a nursery from intruders: standard combat may be sufficient;
- physically intercept an attack aimed at an Egg carrier: depends on complete movement/reactions and possibly Trainer Features;
- battlefield heat/cold threatening incubation: depends on terrain/weather/hazard lifecycle and must not be improvised;
- an item changing hatch timing: must use the authoritative PTU item rule outside or alongside the battle system, never a Minecraft-only shortcut;
- parent Abilities affecting offspring: breeding resolution, not battle ability execution.

## Design lessons for Ouros

1. Eggs should persist as first-class world objects with provenance and custody.
2. Hatching should write into the Chronicle and create a persistent Pokémon entity.
3. A nursery should have finite, explainable capacity when the simulation needs constraints.
4. Different institutions may specialize in hatching, care, training, research or breeding support.
5. Parentage and inheritance are mechanical/legal facts, never vibes inferred by the generator.
6. Wild nesting ecology and Trainer-directed breeding remain separate systems.
7. Nursery staff can become recurring mentors, witnesses and community actors.
8. Hatching clocks should usually advance quietly and surface only when a meaningful event intersects them.
9. Player-authored care may matter narratively without creating hidden stat bonuses.
10. Lineage records can support history and ecology without creating a purity/value hierarchy.

## Copyright and originality boundary

No distinctive plot, character, dialogue, facility name, specific fangame system, game-specific inheritance formula or competitive breeding algorithm is copied. External works contribute only high-level structures and evidence that the activity can support long-form play.