import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDisposition,
    AssistanceCommitmentDispositionLedger,
    CommitmentStartDisposition,
)
from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartAssessment,
    AssistanceCommitmentStartLedger,
    AssistanceCommitmentStartWatch,
    CommitmentStartCondition,
)
from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    AssistanceCommitmentViabilityObservation,
)
from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger, AssistanceCounterproposalRecord
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_world_checkpoint import build_assistance_world_checkpoint
from tools.global_npc_assistance_world_checkpoint_v5 import (
    build_assistance_world_checkpoint_v5,
    restore_assistance_world_checkpoint_v5,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


class AssistanceWorldCheckpointV5Tests(unittest.TestCase):
    def _state(self):
        agents = {
            "requester": NpcAgentState("requester", AgentMode.OFFSCREEN_NAMED, "synthetic", "station"),
            "responder": NpcAgentState("responder", AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        }
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        queue = NpcReplanQueue()
        scheduled = ScheduledCommitment(
            commitment_id="commit:1", intent_kind="ASSIST_SURVEY", start_minute=80, end_minute=110,
            priority=8, hard=False, grace_minutes=5, required_knowledge=frozenset(),
            required_permissions=frozenset(), target_ref="requester", requires_local_projection=True,
            requires_structured_mechanics=False,
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
            replan_queue=queue, agents=agents,
            agendas={"responder": AgentAgendaProfile(commitments=(scheduled,))},
        )
        actions = WorldActionIntentLedger()
        actions.records["request:1"] = WorldActionIntentRecord(
            action_id="request:1", agent_id="requester", intent_id="intent:req", intent_kind="REQUEST_ASSISTANCE",
            target_ref="responder", semantic_minute=10, trigger_ids=("t:req",), reason_codes=("NEEDS_SUPPORT",),
            source_type="SITUATIONAL", source_ref="site:crossing",
        )
        actions.records["response:1"] = WorldActionIntentRecord(
            action_id="response:1", agent_id="responder", intent_id="intent:counter",
            intent_kind="COUNTERPROPOSE_ASSISTANCE_REQUEST", target_ref="requester", semantic_minute=20,
            trigger_ids=("t:counter",), reason_codes=("CAN_HELP_LATER",), source_type="SITUATIONAL",
            source_ref="request:1",
        )
        actions.records["decision:1"] = WorldActionIntentRecord(
            action_id="decision:1", agent_id="requester", intent_id="intent:accept",
            intent_kind="ACCEPT_ASSISTANCE_COUNTERPROPOSAL", target_ref="responder", semantic_minute=30,
            trigger_ids=("t:accept",), reason_codes=("TERMS_ACCEPTED",), source_type="SITUATIONAL",
            source_ref="proposal:1",
        )
        proposals = AssistanceCounterproposalLedger()
        proposals.add(AssistanceCounterproposalRecord(
            proposal_id="proposal:1", request_action_id="request:1", response_action_id="response:1",
            requester_id="requester", responder_id="responder", proposed_start_minute=80, proposed_end_minute=110,
            location_ref="site:crossing", scope_ref="scope:survey", alternative_ref="alternative:report",
            expires_minute=50, provenance_root="response:1",
        ))
        negotiated = AssistanceCounterproposalCommitmentLedger()
        negotiated.add(AssistanceCounterproposalCommitmentRecord(
            commitment_id="commit:1", proposal_id="proposal:1", request_action_id="request:1",
            response_action_id="response:1", decision_action_id="decision:1", requester_id="requester",
            responder_id="responder", intent_kind="ASSIST_SURVEY", start_minute=80, end_minute=110,
            location_ref="site:crossing", scope_ref="scope:survey", alternative_ref="alternative:report",
            priority=8, hard=False, grace_minutes=5, required_knowledge=(), required_permissions=(),
            requires_local_projection=True, requires_structured_mechanics=False, provenance_root="decision:1",
        ))
        viability = AssistanceCommitmentViabilityLedger()
        viability.add(AssistanceCommitmentViabilityObservation(
            observation_id="viability:1", commitment_id="commit:1", proposal_id="proposal:1",
            requester_id="requester", responder_id="responder", observer_id="responder", semantic_minute=40,
            viability="BLOCKED", constraint_kind="ROUTE_UNAVAILABLE", constraint_ref="route:crossing",
            evidence_ref="claim:closure", provenance_root="claim:closure",
        ))
        queue.schedule(ReplanTrigger(
            trigger_id="replan:assistance-viability:viability:1", agent_id="responder",
            reason=ReplanReason.EXTERNAL_EVENT, due_minute=40, source_ref="viability:1", priority=8,
        ))
        start = AssistanceCommitmentStartLedger()
        start.add_watch(AssistanceCommitmentStartWatch(
            watch_id="watch:1", commitment_id="commit:1", proposal_id="proposal:1", requester_id="requester",
            responder_id="responder", start_minute=80, armed_minute=45, provenance_root="viability:1",
            trigger_id="replan:assistance-start:watch:1",
        ))
        queue.schedule(ReplanTrigger(
            trigger_id="replan:assistance-start:watch:1", agent_id="responder",
            reason=ReplanReason.SCHEDULE_DUE, due_minute=80, source_ref="watch:1", priority=9,
        ))
        queue.process_due(80)
        start.add_assessment(AssistanceCommitmentStartAssessment(
            assessment_id="assessment:1", watch_id="watch:1", commitment_id="commit:1", proposal_id="proposal:1",
            requester_id="requester", responder_id="responder", semantic_minute=80,
            condition=CommitmentStartCondition.BLOCKED_AT_START.value, viability_observation_id="viability:1",
            constraint_kind="ROUTE_UNAVAILABLE", constraint_ref="route:crossing", evidence_ref="claim:closure",
            provenance_root="claim:closure",
        ))
        disposition = AssistanceCommitmentDispositionLedger()
        disposition.add(AssistanceCommitmentDisposition(
            disposition_id="disposition:1", commitment_id="commit:1", proposal_id="proposal:1",
            assessment_id="assessment:1", requester_id="requester", responder_id="responder", actor_id="responder",
            semantic_minute=80, disposition=CommitmentStartDisposition.WAIT_FOR_CLEARANCE.value,
            rationale_ref="reason:route-still-closed", provenance_root="assessment:1",
        ))
        return coordinator, channels, actions, proposals, negotiated, viability, start, disposition

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(raw).hexdigest()

    def test_start_fact_and_disposition_restore_as_one_generation(self):
        coordinator, channels, actions, proposals, negotiated, viability, start, disposition = self._state()
        checkpoint = build_assistance_world_checkpoint_v5(
            coordinator, semantic_minute=80, action_ledger=actions, commitment_ledger=AssistanceCommitmentLedger(),
            counterproposal_ledger=proposals, counterproposal_commitment_ledger=negotiated,
            commitment_viability_ledger=viability, commitment_start_ledger=start,
            commitment_disposition_ledger=disposition,
        )
        self.assertEqual(checkpoint["schema_version"], "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V5")
        restored = restore_assistance_world_checkpoint_v5(checkpoint, channels=channels)
        self.assertEqual(restored.commitment_start_ledger.assessments["assessment:1"].constraint_ref, "route:crossing")
        self.assertEqual(restored.commitment_disposition_ledger.records["disposition:1"].disposition, "WAIT_FOR_CLEARANCE")
        self.assertIn("replan:assistance-start:watch:1", restored.base.world.coordinator.replan_queue.completed_trigger_ids)

    def test_redigested_snapshot_cannot_rebind_disposition_actor(self):
        coordinator, channels, actions, proposals, negotiated, viability, start, disposition = self._state()
        checkpoint = build_assistance_world_checkpoint_v5(
            coordinator, semantic_minute=80, action_ledger=actions, commitment_ledger=AssistanceCommitmentLedger(),
            counterproposal_ledger=proposals, counterproposal_commitment_ledger=negotiated,
            commitment_viability_ledger=viability, commitment_start_ledger=start,
            commitment_disposition_ledger=disposition,
        )
        corrupted = copy.deepcopy(checkpoint)
        corrupted["assistance_commitment_disposition"]["records"][0]["actor_id"] = "requester"
        self._redigest(corrupted)
        with self.assertRaisesRegex(ValueError, "does not own commitment"):
            restore_assistance_world_checkpoint_v5(corrupted, channels=channels)

    def test_v4_restore_defaults_new_ledgers_to_empty(self):
        coordinator, channels, actions, proposals, negotiated, viability, _, _ = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator, semantic_minute=80, action_ledger=actions, commitment_ledger=AssistanceCommitmentLedger(),
            counterproposal_ledger=proposals, counterproposal_commitment_ledger=negotiated,
            commitment_viability_ledger=viability,
        )
        restored = restore_assistance_world_checkpoint_v5(checkpoint, channels=channels)
        self.assertEqual(restored.commitment_start_ledger.watches, {})
        self.assertEqual(restored.commitment_disposition_ledger.records, {})

    def test_checkpoint_v5_does_not_execute_policy(self):
        source = open("tools/global_npc_assistance_world_checkpoint_v5.py", encoding="utf-8").read().lower()
        for forbidden in ("reserve_route", "consume_item", "apply_damage", "roll_accuracy", "knockback", "send_message"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
