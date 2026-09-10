from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Iterable, Mapping

from tools.global_npc_resources import ResourceState, WorldResource


WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA = "OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1"


@dataclass(frozen=True)
class RestoredWorldResourceCatalog:
    semantic_minute: int
    resources: tuple[WorldResource, ...]

    def by_id(self) -> dict[str, WorldResource]:
        return {resource.resource_id: resource for resource in self.resources}


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _digest(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _validate_resource_identity(resource: WorldResource) -> None:
    if not isinstance(resource.resource_id, str) or not resource.resource_id.strip():
        raise ValueError("world resource id is required")
    if isinstance(resource.quantity, bool) or not isinstance(resource.quantity, int):
        raise ValueError("world resource quantity must be an integer")
    if any(not isinstance(ref, str) or not ref.strip() for ref in resource.capability_refs):
        raise ValueError("world resource capability refs must be non-empty strings")
    for label, value in (
        ("location_ref", resource.location_ref),
        ("holder_actor_id", resource.holder_actor_id),
        ("reserved_for_actor_id", resource.reserved_for_actor_id),
    ):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f"world resource {label} must be a non-empty string when present")


def _canonical_resources(resources: Iterable[WorldResource]) -> tuple[WorldResource, ...]:
    ordered = tuple(sorted(resources, key=lambda resource: resource.resource_id))
    seen: set[str] = set()
    for resource in ordered:
        _validate_resource_identity(resource)
        if resource.resource_id in seen:
            raise ValueError("duplicate world resource id")
        seen.add(resource.resource_id)
    return ordered


def _serialize_resource(resource: WorldResource) -> dict[str, object]:
    return {
        "resource_id": resource.resource_id,
        "capability_refs": sorted(resource.capability_refs),
        "quantity": resource.quantity,
        "state": resource.state.value,
        "location_ref": resource.location_ref,
        "holder_actor_id": resource.holder_actor_id,
        "reserved_for_actor_id": resource.reserved_for_actor_id,
    }


def snapshot_world_resource_catalog(
    resources: Iterable[WorldResource],
    *,
    semantic_minute: int,
) -> dict:
    """Snapshot the complete current mutable WorldResource catalog.

    This owner records current operational resource state only. It does not own request,
    reservation, handoff, custody, consumption or provenance history.
    """
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int) or semantic_minute < 0:
        raise ValueError("semantic_minute must be a non-negative integer")

    ordered = _canonical_resources(resources)
    payload = {
        "schema": WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
        "semantic_minute": semantic_minute,
        "resources": [_serialize_resource(resource) for resource in ordered],
    }
    return payload | {"sha256": _digest(payload)}


def _required_string(record: Mapping[str, object], field: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"world resource {field} is required")
    return value


def _optional_string(record: Mapping[str, object], field: str) -> str | None:
    value = record.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"world resource {field} must be a non-empty string when present")
    return value


def _deserialize_resource(raw: object) -> WorldResource:
    if not isinstance(raw, Mapping):
        raise ValueError("world resource record must be an object")

    resource_id = _required_string(raw, "resource_id")

    capability_refs = raw.get("capability_refs")
    if not isinstance(capability_refs, list):
        raise ValueError("world resource capability_refs must be a list")
    if any(not isinstance(ref, str) or not ref.strip() for ref in capability_refs):
        raise ValueError("world resource capability refs must be non-empty strings")
    if len(set(capability_refs)) != len(capability_refs):
        raise ValueError("world resource capability refs must be unique")

    quantity = raw.get("quantity")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise ValueError("world resource quantity must be an integer")

    raw_state = raw.get("state")
    if not isinstance(raw_state, str):
        raise ValueError("world resource state is required")
    try:
        state = ResourceState(raw_state)
    except ValueError as exc:
        raise ValueError("unknown world resource state") from exc

    return WorldResource(
        resource_id=resource_id,
        capability_refs=frozenset(capability_refs),
        quantity=quantity,
        state=state,
        location_ref=_optional_string(raw, "location_ref"),
        holder_actor_id=_optional_string(raw, "holder_actor_id"),
        reserved_for_actor_id=_optional_string(raw, "reserved_for_actor_id"),
    )


def restore_world_resource_catalog(
    snapshot: Mapping[str, object],
    *,
    recovery_semantic_minute: int | None = None,
) -> RestoredWorldResourceCatalog:
    """Restore one exact catalog generation after digest and schema validation."""
    if snapshot.get("schema") != WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA:
        raise ValueError("unsupported world resource catalog checkpoint schema")

    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest:
        raise ValueError("world resource catalog checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != supplied_digest:
        raise ValueError("world resource catalog checkpoint digest mismatch")

    semantic_minute = payload.get("semantic_minute")
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int) or semantic_minute < 0:
        raise ValueError("world resource catalog semantic_minute must be a non-negative integer")
    if recovery_semantic_minute is not None:
        if (
            isinstance(recovery_semantic_minute, bool)
            or not isinstance(recovery_semantic_minute, int)
            or recovery_semantic_minute < 0
        ):
            raise ValueError("recovery_semantic_minute must be a non-negative integer")
        if semantic_minute > recovery_semantic_minute:
            raise ValueError("world resource catalog checkpoint is from the future")

    raw_resources = payload.get("resources")
    if not isinstance(raw_resources, list):
        raise ValueError("world resource catalog resources must be a list")

    resources = tuple(_deserialize_resource(raw) for raw in raw_resources)
    canonical = _canonical_resources(resources)
    if resources != canonical:
        raise ValueError("world resource catalog records must use canonical resource-id order")

    return RestoredWorldResourceCatalog(semantic_minute, resources)
