# Global NPC AI readiness snapshot — Pass 300

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before this pass: `e44b86315f6b12199574a108e431946971516177`.

Read-only engine evidence checked during this pass:

AutoPTU-Java `50c5f4c04fb3dcfb0abd468a72832aeb3edcd404` — PR #377 adds a pure ordinary-damage temporary-HP absorption resolver. Its own contract explicitly excludes HP mutation, injury processing, faint prevention, history recording and adapter-side evaluation. This is concrete evidence for one stage of the stateful damage ingress pipeline only and does not establish the complete damage pipeline.

AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` remains the pinned oracle head previously audited as presentation-only at its latest change.

Capability classification retained conservatively:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL; PR #377 strengthens one temporary-HP absorption seam but explicitly omits downstream state mutation and injury/faint handling;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

Pass 300's reduced communication-posture loop has no tactical dependency. The mechanically rich route-hazard variant inherits only the exact families it actually exercises. No engine family is promoted by the live evidence above.
