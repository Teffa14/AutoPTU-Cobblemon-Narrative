# Global NPC resource handoff checkpoint contract — Pass 355

Status: IMPLEMENTED / NON-CANON INFRASTRUCTURE
Date: 2026-09-08

## Purpose

Pass 353 created `OUROS_NPC_RESOURCE_CHECKPOINT_V1` for reservations and resource requests. Pass 354 placed that bundle inside the coherent V6 world checkpoint. Pass 355 extends the standalone resource persistence boundary to handoff authorization and completed custody transfer history.

The new standalone schema is `OUROS_NPC_RESOURCE_CHECKPOINT_V2`.

This pass does not yet advance the global world checkpoint beyond V6. V2 is deliberately validated first as an isolated resource codec before later atomic integration.

## Owners preserved

Pass 355 does not replace or duplicate these owners:

- Pass 339 remains owner of reservations.
- Pass 342 remains owner of resource requests and their state transitions.
- Pass 343 remains owner of handoff authorization and custody transfer semantics.
- `tools/global_npc_resource_checkpoint.py` owns only serialization, restore validation and semantic-time admissibility for these ledgers.

Restore never calls `execute_authorized_handoff` and never changes a `WorldResource` holder.

## V2 contents

The V2 resource checkpoint contains:

- reservations;
- resource requests;
- resource request events;
- handoff authorizations;
- custody transfers.

Authorization persistence includes request, provider, accountable actor, receiver, exact resource, handoff mode, place, validity window and authority provenance.

Transfer persistence includes authorization, request, resource, from/to actors, accountable actor, place, semantic time and optional condition provenance.

## Compatibility

`restore_resource_state_with_handoffs()` accepts V1. A V1 resource checkpoint restores its reservations and requests and returns an empty `ResourceHandoffLedger`.

It does not infer missing handoffs from:

- current resource holder;
- inventory state;
- NPC memory;
- dialogue;
- a later reservation;
- a later notice;
- a current location.

That absence is historical uncertainty, not permission to manufacture history.

## Cross-ledger validation

A restored handoff authorization must reference an existing resource request.

The provider must match the request provider.

The exact resource must match the accepted offered resource when an accepted request event names one; otherwise it must match the resource originally requested.

The authorization cannot predate request creation.

A restored custody transfer must reference a restored authorization. Its request, resource, provider, receiver, accountable actor and place must match that authorization exactly.

One authorization can be consumed by at most one custody transfer.

A transfer cannot occur before `valid_from_tick` or at/after `valid_until_tick` when the authorization has a closing bound.

Duplicate authorization IDs and duplicate transfer IDs fail closed.

## Semantic-time rule

A future authorization window is permitted. World actors may schedule a pickup that has not happened yet.

A completed custody transfer is an observed historical event. `validate_handoff_checkpoint_time()` therefore rejects any transfer whose `at_tick` is later than the checkpoint semantic minute.

This preserves the same distinction introduced in Pass 353 between prospective commitments and completed facts.

## Determinism

Serialization sorts authorizations by stable authorization ID and transfers by `(at_tick, transfer_id)`.

Equivalent ledger state must produce equivalent serialized order regardless of tuple insertion order.

## Narrative consequence

After restart, Ouros can distinguish these situations without inference:

- request accepted but no handoff authorized yet;
- handoff authorized for a future window;
- authorization exists but remains unused;
- authorized transfer completed;
- old V1 save contains no provable handoff history.

A current holder can therefore remain separate from the evidence explaining how custody changed.

## AutoPTU boundary

This checkpoint is world-state infrastructure. It does not implement tactical pickup, carrying, interception or transfer actions.

A mechanically rich handoff scene retains the permanent dependency categories:

- targeting/footprints/range/LoS for tactical target or interaction reach;
- base movement legality for ordinary positioning;
- complete movement for interception, forced movement, push/pull/knockback or carrier displacement;
- action economy/initiative for pickup/drop/handoff timing if represented as tactical actions;
- full turn/round lifecycle for round-bounded deadlines and interrupts;
- full stateful damage pipeline for damage to carrier or cargo when rules require it;
- status lifecycle for persistent conditions;
- terrain/weather/hazards/zones/reactions when present;
- Move-specific behavior, Abilities, Items and Trainer Features/perks individually;
- AI legal-action infrastructure for any new cargo interaction action;
- AI tactical policy for protect-carrier, intercept, delivery-first or disengage-after-objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback for authoritative presentation and acknowledgement.

No capability family becomes complete because the narrative checkpoint can remember a transfer.

## Deferred integration

The next durability seam is to integrate the validated V2 handoff bundle into a new coherent world checkpoint schema while retaining V6 compatibility. Failed attempts, appointments, reschedules, allocation and notice ledgers remain later incremental codecs and must receive their own cross-ledger validation rather than being serialized as opaque blobs.
