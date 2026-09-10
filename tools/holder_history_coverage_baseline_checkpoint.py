from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Iterable, Mapping

from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline


HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA = (
    "OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1"
)


@dataclass(frozen=True)
class RestoredHolderHistoryCoverageBaselines:
    semantic_minute: int
    baselines: tuple[HolderHistoryCoverageBaseline, ...]


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _digest(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _serialize_baseline(baseline: HolderHistoryCoverageBaseline) -> dict[str, object]:
    return {
        "baseline_id": baseline.baseline_id,
        "resource_id": baseline.resource_id,
        "at_tick": baseline.at_tick,
        "holder_actor_id": baseline.holder_actor_id,
        "source_ref": baseline.source_ref,
    }


def _canonical_baselines(
    baselines: Iterable[HolderHistoryCoverageBaseline],
) -> tuple[HolderHistoryCoverageBaseline, ...]:
    ordered = tuple(sorted(baselines, key=lambda item: (item.resource_id, item.baseline_id)))
    seen_ids: set[str] = set()
    seen_resources: set[str] = set()
    for baseline in ordered:
        if baseline.baseline_id in seen_ids:
            raise ValueError("duplicate holder history coverage baseline id")
        if baseline.resource_id in seen_resources:
            raise ValueError("multiple holder history coverage baselines for resource")
        seen_ids.add(baseline.baseline_id)
        seen_resources.add(baseline.resource_id)
    return ordered


def snapshot_holder_history_coverage_baselines(
    baselines: Iterable[HolderHistoryCoverageBaseline],
    *,
    semantic_minute: int,
) -> dict:
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int) or semantic_minute < 0:
        raise ValueError("semantic_minute must be a non-negative integer")

    ordered = _canonical_baselines(baselines)
    if any(baseline.at_tick > semantic_minute for baseline in ordered):
        raise ValueError("holder history coverage baseline cannot be later than checkpoint semantic_minute")

    payload = {
        "schema": HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA,
        "semantic_minute": semantic_minute,
        "baselines": [_serialize_baseline(item) for item in ordered],
    }
    return payload | {"sha256": _digest(payload)}


def _required_string(record: Mapping[str, object], field: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"holder history coverage baseline {field} is required")
    return value


def _optional_string(record: Mapping[str, object], field: str) -> str | None:
    value = record.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"holder history coverage baseline {field} must be a non-empty string when present"
        )
    return value


def _deserialize_baseline(raw: object) -> HolderHistoryCoverageBaseline:
    if not isinstance(raw, Mapping):
        raise ValueError("holder history coverage baseline record must be an object")

    at_tick = raw.get("at_tick")
    if isinstance(at_tick, bool) or not isinstance(at_tick, int) or at_tick < 0:
        raise ValueError("holder history coverage baseline at_tick must be a non-negative integer")

    return HolderHistoryCoverageBaseline(
        baseline_id=_required_string(raw, "baseline_id"),
        resource_id=_required_string(raw, "resource_id"),
        at_tick=at_tick,
        holder_actor_id=_optional_string(raw, "holder_actor_id"),
        source_ref=_required_string(raw, "source_ref"),
    )


def restore_holder_history_coverage_baselines(
    snapshot: Mapping[str, object],
    *,
    recovery_semantic_minute: int | None = None,
) -> RestoredHolderHistoryCoverageBaselines:
    if snapshot.get("schema") != HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA:
        raise ValueError("unsupported holder history coverage baseline checkpoint schema")

    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest:
        raise ValueError("holder history coverage baseline checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != supplied_digest:
        raise ValueError("holder history coverage baseline checkpoint digest mismatch")

    semantic_minute = payload.get("semantic_minute")
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int) or semantic_minute < 0:
        raise ValueError("holder history coverage baseline semantic_minute must be a non-negative integer")
    if recovery_semantic_minute is not None:
        if (
            isinstance(recovery_semantic_minute, bool)
            or not isinstance(recovery_semantic_minute, int)
            or recovery_semantic_minute < 0
        ):
            raise ValueError("recovery_semantic_minute must be a non-negative integer")
        if semantic_minute > recovery_semantic_minute:
            raise ValueError("holder history coverage baseline checkpoint is from the future")

    raw_baselines = payload.get("baselines")
    if not isinstance(raw_baselines, list):
        raise ValueError("holder history coverage baseline checkpoint baselines must be a list")

    baselines = tuple(_deserialize_baseline(raw) for raw in raw_baselines)
    if any(baseline.at_tick > semantic_minute for baseline in baselines):
        raise ValueError("holder history coverage baseline cannot be later than checkpoint semantic_minute")

    canonical = _canonical_baselines(baselines)
    if baselines != canonical:
        raise ValueError("holder history coverage baselines must use canonical resource/id order")

    return RestoredHolderHistoryCoverageBaselines(
        semantic_minute=semantic_minute,
        baselines=baselines,
    )
