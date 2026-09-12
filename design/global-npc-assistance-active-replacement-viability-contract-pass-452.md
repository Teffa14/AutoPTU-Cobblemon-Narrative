# Global NPC Assistance Active Replacement Viability Contract — Pass 452

Status: IMPLEMENTED SUPPORT CONTRACT
Date: 2026-09-12

## Purpose

Pass 451 can validate a multigenerational assistance commitment lineage, but Pass 437 viability observations still bind only to the original negotiated commitment ledger. That leaves a replaced schedule unable to accumulate new pre-start blocker evidence without pretending that an older generation is still active.

Pass 452 admits viability evidence on the current replacement leaf while preserving the original Pass 437 owner for generation zero.

## Inputs

The bridge consumes:

- the original `AssistanceCounterproposalCommitmentLedger`;
- `AssistanceRenegotiationReplacementCommitmentLedger`;
- the derived Pass 451 lineage view;
- the existing `AssistanceCommitmentViabilityLedger`;
- the existing NPC replan queue.

It introduces no second viability history.

## Admission rules

A replacement viability observation is valid only when its `commitment_id` exists in replacement history and is the active leaf of a valid lineage rooted in an original negotiated assistance commitment.

A superseded replacement cannot receive fresh viability evidence. The original generation remains handled by Pass 437.

The observer must be the responder who owns the active commitment. The observation must occur before that generation's start minute.

The stored `proposal_id` comes from the active lineage node, so evidence remains bound to the exact terms currently governing execution.

## Existing viability semantics preserved

The allowed outcomes remain `AT_RISK`, `BLOCKED`, and `RESTORED`.

`RESTORED` requires a prior at-risk or blocked observation for the same active commitment and uses `CLEARED`. `CLEARED` cannot be used for a blocked or at-risk observation.

History remains append-only and cannot move backward in semantic time. Replay with identical content is idempotent; conflicting reuse of an observation ID fails closed.

Each new observation wakes only the responder through the existing replanning queue.

## Ownership boundary

This bridge records evidence only. It does not cancel or reschedule a commitment, create another replacement, formulate or communicate renegotiation terms, reserve a route, grant access, allocate resources, move an actor, alter relationships, determine fault, complete assistance, or invoke AutoPTU.

Pass 452 therefore enables the first prerequisite of another renegotiation generation without claiming that the full second-renegotiation cycle exists.

## Canon boundary

No region, settlement, institution, named NPC, species distribution, faction, historical event, or League structure becomes canon through this contract.

## Mechanical boundary

The viability bridge itself has no battle-mechanics dependency.

A later scene that consumes the blocker must declare its own exact requirements across targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.
