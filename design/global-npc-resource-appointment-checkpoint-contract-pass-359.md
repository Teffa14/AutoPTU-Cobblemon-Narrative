# Global NPC resource appointment checkpoint contract — Pass 359

Status: IMPLEMENTED ARCHITECTURE CONTRACT
Canon authority: NONE
Date: 2026-09-08

## Purpose

Pass 359 adds a durable checkpoint codec for the Pass 345 handoff-appointment notice ledger.

The checkpoint extends the existing resource history chain:

reservation -> request -> authorization -> failed attempt history -> authored appointment notice

It does not make the communication queue a resource owner and does not duplicate message delivery state.

## Schema

`OUROS_NPC_RESOURCE_CHECKPOINT_V4`

The V4 payload preserves the complete V3 resource checkpoint plus ordered `handoff_appointment_notices`.

Each notice preserves:

- notice identity;
- authorization identity;
- sender and receiver identity;
- `CONFIRM`, `CANCEL` or `RESCHEDULE_REQUEST` kind;
- source claim identity;
- communication event identity;
- authored semantic tick;
- optional reason provenance.

## Ownership boundary

`ResourceHandoffAppointmentLedger` owns the fact that a participant authored a coordination notice.

`InformationEventQueue` owns whether the associated communication event is queued, waiting for acknowledgement, delivered or failed.

The resource checkpoint therefore preserves `communication_event_id` but does not serialize a delivery status beside the notice.

`NOTICE_AUTHORED != NOTICE_DELIVERED`

`CONFIRM_AUTHORED != MUTUALLY_CONFIRMED`

`RESCHEDULE_REQUEST != RESCHEDULE_APPROVED`

`CANCEL_AUTHORED != RESOURCE_TRANSFERRED`

## Restore validation

Restore fails closed when:

- the V4 collection is malformed;
- notice IDs repeat;
- communication event IDs repeat inside the appointment ledger;
- a notice references an authorization absent from the restored handoff ledger;
- sender or receiver is not a participant in that authorization;
- a notice is authored at or after authorization expiry;
- a notice is authored at or after a custody transfer that already completed the authorization.

A notice may legitimately be authored before `valid_from_tick`; confirmations and coordination can occur before the pickup window opens.

A notice may also remain historically valid when a later custody transfer succeeds. Restore preserves both events when the notice predates the transfer.

## Semantic-time boundary

`created_tick` records an authored communicative act. It cannot be later than the semantic minute of the checkpoint that claims to contain it.

This differs from the authorization's future-valid window, which may be prospective.

## Backward compatibility

V1, V2 and V3 resource checkpoints restore through the V4 reader with an empty `ResourceHandoffAppointmentLedger`.

The loader does not infer old confirmations, cancellations or reschedule requests from:

- later custody state;
- NPC memory;
- current location;
- a successor authorization;
- dialogue;
- a communication event that lacks the historical appointment record.

Absence in an older checkpoint remains absence of persisted evidence.

## Communication cross-validation deferred to coherent world integration

The standalone resource codec cannot prove that `source_claim_id` and `communication_event_id` exist in the world information runtime because that runtime is outside this payload.

When V4 is integrated into the coherent world checkpoint, the integration layer should validate the notice against available queue/envelope provenance without copying delivery ownership into the resource subsystem.

## Canon boundary

This contract adds no regional institution, NPC obligation, service policy or PTU rule. Local proposals may use it as evidence infrastructure, but authored policy must still come from canon or remain explicitly proposed.
