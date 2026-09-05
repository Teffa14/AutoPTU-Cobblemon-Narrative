# Global NPC AI readiness snapshot — Pass 293

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Narrative repo head before this pass: `a6d71063e513e5cef1da5fabe82ba7ae71361ffc`.

Read-only engine evidence checked during this pass:

- AutoPTU-Java `ae196d63011617d67cecde442124645da6400026` — Adaptive Geography is wired through selective TURN_END cleanup. This is narrow evidence for declarative temporary-effect/lifecycle infrastructure and one Trainer Feature seam. It does not prove lifecycle, Trainer Features, terrain or status families complete.
- AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — head remains presentation-only and explicitly does not change battle rules/outcomes.

Capability classification retained conservatively:

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

Pass 293 memory retrieval has no tactical dependency in its reduced form. Any structured scene caused by recalled or forgotten information inherits only the exact capability families it uses.

No category is promoted because of one representative hook or mechanic.
