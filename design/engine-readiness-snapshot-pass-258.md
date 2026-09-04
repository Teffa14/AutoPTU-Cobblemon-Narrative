# Engine readiness snapshot — Pass 258

Evidence checked live on 2026-09-04. AutoPTU-Java and AutoPTU are read-only inputs to this narrative task.

## Live heads

AutoPTU-Java: `faf25d7473920f4bd2e03520553f5db5da20abd8` — merge of PR #344, composing move/damage hook registries through current runtime dependencies. This is concrete composition evidence for those seams. It does not prove complete move-specific behavior, damage, reactions, statuses, movement or battle lifecycle as capability families.

AutoPTU Python oracle: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — latest change remains viewport/presentation coordinate synchronization and explicitly does not change battle rules or outcomes.

## Permanent capability audit

- targeting / footprints / range / LoS: VERIFIED within audited contracts.
- base movement legality: VERIFIED within audited contracts.
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
- core calculations: VERIFIED within audited contracts.
- action economy / initiative: VERIFIED within audited contracts.
- full turn / round lifecycle: PARTIAL.
- full stateful damage pipeline: PARTIAL.
- status lifecycle: PARTIAL.
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING.
- move-specific behavior: PARTIAL.
- abilities: PARTIAL.
- items: PARTIAL.
- Trainer Features / perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED within audited contracts.
- AI tactical policy: BLOCKING.
- Minecraft / Cobblemon / Craftics adapter and playback: PARTIAL / BLOCKING end-to-end.

No category is promoted in Pass 258 merely because a representative hook or integration test exists.

## Pass 258 dependency classification

The reduced counted-source resolution transaction is ecology-ledger work and requires no tactical AutoPTU capability family. Its production blocker is adapter/playback evidence for a stable, authoritative source-lineage signal that can distinguish an already-counted anonymous source across the relevant materialization lifecycle.

A richer pursuit scene requires targeting/LoS, base movement, action economy/initiative, full lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement is additionally required when interception, blocking or forced movement is authored. Terrain/weather/hazards/zones/reactions, damage, status, Moves, Abilities, Items and Trainer Features/perks remain exact dependencies only if the scene invokes them.

## Unresolved evidence questions

The narrative repository now defines what an atomic unresolved-to-persistent source conversion must preserve, but current evidence does not yet verify the production adapter token/lineage mechanism that should authorize it. The threshold for when durable individual ecology history forces internal resolution also remains a design/canon question rather than an engine fact.
