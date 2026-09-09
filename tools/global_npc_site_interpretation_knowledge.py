from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from tools.global_npc_memory import Claim, KnowledgeLedgerStore, SourceKind
from tools.global_npc_site_evidence import SiteEvidenceLedger


SITE_INTERPRETATION_KNOWLEDGE_SCHEMA = "OUROS_SITE_INTERPRETATION_KNOWLEDGE_V1"


@dataclass(frozen=True)
class SiteInterpretationKnowledgeRecord:
    materialization_id: str
    interpretation_id: str
    site_id: str
    agent_id: str
    claim_id: str
    semantic_minute: int
    observation_ids: tuple[str, ...]
    source_provenance_roots: tuple[str, ...]
    supersedes_id: str | None
    parent_claim_id: str | None


@dataclass
class SiteInterpretationKnowledgeLedger:
    records: dict[str, SiteInterpretationKnowledgeRecord] = field(default_factory=dict)

    @staticmethod
    def materialization_id_for(interpretation_id: str) -> str:
        return f"site-interpretation-materialization:{interpretation_id}"

    @staticmethod
    def claim_id_for(interpretation_id: str) -> str:
        return f"site-interpretation-claim:{interpretation_id}"

    @staticmethod
    def subject_for(site_id: str) -> str:
        return f"site-interpretation:{site_id}"

    @staticmethod
    def observation_subject(observation_id: str) -> str:
        return f"site-observation:{observation_id}"

    @staticmethod
    def confidence_percent(confidence: float) -> int:
        return max(0, min(100, int(round(confidence * 100))))

    def _source_roots_known_by_actor(self, *, interpretation_id: str, site_evidence: SiteEvidenceLedger, knowledge_store: KnowledgeLedgerStore) -> tuple[str, ...]:
        interpretation = site_evidence.interpretations[interpretation_id]
        try:
            private_ledger = knowledge_store.require(interpretation.actor_id)
        except KeyError as exc:
            raise ValueError("site interpreter has no managed private knowledge ledger") from exc

        roots: set[str] = set()
        for observation_id in interpretation.observation_ids:
            observation = site_evidence.observations[observation_id]
            candidates = [
                claim
                for claim in private_ledger.claims_for(self.observation_subject(observation_id))
                if claim.semantic_minute <= interpretation.semantic_minute
                and claim.value == observation.content
                and claim.provenance_root == observation.provenance_root
            ]
            if not candidates:
                raise ValueError("site interpreter lacks explicit private knowledge of supporting observation")
            roots.add(observation.provenance_root)
        return tuple(sorted(roots))

    def materialize_interpretation(self, *, interpretation_id: str, site_evidence: SiteEvidenceLedger, knowledge_store: KnowledgeLedgerStore) -> SiteInterpretationKnowledgeRecord:
        interpretation = site_evidence.interpretations.get(interpretation_id)
        if interpretation is None:
            raise ValueError("site inference materialization references missing interpretation")

        materialization_id = self.materialization_id_for(interpretation_id)
        existing = self.records.get(materialization_id)
        if existing is not None:
            return existing

        roots = self._source_roots_known_by_actor(
            interpretation_id=interpretation_id,
            site_evidence=site_evidence,
            knowledge_store=knowledge_store,
        )
        private_ledger = knowledge_store.require(interpretation.actor_id)

        parent_claim_id = None
        provenance_root = roots[0]
        if interpretation.supersedes_id is not None:
            parent_record = self.records.get(self.materialization_id_for(interpretation.supersedes_id))
            if parent_record is None:
                raise ValueError("superseding site interpretation requires prior private inference materialization")
            if parent_record.agent_id != interpretation.actor_id or parent_record.site_id != interpretation.site_id:
                raise ValueError("invalid private interpretation supersession")
            parent_claim_id = parent_record.claim_id
            parent_claim = private_ledger.claims.get(parent_claim_id)
            if parent_claim is None:
                raise ValueError("superseding site interpretation is missing parent private claim")
            provenance_root = parent_claim.provenance_root

        claim_id = self.claim_id_for(interpretation_id)
        private_ledger.add(Claim(
            claim_id=claim_id,
            subject=self.subject_for(interpretation.site_id),
            value=interpretation.claim,
            source_kind=SourceKind.INFERENCE,
            source_agent_id=interpretation.actor_id,
            semantic_minute=interpretation.semantic_minute,
            confidence=self.confidence_percent(interpretation.confidence),
            provenance_root=provenance_root,
            parent_claim_id=parent_claim_id,
        ))

        record = SiteInterpretationKnowledgeRecord(
            materialization_id=materialization_id,
            interpretation_id=interpretation.interpretation_id,
            site_id=interpretation.site_id,
            agent_id=interpretation.actor_id,
            claim_id=claim_id,
            semantic_minute=interpretation.semantic_minute,
            observation_ids=tuple(interpretation.observation_ids),
            source_provenance_roots=roots,
            supersedes_id=interpretation.supersedes_id,
            parent_claim_id=parent_claim_id,
        )
        self.records[materialization_id] = record
        return record

    def validate(self, *, site_evidence: SiteEvidenceLedger, knowledge_store: KnowledgeLedgerStore, semantic_minute: int | None = None) -> None:
        seen: set[str] = set()
        for record in self.records.values():
            if record.interpretation_id in seen:
                raise ValueError("site interpretation materialized more than once")
            seen.add(record.interpretation_id)

            interpretation = site_evidence.interpretations.get(record.interpretation_id)
            if interpretation is None:
                raise ValueError("site inference materialization references missing interpretation")
            if record.materialization_id != self.materialization_id_for(record.interpretation_id) or record.claim_id != self.claim_id_for(record.interpretation_id):
                raise ValueError("invalid site interpretation materialization identity")
            if record.site_id != interpretation.site_id or record.agent_id != interpretation.actor_id or record.semantic_minute != interpretation.semantic_minute:
                raise ValueError("site inference materialization diverges from interpretation provenance")
            if record.observation_ids != tuple(interpretation.observation_ids) or record.supersedes_id != interpretation.supersedes_id:
                raise ValueError("site inference materialization diverges from supporting interpretation")
            if semantic_minute is not None and record.semantic_minute > semantic_minute:
                raise ValueError("site inference materialization comes from the future")

            roots = self._source_roots_known_by_actor(
                interpretation_id=record.interpretation_id,
                site_evidence=site_evidence,
                knowledge_store=knowledge_store,
            )
            if roots != record.source_provenance_roots:
                raise ValueError("site inference materialization diverges from source provenance roots")

            private_ledger = knowledge_store.require(record.agent_id)
            claim = private_ledger.claims.get(record.claim_id)
            if claim is None:
                raise ValueError("site inference materialization is missing its private claim")

            expected_parent = None
            expected_root = roots[0]
            if interpretation.supersedes_id is not None:
                parent_record = self.records.get(self.materialization_id_for(interpretation.supersedes_id))
                if parent_record is None:
                    raise ValueError("superseding site interpretation requires prior private inference materialization")
                expected_parent = parent_record.claim_id
                parent_claim = private_ledger.claims.get(expected_parent)
                if parent_claim is None:
                    raise ValueError("superseding site interpretation is missing parent private claim")
                expected_root = parent_claim.provenance_root
            if record.parent_claim_id != expected_parent:
                raise ValueError("site inference parent lineage diverges from supersession")
            if (
                claim.subject != self.subject_for(interpretation.site_id)
                or claim.value != interpretation.claim
                or claim.source_kind is not SourceKind.INFERENCE
                or claim.source_agent_id != interpretation.actor_id
                or claim.semantic_minute != interpretation.semantic_minute
                or claim.confidence != self.confidence_percent(interpretation.confidence)
                or claim.provenance_root != expected_root
                or claim.parent_claim_id != expected_parent
                or claim.message_id is not None
            ):
                raise ValueError("private site-inference claim diverges from source interpretation")

    def snapshot(self) -> dict:
        return {
            "schema": SITE_INTERPRETATION_KNOWLEDGE_SCHEMA,
            "records": [
                {
                    "materialization_id": row.materialization_id,
                    "interpretation_id": row.interpretation_id,
                    "site_id": row.site_id,
                    "agent_id": row.agent_id,
                    "claim_id": row.claim_id,
                    "semantic_minute": row.semantic_minute,
                    "observation_ids": list(row.observation_ids),
                    "source_provenance_roots": list(row.source_provenance_roots),
                    "supersedes_id": row.supersedes_id,
                    "parent_claim_id": row.parent_claim_id,
                }
                for row in sorted(self.records.values(), key=lambda value: (value.semantic_minute, value.materialization_id))
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object], *, site_evidence: SiteEvidenceLedger, knowledge_store: KnowledgeLedgerStore, semantic_minute: int | None = None) -> "SiteInterpretationKnowledgeLedger":
        if snapshot.get("schema") != SITE_INTERPRETATION_KNOWLEDGE_SCHEMA:
            raise ValueError("unsupported site interpretation knowledge schema")
        rows = snapshot.get("records", [])
        if not isinstance(rows, list):
            raise ValueError("site interpretation knowledge records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("site interpretation knowledge row must be a mapping")
            record = SiteInterpretationKnowledgeRecord(
                materialization_id=str(raw["materialization_id"]),
                interpretation_id=str(raw["interpretation_id"]),
                site_id=str(raw["site_id"]),
                agent_id=str(raw["agent_id"]),
                claim_id=str(raw["claim_id"]),
                semantic_minute=int(raw["semantic_minute"]),
                observation_ids=tuple(str(value) for value in raw.get("observation_ids", [])),
                source_provenance_roots=tuple(str(value) for value in raw.get("source_provenance_roots", [])),
                supersedes_id=None if raw.get("supersedes_id") is None else str(raw["supersedes_id"]),
                parent_claim_id=None if raw.get("parent_claim_id") is None else str(raw["parent_claim_id"]),
            )
            if record.materialization_id in ledger.records:
                raise ValueError("duplicate site interpretation materialization")
            ledger.records[record.materialization_id] = record
        ledger.validate(site_evidence=site_evidence, knowledge_store=knowledge_store, semantic_minute=semantic_minute)
        return ledger
