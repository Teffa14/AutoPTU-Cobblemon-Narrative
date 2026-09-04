# Engine readiness snapshot — Pass 252

Status: EVIDENCE SNAPSHOT
Canon effect: NONE
Date: 2026-09-04

## Narrative-repo result

Pass 252 source-verifies a Cobblemon 1.7.3 save/load seam for managed wild presentation continuity and adds a non-canon Marea fixture plus regression tests.

The key boundary is that serialized entity data can carry projection correlation evidence, but it cannot become the Ouros population ledger. A valid load receipt reconciles to an existing actor/lease. A stale, conflicting or unclaimed managed load fails closed and produces no demographic event or AutoPTU eligibility.

## Cobblemon 1.7.3 source evidence

SOURCE VERIFIED:

- `PokemonEntity.saveWithoutId(...)` posts `CobblemonEvents.POKEMON_ENTITY_SAVE` with the entity NBT before return.
- `PokemonEntity.load(...)` posts `CobblemonEvents.POKEMON_ENTITY_LOAD` after Cobblemon restores entity state.
- `POKEMON_ENTITY_LOAD` is cancellable and cancellation discards the entity.
- `PokemonEntity.spawnCause` is explicitly wiped by chunk unload and is not a durable restore identity.

CONTRACT DEFINED / RUNTIME UNVERIFIED:

- the Ouros namespaced projection receipt;
- exact round-trip survival of that receipt under the eventual runtime dependency pin;
- the ordering guarantee needed to prevent invalid restored entities from player interaction before reconciliation;
- owned/system load classification under the eventual adapter;
- persistence mechanism for the authoritative Ouros lease ledger itself.

The repository still does not establish the actual writable Ouros/Craftics runtime dependency pin. Adapter/playback therefore remains PARTIAL/BLOCKING end-to-end.

## Live AutoPTU-Java evidence

Read-only head inspected: `23ac19915d5b71bbae52d7e089741579527cdc81`.

Latest commit: `Freeze forced movement landing across move producers (#341)`.

This advances forced-movement landing parity across multiple move producers and adds a cross-producer landing gate. It strengthens the representative forced-movement family evidence, but does not establish complete movement as a whole. It does not prove all pushes, pulls, knockback, interception, reactions, terrain/hazard interactions or all producer-specific effects.

## Live Python AutoPTU evidence

Read-only head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Latest change remains presentation-only coordinate synchronization after viewport resize. It adds no PTU rules evidence.

## Permanent capability audit

Targeting / footprints / range / LoS: VERIFIED within audited contracts.

Base movement legality: VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Cross-producer forced-movement landing evidence improved in Java, but full-family parity is not established.

Core calculations: VERIFIED within audited deterministic contracts.

Action economy / initiative: VERIFIED within audited contracts.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING as a complete family.

Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end. Pass 252 identifies source-level save/load surfaces and a reconciliation contract but no writable runtime adapter implementation has yet been proven.

## Encounter dependency consequence

Reduced repeated-sighting continuity requires no AutoPTU tactical mechanics. It depends only on Minecraft/Cobblemon/Craftics adapter/playback and Ouros persistence/reconciliation.

A rich resighting that turns into pursuit/interception depends on complete movement and, if tactical timing is opened, full turn/round lifecycle. Autonomous tactical choices additionally require AI legal-action infrastructure and AI tactical policy. Add terrain/weather/hazards/zones/reactions, damage/status, Moves, Abilities, Items and Trainer Features only when the specific encounter invokes those families.

## Highest-value next gap

Locate or establish the writable Ouros/Craftics runtime integration and freeze its actual Cobblemon, Minecraft and loader versions. Then implement an adapter harness proving projection receipt save/load round-trip and fail-closed rejection before an invalid restored entity can create capture, battle or ecology effects.

A second useful slice is player-facing longitudinal recognition: repeated observations of the same actor should accumulate evidence and history without revealing persistent internal IDs or requiring a physical tag to be canon.
