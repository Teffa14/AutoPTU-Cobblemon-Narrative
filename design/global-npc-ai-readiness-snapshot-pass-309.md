# Global NPC AI readiness snapshot — pass 309

Status: DESIGN EVIDENCE / NOT CANON
Date: 2026-09-06

Pass 309 adds explicit propagation for superseding custody assessments. The propagation runtime itself uses world-simulation information infrastructure and does not require AutoPTU combat.

Read-only engine evidence checked during this pass:

AutoPTU-Java main: `3ca3540a94bafdb57ff69d2feaa56ec0b3d65d3b`, commit “Add reusable post-damage faint transition contract (#381)”, dated 2026-09-06. This provides a server-owned post-damage faint-transition seam and parity evidence against the Python oracle. It strengthens one part of the stateful damage path without establishing complete Substitute handling, prevention/reactions, Injuries, faint prevention, history rotation, all semantic events, source attribution, move behavior or end-to-end playback.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, commit “Career: keep battle coordinates synced after viewport resize (#237)”, dated 2026-08-29. The commit explicitly states that it changes presentation only and no battle rules or outcomes.

Capability classification retained from live evidence:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- Abilities: PARTIAL;
- Items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No capability category is promoted in Pass 309.

For `The Correction That Never Arrived`, the reduced version requires no tactical capability. The full damaged-annex version depends on complete movement for forced movement/interception/rescue displacement, lifecycle for delayed collapses, stateful damage for environmental injury, status lifecycle for persistent conditions, and terrain/weather/hazards/zones/reactions for dynamic structural danger. Move, Ability, Item and Trainer Feature dependencies apply only when those elements are authored. Autonomous tactical rescue remains blocked on AI tactical policy, while reliable visible execution remains constrained by Minecraft/Cobblemon/Craftics adapter/playback support.

PTU/Caelo authority remains unchanged. Public research in Pass 309 contributes narrative and information-propagation patterns only.
