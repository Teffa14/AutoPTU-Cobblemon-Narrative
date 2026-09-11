import unittest

from tools.autoptu_world_observation_delivery import schedule_world_observation_delivery
from tools.autoptu_world_observation_owner import WorldObservationRecord
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind


class AutoPTUWorldObservationDeliveryTests(unittest.TestCase):
    def observation(self):
        return WorldObservationRecord(
            transaction_id="ouros.world-consequence.pass420",
            session_id="ouros.autoptu.session.pass420",
            result_ref="result:pass420:1",
            objective_ref="objective:pass420:route-inspection",
            outcome="PARTIAL",
            provenance_ref="ingress:pass420:1",
            evidence_ref="evidence:pass420:marker",
        )

    def queue(self, *, latency=2, available=True):
        ledgers = {
            "marea-dispatch": KnowledgeLedger("marea-dispatch"),
            "field-team-b": KnowledgeLedger("field-team-b"),
            "unrelated-member": KnowledgeLedger("unrelated-member"),
        }
        channels = {
            "radio": CommunicationChannel(
                channel_id="radio",
                kind="RADIO",
                latency_minutes=latency,
                available=available,
            )
        }
        return InformationEventQueue(channels=channels, ledgers=ledgers)

    def schedule(self, queue, **overrides):
        values = {
            "custodian_id": "marea-dispatch",
            "recipient_id": "field-team-b",
            "channel_id": "radio",
            "created_minute": 100,
            "source_claim_id": "claim:pass420:observation-record",
            "event_id": "delivery:pass420:field-team-b",
            "message_id": "message:pass420:field-team-b",
            "receiver_claim_id": "claim:pass420:field-team-b",
        }
        values.update(overrides)
        return schedule_world_observation_delivery(self.observation(), queue=queue, **values)

    def test_observation_is_materialized_for_one_custodian_then_one_recipient(self):
        queue = self.queue()
        scheduled, changed = self.schedule(queue)
        self.assertTrue(changed)
        self.assertEqual(scheduled.observation_transaction_id, "ouros.world-consequence.pass420")
        self.assertEqual(scheduled.observation_provenance_ref, "ingress:pass420:1")

        source = queue.ledgers["marea-dispatch"].claims[scheduled.source_claim_id]
        self.assertEqual(source.source_kind, SourceKind.INSTITUTIONAL_RECORD)
        self.assertEqual(source.subject, "objective:pass420:route-inspection")
        self.assertEqual(source.value, "PARTIAL")
        self.assertEqual(source.provenance_root, "ouros.world-consequence.pass420")
        self.assertEqual(queue.ledgers["field-team-b"].claims, {})
        self.assertEqual(queue.ledgers["unrelated-member"].claims, {})

        queue.process_due(102)
        received = queue.ledgers["field-team-b"].claims["claim:pass420:field-team-b"]
        self.assertEqual(received.source_kind, SourceKind.REPORT)
        self.assertEqual(received.provenance_root, "ouros.world-consequence.pass420")
        self.assertEqual(received.parent_claim_id, "claim:pass420:observation-record")
        self.assertEqual(queue.ledgers["unrelated-member"].claims, {})

    def test_delivery_latency_preserves_stale_recipient_until_due(self):
        queue = self.queue(latency=5)
        self.schedule(queue)
        self.assertEqual(queue.process_due(104), [])
        self.assertEqual(queue.ledgers["field-team-b"].claims, {})
        queue.process_due(105)
        self.assertIn("claim:pass420:field-team-b", queue.ledgers["field-team-b"].claims)

    def test_exact_replay_is_idempotent_before_and_after_delivery(self):
        queue = self.queue()
        first, first_changed = self.schedule(queue)
        second, second_changed = self.schedule(queue)
        self.assertTrue(first_changed)
        self.assertFalse(second_changed)
        self.assertEqual(first, second)

        queue.process_due(102)
        third, third_changed = self.schedule(queue)
        self.assertFalse(third_changed)
        self.assertEqual(third.envelope.event_id, first.envelope.event_id)
        self.assertEqual(len(queue.ledgers["marea-dispatch"].claims), 1)
        self.assertEqual(len(queue.ledgers["field-team-b"].claims), 1)

    def test_same_event_identity_cannot_target_a_different_recipient(self):
        queue = self.queue()
        self.schedule(queue)
        with self.assertRaisesRegex(ValueError, "conflicting replay"):
            self.schedule(queue, recipient_id="unrelated-member")

    def test_shared_membership_does_not_expand_recipient_scope(self):
        queue = self.queue()
        self.schedule(queue)
        queue.process_due(102)
        self.assertIn("claim:pass420:field-team-b", queue.ledgers["field-team-b"].claims)
        self.assertEqual(queue.ledgers["unrelated-member"].claims, {})

    def test_missing_explicit_identity_fails_closed(self):
        queue = self.queue()
        with self.assertRaisesRegex(ValueError, "recipient_id is required"):
            self.schedule(queue, recipient_id="   ")
        with self.assertRaisesRegex(KeyError, "custodian and recipient"):
            self.schedule(queue, recipient_id="unknown-agent")

    def test_conflicting_source_claim_reuse_fails_closed(self):
        queue = self.queue()
        self.schedule(queue)
        changed_observation = WorldObservationRecord(
            transaction_id="ouros.world-consequence.other",
            session_id="ouros.autoptu.session.other",
            result_ref="result:other:1",
            objective_ref="objective:pass420:route-inspection",
            outcome="COMPLETE",
            provenance_ref="ingress:other:1",
        )
        with self.assertRaisesRegex(ValueError, "claim_id collision"):
            schedule_world_observation_delivery(
                changed_observation,
                queue=queue,
                custodian_id="marea-dispatch",
                recipient_id="field-team-b",
                channel_id="radio",
                created_minute=100,
                source_claim_id="claim:pass420:observation-record",
                event_id="delivery:pass420:other",
                message_id="message:pass420:other",
                receiver_claim_id="claim:pass420:other",
            )


if __name__ == "__main__":
    unittest.main()
