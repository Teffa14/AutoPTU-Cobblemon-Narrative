# Global NPC assistance deferral contract — Pass 430

Status: IMPLEMENTED / NON-CANON ARCHITECTURE
Date: 2026-09-11

## Scope

This pass owns one narrow transition: a durable `DEFER_ASSISTANCE_REQUEST` may create one future reconsideration wake-up for the responder.

It does not create an assistance commitment, promise future help, alter the requester, reserve travel, reserve inventory/resources, mutate relationships, resolve a quest, project a Minecraft entity or execute AutoPTU mechanics.

## Preconditions

The original world action must remain a `PLANNED` `REQUEST_ASSISTANCE` with another explicit actor as target.

The response must remain a `PLANNED` `DEFER_ASSISTANCE_REQUEST`. Its actor must be the request target and its target must be the original requester.

The response must preserve the request-delivery replan trigger in its durable trigger history. The reconsideration minute must be strictly later than the response decision. An optional expiry may equal or follow reconsideration, but may not precede it.

## Durable record

`OUROS_ASSISTANCE_DEFERRAL_LEDGER_V1` stores:

- deferral identity;
- original request action identity;
- DEFER response action identity;
- requester and responder identities;
- reconsideration semantic minute;
- optional expiry semantic minute;
- wake priority;
- generated replan trigger identity;
- provenance root, which is the DEFER response action identity.

Identical replay is idempotent. Reusing one deferral identity with conflicting content fails closed.

## Wake-up behavior

The pass schedules one ordinary `ReplanTrigger` in the existing global `NpcReplanQueue`.

Reason: `SCHEDULE_DUE`.

Agent: the responder only.

Due minute: the declared reconsideration minute.

Source reference: the durable DEFER response action ID.

A future due wake means only “reconsider now.” It does not guarantee that assistance wins agenda competition. Current goals, needs, commitments, knowledge, permissions, risk, travel and situational intents remain authoritative inputs to the ordinary planner.

## Window semantics

Before reconsideration: `WAITING`.

At or after reconsideration and before optional expiry: `OPEN`.

After optional expiry: `EXPIRED`.

Expiry is descriptive in this pass. It does not delete history or fabricate an answer.

## Persistence boundary

The deferral ledger has deterministic snapshot/restore. The global replan queue already persists scheduled triggers through the world checkpoint. This pass deliberately does not yet add the deferral ledger itself to `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1`; that coherent-generation integration remains a follow-up seam.

## PTU boundary

No PTU battle capability is exercised by scheduling or opening a deferral window. If later replanning selects an intent that requires structured mechanics, the existing `REQUEST_AUTOPTU` boundary remains mandatory.

No representative AutoPTU mechanic should be interpreted as verification of a full capability family.
