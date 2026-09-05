from __future__ import annotations

import heapq
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_ai import (
    AgendaDecision,
    DurableGoal,
    NeedState,
    NpcAgentState,
    NpcIntent,
    PlanningContext,
    ScheduledCommitment,
    choose_agenda_intent,
    receive_information,
)


class ReplanReason(str, Enum):
    KNOWLEDGE_DELIVERED = "KNOWLEDGE_DELIVERED"
    SCHEDULE_DUE = "SCHEDULE_DUE"
    TRAVEL_INVALIDATED = "TRAVEL_INVALIDATED"
    NEED_THRESHOLD = "NEED_THRESHOLD"
    SOCIAL_CHANGE = "SOCIAL_CHANGE"
    EXTERNAL_EVENT = "EXTERNAL_EVENT"


@dataclass(frozen=True)
class ReplanTrigger:
    trigger_id: str
    agent_id: str
    reason: ReplanReason
    due_minute: int
    source_ref: str
    priority: int = 0


@dataclass(frozen=True)
class ReplanBatch:
    agent_id: str
    semantic_minute: int
    trigger_ids: tuple[str, ...]
    reasons: tuple[str, ...]
    source_refs: tuple[str, ...]
    highest_priority: int


@dataclass
class NpcReplanQueue:
    pending: list[tuple[int, int, str, ReplanTrigger]] = field(default_factory=list)
    known_trigger_ids: set[str] = field(default_factory=set)
    completed_trigger_ids: set[str] = field(default_factory=set)

    def schedule(self, trigger: ReplanTrigger) -> None:
        if trigger.trigger_id in self.known_trigger_ids:
            raise ValueError(f"trigger_id already exists: {trigger.trigger_id}")
        self.known_trigger_ids.add(trigger.trigger_id)
        heapq.heappush(
            self.pending,
            (trigger.due_minute, -trigger.priority, trigger.trigger_id, trigger),
        )

    def process_due(self, semantic_minute: int) -> list[ReplanBatch]:
        due: list[ReplanTrigger] = []
        while self.pending and self.pending[0][0] <= semantic_minute:
            _, _, _, trigger = heapq.heappop(self.pending)
            if trigger.trigger_id in self.completed_trigger_ids:
                continue
            self.completed_trigger_ids.add(trigger.trigger_id)
            due.append(trigger)

        grouped: dict[str, list[ReplanTrigger]] = {}
        for trigger in due:
            grouped.setdefault(trigger.agent_id, []).append(trigger)

        batches: list[ReplanBatch] = []
        for agent_id in sorted(grouped):
            entries = sorted(
                grouped[agent_id],
                key=lambda item: (-item.priority, item.reason.value, item.trigger_id),
            )
            batches.append(
                ReplanBatch(
                    agent_id=agent_id,
                    semantic_minute=semantic_minute,
                    trigger_ids=tuple(item.trigger_id for item in entries),
                    reasons=tuple(item.reason.value for item in entries),
                    source_refs=tuple(item.source_ref for item in entries),
                    highest_priority=max(item.priority for item in entries),
                )
            )
        return batches

    def to_snapshot(self) -> dict:
        pending = [entry[3] for entry in sorted(self.pending)]
        return {
            "schema": "OUROS_NPC_REPLAN_QUEUE_V1",
            "pending": [
                {
                    "trigger_id": item.trigger_id,
                    "agent_id": item.agent_id,
                    "reason": item.reason.value,
                    "due_minute": item.due_minute,
                    "source_ref": item.source_ref,
                    "priority": item.priority,
                }
                for item in pending
            ],
            "known_trigger_ids": sorted(self.known_trigger_ids),
            "completed_trigger_ids": sorted(self.completed_trigger_ids),
        }

    @classmethod
    def from_snapshot(cls, snapshot: Mapping[str, object]) -> "NpcReplanQueue":
        if snapshot.get("schema") != "OUROS_NPC_REPLAN_QUEUE_V1":
            raise ValueError("unsupported replan queue snapshot schema")
        queue = cls()
        queue.known_trigger_ids = set(str(v) for v in snapshot.get("known_trigger_ids", []))
        queue.completed_trigger_ids = set(str(v) for v in snapshot.get("completed_trigger_ids", []))
        for row in snapshot.get("pending", []):
            if not isinstance(row, Mapping):
                raise ValueError("pending snapshot row must be a mapping")
            trigger = ReplanTrigger(
                trigger_id=str(row["trigger_id"]),
                agent_id=str(row["agent_id"]),
                reason=ReplanReason(str(row["reason"])),
                due_minute=int(row["due_minute"]),
                source_ref=str(row["source_ref"]),
                priority=int(row.get("priority", 0)),
            )
            heapq.heappush(
                queue.pending,
                (trigger.due_minute, -trigger.priority, trigger.trigger_id, trigger),
            )
            queue.known_trigger_ids.add(trigger.trigger_id)
        return queue


def schedule_information_replan(
    queue: NpcReplanQueue,
    *,
    delivery: Mapping[str, object],
    semantic_minute: int,
    priority: int = 5,
) -> ReplanTrigger | None:
    if str(delivery.get("status")) != "DELIVERED":
        return None
    receiver_id = delivery.get("receiver_id")
    event_id = delivery.get("event_id")
    if receiver_id is None or event_id is None:
        raise ValueError("delivered information must identify receiver_id and event_id")
    trigger = ReplanTrigger(
        trigger_id=f"replan:information:{event_id}",
        agent_id=str(receiver_id),
        reason=ReplanReason.KNOWLEDGE_DELIVERED,
        due_minute=semantic_minute,
        source_ref=str(event_id),
        priority=priority,
    )
    queue.schedule(trigger)
    return trigger


def apply_information_delivery(
    agent: NpcAgentState,
    delivery: Mapping[str, object],
) -> NpcAgentState:
    if str(delivery.get("status")) != "DELIVERED":
        return agent
    if str(delivery.get("receiver_id")) != agent.agent_id:
        return agent
    claim_id = delivery.get("claim_id")
    provenance_root = delivery.get("provenance_root")
    if claim_id is None or provenance_root is None:
        raise ValueError("delivered information must include claim_id and provenance_root")
    return receive_information(
        agent,
        claim_ref=str(claim_id),
        provenance_ref=str(provenance_root),
    )


def replan_from_batch(
    agent: NpcAgentState,
    batch: ReplanBatch,
    *,
    goals: Iterable[DurableGoal] = (),
    needs: Iterable[NeedState] = (),
    commitments: Iterable[ScheduledCommitment] = (),
    situational_intents: Iterable[NpcIntent] = (),
    active_intent_id: str | None = None,
    continuity_bonus: int = 1,
) -> AgendaDecision:
    if batch.agent_id != agent.agent_id:
        raise ValueError("replan batch belongs to another agent")
    return choose_agenda_intent(
        agent,
        goals=goals,
        needs=needs,
        commitments=commitments,
        situational_intents=situational_intents,
        context=PlanningContext(
            semantic_minute=batch.semantic_minute,
            active_intent_id=active_intent_id,
            continuity_bonus=continuity_bonus,
        ),
    )


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    queue = NpcReplanQueue()
    results: list[dict] = []

    for event in data["events"]:
        kind = event["kind"]
        if kind == "schedule":
            trigger = ReplanTrigger(
                trigger_id=event["trigger_id"],
                agent_id=event["agent_id"],
                reason=ReplanReason(event["reason"]),
                due_minute=event["due_minute"],
                source_ref=event["source_ref"],
                priority=event.get("priority", 0),
            )
            queue.schedule(trigger)
            results.append({"event_id": event["event_id"], "status": "QUEUED"})
        elif kind == "advance":
            batches = queue.process_due(event["semantic_minute"])
            results.append(
                {
                    "event_id": event["event_id"],
                    "batches": [
                        {
                            "agent_id": batch.agent_id,
                            "trigger_ids": list(batch.trigger_ids),
                            "reasons": list(batch.reasons),
                            "highest_priority": batch.highest_priority,
                        }
                        for batch in batches
                    ],
                }
            )
        elif kind == "restart":
            queue = NpcReplanQueue.from_snapshot(queue.to_snapshot())
            results.append({"event_id": event["event_id"], "status": "RESTORED"})
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_replanning <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
