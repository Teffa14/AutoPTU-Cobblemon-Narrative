# Global NPC terminal message envelope provenance contract — Pass 352

Status: IMPLEMENTED / GLOBAL WORLD-SIMULATION CONTRACT
Date: 2026-09-08
Canon effect: NONE

## Purpose

Preserve enough transport provenance after a communication event reaches a terminal state that later systems can safely reconstruct sender/receiver/message/channel identity without keeping the event in the live delivery queue.

This closes the post-delivery audit gap exposed by Pass 351.

## Owner boundary

`tools/global_npc_information_network.py` remains the transport owner.

Pass 352 adds terminal envelope retention to that existing owner. It does not create a second messaging system, a second memory system, or a resource-specific transport ledger.

`tools/global_npc_resource_allocation_notices.py` consumes this transport provenance. It does not own it.

## Terminal archive state

`InformationEventQueue.archived_envelopes` maps stable `event_id` to the immutable `InformationEnvelope` that reached a terminal queue state.

The retained envelope includes:

- event ID;
- message ID;
- sender ID;
- receiver ID;
- source claim ID;
- receiver claim ID;
- channel ID;
- authored minute;
- scheduled delivery minute;
- receiver trust input used for the transport operation.

The archive currently covers successful `DELIVERED` events and terminal `FAILED_CHANNEL_UNAVAILABLE` events, including local-projection rejection.

## Query contract

`InformationEventQueue.envelope_provenance(event_id)` resolves addressable transport metadata in this order:

1. awaiting-local-ack envelope;
2. pending envelope;
3. terminal archived envelope.

A caller therefore does not need to know whether the event is still live or already terminal in order to validate sender/receiver provenance.

The query returns no value when the transport owner has no inspectable envelope for that event.

## Invariants

### Terminal archive is immutable evidence

An existing archived event ID cannot be associated with a different envelope.

`ARCHIVED_EVENT_ID + DIFFERENT_ENVELOPE -> FAIL CLOSED`

### Delivery and archive are separate facts

An archived envelope may represent a failed terminal attempt.

`ARCHIVED_ENVELOPE != DELIVERED`

Callers must still inspect `DeliveryStatus`.

### Transport evidence does not prove message truth

A preserved envelope says which transport event the runtime processed. It does not prove that the source claim was objectively correct.

`TRANSPORT_PROVENANCE != WORLD_TRUTH`

### Transport evidence does not prove current recall

A successfully delivered claim may later be inaccessible under the existing memory-retrieval owner.

`DELIVERY_HISTORY != CURRENT_MEMORY_ACCESS`

### Transport evidence does not imply agreement

Receipt does not establish acceptance, compliance, consent, reservation release, handoff, relationship change, or belief certainty.

### Deception remains deception

`DeceptionInformationEventQueue` archives the same transport envelope while retaining its separate deceptive statement mapping and source-attribution store.

Restart cannot sanitize a deceptive delivery into an ordinary retransmission.

### Restart preserves terminal provenance

`InformationEventQueue.snapshot()` includes archived envelopes. Restore validates that every archived event has a known terminal status and a known channel.

Legacy queue snapshots that do not contain `archived_envelopes` remain readable and restore with an empty terminal archive.

## Resource-allocation notice integration

Pass 351 required a notice link to be created before final delivery because only pending/ack envelopes exposed sender and receiver.

Pass 352 changes that constraint.

`link_notice_communication()` now consumes `queue.envelope_provenance(event_id)`.

A notice can therefore be linked during a later audit after delivery or restart if and only if:

- the obligation exists;
- the communication event exists;
- envelope provenance exists;
- the declared sender matches the envelope sender;
- the affected reservation holder matches the envelope receiver;
- the link does not predate message authorship;
- the communication event is not already linked elsewhere.

A wrong-recipient terminal delivery remains invalid for the affected obligation.

## Persistence compatibility

The existing information queue snapshot schema identifier remains unchanged because the new archive field is additive and restore treats it as optional.

Any future schema migration must preserve the same semantic invariant: terminal transport provenance cannot disappear merely because the live queue no longer needs the envelope.

## Failure behavior

Restore fails closed when:

- an archived envelope references an unknown channel;
- an archived envelope has no corresponding queue status;
- its status is not terminal;
- the archived dictionary key and embedded event ID disagree.

Resource-notice linking fails closed when sender or receiver provenance does not match the obligation.

## Explicit non-goals

Pass 352 does not implement:

- read receipts distinct from the current managed-agent delivery semantics;
- human comprehension modeling;
- acknowledgement of agreement;
- retention/expiry policy for very large communication archives;
- archival indexing beyond stable event ID;
- full checkpoint integration for the newer resource ledgers;
- UI inspection tooling;
- Minecraft presentation of audit history;
- any new PTU battle mechanic.

## Test coverage

`tests/test_global_npc_information_terminal_provenance.py` covers:

- successful delivery archive;
- restart persistence;
- failed terminal channel attempt without fake delivery;
- deceptive delivery archive across deception-queue restart.

`tests/test_global_npc_resource_allocation_notice_binding.py` now covers safe post-delivery and post-restart allocation-notice binding through archived address provenance.
