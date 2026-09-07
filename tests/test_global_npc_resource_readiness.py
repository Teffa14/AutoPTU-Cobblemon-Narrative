import inspect
import unittest

from tools.global_npc_ai import AgentMode, Handoff, NpcAgentState, NpcIntent
from tools.global_npc_resource_readiness import (
    OperationalReadinessRecord,
    OperationalReadinessStatus,
    effective_readiness_record,
    project_readiness_onto_resources,
)
from tools.global_npc_resources import (
    ResourceAwareIntent,
    ResourceRequirement,
    ResourceState,
    WorldResource,
    choose_resource_aware_intent,
)


class GlobalNpcResourceReadinessTests(unittest.TestCase):
    def setUp(self):
        self.agent = NpcAgentState(
            agent_id="fixture:npc:worker",
            mode=AgentMode.LOCAL_ACTIVE,
            region_ref="fixture:region:any",
            location_ref="fixture:site:work",
            knowledge=frozenset({"claim:task-known"}),
            permissions=frozenset({"WORK"}),
        )
        self.resource = WorldResource(
            "resource:meter:1",
            frozenset({"FIELD_METER"}),
            location_ref=self.agent.location_ref,
        )

    def record(self, status, tick=0, record_id="readiness:1", until=None):
        return OperationalReadinessRecord(
            record_id=record_id,
            resource_id=self.resource.resource_id,
            status=status,
            source_record_ref="maintenance:verification:fixture",
            effective_from_tick=tick,
            valid_until_tick=until,
        )

    def structured_intent(self):
        return ResourceAwareIntent(
            NpcIntent(
                intent_id="structured",
                kind="DO_FIELD_WORK",
                base_priority=10,
                required_knowledge=frozenset({"claim:task-known"}),
                required_permissions=frozenset({"WORK"}),
                requires_structured_mechanics=True,
            ),
            (ResourceRequirement("FIELD_METER"),),
        )

    def test_module_contains_no_local_fixture_names(self):
        import tools.global_npc_resource_readiness as module

        source = inspect.getsource(module).lower()
        for local_name in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(local_name, source)

    def test_ready_record_preserves_available_resource(self):
        result = project_readiness_onto_resources(
            [self.resource],
            [self.record(OperationalReadinessStatus.READY_FOR_AUTHORED_USE)],
            5,
            require_explicit_readiness=True,
        )
        self.assertEqual(result.resources[0].state, ResourceState.AVAILABLE)
        self.assertEqual(
            result.readiness_by_resource[self.resource.resource_id],
            OperationalReadinessStatus.READY_FOR_AUTHORED_USE,
        )

    def test_inspection_pending_blocks_planner_view(self):
        result = project_readiness_onto_resources(
            [self.resource],
            [self.record(OperationalReadinessStatus.INSPECTION_PENDING)],
            5,
        )
        self.assertEqual(result.resources[0].state, ResourceState.UNAVAILABLE)
        self.assertEqual(
            result.blocked_reason_by_resource[self.resource.resource_id],
            "RESOURCE_INSPECTION_PENDING",
        )

    def test_maintenance_and_out_of_service_are_blocking(self):
        for status in (
            OperationalReadinessStatus.MAINTENANCE,
            OperationalReadinessStatus.OUT_OF_SERVICE,
        ):
            with self.subTest(status=status):
                result = project_readiness_onto_resources(
                    [self.resource], [self.record(status)], 5
                )
                self.assertEqual(result.resources[0].state, ResourceState.UNAVAILABLE)

    def test_limited_is_conservative_in_v1(self):
        result = project_readiness_onto_resources(
            [self.resource],
            [self.record(OperationalReadinessStatus.LIMITED)],
            5,
        )
        self.assertEqual(result.resources[0].state, ResourceState.UNAVAILABLE)
        self.assertEqual(
            result.blocked_reason_by_resource[self.resource.resource_id],
            "RESOURCE_READINESS_LIMITED",
        )

    def test_missing_record_can_be_required_explicitly(self):
        result = project_readiness_onto_resources(
            [self.resource], [], 5, require_explicit_readiness=True
        )
        self.assertEqual(result.resources[0].state, ResourceState.UNAVAILABLE)
        self.assertEqual(
            result.blocked_reason_by_resource[self.resource.resource_id],
            "RESOURCE_READINESS_UNKNOWN",
        )

    def test_missing_record_remains_permissive_when_not_required(self):
        result = project_readiness_onto_resources([self.resource], [], 5)
        self.assertEqual(result.resources[0], self.resource)
        self.assertNotIn(self.resource.resource_id, result.readiness_by_resource)

    def test_latest_applicable_record_wins_deterministically(self):
        older = self.record(
            OperationalReadinessStatus.MAINTENANCE,
            tick=2,
            record_id="readiness:older",
        )
        newer = self.record(
            OperationalReadinessStatus.READY_FOR_AUTHORED_USE,
            tick=4,
            record_id="readiness:newer",
        )
        effective = effective_readiness_record(
            self.resource.resource_id, [newer, older], 5
        )
        self.assertEqual(effective, newer)

    def test_expired_record_does_not_author_current_readiness(self):
        expired = self.record(
            OperationalReadinessStatus.READY_FOR_AUTHORED_USE,
            tick=0,
            until=5,
        )
        result = project_readiness_onto_resources(
            [self.resource], [expired], 5, require_explicit_readiness=True
        )
        self.assertEqual(result.resources[0].state, ResourceState.UNAVAILABLE)
        self.assertEqual(
            result.blocked_reason_by_resource[self.resource.resource_id],
            "RESOURCE_READINESS_UNKNOWN",
        )

    def test_projection_preserves_source_reference_and_input_object(self):
        original = self.resource
        result = project_readiness_onto_resources(
            [original],
            [self.record(OperationalReadinessStatus.INSPECTION_PENDING)],
            5,
        )
        self.assertEqual(original.state, ResourceState.AVAILABLE)
        self.assertEqual(
            result.source_refs_by_resource[original.resource_id],
            "maintenance:verification:fixture",
        )

    def test_readiness_gate_blocks_autoptu_handoff(self):
        projection = project_readiness_onto_resources(
            [self.resource],
            [self.record(OperationalReadinessStatus.INSPECTION_PENDING)],
            5,
        )
        result = choose_resource_aware_intent(
            self.agent, [self.structured_intent()], projection.resources
        )
        self.assertEqual(result.decision.kind, "WAIT_RESOURCE")
        self.assertEqual(result.decision.handoff, Handoff.NONE)

    def test_ready_alternative_can_satisfy_existing_resource_gate(self):
        second = WorldResource(
            "resource:meter:2",
            frozenset({"FIELD_METER"}),
            location_ref=self.agent.location_ref,
        )
        records = [
            self.record(OperationalReadinessStatus.MAINTENANCE),
            OperationalReadinessRecord(
                "readiness:2",
                second.resource_id,
                OperationalReadinessStatus.READY_FOR_AUTHORED_USE,
                "maintenance:verification:second",
                0,
            ),
        ]
        projection = project_readiness_onto_resources(
            [self.resource, second], records, 5, require_explicit_readiness=True
        )
        result = choose_resource_aware_intent(
            self.agent, [self.structured_intent()], projection.resources
        )
        self.assertEqual(result.decision.handoff, Handoff.REQUEST_AUTOPTU)
        self.assertEqual(
            result.assessments_by_intent["structured"][0].resource_ids,
            ("resource:meter:2",),
        )


if __name__ == "__main__":
    unittest.main()
