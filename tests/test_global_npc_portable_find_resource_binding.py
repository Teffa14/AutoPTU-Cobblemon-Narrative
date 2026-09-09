import copy
import unittest

from tools.global_npc_portable_find_resource_binding import PortableFindResourceBindingLedger
from tools.global_npc_resources import ResourceState, WorldResource
from tools.global_npc_site_evidence import ObservationKind, SiteAccessState, SiteEvidenceLedger


class GlobalNpcPortableFindResourceBindingTests(unittest.TestCase):
    def _site_evidence(self, *, kind=ObservationKind.PORTABLE_FIND, content="A tagged ceramic fragment rests in the exposed layer."):
        ledger = SiteEvidenceLedger()
        ledger.record_revision(
            revision_id="site.alpha:r1",
            site_id="site.alpha",
            semantic_minute=10,
            access_state=SiteAccessState.OPEN,
            change_kind="BASELINE_DOCUMENTED",
            source_ref="survey:alpha",
        )
        ledger.record_observation(
            observation_id="obs.find.alpha",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=12,
            evidence_ref="find.field-number.17",
            kind=kind,
            content=content,
            provenance_root="field-note:alpha:17",
        )
        return ledger

    def _resources(self, **overrides):
        values = {
            "resource_id": "resource.find.alpha",
            "capability_refs": frozenset({"portable_find"}),
            "quantity": 1,
            "state": ResourceState.AVAILABLE,
            "location_ref": "site.alpha",
            "holder_actor_id": None,
            "reserved_for_actor_id": None,
        }
        values.update(overrides)
        resource = WorldResource(**values)
        return {resource.resource_id: resource}

    def _bound(self):
        evidence = self._site_evidence()
        resources = self._resources()
        ledger = PortableFindResourceBindingLedger()
        ledger.bind(
            binding_id="binding.find.alpha",
            observation_id="obs.find.alpha",
            resource_id="resource.find.alpha",
            bound_at_semantic_minute=13,
            bound_by_actor_id="researcher.a",
            authority_ref="field-register:alpha",
            site_evidence=evidence,
            declared_resources=resources,
        )
        return ledger, evidence, resources

    def test_portable_find_binding_round_trip(self):
        ledger, evidence, resources = self._bound()
        snapshot = ledger.snapshot(
            site_evidence=evidence,
            declared_resources=resources,
            semantic_minute=20,
        )
        restored = PortableFindResourceBindingLedger.restore(
            snapshot,
            site_evidence=evidence,
            declared_resources=resources,
            semantic_minute=20,
        )
        self.assertEqual(
            restored.snapshot(
                site_evidence=evidence,
                declared_resources=resources,
                semantic_minute=20,
            ),
            snapshot,
        )
        self.assertEqual(restored.binding_for_observation("obs.find.alpha").resource_id, "resource.find.alpha")
        self.assertEqual(restored.binding_for_resource("resource.find.alpha").observation_id, "obs.find.alpha")

    def test_binding_requires_portable_find_observation(self):
        evidence = self._site_evidence(kind=ObservationKind.FIXED_FEATURE)
        with self.assertRaisesRegex(ValueError, "PORTABLE_FIND"):
            PortableFindResourceBindingLedger().bind(
                binding_id="binding.bad",
                observation_id="obs.find.alpha",
                resource_id="resource.find.alpha",
                bound_at_semantic_minute=13,
                bound_by_actor_id="researcher.a",
                authority_ref="field-register:alpha",
                site_evidence=evidence,
                declared_resources=self._resources(),
            )

    def test_binding_requires_declared_world_resource(self):
        evidence = self._site_evidence()
        with self.assertRaisesRegex(ValueError, "missing world resource"):
            PortableFindResourceBindingLedger().bind(
                binding_id="binding.bad",
                observation_id="obs.find.alpha",
                resource_id="resource.missing",
                bound_at_semantic_minute=13,
                bound_by_actor_id="researcher.a",
                authority_ref="field-register:alpha",
                site_evidence=evidence,
                declared_resources=self._resources(),
            )

    def test_binding_cannot_predate_observation(self):
        evidence = self._site_evidence()
        with self.assertRaisesRegex(ValueError, "cannot predate"):
            PortableFindResourceBindingLedger().bind(
                binding_id="binding.bad",
                observation_id="obs.find.alpha",
                resource_id="resource.find.alpha",
                bound_at_semantic_minute=11,
                bound_by_actor_id="researcher.a",
                authority_ref="field-register:alpha",
                site_evidence=evidence,
                declared_resources=self._resources(),
            )

    def test_one_observation_and_one_resource_each_have_one_binding(self):
        ledger, evidence, resources = self._bound()
        resources = dict(resources)
        resources["resource.find.beta"] = WorldResource(
            resource_id="resource.find.beta",
            capability_refs=frozenset({"portable_find"}),
        )
        with self.assertRaisesRegex(ValueError, "observation is already bound"):
            ledger.bind(
                binding_id="binding.second-observation",
                observation_id="obs.find.alpha",
                resource_id="resource.find.beta",
                bound_at_semantic_minute=14,
                bound_by_actor_id="researcher.a",
                authority_ref="field-register:alpha",
                site_evidence=evidence,
                declared_resources=resources,
            )

        evidence.record_observation(
            observation_id="obs.find.beta",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=14,
            evidence_ref="find.field-number.18",
            kind=ObservationKind.PORTABLE_FIND,
            content="A second tagged fragment is documented separately.",
            provenance_root="field-note:alpha:18",
        )
        with self.assertRaisesRegex(ValueError, "already bound to another portable find"):
            ledger.bind(
                binding_id="binding.second-resource",
                observation_id="obs.find.beta",
                resource_id="resource.find.alpha",
                bound_at_semantic_minute=15,
                bound_by_actor_id="researcher.a",
                authority_ref="field-register:alpha",
                site_evidence=evidence,
                declared_resources=resources,
            )

    def test_restore_detects_changed_observation_provenance(self):
        ledger, evidence, resources = self._bound()
        snapshot = ledger.snapshot(site_evidence=evidence, declared_resources=resources)
        altered_evidence = self._site_evidence(content="The same observation ID now carries different field content.")
        with self.assertRaisesRegex(ValueError, "observation provenance mismatch"):
            PortableFindResourceBindingLedger.restore(
                snapshot,
                site_evidence=altered_evidence,
                declared_resources=resources,
            )

    def test_restore_rejects_binding_from_future(self):
        ledger, evidence, resources = self._bound()
        snapshot = ledger.snapshot(site_evidence=evidence, declared_resources=resources)
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            PortableFindResourceBindingLedger.restore(
                snapshot,
                site_evidence=evidence,
                declared_resources=resources,
                semantic_minute=12,
            )

    def test_binding_does_not_freeze_or_mutate_operational_resource_state(self):
        ledger, evidence, resources = self._bound()
        original_resource = copy.deepcopy(resources["resource.find.alpha"])
        snapshot = ledger.snapshot(site_evidence=evidence, declared_resources=resources)
        self.assertEqual(resources["resource.find.alpha"], original_resource)

        moved_resources = self._resources(
            state=ResourceState.IN_USE,
            location_ref="archive.receiving",
            holder_actor_id="curator.b",
        )
        restored = PortableFindResourceBindingLedger.restore(
            snapshot,
            site_evidence=evidence,
            declared_resources=moved_resources,
            semantic_minute=30,
        )
        self.assertEqual(restored.binding_for_resource("resource.find.alpha").observation_id, "obs.find.alpha")
        self.assertEqual(moved_resources["resource.find.alpha"].holder_actor_id, "curator.b")
        self.assertEqual(moved_resources["resource.find.alpha"].location_ref, "archive.receiving")

    def test_snapshot_rejects_resource_catalog_key_identity_mismatch(self):
        ledger, evidence, resources = self._bound()
        mismatched = {
            "resource.find.alpha": WorldResource(
                resource_id="resource.other",
                capability_refs=frozenset({"portable_find"}),
            )
        }
        with self.assertRaisesRegex(ValueError, "key does not match"):
            ledger.snapshot(site_evidence=evidence, declared_resources=mismatched)


if __name__ == "__main__":
    unittest.main()
