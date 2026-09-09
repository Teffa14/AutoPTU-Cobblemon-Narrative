from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from tools.global_npc_replanning import ReplanReason, ReplanTrigger
from tools.global_npc_world_event_coordinator import CoordinatorCycle, GlobalNpcWorldEventCoordinator, MaterializedDelivery


PROVENANCE_SCHEMA = "OUROS_NPC_DELIVERY_REPLAN_PROVENANCE_V1"


@dataclass(frozen=True)
class MaterializedDeliveryReceipt:
    receipt_id: str
    delivery_event_id: str
    receiver_id: str
    claim_ref: str
    provenance_root: str
    materialized_minute: int
    wake_status: str
    replan_trigger_id: str | None


@dataclass(frozen=True)
class ConsumedReplanRecord:
    consumption_id: str
    trigger_id: str
    agent_id: str
    reason: str
    source_ref: str
    due_minute: int
    priority: int
    processed_minute: int
    batch_key: str


@dataclass
class DeliveryReplanProvenanceLedger:
    materializations: dict[str, MaterializedDeliveryReceipt] = field(default_factory=dict)
    consumptions: dict[str, ConsumedReplanRecord] = field(default_factory=dict)

    def record_materialization(
        self,
        delivery: Mapping[str, object],
        materialized: MaterializedDelivery,
        *,
        semantic_minute: int,
    ) -> MaterializedDeliveryReceipt | None:
        if materialized.wake_status != "WAKE_SCHEDULED":
            return None
        if str(delivery.get("status")) != "DELIVERED":
            raise ValueError("successful materialization requires a delivered event")
        event_id = str(delivery.get("event_id", ""))
        receiver_id = str(delivery.get("receiver_id", ""))
        claim_ref = str(delivery.get("claim_id", ""))
        provenance_root = str(delivery.get("provenance_root", ""))
        if not event_id or not receiver_id or not claim_ref or not provenance_root:
            raise ValueError("materialized delivery provenance is incomplete")
        if materialized.event_id != event_id or materialized.receiver_id != receiver_id:
            raise ValueError("materialized delivery identity mismatch")
        if materialized.trigger_id is None:
            raise ValueError("wake-scheduled materialization requires a replan trigger")
        if event_id in self.materializations:
            raise ValueError(f"delivery already materialized in provenance ledger: {event_id}")
        receipt = MaterializedDeliveryReceipt(
            receipt_id=f"materialized-delivery:{event_id}",
            delivery_event_id=event_id,
            receiver_id=receiver_id,
            claim_ref=claim_ref,
            provenance_root=provenance_root,
            materialized_minute=int(semantic_minute),
            wake_status=materialized.wake_status,
            replan_trigger_id=materialized.trigger_id,
        )
        self.materializations[event_id] = receipt
        return receipt

    def record_consumed_trigger(
        self,
        trigger: ReplanTrigger,
        *,
        processed_minute: int,
    ) -> ConsumedReplanRecord:
        if trigger.trigger_id in self.consumptions:
            raise ValueError(f"trigger already consumed in provenance ledger: {trigger.trigger_id}")
        if processed_minute < trigger.due_minute:
            raise ValueError("replan trigger cannot be consumed before its due minute")
        record = ConsumedReplanRecord(
            consumption_id=f"consumed-replan:{trigger.trigger_id}",
            trigger_id=trigger.trigger_id,
            agent_id=trigger.agent_id,
            reason=trigger.reason.value,
            source_ref=trigger.source_ref,
            due_minute=trigger.due_minute,
            priority=trigger.priority,
            processed_minute=int(processed_minute),
            batch_key=f"replan-batch:{trigger.agent_id}:{int(processed_minute)}",
        )
        self.consumptions[trigger.trigger_id] = record
        return record

    def snapshot(self) -> dict:
        return {
            "schema": PROVENANCE_SCHEMA,
            "materializations": [
                {
                    "receipt_id": row.receipt_id,
                    "delivery_event_id": row.delivery_event_id,
                    "receiver_id": row.receiver_id,
                    "claim_ref": row.claim_ref,
                    "provenance_root": row.provenance_root,
                    "materialized_minute": row.materialized_minute,
                    "wake_status": row.wake_status,
                    "replan_trigger_id": row.replan_trigger_id,
                }
                for row in sorted(self.materializations.values(), key=lambda item: item.receipt_id)
            ],
            "consumptions": [
                {
                    "consumption_id": row.consumption_id,
                    "trigger_id": row.trigger_id,
                    "agent_id": row.agent_id,
                    "reason": row.reason,
                    "source_ref": row.source_ref,
                    "due_minute": row.due_minute,
                    "priority": row.priority,
                    "processed_minute": row.processed_minute,
                    "batch_key": row.batch_key,
                }
                for row in sorted(self.consumptions.values(), key=lambda item: item.consumption_id)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "DeliveryReplanProvenanceLedger":
        if snapshot.get("schema") != PROVENANCE_SCHEMA:
            raise ValueError("unsupported delivery/replan provenance schema")
        ledger = cls()
        receipt_ids: set[str] = set()
        for raw in snapshot.get("materializations", []):
            if not isinstance(raw, Mapping):
                raise ValueError("materialization row must be a mapping")
            event_id = str(raw["delivery_event_id"])
            receipt = MaterializedDeliveryReceipt(
                receipt_id=str(raw["receipt_id"]),
                delivery_event_id=event_id,
                receiver_id=str(raw["receiver_id"]),
                claim_ref=str(raw["claim_ref"]),
                provenance_root=str(raw["provenance_root"]),
                materialized_minute=int(raw["materialized_minute"]),
                wake_status=str(raw["wake_status"]),
                replan_trigger_id=None if raw.get("replan_trigger_id") is None else str(raw["replan_trigger_id"]),
            )
            if receipt.receipt_id in receipt_ids or event_id in ledger.materializations:
                raise ValueError("duplicate materialized delivery provenance")
            if receipt.wake_status != "WAKE_SCHEDULED" or receipt.replan_trigger_id is None:
                raise ValueError("persisted materialization must identify its wake trigger")
            receipt_ids.add(receipt.receipt_id)
            ledger.materializations[event_id] = receipt

        consumption_ids: set[str] = set()
        for raw in snapshot.get("consumptions", []):
            if not isinstance(raw, Mapping):
                raise ValueError("consumption row must be a mapping")
            trigger_id = str(raw["trigger_id"])
            record = ConsumedReplanRecord(
                consumption_id=str(raw["consumption_id"]),
                trigger_id=trigger_id,
                agent_id=str(raw["agent_id"]),
                reason=ReplanReason(str(raw["reason"])).value,
                source_ref=str(raw["source_ref"]),
                due_minute=int(raw["due_minute"]),
                priority=int(raw["priority"]),
                processed_minute=int(raw["processed_minute"]),
                batch_key=str(raw["batch_key"]),
            )
            if record.consumption_id in consumption_ids or trigger_id in ledger.consumptions:
                raise ValueError("duplicate consumed replan provenance")
            if record.processed_minute < record.due_minute:
                raise ValueError("persisted replan consumption predates due minute")
            consumption_ids.add(record.consumption_id)
            ledger.consumptions[trigger_id] = record
        return ledger

    def validate_against(
        self,
        coordinator: GlobalNpcWorldEventCoordinator,
        *,
        semantic_minute: int,
    ) -> None:
        queue = coordinator.information_queue
        replan_queue = coordinator.replan_queue
        for event_id, receipt in self.materializations.items():
            if receipt.materialized_minute > semantic_minute:
                raise ValueError(f"materialization comes from the future: {receipt.receipt_id}")
            if event_id not in queue.delivered_event_ids:
                raise ValueError(f"materialization references non-delivered event: {receipt.receipt_id}")
            envelope = queue.envelope_provenance(event_id)
            if envelope is None:
                raise ValueError(f"materialization envelope provenance unavailable: {receipt.receipt_id}")
            if envelope.receiver_id != receipt.receiver_id:
                raise ValueError(f"materialization receiver mismatch: {receipt.receipt_id}")
            agent = coordinator.agents.get(receipt.receiver_id)
            if agent is None:
                raise ValueError(f"materialization references unmanaged receiver: {receipt.receipt_id}")
            if receipt.claim_ref not in agent.knowledge:
                raise ValueError(f"materialized claim missing from receiver knowledge: {receipt.receipt_id}")
            if receipt.provenance_root not in agent.memory_refs:
                raise ValueError(f"materialized provenance missing from receiver memory refs: {receipt.receipt_id}")
            if receipt.replan_trigger_id not in replan_queue.known_trigger_ids:
                raise ValueError(f"materialization references unknown replan trigger: {receipt.receipt_id}")

        pending = {entry[3].trigger_id: entry[3] for entry in replan_queue.pending}
        for trigger_id, record in self.consumptions.items():
            if record.processed_minute > semantic_minute:
                raise ValueError(f"replan consumption comes from the future: {record.consumption_id}")
            if trigger_id not in replan_queue.completed_trigger_ids:
                raise ValueError(f"replan consumption references incomplete trigger: {record.consumption_id}")
            if trigger_id in pending:
                raise ValueError(f"completed replan trigger is still pending: {record.consumption_id}")
            if record.reason == ReplanReason.KNOWLEDGE_DELIVERED.value:
                receipt = self.materializations.get(record.source_ref)
                if receipt is None:
                    raise ValueError(f"knowledge-delivered consumption lacks materialization receipt: {record.consumption_id}")
                if receipt.receiver_id != record.agent_id:
                    raise ValueError(f"knowledge-delivered consumption receiver mismatch: {record.consumption_id}")
                if receipt.replan_trigger_id != trigger_id:
                    raise ValueError(f"knowledge-delivered consumption trigger mismatch: {record.consumption_id}")


@dataclass
class ProvenanceAwareWorldEventRuntime:
    coordinator: GlobalNpcWorldEventCoordinator
    ledger: DeliveryReplanProvenanceLedger = field(default_factory=DeliveryReplanProvenanceLedger)

    def _record_materialized_rows(
        self,
        cycle: CoordinatorCycle,
        *,
        semantic_minute: int,
        replan_priority: int,
    ) -> dict[str, ReplanTrigger]:
        deliveries = {str(row.get("event_id", "")): row for row in cycle.deliveries}
        created: dict[str, ReplanTrigger] = {}
        for row in cycle.materialized:
            delivery = deliveries.get(row.event_id)
            if delivery is None:
                continue
            receipt = self.ledger.record_materialization(delivery, row, semantic_minute=semantic_minute)
            if receipt is None or receipt.replan_trigger_id is None:
                continue
            created[receipt.replan_trigger_id] = ReplanTrigger(
                trigger_id=receipt.replan_trigger_id,
                agent_id=receipt.receiver_id,
                reason=ReplanReason.KNOWLEDGE_DELIVERED,
                due_minute=semantic_minute,
                source_ref=receipt.delivery_event_id,
                priority=replan_priority,
            )
        return created

    def process_cycle(
        self,
        semantic_minute: int,
        *,
        delivery_budget: int,
        replan_priority: int = 5,
    ) -> CoordinatorCycle:
        pending_before = {entry[3].trigger_id: entry[3] for entry in self.coordinator.replan_queue.pending}
        completed_before = set(self.coordinator.replan_queue.completed_trigger_ids)
        cycle = self.coordinator.process_cycle(
            semantic_minute,
            delivery_budget=delivery_budget,
            replan_priority=replan_priority,
        )
        created = self._record_materialized_rows(
            cycle,
            semantic_minute=semantic_minute,
            replan_priority=replan_priority,
        )
        trigger_candidates = pending_before | created
        newly_completed = self.coordinator.replan_queue.completed_trigger_ids - completed_before
        for trigger_id in sorted(newly_completed):
            trigger = trigger_candidates.get(trigger_id)
            if trigger is None:
                raise ValueError(f"completed replan trigger lacks structured provenance: {trigger_id}")
            self.ledger.record_consumed_trigger(trigger, processed_minute=semantic_minute)
        return cycle

    def materialize_delivery(
        self,
        delivery: Mapping[str, object],
        *,
        semantic_minute: int,
        replan_priority: int = 5,
    ) -> MaterializedDelivery:
        materialized = self.coordinator.materialize_delivery(
            delivery,
            semantic_minute=semantic_minute,
            replan_priority=replan_priority,
        )
        self.ledger.record_materialization(delivery, materialized, semantic_minute=semantic_minute)
        return materialized
