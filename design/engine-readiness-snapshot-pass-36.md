# Engine Readiness Snapshot — Pass 36

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `781e61ff7413764cd507fa970e162c12f08aae65`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

The newest Java slice adds an ordered authoritative status-application hook registry. Status application now passes through that boundary, and a concrete Inner Focus hook prevents Flinch. Python-oracle fixtures and parity tests cover this bounded behavior.

This strengthens evidence for status lifecycle and abilities. It does not establish complete coverage for either family.

No-inference rules:
- Inner Focus preventing Flinch does not prove every status-prevention Ability.
- A generic application registry does not prove all statuses, Save Checks, expiries or interactions.
- One Ability hook does not prove the complete Ability registry.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

The verified movement slice excludes interception and forced movement. Verified calculations remain primitives rather than a complete damage pipeline. Legal AI choices do not imply tactical quality.

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

Lifecycle evidence includes authoritative actor/phase state, START/COMMAND/ACTION/END transitions, round cleanup/history rotation, delayed-hit infrastructure, status-phase hooks and pending skips.

Status evidence includes the ordered phase registry, Flinch behavior/expiry, Strange Tempo + Confusion coverage, status metadata, the new application registry and Inner Focus prevention. The Java README still describes the status controller and broader battle state as incomplete.

Selected move, Ability and held-item slices have parity evidence, but none establishes complete family coverage.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

The Java README still lists forced movement, reactions, terrain/hazards, complete registries, tactical AI and Minecraft integration as future work.

## Pass 36 encounter dependencies

### Gallery Lockdown

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING if tactical evacuation/chokepoints are used
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic fixture/smoke/collapse effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — BLOCKING
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version: evacuation and fragile-object handling remain in world state; AutoPTU receives a stable cleared arena.

### Archive Water Intrusion

FULL version needs dynamic terrain/hazards, changing passability, objective handling and objective-aware AI, so it remains BLOCKING.

REDUCED version keeps water, pumps and holdings outside the tactical grid and uses a static legal encounter.

### Traveling Exhibit Intercept

FULL version needs protect/breakthrough objectives, interception and tactical policy, so it remains BLOCKING.

REDUCED version stops the vehicle, keeps staff/crates outside the grid, runs a static encounter, then updates custody/transport state from the authoritative result.

## Collection-state non-inference

Narrative collection metadata cannot grant mechanics.

Do not infer artifact bonuses from age or historical importance, automatic Skill success from catalog knowledge, mechanical repair from conservation treatment, Trainer progression from archive access, or supernatural effects from museum classification.

If a collection object is also a PTU item, its battle behavior comes from its authoritative mechanical identity and rules implementation.

## Conclusion

Pass 36 can safely advance catalog records, archival holdings, exhibit lifecycle, custody/loan history, access policy, conservation history and public interpretation as narrative/world state.

Rich tactical museum/archive scenarios should use reduced forms until forced movement/interception, dynamic hazards/zones, objective-aware AI and Minecraft playback are implemented and parity-validated.