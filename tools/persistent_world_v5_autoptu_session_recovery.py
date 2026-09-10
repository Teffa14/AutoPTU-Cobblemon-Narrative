from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_ai import agent_from_dict
from tools.global_npc_autoptu_session_recovery import (
    AutoPTUSessionRecoveryValidation,
    reconcile_autoptu_session_checkpoint_with_agents,
    unresolved_engine_bound_sessions,
)
from tools.persistent_world_recovery_manifest import (
    PERSISTENT_WORLD_RECOVERY_MANIFEST_V5_SCHEMA,
    ReconciledPersistentWorldRecoveryManifest,
    reconcile_persistent_world_recovery_manifest,
)


@dataclass(frozen=True)
class PersistentWorldV5AutoPTUSessionRecovery:
    manifest: ReconciledPersistentWorldRecoveryManifest
    session_validation: AutoPTUSessionRecoveryValidation
    unresolved_engine_bound_session_ids: tuple[str, ...]


def _agents_selected_by_global_checkpoint(global_npc_checkpoint: Mapping[str, object]):
    raw_agents = global_npc_checkpoint.get("agents")
    if not isinstance(raw_agents, list):
        raise ValueError("selected global NPC checkpoint must contain an agents list")

    agents = []
    seen_ids: set[str] = set()
    for raw in raw_agents:
        if not isinstance(raw, Mapping):
            raise ValueError("selected global NPC checkpoint contains malformed agent state")
        agent = agent_from_dict(raw)
        if agent.agent_id in seen_ids:
            raise ValueError(f"selected global NPC checkpoint contains duplicate agent_id: {agent.agent_id}")
        seen_ids.add(agent.agent_id)
        agents.append(agent)
    return tuple(sorted(agents, key=lambda item: item.agent_id))


def reconcile_v5_autoptu_session_recovery_boundary(
    manifest_snapshot: Mapping[str, object],
    *,
    global_npc_checkpoint: Mapping[str, object],
    persistent_world_evidence_checkpoint: Mapping[str, object],
    world_resource_catalog_checkpoint: Mapping[str, object],
    resource_holder_transition_checkpoint: Mapping[str, object],
    holder_history_coverage_baseline_checkpoint: Mapping[str, object],
    autoptu_session_checkpoint: Mapping[str, object],
) -> PersistentWorldV5AutoPTUSessionRecovery:
    """Bind restored NPC AutoPTU references to the exact V5-selected session owner.

    The manifest boundary is validated before any session identity can influence
    restored NPC state. Agents are reconstructed from the exact global checkpoint
    whose digest the same V5 manifest selected. The AutoPTU session ledger is then
    restored from the exact session checkpoint selected by that generation.

    This proves Ouros-side identity continuity only. ENGINE_BOUND sessions without
    an authoritative result remain unresolved and are surfaced explicitly. This
    function never infers a tactical result, releases an agent, resumes a battle,
    or treats Minecraft/Cobblemon presentation as battle authority.
    """
    if manifest_snapshot.get("schema") != PERSISTENT_WORLD_RECOVERY_MANIFEST_V5_SCHEMA:
        raise ValueError("exact AutoPTU session recovery boundary requires V5 manifest")

    manifest = reconcile_persistent_world_recovery_manifest(
        manifest_snapshot,
        global_npc_checkpoint=global_npc_checkpoint,
        persistent_world_evidence_checkpoint=persistent_world_evidence_checkpoint,
        world_resource_catalog_checkpoint=world_resource_catalog_checkpoint,
        resource_holder_transition_checkpoint=resource_holder_transition_checkpoint,
        holder_history_coverage_baseline_checkpoint=holder_history_coverage_baseline_checkpoint,
        autoptu_session_checkpoint=autoptu_session_checkpoint,
    )

    agents = _agents_selected_by_global_checkpoint(global_npc_checkpoint)
    validation = reconcile_autoptu_session_checkpoint_with_agents(
        autoptu_session_checkpoint,
        recovery_semantic_minute=manifest.semantic_minute,
        agents=agents,
    )
    if validation.semantic_minute != manifest.semantic_minute:
        raise ValueError("selected AutoPTU session checkpoint does not match V5 recovery cut")

    unresolved = unresolved_engine_bound_sessions(validation)
    return PersistentWorldV5AutoPTUSessionRecovery(
        manifest=manifest,
        session_validation=validation,
        unresolved_engine_bound_session_ids=tuple(binding.session_id for binding in unresolved),
    )
