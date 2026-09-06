# Global NPC AI readiness snapshot — pass 308

Status: DESIGN EVIDENCE / NOT CANON
Date: 2026-09-06

Pass 308 adds custody-assessment lineage to the world simulation. The lineage subsystem itself does not require AutoPTU combat. Tactical dependencies arise only if the authored evidence-recovery scene activates them.

Read-only engine evidence checked during this pass:

AutoPTU-Java main: `3ca3540a94bafdb57ff69d2feaa56ec0b3d65d3b`, commit “Add reusable post-damage faint transition contract (#381)”, dated 2026-09-06. The current seam exposes a server-owned post-damage faint transition and is parity-gated against the Python oracle. It strengthens one part of the stateful damage path; it does not establish complete Substitute handling, prevention/reactions, Injuries, faint prevention, history rotation, semantic events, source attribution, all move behavior or end-to-end playback.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, commit “Career: keep battle coordinates synced after viewport resize (#237)”, dated 2026-08-29. The commit explicitly states that it is presentation-only and changes no battle rules or outcomes.

Capability classification retained from live audited evidence:

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

No category is promoted by Pass 308. One verified representative seam remains evidence only for that seam.

For `The Report That Corrected Itself`, the reduced world-simulation version needs no tactical capability. The reduced tactical fallback can use static blocked nodes plus verified base movement and only individually verified actions. The full damaged-annex version depends on complete movement for forced movement/interception/rescue displacement, lifecycle for delayed collapses, stateful damage for real hazard injury, status lifecycle for persistent conditions, terrain/weather/hazards/zones/reactions for dynamic structural danger, and exact Move/Ability/Item/Trainer Feature families when authored. Autonomous tactical rescue additionally remains blocked on AI tactical policy, and visible end-to-end execution remains constrained by adapter/playback support.

PTU/Caelo mechanical authority remains unchanged. Public research in Pass 308 supplies narrative and information-management patterns only and cannot define Skill checks, Features, Pokémon senses, item behavior, hazard math or combat legality.
