import copy
import unittest

from tools.global_npc_site_evidence import ObservationKind, SiteAccessState, SiteEvidenceLedger


class GlobalNpcSiteEvidenceTests(unittest.TestCase):
    def _ledger(self):
        ledger = SiteEvidenceLedger()
        ledger.record_revision(
            revision_id="site.alpha:r1",
            site_id="site.alpha",
            semantic_minute=10,
            access_state=SiteAccessState.OPEN,
            change_kind="BASELINE_DOCUMENTED",
            source_ref="survey:first",
        )
        ledger.record_observation(
            observation_id="obs.upper-floor",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=12,
            evidence_ref="feature.upper-floor",
            kind=ObservationKind.FIXED_FEATURE,
            content="Visible floor aligns with the upper chamber walls.",
            provenance_root="field-note:upper-floor",
        )
        return ledger

    def test_revision_observation_and_interpretation_round_trip(self):
        ledger = self._ledger()
        ledger.record_interpretation(
            interpretation_id="interp.upper-room",
            site_id="site.alpha",
            actor_id="researcher.a",
            semantic_minute=13,
            observation_ids=("obs.upper-floor",),
            claim="The visible floor belongs to the upper room phase.",
            confidence=0.7,
        )
        restored = SiteEvidenceLedger.restore(ledger.snapshot())
        self.assertEqual(restored.snapshot(), ledger.snapshot())

    def test_later_revision_preserves_earlier_observation(self):
        ledger = self._ledger()
        ledger.record_revision(
            revision_id="site.alpha:r2",
            site_id="site.alpha",
            previous_revision_id="site.alpha:r1",
            semantic_minute=30,
            access_state=SiteAccessState.RESTRICTED,
            change_kind="LOWER_MASONRY_EXPOSED",
            source_ref="event:floor-exposure",
        )
        ledger.record_observation(
            observation_id="obs.lower-wall",
            site_id="site.alpha",
            revision_id="site.alpha:r2",
            observer_id="researcher.b",
            semantic_minute=31,
            evidence_ref="feature.lower-wall",
            kind=ObservationKind.SPATIAL_RELATIONSHIP,
            content="Lower masonry is misaligned with the visible upper room.",
            provenance_root="field-note:lower-wall",
        )
        self.assertEqual(ledger.observations["obs.upper-floor"].revision_id, "site.alpha:r1")
        self.assertEqual(ledger.observations["obs.lower-wall"].revision_id, "site.alpha:r2")

    def test_interpretation_cannot_use_future_observation(self):
        ledger = self._ledger()
        with self.assertRaisesRegex(ValueError, "future observation"):
            ledger.record_interpretation(
                interpretation_id="interp.bad",
                site_id="site.alpha",
                actor_id="researcher.a",
                semantic_minute=11,
                observation_ids=("obs.upper-floor",),
                claim="Premature conclusion",
                confidence=0.4,
            )

    def test_interpretation_cannot_mix_sites(self):
        ledger = self._ledger()
        ledger.record_revision(
            revision_id="site.beta:r1",
            site_id="site.beta",
            semantic_minute=8,
            access_state=SiteAccessState.OPEN,
            change_kind="BASELINE_DOCUMENTED",
            source_ref="survey:beta",
        )
        ledger.record_observation(
            observation_id="obs.beta",
            site_id="site.beta",
            revision_id="site.beta:r1",
            observer_id="researcher.b",
            semantic_minute=9,
            evidence_ref="feature.beta",
            kind=ObservationKind.FIXED_FEATURE,
            content="Independent feature at another site.",
            provenance_root="field-note:beta",
        )
        with self.assertRaisesRegex(ValueError, "cannot mix sites"):
            ledger.record_interpretation(
                interpretation_id="interp.mix",
                site_id="site.alpha",
                actor_id="researcher.a",
                semantic_minute=20,
                observation_ids=("obs.upper-floor", "obs.beta"),
                claim="Invalid cross-site flattening",
                confidence=0.5,
            )

    def test_revision_history_cannot_fork(self):
        ledger = self._ledger()
        ledger.record_revision(
            revision_id="site.alpha:r2",
            site_id="site.alpha",
            previous_revision_id="site.alpha:r1",
            semantic_minute=20,
            access_state=SiteAccessState.OPEN,
            change_kind="FIRST_CHANGE",
            source_ref="event:first",
        )
        with self.assertRaisesRegex(ValueError, "cannot fork"):
            ledger.record_revision(
                revision_id="site.alpha:r2b",
                site_id="site.alpha",
                previous_revision_id="site.alpha:r1",
                semantic_minute=21,
                access_state=SiteAccessState.OPEN,
                change_kind="CONTRADICTORY_BRANCH",
                source_ref="event:second",
            )

    def test_superseding_interpretation_does_not_mutate_observation(self):
        ledger = self._ledger()
        ledger.record_interpretation(
            interpretation_id="interp.first",
            site_id="site.alpha",
            actor_id="researcher.a",
            semantic_minute=13,
            observation_ids=("obs.upper-floor",),
            claim="Single construction phase.",
            confidence=0.6,
        )
        original_observation = copy.deepcopy(ledger.observations["obs.upper-floor"])
        ledger.record_interpretation(
            interpretation_id="interp.revised",
            site_id="site.alpha",
            actor_id="researcher.a",
            semantic_minute=14,
            observation_ids=("obs.upper-floor",),
            claim="Upper floor evidence alone cannot establish a single phase.",
            confidence=0.8,
            supersedes_id="interp.first",
        )
        self.assertEqual(ledger.observations["obs.upper-floor"], original_observation)

    def test_future_evidence_rejected_by_world_time_validation(self):
        ledger = self._ledger()
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            ledger.validate(semantic_minute=11)


if __name__ == "__main__":
    unittest.main()
