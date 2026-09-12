# Global NPC Assistance Renegotiation Decision Dispatch Contract — Pass 444

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Carry the requester's explicit Pass 443 answer back to the responder through ordinary private communication. Recording consent or refusal does not make the responder know it.

Owner

The durable decision remains owned by `OUROS_ASSISTANCE_RENEGOTIATION_DECISION_LEDGER_V1`. Transport is owned by the existing `InformationEventQueue`; Pass 444 does not invent a second message ledger.

Required causal chain

An accepted negotiated assistance commitment exists. The responder requested renegotiation. That request reached terminal `DELIVERED`. The requester recorded `ACCEPT_RENEGOTIATION_REQUEST` or `REJECT_RENEGOTIATION_REQUEST`. Only then may Pass 444 author a requester-owned claim and schedule a requester-to-responder information envelope.

The original request event must still resolve to the same responder/requester pair and remain terminal `DELIVERED`. Commitment, proposal, disposition, actors and prior request provenance must still match the durable decision.

Reply provenance

The requester answer is a new communicative act. Its authored claim therefore starts a new provenance root at `decision_id` while the structured payload preserves the prior renegotiation-request provenance root as causal context.

This prevents the answer from being collapsed into the earlier request while retaining lineage back to the conversation that caused it.

Delivery invariant

`REQUESTER_DECISION_RECORDED != REPLY_AUTHORED != REPLY_DELIVERED != RESPONDER_KNOWS_REPLY`.

Before terminal delivery, the responder does not gain a report claim. Channel failure creates no responder knowledge. Local-projection acknowledgement rules remain those of the shared information queue.

Payload

The reply reports the exact commitment, proposal, disposition, request event, decision identity, decision value, optional rationale, decision minute, accepted window, location, scope, alternative and prior request provenance.

The reply does not contain replacement terms.

Explicit non-effects

Acceptance delivery does not create a new proposal, new commitment, new schedule, route reservation, permission, resource allocation, travel action, relationship update or AutoPTU request.

Rejection delivery does not mark the original commitment fulfilled, missed, blameworthy or socially damaging.

The old commitment remains historical fact regardless of answer.

Replay and identity

Exact replay of the same envelope is idempotent. Reusing an event identity with different message/envelope content fails closed. Source claim identity collisions remain guarded by the knowledge ledger.

AutoPTU boundary

Pass 444 has no tactical effect. A later replacement proposal may eventually lead to hazardous travel or a structured objective, but that must cross existing world-action and `REQUEST_AUTOPTU` boundaries.

Open seam

After an acceptance is actually delivered, a later owner may author replacement terms with explicit lineage to the old commitment and Pass 443 decision. Those new terms still require their own proposal and acceptance cycle before they can replace future obligations. A delivered rejection closes this reopen request as communicated information but does not itself adjudicate missed-obligation consequences.