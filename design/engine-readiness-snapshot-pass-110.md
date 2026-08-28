# Engine Readiness Snapshot — Pass 110

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.

Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`9f63f0a81af45af2fbc87928b96c1cec4fcff4b0`

Commit/PR #262: `Rebind move preparation after pre-resolution target replacement`.

AutoPTU head inspected:

`8930a2045bbb04dba3f227951309d67bbbc52ada`

Commit/PR #218: `Career: tolerate legacy battle transcripts without hash`.

Neither repository was modified by this pass.

## Java evidence added by the current live head

The Java core now composes authoritative pre-resolution target replacement with target-dependent move preparation. After a target hook replaces the defender, defender-bound inputs are rebuilt from the effective authoritative combatant before accuracy RNG. Tests cover defense/evasion rebinding and preserve the server-owned boundary.

This strengthens the narrow Intercept/target-replacement path established across recent slices.

It does not prove broad reaction or forced-movement coverage.

Still unverified as complete families include:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- generalized competing reactions;
- reaction ordering outside the implemented target-replacement path;
- all Move registrations into the hook system;
- all Ability registrations;
- all Item registrations;
- all Trainer Feature/perk registrations;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

A hook registry capable of representing a source does not prove that every legal source is registered and implemented.

## AutoPTU evidence

The Python/web repository's current change normalizes missing or non-string legacy battle transcript hashes to a stable legacy value at the Career API/cache boundary.

This is client stability/backward-compatibility work. It does not add a tactical capability and causes no capability promotion.

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

No category is promoted in Pass 110.

## Pass 110 seismic concept dependencies

### Monitoring Ridge Withdrawal — full version

Requires:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if timed environmental phases exist
- full stateful damage pipeline: PARTIAL if environmental damage exists
- status lifecycle: PARTIAL if environmental statuses exist
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
- withdrawal/protection objective semantics: not verified

Primary blockers are active environmental zones/reactions, objective policy and adapter/playback. Intercept has increasingly strong narrow evidence but does not satisfy the whole complete-movement family.

Reduced version can run narratively by ending active shaking before BattleSpec creation, excluding unsafe terrain and nonparticipants, and using a static reviewed arena.

### Post-Event Plaza Perimeter — full version

Requires the same core verified families. Dynamic falling debris, secondary shaking, changing blocked cells or structural zones are BLOCKING under terrain/weather/hazards/zones/reactions. Protection behavior needs AI tactical policy. Any falling-debris damage also relies on the still-PARTIAL damage pipeline plus a governing hazard contract.

Reduced version uses an already evacuated and reviewed open plaza. No dynamic collapse or debris participates in battle.

### Sensor Vault Diversion — full version

If the scene includes a delayed aftershock or timed technical-object phase, full turn/round lifecycle is directly required and remains PARTIAL. Technical hazards or changing access zones require the BLOCKING terrain/hazard/reaction family. Objective-aware protection of equipment requires BLOCKING tactical policy. Playback remains BLOCKING.

Reduced version keeps the vault inert and outside the battle grid.

## Seismic mechanical unknowns

Current evidence does not verify a universal PTU/Caelo contract for:

- natural earthquake event simulation;
- seismic magnitude/intensity arithmetic;
- environmental forced movement from shaking;
- automatic prone/knockdown from tremors;
- falling-rock or debris damage;
- building or infrastructure HP;
- structural collapse;
- fissure creation;
- landslide behavior;
- aftershock scheduling;
- earthquake prediction;
- seismic monitoring Skill checks;
- rescue/carry during active shaking;
- species-level seismic sensing;
- Ground-type environmental immunity;
- Move-powered monitoring or stabilization.

A specific Move such as Earthquake does not establish any of these world-event rules.

## PTU/Caelo guardrail

The internal project source scan remains controlling: Caelo can define specific location effects when governing material explicitly provides them. That supports authored mechanical location identity, not free extrapolation to every environmental event.

For seismic content, mechanically active shaking, debris, unstable surfaces, collapse, delayed effects or status exposure must cite an exact PTU/Caelo rule plus current engine tests/contracts before entering a BattleSpec.

Until then, those facts remain overworld/narrative state or are removed from the tactical arena in the reduced version.

## Minecraft/Cobblemon/Craftics boundary

Presentation can reuse world geometry, cracks, repaired structures, barriers, monitoring props, warning visuals, NPC crews, Pokémon models/forms/poses/animations/cries, sound, particles, UI, networking, entity tracking and persistence hooks.

The adapter must not infer tactical truth from presentation.

- screen shake does not apply forced movement;
- native falling blocks do not apply PTU damage;
- Minecraft block breakage does not establish collapse state;
- entity pathfinding does not complete evacuation;
- a warning light does not prove alert receipt;
- a Pokémon moving away does not establish prediction;
- Cobblemon BattleState/controller logic does not choose combatants or resolve legality, HP/status, positions or outcomes.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and resolution. The adapter presents authoritative outcomes.

## Canon questions carried forward

Pass 110 leaves these unresolved:

- seismic geography of Ouros;
- monitoring technologies and institutions;
- alert authority and dissemination methods;
- measurement systems, if any;
- historic earthquakes and their settlement consequences;
- inspection/reopening practices by region;
- formal after-event advisory practice;
- temporary versus permanent monitoring sites;
- individual Pokémon roles in observation or response;
- access/privacy rules for event and inspection records.

## Promotion rule

Do not promote a permanent capability because one representative mechanic works. Promotion requires evidence that the family contract is broadly implemented and tested. Recent Intercept/target-replacement work remains narrow positive evidence inside a PARTIAL family.