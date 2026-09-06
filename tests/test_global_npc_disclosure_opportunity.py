import unittest

from tools.global_npc_communication_runtime import DispatchResult
from tools.global_npc_deception_policy import (
    CommunicationOpportunity,
    CommunicationPolicyDecision,
    CommunicationPosture,
    DeceptionMotive,
)
from tools.global_npc_disclosure_expectation import DisclosureBasis, DisclosureExpectation
from tools.global_npc_disclosure_opportunity import (
    CommunicationAccessStatus,
    DisclosureResponsibilityStatus,
    assess_disclosure_responsibility,
    available_access_evidence,
    capture_dispatch_access,
)
from tools.global_npc_information_network import (
    CommunicationChannel,
    InformationEventQueue,
)
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_audience import AudienceSelection


class GlobalNpcDisclosureOpportunityTests(unittest.TestCase):
    def opportunity(self):
        return CommunicationOpportunity(
            opportunity_id="op-1",
            speaker_id="dispatcher",
            target_agent_id="traveler",
            basis_claim_id="route-state",
            asserted_value="CLOSED",
            declared_source_agent_id=None,
            semantic_minute=20,
            motive=DeceptionMotive.DUTY_CONFLICT,
        )

    def expectation(self):
        return DisclosureExpectation(
            expectation_id="expect-1",
            speaker_id="dispatcher",
            recipient_id="traveler",
            basis_claim_id="route-state",
            basis=DisclosureBasis.EMERGENCY_WARNING,
            created_semantic_minute=10,
            strength=80,
            provenance_ref="duty:route-warning",
        )

    def decision(self, posture):
        return CommunicationPolicyDecision(
            opportunity_id="op-1",
            posture=posture,
            truthful_score=0,
            silence_score=0,
            deception_score=0,
            reason_codes=(),
        )

    def queue(self, *, available=True, requires_local_projection=False):
        ledgers = {
            "dispatcher": KnowledgeLedger("dispatcher"),
            "traveler": KnowledgeLedger("traveler"),
        }
        record_direct_observation(
            ledgers["dispatcher"],
            claim_id="route-state",
            subject="route:north",
            value="CLOSED",
            semantic_minute=10,
            confidence=100,
        )
        channels = {
            "radio": CommunicationChannel(
                channel_id="radio",
                kind="RADIO",
                latency_minutes=2,
                available=available,
                requires_local_projection=requires_local_projection,
            )
        }
        return InformationEventQueue(channels=channels, ledgers=ledgers)

    def dispatch(self, *, scheduled=(), unscheduled=()):
        return DispatchResult(
            selection=AudienceSelection(selected_agent_ids=("traveler",), scored_candidates=()),
            scheduled=tuple(scheduled),
            unscheduled=tuple(unscheduled),
        )

    def test_proven_direct_contact_allows_willful_withholding_finding(self):
        access = available_access_evidence(
            self.opportunity(),
            self.expectation(),
            semantic_minute=20,
            provenance_ref="scene:face-to-face",
        )
        finding = assess_disclosure_responsibility(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(),
            access,
            observed_semantic_minute=21,
        )
        self.assertEqual(DisclosureResponsibilityStatus.WILLFUL_WITHHOLDING, finding.status)
        self.assertIsNotNone(finding.breach_assessment)

    def test_no_known_channel_is_not_a_silence_breach(self):
        access = capture_dispatch_access(
            self.dispatch(unscheduled=(("traveler", "NO_KNOWN_CHANNEL"),)),
            expectation=self.expectation(),
            opportunity=self.opportunity(),
            receiver_id="traveler",
            queue=self.queue(),
            semantic_minute=20,
        )
        finding = assess_disclosure_responsibility(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(),
            access,
            observed_semantic_minute=21,
        )
        self.assertEqual(CommunicationAccessStatus.NO_KNOWN_CHANNEL, access.status)
        self.assertEqual(DisclosureResponsibilityStatus.NO_USABLE_PATH, finding.status)
        self.assertIsNone(finding.breach_assessment)

    def test_queued_attempt_is_not_reclassified_as_withholding(self):
        queue = self.queue()
        envelope = queue.schedule(
            event_id="dispatch-1:delivery:traveler",
            message_id="message-1",
            sender_id="dispatcher",
            receiver_id="traveler",
            source_claim_id="route-state",
            new_claim_id="received-route-state",
            channel_id="radio",
            created_minute=20,
        )
        access = capture_dispatch_access(
            self.dispatch(scheduled=({
                "receiver_id": "traveler",
                "event_id": envelope.event_id,
                "channel_id": "radio",
                "delivery_minute": envelope.delivery_minute,
            },)),
            expectation=self.expectation(),
            opportunity=self.opportunity(),
            receiver_id="traveler",
            queue=queue,
            semantic_minute=20,
        )
        finding = assess_disclosure_responsibility(
            self.decision(CommunicationPosture.TRUTHFUL),
            self.opportunity(),
            self.expectation(),
            access,
            observed_semantic_minute=20,
        )
        self.assertEqual(CommunicationAccessStatus.ATTEMPT_QUEUED, access.status)
        self.assertEqual(DisclosureResponsibilityStatus.ATTEMPT_IN_PROGRESS, finding.status)

    def test_channel_failure_after_attempt_is_not_speaker_withholding(self):
        queue = self.queue(available=False)
        envelope = queue.schedule(
            event_id="dispatch-1:delivery:traveler",
            message_id="message-1",
            sender_id="dispatcher",
            receiver_id="traveler",
            source_claim_id="route-state",
            new_claim_id="received-route-state",
            channel_id="radio",
            created_minute=20,
        )
        queue.process_due(22)
        access = capture_dispatch_access(
            self.dispatch(scheduled=({
                "receiver_id": "traveler",
                "event_id": envelope.event_id,
                "channel_id": "radio",
                "delivery_minute": envelope.delivery_minute,
            },)),
            expectation=self.expectation(),
            opportunity=self.opportunity(),
            receiver_id="traveler",
            queue=queue,
            semantic_minute=22,
        )
        finding = assess_disclosure_responsibility(
            self.decision(CommunicationPosture.TRUTHFUL),
            self.opportunity(),
            self.expectation(),
            access,
            observed_semantic_minute=22,
        )
        self.assertEqual(CommunicationAccessStatus.DELIVERY_FAILED, access.status)
        self.assertEqual(DisclosureResponsibilityStatus.ATTEMPT_FAILED, finding.status)

    def test_waiting_local_ack_remains_unresolved(self):
        queue = self.queue(requires_local_projection=True)
        envelope = queue.schedule(
            event_id="dispatch-1:delivery:traveler",
            message_id="message-1",
            sender_id="dispatcher",
            receiver_id="traveler",
            source_claim_id="route-state",
            new_claim_id="received-route-state",
            channel_id="radio",
            created_minute=20,
        )
        queue.process_due(22)
        access = capture_dispatch_access(
            self.dispatch(scheduled=({
                "receiver_id": "traveler",
                "event_id": envelope.event_id,
                "channel_id": "radio",
                "delivery_minute": envelope.delivery_minute,
            },)),
            expectation=self.expectation(),
            opportunity=self.opportunity(),
            receiver_id="traveler",
            queue=queue,
            semantic_minute=22,
        )
        self.assertEqual(CommunicationAccessStatus.WAITING_LOCAL_ACK, access.status)
        finding = assess_disclosure_responsibility(
            self.decision(CommunicationPosture.TRUTHFUL),
            self.opportunity(),
            self.expectation(),
            access,
            observed_semantic_minute=22,
        )
        self.assertEqual(DisclosureResponsibilityStatus.ATTEMPT_IN_PROGRESS, finding.status)

    def test_weak_expectation_does_not_become_willful_breach(self):
        weak = DisclosureExpectation(
            expectation_id="expect-1",
            speaker_id="dispatcher",
            recipient_id="traveler",
            basis_claim_id="route-state",
            basis=DisclosureBasis.EXPLICIT_REQUEST,
            created_semantic_minute=10,
            strength=30,
            provenance_ref="request:route-status",
        )
        access = available_access_evidence(
            self.opportunity(), weak, semantic_minute=20, provenance_ref="scene:direct-contact"
        )
        finding = assess_disclosure_responsibility(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            weak,
            access,
            observed_semantic_minute=21,
        )
        self.assertEqual(DisclosureResponsibilityStatus.EXPECTATION_TOO_WEAK, finding.status)

    def test_identity_and_causality_guards_fail_closed(self):
        access = available_access_evidence(
            self.opportunity(), self.expectation(), semantic_minute=20, provenance_ref="scene:direct"
        )
        with self.assertRaises(ValueError):
            assess_disclosure_responsibility(
                self.decision(CommunicationPosture.SILENT),
                self.opportunity(),
                self.expectation(),
                access,
                observed_semantic_minute=19,
            )


if __name__ == "__main__":
    unittest.main()
