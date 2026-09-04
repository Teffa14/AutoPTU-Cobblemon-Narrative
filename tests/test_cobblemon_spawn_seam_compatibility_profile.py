import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "implementation" / "cobblemon-1.7.3-spawn-seam-compatibility-profile-v1.json"


class CobblemonSpawnSeamCompatibilityProfileTest(unittest.TestCase):
    def setUp(self):
        with PROFILE_PATH.open("r", encoding="utf-8") as handle:
            self.profile = json.load(handle)

    def test_profile_does_not_claim_runtime_pin(self):
        self.assertFalse(self.profile["upstream"]["ouros_runtime_dependency_pin_verified"])

    def test_spawn_event_scope_is_not_universal(self):
        primitive = next(item for item in self.profile["verified_primitives"] if item["id"] == "pokemon_entity_spawn_projection")
        self.assertEqual(primitive["scope"], "PokemonEntity instances on the BestSpawner path")
        self.assertIn(
            "POKEMON_ENTITY_SPAWN observes every PokemonEntity created by every system",
            self.profile["explicit_non_claims"],
        )

    def test_cancellation_order_is_source_verified(self):
        primitive = next(item for item in self.profile["verified_primitives"] if item["id"] == "single_entity_ordering")
        self.assertTrue(primitive["cancellation_before_world_add"])
        self.assertEqual(primitive["confidence"], "SOURCE_VERIFIED")

    def test_owned_send_out_is_separate_path(self):
        path = next(item for item in self.profile["path_matrix"] if item["path"] == "OWNED_PARTY_SEND_OUT")
        self.assertEqual(path["event_surface"], "POKEMON_SENT_PRE/POST")
        self.assertNotEqual(path["status"], "SOURCE_VERIFIED_AS_BESTSPAWNER")

    def test_unresolved_paths_remain_unresolved(self):
        paths = {item["path"]: item for item in self.profile["path_matrix"]}
        self.assertEqual(paths["ENTITY_LOAD_OR_RESTORE"]["status"], "UNRESOLVED")
        self.assertEqual(paths["COMMAND_CREATED"]["status"], "UNRESOLVED")
        self.assertEqual(paths["THIRD_PARTY_INTEGRATION"]["status"], "UNRESOLVED")

    def test_ouros_projection_requires_lease_before_token(self):
        sequence = self.profile["ouros_admission_path"]
        self.assertLess(sequence.index("reserve_projection_lease"), sequence.index("issue_one_use_admission_token"))
        self.assertLess(sequence.index("issue_one_use_admission_token"), sequence.index("receive_bestspawner_pokemon_spawn_callback"))


if __name__ == "__main__":
    unittest.main()
