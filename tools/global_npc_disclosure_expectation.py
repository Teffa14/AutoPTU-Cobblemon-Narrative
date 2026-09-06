from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Mapping

from tools.global_npc_deception_policy import (
    CommunicationOpportunity,
    CommunicationPolicyDecision,
    CommunicationPosture,
)
from tools.global_npc_social import RelationshipState, apply_relationship_event


class DisclosureBasis(str, Enum):
    EXPLICIT_REQUEST = "EXPLICIT_REQUEST"
    ROLE_DUTY = "ROLE_DUTY"
    FACTION_OBLIGATION = "FACTION_OBLIGATION"
    PROMISE = "PROMISE"
    EMERGENCY_WARNING = "EMERGENCY_WARNING"


class DisclosureAssessmentStatus(str, Enum):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    DISCLOSED_OR_DECEIVED = "DISCLOSED_OR_DECEIVED"
    EXPECTATION_TOO_WEAK = "EXPECTATION_TOO_WEAK"
    EXPECTATION_BREACHED = "EXPECTATION_BREACHED"


_DUTY_BASES = {
    DisclosureBasis.ROLE_DUTY,
    DisclosureBasis.FACTION_OBLIGATION,
    DisclosureBasis.PROMISE,
    DisclosureBasis.EMERGENCY_WARNING,
}


@dataclass(frozen=True)
class DisclosureExpectation:
    expectation_id: str
    speaker_id: str
    recipient_id: str
    basis_claim_id: str
    basis: DisclosureBasis
    created_semantic_minute: int
    strength: int
    provenance_ref: str
    expires_semantic_minute: int | None = None

    def __post_init__(self) -> None:
        if not self.expectation_id:
            raise ValueError("expectation_id is required")
        if self.speaker_id == self.recipient_id:
            raise ValueError("disclosure expectation must target another agent")
        if not self.basis_claim_id:
            raise ValueError("basis_claim_id is required")
        if not self.provenance_ref:
            raise ValueError("disclosure expectation requires provenance")
        if self.strength < 0 or self.strength > 100:
            raise ValueError("strength must be within 0..100")
        if self.expires_semantic_minute is not None and self.expires_semantic_minute < self.created_semantic_minute:
            raise ValueError("expectation cannot expire before it is created")

    def active_at(self, semantic_minute: int) -> bool:
        if semantic_minute < self.created_semantic_minute:
            return False
        return self.expires_semantic_minute is None or semantic_minute <= self.expires_semantic_minute


@dataclass(frozen=True)
class DisclosureAssessment:
    finding_id: str
    expectation_id: str
    opportunity_id: str
    speaker_id: str
    recipient_id: str
    semantic_minute: int
    status: DisclosureAssessmentStatus
    strength: int
    provenance_refs: tuple[str, ...]


class DisclosureBreachRegistry:
    def __init__(self) -> None:
        self.applied_finding_ids: set[str] = set()

    def snapshot(self) -> dict[str, object]:
        return {
            "schema": "OUROS_DISCLOSURE_BREACH_REGISTRY_V1",
            "applied_finding_ids": sorted(self.applied_finding_ids),
        }

    @classmethod
    def restore(cls, payload: Mapping[str, object]) -> "DisclosureBreachRegistry":
        if payload.get("schema") != "OUROS_DISCLOSURE_BREACH_REGISTRY_V1":
            raise ValueError("unsupported disclosure breach registry schema")
        registry = cls()
        registry.applied_finding_ids = {
            str(value) for value in payload.get("applied_finding_ids", [])
        }
        return registry


def bind_disclosure_expectation(
    opportunity: CommunicationOpportunity,
    expectation: DisclosureExpectation,
) -> CommunicationOpportunity:
    """Derive communication-policy pressure from an explicit disclosure expectation."""
    _validate_match(opportunity, expectation)
    if not expectation.active_at(opportunity.semantic_minute):
        return opportunity

    obligation_pressure = expectation.strength if expectation.basis in _DUTY_BASES else 0
    return replace(
        opportunity,
        silence_cost=max(opportunity.silence_cost, expectation.strength),
        obligation_conflict=max(opportunity.obligation_conflict, obligation_pressure),
    )


def assess_observable_silence(
    decision: CommunicationPolicyDecision,
    opportunity: CommunicationOpportunity,
    expectation: DisclosureExpectation,
    *,
    observed_semantic_minute: int,
    breach_threshold: int = 50,
) -> DisclosureAssessment:
    """Assess an observed communication decision without inferring unseen omissions."""
    if breach_threshold < 0 or breach_threshold > 100:
        raise ValueError("breach_threshold must be within 0..100")
    _validate_match(opportunity, expectation)
    if decision.opportunity_id != opportunity.opportunity_id:
        raise ValueError("decision must refer to the supplied opportunity")
    if observed_semantic_minute < opportunity.semantic_minute:
        raise ValueError("silence cannot be observed before the communication opportunity")

    finding_id = f"disclosure:{expectation.expectation_id}:{opportunity.opportunity_id}"
    provenance_refs = (expectation.provenance_ref, f"decision:{decision.opportunity_id}")

    if not expectation.active_at(opportunity.semantic_minute):
        status = DisclosureAssessmentStatus.NOT_APPLICABLE
    elif decision.posture is not CommunicationPosture.SILENT:
        status = DisclosureAssessmentStatus.DISCLOSED_OR_DECEIVED
    elif expectation.strength < breach_threshold:
        status = DisclosureAssessmentStatus.EXPECTATION_TOO_WEAK
    else:
        status = DisclosureAssessmentStatus.EXPECTATION_BREACHED

    return DisclosureAssessment(
        finding_id=finding_id,
        expectation_id=expectation.expectation_id,
        opportunity_id=opportunity.opportunity_id,
        speaker_id=opportunity.speaker_id,
        recipient_id=opportunity.target_agent_id,
        semantic_minute=observed_semantic_minute,
        status=status,
        strength=expectation.strength,
        provenance_refs=provenance_refs,
    )


def apply_disclosure_breach_trust(
    relationship: RelationshipState,
    assessment: DisclosureAssessment,
    registry: DisclosureBreachRegistry,
    *,
    max_trust_penalty: int = 10,
) -> tuple[RelationshipState, bool]:
    """Apply one directional trust consequence for one proven expectation breach."""
    if max_trust_penalty < 1:
        raise ValueError("max_trust_penalty must be positive")
    if assessment.status is not DisclosureAssessmentStatus.EXPECTATION_BREACHED:
        return relationship, False
    if relationship.source_agent_id != assessment.recipient_id or relationship.target_agent_id != assessment.speaker_id:
        raise ValueError("trust consequence must run from recipient toward speaker")
    if assessment.finding_id in registry.applied_finding_ids:
        return relationship, False

    penalty = max(1, min(max_trust_penalty, assessment.strength // 10))
    updated = apply_relationship_event(
        relationship,
        provenance_ref=f"disclosure-breach:{assessment.finding_id}",
        semantic_minute=assessment.semantic_minute,
        trust_delta=-penalty,
    )
    registry.applied_finding_ids.add(assessment.finding_id)
    return updated, True


def _validate_match(
    opportunity: CommunicationOpportunity,
    expectation: DisclosureExpectation,
) -> None:
    if opportunity.speaker_id != expectation.speaker_id:
        raise ValueError("expectation speaker does not match communication opportunity")
    if opportunity.target_agent_id != expectation.recipient_id:
        raise ValueError("expectation recipient does not match communication opportunity")
    if opportunity.basis_claim_id != expectation.basis_claim_id:
        raise ValueError("expectation claim does not match communication opportunity")
