# Engine Readiness Snapshot — Pass 132

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records only evidence relevant to narrative implementation boundaries at the time of Pass 132. AutoPTU-Java and AutoPTU are read-only sources for this task.

A representative implemented mechanic never promotes an entire capability family by itself.

## Inspected engine heads

AutoPTU-Java:

`aefc058328a9217d634477835a4851d521aaeccb`

Latest inspected commit:

`Apply reaction movement authoritatively (#162)`

AutoPTU Python:

`29a8e62e24c3e58233ca2c8154a30d796099f90a`

Recent Python changes are Career persistence/resilience work and do not alter the tactical classification below.

## New Java evidence since Pass 131

The latest Java slice adds a server-authoritative application boundary for one reaction-movement pattern.

Observed behavior in the commit:

- reachability is derived from canonical battle grid and movement profile;
- a safe destination is selected using the previously frozen area-escape reaction contract;
- the combatant’s canonical position is mutated;
- a `ShiftResolvedEvent` is emitted;
- this reaction movement does not spend the actor’s normal Shift action budget;
- an optional displacement cap and fit predicate are respected;
- when no safe destination exists, state remains unchanged.

This is meaningful movement/reaction progress.

## What that slice does not prove

It does not verify:

- generic reaction trigger/permission dispatch;
- interception;
- attacks of opportunity;
- Push execution;
- Pull execution;
- knockback;
- collision chains;
- falling;
- movement-triggered hazards;
- zone entry/exit triggers;
- all reaction resource/usage bookkeeping;
- dynamic objectives;
- escort behavior;
- civilian movement;
- general forced movement;
- Minecraft playback.

The current Java README still explicitly lists status controller, terrain, hazards, forced movement and reactions as incomplete. It also lists full damage, hook registries, AI policy and Minecraft/Cobblemon integration as unfinished.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Evidence remains strong for geometry, footprints, anchors, range and LoS in the ported contracts.

Do not infer visibility under darkness, smoke or weather from geometric LoS alone.

### base movement legality — VERIFIED

Java has verified Shift legality and several movement-profile primitives.

Do not infer complete encounter movement objectives from this family.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

The new reaction-escape application is a narrow real slice.

The family remains BLOCKING because generic forced movement, Push/Pull application, knockback, interception, collision and movement-triggered effects are not complete.

### core calculations — VERIFIED

Core calculation primitives remain verified for the ported scope.

### action economy/initiative — VERIFIED

Action budget and initiative infrastructure have substantial parity-backed coverage.

The new reaction movement correctly preserves normal Shift action budget under its specific contract.

### full turn/round lifecycle — PARTIAL

Java has increasing lifecycle coverage, including round transitions, temporary effect cleanup, delayed-hit maturity and specific phase ordering.

The entire lifecycle and every phase-trigger interaction remain incomplete.

### full stateful damage pipeline — PARTIAL

Significant stateful damage behavior exists, including multiple post-damage hooks and delayed-hit paths.

The README still marks full damage as incomplete.

### status lifecycle — PARTIAL

Java has status state, several prevention families and specific Safeguard/Ability interactions.

The status controller as a whole remains incomplete.

### terrain/weather/hazards/zones/reactions — BLOCKING

Java has some semantic field state, progression primitives and now one applied reaction movement path.

This category remains BLOCKING because the combined family is not complete and the README still lists terrain, hazards and reactions as unfinished.

### move-specific behavior — PARTIAL

Multiple representative Move contracts exist, including delayed-hit behavior and forced-movement instruction parsing.

The Move catalog is not complete.

### abilities — PARTIAL

Many individual Ability hooks have parity evidence.

No whole-family promotion is justified.

### items — PARTIAL

Item coverage remains incomplete.

### Trainer Features/perks — PARTIAL

Java now has broad generic Feature infrastructure for prerequisites, context, frequency/cooldown, resources, usage bookkeeping, target scopes and several generic effect types.

Concrete Feature catalog execution remains incomplete.

### AI legal-action infrastructure — VERIFIED

The engine can construct/filter legal action choices under the ported contracts.

### AI tactical policy — BLOCKING

No complete objective-aware policy exists for goals such as:

- `ESCORT`;
- `PROTECT_TECHNICIAN`;
- `CLEAR_ROUTE`;
- `WITHDRAW`;
- `REACH_EXIT`;
- `REACH_GROUP`;
- `EVACUATE`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

The Java README still describes this as future work after a parity-safe vertical slice.

Minecraft must remain a renderer/adapter rather than an owner of PTU rules.

## Pass 132 encounter dependencies

### Clocktower Relay Access — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for a technician moving during battle;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage — PARTIAL;
- status lifecycle — PARTIAL if used;
- terrain/weather/hazards/zones/reactions — BLOCKING if live environmental/reaction behavior is present;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING.

REDUCED:

Technician movement and clock work happen outside the grid. A static conventional battle can run using the verified/basic families.

### Station Platform Time Dispute — FULL

Primary blockers:

- complete movement/interception for crowds/staff;
- AI tactical policy for route-clearing and protection;
- Minecraft/Cobblemon/Craftics playback for platform/crowd semantics.

Environment remains optional and must not be invented from station scenery.

REDUCED:

Staff clear the platform in world state before battle. AutoPTU receives only actual combatants and static geometry.

### Observatory Timestamp Reconciliation

Primary mode is non-combat.

No tactical engine dependency is required unless an independent battle occurs.

## Timekeeping-specific non-inferences

Pass 132 must not infer:

- accurate clock -> initiative bonus;
- synchronized party -> shared initiative;
- stopwatch -> extra action;
- clock drift -> delayed Move change;
- schedule deadline -> action-economy penalty;
- day/night display -> PTU Weather;
- Minecraft sun position -> authoritative timestamp;
- client system clock -> world chronology;
- timestamp discrepancy -> time travel;
- broken clock -> temporal anomaly;
- precise timestamp -> factual truth of the recorded claim.

## World-state blockers introduced by Pass 132

These are outside the battle core:

- `AUTHORITATIVE_WORLD_TIME_SERVICE`;
- `TIME_STANDARD_REGISTRY`;
- `TIME_STANDARD_REVISION_HISTORY`;
- `LOCAL_TIME_RULESET_STATE`;
- `CLOCK_INSTANCE_STATE`;
- `CLOCK_SYNC_EVENT_HISTORY`;
- `RAW_TIMESTAMP_PROVENANCE`;
- `CORRECTED_TIMESTAMP_ESTIMATES`;
- `SCHEDULE_TIME_REFERENCE`;
- `TEMPORAL_DISCREPANCY_CASES`;
- `TIMEKEEPING_TO_DIGITAL_LOG_HANDOFF`;
- `TIMEKEEPING_TO_RAIL_POSTAL_DISPATCH_HANDOFF`;
- `TIMEKEEPING_TO_SCIENCE_OBSERVATION_HANDOFF`;
- `TIMEKEEPING_TO_MINECRAFT_DISPLAY_PROJECTION`.

## PTU/Caelo evidence boundary

No public narrative source is used as a rules authority.

The complete named Caelo source corpus was not recoverable as a reliable invocable source during this run. Super PTU Online Helper was not exposed as a callable capability.

Do not invent:

- timekeeping Skill checks;
- timing bonuses;
- day/night battle modifiers;
- clock items with combat effects;
- initiative modifiers from synchronization;
- temporal Move behavior;
- Legendary time mechanics.

## Current implementation strategy for narrative authors

Use server/world time to schedule and timestamp narrative state.

When a concept becomes a battle:

1. resolve clock/schedule discrepancies before opening AutoPTU when possible;
2. freeze world geometry and participating combatants;
3. do not encode timing narrative as custom PTU modifiers;
4. use reduced encounter versions until complete movement, tactical AI and adapter playback are actually verified;
5. after battle, write authoritative AutoPTU results back to world state without letting the battle decide clock synchronization or institutional conclusions.
