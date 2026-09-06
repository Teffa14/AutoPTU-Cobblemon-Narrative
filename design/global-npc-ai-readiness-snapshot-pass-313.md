# Global NPC AI readiness snapshot — pass 313

Status: DESIGN EVIDENCE / NOT CANON
Date: 2026-09-06

Pass 313 persists assessment-dependent decisions, explicit decision reviews and selective consequence repairs inside the atomic global NPC world checkpoint. The new checkpoint work itself is world-simulation persistence and requires no AutoPTU battle capability.

Read-only engine evidence checked during this pass:

AutoPTU-Java main: `ae2a9c9a105615291b12ef9f24c8ab483e2aa187`, commit `Align round history rotation after initiative rebuild (#383)`, dated 2026-09-06. The change adds a post-initiative round-start hook and moves round-history rotation after initiative rebuild, with Python-oracle parity coverage. This strengthens one ordering seam inside round lifecycle/history bookkeeping only. It does not establish complete round lifecycle, general delayed effects, complete damage/injury semantics or all effect ordering.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, commit `Career: keep battle coordinates synced after viewport resize (#237)`, dated 2026-08-29. The commit explicitly states that the change is presentation-only and does not alter battle rules or outcomes.

Capability classification from live evidence:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL; PR #383 verifies one round-start/history ordering seam only;
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

No capability category is promoted in Pass 313.

`The Night Shift After the Revision` has a reduced version requiring no tactical combat capability. Its full elevated-service-complex version depends on targeting/LoS for spatial rescue legality, base movement for traversal, complete movement for wind/forced movement/interception, core calculations and action economy for tactical resolution, lifecycle for timed platform or deterioration behavior, stateful damage for environmental harm, status lifecycle for persistent conditions, and terrain/weather/hazards/zones/reactions for exposed surfaces and reactive rescue. Move-specific behavior, Abilities, Items and Trainer Features apply only when explicitly authored and verified. General autonomous tactical rescue remains blocked on AI tactical policy, and final visible authoritative execution still depends on Minecraft/Cobblemon/Craftics adapter/playback support.

PTU/Caelo/Kairos authority remains unchanged. Public sources in Pass 313 contribute narrative structures only. No new mechanical overlay or canon element is activated.
