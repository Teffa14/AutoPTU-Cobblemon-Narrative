# Global NPC AI readiness snapshot — Pass 298

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Narrative repo head before this pass: `7c83242dca7f198f85500b381354487e5788f3e4`.

Read-only engine evidence checked during this pass:

AutoPTU-Java `889fab8ac857b50563648da935f5d7a2b8e31d68` — PR #376 wires Psionic Sponge borrowed-Move cleanup into the built-in TURN_END registry, removes the borrowed Moves from authoritative runtime state, clears matching temporary-effect entries and emits `BorrowMoveEndedEvent`. Tests cover actor isolation, stable ordering and no-op behavior. This is stronger evidence for that specific TURN_END temporary-Move seam, but it does not prove the full Move corpus, lifecycle, Trainer Features, status system or adapter playback complete.

AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — head remains presentation-only and explicitly states that battle rules and outcomes do not change.

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

Pass 298's reduced investigation/trust loop has no tactical dependency. Any structured confrontation inherits only the exact capability families it actually exercises. The new Psionic Sponge evidence is narrow and does not promote a family.
