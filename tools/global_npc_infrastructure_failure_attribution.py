from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_disclosure_opportunity import (
    CommunicationAccessEvidence,
    CommunicationAccessStatus,
)
from tools.global_npc_memory import KnowledgeLedger


INFRASTRUCTURE_ATTRIBUTION_SNAPSHOT_SCHEMA = "OUROS_NPC_INFRASTRUCTURE_FAILURE_ATTRIBUTION_V1"


class InfrastructureEvidenceKind(str, Enum):
    ACCIDENTAL_CAUSE = "ACCIDENTAL_CAUSE"
    TAMPERING_TRACE = "TAMPERING_TRACE"
    CONTRIBUTION_LINK = "CONTRIBUTION_LINK"
    ACTOR_LINK = "ACTOR_LINK"
    INTENT_EVIDENCE = "INTENT_EVIDENCE"


class InfrastructureCauseStructure(str, Enum):
    UNRESOLVED = "UNRESOLVED"
    ACCIDENT_ONLY = "ACCIDENT_ONLY"
    TAMPERING_ONLY = "TAMPERING_ONLY"
    CONTESTED = "CONTESTED"
    CONCURRENT = "CONCURRENT"


class InfrastructureAttributionStatus(str, Enum):
    CAUSE_UNRESOLVED = "CAUSE_UNRESOLVED"
    ACCIDENTAL_CAUSE_SUPPORTED = "ACCIDENTAL_CAUSE_SUPPORTED"
    TAMPERING_CORROBORATED = "TAMPERING_CORROBORATED"
    CONTRIBUTING_CAUSES_CORROBORATED = "CONTRIBUTING_CAUSES_CORROBORATED"
    SABOTEUR_LINKED = "SABOTEUR_LINKED"
    SABOTAGE_INTENT_ATTRIBUTED = "SABOTAGE_INTENT_ATTRIBUTED"
    CAUSE_CONTESTED = "CAUSE_CONTESTED"


@dataclass(frozen=True)
class InfrastructureFailureIncident:
    incident_id: str
    infrastructure_id: str
    observed_semantic_minute: int
    failure_ref: str
    provenance_refs: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.incident_id:
            raise ValueError("incident_id is required")
        if not self.infrastructure_id:
            raise ValueError("infrastructure_id is required")
        if not self.failure_ref:
            raise ValueError("failure_ref is required")
        if not self.provenance_refs:
            raise ValueError("infrastructure failure requires provenance")


@dataclass(frozen=True)
class InfrastructureCausalEvidence:
    claim_id: str
    kind: InfrastructureEvidenceKind
    incident_id: str
    linked_actor_id: str | None = None


@dataclass(frozen=True)
class InfrastructureAttributionFinding:
    finding_id: str
    discoverer_id: str
    incident_id: str
    infrastructure_id: str
    semantic_minute: int
    status: InfrastructureAttributionStatus
    evidence_claim_ids: tuple[str, ...]
    linked_actor_id: str | None = None
    cause_structure: InfrastructureCauseStructure = InfrastructureCauseStructure.UNRESOLVED

    def to_snapshot(self) -> dict:
        return {
            "finding_id": self.finding_id,
            "discoverer_id": self.discoverer_id,
            "incident_id": self.incident_id,
            "infrastructure_id": self.infrastructure_id,
            "semantic_minute": self.semantic_minute,
            "status": self.status.value,
            "evidence_claim_ids": list(self.evidence_claim_ids),
            "linked_actor_id": self.linked_actor_id,
            "cause_structure": self.cause_structure.value,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "InfrastructureAttributionFinding":
        status = InfrastructureAttributionStatus(str(raw["status"]))
        raw_structure = raw.get("cause_structure")
        if raw_structure is None:
            legacy_map = {
                InfrastructureAttributionStatus.CAUSE_UNRESOLVED: InfrastructureCauseStructure.UNRESOLVED,
                InfrastructureAttributionStatus.ACCIDENTAL_CAUSE_SUPPORTED: InfrastructureCauseStructure.ACCIDENT_ONLY,
                InfrastructureAttributionStatus.TAMPERING_CORROBORATED: InfrastructureCauseStructure.TAMPERING_ONLY,
                InfrastructureAttributionStatus.SABOTEUR_LINKED: InfrastructureCauseStructure.TAMPERING_ONLY,
                InfrastructureAttributionStatus.SABOTAGE_INTENT_ATTRIBUTED: InfrastructureCauseStructure.TAMPERING_ONLY,
                InfrastructureAttributionStatus.CAUSE_CONTESTED: InfrastructureCauseStructure.CONTESTED,
                InfrastructureAttributionStatus.CONTRIBUTING_CAUSES_CORROBORATED: InfrastructureCauseStructure.CONCURRENT,
            }
            cause_structure = legacy_map[status]
        else:
            cause_structure = InfrastructureCauseStructure(str(raw_structure))
        return cls(
            finding_id=str(raw["finding_id"]),
            discoverer_id=str(raw["discoverer_id"]),
            incident_id=str(raw["incident_id"]),
            infrastructure_id=str(raw["infrastructure_id"]),
            semantic_minute=int(raw["semantic_minute"]),
            status=status,
            evidence_claim_ids=tuple(str(value) for value in raw.get("evidence_claim_ids", [])),
            linked_actor_id=None if raw.get("linked_actor_id") is None else str(raw["linked_actor_id"]),
            cause_structure=cause_structure,
        )


@dataclass
class InfrastructureAttributionRegistry:
    findings: dict[str, InfrastructureAttributionFinding] = field(default_factory=dict)

    def add(self, finding: InfrastructureAttributionFinding) -> None:
        existing = self.findings.get(finding.finding_id)
        if existing is not None and existing != finding:
            raise ValueError(f"finding_id collision: {finding.finding_id}")
        self.findings[finding.finding_id] = finding

    def snapshot(self) -> dict:
        return {
            "schema": INFRASTRUCTURE_ATTRIBUTION_SNAPSHOT_SCHEMA,
            "findings": [self.findings[key].to_snapshot() for key in sorted(self.findings)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "InfrastructureAttributionRegistry":
        if snapshot.get("schema") != INFRASTRUCTURE_ATTRIBUTION_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported infrastructure attribution snapshot schema")
        registry = cls()
        for raw in snapshot.get("findings", []):
            if not isinstance(raw, Mapping):
                raise ValueError("infrastructure attribution row must be a mapping")
            registry.add(InfrastructureAttributionFinding.from_snapshot(raw))
        return registry


def incident_from_communication_failure(
    access: CommunicationAccessEvidence,
    *,
    incident_id: str,
    infrastructure_id: str,
    semantic_minute: int,
) -> InfrastructureFailureIncident:
    """Bind a proven communication failure to a physical/logical infrastructure incident.

    The failure becomes an investigation subject. It does not imply an accidental cause,
    tampering, sabotage, or a responsible actor.
    """
    if access.status not in (
        CommunicationAccessStatus.CHANNEL_UNAVAILABLE,
        CommunicationAccessStatus.DELIVERY_FAILED,
    ):
        raise ValueError("infrastructure incident requires failed/unavailable communication access")
    if semantic_minute < access.semantic_minute:
        raise ValueError("infrastructure incident cannot precede access evidence")
    return InfrastructureFailureIncident(
        incident_id=incident_id,
        infrastructure_id=infrastructure_id,
        observed_semantic_minute=semantic_minute,
        failure_ref=access.evidence_id,
        provenance_refs=access.provenance_refs,
    )


def assess_infrastructure_failure(
    discoverer: KnowledgeLedger,
    incident: InfrastructureFailureIncident,
    *,
    finding_id: str,
    evidence: tuple[InfrastructureCausalEvidence, ...],
    semantic_minute: int,
    minimum_evidence_confidence: int = 60,
) -> InfrastructureAttributionFinding:
    """Assess cause and responsibility from evidence actually available to one NPC.

    Repeated claims from one provenance root count once. Failure alone never implies
    sabotage. Actor access/opportunity alone never proves tampering or intent. Independent
    accidental and tampering evidence remain contested unless a separate contribution-link
    claim supports a combined causal explanation.
    """
    if semantic_minute < incident.observed_semantic_minute:
        raise ValueError("attribution cannot precede the infrastructure failure")

    roots: set[str] = set()
    ordered_ids: list[str] = []
    accidental = False
    tampering = False
    contribution_link = False
    actor_links: set[str] = set()
    intent_links: set[str] = set()

    for ref in sorted(evidence, key=lambda item: (item.claim_id, item.kind.value, item.linked_actor_id or "")):
        if ref.incident_id != incident.incident_id:
            raise ValueError("causal evidence targets a different infrastructure incident")
        claim = discoverer.claims[ref.claim_id]
        if claim.semantic_minute > semantic_minute:
            raise ValueError("causal evidence cannot come from the future")
        if claim.confidence < minimum_evidence_confidence:
            raise ValueError("causal evidence below threshold")
        if claim.provenance_root in roots:
            continue
        roots.add(claim.provenance_root)
        ordered_ids.append(ref.claim_id)

        if ref.kind is InfrastructureEvidenceKind.ACCIDENTAL_CAUSE:
            if ref.linked_actor_id is not None:
                raise ValueError("accidental-cause evidence cannot name a responsible actor")
            accidental = True
        elif ref.kind is InfrastructureEvidenceKind.TAMPERING_TRACE:
            if ref.linked_actor_id is not None:
                raise ValueError("tampering trace records physical cause, not actor identity")
            tampering = True
        elif ref.kind is InfrastructureEvidenceKind.CONTRIBUTION_LINK:
            if ref.linked_actor_id is not None:
                raise ValueError("contribution-link evidence records causal composition, not actor identity")
            contribution_link = True
        elif ref.kind is InfrastructureEvidenceKind.ACTOR_LINK:
            if not ref.linked_actor_id:
                raise ValueError("actor-link evidence requires linked_actor_id")
            actor_links.add(ref.linked_actor_id)
        elif ref.kind is InfrastructureEvidenceKind.INTENT_EVIDENCE:
            if not ref.linked_actor_id:
                raise ValueError("intent evidence requires linked_actor_id")
            if claim.source_agent_id != ref.linked_actor_id:
                raise ValueError("intent evidence must be attributable to the linked actor")
            intent_links.add(ref.linked_actor_id)
        else:
            raise ValueError("unsupported infrastructure evidence kind")

    if contribution_link and not (accidental and tampering):
        raise ValueError("contribution-link evidence requires independent accidental and tampering support")

    linked_candidates = sorted(actor_links)
    intent_candidates = sorted(actor_links & intent_links)

    if accidental and tampering and contribution_link:
        cause_structure = InfrastructureCauseStructure.CONCURRENT
        if len(intent_candidates) == 1:
            status = InfrastructureAttributionStatus.SABOTAGE_INTENT_ATTRIBUTED
            linked_actor_id = intent_candidates[0]
        elif len(linked_candidates) == 1:
            status = InfrastructureAttributionStatus.SABOTEUR_LINKED
            linked_actor_id = linked_candidates[0]
        else:
            status = InfrastructureAttributionStatus.CONTRIBUTING_CAUSES_CORROBORATED
            linked_actor_id = None
    elif accidental and tampering:
        cause_structure = InfrastructureCauseStructure.CONTESTED
        status = InfrastructureAttributionStatus.CAUSE_CONTESTED
        linked_actor_id = None
    elif tampering:
        cause_structure = InfrastructureCauseStructure.TAMPERING_ONLY
        if len(intent_candidates) == 1:
            status = InfrastructureAttributionStatus.SABOTAGE_INTENT_ATTRIBUTED
            linked_actor_id = intent_candidates[0]
        elif len(linked_candidates) == 1:
            status = InfrastructureAttributionStatus.SABOTEUR_LINKED
            linked_actor_id = linked_candidates[0]
        else:
            status = InfrastructureAttributionStatus.TAMPERING_CORROBORATED
            linked_actor_id = None
    elif accidental:
        cause_structure = InfrastructureCauseStructure.ACCIDENT_ONLY
        status = InfrastructureAttributionStatus.ACCIDENTAL_CAUSE_SUPPORTED
        linked_actor_id = None
    else:
        cause_structure = InfrastructureCauseStructure.UNRESOLVED
        status = InfrastructureAttributionStatus.CAUSE_UNRESOLVED
        linked_actor_id = None

    return InfrastructureAttributionFinding(
        finding_id=finding_id,
        discoverer_id=discoverer.agent_id,
        incident_id=incident.incident_id,
        infrastructure_id=incident.infrastructure_id,
        semantic_minute=semantic_minute,
        status=status,
        evidence_claim_ids=tuple(ordered_ids),
        linked_actor_id=linked_actor_id,
        cause_structure=cause_structure,
    )
