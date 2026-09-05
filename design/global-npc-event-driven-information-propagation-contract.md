# Global NPC Event-Driven Information Propagation Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: region-neutral communication scheduling for persistent and recurring Ouros NPCs.

## Purpose

Pass 282 established per-agent knowledge ledgers and explicit one-to-one information transfer. This contract defines how those transfers are scheduled and delivered across a large cast without scanning every NPC every world tick and without turning factions, settlements or communication systems into shared omniscience.

The transport layer schedules information. `tools/global_npc_memory.py` remains owner of claims, provenance roots, report attenuation and belief assessment.

`TRANSPORT != BELIEF`

## Information flow

```text
sender legally knows claim
-> communication opportunity/channel selected
-> message event queued at semantic time
-> latency / availability / projection gates
-> delivery event becomes due
-> Pass 282 creates receiver report claim
-> receiver may re-evaluate belief and agenda
```

No receiver learns a claim merely because a sender, faction or world system knows it.

## Event-driven scheduling

The scheduler processes communication events by semantic due time. It does not require a high-frequency update over every persistent NPC.

Each envelope records:
- stable event ID;
- stable message ID;
- sender and receiver;
- source claim ID;
- receiver claim ID;
- channel;
- creation semantic minute;
- delivery semantic minute;
- optional receiver trust input owned by the social layer.

Equal-time events use deterministic event-ID ordering. Identical persistent state must replay identically.

## Channels

A communication channel may define:
- kind;
- latency;
- current availability;
- whether local Minecraft/Cobblemon projection is required before delivery can become authoritative.

Examples may later include face-to-face conversation, courier, telephone, institutional dispatch, bulletin, radio or other canon-supported media. Their existence, coverage and speed are content/world facts, not assumptions created by this contract.

A broadcast service is implemented as explicit scheduled receiver deliveries or a higher-level audience resolver. Membership alone never mutates all member ledgers.

`FACTION_MEMBERSHIP != AUTOMATIC_BROADCAST`

## Provenance

Forwarding uses the Pass 282 source claim as its parent. The original `provenance_root` therefore survives every relay.

Two delivery paths derived from one original observation still represent one independent root. A second genuinely independent observation can add another root.

`DELIVERY_PATH_COUNT != INDEPENDENT_SOURCE_COUNT`

The transport layer must not manufacture corroboration.

## Availability and failure

A message whose channel is unavailable when delivery is attempted becomes an explicit delivery failure. Failure does not create receiver knowledge.

Future designs may distinguish retryable outage, permanent failure, queue congestion, interception, loss or delay. Those states require explicit contracts; this first version does not infer them from a generic failure.

## Local projection acknowledgement

Some communication requires a local visible interaction. In that case the event enters `WAITING_LOCAL_ACK` when due. The receiver ledger remains unchanged until the adapter returns an accepted acknowledgement.

Minecraft animation, proximity or entity presence cannot silently create knowledge.

`VISIBLE_CONTACT != AUTHORITATIVE_DELIVERY`

A rejected acknowledgement records failure; it does not pretend the conversation occurred.

## Persistence and replay

Delivered event IDs are idempotency keys. A restart/replay must not deliver an already accepted event twice.

Production persistence must store pending envelopes, awaiting acknowledgements, channel-relevant durable state and delivered-event IDs. The current executable fixture proves deterministic in-process semantics; durable storage integration remains open.

## Relationship and faction integration

Pass 280 can influence whether an NPC chooses to communicate and may supply trust used by Pass 282 attenuation. This scheduler does not decide affection, loyalty, secrecy or institutional access by itself.

A later audience resolver may use relationship, role, permission, topic sensitivity and channel access to decide recipients. It must return explicit recipients before delivery scheduling.

## Agenda integration

A delivered claim can make an existing world intent newly eligible or urgent. Replanning should be event-triggered for affected recipients rather than a global NPC scan.

The communication event itself does not directly modify goals, faction standing or relationships. Those changes need their owning subsystem and provenance.

## AutoPTU boundary

Ordinary information delivery uses no PTU tactical mechanics.

If a communication scene becomes a structured confrontation, chase or battle, the global world-agent layer must issue `REQUEST_AUTOPTU`. This transport layer never resolves targeting, movement, initiative, damage, statuses, reactions, Moves, Abilities, Items or Trainer Features.

## Minecraft/Cobblemon boundary

Remote/off-screen communication can complete without a loaded Minecraft entity when the channel contract permits it. Face-to-face or other projection-required channels wait for adapter acknowledgement.

Minecraft does not own message truth, provenance, receiver belief or persistent NPC identity.

## Current executable states

- `QUEUED`
- `WAITING_LOCAL_ACK`
- `DELIVERED`
- `FAILED_CHANNEL_UNAVAILABLE`

These are transport states, not beliefs or PTU Status Afflictions.

## Non-goals for v1

This version does not yet simulate:
- intentional deception;
- accidental paraphrase or mutation of claim content;
- source confusion or forgetting;
- cryptography or interception;
- bandwidth/congestion;
- dynamic audience discovery;
- mass-media editorial policy;
- probabilistic gossip selection;
- tactical communication actions.

Those require separate contracts so they cannot be introduced accidentally through transport code.

## Canon status

This contract canonizes no communication technology, faction network, newspaper, radio service, settlement, route or NPC behavior. Fixture agents and channels are synthetic validation data.
