from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from tools.global_npc_memory import Claim, KnowledgeLedgerStore, SourceKind
from tools.global_npc_site_evidence import SiteEvidenceLedger


SITE_OBSERVATION_KNOWLEDGE_SCHEMA = "OUROS_SITE_OBSERVATION_KNOWLEDGE_V1"


@dataclass(frozen=True)
class SiteObservationKnowledgeRecord:
    materialization_id: str
    observation_id: str
    site_id: str
    revision_id: str
    evidence_ref: str
    agent_id: str
    claim_id: str
    semantic_minute: int


@dataclass
class SiteObservationKnowledgeLedger:
    records: dict[str, SiteObservationKnowledgeRecord] = field(default_factory=dict)

    @staticmethod
    def materialization_id_for(observation_id: str) -> str:
        return f"site-observation-materialization:{observation_id}"

    @staticmethod
    def claim_id_for(observation_id: str) -> str:
        return f"site-observation-claim:{observation_id}"

    @staticmethod
    def subject_for(observation_id: str) -> str:
        return f"site-observation:{observation_id}"

    def materialize_observation(
        self,
        *,
        observation_id: str,
        site_evidence: SiteEvidenceLedger,
        knowledge_store: KnowledgeLedgerStore,
    ) -> SiteObservationKnowledgeRecord:
        observation = site_evidence.observations.get(observation_id)
        if observation is None:
            raise ValueError("site knowledge materialization references missing observation")

        materialization_id = self.materialization_id_for(observation_id)
        existing = self.records.get(materialization_id)
        if existing is not None:
            return existing

        try:
            private_ledger = knowledge_store.require(observation.observer_id)
        except KeyError as exc:
            raise ValueError("site observer has no managed private knowledge ledger") from exc

        claim_id = self.claim_id_for(observation_id)
        claim = Claim(
            claim_id=claim_id,
            subject=self.subject_for(observation_id),
            value=observation.content,
            source_kind=SourceKind.DIRECT_OBSERVATION,
            source_agent_id=observation.observer_id,
            semantic_minute=observation.semantic_minute,
            confidence=100,
            provenance_root=observation.provenance_root,
        )
        private_ledger.add(claim)

        record = SiteObservationKnowledgeRecord(
            materialization_id=materialization_id,
            observation_id=observation.observation_id,
            site_id=observation.site_id,
            revision_id=observation.revision_id,
            evidence_ref=observation.evidence_ref,
            agent_id=observation.observer_id,
            claim_id=claim_id,
            semantic_minute=observation.semantic_minute,
        )
        self.records[materialization_id] = record
        return record

    def validate(
        self,
        *,
        site_evidence: SiteEvidenceLedger,
        knowledge_store: KnowledgeLedgerStore,
        semantic_minute: int | None = None,
    ) -> None:
        seen_observations: set[str] = set()
        for record in self.records.values():
            if record.observation_id in seen_observations:
                raise ValueError("site observation materialized more than once")
            seen_observations.add(record.observation_id)

            observation = site_evidence.observations.get(record.observation_id)
            if observation is None:
                raise ValueError("site knowledge materialization references missing observation")
            if record.materialization_id != self.materialization_id_for(record.observation_id):
                raise ValueError("invalid site knowledge materialization identity")
            if record.claim_id != self.claim_id_for(record.observation_id):
                raise ValueError("invalid site observation claim identity")
            if record.agent_id != observation.observer_id:
                raise ValueError("site observation cannot materialize to a non-observer")
            if (
                record.site_id != observation.site_id
                or record.revision_id != observation.revision_id
                or record.evidence_ref != observation.evidence_ref
                or record.semantic_minute != observation.semantic_minute
            ):
                raise ValueError("site knowledge materialization diverges from observation provenance")
            if semantic_minute is not None and record.semantic_minute > semantic_minute:
                raise ValueError("site knowledge materialization comes from the future")

            try:
                private_ledger = knowledge_store.require(record.agent_id)
            except KeyError as exc:
                raise ValueError("site observer has no managed private knowledge ledger") from exc
            claim = private_ledger.claims.get(record.claim_id)
            if claim is None:
                raise ValueError("site knowledge materialization is missing its private claim")
            if (
                claim.subject != self.subject_for(record.observation_id)
                or claim.value != observation.content
                or claim.source_kind is not SourceKind.DIRECT_OBSERVATION
                or claim.source_agent_id != observation.observer_id
                or claim.semantic_minute != observation.semantic_minute
                or claim.confidence != 100
                or claim.provenance_root != observation.provenance_root
                or claim.parent_claim_id is not None
                or claim.message_id is not None
            ):
                raise ValueError("private site-observation claim diverges from source evidence")

    def snapshot(self) -> dict:
        return {
            "schema": SITE_OBSERVATION_KNOWLEDGE_SCHEMA,
            "records": [
                {
                    "materialization_id": row.materialization_id,
                    "observation_id": row.observation_id,
                    "site_id": row.site_id,
                    "revision_id": row.revision_id,
                    "evidence_ref": row.evidence_ref,
                    "agent_id": row.agent_id,
                    "claim_id": row.claim_id,
                    "semantic_minute": row.semantic_minute,
                }
                for row in sorted(
                    self.records.values(),
                    key=lambda value: (value.semantic_minute, value.materialization_id),
                )
            ],
        }

    @classmethod
    def restore(
        cls,
        snapshot: Mapping[str, object],
        *,
        site_evidence: SiteEvidenceLedger,
        knowledge_store: KnowledgeLedgerStore,
        semantic_minute: int | None = None,
    ) -> "SiteObservationKnowledgeLedger":
        if snapshot.get("schema") != SITE_OBSERVATION_KNOWLEDGE_SCHEMA:
            raise ValueError("unsupported site observation knowledge schema")
        ledger = cls()
        rows = snapshot.get("records", [])
        if not isinstance(rows, list):
            raise ValueError("site observation knowledge records must be a list")
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("site observation knowledge row must be a mapping")
            record = SiteObservationKnowledgeRecord(
                materialization_id=str(raw["materialization_id"]),
                observation_id=str(raw["observation_id"]),
                site_id=str(raw["site_id"]),
                revision_id=str(raw["revision_id"]),
                evidence_ref=str(raw["evidence_ref"]),
                agent_id=str(raw["agent_id"]),
                claim_id=str(raw["claim_id"]),
                semantic_minute=int(raw["semantic_minute"]),
            )
            if record.materialization_id in ledger.records:
                raise ValueError("duplicate site observation materialization")
            ledger.records[record.materialization_id] = record
        ledger.validate(
            site_evidence=site_evidence,
            knowledge_store=knowledge_store,
            semantic_minute=semantic_minute,
        )
        return ledger
