from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, evaluate_belief, record_direct_observation
from tools.global_npc_publication import PublicAudienceMember, ExpansionResult, expand_publication_bounded, member_from_dict
from tools.global_npc_publication_revision import (
    PublicationRevision,
    PublicationRevisionRegistry,
    ReceivedLineageState,
    revision_from_dict,
)
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


SNAPSHOT_SCHEMA = "OUROS_NPC_PUBLICATION_REVISION_RUNTIME_V1"


@dataclass(frozen=True)
class RevisionExpansion:
    publication_id: str
    scheduled_agent_ids: tuple[str, ...]
    next_cursor: str | None
    eligible_remaining: int


@dataclass(frozen=True)
class RevisionDeliveryCycle:
    semantic_minute: int
    delivered_revision_receipts: tuple[tuple[str, str], ...]
    wake_statuses: tuple[str, ...]
    decision_agent_ids: tuple[str, ...]
    delivery_processed_count: int
    delivery_deferred_due_count: int


class PublicationRevisionRuntime:
    """Compose revision lineage, public receipt expansion and selective replanning.

    Each revision is an independent publication event. Audience eligibility is
    evaluated at that revision's expansion time. Historical receipts are never
    rewritten when a later correction, update or retraction is registered.
    """

    def __init__(
        self,
        *,
        registry: PublicationRevisionRegistry,
        coordinator: GlobalNpcWorldEventCoordinator,
    ) -> None:
        self.registry = registry
        self.coordinator = coordinator
        self.cursor_by_publication_id: dict[str, str | None] = {}
        self.publication_by_delivery_event_id: dict[str, str] = {}
        self.received_publication_ids_by_agent: dict[str, set[str]] = {
            agent_id: set() for agent_id in coordinator.information_queue.ledgers
        }

    def register_and_expand(
        self,
        *,
        revision: PublicationRevision,
        members: Iterable[PublicAudienceMember],
        semantic_minute: int,
        max_receivers: int,
        receiver_trust_in_publisher: Mapping[str, int] | None = None,
    ) -> RevisionExpansion:
        publication = revision.publication
        if semantic_minute < publication.published_minute:
            raise ValueError("revision cannot expand before published_minute")
        self.registry.register(revision)
        cursor = self.cursor_by_publication_id.get(publication.publication_id)
        result: ExpansionResult = expand_publication_bounded(
            publication=publication,
            members=members,
            semantic_minute=semantic_minute,
            max_receivers=max_receivers,
            queue=self.coordinator.information_queue,
            cursor_after_agent_id=cursor,
            receiver_trust_in_publisher=receiver_trust_in_publisher,
        )
        self.cursor_by_publication_id[publication.publication_id] = result.next_cursor
        for agent_id in result.scheduled_agent_ids:
            event_id = f"{publication.publication_id}:receipt:{agent_id}"
            self.publication_by_delivery_event_id[event_id] = publication.publication_id
        return RevisionExpansion(
            publication_id=publication.publication_id,
            scheduled_agent_ids=result.scheduled_agent_ids,
            next_cursor=result.next_cursor,
            eligible_remaining=result.eligible_remaining,
        )

    def process_cycle(
        self,
        semantic_minute: int,
        *,
        delivery_budget: int,
        replan_priority: int = 5,
    ) -> RevisionDeliveryCycle:
        cycle = self.coordinator.process_cycle(
            semantic_minute,
            delivery_budget=delivery_budget,
            replan_priority=replan_priority,
        )
        receipts: list[tuple[str, str]] = []
        for delivery in cycle.deliveries:
            if str(delivery.get("status")) != "DELIVERED" or bool(delivery.get("duplicate", False)):
                continue
            event_id = str(delivery.get("event_id", ""))
            publication_id = self.publication_by_delivery_event_id.get(event_id)
            receiver_raw = delivery.get("receiver_id")
            if publication_id is None or receiver_raw is None:
                continue
            receiver_id = str(receiver_raw)
            self.received_publication_ids_by_agent.setdefault(receiver_id, set()).add(publication_id)
            receipts.append((receiver_id, publication_id))
        return RevisionDeliveryCycle(
            semantic_minute=semantic_minute,
            delivered_revision_receipts=tuple(receipts),
            wake_statuses=tuple(row.wake_status for row in cycle.materialized),
            decision_agent_ids=tuple(row.agent_id for row in cycle.decisions),
            delivery_processed_count=cycle.delivery_processed_count,
            delivery_deferred_due_count=cycle.delivery_deferred_due_count,
        )

    def received_state(self, agent_id: str, publication_id: str) -> ReceivedLineageState:
        return self.registry.received_state(
            publication_id,
            self.received_publication_ids_by_agent.get(agent_id, set()),
        )

    def snapshot(self) -> dict:
        return {
            "schema": SNAPSHOT_SCHEMA,
            "registry": self.registry.snapshot(),
            "cursor_by_publication_id": dict(sorted(self.cursor_by_publication_id.items())),
            "publication_by_delivery_event_id": dict(sorted(self.publication_by_delivery_event_id.items())),
            "received_publication_ids_by_agent": {
                agent_id: sorted(publication_ids)
                for agent_id, publication_ids in sorted(self.received_publication_ids_by_agent.items())
            },
        }

    @classmethod
    def restore(
        cls,
        data: Mapping[str, object],
        *,
        coordinator: GlobalNpcWorldEventCoordinator,
    ) -> "PublicationRevisionRuntime":
        if data.get("schema") != SNAPSHOT_SCHEMA:
            raise ValueError("unsupported publication revision runtime snapshot schema")
        runtime = cls(
            registry=PublicationRevisionRegistry.restore(data["registry"]),
            coordinator=coordinator,
        )
        runtime.cursor_by_publication_id = {
            str(key): None if value is None else str(value)
            for key, value in dict(data.get("cursor_by_publication_id", {})).items()
        }
        runtime.publication_by_delivery_event_id = {
            str(key): str(value)
            for key, value in dict(data.get("publication_by_delivery_event_id", {})).items()
        }
        runtime.received_publication_ids_by_agent = {
            str(agent_id): {str(value) for value in values}
            for agent_id, values in dict(data.get("received_publication_ids_by_agent", {})).items()
        }
        for agent_id in coordinator.information_queue.ledgers:
            runtime.received_publication_ids_by_agent.setdefault(agent_id, set())
        return runtime


def _agent_from_dict(row: Mapping[str, object]) -> NpcAgentState:
    return NpcAgentState(
        str(row["agent_id"]),
        AgentMode(str(row.get("mode", "OFFSCREEN_NAMED"))),
        str(row["region_ref"]),
        str(row["location_ref"]),
    )


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    agents = {str(row["agent_id"]): _agent_from_dict(row) for row in data["agents"]}
    publisher_ids = {str(row["publisher_id"]) for row in data["publications"]}
    all_agent_ids = set(agents) | publisher_ids
    ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in all_agent_ids}
    channels = {
        str(row["channel_id"]): CommunicationChannel(
            channel_id=str(row["channel_id"]),
            kind=str(row["kind"]),
            latency_minutes=int(row["latency_minutes"]),
            available=bool(row.get("available", True)),
            requires_local_projection=bool(row.get("requires_local_projection", False)),
        )
        for row in data["channels"]
    }
    queue = InformationEventQueue(channels=channels, ledgers=ledgers)
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
    )
    runtime = PublicationRevisionRuntime(
        registry=PublicationRevisionRegistry(),
        coordinator=coordinator,
    )
    members = tuple(member_from_dict(row) for row in data["audience_members"])
    publications = {
        str(row["publication_id"]): revision_from_dict(row)
        for row in data["publications"]
    }
    results: list[dict] = []

    for event in data["events"]:
        kind = str(event["kind"])
        if kind == "observe":
            claim = record_direct_observation(
                ledgers[str(event["agent_id"])],
                claim_id=str(event["claim_id"]),
                subject=str(event["subject"]),
                value=str(event["value"]),
                semantic_minute=int(event["semantic_minute"]),
                confidence=int(event["confidence"]),
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "publish":
            revision = publications[str(event["publication_id"])]
            expansion = runtime.register_and_expand(
                revision=revision,
                members=members,
                semantic_minute=int(event["semantic_minute"]),
                max_receivers=int(event["max_receivers"]),
            )
            results.append({
                "event_id": event["event_id"],
                "scheduled_agent_ids": list(expansion.scheduled_agent_ids),
                "next_cursor": expansion.next_cursor,
                "eligible_remaining": expansion.eligible_remaining,
            })
        elif kind == "cycle":
            cycle = runtime.process_cycle(
                int(event["semantic_minute"]),
                delivery_budget=int(event["delivery_budget"]),
            )
            results.append({
                "event_id": event["event_id"],
                "receipts": [list(value) for value in cycle.delivered_revision_receipts],
                "wake_statuses": list(cycle.wake_statuses),
                "decision_agent_ids": list(cycle.decision_agent_ids),
                "processed": cycle.delivery_processed_count,
                "deferred": cycle.delivery_deferred_due_count,
            })
        elif kind == "assess_lineage":
            state = runtime.received_state(str(event["agent_id"]), str(event["publication_id"]))
            results.append({
                "event_id": event["event_id"],
                "received_publication_ids": list(state.received_publication_ids),
                "latest_received_publication_id": state.latest_received_publication_id,
                "latest_received_kind": state.latest_received_kind.value if state.latest_received_kind else None,
                "current_revision_received": state.current_revision_received,
            })
        elif kind == "assess_belief":
            assessment = evaluate_belief(ledgers[str(event["agent_id"])], str(event["subject"]))
            results.append({
                "event_id": event["event_id"],
                "status": assessment.status.value,
                "preferred_value": assessment.preferred_value,
            })
        elif kind == "restart_runtime":
            runtime = PublicationRevisionRuntime.restore(runtime.snapshot(), coordinator=coordinator)
            results.append({"event_id": event["event_id"], "status": "RESTORED"})
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_publication_revision_runtime <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
