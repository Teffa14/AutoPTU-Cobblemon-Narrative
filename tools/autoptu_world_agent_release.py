from __future__ import annotations

from dataclasses import dataclass

from tools.autoptu_session_identity import AutoPTUSessionLedger, AutoPTUSessionState
from tools.global_npc_ai import AgentMode, NpcAgentState, release_autoptu


@dataclass(frozen=True)
class AutoPTUWorldAgentRelease:
    agent: NpcAgentState
    session_id: str
    result_ref: str
    changed: bool


def release_world_agent_after_recorded_result(
    *,
    ledger: AutoPTUSessionLedger,
    agent: NpcAgentState,
    session_id: str,
    result_ref: str,
    local_after_release: bool = True,
) -> AutoPTUWorldAgentRelease:
    """Release one exact world agent after one exact admitted result was recorded.

    This is phase one of completion. The session remains RESULT_RECORDED. Keeping
    retirement separate makes the safe persisted intermediate state:

        released agent + RESULT_RECORDED session

    A crash may therefore occur after agent persistence and before session
    retirement without producing a retired session still referenced by an
    AUTOPTU_BOUND agent.
    """
    clean_result_ref = str(result_ref).strip()
    if not clean_result_ref:
        raise ValueError("exact result_ref is required for world-agent release")

    session = ledger.get(session_id)
    if session.state != AutoPTUSessionState.RESULT_RECORDED:
        raise ValueError("world-agent release requires RESULT_RECORDED session")
    if session.authoritative_result_ref != clean_result_ref:
        raise ValueError("world-agent release result_ref does not match durable session result")
    if agent.agent_id not in session.participant_refs:
        raise ValueError("world agent is not a participant in the AutoPTU session")

    if agent.mode == AgentMode.AUTOPTU_BOUND:
        if agent.active_autoptu_binding != session_id:
            raise ValueError("world agent is bound to a different AutoPTU session")
        released = release_autoptu(agent, local_after_release=local_after_release)
        return AutoPTUWorldAgentRelease(
            agent=released,
            session_id=session_id,
            result_ref=clean_result_ref,
            changed=True,
        )

    if agent.active_autoptu_binding is not None:
        raise ValueError("non-AUTOPTU_BOUND world agent carries an AutoPTU binding")

    # Idempotent replay after phase-one state was already persisted.
    return AutoPTUWorldAgentRelease(
        agent=agent,
        session_id=session_id,
        result_ref=clean_result_ref,
        changed=False,
    )


def retire_session_after_world_release(
    *,
    ledger: AutoPTUSessionLedger,
    released_agent: NpcAgentState,
    session_id: str,
    result_ref: str,
):
    """Retire only after the world agent no longer carries tactical ownership."""
    clean_result_ref = str(result_ref).strip()
    if not clean_result_ref:
        raise ValueError("exact result_ref is required for session retirement")

    session = ledger.get(session_id)
    if session.state == AutoPTUSessionState.RETIRED:
        if session.authoritative_result_ref != clean_result_ref:
            raise ValueError("retired session carries a different authoritative result")
        if released_agent.active_autoptu_binding is not None or released_agent.mode == AgentMode.AUTOPTU_BOUND:
            raise ValueError("retired session cannot still be owned by AUTOPTU_BOUND world agent")
        return session

    if session.state != AutoPTUSessionState.RESULT_RECORDED:
        raise ValueError("session retirement requires RESULT_RECORDED session")
    if session.authoritative_result_ref != clean_result_ref:
        raise ValueError("session retirement result_ref does not match durable session result")
    if released_agent.agent_id not in session.participant_refs:
        raise ValueError("released world agent is not a participant in the AutoPTU session")
    if released_agent.mode == AgentMode.AUTOPTU_BOUND or released_agent.active_autoptu_binding is not None:
        raise ValueError("world agent must be released before AutoPTU session retirement")

    return ledger.retire(session_id)
