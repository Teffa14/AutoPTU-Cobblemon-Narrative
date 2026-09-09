from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_memory import KnowledgeLedgerStore
from tools.global_npc_portable_find_resource_binding import (
    PORTABLE_FIND_RESOURCE_BINDING_SCHEMA,
    PortableFindResourceBindingLedger,
)
from tools.global_npc_resources import WorldResource
from tools.global_npc_site_evidence import SITE_EVIDENCE_SCHEMA, SiteEvidenceLedger
from tools.global_npc_site_observation_knowledge import (
    SITE_OBSERVATION_KNOWLEDGE_SCHEMA,
    SiteObservationKnowledgeLedger,
)
from tools.global_npc_site_interpretation_knowledge import (
    SITE_INTERPRETATION_KNOWLEDGE_SCHEMA,
    SiteInterpretationKnowledgeLedger,
)


LEGACY_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA = "OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1"
PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA = "OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2"


@dataclass(frozen=True)
class RestoredPersistentWorldEvidenceCheckpoint:
    semantic_minute: int
    site_evidence: SiteEvidenceLedger
    observation_knowledge: SiteObservationKnowledgeLedger
    interpretation_knowledge: SiteInterpretationKnowledgeLedger
    portable_find_bindings: PortableFindResourceBindingLedger
    knowledge_store_sha256: str
    resource_identity_catalog_sha256: str | None


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def knowledge_store_digest(knowledge_store: KnowledgeLedgerStore) -> str:
    return _digest(knowledge_store.snapshot())


def resource_identity_catalog_digest(declared_resources: Mapping[str, WorldResource]) -> str:
    """Fingerprint only stable resource identities, not mutable operational resource state.

    Holder, location, reservation, quantity and current state remain owned by the resource/custody
    systems. This digest proves which declared resource identities existed for evidence bindings at
    checkpoint time without turning persistent-world evidence into a second resource-state owner.
    """
    resource_ids: list[str] = []
    for key, resource in declared_resources.items():
        if key != resource.resource_id:
            raise ValueError("world resource declaration key does not match resource identity")
        resource_ids.append(resource.resource_id)
    return _digest({"resource_ids": sorted(resource_ids)})


def build_persistent_world_evidence_checkpoint(
    *,
    semantic_minute: int,
    site_evidence: SiteEvidenceLedger,
    observation_knowledge: SiteObservationKnowledgeLedger,
    interpretation_knowledge: SiteInterpretationKnowledgeLedger,
    knowledge_store: KnowledgeLedgerStore,
    portable_find_bindings: PortableFindResourceBindingLedger | None = None,
    declared_resources: Mapping[str, WorldResource] | None = None,
) -> dict:
    """Bind durable world evidence to the external private-knowledge and resource identities it uses.

    This checkpoint owns evidence history and cross-system evidence bridges. It does not own private
    NPC claims or mutable WorldResource state. Digests prevent recovery against incompatible external
    owners while keeping those owners separate.
    """
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    resources = declared_resources or {}
    bindings = portable_find_bindings or PortableFindResourceBindingLedger()

    site_evidence.validate(semantic_minute=semantic_minute)
    observation_knowledge.validate(
        site_evidence=site_evidence,
        knowledge_store=knowledge_store,
        semantic_minute=semantic_minute,
    )
    interpretation_knowledge.validate(
        site_evidence=site_evidence,
        knowledge_store=knowledge_store,
        semantic_minute=semantic_minute,
    )
    binding_snapshot = bindings.snapshot(
        site_evidence=site_evidence,
        declared_resources=resources,
        semantic_minute=semantic_minute,
    )
    payload = {
        "schema": PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
        "semantic_minute": semantic_minute,
        "knowledge_store_sha256": knowledge_store_digest(knowledge_store),
        "resource_identity_catalog_sha256": resource_identity_catalog_digest(resources),
        "site_evidence": site_evidence.snapshot(),
        "observation_knowledge": observation_knowledge.snapshot(),
        "interpretation_knowledge": interpretation_knowledge.snapshot(),
        "portable_find_bindings": binding_snapshot,
    }
    return payload | {"sha256": _digest(payload)}


def restore_persistent_world_evidence_checkpoint(
    snapshot: Mapping[str, object],
    *,
    knowledge_store: KnowledgeLedgerStore,
    declared_resources: Mapping[str, WorldResource] | None = None,
) -> RestoredPersistentWorldEvidenceCheckpoint:
    schema = snapshot.get("schema")
    if schema not in {
        LEGACY_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
        PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
    }:
        raise ValueError("unsupported persistent world evidence checkpoint schema")

    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest:
        raise ValueError("persistent world evidence checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != supplied_digest:
        raise ValueError("persistent world evidence checkpoint digest mismatch")

    semantic_minute = int(payload["semantic_minute"])
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")

    expected_store_digest = payload.get("knowledge_store_sha256")
    if not isinstance(expected_store_digest, str) or not expected_store_digest:
        raise ValueError("knowledge store digest is required")
    actual_store_digest = knowledge_store_digest(knowledge_store)
    if actual_store_digest != expected_store_digest:
        raise ValueError("persistent world evidence checkpoint does not match private knowledge state")

    raw_evidence = payload.get("site_evidence")
    raw_observation_bridge = payload.get("observation_knowledge")
    raw_interpretation_bridge = payload.get("interpretation_knowledge")
    if not isinstance(raw_evidence, Mapping) or raw_evidence.get("schema") != SITE_EVIDENCE_SCHEMA:
        raise ValueError("persistent world evidence checkpoint requires site evidence V1")
    if not isinstance(raw_observation_bridge, Mapping) or raw_observation_bridge.get("schema") != SITE_OBSERVATION_KNOWLEDGE_SCHEMA:
        raise ValueError("persistent world evidence checkpoint requires observation knowledge V1")
    if not isinstance(raw_interpretation_bridge, Mapping) or raw_interpretation_bridge.get("schema") != SITE_INTERPRETATION_KNOWLEDGE_SCHEMA:
        raise ValueError("persistent world evidence checkpoint requires interpretation knowledge V1")

    site_evidence = SiteEvidenceLedger.restore(raw_evidence)
    site_evidence.validate(semantic_minute=semantic_minute)
    observation_knowledge = SiteObservationKnowledgeLedger.restore(
        raw_observation_bridge,
        site_evidence=site_evidence,
        knowledge_store=knowledge_store,
        semantic_minute=semantic_minute,
    )
    interpretation_knowledge = SiteInterpretationKnowledgeLedger.restore(
        raw_interpretation_bridge,
        site_evidence=site_evidence,
        knowledge_store=knowledge_store,
        semantic_minute=semantic_minute,
    )

    resources = declared_resources or {}
    if schema == LEGACY_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA:
        bindings = PortableFindResourceBindingLedger()
        resource_catalog_digest: str | None = None
    else:
        expected_resource_digest = payload.get("resource_identity_catalog_sha256")
        if not isinstance(expected_resource_digest, str) or not expected_resource_digest:
            raise ValueError("resource identity catalog digest is required")
        actual_resource_digest = resource_identity_catalog_digest(resources)
        if actual_resource_digest != expected_resource_digest:
            raise ValueError("persistent world evidence checkpoint does not match declared resource identities")

        raw_bindings = payload.get("portable_find_bindings")
        if not isinstance(raw_bindings, Mapping) or raw_bindings.get("schema") != PORTABLE_FIND_RESOURCE_BINDING_SCHEMA:
            raise ValueError("persistent world evidence checkpoint requires portable-find resource binding V1")
        bindings = PortableFindResourceBindingLedger.restore(
            raw_bindings,
            site_evidence=site_evidence,
            declared_resources=resources,
            semantic_minute=semantic_minute,
        )
        resource_catalog_digest = expected_resource_digest

    return RestoredPersistentWorldEvidenceCheckpoint(
        semantic_minute=semantic_minute,
        site_evidence=site_evidence,
        observation_knowledge=observation_knowledge,
        interpretation_knowledge=interpretation_knowledge,
        portable_find_bindings=bindings,
        knowledge_store_sha256=expected_store_digest,
        resource_identity_catalog_sha256=resource_catalog_digest,
    )
