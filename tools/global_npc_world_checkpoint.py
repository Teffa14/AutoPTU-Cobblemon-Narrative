from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from tools.global_npc_ai import AgentMode, NpcAgentState, agent_from_dict
from tools.global_npc_deception_runtime import DeceptionInformationEventQueue
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, KnowledgeLedgerStore, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V2"
LEGACY_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V1"
STANDARD_QUEUE_KIND = "STANDARD"
DECEPTION_QUEUE_KIND = "DECEPTION"


@dataclass(frozen=True)
class RestoredWorldCheckpoint:
    semantic_minute: int
    coordinator: GlobalNpcWorldEventCoordinator
    ledger_store: KnowledgeLedgerStore
    publication_runtime_snapshot: Mapping[str, object] | None


def _agent_snapshot(agent: NpcAgentState) -> dict:
    return {
        "agent_id": agent.agent_id,
        "mode": agent.mode.value,
        "region_ref": agent.region_ref,
        "location_ref": agent.location_ref,
        "risk_tolerance": agent.risk_tolerance,
        "energy": agent.energy,
        "knowledge": sorted(agent.knowledge),
        "permissions": sorted(agent.permissions),
        "memory_refs": list(agent.memory_refs),
        "active_autoptu_binding": agent.active_autoptu_binding,
    }


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _validated_payload(snapshot: Mapping[str, object]) -> dict:
    if snapshot.get("schema") not in {CHECKPOINT_SCHEMA, LEGACY_CHECKPOINT_SCHEMA}:
        raise ValueError("unsupported global NPC world checkpoint schema")
    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world checkpoint digest mismatch")
    return payload


def _queue_kind(queue: InformationEventQueue) -> str:
    if isinstance(queue, DeceptionInformationEventQueue):
        return DECEPTION_QUEUE_KIND
    return STANDARD_QUEUE_KIND


def build_checkpoint(
    coordinator: GlobalNpcWorldEventCoordinator,
    *,
    semantic_minute: int,
    publication_runtime_snapshot: Mapping[str, object] | None = None,
) -> dict:
    """Create one deterministic logical snapshot of coupled global-NPC state.

    The returned object is a logical atomic unit only. Durable crash-safe commit
    to disk/database belongs to the persistence adapter and is intentionally not
    claimed by this module.
    """
    ledger_store = KnowledgeLedgerStore(dict(coordinator.information_queue.ledgers))
    payload = {
        "schema": CHECKPOINT_SCHEMA,
        "semantic_minute": int(semantic_minute),
        "agents": [
            _agent_snapshot(coordinator.agents[agent_id])
            for agent_id in sorted(coordinator.agents)
        ],
        "knowledge_ledgers": ledger_store.snapshot(),
        "information_queue_kind": _queue_kind(coordinator.information_queue),
        "information_queue": coordinator.information_queue.snapshot(),
        "replan_queue": coordinator.replan_queue.to_snapshot(),
        "materialized_delivery_event_ids": sorted(coordinator.materialized_delivery_event_ids),
        "publication_runtime": None if publication_runtime_snapshot is None else dict(publication_runtime_snapshot),
    }
    return payload | {"sha256": _digest_payload(payload)}


def _validate_references(
    *,
    queue: InformationEventQueue,
    coordinator: GlobalNpcWorldEventCoordinator,
) -> None:
    ledgers = queue.ledgers
    envelopes = [entry[2] for entry in queue.pending] + list(queue.awaiting_local_ack.values())
    for envelope in envelopes:
        if envelope.sender_id not in ledgers or envelope.receiver_id not in ledgers:
            raise ValueError(f"checkpoint envelope references missing ledger: {envelope.event_id}")
        if envelope.source_claim_id not in ledgers[envelope.sender_id].claims:
            raise ValueError(f"checkpoint envelope source claim is missing: {envelope.event_id}")
    missing_materialized = coordinator.materialized_delivery_event_ids - queue.delivered_event_ids
    if missing_materialized:
        raise ValueError(
            "checkpoint materialized delivery guard references non-delivered events: "
            + ",".join(sorted(missing_materialized))
        )


def _restore_information_queue(
    payload: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    ledgers: dict[str, KnowledgeLedger],
) -> InformationEventQueue:
    kind = str(payload.get("information_queue_kind", STANDARD_QUEUE_KIND))
    queue_snapshot = payload["information_queue"]
    if not isinstance(queue_snapshot, Mapping):
        raise ValueError("information_queue checkpoint must be a mapping")
    if kind == STANDARD_QUEUE_KIND:
        return InformationEventQueue.restore(queue_snapshot, channels=dict(channels), ledgers=ledgers)
    if kind == DECEPTION_QUEUE_KIND:
        return DeceptionInformationEventQueue.restore(queue_snapshot, channels=dict(channels), ledgers=ledgers)
    raise ValueError(f"unsupported information queue kind: {kind}")


def restore_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    agendas: Mapping[str, AgentAgendaProfile] | None = None,
) -> RestoredWorldCheckpoint:
    """Validate the complete checkpoint before returning restored live objects."""
    payload = _validated_payload(snapshot)
    ledger_store = KnowledgeLedgerStore.restore(payload["knowledge_ledgers"])
    queue = _restore_information_queue(payload, channels=channels, ledgers=ledger_store.ledgers)
    replan_queue = NpcReplanQueue.from_snapshot(payload["replan_queue"])
    agents = {
        str(row["agent_id"]): agent_from_dict(row)
        for row in payload.get("agents", [])
    }
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=replan_queue,
        agents=agents,
        agendas=agendas,
    )
    coordinator.materialized_delivery_event_ids = {
        str(value) for value in payload.get("materialized_delivery_event_ids", [])
    }
    _validate_references(queue=queue, coordinator=coordinator)
    runtime = payload.get("publication_runtime")
    if runtime is not None and not isinstance(runtime, Mapping):
        raise ValueError("publication_runtime checkpoint must be a mapping or null")
    return RestoredWorldCheckpoint(
        semantic_minute=int(payload["semantic_minute"]),
        coordinator=coordinator,
        ledger_store=ledger_store,
        publication_runtime_snapshot=runtime,
    )


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    agents = {
        str(row["agent_id"]): NpcAgentState(
            agent_id=str(row["agent_id"]),
            mode=AgentMode(str(row.get("mode", "OFFSCREEN_NAMED"))),
            region_ref=str(row["region_ref"]),
            location_ref=str(row["location_ref"]),
        )
        for row in data["agents"]
    }
    ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
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
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
        replan_queue=NpcReplanQueue(),
        agents=agents,
    )
    results: list[dict] = []

    for event in data["events"]:
        kind = str(event["kind"])
        if kind == "observe":
            claim = record_direct_observation(
                coordinator.information_queue.ledgers[str(event["agent_id"])],
                claim_id=str(event["claim_id"]),
                subject=str(event["subject"]),
                value=str(event["value"]),
                semantic_minute=int(event["semantic_minute"]),
                confidence=int(event["confidence"]),
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "schedule":
            envelope = coordinator.information_queue.schedule(
                event_id=str(event["delivery_event_id"]),
                message_id=str(event["message_id"]),
                sender_id=str(event["sender_id"]),
                receiver_id=str(event["receiver_id"]),
                source_claim_id=str(event["source_claim_id"]),
                new_claim_id=str(event["new_claim_id"]),
                channel_id=str(event["channel_id"]),
                created_minute=int(event["semantic_minute"]),
            )
            results.append({"event_id": event["event_id"], "delivery_minute": envelope.delivery_minute})
        elif kind == "checkpoint_restart":
            checkpoint = build_checkpoint(coordinator, semantic_minute=int(event["semantic_minute"]))
            restored = restore_checkpoint(checkpoint, channels=channels)
            coordinator = restored.coordinator
            results.append({
                "event_id": event["event_id"],
                "status": "RESTORED",
                "semantic_minute": restored.semantic_minute,
                "digest": checkpoint["sha256"],
            })
        elif kind == "cycle":
            cycle = coordinator.process_cycle(
                int(event["semantic_minute"]),
                delivery_budget=int(event["delivery_budget"]),
            )
            results.append({
                "event_id": event["event_id"],
                "processed": cycle.delivery_processed_count,
                "deferred": cycle.delivery_deferred_due_count,
                "wake_statuses": [row.wake_status for row in cycle.materialized],
                "decision_agent_ids": [row.agent_id for row in cycle.decisions],
            })
        elif kind == "inspect":
            agent_id = str(event["agent_id"])
            results.append({
                "event_id": event["event_id"],
                "claim_ids": sorted(coordinator.information_queue.ledgers[agent_id].claims),
                "knowledge": sorted(coordinator.agents[agent_id].knowledge),
                "delivered_event_ids": sorted(coordinator.information_queue.delivered_event_ids),
                "materialized_event_ids": sorted(coordinator.materialized_delivery_event_ids),
            })
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_world_checkpoint <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
