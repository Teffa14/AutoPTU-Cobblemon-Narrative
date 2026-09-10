# Global NPC Rescheduled Handoff Legacy Closure Contract — Pass 401

Status: IMPLEMENTED / GLOBAL NPC RESOURCE SEAM
Canon effect: NONE

## Problem

Pass 400 introduced `execute_current_authorized_handoff_with_holder_transition()`, which validates current reschedule authority and journals every accepted holder mutation.

The older compatibility function `execute_current_authorized_handoff()` still called `execute_authorized_handoff()` directly for a current authorization. That meant one accepted rescheduled transfer could update `WorldResource.holder_actor_id` and custody history without producing `ResourceHolderTransition`.

## Pass 401 rule

The legacy compatibility function may validate reschedule authority, but it may no longer execute a current transfer.

Behavior:

- superseded authorization -> reject with `HANDOFF_AUTHORIZATION_SUPERSEDED`;
- current authorization -> reject with `HOLDER_TRANSITION_LEDGER_REQUIRED`;
- neither rejection may append custody history or mutate the resource.

Successful current execution must use `tools/global_npc_resource_handoff_rescheduling_holder.py::execute_current_authorized_handoff_with_holder_transition()`.

## Authority boundaries

`ResourceHandoffRescheduleLedger` owns replacement lineage and which authorization remains current.

`ResourceHandoffLedger` owns handoff authorization and custody-transfer facts.

`ResourceHolderTransitionLedger` owns explicit holder-transition history for journaled mutation paths.

`WorldResource` remains the present-state object.

No owner reconstructs missing events from another owner's current state.

## Coverage claim

Repository-wide search at Pass 401 found the known reschedule-specific direct execution bypass in the legacy compatibility function and no second production call site outside the holder-aware wrapper that invokes `execute_authorized_handoff()` after reschedule resolution.

Pass 401 closes that known reschedule-specific bypass.

This does not create a permanent universal guarantee for all future code. Any new holder mutation path must still be audited and routed through holder history before `complete_holder_history_resource_ids` can be broadened automatically.

## Regression requirement

The legacy executor must retain its superseded-authority rejection and must reject a valid current successor without mutating resource or custody state.

The Pass 400 holder-aware tests continue to prove the accepted path:

- current successor accepted;
- custody transfer recorded;
- holder changes to receiver;
- exactly one HANDOFF holder transition emitted with the transfer ID as provenance;
- rejected or stale transfers create no holder history.

## Mechanical boundary

This contract changes persistent-world resource provenance only. It grants no PTU Item effect, movement rule, Trainer Feature, Ability behavior, tactical objective policy or Minecraft authority.
