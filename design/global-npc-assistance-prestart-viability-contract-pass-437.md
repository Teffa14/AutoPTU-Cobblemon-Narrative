# Global NPC Assistance Pre-start Viability Contract — Pass 437

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 436 made a negotiated assistance agreement survive restart together with its structured terms and responder-owned `ScheduledCommitment`. The remaining causal gap was pre-start invalidation: after an agreement exists, later evidence can make the original plan risky or impossible before the promised window begins.

Pass 437 adds `OUROS_ASSISTANCE_COMMITMENT_VIABILITY_LEDGER_V1` as an append-only owner for that later evidence.

The agreement remains owned by `OUROS_ASSISTANCE_COUNTERPROPOSAL_COMMITMENT_LEDGER_V1`. Viability observations never rewrite the accepted terms.

## Observation model

A viability observation identifies:

- one negotiated `commitment_id` and its `proposal_id`;
- requester and responder;
- the responder as the observer/owner of execution viability;
- semantic minute;
- `AT_RISK`, `BLOCKED`, or `RESTORED` viability;
- a typed constraint family;
- a concrete constraint reference;
- evidence and provenance references.

Supported constraint families are intentionally generic:

- route unavailable;
- access revoked;
- actor unavailable;
- required resource unavailable;
- premise invalidated;
- another evidenced constraint;
- cleared, used only when viability is restored.

This vocabulary records why the responder must reconsider. It does not implement route, permission, injury, resource or investigation authorities itself.

## Causal invariants

Only the responder who owns the negotiated commitment can record execution viability through this owner. Requester knowledge does not mutate responder viability automatically.

The observation must occur before the negotiated start minute. Once the work window begins, due/missed commitment state and any local/tactical resolution require their own owners.

History is monotonic in semantic time. The same observation ID may replay idempotently with identical content but cannot be reused for different content.

`RESTORED` requires an earlier `AT_RISK` or `BLOCKED` observation for the same commitment. It records that the previous blocker was cleared; it does not erase the earlier observation.

The original requester, responder, proposal, accepted time window, location metadata, scope metadata, alternative metadata and commitment provenance remain unchanged.

## Replanning behavior

Every new viability observation schedules one ordinary `EXTERNAL_EVENT` replan trigger for the responder only.

The trigger means `reconsider current world state because execution viability changed`.

It does not mean:

- cancel the commitment;
- reschedule it;
- notify the requester;
- move the responder;
- reserve a route;
- consume or allocate a resource;
- grant access;
- complete the assistance;
- start a battle;
- invoke AutoPTU.

If the requester needs to learn about the blocker, that information must travel through the existing communication/knowledge path and produce explicit receipt.

## Persistence boundary

The viability ledger has its own deterministic snapshot/restore contract. Integration into the coherent assistance world checkpoint is intentionally left to a subsequent pass so this slice can first establish the owner and invariants independently.

Until that integration exists, no feature should assume these observations survive an outer assistance-world restart atomically with V3.

## Mechanical capability posture

The pre-start viability owner requires no battle capability family.

If replanning later produces a mechanically rich field scene, that scene must independently classify all permanent capability categories:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

A blocker record is world evidence, not proof that any tactical mechanic exists.

## Verification

`tests/test_global_npc_assistance_commitment_viability.py` covers:

- a route blocker preserving the accepted commitment unchanged;
- responder-only wake-up through the ordinary replan queue;
- append-only `AT_RISK -> RESTORED` history;
- rejection of ungrounded `RESTORED` state;
- responder ownership and pre-start timing boundaries;
- unknown commitments and invalid state combinations;
- replay idempotency and conflicting identity rejection;
- monotonic semantic history;
- snapshot/restore;
- a source-level guard against tactical execution, route reservation, resource allocation and commitment mutation entering this owner.
