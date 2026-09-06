from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from tools.global_npc_evidence_custody import CustodyAssessment, EvidenceCustodyRegistry
from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind


@dataclass(frozen=True)
class AssessmentRevisionNotice:
    notice_id: str
    assessment_id: str
    investigator_id: str
    evidence_id: str
    conclusion_claim_id: str
    supersedes_assessment_id: str | None
    semantic_minute: int

    def __post_init__(self) -> None:
        if not self.notice_id or not self.assessment_id or not self.investigator_id or not self.evidence_id:
            raise ValueError("assessment revision notice identity is required")
        if not self.conclusion_claim_id:
            raise ValueError("assessment revision notice requires a conclusion claim")
        if self.semantic_minute < 0:
            raise ValueError("assessment revision notice time cannot be negative")


@dataclass
class AssessmentRevisionPropagationRegistry:
    notices: dict[str, AssessmentRevisionNotice] = field(default_factory=dict)
    assessment_to_notice_id: dict[str, str] = field(default_factory=dict)

    def register(self, notice: AssessmentRevisionNotice) -> None:
        existing = self.notices.get(notice.notice_id)
        if existing is not None:
            if existing != notice:
                raise ValueError(f"assessment notice collision: {notice.notice_id}")
            return
        existing_notice_id = self.assessment_to_notice_id.get(notice.assessment_id)
        if existing_notice_id is not None and existing_notice_id != notice.notice_id:
            raise ValueError(f"assessment already has a notice: {notice.assessment_id}")
        self.notices[notice.notice_id] = notice
        self.assessment_to_notice_id[notice.assessment_id] = notice.notice_id


def record_assessment_conclusion(
    investigator: KnowledgeLedger,
    custody: EvidenceCustodyRegistry,
    *,
    assessment_id: str,
    claim_id: str,
    confidence: int = 80,
) -> Claim:
    """Materialize one investigator-owned claim for a custody assessment.

    The claim records what this investigator concluded at that semantic time. It does not
    mutate earlier conclusions and does not communicate anything to other NPCs.
    """
    assessment = custody.assessments[assessment_id]
    if investigator.agent_id != assessment.investigator_id:
        raise ValueError("only the assessment investigator can author its conclusion claim")
    claim = Claim(
        claim_id=claim_id,
        subject=f"custody:{assessment.evidence_id}",
        value=assessment.status.value,
        source_kind=SourceKind.INFERENCE,
        source_agent_id=investigator.agent_id,
        semantic_minute=assessment.semantic_minute,
        confidence=confidence,
        provenance_root=f"custody-assessment:{assessment.assessment_id}",
        parent_claim_id=None,
        message_id=None,
    )
    investigator.add(claim)
    return claim


def register_assessment_notice(
    registry: AssessmentRevisionPropagationRegistry,
    custody: EvidenceCustodyRegistry,
    investigator: KnowledgeLedger,
    *,
    assessment_id: str,
    conclusion_claim_id: str,
    notice_id: str,
) -> AssessmentRevisionNotice:
    assessment = custody.assessments[assessment_id]
    if investigator.agent_id != assessment.investigator_id:
        raise ValueError("notice investigator must match assessment investigator")
    claim = investigator.claims[conclusion_claim_id]
    if claim.provenance_root != f"custody-assessment:{assessment.assessment_id}":
        raise ValueError("notice conclusion claim does not belong to assessment")
    if claim.semantic_minute != assessment.semantic_minute:
        raise ValueError("notice conclusion claim time must match assessment")
    notice = AssessmentRevisionNotice(
        notice_id=notice_id,
        assessment_id=assessment.assessment_id,
        investigator_id=assessment.investigator_id,
        evidence_id=assessment.evidence_id,
        conclusion_claim_id=conclusion_claim_id,
        supersedes_assessment_id=assessment.supersedes_assessment_id,
        semantic_minute=assessment.semantic_minute,
    )
    registry.register(notice)
    return notice


def schedule_assessment_notice(
    queue: InformationEventQueue,
    propagation: AssessmentRevisionPropagationRegistry,
    *,
    notice_id: str,
    receiver_ids: Iterable[str],
    channel_id: str,
    created_minute: int,
    receiver_trust_in_investigator: int = 0,
) -> tuple[InformationEnvelope, ...]:
    """Schedule explicit per-recipient delivery of one assessment conclusion.

    A superseding assessment does not automatically target everyone who heard the old one.
    Callers must supply concrete recipients. Delivery, failure, backlog and local ACK remain
    owned by the ordinary InformationEventQueue.
    """
    notice = propagation.notices[notice_id]
    if created_minute < notice.semantic_minute:
        raise ValueError("assessment notice cannot be sent before its conclusion exists")
    envelopes: list[InformationEnvelope] = []
    for receiver_id in sorted(set(receiver_ids)):
        if receiver_id == notice.investigator_id:
            continue
        envelope = queue.schedule(
            event_id=f"{notice.notice_id}:to:{receiver_id}",
            message_id=notice.notice_id,
            sender_id=notice.investigator_id,
            receiver_id=receiver_id,
            source_claim_id=notice.conclusion_claim_id,
            new_claim_id=f"{notice.conclusion_claim_id}:received:{receiver_id}",
            channel_id=channel_id,
            created_minute=created_minute,
            receiver_trust_in_sender=receiver_trust_in_investigator,
        )
        envelopes.append(envelope)
    return tuple(envelopes)
