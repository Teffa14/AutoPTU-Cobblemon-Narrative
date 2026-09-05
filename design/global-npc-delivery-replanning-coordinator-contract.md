# Global NPC Delivery-to-Replanning Coordinator Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPCs, independent of region.

## Purpose

Connect the existing private-information runtime to the existing event-triggered world-agent planner without global polling or duplicated subsystem authority.

The coordinator composes existing systems:

```text
private envelope becomes due
-> communication runtime attempts delivery
-> receiver knowledge ledger changes only on successful delivery
-> receiver world-agent knowledge reference changes
-> one KNOWLEDGE_DELIVERED wake-up is scheduled
-> simultaneous wake-ups may coalesce
-> existing agenda planner re-evaluates that receiver
-> ordinary world intent continues OR REQUEST_AUTOPTU/HOLD_AUTOPTU preserves structured ownership
```

`DELIVERED_INFORMATION -> SELECTIVE_REPLAN`

A queued, failed, deferred or unacknowledged message does not satisfy this transition.

## 1. Responsibility boundary

The coordinator owns orchestration only.

It does not redefine:
- audience selection;
- channel latency;
- message delivery semantics;
- memory provenance;
- belief assessment;
- goal/need/schedule scoring;
- tactical legality;
- combat resolution;
- Minecraft presentation.

Those responsibilities remain in their existing subsystem owners.

## 2. Successful-delivery gate

Only a delivery result whose status is `DELIVERED` may materialize a knowledge-driven replan.

Required delivery fields for a managed persistent NPC:
- `event_id`;
- `receiver_id`;
- `claim_id`;
- `provenance_root`.

The receiver's world-agent knowledge reference is updated through the existing Pass 284 delivery application seam. The underlying claim already resides in the receiver's Pass 282 knowledge ledger because the communication queue owns claim transmission.

## 3. Non-delivery states

The following do not produce a knowledge wake-up:
- message is not yet due;
- delivery is deferred because the communication budget is exhausted;
- channel is unavailable;
- visible/local delivery waits for adapter acknowledgement;
- local acknowledgement rejects delivery.

A later accepted local acknowledgement can be materialized through the same coordinator seam.

`MESSAGE_EXISTS != RECEIVER_KNOWS_MESSAGE`

## 4. Selective wake-up

A successful private delivery wakes only the explicit receiver.

The coordinator must not:
- wake all NPCs in a region;
- wake all members of a faction;
- wake every NPC connected to the sender;
- infer additional witnesses from Minecraft proximity;
- broadcast because the subject is important.

Publications and broadcasts require their own explicit audience-expansion contract.

## 5. Duplicate protection

One delivered communication event can materialize at most one knowledge-driven wake-up in a coordinator lifetime.

If a completed delivery result is presented again, its outcome is `NO_WAKE_DUPLICATE`.

The communication queue already preserves delivered-event identity. Pass 287 adds an orchestration guard so a replayed result cannot create an additional replan trigger.

Durable cross-process persistence of the coordinator materialization ledger remains a later persistence seam and must be handled together with durable knowledge-ledger state rather than implied by this in-memory guard.

## 6. Budget interaction

Pass 286's delivery budget remains authoritative for how many due private messages can be attempted in one communication cycle.

Therefore the number of agents awakened by newly processed private messages in a cycle is naturally bounded by successfully delivered events in that cycle.

Deferred due messages remain queued. Their receivers remain unchanged until delivery actually occurs.

This contract does not yet add a separate replan-work budget or fairness/aging policy. Those remain explicit follow-up work.

## 7. Coalescing

Pass 284 remains the owner of wake-up coalescing.

If one agent receives a message at the same semantic minute that a schedule, social, travel or other semantic event also triggers reconsideration, the replan queue may combine those causes into one `ReplanBatch` while preserving trigger IDs, reason codes and source references.

The agenda should be evaluated once for that batch.

## 8. AutoPTU ownership

Information delivery can wake an NPC while structured mechanics already own that actor.

If the receiver is `AUTOPTU_BOUND`, the existing global planner returns `HOLD_AUTOPTU` with `HOLD_EXISTING_AUTOPTU_BINDING`.

The coordinator must not use a new world-state fact to select squares, Moves, targets, initiative actions, damage, reactions or forced movement while the tactical engine owns resolution.

After the semantic AutoPTU result returns and the binding is released, world-agent planning can consume the updated knowledge normally.

## 9. Minecraft/Cobblemon ownership

Local visible communication may require adapter acknowledgement before the claim becomes delivered.

Minecraft/Cobblemon may display speech, gestures, travel or other presentation. The adapter cannot create canonical private knowledge merely because two entities were close enough to animate a conversation.

For world actions selected after replanning:
- world-semantic actions can continue off-screen where their contracts allow;
- local presentation actions request the adapter;
- structured mechanical actions request AutoPTU.

## 10. Determinism

For identical:
- communication-queue state;
- replan-queue state;
- agent state;
- agenda inputs;
- semantic minute;
- processing budget;

the coordinator must produce the same materialization and decision ordering.

## 11. Full and reduced encounter use

A narrative event can use two implementations without changing its premise.

Reduced world-state version:
- warning is delivered;
- receiver changes route, schedule, availability, report target or quest participation;
- no structured battle is required.

Full structured version:
- the same information causes confrontation, pursuit, rescue or another mechanical encounter;
- Ouros selects the world intent;
- AutoPTU resolves only the mechanics its current contracts actually verify.

The narrative layer must declare exact capability dependencies for the full version.

## 12. Initial executable evidence

- `tools/global_npc_world_event_coordinator.py`
- `implementation/global-npc-world-event-coordinator-fixture-v1.json`
- `tests/test_global_npc_world_event_coordinator.py`

The fixture proves that one private warning can change one courier's agenda while an uninformed nearby/background agent remains unchanged.

## 13. Explicit non-goals

Pass 287 does not implement:
- public news/broadcast expansion;
- durable knowledge-ledger storage;
- forgetting;
- deception;
- source confusion;
- inventory/resource reasoning;
- generated dialogue;
- replan fairness under sustained overload;
- tactical AI;
- local Minecraft movement/playback completion.
