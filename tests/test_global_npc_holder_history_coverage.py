import unittest

from tools.global_npc_holder_history_coverage import (
    HolderHistoryCoverageBaseline,
    derive_bounded_holder_history_coverage,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
)
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_resources import ResourceState, WorldResource
from tools.world_resource_history_reconciliation import reconcile_world_resource_history


class GlobalNpcHolderHistoryCoverageTests(unittest.TestCase):
    def test_baseline_replays_only_later_transitions(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.IN_USE,
            holder_actor_id="npc-c",
        )
        ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="old-checkout",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-a",
                    at_tick=5,
                ),
                ResourceHolderTransition(
                    transition_id="later-handoff",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.HANDOFF,
                    from_actor_id="npc-b",
                    to_actor_id="npc-c",
                    at_tick=20,
                ),
            )
        )
        baseline = HolderHistoryCoverageBaseline(
            baseline_id="baseline-15",
            resource_id="meter-1",
            at_tick=15,
            holder_actor_id="npc-b",
            source_ref="catalog-checkpoint-15",
        )

        coverage = derive_bounded_holder_history_coverage(
            (resource,),
            (baseline,),
            ledger,
            through_tick=25,
        )

        self.assertEqual(len(coverage), 1)
        self.assertEqual(coverage[0].expected_holder_actor_id, "npc-c")
        self.assertEqual(
            coverage[0].evidence_refs,
            ("catalog-checkpoint-15", "baseline-15", "later-handoff"),
        )

    def test_baseline_conflicting_with_later_journal_fails_closed(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
        )
        ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="handoff-1",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.HANDOFF,
                    from_actor_id="npc-a",
                    to_actor_id="npc-b",
                    at_tick=20,
                ),
            )
        )
        baseline = HolderHistoryCoverageBaseline(
            baseline_id="baseline-15",
            resource_id="meter-1",
            at_tick=15,
            holder_actor_id="npc-x",
            source_ref="catalog-checkpoint-15",
        )

        with self.assertRaisesRegex(ValueError, "conflicts with journal continuity"):
            derive_bounded_holder_history_coverage(
                (resource,),
                (baseline,),
                ledger,
                through_tick=25,
            )

    def test_reconciliation_confirms_current_holder_from_bounded_baseline(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.IN_USE,
            holder_actor_id="npc-c",
        )
        ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="old-checkout",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-a",
                    at_tick=5,
                ),
                ResourceHolderTransition(
                    transition_id="later-handoff",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.HANDOFF,
                    from_actor_id="npc-b",
                    to_actor_id="npc-c",
                    at_tick=20,
                ),
            )
        )
        baseline = HolderHistoryCoverageBaseline(
            baseline_id="baseline-15",
            resource_id="meter-1",
            at_tick=15,
            holder_actor_id="npc-b",
            source_ref="catalog-checkpoint-15",
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            semantic_minute=25,
            holder_transition_ledger=ledger,
            holder_history_coverage_baselines=(baseline,),
        )

        matches = [
            finding
            for finding in report.confirmed
            if finding.reason_code == "CURRENT_HOLDER_MATCHES_BOUNDED_HOLDER_HISTORY"
        ]
        self.assertEqual(len(matches), 1)
        self.assertTrue(report.safe_to_restore)

    def test_reconciliation_rejects_current_holder_that_conflicts_with_bounded_baseline(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.IN_USE,
            holder_actor_id="npc-x",
        )
        ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="handoff-1",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.HANDOFF,
                    from_actor_id="npc-b",
                    to_actor_id="npc-c",
                    at_tick=20,
                ),
            )
        )
        baseline = HolderHistoryCoverageBaseline(
            baseline_id="baseline-15",
            resource_id="meter-1",
            at_tick=15,
            holder_actor_id="npc-b",
            source_ref="catalog-checkpoint-15",
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            semantic_minute=25,
            holder_transition_ledger=ledger,
            holder_history_coverage_baselines=(baseline,),
        )

        self.assertFalse(report.safe_to_restore)
        self.assertEqual(
            report.conflicts[0].reason_code,
            "CURRENT_HOLDER_CONFLICTS_BOUNDED_HOLDER_HISTORY",
        )

    def test_future_or_unknown_baseline_fails_closed(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
        )
        future = HolderHistoryCoverageBaseline(
            baseline_id="future",
            resource_id="meter-1",
            at_tick=30,
            holder_actor_id=None,
            source_ref="checkpoint-30",
        )
        with self.assertRaisesRegex(ValueError, "later than requested coverage cut"):
            derive_bounded_holder_history_coverage(
                (resource,),
                (future,),
                ResourceHolderTransitionLedger(),
                through_tick=25,
            )

        unknown = HolderHistoryCoverageBaseline(
            baseline_id="unknown",
            resource_id="missing-meter",
            at_tick=10,
            holder_actor_id=None,
            source_ref="checkpoint-10",
        )
        with self.assertRaisesRegex(ValueError, "absent from current catalog"):
            derive_bounded_holder_history_coverage(
                (resource,),
                (unknown,),
                ResourceHolderTransitionLedger(),
                through_tick=25,
            )

    def test_legacy_complete_ids_cannot_be_combined_with_bounded_baselines(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
        )
        baseline = HolderHistoryCoverageBaseline(
            baseline_id="baseline-10",
            resource_id="meter-1",
            at_tick=10,
            holder_actor_id=None,
            source_ref="checkpoint-10",
        )
        with self.assertRaisesRegex(ValueError, "not both"):
            reconcile_world_resource_history(
                (resource,),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                semantic_minute=20,
                holder_transition_ledger=ResourceHolderTransitionLedger(),
                complete_holder_history_resource_ids=frozenset({"meter-1"}),
                holder_history_coverage_baselines=(baseline,),
            )


if __name__ == "__main__":
    unittest.main()
