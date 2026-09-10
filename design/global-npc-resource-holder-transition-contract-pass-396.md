# Global NPC resource holder-transition contract — Pass 396

Status: IMPLEMENTED PROVISIONAL CONTRACT
Date: 2026-09-10

## Scope

Pass 396 introduces `ResourceHolderTransitionLedger` in `tools/global_npc_resource_holder_transitions.py`.

The ledger records explicit changes to `WorldResource.holder_actor_id` for the three production mutation paths currently identified by repository inspection: reserved checkout, return and authorized handoff.

This pass does not claim that every future or external mutation path already uses the journal. Universal authority requires all holder-changing production callers plus recovery to route through this contract.

## Event identity

Each `ResourceHolderTransition` contains:

- stable `transition_id`;
- stable `resource_id`;
- transition kind: `CHECKOUT`, `RETURN` or `HANDOFF`;
- prior holder;
- next holder;
- semantic tick;
- optional location;
- optional causal `source_ref`.

Events are immutable.

## Continuity rules

For one resource, a later journaled transition must begin from the holder produced by the previous journaled transition.

Semantic ticks must increase strictly for successive holder changes of the same resource. V1 has no causal ordinal inside one tick, so two same-tick holder changes are rejected instead of being silently ordered by identifier.

Duplicate transition IDs are rejected.

Kind-specific holder shapes are enforced:

- checkout: no holder -> actor;
- return: actor -> no holder;
- handoff: actor -> distinct actor.

The ledger does not infer missing events to repair continuity.

## Mutation wrappers

`checkout_with_holder_transition` executes the existing reservation checkout and records the active reservation ID as causal source.

`return_with_holder_transition` executes the existing return operation and records the holder transition.

`execute_handoff_with_holder_transition` executes the existing authorized handoff. It adds a holder event only if the custody transfer succeeds and links the event to the existing transfer ID.

Failed handoffs do not create holder history.

## Authority boundary

`WorldResource` continues to own current operational resource state.

`ReservationLedger` continues to own temporal reservation claims.

`ResourceHandoffLedger` continues to own handoff authorization and custody-transfer history.

`ResourceHolderTransitionLedger` owns only the explicit causal sequence of holder mutations routed through it.

It does not own legal ownership, discovery provenance, resource capability, quantity, service state, reservation policy, private knowledge, custody authorization or Minecraft presentation.

A holder transition can reference a custody transfer without replacing it.

## Recovery boundary

Pass 396 does not yet add the journal to a checkpoint or the persistent-world recovery manifest. Therefore post-restore validation from Pass 395 cannot yet treat it as universally available.

The next recovery seam is a deterministic snapshot/restore owner for the journal followed by same-minute integration with the resource catalog and post-restore reconciliation.

Until that seam exists, Pass 394's conservative `INDETERMINATE` treatment remains correct when current holder cannot be derived from the older reservation/handoff ledgers alone.

## Narrative rule

A missing holder event remains missing evidence. It must not be converted into theft, deception, negligence, teleportation, ownership transfer or a fabricated handoff.

Once an authoritative recovered holder journal covers the relevant interval, an impossible current holder becomes a consistency failure rather than an automatically generated mystery.

## Engine boundary

Holder history is persistent-world bookkeeping and requires no AutoPTU battle implementation.

If a scene adds escort, forced movement, hazards, weather, timed phases, item effects, Trainer Feature interrupts or objective-aware AI, those exact permanent capability families remain separately gated.
