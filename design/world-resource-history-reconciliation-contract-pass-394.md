# World Resource History Reconciliation Contract — Pass 394

Status: DESIGN / EXECUTABLE CONTRACT. Not canon.
Date: 2026-09-09

## Purpose

Pass 392 made the complete mutable `WorldResource` catalog recoverable. Pass 393 bound that catalog to the same recovery generation as global-NPC state and persistent evidence. This pass defines the next cross-owner check: compare restored current resource state with known reservation and custody history without pretending those ledgers form a complete event stream for every resource mutation.

The executable owner is `tools/world_resource_history_reconciliation.py`.

## Authority boundary

Current operational truth remains owned by `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1`.

Historical temporal reservations remain owned by `ReservationLedger`.

Authorized custody-transfer history remains owned by `ResourceHandoffLedger`.

The reconciliation layer owns no resource state and mutates nothing. It produces findings only.

`CURRENT_RESOURCE_STATE != COMPLETE_RESOURCE_EVENT_HISTORY`

`LATEST_KNOWN_HANDOFF != NECESSARILY_CURRENT_HOLDER`

`ACTIVE_RESERVATION_HISTORY != AUTOMATIC_CATALOG_PROJECTION`

A checkout, return, service-state change or other legal world operation may change present state without creating a custody transfer. Therefore a holder mismatch against the latest handoff is not enough to declare corruption.

## Finding classes

`CONFIRMED` means current state agrees with a historical fact that can be compared directly.

`CONFLICT` means the supplied owners make two explicit claims that cannot both be true under the narrow contract being checked. V1 uses this only for explicit reservation-owner disagreement, multiple simultaneously active reservations, and a catalog record that declares `RESERVED` without any reserved actor.

`INDETERMINATE` means known history is insufficient to derive the current state. This is a valid recovery outcome and must not be silently upgraded to corruption or to a fabricated history.

A report is `safe_to_restore` when it contains no `CONFLICT`. Indeterminate evidence stays visible to later diagnostics or narrative systems.

## Reservation reconciliation

At a semantic minute, one active reservation with the same actor as `WorldResource.reserved_for_actor_id` is confirmed.

An active reservation and an explicit different `reserved_for_actor_id` are a conflict.

An active reservation with no projected catalog reservation is indeterminate because reservation projection is a separate operation.

A current reserved actor with no active reservation in the supplied history is indeterminate. The reconciler does not invent a missing reservation or clear the catalog field.

## Custody reconciliation

If the current holder equals the receiver in the latest known custody transfer at or before the recovery minute, that narrow relation is confirmed.

If the current holder differs, the result is indeterminate. The system must not rewind the object to the latest transfer receiver, because return, checkout or other state changes may have occurred after that transfer.

A historical resource ID absent from the current catalog is also indeterminate in V1. The project has not yet established a universal retention/deletion rule for retired catalog identities, so absence alone cannot prove corruption.

## Recovery use

This layer is intended to run after the existing owners have individually restored and validated their own schemas, digests and semantic-time constraints.

It must not replace `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2`. The manifest selects one coherent generation. This layer then checks cross-owner facts inside that selected generation.

## Narrative value

The distinction supports ordinary institutional disagreement without requiring a hidden liar. A dispatcher may hold a valid reservation record while a depot snapshot is not yet projected. A custody ledger may correctly show the last formal transfer while the object has since been returned through another legal path. NPC knowledge must still depend on the records each actor actually received.

## PTU / AutoPTU boundary

This is world-state and recovery infrastructure. It introduces no PTU Skill check, Item effect, Trainer Feature, combat action or tactical legality.

Any later encounter that turns resource recovery into an active battle objective must classify exact dependencies using the permanent engine capability families. The world reconciler cannot simulate missing AutoPTU rules.

## Deferred work

Future work may add stronger proofs only when the project has authoritative history for the relevant mutation family. In particular, a complete holder transition journal could permit stronger custody validation, but V1 deliberately does not infer one from the ledgers that currently exist.
