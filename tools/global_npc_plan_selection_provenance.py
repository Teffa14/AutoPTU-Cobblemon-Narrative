from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Mapping

from tools.global_npc_ai import (
    AgendaDecision,
    DurableGoal,
    NeedState,
    NpcAgentState,
    NpcIntent,
    ScheduledCommitment,
    agent_from_dict,
    commitment_from_dict,
    goal_from_dict,
    intent_from_dict,
    need_from_dict,
)
from tools.global_npc_delivery_replan_provenance import DeliveryReplanProvenanceLedger
from tools.global_npc_replanning import ReplanBatch, replan_from_batch


PLAN_SELECTION_SCHEMA = "OUROS_NPC_PLAN_SELECTION_PROVENANCE_V1"


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


def _goal_snapshot(goal: DurableGoal) -> dict:
    return {
        "goal_id": goal.goal_id,
        "intent_kind": goal.intent_kind,
        "priority": goal.priority,
        "progress": goal.progress,
        "target_progress": goal.target_progress,
        "required_knowledge": sorted(goal.required_knowledge),
        "required_permissions": sorted(goal.required_permissions),
        "target_ref": goal.target_ref,
        "requires_local_projection": goal.requires_local_projection,
        "requires_structured_mechanics": goal.requires_structured_mechanics,
    }


def _need_snapshot(need: NeedState) -> dict:
    return {
        "need_id": need.need_id,
        "intent_kind": need.intent_kind,
        "pressure": need.pressure,
        "activation_threshold": need.activation_threshold,
        "critical_threshold": need.critical_threshold,
        "target_ref": need.target_ref,
    }


def _commitment_snapshot(commitment: ScheduledCommitment) -> dict:
    return {
        "commitment_id": commitment.commitment_id,
        "intent_kind": commitment.intent_kind,
        "start_minute": commitment.start_minute,
        "end_minute": commitment.end_minute,
        "priority": commitment.priority,
        "hard": commitment.hard,
        "grace_minutes": commitment.grace_minutes,
        "required_knowledge": sorted(commitment.required_knowledge),
        "required_permissions": sorted(commitment.required_permissions),
        "target_ref": commitment.target_ref,
        "requires_local_projection": commitment.requires_local_projection,
        "requires_structured_mechanics": commitment.requires_structured_mechanics,
    }


def _intent_snapshot(intent: NpcIntent) -> dict:
    return {
        "intent_id": intent.intent_id,
        "kind": intent.kind,
        "base_priority": intent.base_priority,
        "urgency": intent.urgency,
        "obligation": intent.obligation,
        "risk": intent.risk,
        "travel_cost": intent.travel_cost,
        "relationship_weight": intent.relationship_weight,
        "required_knowledge": sorted(intent.required_knowledge),
        "required_permissions": sorted(intent.required_permissions),
        "requires_local_projection": intent.requires_local_projection,
        "requires_structured_mechanics": intent.requires_structured_mechanics,
        "target_ref": intent.target_ref,
    }


def _decision_snapshot(decision: AgendaDecision) -> dict:
    row = decision.decision
    return {
        "agent_id": row.agent_id,
        "intent_id": row.intent_id,
        "kind": row.kind,
        "score": row.score,
        "handoff": row.handoff.value,
        "reason_codes": list(row.reason_codes),
        "target_ref": row.target_ref,
        "source_type": decision.source_type,
        "source_ref": decision.source_ref,
        "schedule_state": decision.schedule_state,
    }


@dataclass(frozen=True)
class PlanSelectionRecord:
    selection_id: str
    batch_key: str
    agent_id: str
    semantic_minute: int
    trigger_ids: tuple[str, ...]
    reasons: tuple[str, ...]
    source_refs: tuple[str, ...]
    highest_priority: int
    agent_snapshot: Mapping[str, object]
    goals: tuple[Mapping[str, object], ...]
    needs: tuple[Mapping[str, object], ...]
    commitments: tuple[Mapping[str, object], ...]
    situational_intents: tuple[Mapping[str, object], ...]
    active_intent_id: str | None
    continuity_bonus: int
    selected: Mapping[str, object]


@dataclass
class PlanSelectionProvenanceLedger:
    selections: dict[str, PlanSelectionRecord] = field(default_factory=dict)

    def record_selection(
        self,
        batch: ReplanBatch,
        agent: NpcAgentState,
        *,
        goals: Iterable[DurableGoal] = (),
        needs: Iterable[NeedState] = (),
        commitments: Iterable[ScheduledCommitment] = (),
        situational_intents: Iterable[NpcIntent] = (),
        active_intent_id: str | None = None,
        continuity_bonus: int = 1,
    ) -> tuple[PlanSelectionRecord, AgendaDecision]:
        if batch.agent_id != agent.agent_id:
            raise ValueError("plan selection batch belongs to another agent")
        goals = tuple(goals)
        needs = tuple(needs)
        commitments = tuple(commitments)
        situational_intents = tuple(situational_intents)
        decision = replan_from_batch(
            agent,
            batch,
            goals=goals,
            needs=needs,
            commitments=commitments,
            situational_intents=situational_intents,
            active_intent_id=active_intent_id,
            continuity_bonus=continuity_bonus,
        )
        batch_key = f"replan-batch:{batch.agent_id}:{batch.semantic_minute}"
        selection_id = f"plan-selection:{batch.agent_id}:{batch.semantic_minute}:{'|'.join(batch.trigger_ids)}"
        if selection_id in self.selections:
            raise ValueError(f"plan selection already recorded: {selection_id}")
        record = PlanSelectionRecord(
            selection_id=selection_id,
            batch_key=batch_key,
            agent_id=batch.agent_id,
            semantic_minute=batch.semantic_minute,
            trigger_ids=tuple(batch.trigger_ids),
            reasons=tuple(batch.reasons),
            source_refs=tuple(batch.source_refs),
            highest_priority=batch.highest_priority,
            agent_snapshot=_agent_snapshot(agent),
            goals=tuple(_goal_snapshot(item) for item in goals),
            needs=tuple(_need_snapshot(item) for item in needs),
            commitments=tuple(_commitment_snapshot(item) for item in commitments),
            situational_intents=tuple(_intent_snapshot(item) for item in situational_intents),
            active_intent_id=active_intent_id,
            continuity_bonus=int(continuity_bonus),
            selected=_decision_snapshot(decision),
        )
        self.selections[selection_id] = record
        return record, decision

    def _replay(self, record: PlanSelectionRecord) -> AgendaDecision:
        batch = ReplanBatch(
            agent_id=record.agent_id,
            semantic_minute=record.semantic_minute,
            trigger_ids=record.trigger_ids,
            reasons=record.reasons,
            source_refs=record.source_refs,
            highest_priority=record.highest_priority,
        )
        return replan_from_batch(
            agent_from_dict(record.agent_snapshot),
            batch,
            goals=tuple(goal_from_dict(row) for row in record.goals),
            needs=tuple(need_from_dict(row) for row in record.needs),
            commitments=tuple(commitment_from_dict(row) for row in record.commitments),
            situational_intents=tuple(intent_from_dict(row) for row in record.situational_intents),
            active_intent_id=record.active_intent_id,
            continuity_bonus=record.continuity_bonus,
        )

    def validate_record(self, record: PlanSelectionRecord) -> None:
        if record.semantic_minute < 0:
            raise ValueError("plan selection semantic minute cannot be negative")
        if len(record.trigger_ids) != len(set(record.trigger_ids)):
            raise ValueError("plan selection contains duplicate trigger IDs")
        replayed = _decision_snapshot(self._replay(record))
        if dict(record.selected) != replayed:
            raise ValueError(f"plan selection no longer replays to persisted decision: {record.selection_id}")

    def validate_against_replan_provenance(
        self,
        provenance: DeliveryReplanProvenanceLedger,
        *,
        semantic_minute: int,
    ) -> None:
        for record in self.selections.values():
            self.validate_record(record)
            if record.semantic_minute > semantic_minute:
                raise ValueError(f"plan selection comes from the future: {record.selection_id}")
            for trigger_id in record.trigger_ids:
                consumed = provenance.consumptions.get(trigger_id)
                if consumed is None:
                    raise ValueError(f"plan selection references unconsumed trigger: {record.selection_id}")
                if consumed.agent_id != record.agent_id:
                    raise ValueError(f"plan selection trigger agent mismatch: {record.selection_id}")
                if consumed.processed_minute != record.semantic_minute:
                    raise ValueError(f"plan selection trigger minute mismatch: {record.selection_id}")
                if consumed.batch_key != record.batch_key:
                    raise ValueError(f"plan selection batch provenance mismatch: {record.selection_id}")

    def snapshot(self) -> dict:
        return {
            "schema": PLAN_SELECTION_SCHEMA,
            "selections": [
                {
                    "selection_id": row.selection_id,
                    "batch_key": row.batch_key,
                    "agent_id": row.agent_id,
                    "semantic_minute": row.semantic_minute,
                    "trigger_ids": list(row.trigger_ids),
                    "reasons": list(row.reasons),
                    "source_refs": list(row.source_refs),
                    "highest_priority": row.highest_priority,
                    "agent_snapshot": dict(row.agent_snapshot),
                    "goals": [dict(item) for item in row.goals],
                    "needs": [dict(item) for item in row.needs],
                    "commitments": [dict(item) for item in row.commitments],
                    "situational_intents": [dict(item) for item in row.situational_intents],
                    "active_intent_id": row.active_intent_id,
                    "continuity_bonus": row.continuity_bonus,
                    "selected": dict(row.selected),
                }
                for row in sorted(self.selections.values(), key=lambda item: item.selection_id)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "PlanSelectionProvenanceLedger":
        if snapshot.get("schema") != PLAN_SELECTION_SCHEMA:
            raise ValueError("unsupported plan selection provenance schema")
        ledger = cls()
        for raw in snapshot.get("selections", []):
            if not isinstance(raw, Mapping):
                raise ValueError("plan selection row must be a mapping")
            selection_id = str(raw["selection_id"])
            if selection_id in ledger.selections:
                raise ValueError("duplicate plan selection provenance")
            record = PlanSelectionRecord(
                selection_id=selection_id,
                batch_key=str(raw["batch_key"]),
                agent_id=str(raw["agent_id"]),
                semantic_minute=int(raw["semantic_minute"]),
                trigger_ids=tuple(str(value) for value in raw.get("trigger_ids", [])),
                reasons=tuple(str(value) for value in raw.get("reasons", [])),
                source_refs=tuple(str(value) for value in raw.get("source_refs", [])),
                highest_priority=int(raw["highest_priority"]),
                agent_snapshot=dict(raw["agent_snapshot"]),
                goals=tuple(dict(item) for item in raw.get("goals", [])),
                needs=tuple(dict(item) for item in raw.get("needs", [])),
                commitments=tuple(dict(item) for item in raw.get("commitments", [])),
                situational_intents=tuple(dict(item) for item in raw.get("situational_intents", [])),
                active_intent_id=None if raw.get("active_intent_id") is None else str(raw["active_intent_id"]),
                continuity_bonus=int(raw.get("continuity_bonus", 1)),
                selected=dict(raw["selected"]),
            )
            ledger.validate_record(record)
            ledger.selections[selection_id] = record
        return ledger
