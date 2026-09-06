# Global NPC AI readiness snapshot — pass 310

Status: DESIGN EVIDENCE / NOT CANON
Date: 2026-09-06

Pass 310 records world decisions against the exact custody assessment claim known by the deciding actor and can later determine whether a superseding assessment exists and has actually reached that actor. The core runtime is world-simulation infrastructure and requires no AutoPTU combat.

Read-only engine evidence checked during this pass:

AutoPTU-Java main: `3ca3540a94bafdb57ff69d2feaa56ec0b3d65d3b`, commit “Add reusable post-damage faint transition contract (#381)”, dated 2026-09-06. The server-owned ordinary-damage ingress exposes a shared post-damage outcome classification and Python parity coverage. Substitute, prevention/reactions, Injuries, faint prevention, history rotation, semantic events, source attribution and broader move/content behavior remain outside that seam. This strengthens one portion of the stateful damage path without establishing the complete category.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, commit “Career: keep battle coordinates synced after viewport resize (#237)”, dated 2026-08-29. The commit explicitly declares presentation-only behavior with no battle-rule or outcome changes.

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
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No capability category is promoted in Pass 310.

`The Order Signed on Yesterday's Report` has a reduced version requiring no tactical battle capability. The full exposed-relay-span version depends on complete movement for wind/forced displacement/interception, lifecycle for timed structural events, stateful damage for environmental injury, status lifecycle for persistent effects, and terrain/weather/hazards/zones/reactions for unstable surfaces, debris and reactive rescue. Move, Ability, Item and Trainer Feature dependencies apply only when those elements are explicitly authored. Autonomous tactical rescue remains blocked on AI tactical policy, while reliable visible execution remains constrained by Minecraft/Cobblemon/Craftics adapter/playback support.

PTU/Caelo/Kairos authority remains unchanged. Public research in Pass 310 contributes narrative, investigation and decision-provenance structures only. No rule-profile overlay is activated.
