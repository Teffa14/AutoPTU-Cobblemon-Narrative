from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_communication_runtime import DispatchResult
from tools.global_npc_deception_policy import (
    CommunicationOpportunity,
    CommunicationPolicyDecision,
    CommunicationPosture,
)
from tools.global_npc_disclosure_expectation import (
    DisclosureAssessment,
    DisclosureAssessmentStatus,
    DisclosureExpectation,
    assess_observable_silence,
)
from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue


class CommunicationAccessStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    NO_KNOWN_CHANNEL = "NO_KNOWN_CHANNEL"
    CHANNEL_UNAVAILABLE = "CHANNEL_UNAVAILABLE"
    ATTEMPT_QUEUED = "ATTEMPT_QUEUED"
    WAITING_LOCAL_ACK = "WAITING_LOCAL_ACK"
    DELIVERY_FAILED = "DELIVERY_FAILED"
    DELIVERED = "DELIVERED"


class DisclosureResponsibilityStatus(str, Enum):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    DISCLOSED_OR_DECEIVED = "DISCLOSED_OR_DECEIVED"
    NO_USABLE_PATH = "NO_USABLE_PATH"
    ATTEMPT_IN_PROGRESS = "ATTEMPT_IN_PROGRESS"
    ATTEMPT_FAILED = "ATTEMPT_FAILED"
    EXPECTATION_TOO_WEAK = "EXPECTATION_TOO_WEAK"
    WILLFUL_WITHHOLDING = "WILLFUL_WITHHOLDING"


@dataclass(frozen=True)
class CommunicationAccessEvidence:
    evidence_id: str
    expectation_id: str
    opportunity_id: str
    speaker_id: str
    recipient_id: str
    semantic_minute: int
    status: CommunicationAccessStatus
    provenance_refs: tuple[str, ...]
    delivery_event_id: str | None = None

    def __post_init__(self) -> None:
        if not self.evidence_id:
            raise ValueError("evidence_id is required")
        if not self.provenance_refs:
            raise ValueError("communication access evidence requires provenance")


@dataclass(frozen=True)
class DisclosureResponsibilityAssessment:
    finding_id: str
    expectation_id: str
    opportunity_id: str
    speaker_id: str
    recipient_id: str
    semantic_minute: int
    status: DisclosureResponsibilityStatus
    provenance_refs: tuple[str, ...]
    breach_assessment: DisclosureAssessment | None = None


def available_access_evidence(
    opportunity: CommunicationOpportunity,
    expectation: DisclosureExpectation,
    *,
    semantic_minute: int,
    provenance_ref: str,
) -> CommunicationAccessEvidence:
    """Record a proven usable communication opportunity such as direct contact."""
    _validate_identity(opportunity, expectation)
    if semantic_minute < opportunity.semantic_minute:
        raise ValueError("access evidence cannot precede the communication opportunity")
    return CommunicationAccessEvidence(
        evidence_id=f"access:{expectation.expectation_id}:{opportunity.opportunity_id}:available",
        expectation_id=expectation.expectation_id,
        opportunity_id=opportunity.opportunity_id,
        speaker_id=opportunity.speaker_id,
        recipient_id=opportunity.target_agent_id,
        semantic_minute=semantic_minute,
        status=CommunicationAccessStatus.AVAILABLE,
        provenance_refs=(provenance_ref,),
    )


def capture_dispatch_access(
    dispatch: DispatchResult,
    *,
    expectation: DisclosureExpectation,
    opportunity: CommunicationOpportunity,
    receiver_id: str,
    queue: InformationEventQueue,
    semantic_minute: int,
) -> CommunicationAccessEvidence:
    """Project existing dispatch/queue state into evidence about communication access."""
    _validate_identity(opportunity, expectation)
    if receiver_id != expectation.recipient_id:
        raise ValueError("receiver does not match disclosure expectation")
    if semantic_minute < opportunity.semantic_minute:
        raise ValueError("access evidence cannot precede the communication opportunity")

    scheduled = [row for row in dispatch.scheduled if row["receiver_id"] == receiver_id]
    unscheduled = [row for row in dispatch.unscheduled if row[0] == receiver_id]
    if scheduled and unscheduled:
        raise ValueError("receiver cannot be both scheduled and unscheduled in one dispatch")

    if unscheduled:
        reason = unscheduled[0][1]
        if reason != "NO_KNOWN_CHANNEL":
            raise ValueError(f"unsupported unscheduled reason: {reason}")
        return CommunicationAccessEvidence(
            evidence_id=f"access:{expectation.expectation_id}:{opportunity.opportunity_id}:no-channel",
            expectation_id=expectation.expectation_id,
            opportunity_id=opportunity.opportunity_id,
            speaker_id=opportunity.speaker_id,
            recipient_id=receiver_id,
            semantic_minute=semantic_minute,
            status=CommunicationAccessStatus.NO_KNOWN_CHANNEL,
            provenance_refs=(f"dispatch:{opportunity.opportunity_id}:NO_KNOWN_CHANNEL",),
        )

    if not scheduled:
        raise ValueError("dispatch contains no evidence for the expected receiver")

    row = scheduled[0]
    event_id = str(row["event_id"])
    delivery_status = queue.statuses.get(event_id)
    if delivery_status is None:
        raise ValueError("scheduled delivery has no queue status")
    mapped = {
        DeliveryStatus.QUEUED: CommunicationAccessStatus.ATTEMPT_QUEUED,
        DeliveryStatus.WAITING_LOCAL_ACK: CommunicationAccessStatus.WAITING_LOCAL_ACK,
        DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE: CommunicationAccessStatus.DELIVERY_FAILED,
        DeliveryStatus.DELIVERED: CommunicationAccessStatus.DELIVERED,
    }[delivery_status]
    return CommunicationAccessEvidence(
        evidence_id=f"access:{expectation.expectation_id}:{opportunity.opportunity_id}:{event_id}",
        expectation_id=expectation.expectation_id,
        opportunity_id=opportunity.opportunity_id,
        speaker_id=opportunity.speaker_id,
        recipient_id=receiver_id,
        semantic_minute=semantic_minute,
        status=mapped,
        provenance_refs=(f"delivery:{event_id}:{delivery_status.value}",),
        delivery_event_id=event_id,
    )


def assess_disclosure_responsibility(
    decision: CommunicationPolicyDecision,
    opportunity: CommunicationOpportunity,
    expectation: DisclosureExpectation,
    access: CommunicationAccessEvidence,
    *,
    observed_semantic_minute: int,
    breach_threshold: int = 50,
) -> DisclosureResponsibilityAssessment:
    """Assign a silence breach only when a usable opportunity is evidenced."""
    _validate_identity(opportunity, expectation)
    if decision.opportunity_id != opportunity.opportunity_id:
        raise ValueError("decision must refer to the supplied opportunity")
    if access.expectation_id != expectation.expectation_id or access.opportunity_id != opportunity.opportunity_id:
        raise ValueError("access evidence does not match expectation/opportunity")
    if access.speaker_id != opportunity.speaker_id or access.recipient_id != opportunity.target_agent_id:
        raise ValueError("access evidence identity does not match opportunity")
    if observed_semantic_minute < access.semantic_minute:
        raise ValueError("responsibility cannot be assessed before access evidence exists")

    finding_id = f"disclosure-responsibility:{expectation.expectation_id}:{opportunity.opportunity_id}"
    provenance = (expectation.provenance_ref,) + access.provenance_refs + (f"decision:{decision.opportunity_id}",)

    if not expectation.active_at(opportunity.semantic_minute):
        status = DisclosureResponsibilityStatus.NOT_APPLICABLE
        breach = None
    elif access.status is CommunicationAccessStatus.NO_KNOWN_CHANNEL:
        status = DisclosureResponsibilityStatus.NO_USABLE_PATH
        breach = None
    elif access.status in (CommunicationAccessStatus.ATTEMPT_QUEUED, CommunicationAccessStatus.WAITING_LOCAL_ACK):
        status = DisclosureResponsibilityStatus.ATTEMPT_IN_PROGRESS
        breach = None
    elif access.status in (CommunicationAccessStatus.CHANNEL_UNAVAILABLE, CommunicationAccessStatus.DELIVERY_FAILED):
        status = DisclosureResponsibilityStatus.ATTEMPT_FAILED
        breach = None
    elif decision.posture is not CommunicationPosture.SILENT:
        status = DisclosureResponsibilityStatus.DISCLOSED_OR_DECEIVED
        breach = None
    elif access.status is CommunicationAccessStatus.DELIVERED:
        raise ValueError("a silent decision cannot have a delivered communication for the same opportunity")
    else:
        breach = assess_observable_silence(
            decision,
            opportunity,
            expectation,
            observed_semantic_minute=observed_semantic_minute,
            breach_threshold=breach_threshold,
        )
        if breach.status is DisclosureAssessmentStatus.EXPECTATION_TOO_WEAK:
            status = DisclosureResponsibilityStatus.EXPECTATION_TOO_WEAK
        elif breach.status is DisclosureAssessmentStatus.EXPECTATION_BREACHED:
            status = DisclosureResponsibilityStatus.WILLFUL_WITHHOLDING
        elif breach.status is DisclosureAssessmentStatus.NOT_APPLICABLE:
            status = DisclosureResponsibilityStatus.NOT_APPLICABLE
        else:
            raise ValueError("unexpected silence assessment state")

    return DisclosureResponsibilityAssessment(
        finding_id=finding_id,
        expectation_id=expectation.expectation_id,
        opportunity_id=opportunity.opportunity_id,
        speaker_id=opportunity.speaker_id,
        recipient_id=opportunity.target_agent_id,
        semantic_minute=observed_semantic_minute,
        status=status,
        provenance_refs=provenance,
        breach_assessment=breach,
    )


def _validate_identity(opportunity: CommunicationOpportunity, expectation: DisclosureExpectation) -> None:
    if opportunity.speaker_id != expectation.speaker_id:
        raise ValueError("expectation speaker does not match communication opportunity")
    if opportunity.target_agent_id != expectation.recipient_id:
        raise ValueError("expectation recipient does not match communication opportunity")
    if opportunity.basis_claim_id != expectation.basis_claim_id:
        raise ValueError("expectation claim does not match communication opportunity")
