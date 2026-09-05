from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.global_npc_memory import BeliefAssessment, Claim, KnowledgeLedger, SourceKind, evaluate_belief


class RecallState(str, Enum):
    RECALLED_WITH_SOURCE = "RECALLED_WITH_SOURCE"
    CONTENT_ONLY = "CONTENT_ONLY"
    INACCESSIBLE = "INACCESSIBLE"


@dataclass(frozen=True)
class MemoryRetrievalPolicy:
    content_threshold: int = 40
    source_threshold: int = 60

    def __post_init__(self) -> None:
        if not 0 <= self.content_threshold <= 100:
            raise ValueError("content_threshold must be between 0 and 100")
        if not 0 <= self.source_threshold <= 100:
            raise ValueError("source_threshold must be between 0 and 100")
        if self.source_threshold < self.content_threshold:
            raise ValueError("source_threshold cannot be lower than content_threshold")


@dataclass(frozen=True)
class ClaimRecall:
    claim_id: str
    state: RecallState
    accessibility: int
    remembered_source_agent_id: str | None
    provenance_root: str


def age_penalty(age_minutes: int) -> int:
    if age_minutes < 0:
        raise ValueError("current semantic time cannot precede the claim")
    if age_minutes <= 60:
        return 0
    if age_minutes <= 24 * 60:
        return 10
    if age_minutes <= 7 * 24 * 60:
        return 20
    if age_minutes <= 30 * 24 * 60:
        return 30
    return 40


def source_access_penalty(kind: SourceKind) -> int:
    if kind is SourceKind.REPORT:
        return 10
    if kind is SourceKind.INFERENCE:
        return 5
    return 0


def recall_claim(
    claim: Claim,
    *,
    current_semantic_minute: int,
    policy: MemoryRetrievalPolicy = MemoryRetrievalPolicy(),
) -> ClaimRecall:
    age = current_semantic_minute - claim.semantic_minute
    accessibility = max(0, claim.confidence - age_penalty(age))

    if accessibility < policy.content_threshold:
        state = RecallState.INACCESSIBLE
        remembered_source_agent_id = None
    else:
        source_accessibility = max(0, accessibility - source_access_penalty(claim.source_kind))
        if source_accessibility >= policy.source_threshold:
            state = RecallState.RECALLED_WITH_SOURCE
            remembered_source_agent_id = claim.source_agent_id
        else:
            state = RecallState.CONTENT_ONLY
            remembered_source_agent_id = None

    return ClaimRecall(
        claim_id=claim.claim_id,
        state=state,
        accessibility=accessibility,
        remembered_source_agent_id=remembered_source_agent_id,
        provenance_root=claim.provenance_root,
    )


def recall_subject(
    ledger: KnowledgeLedger,
    subject: str,
    *,
    current_semantic_minute: int,
    policy: MemoryRetrievalPolicy = MemoryRetrievalPolicy(),
) -> tuple[ClaimRecall, ...]:
    return tuple(
        recall_claim(claim, current_semantic_minute=current_semantic_minute, policy=policy)
        for claim in ledger.claims_for(subject)
    )


def accessible_claim_ids(
    ledger: KnowledgeLedger,
    subject: str,
    *,
    current_semantic_minute: int,
    policy: MemoryRetrievalPolicy = MemoryRetrievalPolicy(),
) -> frozenset[str]:
    return frozenset(
        recall.claim_id
        for recall in recall_subject(
            ledger,
            subject,
            current_semantic_minute=current_semantic_minute,
            policy=policy,
        )
        if recall.state is not RecallState.INACCESSIBLE
    )


def evaluate_recalled_belief(
    ledger: KnowledgeLedger,
    subject: str,
    *,
    current_semantic_minute: int,
    policy: MemoryRetrievalPolicy = MemoryRetrievalPolicy(),
    support_threshold: int = 60,
    contest_margin: int = 15,
) -> BeliefAssessment:
    active_ids = accessible_claim_ids(
        ledger,
        subject,
        current_semantic_minute=current_semantic_minute,
        policy=policy,
    )
    recalled = KnowledgeLedger(agent_id=ledger.agent_id)
    for claim_id in sorted(active_ids):
        recalled.add(ledger.claims[claim_id])
    return evaluate_belief(
        recalled,
        subject,
        support_threshold=support_threshold,
        contest_margin=contest_margin,
    )


def source_attributions(
    ledger: KnowledgeLedger,
    claim_ids: Iterable[str],
    *,
    current_semantic_minute: int,
    policy: MemoryRetrievalPolicy = MemoryRetrievalPolicy(),
) -> dict[str, str | None]:
    out: dict[str, str | None] = {}
    for claim_id in sorted(set(claim_ids)):
        recall = recall_claim(
            ledger.claims[claim_id],
            current_semantic_minute=current_semantic_minute,
            policy=policy,
        )
        out[claim_id] = recall.remembered_source_agent_id
    return out
