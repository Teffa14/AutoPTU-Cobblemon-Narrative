from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
import hashlib
import json
from typing import Iterable, Mapping


AUTOPTU_SESSION_CHECKPOINT_SCHEMA = "OUROS_AUTOPTU_SESSION_CHECKPOINT_V1"


class AutoPTUSessionState(str, Enum):
    REQUESTED = "REQUESTED"
    ENGINE_BOUND = "ENGINE_BOUND"
    RESULT_RECORDED = "RESULT_RECORDED"
    RETIRED = "RETIRED"
    QUARANTINED = "QUARANTINED"


@dataclass(frozen=True)
class AutoPTUSessionBinding:
    session_id: str
    handoff_request_id: str
    world_action_ref: str
    participant_refs: tuple[str, ...]
    rules_profile_id: str
    requested_at_minute: int
    state: AutoPTUSessionState = AutoPTUSessionState.REQUESTED
    engine_session_ref: str | None = None
    authoritative_result_ref: str | None = None


def _required(value: str, field: str) -> str:
    cleaned = str(value).strip()
    if not cleaned:
        raise ValueError(f"{field} is required")
    return cleaned


def _canonical_participants(values: Iterable[str]) -> tuple[str, ...]:
    participants = tuple(sorted({_required(value, "participant_ref") for value in values}))
    if not participants:
        raise ValueError("at least one participant_ref is required")
    return participants


def deterministic_session_id(
    *,
    handoff_request_id: str,
    world_action_ref: str,
    participant_refs: Iterable[str],
    rules_profile_id: str,
    requested_at_minute: int,
) -> str:
    if requested_at_minute < 0:
        raise ValueError("requested_at_minute cannot be negative")
    payload = {
        "schema": "OUROS_AUTOPTU_SESSION_ID_V1",
        "handoff_request_id": _required(handoff_request_id, "handoff_request_id"),
        "world_action_ref": _required(world_action_ref, "world_action_ref"),
        "participant_refs": list(_canonical_participants(participant_refs)),
        "rules_profile_id": _required(rules_profile_id, "rules_profile_id"),
        "requested_at_minute": requested_at_minute,
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return f"autoptu.session.{digest[:32]}"


def build_session_binding(
    *,
    handoff_request_id: str,
    world_action_ref: str,
    participant_refs: Iterable[str],
    rules_profile_id: str,
    requested_at_minute: int,
) -> AutoPTUSessionBinding:
    participants = _canonical_participants(participant_refs)
    session_id = deterministic_session_id(
        handoff_request_id=handoff_request_id,
        world_action_ref=world_action_ref,
        participant_refs=participants,
        rules_profile_id=rules_profile_id,
        requested_at_minute=requested_at_minute,
    )
    return AutoPTUSessionBinding(
        session_id=session_id,
        handoff_request_id=_required(handoff_request_id, "handoff_request_id"),
        world_action_ref=_required(world_action_ref, "world_action_ref"),
        participant_refs=participants,
        rules_profile_id=_required(rules_profile_id, "rules_profile_id"),
        requested_at_minute=requested_at_minute,
    )


class AutoPTUSessionLedger:
    def __init__(self, bindings: Iterable[AutoPTUSessionBinding] = ()) -> None:
        self._bindings: dict[str, AutoPTUSessionBinding] = {}
        self._request_to_session: dict[str, str] = {}
        for binding in bindings:
            self._insert_restored(binding)

    def _insert_restored(self, binding: AutoPTUSessionBinding) -> None:
        if binding.session_id in self._bindings:
            raise ValueError(f"duplicate AutoPTU session_id: {binding.session_id}")
        if binding.handoff_request_id in self._request_to_session:
            raise ValueError(f"duplicate AutoPTU handoff_request_id: {binding.handoff_request_id}")
        expected = build_session_binding(
            handoff_request_id=binding.handoff_request_id,
            world_action_ref=binding.world_action_ref,
            participant_refs=binding.participant_refs,
            rules_profile_id=binding.rules_profile_id,
            requested_at_minute=binding.requested_at_minute,
        ).session_id
        if expected != binding.session_id:
            raise ValueError("AutoPTU session identity does not match immutable handoff inputs")
        self._bindings[binding.session_id] = binding
        self._request_to_session[binding.handoff_request_id] = binding.session_id

    def request_session(
        self,
        *,
        handoff_request_id: str,
        world_action_ref: str,
        participant_refs: Iterable[str],
        rules_profile_id: str,
        requested_at_minute: int,
    ) -> AutoPTUSessionBinding:
        proposed = build_session_binding(
            handoff_request_id=handoff_request_id,
            world_action_ref=world_action_ref,
            participant_refs=participant_refs,
            rules_profile_id=rules_profile_id,
            requested_at_minute=requested_at_minute,
        )
        existing_id = self._request_to_session.get(proposed.handoff_request_id)
        if existing_id is not None:
            existing = self._bindings[existing_id]
            if existing.session_id != proposed.session_id:
                raise ValueError("handoff request already belongs to a different AutoPTU session identity")
            return existing
        self._bindings[proposed.session_id] = proposed
        self._request_to_session[proposed.handoff_request_id] = proposed.session_id
        return proposed

    def get(self, session_id: str) -> AutoPTUSessionBinding:
        try:
            return self._bindings[session_id]
        except KeyError as exc:
            raise ValueError(f"unknown AutoPTU session_id: {session_id}") from exc

    def bindings(self) -> tuple[AutoPTUSessionBinding, ...]:
        return tuple(self._bindings[key] for key in sorted(self._bindings))

    def bind_engine_session(self, session_id: str, *, engine_session_ref: str) -> AutoPTUSessionBinding:
        current = self.get(session_id)
        engine_ref = _required(engine_session_ref, "engine_session_ref")
        if current.state == AutoPTUSessionState.ENGINE_BOUND:
            if current.engine_session_ref != engine_ref:
                raise ValueError("AutoPTU session already bound to a different engine session")
            return current
        if current.state != AutoPTUSessionState.REQUESTED:
            raise ValueError(f"cannot bind engine session from state {current.state.value}")
        updated = replace(current, state=AutoPTUSessionState.ENGINE_BOUND, engine_session_ref=engine_ref)
        self._bindings[session_id] = updated
        return updated

    def record_authoritative_result(self, session_id: str, *, result_ref: str) -> AutoPTUSessionBinding:
        current = self.get(session_id)
        result = _required(result_ref, "result_ref")
        if current.state == AutoPTUSessionState.RESULT_RECORDED:
            if current.authoritative_result_ref != result:
                raise ValueError("AutoPTU session already records a different authoritative result")
            return current
        if current.state != AutoPTUSessionState.ENGINE_BOUND:
            raise ValueError("authoritative result requires an explicitly engine-bound session")
        updated = replace(
            current,
            state=AutoPTUSessionState.RESULT_RECORDED,
            authoritative_result_ref=result,
        )
        self._bindings[session_id] = updated
        return updated

    def retire(self, session_id: str) -> AutoPTUSessionBinding:
        current = self.get(session_id)
        if current.state == AutoPTUSessionState.RETIRED:
            return current
        if current.state != AutoPTUSessionState.RESULT_RECORDED:
            raise ValueError("session cannot retire before an authoritative result is recorded")
        updated = replace(current, state=AutoPTUSessionState.RETIRED)
        self._bindings[session_id] = updated
        return updated

    def quarantine(self, session_id: str) -> AutoPTUSessionBinding:
        current = self.get(session_id)
        if current.state == AutoPTUSessionState.RETIRED:
            raise ValueError("retired AutoPTU session cannot be reactivated or quarantined")
        if current.state == AutoPTUSessionState.QUARANTINED:
            return current
        updated = replace(current, state=AutoPTUSessionState.QUARANTINED)
        self._bindings[session_id] = updated
        return updated


def _binding_to_dict(binding: AutoPTUSessionBinding) -> dict[str, object]:
    return {
        "session_id": binding.session_id,
        "handoff_request_id": binding.handoff_request_id,
        "world_action_ref": binding.world_action_ref,
        "participant_refs": list(binding.participant_refs),
        "rules_profile_id": binding.rules_profile_id,
        "requested_at_minute": binding.requested_at_minute,
        "state": binding.state.value,
        "engine_session_ref": binding.engine_session_ref,
        "authoritative_result_ref": binding.authoritative_result_ref,
    }


def snapshot_autoptu_sessions(ledger: AutoPTUSessionLedger, *, semantic_minute: int) -> dict[str, object]:
    if semantic_minute < 0:
        raise ValueError("semantic_minute cannot be negative")
    bindings = ledger.bindings()
    if any(binding.requested_at_minute > semantic_minute for binding in bindings):
        raise ValueError("AutoPTU session cannot be checkpointed before its request time")
    payload: dict[str, object] = {
        "schema": AUTOPTU_SESSION_CHECKPOINT_SCHEMA,
        "semantic_minute": semantic_minute,
        "sessions": [_binding_to_dict(binding) for binding in bindings],
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


def restore_autoptu_sessions(
    snapshot: Mapping[str, object], *, recovery_semantic_minute: int | None = None
) -> AutoPTUSessionLedger:
    if snapshot.get("schema") != AUTOPTU_SESSION_CHECKPOINT_SCHEMA:
        raise ValueError("unsupported AutoPTU session checkpoint schema")
    payload = {key: value for key, value in snapshot.items() if key != "sha256"}
    expected = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    if snapshot.get("sha256") != expected:
        raise ValueError("AutoPTU session checkpoint digest mismatch")
    semantic_minute = int(snapshot["semantic_minute"])
    if recovery_semantic_minute is not None and semantic_minute > recovery_semantic_minute:
        raise ValueError("AutoPTU session checkpoint is newer than recovery cut")

    raw_sessions = snapshot.get("sessions", [])
    if not isinstance(raw_sessions, list):
        raise ValueError("AutoPTU session checkpoint sessions must be a list")
    bindings: list[AutoPTUSessionBinding] = []
    for raw in raw_sessions:
        if not isinstance(raw, Mapping):
            raise ValueError("AutoPTU session checkpoint contains malformed session")
        binding = AutoPTUSessionBinding(
            session_id=str(raw["session_id"]),
            handoff_request_id=str(raw["handoff_request_id"]),
            world_action_ref=str(raw["world_action_ref"]),
            participant_refs=tuple(str(value) for value in raw.get("participant_refs", [])),
            rules_profile_id=str(raw["rules_profile_id"]),
            requested_at_minute=int(raw["requested_at_minute"]),
            state=AutoPTUSessionState(str(raw["state"])),
            engine_session_ref=None if raw.get("engine_session_ref") is None else str(raw["engine_session_ref"]),
            authoritative_result_ref=(
                None if raw.get("authoritative_result_ref") is None else str(raw["authoritative_result_ref"])
            ),
        )
        if binding.requested_at_minute > semantic_minute:
            raise ValueError("AutoPTU session request is newer than its checkpoint")
        if binding.state in {AutoPTUSessionState.ENGINE_BOUND, AutoPTUSessionState.RESULT_RECORDED, AutoPTUSessionState.RETIRED} and not binding.engine_session_ref:
            raise ValueError("engine-bound AutoPTU session state requires engine_session_ref")
        if binding.state in {AutoPTUSessionState.RESULT_RECORDED, AutoPTUSessionState.RETIRED} and not binding.authoritative_result_ref:
            raise ValueError("resolved AutoPTU session state requires authoritative_result_ref")
        bindings.append(binding)

    if [binding.session_id for binding in bindings] != sorted(binding.session_id for binding in bindings):
        raise ValueError("AutoPTU session checkpoint is not canonically ordered")
    return AutoPTUSessionLedger(bindings)
