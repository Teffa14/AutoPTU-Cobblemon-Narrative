# Global NPC Assistance Commitment Lineage View Contract — Pass 451

Status: IMPLEMENTED SUPPORT CONTRACT
Date: 2026-09-12

## Purpose

Pass 450 preserves one original assistance commitment plus one accepted replacement across restart. The next requirement is generation-neutral history. A later replacement must be able to point to the currently active replacement without losing the original promise or allowing an older schedule to become executable again.

This pass adds a derived lineage view. It does not create a new durable owner and does not alter any existing ledger.

## Inputs

The view consumes only:

- `AssistanceCounterproposalCommitmentLedger` as the original accepted commitment source;
- `AssistanceRenegotiationReplacementCommitmentLedger` as replacement history;
- optionally the global NPC coordinator agenda for active-schedule consistency.

## Required invariants

A valid lineage has exactly one original root.

Every replacement names one existing parent commitment. The parent may be the original commitment or a prior replacement.

A parent can have at most one accepted replacement child. Sibling replacement commitments would make active-history authority ambiguous and fail closed.

Cycles and orphan replacement records fail closed.

A replacement preserves requester, responder, intent kind, priority, hardness, grace, knowledge requirements, permission requirements, local-projection requirement and structured-mechanics requirement. Time window, location, scope and alternative may change because those are the negotiated terms.

Each child must preserve the exact provenance root of its parent in `superseded_provenance_root`.

## Active schedule rule

For one validated lineage, only its latest generation may appear in the responder agenda.

Historical generations remain queryable in their source ledgers. They are evidence, not executable work.

An old generation reappearing in the agenda is an invalid state. Restart, replay, accountability processing or later narrative systems must not reactivate it.

Other unrelated commitments on the same responder agenda are unaffected.

## Ownership boundary

The lineage view only validates and queries history.

It does not formulate replacement terms, communicate them, accept or reject them, create commitments, reserve routes, grant permissions, allocate resources, move actors, change relationships, determine blame, complete assistance or request AutoPTU.

## Multigeneration admission

Current Pass 449 materialization still creates the first replacement from the original counterproposal commitment. Pass 451 deliberately accepts a replacement whose parent is another replacement so future materialization work can reuse one historical model instead of introducing a second lineage representation.

A future second-renegotiation pass must still prove the full communication and consent chain for that generation before writing such a record.

## Mechanical boundary

This support layer has no battle-mechanics dependency. If the resulting assistance scene later becomes structured combat or tactical objective play, the encounter must declare its exact engine capability families independently.