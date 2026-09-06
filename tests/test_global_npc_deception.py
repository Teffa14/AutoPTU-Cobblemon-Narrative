import unittest

from tools.global_npc_deception import (
    AttributionKind,
    DeceptionKind,
    SourceAttributionStore,
    author_deceptive_statement,
    materialize_deceptive_report,
    perceived_source,
    record_source_confusion,
)
from tools.global_npc_memory import KnowledgeLedger, evaluate_belief, record_direct_observation


class GlobalNpcDeceptionTests(unittest.TestCase):
    def setUp(self):
        self.speaker = KnowledgeLedger("speaker")
        self.receiver = KnowledgeLedger("receiver")
        self.store = SourceAttributionStore()
        record_direct_observation(
            self.speaker,
            claim_id="basis-1",
            subject="route-state",
            value="CLOSED",
            semantic_minute=10,
            confidence=90,
        )

    def test_false_content_creates_new_provenance_root_and_preserves_actual_speaker(self):
        statement = author_deceptive_statement(
            self.speaker,
            statement_id="lie-1",
            basis_claim_id="basis-1",
            asserted_value="OPEN",
            semantic_minute=20,
        )
        self.assertEqual(DeceptionKind.FALSE_CONTENT, statement.kind)

        claim = materialize_deceptive_report(
            self.receiver,
            self.store,
            statement=statement,
            claim_id="received-lie",
            message_id="message-1",
            semantic_minute=25,
            confidence=80,
        )
        self.assertEqual("OPEN", claim.value)
        self.assertEqual("speaker", claim.source_agent_id)
        self.assertEqual("deception:lie-1", claim.provenance_root)
        self.assertEqual("basis-1", claim.parent_claim_id)
        self.assertEqual("speaker", perceived_source(self.receiver, self.store, claim.claim_id))

        belief = evaluate_belief(self.receiver, "route-state")
        self.assertEqual("OPEN", belief.preferred_value)

    def test_false_source_is_subjective_overlay_not_provenance_rewrite(self):
        statement = author_deceptive_statement(
            self.speaker,
            statement_id="lie-source",
            basis_claim_id="basis-1",
            asserted_value="CLOSED",
            declared_source_agent_id="third-party",
            semantic_minute=20,
        )
        self.assertEqual(DeceptionKind.FALSE_SOURCE, statement.kind)

        claim = materialize_deceptive_report(
            self.receiver,
            self.store,
            statement=statement,
            claim_id="received-source-lie",
            message_id="message-2",
            semantic_minute=21,
            confidence=70,
        )
        self.assertEqual("speaker", claim.source_agent_id)
        self.assertEqual("third-party", perceived_source(self.receiver, self.store, claim.claim_id))
        record = self.store.for_claim("receiver", claim.claim_id)[0]
        self.assertEqual(AttributionKind.SPEAKER_DECLARATION, record.kind)
        self.assertEqual("speaker", record.actual_source_agent_id)

    def test_source_confusion_changes_perception_without_mutating_claim(self):
        claim = materialize_deceptive_report(
            self.receiver,
            self.store,
            statement=author_deceptive_statement(
                self.speaker,
                statement_id="lie-2",
                basis_claim_id="basis-1",
                asserted_value="OPEN",
                semantic_minute=20,
            ),
            claim_id="claim-2",
            message_id="message-3",
            semantic_minute=22,
            confidence=65,
        )
        original = claim
        record_source_confusion(
            self.receiver,
            self.store,
            attribution_id="confusion-1",
            claim_id=claim.claim_id,
            perceived_source_agent_id="other-witness",
            semantic_minute=100,
        )
        self.assertEqual("other-witness", perceived_source(self.receiver, self.store, claim.claim_id))
        self.assertEqual(original, self.receiver.claims[claim.claim_id])
        self.assertEqual("speaker", self.receiver.claims[claim.claim_id].source_agent_id)

    def test_latest_attribution_is_deterministic(self):
        claim = materialize_deceptive_report(
            self.receiver,
            self.store,
            statement=author_deceptive_statement(
                self.speaker,
                statement_id="lie-3",
                basis_claim_id="basis-1",
                asserted_value="OPEN",
                semantic_minute=20,
            ),
            claim_id="claim-3",
            message_id="message-4",
            semantic_minute=25,
            confidence=60,
        )
        record_source_confusion(
            self.receiver,
            self.store,
            attribution_id="a",
            claim_id=claim.claim_id,
            perceived_source_agent_id="source-a",
            semantic_minute=50,
        )
        record_source_confusion(
            self.receiver,
            self.store,
            attribution_id="b",
            claim_id=claim.claim_id,
            perceived_source_agent_id="source-b",
            semantic_minute=50,
        )
        self.assertEqual("source-b", perceived_source(self.receiver, self.store, claim.claim_id))

    def test_snapshot_restore_preserves_subjective_attribution(self):
        statement = author_deceptive_statement(
            self.speaker,
            statement_id="lie-4",
            basis_claim_id="basis-1",
            asserted_value="OPEN",
            declared_source_agent_id="invented-source",
            semantic_minute=20,
        )
        claim = materialize_deceptive_report(
            self.receiver,
            self.store,
            statement=statement,
            claim_id="claim-4",
            message_id="message-5",
            semantic_minute=30,
            confidence=75,
        )
        restored = SourceAttributionStore.restore(self.store.snapshot())
        self.assertEqual("invented-source", perceived_source(self.receiver, restored, claim.claim_id))

    def test_truthful_restatement_is_rejected_by_deception_api(self):
        with self.assertRaises(ValueError):
            author_deceptive_statement(
                self.speaker,
                statement_id="not-a-lie",
                basis_claim_id="basis-1",
                asserted_value="CLOSED",
                declared_source_agent_id="speaker",
                semantic_minute=20,
            )

    def test_causal_time_guards(self):
        statement = author_deceptive_statement(
            self.speaker,
            statement_id="lie-5",
            basis_claim_id="basis-1",
            asserted_value="OPEN",
            semantic_minute=20,
        )
        with self.assertRaises(ValueError):
            materialize_deceptive_report(
                self.receiver,
                self.store,
                statement=statement,
                claim_id="early",
                message_id="message-6",
                semantic_minute=19,
                confidence=50,
            )


if __name__ == "__main__":
    unittest.main()
