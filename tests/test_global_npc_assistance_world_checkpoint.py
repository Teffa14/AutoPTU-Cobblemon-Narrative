import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger, AssistanceCommitmentRecord
from tools.global_npc_assistance_world_checkpoint import (
    build_assistance_world_checkpoint,
    restore_assistance_world_checkpoint,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


class AssistanceWorldCheckpointTests(unittest.TestCase):
    def _state(self):
        agents = {
            "requester": NpcAgentState("requester", AgentMode.OFFSCREEN_NAMED, "synthetic", "office"),
            "responder": NpcAgentState("responder", AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        }
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
        commitment = ScheduledCommitment(
            commitment_id="commit:assist:1",
            intent_kind="ASSIST_ROUTE_INSPECTION",
            start_minute=40,
            end_minute=70,
            priority=7,
            hard=True,
            grace_minutes=5,
            target_ref="requester",
            requires_structured_mechanics=False,
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
            replan_queue=NpcReplanQueue(),
            agents=agents,
            agendas={"responder": AgentAgendaProfile(commitments=(commitment,))},
        )
        action_ledger = WorldActionIntentLedger()
        action_ledger.records["request:1"] = WorldActionIntentRecord(
            action_id="request:1",
            agent_id="requester",
            intent_id="intent:request",
            intent_kind="REQUEST_ASSISTANCE",
            target_ref="responder",
            semantic_minute=10,
            trigger_ids=("trigger:request",),
            reason_codes=("NEEDS_SUPPORT",),
            source_type="SITUATIONAL",
            source_ref="warning:1",
        )
        action_ledger.records["response:1"] = WorldActionIntentRecord(
            action_id="response:1",
            agent_id="responder",
            intent_id="intent:accept",
            intent_kind="ACCEPT_ASSISTANCE_REQUEST",
            target_ref="requester",
            semantic_minute=20,
            trigger_ids=("trigger:response",),
            reason_codes=("CAN_HELP",),
            source_type="SITUATIONAL",
            source_ref="request:1",
        )
        commitment_ledger = AssistanceCommitmentLedger()
        commitment_ledger.add(
            AssistanceCommitmentRecord(
                commitment_id="commit:assist:1",
                request_action_id="request:1",
                response_action_id="response:1",
                response_event_id="event:response:1",
                responder_id="responder",
                requester_id="requester",
                intent_kind="ASSIST_ROUTE_INSPECTION",
                start_minute=40,
                end_minute=70,
                priority=7,
                hard=True,
                grace_minutes=5,
                required_knowledge=(),
                required_permissions=(),
                requires_local_projection=False,
                requires_structured_mechanics=False,
                provenance_root="response:1",
            )
        )
        return coordinator, channels, action_ledger, commitment_ledger

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(raw).hexdigest()

    def test_action_and_commitment_restore_as_one_generation(self):
        coordinator, channels, actions, commitments = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator,
            semantic_minute=30,
            action_ledger=actions,
            commitment_ledger=commitments,
        )
        restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.world.semantic_minute, 30)
        self.assertEqual(set(restored.action_ledger.records), {"request:1", "response:1"})
        self.assertIn("commit:assist:1", restored.commitment_ledger.records)
        agenda = restored.world.coordinator.agendas["responder"]
        self.assertEqual([row.commitment_id for row in agenda.commitments], ["commit:assist:1"])
        self.assertEqual(agenda.commitments[0].target_ref, "requester")

    def test_build_fails_if_commitment_is_not_in_responder_agenda(self):
        coordinator, _, actions, commitments = self._state()
        coordinator.agendas["responder"] = AgentAgendaProfile()
        with self.assertRaisesRegex(ValueError, "missing from responder agenda"):
            build_assistance_world_checkpoint(
                coordinator,
                semantic_minute=30,
                action_ledger=actions,
                commitment_ledger=commitments,
            )

    def test_build_fails_if_action_intent_is_from_future(self):
        coordinator, _, actions, commitments = self._state()
        row = actions.records["response:1"]
        actions.records["response:1"] = WorldActionIntentRecord(**{**row.__dict__, "semantic_minute": 31})
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            build_assistance_world_checkpoint(
                coordinator,
                semantic_minute=30,
                action_ledger=actions,
                commitment_ledger=commitments,
            )

    def test_outer_digest_rejects_mixed_generation(self):
        coordinator, channels, actions, commitments = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator,
            semantic_minute=30,
            action_ledger=actions,
            commitment_ledger=commitments,
        )
        corrupted = copy.deepcopy(checkpoint)
        corrupted["semantic_minute"] = 31
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_assistance_world_checkpoint(corrupted, channels=channels)

    def test_validly_redigested_generation_time_mismatch_fails_closed(self):
        coordinator, channels, actions, commitments = self._state()
        checkpoint = build_assistance_world_checkpoint(
            coordinator,
            semantic_minute=30,
            action_ledger=actions,
            commitment_ledger=commitments,
        )
        checkpoint["semantic_minute"] = 31
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "generation time"):
            restore_assistance_world_checkpoint(checkpoint, channels=channels)

    def test_core_has_no_authored_region_or_tactical_special_case(self):
        source = open("tools/global_npc_assistance_world_checkpoint.py", encoding="utf-8").read().lower()
        for forbidden in ("marea", "sendero", "knockback", "initiative", "damage roll", "move accuracy"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
