# Global NPC reviewed-consequence checkpoint integration contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 313

## Purpose

The atomic global NPC checkpoint must preserve the causal chain created by custody reassessment, downstream decisions, explicit review and selective consequence repair.

The checkpoint is a logical recovery unit. It does not claim physical database transaction durability, filesystem fsync guarantees or AutoPTU battle-session reconciliation.

## Schema

`OUROS_NPC_WORLD_CHECKPOINT_V5` adds three coupled registries:

`assessment_decision_dependencies`
`assessment_decision_reviews`
`decision_consequence_repairs`

V4 and earlier checkpoints remain readable. Because those schemas never stored these registries, legacy restore yields empty registries rather than inventing decisions, reviews or repairs.

## Required causal invariants

A restored assessment-dependent decision must reference an existing custody assessment and an actor ledger that still contains the exact basis claim. The basis claim must preserve the expected custody subject, conclusion value and provenance root. Neither assessment nor claim may postdate the decision.

A restored decision review must reference an existing decision, the same actor, and a superseding custody assessment whose lineage descends from the decision basis. The actor ledger must still contain the exact superseding claim used by the review. The review cannot predate that claim or come from after the checkpoint.

A restored consequence must reference an existing decision and cannot predate it or come from the future.

A restored consequence repair must reference both an existing consequence and review. The review must belong to the same source decision, the repair actor must match the review actor, and the repair cannot predate either the consequence or review or come from the future.

## History preservation

Checkpoint restore must not collapse the chain into a single current value.

The original assessment remains queryable.
The original decision remains queryable.
The review remains a separate event.
The original consequence remains queryable.
The repair remains a separate event.
The effective consequence can be derived from that history.

This preserves the distinction between what happened, why it happened, what was later learned and what was subsequently changed.

## Non-omniscience

The checkpoint does not grant any NPC claims that were absent from that NPC's restored ledger. A correction can exist globally while an actor remains unaware of it. Restart cannot turn global lineage into personal knowledge.

## Domain boundary

This contract changes world-agent persistence only. It does not authorize PTU moves, statuses, hazards, reactions, Trainer Features, items or Pokémon abilities. AutoPTU remains the authority for tactical resolution when a world event crosses that boundary.
