# AutoPTU World-Agent Release Contract — Pass 417

Status: IMPLEMENTED / NON-CANON TECHNICAL CONTRACT

Purpose

Pass 416 records an exact admitted result on an exact durable AutoPTU session and deliberately stops at RESULT_RECORDED. Pass 417 adds the downstream ownership-release boundary without allowing retirement to race ahead of world-agent persistence.

Release proof

release_world_agent_after_recorded_result() requires all of the following:

- the durable session exists;
- the session is RESULT_RECORDED;
- its authoritative_result_ref exactly matches the supplied result_ref;
- the selected persistent NPC is a participant in that session;
- if the NPC is still AUTOPTU_BOUND, active_autoptu_binding exactly equals that session_id.

A successful first release clears the binding through the existing global NPC release primitive and returns the NPC either LOCAL_ACTIVE or OFFSCREEN_NAMED according to the caller's explicit projection choice.

The session remains RESULT_RECORDED during this phase.

Restart-safe ordering

The permitted persisted intermediate state is:

released world agent + RESULT_RECORDED session

That state can be replayed idempotently after restart. It is preferable to the inverse ordering because a RETIRED session must never remain referenced by an AUTOPTU_BOUND NPC.

retire_session_after_world_release() therefore accepts retirement only after the selected NPC carries no AutoPTU binding and is no longer AUTOPTU_BOUND. The exact session/result pair and participant relationship are checked again before retirement.

Replay of the same already-retired session is idempotent only when the same authoritative result is still present and the world agent remains released.

Explicit non-effects

This pass does not interpret a battle result payload, update world consequences from that payload, select a new NPC agenda, mutate Minecraft/Cobblemon/Craftics state, resolve UNKNOWN engine authority, treat abandonment as battle completion, or reconstruct tactical state.

The ordering chain is now:

ENGINE_AUTHORITY_REPORT -> RESULT_ADMISSION -> TRANSITION_PLAN -> EXACT_RESULT_RECORDING -> WORLD_AGENT_RELEASE -> SESSION_RETIREMENT

Each arrow remains a separate proof boundary.

Recovery implication

A crash after world-agent release but before session retirement leaves a valid recoverable pair: a released agent plus a RESULT_RECORDED session. A later recovery can retire the session after rechecking the exact participant and result reference.

A crash must never be repaired by guessing a result, clearing an unrelated binding, or retiring a session whose participant still advertises tactical ownership.
