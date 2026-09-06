import unittest

from tools.global_npc_audience import AudienceCandidate, AudiencePolicy
from tools.global_npc_deception import SourceAttributionStore, author_deceptive_statement, perceived_source
from tools.global_npc_deception_runtime import (
    DeceptionInformationEventQueue,
    dispatch_deception_to_audience,
)
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_social import FactionMembership, RelationshipState


class GlobalNpcDeceptionRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ledgers = {
            agent_id: KnowledgeLedger(agent_id)
            for agent_id in ("speaker", "friend", "officer", "coworker")
        }
        self.channels = {
            "radio": CommunicationChannel("radio", "RADIO", 5),
            "local": CommunicationChannel("local", "LOCAL", 1),
        }
        self.attributions = SourceAttributionStore()
        self.queue = DeceptionInformationEventQueue(
            channels=self.channels,
            ledgers=self.ledgers,
            attribution_store=self.attributions,
        )
        record_direct_observation(
            self.ledgers["speaker"],
            claim_id="basis:route",
            subject="route:ridge:status",
            value="CLOSED",
            semantic_minute=10,
            confidence=90,
        )
        self.statement = author_deceptive_statement(
            self.ledgers["speaker"],
            statement_id="lie:route-open",
            basis_claim_id="basis:route",
            asserted_value="OPEN",
            semantic_minute=12,
            declared_source_agent_id="inspector",
        )

    def test_targeted_deception_uses_normal_audience_and_preserves_speaker_belief(self) -> None:
        memberships = (
            FactionMembership("speaker", "guild", "member"),
            FactionMembership("coworker", "guild", "member"),
        )
        result = dispatch_deception_to_audience(
            dispatch_id="dispatch:lie",
            statement=self.statement,
            semantic_minute=12,
            queue=self.queue,
            candidates=(
                AudienceCandidate("friend", ("radio",), topic_relevance=7),
                AudienceCandidate("officer", ("radio",), explicit_role_relevance=6),
                AudienceCandidate("coworker", ("radio",)),
            ),
            relationships=(RelationshipState("speaker", "friend", trust=48, affinity=40),),
            memberships=memberships,
            policy=AudiencePolicy(max_recipients=2, min_score=1),
            receiver_trust_in_sender={"friend": 20, "officer": 0},
        )
        self.assertEqual(result.selection.selected_agent_ids, ("friend", "officer"))
        self.assertIn(("coworker", "BELOW_THRESHOLD"), result.selection.rejected)

        first = self.queue.process_due_budgeted(17, max_events=1)
        self.assertEqual(first["processed_count"], 1)
        self.assertEqual(first["deferred_due_count"], 1)
        self.assertEqual(first["deliveries"][0]["deception_kind"], "FALSE_CONTENT_AND_SOURCE")

        second = self.queue.process_due_budgeted(17, max_events=1)
        self.assertEqual(second["processed_count"], 1)
        self.assertEqual(second["deferred_due_count"], 0)

        self.assertEqual(self.ledgers["speaker"].claims["basis:route"].value, "CLOSED")
        self.assertEqual(len(self.ledgers["speaker"].claims), 1)
        self.assertEqual(len(self.ledgers["coworker"].claims), 0)
        for receiver_id in ("friend", "officer"):
            claim = next(iter(self.ledgers[receiver_id].claims.values()))
            self.assertEqual(claim.value, "OPEN")
            self.assertEqual(claim.source_agent_id, "speaker")
            self.assertEqual(claim.provenance_root, "deception:lie:route-open")
            self.assertEqual(perceived_source(self.ledgers[receiver_id], self.attributions, claim.claim_id), "inspector")

    def test_snapshot_restore_keeps_pending_deception_and_attribution(self) -> None:
        self.queue.schedule_statement(
            statement=self.statement,
            event_id="event:friend",
            message_id="message:friend",
            receiver_id="friend",
            new_claim_id="claim:friend",
            channel_id="radio",
            created_minute=12,
            receiver_trust_in_sender=0,
        )
        snapshot = self.queue.snapshot()
        restored = DeceptionInformationEventQueue.restore(
            snapshot,
            channels=self.channels,
            ledgers=self.ledgers,
        )
        delivery = restored.process_due(17)
        self.assertEqual(len(delivery), 1)
        self.assertEqual(delivery[0]["statement_id"], "lie:route-open")
        self.assertEqual(restored.statuses["event:friend"], DeliveryStatus.DELIVERED)
        self.assertEqual(self.ledgers["friend"].claims["claim:friend"].value, "OPEN")
        self.assertEqual(
            perceived_source(self.ledgers["friend"], restored.attribution_store, "claim:friend"),
            "inspector",
        )
        self.assertEqual(restored.process_due(30), [])

    def test_local_projection_ack_materializes_deception_only_after_acceptance(self) -> None:
        channels = {"local": CommunicationChannel("local", "LOCAL", 0, requires_local_projection=True)}
        queue = DeceptionInformationEventQueue(channels=channels, ledgers=self.ledgers)
        queue.schedule_statement(
            statement=self.statement,
            event_id="event:local",
            message_id="message:local",
            receiver_id="friend",
            new_claim_id="claim:local",
            channel_id="local",
            created_minute=12,
        )
        result = queue.process_due(12)
        self.assertEqual(result[0]["status"], DeliveryStatus.WAITING_LOCAL_ACK.value)
        self.assertNotIn("claim:local", self.ledgers["friend"].claims)
        acknowledged = queue.acknowledge_local_delivery("event:local", 13, accepted=True)
        self.assertEqual(acknowledged["status"], DeliveryStatus.DELIVERED.value)
        self.assertEqual(self.ledgers["friend"].claims["claim:local"].value, "OPEN")

    def test_ordinary_information_still_uses_base_queue_delivery(self) -> None:
        record_direct_observation(
            self.ledgers["speaker"],
            claim_id="basis:weather",
            subject="weather:plain",
            value="CLEAR",
            semantic_minute=20,
            confidence=80,
        )
        self.queue.schedule(
            event_id="event:ordinary",
            message_id="message:ordinary",
            sender_id="speaker",
            receiver_id="friend",
            source_claim_id="basis:weather",
            new_claim_id="claim:ordinary",
            channel_id="local",
            created_minute=20,
        )
        result = self.queue.process_due(21)
        self.assertEqual(result[0]["provenance_root"], "basis:weather")
        self.assertNotIn("statement_id", result[0])

    def test_rejects_statement_when_basis_has_changed_or_dispatch_precedes_authorship(self) -> None:
        with self.assertRaises(ValueError):
            self.queue.schedule_statement(
                statement=self.statement,
                event_id="event:early",
                message_id="message:early",
                receiver_id="friend",
                new_claim_id="claim:early",
                channel_id="radio",
                created_minute=11,
            )


if __name__ == "__main__":
    unittest.main()
