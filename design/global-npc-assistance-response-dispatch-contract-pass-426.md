# Global NPC assistance response dispatch contract — Pass 426

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

Pass 425 records ACCEPT, DEFER, REJECT or COUNTERPROPOSE as the assistance recipient's own durable world action. The original requester still cannot know that answer until it is communicated.

Pass 426 adds the explicit return-path dispatch seam. One admitted durable response can author one response claim and schedule one ordinary information envelope back to the original requester.

Implemented owner

`tools/global_npc_assistance_response_dispatch.py`

Entry point

`schedule_assistance_response_from_action(...)`

Admission chain

The original request action must exist, remain `PLANNED`, have semantic kind `REQUEST_ASSISTANCE`, and name an explicit recipient.

The response action must exist, remain `PLANNED`, and use one of the four admitted assistance response kinds:

- `ACCEPT_ASSISTANCE_REQUEST`
- `DEFER_ASSISTANCE_REQUEST`
- `REJECT_ASSISTANCE_REQUEST`
- `COUNTERPROPOSE_ASSISTANCE_REQUEST`

The response actor must be the original request recipient. The response target must be the original requester. The response cannot predate the request, and communication authoring cannot predate the response action.

Sender and requester must already have private knowledge ledgers. The selected communication channel must already exist in the ordinary `InformationEventQueue`.

Causal record

The responding actor receives one `AUTHORED_START` claim.

Its subject is `assistance_response:<request_action_id>:<response_action_id>`.

Its value is the durable response kind.

Its provenance root is the response action ID, not the original request action ID. This keeps request and answer as separate causal facts while the subject retains the link between them.

The ordinary information envelope references this response claim. If delivery later succeeds, existing information transmission materializes the requester's `REPORT` claim while preserving the response action as provenance root.

The resulting history can remain separately queryable:

request world action -> request communication -> recipient receipt -> recipient replan -> durable response world action -> response communication -> requester receipt.

Requester isolation

Scheduling the response does not mutate requester knowledge.

`QUEUED` does not mean received.

`WAITING_LOCAL_ACK` does not mean received.

`FAILED_CHANNEL_UNAVAILABLE` does not mean received.

Only ordinary terminal delivery may create the requester-side claim.

Pass 426 deliberately does not call the delivery-to-replanning coordinator. Requester replanning after actual receipt remains the next seam.

Agency boundary

An ACCEPT message does not create a commitment, reservation, free time, route, arrival or completed assistance.

A DEFER message does not create its own wake condition or future appointment.

A REJECT message does not automatically change trust or relationship state.

A COUNTERPROPOSE message does not change the requester's plan before the counterproposal is delivered, and its detailed proposed scope/time/location still requires a later explicit payload contract.

No response dispatch mutates the original request or response record.

Replay and conflict behavior

The response claim uses the existing knowledge-ledger collision guard. Exact replay is idempotent.

Before authoring a new source claim, the helper checks existing envelope provenance for the supplied event ID. Reusing an event ID with conflicting sender, receiver, message, claim, channel, time or trust data fails closed.

Exact replay may return the same pending or terminal envelope without duplicating sender or receiver knowledge.

AutoPTU boundary

This seam is world-level communication only. It does not resolve PTU mechanics, inspect battle state or grant Moves, Abilities, Items, Trainer Features, movement permissions or reactions.

If a later accepted response leads to structured tactical play, that later world action must enter through the explicit AutoPTU handoff and admit every required engine capability family independently.

Checkpoint boundary

The ordinary information queue and private ledgers already participate in the global persistence architecture.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` remains outside the coherent persistent-world checkpoint generation at this pass. A surviving response message must not be used to reconstruct missing response-action authority after a mismatched restart.

Regression

`tests/test_global_npc_assistance_response_dispatch.py` covers all four response kinds, sender/requester binding, source provenance, pre-delivery requester isolation, successful delivery lineage, queued/failed/local-ack isolation, terminal replay idempotency, chronology, unsupported response rejection and conflicting event reuse.

Next boundary

A response-specific delivery-to-replanning bridge should admit only terminal delivery and wake only the original requester from the exact response event. ACCEPT then needs a separate commitment/reservation owner before time or travel is consumed. DEFER needs an explicit future condition/window. COUNTERPROPOSE needs an explicit proposal payload rather than relying only on the response kind.
