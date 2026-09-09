from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_ai import AgentMode, Handoff, NpcAgentState, agent_from_dict, bind_autoptu
from tools.global_npc_plan_selection_provenance import PlanSelectionProvenanceLedger, PlanSelectionRecord
from tools.global_npc_travel import (
    RouteEdge,
    TravelDecisionKind,
    TravelPlan,
    TravelState,
    advance_travel,
    edge_from_dict,
)


ACTION_START_SCHEMA = "OUROS_NPC_ACTION_START_PROVENANCE_V1"


class ActionStartKind(str, Enum):
    TRAVEL_EDGE_STARTED = "TRAVEL_EDGE_STARTED"
    AUTOPTU_BINDING_ACCEPTED = "AUTOPTU_BINDING_ACCEPTED"


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


def _edge_snapshot(edge: RouteEdge) -> dict:
    return {
        "edge_id": edge.edge_id,
        "from_node": edge.from_node,
        "to_node": edge.to_node,
        "duration_minutes": edge.duration_minutes,
        "enabled": edge.enabled,
        "requires_local_projection": edge.requires_local_projection,
        "requires_structured_resolution": edge.requires_structured_resolution,
        "required_knowledge": sorted(edge.required_knowledge),
        "required_permissions": sorted(edge.required_permissions),
    }


def _travel_plan_snapshot(plan: TravelPlan) -> dict:
    return {
        "plan_id": plan.plan_id,
        "agent_id": plan.agent_id,
        "origin_node": plan.origin_node,
        "destination_node": plan.destination_node,
        "edge_ids": list(plan.edge_ids),
        "departure_minute": plan.departure_minute,
        "expected_arrival_minute": plan.expected_arrival_minute,
        "reason_ref": plan.reason_ref,
        "commitment_start_minute": plan.commitment_start_minute,
        "arrival_buffer_minutes": plan.arrival_buffer_minutes,
    }


def _travel_state_snapshot(state: TravelState) -> dict:
    return {
        "plan": _travel_plan_snapshot(state.plan),
        "current_node": state.current_node,
        "next_edge_index": state.next_edge_index,
        "edge_started_minute": state.edge_started_minute,
        "semantic_minute": state.semantic_minute,
        "blocked_edge_id": state.blocked_edge_id,
    }


def _travel_state_from_dict(data: Mapping[str, object]) -> TravelState:
    raw_plan = data["plan"]
    if not isinstance(raw_plan, Mapping):
        raise ValueError("travel action-start plan snapshot must be a mapping")
    plan = TravelPlan(
        plan_id=str(raw_plan["plan_id"]),
        agent_id=str(raw_plan["agent_id"]),
        origin_node=str(raw_plan["origin_node"]),
        destination_node=str(raw_plan["destination_node"]),
        edge_ids=tuple(str(value) for value in raw_plan.get("edge_ids", [])),
        departure_minute=int(raw_plan["departure_minute"]),
        expected_arrival_minute=int(raw_plan["expected_arrival_minute"]),
        reason_ref=None if raw_plan.get("reason_ref") is None else str(raw_plan["reason_ref"]),
        commitment_start_minute=(
            None if raw_plan.get("commitment_start_minute") is None else int(raw_plan["commitment_start_minute"])
        ),
        arrival_buffer_minutes=int(raw_plan.get("arrival_buffer_minutes", 0)),
    )
    return TravelState(
        plan=plan,
        current_node=str(data["current_node"]),
        next_edge_index=int(data.get("next_edge_index", 0)),
        edge_started_minute=None if data.get("edge_started_minute") is None else int(data["edge_started_minute"]),
        semantic_minute=int(data.get("semantic_minute", 0)),
        blocked_edge_id=None if data.get("blocked_edge_id") is None else str(data["blocked_edge_id"]),
    )


@dataclass(frozen=True)
class ActionStartRecord:
    action_start_id: str
    selection_id: str
    agent_id: str
    intent_id: str
    started_minute: int
    kind: ActionStartKind
    target_ref: str | None
    evidence: Mapping[str, object]


@dataclass
class ActionStartProvenanceLedger:
    starts: dict[str, ActionStartRecord] = field(default_factory=dict)

    def _selection_fields(self, selection: PlanSelectionRecord) -> tuple[str, str, str | None]:
        selected = selection.selected
        intent_id = selected.get("intent_id")
        if intent_id is None:
            raise ValueError("plan selection has no executable intent")
        return selection.agent_id, str(intent_id), None if selected.get("target_ref") is None else str(selected["target_ref"])

    def _reserve_id(self, selection: PlanSelectionRecord, kind: ActionStartKind) -> str:
        action_start_id = f"action-start:{selection.selection_id}:{kind.value}"
        if action_start_id in self.starts:
            raise ValueError(f"action start already recorded: {action_start_id}")
        return action_start_id

    def record_travel_start(
        self,
        selection: PlanSelectionRecord,
        agent: NpcAgentState,
        state_before: TravelState,
        edges: tuple[RouteEdge, ...],
        *,
        semantic_minute: int,
    ) -> tuple[ActionStartRecord, TravelState]:
        agent_id, intent_id, target_ref = self._selection_fields(selection)
        if agent.agent_id != agent_id or state_before.plan.agent_id != agent_id:
            raise ValueError("travel action start belongs to another agent")
        if semantic_minute < selection.semantic_minute:
            raise ValueError("travel action cannot start before plan selection")
        if target_ref is not None and target_ref != state_before.plan.destination_node:
            raise ValueError("travel destination does not match selected target")

        state_after, decision = advance_travel(agent, state_before, edges, semantic_minute=semantic_minute)
        if decision.kind != TravelDecisionKind.DEPART_NOW or state_after.edge_started_minute is None:
            raise ValueError("travel evidence does not prove a departure")

        action_start_id = self._reserve_id(selection, ActionStartKind.TRAVEL_EDGE_STARTED)
        record = ActionStartRecord(
            action_start_id=action_start_id,
            selection_id=selection.selection_id,
            agent_id=agent_id,
            intent_id=intent_id,
            started_minute=state_after.edge_started_minute,
            kind=ActionStartKind.TRAVEL_EDGE_STARTED,
            target_ref=target_ref,
            evidence={
                "agent_before": _agent_snapshot(agent),
                "travel_before": _travel_state_snapshot(state_before),
                "edges": [_edge_snapshot(edge) for edge in edges],
                "decision_kind": decision.kind.value,
                "decision_edge_id": decision.edge_id,
                "travel_after": _travel_state_snapshot(state_after),
            },
        )
        self.validate_record(record)
        self.starts[action_start_id] = record
        return record, state_after

    def record_autoptu_binding_start(
        self,
        selection: PlanSelectionRecord,
        agent_before: NpcAgentState,
        *,
        binding_ref: str,
        semantic_minute: int,
    ) -> tuple[ActionStartRecord, NpcAgentState]:
        agent_id, intent_id, target_ref = self._selection_fields(selection)
        if agent_before.agent_id != agent_id:
            raise ValueError("AutoPTU action start belongs to another agent")
        if semantic_minute < selection.semantic_minute:
            raise ValueError("AutoPTU action cannot start before plan selection")
        if selection.selected.get("handoff") != Handoff.REQUEST_AUTOPTU.value:
            raise ValueError("selected plan did not request AutoPTU")
        if not binding_ref:
            raise ValueError("AutoPTU binding reference is required")

        agent_after = bind_autoptu(agent_before, binding_ref)
        action_start_id = self._reserve_id(selection, ActionStartKind.AUTOPTU_BINDING_ACCEPTED)
        record = ActionStartRecord(
            action_start_id=action_start_id,
            selection_id=selection.selection_id,
            agent_id=agent_id,
            intent_id=intent_id,
            started_minute=semantic_minute,
            kind=ActionStartKind.AUTOPTU_BINDING_ACCEPTED,
            target_ref=target_ref,
            evidence={
                "agent_before": _agent_snapshot(agent_before),
                "binding_ref": binding_ref,
                "agent_after": _agent_snapshot(agent_after),
            },
        )
        self.validate_record(record)
        self.starts[action_start_id] = record
        return record, agent_after

    def validate_record(self, record: ActionStartRecord) -> None:
        if record.started_minute < 0:
            raise ValueError("action start semantic minute cannot be negative")
        evidence = record.evidence

        if record.kind == ActionStartKind.TRAVEL_EDGE_STARTED:
            raw_agent = evidence.get("agent_before")
            raw_before = evidence.get("travel_before")
            raw_after = evidence.get("travel_after")
            raw_edges = evidence.get("edges", [])
            if not isinstance(raw_agent, Mapping) or not isinstance(raw_before, Mapping) or not isinstance(raw_after, Mapping):
                raise ValueError("travel action-start evidence is incomplete")
            agent = agent_from_dict(raw_agent)
            before = _travel_state_from_dict(raw_before)
            expected_after = _travel_state_from_dict(raw_after)
            edges = tuple(edge_from_dict(row) for row in raw_edges if isinstance(row, Mapping))
            replayed_after, decision = advance_travel(agent, before, edges, semantic_minute=record.started_minute)
            if decision.kind != TravelDecisionKind.DEPART_NOW:
                raise ValueError("travel action-start evidence no longer replays to departure")
            if _travel_state_snapshot(replayed_after) != _travel_state_snapshot(expected_after):
                raise ValueError("travel action-start state no longer replays")
            if decision.edge_id != evidence.get("decision_edge_id"):
                raise ValueError("travel action-start edge provenance mismatch")
            if agent.agent_id != record.agent_id or before.plan.agent_id != record.agent_id:
                raise ValueError("travel action-start agent provenance mismatch")
            if expected_after.edge_started_minute != record.started_minute:
                raise ValueError("travel action-start minute provenance mismatch")
            return

        if record.kind == ActionStartKind.AUTOPTU_BINDING_ACCEPTED:
            raw_agent = evidence.get("agent_before")
            raw_after = evidence.get("agent_after")
            binding_ref = str(evidence.get("binding_ref", ""))
            if not isinstance(raw_agent, Mapping) or not isinstance(raw_after, Mapping) or not binding_ref:
                raise ValueError("AutoPTU action-start evidence is incomplete")
            agent_before = agent_from_dict(raw_agent)
            expected_after = agent_from_dict(raw_after)
            replayed_after = bind_autoptu(agent_before, binding_ref)
            if _agent_snapshot(replayed_after) != _agent_snapshot(expected_after):
                raise ValueError("AutoPTU action-start state no longer replays")
            if agent_before.agent_id != record.agent_id or expected_after.agent_id != record.agent_id:
                raise ValueError("AutoPTU action-start agent provenance mismatch")
            if expected_after.mode != AgentMode.AUTOPTU_BOUND or expected_after.active_autoptu_binding != binding_ref:
                raise ValueError("AutoPTU action-start binding provenance mismatch")
            return

        raise ValueError("unsupported action start kind")

    def validate_against_plan_selections(
        self,
        selections: PlanSelectionProvenanceLedger,
        *,
        semantic_minute: int,
    ) -> None:
        seen_selection_kinds: set[tuple[str, ActionStartKind]] = set()
        for record in self.starts.values():
            self.validate_record(record)
            if record.started_minute > semantic_minute:
                raise ValueError(f"action start comes from the future: {record.action_start_id}")
            selection = selections.selections.get(record.selection_id)
            if selection is None:
                raise ValueError(f"action start references missing plan selection: {record.action_start_id}")
            agent_id, intent_id, target_ref = self._selection_fields(selection)
            if record.agent_id != agent_id or record.intent_id != intent_id or record.target_ref != target_ref:
                raise ValueError(f"action start selection provenance mismatch: {record.action_start_id}")
            if record.started_minute < selection.semantic_minute:
                raise ValueError(f"action start predates plan selection: {record.action_start_id}")
            if record.kind == ActionStartKind.AUTOPTU_BINDING_ACCEPTED and selection.selected.get("handoff") != Handoff.REQUEST_AUTOPTU.value:
                raise ValueError(f"action start lacks AutoPTU request provenance: {record.action_start_id}")
            key = (record.selection_id, record.kind)
            if key in seen_selection_kinds:
                raise ValueError("duplicate action-start kind for one plan selection")
            seen_selection_kinds.add(key)

    def snapshot(self) -> dict:
        return {
            "schema": ACTION_START_SCHEMA,
            "starts": [
                {
                    "action_start_id": row.action_start_id,
                    "selection_id": row.selection_id,
                    "agent_id": row.agent_id,
                    "intent_id": row.intent_id,
                    "started_minute": row.started_minute,
                    "kind": row.kind.value,
                    "target_ref": row.target_ref,
                    "evidence": dict(row.evidence),
                }
                for row in sorted(self.starts.values(), key=lambda item: item.action_start_id)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "ActionStartProvenanceLedger":
        if snapshot.get("schema") != ACTION_START_SCHEMA:
            raise ValueError("unsupported action start provenance schema")
        ledger = cls()
        for raw in snapshot.get("starts", []):
            if not isinstance(raw, Mapping):
                raise ValueError("action start row must be a mapping")
            action_start_id = str(raw["action_start_id"])
            if action_start_id in ledger.starts:
                raise ValueError("duplicate action start provenance")
            record = ActionStartRecord(
                action_start_id=action_start_id,
                selection_id=str(raw["selection_id"]),
                agent_id=str(raw["agent_id"]),
                intent_id=str(raw["intent_id"]),
                started_minute=int(raw["started_minute"]),
                kind=ActionStartKind(str(raw["kind"])),
                target_ref=None if raw.get("target_ref") is None else str(raw["target_ref"]),
                evidence=dict(raw.get("evidence", {})),
            )
            ledger.validate_record(record)
            ledger.starts[action_start_id] = record
        return ledger
