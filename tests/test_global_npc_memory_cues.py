import unittest

from tools.global_npc_memory import KnowledgeLedger, record_direct_observation, transmit_claim
from tools.global_npc_memory_cues import (
    ArchiveRecord,
    MemoryCueKind,
    RetrievalCue,
    lookup_archive,
    recall_claim_with_cues,
)
from tools.global_npc_memory_retrieval import RecallState


class GlobalNpcMemoryCueTests(unittest.TestCase):
    def test_matching_place_cue_can_restore_content_access_without_rewriting_claim(self):
        ledger = KnowledgeLedger("witness")
        claim = record_direct_observation(
            ledger,
            claim_id="obs-1",
            subject="marker_colour",
            value="BLUE",
            semantic_minute=0,
            confidence=65,
        )
        cue = RetrievalCue(
            cue_id="return-to-marker",
            kind=MemoryCueKind.PLACE,
            claim_ids=frozenset({"obs-1"}),
            content_bonus=20,
        )
        result = recall_claim_with_cues(
            claim,
            current_semantic_minute=40 * 24 * 60,
            cues=[cue],
        )
        self.assertEqual(RecallState.CONTENT_ONLY, result.recall.state)
        self.assertEqual(("return-to-marker",), result.applied_cue_ids)
        self.assertIn("obs-1", ledger.claims)
        self.assertEqual(65, ledger.claims["obs-1"].confidence)

    def test_source_specific_cue_can_restore_attribution(self):
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
        cue = RetrievalCue(
            cue_id="sender-signature",
            kind=MemoryCueKind.RECORD_REFERENCE,
            claim_ids=frozenset({"report-1"}),
            source_bonus=25,
        )
        result = recall_claim_with_cues(
            report,
            current_semantic_minute=2 * 24 * 60,
            cues=[cue],
        )
        self.assertEqual(RecallState.RECALLED_WITH_SOURCE, result.recall.state)
        self.assertEqual("sender", result.recall.remembered_source_agent_id)

    def test_unrelated_cue_has_no_effect(self):
        ledger = KnowledgeLedger("witness")
        claim = record_direct_observation(
            ledger,
            claim_id="obs-1",
            subject="marker_colour",
            value="BLUE",
            semantic_minute=0,
            confidence=65,
        )
        unrelated = RetrievalCue(
            cue_id="other-place",
            kind=MemoryCueKind.PLACE,
            claim_ids=frozenset({"different-claim"}),
            content_bonus=40,
            source_bonus=40,
        )
        result = recall_claim_with_cues(
            claim,
            current_semantic_minute=40 * 24 * 60,
            cues=[unrelated],
        )
        self.assertEqual(RecallState.INACCESSIBLE, result.recall.state)
        self.assertEqual((), result.applied_cue_ids)

    def test_multiple_cues_are_deterministic_and_bonus_is_capped(self):
        ledger = KnowledgeLedger("witness")
        claim = record_direct_observation(
            ledger,
            claim_id="obs-1",
            subject="route_state",
            value="OPEN",
            semantic_minute=0,
            confidence=60,
        )
        cues = [
            RetrievalCue("z-cue", MemoryCueKind.OBJECT, frozenset({"obs-1"}), content_bonus=30),
            RetrievalCue("a-cue", MemoryCueKind.PLACE, frozenset({"obs-1"}), content_bonus=30),
        ]
        result = recall_claim_with_cues(
            claim,
            current_semantic_minute=40 * 24 * 60,
            cues=cues,
        )
        self.assertEqual(("a-cue", "z-cue"), result.applied_cue_ids)
        self.assertEqual(60, result.recall.accessibility)

    def test_archive_lookup_does_not_become_personal_memory(self):
        archive = KnowledgeLedger("archive")
        record_direct_observation(
            archive,
            claim_id="recorded-claim",
            subject="shipment_state",
            value="DELAYED",
            semantic_minute=100,
            confidence=95,
        )
        npc = KnowledgeLedger("investigator")
        record = ArchiveRecord("dispatch-log", ("recorded-claim",))
        found = lookup_archive(record, archive)
        self.assertEqual(("recorded-claim",), tuple(claim.claim_id for claim in found))
        self.assertEqual({}, npc.claims)

    def test_archive_lookup_rejects_broken_record_reference(self):
        archive = KnowledgeLedger("archive")
        with self.assertRaises(KeyError):
            lookup_archive(ArchiveRecord("broken", ("missing",)), archive)


if __name__ == "__main__":
    unittest.main()
