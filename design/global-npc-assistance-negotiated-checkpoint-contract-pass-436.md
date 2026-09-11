# Global NPC Assistance Negotiated Checkpoint Contract — Pass 436

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 435 made an accepted assistance counterproposal capable of producing a responder-owned `ScheduledCommitment`. That left one causal gap: the structured offer and the negotiated commitment could still live outside the assistance world checkpoint that already owns ordinary assistance commitments and deferrals.

Pass 436 advances the outer checkpoint to `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V3`.

V3 snapshots and restores one logical generation containing:

- the underlying NPC world checkpoint;
- durable world-action intents;
- ordinary assistance commitments;
- assistance deferrals;
- structured assistance counterproposals;
- commitments materialized from accepted counterproposals.

## Causal invariants

A stored counterproposal must still resolve to its original `REQUEST_ASSISTANCE` and `COUNTERPROPOSE_ASSISTANCE_REQUEST` actions. Requester and responder bindings must agree. The proposal provenance root must remain the response action. The response cannot predate the request or come from the future relative to the checkpoint generation.

A negotiated commitment must resolve to the same proposal, original request, responder counterproposal and requester `ACCEPT_ASSISTANCE_COUNTERPROPOSAL` action. The acceptance must name the exact `proposal_id`. Its provenance root remains the requester decision action.

Time, location, scope and alternative terms in the negotiated commitment must exactly match the structured proposal that was accepted. A checkpoint cannot silently turn `survey-only` into `repair`, move the appointment, change its location, or substitute an alternative.

The responder agenda must contain the exact `ScheduledCommitment` represented by the negotiated commitment ledger. A commitment id cannot be owned simultaneously by the ordinary assistance commitment ledger and the counterproposal commitment ledger.

## Restore behavior

The checkpoint restores the world first, then ensures durable assistance commitments are present in responder agendas. If a caller-supplied agenda contains the same commitment id with conflicting content, restore fails closed.

V2 remains readable. Because V2 had no counterproposal or negotiated-commitment sections, restoring a V2 generation produces empty ledgers for those families. V1 remains readable and also restores an empty deferral ledger.

## Authority boundary

Checkpoint persistence records what the world already decided. It does not execute the promised work.

V3 does not reserve a route, allocate equipment, consume inventory, grant access, move an actor, resolve an inspection, complete a quest, mutate relationships or call AutoPTU. `location_ref`, `scope_ref` and `alternative_ref` remain negotiated provenance until dedicated owners normalize and consume them.

## Mechanical capability posture

This persistence contract requires no battle capability family by itself.

If a restored commitment later resolves through a mechanically rich encounter, its encounter contract must independently declare dependencies across the permanent engine capability categories. Persistence cannot be used as evidence that a tactical category is implemented.

## Verification

`tests/test_global_npc_assistance_world_checkpoint_v3.py` covers:

- round-trip persistence of structured terms and the negotiated commitment;
- exact restoration into the responder agenda;
- rejection when accepted non-time terms drift after agreement;
- rejection when the requester acceptance names another proposal;
- rejection of a validly re-digested snapshot whose proposal terms were altered independently of its commitment;
- V2 backward compatibility with empty new ledgers;
- a source-level guard against route reservation, item consumption and tactical execution entering the checkpoint owner.
