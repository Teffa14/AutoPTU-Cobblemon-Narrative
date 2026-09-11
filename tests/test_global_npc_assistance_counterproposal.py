from __future__ import annotations

import pytest

from tools.global_npc_assistance_counterproposal import (
    AssistanceCounterproposalLedger,
    record_assistance_counterproposal_terms,
)
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord


REQUEST = "action:request"
RESPONSE = "action:counterproposal"
DELIVERY_TRIGGER = "replan:information:event:request"
MARA = "npc:mara"
TEO = "npc:teo"


def _actions(*, response_kind: str = "COUNTERPROPOSE_ASSISTANCE_REQUEST", responder: str = TEO, target: str = MARA) -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    ledger.records[REQUEST] = WorldActionIntentRecord(
        action_id=REQUEST,
        agent_id=MARA,
        intent_id="intent:ask-teo",
        intent_kind="REQUEST_ASSISTANCE",
        target_ref=TEO,
        semantic_minute=100,
        trigger_ids=("replan:information:event:warning",),
        reason_codes=("KNOWLEDGE_DELIVERED",),
        source_type="SITUATIONAL",
        source_ref="warning",
    )
    ledger.records[RESPONSE] = WorldActionIntentRecord(
        action_id=RESPONSE,
        agent_id=responder,
        intent_id="intent:counter-mara",
        intent_kind=response_kind,
        target_ref=target,
        semantic_minute=120,
        trigger_ids=(DELIVERY_TRIGGER,),
        reason_codes=("KNOWLEDGE_DELIVERED",),
        source_type="SITUATIONAL",
        source_ref=REQUEST,
    )
    return ledger


def _record(*, actions: WorldActionIntentLedger | None = None, ledger: AssistanceCounterproposalLedger | None = None, **overrides):
    actions = actions or _actions()
    ledger = ledger or AssistanceCounterproposalLedger()
    values = dict(
        action_ledger=actions,
        proposal_ledger=ledger,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        proposal_id="proposal:teo:mara:1",
        request_delivery_trigger_id=DELIVERY_TRIGGER,
        proposed_start_minute=180,
        proposed_end_minute=210,
        location_ref="location:repair-row",
        scope_ref="scope:inspect-only",
        alternative_ref=None,
        expires_minute=150,
    )
    values.update(overrides)
    return record_assistance_counterproposal_terms(**values), ledger


def test_counterproposal_persists_concrete_terms_without_creating_commitment() -> None:
    record, ledger = _record()
    assert record.requester_id == MARA
    assert record.responder_id == TEO
    assert record.proposed_start_minute == 180
    assert record.proposed_end_minute == 210
    assert record.location_ref == "location:repair-row"
    assert record.scope_ref == "scope:inspect-only"
    assert record.expires_minute == 150
    assert record.provenance_root == RESPONSE
    assert set(ledger.records) == {record.proposal_id}


def test_counterproposal_can_offer_an_alternative_without_time_or_place() -> None:
    record, _ = _record(
        proposed_start_minute=None,
        proposed_end_minute=None,
        location_ref=None,
        scope_ref=None,
        alternative_ref="alternative:ask-nerea-for-remote-check",
        expires_minute=None,
    )
    assert record.alternative_ref == "alternative:ask-nerea-for-remote-check"


def test_replay_is_idempotent_and_conflicting_reuse_fails_closed() -> None:
    record, ledger = _record()
    replay, _ = _record(ledger=ledger)
    assert replay == record

    with pytest.raises(ValueError, match="conflicting content"):
        _record(ledger=ledger, scope_ref="scope:full-repair")


def test_snapshot_restore_preserves_terms_and_provenance() -> None:
    record, ledger = _record()
    restored = AssistanceCounterproposalLedger.from_snapshot(ledger.snapshot())
    assert restored.records[record.proposal_id] == record
    assert restored.records[record.proposal_id].provenance_root == RESPONSE


def test_only_counterproposal_with_original_delivery_trigger_can_own_terms() -> None:
    with pytest.raises(ValueError, match="only COUNTERPROPOSE_ASSISTANCE_REQUEST"):
        _record(actions=_actions(response_kind="ACCEPT_ASSISTANCE_REQUEST"))

    with pytest.raises(ValueError, match="request-delivery replan trigger"):
        _record(request_delivery_trigger_id="replan:information:event:other")

    with pytest.raises(ValueError, match="actor binding"):
        _record(actions=_actions(responder="npc:oren"))


def test_counterproposal_requires_at_least_one_concrete_term() -> None:
    with pytest.raises(ValueError, match="at least one concrete term"):
        _record(
            proposed_start_minute=None,
            proposed_end_minute=None,
            location_ref=None,
            scope_ref=None,
            alternative_ref=None,
            expires_minute=None,
        )


def test_counterproposal_rejects_invalid_time_shapes() -> None:
    with pytest.raises(ValueError, match="requires proposed_start_minute"):
        _record(proposed_start_minute=None, proposed_end_minute=200)
    with pytest.raises(ValueError, match="cannot precede proposed_start_minute"):
        _record(proposed_start_minute=200, proposed_end_minute=199)
    with pytest.raises(ValueError, match="start in the past"):
        _record(proposed_start_minute=119, proposed_end_minute=140)
    with pytest.raises(ValueError, match="already be expired"):
        _record(expires_minute=119)


def test_optional_refs_cannot_be_blank() -> None:
    with pytest.raises(ValueError, match="location_ref cannot be blank"):
        _record(location_ref="  ")
