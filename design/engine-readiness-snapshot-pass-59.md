# Engine Readiness Snapshot — Pass 59

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`20841745242df28ef2e6a5f0e6f593dbcdfb2547`

Latest inspected commit:

`Resolve START effects before autobattler decision window (#90)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/20841745242df28ef2e6a5f0e6f593dbcdfb2547

The commit routes combatant START effects through the lifecycle seam before the autobattler receives a decision window. It explicitly allows START-turn status, Ability and perk phase effects, preserves ordering from the Python oracle and consumes a pending status skip before returning control.

This materially strengthens evidence for:

- action economy / initiative;
- full turn / round lifecycle infrastructure;
- status timing infrastructure;
- Ability timing infrastructure;
- Trainer Feature/perk timing infrastructure.

It does not prove:

- complete lifecycle coverage;
- all statuses;
- all Abilities;
- all Trainer Features;
- broad reactions or interrupts;
- complete round rollover;
- full damage sequencing;
- terrain/hazard runtime;
- tactical AI;
- Minecraft playback.

The Java README continues to state that Python AutoPTU remains authoritative while the port is incomplete and lists the following broad areas as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/Ability/item/perk/Trainer Feature registries;
- semantic BattleSpec → BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent inspected Python commits remain Career-focused. No new Python tactical commit changes the permanent classification below.

Python remains the behavioral oracle for rule slices explicitly frozen into Java parity contracts.

## Permanent capability map

The classification stays conservative. One representative mechanic never promotes the entire family.

| Permanent capability family | Pass 59 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated targeting, areas, footprints, anchors and LoS coverage exist. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, movement costs, blockers and fit rules are covered. This is not complete movement. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement and broad reactions remain unfinished. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy primitives, crit probability and multiple modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, action budget, deterministic initiative, authoritative progress and combatant-turn advancement are directly evidenced. |
| full turn / round lifecycle | PARTIAL | START effects now resolve before the decision window, but full round/phase coverage and all dependent mechanics remain incomplete. |
| full stateful damage pipeline | PARTIAL | Multiple post-damage/RNG slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | START status effects and several specific status slices exist; full controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Calculation primitives and movement costs do not prove runtime terrain, hazards, dynamic zones or broad reactions. |
| move-specific behavior | PARTIAL | Selected contracts and behavior exist; the complete PTU Move library does not. |
| abilities | PARTIAL | Multiple Abilities and lifecycle hooks exist, including START timing support; full registry remains incomplete. |
| items | PARTIAL | Selected item slices exist; full catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure and selected Features exist; full catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal action generation/filtering is implemented. |
| AI tactical policy | BLOCKING | Scoring/policy remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core, not the Minecraft adapter. |

## Pass 59-specific overworld boundary

Architecture and built-environment persistence mostly belongs outside AutoPTU-Java.

Suggested non-battle blockers:

`OVERWORLD_STRUCTURE_VERSIONING = BLOCKING`

The server needs stable structure IDs and version history for geometry, use and condition.

`OVERWORLD_SETTLEMENT_MORPHOLOGY = BLOCKING`

The server needs a representation of districts, routes, public spaces and terrain-aware spatial grammar.

`OVERWORLD_BUILDING_CONDITION_AND_REUSE = BLOCKING`

Condition, adaptive reuse, repair and retained historic layers require persistent world-state authority.

`OVERWORLD_SPATIAL_SEMANTIC_MAP = BLOCKING`

Minecraft geometry needs semantic references such as entrance, corridor, room, stair, courtyard, roof and service zone without making block coordinates the only source of truth.

`OVERWORLD_STRUCTURE_TO_BATTLE_PROJECTION = BLOCKING`

A frozen structure version must be translated into legal tactical geometry before battle. Minecraft must not invent PTU cover, hazards or damage effects.

These blockers do not lower any battle-core category. They identify work outside the Java rules core.

## Why the newest START-effect slice does not promote lifecycle

The latest commit is significant because initiative advancement now resolves START effects before the AI can choose an action. This closes a real ordering gap.

The remaining lifecycle surface still includes:

- complete round rollover;
- all end/start round behavior;
- every status timing rule;
- every Ability/Feature phase trigger;
- reaction and interrupt windows;
- complete delayed-effect behavior;
- complete transcript parity;
- interaction with every stateful damage and movement rule.

`full turn / round lifecycle` remains PARTIAL.

## Encounter dependency review

### Old Arcade Firebreak

Full version needs:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement if debris or moving actors alter routes — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions for active fire, smoke or falling debris — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- structure versioning/projection — BLOCKING outside battle core.

Reduced version:

Evacuation and structural changes resolve before battle. AutoPTU receives one frozen static arena with fixed blockers. Fire/smoke remain narrative/overworld state and apply no invented PTU damage.

### Bellhouse Restoration Dispute

Full version may need:

- autonomous wild withdrawal/protection goals;
- dynamic room access;
- interactable renovation zones;
- tactical AI;
- adapter playback.

The full version is blocked mainly by objective-aware AI, dynamic zone support and Minecraft integration.

Reduced version:

Freeze open/closed rooms before battle. Keep construction equipment and noncombatant movement outside the grid. Use a standard legal encounter when conflict occurs.

### Underpass Conversion

Full version may need:

- multiple moving groups;
- route-control or exit objectives;
- interception/forced movement;
- dynamic zones;
- objective-aware tactical AI;
- Minecraft playback.

Those dependencies remain BLOCKING.

Reduced version:

Resolve commuter/wildlife corridor timing in world state before battle. If combat occurs, AutoPTU receives a static arena and normal combatants only.

## PTU / Caelo caution

Pass 59 does not create architecture mechanics.

No narrative building state may invent:

- falling damage;
- collapse damage;
- cover bonuses;
- urban terrain bonuses;
- climbing checks;
- jump distances;
- door-breaking rules;
- smoke effects;
- fire damage;
- structural HP;
- demolition actions;
- building-material resistances.

The project-supplied primary Caelo PDFs were not reliably retrievable in this automation runtime, so no new Caelo-specific building, urban-terrain or hazard rule is asserted.

## Evidence required for richer built-environment encounters

Battle-side:

- verified objective-state contracts for PROTECT / REACH_EXIT / CLEAR_ZONE or equivalents;
- complete forced movement/interception;
- broad terrain/hazard/zone/reaction contracts;
- tactical AI that understands spatial goals;
- authoritative adapter/playback.

Overworld-side:

- persistent structure IDs;
- geometry/version history;
- condition records;
- adaptive reuse projects;
- semantic room/entrance/circulation graph;
- access and accessibility integration;
- ecology links;
- archive/photo/map provenance;
- terrain-aware settlement generation;
- safe conversion from structure state to frozen battle projection.

## Snapshot conclusion

Pass 59 adds no reason to relax the permanent capability map.

The newest Java commit materially improves authoritative turn-start ordering. Rich architectural encounters are still primarily blocked by dynamic movement, hazards/zones, tactical AI and Minecraft integration.

Worldbuilding can advance now because structures, districts, morphology, adaptive reuse, condition and architectural history are persistent overworld concepts. Reduced encounters can freeze the current building version and use static battle geometry until the missing tactical families are verified.