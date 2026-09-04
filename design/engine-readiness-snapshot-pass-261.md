# Engine readiness snapshot — Pass 261

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU inspected read-only.

AutoPTU-Java head: `fd31148e3f97b4d79f98a193f34392e35502b4c8`, merge of PR #345, `Compose move-special registry factory`.

The live commit history shows the move-special registry factory and direct move-special routing being composed through runtime dependencies. This strengthens that specific move-special composition seam. It does not prove complete move-specific behavior, status lifecycle, damage, reactions, Abilities, Items, Trainer Features or tactical policy.

AutoPTU Python oracle head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains viewport/presentation coordinate synchronization and explicitly does not alter battle rules or outcomes.

## Permanent capability audit

- targeting/footprints/range/LoS: VERIFIED within audited contracts.
- base movement legality: VERIFIED within audited contracts.
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
- core calculations: VERIFIED within audited contracts.
- action economy/initiative: VERIFIED within audited contracts.
- full turn/round lifecycle: PARTIAL.
- full stateful damage pipeline: PARTIAL.
- status lifecycle: PARTIAL.
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING.
- move-specific behavior: PARTIAL.
- abilities: PARTIAL.
- items: PARTIAL.
- Trainer Features/perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED within audited contracts.
- AI tactical policy: BLOCKING.
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

No capability family is promoted because one registry, hook, representative move or test exists.

## Pass 261 dependency boundary

The reduced semantic-horizon registry and clock fixture requires no tactical AutoPTU capability family. It performs retention bookkeeping only.

Production implementation depends on Minecraft/Cobblemon/Craftics adapter/playback to provide a verified restart-safe clock source and to correlate projection lifecycle events correctly.

Pass 261 does not assert that the currently surveyed Yarn 1.21 names are the production Ouros API. The exact Minecraft/loader/Cobblemon pin remains unresolved.

A richer field-follow scene requires targeting/LoS, base movement, action economy/initiative, full turn/round lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement is additionally required for interception, blocking, push/pull/knockback or forced movement.

Terrain/weather/hazards/zones/reactions becomes a dependency when environmental mechanics actually alter observation, movement, recovery or encounter state.

A future persistent injury or status horizon can consume only an authoritative semantic result. It depends on the full stateful damage pipeline and every additional lifecycle/status/move/Ability/Item/Trainer Feature family actually used to produce that result. The clock layer cannot manufacture or repair missing PTU authority.

## PTU/Caelo/Kairos boundary

PTU remains the mechanical baseline selected by project policy. Survival is relevant to wilderness scouting and tracking, but it does not define the internal Ouros retention clock.

Kairos remains a living-world/routing reference and does not automatically activate its rules in Ouros.

The Narrative source tree still has no local Caelo source pack identified during this pass, so no Caelo-specific mechanical claim is promoted.

## Pass 261 unresolved blockers

- Pin the exact Minecraft/Cobblemon/Craftics production versions and verify the persisted world-time primitive against them.
- Decide whether ecological progression pauses when the server is offline or uses an additional calendar-time domain.
- Define species/context-specific semantic-horizon policy records instead of fixture durations.
- Define clock-epoch migration/rollback persistence in the actual world-state store.
- Define the typed AutoPTU semantic-result envelope before battle-authored persistent consequences can enter this registry.
