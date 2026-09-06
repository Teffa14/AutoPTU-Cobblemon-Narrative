from __future__ import annotations

from dataclasses import asdict
from typing import Iterable, Mapping

from tools.global_npc_audience import AudienceCandidate, AudiencePolicy, AudienceSelection, resolve_audience
from tools.global_npc_communication_runtime import choose_channel
from tools.global_npc_deception import (
    DeceptionKind,
    DeceptiveStatement,
    SourceAttributionStore,
    materialize_deceptive_report,
)
from tools.global_npc_information_network import (
    CommunicationChannel,
    DeliveryStatus,
    InformationEnvelope,
    InformationEventQueue,
)
from tools.global_npc_memory import KnowledgeLedger, clamp
from tools.global_npc_social import FactionMembership, RelationshipState


DECEPTION_QUEUE_SNAPSHOT_SCHEMA = "OUROS_NPC_DECEPTION_INFORMATION_QUEUE_V1"


def _statement_to_snapshot(statement: DeceptiveStatement) -> dict:
    row = asdict(statement)
    row["kind"] = statement.kind.value
    return row


def _statement_from_snapshot(raw: Mapping[str, object]) -> DeceptiveStatement:
    return DeceptiveStatement(
        statement_id=str(raw["statement_id"]),
        speaker_id=str(raw["speaker_id"]),
        basis_claim_id=str(raw["basis_claim_id"]),
        subject=str(raw["subject"]),
        basis_value=str(raw["basis_value"]),
        asserted_value=str(raw["asserted_value"]),
        basis_source_agent_id=None if raw.get("basis_source_agent_id") is None else str(raw["basis_source_agent_id"]),
        declared_source_agent_id=None if raw.get("declared_source_agent_id") is None else str(raw["declared_source_agent_id"]),
        semantic_minute=int(raw["semantic_minute"]),
        kind=DeceptionKind(str(raw["kind"])),
    )


class DeceptionInformationEventQueue(InformationEventQueue):
    """Information queue that can transport authored deceptive statements.

    Ordinary envelopes retain the exact InformationEventQueue behavior. A deceptive
    envelope still points at a real basis claim owned by the speaker, but delivery
    materializes the authored assertion instead of retransmitting the basis value.
    """

    def __init__(
        self,
        *,
        channels: dict[str, CommunicationChannel],
        ledgers: dict[str, KnowledgeLedger],
        attribution_store: SourceAttributionStore | None = None,
    ) -> None:
        super().__init__(channels=channels, ledgers=ledgers)
        self.attribution_store = attribution_store or SourceAttributionStore()
        self.statements: dict[str, DeceptiveStatement] = {}
        self.event_statement_ids: dict[str, str] = {}

    def register_statement(self, statement: DeceptiveStatement) -> None:
        existing = self.statements.get(statement.statement_id)
        if existing is not None and existing != statement:
            raise ValueError(f"statement_id collision: {statement.statement_id}")
        speaker = self.ledgers[statement.speaker_id]
        basis = speaker.claims[statement.basis_claim_id]
        if basis.subject != statement.subject or basis.value != statement.basis_value:
            raise ValueError("deceptive statement no longer matches its evidence basis")
        if statement.semantic_minute < basis.semantic_minute:
            raise ValueError("deceptive statement cannot precede its evidence basis")
        self.statements[statement.statement_id] = statement

    def schedule_statement(
        self,
        *,
        statement: DeceptiveStatement,
        event_id: str,
        message_id: str,
        receiver_id: str,
        new_claim_id: str,
        channel_id: str,
        created_minute: int,
        receiver_trust_in_sender: int = 0,
    ) -> InformationEnvelope:
        if created_minute < statement.semantic_minute:
            raise ValueError("dispatch cannot precede the authored statement")
        self.register_statement(statement)
        envelope = super().schedule(
            event_id=event_id,
            message_id=message_id,
            sender_id=statement.speaker_id,
            receiver_id=receiver_id,
            source_claim_id=statement.basis_claim_id,
            new_claim_id=new_claim_id,
            channel_id=channel_id,
            created_minute=created_minute,
            receiver_trust_in_sender=receiver_trust_in_sender,
        )
        self.event_statement_ids[event_id] = statement.statement_id
        return envelope

    def _deliver(self, envelope: InformationEnvelope, semantic_minute: int) -> dict:
        statement_id = self.event_statement_ids.get(envelope.event_id)
        if statement_id is None:
            return super()._deliver(envelope, semantic_minute)
        if envelope.event_id in self.delivered_event_ids:
            return {
                "event_id": envelope.event_id,
                "receiver_id": envelope.receiver_id,
                "status": DeliveryStatus.DELIVERED.value,
                "duplicate": True,
            }

        statement = self.statements[statement_id]
        if statement.speaker_id != envelope.sender_id or statement.basis_claim_id != envelope.source_claim_id:
            raise ValueError("deception envelope does not match its authored statement")
        basis = self.ledgers[statement.speaker_id].claims[statement.basis_claim_id]
        trust = clamp(envelope.receiver_trust_in_sender, -100, 100)
        reported_confidence = min(basis.confidence, clamp(basis.confidence - 20 + trust // 4))
        claim = materialize_deceptive_report(
            self.ledgers[envelope.receiver_id],
            self.attribution_store,
            statement=statement,
            claim_id=envelope.new_claim_id,
            message_id=envelope.message_id,
            semantic_minute=semantic_minute,
            confidence=reported_confidence,
        )
        self.delivered_event_ids.add(envelope.event_id)
        self.statuses[envelope.event_id] = DeliveryStatus.DELIVERED
        return {
            "event_id": envelope.event_id,
            "sender_id": envelope.sender_id,
            "receiver_id": envelope.receiver_id,
            "status": DeliveryStatus.DELIVERED.value,
            "claim_id": claim.claim_id,
            "provenance_root": claim.provenance_root,
            "statement_id": statement.statement_id,
            "deception_kind": statement.kind.value,
        }

    def snapshot(self) -> dict:
        return {
            "schema": DECEPTION_QUEUE_SNAPSHOT_SCHEMA,
            "information_queue": super().snapshot(),
            "statements": [
                _statement_to_snapshot(self.statements[statement_id])
                for statement_id in sorted(self.statements)
            ],
            "event_statement_ids": dict(sorted(self.event_statement_ids.items())),
            "attribution_store": self.attribution_store.snapshot(),
        }

    @classmethod
    def restore(
        cls,
        snapshot: Mapping[str, object],
        *,
        channels: dict[str, CommunicationChannel],
        ledgers: dict[str, KnowledgeLedger],
    ) -> "DeceptionInformationEventQueue":
        if snapshot.get("schema") != DECEPTION_QUEUE_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported deception information queue snapshot schema")
        base_raw = snapshot.get("information_queue")
        if not isinstance(base_raw, Mapping):
            raise ValueError("deception snapshot requires an information_queue mapping")
        attribution_raw = snapshot.get("attribution_store")
        if not isinstance(attribution_raw, Mapping):
            raise ValueError("deception snapshot requires an attribution_store mapping")

        base = InformationEventQueue.restore(base_raw, channels=channels, ledgers=ledgers)
        queue = cls(
            channels=channels,
            ledgers=ledgers,
            attribution_store=SourceAttributionStore.restore(attribution_raw),
        )
        queue.pending = base.pending
        queue.statuses = base.statuses
        queue.delivered_event_ids = base.delivered_event_ids
        queue.awaiting_local_ack = base.awaiting_local_ack

        rows = snapshot.get("statements", [])
        if not isinstance(rows, list):
            raise ValueError("deception statements must be a list")
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("deception statement snapshot row must be a mapping")
            queue.register_statement(_statement_from_snapshot(raw))

        mapping_raw = snapshot.get("event_statement_ids", {})
        if not isinstance(mapping_raw, Mapping):
            raise ValueError("event_statement_ids must be a mapping")
        queue.event_statement_ids = {str(event_id): str(statement_id) for event_id, statement_id in mapping_raw.items()}
        for event_id, statement_id in queue.event_statement_ids.items():
            if statement_id not in queue.statements:
                raise KeyError(f"event references unknown deceptive statement: {statement_id}")
            if event_id not in queue.statuses and event_id not in queue.delivered_event_ids:
                raise KeyError(f"deception mapping references unknown queue event: {event_id}")
        return queue


class DeceptionDispatchResult:
    def __init__(
        self,
        selection: AudienceSelection,
        scheduled: tuple[dict, ...],
        unscheduled: tuple[tuple[str, str], ...],
    ) -> None:
        self.selection = selection
        self.scheduled = scheduled
        self.unscheduled = unscheduled


def dispatch_deception_to_audience(
    *,
    dispatch_id: str,
    statement: DeceptiveStatement,
    semantic_minute: int,
    queue: DeceptionInformationEventQueue,
    candidates: Iterable[AudienceCandidate],
    relationships: Iterable[RelationshipState] = (),
    memberships: Iterable[FactionMembership] = (),
    required_obligation_tag: str | None = None,
    policy: AudiencePolicy = AudiencePolicy(),
    receiver_trust_in_sender: Mapping[str, int] | None = None,
) -> DeceptionDispatchResult:
    if semantic_minute < statement.semantic_minute:
        raise ValueError("deception dispatch cannot precede statement authorship")
    candidate_list = tuple(candidates)
    candidate_by_id = {candidate.agent_id: candidate for candidate in candidate_list}
    selection = resolve_audience(
        sender_id=statement.speaker_id,
        candidates=candidate_list,
        relationships=relationships,
        memberships=memberships,
        required_obligation_tag=required_obligation_tag,
        policy=policy,
    )
    trust = receiver_trust_in_sender or {}
    scheduled: list[dict] = []
    unscheduled: list[tuple[str, str]] = []

    for receiver_id in selection.selected_agent_ids:
        candidate = candidate_by_id[receiver_id]
        channel = choose_channel(candidate, queue.channels)
        if channel is None:
            unscheduled.append((receiver_id, "NO_KNOWN_CHANNEL"))
            continue
        event_id = f"{dispatch_id}:delivery:{receiver_id}"
        envelope = queue.schedule_statement(
            statement=statement,
            event_id=event_id,
            message_id=f"{dispatch_id}:message:{receiver_id}",
            receiver_id=receiver_id,
            new_claim_id=f"{dispatch_id}:claim:{receiver_id}",
            channel_id=channel.channel_id,
            created_minute=semantic_minute,
            receiver_trust_in_sender=int(trust.get(receiver_id, 0)),
        )
        scheduled.append({
            "receiver_id": receiver_id,
            "event_id": event_id,
            "channel_id": channel.channel_id,
            "delivery_minute": envelope.delivery_minute,
        })

    return DeceptionDispatchResult(selection, tuple(scheduled), tuple(sorted(unscheduled)))
