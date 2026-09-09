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


ACTION_TERMINAL_SCHEMA = "OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1"


class ActionTerminalKind(str, Enum):
    TRAVEL_DESTINATION_ARRIVED = "TRAVEL_DESTINATION_ARRIVED"


@dataclass(frozen=True)
class ActionTerminalRecord:
    action_terminal_id: str
    action_start_id: str
    selection_id: str
    agent_id: str
    intent_id: str
    terminal_minute: int
    kind: ActionTerminalKind
    target_ref: str | None
    evidence: Mapping[str, object]


@dataclass
class ActionTerminalProvenanceLedger:
    terminals: dict[str, ActionTerminalRecord] = field(default_factory=dict)

    def _reserve_id(self, start: ActionStartRecord, kind: ActionTerminalKind) -> str:
        terminal_id = f"action-terminal:{start.action_start_id}:{kind.value}"
        if terminal_id in self.terminals:
            raise ValueError(f"action terminal already recorded: {terminal_id}")
        return terminal_id

    def record_travel_arrival(
        self,
        start: ActionStartRecord,
        *,
        semantic_minute: int,
    ) -> ActionTerminalRecord:
        if start.kind != ActionStartKind.TRAVEL_EDGE_STARTED:
            raise ValueError("travel arrival requires a travel action start")
        if semantic_minute < start.started_minute:
            raise ValueError("travel arrival cannot precede action start")

        raw_agent = start.evidence.get("agent_before")
        raw_started = start.evidence.get("travel_after")
        raw_edges = start.evidence.get("edges", [])
        if not isinstance(raw_agent, Mapping) or not isinstance(raw_started, Mapping):
            raise ValueError("source travel action-start evidence is incomplete")

        agent = agent_from_dict(raw_agent)
        started_state = _travel_state_from_dict(raw_started)
        edges = tuple(edge_from_dict(row) for row in raw_edges if isinstance(row, Mapping))
        arrived_state, decision = advance_travel(
            agent,
            started_state,
            edges,
            semantic_minute=semantic_minute,
        )
        if decision.kind != TravelDecisionKind.ARRIVED:
            raise ValueError("travel evidence does not prove destination arrival")
        if arrived_state.current_node != arrived_state.plan.destination_node:
            raise ValueError("travel arrival state is not at destination")

        terminal_id = self._reserve_id(start, ActionTerminalKind.TRAVEL_DESTINATION_ARRIVED)
        record = ActionTerminalRecord(
            action_terminal_id=terminal_id,
            action_start_id=start.action_start_id,
            selection_id=start.selection_id,
            agent_id=start.agent_id,
            intent_id=start.intent_id,
            terminal_minute=semantic_minute,
            kind=ActionTerminalKind.TRAVEL_DESTINATION_ARRIVED,
            target_ref=start.target_ref,
            evidence={
                "agent": _agent_snapshot(agent),
                "travel_started": _travel_state_snapshot(started_state),
                "edges": [_edge_snapshot(edge) for edge in edges],
                "decision_kind": decision.kind.value,
                "decision_edge_id": decision.edge_id,
                "travel_terminal": _travel_state_snapshot(arrived_state),
            },
        )
        self.validate_record(record)
        self.terminals[terminal_id] = record
        return record

    def validate_record(self, record: ActionTerminalRecord) -> None:
        if record.terminal_minute < 0:
            raise ValueError("action terminal semantic minute cannot be negative")
        if record.kind != ActionTerminalKind.TRAVEL_DESTINATION_ARRIVED:
            raise ValueError("unsupported action terminal kind")

        evidence = record.evidence
        raw_agent = evidence.get("agent")
        raw_started = evidence.get("travel_started")
        raw_terminal = evidence.get("travel_terminal")
        raw_edges = evidence.get("edges", [])
        if not isinstance(raw_agent, Mapping) or not isinstance(raw_started, Mapping) or not isinstance(raw_terminal, Mapping):
            raise ValueError("travel terminal evidence is incomplete")

        agent = agent_from_dict(raw_agent)
        started_state = _travel_state_from_dict(raw_started)
        expected_terminal = _travel_state_from_dict(raw_terminal)
        edges = tuple(edge_from_dict(row) for row in raw_edges if isinstance(row, Mapping))
        replayed_terminal, decision = advance_travel(
            agent,
            started_state,
            edges,
            semantic_minute=record.terminal_minute,
        )
        if decision.kind != TravelDecisionKind.ARRIVED:
            raise ValueError("travel terminal evidence no longer replays to arrival")
        if _travel_state_snapshot(replayed_terminal) != _travel_state_snapshot(expected_terminal):
            raise ValueError("travel terminal state no longer replays")
        if decision.edge_id != evidence.get("decision_edge_id"):
            raise ValueError("travel terminal edge provenance mismatch")
        if evidence.get("decision_kind") != TravelDecisionKind.ARRIVED.value:
            raise ValueError("travel terminal decision provenance mismatch")
        if agent.agent_id != record.agent_id or started_state.plan.agent_id != record.agent_id:
            raise ValueError("travel terminal agent provenance mismatch")
        if expected_terminal.current_node != expected_terminal.plan.destination_node:
            raise ValueError("travel terminal destination provenance mismatch")
        if expected_terminal.semantic_minute != record.terminal_minute:
            raise ValueError("travel terminal minute provenance mismatch")
        if started_state.edge_started_minute is None or record.terminal_minute < started_state.edge_started_minute:
            raise ValueError("travel terminal predates replayable departure")

    def validate_against_action_starts(
        self,
        starts: ActionStartProvenanceLedger,
        *,
        semantic_minute: int,
    ) -> None:
        seen_starts: set[str] = set()
        for record in self.terminals.values():
            self.validate_record(record)
            if record.terminal_minute > semantic_minute:
                raise ValueError(f"action terminal comes from the future: {record.action_terminal_id}")
            start = starts.starts.get(record.action_start_id)
            if start is None:
                raise ValueError(f"action terminal references missing action start: {record.action_terminal_id}")
            if start.kind != ActionStartKind.TRAVEL_EDGE_STARTED:
                raise ValueError(f"travel terminal lacks travel start provenance: {record.action_terminal_id}")
            if (
                record.selection_id != start.selection_id
                or record.agent_id != start.agent_id
                or record.intent_id != start.intent_id
                or record.target_ref != start.target_ref
            ):
                raise ValueError(f"action terminal start provenance mismatch: {record.action_terminal_id}")
            if record.terminal_minute < start.started_minute:
                raise ValueError(f"action terminal predates action start: {record.action_terminal_id}")
            if record.action_start_id in seen_starts:
                raise ValueError("duplicate terminal outcome for one action start")
            seen_starts.add(record.action_start_id)

            source_agent = start.evidence.get("agent_before")
            source_started = start.evidence.get("travel_after")
            source_edges = start.evidence.get("edges", [])
            if record.evidence.get("agent") != source_agent:
                raise ValueError(f"action terminal agent snapshot diverges from source start: {record.action_terminal_id}")
            if record.evidence.get("travel_started") != source_started:
                raise ValueError(f"action terminal travel snapshot diverges from source start: {record.action_terminal_id}")
            if record.evidence.get("edges") != source_edges:
                raise ValueError(f"action terminal route evidence diverges from source start: {record.action_terminal_id}")

    def snapshot(self) -> dict:
        return {
            "schema": ACTION_TERMINAL_SCHEMA,
            "terminals": [
                {
                    "action_terminal_id": row.action_terminal_id,
                    "action_start_id": row.action_start_id,
                    "selection_id": row.selection_id,
                    "agent_id": row.agent_id,
                    "intent_id": row.intent_id,
                    "terminal_minute": row.terminal_minute,
                    "kind": row.kind.value,
                    "target_ref": row.target_ref,
                    "evidence": dict(row.evidence),
                }
                for row in sorted(self.terminals.values(), key=lambda item: item.action_terminal_id)
            ],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "ActionTerminalProvenanceLedger":
        if snapshot.get("schema") != ACTION_TERMINAL_SCHEMA:
            raise ValueError("unsupported action terminal provenance schema")
        ledger = cls()
        for raw in snapshot.get("terminals", []):
            if not isinstance(raw, Mapping):
                raise ValueError("action terminal row must be a mapping")
            terminal_id = str(raw["action_terminal_id"])
            if terminal_id in ledger.terminals:
                raise ValueError("duplicate action terminal provenance")
            record = ActionTerminalRecord(
                action_terminal_id=terminal_id,
                action_start_id=str(raw["action_start_id"]),
                selection_id=str(raw["selection_id"]),
                agent_id=str(raw["agent_id"]),
                intent_id=str(raw["intent_id"]),
                terminal_minute=int(raw["terminal_minute"]),
                kind=ActionTerminalKind(str(raw["kind"])),
                target_ref=None if raw.get("target_ref") is None else str(raw["target_ref"]),
                evidence=dict(raw.get("evidence", {})),
            )
            ledger.validate_record(record)
            ledger.terminals[terminal_id] = record
        return ledger
