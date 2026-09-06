# Global NPC AI readiness snapshot — Pass 301

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 301: `85a5205f58f900112668e69a30c8ead8ae06d4c1`.

Read-only engine evidence checked during this pass:

AutoPTU-Java `50c5f4c04fb3dcfb0abd468a72832aeb3edcd404` remains the live head. PR #377 adds ordinary-damage temporary-HP absorption as a pure contract and explicitly leaves HP mutation, injury processing, faint prevention, history recording and adapter evaluation outside that seam. This strengthens one stateful-damage stage only.

AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` remains unchanged. Its current head is presentation-only and states that battle rules/outcomes are unaffected.

Capability classification remains conservative:

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

Pass 301’s reduced disclosure-expectation and missing-warning investigation loop has no tactical dependency. Its full storm-ravine rescue variant requires only the exact families enabled by the authored encounter: range/LoS and base movement for basic structured rescue; complete movement for forced displacement/interception; lifecycle for delayed phases; damage/status for mechanical injury or conditions; terrain/weather/hazards/zones/reactions for the intended ravine hazard; owner families for any Move/Ability/Item/Trainer Feature; tactical policy for autonomous rescue choices; and adapter/playback for visible authoritative projection.

No category is promoted by Pass 301. No narrative contract assumes a representative Java seam proves its entire capability family.