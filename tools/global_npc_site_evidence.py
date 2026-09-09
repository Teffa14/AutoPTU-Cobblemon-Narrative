from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

SITE_EVIDENCE_SCHEMA = "OUROS_SITE_EVIDENCE_LEDGER_V1"

class SiteAccessState(str, Enum):
    OPEN = "OPEN"
    RESTRICTED = "RESTRICTED"
    CLOSED = "CLOSED"
    UNKNOWN = "UNKNOWN"

class ObservationKind(str, Enum):
    FIXED_FEATURE = "FIXED_FEATURE"
    PORTABLE_FIND = "PORTABLE_FIND"
    SPATIAL_RELATIONSHIP = "SPATIAL_RELATIONSHIP"
    MATERIAL_CONDITION = "MATERIAL_CONDITION"
    ACCESS_STATE = "ACCESS_STATE"

@dataclass(frozen=True)
class SiteRevisionRecord:
    revision_id: str
    site_id: str
    previous_revision_id: str | None
    semantic_minute: int
    access_state: SiteAccessState
    change_kind: str
    source_ref: str

@dataclass(frozen=True)
class SiteObservationRecord:
    observation_id: str
    site_id: str
    revision_id: str
    observer_id: str
    semantic_minute: int
    evidence_ref: str
    kind: ObservationKind
    content: str
    provenance_root: str

@dataclass(frozen=True)
class SiteInterpretationRecord:
    interpretation_id: str
    site_id: str
    actor_id: str
    semantic_minute: int
    observation_ids: tuple[str, ...]
    claim: str
    confidence: float
    supersedes_id: str | None = None

@dataclass
class SiteEvidenceLedger:
    revisions: dict[str, SiteRevisionRecord] = field(default_factory=dict)
    observations: dict[str, SiteObservationRecord] = field(default_factory=dict)
    interpretations: dict[str, SiteInterpretationRecord] = field(default_factory=dict)

    def record_revision(self, *, revision_id: str, site_id: str, semantic_minute: int, access_state: SiteAccessState, change_kind: str, source_ref: str, previous_revision_id: str | None = None) -> SiteRevisionRecord:
        if revision_id in self.revisions:
            raise ValueError(f"site revision already recorded: {revision_id}")
        if semantic_minute < 0 or not site_id or not change_kind or not source_ref:
            raise ValueError("invalid site revision")
        if previous_revision_id is None:
            if any(r.site_id == site_id for r in self.revisions.values()):
                raise ValueError("non-initial site revision requires previous revision")
        else:
            previous = self.revisions.get(previous_revision_id)
            if previous is None:
                raise ValueError("site revision references missing previous revision")
            if previous.site_id != site_id or previous.semantic_minute > semantic_minute:
                raise ValueError("invalid site revision ancestry")
            if any(r.previous_revision_id == previous_revision_id for r in self.revisions.values()):
                raise ValueError("site revision history cannot fork")
        record = SiteRevisionRecord(revision_id, site_id, previous_revision_id, semantic_minute, access_state, change_kind, source_ref)
        self.revisions[revision_id] = record
        return record

    def record_observation(self, *, observation_id: str, site_id: str, revision_id: str, observer_id: str, semantic_minute: int, evidence_ref: str, kind: ObservationKind, content: str, provenance_root: str) -> SiteObservationRecord:
        if observation_id in self.observations:
            raise ValueError(f"site observation already recorded: {observation_id}")
        revision = self.revisions.get(revision_id)
        if revision is None:
            raise ValueError("site observation references missing revision")
        if revision.site_id != site_id:
            raise ValueError("site observation revision belongs to another site")
        if semantic_minute < revision.semantic_minute:
            raise ValueError("site observation cannot predate its site revision")
        if not observer_id or not evidence_ref or not content or not provenance_root:
            raise ValueError("site observation requires observer, evidence, content and provenance")
        record = SiteObservationRecord(observation_id, site_id, revision_id, observer_id, semantic_minute, evidence_ref, kind, content, provenance_root)
        self.observations[observation_id] = record
        return record

    def record_interpretation(self, *, interpretation_id: str, site_id: str, actor_id: str, semantic_minute: int, observation_ids: tuple[str, ...], claim: str, confidence: float, supersedes_id: str | None = None) -> SiteInterpretationRecord:
        if interpretation_id in self.interpretations:
            raise ValueError(f"site interpretation already recorded: {interpretation_id}")
        if not 0.0 <= confidence <= 1.0 or not observation_ids or len(set(observation_ids)) != len(observation_ids):
            raise ValueError("invalid site interpretation")
        for observation_id in observation_ids:
            observation = self.observations.get(observation_id)
            if observation is None:
                raise ValueError("site interpretation references missing observation")
            if observation.site_id != site_id:
                raise ValueError("site interpretation cannot mix sites")
            if observation.semantic_minute > semantic_minute:
                raise ValueError("site interpretation cannot use future observation")
        if supersedes_id is not None:
            previous = self.interpretations.get(supersedes_id)
            if previous is None:
                raise ValueError("site interpretation supersedes missing interpretation")
            if previous.site_id != site_id or previous.actor_id != actor_id or previous.semantic_minute > semantic_minute:
                raise ValueError("invalid interpretation supersession")
        record = SiteInterpretationRecord(interpretation_id, site_id, actor_id, semantic_minute, tuple(observation_ids), claim, float(confidence), supersedes_id)
        self.interpretations[interpretation_id] = record
        return record

    def validate(self, *, semantic_minute: int | None = None) -> None:
        if semantic_minute is not None:
            for row in (*self.revisions.values(), *self.observations.values(), *self.interpretations.values()):
                if row.semantic_minute > semantic_minute:
                    raise ValueError("site evidence comes from the future")
        for row in self.observations.values():
            revision = self.revisions.get(row.revision_id)
            if revision is None or revision.site_id != row.site_id or row.semantic_minute < revision.semantic_minute:
                raise ValueError("invalid site observation provenance")
        for row in self.interpretations.values():
            if any(obs_id not in self.observations for obs_id in row.observation_ids):
                raise ValueError("site interpretation references missing observation")

    def snapshot(self) -> dict:
        self.validate()
        return {
            "schema": SITE_EVIDENCE_SCHEMA,
            "revisions": [dict(revision_id=r.revision_id, site_id=r.site_id, previous_revision_id=r.previous_revision_id, semantic_minute=r.semantic_minute, access_state=r.access_state.value, change_kind=r.change_kind, source_ref=r.source_ref) for r in sorted(self.revisions.values(), key=lambda x: (x.semantic_minute, x.revision_id))],
            "observations": [dict(observation_id=o.observation_id, site_id=o.site_id, revision_id=o.revision_id, observer_id=o.observer_id, semantic_minute=o.semantic_minute, evidence_ref=o.evidence_ref, kind=o.kind.value, content=o.content, provenance_root=o.provenance_root) for o in sorted(self.observations.values(), key=lambda x: (x.semantic_minute, x.observation_id))],
            "interpretations": [dict(interpretation_id=i.interpretation_id, site_id=i.site_id, actor_id=i.actor_id, semantic_minute=i.semantic_minute, observation_ids=list(i.observation_ids), claim=i.claim, confidence=i.confidence, supersedes_id=i.supersedes_id) for i in sorted(self.interpretations.values(), key=lambda x: (x.semantic_minute, x.interpretation_id))],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "SiteEvidenceLedger":
        if snapshot.get("schema") != SITE_EVIDENCE_SCHEMA:
            raise ValueError("unsupported site evidence schema")
        ledger = cls()
        for raw in snapshot.get("revisions", []):
            ledger.record_revision(revision_id=str(raw["revision_id"]), site_id=str(raw["site_id"]), previous_revision_id=None if raw.get("previous_revision_id") is None else str(raw["previous_revision_id"]), semantic_minute=int(raw["semantic_minute"]), access_state=SiteAccessState(str(raw["access_state"])), change_kind=str(raw["change_kind"]), source_ref=str(raw["source_ref"]))
        for raw in snapshot.get("observations", []):
            ledger.record_observation(observation_id=str(raw["observation_id"]), site_id=str(raw["site_id"]), revision_id=str(raw["revision_id"]), observer_id=str(raw["observer_id"]), semantic_minute=int(raw["semantic_minute"]), evidence_ref=str(raw["evidence_ref"]), kind=ObservationKind(str(raw["kind"])), content=str(raw["content"]), provenance_root=str(raw["provenance_root"]))
        for raw in snapshot.get("interpretations", []):
            ledger.record_interpretation(interpretation_id=str(raw["interpretation_id"]), site_id=str(raw["site_id"]), actor_id=str(raw["actor_id"]), semantic_minute=int(raw["semantic_minute"]), observation_ids=tuple(str(v) for v in raw.get("observation_ids", [])), claim=str(raw["claim"]), confidence=float(raw["confidence"]), supersedes_id=None if raw.get("supersedes_id") is None else str(raw["supersedes_id"]))
        ledger.validate()
        return ledger
