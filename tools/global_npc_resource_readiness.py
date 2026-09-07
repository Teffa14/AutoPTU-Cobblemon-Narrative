from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Iterable, Mapping

from tools.global_npc_resources import ResourceState, WorldResource


class OperationalReadinessStatus(str, Enum):
    READY_FOR_AUTHORED_USE = "READY_FOR_AUTHORED_USE"
    LIMITED = "LIMITED"
    INSPECTION_PENDING = "INSPECTION_PENDING"
    MAINTENANCE = "MAINTENANCE"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class OperationalReadinessRecord:
    record_id: str
    resource_id: str
    status: OperationalReadinessStatus
    source_record_ref: str
    effective_from_tick: int
    valid_until_tick: int | None = None


@dataclass(frozen=True)
class ReadinessProjectionResult:
    resources: tuple[WorldResource, ...]
    readiness_by_resource: Mapping[str, OperationalReadinessStatus]
    source_refs_by_resource: Mapping[str, str]
    blocked_reason_by_resource: Mapping[str, str]


def _record_applies(record: OperationalReadinessRecord, now_tick: int) -> bool:
    if now_tick < record.effective_from_tick:
        return False
    if record.valid_until_tick is not None and now_tick >= record.valid_until_tick:
        return False
    return True


def effective_readiness_record(
    resource_id: str,
    records: Iterable[OperationalReadinessRecord],
    now_tick: int,
) -> OperationalReadinessRecord | None:
    applicable = [
        record
        for record in records
        if record.resource_id == resource_id and _record_applies(record, now_tick)
    ]
    if not applicable:
        return None
    return max(applicable, key=lambda record: (record.effective_from_tick, record.record_id))


def _blocking_reason(status: OperationalReadinessStatus) -> str | None:
    return {
        OperationalReadinessStatus.LIMITED: "RESOURCE_READINESS_LIMITED",
        OperationalReadinessStatus.INSPECTION_PENDING: "RESOURCE_INSPECTION_PENDING",
        OperationalReadinessStatus.MAINTENANCE: "RESOURCE_IN_MAINTENANCE",
        OperationalReadinessStatus.OUT_OF_SERVICE: "RESOURCE_OUT_OF_SERVICE",
        OperationalReadinessStatus.UNKNOWN: "RESOURCE_READINESS_UNKNOWN",
    }.get(status)


def project_readiness_onto_resources(
    resources: Iterable[WorldResource],
    records: Iterable[OperationalReadinessRecord],
    now_tick: int,
    *,
    require_explicit_readiness: bool = False,
) -> ReadinessProjectionResult:
    """Create a planner-only resource view using owner-supplied readiness facts.

    This bridge never performs inspection, calibration, repair or verification. It
    only consumes externally authored readiness records and projects blocking
    outcomes to Pass 338's generic UNAVAILABLE state. Source records remain the
    authority and the input objects are never mutated.
    """
    if now_tick < 0:
        raise ValueError("now_tick must be non-negative")

    record_list = tuple(records)
    projected: list[WorldResource] = []
    readiness: dict[str, OperationalReadinessStatus] = {}
    source_refs: dict[str, str] = {}
    blocked_reasons: dict[str, str] = {}

    for resource in sorted(resources, key=lambda item: item.resource_id):
        record = effective_readiness_record(resource.resource_id, record_list, now_tick)
        if record is None:
            if require_explicit_readiness:
                status = OperationalReadinessStatus.UNKNOWN
                readiness[resource.resource_id] = status
                blocked_reasons[resource.resource_id] = "RESOURCE_READINESS_UNKNOWN"
                if resource.state not in {ResourceState.DEPLETED, ResourceState.RETIRED}:
                    resource = replace(resource, state=ResourceState.UNAVAILABLE)
            projected.append(resource)
            continue

        readiness[resource.resource_id] = record.status
        source_refs[resource.resource_id] = record.source_record_ref
        reason = _blocking_reason(record.status)
        if reason is not None:
            blocked_reasons[resource.resource_id] = reason
            if resource.state not in {ResourceState.DEPLETED, ResourceState.RETIRED}:
                resource = replace(resource, state=ResourceState.UNAVAILABLE)
        projected.append(resource)

    return ReadinessProjectionResult(
        resources=tuple(projected),
        readiness_by_resource=readiness,
        source_refs_by_resource=source_refs,
        blocked_reason_by_resource=blocked_reasons,
    )
