# Engine Readiness Snapshot — Pass 126

Status: implementation-evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `554b97e44fca9736f98704f8db3b1a661c63e93f`

Newest Java slice: `Port Flower Veil combat-stage prevention (#157)`.

That slice adds a parity-backed, geometry-aware Ability boundary that can prevent external negative Combat Stage mutations for the specific Flower Veil family. It strengthens evidence for Ability hooks and Combat Stage mutation ordering.

It does not prove:

- complete Ability coverage;
- generic olfactory mechanics;
- Stench overworld behavior;
- Sweet Scent;
- Odor Sleuth;
- Tracker;
- scent propagation;
- smell-based Perception;
- environmental gas or odor hazards;
- wildlife attraction/repulsion;
- AI scent pursuit;
- Minecraft sensory projection.

AutoPTU `main`: `9df36aeae4bcbef49fd5edb658b51d68bd45fa71`

Newest Python change is Career-oriented rival-memory persistence and does not promote a battle capability family.

The Python data repository exposes `Tracker` in `PTUDatabase-main/PTUDatabase/Enums/OtherCapability.cs`. Enum/data presence is not runtime implementation.

## Current Java README evidence

The live Java README still marks these broad areas incomplete:

- broader canonical combatant/grid state;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/Perk/Trainer Feature registries;
- semantic BattleSpec → BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative parity-tested rules must not be promoted to whole-family coverage.

## Permanent capability map

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 126.

## Why olfaction remains overworld state

Nothing inspected establishes an authoritative battle or adapter subsystem for:

- odor-source identity;
- scent emission events;
- olfactory-field propagation;
- scent degradation outside a specific rule;
- masking between odors;
- observer smell sensitivity;
- scent-mark persistence;
- scent-based geographic inference;
- odor baselines/anomalies;
- wildlife route changes in response to odor;
- scent-sensitive institutional work;
- smellscape persistence while chunks are unloaded;
- semantic odor presentation in Minecraft.

Those belong to world state, observation, ecology and research until a specific PTU mechanic is validated.

## Critical separation from LoS

`targeting / footprints / range / LoS` remains VERIFIED for the current battle contract.

That does not imply olfactory detection.

Visual line of sight cannot be reused as:

- scent line of sight;
- smell radius;
- scent-trail routing;
- ventilation modeling;
- downwind propagation;
- odor masking;
- scent identity certainty.

A future sensory API should keep visual geometry and olfactory information semantically distinct.

## Critical separation from Tracker

The source data contains a `Tracker` capability label.

This does not demonstrate:

- which current Pokémon receive it under project-authoritative data;
- exact PTU/Caelo scent rules;
- Java runtime support;
- a world tracking service;
- detection range;
- certainty of identification;
- environmental degradation math;
- AI pursuit behavior.

The Field Signs layer remains the authority for scent traces used as evidence. Pass 126 adds ambient/multi-source smellscape state around those traces.

## Encounter dependency map — Masked Trail at Alder Crossing

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement incl. push/pull/knockback/interception/forced movement: BLOCKING for moving search, protected lanes and withdrawal
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if masking becomes a validated tactical effect
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for SEARCH / WITHDRAW / REACH_OBSERVATION_POINT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Tracking, masking and route inference resolve in overworld state. If conflict remains, AutoPTU receives a fixed crossing and only actual combatants. No scent-based target arrow or modifier is created.

## Encounter dependency map — Stunky Route Closure

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement incl. interception/forced movement: BLOCKING for retreat and corridor protection
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL; ordinary odor has no validated status effect
- terrain/weather/hazards/zones/reactions: BLOCKING for any odor zone or repulsion mechanic
- move-specific behavior: PARTIAL
- abilities: PARTIAL; Stench is not generalized from Pokédex flavor
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for WITHDRAW / CLEAR_ROUTE / AVOID_CONFLICT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

The route closes, visitors move away and observers investigate in world state. Any actual battle uses a static map. The odor event does not cause Flinch, Poisoned or forced movement.

## Encounter dependency map — The Clean Room Anomaly

FULL version if a real tactical hazard is later verified:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING for evacuation/interception objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for environmental gas/odor hazards
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for EVACUATE / SHUTDOWN / PROTECT_TECHNICIAN
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

The facility shuts down and workers leave before any battle. Investigation uses Technology/Science/Metrology state. A separate threat can use a static safe-zone arena. Smell is evidence, not damage.

## New overworld blockers introduced by Pass 126

- `OLFACTORY_SOURCE_REGISTRY`
- `ODOR_EVENT_HISTORY`
- `OLFACTORY_FIELD_STATE`
- `SMELLSCAPE_BASELINE`
- `OLFACTORY_OBSERVATION_LEDGER`
- `OLFACTORY_PROFILE_VERSIONING`
- `SCENT_MARK_OLFACTORY_STATE`
- `OLFACTORY_MASKING_STATE`
- `OLFACTORY_ANOMALY_CASE`
- `SCENT_SENSITIVE_WORK_ROLE_STATE`
- `OLFACTION_TO_TRACKING_HANDOFF`
- `OLFACTION_TO_FLORA_HANDOFF`
- `OLFACTION_TO_DECOMPOSITION_HANDOFF`
- `OLFACTION_TO_WASTE_HANDOFF`
- `OLFACTION_TO_AIR_QUALITY_HANDOFF`
- `OLFACTION_TO_URBAN_WILDLIFE_HANDOFF`
- `OLFACTION_TO_MIGRATION_HANDOFF`
- `OLFACTION_TO_SOCIAL_LEARNING_HANDOFF`
- `OLFACTION_TO_COBBLEMON_PROJECTION`
- `OLFACTION_TO_MINECRAFT_PRESENTATION`
- `OLFACTION_TO_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 126

Do not infer:

- scent → exact location;
- scent → individual identity;
- smell → Poisoned;
- unpleasant smell → Flinch;
- fragrance → Charm or morale bonus;
- pleasant scent → healing;
- scent mark → ownership or territory;
- overlapping smell → accuracy penalty;
- strong smell → hazard zone;
- Stunky flavor → active Stench mechanics;
- Aromatisse flavor → combat buff/debuff;
- Spritzee diet change → mechanical form change;
- Slurpuff lore → Tracker implementation;
- Skiploom fragrance → exact birthplace;
- `Tracker` enum → Java Tracker support;
- battle LoS → olfactory propagation;
- smoke odor → tactical smoke effect;
- decay odor → disease;
- waste odor → contamination;
- missing expected odor → absence of source;
- Minecraft particles → world-truth scent field.

## Open mechanical and canon questions

- Exact PTU/Caelo text for Tracker and smell-based Perception.
- Exact PTU/Caelo treatment of Sweet Scent, Odor Sleuth, Stench and aroma-related effects.
- Which Pokémon have project-authoritative olfactory capabilities.
- Whether scent communication is authored for any Ouros populations.
- Which regions have strong place-specific smellscapes.
- Whether any institutions use Pokémon for scent-sensitive work.
- How weather, ventilation, water and enclosed spaces affect smell without unsupported simulation.
- Whether a future adapter should expose semantic sensory observations beyond visual LoS.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output was invented.