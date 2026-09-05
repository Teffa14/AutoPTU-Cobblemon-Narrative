from pathlib import Path
import unittest

from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import BeliefStatus, KnowledgeLedger, evaluate_belief, record_direct_observation
from tools.global_npc_publication import (
    PublicAudienceMember,
    PublicPublication,
    expand_publication_bounded,
    replay_fixture,
    resolve_public_audience,
)


class GlobalNpcPublicationTest(unittest.TestCase):
    def setUp(self):
        self.ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in ("publisher", "a", "b", "c", "outside", "offline")}
        record_direct_observation(
            self.ledgers["publisher"],
            claim_id="source",
            subject="route.state",
            value="CLOSED",
            semantic_minute=10,
            confidence=95,
        )
        self.queue = InformationEventQueue(
            channels={"public": CommunicationChannel("public", "PUBLIC_BROADCAST", 2)},
            ledgers=self.ledgers,
        )
        self.publication = PublicPublication(
            publication_id="pub",
            publisher_id="publisher",
            source_claim_id="source",
            service_id="service",
            channel_id="public",
            published_minute=11,
            scope_ids=frozenset({"north"}),
            topic_id="alert",
            retention_until_minute=30,
        )
        self.members = (
            PublicAudienceMember("a", frozenset({"north"}), frozenset({"service"}), frozenset({"alert"})),
            PublicAudienceMember("b", frozenset({"north"}), frozenset({"service"}), frozenset({"alert"})),
            PublicAudienceMember("c", frozenset({"north"}), frozenset({"service"}), frozenset({"alert"})),
            PublicAudienceMember("outside", frozenset({"south"}), frozenset({"service"}), frozenset({"alert"})),
            PublicAudienceMember("offline", frozenset({"north"}), frozenset({"service"}), frozenset({"alert"}), False),
        )

    def test_publication_does_not_imply_universal_receipt(self):
        self.assertEqual(resolve_public_audience(self.publication, self.members, semantic_minute=11), ("a", "b", "c"))
        self.assertEqual(evaluate_belief(self.ledgers["outside"], "route.state").status, BeliefStatus.UNKNOWN)

    def test_bounded_expansion_uses_stable_cursor(self):
        first = expand_publication_bounded(publication=self.publication, members=self.members, semantic_minute=11, max_receivers=2, queue=self.queue)
        self.assertEqual(first.scheduled_agent_ids, ("a", "b"))
        self.assertEqual(first.next_cursor, "b")
        self.assertEqual(first.eligible_remaining, 1)
        second = expand_publication_bounded(publication=self.publication, members=self.members, semantic_minute=11, max_receivers=2, queue=self.queue, cursor_after_agent_id=first.next_cursor)
        self.assertEqual(second.scheduled_agent_ids, ("c",))
        self.assertIsNone(second.next_cursor)

    def test_receipt_is_delayed_and_private_to_eligible_receiver(self):
        expand_publication_bounded(publication=self.publication, members=(self.members[0],), semantic_minute=11, max_receivers=1, queue=self.queue)
        self.assertEqual(evaluate_belief(self.ledgers["a"], "route.state").status, BeliefStatus.UNKNOWN)
        self.queue.process_due(13)
        self.assertEqual(evaluate_belief(self.ledgers["a"], "route.state").status, BeliefStatus.SUPPORTED)
        self.assertEqual(evaluate_belief(self.ledgers["b"], "route.state").status, BeliefStatus.UNKNOWN)

    def test_expired_publication_has_no_new_audience(self):
        self.assertEqual(resolve_public_audience(self.publication, self.members, semantic_minute=31), ())

    def test_fixture_replays(self):
        result = replay_fixture(Path("implementation/global-npc-publication-broadcast-fixture-v1.json"))
        self.assertEqual(result["fixture_id"], "global-npc-publication-broadcast-v1")
        by_id = {row["event_id"]: row for row in result["results"]}
        self.assertEqual(by_id["expand.batch.1"]["scheduled_agent_ids"], ["listener.alpha", "listener.beta"])
        self.assertEqual(by_id["expand.batch.2"]["scheduled_agent_ids"], ["listener.gamma"])
        self.assertEqual(by_id["after.gamma"]["status"], "SUPPORTED")
        self.assertEqual(by_id["outside.unknown"]["status"], "UNKNOWN")
        self.assertEqual(by_id["offline.unknown"]["status"], "UNKNOWN")

    def test_core_is_region_neutral_and_non_tactical(self):
        source = Path("tools/global_npc_publication.py").read_text(encoding="utf-8")
        for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
            self.assertNotIn(forbidden, source)
        for forbidden in ("knockback", "initiative", "damage", "status_affliction", "move_id"):
            self.assertNotIn(forbidden, source.lower())


if __name__ == "__main__":
    unittest.main()
