from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger
from tools.global_npc_world_action_intent import WorldActionIntentLedger


SCHEMA_VERSION = "OUROS_ASSISTANCE_DEFERRAL_LEDGER_V1"
REQUEST_KIND = "REQUEST_ASSISTANCE"
DEFER_KIND = "DEFER_ASSISTANCE_REQUEST"


@dataclass(frozen=True)
class AssistanceDeferralRecord:
    deferral_id: str
    request_action_id: str
    response_action_id: str
    requester_id: str
    responder_id: str
    reconsider_minute: int
    expires_minute: int | None
    priority: int
    trigger_id: str
    provenance_root: str


class AssistanceDeferralLedger:
    def __init__(self) -> None:
        self.records: dict[str, AssistanceDeferralRecord] = {}

    def add(self, record: AssistanceDeferralRecord) -> AssistanceDeferralRecord:
        existing = self.records.get(record.deferral_id)
        if existing is not None:
            if existing != record:
                raise ValueError("assistance deferral id reused with conflicting content")
            return existing
        self.records[record.deferral_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceDeferralLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance deferral ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance deferral snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance deferral snapshot row must be an object")
            expires_raw = raw.get("expires_minute")
            record = AssistanceDeferralRecord(
                deferral_id=str(raw["deferral_id"]),
                request_action_id=str(raw["request_action_id"]),
                response_action_id=str(raw["response_action_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                reconsider_minute=int(raw["reconsider_minute"]),
                expires_minute=None if expires_raw is None else int(expires_raw),
                priority=int(raw["priority"]),
                trigger_id=str(raw["trigger_id"]),
                provenance_root=str(raw["provenance_root"]),
            )
            if not record.deferral_id or not record.trigger_id or not record.provenance_root:
                raise ValueError("invalid assistance deferral snapshot row")
            if record.reconsider_minute < 0 or record.priority < 0:
                raise ValueError("invalid assistance deferral snapshot time/priority")
            if record.expires_minute is not None and record.expires_minute < record.reconsider_minute:
                raise ValueError("assistance deferral expiry precedes reconsideration")
            ledger.add(record)
        return ledger


def deferral_window_state(record: AssistanceDeferralRecord, semantic_minute: int) -> str:
    if semantic_minute < record.reconsider_minute:
        return "WAITING"
    if record.expires_minute is not None and semantic_minute > record.expires_minute:
        return "EXPIRED"
    return "OPEN"


def schedule_assistance_deferral(
    *,
    action_ledger: WorldActionIntentLedger,
    deferral_ledger: AssistanceDeferralLedger,
    replan_queue: NpcReplanQueue,
    request_action_id: str,
    response_action_id: str,
    deferral_id: str,
    request_delivery_trigger_id: str,
    reconsider_minute: int,
    expires_minute: int | None = None,
    priority: int = 5,
) -> AssistanceDeferralRecord:
    """Persist a DEFER decision and schedule one future reconsideration wake-up.

    This owner does not accept assistance, create a commitment, move the NPC,
    reserve a route/resource, message another actor, or resolve PTU mechanics.
    """
    if not deferral_id or not request_delivery_trigger_id:
        raise ValueError("deferral_id and request_delivery_trigger_id are required")
    if min(reconsider_minute, priority) < 0:
        raise ValueError("deferral time/priority values must be non-negative")
    if expires_minute is not None and expires_minute < reconsider_minute:
        raise ValueError("deferral expires_minute cannot precede reconsider_minute")

    request = action_ledger.records.get(request_action_id)
    if request is None:
        raise KeyError(f"unknown assistance request action: {request_action_id}")
    if request.status != "PLANNED" or request.intent_kind != REQUEST_KIND:
        raise ValueError("referenced action is not a PLANNED assistance request")
    if not request.target_ref or request.target_ref == request.agent_id:
        raise ValueError("assistance request requires another explicit recipient")

    response = action_ledger.records.get(response_action_id)
    if response is None:
        raise KeyError(f"unknown assistance response action: {response_action_id}")
    if response.status != "PLANNED" or response.intent_kind != DEFER_KIND:
        raise ValueError("only DEFER_ASSISTANCE_REQUEST can create a deferral")
    if response.agent_id != request.target_ref or response.target_ref != request.agent_id:
        raise ValueError("assistance deferral actor binding mismatch")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError("assistance deferral cannot predate its request")
    if reconsider_minute <= response.semantic_minute:
        raise ValueError("assistance deferral reconsideration must be in the future")
    if request_delivery_trigger_id not in response.trigger_ids:
        raise ValueError("assistance deferral lacks the request-delivery replan trigger")
    if not request_delivery_trigger_id.startswith("replan:information:"):
        raise ValueError("assistance deferral trigger must derive from information delivery")

    trigger_id = f"replan:assistance-deferral:{deferral_id}"
    record = AssistanceDeferralRecord(
        deferral_id=deferral_id,
        request_action_id=request.action_id,
        response_action_id=response.action_id,
        requester_id=request.agent_id,
        responder_id=response.agent_id,
        reconsider_minute=reconsider_minute,
        expires_minute=expires_minute,
        priority=priority,
        trigger_id=trigger_id,
        provenance_root=response.action_id,
    )
    record = deferral_ledger.add(record)

    if trigger_id not in replan_queue.known_trigger_ids:
        replan_queue.schedule(
            ReplanTrigger(
                trigger_id=trigger_id,
                agent_id=response.agent_id,
                reason=ReplanReason.SCHEDULE_DUE,
                due_minute=reconsider_minute,
                source_ref=response.action_id,
                priority=priority,
            )
        )
    return record
