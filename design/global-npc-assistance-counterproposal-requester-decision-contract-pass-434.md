# Global NPC Assistance Counterproposal Requester Decision Contract — Pass 434

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 433 made responder-authored counterproposal terms travel through the ordinary information network. Pass 434 adds the next ownership boundary: the original requester can make a durable decision about one exact delivered proposal.

A globally stored proposal is not consent. A delivered proposal is not consent. Only a requester-owned decision can accept or reject those terms.

## Inputs

The decision bridge consumes existing owners only:

- `OUROS_WORLD_ACTION_INTENT_LEDGER_V1` for the original request, responder counterproposal and requester decision;
- `OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1` for structured terms;
- `InformationEventQueue` for exact terms delivery and per-agent knowledge evidence;
- a `CoordinatedDecision` caused by the delivery wake-up.

## Supported requester actions

- `ACCEPT_ASSISTANCE_COUNTERPROPOSAL`
- `REJECT_ASSISTANCE_COUNTERPROPOSAL`

The recorded world action must name the exact `proposal_id` in `source_ref` and target the original responder.

## Required evidence

Before either action can become durable, the bridge verifies:

1. the referenced `REQUEST_ASSISTANCE` still exists as a PLANNED world action;
2. the referenced responder action is a PLANNED `COUNTERPROPOSE_ASSISTANCE_REQUEST`;
3. requester/responder bindings match the durable proposal;
4. the terms envelope exists and ran to terminal `DELIVERED`;
5. sender and receiver match responder and requester exactly;
6. authored and received claims retain the proposal response action as provenance root;
7. the received claim is REPORT evidence descended from the authored terms claim;
8. the structured JSON payload matches the durable proposal term for term;
9. the replan contains `replan:information:<terms_event_id>`;
10. the deciding actor is the original requester;
11. the agenda `source_ref` names the exact proposal;
12. acceptance occurs no later than `expires_minute` when an expiry exists.

A stale proposal may still be rejected as a historical offer. It cannot be accepted after expiry.

## Non-effects

Neither decision creates a scheduled commitment, reserves time, reserves a route, moves an actor, allocates equipment or inventory, changes a relationship, marks work complete, or enters AutoPTU.

Acceptance means only that the requester selected those terms. A later owner must convert an accepted proposal into a concrete commitment using the proposal's exact terms.

## Information boundary

`QUEUED`, failed-channel and `WAITING_LOCAL_ACK` terms do not authorize a requester decision. Global proposal existence also does not authorize it. The requester must possess the delivered claim.

This preserves the project invariant that shared world state is not shared cognition.

## Replay and tamper behavior

The existing world-action ledger provides idempotent replay for the same decision action ID and rejects conflicting reuse. The bridge additionally fails closed on changed proposal provenance, changed payload, wrong actor binding, wrong proposal source reference, missing delivery trigger and AutoPTU handoff attempts.

## AutoPTU capability dependency posture

This contract is world-simulation-only and can run without tactical resolution.

If an accepted proposal later becomes a tactical field operation, dependency classification remains explicit:

- targeting/footprints/range/LoS — VERIFIED only in audited scopes;
- base movement legality — VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only in audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated;
- AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract require explicit admission;
- AI tactical policy — BLOCKING for specialized objective policies;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized authoritative objective state, non-KO completion and in-flight recovery.

## Reduced encounter form

A complete reduced story can run as:

request -> counterproposal -> terms delivery -> requester replan -> explicit accept/reject -> later world simulation.

It needs semantic time, private knowledge, communications, world-action persistence and ordinary scheduling only.

## Full encounter form

An accepted negotiated scope may later become hazardous repair, escort, retrieval, containment, rescue or another field operation. Those mechanics remain downstream owners. Pass 434 never treats narrative agreement as tactical legality.

## Regression

`tests/test_global_npc_assistance_counterproposal_decision.py` covers exact delivered-term acceptance, rejection, undelivered isolation, requester ownership, exact proposal binding, delivery-trigger binding, provenance and payload tampering, expiry behavior, AutoPTU handoff rejection and idempotent replay.
