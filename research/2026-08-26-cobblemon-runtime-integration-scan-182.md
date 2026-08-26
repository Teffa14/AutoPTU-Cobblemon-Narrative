# Cobblemon Runtime Integration Scan — Pass 182

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-08-26

## Why this pass exists

Ouros now has deep world-state and encounter design, but most of it is still implementation-facing prose rather than server-executable content. Pass 182 changes the research direction from adding another world domain to identifying concrete runtime seams that can make existing Ouros state visible and interactive inside Minecraft/Cobblemon while keeping PTU rules authoritative in AutoPTU-Java.

This note does not establish a Cobblemon version, modloader, canon scene, Pokémon behavior or PTU rule. It records current public implementation evidence that can guide adapter prototypes.

## Existing Ouros boundary

The narrative repository already requires Minecraft/Cobblemon/Craftics to present world state rather than decide PTU or challenge truth. `design/encounter-implementation-contracts.md` and `design/puzzles-dungeons-challenge-state-layer.md` already separate narrative premise, persistent state, battle handoff and adapter playback.

AutoPTU-Java's `docs/MINECRAFT_AUTOBATTLER_ARCHITECTURE.md` similarly requires stable combatant IDs, server authority, semantic battle events and a Minecraft adapter that never recalculates PTU results.

Pass 182 therefore does not replace those boundaries. It adds the missing executable scene/runtime layer between persistent Ouros state and the Minecraft/Cobblemon presentation.

## Public Cobblemon implementation evidence inspected

### CobblemonEvents provides server integration seams

Current public Cobblemon source exposes event observables for entity lifecycle and other runtime actions, including Pokémon entity save/load/save-to-world and entity spawn events.

Source:
- https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/api/events/CobblemonEvents.kt
- https://gitlab.com/cable-mc/cobblemon/-/tree/main/common/src/main/kotlin/com/cobblemon/mod/common/api/events

Design implication:
Ouros persistent identity should bind through explicit server-side lifecycle hooks. Chunk unload/reload must not create a new narrative Pokémon merely because a new Minecraft entity object exists.

### PokemonEntity is a real runtime object with lifecycle integration

Current public source shows `PokemonEntity` as Cobblemon's world entity for an instantiated Pokémon and includes event integration around entity load/save behavior.

Source:
- https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/entity/pokemon/PokemonEntity.kt

Design implication:
The future adapter can maintain `pokemon_entity_id <-> current PokemonEntity UUID/reference` without treating the transient Minecraft object as the canonical identity.

### Pokémon can be instantiated into the world without deriving narrative identity from spawning

Current `Pokemon.kt` source exposes world send-out paths that construct a `PokemonEntity`, position it server-side and add it to the level, with mutation hooks around creation.

Source:
- https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/pokemon/Pokemon.kt

Design implication:
An authored persistent Pokémon can be materialized for a scene from an existing Ouros identity. The adapter must not invert that relationship by treating every spawned entity as a new canonical actor.

### Entity callbacks are available

Cobblemon 1.7 developer notes describe `EntityCallbacks` on `NPCEntity` and `PokemonEntity`, including custom callback processing.

Source:
- https://gitlab.com/cable-mc/cobblemon/-/blob/main/changelogs/CHANGELOG-1.7.0.md

Design implication:
Interactions such as inspect, talk, acknowledge, request help, activate a station or advance a scene can be routed through server-owned callback identifiers rather than inferred from client animation or proximity.

### Dialogue is an API surface, not only static text

Cobblemon's public API tree contains dialogue support, and its development history records a dialogue API/data registry.

Sources:
- https://gitlab.com/cable-mc/cobblemon/-/tree/main/common/src/main/kotlin/com/cobblemon/mod/common/api
- https://gitlab.com/cable-mc/cobblemon/-/blob/24c34af8bf59034700d66265eabf359129ba0bfa/CHANGELOG.md

Design implication:
Ouros scenes should reference dialogue keys/nodes and state predicates. Final dialogue prose can remain content data while the runtime decides which node is currently legal.

## Runtime lessons for Ouros

### 1. Persistent actor identity must survive Minecraft lifecycle

Required direction:

`Ouros actor id -> binding record -> current Minecraft/Cobblemon entity reference`

Never:

`loaded PokemonEntity -> therefore a new persistent Ouros actor`

A binding can become temporarily `UNMATERIALIZED` while the underlying Ouros actor continues to exist.

### 2. Scene triggers need explicit server-owned causes

Useful trigger families include:
- player enters/leaves an authored zone;
- player interacts with an authored entity callback;
- persistent clock reaches an authored window;
- world-state predicate becomes true;
- a prior scene transition commits;
- an authoritative AutoPTU result returns;
- a server recovery/reload reconstructs an active scene.

Chunk load, entity aggro, despawn, vanilla death animation, client particles or redstone state must not silently become narrative truth.

### 3. A scene is a state machine, not a cutscene string

Minimum executable scene state needs:
- stable scene-instance ID;
- revision ID;
- participant bindings;
- current node;
- preconditions;
- accepted interaction requests;
- side effects;
- persistence policy;
- recovery policy;
- completion/failure outputs;
- optional battle handoff.

This supports interruptions, disconnects, multiplayer ordering and callbacks years later.

### 4. World effects need an idempotent command layer

Examples:
- materialize actor;
- dematerialize actor;
- set NPC dialogue state;
- open/close authored passage presentation;
- enable/disable an interaction proxy;
- publish/remove a notice;
- schedule a later scene transition;
- start a battle handoff;
- render a semantic battle event.

Every command needs a stable operation ID so reconnect/retry cannot spawn duplicate NPCs, duplicate rewards or repeat irreversible state changes.

### 5. Battle handoff must freeze the correct world state

A scene may request an AutoPTU battle, but it must first create a deterministic battle request containing persistent combatant IDs, arena transform/version and permitted world facts. AutoPTU returns authoritative results. The scene runtime consumes only fields declared by the handoff contract.

Minecraft/Cobblemon may render the battle; it does not infer victory from entity death or animation.

### 6. Offline progression needs explicit policy

A living world cannot depend on every entity being loaded. Each scene/world process therefore needs one of:
- `PAUSE_WHEN_UNLOADED`;
- `ADVANCE_BY_PERSISTENT_CLOCK`;
- `ADVANCE_BY_WORLD_SERVICE`;
- `RECOMPUTE_ON_MATERIALIZATION`.

The choice belongs to the authored system. Minecraft ticking is not automatically ecological or narrative time.

## First vertical-slice recommendation

Use an existing reduced encounter rather than inventing another lore domain. Pass 181's `Alarm Network at Cedar Meadow` is a useful first scene because it exercises persistent wild Pokémon identity, an authored world trigger, observable Pokémon behavior, player observation, a scene branch and an optional standard AutoPTU handoff while deliberately avoiding unsupported group tactical AI.

The first runtime version should not implement ecological warning behavior by emergent Minecraft AI. It should materialize authored persistent actors, play a server-authorized scene transition, persist what was actually observed and only open AutoPTU if an independent hostile encounter remains.

The accompanying machine-readable slice is `implementation/vertical-slices/cedar-meadow-alarm-network-v1.yaml`.

## What still requires source/prototype proof

- exact Cobblemon version and loader targeted by the project;
- stable Java/Kotlin signatures for entity callbacks in that version;
- whether dialogue nodes can be injected or referenced cleanly from the Ouros adapter;
- safe suspension/control of wild `PokemonEntity` navigation for authored scenes;
- server-owned path playback without allowing Minecraft pathfinding to decide PTU legality;
- persistence strategy for custom Ouros IDs across Cobblemon entity save/load;
- whether Craftics supplies suitable movement/render primitives for non-battle scene actors;
- final adapter module ownership and networking protocol.

No unsupported API behavior above is treated as proven until a source-pinned prototype/test verifies it.