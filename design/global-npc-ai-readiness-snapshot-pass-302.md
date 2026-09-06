# Global NPC AI readiness snapshot — Pass 302

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 302: `b612c613dda96d68449067ea53db9ad64c70e388`.

Read-only engine evidence checked during this pass:

AutoPTU-Java advanced to `c06eee09a22c9c3459f23a320a1fbdbe99059119` via PR #378, `Freeze temporary-HP absorption against Python oracle`. The change adds a parity workflow and frozen Python-oracle comparison for the already narrow ordinary-damage temporary-HP absorption seam introduced by PR #377. It strengthens confidence in that exact seam. It does not add downstream HP mutation, Injury handling, faint prevention, battle history, general damage ordering or adapter evaluation.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its live head is still presentation-only and explicitly states that battle rules and outcomes are unchanged. Java PR #378 uses a separately pinned Python oracle commit for its parity fixture; that does not change the current narrative-task read-only AutoPTU head.

Capability classification remains conservative:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL; PR #378 freezes one temporary-HP absorption seam against an oracle but does not complete the pipeline;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

Pass 302 itself is world-simulation only. Distinguishing `NO_KNOWN_CHANNEL`, queued attempts, local-ack waits, failed delivery and proven usable access has no tactical dependency.

The proposed full relay-site rescue depends on only the exact authored families: targeting/base movement for structured positioning; complete movement for forced displacement/interception; lifecycle for timed phases; stateful damage for mechanical environmental damage; status lifecycle for persistent conditions; terrain/weather/hazards/zones/reactions for a mechanically active storm/relay site; owner families for any Move/Ability/Item/Trainer Feature; AI tactical policy for autonomous rescue choices; and adapter/playback for authoritative visible projection.

No capability category is promoted by Pass 302 or by the single Java parity seam.
