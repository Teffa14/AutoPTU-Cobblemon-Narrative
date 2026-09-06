# Global NPC AI readiness snapshot — Pass 295

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Narrative repo head before this pass: `3289dcd6d5787aa166b1f66f23f1d83ecc689985`.

Read-only engine evidence checked during this pass:

- AutoPTU-Java `e7ee429e1d56d0c6b7d9b8424f9895277fb9c498` — adds a server-owned runtime mutation boundary for canonical moveset removal. The service applies the existing canonical removal resolver to one known combatant, persists the resulting moveset into authoritative battle state, leaves adapters read-only and has regressions for isolation, no-op behavior, missing canonical ownership and unknown combatants. This is narrow evidence for authoritative move-state mutation and temporary borrowed-move cleanup. It does not prove move-specific behavior or full lifecycle complete.
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

Pass 295 deliberate deception, testimony divergence and subjective source attribution have no tactical dependency in their reduced form.

If a resulting investigation enters structured battle, chase or hazardous exploration, it inherits only the exact capability families used by that encounter. Interception/forced movement require complete movement; mechanical hazards/weather/zones/reactions require that family; temporary or delayed effects require their relevant lifecycle and owner-specific behavior; autonomous tactical choice requires AI tactical policy; in-world battle presentation requires the adapter/playback boundary.

No category is promoted because one representative hook, registry, cleanup resolver or mutation service exists.
