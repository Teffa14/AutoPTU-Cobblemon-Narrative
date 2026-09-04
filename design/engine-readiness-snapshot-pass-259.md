# Engine readiness snapshot — Pass 259

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU were inspected read-only.

AutoPTU-Java head: `fd31148e3f97b4d79f98a193f34392e35502b4c8`. PR #345 composes the move-special registry factory through runtime dependencies. The changed runtime files and tests strengthen that specific composition seam. They do not demonstrate the whole move-specific family or any other complete capability family.

AutoPTU Python oracle head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-coordinate synchronization and explicitly does not change rules or outcomes.

Permanent capability audit:

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

No category is promoted from one representative implementation, registry, hook or test.

Pass 259 reduced dependency: the provisional-state lifecycle is ecology-persistence bookkeeping and does not require AutoPTU. Production observation/projection still depends on adapter/playback.

A richer field-follow encounter adds targeting/LoS, base movement, action economy, lifecycle, legal-action infrastructure, tactical policy and adapter/playback. Complete movement is required when interception, blocking or forced movement occurs. Terrain/weather/reactions is required only when those mechanics affect approach or detection. Trainer Features/perks is required only when a trainer rule modifies evidence. Other families are dependencies only when explicitly invoked.

PTU/Caelo boundary: Pass 259 does not author PTU state. Repository search found PTU Survival/Perception and trainer-class material in the Python oracle. No file matching `Caelo` was found in the current narrative, Java or Python repositories, so this pass makes no Caelo-specific rule claim.