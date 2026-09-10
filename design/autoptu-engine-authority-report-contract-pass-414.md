# AutoPTU Engine Authority Report Contract — Pass 414

Status: DESIGN / EXECUTABLE CONTRACT — NOT CANON
Date: 2026-09-10

## Purpose

Pass 413 proves which Ouros-side AutoPTU session identity survived inside one exact V5 persistent-world generation. A restored `ENGINE_BOUND` session can still be unresolved because Ouros does not own AutoPTU tactical state.

Pass 414 adds a narrow evidence contract for a future verified AutoPTU authority adapter. It defines which external claims Ouros may accept for an already restored session identity without pretending that the adapter exists today.

`ENGINE AUTHORITY REPORT != MINECRAFT OBSERVATION`

`VALID REPORT != AUTOMATIC WORLD MUTATION`

## Report identity and provenance

An `AutoPTUEngineAuthorityReport` carries:

- Ouros `session_id`;
- exact `engine_session_ref` already bound to that session;
- `authority_ref` identifying the verified engine authority that supplied the claim;
- unique `authority_report_ref` for provenance/idempotency above this seam;
- semantic minute when the authority observation was made;
- one bounded authority state;
- result or abandonment evidence only when that state requires it.

The report may target only an unresolved `ENGINE_BOUND` session from the restored Ouros ledger. Its `engine_session_ref` must match exactly. A report cannot predate the session request or come from after the recovery cut being reconciled.

## Bounded authority states

### ACTIVE

The engine authority confirms that the referenced session remains active/recoverable under its own contract.

Ouros keeps tactical ownership unresolved. Pass 414 does not reconstruct a turn, initiative order, HP, position, status or other tactical state.

### COMPLETED

The authority reports completion and supplies an explicit `authoritative_result_ref`.

Pass 414 classifies the result reference but deliberately does not call `record_authoritative_result()` itself. A later ingress contract must validate the result payload, identity and semantics before persistent world state changes.

### UNKNOWN

The authority cannot establish the referenced engine session from the query being reconciled.

`UNKNOWN` does not mean loss, draw, forfeit, void, victory or abandonment. Ouros keeps the uncertainty visible. A later policy may quarantine the session, but this report alone cannot create a battle result.

### EXPLICITLY_ABANDONED

The authority reports that the session left active resolution through an explicitly authorized abandonment path. The report must carry an `abandonment_authorization_ref`.

This state still does not invent a winner, loser or ordinary battle result. Any world-agent release or administrative consequence belongs to a later audited transition contract.

## Fail-closed rules

Pass 414 rejects:

- a report for an unknown Ouros session;
- a report for a session that is not unresolved `ENGINE_BOUND`;
- an `engine_session_ref` mismatch;
- a report before the handoff request;
- a report newer than the recovery cut;
- more than one report for the same session in one reconciliation batch;
- duplicate `authority_report_ref` values;
- `COMPLETED` without an explicit result reference;
- `EXPLICITLY_ABANDONED` without explicit authorization provenance;
- result evidence on `ACTIVE` or `UNKNOWN`;
- abandonment evidence on any state that does not require it.

## Mutation boundary

`reconcile_engine_authority_reports()` returns classification only.

It does not:

- mutate `AutoPTUSessionLedger`;
- release `AUTOPTU_BOUND` agents;
- convert `UNKNOWN` into `QUARANTINED` automatically;
- record a result merely because a string reference exists;
- synthesize result payloads;
- infer a state from disconnects, elapsed time, entity despawn, UI frames or Minecraft/Cobblemon state;
- reconstruct tactical state.

This makes the seam useful now while keeping AutoPTU-Java and AutoPTU read-only and preserving their authority.

## Integration sequence

```text
exact V5 persistent-world generation
  -> Pass 413 selected session identity reconciliation
  -> verified AutoPTU authority adapter (future external dependency)
  -> AutoPTUEngineAuthorityReport
  -> Pass 414 identity/provenance/state validation
  -> ACTIVE: preserve unresolved tactical ownership
  -> COMPLETED: hand result ref to future authoritative result ingress
  -> UNKNOWN: preserve uncertainty / future quarantine policy
  -> EXPLICITLY_ABANDONED: require later audited abandonment transition
```

## Live evidence boundary

AutoPTU-Java currently provides no project-verified durable query API matching this contract. Pass 414 therefore defines the consumer-side evidence shape only. No adapter or engine capability is marked complete because this type exists.

The current Java work around switch post-entry dispatch strengthens a switching seam. It does not establish persistent battle-session lookup or crash recovery.

## Next seam

The next safe integration step is a verified adapter or fixture that maps real AutoPTU authority output into this report shape. Only after that evidence exists should Ouros implement state transitions for `COMPLETED`, `UNKNOWN` or `EXPLICITLY_ABANDONED`.
