# Engine readiness snapshot — Pass 251

Status: EVIDENCE SNAPSHOT
Canon effect: NONE
Date: 2026-09-04

## Narrative-repo result

Pass 251 narrows the Cobblemon admission seam to the upstream 1.7.3 path actually verified by source.

The important correction is that `CobblemonEvents.POKEMON_ENTITY_SPAWN` is the PokemonEntity-filtered view of `ENTITY_SPAWN`, while `SpawnEvent` itself documents a `BestSpawner` scope. It must not be treated as a universal hook for every PokemonEntity lifecycle path.

The Pass 250 contract, fixture, replay and regression tests were corrected accordingly. A versioned compatibility profile now freezes what is verified, what is explicitly not claimed, and which entity-creation paths remain unresolved.

## Cobblemon 1.7.3 compatibility evidence

SOURCE VERIFIED:

- `ENTITY_SPAWN` is cancellable.
- `POKEMON_ENTITY_SPAWN` filters that event to PokemonEntity.
- `SpawnEvent` is documented for BestSpawner-created entities.
- `SingleEntitySpawnAction.run()` posts the event before `world.addFreshEntity` and only inserts the entity when the event succeeds.
- `PokemonSpawnAction` extends the single-entity action path.
- `POKEMON_SENT_PRE` and `POKEMON_SENT_POST` provide a distinct owned party send-out lifecycle surface.

DOCUMENTATION VERIFIED:

- Spawn Rules `filter` and `location` components can reject spawn candidates/locations early.

UNRESOLVED FOR OUROS RUNTIME:

- actual Cobblemon version pin;
- actual loader and Minecraft version pin;
- the concrete API call used by Ouros to request a projection through the validated path;
- save/load/restore reconciliation;
- command-created Pokemon;
- fishing/bait/snack integration semantics;
- third-party entity creation paths;
- whether `SpawnCause` metadata is sufficient and stable for the final classifier.

Therefore Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL/BLOCKING end-to-end.

## Live AutoPTU-Java evidence

Read-only head inspected: `4e5ff6bbd6637d46598bce99e1dccf77f81ee9e8`.

Latest commit: `Run Java landing contract in forced movement parity gate (#340)`.

The change runs the Java landing consequence/public hazard event regression in the forced-movement trap parity workflow. This strengthens automated evidence for that exact forced-movement landing seam. It does not demonstrate complete movement, all terrain/hazard behavior, reactions, status lifecycle or all ability interactions.

## Live Python AutoPTU evidence

Read-only head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Latest change is presentation-only coordinate synchronization after viewport resize. It adds no new PTU rules evidence.

## Permanent capability audit

Targeting / footprints / range / LoS: VERIFIED within audited contracts.

Base movement legality: VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Representative forced-movement and landing slices exist; full-family parity is not established.

Core calculations: VERIFIED within audited deterministic contracts.

Action economy / initiative: VERIFIED within audited contracts.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING. Specific trap landing semantics have evidence; the family is not complete.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING as a complete family.

Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end. Pass 251 removes an unsafe universal-event assumption and source-verifies one upstream BestSpawner seam, but the writable runtime integration and dependency pin are still missing from evidence.

## Encounter dependency consequence

Reduced ecology presentation using indirect signs plus a direct BestSpawner projection does not require AutoPTU tactical mechanics. Its blocker is adapter implementation/version binding.

A pursuit or interception encounter after direct admission requires base movement and, when interception/forced movement matters, complete movement. Structured timing requires action economy and lifecycle. Tactical autonomous behavior requires AI legal-action infrastructure plus AI tactical policy. Terrain/reactions, damage/statuses, Moves, Abilities, Items and Trainer Features are dependencies only when the specific encounter uses them.

## Highest-value next gap

Locate or establish the actual writable Ouros/Craftics integration repository and freeze its Cobblemon, Minecraft and loader versions. Then implement a small adapter harness against that pin proving three separate paths without inference:

1. generic BestSpawner wild candidate in a managed scope is rejected before world insertion;
2. Ouros-managed projection with counted source, lease and token is admitted exactly once;
3. owned party send-out remains outside the wild population gate and preserves normal gameplay.

After that, add restore/load reconciliation as a fourth path rather than assuming it behaves like natural spawning.
