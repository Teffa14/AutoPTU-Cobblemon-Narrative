import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
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
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


class AssistanceWorldCheckpointV3Tests(unittest.TestCase):
    def _state(self):
        agents = {
            "requester": NpcAgentState("requester", AgentMode.OFFSCREEN_NAMED, "synthetic", "station"),
            "responder": NpcAgentState("responder", AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        }
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
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
            replan_queue=NpcReplanQueue(),
            agents=agents,
            agendas={"responder": AgentAgendaProfile(commitments=(scheduled,))},
        )

        actions = WorldActionIntentLedger()
        actions.records["request:1"] = WorldActionIntentRecord(
            action_id="request:1",
            agent_id="requester",
            intent_id="intent:request",
            intent_kind="REQUEST_ASSISTANCE",
            target_ref="responder",
            semantic_minute=10,
            trigger_ids=("trigger:request",),
            reason_codes=("NEEDS_SUPPORT",),
            source_type="SITUATIONAL",
            source_ref="hazard:bridge",
        )
        actions.records["response:1"] = WorldActionIntentRecord(
            action_id="response:1",
            agent_id="responder",
            intent_id="intent:counter",
            intent_kind="COUNTERPROPOSE_ASSISTANCE_REQUEST",
            target_ref="requester",
            semantic_minute=20,
            trigger_ids=("replan:information:event:request:1",),
            reason_codes=("CAN_HELP_LATER",),
            source_type="SITUATIONAL",
            source_ref="request:1",
        )
        actions.records["decision:1"] = WorldActionIntentRecord(
            action_id="decision:1",
            agent_id="requester",
            intent_id="intent:accept-counter",
            intent_kind="ACCEPT_ASSISTANCE_COUNTERPROPOSAL",
            target_ref="responder",
            semantic_minute=30,
            trigger_ids=("replan:information:event:terms:1",),
            reason_codes=("TERMS_ACCEPTED",),
            source_type="SITUATIONAL",
            source_ref="proposal:1",
        )

        proposals = AssistanceCounterproposalLedger()
        proposals.add(
            AssistanceCounterproposalRecord(
                proposal_id="proposal:1",
                request_action_id="request:1",
                response_action_id="response:1",
                requester_id="requester",
                responder_id="responder",
                proposed_start_minute=80,
                proposed_end_minute=110,
                location_ref="site:causeway-east",
                scope_ref="scope:survey-only",
                alternative_ref="alternative:remote-report",
                expires_minute=50,
                provenance_root="response:1",
            )
        )

        negotiated = AssistanceCounterproposalCommitmentLedger()
        negotiated.add(
            AssistanceCounterproposalCommitmentRecord(
                commitment_id="commit:negotiated:1",
                proposal_id="proposal:1",
                request_action_id="request:1",
                response_action_id="response:1",
                decision_action_id="decision:1",
                requester_id="requester",
                responder_id="responder",
                intent_kind="ASSIST_CAUSEWAY_SURVEY",
                start_minute=80,
                end_minute=110,
                location_ref="site:causeway-east",
                scope_ref="scope:survey-only",
                alternative_ref="alternative:remote-report",
                priority=8,
                hard=False,
                grace_minutes=5,
                required_knowledge=("claim:access-window",),
                required_permissions=("permit:causeway",),
                requires_local_projection=True,
                requires_structured_mechanics=False,
                provenance_root="decision:1",
            )
        )
        return coordinator, channels, actions, proposals, negotiated

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(raw).hexdigest()

    def test_negotiated_terms_and_commitment_restore_as_one_generation(self):
        coordinator, channels, actions, proposals, negotiated = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator,
            semantic_minute=40,
            action_ledger=actions,
            commitment_ledger=AssistanceCommitmentLedger(),
            counterproposal_ledger=proposals,
            counterproposal_commitment_ledger=negotiated,
        )
        restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.world.semantic_minute, 40)
        self.assertEqual(restored.counterproposal_ledger.records["proposal:1"].scope_ref, "scope:survey-only")
        record = restored.counterproposal_commitment_ledger.records["commit:negotiated:1"]
        self.assertEqual(record.provenance_root, "decision:1")
        self.assertEqual(record.location_ref, "site:causeway-east")
        agenda = restored.world.coordinator.agendas["responder"]
        self.assertEqual([row.commitment_id for row in agenda.commitments], ["commit:negotiated:1"])
        self.assertEqual(agenda.commitments[0].start_minute, 80)

    def test_build_fails_if_negotiated_terms_drift_from_proposal(self):
        coordinator, _, actions, proposals, negotiated = self._state()
        row = negotiated.records["commit:negotiated:1"]
        negotiated.records["commit:negotiated:1"] = AssistanceCounterproposalCommitmentRecord(
            **{**row.__dict__, "scope_ref": "scope:repair"}
        )
        with self.assertRaisesRegex(ValueError, "changed accepted non-time terms"):
            build_assistance_world_checkpoint(
                coordinator,
                semantic_minute=40,
                action_ledger=actions,
                commitment_ledger=AssistanceCommitmentLedger(),
                counterproposal_ledger=proposals,
                counterproposal_commitment_ledger=negotiated,
            )

    def test_build_fails_if_requester_acceptance_names_another_proposal(self):
        coordinator, _, actions, proposals, negotiated = self._state()
        row = actions.records["decision:1"]
        actions.records["decision:1"] = WorldActionIntentRecord(**{**row.__dict__, "source_ref": "proposal:other"})
        with self.assertRaisesRegex(ValueError, "names another proposal"):
            build_assistance_world_checkpoint(
                coordinator,
                semantic_minute=40,
                action_ledger=actions,
                commitment_ledger=AssistanceCommitmentLedger(),
                counterproposal_ledger=proposals,
                counterproposal_commitment_ledger=negotiated,
            )

    def test_validly_redigested_snapshot_cannot_change_proposal_terms(self):
        coordinator, channels, actions, proposals, negotiated = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator,
            semantic_minute=40,
            action_ledger=actions,
            commitment_ledger=AssistanceCommitmentLedger(),
            counterproposal_ledger=proposals,
            counterproposal_commitment_ledger=negotiated,
        )
        corrupted = copy.deepcopy(checkpoint)
        corrupted["assistance_counterproposals"]["records"][0]["location_ref"] = "site:elsewhere"
        self._redigest(corrupted)
        with self.assertRaisesRegex(ValueError, "changed accepted non-time terms"):
            restore_assistance_world_checkpoint(corrupted, channels=channels)

    def test_v2_restore_keeps_new_ledgers_empty(self):
        coordinator, channels, actions, _, _ = self._state()
        coordinator.agendas["responder"] = AgentAgendaProfile()
        checkpoint = build_assistance_world_checkpoint(
            coordinator,
            semantic_minute=40,
            action_ledger=actions,
            commitment_ledger=AssistanceCommitmentLedger(),
        )
        checkpoint["schema_version"] = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V2"
        checkpoint.pop("assistance_counterproposals")
        checkpoint.pop("assistance_counterproposal_commitments")
        self._redigest(checkpoint)
        restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.counterproposal_ledger.records, {})
        self.assertEqual(restored.counterproposal_commitment_ledger.records, {})

    def test_checkpoint_owner_does_not_execute_negotiated_work(self):
        source = open("tools/global_npc_assistance_world_checkpoint.py", encoding="utf-8").read().lower()
        for forbidden in ("reserve_route", "consume_item", "apply_damage", "roll_accuracy", "knockback"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
