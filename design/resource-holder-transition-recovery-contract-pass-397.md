# Resource holder-transition recovery contract — Pass 397

Status: IMPLEMENTED PROVISIONAL CONTRACT
Date: 2026-09-10

## Scope

Pass 397 adds `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1` through `tools/resource_holder_transition_checkpoint.py`.

The checkpoint makes the Pass 396 holder-transition journal durable across restart without merging it into the mutable `WorldResource` catalog, reservation history or custody-transfer history.

## Recovery ownership

`WorldResource` remains authority for current operational resource state.

`ReservationLedger` remains authority for reservation claims.

`ResourceHandoffLedger` remains authority for authorized custody transfers.

`ResourceHolderTransitionLedger` remains authority only for explicit holder mutations that were routed through its wrappers.

`OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1` owns recovery of that journal generation.

## Snapshot payload

The checkpoint stores:

- schema identity;
- semantic minute of the recovery cut;
- immutable holder-transition records;
- deterministic SHA-256 over the canonical payload.

Each holder transition preserves:

- transition ID;
- resource ID;
- transition kind;
- prior holder;
- next holder;
- semantic tick;
- optional location;
- optional causal source reference.

Records use deterministic resource/time/ID ordering in the serialized checkpoint.

## Restore validation

Restore rejects:

- an unsupported schema;
- missing or mismatched digest;
- invalid semantic minute;
- a checkpoint from after the requested recovery time;
- malformed transition records;
- unknown transition kinds;
- duplicate transition IDs;
- same-resource non-increasing semantic order;
- same-resource holder continuity breaks;
- noncanonical serialized record order.

The outer digest therefore does not replace semantic validation.

## Authority limitation

This checkpoint does not claim universal holder-history completeness yet.

Pass 396 identified the currently known production mutations and routed them through journal-aware wrappers, but future or external mutation paths could still bypass them. Recovery durability is necessary before the journal can strengthen post-restore reconciliation, but universal authority additionally requires an audit proving that every production holder mutation passes through the journal.

`RECOVERED_JOURNAL != PROVEN_COMPLETE_JOURNAL`

## Integration boundary

Pass 397 does not yet add this checkpoint to `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2` and does not change Pass 395 activation gating.

The next safe integration step is a new manifest generation that selects, at one semantic cut:

- global NPC state;
- persistent-world evidence;
- current `WorldResource` catalog;
- holder-transition history.

Only after that same-generation binding exists should post-restore reconciliation use the recovered holder journal to upgrade cases from `INDETERMINATE` to `CONFIRMED` or `CONFLICT`.

## Narrative rule

Facts recorded inside a valid recovered journal remain facts after restart.

Events after the selected checkpoint remain unknown unless another recovered owner proves them. Missing post-checkpoint history must not become theft, teleportation, deception, negligence or a fabricated handoff.

## Engine boundary

Holder-transition recovery is persistent-world bookkeeping. It requires no AutoPTU tactical implementation.

Any encounter layered on top of the recovered history must continue to declare its exact permanent capability dependencies. Switching parity or one implemented Ability path does not imply complete movement, lifecycle, hazards, Items, Trainer Features, tactical policy or adapter support.
