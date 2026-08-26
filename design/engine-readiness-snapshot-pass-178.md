# Engine Readiness Snapshot — Pass 178

Status: evidence snapshot for narrative dependency classification.
Date: 2026-08-26
Pass: 178

Authority correction: Pass 64 `wildfire-fire-ecology-landscape-recovery-layer.md` remains the fire-ecology authority. Pass 178 only adds monitoring/treatment-review/reburn-comparability protocol material.

AutoPTU-Java and AutoPTU were inspected read-only.

## Live evidence

AutoPTU-Java head inspected: `a9fb0d81238e69a5263f074b4a8ad8ef1905325d`.

Recent evidence includes canonical seven-Combat-Stage state, authoritative mutation/hooks for Accuracy and Evasion, secondary Combat Stage application, Mirror Armor coverage and earlier live secondary-Status execution. These are specific contracts, not proof that full Status, Ability or Move families are complete.

AutoPTU Python head inspected: `44305a1b3f06a45fbd06392a64573f287ac31555`.

Its newest inspected change is Career sponsor-memory normalization and explicitly preserves battle behavior.

The Java README still marks core combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, registries, transcript parity, AI scoring/policy and Craftics/Cobblemon integration as incomplete.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions as a complete family
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted in Pass 178.

## Encounter dependencies

### Monitoring Plot Retrieval — FULL

- targeting/footprints/range/LoS: VERIFIED for battle targeting only
- base movement legality: VERIFIED
- complete movement: BLOCKING if technicians cross/withdraw or interception matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when invoked
- terrain/weather/hazards/zones/reactions: BLOCKING if unstable post-fire ground, smoke, debris or protected tactical zones matter
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`
- adapter/playback: BLOCKING

REDUCED version: monitoring equipment, technicians and fire-history state remain outside battle authority; AutoPTU receives only a stable conventional arena if an independent confrontation remains.

### Treatment Review Field Day — FULL

Same permanent map. Complete movement/tactical AI are needed only if researchers remain tactical actors. Environmental fire mechanics are not assumed.

REDUCED version: field sampling and treatment review occur in world state before/after a static battle.

### Reburn Transect Survey — FULL

Same permanent map. Environment enters only if present-day terrain has exact validated tactical consequences.

REDUCED version: transect observations and overlap interpretation remain outside AutoPTU; any battle occurs on stable adjacent ground.

### Regime Evidence Review

No battle-engine dependency.

## Critical boundary

Neither Pass 64 nor Pass 178 authorizes a generic tactical wildfire simulator.

Do not synthesize:
- spreading fire tiles
- smoke penalties
- ambient Burned
- heat damage
- delayed ignition
- wind-driven fire phases
- ash hazards
- falling burned trees
- wildfire pathfinding
- responder/civilian AI
- charred-ground terrain

from narrative state alone.

If a future engine slice validates one representative rule, only that exact rule becomes locally available.

## Minecraft boundary

Minecraft may render charred terrain, regrowth, monitoring plots, treatment boundaries, closures and signage. It must not derive authoritative burn severity, treatment success, fire-regime revision, recovery state or reburn causality from block fire spread, block counts, chunk load, particles, entity despawn or biome color.

The direction remains world state -> adapter presentation.

## PTU/Caelo unresolved

No validated evidence in this run establishes generic environmental wildfire rules, Water-Move suppression volume, Fire-type ecological immunity, smoke Status, or charred-ground Terrain.

The complete Caelo corpus was not reliably available. Super PTU Online Helper was not exposed as an invocable capability. No output from either source was invented.
