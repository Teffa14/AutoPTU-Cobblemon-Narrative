# Engine Readiness Snapshot — Pass 184

Status: IMPLEMENTATION DEPENDENCY SNAPSHOT / NON-CANON
Date: 2026-08-26

## Purpose

This snapshot records the live battle/runtime evidence used by `implementation/vertical-slices/rotating-archive-hall-v1.yaml`. It does not promote a capability family from one representative implementation.

## Read-only engine heads inspected

AutoPTU-Java:
- head inspected: `b35f09bbcc4246b1846e57c5c4f9bb5771d474e8`;
- latest slice: materialize temporary Accuracy bonus inputs from runtime state;
- prior slices freeze temporary Accuracy bonus parity, intrinsic Accuracy CS ownership and effective Accuracy/Evasion projection.

AutoPTU Python:
- head inspected: `011ba46379255dc2175c08a73c08a7b7e6200176`;
- latest change bounds visible Career leaderboard names and explicitly leaves score, ranking and battle rules unchanged;
- no new battle-family evidence was found in that change.

## Live Java README boundary

At the inspected Java head, the repository still explicitly lists these as pending:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- remaining move/ability/item/perk/Trainer Feature hook registries;
- semantic event/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Therefore Pass 184 keeps the permanent capability map unchanged.

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
- terrain/weather/hazards/zones/reactions as a complete tactical family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

## Rotating Archive Hall — REDUCED v1

The base puzzle itself requires no battle engine.

It requires the future Ouros/Minecraft adapter to prove:

- server-owned persistent challenge state;
- interaction requests with observed revision;
- authoritative transition validation;
- idempotent block/model presentation;
- restart reconstruction;
- persistent shortcut state;
- stable operation IDs;
- optional BattleSpec request deduplication;
- exact-once battle-result ingestion.

Minecraft/Cobblemon/Craftics adapter/playback is therefore BLOCKING for running the scene in-game, even though the scene contract is now specified.

If the optional static battle begins:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement incl. forced/interception: BLOCKING but deliberately unused;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if invoked;
- terrain/weather/hazards/zones/reactions: BLOCKING but deliberately unused;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING; v1 must not require semantic non-KO objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

## Rotating Archive Hall — intended FULL version

A future version may rotate sections while actors are inside the tactical space, change legal routes between turns or create authored reaction windows.

That version depends directly on:

- complete movement including forced movement/interception: BLOCKING;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- AI tactical policy: BLOCKING when actors need `REACH_CONTROL`, `WITHDRAW`, `AVOID_ROTATION_PATH` or similar semantic goals;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL if the mechanism can cause battle damage;
- status lifecycle: PARTIAL if any exact Status interaction exists;
- move-specific behavior/abilities/items/Trainer Features: PARTIAL whenever an exact rule is offered as a solution or battle interaction.

No full-version mechanic is approximated through vanilla pistons, redstone, knockback or pathfinding.

## PTU/Caelo guardrails

Pass 184 does not add puzzle Skill DCs, trap damage, lockpicking rules or universal Move/Capability bypasses.

A future interaction such as Technology Education, Strength, Teleport, Groundshaper or a specific Move must have:

1. primary PTU/Caelo rules evidence;
2. an explicit legal interaction contract;
3. engine support for the exact effect when battle-state mutation is involved;
4. a world-state handoff that does not let Minecraft reinterpret the rule.

The complete primary Caelo corpus was not available as an invocable authoritative source during this pass, so no Caelo-specific puzzle mechanic is claimed.

## Promotion decision

No permanent capability family is promoted in Pass 184.

The meaningful progress is on the narrative-to-runtime side: a second machine-readable scene now specifies shared persistent mechanism state, concurrency, recovery, reset and battle handoff acceptance tests. This reduces ambiguity for the future adapter without pretending the adapter exists already.