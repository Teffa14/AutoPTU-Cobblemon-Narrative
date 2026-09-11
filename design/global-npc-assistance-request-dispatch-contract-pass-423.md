# Global NPC assistance request dispatch contract — Pass 423

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

Pass 422 records one named actor's selected world action as a durable `PLANNED` intent. A `REQUEST_ASSISTANCE` intent still cannot change the proposed recipient.

Pass 423 introduces the next boundary: one admitted assistance-request intent can author one request claim for the deciding actor and schedule one ordinary information envelope toward the exact target selected by that action.

Implemented owner

`tools/global_npc_assistance_request_dispatch.py`

Entry point

`schedule_assistance_request_from_action(...)`

Admission requirements

The referenced `action_id` must exist in `WorldActionIntentLedger`.

Its status must remain `PLANNED`.

Its semantic kind must be exactly `REQUEST_ASSISTANCE`.

It must name an explicit target different from the requester.

The request cannot be authored before the action's semantic minute.

Sender and receiver must already have private `KnowledgeLedger` owners in the supplied `InformationEventQueue`.

The selected communication channel must already exist in that queue.

No PTU permission, Feature, move, Item, class benefit or tactical capability is inferred from the request.

Causal record

The requester receives an `AUTHORED_START` claim whose provenance root is the world `action_id`.

Its subject is `assistance_request:<action_id>` and its value is the originating world intent ID.

The ordinary information envelope references that claim. If delivery later succeeds, the existing `transmit_claim` behavior creates the receiver's `REPORT` claim while preserving the same provenance root.

Therefore the causal chain remains queryable:

replan trigger -> selected agenda decision -> durable world action intent -> authored request claim -> information envelope -> receiver report claim.

Receiver isolation

Scheduling the request does not mutate the receiver's private knowledge.

`QUEUED` does not mean received.

`WAITING_LOCAL_ACK` does not mean received.

`FAILED_CHANNEL_UNAVAILABLE` does not mean received.

Only the ordinary information queue's terminal successful delivery creates the receiver claim.

This owner does not call the replanning coordinator. Existing delivery-to-replanning architecture remains the sole path that may later wake the explicit receiver after real delivery.

Independent agency boundary

Receipt does not mean acceptance.

Pass 423 does not create a commitment, reservation, travel plan, appointment, task assignment or schedule mutation for the requested actor.

If the receiver later accepts, that choice must be represented as the receiver's own durable decision or world action. A requester cannot write another actor's agenda by creating a request.

Replay and conflict behavior

The source request claim uses the existing `KnowledgeLedger.add` collision guard. Exact replay is idempotent.

The dispatch function checks any existing envelope provenance before authoring a new source claim. Reusing an event ID for a different sender, receiver, message, claim, channel, creation minute, delivery minute or trust value fails closed without authoring the conflicting request claim.

Exact replay may return the same pending, waiting or archived envelope. This includes replay after successful terminal delivery.

Checkpoint boundary

The information queue and knowledge ledgers already have durable checkpoint coverage through the existing global NPC world checkpoint chain.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` itself is still outside the coherent persistent-world checkpoint generation. Pass 423 does not hide that gap. Recovery must not reconstruct a missing world action intent solely from a delivered request claim.

AutoPTU boundary

This seam is world-level communication. It does not call AutoPTU and does not interpret battle state.

If a later accepted request leads to a structured PTU action, the current actor state must be validated and resolution must enter through explicit AutoPTU ownership. Narrative job titles and relationship roles do not grant mechanics.

Regression

`tests/test_global_npc_assistance_request_dispatch.py` covers request authoring, queued receiver isolation, provenance after successful delivery, failed-channel isolation, local-ACK isolation, terminal replay idempotency, conflicting event reuse, semantic-kind admission, explicit-target admission, self-target rejection, chronology and unknown-action failure.

Next boundary

A successful delivered request should become eligible for the existing selective delivery-to-replanning coordinator. That coordinator may wake only the explicit receiver. A resulting acceptance, deferral, rejection or counterproposal should then become the receiver's own durable choice rather than mutating the original request into an assignment.
