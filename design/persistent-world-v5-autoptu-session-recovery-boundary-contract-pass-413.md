# Persistent World V5 AutoPTU Session Recovery Boundary — Pass 413

Status: DESIGN / EXECUTABLE CONTRACT — NOT CANON
Date: 2026-09-10

## Purpose

Pass 412 made `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1` an explicit owner inside `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V5`. Pass 413 closes the next recovery seam: persistent NPC `active_autoptu_binding` references may be reconciled against a session ledger only after both the global NPC checkpoint and the AutoPTU session checkpoint are proven to be the exact owners selected by the same V5 generation.

The boundary proves Ouros-side identity continuity. It does not restore AutoPTU tactical state and does not decide a battle result.

## Exact-generation rule

`reconcile_v5_autoptu_session_recovery_boundary()` accepts:

- one V5 manifest;
- the six candidate owner checkpoints selected by that manifest;
- no independently supplied agent list.

The function first calls the existing persistent-world manifest reconciliation. Only after schema, digest and same-minute validation succeeds does it read agent rows from the selected global NPC checkpoint. The session ledger is restored from the selected AutoPTU session checkpoint.

This order is deliberate.

A valid same-minute session checkpoint from another generation cannot affect agent recovery. A valid same-minute global NPC checkpoint from another generation cannot provide replacement agent bindings. Both fail at the manifest boundary before their mutable contents are interpreted.

## Agent/session invariants

After the V5 boundary succeeds, existing Pass 411 session recovery rules still apply:

- `AUTOPTU_BOUND` requires `active_autoptu_binding`;
- an agent outside `AUTOPTU_BOUND` may not retain an active binding;
- the referenced session must exist in the selected session ledger;
- the agent must be an explicit participant in that session;
- a persistent agent may not reference a retired session;
- duplicate persistent agent IDs fail closed.

An `ENGINE_BOUND` session without an authoritative result remains unresolved and is surfaced explicitly as reconciliation work.

`SELECTED_SESSION_IDENTITY != RESOLVED_TACTICAL_STATE`

## Historical compatibility

The exact session-recovery boundary requires V5.

V4 and earlier recovery generations did not select the AutoPTU session owner. They cannot be reinterpreted retroactively to do so. A caller attempting to enter this boundary with V4 fails before session reconciliation.

## Authority boundary

Ouros owns persistent world state, handoff provenance and the durable identity/reference record needed to find an AutoPTU session again.

AutoPTU owns tactical state and authoritative result generation.

Minecraft/Cobblemon/Craftics may project actors, animation and interaction. Presentation cannot prove whether an `ENGINE_BOUND` battle is still active, completed, abandoned or lost.

This pass therefore does not:

- declare a winner, loser, draw, forfeit or void;
- release an `AUTOPTU_BOUND` agent;
- synthesize an `authoritative_result_ref`;
- resume a battle from a Minecraft frame;
- infer completion from despawn, disconnect, UI state or elapsed world time;
- create an engine-session query API.

## Recovery sequence

```text
candidate V5 manifest + six candidate owner checkpoints
  -> verify manifest integrity
  -> verify exact selected digest for every owner
  -> verify coherent semantic minute
  -> parse agents from selected global NPC checkpoint
  -> restore selected AutoPTU session ledger
  -> validate each persistent agent/session reference
  -> enumerate unresolved ENGINE_BOUND sessions
  -> wait for a separate authoritative engine reconciliation contract
```

## Fail-closed cases covered

Pass 413 regression coverage demonstrates:

- one exact V5 generation restores one active persistent NPC/session identity;
- an alternate valid same-minute session generation is rejected by digest before binding;
- an alternate valid same-minute global checkpoint is rejected before agent parsing;
- an exact selected generation with an unknown session reference is rejected;
- V4 cannot enter the V5 session-recovery boundary.

## Next seam

The remaining tactical crash-recovery problem is external to this identity boundary. Ouros needs an authoritative AutoPTU-side lookup/reconciliation contract for the durable engine-session reference.

A future contract may distinguish outcomes such as still active, completed with a verifiable result, unknown/unrecoverable, or explicitly abandoned. Those states must be defined against live engine evidence before Ouros can change persistent world-agent ownership.
