from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.global_npc_memory import Claim, KnowledgeLedger
from tools.global_npc_memory_retrieval import (
    ClaimRecall,
    MemoryRetrievalPolicy,
    RecallState,
    age_penalty,
    source_access_penalty,
)


class MemoryCueKind(str, Enum):
    PLACE = "PLACE"
    OBJECT = "OBJECT"
    PERSON = "PERSON"
    RECORD_REFERENCE = "RECORD_REFERENCE"
    REHEARSAL = "REHEARSAL"


@dataclass(frozen=True)
class RetrievalCue:
    cue_id: str
    kind: MemoryCueKind
    claim_ids: frozenset[str]
    content_bonus: int = 0
    source_bonus: int = 0

    def __post_init__(self) -> None:
        if not self.cue_id:
            raise ValueError("cue_id is required")
        if not self.claim_ids:
            raise ValueError("claim_ids cannot be empty")
        if not 0 <= self.content_bonus <= 40:
            raise ValueError("content_bonus must be between 0 and 40")
        if not 0 <= self.source_bonus <= 40:
            raise ValueError("source_bonus must be between 0 and 40")


@dataclass(frozen=True)
class CueAssistedRecall:
    recall: ClaimRecall
    applied_cue_ids: tuple[str, ...]


def recall_claim_with_cues(
    claim: Claim,
    *,
    current_semantic_minute: int,
    cues: Iterable[RetrievalCue] = (),
    policy: MemoryRetrievalPolicy = MemoryRetrievalPolicy(),
) -> CueAssistedRecall:
    age = current_semantic_minute - claim.semantic_minute
    if age < 0:
        raise ValueError("current semantic time cannot precede the claim")

    matched = tuple(sorted((cue for cue in cues if claim.claim_id in cue.claim_ids), key=lambda cue: cue.cue_id))
    content_bonus = min(40, sum(cue.content_bonus for cue in matched))
    source_bonus = min(40, sum(cue.source_bonus for cue in matched))

    accessibility = max(0, min(100, claim.confidence - age_penalty(age) + content_bonus))
    if accessibility < policy.content_threshold:
        state = RecallState.INACCESSIBLE
        remembered_source_agent_id = None
    else:
        source_accessibility = max(
            0,
            min(100, accessibility - source_access_penalty(claim.source_kind) + source_bonus),
        )
        if source_accessibility >= policy.source_threshold:
            state = RecallState.RECALLED_WITH_SOURCE
            remembered_source_agent_id = claim.source_agent_id
        else:
            state = RecallState.CONTENT_ONLY
            remembered_source_agent_id = None

    return CueAssistedRecall(
        recall=ClaimRecall(
            claim_id=claim.claim_id,
            state=state,
            accessibility=accessibility,
            remembered_source_agent_id=remembered_source_agent_id,
            provenance_root=claim.provenance_root,
        ),
        applied_cue_ids=tuple(cue.cue_id for cue in matched),
    )


@dataclass(frozen=True)
class ArchiveRecord:
    record_id: str
    claim_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.record_id:
            raise ValueError("record_id is required")
        if not self.claim_ids:
            raise ValueError("claim_ids cannot be empty")


def lookup_archive(record: ArchiveRecord, archive_ledger: KnowledgeLedger) -> tuple[Claim, ...]:
    """Return documentary evidence without mutating any NPC personal ledger."""
    missing = [claim_id for claim_id in record.claim_ids if claim_id not in archive_ledger.claims]
    if missing:
        raise KeyError(f"archive record references missing claims: {','.join(sorted(missing))}")
    return tuple(archive_ledger.claims[claim_id] for claim_id in record.claim_ids)
