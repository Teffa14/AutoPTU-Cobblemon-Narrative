# Global NPC resource checkpoint foundation contract — Pass 353

Status: IMPLEMENTED FOUNDATION
Canon authority: NONE

## Purpose

Pass 353 begins closing the durability gap between the atomic world checkpoint and the resource/logistics layers added after that checkpoint was introduced.

The first bounded slice covers two existing owners:

- Pass 339 `ReservationLedger`
- Pass 342 `ResourceRequestLedger`

The codec lives in `tools/global_npc_resource_checkpoint.py`.

## Ownership boundary

The checkpoint layer may serialize, restore and validate persisted records. It may not reinterpret or execute them.

Reservation creation/closure remains owned by `global_npc_resource_reservations.py`.
Request submission and transitions remain owned by `global_npc_resource_requests.py`.
Resource physical state remains owned by `global_npc_resources.py`.
Later handoff, allocation and notification owners remain independent.

## V1 payload

`OUROS_NPC_RESOURCE_CHECKPOINT_V1` preserves:

- reservation identity, exact resource, actor, window, state and purpose reference;
- request identity, requester, provider, exact resource, creation/expiry time, quantity and purpose reference;
- request-event identity, request reference, actor, transition kind, event time, offered resource and reason reference.

Serialization order is deterministic.

## Restore invariants

Restore fails closed when:

- the schema is unknown;
- a persisted collection has the wrong structural type;
- reservation, request or event IDs are duplicated;
- a request event references a missing request;
- an event predates its request;
- an event actor is neither requester nor provider;
- a request or request event claims to exist after the world checkpoint semantic time when `validate_resource_checkpoint_time` is applied.

Dataclass constructors continue enforcing their native validation rules.

## Deliberate limitation

This pass does not yet insert the resource payload into `OUROS_NPC_WORLD_CHECKPOINT_V5`. The codec and regression suite are an isolated compatibility layer first. The next integration can advance the global checkpoint schema with smaller risk because resource round-trip and corruption behavior are already frozen independently.

Passes 343–352 remain outside this V1 resource bundle. They should be added incrementally rather than through a generic serializer that erases type-specific invariants.

## Replay principle

Restoring a reservation or request does not replay the business action. It reconstructs the ledger record so the original owner can derive current state from the same facts.

A restart cannot:

- create a new reservation;
- re-accept a request;
- change a resource holder;
- infer that a communication was delivered;
- promote a proposal to canon;
- create PTU battle effects.

## Test surface

`tests/test_global_npc_resource_checkpoint.py` covers deterministic round-trip, input-order normalization, orphan events, non-participant actors, future events, duplicate identity and unknown schema rejection.
