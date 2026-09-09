from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_action_start_provenance import (
    ActionStartKind,
    ActionStartProvenanceLedger,
    ActionStartRecord,
    _agent_snapshot,
    _edge_snapshot,
    _travel_state_from_dict,
    _travel_state_snapshot,
)
from tools.global_npc_ai import agent_from_dict
from tools.global_npc_travel import TravelDecisionKind, advance_travel, edge_from_dict


ACTION_INTERRUPTION_SCHEMA = "OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1"


class ActionInterruptionKind(str, Enum):
    TRAVEL_REPLAN_REQUIRED = "TRAVEL_REPLAN_REQUIRED"


@dataclass(frozen=True)
class ActionInterruptionRecord:
    action_interruption_id: str
    action_start_id: str
    selection_id: str
    agent_id: str
    intent_id: str
    interrupted_minute: int
    kind: ActionInterruptionKind
    target_ref: str | None
    evidence: Mapping[str, object]


@dataclass
class ActionInterruptionProvenanceLedger:
    interruptions: dict[str, ActionInterruptionRecord] = field(default_factory=dict)

    def _reserve_id(self, start: ActionStartRecord, kind: ActionInterruptionKind) -> str:
        interruption_id = f"action-interruption:{start.action_start_id}:{kind.value}"
        if interruption_id in self.interruptions:
            raise ValueError(f"action interruption already recorded: {interruption_id}")
        return interruption_id

    def record_travel_replan_required(
        self,
        start: ActionStartRecord,
        current_edges: tuple[object, ...],
        *,
        semantic_minute: int,
    ) -> ActionInterruptionRecord:
        if start.kind != ActionStartKind.TRAVEL_EDGE_STARTED:
            raise ValueError("travel interruption requires a travel action start")
        if semantic_minute < start.started_minute:
            raise ValueError("travel interruption cannot precede action start")

        raw_agent = start.evidence.get("agent_before")
        raw_started = start.evidence.get("travel_after")
        if not isinstance(raw_agent, Mapping) or not isinstance(raw_started, Mapping):
            raise ValueError("source travel action-start evidence is incomplete")

        agent = agent_from_dict(raw_agent)
        started_state = _travel_state_from_dict(raw_started)
        edges = tuple(current_edges)
        interrupted_state, decision = advance_travel(
            agent,
            started_state,
            edges,
            semantic_minute=semantic_minute,
        )
        if decision.kind != TravelDecisionKind.REPLAN_REQUIRED:
            raise ValueError("travel evidence does not prove a replan-required interruption")

        interruption_id = self._reserve_id(start, ActionInterruptionKind.TRAVEL_REPLAN_REQUIRED)
        record = ActionInterruptionRecord(
            action_interruption_id=interruption_id,
            action_start_id=start.action_start_id,
            selection_id=start.selection_id,
            agent_id=start.agent_id,
            intent_id=start.intent_id,
            interrupted_minute=semantic_minute,
            kind=ActionInterruptionKind.TRAVEL_REPLAN_REQUIRED,
            target_ref=start.target_ref,
            evidence={
                "agent": _agent_snapshot(agent),
                "travel_started": _travel_state_snapshot(started_state),
                "edges_at_interruption": [_edge_snapshot(edge) for edge in edges],
                "decision_kind": decision.kind.value,
                "decision_edge_id": decision.edge_id,
                "reason_codes": list(decision.reason_codes),
                "travel_interrupted": _travel_state_snapshot(interrupted_state),
            },
        )
        self.validate_record(record)
        self.interruptions[interruption_id] = record
        return record

    def validate_record(self, record: ActionInterruptionRecord) -> None:
        if record.interrupted_minute < 0:
            raise ValueError("action interruption semantic minute cannot be negative")
        if record.kind != ActionInterruptionKind.TRAVEL_REPLAN_REQUIRED:
            raise ValueError("unsupported action interruption kind")

        evidence = record.evidence
        raw_agent = evidence.get("agent")
        raw_started = evidence.get("travel_started")
        raw_interrupted = evidence.get("travel_interrupted")
        raw_edges = evidence.get("edges_at_interruption", [])
        if not isinstance(raw_agent, Mapping) or not isinstance(raw_started, Mapping) or not isinstance(raw_interrupted, Mapping):
            raise ValueError("travel interruption evidence is incomplete")

        agent = agent_from_dict(raw_agent)
        started_state = _travel_state_from_dict(raw_started)
        expected_interrupted = _travel_state_from_dict(raw_interrupted)
        edges = tuple(edge_from_dict(row) for row in raw_edges if isinstance(row, Mapping))
        replayed_state, decision = advance_travel(
            agent,
            started_state,
            edges,
            semantic_minute=record.interrupted_minute,
        )
        if decision.kind != TravelDecisionKind.REPLAN_REQUIRED:
            raise ValueError("travel interruption evidence no longer replays to replan required")
        if _travel_state_snapshot(replayed_state) != _travel_state_snapshot(expected_interrupted):
            raise ValueError("travel interruption state no longer replays")
        if evidence.get("decision_kind") != TravelDecisionKind.REPLAN_REQUIRED.value:
            raise ValueError("travel interruption decision provenance mismatch")
        if decision.edge_id != evidence.get("decision_edge_id"):
            raise ValueError("travel interruption edge provenance mismatch")
        if list(decision.reason_codes) != list(evidence.get("reason_codes", [])):
            raise ValueError("travel interruption reason provenance mismatch")
        if agent.agent_id != record.agent_id or started_state.plan.agent_id != record.agent_id:
            raise ValueError("travel interruption agent provenance mismatch")
        if expected_interrupted.semantic_minute != record.interrupted_minute:
            raise ValueError("travel interruption minute provenance mismatch")
        if expected_interrupted.blocked_edge_id != decision.edge_id:
            raise ValueError("travel interruption blocked-edge provenance mismatch")

    def validate_against_action_starts(
        self,
        starts: ActionStartProvenanceLedger,
        *,
        semantic_minute: int,
    ) -> None:
        seen_starts: set[str] = set()
        for record in self.interruptions.values():
            self.validate_record(record)
            if record.interrupted_minute > semantic_minute:
                raise ValueError(f"action interruption comes from the future: {record.action_interruption_id}")
            start = starts.starts.get(record.action_start_id)
            if start is None:
                raise ValueError(f"action interruption references missing action start: {record.action_interruption_id}")
            if start.kind != ActionStartKind.TRAVEL_EDGE_STARTED:
                raise ValueError(f"travel interruption lacks travel start provenance: {record.action_interruption_id}")
            if (
                record.selection_id != start.selection_id
                or record.agent_id != start.agent_id
                or record.intent_id != start.intent_id
                or record.target_ref != start.target_ref
            ):
                raise ValueError(f"action interruption start provenance mismatch: {record.action_interruption_id}")
            if record.interrupted_minute < start.started_minute:
                raise ValueError(f"action interruption predates action start: {record.action_interruption_id}")
            if record.action_start_id in seen_starts:
                raise ValueError("duplicate interruption outcome for one action start")
            seen_starts.add(record.action_start_id)

            if record.evidence.get("agent") != start.evidence.get("agent_before"):
                raise ValueError(f"action interruption agent snapshot diverges from source start: {record.action_interruption_id}")
            if record.evidence.get("travel_started") != start.evidence.get("travel_after"):
                raise ValueError(f"action interruption travel snapshot diverges from source start: {record.action_interruption_id}")

    def snapshot(self) -> dict:
        return {
            "schema": ACTION_INTERRUPTION_SCHEMA,
            "interruptions": [
                {
                    "action_interruption_id": row.action_interruption_id,
                    "action_start_id": row.action_start_id,
                    "selection_id": row.selection_id,
                    "agent_id": row.agent_id,
                    "intent_id": row.intent_id,
                    "interrupted_minute": row.interrupted_minute,
                    "kind": row.kind.value,
                    "target_ref": row.target_ref,
                    "evidence": dict(row.evidence),
                }
                for row in sorted(self.interruptions.values(), key=lambda item: item.action_interruption_id)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "ActionInterruptionProvenanceLedger":
        if snapshot.get("schema") != ACTION_INTERRUPTION_SCHEMA:
            raise ValueError("unsupported action interruption provenance schema")
        ledger = cls()
        for raw in snapshot.get("interruptions", []):
            if not isinstance(raw, Mapping):
                raise ValueError("action interruption row must be a mapping")
            interruption_id = str(raw["action_interruption_id"])
            if interruption_id in ledger.interruptions:
                raise ValueError("duplicate action interruption provenance")
            record = ActionInterruptionRecord(
                action_interruption_id=interruption_id,
                action_start_id=str(raw["action_start_id"]),
                selection_id=str(raw["selection_id"]),
                agent_id=str(raw["agent_id"]),
                intent_id=str(raw["intent_id"]),
                interrupted_minute=int(raw["interrupted_minute"]),
                kind=ActionInterruptionKind(str(raw["kind"])),
                target_ref=None if raw.get("target_ref") is None else str(raw["target_ref"]),
                evidence=dict(raw.get("evidence", {})),
            )
            ledger.validate_record(record)
            ledger.interruptions[interruption_id] = record
        return ledger
