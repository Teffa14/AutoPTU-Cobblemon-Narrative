# Cobblemon entity save/load reconciliation contract

Status: IMPLEMENTATION CONTRACT / NON-CANON
Pass: 252
Canon effect: NONE

## Purpose

Preserve one Ouros persistent wild actor across Minecraft save, chunk unload, load and restart without allowing a serialized `PokemonEntity` to create ecological truth.

This contract extends the population/projection boundary from Pass 239 and the BestSpawner admission boundary from Pass 250–251.

## Authority rule

Ouros owns persistent actor identity, population membership, demographic state, projection leases and ecology.

Cobblemon owns physical `PokemonEntity` presentation and serialization mechanics.

A Minecraft save record is a correlation carrier. It is never the authoritative wild-population ledger.

AutoPTU remains outside this path unless the Pass 242 encounter evaluator later returns `OPEN_AUTOPTU` and a combatant manifest is frozen.

## Source-verified Cobblemon 1.7.3 surfaces

`CobblemonEvents.POKEMON_ENTITY_SAVE` is posted from `PokemonEntity.saveWithoutId(...)` with the NBT compound before the method returns.

`CobblemonEvents.POKEMON_ENTITY_LOAD` is posted from `PokemonEntity.load(...)` with the loaded entity and NBT compound.

The load observable is cancellable. Cobblemon discards the entity when that event is cancelled.

`PokemonEntity.spawnCause` is explicitly transient across chunk unload and must not be used as restore identity.

These are source-verified upstream 1.7.3 facts. The actual Ouros runtime version/loader pin remains unresolved.

## Projection receipt

A managed direct projection may serialize a minimal namespaced receipt:

`schema_version`

`persistent_actor_id`

`projection_lease_id`

`scope_id`

`projection_epoch`

The receipt contains no PTU battle authority, hidden ecology totals, encounter outcome or demographic instruction.

The persistent actor ID is internal adapter metadata. It must not be exposed through normal player observation surfaces.

## Save path

When `POKEMON_ENTITY_SAVE` fires for an Ouros-managed direct projection:

1. resolve the Minecraft UUID to one current projection lease;
2. resolve that lease to one counted persistent source;
3. verify the entity species/form is compatible with the source;
4. write the projection receipt into an Ouros-namespaced NBT compound;
5. do not modify population, demographics or encounter history merely because serialization occurred.

If the live entity has no authoritative projection mapping, the adapter must not manufacture a receipt from species, location or UUID.

## Load path

When `POKEMON_ENTITY_LOAD` fires, classify before granting managed-wild authority.

`RECONCILE_EXISTING_PROJECTION`

Use when the receipt resolves to the same persistent actor, compatible species/form, scope and a lease whose persistence state permits restore. Bind the loaded Minecraft UUID to that lease. Population delta remains zero.

`REJECT_STALE_OR_CONFLICTING_RECEIPT`

Use when actor, lease, scope, epoch, species/form or current projection ownership conflicts with the authoritative ledger. Cancel/discard the physical entity. Do not repair the mismatch by creating an actor or demographic event.

`UNCLAIMED_LOAD`

Use when no Ouros receipt exists. The entity receives no wild ecological authority by inference. If another explicit lifecycle contract identifies it as owned/system presentation, route there. Otherwise a PokemonEntity loading inside a managed ecological scope is fail-closed until classified.

`DUPLICATE_PROJECTION`

If another live entity already owns the actor/lease, the second loaded entity is rejected. One persistent member cannot have two authoritative direct presentations.

## Restart and lease state

Runtime-only admission tokens are not durable and must be cleared at restart.

A projection lease may be represented as `ACTIVE`, `SUSPENDED_FOR_RESTORE` or `RELEASED` by the Ouros ledger. Persisted Minecraft NBT cannot promote a released lease back to active.

If a saved entity cannot be safely reconciled, Ouros may release the stale presentation and later create a fresh direct projection through the validated BestSpawner admission path. The new Minecraft UUID still maps to the same persistent actor.

## Failure rules

Save/load never changes population total by itself.

Chunk unload is not emigration.

Entity discard is not mortality.

Missing NBT metadata is not evidence that a new wild Pokemon exists.

A receipt mismatch is not evidence that the persistent actor disappeared.

A reloaded entity is not AutoPTU-eligible solely because it is physically present.

Minecraft/Cobblemon HP, status, battle flags or movement state do not overwrite AutoPTU authority.

## Reduced narrative version

The same Fletchling can disappear with chunk unload or restart and later be presented again as the same Ouros actor. The player can build a history of sightings without any tactical battle. Required engine family: Minecraft/Cobblemon/Craftics adapter/playback only.

## Full encounter version

A later resighting can become a pursuit, interception or structured confrontation. Add complete movement when interception/forced movement matters; full lifecycle for tactical timing; AI legal-action infrastructure plus AI tactical policy for autonomous tactical choices. Add terrain/weather/hazards/zones/reactions, damage/status, Moves, Abilities, Items or Trainer Features only when the encounter actually invokes those mechanics.

## Upgrade gate

Before runtime implementation is declared verified, prove against the actual dependency pin that:

- the save callback can attach the namespaced receipt and it survives world serialization;
- the load callback can read it before the entity becomes interactable as managed wild presentation;
- cancellation/discard prevents the invalid loaded entity from producing capture/battle/ecology effects;
- owned/system save-load paths remain distinguishable and are not absorbed into wild ecology;
- duplicate receipt claims fail closed;
- restart clears admission tokens but preserves authoritative actor/lease state as designed.
