# Engine readiness snapshot — Pass 260

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU were inspected read-only.

AutoPTU-Java head: `fd31148e3f97b4d79f98a193f34392e35502b4c8`. The current head remains PR #345, which composes the move-special registry factory through runtime dependencies. This strengthens that specific move-special composition seam. It does not demonstrate the whole move-specific family, status family, damage family or any other complete capability family.

AutoPTU Python oracle head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-coordinate synchronization after viewport resize and explicitly does not change rules or battle outcomes.

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

No category is promoted from a representative implementation, registry, hook or test.

Pass 260 reduced dependency: provisional retention/expiry/restart bookkeeping does not require AutoPTU. Production observation and correct source projection still depend on Minecraft/Cobblemon/Craftics adapter/playback.

Pass 260 explicitly rejects Minecraft-only damage presentation as a source of persistent PTU injury. A future authoritative injury-retention path depends on a verified semantic return from the full stateful damage pipeline plus every lifecycle/status/move/Ability/Item/Trainer Feature family used by that encounter. The retention layer may preserve an authoritative result but cannot manufacture one.

A richer field-follow encounter adds targeting/LoS, base movement, action economy/initiative, full turn/round lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement is required when interception, blocking, push/pull/knockback or forced movement occurs. Terrain/weather/hazards/zones/reactions is required only when those mechanics alter approach, observation or the encounter. Other permanent families are dependencies only when explicitly invoked.

PTU/Kairos/Caelo boundary: `sources/kairos/KAIROS_SOURCE_INDEX.md` is present and remains a routing/reference layer, not automatic Ouros authority. The current Narrative source tree contains Kairos but no local Caelo source pack, so Pass 260 makes no Caelo-specific mechanical claim. PTU mechanical state continues to require the project-selected authoritative rules path rather than Minecraft inference.