import unittest

from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
)
from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
    checkout_with_holder_transition,
    execute_handoff_with_holder_transition,
    holder_history,
    record_holder_transition,
    return_with_holder_transition,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ResourceReservation,
)
from tools.global_npc_resources import ResourceState, WorldResource


class ResourceHolderTransitionTests(unittest.TestCase):
    def _resource(self, **overrides):
        values = {
            "resource_id": "resource:field-kit:1",
            "capability_refs": frozenset({"FIELD_SAMPLE_KIT"}),
            "location_ref": "place:depot",
        }
        values.update(overrides)
        return WorldResource(**values)

    def test_checkout_and_return_form_contiguous_holder_history(self):
        reservation = ResourceReservation(
            reservation_id="reservation:1",
            resource_id="resource:field-kit:1",
            actor_id="npc:iris",
            start_tick=10,
            end_tick=100,
        )
        reservation_ledger = ReservationLedger((reservation,))
        holder_ledger = ResourceHolderTransitionLedger()

        checked_out, holder_ledger, checkout = checkout_with_holder_transition(
            self._resource(),
            reservation_ledger,
            holder_ledger,
            actor_id="npc:iris",
            at_tick=20,
            transition_id="holder-transition:checkout:1",
        )
        self.assertEqual(checked_out.holder_actor_id, "npc:iris")
        self.assertEqual(checkout.kind, HolderTransitionKind.CHECKOUT)
        self.assertEqual(checkout.source_ref, "reservation:1")

        returned, holder_ledger, returned_event = return_with_holder_transition(
            checked_out,
            holder_ledger,
            actor_id="npc:iris",
            return_location_ref="place:ridge-depot",
            at_tick=55,
            transition_id="holder-transition:return:1",
        )
        self.assertIsNone(returned.holder_actor_id)
        self.assertEqual(returned.location_ref, "place:ridge-depot")
        self.assertEqual(returned_event.kind, HolderTransitionKind.RETURN)
        self.assertEqual(
            tuple(item.transition_id for item in holder_history(holder_ledger, returned.resource_id)),
            ("holder-transition:checkout:1", "holder-transition:return:1"),
        )

    def test_handoff_wrapper_records_same_authoritative_transfer(self):
        resource = self._resource(
            state=ResourceState.IN_USE,
            holder_actor_id="npc:iris",
            reserved_for_actor_id="npc:iris",
        )
        authorization = ResourceHandoffAuthorization(
            authorization_id="handoff-auth:1",
            request_id="request:1",
            provider_actor_id="npc:iris",
            accountable_actor_id="npc:iris",
            receiving_actor_id="npc:teo",
            resource_id=resource.resource_id,
            mode=HandoffMode.DELIVERY,
            handoff_location_ref="place:depot",
            valid_from_tick=30,
        )
        handoff_ledger = ResourceHandoffLedger(authorizations=(authorization,))
        holder_ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="holder-transition:checkout:1",
                    resource_id=resource.resource_id,
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc:iris",
                    at_tick=20,
                    location_ref="place:depot",
                    source_ref="reservation:1",
                ),
            )
        )
        transfer = ResourceCustodyTransfer(
            transfer_id="custody-transfer:1",
            authorization_id=authorization.authorization_id,
            request_id=authorization.request_id,
            resource_id=resource.resource_id,
            from_actor_id="npc:iris",
            to_actor_id="npc:teo",
            accountable_actor_id="npc:iris",
            location_ref="place:depot",
            at_tick=40,
        )

        result = execute_handoff_with_holder_transition(
            handoff_ledger,
            holder_ledger,
            resource,
            transfer,
            transition_id="holder-transition:handoff:1",
        )
        self.assertTrue(result.handoff.accepted)
        self.assertEqual(result.handoff.resource.holder_actor_id, "npc:teo")
        self.assertIsNotNone(result.holder_transition)
        self.assertEqual(result.holder_transition.source_ref, "custody-transfer:1")
        self.assertEqual(result.holder_transition.to_actor_id, "npc:teo")

    def test_failed_handoff_does_not_create_holder_event(self):
        resource = self._resource(
            state=ResourceState.IN_USE,
            holder_actor_id="npc:iris",
        )
        transfer = ResourceCustodyTransfer(
            transfer_id="custody-transfer:missing-auth",
            authorization_id="handoff-auth:missing",
            request_id="request:1",
            resource_id=resource.resource_id,
            from_actor_id="npc:iris",
            to_actor_id="npc:teo",
            accountable_actor_id="npc:iris",
            location_ref="place:depot",
            at_tick=40,
        )
        result = execute_handoff_with_holder_transition(
            ResourceHandoffLedger(),
            ResourceHolderTransitionLedger(),
            resource,
            transfer,
            transition_id="holder-transition:should-not-exist",
        )
        self.assertFalse(result.handoff.accepted)
        self.assertEqual(result.holder_ledger.transitions, ())
        self.assertIsNone(result.holder_transition)

    def test_journal_rejects_continuity_gap(self):
        ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="holder-transition:checkout:1",
                    resource_id="resource:field-kit:1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc:iris",
                    at_tick=10,
                ),
            )
        )
        with self.assertRaisesRegex(ValueError, "continuity"):
            record_holder_transition(
                ledger,
                ResourceHolderTransition(
                    transition_id="holder-transition:return:bad",
                    resource_id="resource:field-kit:1",
                    kind=HolderTransitionKind.RETURN,
                    from_actor_id="npc:teo",
                    to_actor_id=None,
                    at_tick=20,
                ),
            )

    def test_journal_rejects_backdated_transition(self):
        ledger = ResourceHolderTransitionLedger(
            transitions=(
                ResourceHolderTransition(
                    transition_id="holder-transition:checkout:1",
                    resource_id="resource:field-kit:1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc:iris",
                    at_tick=30,
                ),
            )
        )
        with self.assertRaisesRegex(ValueError, "semantic order"):
            record_holder_transition(
                ledger,
                ResourceHolderTransition(
                    transition_id="holder-transition:return:1",
                    resource_id="resource:field-kit:1",
                    kind=HolderTransitionKind.RETURN,
                    from_actor_id="npc:iris",
                    to_actor_id=None,
                    at_tick=20,
                ),
            )

    def test_kind_specific_actor_shapes_are_validated(self):
        with self.assertRaisesRegex(ValueError, "checkout"):
            ResourceHolderTransition(
                transition_id="holder-transition:bad",
                resource_id="resource:field-kit:1",
                kind=HolderTransitionKind.CHECKOUT,
                from_actor_id="npc:iris",
                to_actor_id="npc:teo",
                at_tick=1,
            )


if __name__ == "__main__":
    unittest.main()
