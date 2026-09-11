# Global NPC assistance counterproposal terms delivery contract — Pass 433

Status: IMPLEMENTED GLOBAL CONTRACT
Canon authority: NONE. This file defines runtime behavior, not world lore.

## Purpose

Pass 432 made responder-authored counterproposal terms durable. The requester still learned only that a `COUNTERPROPOSE_ASSISTANCE_REQUEST` response existed. Pass 433 closes the information boundary between durable terms and recipient knowledge.

A stored proposal and a received proposal are different facts. Structured terms become usable requester knowledge only after an explicit information envelope reaches the requester through the ordinary communication runtime.

## Owner

Executable owner:
- `tools/global_npc_assistance_counterproposal_dispatch.py`

Regression:
- `tests/test_global_npc_assistance_counterproposal_dispatch.py`

Inputs:
- `OUROS_WORLD_ACTION_INTENT_LEDGER_V1` request and counterproposal response actions;
- `OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1` structured terms;
- the existing `InformationEventQueue` and per-agent `KnowledgeLedger` instances.

## Required causal chain

The dispatch must prove all of the following before scheduling terms:

1. the referenced proposal exists;
2. its provenance root is its `response_action_id`;
3. its request remains a PLANNED `REQUEST_ASSISTANCE` action;
4. requester and responder still match that request;
5. its response remains a PLANNED `COUNTERPROPOSE_ASSISTANCE_REQUEST` action;
6. responder and requester still match that response;
7. the response does not predate the request;
8. the terms message is not authored before the response;
9. both actors have explicit knowledge ledgers;
10. the named communication channel exists.

Failure is closed. No fallback broadcast or inferred faction recipient is permitted.

## Transport representation

`Claim.value` is currently a string contract. Pass 433 therefore serializes the structured proposal as deterministic compact JSON with sorted keys. The payload carries:

- proposal identity;
- request action identity;
- response action identity;
- proposed start and optional end;
- location reference;
- scope reference;
- alternative reference;
- expiry minute.

The source claim subject is:

`assistance_counterproposal_terms:<request_action_id>:<response_action_id>:<proposal_id>`

The claim provenance root is the responder's `response_action_id`, not the later message ID and not the original request.

This encoding is a transport representation. `OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1` remains the structured durable owner of the terms.

## Delivery semantics

Before delivery, only the responder owns the authored terms claim.

`QUEUED`, `FAILED_CHANNEL_UNAVAILABLE` and `WAITING_LOCAL_ACK` do not create requester knowledge.

After terminal `DELIVERED`, the ordinary information queue materializes a REPORT claim for the requester with parent-claim and provenance lineage intact.

An offer may arrive after its `expires_minute`. This is valid stale information. Expiry travels inside the payload so downstream policy can recognize that the offer is no longer actionable. Delivery must not silently convert expiry into acceptance, renewal or success.

## Explicit non-effects

Pass 433 does not:

- accept the proposal;
- create or modify a scheduled commitment;
- reserve the responder's time;
- reserve a route;
- move either actor;
- allocate items, tools, Pokémon or other resources;
- mutate relationships or faction state;
- complete a quest or incident;
- wake unrelated agents;
- infer that public/faction peers also heard the terms;
- invoke AutoPTU;
- resolve any PTU rule.

A future requester decision must explicitly accept, reject, defer or answer the received terms before a commitment can exist.

## Replay and identity

Exact replay with the same event/envelope identity is idempotent, including after terminal delivery. Reusing the event ID with different envelope content fails closed. Source-claim identity remains protected by the existing knowledge-ledger collision rules.

## PTU / Caelo / Kairos boundary

This pass is world-simulation communication. The Kairos source index remains a routing aid rather than a substitute for supplied PTU/Kairos rules. Nothing in PTU encounter, battle, movement, status, Ability, Item or Trainer Feature material grants automatic support to this communication layer.

If accepted assistance later becomes a structured encounter, the existing explicit `REQUEST_AUTOPTU` boundary remains mandatory.

## Capability posture for downstream encounter use

Pass 433 itself requires none of the battle capability families. A later mechanically rich assistance scene must classify its actual mechanics independently.

Current conservative live posture:

- targeting/footprints/range/LoS: VERIFIED only in audited scopes;
- base movement legality: VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only in audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by mechanism;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: VERIFIED only for audited ordinary actions;
- AI tactical policy: BLOCKING for specialized objective-aware rescue/escort/protect/retrieve/extract behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for specialized objective state, non-KO completion and in-flight recovery.

The current AutoPTU-Java evidence for replacement initiative is a real production seam but does not promote the whole action-economy family. AutoPTU Python's current head remains presentation-only relative to battle rules.

## Next seam

Once terms are delivered, the requester needs a durable responder-to-proposal decision with the proposal identity and delivery trigger in its causal history. Only a positive acceptance of the exact proposal should be eligible to create a later scheduled commitment. The counterproposal ledger also remains outside the assistance coherent checkpoint and must enter a later checkpoint revision before restart-safe end-to-end reliance.
