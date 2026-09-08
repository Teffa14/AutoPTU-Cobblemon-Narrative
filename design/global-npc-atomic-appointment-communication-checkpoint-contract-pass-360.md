# Global NPC atomic appointment / communication checkpoint contract — Pass 360

Status: IMPLEMENTED DESIGN CONTRACT
Canon authority: NONE
Date: 2026-09-08

## Purpose

Advance the coherent world/resource checkpoint through Pass 345 appointment notices without duplicating Communications ownership.

Pass 359 proved that authored appointment notices can persist in `OUROS_NPC_RESOURCE_CHECKPOINT_V4`. Pass 352 proved that `InformationEventQueue` can preserve addressable envelope provenance after terminal delivery. Pass 360 composes those facts in one restore boundary.

## Schema

`OUROS_NPC_WORLD_CHECKPOINT_V9`

The V9 world checkpoint contains the existing V5 world payload plus a resource bundle. When the appointment owner is supplied, that bundle uses V4 and preserves Pass 339 reservations, Pass 342 requests and request events, Pass 343 handoff authorizations and custody transfers, Pass 344 failed handoff attempts and Pass 345 authored appointment notices.

For compatibility with existing V8-era callers that intentionally do not supply an appointment ledger, V9 may embed the V3 resource shape. Restore then returns an explicit empty `ResourceHandoffAppointmentLedger`. It does not infer missing appointment history.

The world payload remains the owner of the information queue and its delivery state.

## Restore invariant

For every restored `ResourceHandoffAppointmentNotice`, `communication_event_id` must resolve through the restored `InformationEventQueue.envelope_provenance()`.

The envelope must match the resource-side notice on sender actor, receiver actor, source claim and authored/created semantic minute. A mismatch fails closed. Restore does not rewrite either owner to make them agree.

## Delivery ownership boundary

`ResourceHandoffAppointmentLedger` records that a notice was authored and associates it with a communication event identity.

`InformationEventQueue` owns whether that event is queued, waiting for local acknowledgement, delivered or terminally failed.

`NOTICE_AUTHORED != NOTICE_DELIVERED`

`COMMUNICATION_EVENT_EXISTS != CORRECT_RECIPIENT`

`DELIVERED_TO_SOMEONE != DELIVERED_TO_INTENDED_APPOINTMENT_PARTICIPANT`

Pass 360 validates cross-owner provenance after both subsystems are restored. It does not copy `DeliveryStatus` into the resource checkpoint.

## Backward compatibility

V8 contains Pass 339/342/343/344 history but did not persist Pass 345 appointment notices. Restoring V8 therefore yields an explicit empty `ResourceHandoffAppointmentLedger`.

V7 restores handoff history with empty attempt and appointment ledgers. V6 restores reservations and requests with empty handoff, attempt and appointment ledgers. V1–V5 world-only saves restore all resource ledgers empty.

A V9 payload containing V3 means the caller did not supply appointment history. It is treated the same way: existing V3 facts are restored and appointment history remains explicitly empty.

No migration infers a missing notice from current memory, custody, actor location, later dialogue, communication content or delivery history.

## Temporal boundary

Resource V4 already rejects authored notices from after the checkpoint semantic minute. V9 additionally requires the corresponding communication envelope to carry the same creation minute as the authored notice.

The checkpoint may contain a notice whose actual delivery is still in the future if the queued communication event was already created by the checkpoint time. That is legitimate pending work, not future-state contamination.

## Idempotency

Restore reconstructs ledgers and queues. It never calls request acceptance, handoff authorization, handoff execution, failed-attempt registration, appointment notice registration, information scheduling or information delivery.

A second restore produces the same historical state without another message or custody mutation.

## Fail-closed cases

Restore rejects missing appointment communication provenance; sender, receiver, source-claim or creation-time mismatches; unsupported nested resource schemas; invalid global digests; and any pre-existing V4 resource validation failure.

## Narrative consequence

This contract allows Ouros to preserve the difference between a real appointment notice and a correctly addressed communication. After a restart, an NPC can reasonably act from stale information if the real notice was sent elsewhere or never entered Communications, while the world still preserves who authored what and when.

## Mechanical boundary

This persistence contract requires no AutoPTU capability. Any later tactical interruption spawned from the appointment or pickup remains separately gated by the permanent engine capability categories.
