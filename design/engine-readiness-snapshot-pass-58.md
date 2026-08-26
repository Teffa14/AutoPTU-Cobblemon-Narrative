# Engine Readiness Snapshot — Pass 58

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`55cd963b2eda46715b6aba3d1c2579ae1b75b501` — Freeze Focused Training and Chronicler Accuracy contracts (#221).

This commit freezes helper ownership and behavior contracts around Accuracy-affecting Focused Training and Chronicler behavior. Together with the preceding Accuracy/Evasion and seven-Combat-Stage work, it provides stronger evidence for the already-verified calculation/state-input slice. It does not establish forced movement, terrain, reactions, complete status/damage lifecycle, full Move/Ability/Item/Trainer Feature registries, tactical AI policy or Minecraft playback.

The AutoPTU-Java README remains controlling category-level evidence. It still explicitly lists as unfinished: core combatant/grid state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, hook registries, full BattleSpec->BattleTranscript parity, AI scoring/policy and Craftics/Cobblemon adapter.

Newest inspected Python AutoPTU commit:

`7c4edba551cc57a51514f7cb43a75745db422837` — Career: keep automatic training progress authoritative (#152).

This hardens persisted training-progress input handling while preserving canonical training behavior. It does not add Java tactical capability families.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No Pass-58 evidence justifies promoting a category.

## Facility-state non-inference gates

A facility observation does not prove a technical cause.

A physically repaired asset does not automatically become fully operational.

A closure does not prove structural damage; staffing, utilities, access, supply or verification may be the actual dependency.

A temporary mitigation does not resolve the underlying fault.

A completed work order does not establish legal inspection, building-code compliance, property ownership, contractor licensing, warranty status or negligence.

A Pokémon’s species or type does not establish construction/maintenance capability.

Minecraft block state must not become authoritative structural-damage or repair logic.

## Encounter review — Active Worksite Collapse

Intended version may require:
- dynamic safe/unsafe routing;
- workers or other noncombatants evacuating;
- changing blocked tiles;
- debris/equipment hazards or zones;
- push/knockback/forced-displacement consequences;
- interception/protection behavior;
- objective-aware withdrawal/protection AI;
- Minecraft playback of worksite state.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate all workers/noncombatants in narrative state before battle. Close the unstable portion of the site outside tactical resolution. Freeze safe geometry and instantiate only legal combatants on a static arena. Do not model collapse progression, debris hazards, destructible supports or changing safe routes. The authoritative AutoPTU result determines whether maintenance resumes, remains suspended or triggers another assessment.

## Encounter review — Closed Utility Room Containment

Intended version may require:
- narrow route handling;
- containment/escape objective logic;
- protected equipment/zones;
- forced displacement;
- reactions/interception;
- AI that values escape/containment/equipment avoidance;
- adapter playback of service shutdown and restoration.

Dependency state remains the same category map above. The richest intended behavior is blocked specifically by complete movement, terrain/hazards/zones/reactions, tactical AI and adapter/playback. Any selected status, Move, Ability, Item or Trainer Feature must also be validated individually while those families remain PARTIAL.

Reduced version:

Shut down the relevant facility service in narrative state, remove noncombatants and dynamic equipment interactions, freeze room geometry or use an adjacent static arena, and resolve only legal combatants. After the battle, maintenance/verification state—not invented combat-object rules—determines whether the service can return.

## Noncombat review — Recurring Fault Review

This concept can run now because it primarily reads and writes narrative evidence/world state:
- current observations;
- prior fault records;
- work orders;
- verification results;
- material provenance;
- staffing/service dependencies;
- route/utility/environmental state where actually recorded;
- public/institutional records.

It must keep symptom, hypothesis, diagnosis, public belief and canonical cause separate.

A fully embodied inspection/worksite loop in Minecraft still depends on adapter/playback support, but the authoritative narrative state can exist before that integration.

## Pass-58 outcome

Facility maintenance is safest to advance now through coarse condition/operational states, traceable faults, dependency-led work orders, temporary mitigations, service relocation, visible worksite overlays, verification, reopening and persistent maintenance history.

Mechanically rich worksite incidents should retain reduced static versions until complete movement, hazards/reactions, tactical AI and Minecraft/Cobblemon/Craftics playback become verified.

Capability classifications remain unchanged from Pass 57.