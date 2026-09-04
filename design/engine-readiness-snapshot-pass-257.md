# Engine readiness snapshot — Pass 257

Date: 2026-09-04

Narrative concept: separate repeated use/detection of a micro-site from individual Pokémon identity and population truth.

Live read-only evidence inspected:
- AutoPTU-Java main: `faf25d7473920f4bd2e03520553f5db5da20abd8`, merge PR #344, composing effective-move, damage-modifier, pre-damage-reaction and post-damage hook registries through `BattleRuntimeDependencies`. This is concrete composition evidence for those seams; it does not prove complete family parity.
- AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only coordinate synchronization after viewport resize. No new rules evidence.

Permanent capability classification remains conservative:

- targeting/footprints/range/LoS — VERIFIED within audited contracts.
- base movement legality — VERIFIED within audited contracts.
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
- core calculations — VERIFIED within audited contracts.
- action economy/initiative — VERIFIED within audited contracts.
- full turn/round lifecycle — PARTIAL.
- full stateful damage pipeline — PARTIAL.
- status lifecycle — PARTIAL.
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING depending on exact mechanic.
- move-specific behavior — PARTIAL.
- abilities — PARTIAL.
- items — PARTIAL.
- Trainer Features/perks — PARTIAL.
- AI legal-action infrastructure — VERIFIED within audited contracts.
- AI tactical policy — BLOCKING for autonomous rich behavior.
- Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING end-to-end.

Reduced Pass 257 scene needs no AutoPTU battle handoff. It depends on Ouros persistence/observation state and Minecraft/Cobblemon/Craftics adapter/playback so that already-counted sources can be presented without creating ecological truth from native entities.

A rich scene where two wild actors physically contest or approach the same site requires targeting/LoS, base movement, action economy, full lifecycle, AI legal-action infrastructure, AI tactical policy, and adapter/playback. Complete movement is required if interception/blocking/forced displacement appears. Terrain/weather/hazards/zones/reactions is required if the site or weather changes legality or triggers responses. Damage/status/Moves/Abilities/Items/Trainer Features are dependencies only if the authored encounter actually invokes those families.

No capability promotion is justified by Pass 257. Site-use identity is an ecology/knowledge contract, not evidence for battle-engine completeness.
