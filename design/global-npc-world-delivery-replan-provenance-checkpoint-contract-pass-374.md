# Global NPC world delivery / replan provenance checkpoint contract — Pass 374

Status: DESIGN / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Purpose

Pass 374 integrates the standalone Pass 373 delivery/replan provenance owner into coherent world recovery.

`OUROS_NPC_WORLD_CHECKPOINT_V15` extends V14 with `OUROS_NPC_DELIVERY_REPLAN_PROVENANCE_V1` under the same SHA-256 recovery unit.

The preserved causal chain is:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED`

The checkpoint does not claim:

`ACKNOWLEDGED`, `ACCEPTED`, `PLAN_SELECTED`, `ACTION_STARTED`, `AUTOPTU_RESOLVED` or `OUTCOME_OBSERVED`.

## Owner boundaries

Communications remains owner of authored envelopes, transport status and delivery provenance.

The managed NPC state remains owner of current knowledge and memory references.

NpcReplanQueue remains owner of pending, known and completed trigger IDs.

DeliveryReplanProvenanceLedger owns append-only evidence connecting successful materialization to the wake trigger and preserving the full structure of triggers after consumption.

V15 composes those owners. It does not replace them.

## Restore invariants

A V15 restore must reject a provenance receipt when the referenced delivery is not recorded as delivered, the archived envelope is unavailable, receiver identity differs, the materialized claim is absent from receiver knowledge, provenance root is absent from receiver memory references or the wake trigger is unknown.

A consumed trigger record must reference a completed trigger that is no longer pending. A `KNOWLEDGE_DELIVERED` consumption must point back to the exact materialization receipt, receiver and wake trigger.

All materialization and consumption timestamps must be at or before the restored semantic minute.

## Migration

V14 and earlier snapshots restore with an empty DeliveryReplanProvenanceLedger.

Migration must not reconstruct materializations from delivered IDs, claims currently present in memory, completed trigger IDs, present agenda state, movement state or later actions.

## Narrative consequence

After restart, Ouros can distinguish all of the following without omniscience:

A message reached an NPC.

That delivery became usable evidence for the NPC.

The delivery woke the planner.

The corresponding wake trigger was actually processed.

None of those facts proves which plan won arbitration or which action the NPC subsequently attempted.

## Next boundary

Future work may persist plan-selection provenance separately. That owner must consume a specific ReplanBatch or equivalent decision context and preserve candidate/selected intent evidence without rewriting the delivery/replan history established here.
