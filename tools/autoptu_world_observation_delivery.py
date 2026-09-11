from __future__ import annotations

from dataclasses import dataclass

from tools.autoptu_world_observation_owner import WorldObservationRecord
from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind


@dataclass(frozen=True)
class ScheduledObservationDelivery:
    observation_transaction_id: str
    observation_provenance_ref: str
    source_claim_id: str
    envelope: InformationEnvelope


def _required(value: str, field_name: str) -> str:
    normalized = str(value).strip()
    if not normalized:
        raise ValueError(f"{field_name} is required")
    return normalized


def schedule_world_observation_delivery(
    observation: WorldObservationRecord,
    *,
    queue: InformationEventQueue,
    custodian_id: str,
    recipient_id: str,
    channel_id: str,
    created_minute: int,
    source_claim_id: str,
    event_id: str,
    message_id: str,
    receiver_claim_id: str,
    confidence: int = 100,
    receiver_trust_in_sender: int = 0,
) -> tuple[ScheduledObservationDelivery, bool]:
    """Schedule one explicit recipient delivery for a committed world observation.

    The observation becomes an institutional record in one explicit custodian's
    private knowledge ledger, then travels through the existing information
    queue to one explicit recipient. Shared faction or institutional membership
    never expands the audience here.
    """

    custodian_id = _required(custodian_id, "custodian_id")
    recipient_id = _required(recipient_id, "recipient_id")
    channel_id = _required(channel_id, "channel_id")
    source_claim_id = _required(source_claim_id, "source_claim_id")
    event_id = _required(event_id, "event_id")
    message_id = _required(message_id, "message_id")
    receiver_claim_id = _required(receiver_claim_id, "receiver_claim_id")
    if created_minute < 0:
        raise ValueError("created_minute must be non-negative")

    try:
        custodian = queue.ledgers[custodian_id]
        queue.ledgers[recipient_id]
    except KeyError as exc:
        raise KeyError("custodian and recipient must have knowledge ledgers") from exc

    channel = queue.channels[channel_id]
    source_claim = Claim(
        claim_id=source_claim_id,
        subject=observation.objective_ref,
        value=observation.outcome,
        source_kind=SourceKind.INSTITUTIONAL_RECORD,
        source_agent_id=custodian_id,
        semantic_minute=created_minute,
        confidence=confidence,
        provenance_root=observation.transaction_id,
    )
    custodian.add(source_claim)

    candidate = InformationEnvelope(
        event_id=event_id,
        message_id=message_id,
        sender_id=custodian_id,
        receiver_id=recipient_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        delivery_minute=created_minute + channel.latency_minutes,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )

    existing = queue.envelope_provenance(event_id)
    if existing is not None:
        if existing != candidate:
            raise ValueError("conflicting replay for observation delivery event")
        return (
            ScheduledObservationDelivery(
                observation_transaction_id=observation.transaction_id,
                observation_provenance_ref=observation.provenance_ref,
                source_claim_id=source_claim_id,
                envelope=existing,
            ),
            False,
        )

    if event_id in queue.statuses or event_id in queue.delivered_event_ids or event_id in queue.archived_envelopes:
        raise ValueError("observation delivery event identity exists without matching provenance")

    envelope = queue.schedule(
        event_id=event_id,
        message_id=message_id,
        sender_id=custodian_id,
        receiver_id=recipient_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )
    return (
        ScheduledObservationDelivery(
            observation_transaction_id=observation.transaction_id,
            observation_provenance_ref=observation.provenance_ref,
            source_claim_id=source_claim_id,
            envelope=envelope,
        ),
        True,
    )
