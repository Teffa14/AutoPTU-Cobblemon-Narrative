# Global NPC Event-Triggered Replanning Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent and recurring Ouros NPC world agents.

## Purpose

Named NPCs must not execute full decision logic every Minecraft tick. The global world-agent layer reacts to meaningful semantic changes and wakes only affected agents.

Core flow:

```text
world event / message / schedule / need / social change / travel invalidation
-> explicit ReplanTrigger
-> persistent semantic-time wake-up queue
-> due triggers grouped by agent
-> one agenda reevaluation for that agent and processing window
-> world intent OR explicit REQUEST_AUTOPTU
```

`WORLD_EVENT != GLOBAL_POLL_ALL_NPCS`

## Trigger families

Initial reusable reasons are:
- knowledge delivered;
- schedule due;
- travel invalidated;
- need threshold crossed;
- social state changed;
- external world event.

These reasons are world-simulation semantics. They are not PTU Actions, Interrupts or Reactions.

## Selective wake-up

A trigger names one affected persistent agent. A delivered message wakes the receiver, not every member of the same faction and not every NPC in the region.

Audience resolution is a separate upstream responsibility. It must produce explicit recipients before this layer schedules work.

## Coalescing

Several due triggers for the same agent in one processing window produce one `ReplanBatch`. The batch preserves every trigger ID, reason and source reference while avoiding repeated agenda evaluation.

Coalescing must not merge different agents or erase provenance.

## Semantic time

Wake-up time uses Ouros semantic minutes. Wall clock, Minecraft ticks, chunk load and entity visibility do not decide whether a trigger is due.

## Persistence and restart

The replan queue serializes pending triggers, known trigger IDs and completed trigger IDs with schema `OUROS_NPC_REPLAN_QUEUE_V1`.

A restart must preserve:
- due minute;
- agent target;
- trigger reason;
- source reference;
- priority;
- duplicate protection;
- completed-trigger protection.

A restart cannot make a future trigger fire early. A completed trigger cannot replay merely because the server restarted.

This contract covers the replanning queue. Durable persistence of the separate Pass 283 information-delivery queue remains an independent integration gap.

## Knowledge delivery integration

Pass 283 delivery results expose the receiver ID. A successful delivery may:
1. update that receiver's private world-agent knowledge reference;
2. preserve the memory provenance root;
3. schedule `KNOWLEDGE_DELIVERED` for that receiver;
4. reevaluate that receiver's agenda when the trigger is due.

Failed or merely queued messages do not wake the receiver as if knowledge had arrived.

## Agenda boundary

The replan layer delegates selection to the global agenda planner from Pass 279. It does not create a second utility model.

An incoming fact can make a previously ineligible intent eligible. Example: a courier learns that a route is closed, then selects `REPLAN_ROUTE` at the next explicit wake-up instead of continuing from stale knowledge.

## AutoPTU boundary

Replanning chooses world intent only. If the selected intent requires structured mechanics, the existing planner emits `REQUEST_AUTOPTU`.

This layer never selects squares, Moves, initiative, damage, statuses, knockback, reactions or tactical targets.

## Minecraft/Cobblemon boundary

A loaded entity is not required for a named NPC to wake and replan. Local projection is requested only when the resulting world intent needs visible/local execution.

## Region neutrality

Marea, Sendero, Puerto Bruma and all other locations remain content bindings and fixtures. Core trigger semantics are global.

`LOCAL_EVENT_SOURCE != LOCAL_AI_ARCHITECTURE`

## Current executable evidence

- `tools/global_npc_replanning.py`
- `implementation/global-npc-event-replanning-fixture-v1.json`
- `tests/test_global_npc_event_replanning.py`

## Deferred work

- durable storage for the Pass 283 information queue itself;
- scalable audience/recipient resolution;
- rate/budget policy for very large event bursts;
- event-triggered travel and social integrations beyond the generic trigger contract;
- distributed persistence if Ouros later shards world simulation;
- production Minecraft adapter acknowledgement.
