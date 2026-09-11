# AutoPTU Admitted Result Executor Contract — Pass 416

Status: IMPLEMENTED / NON-CANON TECHNICAL CONTRACT

## Purpose

Pass 415 converts a validated engine-authority reconciliation into conservative transition intents. This pass implements only the narrow mutation that is already justified when an intent is `RECORD_ADMITTED_RESULT`.

The executor records the exact admitted result reference on the exact durable AutoPTU session identity. It does not interpret battle payloads, infer outcomes, retire sessions, release world agents or change Minecraft/Cobblemon state.

## Preconditions

`execute_admitted_result_recording()` accepts one `AutoPTUAuthorityTransitionIntent` and one `AutoPTUSessionLedger`.

The intent must:
- use `RECORD_ADMITTED_RESULT`;
- identify an existing durable session;
- carry a non-blank exact result reference;
- target an `ENGINE_BOUND` session, or an already `RESULT_RECORDED` session carrying the same result reference for idempotent replay.

Any other transition kind fails closed. `ACTIVE`, `UNKNOWN` and `EXPLICITLY_ABANDONED` therefore cannot reach this mutation by substituting their evidence into the normal completion path.

## Mutation boundary

Successful first execution changes only the selected session from `ENGINE_BOUND` to `RESULT_RECORDED` and preserves its existing `engine_session_ref`.

Replaying the same exact intent is idempotent. Replaying a different result reference against the same resolved session fails closed.

`REQUESTED`, `RETIRED` and `QUARANTINED` sessions cannot use this executor to bypass their own state transitions.

## Explicit non-effects

This pass does not:
- validate the semantic contents of a result payload;
- create an admission decision;
- retire a session;
- clear an NPC `active_autoptu_binding`;
- move an NPC out of `AUTOPTU_BOUND`;
- synthesize winner, draw, forfeit, void or abandonment semantics;
- reconstruct turn, HP, position, initiative, status, weather, terrain or any other tactical state;
- make Minecraft/Cobblemon/Craftics authoritative for battle outcome.

Result admission remains upstream. World-agent release remains downstream and requires its own exact binding/result contract.

## Recovery invariant

Restart may replay the same admitted-result operation. The result reference already stored on the durable session must match exactly. A conflicting result cannot overwrite the earlier authoritative reference.

`ENGINE_AUTHORITY_REPORT -> RESULT_ADMISSION -> TRANSITION_PLAN -> EXACT_RESULT_RECORDING -> FUTURE_WORLD_RELEASE`

Each arrow is a separate proof boundary.
