# Global NPC AI Readiness Snapshot — Pass 284

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository evidence

Pass 284 adds selective event-triggered replanning for persistent/recurring NPC world agents.

Executable evidence:
- `tools/global_npc_replanning.py`
- `implementation/global-npc-event-replanning-fixture-v1.json`
- `tests/test_global_npc_event_replanning.py`

The Pass 283 information transport now exposes sender/receiver identity in delivery results so successful delivery can be routed into a receiver-specific replan trigger without faction-wide or region-wide polling.

Covered contracts include due-only wake-up, per-agent selectivity, same-window trigger coalescing, deterministic ordering, trigger provenance, queue snapshot/restore, duplicate trigger rejection, completed-trigger persistence, private-knowledge update and agenda change after information delivery.

Durable persistence of the Pass 283 information-delivery queue itself remains unresolved. Pass 284 persists the separate replanning queue only.

## Read-only AutoPTU-Java evidence

Live main inspected at:
`d6c42c2d7c6750a71f10614d2db7525757cc4dca`

Head commit: `Extract declarative temporary-effect lifecycle cleanup hook (#362)`.

This remains narrow evidence for a reusable temporary-effect cleanup seam routed through round-start lifecycle infrastructure. It does not prove complete turn/round lifecycle or complete status-family coverage.

## Read-only AutoPTU Python evidence

Live main inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head commit remains presentation-only (`Career: keep battle coordinates synced after viewport resize (#237)`) and explicitly states that battle rules/outcomes do not change.

## Permanent capability-category audit

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy / initiative: VERIFIED within audited contracts;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING depending on behavior;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for autonomous structured tactical choice;
- Minecraft / Cobblemon / Craftics adapter and playback support: PARTIAL / BLOCKING end-to-end.

No representative implementation is treated as proof of its entire family.

## Pass 284 dependency interpretation

The new wake-up queue, information-driven eligibility changes, off-screen agenda reevaluation and semantic event persistence are world-agent functions. They do not depend on AutoPTU tactical capabilities.

If a replanned world intent crosses into a structured encounter, dependency classification follows the exact behavior requested:
- pursuit/interception/forced movement -> complete movement;
- mechanical weather/hazard/zone/reaction effects -> terrain/weather/hazards/zones/reactions;
- delayed or temporary combat effects -> full lifecycle/status plus the owning move/ability/item/feature behavior;
- autonomous tactical decisions -> AI tactical policy;
- visible execution fidelity -> Minecraft/Cobblemon/Craftics adapter/playback support.

A `ReplanTrigger` is never promoted into a PTU Reaction, Interrupt or Action.

## PTU/Caelo/Kairos authority

Pass 284 adopts no PTU, Caelo or Kairos rule. Wake-up reasons, coalescing, persistence and semantic-time scheduling are Ouros simulation policy.

`SOURCE_HAS_RULE != OUROS_USES_RULE` remains binding.

## Open implementation risks

- durable persistence of the information-delivery queue itself;
- scalable audience/recipient resolution;
- event budgets/backpressure for very large bursts;
- production storage transaction boundaries between message delivery, knowledge update and replan scheduling;
- forgetting/deception/source confusion;
- resource/inventory-aware intent generation;
- belief-aware dialogue projection;
- production local-adapter acknowledgement;
- scale testing with thousands of persistent agents and pending events.
