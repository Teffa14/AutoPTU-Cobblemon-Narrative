# Global NPC Communication Runtime Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPC communication flows.

## Purpose

Passes 282-285 separated memory, transport, selective wake-up and sender-side audience selection. This contract closes the runtime seam between audience choice and durable delivery while keeping load bounded.

```text
private sender claim
-> explicit audience resolution
-> deterministic channel choice
-> durable information envelope
-> semantic-time delivery queue
-> bounded due-event processing
-> receiver knowledge ledger
-> selective replanning wake-up
```

No stage implies faction-wide knowledge or tactical resolution.

## Durable queue

The information queue snapshot schema is `OUROS_NPC_INFORMATION_QUEUE_V1`.

A snapshot preserves pending envelopes, delivery status, delivered event IDs and local-projection acknowledgements still awaiting resolution. Queue restoration assumes the authoritative NPC knowledge ledgers and channel registry are restored by their owning persistence layers.

Restart must not:
- deliver a future message early;
- duplicate an already delivered event;
- erase a pending message;
- turn an unacknowledged local conversation into a completed delivery;
- change delivery ordering for identical state.

## Bounded processing

`process_due_budgeted(semantic_minute, max_events=N)` processes at most N due envelopes.

Due envelopes beyond that budget stay in the queue. Default private-message policy is defer, not drop.

This is deliberate. A temporary load spike is not evidence that a message never existed. Dropping or coalescing information requires a separate explicit channel policy because it can change world causality.

`OVER_BUDGET != MESSAGE_DESTROYED`

The runtime exposes `deferred_due_count` so production scheduling can detect backlog and allocate later capacity.

## Audience-to-envelope integration

`tools/global_npc_communication_runtime.py` consumes Pass 285 `AudienceSelection` semantics and Pass 283 `InformationEventQueue` transport.

For each selected receiver it chooses one declared reachable channel deterministically:
1. prefer currently available channels;
2. prefer lower semantic latency;
3. break ties by stable channel ID.

Only selected recipients receive envelopes. Shared faction membership cannot create an envelope by itself.

Event, message and claim IDs derive from a caller-provided unique dispatch ID plus receiver ID. The caller therefore owns dispatch-ID uniqueness across persistent history.

## Failure boundaries

An audience candidate can be selected but remain unscheduled if none of its declared reachable channels exists in the active channel registry. This returns `NO_KNOWN_CHANNEL` and does not mutate receiver knowledge.

A known channel may become unavailable after scheduling. Pass 283 then returns `FAILED_CHANNEL_UNAVAILABLE`; it does not pretend delivery occurred.

A channel requiring visible/local presentation still stops at `WAITING_LOCAL_ACK` until the adapter confirms the interaction.

## Broadcast/publication exclusion

This contract handles explicit receiver envelopes.

It does not implement newspapers, radio, public boards, mass alerts, social feeds or faction-wide broadcasts. Those mechanisms need their own audience-expansion, retention and overload semantics instead of setting an enormous private-message fanout budget.

## Authority boundaries

Ouros owns communication intent, audience selection, semantic scheduling, knowledge provenance and world-level consequences.

Minecraft/Cobblemon may project local conversations or media surfaces and acknowledge completion. It does not decide who learned a claim simply because entities were nearby.

AutoPTU is not used for ordinary information transport. If a later consequence becomes a structured encounter, the world-agent layer emits the existing explicit AutoPTU handoff.

## Determinism

Identical sender state, candidate set, relationships, memberships, channel registry, queue state and semantic time must yield identical selected receivers, channel choices, delivery ordering and backlog counts.
