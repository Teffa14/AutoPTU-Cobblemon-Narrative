import inspect
import unittest

from tools.global_npc_ai import AgentMode, Handoff, NpcAgentState, NpcIntent
from tools.global_npc_resources import (
    ResourceAwareIntent,
    ResourceRequirement,
    ResourceState,
    WorldResource,
    assess_requirement,
    choose_resource_aware_intent,
)


class GlobalNpcResourceTests(unittest.TestCase):
    def setUp(self):
        self.agent = NpcAgentState(
            agent_id="fixture:npc:worker",
            mode=AgentMode.LOCAL_ACTIVE,
            region_ref="fixture:region:any",
            location_ref="fixture:site:work",
            knowledge=frozenset({"claim:task-known"}),
            permissions=frozenset({"WORK"}),
        )
        self.req = ResourceRequirement("FIELD_SAMPLE_KIT")

    def wrap(self, intent_id="work", priority=5, structured=False):
        return ResourceAwareIntent(
            NpcIntent(
                intent_id=intent_id,
                kind="DO_FIELD_WORK",
                base_priority=priority,
                required_knowledge=frozenset({"claim:task-known"}),
                required_permissions=frozenset({"WORK"}),
                requires_structured_mechanics=structured,
            ),
            (self.req,),
        )

    def test_global_module_contains_no_local_fixture_names(self):
        import tools.global_npc_resources as module

        source = inspect.getsource(module).lower()
        for local_name in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(local_name, source)

    def test_known_and_permitted_task_still_blocks_when_resource_is_elsewhere(self):
        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            location_ref="fixture:site:storage",
        )
        result = choose_resource_aware_intent(self.agent, [self.wrap()], [resource])
        self.assertEqual(result.decision.kind, "WAIT_RESOURCE")
        assessment = result.assessments_by_intent["work"][0]
        self.assertFalse(assessment.satisfied)
        self.assertEqual(assessment.reason_code, "RESOURCE_NOT_LOCALLY_AVAILABLE")

    def test_local_available_resource_makes_intent_ready(self):
        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            location_ref=self.agent.location_ref,
        )
        result = choose_resource_aware_intent(self.agent, [self.wrap()], [resource])
        self.assertEqual(result.decision.kind, "DO_FIELD_WORK")
        self.assertEqual(result.ready_intent_ids, ("work",))

    def test_resource_reserved_for_other_actor_is_unavailable(self):
        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            state=ResourceState.RESERVED,
            location_ref=self.agent.location_ref,
            reserved_for_actor_id="fixture:npc:other",
        )
        assessment = assess_requirement(self.agent, self.req, [resource])
        self.assertFalse(assessment.satisfied)
        self.assertEqual(assessment.reason_code, "RESOURCE_RESERVED_FOR_OTHER_ACTOR")

    def test_resource_reserved_for_same_actor_is_ready(self):
        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            state=ResourceState.RESERVED,
            location_ref=self.agent.location_ref,
            reserved_for_actor_id=self.agent.agent_id,
        )
        assessment = assess_requirement(self.agent, self.req, [resource])
        self.assertTrue(assessment.satisfied)
        self.assertEqual(assessment.resource_ids, ("resource:kit:1",))

    def test_held_resource_is_ready_even_if_storage_location_differs(self):
        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            location_ref="fixture:site:storage",
            holder_actor_id=self.agent.agent_id,
        )
        assessment = assess_requirement(self.agent, self.req, [resource])
        self.assertTrue(assessment.satisfied)

    def test_insufficient_quantity_blocks(self):
        requirement = ResourceRequirement("SAMPLE_VIAL", quantity=3)
        resources = [
            WorldResource(
                "resource:vial:lot-a",
                frozenset({"SAMPLE_VIAL"}),
                quantity=2,
                location_ref=self.agent.location_ref,
            )
        ]
        assessment = assess_requirement(self.agent, requirement, resources)
        self.assertFalse(assessment.satisfied)
        self.assertEqual(assessment.reason_code, "INSUFFICIENT_RESOURCE_QUANTITY")

    def test_deterministic_allocation_uses_sorted_resource_ids(self):
        requirement = ResourceRequirement("SAMPLE_VIAL", quantity=2)
        resources = [
            WorldResource(
                "resource:vial:b",
                frozenset({"SAMPLE_VIAL"}),
                location_ref=self.agent.location_ref,
            ),
            WorldResource(
                "resource:vial:a",
                frozenset({"SAMPLE_VIAL"}),
                location_ref=self.agent.location_ref,
            ),
        ]
        assessment = assess_requirement(self.agent, requirement, resources)
        self.assertTrue(assessment.satisfied)
        self.assertEqual(assessment.resource_ids, ("resource:vial:a", "resource:vial:b"))

    def test_blocked_high_priority_intent_does_not_hide_ready_lower_priority_work(self):
        blocked = self.wrap("blocked", priority=20)
        ready_intent = ResourceAwareIntent(
            NpcIntent("ready", "DO_DESK_WORK", base_priority=2),
            (),
        )
        result = choose_resource_aware_intent(self.agent, [blocked, ready_intent], [])
        self.assertEqual(result.decision.intent_id, "ready")
        self.assertEqual(result.decision.kind, "DO_DESK_WORK")

    def test_autoptu_handoff_only_occurs_after_resource_gate_passes(self):
        wrapped = self.wrap("structured", priority=10, structured=True)
        blocked = choose_resource_aware_intent(self.agent, [wrapped], [])
        self.assertEqual(blocked.decision.handoff, Handoff.NONE)
        self.assertEqual(blocked.decision.kind, "WAIT_RESOURCE")

        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            location_ref=self.agent.location_ref,
        )
        ready = choose_resource_aware_intent(self.agent, [wrapped], [resource])
        self.assertEqual(ready.decision.handoff, Handoff.REQUEST_AUTOPTU)

    def test_depleted_resource_does_not_count_as_quantity(self):
        resource = WorldResource(
            "resource:kit:1",
            frozenset({"FIELD_SAMPLE_KIT"}),
            quantity=99,
            state=ResourceState.DEPLETED,
            location_ref=self.agent.location_ref,
        )
        result = choose_resource_aware_intent(self.agent, [self.wrap()], [resource])
        self.assertEqual(result.decision.kind, "WAIT_RESOURCE")


if __name__ == "__main__":
    unittest.main()
