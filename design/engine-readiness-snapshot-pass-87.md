# Engine Readiness Snapshot — Pass 87

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`f4a5232b406fe0c80137e4d1d2f8408771ab4ba0`

Latest visible commit:

`Run canonical field progression during ROUND_START`

AutoPTU Python `main` inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python changes remain Career-oriented and do not justify tactical capability promotions.

## Java evidence relevant to Pass 87

The current Java field-state work now demonstrates all of the following for a narrow lifecycle slice:

- canonical terrain/zone/room entries are stored in `BattleEnvironmentState`;
- duration-bearing field entries are advanced during authoritative `ROUND_START`;
- field expiry can emit semantic events;
- field cleanup can remove named statuses when the verified contract requires it;
- the lifecycle-level behavior is checked against Python-oracle fixtures;
- Minecraft/controller code does not own field expiry.

This is meaningful infrastructure for future environment mechanics.

It does not demonstrate an ocean/current subsystem.

## Explicit non-inferences for open-ocean content

The current Java evidence does not prove:

- a current field effect;
- water-driven forced movement;
- entry/exit reactions from currents;
- thermocline effects;
- temperature-front modifiers;
- open-ocean Weather lifecycle;
- underwater depth bands;
- pressure or breathing;
- underwater visibility;
- wave/swell mechanics;
- buoy or vessel movement;
- plankton or ecological mechanics;
- upwelling/downwelling;
- bloom/toxin effects;
- pelagic tactical AI;
- initialization of ocean state from Minecraft.

## AutoPTU-Java README anti-overclaim boundary

The current README continues to list unfinished work for:

- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Pass 87 therefore keeps the permanent capability map conservative.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for implemented static geometric targeting.

Pass 87 guardrail:

Geometric LoS does not prove underwater visibility, haze in water, turbidity, depth visibility, waves or line-of-sight through a moving water column.

### base movement legality

VERIFIED for implemented Shift/Jump and Overland/Swim/Sky surface contracts already ported.

Pass 87 guardrail:

`Swim` legality does not prove current resistance, long-distance swimming, vertical diving, pressure tolerance, passenger transport or pelagic navigation.

### core calculations

VERIFIED for ported calculation primitives.

Pass 87 guardrail:

There is no generic current, thermocline, cold-water, warm-water, upwelling, plankton, bloom, depth or pressure modifier.

### action economy/initiative

VERIFIED for the implemented initiative/action surface.

Pass 87 guardrail:

Ocean drift, front movement and sampling windows are overworld state unless an exact battle mechanic is authored and implemented.

### AI legal-action infrastructure

VERIFIED for supported legal choices.

It does not provide tactical goals such as:

- HOLD_POSITION_IN_CURRENT;
- REACH_BUOY;
- WITHDRAW_FROM_FRONT;
- PROTECT_RESEARCH_RIG;
- AVOID_VESSEL;
- FOLLOW_SCHOOL;
- DRIFT_WITH_CURRENT;
- SWIM_UPSTREAM.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java now executes canonical field progression during default `ROUND_START`, in addition to existing phase, cleanup, RNG, initiative and delayed-hit slices.

It still does not prove every phase effect, field interaction, send-out path, switch path, delayed effect, duration, cleanup or transcript event.

### full stateful damage pipeline

PARTIAL.

The normal/delayed pipelines increasingly use authoritative runtime state.

Pass 87 guardrail:

Currents, cold water, waves, pressure, collision with vessels, drowning, debris or depth cannot deal HP damage unless a verified rule path produces it.

### status lifecycle

PARTIAL.

Representative status application/phase/expiry slices exist.

Pass 87 guardrail:

A bloom, cold current, deep water or rough sea cannot create Poisoned, Slowed, Tripped, Stuck, Injured or any other status through narrative description.

### move-specific behavior

PARTIAL.

Representative Move contracts, keywords and delayed-hit execution exist.

Pass 87 guardrail:

A Move that pushes water, creates weather, changes terrain, pulls targets or manipulates depth must be individually verified before an ocean encounter depends on it.

### abilities

PARTIAL.

Representative Ability hooks have parity evidence.

Pass 87 guardrail:

Swift Swim, Water Absorb, Storm Drain, Water Veil, species flavor or a Maelstrom concept cannot be generalized into current immunity, open-ocean navigation or water-temperature adaptation.

### items

PARTIAL.

Representative held-item behavior exists.

Pass 87 guardrail:

Buoys, sampling nets, tags, sonar, diving gear, research instruments and vessel equipment remain world-state assets unless they correspond to verified PTU Items.

### Trainer Features/perks

PARTIAL.

Representative Trainer Features and hook infrastructure exist.

The AutoPTU repository contains audit/source evidence for Water Elementalist: Maelstrom and Gilled/Swim-related text, but that is not evidence that Java has implemented the class.

Pass 87 guardrail:

No Maelstrom, Gilled, Survival, Athletics or other Feature benefit may be assumed without exact implementation/rules validation.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 87 FULL encounters may need:

- current-driven displacement;
- holding position against drift;
- intercepting actors before they cross a current boundary;
- moving objectives such as buoys or rigs;
- displacement around vessel edges;
- retreat through open water;
- movement between depth bands if ever supported.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family despite canonical field-state lifecycle progress.

The current Java head proves storage and ROUND_START progression/expiry for generic terrain/zone/room entries.

It does not authorize:

- current zones;
- thermocline zones;
- open-ocean weather phases;
- cold/warm-water field effects;
- bloom hazards;
- pressure zones;
- wave hazards;
- depth zones;
- zone entry/exit reactions;
- forced movement from fields;
- field creation from Minecraft ocean state.

### AI tactical policy

BLOCKING.

Legal actions exist, but there is no verified policy for:

- holding position in current;
- withdrawing with wildlife;
- protecting sampling equipment;
- avoiding vessels;
- reaching a buoy;
- staying near a front;
- escorting noncombatants in open water.

### Minecraft/Cobblemon/Craftics adapter/playback

BLOCKING.

There is no verified end-to-end contract that converts persistent oceanographic world state into authoritative AutoPTU field state and then plays current/depth/vessel consequences back into Minecraft without duplicating PTU rules.

# Pass 87 encounter dependency summary

## Pelagic Front Survey

REDUCED version can rely on:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when an ordinary legal battle uses them:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for the FULL version:
- complete movement/forced movement if current drift is tactical;
- terrain/weather/hazards/zones/reactions for current/front field effects;
- AI tactical policy;
- adapter/playback.

Reduced implementation rule:

The front and currents remain world state. The vessel chooses a stable location before battle. The tactical map remains static for the encounter.

## Drifting Buoy Recovery

REDUCED version can use world-state drift + static combat.

FULL version additionally depends on:
- complete movement if the buoy continues moving on-grid;
- field/hazard lifecycle if current is tactical;
- AI tactical policy for retrieval/protection;
- adapter/playback.

## Open-Water Wildlife Aggregation

REDUCED version can keep most wildlife and vessels outside the grid.

FULL version additionally depends on:
- complete movement/interception for moving groups;
- terrain/weather/hazards/zones/reactions if the ocean state is mechanically active;
- AI tactical policy for WITHDRAW/AVOID/PROTECT;
- adapter/playback.

# Pass 87 overworld blockers

These are outside the Java battle core and remain BLOCKING until a server/world-state implementation exists:

- `OPEN_OCEAN_REGION_STATE`;
- `OCEAN_STATE_REVISION_HISTORY`;
- `CURRENT_REGIME_STATE`;
- `WATER_MASS_STATE`;
- `OCEAN_FRONT_GEOMETRY_HISTORY`;
- `VERTICAL_WATER_PROFILE`;
- `STRATIFICATION_ASSESSMENTS`;
- `UPWELLING_DOWNWELLING_EVENTS`;
- `PELAGIC_HABITAT_ZONE_STATE`;
- `PLANKTON_SAMPLE_PROVENANCE`;
- `DRIFT_COHORT_STATE`;
- `BLOOM_OBSERVATION_STATE`;
- `OCEANOGRAPHIC_STATION_NETWORK`;
- `OPEN_OCEAN_TO_FISHERIES_CONNECTOR`;
- `OPEN_OCEAN_TO_REEF_ESTUARY_CONNECTOR`;
- `OPEN_OCEAN_TO_COBBLEMON_PROJECTION`;
- `OPEN_OCEAN_TO_BATTLE_SNAPSHOT`;
- `OPEN_OCEAN_TO_MINECRAFT_PLAYBACK`.

# Python oracle evidence used carefully

AutoPTU Python remains authoritative while the Java port is incomplete.

The repository contains source/audit material mentioning Maelstrom, Gilled and Swim-related rules.

That proves only that these PTU concepts exist in source material available to the project.

It does not prove a complete runtime implementation of:

- Maelstrom;
- Gilled;
- currents;
- underwater movement;
- water hazards;
- pressure;
- visibility;
- pelagic navigation.

No capability promotion is based on those terms alone.

# Recommended implementation order for ocean encounters

1. Keep oceanography entirely as server world state.
2. Project a static, safe arena snapshot into AutoPTU.
3. Use only verified Swim/movement legality and ordinary battle rules.
4. Add semantic current/depth fields only after exact PTU contracts exist.
5. Add forced movement only after the complete-movement family supports it.
6. Add tactical wildlife/vessel objectives only after AI policy exists.
7. Add Minecraft playback last, consuming semantic events from Java rather than recreating rules.

# Unresolved mechanical questions

- Exact PTU/Caelo text for Gilled and Swim.
- Exact Maelstrom Feature set and any current-related effects.
- Whether PTU/Caelo defines generic current movement.
- Whether underwater visibility/depth has explicit rules.
- Whether drowning/suffocation exists and how it interacts with Gilled.
- How capture/escape works in open-water encounters.
- Whether any Water Weather/Terrain maps to ocean physical state.
- How future Java field effects represent named PTU effects without generic narrative overreach.
- Whether 3D/depth combat is required or a 2D frozen layer is sufficient for the intended Minecraft experience.
