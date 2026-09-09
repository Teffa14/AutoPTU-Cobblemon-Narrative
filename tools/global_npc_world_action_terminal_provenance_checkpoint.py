from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_action_terminal_provenance import (
    ACTION_TERMINAL_SCHEMA,
    ActionTerminalProvenanceLedger,
)
from tools.global_npc_world_action_start_provenance_checkpoint import (
    WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA,
    RestoredWorldActionStartProvenanceCheckpoint,
    build_world_action_start_provenance_checkpoint,
    restore_world_action_start_provenance_checkpoint,
)


WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V18"


@dataclass(frozen=True)
class RestoredWorldActionTerminalProvenanceCheckpoint:
    world_action_start_provenance: RestoredWorldActionStartProvenanceCheckpoint
    action_terminal_provenance: ActionTerminalProvenanceLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_action_terminal_provenance_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    delivery_replan_provenance,
    plan_selection_provenance,
    action_start_provenance,
    action_terminal_provenance: ActionTerminalProvenanceLedger,
    **v17_kwargs,
) -> dict:
    """Build one coherent checkpoint through replayable action terminal evidence.

    V18 places narrow terminal provenance under the same digest as V17. The
    currently admitted terminal is semantic travel destination arrival. Arrival
    does not imply objective success, generic action success, AutoPTU resolution
    or tactical result ingress.
    """
    action_terminal_provenance.validate_against_action_starts(
        action_start_provenance,
        semantic_minute=semantic_minute,
    )
    base = build_world_action_start_provenance_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=delivery_replan_provenance,
        plan_selection_provenance=plan_selection_provenance,
        action_start_provenance=action_start_provenance,
        **v17_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected V17 world checkpoint schema")
    payload["schema"] = WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA
    payload["action_terminal_provenance"] = action_terminal_provenance.snapshot()
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_action_terminal_provenance_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldActionTerminalProvenanceCheckpoint:
    """Restore V18, or migrate V17 and earlier with empty terminal history.

    Migration never infers a historical terminal from current location, a
    completed-looking travel state, current AutoPTU binding, tactical result,
    dialogue, inventory, mission state or any later consequence.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA:
        restored = restore_world_action_start_provenance_checkpoint(
            snapshot,
            channels=channels,
            agendas=agendas,
        )
        return RestoredWorldActionTerminalProvenanceCheckpoint(
            world_action_start_provenance=restored,
            action_terminal_provenance=ActionTerminalProvenanceLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world action-terminal provenance checkpoint digest mismatch")

    raw_action_terminal = payload.get("action_terminal_provenance")
    if not isinstance(raw_action_terminal, Mapping):
        raise ValueError("action_terminal_provenance checkpoint is required")
    if raw_action_terminal.get("schema") != ACTION_TERMINAL_SCHEMA:
        raise ValueError("V18 world checkpoint requires action-terminal provenance V1")
    action_terminal_provenance = ActionTerminalProvenanceLedger.restore(raw_action_terminal)

    v17_payload = dict(payload)
    v17_payload.pop("action_terminal_provenance", None)
    v17_payload["schema"] = WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_action_start_provenance_checkpoint(
        _redigest(v17_payload),
        channels=channels,
        agendas=agendas,
    )
    semantic_minute = int(payload["semantic_minute"])
    action_terminal_provenance.validate_against_action_starts(
        restored.action_start_provenance,
        semantic_minute=semantic_minute,
    )

    return RestoredWorldActionTerminalProvenanceCheckpoint(
        world_action_start_provenance=restored,
        action_terminal_provenance=action_terminal_provenance,
    )
