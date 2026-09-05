# Global NPC memory retrieval / access contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-memory-belief-communication-contract.md`

## Purpose

Separate durable epistemic history from what an NPC can currently retrieve.

The KnowledgeLedger remains the audit record of exposure and provenance. Retrieval is a temporary projection over that history at a semantic time.

`LEDGER_HISTORY != CURRENT_RECALL`

Forgetting never deletes provenance. Source-access failure never rewrites the original source.

## Recall states

A claim can currently be:

- `RECALLED_WITH_SOURCE`: content is accessible and the source attribution is accessible;
- `CONTENT_ONLY`: content is accessible but source attribution is not;
- `INACCESSIBLE`: the claim remains in history but is not currently projected into recalled belief.

`CONTENT_ONLY` does not mean the NPC invents a replacement source. It means source attribution is unavailable.

## First deterministic policy

Pass 293 uses semantic age and original claim confidence to calculate retrieval accessibility. Reports and inferences receive an extra source-access penalty because source attribution is modeled as a stricter retrieval gate than content access.

The thresholds and age bands are game-simulation policy. They are not human memory measurements, PTU mechanics, probabilities or medical claims.

The policy is intentionally inspectable and replaceable.

## Belief interaction

`evaluate_recalled_belief()` builds a temporary view containing only currently accessible claims and then reuses the existing Pass 282 belief evaluator.

The durable ledger is not mutated.

A character can therefore possess historical evidence that no longer participates in their immediate recalled belief. Later systems may introduce explicit cues, rehearsal, records or questioning that improve access without rewriting the historical claim.

## Source-monitoring boundary

Pass 293 supports lost attribution only.

It does not implement false attribution, deliberate deception, confabulation or source substitution. Those require separate contracts because they create new semantic claims about origin rather than merely making an existing source inaccessible.

## Narrative use

This enables witness interviews, old rumors, investigations reopened after long delays, corrections that are remembered without their original context, and disagreement between archival records and current testimony.

An investigator can distinguish:

- the NPC was never exposed;
- the NPC was exposed but cannot currently retrieve the content;
- the NPC remembers the content but cannot identify the source;
- the NPC remembers both content and source.

## AutoPTU boundary

Memory retrieval is world-agent state and does not require tactical resolution.

If recalled or forgotten information causes a structured pursuit or battle, only the mechanics actually used by that encounter are dependencies. Memory access does not implement targeting, movement, lifecycle, damage, status, terrain, Move, Ability, Item, Trainer Feature, tactical-policy or adapter behavior.

## Canon boundary

This contract changes no established location, NPC, faction, historical event or PTU/Caelo/Kairos rule. Synthetic thresholds are implementation policy only.
