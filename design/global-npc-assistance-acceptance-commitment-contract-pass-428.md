# Global NPC assistance acceptance commitment contract — Pass 428

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

Pass 427 allows a delivered assistance response to update only the original requester and wake that actor. An ACCEPT still carries no schedule cost by itself.

Pass 428 adds the next world-level seam: one terminally delivered `ACCEPT_ASSISTANCE_REQUEST` may create one explicit responder-owned `ScheduledCommitment` using the existing global agenda model.

Implemented owner

`tools/global_npc_assistance_acceptance_commitment.py`

The new `AssistanceCommitmentLedger` preserves the causal binding between the commitment, original request, ACCEPT response and delivered response event. The operational schedule object remains the existing `ScheduledCommitment`; Pass 428 does not create a second scheduler.

Admission chain

The original request must remain a PLANNED `REQUEST_ASSISTANCE` action and identify another actor.

The response must remain a PLANNED `ACCEPT_ASSISTANCE_REQUEST`, belong to the original recipient and target the original requester.

The response communication must have reached terminal `DELIVERED`. Its envelope sender/receiver and both claim ledgers must still preserve the response action as provenance root. The source subject and value must still identify the exact request/response pair and ACCEPT kind.

A commitment window must be explicitly supplied. The end cannot precede the start. The start cannot be earlier than materialization time. This prevents retroactive reservation of time.

Agenda behavior

The commitment is attached to the responder's existing `AgentAgendaProfile.commitments` tuple.

The existing global scheduler remains authority for UPCOMING, DUE, GRACE and MISSED states. Existing utility selection decides whether the commitment wins against goals, needs, other commitments and situational work. A hard commitment receives the existing hard-commitment pressure; Pass 428 adds no special scoring formula.

A missed window follows the existing `RESCHEDULE_OR_REPORT_MISSED_COMMITMENT` behavior. It never teleports the actor or marks assistance completed off-screen.

Agency and execution boundary

A commitment records a responder-owned obligation window. It does not move the responder, reserve a route, book a resource, change custody, change relationships, mark a quest complete or invoke AutoPTU.

`requires_structured_mechanics=True` is allowed only as an ordinary property of the resulting scheduled work. When that work becomes selected by the agenda, the existing planner emits `REQUEST_AUTOPTU`. The commitment owner itself does not call the engine.

Replay and persistence

Exact commitment replay is idempotent. Reusing a commitment ID with different provenance or schedule content fails closed. A conflicting commitment already attached to the same responder agenda also fails closed.

`OUROS_ASSISTANCE_COMMITMENT_LEDGER_V1` has deterministic local snapshot/restore coverage. It is not yet included in the coherent persistent-world checkpoint chain. The existing broader gap for `OUROS_WORLD_ACTION_INTENT_LEDGER_V1` also remains. A later checkpoint pass must restore action intent, assistance commitment and agenda state from one compatible generation rather than reconstructing authority from messages alone.

PTU/Caelo boundary

No PTU rule is created. A scheduled world obligation grants no Move, Ability, Item, Trainer Feature, movement permission, reaction or tactical objective. Any later structured scene must independently admit each engine capability family it uses.

Regression

`tests/test_global_npc_assistance_acceptance_commitment.py` covers delivered-ACCEPT admission, agenda insertion, UPCOMING/DUE behavior, no location mutation, explicit AutoPTU handoff only when structured work becomes agenda-selected, non-ACCEPT rejection, non-delivery rejection, non-retroactive time windows, replay idempotency, conflict failure, ledger snapshot durability and provenance tampering.

Next boundaries

A later pass should integrate the world-action and assistance-commitment ledgers into coherent checkpoint recovery. DEFER still needs an explicit condition/window owner. COUNTERPROPOSE still needs structured proposal content. Travel, resources and tactical resolution remain separate owners.
