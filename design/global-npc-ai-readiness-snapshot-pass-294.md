# Global NPC AI readiness snapshot — Pass 294

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Narrative repo head before this pass: `2ce7bb4c31bbb75918e962bead539ca529138f6a`.

Read-only engine evidence checked during this pass:

- AutoPTU-Java `f3bd5bbb1a37eef0dc985d9cb8d9bdd74d352c0f` — adds a canonical moveset removal resolver with normalized identity matching and tests. The commit cites temporary borrowed-move cleanup such as Psionic Sponge as an intended consumer. This is narrow infrastructure evidence for move/lifecycle cleanup; it does not prove move-specific behavior or full lifecycle complete.
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

Pass 294 cue-assisted recall and archive lookup have no tactical dependency in their reduced form. Any structured scene caused by recovered information inherits only the exact capability families it uses.

No category is promoted because of one representative hook, cleanup utility or mechanic.
