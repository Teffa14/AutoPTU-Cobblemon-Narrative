from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Mapping

from tools.global_npc_resources import WorldResource
from tools.global_npc_site_evidence import ObservationKind, SiteEvidenceLedger, SiteObservationRecord


PORTABLE_FIND_RESOURCE_BINDING_SCHEMA = "OUROS_PORTABLE_FIND_RESOURCE_BINDING_V1"


def _canonical_observation_payload(observation: SiteObservationRecord) -> dict[str, object]:
    return {
        "observation_id": observation.observation_id,
        "site_id": observation.site_id,
        "revision_id": observation.revision_id,
        "observer_id": observation.observer_id,
        "semantic_minute": observation.semantic_minute,
        "evidence_ref": observation.evidence_ref,
        "kind": observation.kind.value,
        "content": observation.content,
        "provenance_root": observation.provenance_root,
    }


def _observation_digest(observation: SiteObservationRecord) -> str:
    payload = json.dumps(
        _canonical_observation_payload(observation),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _declared_resource(
    declared_resources: Mapping[str, WorldResource],
    resource_id: str,
) -> WorldResource:
    resource = declared_resources.get(resource_id)
    if resource is None:
        raise ValueError("portable-find binding references missing world resource")
    if resource.resource_id != resource_id:
        raise ValueError("world resource declaration key does not match resource identity")
    return resource


@dataclass(frozen=True)
class PortableFindResourceBinding:
    binding_id: str
    observation_id: str
    resource_id: str
    bound_at_semantic_minute: int
    bound_by_actor_id: str
    authority_ref: str
    observation_sha256: str


@dataclass
class PortableFindResourceBindingLedger:
    bindings: dict[str, PortableFindResourceBinding] = field(default_factory=dict)

    def bind(
        self,
        *,
        binding_id: str,
        observation_id: str,
        resource_id: str,
        bound_at_semantic_minute: int,
        bound_by_actor_id: str,
        authority_ref: str,
        site_evidence: SiteEvidenceLedger,
        declared_resources: Mapping[str, WorldResource],
    ) -> PortableFindResourceBinding:
        if binding_id in self.bindings:
            raise ValueError(f"portable-find binding already recorded: {binding_id}")
        if not binding_id or not bound_by_actor_id or not authority_ref:
            raise ValueError("portable-find binding requires identity, actor and authority")
        if bound_at_semantic_minute < 0:
            raise ValueError("portable-find binding minute must be non-negative")

        observation = site_evidence.observations.get(observation_id)
        if observation is None:
            raise ValueError("portable-find binding references missing site observation")
        if observation.kind is not ObservationKind.PORTABLE_FIND:
            raise ValueError("portable-find binding requires a PORTABLE_FIND observation")
        if bound_at_semantic_minute < observation.semantic_minute:
            raise ValueError("portable-find binding cannot predate its observation")

        _declared_resource(declared_resources, resource_id)

        if any(row.observation_id == observation_id for row in self.bindings.values()):
            raise ValueError("portable-find observation is already bound")
        if any(row.resource_id == resource_id for row in self.bindings.values()):
            raise ValueError("world resource is already bound to another portable find")

        record = PortableFindResourceBinding(
            binding_id=binding_id,
            observation_id=observation_id,
            resource_id=resource_id,
            bound_at_semantic_minute=bound_at_semantic_minute,
            bound_by_actor_id=bound_by_actor_id,
            authority_ref=authority_ref,
            observation_sha256=_observation_digest(observation),
        )
        self.bindings[binding_id] = record
        return record

    def validate(
        self,
        *,
        site_evidence: SiteEvidenceLedger,
        declared_resources: Mapping[str, WorldResource],
        semantic_minute: int | None = None,
    ) -> None:
        if semantic_minute is not None and semantic_minute < 0:
            raise ValueError("semantic_minute must be non-negative")

        seen_observations: set[str] = set()
        seen_resources: set[str] = set()
        for row in self.bindings.values():
            if not row.binding_id or not row.bound_by_actor_id or not row.authority_ref:
                raise ValueError("invalid portable-find binding")
            if row.bound_at_semantic_minute < 0:
                raise ValueError("invalid portable-find binding minute")
            if semantic_minute is not None and row.bound_at_semantic_minute > semantic_minute:
                raise ValueError("portable-find binding comes from the future")

            observation = site_evidence.observations.get(row.observation_id)
            if observation is None:
                raise ValueError("portable-find binding references missing site observation")
            if observation.kind is not ObservationKind.PORTABLE_FIND:
                raise ValueError("portable-find binding requires a PORTABLE_FIND observation")
            if row.bound_at_semantic_minute < observation.semantic_minute:
                raise ValueError("portable-find binding predates its observation")
            if row.observation_sha256 != _observation_digest(observation):
                raise ValueError("portable-find binding observation provenance mismatch")

            _declared_resource(declared_resources, row.resource_id)

            if row.observation_id in seen_observations:
                raise ValueError("portable-find observation has multiple bindings")
            if row.resource_id in seen_resources:
                raise ValueError("world resource has multiple portable-find bindings")
            seen_observations.add(row.observation_id)
            seen_resources.add(row.resource_id)

    def binding_for_observation(self, observation_id: str) -> PortableFindResourceBinding | None:
        return next(
            (row for row in self.bindings.values() if row.observation_id == observation_id),
            None,
        )

    def binding_for_resource(self, resource_id: str) -> PortableFindResourceBinding | None:
        return next(
            (row for row in self.bindings.values() if row.resource_id == resource_id),
            None,
        )

    def snapshot(
        self,
        *,
        site_evidence: SiteEvidenceLedger,
        declared_resources: Mapping[str, WorldResource],
        semantic_minute: int | None = None,
    ) -> dict[str, object]:
        self.validate(
            site_evidence=site_evidence,
            declared_resources=declared_resources,
            semantic_minute=semantic_minute,
        )
        return {
            "schema": PORTABLE_FIND_RESOURCE_BINDING_SCHEMA,
            "bindings": [
                {
                    "binding_id": row.binding_id,
                    "observation_id": row.observation_id,
                    "resource_id": row.resource_id,
                    "bound_at_semantic_minute": row.bound_at_semantic_minute,
                    "bound_by_actor_id": row.bound_by_actor_id,
                    "authority_ref": row.authority_ref,
                    "observation_sha256": row.observation_sha256,
                }
                for row in sorted(
                    self.bindings.values(),
                    key=lambda value: (value.bound_at_semantic_minute, value.binding_id),
                )
            ],
        }

    @classmethod
    def restore(
        cls,
        snapshot: Mapping[str, object],
        *,
        site_evidence: SiteEvidenceLedger,
        declared_resources: Mapping[str, WorldResource],
        semantic_minute: int | None = None,
    ) -> "PortableFindResourceBindingLedger":
        if snapshot.get("schema") != PORTABLE_FIND_RESOURCE_BINDING_SCHEMA:
            raise ValueError("unsupported portable-find resource binding schema")

        ledger = cls()
        raw_bindings = snapshot.get("bindings", [])
        if not isinstance(raw_bindings, list):
            raise ValueError("portable-find binding snapshot requires bindings list")

        for raw in raw_bindings:
            if not isinstance(raw, Mapping):
                raise ValueError("invalid portable-find binding snapshot row")
            record = ledger.bind(
                binding_id=str(raw["binding_id"]),
                observation_id=str(raw["observation_id"]),
                resource_id=str(raw["resource_id"]),
                bound_at_semantic_minute=int(raw["bound_at_semantic_minute"]),
                bound_by_actor_id=str(raw["bound_by_actor_id"]),
                authority_ref=str(raw["authority_ref"]),
                site_evidence=site_evidence,
                declared_resources=declared_resources,
            )
            supplied_observation_digest = str(raw.get("observation_sha256", ""))
            if not supplied_observation_digest or supplied_observation_digest != record.observation_sha256:
                raise ValueError("portable-find binding observation provenance mismatch")

        ledger.validate(
            site_evidence=site_evidence,
            declared_resources=declared_resources,
            semantic_minute=semantic_minute,
        )
        return ledger
