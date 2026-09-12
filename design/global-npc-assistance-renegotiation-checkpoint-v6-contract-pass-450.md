# Assistance Renegotiation Checkpoint V6 Contract — Pass 450

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE

## Purpose

Pass 449 can replace the future executable schedule for one negotiated assistance obligation while retaining the original commitment as historical evidence. That creates a persistence boundary that `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V5` predates.

A restart must preserve both the historical obligation and the complete replacement lineage without reactivating the superseded schedule.

Pass 450 introduces `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V6` for that boundary.

## State owned by V6

V6 snapshots one coherent generation containing the existing world checkpoint, assistance action/commitment history, deferrals, counterproposals, negotiated commitments, viability observations, start watches/assessments, start dispositions, requester reopening decisions, replacement proposals, replacement-proposal decisions, and replacement commitments.

The information queue remains the authority for transmitted requests, replies and offers. V6 persists that queue through the existing world checkpoint instead of creating a second communication history.

## Replacement execution invariant

A negotiated commitment that has not been superseded remains executable and must match the responder agenda.

Once a valid replacement commitment supersedes it:

- the old negotiated commitment remains present in its historical ledger;
- the replacement record retains lineage to the old commitment, old proposal, replacement proposal and accepted replacement terms;
- the responder agenda contains the replacement schedule;
- the responder agenda does not contain the superseded schedule;
- restart may not reconstruct the old schedule merely because its historical commitment record still exists.

The original agreement therefore remains queryable for later accountability without becoming a second active appointment.

## Validation strategy

Earlier assistance validators correctly require historical negotiated commitments to be present in an agenda because, before Pass 449, every such record was executable. V6 must preserve those earlier checks without changing their contract.

For validation only, V6 builds a private shallow view that reinserts superseded schedules. That temporary view is used to verify the old request/counterproposal/acceptance, viability, start and disposition chain. It is never returned as live world state.

The real restored coordinator is separately checked to require the replacement and reject the superseded executable schedule.

## Renegotiation lineage

For a replacement commitment to be valid at checkpoint time, V6 requires a coherent causal path:

1. the original negotiated commitment exists;
2. its responder recorded `REQUEST_RENEGOTIATION` after an adverse start;
3. the reopen request was delivered to the requester;
4. the requester recorded `ACCEPT_RENEGOTIATION_REQUEST`;
5. that permission was delivered back to the responder;
6. the responder authored replacement terms;
7. those terms were delivered to the requester;
8. the requester recorded `ACCEPT_REPLACEMENT_TERMS`;
9. that acceptance was delivered back to the responder;
10. the replacement commitment refers to those exact accepted terms.

Chronology and actor bindings must remain consistent. A redigested but causally altered snapshot fails closed.

## Backward compatibility

A valid V5 checkpoint can be restored through the V6 API. Post-V5 renegotiation ledgers default to empty because V5 never owned those facts. V6 does not invent missing negotiation history from messages or agenda shape.

## Authority boundary

Checkpoint V6 preserves causal state. It does not choose whether to renegotiate, send messages, reserve travel, allocate resources, grant access, move actors, complete assistance, change relationships, assign fault, calculate compensation, resolve combat, or invoke AutoPTU.

Those decisions remain with their existing owners.

## Engine boundary

The checkpoint itself has no battle-engine dependency. A later assistance objective may request AutoPTU only after the replacement obligation reaches execution and the current world state actually requires structured mechanics.

A saved promise cannot be used as evidence that any movement, reaction, weather, ability, item, Trainer Feature or tactical objective family exists.

## Known future questions

A future accountability owner may consume both the original and replacement commitments, but must not become schedule authority.

Repeated renegotiation where a replacement commitment itself is superseded needs an explicit lineage design before it is admitted. V6 currently guarantees one historical negotiated commitment followed by one replacement commitment.

Cancellation, fulfillment and missed-obligation terminal history also remain separate from checkpoint ownership.