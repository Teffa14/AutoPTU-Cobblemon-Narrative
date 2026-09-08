# Global NPC world resource allocation checkpoint contract — Pass 366

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

## Purpose

Pass 366 adds `OUROS_NPC_WORLD_CHECKPOINT_V12` above the Pass 364 V11 world admission checkpoint and the Pass 365 V7 standalone allocation checkpoint.

V12 preserves Pass 348 allocation authority and resolution provenance inside the same global digest as semantic time, NPC state, communications, reservations, requests, handoff history, appointments, reschedule lineage and Pass 347 historical conflict admission.

## Ownership boundary

Pass 347 owns the observed conflict. Pass 348 owns the institutional decision and authority evidence. Pass 349 owns operational application. Communications owns message transport and delivery. Memory/belief owns private knowledge.

Restore validates the owners together. It does not execute Pass 349, mutate reservations to match a decision, deliver a message, or teach the decision to an NPC.

## Recovery invariants

A V12 allocation resolution must still have matching historical conflict admission in the same resource snapshot. Its authority evidence must identify the decision actor, `ALLOCATE_RESOURCE_WINDOW` scope, target resource, authorized state and a time window current when the decision was made. Allocation authority and resolution ticks cannot occur after the restored semantic minute.

V12 delegates all earlier cross-owner checks to V11 after rebuilding the exact V6 admission-aware resource state. The reconstructed reservations, requests, handoffs, attempts, appointments, reschedules and admission ledger must match the V12 owners exactly.

The global digest covers the allocation records. Tampering without re-signing fails at the digest. A re-signed but causally invalid history fails during owner validation.

## Migration

V11 and earlier checkpoints restore through the existing recovery chain and return empty allocation authority and resolution history. No decision is inferred from current reservations, downstream application, communication, memory, dialogue or custody.

## Canon and mechanics boundary

This pass changes persistence architecture only. It establishes no PTU rule, Caelo fact, fictional resource-allocation policy, Move, Ability, Item or Trainer Feature.
