# Global NPC assessment-dependent decision contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 310

## Purpose

Preserve which concrete world decisions were made using a specific custody assessment conclusion known by the deciding actor at that semantic time.

This contract extends Passes 308–309. Assessment lineage records that a conclusion changed. Revision propagation records who actually received the newer conclusion. Pass 310 records downstream decision dependency so the world can later identify consequences that may deserve review.

## Invariants

Every recorded decision must identify one persistent actor, one basis assessment, one exact basis claim held in that actor's private `KnowledgeLedger`, one decision kind, one affected subject and one semantic decision time.

The basis claim must preserve the assessment's provenance root, evidence subject and conclusion value. The claim must exist no later than the decision itself.

A newer assessment existing globally does not update the decision actor. Until a provenance-backed claim rooted in a superseding assessment reaches that actor, the review state remains `SUPERSEDED_NOT_RECEIVED`.

Receipt of a relevant revision changes the review state to `REVIEW_ELIGIBLE`. It does not reverse, cancel, refund, reopen, apologize for, compensate for or otherwise repair the old decision.

`REVIEW_ELIGIBLE != AUTOMATIC_REVERSAL`

`ASSESSMENT_SUPERSEDED != ACTOR_KNOWS_REVISION`

`DECISION_PROVENANCE != DECISION_CORRECTNESS`

Unrelated assessments, even when known by the actor, cannot make a decision reviewable.

Historical decisions remain immutable records. A later review, replacement decision or repair event must be a new causal event with its own provenance.

## Runtime

`tools/global_npc_assessment_decision_dependency.py`

`AssessmentDependentDecision` stores the minimal durable dependency edge.

`record_assessment_dependent_decision()` validates that the deciding actor actually possesses the claimed basis and that it matches the selected custody assessment.

`superseding_assessments()` derives later validated descendants from the custody lineage without granting that knowledge to any actor.

`affected_decisions()` identifies decisions whose basis is an ancestor of a particular superseding assessment.

`evaluate_decision_review_status()` combines global lineage with the deciding actor's private ledger and returns `BASIS_CURRENT`, `SUPERSEDED_NOT_RECEIVED` or `REVIEW_ELIGIBLE`.

The registry has its own V1 snapshot. Atomic world-checkpoint integration is deliberately deferred until this seam has stable review/repair semantics.

## Boundary with social state and authored consequences

This pass must not mutate trust, affinity, rivalry, faction standing, schedules, money, route state, permissions, employment, custody conclusions or publication history. Those may be consequences of a later explicit review event.

A corrected evidence basis can justify reopening one decision while leaving other independent reasons intact. Selective repair therefore requires a future consequence dependency layer rather than a global relationship reset.

## Battle boundary

The core dependency runtime requires no AutoPTU combat capability.

A narrative scene triggered by an affected decision must declare its own exact engine dependencies. No decision record may imply that movement, hazards, statuses, reactions, Moves, Abilities, Items or Trainer Features are already implemented.

## Persistence boundary

The registry snapshot makes the seam testable and restart-safe in isolation. It is not yet part of `OUROS_NPC_WORLD_CHECKPOINT_V4`. World-checkpoint integration is a future bounded slice once the project decides whether review events and consequence repair belong in the same atomic unit.
