# Persistent World Recovery Manifest V5 — AutoPTU Session Owner — Pass 412

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-10

## Purpose

Pass 412 adds `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V5` as an explicit six-owner generation boundary. V5 selects the same five owners as historical V4 plus `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1`.

V4 remains a five-owner schema. It is not reinterpreted to include tactical-session identity.

## Six selected owners

A V5 generation binds one semantic minute across:

- global NPC/world-action interruption provenance checkpoint;
- persistent-world evidence checkpoint;
- WorldResource catalog checkpoint;
- resource-holder transition checkpoint;
- holder-history coverage baseline checkpoint;
- AutoPTU session identity checkpoint.

Each owner keeps its own restore semantics. The manifest owns exact generation selection only.

## Fail-closed rules

`build_persistent_world_recovery_manifest_v5()` requires the current schema and valid SHA-256 for all six owner checkpoints. Every owner must use the same semantic minute.

`reconcile_persistent_world_recovery_manifest()` accepts V5 only when the supplied AutoPTU session checkpoint matches the digest selected by the manifest. A valid same-minute session checkpoint from another generation is rejected.

V1 through V4 remain readable under their historical owner sets. Supplying an AutoPTU session checkpoint to V4 is rejected because V4 never selected that owner.

## Authority boundary

Selection of `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1` does not serialize AutoPTU combat state and does not make Ouros the tactical authority. An `ENGINE_BOUND` record without an authoritative result remains unresolved after recovery.

Minecraft/Cobblemon/Craftics presentation cannot promote an unresolved session to completed. A later integration must reconcile the selected session identity against an authoritative AutoPTU-side session store or explicit result contract.

## Compatibility

`PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA` remains the historical V4 alias so existing V4 builders and fixtures keep their previous meaning. New code that needs the sixth owner must call the explicit V5 builder and V5 schema.
