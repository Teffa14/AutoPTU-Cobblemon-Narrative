from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_ai import (
    AgendaDecision,
    AgentMode,
    DurableGoal,
    NeedState,
    NpcAgentState,
    NpcIntent,
    ScheduledCommitment,
)
from tools.global_npc_information_network import InformationEventQueue
from tools.global_npc_replanning import (
    NpcReplanQueue,
    ReplanBatch,
    apply_information_delivery,
    replan_from_batch,
    schedule_information_replan,
)


@dataclass(frozen=True)
class AgentAgendaProfile:
    goals: tuple[DurableGoal, ...] = ()
    needs: tuple[NeedState, ...] = ()
    commitments: tuple[ScheduledCommitment, ...] = ()
    situational_intents: tuple[NpcIntent, ...] = ()
    active_intent_id: str | None = None
    continuity_bonus: int = 1


@dataclass(frozen=True)
class MaterializedDelivery:
    event_id: str
    receiver_id: str | None
    wake_status: str
    trigger_id: str | None = None


@dataclass(frozen=True)
class CoordinatedDecision:
    agent_id: str
    trigger_ids: tuple[str, ...]
    reasons: tuple[str, ...]
    decision: AgendaDecision


@dataclass(frozen=True)
class CoordinatorCycle:
    semantic_minute: int
    deliveries: tuple[Mapping[str, object], ...]
    materialized: tuple[MaterializedDelivery, ...]
    decisions: tuple[CoordinatedDecision, ...]
    delivery_processed_count: int
    delivery_deferred_due_count: int


class GlobalNpcWorldEventCoordinator:
    """Connect semantic information delivery to selective world-agent replanning.

    The coordinator composes existing Ouros subsystems. It does not own memory
    truth, communication transport, tactical legality or Minecraft projection.
    """

    def __init__(
        self,
        *,
        information_queue: InformationEventQueue,
        replan_queue: NpcReplanQueue,
        agents: Mapping[str, NpcAgentState],
        agendas: Mapping[str, AgentAgendaProfile] | None = None,
    ) -> None:
        self.information_queue = information_queue
        self.replan_queue = replan_queue
        self.agents = dict(agents)
        self.agendas = dict(agendas or {})
        self.materialized_delivery_event_ids: set[str] = set()

    def _materialize_delivery(
        self,
        delivery: Mapping[str, object],
        *,
        semantic_minute: int,
        replan_priority: int,
    ) -> MaterializedDelivery:
        event_id = str(delivery.get("event_id", ""))
        receiver_raw = delivery.get("receiver_id")
        receiver_id = None if receiver_raw is None else str(receiver_raw)

        if str(delivery.get("status")) != "DELIVERED":
            return MaterializedDelivery(event_id, receiver_id, "NO_WAKE_NON_DELIVERY")
        if bool(delivery.get("duplicate", False)) or event_id in self.materialized_delivery_event_ids:
            return MaterializedDelivery(event_id, receiver_id, "NO_WAKE_DUPLICATE")
        if receiver_id is None or receiver_id not in self.agents:
            self.materialized_delivery_event_ids.add(event_id)
            return MaterializedDelivery(event_id, receiver_id, "NO_MANAGED_WORLD_AGENT")

        agent = apply_information_delivery(self.agents[receiver_id], delivery)
        self.agents[receiver_id] = agent
        trigger = schedule_information_replan(
            self.replan_queue,
            delivery=delivery,
            semantic_minute=semantic_minute,
            priority=replan_priority,
        )
        self.materialized_delivery_event_ids.add(event_id)
        return MaterializedDelivery(
            event_id,
            receiver_id,
            "WAKE_SCHEDULED",
            None if trigger is None else trigger.trigger_id,
        )

    def materialize_delivery(
        self,
        delivery: Mapping[str, object],
        *,
        semantic_minute: int,
        replan_priority: int = 5,
    ) -> MaterializedDelivery:
        """Apply one externally completed delivery, including local-adapter ACK results."""
        return self._materialize_delivery(
            delivery,
            semantic_minute=semantic_minute,
            replan_priority=replan_priority,
        )

    def _decide_batch(self, batch: ReplanBatch) -> CoordinatedDecision | None:
        agent = self.agents.get(batch.agent_id)
        if agent is None:
            return None
        profile = self.agendas.get(batch.agent_id, AgentAgendaProfile())
        decision = replan_from_batch(
            agent,
            batch,
            goals=profile.goals,
            needs=profile.needs,
            commitments=profile.commitments,
            situational_intents=profile.situational_intents,
            active_intent_id=profile.active_intent_id,
            continuity_bonus=profile.continuity_bonus,
        )
        return CoordinatedDecision(
            agent_id=batch.agent_id,
            trigger_ids=batch.trigger_ids,
            reasons=batch.reasons,
            decision=decision,
        )

    def process_cycle(
        self,
        semantic_minute: int,
        *,
        delivery_budget: int,
        replan_priority: int = 5,
    ) -> CoordinatorCycle:
        delivery_outcome = self.information_queue.process_due_budgeted(
            semantic_minute,
            max_events=delivery_budget,
        )
        deliveries = tuple(delivery_outcome["deliveries"])
        materialized = tuple(
            self._materialize_delivery(
                delivery,
                semantic_minute=semantic_minute,
                replan_priority=replan_priority,
            )
            for delivery in deliveries
        )
        batches = self.replan_queue.process_due(semantic_minute)
        decisions = tuple(
            decision
            for batch in batches
            if (decision := self._decide_batch(batch)) is not None
        )
        return CoordinatorCycle(
            semantic_minute=semantic_minute,
            deliveries=deliveries,
            materialized=materialized,
            decisions=decisions,
            delivery_processed_count=int(delivery_outcome["processed_count"]),
            delivery_deferred_due_count=int(delivery_outcome["deferred_due_count"]),
        )


def _agent_from_dict(row: Mapping[str, object]) -> NpcAgentState:
    return NpcAgentState(
        agent_id=str(row["agent_id"]),
        mode=AgentMode(str(row.get("mode", "OFFSCREEN_NAMED"))),
        region_ref=str(row["region_ref"]),
        location_ref=str(row["location_ref"]),
        risk_tolerance=int(row.get("risk_tolerance", 50)),
        energy=int(row.get("energy", 100)),
        knowledge=frozenset(str(value) for value in row.get("knowledge", [])),
        permissions=frozenset(str(value) for value in row.get("permissions", [])),
    )


def replay_fixture(path: str | Path) -> dict:
    from tools.global_npc_information_network import CommunicationChannel
    from tools.global_npc_memory import KnowledgeLedger, evaluate_belief, record_direct_observation

    data = json.loads(Path(path).read_text(encoding="utf-8"))
    agents = {row["agent_id"]: _agent_from_dict(row) for row in data["agents"]}
    ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
    channels = {
        row["channel_id"]: CommunicationChannel(
            channel_id=row["channel_id"],
            kind=row["kind"],
            latency_minutes=int(row["latency_minutes"]),
            available=bool(row.get("available", True)),
            requires_local_projection=bool(row.get("requires_local_projection", False)),
        )
        for row in data["channels"]
    }
    information_queue = InformationEventQueue(channels=channels, ledgers=ledgers)
    replan_queue = NpcReplanQueue()
    agendas: dict[str, AgentAgendaProfile] = {}
    for row in data.get("agendas", []):
        goals = tuple(
            DurableGoal(
                goal_id=str(goal["goal_id"]),
                intent_kind=str(goal["intent_kind"]),
                priority=int(goal["priority"]),
                target_ref=goal.get("target_ref"),
            )
            for goal in row.get("goals", [])
        )
        intents = tuple(
            NpcIntent(
                intent_id=str(intent["intent_id"]),
                kind=str(intent["kind"]),
                base_priority=int(intent.get("base_priority", 0)),
                urgency=int(intent.get("urgency", 0)),
                required_knowledge=frozenset(str(value) for value in intent.get("required_knowledge", [])),
                target_ref=intent.get("target_ref"),
                requires_structured_mechanics=bool(intent.get("requires_structured_mechanics", False)),
            )
            for intent in row.get("situational_intents", [])
        )
        agendas[str(row["agent_id"])] = AgentAgendaProfile(goals=goals, situational_intents=intents)

    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=information_queue,
        replan_queue=replan_queue,
        agents=agents,
        agendas=agendas,
    )
    results: list[dict] = []

    for event in data["events"]:
        kind = event["kind"]
        if kind == "observe":
            claim = record_direct_observation(
                ledgers[event["agent_id"]],
                claim_id=event["claim_id"],
                subject=event["subject"],
                value=event["value"],
                semantic_minute=int(event["semantic_minute"]),
                confidence=int(event["confidence"]),
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "schedule_message":
            envelope = information_queue.schedule(
                event_id=event["delivery_event_id"],
                message_id=event["message_id"],
                sender_id=event["sender_id"],
                receiver_id=event["receiver_id"],
                source_claim_id=event["source_claim_id"],
                new_claim_id=event["new_claim_id"],
                channel_id=event["channel_id"],
                created_minute=int(event["semantic_minute"]),
                receiver_trust_in_sender=int(event.get("receiver_trust_in_sender", 0)),
            )
            results.append({"event_id": event["event_id"], "delivery_minute": envelope.delivery_minute})
        elif kind == "cycle":
            cycle = coordinator.process_cycle(
                int(event["semantic_minute"]),
                delivery_budget=int(event["delivery_budget"]),
                replan_priority=int(event.get("replan_priority", 5)),
            )
            results.append({
                "event_id": event["event_id"],
                "processed": cycle.delivery_processed_count,
                "deferred": cycle.delivery_deferred_due_count,
                "materialized": [row.wake_status for row in cycle.materialized],
                "decisions": [
                    {
                        "agent_id": row.agent_id,
                        "kind": row.decision.decision.kind,
                        "handoff": row.decision.decision.handoff.value,
                        "target_ref": row.decision.decision.target_ref,
                    }
                    for row in cycle.decisions
                ],
            })
        elif kind == "assess":
            assessment = evaluate_belief(ledgers[event["agent_id"]], event["subject"])
            results.append({
                "event_id": event["event_id"],
                "status": assessment.status.value,
                "preferred_value": assessment.preferred_value,
                "agent_knows_claim": event["claim_id"] in coordinator.agents[event["agent_id"]].knowledge,
            })
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_world_event_coordinator <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
