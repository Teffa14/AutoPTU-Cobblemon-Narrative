import copy
import hashlib
import json
import unittest

from tools.global_npc_resources import ResourceState, WorldResource
from tools.world_resource_catalog_checkpoint import (
    WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
    restore_world_resource_catalog,
    snapshot_world_resource_catalog,
)


def redigest(snapshot: dict) -> dict:
    payload = {key: value for key, value in snapshot.items() if key != "sha256"}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


class WorldResourceCatalogCheckpointTests(unittest.TestCase):
    def _resources(self):
        return (
            WorldResource(
                resource_id="repeater-7",
                capability_refs=frozenset({"FIELD_COMMS", "LONG_RANGE_COMMS"}),
                quantity=1,
                state=ResourceState.IN_USE,
                location_ref="ridge-station",
                holder_actor_id="npc-iris",
            ),
            WorldResource(
                resource_id="pump-2",
                capability_refs=frozenset({"WATER_PUMP"}),
                quantity=2,
                state=ResourceState.RESERVED,
                location_ref="depot-east",
                reserved_for_actor_id="npc-toma",
            ),
        )

    def test_round_trip_preserves_complete_current_resource_state(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=73)
        self.assertEqual(snapshot["schema"], WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA)

        restored = restore_world_resource_catalog(snapshot, recovery_semantic_minute=73)
        self.assertEqual(restored.semantic_minute, 73)
        self.assertEqual(restored.resources, tuple(sorted(self._resources(), key=lambda item: item.resource_id)))
        self.assertEqual(restored.by_id()["repeater-7"].holder_actor_id, "npc-iris")
        self.assertEqual(restored.by_id()["pump-2"].reserved_for_actor_id, "npc-toma")

    def test_snapshot_is_deterministic_across_input_order_and_capability_order(self):
        resources = self._resources()
        reversed_repeater = WorldResource(
            resource_id="repeater-7",
            capability_refs=frozenset(["LONG_RANGE_COMMS", "FIELD_COMMS"]),
            quantity=1,
            state=ResourceState.IN_USE,
            location_ref="ridge-station",
            holder_actor_id="npc-iris",
        )
        alternate = snapshot_world_resource_catalog(
            (resources[1], reversed_repeater),
            semantic_minute=73,
        )
        original = snapshot_world_resource_catalog(resources, semantic_minute=73)
        self.assertEqual(alternate, original)

    def test_snapshot_rejects_duplicate_resource_ids(self):
        duplicate = WorldResource(
            resource_id="pump-2",
            capability_refs=frozenset({"BACKUP_PUMP"}),
        )
        with self.assertRaisesRegex(ValueError, "duplicate world resource id"):
            snapshot_world_resource_catalog((*self._resources(), duplicate), semantic_minute=73)

    def test_restore_rejects_tampering_without_redigest(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=73)
        tampered = copy.deepcopy(snapshot)
        tampered["resources"][0]["location_ref"] = "unknown-yard"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_world_resource_catalog(tampered)

    def test_restore_rejects_unknown_state_even_after_redigest(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=73)
        tampered = copy.deepcopy(snapshot)
        tampered["resources"][0]["state"] = "TELEPORTED"
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "unknown world resource state"):
            restore_world_resource_catalog(tampered)

    def test_restore_rejects_noncanonical_record_order_even_after_redigest(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=73)
        tampered = copy.deepcopy(snapshot)
        tampered["resources"] = list(reversed(tampered["resources"]))
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "canonical resource-id order"):
            restore_world_resource_catalog(tampered)

    def test_restore_rejects_future_catalog_generation(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=74)
        with self.assertRaisesRegex(ValueError, "from the future"):
            restore_world_resource_catalog(snapshot, recovery_semantic_minute=73)

    def test_catalog_snapshot_does_not_claim_custody_history(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=73)
        serialized = json.dumps(snapshot)
        self.assertNotIn("transfer_id", serialized)
        self.assertNotIn("authorization_id", serialized)
        self.assertNotIn("request_id", serialized)
        self.assertNotIn("condition_ref", serialized)

    def test_restore_rejects_duplicate_capability_refs_after_redigest(self):
        snapshot = snapshot_world_resource_catalog(self._resources(), semantic_minute=73)
        tampered = copy.deepcopy(snapshot)
        tampered["resources"][1]["capability_refs"] = ["FIELD_COMMS", "FIELD_COMMS"]
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "capability refs must be unique"):
            restore_world_resource_catalog(tampered)


if __name__ == "__main__":
    unittest.main()
