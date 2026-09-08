import copy
import unittest

from tools.global_npc_resource_appointment_checkpoint import snapshot_resource_state_with_appointment_notices
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_rescheduling import (
    HandoffRescheduleDecisionKind,
    ResourceHandoffAuthorizationReplacement,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoffs import HandoffMode, ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
)
from tools.global_npc_resource_reschedule_checkpoint import (
    RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA,
    restore_resource_state_with_reschedules,
    snapshot_resource_state_with_reschedules,
    validate_reschedule_checkpoint_time,
)
from tools.global_npc_resource_reservations import ReservationLedger


class GlobalNpcResourceRescheduleCheckpointTests(unittest.TestCase):
    def _state(self):
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
            notice_id="notice:reschedule", authorization_id="auth:old", sender_actor_id="ema",
            receiver_actor_id="teo", kind=HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST,
            source_claim_id="claim:reschedule", communication_event_id="delivery:reschedule", created_tick=40,
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
        return (
            ReservationLedger(), requests, ResourceHandoffLedger((new, old), ()), ResourceHandoffAttemptLedger(),
            ResourceHandoffAppointmentLedger((notice,)),
            ResourceHandoffRescheduleLedger((proposal,), (decision,), (replacement,)),
        )

    def test_round_trip_preserves_successor_history(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_reschedules(*state)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA)
        self.assertEqual(restore_resource_state_with_reschedules(snapshot), state)
        validate_reschedule_checkpoint_time(state[5], semantic_minute=46)

    def test_v4_restore_keeps_reschedule_history_empty(self):
        reservations, requests, handoffs, attempts, appointments, _ = self._state()
        snapshot = snapshot_resource_state_with_appointment_notices(
            reservations, requests, handoffs, attempts, appointments
        )
        restored = restore_resource_state_with_reschedules(snapshot)
        self.assertEqual(restored[:5], (reservations, requests, handoffs, attempts, appointments))
        self.assertEqual(restored[5], ResourceHandoffRescheduleLedger())

    def test_successor_must_match_accepted_proposal(self):
        snapshot = snapshot_resource_state_with_reschedules(*self._state())
        for row in snapshot["handoff_authorizations"]:
            if row["authorization_id"] == "auth:new":
                row["handoff_location_ref"] = "place:wrong"
        with self.assertRaisesRegex(ValueError, "successor authorization does not match"):
            restore_resource_state_with_reschedules(snapshot)

    def test_replacement_requires_acceptance(self):
        snapshot = snapshot_resource_state_with_reschedules(*self._state())
        snapshot["handoff_reschedule_decisions"][0]["kind"] = "REJECT"
        with self.assertRaisesRegex(ValueError, "lacks matching acceptance"):
            restore_resource_state_with_reschedules(snapshot)

    def test_duplicate_successor_and_replacement_ids_fail_closed(self):
        snapshot = snapshot_resource_state_with_reschedules(*self._state())
        duplicate = copy.deepcopy(snapshot["handoff_authorization_replacements"][0])
        snapshot["handoff_authorization_replacements"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "duplicate handoff authorization replacement IDs"):
            restore_resource_state_with_reschedules(snapshot)

    def test_reschedule_history_cannot_come_from_future(self):
        ledger = self._state()[5]
        with self.assertRaisesRegex(ValueError, "handoff reschedule decision comes from the future"):
            validate_reschedule_checkpoint_time(ledger, semantic_minute=45)


if __name__ == "__main__":
    unittest.main()
