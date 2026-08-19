# Engine Readiness Snapshot — Pass 22

Status: implementation evidence snapshot for narrative authoring. Not canon. AutoPTU-Java and AutoPTU are read-only inputs for this task.

Inspected date: 2026-08-19

## Live revisions inspected

Latest inspected AutoPTU-Java commit:

`62e6bef9e45b2e30febb48b4b6b73927c36328c0` — Bind delayed hits to canonical move execution inputs (#48)

Recent relevant Java evidence remains:

- `6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` — authoritative delayed-hit scheduling state and due/future partitioning with Python parity.
- `6c357d59061be2eae7bbbb85f401750acd7cf686` — payload-bearing temporary effect state and round-cleanup parity.
- `6570d95ac874bc26bc6bcc8ffe64d007bba37e34` — authoritative lifecycle hook registry.
- `046cc9f97ed8893e97674222f80789afcdf2cc7f` — pre-damage move hooks including a parity-backed Mega Launcher slice.
- `1757163fe793335e24a17769ee0fdfb78e87c754` — held-item state and parity-backed Pink Pearl damage hook.
- `7b0fac33d139d8bd72b265aa00bb939e895d5a9a` — ordered damage hook registry with representative Burn behavior.
- `63110d03ada723f41a671137a945e8f7b0316198` — authoritative round lifecycle controller with Python parity.

Latest inspected Python AutoPTU commit surfaced during this pass:

`403181e35c64ec165d49c2d68329a56609c39a15` — Career: trainer sprites and readable leaderboard names.

The Python repository remains the behavioral oracle for battle rules while the Java port is incomplete. Recent Career-mode commits do not by themselves change the battle capability classification below.

## Permanent capability classification

### VERIFIED

#### targeting/footprints/range/LoS

Canonical target anchors, direct/tile/Self/Field target handling, footprints, range and LoS have explicit action-space/test evidence.

#### base movement legality

Verified for the currently ported Shift/Jump legality slice, supported movement modes, terrain cost/blockers and landing-fit rules.

This does not include forced movement, push/pull, knockback or interception.

#### core calculations

Verified for explicitly ported primitives including Damage Base tables, type-effectiveness steps, stages, supported accuracy/crit/weather calculation slices, Burn calculation slices, modifiers and rounding points.

This does not establish the full end-to-end stateful damage pipeline.

#### action economy/initiative

Typed phases, action budget, deterministic initiative order, Trick Room/League ordering and declared-action ordering have direct evidence.

#### AI legal-action infrastructure

The engine can enumerate deterministic legal choices for supported movement and Move target modes with action-budget filtering.

This is legality infrastructure, not tactical judgment.

### PARTIAL

#### full turn/round lifecycle

Round lifecycle control, lifecycle hooks, temporary-effect cleanup/payload state and delayed-hit scheduling/binding are meaningful slices.

Still PARTIAL because full effect execution, all durations, all hook families and complete BattleSpec -> BattleTranscript parity remain incomplete.

#### full stateful damage pipeline

Calculation primitives and ordered hook infrastructure exist with representative Burn, Mega Launcher and Pink Pearl slices.

Still PARTIAL because all stateful modifier sources and the full end-to-end pipeline are not verified.

#### status lifecycle

Burn and lifecycle infrastructure provide real evidence.

Still PARTIAL because the complete PTU status controller, save checks, durations and interactions are not ported.

#### move-specific behavior

Canonical move state, selected move hooks and delayed-hit scheduling/binding exist.

Still PARTIAL. No representative Move proves the full Move library.

#### abilities

Mega Launcher is a parity-backed representative slice through an authoritative path.

Still PARTIAL. The complete Ability registry and behavior set are not established.

#### items

Held-item state and Pink Pearl provide one authoritative representative slice.

Still PARTIAL. The complete item library and all item hook families remain unverified.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement

The Java README still lists forced movement/reactions within unfinished work. No live evidence verifies this family.

#### terrain/weather/hazards/zones/reactions

Weather-related calculations do not establish authoritative battlefield weather state, terrain transitions, hazards, zones or reactions. This remains blocking for encounters where those states change tactics.

#### Trainer Features/perks

The Java README continues to list perk/Trainer Feature hook registries among unfinished work. General hook infrastructure does not prove these families.

#### AI tactical policy

Legal action generation exists. Scoring and policy over legal `BattleChoice` lists remains explicitly unfinished.

#### Minecraft/Cobblemon/Craftics adapter/playback support

The Java repository explicitly remains a standalone Java rules core rather than a Minecraft mod. Adapter/playback is planned after a parity-safe vertical slice and remains blocking for production in-world execution.

## Consequences for Pass 22 science encounters

Most research gameplay can advance without tactical engine dependencies because it is world-state logic:

- research questions;
- observations;
- datasets;
- hypotheses;
- replication;
- review;
- publication;
- institutional disagreement;
- sample provenance;
- field-station state;
- research standing;
- access and scheduling.

The following tactical ideas remain reduced-only unless later engine evidence appears:

- protecting instruments as tactical objective entities;
- retrieving sensors while AI pursues/intercepts the carrier;
- weather conditions that mechanically change during a replication encounter;
- objective-aware wild AI that prioritizes territory/equipment rather than ordinary combat choices;
- reaction zones around equipment;
- knockback into/out of observation zones;
- Trainer Feature interrupts by research staff;
- Minecraft rendering of objective state and battle writeback.

## Pass 22 encounter dependency table

| Encounter | Full-version key dependencies | Current status | Reduced version |
|---|---|---|---|
| Field Station Disturbance | hazards/zones/reactions; tactical AI; possibly forced movement/interception; full lifecycle/damage/status/move/ability/item support; Minecraft playback | BLOCKING overall | keep instruments outside grid; static legal encounter; station consequences in overworld |
| Remote Sensor Retrieval | interception/forced movement if pursuit matters; tactical AI; environment families if tactical; Minecraft playback | BLOCKING overall | retrieval in overworld; ordinary static encounter only if triggered |
| Weather Platform Replication | authoritative battlefield weather/terrain state; lifecycle; selected move/ability/item behavior; tactical AI if objectives matter; Minecraft playback | BLOCKING overall | weather remains narrative/world-state context; static legal battle does not claim weather mechanics |

Verified families may still be used inside each reduced battle where the selected combatants and arena stay inside their proven scope.

## Important non-inference rule

Research narrative must not infer a battle capability from scientific world state.

Examples:

- an observed weather correlation does not mean Java supports battlefield weather;
- a field station tracking movement does not mean the engine supports interception;
- a research assistant having an authored profession does not mean Trainer Features/perks are ported;
- identifying an Ability after lawful observation does not mean the full Ability registry exists;
- a sample mentioning a Move does not authorize executing that Move unless the exact Move is present and validated through the authoritative engine path.

## Source authority boundary

Python `Teffa14/AutoPTU` remains the behavioral oracle while the port is incomplete.

The narrative repository may describe desired scientific encounters and reduced alternatives. It must never implement missing PTU battle behavior inside narrative scripts or the future Minecraft adapter.
