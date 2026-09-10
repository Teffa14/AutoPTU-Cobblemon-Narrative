from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

from tools.autoptu_session_identity import (
    AutoPTUSessionBinding,
    AutoPTUSessionLedger,
    AutoPTUSessionState,
    restore_autoptu_sessions,
)
from tools.global_npc_ai import AgentMode, NpcAgentState


@dataclass(frozen=True)
class AutoPTUSessionRecoveryValidation:
    semantic_minute: int
    ledger: AutoPTUSessionLedger
    active_agent_session_ids: tuple[tuple[str, str], ...]


def _validate_agent_binding(
    agent: NpcAgentState,
    ledger: AutoPTUSessionLedger,
) -> tuple[str, str] | None:
    session_ref = agent.active_autoptu_binding

    if agent.mode == AgentMode.AUTOPTU_BOUND and session_ref is None:
        raise ValueError(f"AUTOPTU_BOUND agent lacks session identity: {agent.agent_id}")
    if agent.mode != AgentMode.AUTOPTU_BOUND and session_ref is not None:
        raise ValueError(f"non-AUTOPTU_BOUND agent carries session identity: {agent.agent_id}")
    if session_ref is None:
        return None

    session = ledger.get(session_ref)
    if agent.agent_id not in session.participant_refs:
        raise ValueError(f"agent is not a participant in referenced AutoPTU session: {agent.agent_id}")
    if session.state == AutoPTUSessionState.RETIRED:
        raise ValueError(f"agent references retired AutoPTU session: {agent.agent_id}")

    return agent.agent_id, session.session_id


def reconcile_autoptu_session_checkpoint_with_agents(
    snapshot: Mapping[str, object],
    *,
    recovery_semantic_minute: int,
    agents: Iterable[NpcAgentState],
) -> AutoPTUSessionRecoveryValidation:
    """Restore the Ouros-side session owner and validate persistent NPC references.

    This function proves identity continuity only. An ENGINE_BOUND session without an
    authoritative result remains unresolved. It never releases an agent, declares a
    winner, invents a draw, or derives tactical state from Minecraft presentation.
    """
    ledger = restore_autoptu_sessions(
        snapshot,
        recovery_semantic_minute=recovery_semantic_minute,
    )

    bindings: list[tuple[str, str]] = []
    seen_agents: set[str] = set()
    for agent in sorted(agents, key=lambda item: item.agent_id):
        if agent.agent_id in seen_agents:
            raise ValueError(f"duplicate persistent NPC agent_id during AutoPTU recovery: {agent.agent_id}")
        seen_agents.add(agent.agent_id)
        validated = _validate_agent_binding(agent, ledger)
        if validated is not None:
            bindings.append(validated)

    semantic_minute = int(snapshot["semantic_minute"])
    return AutoPTUSessionRecoveryValidation(
        semantic_minute=semantic_minute,
        ledger=ledger,
        active_agent_session_ids=tuple(bindings),
    )


def unresolved_engine_bound_sessions(
    validation: AutoPTUSessionRecoveryValidation,
) -> tuple[AutoPTUSessionBinding, ...]:
    """Return sessions that still need authoritative engine reconciliation."""
    return tuple(
        binding
        for binding in validation.ledger.bindings()
        if binding.state == AutoPTUSessionState.ENGINE_BOUND
        and binding.authoritative_result_ref is None
    )
