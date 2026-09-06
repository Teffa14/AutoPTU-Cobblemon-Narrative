import unittest

from tools.global_npc_assessment_revision_propagation import (
    AssessmentRevisionPropagationRegistry,
    record_assessment_conclusion,
    register_assessment_notice,
    schedule_assessment_notice,
)
from tools.global_npc_evidence_custody import (
    CustodyAssessment,
    CustodyIntegrityStatus,
    EvidenceCustodyRegistry,
)
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger


class AssessmentRevisionPropagationTests(unittest.TestCase):
    def setUp(self):
        self.custody = EvidenceCustodyRegistry()
        self.investigator = KnowledgeLedger("investigator")
        self.receiver_old = KnowledgeLedger("receiver-old")
        self.receiver_new = KnowledgeLedger("receiver-new")
        self.queue = InformationEventQueue(
            channels={"radio": CommunicationChannel("radio", "RADIO", 5)},
            ledgers={
                self.investigator.agent_id: self.investigator,
                self.receiver_old.agent_id: self.receiver_old,
                self.receiver_new.agent_id: self.receiver_new,
            },
        )
        self.old = CustodyAssessment(
            assessment_id="assessment-old",
            investigator_id="investigator",
            evidence_id="relay-sample",
            semantic_minute=10,
            status=CustodyIntegrityStatus.DOCUMENTATION_GAP,
            known_record_ids=(),
            support_claim_ids=(),
        )
        self.new = CustodyAssessment(
            assessment_id="assessment-new",
            investigator_id="investigator",
            evidence_id="relay-sample",
            semantic_minute=30,
            status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
            known_record_ids=(),
            support_claim_ids=(),
            supersedes_assessment_id="assessment-old",
        )
        self.custody.add_assessment(self.old)
        self.custody.add_assessment(self.new)

    def test_superseding_assessment_becomes_distinct_claim(self):
        old_claim = record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-old", claim_id="claim-old"
        )
        new_claim = record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-new", claim_id="claim-new"
        )
        self.assertEqual(old_claim.value, "DOCUMENTATION_GAP")
        self.assertEqual(new_claim.value, "CONTINUITY_SUPPORTED")
        self.assertNotEqual(old_claim.provenance_root, new_claim.provenance_root)
        self.assertIn("claim-old", self.investigator.claims)
        self.assertIn("claim-new", self.investigator.claims)

    def test_revision_only_changes_recipient_after_real_delivery(self):
        record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-new", claim_id="claim-new"
        )
        registry = AssessmentRevisionPropagationRegistry()
        register_assessment_notice(
            registry,
            self.custody,
            self.investigator,
            assessment_id="assessment-new",
            conclusion_claim_id="claim-new",
            notice_id="notice-new",
        )
        schedule_assessment_notice(
            self.queue,
            registry,
            notice_id="notice-new",
            receiver_ids=("receiver-new",),
            channel_id="radio",
            created_minute=30,
        )
        self.assertEqual(self.receiver_new.claims, {})
        self.assertEqual(self.receiver_old.claims, {})
        results = self.queue.process_due(35)
        self.assertEqual(results[0]["status"], DeliveryStatus.DELIVERED.value)
        self.assertIn("claim-new:received:receiver-new", self.receiver_new.claims)
        self.assertEqual(self.receiver_old.claims, {})

    def test_superseding_notice_does_not_auto_target_old_audience(self):
        record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-new", claim_id="claim-new"
        )
        registry = AssessmentRevisionPropagationRegistry()
        notice = register_assessment_notice(
            registry,
            self.custody,
            self.investigator,
            assessment_id="assessment-new",
            conclusion_claim_id="claim-new",
            notice_id="notice-new",
        )
        self.assertEqual(notice.supersedes_assessment_id, "assessment-old")
        envelopes = schedule_assessment_notice(
            self.queue,
            registry,
            notice_id="notice-new",
            receiver_ids=("receiver-new",),
            channel_id="radio",
            created_minute=31,
        )
        self.assertEqual(tuple(row.receiver_id for row in envelopes), ("receiver-new",))

    def test_notice_rejects_claim_from_other_assessment(self):
        record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-old", claim_id="claim-old"
        )
        with self.assertRaises(ValueError):
            register_assessment_notice(
                AssessmentRevisionPropagationRegistry(),
                self.custody,
                self.investigator,
                assessment_id="assessment-new",
                conclusion_claim_id="claim-old",
                notice_id="notice-bad",
            )

    def test_only_assessment_investigator_can_materialize_conclusion(self):
        outsider = KnowledgeLedger("outsider")
        with self.assertRaises(ValueError):
            record_assessment_conclusion(
                outsider, self.custody, assessment_id="assessment-new", claim_id="claim-bad"
            )

    def test_channel_failure_does_not_create_receiver_knowledge(self):
        record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-new", claim_id="claim-new"
        )
        registry = AssessmentRevisionPropagationRegistry()
        register_assessment_notice(
            registry,
            self.custody,
            self.investigator,
            assessment_id="assessment-new",
            conclusion_claim_id="claim-new",
            notice_id="notice-new",
        )
        self.queue.channels["radio"] = CommunicationChannel("radio", "RADIO", 0, available=False)
        schedule_assessment_notice(
            self.queue,
            registry,
            notice_id="notice-new",
            receiver_ids=("receiver-new",),
            channel_id="radio",
            created_minute=30,
        )
        result = self.queue.process_due(30)[0]
        self.assertEqual(result["status"], DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value)
        self.assertEqual(self.receiver_new.claims, {})

    def test_notice_cannot_predate_assessment(self):
        record_assessment_conclusion(
            self.investigator, self.custody, assessment_id="assessment-new", claim_id="claim-new"
        )
        registry = AssessmentRevisionPropagationRegistry()
        register_assessment_notice(
            registry,
            self.custody,
            self.investigator,
            assessment_id="assessment-new",
            conclusion_claim_id="claim-new",
            notice_id="notice-new",
        )
        with self.assertRaises(ValueError):
            schedule_assessment_notice(
                self.queue,
                registry,
                notice_id="notice-new",
                receiver_ids=("receiver-new",),
                channel_id="radio",
                created_minute=29,
            )


if __name__ == "__main__":
    unittest.main()
