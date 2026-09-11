from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_world_action_intent import WorldActionIntentLedger


SCHEMA_VERSION = "OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1"
REQUEST_KIND = "REQUEST_ASSISTANCE"
COUNTERPROPOSE_KIND = "COUNTERPROPOSE_ASSISTANCE_REQUEST"


@dataclass(frozen=True)
class AssistanceCounterproposalRecord:
    proposal_id: str
    request_action_id: str
    response_action_id: str
    requester_id: str
    responder_id: str
    proposed_start_minute: int | None
    proposed_end_minute: int | None
    location_ref: str | None
    scope_ref: str | None
    alternative_ref: str | None
    expires_minute: int | None
    provenance_root: str


class AssistanceCounterproposalLedger:
    """Durable structured terms for one assistance counterproposal.

    The ledger records what the responder proposed. It does not accept those
    terms, create a commitment, reserve time, move either actor, allocate a
    route/resource, mutate relationships, or resolve PTU mechanics.
    """

    def __init__(self) -> None:
        self.records: dict[str, AssistanceCounterproposalRecord] = {}

    def add(self, record: AssistanceCounterproposalRecord) -> AssistanceCounterproposalRecord:
        existing = self.records.get(record.proposal_id)
        if existing is not None:
            if existing != record:
                raise ValueError("assistance counterproposal id reused with conflicting content")
            return existing
        self.records[record.proposal_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceCounterproposalLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance counterproposal ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance counterproposal snapshot records must be a list")

        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance counterproposal snapshot row must be an object")
            record = AssistanceCounterproposalRecord(
                proposal_id=str(raw["proposal_id"]),
                request_action_id=str(raw["request_action_id"]),
                response_action_id=str(raw["response_action_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                proposed_start_minute=None if raw.get("proposed_start_minute") is None else int(raw["proposed_start_minute"]),
                proposed_end_minute=None if raw.get("proposed_end_minute") is None else int(raw["proposed_end_minute"]),
                location_ref=None if raw.get("location_ref") is None else str(raw["location_ref"]),
                scope_ref=None if raw.get("scope_ref") is None else str(raw["scope_ref"]),
                alternative_ref=None if raw.get("alternative_ref") is None else str(raw["alternative_ref"]),
                expires_minute=None if raw.get("expires_minute") is None else int(raw["expires_minute"]),
                provenance_root=str(raw["provenance_root"]),
            )
            _validate_record_shape(record)
            ledger.add(record)
        return ledger


def _clean_optional_ref(value: str | None, name: str) -> str | None:
    if value is None:
        return None
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{name} cannot be blank")
    return cleaned


def _validate_record_shape(record: AssistanceCounterproposalRecord) -> None:
    if not record.proposal_id or not record.request_action_id or not record.response_action_id:
        raise ValueError("invalid assistance counterproposal identity")
    if not record.requester_id or not record.responder_id or not record.provenance_root:
        raise ValueError("invalid assistance counterproposal actor/provenance identity")
    if record.provenance_root != record.response_action_id:
        raise ValueError("assistance counterproposal provenance must match response action")
    if record.requester_id == record.responder_id:
        raise ValueError("assistance counterproposal requires two distinct actors")
    for value, name in (
        (record.location_ref, "location_ref"),
        (record.scope_ref, "scope_ref"),
        (record.alternative_ref, "alternative_ref"),
    ):
        if value is not None and not value.strip():
            raise ValueError(f"{name} cannot be blank")
    if record.proposed_start_minute is not None and record.proposed_start_minute < 0:
        raise ValueError("proposed_start_minute must be non-negative")
    if record.proposed_end_minute is not None:
        if record.proposed_start_minute is None:
            raise ValueError("proposed_end_minute requires proposed_start_minute")
        if record.proposed_end_minute < record.proposed_start_minute:
            raise ValueError("proposed_end_minute cannot precede proposed_start_minute")
    if record.expires_minute is not None and record.expires_minute < 0:
        raise ValueError("expires_minute must be non-negative")
    if not any(
        value is not None
        for value in (
            record.proposed_start_minute,
            record.location_ref,
            record.scope_ref,
            record.alternative_ref,
        )
    ):
        raise ValueError("assistance counterproposal requires at least one concrete term")


def record_assistance_counterproposal_terms(
    *,
    action_ledger: WorldActionIntentLedger,
    proposal_ledger: AssistanceCounterproposalLedger,
    request_action_id: str,
    response_action_id: str,
    proposal_id: str,
    request_delivery_trigger_id: str,
    proposed_start_minute: int | None = None,
    proposed_end_minute: int | None = None,
    location_ref: str | None = None,
    scope_ref: str | None = None,
    alternative_ref: str | None = None,
    expires_minute: int | None = None,
) -> AssistanceCounterproposalRecord:
    """Persist concrete responder-authored terms without accepting or executing them."""

    if not proposal_id or not request_delivery_trigger_id:
        raise ValueError("proposal_id and request_delivery_trigger_id are required")

    location_ref = _clean_optional_ref(location_ref, "location_ref")
    scope_ref = _clean_optional_ref(scope_ref, "scope_ref")
    alternative_ref = _clean_optional_ref(alternative_ref, "alternative_ref")

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
    if response.status != "PLANNED" or response.intent_kind != COUNTERPROPOSE_KIND:
        raise ValueError("only COUNTERPROPOSE_ASSISTANCE_REQUEST can own counterproposal terms")
    if response.agent_id != request.target_ref or response.target_ref != request.agent_id:
        raise ValueError("assistance counterproposal actor binding mismatch")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError("assistance counterproposal cannot predate its request")
    if request_delivery_trigger_id not in response.trigger_ids:
        raise ValueError("assistance counterproposal lacks the request-delivery replan trigger")
    if not request_delivery_trigger_id.startswith("replan:information:"):
        raise ValueError("assistance counterproposal trigger must derive from information delivery")

    if proposed_start_minute is not None and proposed_start_minute < response.semantic_minute:
        raise ValueError("assistance counterproposal cannot propose a start in the past")
    if expires_minute is not None and expires_minute < response.semantic_minute:
        raise ValueError("assistance counterproposal cannot already be expired when authored")

    record = AssistanceCounterproposalRecord(
        proposal_id=proposal_id,
        request_action_id=request.action_id,
        response_action_id=response.action_id,
        requester_id=request.agent_id,
        responder_id=response.agent_id,
        proposed_start_minute=proposed_start_minute,
        proposed_end_minute=proposed_end_minute,
        location_ref=location_ref,
        scope_ref=scope_ref,
        alternative_ref=alternative_ref,
        expires_minute=expires_minute,
        provenance_root=response.action_id,
    )
    _validate_record_shape(record)
    return proposal_ledger.add(record)
