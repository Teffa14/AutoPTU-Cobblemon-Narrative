# Global NPC AI Readiness Snapshot — Pass 285

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository evidence

Pass 285 adds explicit sender-side audience resolution before Pass 283 transport.

Executable evidence:
- `tools/global_npc_audience.py`
- `implementation/global-npc-audience-resolution-fixture-v1.json`
- `tests/test_global_npc_audience.py`

Covered contracts include directional relationship relevance, explicit institutional recipient duty, channel reachability, bounded fanout, deterministic tie-breaking, rejection reasons and the invariant that shared faction membership alone does not create an audience.

Audience selection does not mutate knowledge. Pass 283 remains delivery authority; Pass 282 remains belief/provenance authority; Pass 284 remains wake-up/replanning authority.

## Read-only AutoPTU-Java evidence

Live main inspected at:
`a61cec7f2f1a198d31ef59511afa199d7422a6d1`

Head commit: `Add global ability phase traversal hook`.

The commit adds `GlobalAbilityPhaseEffectHook` plus tests showing stable battle-roster traversal through an existing ability phase-effect registry and phase filtering. This is meaningful narrow evidence for ability/lifecycle infrastructure. It does not prove the complete Abilities family or the complete turn/round lifecycle.

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

No category is promoted because one representative hook exists.

## Pass 285 dependency interpretation

Recipient ranking, institutional routing, reachability filtering and fanout budgeting are world-agent functions. They require no AutoPTU tactical capability.

If information later causes a structured encounter, dependency classification follows the requested mechanics exactly:
- pursuit/interception/forced movement -> complete movement;
- mechanical weather/hazard/zone/reaction effects -> terrain/weather/hazards/zones/reactions;
- temporary/delayed effects -> lifecycle/status plus owning move/ability/item/feature behavior;
- autonomous tactical selection -> AI tactical policy;
- visible end-to-end execution -> Minecraft/Cobblemon/Craftics adapter/playback support.

An audience score is never a PTU skill check, command, action, reaction or social mechanic.

## PTU/Caelo/Kairos authority

Pass 285 adopts no PTU, Caelo or Kairos rule. Recipient scoring, thresholds and fanout budgets are Ouros simulation policy.

`SOURCE_HAS_RULE != OUROS_USES_RULE` remains binding.

## Open implementation risks

- durable persistence of the Pass 283 information-delivery queue;
- direct integration from audience selection into envelope scheduling;
- event budgets/backpressure for large communication bursts;
- explicit broadcast/publication audience expansion;
- forgetting, deception and source confusion;
- resource/inventory-aware intent generation;
- belief-aware dialogue projection;
- production local-adapter acknowledgement;
- scale tests with thousands of contacts and pending events.
