# Persistent World Recovery Manifest V2 Contract — Pass 393

Status: DESIGN / IMPLEMENTED. Not canon.
Date: 2026-09-09

## Purpose

Pass 393 extends coherent persistent-world recovery after Pass 392 gave the mutable `WorldResource` catalog its own checkpoint owner.

`OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2` selects one exact generation of three independent owners at one semantic minute:

- `OUROS_NPC_WORLD_CHECKPOINT_V19` global NPC / world-agent causal state;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2` persistent evidence, observation, interpretation and portable-find binding state;
- `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` current mutable resource state.

The manifest stores only owner digests plus semantic time. It does not copy owner payloads and does not become authority for their domain state.

## Recovery invariant

A valid owner snapshot is insufficient by itself. Recovery requires a compatible generation across all selected owners.

A world in which the NPC checkpoint says a field team already departed, the evidence checkpoint says the route closure has not yet been observed, and the resource checkpoint says the team's equipment is still available at the depot may be impossible even when all three snapshots pass their own integrity checks.

V2 prevents selecting that mixed generation.

## Build contract

`build_persistent_world_recovery_manifest()` requires the current schema for all three owners.

All three checkpoints must:

- carry a valid SHA-256 over their own payload;
- carry a non-negative semantic minute;
- use the same semantic minute.

The manifest then records the three supplied owner digests and signs its own canonical payload.

## Reconcile contract

`reconcile_persistent_world_recovery_manifest()` verifies:

- manifest schema and digest;
- candidate owner schemas and owner digests;
- exact semantic-minute equality;
- exact digest equality between each candidate and the manifest-selected generation.

It stops before domain restore. Each owner still runs its own semantic validation after selection.

`MANIFEST_SELECTION != DOMAIN_RESTORE`

## V1 compatibility

Legacy `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1` remains readable for its original two-owner recovery boundary.

V1 does not acquire a fabricated resource checkpoint during migration. Its reconciled result reports no resource-catalog digest.

A new V2 generation must be created only when a real `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` exists at the same semantic minute.

## Authority boundaries

Global NPC checkpoint owns causal world-agent state and histories already assigned to V19.

Persistent world evidence owns site revisions, observations, interpretation bridges and portable-find binding state.

Resource catalog checkpoint owns current resource identity/capability/quantity/state/location/holder/reservation projection.

Historical request, reservation and custody ledgers retain their existing authority. V2 does not infer missing handoffs, requests or provenance from current resource fields.

Minecraft/Cobblemon/Craftics remains presentation and acknowledgement downstream of these owners.

AutoPTU remains authority for structured tactical resolution and battle/session state.

## In-flight AutoPTU boundary

V2 does not solve a crash while AutoPTU owns an active tactical session.

A future recovery seam must bind battle/session identity and authoritative tactical result or resumable battle state. Until that contract exists, world recovery must not infer battle completion from NPC intent, Minecraft entity state, resource displacement or a partially observed objective.

## Regression expectations

Pass 393 regression coverage requires:

- exact three-owner round trip;
- rejection when any owner has another semantic minute;
- rejection of another valid resource generation at the same minute;
- rejection of owner or manifest corruption;
- rejection of a redigested manifest pointing to the wrong resource generation;
- explicit V2 failure when no resource checkpoint candidate is provided;
- V1 readability without inventing a resource owner;
- rejection of unsupported owner schemas.
