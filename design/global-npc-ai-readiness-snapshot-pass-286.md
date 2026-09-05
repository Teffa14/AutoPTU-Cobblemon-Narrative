# Global NPC AI Readiness Snapshot — Pass 286

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository evidence

Pass 286 closes three runtime gaps from Pass 285:
- durable snapshot/restore for the private information-delivery queue;
- direct audience-to-envelope integration;
- bounded due-event processing with explicit deferred backlog.

Executable evidence:
- `tools/global_npc_information_network.py`
- `tools/global_npc_communication_runtime.py`
- `implementation/global-npc-communication-runtime-fixture-v1.json`
- `tests/test_global_npc_communication_runtime.py`

Private messages are deferred rather than dropped when the per-cycle budget is exhausted. Restart preserves pending envelopes and delivered-event identity. Shared faction membership still cannot create an audience or envelope by itself.

## Read-only AutoPTU-Java evidence

Live main inspected at:
`a61cec7f2f1a198d31ef59511afa199d7422a6d1`

Head commit remains `Add global ability phase traversal hook`.

The head provides narrow tested evidence for stable roster traversal through an ability phase-effect registry and phase filtering. This remains partial infrastructure evidence for Abilities and lifecycle. It does not verify the complete Abilities family or complete turn/round lifecycle.

## Read-only AutoPTU Python evidence

Live main inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head remains `Career: keep battle coordinates synced after viewport resize (#237)` and explicitly states that battle rules/outcomes do not change.

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

No category is promoted from a representative hook.

## Pass 286 dependency interpretation

Audience routing, private envelope scheduling, queue persistence and backlog budgeting are Ouros world-agent functions. They require no AutoPTU tactical capability.

If delayed or missing information later causes a structured encounter:
- pursuit/interception/forced movement -> complete movement;
- mechanical weather/hazard/zone/reaction behavior -> terrain/weather/hazards/zones/reactions;
- delayed/temporary effects -> lifecycle/status plus the owning Move/Ability/Item/Feature behavior;
- autonomous tactical choice -> AI tactical policy;
- visible end-to-end execution -> Minecraft/Cobblemon/Craftics adapter/playback support.

Queue priority, latency and backlog are not PTU initiative, turn order or action economy.

## PTU/Caelo/Kairos authority

Pass 286 adopts no PTU, Caelo or Kairos rule. Queue budgets, snapshot schema and deterministic channel selection are Ouros MMO simulation policy.

`SOURCE_HAS_RULE != OUROS_USES_RULE` remains binding.

## Open implementation risks

- authoritative persistence for NPC memory ledgers themselves;
- direct delivery-to-replanning integration in one runtime coordinator;
- explicit public/broadcast/publication channels with separate retention/overload policy;
- backlog aging, priority classes and fairness under sustained load;
- forgetting, deception and source confusion;
- resource/inventory-aware intent generation;
- belief-aware dialogue projection;
- production local-adapter acknowledgement;
- scale tests with thousands of agents and pending envelopes.
