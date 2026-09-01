# Engine Readiness Snapshot — Pass 177

Status: READ-ONLY EVIDENCE SNAPSHOT
Date: 2026-09-01

Purpose: freeze the engine evidence used by pass 177 narrative concepts. This document does not modify or grade engine repositories beyond evidence visible at their current heads.

## AutoPTU-Java

Inspected head: `8fd11090b31d413072808662c01fc2e2316420ff`

Newest relevant commit: `Compose content-backed forced movement prevention (#314)`.

Observed evidence:
- declarative composite forced-movement prevention rules can depend on required Trainer Features plus capabilities;
- post-hit forced movement consults this content-backed prevention path;
- dedicated runtime tests and parity workflow coverage were added;
- this extends the previously demonstrated generic candidate-step/Shadow Tag forced-movement work.

What this proves:
- one more real forced-movement composition path is covered;
- Trainer Feature + capability content can participate in forced-movement prevention through a declarative core rule;
- post-hit forced movement has additional tested prevention semantics.

What this does not prove:
- the complete movement family;
- every Push/Pull/Knockback variant;
- all interception behavior;
- collision/partial-stop parity across all move/content combinations;
- all Trainer Features/perks;
- all status/terrain/reaction interactions.

## AutoPTU Python

Last visible project head used by recent narrative snapshots: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Relevant source evidence inspected during this pass includes:
- Pokémon Education references in Trainer class/feature data;
- Telepath Trainer class/capability surfaces;
- Mindlock reference behavior affecting Telepathy and related effects;
- existing ability audit evidence for the battle Ability named Telepathy.

Narrative rule:
The existence of similarly named concepts does not make them interchangeable. A Trainer Telepath class/capability, the battle Ability Telepathy, Channeler-style communication and ordinary social interpretation must be resolved through their exact source definitions.

No write was made to AutoPTU.

## Minecraft/Cobblemon RPG adapter evidence

Recent read-only evidence inspected:
- `077167dbfc96b69a48a217f343f3a57aeda1b347` adds/captures an authoritative in-world graphical RPG scene through CI;
- `40ef2d4af9100d5ce5a1dbc8308a350482cffff2` provisions a persistent canonical Cedar field-notes quest object in the normal Overworld and gates objective progress to that exact server-owned physical object.

Narrative implication:
- physical authored evidence objects and visible scene verification are stronger than in earlier snapshots;
- low-risk archive/inscription quests can reasonably target server-owned physical objects as adapter work progresses;
- this still does not establish complete tactical playback parity.

## Permanent capability categories

### VERIFIED for current covered contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` means current audited contracts in that family are real. It does not mean every future content interaction is automatically covered.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

The newest forced-movement commit strengthens the first of these but does not promote it.

### BLOCKING as complete families when required by a design

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

The adapter now has meaningful physical-world and graphical evidence. It remains BLOCKING for concepts that require the complete battle playback family rather than those narrower verified presentation surfaces.

## Pass 177 encounter implications

Most new pass 177 concepts require no BattleSpec:
- archive comparison;
- transcription;
- interpretation revision;
- physical document retrieval;
- dock operational signals;
- field-notation crosswalks;
- actor knowledge propagation.

These can progress using world, quest, dialogue, archive, communications and physical-object surfaces.

`Signal Under Pressure` full version requires all permanent tactical families listed in its proposal, especially:
- complete movement;
- full lifecycle;
- full damage/status behavior for selected combatants;
- terrain/weather/hazards/zones/reactions;
- exact communication-related Trainer Feature/perk behavior;
- AI tactical policy;
- full adapter/playback.

Therefore full version status: BLOCKED.

Reduced version status: NARRATIVELY READY, subject to ordinary BattleSpec parity audit if a separate battle is selected. All interpretation happens outside combat and the battle cannot author semantic truth.

## Unresolved mechanical questions

1. Which exact PTU Features/Capabilities, if any, permit direct semantic communication with Pokémon under the project's chosen source priority?
2. Which non-combat skill checks are authoritative for deciphering unfamiliar human scripts, damaged records or field notation?
3. Does the Caelo source set define regional languages, scripts, literacy assumptions or translation conventions that must override generic proposals?
4. Which Trainer Features/perks involved in communication already have Java parity contracts?
5. When can a physical Minecraft quest object safely expose a transcription UI without duplicating canonical document state?

Until answered, narrative files must keep these points proposed/uncertain rather than infer mechanics.