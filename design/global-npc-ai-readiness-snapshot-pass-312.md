# Global NPC AI readiness snapshot — pass 312

Status: DESIGN EVIDENCE / NOT CANON
Date: 2026-09-06

Pass 312 adds selective repair for consequences created by a reviewed assessment-dependent decision. The repair runtime itself is world-simulation logic and requires no AutoPTU battle capability.

Read-only engine evidence checked during this pass:

AutoPTU-Java main: `ae2a9c9a105615291b12ef9f24c8ab483e2aa187`, commit `Align round history rotation after initiative rebuild (#383)`, dated 2026-09-06. The change introduces a post-initiative round-start hook point and moves damage/injury history rotation behind initiative rebuild, with a Python oracle parity gate. This strengthens evidence for a specific ordering seam inside round lifecycle and history bookkeeping. It does not establish complete round lifecycle, complete history semantics, full damage/injury behavior or general effect ordering.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, commit `Career: keep battle coordinates synced after viewport resize (#237)`, dated 2026-08-29. The commit explicitly states presentation-only behavior with no battle-rule or outcome changes.

Capability classification from live evidence:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL; PR #383 adds verified ordering for one round-start/history seam only;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No capability category is promoted in Pass 312.

`The Gate After the Order` has a reduced version requiring no tactical combat capability. Its full storm-exposed inspection depends on complete movement for forced movement and interception, turn/round lifecycle for timed deterioration, stateful damage for environmental harm, status lifecycle if persistent conditions are authored, and terrain/weather/hazards/zones/reactions for unstable surfaces and rescue reactions. Move-specific behavior, Abilities, Items and Trainer Features apply only when the encounter explicitly invokes them. General autonomous rescue/combat still depends on AI tactical policy, and visible authoritative execution still depends on Minecraft/Cobblemon/Craftics adapter/playback support.

PTU/Caelo/Kairos authority remains unchanged. Public sources in Pass 312 contribute narrative and systems-design structures only. No new rules overlay is activated.
