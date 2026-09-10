# AutoPTU Session Identity Checkpoint Contract — Pass 411

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-10

## Purpose

Ouros already stores `active_autoptu_binding` on persistent NPC state and already defines opaque battle-session references in the battle-subject binding contract. That reference still needs one durable owner that survives restart without guessing whether a tactical resolution completed.

Pass 411 adds `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1` as the first explicit Ouros-side owner for stable AutoPTU session identity.

This owner does not serialize AutoPTU tactical state and does not determine battle outcome. It only preserves the identity and lifecycle facts Ouros is allowed to know.

## Immutable identity inputs

A session identity derives from:

- `handoff_request_id`;
- `world_action_ref`;
- canonical participant references;
- `rules_profile_id`;
- `requested_at_minute`.

The resulting `session_id` is deterministic. Replaying the same handoff event produces the same identity. Reusing the same handoff request with changed immutable inputs fails closed.

`session_id` is an Ouros correlation identity. It is not a substitute for an AutoPTU engine-owned battle/session identifier.

## Lifecycle

`REQUESTED`

Ouros selected structured mechanics and created a stable session identity. No engine session is claimed yet.

`ENGINE_BOUND`

An explicit authoritative engine-session reference was supplied. The existence of this state does not imply completion or any battle result.

`RESULT_RECORDED`

An authoritative result reference has been explicitly received and attached to the engine-bound session. Conflicting result references fail closed.

`RETIRED`

The session can retire only after an authoritative result exists. Restart cannot turn an unresolved battle into a retired battle.

`QUARANTINED`

Identity or reconciliation uncertainty may be preserved without inventing a result.

## Restart invariant

A checkpoint containing an `ENGINE_BOUND` session with no result must restore as the same unresolved `ENGINE_BOUND` session.

The persistent world must continue to hold affected agents at the AutoPTU boundary until a later authoritative reconciliation decides whether the engine session remains active, completed with a result, or requires quarantine/abandonment under a future explicit recovery contract.

Minecraft, Cobblemon and Craftics cannot infer completion from entity disappearance, animation end, disconnect, chunk unload, UI state or server restart.

## Checkpoint integrity

`OUROS_AUTOPTU_SESSION_CHECKPOINT_V1` contains semantic time, canonically ordered session records and SHA-256 over the complete payload.

Restore rejects:

- digest mismatch;
- future checkpoint relative to the recovery cut;
- future session request relative to the checkpoint;
- duplicate session IDs;
- duplicate handoff request IDs;
- session IDs that do not match immutable handoff inputs;
- resolved/retired states without an engine-session reference;
- resolved/retired states without an authoritative result reference;
- non-canonical session ordering.

## Relation to existing contracts

`design/battle-subject-binding-contract.md` remains responsible for binding persistent ecological subjects to opaque per-session battle references.

`design/autoptu-semantic-result-ingress-contract.md` remains responsible for validating semantic results and producer authority.

The global NPC checkpoint may continue to store `active_autoptu_binding`. Pass 411 supplies the missing durable identity owner that can later be selected by a coherent outer recovery generation.

No current persistent-world recovery manifest selects this new owner yet. Adding it requires a new manifest generation or another explicit coherent recovery owner boundary. Legacy recovery manifests must not silently assume the checkpoint exists.

## Capability effect

No PTU capability family becomes complete because of Pass 411.

This pass only improves cross-system identity/recovery infrastructure. Tactical legality, movement, damage, statuses, terrain, Moves, Abilities, Items, Trainer Features, AI policy and adapter playback retain their existing evidence classifications.
