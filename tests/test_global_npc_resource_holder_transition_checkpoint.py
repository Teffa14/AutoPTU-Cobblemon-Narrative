import copy
import hashlib
import json
import unittest

from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
    record_holder_transition,
)
from tools.resource_holder_transition_checkpoint import (
    RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA,
    restore_resource_holder_transitions,
    snapshot_resource_holder_transitions,
)


def redigest(snapshot: dict) -> dict:
    payload = {key: value for key, value in snapshot.items() if key != "sha256"}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


class ResourceHolderTransitionCheckpointTests(unittest.TestCase):
    def _ledger(self) -> ResourceHolderTransitionLedger:
        ledger = ResourceHolderTransitionLedger()
        for transition in (
            ResourceHolderTransition(
                transition_id="meter-checkout",
                resource_id="survey-meter-4",
                kind=HolderTransitionKind.CHECKOUT,
                from_actor_id=None,
                to_actor_id="npc-ara",
                at_tick=10,
                location_ref="field-depot",
                source_ref="reservation-meter-4",
            ),
            ResourceHolderTransition(
                transition_id="meter-handoff",
                resource_id="survey-meter-4",
                kind=HolderTransitionKind.HANDOFF,
                from_actor_id="npc-ara",
                to_actor_id="npc-beto",
                at_tick=12,
                location_ref="ridge-station",
                source_ref="transfer-meter-4",
            ),
            ResourceHolderTransition(
                transition_id="meter-return",
                resource_id="survey-meter-4",
                kind=HolderTransitionKind.RETURN,
                from_actor_id="npc-beto",
                to_actor_id=None,
                at_tick=15,
                location_ref="field-depot",
            ),
        ):
            ledger = record_holder_transition(ledger, transition)
        return ledger

    def test_round_trip_preserves_transition_history_and_provenance(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=20)
        self.assertEqual(snapshot["schema"], RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA)

        restored = restore_resource_holder_transitions(snapshot, recovery_semantic_minute=20)
        self.assertEqual(restored.semantic_minute, 20)
        self.assertEqual(restored.ledger, self._ledger())
        self.assertEqual(restored.ledger.transitions[1].source_ref, "transfer-meter-4")

    def test_snapshot_is_deterministic_across_input_order_for_different_resources(self):
        first = ResourceHolderTransition(
            transition_id="z-checkout",
            resource_id="z-kit",
            kind=HolderTransitionKind.CHECKOUT,
            from_actor_id=None,
            to_actor_id="npc-zed",
            at_tick=4,
        )
        second = ResourceHolderTransition(
            transition_id="a-checkout",
            resource_id="a-kit",
            kind=HolderTransitionKind.CHECKOUT,
            from_actor_id=None,
            to_actor_id="npc-ana",
            at_tick=4,
        )
        left = ResourceHolderTransitionLedger((first, second))
        right = ResourceHolderTransitionLedger((second, first))
        self.assertEqual(
            snapshot_resource_holder_transitions(left, semantic_minute=8),
            snapshot_resource_holder_transitions(right, semantic_minute=8),
        )

    def test_snapshot_rejects_transition_later_than_its_semantic_cut(self):
        transition = ResourceHolderTransition(
            transition_id="future-checkout",
            resource_id="meter-1",
            kind=HolderTransitionKind.CHECKOUT,
            from_actor_id=None,
            to_actor_id="npc-a",
            at_tick=21,
        )
        with self.assertRaisesRegex(ValueError, "later than checkpoint semantic_minute"):
            snapshot_resource_holder_transitions(
                ResourceHolderTransitionLedger((transition,)),
                semantic_minute=20,
            )

    def test_restore_rejects_transition_later_than_cut_even_after_redigest(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=20)
        tampered = copy.deepcopy(snapshot)
        tampered["transitions"][-1]["at_tick"] = 21
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "later than checkpoint semantic_minute"):
            restore_resource_holder_transitions(tampered)

    def test_restore_rejects_tampering_without_redigest(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=20)
        tampered = copy.deepcopy(snapshot)
        tampered["transitions"][1]["to_actor_id"] = "npc-other"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_resource_holder_transitions(tampered)

    def test_restore_rejects_continuity_break_even_after_redigest(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=20)
        tampered = copy.deepcopy(snapshot)
        tampered["transitions"][1]["from_actor_id"] = "npc-other"
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "breaks resource holder continuity"):
            restore_resource_holder_transitions(tampered)

    def test_restore_rejects_duplicate_or_reversed_semantic_order_even_after_redigest(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=20)
        tampered = copy.deepcopy(snapshot)
        tampered["transitions"][1]["at_tick"] = 10
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "strictly increasing semantic order"):
            restore_resource_holder_transitions(tampered)

    def test_restore_rejects_noncanonical_cross_resource_order_after_redigest(self):
        ledger = ResourceHolderTransitionLedger(
            (
                ResourceHolderTransition(
                    transition_id="b-checkout",
                    resource_id="b-kit",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-b",
                    at_tick=1,
                ),
                ResourceHolderTransition(
                    transition_id="a-checkout",
                    resource_id="a-kit",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-a",
                    at_tick=1,
                ),
            )
        )
        snapshot = snapshot_resource_holder_transitions(ledger, semantic_minute=3)
        tampered = copy.deepcopy(snapshot)
        tampered["transitions"] = list(reversed(tampered["transitions"]))
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "canonical resource/time/id order"):
            restore_resource_holder_transitions(tampered)

    def test_restore_rejects_unknown_transition_kind_after_redigest(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=20)
        tampered = copy.deepcopy(snapshot)
        tampered["transitions"][0]["kind"] = "TELEPORT"
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "unknown holder transition kind"):
            restore_resource_holder_transitions(tampered)

    def test_restore_rejects_future_checkpoint_generation(self):
        snapshot = snapshot_resource_holder_transitions(self._ledger(), semantic_minute=21)
        with self.assertRaisesRegex(ValueError, "from the future"):
            restore_resource_holder_transitions(snapshot, recovery_semantic_minute=20)

    def test_snapshot_normalizes_existing_cross_resource_record_order(self):
        first = ResourceHolderTransition(
            transition_id="b-checkout",
            resource_id="b-kit",
            kind=HolderTransitionKind.CHECKOUT,
            from_actor_id=None,
            to_actor_id="npc-b",
            at_tick=1,
        )
        second = ResourceHolderTransition(
            transition_id="a-checkout",
            resource_id="a-kit",
            kind=HolderTransitionKind.CHECKOUT,
            from_actor_id=None,
            to_actor_id="npc-a",
            at_tick=1,
        )
        snapshot = snapshot_resource_holder_transitions(
            ResourceHolderTransitionLedger((first, second)),
            semantic_minute=3,
        )
        self.assertEqual(
            [item["resource_id"] for item in snapshot["transitions"]],
            ["a-kit", "b-kit"],
        )


if __name__ == "__main__":
    unittest.main()
