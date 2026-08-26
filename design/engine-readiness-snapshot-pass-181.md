# Engine Readiness Snapshot — Pass 181

Status: ENGINE EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-26
Narrative scope: Pokémon vigilance, alarm signals and anti-predator behavior

## Read-only engine heads inspected

AutoPTU-Java head inspected:

`cbb57447a387734301b4c9fcc2737c1ecb9c5b66`

Latest inspected slice:

`Own intrinsic Accuracy CS in combatant profile (#218)`

This stores content-owned intrinsic Accuracy Combat Stage separately from mutable battle stages and tests that projection boundary. It is a narrow ownership/calculation improvement. It does not implement ecological vigilance, sentinel behavior, alarm propagation, false alarms, group risk knowledge, retreat AI or reinforcement calls.

AutoPTU Python head inspected:

`231c50e4f2e7c4c0442123b1ba2221b7d07384eb`

No evidence inspected in this pass promotes a permanent capability category.

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

A representative Accuracy-stage primitive, Status path, Ability hook, Move Special or reaction never promotes its whole family.

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions as a complete family
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

The current Java README still lists core combatant/grid battle state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, tactical AI and Craftics/Cobblemon integration as incomplete.

## Pass 181 mechanics boundary

Vigilance is world-state behavior unless an exact PTU mechanic is explicitly invoked.

Explicit prohibitions:

`lookout behavior -> Perception bonus`

`sentinel role -> Keen Eye / Illuminate`

`alarm call -> Intimidate`

`warning signal -> Flinch / Confused / Frightened / Status`

`mobbing -> Pack Mon`

`signal reception -> free reaction`

`collective warning -> shared Initiative`

`vigilance -> Accuracy or Evasion Combat Stage`

`SOS battle precedent -> reinforcement mechanic`

`noise masking -> Accuracy penalty`

`shelter-seeking -> forced movement`

`false alarm -> Guile failure or deception`

`predator-detection behavior -> Forewarn / Anticipation`

## Encounter dependency matrix

### Alarm Network at Cedar Meadow — FULL

Targeting / footprints / range / LoS: VERIFIED for battle actors.

Base movement legality: VERIFIED.

Complete movement: BLOCKING for dynamic withdrawal, crossing, interception and moving multiple non-hostile groups.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL when an exact Status is invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING if shelter, masking/noise areas or environmental pressure have tactical effects.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `WITHDRAW`, `SEEK_COVER`, `REJOIN_GROUP`, `AVOID_THREAT` and other non-KO goals.

Minecraft / Cobblemon / Craftics adapter/playback: BLOCKING.

REDUCED contract:

Resolve detection, alarm reception and wildlife withdrawal in world state. Remove non-combatants. If a hostile pressure remains, instantiate a static legal AutoPTU battle. No battle result decides whether the signal was accurate.

### False Alarm Corridor — FULL

Targeting / footprints / range / LoS: VERIFIED for any independent battle.

Base movement legality: VERIFIED.

Complete movement: BLOCKING for civilians/wildlife crossing, evacuation and withdrawal.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Lifecycle / damage / Status / Move / Ability / Item / Feature families: PARTIAL when invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING only if noise, barriers, debris or other conditions are actual tactical mechanics.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `AVOID_WILDLIFE`.

Adapter/playback: BLOCKING.

REDUCED contract:

Close the route, move civilians and wildlife through world state and investigate signal evidence outside combat. A later battle is independent.

### Mobbing at the Research Tower — FULL

Targeting / footprints / range / LoS: VERIFIED for an independent battle.

Base movement legality: VERIFIED.

Complete movement: BLOCKING for approach, disengagement, withdrawal and interception.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Lifecycle / damage / Status / Move / Ability / Item / Feature families: PARTIAL when invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING if tower damage, unstable ground or protected areas have tactical effects.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING because mobbing requires approach/harass/disengage behavior rather than universal KO seeking.

Adapter/playback: BLOCKING.

REDUCED contract:

Resolve the mobbing episode as behavioral world state, clear wildlife and preserve observations. If a separate hostile actor remains, run a static battle afterward.

### Which Signal Means Danger? — NON-COMBAT

No battle-engine capability is required.

Wild Collectives, Interspecies Ecology, Soundscapes, Passive Acoustics, Social Learning and Pass 181 compare evidence. `UNRESOLVED` is a legitimate outcome.

## Why existing battle systems are insufficient

Battle LoS answers a geometric legality question. It does not prove ecological detection.

AI legal-action infrastructure can enumerate legal choices. It does not choose realistic anti-predator goals.

Base movement legality can validate a Shift. It does not implement coordinated retreat, crossing, shelter selection or interception-aware escape behavior.

Accuracy/Evasion Combat Stage infrastructure is unrelated to ecological attentiveness unless an exact PTU rule explicitly connects them.

## Minecraft adapter boundary

Minecraft/Cobblemon may eventually render:

- an authored lookout posture;
- warning cries or gestures already established by world state;
- a collective moving toward shelter;
- a monitored observation site;
- an already-authored disturbance.

It must not derive:

- vigilance from head rotation;
- sentinel role from standing position;
- alarm truth from sound playback;
- threat identity from aggro target;
- collective knowledge from loaded entities;
- ecological fear from pathfinding;
- response reliability from animation counts;
- population change from despawn or withdrawal.

## Engine changes observed since Pass 180

The newest inspected Java commit is `cbb57447...`, which stores intrinsic Accuracy CS within the combatant stat profile and keeps it separate from mutable Combat Stages until effective Accuracy projection.

This is a useful ownership/calculation refinement. It does not affect the Pass 181 classification.

The inspected Python head is `231c50e4...`; no change inspected here warrants a readiness promotion.

## Unresolved mechanical questions

- whether Caelo changes Perception, Keen Eye, Illuminate, Forewarn, Anticipation, Intimidate, Pack Mon or warning-adjacent Features;
- whether PTU/Caelo defines any non-combat alarm, vigilance or group-warning procedure;
- whether future tactical AI supports non-hostile risk responses and collective withdrawal goals;
- whether future movement supports coordinated escape, interception and moving objectives;
- whether any future environment system models acoustic masking authoritatively;
- how Minecraft should display warning behavior without becoming its rules authority.

## Canon questions

- which Ouros species/populations possess authored warning repertoires;
- whether mixed-species warning networks exist;
- which persistent individuals have recurring lookout histories;
- which infrastructure/noise changes have altered warning behavior;
- which community interpretations are folklore versus supported behavioral function;
- which observation sites require disturbance limits;
- how much vigilance state may advance offline.

No answer above is established as canon by this snapshot.
