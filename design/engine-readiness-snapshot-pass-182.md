# Engine Readiness Snapshot — Pass 182

Status: IMPLEMENTATION READINESS SNAPSHOT
Date: 2026-08-26
Pass: 182

## Why this snapshot is different

Pass 182 begins the transition from implementation-aware worldbuilding to executable Ouros runtime slices.

The relevant question is no longer only whether AutoPTU can support a proposed battle. It is also whether persistent Ouros state can be materialized, interacted with, recovered after reload and handed to AutoPTU without Minecraft/Cobblemon/Craftics becoming a second rules engine.

The first concrete target is:

`implementation/vertical-slices/cedar-meadow-alarm-network-v1.yaml`

This is a REDUCED implementation of the existing Pass 181 encounter contract. It deliberately resolves ecological warning and withdrawal through authoritative world state and uses AutoPTU only for an optional independent static battle.

## Live read-only engine evidence

### AutoPTU-Java

Inspected head: `b35f09bbcc4246b1846e57c5c4f9bb5771d474e8`

Recent slices:
- `b35f09bb` materializes temporary Accuracy inputs from runtime state;
- `f280fc66` freezes the temporary Accuracy bonus contract;
- `cbb57447` makes the combatant profile own intrinsic Accuracy CS;
- prior slices project effective Accuracy/Evasion and route Combat Stage state through authoritative mutation/hooks.

This is useful progress in core calculations and runtime state ownership.

It does not prove:
- complete battle state;
- complete damage;
- full Status lifecycle;
- complete Move/Ability/Item/Trainer Feature registries;
- complete movement;
- terrain/hazard/reaction families;
- tactical AI;
- Minecraft/Cobblemon/Craftics integration.

The live README still states that AutoPTU-Java is not yet a Minecraft mod. It explicitly leaves core combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, tactical AI and the Craftics/Cobblemon adapter unfinished.

### AutoPTU Python

Inspected head: `7e6ce7c8138273f8d45180d192e84088b9f0986f`

The latest inspected change sanitizes persisted Pokémon progress state in Career. It does not change the tactical capability assessment used by this repository.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

### PARTIAL

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

No family is promoted by Pass 182.

## Cedar Meadow reduced slice

### World-runtime requirements

The scene requires a future Ouros/Cobblemon adapter to prove:

- stable persistent actor ID binding across entity materialization;
- explicit zone entry event delivered to server-owned scene state;
- server-authoritative scene revision and interaction validation;
- idempotent presentation commands;
- world-state writeback exactly once;
- recovery after chunk unload and server restart;
- optional AutoPTU battle request exactly once;
- authoritative AutoPTU result ingestion exactly once.

These requirements belong to the currently BLOCKING `Minecraft/Cobblemon/Craftics adapter/playback` family.

### Battle dependencies when no optional confrontation exists

None.

The base scene can execute observation, alarm-event presentation and ecological withdrawal without asking AutoPTU to simulate the withdrawal tactically.

This is intentional. A living-world scene is allowed to exist without combat.

### Optional static confrontation

If another authoritative world fact creates an independent hostile encounter after background wildlife has already withdrawn, the reduced scene may request a conventional static AutoPTU battle.

Required capability status:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- move-specific behavior — PARTIAL for exact Moves used;
- status lifecycle — PARTIAL if exact Status effects are used;
- abilities — PARTIAL if exact Abilities are used;
- items — PARTIAL if exact Items are used;
- Trainer Features/perks — PARTIAL if exact Features/perks are used.

The reduced battle must not require:
- group withdrawal inside the tactical grid;
- interception or forced movement;
- shelter/noise custom tactical zones;
- changing terrain/weather/hazards/reactions;
- non-hostile ecological tactical AI.

If those are required, the scene must remain suspended or use a different authored reduced path. The adapter must not emulate them.

## Full Pass 181 version remains blocked

`Alarm Network at Cedar Meadow` FULL still needs:

- complete movement for dynamic withdrawal, crossing and interception;
- terrain/weather/hazards/zones/reactions if shelter/noise/environment has tactical effect;
- AI tactical policy for `WITHDRAW`, `SEEK_COVER`, `REJOIN_GROUP` and `AVOID_THREAT` behavior;
- Minecraft/Cobblemon/Craftics adapter/playback.

The implementation slice does not pretend these dependencies disappeared. It moves the ecological process outside battle in a declared, persistent and testable way.

## Adapter acceptance gates introduced by Pass 182

The adapter family must not become VERIFIED merely because a Pokémon can be spawned or a dialogue can appear.

At minimum, a vertical slice must prove:

1. Persistent identity survives unload/reload.
2. Server-owned world state, not Minecraft entity state, chooses the scene transition.
3. Duplicate interactions do not duplicate consequences.
4. Server restart reconstructs current presentation from committed state.
5. A battle handoff is idempotent.
6. Minecraft does not calculate PTU legality or results.
7. AutoPTU result ingestion is idempotent.
8. Scene completion writes Chronicle/world state exactly once.
9. Unsupported PTU families are not recreated as adapter-side shortcuts.
10. The same scenario has deterministic server-side transition tests independent of rendering.

Passing one slice establishes one adapter vertical slice. It does not establish the complete adapter family.

## Implementation priority after Pass 182

The next implementation work should prefer existing researched scenarios that exercise one new runtime primitive at a time.

High-value sequence:

- persistent actor materialization + identity binding;
- zone/callback-triggered scene state;
- dialogue/interaction request validation;
- scheduled/offline process transition;
- block/passage presentation driven by authoritative challenge state;
- static AutoPTU battle request/result ingestion;
- semantic battle-event playback;
- only later, dynamic actor path playback and richer tactical objectives.

This order can make the world visibly persistent before complete tactical movement and AI policy exist.

## Canon boundary

`Cedar Meadow` remains NON-CANON.

Pass 182 proves an implementation shape, not a lore decision. A later canon-approved location, population, NPC or institution can instantiate the same runtime schema without changing its authority boundaries.

## Unresolved implementation questions

- exact Cobblemon version and loader;
- exact Craftics runtime/API expected by the project;
- module/repository that will own the Ouros scene service;
- storage technology for scene/world-process state;
- authoritative mapping between `pokemon_entity_id`, Cobblemon Pokémon identity and transient `PokemonEntity` UUID;
- networking format for scene revisions and interaction requests;
- scene data loader and schema validation;
- dialogue-key integration;
- battle-session reconnect semantics;
- adapter-side animation/path playback primitives;
- how Minecraft world edits are reconciled when chunks were edited externally while a scene was unloaded.

None should be solved by silently moving PTU or narrative authority into Minecraft.