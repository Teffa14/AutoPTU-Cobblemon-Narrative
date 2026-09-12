# Global NPC Assistance Renegotiation Requester Decision Contract — Pass 443

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Persist the requester's explicit decision after a renegotiation request has actually been delivered. Receipt alone cannot reopen accepted terms.

Owner

`OUROS_ASSISTANCE_RENEGOTIATION_DECISION_LEDGER_V1`

Supported decisions

- `ACCEPT_RENEGOTIATION_REQUEST`
- `REJECT_RENEGOTIATION_REQUEST`

Required causal chain

An accepted negotiated assistance commitment exists. The responder reaches a valid `REQUEST_RENEGOTIATION` disposition. Pass 442 authors and transmits the renegotiation request. The information envelope reaches terminal `DELIVERED`. The requester has a provenance-preserving `REPORT` whose parent is the responder-authored source claim. Only then may Pass 443 persist the requester's choice.

Validation

The decision binds the exact commitment, proposal, disposition and information event. Sender and receiver must match responder and requester. The structured payload received by the requester must exactly match the durable commitment/disposition state. Subject, value, parent claim and provenance must remain coherent. The decision cannot predate actual requester receipt.

Late decisions

Pass 443 permits a requester to answer after the old assistance window has ended. This does not extend or revive the old commitment. It records only whether the requester consents to reopen negotiation after learning that the responder requested it. Accountability for the expired original obligation remains a separate concern.

Explicit non-effects

An acceptance does not create replacement terms, a counterproposal, a new commitment, route reservation, access permission, resource allocation, travel, relationship change, social blame, or tactical resolution.

A rejection does not itself mark the old commitment fulfilled, missed, abandoned or blameworthy.

Neither choice communicates itself back to the responder. A later dispatch seam must carry that information through the normal communication system.

Knowledge invariant

`REQUEST_SENT != REQUEST_DELIVERED != REQUESTER_CONSENT`.

No shared faction, location, agenda or global world state may collapse these facts.

Persistence

The ledger has deterministic snapshot/restore and exact replay idempotency. Reusing a decision identity with conflicting content fails closed.

AutoPTU boundary

This contract is pure world-simulation state. It has no `REQUEST_AUTOPTU` behavior. Any later hazardous survey, escort, protection, retrieval, containment or extraction must cross the normal explicit handoff boundary and declare the exact capability families it requires.

Open seam

The next step is communication of the requester decision. If acceptance reaches the responder, a later proposal owner can author replacement terms while preserving the old commitment as historical fact. If rejection reaches the responder, subsequent waiting, abandonment, missed-obligation handling or another independent request remains policy outside this ledger.
