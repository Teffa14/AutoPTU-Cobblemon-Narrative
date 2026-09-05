import unittest
from pathlib import Path

from tools.global_npc_audience import (
    AudienceCandidate,
    AudiencePolicy,
    resolve_audience,
    replay_fixture,
)
from tools.global_npc_social import FactionMembership, RelationshipState


class GlobalNpcAudienceTests(unittest.TestCase):
    def test_relationship_and_relevance_selective_contact(self):
        selection = resolve_audience(
            sender_id="a",
            candidates=(
                AudienceCandidate("b", ("voice",), proximity_band=2, topic_relevance=2),
                AudienceCandidate("c", ("message",), topic_relevance=1),
            ),
            relationships=(RelationshipState("a", "b", affinity=50, trust=60),),
            policy=AudiencePolicy(max_recipients=1),
        )
        self.assertEqual(selection.selected_agent_ids, ("b",))

    def test_shared_faction_alone_does_not_select(self):
        memberships = (
            FactionMembership("a", "f", "member"),
            FactionMembership("b", "f", "member"),
        )
        selection = resolve_audience(
            sender_id="a",
            candidates=(AudienceCandidate("b", ("message",)),),
            memberships=memberships,
            policy=AudiencePolicy(max_recipients=3, min_score=1),
        )
        self.assertEqual(selection.selected_agent_ids, ())
        self.assertIn(("b", "BELOW_THRESHOLD"), selection.rejected)

    def test_explicit_institutional_obligation_can_route(self):
        memberships = (
            FactionMembership("a", "f", "field"),
            FactionMembership("b", "f", "officer", commitment=80, obligation_tags=frozenset({"RECEIVE_REPORT"})),
        )
        selection = resolve_audience(
            sender_id="a",
            candidates=(AudienceCandidate("b", ("dispatch",)),),
            memberships=memberships,
            required_obligation_tag="RECEIVE_REPORT",
            policy=AudiencePolicy(max_recipients=1),
        )
        self.assertEqual(selection.selected_agent_ids, ("b",))

    def test_unreachable_recipient_is_rejected(self):
        selection = resolve_audience(
            sender_id="a",
            candidates=(AudienceCandidate("b", (), topic_relevance=10),),
        )
        self.assertEqual(selection.selected_agent_ids, ())
        self.assertIn(("b", "NO_REACHABLE_CHANNEL"), selection.rejected)

    def test_budget_caps_fanout_deterministically(self):
        selection = resolve_audience(
            sender_id="a",
            candidates=(
                AudienceCandidate("c", ("message",), topic_relevance=5),
                AudienceCandidate("b", ("message",), topic_relevance=5),
            ),
            policy=AudiencePolicy(max_recipients=1),
        )
        self.assertEqual(selection.selected_agent_ids, ("b",))
        self.assertIn(("c", "AUDIENCE_BUDGET"), selection.rejected)

    def test_fixture_replays(self):
        payload = replay_fixture(Path("implementation/global-npc-audience-resolution-fixture-v1.json"))
        self.assertEqual(payload["fixture_id"], "GLOBAL_NPC_AUDIENCE_RESOLUTION_V1")
        by_id = {row["scenario_id"]: row for row in payload["results"]}
        self.assertEqual(by_id["shared_faction_is_not_broadcast"]["selected_agent_ids"], ["agent.friend"])
        self.assertEqual(by_id["institutional_obligation_routes_report"]["selected_agent_ids"], ["agent.officer"])

    def test_core_is_region_neutral_and_not_tactical(self):
        source = Path("tools/global_npc_audience.py").read_text(encoding="utf-8")
        for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
            self.assertNotIn(forbidden, source)
        for forbidden in ("damage", "initiative", "knockback", "move_id", "status_affliction"):
            self.assertNotIn(forbidden, source.lower())


if __name__ == "__main__":
    unittest.main()
