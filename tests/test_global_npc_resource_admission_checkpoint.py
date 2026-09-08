import copy
import unittest

from tools.global_npc_resource_admission_checkpoint import (
    RESOURCE_CHECKPOINT_ADMISSION_SCHEMA,
    restore_resource_state_with_admissions,
    snapshot_resource_state_with_admissions,
    validate_admission_checkpoint_time,
)
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_reschedule_admission import RescheduleAdmissionAssessment, RescheduleAdmissionState
from tools.global_npc_resource_handoff_reschedule_admission_history import (
    ResourceRescheduleAdmissionLedger,
    record_reschedule_admission,
)
from tools.global_npc_resource_handoff_rescheduling import (
    HandoffRescheduleDecisionKind,
    ResourceHandoffAuthorizationReplacement,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoffs import HandoffMode, ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequest, ResourceRequestEvent, ResourceRequestEventKind, ResourceRequestLedger
from tools.global_npc_resource_reschedule_checkpoint import snapshot_resource_state_with_reschedules
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation


class GlobalNpcResourceAdmissionCheckpointTests(unittest.TestCase):
    def _state(self):
        reservations = ReservationLedger((
            ResourceReservation("reservation:other", "meter:field:7", "ori", 95, 110, purpose_ref="survey:marsh"),
        ))
        requests = ResourceRequestLedger(
            requests=(ResourceRequest(
                request_id="request:meter:nerea", requester_actor_id="nerea", provider_actor_id="teo",
                resource_id="meter:field:7", created_tick=12, expires_at_tick=150, purpose_ref="survey:ridge",
            ),),
            events=(ResourceRequestEvent(
                event_id="request-event:accepted", request_id="request:meter:nerea", actor_id="teo",
                kind=ResourceRequestEventKind.ACCEPTED, at_tick=18, offered_resource_id="meter:field:7",
            ),),
        )
        old = ResourceHandoffAuthorization(
            authorization_id="auth:old", request_id="request:meter:nerea", provider_actor_id="teo",
            accountable_actor_id="nerea", receiving_actor_id="ema", resource_id="meter:field:7",
            mode=HandoffMode.PICKUP, handoff_location_ref="place:repair-row", valid_from_tick=30,
            valid_until_tick=70, authority_ref="request-event:accepted",
        )
        new = ResourceHandoffAuthorization(
            authorization_id="auth:new", request_id=old.request_id, provider_actor_id=old.provider_actor_id,
            accountable_actor_id=old.accountable_actor_id, receiving_actor_id=old.receiving_actor_id,
            resource_id=old.resource_id, mode=old.mode, handoff_location_ref="place:field-office",
            valid_from_tick=90, valid_until_tick=120, authority_ref="decision:accept",
        )
        notice = ResourceHandoffAppointmentNotice(
            notice_id="notice:reschedule", authorization_id="auth:old", sender_actor_id="ema", receiver_actor_id="teo",
            kind=HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST, source_claim_id="claim:reschedule",
            communication_event_id="delivery:reschedule", created_tick=40,
        )
        proposal = ResourceHandoffRescheduleProposal(
            proposal_id="proposal:later", authorization_id="auth:old", source_notice_id="notice:reschedule",
            proposer_actor_id="ema", responder_actor_id="teo", proposed_location_ref="place:field-office",
            proposed_valid_from_tick=90, proposed_valid_until_tick=120, created_tick=40,
        )
        decision = ResourceHandoffRescheduleDecision(
            decision_id="decision:accept", proposal_id="proposal:later", actor_id="teo",
            kind=HandoffRescheduleDecisionKind.ACCEPT, at_tick=46,
        )
        replacement = ResourceHandoffAuthorizationReplacement(
            replacement_id="replacement:1", proposal_id="proposal:later", decision_id="decision:accept",
            superseded_authorization_id="auth:old", successor_authorization_id="auth:new", at_tick=46,
        )
        reschedules = ResourceHandoffRescheduleLedger((proposal,), (decision,), (replacement,))
        assessment = RescheduleAdmissionAssessment(
            state=RescheduleAdmissionState.CONFLICT, proposal_id="proposal:later", resource_id="meter:field:7",
            conflicting_reservation_ids=("reservation:other",),
        )
        admissions = record_reschedule_admission(
            ResourceRescheduleAdmissionLedger(), assessment, record_id="admission:1", assessed_tick=44
        )
        return (
            reservations, requests, ResourceHandoffLedger((new, old), ()), ResourceHandoffAttemptLedger(),
            ResourceHandoffAppointmentLedger((notice,)), reschedules, admissions,
        )

    def test_round_trip_preserves_historical_conflict(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_admissions(*state)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_ADMISSION_SCHEMA)
        self.assertEqual(restore_resource_state_with_admissions(snapshot), state)

    def test_v5_restore_keeps_admission_history_empty(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_reschedules(*state[:6])
        restored = restore_resource_state_with_admissions(snapshot)
        self.assertEqual(restored[:6], state[:6])
        self.assertEqual(restored[6], ResourceRescheduleAdmissionLedger())

    def test_conflict_reservation_must_still_exist_as_history(self):
        snapshot = snapshot_resource_state_with_admissions(*self._state())
        snapshot["reservations"] = []
        with self.assertRaisesRegex(ValueError, "missing conflict reservation"):
            restore_resource_state_with_admissions(snapshot)

    def test_conflict_evidence_cannot_be_reclassified_as_same_purpose(self):
        snapshot = snapshot_resource_state_with_admissions(*self._state())
        snapshot["reservations"][0]["purpose_ref"] = "request:meter:nerea"
        with self.assertRaisesRegex(ValueError, "conflict evidence mismatch"):
            restore_resource_state_with_admissions(snapshot)

    def test_clear_record_cannot_hide_persisted_conflict_ids(self):
        snapshot = snapshot_resource_state_with_admissions(*self._state())
        snapshot["reschedule_admission_records"][0]["state"] = "CLEAR"
        with self.assertRaisesRegex(ValueError, "clear admission contains conflict evidence"):
            restore_resource_state_with_admissions(snapshot)

    def test_assessment_cannot_come_from_future(self):
        with self.assertRaisesRegex(ValueError, "assessment comes from the future"):
            validate_admission_checkpoint_time(self._state()[6], semantic_minute=43)

    def test_duplicate_record_id_fails_closed(self):
        snapshot = snapshot_resource_state_with_admissions(*self._state())
        snapshot["reschedule_admission_records"].append(copy.deepcopy(snapshot["reschedule_admission_records"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate reschedule admission record IDs"):
            restore_resource_state_with_admissions(snapshot)


if __name__ == "__main__":
    unittest.main()
