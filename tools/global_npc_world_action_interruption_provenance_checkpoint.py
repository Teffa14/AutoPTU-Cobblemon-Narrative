from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_action_interruption_provenance import (
    ACTION_INTERRUPTION_SCHEMA,
    ActionInterruptionProvenanceLedger,
)
from tools.global_npc_action_terminal_provenance import ActionTerminalProvenanceLedger
from tools.global_npc_world_action_terminal_provenance_checkpoint import (
    WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA,
    RestoredWorldActionTerminalProvenanceCheckpoint,
    build_world_action_terminal_provenance_checkpoint,
    restore_world_action_terminal_provenance_checkpoint,
)


WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V19"


@dataclass(frozen=True)
class RestoredWorldActionInterruptionProvenanceCheckpoint:
    world_action_terminal_provenance: RestoredWorldActionTerminalProvenanceCheckpoint
    action_interruption_provenance: ActionInterruptionProvenanceLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def _validate_outcome_exclusivity(
    terminals: ActionTerminalProvenanceLedger,
    interruptions: ActionInterruptionProvenanceLedger,
) -> None:
    terminal_start_ids = {record.action_start_id for record in terminals.terminals.values()}
    interruption_start_ids = {record.action_start_id for record in interruptions.interruptions.values()}
    overlap = sorted(terminal_start_ids & interruption_start_ids)
    if overlap:
        raise ValueError(f"action start has conflicting terminal and interruption outcomes: {overlap[0]}")


def build_world_action_interruption_provenance_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    delivery_replan_provenance,
    plan_selection_provenance,
    action_start_provenance,
    action_terminal_provenance: ActionTerminalProvenanceLedger,
    action_interruption_provenance: ActionInterruptionProvenanceLedger,
    **v18_kwargs,
) -> dict:
    """Build one coherent checkpoint through replayable action interruptions.

    V19 places deterministic travel REPLAN_REQUIRED provenance under the same
    digest as V18 while keeping interruption distinct from arrival, failure,
    cancellation and objective outcome.
    """
    action_interruption_provenance.validate_against_action_starts(
        action_start_provenance,
        semantic_minute=semantic_minute,
    )
    _validate_outcome_exclusivity(action_terminal_provenance, action_interruption_provenance)
    base = build_world_action_terminal_provenance_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=delivery_replan_provenance,
        plan_selection_provenance=plan_selection_provenance,
        action_start_provenance=action_start_provenance,
        action_terminal_provenance=action_terminal_provenance,
        **v18_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected V18 world checkpoint schema")
    payload["schema"] = WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA
    payload["action_interruption_provenance"] = action_interruption_provenance.snapshot()
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_action_interruption_provenance_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldActionInterruptionProvenanceCheckpoint:
    """Restore V19, or migrate V18 and earlier with empty interruption history.

    Migration never infers a historical interruption from a currently blocked
    route, a later replan, current location, dialogue, mission state or another
    downstream consequence.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA:
        restored = restore_world_action_terminal_provenance_checkpoint(
            snapshot,
            channels=channels,
            agendas=agendas,
        )
        return RestoredWorldActionInterruptionProvenanceCheckpoint(
            world_action_terminal_provenance=restored,
            action_interruption_provenance=ActionInterruptionProvenanceLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world action-interruption provenance checkpoint digest mismatch")

    raw_action_interruption = payload.get("action_interruption_provenance")
    if not isinstance(raw_action_interruption, Mapping):
        raise ValueError("action_interruption_provenance checkpoint is required")
    if raw_action_interruption.get("schema") != ACTION_INTERRUPTION_SCHEMA:
        raise ValueError("V19 world checkpoint requires action-interruption provenance V1")
    action_interruption_provenance = ActionInterruptionProvenanceLedger.restore(raw_action_interruption)

    v18_payload = dict(payload)
    v18_payload.pop("action_interruption_provenance", None)
    v18_payload["schema"] = WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_action_terminal_provenance_checkpoint(
        _redigest(v18_payload),
        channels=channels,
        agendas=agendas,
    )
    semantic_minute = int(payload["semantic_minute"])
    action_interruption_provenance.validate_against_action_starts(
        restored.world_action_start_provenance.action_start_provenance,
        semantic_minute=semantic_minute,
    )
    _validate_outcome_exclusivity(
        restored.action_terminal_provenance,
        action_interruption_provenance,
    )

    return RestoredWorldActionInterruptionProvenanceCheckpoint(
        world_action_terminal_provenance=restored,
        action_interruption_provenance=action_interruption_provenance,
    )
