from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_social import RelationshipState


class CommunicationPosture(str, Enum):
    TRUTHFUL = "TRUTHFUL"
    SILENT = "SILENT"
    DECEPTIVE = "DECEPTIVE"


class DeceptionMotive(str, Enum):
    SELF_PROTECTION = "SELF_PROTECTION"
    PROTECT_OTHER = "PROTECT_OTHER"
    MATERIAL_GAIN = "MATERIAL_GAIN"
    STRATEGIC_CONCEALMENT = "STRATEGIC_CONCEALMENT"
    RIVALRY = "RIVALRY"
    RETALIATION = "RETALIATION"
    DUTY_CONFLICT = "DUTY_CONFLICT"


@dataclass(frozen=True)
class DeceptionPolicyProfile:
    agent_id: str
    deception_aversion: int = 50
    harm_aversion: int = 50
    exposure_sensitivity: int = 50
    silence_preference: int = 20

    def __post_init__(self) -> None:
        for field_name in (
            "deception_aversion",
            "harm_aversion",
            "exposure_sensitivity",
            "silence_preference",
        ):
            value = getattr(self, field_name)
            if value < 0 or value > 100:
                raise ValueError(f"{field_name} must be within 0..100")


@dataclass(frozen=True)
class CommunicationOpportunity:
    opportunity_id: str
    speaker_id: str
    target_agent_id: str
    basis_claim_id: str
    asserted_value: str
    declared_source_agent_id: str | None
    semantic_minute: int
    motive: DeceptionMotive
    goal_pressure: int = 0
    utility_gain: int = 0
    secrecy_value: int = 0
    truthful_cost: int = 0
    silence_cost: int = 0
    exposure_risk: int = 0
    third_party_harm: int = 0
    obligation_conflict: int = 0

    def __post_init__(self) -> None:
        if not self.opportunity_id:
            raise ValueError("opportunity_id is required")
        if self.speaker_id == self.target_agent_id:
            raise ValueError("communication opportunity must target another agent")
        for field_name in (
            "goal_pressure",
            "utility_gain",
            "secrecy_value",
            "truthful_cost",
            "silence_cost",
            "exposure_risk",
            "third_party_harm",
            "obligation_conflict",
        ):
            value = getattr(self, field_name)
            if value < 0 or value > 100:
                raise ValueError(f"{field_name} must be within 0..100")


@dataclass(frozen=True)
class CommunicationPolicyDecision:
    opportunity_id: str
    posture: CommunicationPosture
    truthful_score: int
    silence_score: int
    deception_score: int
    reason_codes: tuple[str, ...]


def _relationship_for(
    speaker_id: str,
    target_agent_id: str,
    relationships: Iterable[RelationshipState],
) -> RelationshipState | None:
    matches = [
        item
        for item in relationships
        if item.source_agent_id == speaker_id and item.target_agent_id == target_agent_id
    ]
    if not matches:
        return None
    matches.sort(key=lambda item: (item.last_update_semantic_minute, item.target_agent_id))
    return matches[-1]


def choose_communication_posture(
    speaker: KnowledgeLedger,
    profile: DeceptionPolicyProfile,
    opportunity: CommunicationOpportunity,
    *,
    relationships: Iterable[RelationshipState] = (),
) -> CommunicationPolicyDecision:
    if speaker.agent_id != profile.agent_id or speaker.agent_id != opportunity.speaker_id:
        raise ValueError("speaker, policy profile and opportunity must refer to the same agent")
    basis = speaker.claims[opportunity.basis_claim_id]
    if opportunity.semantic_minute < basis.semantic_minute:
        raise ValueError("communication decision cannot precede its evidence basis")

    false_content = opportunity.asserted_value != basis.value
    false_source = (
        opportunity.declared_source_agent_id is not None
        and opportunity.declared_source_agent_id != basis.source_agent_id
    )
    deceptive_option_exists = false_content or false_source

    relation = _relationship_for(
        speaker.agent_id,
        opportunity.target_agent_id,
        relationships,
    )
    trust = 0 if relation is None else relation.trust
    affinity = 0 if relation is None else relation.affinity
    rivalry = 0 if relation is None else relation.rivalry
    fear = 0 if relation is None else relation.fear

    relationship_honesty = max(0, trust) // 4 + max(0, affinity) // 8
    relationship_deception_pressure = max(0, rivalry) // 5 + max(0, fear) // 10

    truthful_score = (
        profile.deception_aversion
        + relationship_honesty
        + opportunity.obligation_conflict // 2
        - opportunity.truthful_cost
        - opportunity.secrecy_value // 2
    )
    silence_score = (
        profile.silence_preference
        + opportunity.secrecy_value
        + opportunity.exposure_risk // 3
        - opportunity.silence_cost
        - opportunity.goal_pressure // 4
    )
    deception_score = (
        opportunity.goal_pressure
        + opportunity.utility_gain
        + opportunity.secrecy_value
        + relationship_deception_pressure
        - profile.deception_aversion
        - (profile.harm_aversion * opportunity.third_party_harm // 100)
        - (profile.exposure_sensitivity * opportunity.exposure_risk // 100)
        - opportunity.obligation_conflict
        - max(0, trust) // 3
    )
    if not deceptive_option_exists:
        deception_score = -10_000

    scored = (
        (truthful_score, CommunicationPosture.TRUTHFUL),
        (silence_score, CommunicationPosture.SILENT),
        (deception_score, CommunicationPosture.DECEPTIVE),
    )
    best_score, posture = max(scored, key=lambda row: (row[0], -list(CommunicationPosture).index(row[1])))

    reasons: list[str] = []
    if posture is CommunicationPosture.DECEPTIVE:
        reasons.append(f"MOTIVE:{opportunity.motive.value}")
        if opportunity.goal_pressure >= 50:
            reasons.append("HIGH_GOAL_PRESSURE")
        if opportunity.secrecy_value >= 50:
            reasons.append("HIGH_SECRECY_VALUE")
        if opportunity.utility_gain >= 50:
            reasons.append("HIGH_UTILITY_GAIN")
        if relationship_deception_pressure > 0:
            reasons.append("ADVERSE_RELATIONSHIP_PRESSURE")
    elif posture is CommunicationPosture.SILENT:
        reasons.append("WITHHOLD_INFORMATION")
        if opportunity.secrecy_value >= 50:
            reasons.append("HIGH_SECRECY_VALUE")
        if opportunity.exposure_risk >= 50:
            reasons.append("HIGH_EXPOSURE_RISK")
    else:
        reasons.append("DISCLOSE_BASIS_VALUE")
        if relationship_honesty > 0:
            reasons.append("RELATIONSHIP_HONESTY_PRESSURE")
        if opportunity.obligation_conflict >= 50:
            reasons.append("DUTY_OPPOSES_DECEPTION")

    if best_score < -5000:
        raise ValueError("no communication posture is available")

    return CommunicationPolicyDecision(
        opportunity_id=opportunity.opportunity_id,
        posture=posture,
        truthful_score=truthful_score,
        silence_score=silence_score,
        deception_score=deception_score,
        reason_codes=tuple(reasons),
    )
