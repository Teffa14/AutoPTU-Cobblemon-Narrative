# Global NPC materialized-delivery / replan provenance contract — Pass 372

Status: DESIGN / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Purpose

Define the missing persistence boundary between a successfully delivered private communication and the world-agent replanning work that follows it.

Existing executable behavior already performs the transition in-process:

`InformationEventQueue delivery -> coordinator materialization -> receiver knowledge ref -> KNOWLEDGE_DELIVERED replan trigger -> agenda reevaluation`

Existing checkpoint state preserves the queue, managed agents, durable evidence, replan queue and the coordinator idempotency set. However, once a replan trigger is consumed, the current queue retains only its completed ID. That is insufficient provenance for a later restart to prove the exact causal relationship between a delivery, its receiver evidence and a consumed planning wake-up.

## Required invariants

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED`

A later state cannot be used to reconstruct an earlier missing state.

A materialized delivery must identify the delivery event, receiver, claim/evidence reference, provenance root, semantic time and optional replan trigger created from it.

A consumed replan must preserve enough structured provenance to identify the original trigger, agent, reason, source reference and consumption time or batch.

Materialization of a non-delivered transport result is invalid.

Materialization for a receiver different from the communication envelope receiver is invalid.

A `KNOWLEDGE_DELIVERED` trigger sourced from a delivery event must target the same managed receiver.

A completed trigger ID without its structured causal row must not be treated as proof that a particular delivery caused that planning cycle.

A plan selected after a batch may lawfully ignore, defer or lose to another higher-priority obligation. The presence of a `KNOWLEDGE_DELIVERED` trigger proves an opportunity to reconsider, not obedience to the message.

## Proposed durable rows

### MaterializedDeliveryReceipt

Suggested fields:

- receipt_id
- delivery_event_id
- receiver_id
- claim_ref
- provenance_root
- materialized_minute
- wake_status
- replan_trigger_id, nullable

The row is append-only. It records the coordinator transition and does not replace the InformationEventQueue envelope, delivery status or KnowledgeLedger claim.

### ConsumedReplanRecord

Suggested fields:

- consumption_id
- trigger_id
- agent_id
- reason
- source_ref
- due_minute
- processed_minute
- batch_id or deterministic batch key

This row records consumption provenance. It does not replace the planner result.

## Ownership

InformationEventQueue owns authored envelopes, delivery status and transport provenance.

KnowledgeLedger owns durable private evidence.

GlobalNpcWorldEventCoordinator owns the in-process transition from completed delivery to agent knowledge reference and wake scheduling.

NpcReplanQueue owns pending trigger ordering and completion state.

A new append-only provenance owner may persist coordinator materialization receipts and consumed replan records, or these rows may be added to the existing coordinator/replan owners if that preserves clean ownership. The implementation choice remains open.

## Restore validation

A future coherent world checkpoint should fail closed when any of these conditions occurs:

- materialization references an event whose queue status is not DELIVERED;
- materialization receiver differs from envelope receiver;
- materialized claim cannot be found in the restored receiver evidence/knowledge state when the receipt asserts knowledge was applied;
- receipt points to a replan trigger that is unknown to both pending and consumed provenance;
- `KNOWLEDGE_DELIVERED` trigger source differs from the delivery event;
- trigger agent differs from delivery receiver;
- receipt or consumption timestamp lies after restored semantic time;
- the same delivery is materialized twice as distinct successful receipts;
- the same trigger is consumed twice;
- a completed-trigger ID is present without enough structured provenance to reconstruct its owner and source.

Migration from the previous checkpoint must remain conservative. Old saves may restore with an empty new provenance ledger. Restore must not infer historical receipts from final knowledge, current routes, completed trigger names or agenda results.

## Acknowledgement boundary

This contract does not create acknowledgement semantics. A receiver may possess evidence and receive a planning wake-up without sending a check-back or accepting the instruction.

If acknowledgement becomes first-class later, it must be represented as its own event or owner and linked explicitly.

## AutoPTU boundary

This provenance layer belongs to world-agent simulation. It does not grant battle legality, movement, reactions, status effects, Abilities, Items or Trainer Features.

If a replanned world intent requires structured mechanics, the existing explicit `REQUEST_AUTOPTU` handoff remains mandatory. AutoPTU owns tactical resolution while bound.

## Acceptance criteria for implementation

An implementation is ready when tests demonstrate at minimum:

1. delivered event -> materialization receipt -> matching `KNOWLEDGE_DELIVERED` trigger round-trip;
2. consumed trigger retains structured receiver/source provenance after restart;
3. terminal failed or deferred messages cannot obtain successful materialization receipts;
4. receiver/source tampering fails even if a checkpoint digest is recomputed;
5. migration from the prior checkpoint produces no invented materialization or consumption history;
6. a delivered message can trigger replanning while the resulting selected plan lawfully remains unchanged or chooses a competing obligation.