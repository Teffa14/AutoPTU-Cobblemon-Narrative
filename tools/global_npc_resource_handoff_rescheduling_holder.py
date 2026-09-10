from __future__ import annotations

from tools.global_npc_resource_handoff_rescheduling import (
    ResourceHandoffRescheduleLedger,
    current_authorization_id,
)
from tools.global_npc_resource_handoffs import (
    ResourceCustodyTransfer,
    ResourceHandoffLedger,
    ResourceHandoffResult,
)
from tools.global_npc_resource_holder_transitions import (
    HolderAwareHandoffResult,
    ResourceHolderTransitionLedger,
    execute_handoff_with_holder_transition,
)
from tools.global_npc_resources import WorldResource


def execute_current_authorized_handoff_with_holder_transition(
    reschedule_ledger: ResourceHandoffRescheduleLedger,
    handoff_ledger: ResourceHandoffLedger,
    holder_ledger: ResourceHolderTransitionLedger,
    resource: WorldResource,
    transfer: ResourceCustodyTransfer,
    *,
    transition_id: str,
) -> HolderAwareHandoffResult:
    """Execute only the current rescheduled authorization and journal holder mutation.

    The reschedule ledger owns which authorization remains operational. The handoff
    ledger owns custody authorization/transfer facts. The holder ledger records the
    resulting holder transition only after the underlying handoff is accepted.
    """
    current_id = current_authorization_id(reschedule_ledger, transfer.authorization_id)
    if current_id != transfer.authorization_id:
        authorization = next(
            (
                item
                for item in handoff_ledger.authorizations
                if item.authorization_id == transfer.authorization_id
            ),
            None,
        )
        rejected = ResourceHandoffResult(
            False,
            handoff_ledger,
            resource,
            authorization,
            reason_code="HANDOFF_AUTHORIZATION_SUPERSEDED",
        )
        return HolderAwareHandoffResult(rejected, holder_ledger)

    return execute_handoff_with_holder_transition(
        handoff_ledger,
        holder_ledger,
        resource,
        transfer,
        transition_id=transition_id,
    )
