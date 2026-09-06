# Global NPC AI readiness snapshot — Pass 296

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Narrative repo head before this pass: `1f29a1b30fe4cfe5f063b0f9b58c4045cdc9bbb5`.

Read-only engine evidence checked during this pass:

- AutoPTU-Java `ac1b6587e4d7046ffd8396493efbcf51a0358702` — PR #374 expands immutable structured `TrainerFeatureEvent` details to support ordered scalar lists, with tests for copied immutable payloads, stable keys, rejection of nested unsupported values and compatibility with existing scalar details. This is narrow event-payload infrastructure useful for a Trainer Feature such as borrowed-move expiry. It does not prove the Trainer Features corpus, move-specific behavior or lifecycle complete.
- AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — head remains presentation-only and explicitly states that battle rules and outcomes do not change.

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

Pass 296 selective deceptive communication has no tactical dependency in its reduced form. It uses world-agent memory, audience selection, semantic communication transport and subjective attribution only.

If the resulting consequence enters structured battle or hazardous exploration, it inherits only the capability families actually exercised. Interception and forced movement require complete movement. Mechanical weather/hazards/zones/reactions require that family. Temporary or delayed effects require their lifecycle and exact Move/Ability/Item/Trainer Feature owner. Autonomous tactical choice requires AI tactical policy. In-world structured playback requires the Minecraft/Cobblemon/Craftics adapter boundary.

No category is promoted because one representative event payload, hook, registry, cleanup resolver or mutation service exists.
