import unittest

from tools.global_npc_memory import KnowledgeLedger, record_direct_observation, transmit_claim
from tools.global_npc_memory_retrieval import (
    RecallState,
    evaluate_recalled_belief,
    recall_claim,
)


class GlobalNpcMemoryRetrievalTests(unittest.TestCase):
    def test_recent_direct_observation_keeps_content_and_source(self):
        ledger = KnowledgeLedger("witness")
        claim = record_direct_observation(
            ledger,
            claim_id="obs-1",
            subject="route_state",
            value="CLOSED",
            semantic_minute=100,
            confidence=85,
        )
        recall = recall_claim(claim, current_semantic_minute=130)
        self.assertEqual(RecallState.RECALLED_WITH_SOURCE, recall.state)
        self.assertEqual("witness", recall.remembered_source_agent_id)

    def test_old_report_can_keep_content_without_source_attribution(self):
        sender = KnowledgeLedger("sender")
        receiver = KnowledgeLedger("receiver")
        source = record_direct_observation(
            sender,
            claim_id="obs-1",
            subject="route_state",
            value="CLOSED",
            semantic_minute=0,
            confidence=90,
        )
        report = transmit_claim(
            sender,
            receiver,
            source_claim_id=source.claim_id,
            new_claim_id="report-1",
            message_id="msg-1",
            semantic_minute=10,
            receiver_trust_in_sender=40,
        )
        recall = recall_claim(report, current_semantic_minute=2 * 24 * 60)
        self.assertEqual(RecallState.CONTENT_ONLY, recall.state)
        self.assertIsNone(recall.remembered_source_agent_id)
        self.assertEqual(source.provenance_root, recall.provenance_root)

    def test_low_accessibility_claim_becomes_inaccessible_without_deletion(self):
        ledger = KnowledgeLedger("witness")
        claim = record_direct_observation(
            ledger,
            claim_id="obs-1",
            subject="marker_colour",
            value="BLUE",
            semantic_minute=0,
            confidence=65,
        )
        recall = recall_claim(claim, current_semantic_minute=40 * 24 * 60)
        self.assertEqual(RecallState.INACCESSIBLE, recall.state)
        self.assertIn(claim.claim_id, ledger.claims)

    def test_recalled_belief_uses_only_currently_accessible_claims(self):
        ledger = KnowledgeLedger("witness")
        record_direct_observation(
            ledger,
            claim_id="old",
            subject="route_state",
            value="OPEN",
            semantic_minute=0,
            confidence=65,
        )
        record_direct_observation(
            ledger,
            claim_id="recent",
            subject="route_state",
            value="CLOSED",
            semantic_minute=60 * 24 * 60,
            confidence=85,
        )
        assessment = evaluate_recalled_belief(
            ledger,
            "route_state",
            current_semantic_minute=60 * 24 * 60 + 30,
        )
        self.assertEqual("SUPPORTED", assessment.status.value)
        self.assertEqual("CLOSED", assessment.preferred_value)
        self.assertEqual(2, len(ledger.claims))

    def test_future_time_is_rejected(self):
        ledger = KnowledgeLedger("witness")
        claim = record_direct_observation(
            ledger,
            claim_id="obs-1",
            subject="route_state",
            value="OPEN",
            semantic_minute=100,
            confidence=80,
        )
        with self.assertRaises(ValueError):
            recall_claim(claim, current_semantic_minute=99)


if __name__ == "__main__":
    unittest.main()
