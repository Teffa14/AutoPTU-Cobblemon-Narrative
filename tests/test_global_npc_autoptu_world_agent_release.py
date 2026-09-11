import unittest

from tools.autoptu_session_identity import AutoPTUSessionLedger, AutoPTUSessionState
from tools.autoptu_world_agent_release import (
    release_world_agent_after_recorded_result,
    retire_session_after_world_release,
)
from tools.global_npc_ai import AgentMode, NpcAgentState, bind_autoptu


class AutoPTUWorldAgentReleaseTests(unittest.TestCase):
    def _resolved(self):
        ledger = AutoPTUSessionLedger()
        binding = ledger.request_session(
            handoff_request_id="handoff:pass417:1",
            world_action_ref="world-action:pass417:1",
            participant_refs=("npc:mara", "player:1"),
            rules_profile_id="ptu:standard",
            requested_at_minute=50,
        )
        ledger.bind_engine_session(binding.session_id, engine_session_ref="engine:pass417:1")
        ledger.record_authoritative_result(binding.session_id, result_ref="result:pass417:1")
        agent = bind_autoptu(
            NpcAgentState(
                agent_id="npc:mara",
                mode=AgentMode.LOCAL_ACTIVE,
                region_ref="ouros:marea",
                location_ref="ouros:marea-field-office",
            ),
            binding.session_id,
        )
        return ledger, binding.session_id, agent

    def test_release_clears_exact_binding_but_does_not_retire(self):
        ledger, session_id, agent = self._resolved()
        execution = release_world_agent_after_recorded_result(
            ledger=ledger,
            agent=agent,
            session_id=session_id,
            result_ref="result:pass417:1",
        )
        self.assertTrue(execution.changed)
        self.assertEqual(execution.agent.mode, AgentMode.LOCAL_ACTIVE)
        self.assertIsNone(execution.agent.active_autoptu_binding)
        self.assertEqual(ledger.get(session_id).state, AutoPTUSessionState.RESULT_RECORDED)

    def test_release_can_return_offscreen_named(self):
        ledger, session_id, agent = self._resolved()
        execution = release_world_agent_after_recorded_result(
            ledger=ledger,
            agent=agent,
            session_id=session_id,
            result_ref="result:pass417:1",
            local_after_release=False,
        )
        self.assertEqual(execution.agent.mode, AgentMode.OFFSCREEN_NAMED)

    def test_wrong_binding_fails_closed(self):
        ledger, session_id, agent = self._resolved()
        wrong = NpcAgentState(
            agent_id=agent.agent_id,
            mode=AgentMode.AUTOPTU_BOUND,
            region_ref=agent.region_ref,
            location_ref=agent.location_ref,
            active_autoptu_binding="autoptu.session.other",
        )
        with self.assertRaisesRegex(ValueError, "different AutoPTU session"):
            release_world_agent_after_recorded_result(
                ledger=ledger,
                agent=wrong,
                session_id=session_id,
                result_ref="result:pass417:1",
            )

    def test_wrong_result_fails_closed(self):
        ledger, session_id, agent = self._resolved()
        with self.assertRaisesRegex(ValueError, "does not match"):
            release_world_agent_after_recorded_result(
                ledger=ledger,
                agent=agent,
                session_id=session_id,
                result_ref="result:other",
            )

    def test_engine_bound_session_cannot_release_agent(self):
        ledger = AutoPTUSessionLedger()
        binding = ledger.request_session(
            handoff_request_id="handoff:pass417:unresolved",
            world_action_ref="world-action:pass417:unresolved",
            participant_refs=("npc:teo", "player:1"),
            rules_profile_id="ptu:standard",
            requested_at_minute=51,
        )
        ledger.bind_engine_session(binding.session_id, engine_session_ref="engine:pass417:unresolved")
        agent = bind_autoptu(
            NpcAgentState(
                agent_id="npc:teo",
                mode=AgentMode.LOCAL_ACTIVE,
                region_ref="ouros:marea",
                location_ref="ouros:sendero-del-vidrio",
            ),
            binding.session_id,
        )
        with self.assertRaisesRegex(ValueError, "RESULT_RECORDED"):
            release_world_agent_after_recorded_result(
                ledger=ledger,
                agent=agent,
                session_id=binding.session_id,
                result_ref="result:not-recorded",
            )

    def test_released_agent_plus_result_recorded_is_idempotent_restart_state(self):
        ledger, session_id, agent = self._resolved()
        first = release_world_agent_after_recorded_result(
            ledger=ledger,
            agent=agent,
            session_id=session_id,
            result_ref="result:pass417:1",
        )
        second = release_world_agent_after_recorded_result(
            ledger=ledger,
            agent=first.agent,
            session_id=session_id,
            result_ref="result:pass417:1",
        )
        self.assertFalse(second.changed)
        self.assertEqual(ledger.get(session_id).state, AutoPTUSessionState.RESULT_RECORDED)

    def test_retirement_requires_release_first(self):
        ledger, session_id, agent = self._resolved()
        with self.assertRaisesRegex(ValueError, "must be released"):
            retire_session_after_world_release(
                ledger=ledger,
                released_agent=agent,
                session_id=session_id,
                result_ref="result:pass417:1",
            )
        self.assertEqual(ledger.get(session_id).state, AutoPTUSessionState.RESULT_RECORDED)

    def test_retire_after_release_and_replay_is_idempotent(self):
        ledger, session_id, agent = self._resolved()
        released = release_world_agent_after_recorded_result(
            ledger=ledger,
            agent=agent,
            session_id=session_id,
            result_ref="result:pass417:1",
        ).agent
        retired = retire_session_after_world_release(
            ledger=ledger,
            released_agent=released,
            session_id=session_id,
            result_ref="result:pass417:1",
        )
        replay = retire_session_after_world_release(
            ledger=ledger,
            released_agent=released,
            session_id=session_id,
            result_ref="result:pass417:1",
        )
        self.assertEqual(retired.state, AutoPTUSessionState.RETIRED)
        self.assertEqual(replay.state, AutoPTUSessionState.RETIRED)

    def test_nonparticipant_cannot_release_or_retire_session(self):
        ledger, session_id, _ = self._resolved()
        outsider = NpcAgentState(
            agent_id="npc:outsider",
            mode=AgentMode.LOCAL_ACTIVE,
            region_ref="ouros:marea",
            location_ref="ouros:marea-field-office",
        )
        with self.assertRaisesRegex(ValueError, "not a participant"):
            release_world_agent_after_recorded_result(
                ledger=ledger,
                agent=outsider,
                session_id=session_id,
                result_ref="result:pass417:1",
            )
        with self.assertRaisesRegex(ValueError, "not a participant"):
            retire_session_after_world_release(
                ledger=ledger,
                released_agent=outsider,
                session_id=session_id,
                result_ref="result:pass417:1",
            )


if __name__ == "__main__":
    unittest.main()
