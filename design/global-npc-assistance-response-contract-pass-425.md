# Global NPC assistance response contract — Pass 425

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

Pass 424 proves that a successfully delivered assistance request may wake only its explicit recipient. The delivered request still does not create acceptance, a commitment or a schedule mutation.

Pass 425 records the recipient's response as that actor's own durable world action.

Implemented owner

`tools/global_npc_assistance_response.py`

Entry point

`record_assistance_response_from_replan(...)`

Supported semantic responses

- `ACCEPT_ASSISTANCE_REQUEST`
- `DEFER_ASSISTANCE_REQUEST`
- `REJECT_ASSISTANCE_REQUEST`
- `COUNTERPROPOSE_ASSISTANCE_REQUEST`

The owner reuses `OUROS_WORLD_ACTION_INTENT_LEDGER_V1`. It does not create a second response-specific persistence system.

Admission chain

The originating action must exist, remain `PLANNED`, have semantic kind `REQUEST_ASSISTANCE`, and name another actor as recipient.

The referenced information envelope must still bind sender to requester and receiver to selected recipient.

The information queue must report terminal `DELIVERED`. The requester source claim must retain the original `action_id` as provenance root, its request subject and the originating request intent. The receiver claim must exist and retain the same provenance root.

The response `CoordinatedDecision` must belong to the delivered recipient and include the exact `replan:information:<event_id>` trigger created by delivery. The selected response must be one of the four supported response kinds, use ordinary world ownership with `Handoff.NONE`, and target the original requester.

A response action receives its own `action_id`. Reusing the request action identity is rejected.

Durability and idempotency

The response is written through `WorldActionIntentLedger.record_from_replan(...)`.

Exact replay returns the existing record. Reusing the same response action ID with different content fails closed.

Snapshot/restore of the world-action ledger preserves both the original request action and the recipient response action.

Agency boundary

A recorded ACCEPT is a durable choice. It is not a commitment, reservation, route, arrival or completed assistance.

A recorded DEFER has no automatic future wake until a later contract attaches an explicit time or condition.

A recorded REJECT does not automatically penalize a relationship.

A recorded COUNTERPROPOSE does not alter the requester's plan. The proposal must be communicated back before it can affect that actor.

No response mutates the original request record. Historical request and historical response remain separately queryable.

AutoPTU boundary

Response selection is world-agent policy and does not call AutoPTU.

The owner rejects a response decision that attempts to hide an `REQUEST_AUTOPTU` handoff inside the response record. If the accepted work later requires structured mechanics, a later world action must enter AutoPTU through the normal explicit handoff boundary.

Regression

`tests/test_global_npc_assistance_response.py` verifies all four semantic responses, exact actor ownership, exact delivery trigger, delivered-request requirement, requester reply target, AutoPTU-handoff rejection, provenance integrity, idempotent replay, conflicting reuse failure and snapshot durability.

Checkpoint boundary

The response uses `OUROS_WORLD_ACTION_INTENT_LEDGER_V1`, which still remains outside the coherent persistent-world checkpoint generation at this pass. Ledger-local snapshot durability is verified, but crash recovery across the complete world still requires checkpoint integration.

Next boundary

A response that should affect the requester needs an explicit reply-dispatch seam. ACCEPT should later create commitment/reservation state only through a separate owner. DEFER needs an explicit future time or condition before it can wake again. COUNTERPROPOSE needs an explicit proposal payload rather than overloading the original request intent.
