from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
    record_holder_transition,
)


RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA = "OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1"


@dataclass(frozen=True)
class RestoredResourceHolderTransitions:
    semantic_minute: int
    ledger: ResourceHolderTransitionLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _digest(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _serialize_transition(transition: ResourceHolderTransition) -> dict[str, object]:
    return {
        "transition_id": transition.transition_id,
        "resource_id": transition.resource_id,
        "kind": transition.kind.value,
        "from_actor_id": transition.from_actor_id,
        "to_actor_id": transition.to_actor_id,
        "at_tick": transition.at_tick,
        "location_ref": transition.location_ref,
        "source_ref": transition.source_ref,
    }


def _canonical_transitions(
    ledger: ResourceHolderTransitionLedger,
) -> tuple[ResourceHolderTransition, ...]:
    ordered = tuple(
        sorted(
            ledger.transitions,
            key=lambda item: (item.resource_id, item.at_tick, item.transition_id),
        )
    )
    rebuilt = ResourceHolderTransitionLedger()
    for transition in ordered:
        rebuilt = record_holder_transition(rebuilt, transition)
    return ordered


def snapshot_resource_holder_transitions(
    ledger: ResourceHolderTransitionLedger,
    *,
    semantic_minute: int,
) -> dict:
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int) or semantic_minute < 0:
        raise ValueError("semantic_minute must be a non-negative integer")

    ordered = _canonical_transitions(ledger)
    if any(transition.at_tick > semantic_minute for transition in ordered):
        raise ValueError("holder transition cannot be later than checkpoint semantic_minute")
    payload = {
        "schema": RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA,
        "semantic_minute": semantic_minute,
        "transitions": [_serialize_transition(item) for item in ordered],
    }
    return payload | {"sha256": _digest(payload)}


def _required_string(record: Mapping[str, object], field: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"holder transition {field} is required")
    return value


def _optional_string(record: Mapping[str, object], field: str) -> str | None:
    value = record.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"holder transition {field} must be a non-empty string when present")
    return value


def _deserialize_transition(raw: object) -> ResourceHolderTransition:
    if not isinstance(raw, Mapping):
        raise ValueError("holder transition record must be an object")

    raw_kind = raw.get("kind")
    if not isinstance(raw_kind, str):
        raise ValueError("holder transition kind is required")
    try:
        kind = HolderTransitionKind(raw_kind)
    except ValueError as exc:
        raise ValueError("unknown holder transition kind") from exc

    at_tick = raw.get("at_tick")
    if isinstance(at_tick, bool) or not isinstance(at_tick, int) or at_tick < 0:
        raise ValueError("holder transition at_tick must be a non-negative integer")

    return ResourceHolderTransition(
        transition_id=_required_string(raw, "transition_id"),
        resource_id=_required_string(raw, "resource_id"),
        kind=kind,
        from_actor_id=_optional_string(raw, "from_actor_id"),
        to_actor_id=_optional_string(raw, "to_actor_id"),
        at_tick=at_tick,
        location_ref=_optional_string(raw, "location_ref"),
        source_ref=_optional_string(raw, "source_ref"),
    )


def restore_resource_holder_transitions(
    snapshot: Mapping[str, object],
    *,
    recovery_semantic_minute: int | None = None,
) -> RestoredResourceHolderTransitions:
    if snapshot.get("schema") != RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA:
        raise ValueError("unsupported resource holder transition checkpoint schema")

    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest:
        raise ValueError("resource holder transition checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != supplied_digest:
        raise ValueError("resource holder transition checkpoint digest mismatch")

    semantic_minute = payload.get("semantic_minute")
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int) or semantic_minute < 0:
        raise ValueError("resource holder transition semantic_minute must be a non-negative integer")
    if recovery_semantic_minute is not None:
        if (
            isinstance(recovery_semantic_minute, bool)
            or not isinstance(recovery_semantic_minute, int)
            or recovery_semantic_minute < 0
        ):
            raise ValueError("recovery_semantic_minute must be a non-negative integer")
        if semantic_minute > recovery_semantic_minute:
            raise ValueError("resource holder transition checkpoint is from the future")

    raw_transitions = payload.get("transitions")
    if not isinstance(raw_transitions, list):
        raise ValueError("resource holder transition checkpoint transitions must be a list")

    transitions = tuple(_deserialize_transition(raw) for raw in raw_transitions)
    if any(transition.at_tick > semantic_minute for transition in transitions):
        raise ValueError("holder transition cannot be later than checkpoint semantic_minute")
    ledger = ResourceHolderTransitionLedger()
    for transition in transitions:
        ledger = record_holder_transition(ledger, transition)

    canonical = _canonical_transitions(ledger)
    if transitions != canonical:
        raise ValueError("holder transition records must use canonical resource/time/id order")

    return RestoredResourceHolderTransitions(semantic_minute, ledger)
