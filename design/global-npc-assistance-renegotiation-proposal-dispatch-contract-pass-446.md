# Global NPC Assistance Renegotiation Proposal Dispatch Contract — Pass 446

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Carry an already-authored replacement assistance offer from the original responder to the requester through the ordinary information network without treating authorship, transmission, receipt or acceptance as the same fact.

Owner

`tools/global_npc_assistance_renegotiation_proposal_dispatch.py` owns dispatch only. `OUROS_ASSISTANCE_RENEGOTIATION_PROPOSAL_LEDGER_V1` remains the durable owner of the replacement terms. `InformationEventQueue` remains the owner of transport and terminal delivery state.

Required causal chain

Pass 445 must already contain the replacement proposal. That proposal already proves that the requester explicitly allowed reopening and that the permission reached the responder. Pass 446 may then author one communication claim from the responder and schedule one responder-to-requester information envelope.

Proposal existence alone does not create requester knowledge. A queued, delayed, failed or local-ack-waiting envelope does not create requester knowledge. Only the existing information runtime may materialize the REPORT claim after terminal `DELIVERED`.

Payload and lineage

The transported payload preserves the replacement proposal id, superseded commitment and proposal ids, reopening decision and reply-event ids, both actors, complete proposed window, location/scope/alternative refs, expiry, proposal authoring minute and decision provenance root.

The communication claim uses the replacement proposal provenance root. The receiver REPORT must therefore remain traceable to the responder-authored new offer while the older reopening-decision lineage stays embedded in the structured payload.

Expiry and chronology

Dispatch cannot predate proposal authorship. A replacement offer with an explicit expiry cannot be newly dispatched after that expiry. Delivery may occur later because transport latency is independently owned by the information network; a later decision owner must evaluate whether the terms are still eligible when the requester actually receives them.

Explicit non-effects

Dispatch does not accept or reject the replacement offer. It does not create a replacement commitment. It does not cancel, rewrite, satisfy or mark missed the older commitment. It does not reserve a route, grant access, allocate resources, move either actor, change relationships, infer blame, freeze world state or invoke AutoPTU.

The site, route, weather, Pokémon activity, access state, actor schedules and resource availability may continue changing while the offer travels.

Failure posture

Unknown proposals, missing actor knowledge ledgers, unknown channels, impossible chronology, already-expired offers, event-id collisions and malformed communication identity fail closed. Exact replay of the same dispatch is idempotent.

PTU / Caelo boundary

This pass adds no PTU or Kairos mechanical rule. The Kairos source inventory remains reference-only until rule-by-rule Ouros review. If a later accepted offer reaches structured travel, combat, hazardous terrain, Trainer Features, item use or other governed mechanics, those systems require their own verified source and engine capability evidence.

AutoPTU boundary

Pass 446 is non-tactical and does not request AutoPTU. A later scene may require an explicit `REQUEST_AUTOPTU` only after world-level legality and objective admission establish that structured mechanics are required.

Open seam

After terminal delivery, the requester needs a separate durable decision owner for the replacement terms. Acceptance, rejection and expiry must remain distinct. Only an explicit valid acceptance should become eligible to create a replacement commitment, and the original commitment must remain queryable as historical causal evidence.