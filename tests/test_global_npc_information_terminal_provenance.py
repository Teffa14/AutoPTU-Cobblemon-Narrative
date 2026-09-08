from tools.global_npc_deception import DeceptionKind, DeceptiveStatement
from tools.global_npc_deception_runtime import DeceptionInformationEventQueue
from tools.global_npc_information_network import (
    CommunicationChannel,
    DeliveryStatus,
    InformationEventQueue,
)
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation


def _ordinary_queue(*, available: bool = True) -> InformationEventQueue:
    ledgers = {
        "npc:sender": KnowledgeLedger("npc:sender"),
        "npc:receiver": KnowledgeLedger("npc:receiver"),
    }
    record_direct_observation(
        ledgers["npc:sender"],
        claim_id="claim:source",
        subject="booking:status",
        value="displaced",
        semantic_minute=10,
        confidence=100,
    )
    return InformationEventQueue(
        channels={"channel:radio": CommunicationChannel("channel:radio", "RADIO", 5, available=available)},
        ledgers=ledgers,
    )


def _schedule(queue: InformationEventQueue, event_id: str = "event:notice") -> None:
    queue.schedule(
        event_id=event_id,
        message_id="message:notice",
        sender_id="npc:sender",
        receiver_id="npc:receiver",
        source_claim_id="claim:source",
        new_claim_id="claim:received",
        channel_id="channel:radio",
        created_minute=11,
    )


def test_delivered_envelope_provenance_survives_restart() -> None:
    queue = _ordinary_queue()
    _schedule(queue)
    queue.process_due(16)

    archived = queue.envelope_provenance("event:notice")
    assert archived is not None
    assert archived.sender_id == "npc:sender"
    assert archived.receiver_id == "npc:receiver"
    assert archived.message_id == "message:notice"
    assert queue.statuses["event:notice"] == DeliveryStatus.DELIVERED

    restored = InformationEventQueue.restore(queue.snapshot(), channels=queue.channels, ledgers=queue.ledgers)
    archived_after_restart = restored.envelope_provenance("event:notice")
    assert archived_after_restart == archived


def test_terminal_channel_failure_keeps_address_provenance_without_faking_delivery() -> None:
    queue = _ordinary_queue(available=False)
    _schedule(queue)
    queue.process_due(16)

    archived = queue.envelope_provenance("event:notice")
    assert archived is not None
    assert archived.receiver_id == "npc:receiver"
    assert queue.statuses["event:notice"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE
    assert "event:notice" not in queue.delivered_event_ids
    assert "claim:received" not in queue.ledgers["npc:receiver"].claims


def test_deceptive_delivery_preserves_transport_envelope_across_restart() -> None:
    ledgers = {
        "npc:speaker": KnowledgeLedger("npc:speaker"),
        "npc:receiver": KnowledgeLedger("npc:receiver"),
    }
    record_direct_observation(
        ledgers["npc:speaker"],
        claim_id="claim:basis",
        subject="route:open",
        value="false",
        semantic_minute=20,
        confidence=100,
    )
    queue = DeceptionInformationEventQueue(
        channels={"channel:phone": CommunicationChannel("channel:phone", "PHONE", 2)},
        ledgers=ledgers,
    )
    statement = DeceptiveStatement(
        statement_id="statement:route",
        speaker_id="npc:speaker",
        basis_claim_id="claim:basis",
        subject="route:open",
        basis_value="false",
        asserted_value="true",
        basis_source_agent_id="npc:speaker",
        declared_source_agent_id=None,
        semantic_minute=21,
        kind=DeceptionKind.FALSE_CONTENT,
    )
    queue.schedule_statement(
        statement=statement,
        event_id="event:deception",
        message_id="message:deception",
        receiver_id="npc:receiver",
        new_claim_id="claim:deceptive-report",
        channel_id="channel:phone",
        created_minute=21,
    )
    queue.process_due(23)

    restored = DeceptionInformationEventQueue.restore(
        queue.snapshot(),
        channels=queue.channels,
        ledgers=queue.ledgers,
    )
    archived = restored.envelope_provenance("event:deception")
    assert archived is not None
    assert archived.sender_id == "npc:speaker"
    assert archived.receiver_id == "npc:receiver"
    assert restored.event_statement_ids["event:deception"] == "statement:route"
