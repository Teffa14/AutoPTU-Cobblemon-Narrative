# Engine Readiness Snapshot — Pass 78

Status: implementation evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`3906892c11129c419e702d87ff71db071c12050f`

Latest visible commit:

`Make authoritative initiative rollover the default lifecycle path (#112)`

Parent inspected in Pass 77:

`2ca88352fbf5ca4d07bd795c49533dc26c41f5c6`

The new slice makes the already-authoritative initiative rollover rebuilder the default lifecycle path and adds tests for that default behavior. The battle core therefore owns reconstruction/installation of the next round's initiative rather than expecting Minecraft/Cobblemon to provide an order.

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its latest visible commit remains Career-oriented (`Career: make roster recovery deterministic`) and does not change the tactical classification below.

## What Pass 78's new Java evidence proves

The latest Java commit strengthens evidence that:

- initiative rollover is server authoritative;
- default lifecycle flow now uses the canonical rollover path;
- initiative ordering remains inside core state instead of renderer/adapter state;
- action economy/initiative remains a robust VERIFIED family.

It does not prove:

- every START/COMMAND/ACTION/END hook;
- all duration expiry;
- complete delayed-effect execution;
- full status controller;
- full damage pipeline;
- environmental tide/water-depth transitions;
- complete Weather/Terrain semantics;
- hazards/zones/reactions;
- forced movement/current displacement;
- tactical AI;
- Minecraft/Cobblemon/Craftics playback.

## Java README boundary

The live README still explicitly lists as unfinished:

- core combatant/grid battle-state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary no-overclaim guardrail.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

Range, target anchors, areas, footprints and geometric LoS remain verified for the ported surface.

Pass 78 guardrail:

Geometric LoS does not establish tidal visibility, turbidity, submerged sight, fog over marshes or line-of-sight changes caused by vegetation/water.

### base movement legality

Current evidence covers Shift legality using Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, landing fit and Jump foundations.

Pass 78 guardrail:

This does not prove changing water depth, current-driven movement, mud entrapment, tidal crossings or passenger transport.

### core calculations

PTU calculation primitives remain verified for the implemented surface: Damage Base tables, type steps, stages, accuracy primitives, crit/Burn/weather DB and modifier/rounding utilities.

Pass 78 guardrail:

A Weather DB or terrain-cost primitive does not make salinity, tide, marsh substrate or estuary chemistry into battle mechanics.

### action economy/initiative

VERIFIED and strengthened again in Pass 78.

Evidence now includes canonical initiative entries/order, ordering modes, round rebuild and default lifecycle rollover from `BattleRuntimeState`.

No promotion of full turn/round lifecycle follows from this.

### AI legal-action infrastructure

The deterministic `BattleChoice` legality surface remains available for currently supported actions, targets, movement and action-budget constraints.

This does not establish objective-aware retreat, tidal-route planning or avoidance of changing water zones.

## PARTIAL

### full turn/round lifecycle

Java has substantial phase, round, cleanup, initiative and effect-hook infrastructure. Pass 78 makes authoritative initiative rollover the default path, but full lifecycle and BattleSpec -> BattleTranscript parity remain incomplete.

### full stateful damage pipeline

Multiple damage/accuracy/post-damage slices exist. Full resolution remains explicitly unfinished in the Java README.

### status lifecycle

Selected application, phase and expiry behavior has parity evidence. The complete controller remains unfinished.

Pass 78 guardrail:

No generic environmental `mud`, `salinity`, `brackish exposure`, `drowning` or `water pressure` status exists by implication.

### move-specific behavior

Selected move contracts/behaviors exist. Full move-library behavior is not demonstrated.

### abilities

Multiple Ability hook families and representatives exist with parity. Full coverage is not demonstrated.

Pass 78 guardrail:

`Storm Drain`, `Water Absorb`, `Swift Swim`, `Static` or similar individual mechanics cannot be reused as estuary simulation primitives.

### items

Representative held-item state/effects exist. Full item behavior remains incomplete.

### Trainer Features/perks

Runtime state, hook infrastructure and representative Features exist. Full Classes/Features/Edges/Orders are not demonstrated.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

Still BLOCKING as a family.

Pass 78 needs this family for any encounter where:

- a current physically displaces combatants;
- a moving tide forces relocation;
- actors intercept wildlife/civilians in a crossing lane;
- unstable footing causes forced displacement;
- evacuation movement is modeled tactically.

A static pre-battle water level can avoid this dependency in reduced versions.

### terrain/weather/hazards/zones/reactions

Still BLOCKING as a family.

`BattleEnvironmentState`/weather/terrain primitives used by selected calculations do not establish complete environment behavior.

Pass 78 specifically requires this category for:

- dynamic tidal-depth zones;
- current zones;
- marsh/mud hazards;
- changing submerged tiles;
- environmental salinity effects;
- water-level transitions during battle;
- unstable boardwalk zones;
- environmental reaction windows.

Until verified, tide/salinity/hydroperiod remain world state and presentation outside the tactical rules core.

### AI tactical policy

Still BLOCKING.

Legal actions exist, but AI cannot be assumed to understand:

- exit/safe-side objectives;
- wildlife withdrawal;
- tidal-window urgency;
- avoiding future inundation;
- protecting a crossing lane;
- choosing observation over combat;
- evacuation goals.

### Minecraft/Cobblemon/Craftics adapter/playback support

Still BLOCKING.

The Java README continues to state that the project is not yet a Minecraft mod and that the adapter follows a parity-safe core slice.

Minecraft must never decide PTU tide, mud, current or salinity effects.

# Pass 78 estuary-specific authority boundary

Available Python evidence supports these narrow statements:

- Swim capability/movement exists in tactical state;
- Naturewalk labels can be read from species/capability/Feature state;
- `swamp`, `wetland`, `marsh` and `mud` can map to a wetlands environment for selected authored effects such as Nature Power.

Those facts do not establish a generic estuary subsystem.

No verified general subsystem was found for:

- salinity bands;
- brackish-water effects;
- tide cycles;
- water-depth transitions;
- tidal currents;
- marsh hydroperiod;
- sediment/accretion;
- saltwater intrusion;
- mudflat exposure;
- estuary-mouth changes;
- salt-marsh migration;
- wetland nursery windows;
- salinity-driven spawning;
- groundwater salinization.

Caelo primary material was not reliably available for a dedicated salinity/tide rule during this run, so no Caelo-specific mechanic is asserted.

# Pass 78 encounter dependencies

## Tidal Creek Crossing — FULL

Required capability categories and live state:

- targeting/footprints/range/LoS — VERIFIED for geometry;
- base movement legality — VERIFIED for current static movement modes;
- complete movement/push/pull/knockback/interception/forced movement — BLOCKING if current or changing path mechanically moves/restricts actors;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if any real PTU status is involved;
- terrain/weather/hazards/zones/reactions — BLOCKING for changing depth/current zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for crossing/withdrawal behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Resolve authoritative tide state before battle and freeze one static geometry. Wildlife movement/crossing remains world state. Use normal legal combat if a battle occurs. No current, salinity, changing depth or mud mechanic is inferred.

## Marsh Boardwalk Breach — FULL

Required:

- targeting — VERIFIED;
- base movement — VERIFIED;
- complete movement/interception — BLOCKING for evacuation actors;
- core calculations — VERIFIED;
- initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage — PARTIAL;
- statuses — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for unstable/failed zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal actions — VERIFIED;
- tactical AI — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:

Evacuate noncombatants in overworld state. Convert the failed boardwalk to static blockers before battle. Use a stable arena and write repair/ecology consequences after resolution.

## Salinity Station Recovery — FULL

This concept is primarily noncombat research.

If a battle occurs:

- targeting/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING only for richer reach/withdraw behavior;
- calculations — VERIFIED;
- initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage — PARTIAL;
- status — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if environmental mechanics are desired;
- move/abilities/items/Features — PARTIAL according to actual combatants;
- AI legal actions — VERIFIED;
- tactical AI — BLOCKING for objective-aware retreat;
- adapter/playback — BLOCKING.

Reduced version:

Station retrieval, samples and salinity evidence remain world state. A conventional static battle opens only if actual encounter state requires it. Measurements never apply tactical effects.

# Pass 78 overworld blockers

These are outside the Java battle-core permanent categories and remain implementation work for Ouros/Minecraft integration:

- `ESTUARY_SYSTEM_GRAPH`
- `SALINITY_OBSERVATION_AND_FRONT_HISTORY`
- `TIDAL_STATE_AND_ACCESS_WINDOWS`
- `TIDAL_WETLAND_HYDROPERIOD`
- `MARSH_EDGE_AND_MIGRATION_HISTORY`
- `ESTUARY_MOUTH_AND_CHANNEL_REVISION`
- `SEDIMENT_BALANCE_EVENT_GRAPH`
- `COASTAL_GROUNDWATER_SALINITY_LINK`
- `ESTUARY_ECOLOGY_OBSERVATION`
- `ESTUARY_TO_COBBLEMON_PROJECTION`
- `ESTUARY_TO_BATTLE_SNAPSHOT`

The battle core should receive only a validated frozen environment snapshot once those systems exist.

# No-inference rules for future implementation

- A wetland label does not imply Slow/Rough Terrain.
- Mud does not imply Tripped or Accuracy loss.
- Brackish water does not imply damage, status or typing changes.
- Low tide does not imply legal walking on every exposed tile.
- High tide does not imply Swim is automatically legal for every combatant.
- Stunfisk habitat does not electrify the environment.
- Storm Drain does not model drainage or freshwater inflow.
- Water Absorb does not prove environmental-water immunity.
- Great Marsh capture presentation does not define PTU capture rules.
- Shellos/Gastrodon distribution observations do not define salinity mechanics.
- Minecraft water blocks do not own PTU environment state.

# Open validation questions

- Exact PTU/Caelo handling of Wetland/Marsh/Mud terrain labels.
- Exact Naturewalk (Wetland) behavior and whether Caelo modifies it.
- Exact Swim and water-entry movement rules relevant to shallow/tidal water.
- Whether any authoritative PTU rule exists for currents, mud, sinking or environmental water hazards.
- How `BattleEnvironmentState` should receive a frozen tide/water-depth projection in Java.
- Whether future objective semantics include WITHDRAW, REACH_EXIT, PROTECT_ROUTE or CLEAR_ROUTE.
- How Cobblemon spawning can consume coarse estuary habitat state without becoming player-manipulable through fast tide changes.
