# Global NPC world resource allocation notice checkpoint contract — Pass 370

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08
Canon effect: NONE

## Purpose

Pass 370 introduces `OUROS_NPC_WORLD_CHECKPOINT_V14` and closes the recovery seam between Pass 350 notice ownership and the Communications owner already preserved by the world checkpoint.

V14 places allocation-notice obligations and notice-to-communication links in the same global digest as semantic time, NPC state, knowledge ledgers, `InformationEventQueue`, reservations, rescheduling, historical conflict admission, allocation authority/resolution and Pass 349 application.

The transport queue remains authoritative for message state and address provenance.

## Owner boundaries

Pass 349 owns operational application.

Pass 350 owns the obligation to inform an affected displaced reservation holder and the stable link from that obligation to one communication event.

Pass 351 owns the sender/receiver binding rule.

Pass 352 makes terminal envelope provenance addressable after successful or failed transport.

`InformationEventQueue` owns `QUEUED`, `WAITING_LOCAL_ACK`, `DELIVERED` and terminal failure state.

Memory/belief remains owner of what an NPC knows or can recall. Replanning remains a later consequence.

## V14 invariant

For every persisted `ResourceAllocationNoticeLink`, recovery requires all of the following:

- its obligation is valid under the V9 standalone resource checkpoint;
- its communication event exists in the restored transport status map;
- `InformationEventQueue.envelope_provenance(event_id)` returns the real envelope;
- the envelope sender equals the sender recorded by the notice link;
- the envelope receiver equals the affected actor recorded by the notice obligation;
- the link timestamp does not predate message authorship;
- the notice obligation and link do not occur after the recovered semantic minute.

The envelope may be pending, awaiting local acknowledgement, delivered or terminally failed. Provenance validates which message was linked. Delivery status answers a separate question.

## Failure semantics

A terminal `FAILED_CHANNEL_UNAVAILABLE` event can remain correctly linked to an obligation. The world therefore remembers that a real attempt was made to the correct holder while also remembering that the holder did not receive the claim.

A delivered envelope addressed to the wrong actor remains a real world communication, but it cannot satisfy the affected holder's notice binding.

A missing terminal archive entry cannot be repaired by looking at a status string, current memory, a changed reservation or later behavior. V14 fails closed.

## Migration

V13 and older coherent world checkpoints restore through the existing migration chain with an empty `ResourceAllocationNoticeLedger`.

No notice obligation or link is reconstructed from current calendar state, archived messages, custody, beliefs, dialogue or travel.

## Explicit semantic boundaries

`ALLOCATION_APPLIED != NOTICE_REQUIRED`

`NOTICE_REQUIRED != MESSAGE_LINKED`

`MESSAGE_LINKED != MESSAGE_DELIVERED`

`MESSAGE_FAILED != MESSAGE_DELIVERED`

`MESSAGE_DELIVERED != CURRENT_RECALL`

`CURRENT_RECALL != PLAN_CHANGED`

## Test coverage

`tests/test_global_npc_world_resource_allocation_notice_checkpoint.py` covers successful terminal delivery, terminal channel failure without fake knowledge, sender tampering under a recalculated digest, missing terminal provenance under a recalculated digest, V13 migration and semantic-time rejection.

## PTU/Caelo boundary

This contract adds no PTU rule, Caelo rule, Move, Ability, Item, Trainer Feature, species behavior or setting fact. Supplied PTU/Caelo material remains the governing source set for mechanical claims. Research and proposals remain non-canon unless promoted through the existing canon process.
