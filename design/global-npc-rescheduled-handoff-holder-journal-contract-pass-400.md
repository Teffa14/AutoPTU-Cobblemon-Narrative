# Global NPC Rescheduled Handoff Holder Journal Contract — Pass 400

Status: IMPLEMENTED / GLOBAL NPC RESOURCE SEAM
Canon effect: NONE

## Problem

Pass 396 introduced explicit holder-transition history for checkout, return and ordinary authorized handoff. Pass 399 then found that `execute_current_authorized_handoff()` in the rescheduling layer still called the lower-level physical handoff executor directly.

A successful rescheduled transfer could therefore change `WorldResource.holder_actor_id` and create `ResourceCustodyTransfer` while leaving no `ResourceHolderTransition`.

That gap prevents a universal holder-history completeness claim.

## Pass 400 boundary

`tools/global_npc_resource_handoff_rescheduling_holder.py` adds the holder-aware operational path:

`execute_current_authorized_handoff_with_holder_transition()`

The function performs two independent checks in sequence.

First, the reschedule ledger resolves whether the supplied authorization remains current. A superseded authorization fails closed and creates neither custody transfer nor holder event.

Second, a current authorization delegates to the existing holder-aware handoff executor. The holder event is written only when the underlying custody transfer succeeds.

The resulting transition records the exact transfer as `source_ref`.

## Authority ownership

The reschedule ledger owns successor/supersession state.

The handoff ledger owns handoff authorization and custody-transfer history.

The holder-transition ledger owns explicit holder mutation history.

The `WorldResource` catalog owns current resource state.

No one owner reconstructs the other histories.

## Failure behavior

Superseded authorization:

- resource unchanged;
- handoff ledger unchanged;
- holder ledger unchanged;
- reason `HANDOFF_AUTHORIZATION_SUPERSEDED`.

Current authorization with invalid handoff facts:

- underlying handoff validation rejects the transfer;
- resource unchanged;
- no holder transition recorded.

Accepted current authorization:

- custody transfer is recorded;
- holder changes to the receiving actor;
- exactly one `HANDOFF` holder transition is recorded with the custody transfer ID as provenance.

## Completeness boundary

Pass 400 closes a safe journal-aware path for rescheduled handoffs. It does not yet delete or rewrite the older `execute_current_authorized_handoff()` compatibility function in `global_npc_resource_handoff_rescheduling.py`.

Therefore global holder-history completeness is still not automatic. Production callers must migrate to the holder-aware operation before a resource traversing the reschedule subsystem can enter `complete_holder_history_resource_ids` without an external audit guarantee.

A later pass should either remove the legacy mutation path or make it incapable of performing a holder mutation without the journal owner.

## Regression requirements

The Pass 400 regression verifies:

- current successor authorization produces both custody transfer and holder transition;
- the holder transition preserves from/to actors, semantic tick and source transfer ID;
- a superseded authorization produces no custody or holder event;
- a current authorization that fails physical handoff validation produces no holder event.

## Tactical boundary

This world-layer contract grants no PTU mechanic. Carrying, interception, forced movement, tactical item effects, rescue priorities or battle objectives remain delegated to their exact AutoPTU capability families.
