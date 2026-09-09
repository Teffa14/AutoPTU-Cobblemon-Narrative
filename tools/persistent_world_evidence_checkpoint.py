from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_memory import KnowledgeLedgerStore
from tools.global_npc_site_evidence import SITE_EVIDENCE_SCHEMA, SiteEvidenceLedger
from tools.global_npc_site_observation_knowledge import (
    SITE_OBSERVATION_KNOWLEDGE_SCHEMA,
    SiteObservationKnowledgeLedger,
)
from tools.global_npc_site_interpretation_knowledge import (
    SITE_INTERPRETATION_KNOWLEDGE_SCHEMA,
    SiteInterpretationKnowledgeLedger,
)


PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA = "OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1"


@dataclass(frozen=True)
class RestoredPersistentWorldEvidenceCheckpoint:
    semantic_minute: int
    site_evidence: SiteEvidenceLedger
    observation_knowledge: SiteObservationKnowledgeLedger
    interpretation_knowledge: SiteInterpretationKnowledgeLedger
    knowledge_store_sha256: str


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def knowledge_store_digest(knowledge_store: KnowledgeLedgerStore) -> str:
    return _digest(knowledge_store.snapshot())


def build_persistent_world_evidence_checkpoint(
    *,
    semantic_minute: int,
    site_evidence: SiteEvidenceLedger,
    observation_knowledge: SiteObservationKnowledgeLedger,
    interpretation_knowledge: SiteInterpretationKnowledgeLedger,
    knowledge_store: KnowledgeLedgerStore,
) -> dict:
    """Bind durable site evidence to the exact private-knowledge state that justifies its bridges.

    This checkpoint owns world-evidence history and bridge provenance. It does not own
    private NPC ledgers; those remain in KnowledgeLedgerStore/global-NPC recovery.
    The store digest prevents restoring site bridges against a different private history.
    """
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
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
    payload = {
        "schema": PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
        "semantic_minute": semantic_minute,
        "knowledge_store_sha256": knowledge_store_digest(knowledge_store),
        "site_evidence": site_evidence.snapshot(),
        "observation_knowledge": observation_knowledge.snapshot(),
        "interpretation_knowledge": interpretation_knowledge.snapshot(),
    }
    return payload | {"sha256": _digest(payload)}


def restore_persistent_world_evidence_checkpoint(
    snapshot: Mapping[str, object],
    *,
    knowledge_store: KnowledgeLedgerStore,
) -> RestoredPersistentWorldEvidenceCheckpoint:
    if snapshot.get("schema") != PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA:
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

    return RestoredPersistentWorldEvidenceCheckpoint(
        semantic_minute=semantic_minute,
        site_evidence=site_evidence,
        observation_knowledge=observation_knowledge,
        interpretation_knowledge=interpretation_knowledge,
        knowledge_store_sha256=expected_store_digest,
    )
