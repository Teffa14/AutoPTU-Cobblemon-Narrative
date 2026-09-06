# Global NPC assessment decision review contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 311

## Purpose

Represent an explicit review of a previously recorded assessment-dependent world decision after the original decision-maker has actually received a superseding custody assessment.

Pass 310 identifies decisions whose evidence basis changed and determines whether review is eligible. Pass 311 records the review event itself without rewriting history or applying downstream repair automatically.

## Invariants

A review must reference one immutable historical decision, the same decision actor, one concrete superseding custody assessment, and the exact provenance-backed claim held by that actor.

The superseding assessment must descend from the assessment that supported the original decision. An unrelated newer assessment cannot authorize review of that decision.

The actor must possess the superseding claim no later than the review time. Global existence of a correction remains insufficient.

Allowed review outcomes are `MAINTAIN`, `AMEND`, `RESCIND` and `DEFER`. These are review conclusions only. They do not directly mutate route state, permissions, money, schedules, faction standing, trust, publication history or any other world consequence.

`REVIEW_OUTCOME != CONSEQUENCE_REPAIR`

`RESCIND != HISTORY_ERASURE`

`MAINTAIN != ORIGINAL_BASIS_STILL_VALID`

A decision may be maintained after its original evidence basis is superseded because another authored reason still supports it. That reason must be represented separately by later consequence/reason provenance rather than inferred here.

Multiple historical reviews may exist for one decision. Earlier reviews remain queryable.

## Runtime

`tools/global_npc_assessment_decision_review.py`

`AssessmentDecisionReviewRegistry` stores review events and can return their history for a decision.

`record_assessment_decision_review()` requires `REVIEW_ELIGIBLE`, validates lineage and the exact superseding claim, then records the chosen outcome and an authored rationale reference.

The V1 registry snapshot is standalone. Atomic world-checkpoint integration is deferred until consequence-repair semantics are explicit.

## PTU / Caelo boundary

This is world-simulation provenance, not a new PTU rule. It does not grant any Skill, Feature, Ability or Pokémon capability.

If a review scene requires discovery or authentication of physical evidence, use only validated PTU/Caelo mechanics. Public PTU reference material identifies Perception as a general investigation Skill and Channeler as a travel/investigation class, but Ouros must still verify the exact requested action against project source material before canonizing a check or capability.

## Battle boundary

The review runtime requires no AutoPTU capability. Any confrontation, rescue or hazard scene caused by the reviewed decision must declare its own engine dependencies and may use a reduced implementation-safe version.
