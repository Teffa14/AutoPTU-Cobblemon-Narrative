# Global NPC AI readiness snapshot — Pass 299

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before this pass: `c29a953823689ea7585bd425597af2a7a650b279`.

Read-only engine evidence checked during this pass:

AutoPTU-Java `889fab8ac857b50563648da935f5d7a2b8e31d68` — PR #376 wires Psionic Sponge borrowed-Move cleanup into the built-in TURN_END registry, removes borrowed Moves from authoritative runtime state, clears matching temporary-effect entries and emits the typed end event. This remains concrete evidence for that specific temporary-Move / TURN_END seam only. It does not prove the complete Move corpus, turn/round lifecycle, Trainer Feature family, status system or adapter playback.

AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — latest head remains explicitly presentation-only and states that battle rules and outcomes do not change.

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

Pass 299's reduced borrowed-authority investigation loop has no tactical dependency. A mechanically rich version inherits only the exact capability families it exercises. No engine family is promoted by the live evidence above.
