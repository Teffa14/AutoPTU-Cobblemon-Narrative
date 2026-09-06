import pytest

from tools.global_npc_disclosure_opportunity import (
    CommunicationAccessEvidence,
    CommunicationAccessStatus,
)
from tools.global_npc_infrastructure_failure_attribution import (
    InfrastructureAttributionRegistry,
    InfrastructureAttributionStatus,
    InfrastructureCausalEvidence,
    InfrastructureEvidenceKind,
    InfrastructureFailureIncident,
    assess_infrastructure_failure,
    incident_from_communication_failure,
)
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind


def claim(
    ledger: KnowledgeLedger,
    claim_id: str,
    *,
    root: str,
    minute: int,
    confidence: int = 90,
    source_agent_id: str | None = None,
) -> Claim:
    row = Claim(
        claim_id=claim_id,
        subject="relay:r17:failure-cause",
        value=claim_id,
        source_kind=SourceKind.DIRECT_OBSERVATION if source_agent_id == ledger.agent_id else SourceKind.REPORT,
        source_agent_id=source_agent_id,
        semantic_minute=minute,
        confidence=confidence,
        provenance_root=root,
    )
    ledger.add(row)
    return row


def incident() -> InfrastructureFailureIncident:
    return InfrastructureFailureIncident(
        incident_id="relay-r17-outage",
        infrastructure_id="relay-r17",
        observed_semantic_minute=100,
        failure_ref="access:warning:relay-r17",
        provenance_refs=("delivery:warning-17:FAILED_CHANNEL_UNAVAILABLE",),
    )


def evidence(claim_id: str, kind: InfrastructureEvidenceKind, actor: str | None = None) -> InfrastructureCausalEvidence:
    return InfrastructureCausalEvidence(
        claim_id=claim_id,
        kind=kind,
        incident_id="relay-r17-outage",
        linked_actor_id=actor,
    )


def test_communication_failure_can_become_investigable_incident_without_assigning_cause() -> None:
    access = CommunicationAccessEvidence(
        evidence_id="access:exp-1:opp-1:event-1",
        expectation_id="exp-1",
        opportunity_id="opp-1",
        speaker_id="dispatcher",
        recipient_id="traveler",
        semantic_minute=100,
        status=CommunicationAccessStatus.DELIVERY_FAILED,
        provenance_refs=("delivery:event-1:FAILED_CHANNEL_UNAVAILABLE",),
        delivery_event_id="event-1",
    )
    result = incident_from_communication_failure(
        access,
        incident_id="relay-r17-outage",
        infrastructure_id="relay-r17",
        semantic_minute=101,
    )
    assert result.failure_ref == access.evidence_id
    assert result.provenance_refs == access.provenance_refs


def test_failure_alone_remains_causally_unresolved() -> None:
    ledger = KnowledgeLedger("investigator")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-unresolved",
        evidence=(),
        semantic_minute=110,
    )
    assert result.status is InfrastructureAttributionStatus.CAUSE_UNRESOLVED
    assert result.linked_actor_id is None


def test_material_failure_evidence_can_support_accidental_cause() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "fatigue-analysis", root="lab:fatigue", minute=120, source_agent_id="engineer")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-fatigue",
        evidence=(evidence("fatigue-analysis", InfrastructureEvidenceKind.ACCIDENTAL_CAUSE),),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.ACCIDENTAL_CAUSE_SUPPORTED


def test_tampering_does_not_identify_an_actor_by_itself() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "cut-fastener", root="scene:cut-fastener", minute=120, source_agent_id="investigator")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-tamper",
        evidence=(evidence("cut-fastener", InfrastructureEvidenceKind.TAMPERING_TRACE),),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.TAMPERING_CORROBORATED
    assert result.linked_actor_id is None


def test_actor_access_without_tampering_cannot_create_sabotage() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "gate-log", root="record:gate-log", minute=121, source_agent_id="relay-office")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-access-only",
        evidence=(evidence("gate-log", InfrastructureEvidenceKind.ACTOR_LINK, "rival-tech"),),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.CAUSE_UNRESOLVED
    assert result.linked_actor_id is None


def test_independent_tampering_and_actor_link_can_link_a_suspect_without_proving_intent() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "cut-fastener", root="scene:cut-fastener", minute=120, source_agent_id="investigator")
    claim(ledger, "gate-log", root="record:gate-log", minute=121, source_agent_id="relay-office")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-linked",
        evidence=(
            evidence("cut-fastener", InfrastructureEvidenceKind.TAMPERING_TRACE),
            evidence("gate-log", InfrastructureEvidenceKind.ACTOR_LINK, "rival-tech"),
        ),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.SABOTEUR_LINKED
    assert result.linked_actor_id == "rival-tech"


def test_intent_requires_tampering_actor_link_and_actor_attributable_evidence() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "cut-fastener", root="scene:cut-fastener", minute=120, source_agent_id="investigator")
    claim(ledger, "gate-log", root="record:gate-log", minute=121, source_agent_id="relay-office")
    claim(ledger, "admission", root="statement:rival-tech", minute=122, source_agent_id="rival-tech")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-intent",
        evidence=(
            evidence("cut-fastener", InfrastructureEvidenceKind.TAMPERING_TRACE),
            evidence("gate-log", InfrastructureEvidenceKind.ACTOR_LINK, "rival-tech"),
            evidence("admission", InfrastructureEvidenceKind.INTENT_EVIDENCE, "rival-tech"),
        ),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.SABOTAGE_INTENT_ATTRIBUTED
    assert result.linked_actor_id == "rival-tech"


def test_one_provenance_root_cannot_bootstrap_actor_link_and_intent() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "cut-fastener", root="scene:cut-fastener", minute=120, source_agent_id="investigator")
    claim(ledger, "rumor-access", root="rumor:one", minute=121, source_agent_id="witness")
    claim(ledger, "rumor-intent", root="rumor:one", minute=122, source_agent_id="rival-tech")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-one-root",
        evidence=(
            evidence("cut-fastener", InfrastructureEvidenceKind.TAMPERING_TRACE),
            evidence("rumor-access", InfrastructureEvidenceKind.ACTOR_LINK, "rival-tech"),
            evidence("rumor-intent", InfrastructureEvidenceKind.INTENT_EVIDENCE, "rival-tech"),
        ),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.SABOTEUR_LINKED


def test_conflicting_independent_accident_and_tampering_evidence_remains_contested() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "fatigue-analysis", root="lab:fatigue", minute=120, source_agent_id="engineer")
    claim(ledger, "cut-fastener", root="scene:cut-fastener", minute=121, source_agent_id="investigator")
    result = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-contested",
        evidence=(
            evidence("fatigue-analysis", InfrastructureEvidenceKind.ACCIDENTAL_CAUSE),
            evidence("cut-fastener", InfrastructureEvidenceKind.TAMPERING_TRACE),
        ),
        semantic_minute=130,
    )
    assert result.status is InfrastructureAttributionStatus.CAUSE_CONTESTED


def test_low_confidence_or_future_evidence_fails_closed() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "weak-trace", root="scene:weak", minute=120, confidence=40, source_agent_id="investigator")
    with pytest.raises(ValueError, match="below threshold"):
        assess_infrastructure_failure(
            ledger,
            incident(),
            finding_id="finding-weak",
            evidence=(evidence("weak-trace", InfrastructureEvidenceKind.TAMPERING_TRACE),),
            semantic_minute=130,
        )

    future = KnowledgeLedger("investigator")
    claim(future, "future-trace", root="scene:future", minute=140, source_agent_id="investigator")
    with pytest.raises(ValueError, match="future"):
        assess_infrastructure_failure(
            future,
            incident(),
            finding_id="finding-future",
            evidence=(evidence("future-trace", InfrastructureEvidenceKind.TAMPERING_TRACE),),
            semantic_minute=130,
        )


def test_registry_round_trip_preserves_finding() -> None:
    ledger = KnowledgeLedger("investigator")
    claim(ledger, "cut-fastener", root="scene:cut-fastener", minute=120, source_agent_id="investigator")
    finding = assess_infrastructure_failure(
        ledger,
        incident(),
        finding_id="finding-persisted",
        evidence=(evidence("cut-fastener", InfrastructureEvidenceKind.TAMPERING_TRACE),),
        semantic_minute=130,
    )
    registry = InfrastructureAttributionRegistry()
    registry.add(finding)
    restored = InfrastructureAttributionRegistry.restore(registry.snapshot())
    assert restored.findings == registry.findings


def test_nonfailure_access_cannot_be_promoted_to_infrastructure_incident() -> None:
    access = CommunicationAccessEvidence(
        evidence_id="access:available",
        expectation_id="exp-1",
        opportunity_id="opp-1",
        speaker_id="dispatcher",
        recipient_id="traveler",
        semantic_minute=100,
        status=CommunicationAccessStatus.AVAILABLE,
        provenance_refs=("direct-contact:opp-1",),
    )
    with pytest.raises(ValueError, match="failed/unavailable"):
        incident_from_communication_failure(
            access,
            incident_id="relay-r17-outage",
            infrastructure_id="relay-r17",
            semantic_minute=101,
        )
