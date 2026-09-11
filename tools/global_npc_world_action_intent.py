from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_ai import Handoff
from tools.global_npc_world_event_coordinator import CoordinatedDecision


SCHEMA_VERSION = "OUROS_WORLD_ACTION_INTENT_LEDGER_V1"


@dataclass(frozen=True)
class WorldActionIntentRecord:
    action_id: str
    agent_id: str
    intent_id: str
    intent_kind: str
    target_ref: str | None
    semantic_minute: int
    trigger_ids: tuple[str, ...]
    reason_codes: tuple[str, ...]
    source_type: str
    source_ref: str | None
    status: str = "PLANNED"


class WorldActionIntentLedger:
    """Durable boundary between a replan decision and later world execution.

    The ledger records what one world agent selected. It does not perform the
    action, mutate another agent, schedule communication, grant permissions,
    or resolve PTU mechanics.
    """

    def __init__(self) -> None:
        self.records: dict[str, WorldActionIntentRecord] = {}

    def record_from_replan(
        self,
        *,
        action_id: str,
        coordinated_decision: CoordinatedDecision,
        semantic_minute: int,
    ) -> WorldActionIntentRecord:
        if not action_id:
            raise ValueError("action_id is required")
        if semantic_minute < 0:
            raise ValueError("semantic_minute must be non-negative")
        if not coordinated_decision.trigger_ids:
            raise ValueError("a world action intent requires at least one replan trigger")

        agenda = coordinated_decision.decision
        decision = agenda.decision
        if coordinated_decision.agent_id != decision.agent_id:
            raise ValueError("coordinated decision agent identity mismatch")
        if decision.intent_id is None:
            raise ValueError("a world action intent requires a selected intent")
        if decision.handoff != Handoff.NONE:
            raise ValueError("AutoPTU handoff decisions are not ordinary world action intents")
        if decision.kind in {"IDLE", "NO_ELIGIBLE_INTENT", "HOLD_AUTOPTU"}:
            raise ValueError("non-action decisions cannot become world action intents")

        record = WorldActionIntentRecord(
            action_id=action_id,
            agent_id=coordinated_decision.agent_id,
            intent_id=decision.intent_id,
            intent_kind=decision.kind,
            target_ref=decision.target_ref,
            semantic_minute=semantic_minute,
            trigger_ids=tuple(coordinated_decision.trigger_ids),
            reason_codes=tuple(coordinated_decision.reasons),
            source_type=agenda.source_type,
            source_ref=agenda.source_ref,
        )

        existing = self.records.get(action_id)
        if existing is not None:
            if existing != record:
                raise ValueError("world action intent id reused with conflicting content")
            return existing

        self.records[action_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [
                {
                    **asdict(record),
                    "trigger_ids": list(record.trigger_ids),
                    "reason_codes": list(record.reason_codes),
                }
                for _, record in sorted(self.records.items())
            ],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "WorldActionIntentLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported world action intent ledger schema")

        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("world action intent snapshot records must be a list")

        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("world action intent snapshot row must be an object")
            record = WorldActionIntentRecord(
                action_id=str(raw["action_id"]),
                agent_id=str(raw["agent_id"]),
                intent_id=str(raw["intent_id"]),
                intent_kind=str(raw["intent_kind"]),
                target_ref=None if raw.get("target_ref") is None else str(raw["target_ref"]),
                semantic_minute=int(raw["semantic_minute"]),
                trigger_ids=tuple(str(value) for value in raw.get("trigger_ids", [])),
                reason_codes=tuple(str(value) for value in raw.get("reason_codes", [])),
                source_type=str(raw["source_type"]),
                source_ref=None if raw.get("source_ref") is None else str(raw["source_ref"]),
                status=str(raw.get("status", "PLANNED")),
            )
            if not record.action_id or not record.intent_id or not record.trigger_ids:
                raise ValueError("invalid world action intent snapshot row")
            existing = ledger.records.get(record.action_id)
            if existing is not None and existing != record:
                raise ValueError("conflicting duplicate world action intent in snapshot")
            ledger.records[record.action_id] = record
        return ledger
