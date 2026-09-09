# Global NPC delivery / replan provenance runtime contract — Pass 373

Status: DESIGN / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Purpose

Implement the standalone provenance owner proposed by Pass 372 without modifying the existing coordinator, replan queue or coherent world-checkpoint schemas.

The new runtime wrapper composes the existing Pass 287 coordinator and Pass 284 replan queue. It records successful delivery materialization and exact consumed-trigger structure while preserving existing ownership.

## Implemented owner

`tools/global_npc_delivery_replan_provenance.py`

Schema:

`OUROS_NPC_DELIVERY_REPLAN_PROVENANCE_V1`

The ledger owns two append-only row families.

`MaterializedDeliveryReceipt` records delivery event, receiver, claim reference, provenance root, materialization minute, wake status and the replan trigger created from that delivery.

`ConsumedReplanRecord` records trigger identity, agent, reason, source reference, due minute, priority, processed minute and deterministic batch key.

The ledger does not replace communication envelopes, private knowledge, replan queue ordering or planner results.

## Runtime composition

`ProvenanceAwareWorldEventRuntime` wraps `GlobalNpcWorldEventCoordinator`.

Before one coordinator cycle it snapshots the full pending trigger structures. The existing coordinator then processes communications, materializes successful deliveries, creates wake triggers and consumes due replans. The wrapper records successful materializations and preserves any newly completed trigger using its pre-cycle or same-cycle structured form.

A completed trigger for which no structured trigger can be recovered causes the wrapper to fail closed instead of treating its bare completed ID as historical proof.

## Invariants

`DELIVERED != MATERIALIZED_AS_EVIDENCE != REPLAN_TRIGGER_CREATED != REPLAN_TRIGGER_CONSUMED != PLAN_SELECTED != ACTION_STARTED`

A successful materialization receipt requires an actual `DELIVERED` result and a concrete wake trigger.

The receipt receiver must match the materialized receiver and the retained communication envelope receiver.

The materialized claim must still exist in the receiver's restored knowledge state when validation asserts that materialization occurred.

The provenance root must remain represented in the receiver memory references.

A materialization receipt cannot point to an unknown trigger.

A consumption row cannot predate the trigger due minute or the restored semantic time.

A consumed trigger must be in the queue's completed set and must no longer remain pending.

For `KNOWLEDGE_DELIVERED`, trigger source must resolve to the exact materialization receipt, agent must match receiver and trigger ID must match the receipt's wake trigger.

The same delivery cannot create two successful provenance receipts. The same trigger cannot create two consumption rows.

## Migration boundary

This pass does not change `NpcReplanQueue` V1, the base world checkpoint or coherent resource-world V14.

A future checkpoint integration may restore older saves with an empty delivery/replan provenance ledger. It must not infer historical receipts from final knowledge, memory refs, completed trigger IDs, current agenda state or travel state.

Standalone `DeliveryReplanProvenanceLedger.snapshot()` / `restore()` is now executable and test-covered. Coherent world integration remains a later pass.

## Acknowledgement boundary

No acknowledgement state is introduced here.

FAA acknowledgement/readback practice is used only as a systems-design reference for keeping transmission, verification, acceptance and execution separate. Ouros still needs a first-class owner if explicit check-back or acknowledgement later becomes narratively necessary.

## AutoPTU boundary

This runtime is world-agent infrastructure. It adds no tactical legality.

A planner decision that requires combat, forced movement, reactions, hazards, move-specific behavior, Abilities, Items or Trainer Feature interrupts must still request AutoPTU and pass the exact capability gate.

## Acceptance coverage

The Pass 373 regression suite covers successful delivery-to-consumption provenance, snapshot round-trip, failed delivery exclusion, receiver/source tampering, future rows, non-information trigger consumption and duplicate successful materialization.

The next integration target is a coherent checkpoint after V14 that validates this ledger against the restored communication queue, agent knowledge and replan state under the same digest.