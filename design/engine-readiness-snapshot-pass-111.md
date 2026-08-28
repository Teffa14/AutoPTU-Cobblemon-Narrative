# Engine Readiness Snapshot — Pass 111

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.

Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`9f63f0a81af45af2fbc87928b96c1cec4fcff4b0`

Commit/PR #262: `Rebind move preparation after pre-resolution target replacement`.

AutoPTU head inspected:

`cd197681c939bbc1189e25633cc42b11c59f8672`

Merge PR #219: `Career: normalize missing initial battle state at API boundary`.

Neither repository was modified by this pass.

## Java live evidence

The live Java head is unchanged from Pass 110. The authoritative pre-resolution target replacement path rebuilds defender-dependent move inputs from the effective target before accuracy RNG. This is strong evidence for the narrow target-replacement/Intercept path that recent slices have been composing.

It still does not verify the whole movement/reaction family.

Still not demonstrated as complete families:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- generalized competing reactions;
- reaction ordering outside implemented target-replacement paths;
- every Move registration;
- every Ability registration;
- every Item registration;
- every Trainer Feature/perk registration;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

A representative mechanic or extensible hook does not promote a permanent capability family.

## AutoPTU live evidence

The Python/web repository advanced since Pass 110 to `cd197681c939bbc1189e25633cc42b11c59f8672`, PR #219.

The current work normalizes a missing/null initial Career battle state at the API boundary and supplies a valid empty BattleFrame fallback for legacy data. This is stability/backward-compatibility work. It does not add tactical legality, movement, reactions, damage, status, tactical policy or adapter semantics.

No capability promotion follows from this change.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category is promoted in Pass 111.

## Pass 111 encounter dependencies

### Lift Lobby Withdrawal — full version

Required categories:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL when timed withdrawal or route changes matter
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL where exact legal effects apply
- terrain/weather/hazards/zones/reactions: BLOCKING if doors, shaft edges, changing cells or generalized reactions participate
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for withdrawal/protection behavior
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
- withdrawal/protection objective semantics: not verified as a complete tactical contract

Reduced version:

Complete civilian relocation before BattleSpec creation. Isolate the lift. Exclude shaft and moving-door mechanics. Use a static reviewed lobby with explicit combatants. The outcome can secure the immediate area but cannot restore service, grant destination authorization or complete later trips.

### Machine-Room Perimeter — full version

The same verified core applies. Any energized/moving equipment, technical danger area or changing restricted space relies on the BLOCKING terrain/hazards/zones/reactions family. Equipment protection requires tactical policy. Any equipment-caused damage or status additionally needs a governing PTU/Caelo rule and the PARTIAL damage/status families.

Reduced version:

Equipment is isolated before combat and remains outside BattleSpec. Workers are nonparticipants. AutoPTU resolves a static service corridor. Maintenance owns all later assessment, repair and verification.

### Split-Floor Diversion — full version

A live diversion with protected withdrawing actors directly relies on complete movement/Intercept when used, generalized reactions, objective-aware tactical policy and adapter playback.

Reduced version:

Move nonparticipants through the alternate route before combat. Resolve a static junction encounter afterward. Accessibility and vertical-route availability remain overworld state.

## Vertical-circulation mechanical unknowns

Current PTU/Caelo and implementation evidence does not verify a universal contract for:

- elevator/lift speed;
- car capacity or weight limits;
- automatic door timing;
- moving-platform tactical movement;
- elevator-shaft falling damage;
- crushing or trapping damage from doors/equipment;
- stalled-car rescue;
- emergency braking;
- power-loss behavior of a conveyance;
- initiative while a platform moves between floors;
- technical repair or inspection Skill checks;
- passenger/freight loading rules;
- moving lift cars as tactical objects;
- Pokémon lift operation derived from Type/species;
- Type-based immunity to technical hazards.

These remain UNKNOWN rather than being invented by the narrative layer.

## PTU/Caelo guardrail

The internal source scan remains controlling. Caelo can attach explicit mechanical identity to authored locations where governing source material defines an effect. That does not authorize free extrapolation from a visually dangerous elevator, shaft, moving platform, machine room or power state.

Before any such feature enters a BattleSpec mechanically, the concept needs both:

1. an exact governing PTU/Caelo rule for the effect; and
2. current engine tests/contracts supporting the required capability families.

Otherwise the feature remains overworld state, inert scenery or is removed from the reduced tactical arena.

## Minecraft/Cobblemon/Craftics boundary

Presentation can reuse authored buildings, lift doors, static cars/platforms, landing indicators, call-button UI, barriers, notices, maintenance props, floor labels, NPCs, Pokémon models/forms/poses/animations/cries, sounds, particles, networking, entity tracking and persistence hooks.

The adapter must not derive tactical or service truth from those visuals.

- redstone power does not establish lift readiness;
- an open door does not prove boarding or destination authorization;
- a moving platform does not become PTU movement by itself;
- teleporting an entity between floors does not prove a completed trip without authoritative state transition;
- Minecraft fall damage does not substitute for PTU damage;
- pistons or native collision do not apply ungoverned crushing effects;
- chunk unload cannot reset a trip interruption or outage;
- Cobblemon BattleState/controller logic does not select combatants or decide legality, HP/status, positions or battle outcomes.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and resolution. The adapter presents authoritative outcomes.

## Canon questions carried forward from Pass 111

Unresolved setting questions include:

- which regions and settlement types use vertical conveyances;
- which device technologies exist;
- public versus residential versus service/freight use;
- operators and institutional ownership;
- destination authorization models;
- regional accessibility practices and fallback routes;
- historic/decommissioned shafts or systems;
- outage and verification customs;
- individual Pokémon roles, if any, supported by explicit canon;
- privacy/access rules for trip and maintenance records.

## Promotion rule

Do not promote a permanent capability because the Intercept target-replacement path is increasingly complete. The permanent `complete movement including push/pull/knockback/interception/forced movement` family remains PARTIAL until its broad contract is implemented and tested. The combined environmental/reaction family, tactical policy and semantic adapter remain BLOCKING.