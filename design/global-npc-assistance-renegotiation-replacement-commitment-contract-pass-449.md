# Global NPC Assistance Renegotiation Replacement Commitment Contract — Pass 449

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 448 can return an explicit requester acceptance of replacement terms to the responder through the ordinary information network. This pass turns that delivered acceptance into one new responder-owned executable commitment while preserving the superseded agreement as historical evidence.

The owner is `materialize_assistance_renegotiation_replacement_commitment(...)` in `tools/global_npc_assistance_renegotiation_replacement_commitment.py`.

## Causal chain

`old commitment -> adverse condition -> request to reopen -> delivered permission -> replacement proposal -> delivered proposal -> requester acceptance -> delivered acceptance reply -> replacement commitment`

Every stage remains independently queryable.

A private acceptance cannot create the replacement. A queued or failed reply cannot create it. The responder must possess terminal `DELIVERED` REPORT evidence of the exact accepted proposal.

## Execution and history boundary

The superseded commitment remains in its durable historical ledger. Its proposal lineage and provenance remain unchanged.

The responder agenda changes from the superseded `ScheduledCommitment` to the replacement `ScheduledCommitment`. This prevents the old schedule from remaining executable after the replacement becomes authoritative for future planning.

The replacement keeps the old commitment's intent kind, priority, hard/soft classification, grace window, knowledge requirements, permission requirements, local-projection flag and structured-mechanics flag. The replacement proposal supplies the new start/end window plus its location/scope/alternative provenance metadata.

The replacement requires a new commitment id. Exact replay is idempotent. Conflicting id reuse or an agenda that no longer matches durable history fails closed.

## Validation boundary

Materialization requires all of the following:

- the replacement-offer outcome is exactly `ACCEPT_REPLACEMENT_TERMS`;
- the decision refers to the exact replacement proposal;
- the proposal points to the exact superseded commitment and proposal;
- requester and responder bindings remain stable through the chain;
- the decision reply event is terminal `DELIVERED` from requester to responder;
- responder knowledge contains the REPORT copied from the exact authored acceptance;
- subject, structured payload and provenance match the durable proposal/decision records;
- materialization does not predate responder receipt;
- the accepted replacement start is not already in the past;
- the superseded schedule exists exactly once in the responder agenda on first materialization.

## Ownership exclusions

This owner does not delete historical ledgers. It does not decide whether renegotiation was socially acceptable. It does not assign blame, trust, reputation, compensation or relationship deltas. It does not reserve travel, grant access, allocate resources, move actors, complete assistance, create quest completion or invoke AutoPTU.

Those effects require separate evidence-driven owners.

## Encounter boundary

The commitment only establishes future obligation timing. It does not pre-author the encounter that will satisfy the obligation.

A reduced narrative path can run with semantic time, communication, travel/access checks, world evidence and ordinary agenda execution.

A rich path may later become survey, escort, protection, retrieval, containment, extraction or another structured objective. That scene must be built from live world state and individually admitted engine capabilities.

## Permanent capability classification

- targeting/footprints/range/LoS — VERIFIED only inside audited scopes;
- base movement legality — VERIFIED only inside audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only inside audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING according to requested behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated;
- AI legal-action infrastructure — specialized verbs require explicit admission;
- AI tactical policy — BLOCKING for specialized nonstandard objectives unless separately verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Live evidence checked 2026-09-12

AutoPTU-Java `main` is `1ff22f2bb1495527ca6aea08d40ce87f38f4a9d5`, merge of PR #452. The new runtime dispatcher applies Feature-specific pre-dispatch guards and dispatches switch-trigger planners from authoritative runtime state. This strengthens one reactive switching seam. It does not verify generic reactions, full action economy or the Trainer Features family.

AutoPTU Python `main` remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its head is presentation-only and does not change battle rules or outcomes.

## Next seam

The replacement commitment now owns future schedule execution, while the superseded commitment stays historical. The next persistence question is checkpoint integration: a restart must restore both lineage records and an agenda containing only the currently executable replacement schedule, without resurrecting the superseded one. Later accountability can then reason over both agreements without controlling scheduling itself.
