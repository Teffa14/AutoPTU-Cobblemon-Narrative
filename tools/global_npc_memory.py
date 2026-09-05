from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping


LEDGER_SNAPSHOT_SCHEMA = "OUROS_NPC_KNOWLEDGE_LEDGER_V1"
LEDGER_STORE_SNAPSHOT_SCHEMA = "OUROS_NPC_KNOWLEDGE_LEDGER_STORE_V1"


class SourceKind(str, Enum):
    DIRECT_OBSERVATION = "DIRECT_OBSERVATION"
    REPORT = "REPORT"
    INSTITUTIONAL_RECORD = "INSTITUTIONAL_RECORD"
    AUTHORED_START = "AUTHORED_START"
    INFERENCE = "INFERENCE"


class BeliefStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    SUPPORTED = "SUPPORTED"
    CONTESTED = "CONTESTED"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class Claim:
    claim_id: str
    subject: str
    value: str
    source_kind: SourceKind
    source_agent_id: str | None
    semantic_minute: int
    confidence: int
    provenance_root: str
    parent_claim_id: str | None = None
    message_id: str | None = None

    def __post_init__(self) -> None:
        if not self.claim_id:
            raise ValueError("claim_id is required")
        if not self.subject:
            raise ValueError("subject is required")
        if not self.provenance_root:
            raise ValueError("provenance_root is required")
        if not 0 <= self.confidence <= 100:
            raise ValueError("confidence must be between 0 and 100")

    def to_snapshot(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "subject": self.subject,
            "value": self.value,
            "source_kind": self.source_kind.value,
            "source_agent_id": self.source_agent_id,
            "semantic_minute": self.semantic_minute,
            "confidence": self.confidence,
            "provenance_root": self.provenance_root,
            "parent_claim_id": self.parent_claim_id,
            "message_id": self.message_id,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "Claim":
        return cls(
            claim_id=str(raw["claim_id"]),
            subject=str(raw["subject"]),
            value=str(raw["value"]),
            source_kind=SourceKind(str(raw["source_kind"])),
            source_agent_id=None if raw.get("source_agent_id") is None else str(raw["source_agent_id"]),
            semantic_minute=int(raw["semantic_minute"]),
            confidence=int(raw["confidence"]),
            provenance_root=str(raw["provenance_root"]),
            parent_claim_id=None if raw.get("parent_claim_id") is None else str(raw["parent_claim_id"]),
            message_id=None if raw.get("message_id") is None else str(raw["message_id"]),
        )


@dataclass
class KnowledgeLedger:
    agent_id: str
    claims: dict[str, Claim] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.agent_id:
            raise ValueError("agent_id is required")

    def add(self, claim: Claim) -> None:
        existing = self.claims.get(claim.claim_id)
        if existing is not None and existing != claim:
            raise ValueError(f"claim_id collision: {claim.claim_id}")
        self.claims[claim.claim_id] = claim

    def claims_for(self, subject: str) -> list[Claim]:
        return sorted(
            (claim for claim in self.claims.values() if claim.subject == subject),
            key=lambda claim: (claim.semantic_minute, claim.claim_id),
        )

    def snapshot(self) -> dict:
        return {
            "schema": LEDGER_SNAPSHOT_SCHEMA,
            "agent_id": self.agent_id,
            "claims": [
                self.claims[claim_id].to_snapshot()
                for claim_id in sorted(self.claims)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "KnowledgeLedger":
        if snapshot.get("schema") != LEDGER_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported knowledge ledger snapshot schema")
        agent_id = str(snapshot["agent_id"])
        ledger = cls(agent_id)
        rows = snapshot.get("claims", [])
        if not isinstance(rows, list):
            raise ValueError("knowledge ledger claims must be a list")
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("knowledge ledger claim row must be a mapping")
            ledger.add(Claim.from_snapshot(raw))
        return ledger


@dataclass
class KnowledgeLedgerStore:
    ledgers: dict[str, KnowledgeLedger] = field(default_factory=dict)

    def add(self, ledger: KnowledgeLedger) -> None:
        existing = self.ledgers.get(ledger.agent_id)
        if existing is not None and existing != ledger:
            raise ValueError(f"agent ledger collision: {ledger.agent_id}")
        self.ledgers[ledger.agent_id] = ledger

    def require(self, agent_id: str) -> KnowledgeLedger:
        return self.ledgers[agent_id]

    def snapshot(self) -> dict:
        return {
            "schema": LEDGER_STORE_SNAPSHOT_SCHEMA,
            "ledgers": [
                self.ledgers[agent_id].snapshot()
                for agent_id in sorted(self.ledgers)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "KnowledgeLedgerStore":
        if snapshot.get("schema") != LEDGER_STORE_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported knowledge ledger store snapshot schema")
        rows = snapshot.get("ledgers", [])
        if not isinstance(rows, list):
            raise ValueError("knowledge ledger store ledgers must be a list")
        store = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("knowledge ledger snapshot must be a mapping")
            store.add(KnowledgeLedger.restore(raw))
        return store


@dataclass(frozen=True)
class BeliefAssessment:
    subject: str
    status: BeliefStatus
    preferred_value: str | None
    support_by_value: dict[str, int]
    independent_roots_by_value: dict[str, tuple[str, ...]]


def clamp(value: int, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, value))


def record_direct_observation(
    ledger: KnowledgeLedger,
    *,
    claim_id: str,
    subject: str,
    value: str,
    semantic_minute: int,
    confidence: int,
) -> Claim:
    claim = Claim(
        claim_id=claim_id,
        subject=subject,
        value=value,
        source_kind=SourceKind.DIRECT_OBSERVATION,
        source_agent_id=ledger.agent_id,
        semantic_minute=semantic_minute,
        confidence=confidence,
        provenance_root=claim_id,
    )
    ledger.add(claim)
    return claim


def transmit_claim(
    sender: KnowledgeLedger,
    receiver: KnowledgeLedger,
    *,
    source_claim_id: str,
    new_claim_id: str,
    message_id: str,
    semantic_minute: int,
    receiver_trust_in_sender: int = 0,
) -> Claim:
    source = sender.claims[source_claim_id]
    trust = clamp(receiver_trust_in_sender, -100, 100)
    reported_confidence = min(source.confidence, clamp(source.confidence - 20 + trust // 4))
    claim = Claim(
        claim_id=new_claim_id,
        subject=source.subject,
        value=source.value,
        source_kind=SourceKind.REPORT,
        source_agent_id=sender.agent_id,
        semantic_minute=semantic_minute,
        confidence=reported_confidence,
        provenance_root=source.provenance_root,
        parent_claim_id=source.claim_id,
        message_id=message_id,
    )
    receiver.add(claim)
    return claim


def evaluate_belief(
    ledger: KnowledgeLedger,
    subject: str,
    *,
    support_threshold: int = 60,
    contest_margin: int = 15,
) -> BeliefAssessment:
    claims = ledger.claims_for(subject)
    if not claims:
        return BeliefAssessment(subject, BeliefStatus.UNKNOWN, None, {}, {})

    by_value_root: dict[str, dict[str, int]] = {}
    for claim in claims:
        roots = by_value_root.setdefault(claim.value, {})
        roots[claim.provenance_root] = max(roots.get(claim.provenance_root, 0), claim.confidence)

    support = {
        value: min(100, sum(root_scores.values()))
        for value, root_scores in by_value_root.items()
    }
    roots_out = {
        value: tuple(sorted(root_scores))
        for value, root_scores in by_value_root.items()
    }
    ranking = sorted(support.items(), key=lambda item: (-item[1], item[0]))
    top_value, top_score = ranking[0]
    second_score = ranking[1][1] if len(ranking) > 1 else 0

    if top_score < support_threshold:
        return BeliefAssessment(subject, BeliefStatus.INCONCLUSIVE, None, support, roots_out)
    if len(ranking) > 1 and top_score - second_score < contest_margin:
        return BeliefAssessment(subject, BeliefStatus.CONTESTED, None, support, roots_out)
    return BeliefAssessment(subject, BeliefStatus.SUPPORTED, top_value, support, roots_out)


def supported_fact_keys(ledger: KnowledgeLedger, subjects: Iterable[str]) -> frozenset[str]:
    keys: set[str] = set()
    for subject in subjects:
        assessment = evaluate_belief(ledger, subject)
        if assessment.status is BeliefStatus.SUPPORTED and assessment.preferred_value is not None:
            keys.add(f"{subject}={assessment.preferred_value}")
    return frozenset(keys)


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    store = KnowledgeLedgerStore({
        entry["agent_id"]: KnowledgeLedger(entry["agent_id"])
        for entry in data["agents"]
    })
    ledgers = store.ledgers
    results: list[dict] = []

    for event in data["events"]:
        kind = event["kind"]
        if kind == "observe":
            claim = record_direct_observation(
                ledgers[event["agent_id"]],
                claim_id=event["claim_id"],
                subject=event["subject"],
                value=event["value"],
                semantic_minute=event["semantic_minute"],
                confidence=event["confidence"],
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "tell":
            claim = transmit_claim(
                ledgers[event["sender_id"]],
                ledgers[event["receiver_id"]],
                source_claim_id=event["source_claim_id"],
                new_claim_id=event["claim_id"],
                message_id=event["message_id"],
                semantic_minute=event["semantic_minute"],
                receiver_trust_in_sender=event.get("receiver_trust_in_sender", 0),
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "restart":
            store = KnowledgeLedgerStore.restore(store.snapshot())
            ledgers = store.ledgers
            results.append({
                "event_id": event["event_id"],
                "status": "RESTORED",
                "agent_ids": sorted(ledgers),
                "claim_count": sum(len(ledger.claims) for ledger in ledgers.values()),
            })
        elif kind == "assess":
            assessment = evaluate_belief(ledgers[event["agent_id"]], event["subject"])
            results.append({
                "event_id": event["event_id"],
                "status": assessment.status.value,
                "preferred_value": assessment.preferred_value,
                "support_by_value": assessment.support_by_value,
                "independent_roots_by_value": {key: list(value) for key, value in assessment.independent_roots_by_value.items()},
            })
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_memory <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
