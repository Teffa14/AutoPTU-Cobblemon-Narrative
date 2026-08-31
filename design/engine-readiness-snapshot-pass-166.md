# Engine Readiness Snapshot — Pass 166

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-08-31
Narrative head before pass: `0432d4cdea485550f08b80d9189b8e15bf90cd05`

## Read-only engine heads inspected

AutoPTU-Java:

`6e7c07ab45d410c099eb52d05ba90067f486dd43` — merged PR #306, `Bind post-hit forced movement into BattleRuntime`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

Neither engine repository was modified by Pass 166.

## New Java evidence since Pass 165

Pass 165 ended at PR #303. Three later forced-movement changes were inspected as a sequence.

PR #304 froze additional Python consumer-pipeline landmarks around the forced-movement callsite.

PR #305 added `RuntimePostHitForcedMovementApplication`, a runtime seam for an already-resolved hit. The seam resolves the Move again from the server-owned canonical moveset, keeps the hit gate, applies the existing forced-movement instruction resolver, composes forced-movement Ability modifiers, then delegates displacement to the shared forced-displacement engine.

PR #306 binds that post-hit seam into `BattleRuntime.applyAuthoritativeMoveInternal` after a successful hit when the acting combatant has canonical Moves.

The inspected production patch calls:

`RuntimePostHitForcedMovementApplication.apply(state, choice, true)`

after the move has hit.

The corresponding `BattleRuntimeAuthoritativeMoveTest` now includes a canonical Push case that changes the target position after a hit and a miss case that leaves the target unmoved. The test also confirms the Standard Action remains consumed through the authoritative move flow.

This is materially stronger evidence than the previous parity-only runtime inventory. A tested forced-movement path is now bound into the production BattleRuntime move pipeline.

## Why complete movement still remains PARTIAL

The new evidence verifies a meaningful integration slice. It does not prove the entire permanent category.

Still not globally verified from the inspected contracts:

- every Push source and edge case;
- every Pull source and edge case;
- general Knockback across all governing rules;
- every Intercept variant and ordering interaction;
- arbitrary forced movement from statuses;
- arbitrary forced movement from terrain;
- arbitrary forced movement from weather;
- all Item-driven forced movement;
- all Ability-driven forced movement;
- all Trainer Feature-driven forced movement;
- escort/rescue movement;
- protected-object carrying;
- crowd/procession routing;
- moving vehicles or platforms;
- generalized reaction windows;
- dynamic tactical-objective policy.

The presence of one canonical Push test in the bound BattleRuntime path therefore cannot promote the whole family.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted in Pass 166.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head states that the change synchronizes battle-renderer coordinates after viewport resize and is presentation-only. It explicitly says battle rules and outcomes do not change.

No new mechanical capability evidence comes from AutoPTU in this pass.

## Population continuity and PTU/Caelo

The population-counting layer itself has no required combat mechanic.

The project's existing mechanical source priority remains authoritative for any future rules claim: PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List, plus current engine implementation.

No inspected project authority establishes a universal census mechanic, resident-count Skill Check, town-size combat modifier, civil-registration rule or population-derived Trainer progression system.

These remain UNKNOWN unless exact project sources establish them.

Population aggregates therefore remain narrative facts with provenance. They do not alter Initiative, Accuracy, damage, movement, status, Features, AI policy or encounter legality.

## Encounter A — Enumeration Team Withdrawal

Full capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as roster/content requires
- status lifecycle — PARTIAL as roster/content requires
- terrain/weather/hazards/zones/reactions — BLOCKING when field conditions become tactical
- move-specific behavior — PARTIAL; selected content audit required
- abilities — PARTIAL; selected content audit required
- items — PARTIAL; selected content audit required
- Trainer Features/perks — PARTIAL; selected content audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for escort/protect/withdraw objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic escort playback

Full status: BLOCKED.

Reduced status: READY at narrative-contract level after ordinary combat-content audit.

Enumerators, forms and instruments leave BattleSpec before initiative. AutoPTU may return only:

`IMMEDIATE_ENUMERATION_SITE_APPROACH_CLEAR`

That fact does not complete enumeration, establish coverage, create resident records or validate a population snapshot.

## Encounter B — Archive Count-Sheet Recovery Perimeter

Full version may require complete movement, protected-object carrying, lifecycle, hazards/zones/reactions, tactical objective policy and adapter playback.

Full status: BLOCKED.

Reduced status: READY.

Records remain outside BattleSpec in an already-authored storage state. AutoPTU can establish only:

`IMMEDIATE_RECORD_STORAGE_APPROACH_CLEAR`

That does not establish that the records are complete, authentic, recovered or correctly interpreted.

## Encounter C — Festival Service Chokepoint

Full version requires reliable crowd/escort routing, complete movement, lifecycle, zones/reactions when crowd geometry matters, tactical policy and semantic playback.

Full status: BLOCKED.

Reduced status: READY.

Civilians and service queues are removed from BattleSpec. Geometry is frozen before initiative. AutoPTU may return only:

`IMMEDIATE_SERVICE_ROUTE_CLEAR`

That does not restore service capacity, move crowds, change resident population, end an event or settle public reaction.

## Encounter D — Remote Count Station Perimeter

Full version can require weather, terrain, hazard, protection or withdrawal mechanics depending on the authored incident.

Full status: BLOCKED whenever those unverified families are required.

Reduced status: READY after content audit.

Staff and instruments remain outside BattleSpec. AutoPTU may establish only:

`IMMEDIATE_COUNT_STATION_ACCESS_CLEAR`

That does not complete a count or produce demographic evidence.

## Adapter authority

Minecraft/Cobblemon/Craftics may present an already-authored population state through crowd density, queues, occupied buildings, temporary camps, event traffic and quieter seasonal periods.

They may not decide population by counting loaded entities.

They may not convert NPC spawn/despawn into birth, death, migration or residence changes.

They may not infer a household from co-location.

They may not classify visitors as residents.

They may not treat visible battle spectators as an electorate or supporter membership.

They may not add wild Pokémon to a human settlement count because they happen to spawn inside municipal geometry.

## Readiness conclusion

PR #306 closes an important implementation gap by binding the tested post-hit forced-movement seam into BattleRuntime. That should be recorded as concrete progress, not generalized into a completed movement category.

Pass 166 therefore keeps the permanent classification unchanged.

The new population-continuity architecture can operate independently of combat. Its reduced encounter variants remain feasible because all demographic, civilian and record-state semantics stay outside BattleSpec and AutoPTU returns only narrow local tactical facts.