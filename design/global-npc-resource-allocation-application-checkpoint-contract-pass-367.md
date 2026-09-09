# Global NPC resource allocation application checkpoint contract — Pass 367

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

## Purpose

Pass 367 adds `OUROS_NPC_RESOURCE_CHECKPOINT_V8` above the Pass 365 V7 allocation-decision checkpoint.

V8 persists Pass 349 application records after an authorized Pass 348 resolution has been operationally applied. The source reservation ledger remains the historical owner; application history records why an operational projection can differ from that source history.

## Ownership boundary

Pass 347 owns conflict admission. Pass 348 owns the institutional choice and authority evidence. Pass 349 owns application. Pass 339 owns reservation lifecycle. Pass 350 owns notice obligations. Communications owns transport/delivery. Memory and belief own actor knowledge. Custody remains independent.

Restore validates lineage between application, resolution, resource and reservations. It does not send notices, mutate the source reservation ledger, transfer custody or grant knowledge.

## Recovery invariants

Every application must reference a persisted Pass 348 resolution for the same resource. Its semantic tick cannot precede the decision. One resolution can be applied at most once and application IDs must be unique.

`SELECT_PROPOSED_WINDOW` requires `DISPLACE_CONFLICTING_RESERVATIONS` with the exact conflict set persisted in the decision and no retained reservation.

`SELECT_EXISTING_RESERVATION` requires `PRESERVE_SELECTED_RESERVATION`, no displacement set and the exact selected reservation from the decision.

`DEFER` requires `DEFER_NO_CHANGE` with no displaced or retained reservation.

Every conflict reservation referenced by the decision must still exist as historical evidence and must belong to the same resource. Restore deliberately does not require its current state to remain `ACTIVE`: a later legitimate release or cancellation cannot erase that the application occurred earlier. Pass 349 itself already required the conflict to be active at application time; reconstructing that prior state from a later scalar reservation state would be an unsafe inference.

Application ticks after the restored semantic minute fail closed.

## Migration

V7 and earlier checkpoints restore with an empty `ResourceAllocationApplicationLedger`. No application is inferred from a later reservation state, current availability, a notice, custody, memory or dialogue.

## Canon and mechanics boundary

This pass changes persistence architecture only. It introduces no PTU rule, Caelo fact, Move, Ability, Item, Trainer Feature or fictional allocation policy. Research and proposals remain outside canon.
