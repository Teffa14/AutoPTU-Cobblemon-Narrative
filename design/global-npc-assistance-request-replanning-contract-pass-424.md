# Global NPC assistance request replanning contract — Pass 424

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

Pass 423 can turn one durable `REQUEST_ASSISTANCE` world action into one explicit information envelope. It deliberately stops before delivery-to-replanning.

Pass 424 binds that envelope to the existing `GlobalNpcWorldEventCoordinator` so only a successfully delivered request may create a `KNOWLEDGE_DELIVERED` wake for the selected recipient.

Implemented owner

`tools/global_npc_assistance_request_replanning.py`

Entry points

`advance_assistance_request_for_replanning(...)`

`acknowledge_assistance_request_for_replanning(...)`

Admission and provenance

The world action must exist, remain `PLANNED`, have semantic kind `REQUEST_ASSISTANCE`, and name another actor as explicit target.

The queue must still own the referenced envelope. Envelope sender must equal the actor who made the world decision. Envelope receiver must equal the action's target.

The sender-side source claim must exist and retain all three causal bindings established by Pass 423: provenance root equals `action_id`, subject equals `assistance_request:<action_id>`, and value equals the originating `intent_id`.

A mismatch fails before delivery is advanced.

Selective wake behavior

The bridge delegates ordinary delivery and wake materialization to `GlobalNpcWorldEventCoordinator`.

`DELIVERED` may create the normal `replan:information:<event_id>` trigger for the named recipient.

`QUEUED`, delivery-budget deferral, `FAILED_CHANNEL_UNAVAILABLE` and `WAITING_LOCAL_ACK` do not create a recipient decision.

A local-projection ACK creates a wake only when the ACK is accepted and ordinary information delivery becomes terminal `DELIVERED`. Rejection creates no new knowledge and no replan.

The bridge filters returned decisions to the explicit recipient and the exact information trigger. An unrelated actor with an otherwise compatible agenda does not gain the claim, provenance root or wake.

Agency boundary

A replanning decision after receipt is still only the recipient's selected agenda decision.

Pass 424 does not mark the original request accepted. It does not create a commitment, reservation, travel plan, task assignment, relationship change or reciprocal message.

The intended next durable boundary is to represent ACCEPT / DEFER / REJECT / COUNTERPROPOSE as the recipient's own world action or equivalent durable choice. If the requester must learn that choice, the reply must travel through ordinary communication rather than shared institutional state.

AutoPTU boundary

This owner does not call AutoPTU. It does not interpret battle payloads or infer PTU capability from narrative roles.

If a received request later leads to structured tactical resolution, exact capability families must be admitted independently. Current live engine evidence does not justify promoting any family from one representative implementation.

Regression

`tests/test_global_npc_assistance_request_replanning.py` verifies terminal delivery selective wake, unrelated-member isolation, queued and failed isolation, local ACK waiting/accept/reject behavior, zero-budget deferral and tampered provenance failure.

Checkpoint boundary

The information queue, private ledgers and ordinary delivery/replanning chain already participate in existing world persistence contracts.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` remains outside the coherent persistent-world checkpoint generation at this pass. Recovery must not reconstruct a missing intent merely because its request claim or delivery survives.
