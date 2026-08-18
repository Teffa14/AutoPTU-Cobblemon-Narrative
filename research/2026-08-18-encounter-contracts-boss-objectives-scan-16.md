# Encounter Contracts, Boss Objectives & Implementation Readiness — Research Pass 16

Status: research/provenance only. Nothing in this file is Ouros canon.

## Purpose

Earlier passes established persistent world state, mission grammar, dungeon memory, crises, institutions, ecology and formal battle records. This pass focuses on a different problem: mechanically ambitious encounters can be narratively excellent while still being impossible to run safely in the current Java/Minecraft stack.

The goal is to preserve ambitious worldbuilding without allowing the narrative layer to assume unfinished PTU engine families exist.

## Sources inspected

### Pokémon Tabletop United development commentary

Source: https://pokemontabletop.com/a-fresh-start-and-ptu-1-05-news/

The PTU team explicitly discussed the difficulties created by boss templates that act multiple times in one round, especially the interaction between repeated turns and Status Effects. They also described the need for dedicated mechanics that let players interact with bosses differently from ordinary enemies.

Reusable lesson:
- a boss with extra turns is not merely a normal combatant with more HP;
- status timing, action denial, damage-over-time and round boundaries become materially different;
- therefore a narrative boss contract must name lifecycle/status dependencies instead of hiding them inside prose.

### PTU first-encounter GM guidance

Source: https://pokemontable.com/ (discovery only; canonical public article used below)
Source used: https://pokemontabletop.com/gm-advice-your-first-ptu-session/

PTU encounter guidance emphasizes party size, number of active Pokémon, capture opportunities and simple motivations such as territorial behavior, protecting another Pokémon or recovering a stolen object.

Reusable lesson:
- an encounter can have a concrete objective and narrative cause without introducing a new combat subsystem;
- simple objectives are valuable reduced versions when the full set piece depends on unfinished engine families.

### Pokémon Sword/Shield Max Raid Battles

Sources:
- https://www.pokemon.com/us/strategy/pokemon-sword-and-pokemon-shield-max-raid-battle-tips
- https://swordshield.pokemon.com/en-au/gameplay/dynamax-powerful-pokemon/

Max Raids combine cooperative party composition with boss-specific barriers, unusual action patterns, ability/stat resets and failure conditions based on party knockouts.

Reusable high-level structures only:
- shared focus against one major threat;
- boss defense that changes encounter tempo;
- failure conditions that are not simply one Trainer losing one Pokémon;
- player support roles when direct offense is unavailable.

Do not import Dynamax, barriers, Max Moves, stat-reset rules or faint counters into PTU.

Implementation lesson:
Most of the interesting parts of this structure require full stateful damage, status/ability hooks, lifecycle semantics and often special objective logic. They therefore belong in FULL versions only until those families are verified.

### Pokémon Scarlet/Violet Tera Raid Battles

Source: https://www.nintendo.com/au/news-and-articles/new-details-revealed-for-pokemon-scarlet-and-pokemon-violet-including-tera/

Tera Raids use cooperative combat under a shared time limit and allow participants to act in a format distinct from ordinary turn order.

Reusable lesson:
A cooperative boss can create pressure through a shared objective clock, but a real-time or asynchronous action model must never be translated directly into PTU. In Ouros, any clock must advance through an explicit reviewed round/turn contract.

### Pokémon Legends: Z-A — Rogue Mega Evolution incidents

Sources:
- https://www.nintendo.com/au/news-and-articles/pack-your-bags-for-lumiose-city-a-new-action-packed-pokemon-adventure-is-finally-here/
- https://www.nintendo.com/au/news-and-articles/pokemon-unveils-new-details-for-pokemon-legends-z-a-pokemon-champions-and-more/

Public descriptions frame Rogue Mega Evolution as an incident to investigate and calm, not only a disconnected boss spawn.

Reusable lesson:
- investigation can precede the tactical confrontation;
- the important encounter can be one phase inside a larger civic/ecological incident;
- boss defeat need not be the only narrative success state if the governing game rules support alternatives.

Do not copy Rogue Mega Evolution incidents, Mega rules, named organizations, characters or rewards.

### Pokémon fangame discovery — field abilities and mixed battle scales

Source: https://www.eeveeexpo.com/completed-games/

Public project descriptions include games with overworld field abilities, exploration/puzzles and mixes of 1v1, 2v2, 3v3 and boss encounters.

Reusable lesson:
Dungeon identity can come from traversal and field interaction before combat. This reduces the pressure to make every room depend on exotic tactical mechanics.

### PTR2e boss documentation — inspiration only, not PTU rules

Source: https://2e.ptr.wiki/en/rules/bosses

This separate system documents sponge, break, puzzle and command-style bosses. It is not a PTU 1.05 rules source and must never be used to validate Ouros mechanics.

Reusable abstract lesson:
Boss archetypes are easier to author when the designer identifies what players are supposed to learn or manipulate: raw endurance, a vulnerability window, a spatial/puzzle condition, or supporting units.

Ouros should keep this at the level of encounter intent and dependency declaration. No PTR2e boss traits, clocks, DR/RES values, delay mechanics or special actions are imported.

### Recent AI/game-agent research

Source: https://arxiv.org/abs/2608.09902

The DSLE benchmark intentionally samples boss encounters with different structural demands: straightforward melee, constrained space, environmental hazard, multi-target pressure and fast high-pressure combat. Results differ drastically across encounter types.

Reusable lesson:
A single successful representative battle test does not prove general battle readiness. Encounter portfolios need coverage by capability family and archetype.

Source: https://arxiv.org/abs/2603.15563

The PokeAgent Challenge emphasizes partial observability, long-horizon reasoning and strategic adaptation.

Reusable lesson:
Legal-action generation and tactical policy are separate capabilities. An engine can enumerate legal choices before it can make good decisions among them.

## Internal project evidence inspected

### AutoPTU-Java

Current README and test tree were inspected from `main`.

The README reports completed targeting, base movement, calculations, action economy/initiative and deterministic legal-action generation. It still lists full damage, status controller, terrain/hazards/forced movement/reactions, hook registries, AI scoring and Minecraft adapter work as unfinished.

The current test tree additionally contains representative runtime/parity tests for:
- battle round control and round lifecycle;
- authoritative move execution;
- move frequency;
- Burn;
- damage modifiers;
- evasion/accuracy state;
- legal action-space generation.

This is meaningful progress but must not be promoted into whole-category completion.

### Python AutoPTU

`Teffa14/AutoPTU` remains the source oracle while the Java port is incomplete. Its current repository head remains ahead in breadth of mechanics. Python behavior can prove that a rule exists in the oracle; it cannot prove that Java or Minecraft can execute/play it back yet.

### Existing narrative repository

The existing repository already has mission blocks such as BATTLE, ESCORT, PROTECT, RESCUE and SURVIVE, plus formal challenge contracts and objective-profile references. This pass therefore does not create another mission grammar. It adds a mechanical readiness contract beneath those existing narrative structures.

## Permanent capability taxonomy for encounter authoring

Every mechanically meaningful encounter should classify dependencies using exactly these project categories:

1. targeting/footprints/range/LoS
2. base movement legality
3. complete movement including push/pull/knockback/interception/forced movement
4. core calculations
5. action economy/initiative
6. full turn/round lifecycle
7. full stateful damage pipeline
8. status lifecycle
9. terrain/weather/hazards/zones/reactions
10. move-specific behavior
11. abilities
12. items
13. Trainer Features/perks
14. AI legal-action infrastructure
15. AI tactical policy
16. Minecraft/Cobblemon/Craftics adapter/playback support

## Live readiness snapshot

This snapshot is intentionally conservative and is about production readiness for mechanically dependent Ouros encounters, not whether some representative method exists somewhere.

| Capability family | Java readiness | Evidence / reason |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | README marks targeting/range/areas/footprints/anchors/LoS complete; legal action-space tests exist. |
| base movement legality | VERIFIED | Shift and Jump legality, movement modes, terrain costs/blockers and fit rules are documented as complete. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | README explicitly lists forced movement and reactions among unported work. |
| core calculations | VERIFIED | PTU tables, stages, accuracy, combat stats, type effectiveness and calculation primitives are implemented/tested. |
| action economy/initiative | VERIFIED | Typed phases, action budget and initiative variants are implemented. |
| full turn/round lifecycle | PARTIAL | Round/lifecycle parity tests exist, but full hook/status/terrain interactions across lifecycle are not complete. |
| full stateful damage pipeline | PARTIAL | Damage resolution and authoritative modifier slices exist; README still says full damage pipeline remains to port. |
| status lifecycle | PARTIAL | Burn and status-skip/runtime slices exist; general status controller remains unfinished. |
| terrain/weather/hazards/zones/reactions | BLOCKING | Family is explicitly listed as future port work. Calculation support for weather DB is not the same as battlefield weather/terrain lifecycle. |
| move-specific behavior | PARTIAL | Authoritative move and frequency slices exist; full move hook registry/library is unfinished. |
| abilities | PARTIAL | Narrow ability-like modifiers are represented in existing calculations/runtime, but the general ability hook registry remains unfinished. |
| items | BLOCKING | General item hook registry is explicitly unfinished; ownership/reservation outside battle does not prove battle item behavior. |
| Trainer Features/perks | BLOCKING | A semantic event type does not prove Feature rules; Trainer Feature/perk hook registries remain unfinished. |
| AI legal-action infrastructure | VERIFIED | Deterministic BattleChoice/action-space contract is documented and parity tested. |
| AI tactical policy | BLOCKING | README explicitly leaves scoring/policy over legal choices unfinished. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | README explicitly defers adapter work until a parity-safe vertical slice exists. |

## Design consequences

A new encounter may be narratively approved while still being mechanically blocked.

The correct response is not to delete the concept and not to fake the missing rule. Store both:
- FULL: intended final encounter;
- REDUCED: a version using only verified families while preserving the same narrative premise.

Examples:

A collapsing bridge boss may ultimately use forced movement and reaction windows. A reduced version can preserve the collapsing-bridge story by using static blocked tiles between rounds and ordinary legal movement, provided the round transition itself is reviewed.

A storm guardian may ultimately create moving weather zones. A reduced version can use a visually stormy arena with no tactical weather modifier and rely on verified targeting/movement/core combat.

A rescue battle may ultimately support enemies pushing civilians, interception and protection reactions. A reduced version can place civilians outside the battle grid and make the encounter objective narratively "clear the path" while AutoPTU resolves a standard legal combat.

## Anti-false-completion rule

One passing mechanic never upgrades a whole capability family.

Examples:
- Burn support does not mean status lifecycle is complete.
- weather damage-base calculation does not mean weather battlefield state exists.
- one TrainerFeatureEvent does not mean Trainer Features are implemented.
- one move runtime test does not mean the move library is complete.
- Shift/Jump movement does not mean forced movement/interception exists.
- legal action enumeration does not mean tactical AI exists.

## Source-use boundary

External games and other tabletop systems are used only for abstract encounter structures. Exact rules, numbers, boss traits, barriers, shields, timers, scripts, named characters and distinctive plot sequences are not copied.

PTU/Caelo and the Python oracle remain the mechanical authority; AutoPTU-Java live tests determine what is currently runnable in the target Java core; Minecraft/Cobblemon/Craftics readiness must be proven separately.