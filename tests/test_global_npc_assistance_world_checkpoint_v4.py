import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    AssistanceCommitmentViabilityObservation,
)
from tools.global_npc_assistance_counterproposal import (
    AssistanceCounterproposalLedger,
    AssistanceCounterproposalRecord,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_world_checkpoint import (
    build_assistance_world_checkpoint,
    restore_assistance_world_checkpoint,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


class AssistanceWorldCheckpointV4Tests(unittest.TestCase):
    def _state(self):
        agents = {
            "requester": NpcAgentState("requester", AgentMode.OFFSCREEN_NAMED, "synthetic", "station"),
            "responder": NpcAgentState("responder", AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        }
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
        queue = NpcReplanQueue()
        scheduled = ScheduledCommitment(
            commitment_id="commit:negotiated:1",
            intent_kind="ASSIST_CAUSEWAY_SURVEY",
            start_minute=80,
            end_minute=110,
            priority=8,
            hard=False,
            grace_minutes=5,
            required_knowledge=frozenset({"claim:access-window"}),
            required_permissions=frozenset({"permit:causeway"}),
            target_ref="requester",
            requires_local_projection=True,
            requires_structured_mechanics=False,
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
            replan_queue=queue,
            agents=agents,
            agendas={"responder": AgentAgendaProfile(commitments=(scheduled,))},
        )

        actions = WorldActionIntentLedger()
        actions.records["request:1"] = WorldActionIntentRecord(
            action_id="request:1", agent_id="requester", intent_id="intent:request",
            intent_kind="REQUEST_ASSISTANCE", target_ref="responder", semantic_minute=10,
            trigger_ids=("trigger:request",), reason_codes=("NEEDS_SUPPORT",),
            source_type="SITUATIONAL", source_ref="hazard:bridge",
        )
        actions.records["response:1"] = WorldActionIntentRecord(
            action_id="response:1", agent_id="responder", intent_id="intent:counter",
            intent_kind="COUNTERPROPOSE_ASSISTANCE_REQUEST", target_ref="requester", semantic_minute=20,
            trigger_ids=("replan:information:event:request:1",), reason_codes=("CAN_HELP_LATER",),
            source_type="SITUATIONAL", source_ref="request:1",
        )
        actions.records["decision:1"] = WorldActionIntentRecord(
            action_id="decision:1", agent_id="requester", intent_id="intent:accept-counter",
            intent_kind="ACCEPT_ASSISTANCE_COUNTERPROPOSAL", target_ref="responder", semantic_minute=30,
            trigger_ids=("replan:information:event:terms:1",), reason_codes=("TERMS_ACCEPTED",),
            source_type="SITUATIONAL", source_ref="proposal:1",
        )

        proposals = AssistanceCounterproposalLedger()
        proposals.add(AssistanceCounterproposalRecord(
            proposal_id="proposal:1", request_action_id="request:1", response_action_id="response:1",
            requester_id="requester", responder_id="responder", proposed_start_minute=80,
            proposed_end_minute=110, location_ref="site:causeway-east", scope_ref="scope:survey-only",
            alternative_ref="alternative:remote-report", expires_minute=50, provenance_root="response:1",
        ))

        negotiated = AssistanceCounterproposalCommitmentLedger()
        negotiated.add(AssistanceCounterproposalCommitmentRecord(
            commitment_id="commit:negotiated:1", proposal_id="proposal:1", request_action_id="request:1",
            response_action_id="response:1", decision_action_id="decision:1", requester_id="requester",
            responder_id="responder", intent_kind="ASSIST_CAUSEWAY_SURVEY", start_minute=80, end_minute=110,
            location_ref="site:causeway-east", scope_ref="scope:survey-only",
            alternative_ref="alternative:remote-report", priority=8, hard=False, grace_minutes=5,
            required_knowledge=("claim:access-window",), required_permissions=("permit:causeway",),
            requires_local_projection=True, requires_structured_mechanics=False, provenance_root="decision:1",
        ))

        viability = AssistanceCommitmentViabilityLedger()
        viability.add(AssistanceCommitmentViabilityObservation(
            observation_id="viability:blocked:1", commitment_id="commit:negotiated:1", proposal_id="proposal:1",
            requester_id="requester", responder_id="responder", observer_id="responder", semantic_minute=40,
            viability="BLOCKED", constraint_kind="ROUTE_UNAVAILABLE", constraint_ref="route:causeway-east",
            evidence_ref="claim:closure-notice", provenance_root="claim:closure-notice",
        ))
        queue.schedule(ReplanTrigger(
            trigger_id="replan:assistance-viability:viability:blocked:1", agent_id="responder",
            reason=ReplanReason.EXTERNAL_EVENT, due_minute=40, source_ref="viability:blocked:1", priority=8,
        ))
        return coordinator, channels, actions, proposals, negotiated, viability

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(raw).hexdigest()

    def test_viability_and_commitment_restore_as_one_generation(self):
        coordinator, channels, actions, proposals, negotiated, viability = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator, semantic_minute=40, action_ledger=actions,
            commitment_ledger=AssistanceCommitmentLedger(), counterproposal_ledger=proposals,
            counterproposal_commitment_ledger=negotiated, commitment_viability_ledger=viability,
        )
        self.assertEqual(checkpoint["schema_version"], "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V4")
        restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
        row = restored.commitment_viability_ledger.records["viability:blocked:1"]
        self.assertEqual(row.constraint_ref, "route:causeway-east")
        self.assertEqual(row.evidence_ref, "claim:closure-notice")
        self.assertIn("commit:negotiated:1", restored.counterproposal_commitment_ledger.records)
        self.assertIn("replan:assistance-viability:viability:blocked:1", restored.world.coordinator.replan_queue.known_trigger_ids)

    def test_build_rejects_viability_for_another_commitment(self):
        coordinator, _, actions, proposals, negotiated, viability = self._state()
        row = viability.records["viability:blocked:1"]
        viability.records[row.observation_id] = AssistanceCommitmentViabilityObservation(
            **{**row.__dict__, "commitment_id": "commit:missing"}
        )
        with self.assertRaisesRegex(ValueError, "missing negotiated commitment"):
            build_assistance_world_checkpoint(
                coordinator, semantic_minute=40, action_ledger=actions,
                commitment_ledger=AssistanceCommitmentLedger(), counterproposal_ledger=proposals,
                counterproposal_commitment_ledger=negotiated, commitment_viability_ledger=viability,
            )

    def test_build_rejects_missing_viability_wakeup(self):
        coordinator, _, actions, proposals, negotiated, viability = self._state()
        coordinator.replan_queue = NpcReplanQueue()
        with self.assertRaisesRegex(ValueError, "trigger missing"):
            build_assistance_world_checkpoint(
                coordinator, semantic_minute=40, action_ledger=actions,
                commitment_ledger=AssistanceCommitmentLedger(), counterproposal_ledger=proposals,
                counterproposal_commitment_ledger=negotiated, commitment_viability_ledger=viability,
            )

    def test_redigested_snapshot_cannot_rebind_viability_actor(self):
        coordinator, channels, actions, proposals, negotiated, viability = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator, semantic_minute=40, action_ledger=actions,
            commitment_ledger=AssistanceCommitmentLedger(), counterproposal_ledger=proposals,
            counterproposal_commitment_ledger=negotiated, commitment_viability_ledger=viability,
        )
        corrupted = copy.deepcopy(checkpoint)
        corrupted["assistance_commitment_viability"]["records"][0]["responder_id"] = "requester"
        self._redigest(corrupted)
        with self.assertRaisesRegex(ValueError, "actor binding mismatch"):
            restore_assistance_world_checkpoint(corrupted, channels=channels)

    def test_v3_restore_defaults_viability_to_empty(self):
        coordinator, channels, actions, proposals, negotiated, _ = self._state()
        coordinator.replan_queue = NpcReplanQueue()
        checkpoint = build_assistance_world_checkpoint(
            coordinator, semantic_minute=40, action_ledger=actions,
            commitment_ledger=AssistanceCommitmentLedger(), counterproposal_ledger=proposals,
            counterproposal_commitment_ledger=negotiated,
        )
        checkpoint["schema_version"] = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V3"
        checkpoint.pop("assistance_commitment_viability")
        self._redigest(checkpoint)
        restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.commitment_viability_ledger.records, {})

    def test_checkpoint_owner_does_not_turn_blocker_into_execution(self):
        source = open("tools/global_npc_assistance_world_checkpoint.py", encoding="utf-8").read().lower()
        for forbidden in ("reserve_route", "consume_item", "apply_damage", "roll_accuracy", "knockback"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
