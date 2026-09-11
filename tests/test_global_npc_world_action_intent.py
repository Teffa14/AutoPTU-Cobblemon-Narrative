import pytest

from tools.global_npc_ai import AgendaDecision, Decision, Handoff
from tools.global_npc_world_action_intent import (
    SCHEMA_VERSION,
    WorldActionIntentLedger,
)
from tools.global_npc_world_event_coordinator import CoordinatedDecision


def _coordinated(
    *,
    agent_id: str = "ouros.npc.mara_veyra",
    intent_id: str | None = "intent:request-specialist",
    kind: str = "REQUEST_ASSISTANCE",
    handoff: Handoff = Handoff.NONE,
    target_ref: str | None = "ouros.npc.teo_lark",
    trigger_ids: tuple[str, ...] = ("trigger:warning-delivered",),
) -> CoordinatedDecision:
    agenda = AgendaDecision(
        decision=Decision(
            agent_id=agent_id,
            intent_id=intent_id,
            kind=kind,
            score=420 if intent_id is not None else None,
            handoff=handoff,
            target_ref=target_ref,
        ),
        source_type="SITUATIONAL_INTENT",
        source_ref=intent_id,
    )
    return CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=trigger_ids,
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=agenda,
    )


def test_records_one_selected_world_action_without_mutating_target_actor() -> None:
    ledger = WorldActionIntentLedger()

    record = ledger.record_from_replan(
        action_id="action:request-teo-001",
        coordinated_decision=_coordinated(),
        semantic_minute=615,
    )

    assert record.agent_id == "ouros.npc.mara_veyra"
    assert record.intent_kind == "REQUEST_ASSISTANCE"
    assert record.target_ref == "ouros.npc.teo_lark"
    assert record.status == "PLANNED"
    assert record.trigger_ids == ("trigger:warning-delivered",)
    assert set(ledger.records) == {"action:request-teo-001"}


def test_exact_replay_is_idempotent_but_conflicting_reuse_fails_closed() -> None:
    ledger = WorldActionIntentLedger()
    first = ledger.record_from_replan(
        action_id="action:request-teo-001",
        coordinated_decision=_coordinated(),
        semantic_minute=615,
    )
    replay = ledger.record_from_replan(
        action_id="action:request-teo-001",
        coordinated_decision=_coordinated(),
        semantic_minute=615,
    )

    assert replay is first

    with pytest.raises(ValueError, match="conflicting content"):
        ledger.record_from_replan(
            action_id="action:request-teo-001",
            coordinated_decision=_coordinated(target_ref="ouros.npc.oren_vale"),
            semantic_minute=615,
        )


def test_auto_ptu_handoff_and_non_action_decisions_do_not_enter_world_action_ledger() -> None:
    ledger = WorldActionIntentLedger()

    with pytest.raises(ValueError, match="AutoPTU handoff"):
        ledger.record_from_replan(
            action_id="action:battle-001",
            coordinated_decision=_coordinated(
                kind="CONTEST_ROUTE_BLOCKER",
                handoff=Handoff.REQUEST_AUTOPTU,
            ),
            semantic_minute=615,
        )

    with pytest.raises(ValueError, match="selected intent"):
        ledger.record_from_replan(
            action_id="action:idle-001",
            coordinated_decision=_coordinated(intent_id=None, kind="IDLE", target_ref=None),
            semantic_minute=615,
        )


def test_replan_trigger_and_agent_identity_are_required() -> None:
    ledger = WorldActionIntentLedger()

    with pytest.raises(ValueError, match="at least one replan trigger"):
        ledger.record_from_replan(
            action_id="action:no-trigger",
            coordinated_decision=_coordinated(trigger_ids=()),
            semantic_minute=615,
        )

    mismatched = _coordinated()
    mismatched = CoordinatedDecision(
        agent_id="ouros.npc.nerea_sol",
        trigger_ids=mismatched.trigger_ids,
        reasons=mismatched.reasons,
        decision=mismatched.decision,
    )
    with pytest.raises(ValueError, match="agent identity mismatch"):
        ledger.record_from_replan(
            action_id="action:mismatch",
            coordinated_decision=mismatched,
            semantic_minute=615,
        )


def test_snapshot_round_trip_preserves_causal_record() -> None:
    ledger = WorldActionIntentLedger()
    original = ledger.record_from_replan(
        action_id="action:request-teo-001",
        coordinated_decision=_coordinated(),
        semantic_minute=615,
    )

    payload = ledger.snapshot()
    assert payload["schema_version"] == SCHEMA_VERSION

    restored = WorldActionIntentLedger.from_snapshot(payload)
    assert restored.records[original.action_id] == original


def test_unknown_schema_fails_closed() -> None:
    with pytest.raises(ValueError, match="unsupported"):
        WorldActionIntentLedger.from_snapshot({"schema_version": "UNKNOWN", "records": []})
