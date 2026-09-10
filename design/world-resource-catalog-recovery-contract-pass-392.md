# World Resource Catalog Recovery Contract — Pass 392

Status: DESIGN / IMPLEMENTED. Not canon.
Date: 2026-09-09

## Purpose

Pass 392 gives the complete mutable `WorldResource` catalog an explicit recovery owner.

Before this pass, resource state existed as live values consumed by readiness, recovery, reservations and handoffs, while checkpoints preserved related ledgers without owning the complete current catalog. That left restart capable of recovering histories without one authoritative snapshot of current resource state.

`OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` closes that gap.

## Ownership boundary

The catalog checkpoint owns the current operational projection of every declared `WorldResource` at one semantic minute:

- stable `resource_id`;
- capability references;
- quantity;
- current `ResourceState`;
- current location;
- current holder;
- current reservation target.

It does not own the historical reason for those values.

`ResourceRequestLedger` remains authority for requests.

`ResourceReservationLedger` remains authority for reservation lifecycle history.

`ResourceHandoffLedger` remains authority for authorized custody-transfer history.

Site-evidence owners remain authority for discovery context and portable-find provenance.

Therefore recovery keeps these distinctions:

`CURRENT_RESOURCE_STATE != CUSTODY_HISTORY`

`CURRENT_RESOURCE_STATE != REQUEST_HISTORY`

`CURRENT_RESOURCE_STATE != DISCOVERY_PROVENANCE`

A current holder field can be restored without inventing a transfer that was never recorded. Conversely, a historical handoff does not by itself authorize reconstruction of arbitrary later current state.

## Snapshot contract

`snapshot_world_resource_catalog()` serializes the whole supplied catalog in canonical `resource_id` order. Capability references are sorted. Duplicate resource IDs are rejected. The payload is bound by SHA-256 and carries a non-negative semantic minute.

The checkpoint is a complete generation, not a patch or event log.

## Restore contract

`restore_world_resource_catalog()` validates schema and digest before reconstructing resources. It rejects duplicate identities, malformed state values, malformed references, duplicate capability refs and non-canonical record order.

When a recovery semantic minute is supplied, a checkpoint from a later minute is rejected.

V1 deliberately cannot prove when an individual mutable field changed because `WorldResource` does not currently carry per-field mutation time. The checkpoint only proves the complete catalog image selected at its own semantic boundary.

## Why custody is not copied

`execute_authorized_handoff()` already mutates the live `WorldResource` holder/location while separately appending an immutable `ResourceCustodyTransfer`. Copying those transfers into this checkpoint would create another custody authority and permit the two histories to diverge.

Future recovery should instead bind compatible owner generations by digest and semantic time, then let each owner perform its own semantic checks.

## Outer manifest seam

Pass 391 introduced `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1` for global-NPC V19 plus persistent-world-evidence V2.

Pass 392 intentionally does not extend that manifest in the same slice. The new owner first needs independent regression evidence. A later manifest version can bind its SHA-256 alongside the existing owners at the same semantic minute.

That future extension must not infer missing resource history from the current catalog.

## Minecraft and AutoPTU boundary

A Minecraft block/entity representation is not the catalog authority. Adapter state must acknowledge or project authoritative resource identity and state rather than independently deciding holder, availability or ownership.

A `WorldResource` may refer to equipment useful during a tactical encounter, but this checkpoint does not grant PTU Item legality, resolve use effects or own battle state. AutoPTU remains authoritative for structured tactical resolution.
