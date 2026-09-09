# Persistent world evidence checkpoint contract — Pass 387

Status: IMPLEMENTED CONTRACT
Canon effect: NONE

## Purpose

`OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1` is the recovery owner for persistent site-evidence history and its two explicit NPC-knowledge bridges.

It keeps this state separate from `OUROS_NPC_WORLD_CHECKPOINT_V19`, whose responsibility remains global-NPC causal/action history.

## Owned state

The checkpoint contains:
- one semantic minute;
- `OUROS_SITE_EVIDENCE_LEDGER_V1`;
- `OUROS_SITE_OBSERVATION_KNOWLEDGE_V1`;
- `OUROS_SITE_INTERPRETATION_KNOWLEDGE_V1`;
- SHA-256 of the exact external `KnowledgeLedgerStore` snapshot used by the bridges;
- SHA-256 of the complete checkpoint payload.

The checkpoint does not duplicate or become authoritative for private NPC claims. `KnowledgeLedgerStore` remains their owner.

## Recovery rule

Restore requires a `KnowledgeLedgerStore` supplied by the caller. Its deterministic snapshot digest must match the digest recorded in this checkpoint before any bridge is accepted.

After digest validation, restore re-runs the existing owner validations in dependency order:
1. site revision / observation / interpretation history;
2. direct-observation bridge against site evidence and private claims;
3. interpretation bridge against site evidence, all private supporting observations and supersession lineage.

Re-signing a semantically inconsistent checkpoint does not make it valid.

## Invariants

`WORLD_EVIDENCE_CHECKPOINT != GLOBAL_NPC_ACTION_CHECKPOINT`

`SITE_EVIDENCE != PRIVATE_KNOWLEDGE`

`MATCHING_HASH != SUFFICIENT_SEMANTIC_VALIDITY`

`RESTORE != RECONSTRUCT_MISSING_HISTORY`

`CURRENT_SITE_STATE != HISTORICAL_SITE_STATE`

A site record cannot come from after the checkpoint minute. A bridge cannot survive if its source record, actor, content, provenance, support set or private claim has diverged.

## Why the private store is referenced rather than copied

Private memory already has a durable owner inside global-NPC recovery. Copying the full store into a second checkpoint would create two competing authorities for the same claims.

The digest acts as a coherence binding. A recovery coordinator must restore the matching global-NPC private state and persistent-world-evidence state together. Later work can add an outer world-recovery manifest that names both checkpoint digests without moving ownership.

## Battle boundary

This checkpoint is world persistence only. It adds no tactical action, battle outcome or AutoPTU authority.

If a site concept later requires unstable terrain, forced movement, reactions, environmental phases, Items, Moves, Abilities or Trainer Features, those exact capability families remain separately gated.
