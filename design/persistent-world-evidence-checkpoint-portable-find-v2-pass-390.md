# Persistent World Evidence Checkpoint V2 — Portable-Find Binding Integration

Status: IMPLEMENTED DESIGN CONTRACT. Not canon.
Date: 2026-09-09

## Purpose

Pass 390 extends persistent-world evidence recovery to preserve the executable `PORTABLE_FIND` → `WorldResource` identity relation introduced in Pass 389.

Schema: `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2`.

Owner: `tools/persistent_world_evidence_checkpoint.py`.

The checkpoint continues to own evidence history and evidence bridges. It does not become the owner of private NPC memory or mutable world-resource state.

## Authority boundaries

`SiteEvidenceLedger` owns historical discovery context.

`PortableFindResourceBindingLedger` owns the explicit cross-system identity relation.

`KnowledgeLedgerStore` owns private NPC claims.

`WorldResource` plus existing resource/custody owners remain authoritative for holder, location, reservation, quantity, operational state and authorized handoffs.

Therefore:

`DISCOVERY_CONTEXT != PORTABLE_IDENTITY_BINDING != CURRENT_RESOURCE_STATE != CUSTODY_HISTORY`

## V2 payload

V2 records:

- semantic minute;
- site evidence snapshot;
- direct-observation knowledge bridge snapshot;
- interpretation/inference knowledge bridge snapshot;
- portable-find resource-binding snapshot;
- SHA-256 of the external private `KnowledgeLedgerStore` snapshot;
- SHA-256 of the stable declared-resource identity catalog.

The declared-resource digest contains sorted stable `resource_id` values only after validating each mapping key against the resource's own ID.

It deliberately excludes holder, location, reservation, quantity, capability set and operational state. Those values can legitimately evolve without changing the fact that one historical find observation refers to the same physical resource identity.

## Recovery rules

V2 restore fails closed when:

- the outer checkpoint digest is invalid;
- private knowledge differs from the snapshot against which evidence bridges were built;
- the declared resource identity set differs;
- the portable binding snapshot has the wrong schema;
- a bound observation is missing or no longer `PORTABLE_FIND`;
- historical observation provenance changed;
- a bound resource identity is missing;
- binding time is later than checkpoint time;
- any existing site-evidence or knowledge-bridge validation fails.

Re-signing a semantically tampered checkpoint does not bypass owner-level validation.

## Mutable resource-state rule

A resource may move after a checkpoint was built and still satisfy this evidence checkpoint if its stable `resource_id` remains in the supplied catalog.

Examples that do not alter archaeological identity:

- holder changes from field researcher to curator;
- location changes from site to receiving room;
- state changes from AVAILABLE to IN_USE;
- reservations change;
- custody handoffs accumulate in their own ledger.

The evidence checkpoint must not reject those changes merely because they occurred outside its authority.

## Legacy recovery

`OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1` remains restorable.

V1 recovery creates an empty `PortableFindResourceBindingLedger` and carries no declared-resource identity digest. It does not infer historical bindings from current resource location, custody history, matching labels or later archive records.

`V1_ABSENCE != PROOF_NO_BINDING_OCCURRED`

It means only that the older checkpoint did not own that relation.

## Outer recovery boundary

V2 still does not solve global crash-coherence for all owners.

A later recovery manifest should bind, by digest and semantic time, the global-NPC checkpoint, persistent-world evidence checkpoint, resource/custody recovery units and any future canonical resource-catalog owner.

Until a complete resource catalog has its own recovery owner, V2 proves compatibility with an explicitly supplied set of stable resource identities only.
