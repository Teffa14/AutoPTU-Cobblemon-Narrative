# Engine readiness snapshot — Pass 262

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU inspected read-only.

AutoPTU-Java head: `136c8d9a7d124849954748c780b12a0e1faf28e0`, merge of PR #347, `Route AoE move specials through runtime composition`.

The live commit changes `BattleRuntime.applyAuthoritativeAreaMoveTarget` so area-resolved move execution obtains `MoveSpecialHookRegistry` from `dependencies.moveSpecialHookRegistryFactory()` rather than constructing the standard registry directly. This is concrete evidence that AoE move-special routing now uses the same runtime composition seam. It strengthens move-special dependency composition for this path. It does not demonstrate complete move-specific behavior, complete AoE targeting semantics, complete status lifecycle, the full stateful damage pipeline, terrain/reaction completeness, Abilities, Items, Trainer Features or tactical policy.

AutoPTU Python oracle head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains viewport/presentation coordinate synchronization and explicitly does not alter battle rules or outcomes.

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

No family is promoted by PR #347 because the evidence is a specific runtime-composition seam for area move specials.

## Pass 262 dependency boundary

The reduced semantic-result ingress fixture does not run AutoPTU mechanics. Its accepted Injury-shaped result is deliberately marked `FIXTURE_PREVALIDATED_ONLY`, `production_admission_claimed = false`, and creates no canon Injury. This proves envelope/replay/authority behavior only.

Production result transport, subject binding and visible aftermath depend on Minecraft/Cobblemon/Craftics adapter/playback support.

A real persistent Injury result requires full turn/round lifecycle and the full stateful damage pipeline to be verified for the exact producing path. Any move-specific, status, Ability, item, Trainer Feature, terrain/reaction, movement or targeting family exercised by that path is also a dependency.

A persistent status result additionally requires status lifecycle. Pass 262 explicitly quarantines the fixture status result while status lifecycle remains PARTIAL.

AI tactical policy becomes a dependency only when autonomous policy selected actions that participate in the encounter path. It remains BLOCKING.

## PTU/Caelo/Kairos boundary

PTU remains the mechanical baseline selected by project policy. Public PTU material reviewed in Pass 262 confirms that Injury has its own mechanical and recovery semantics, supporting the existing authority boundary; exact rule adjudication still comes from the project-local PTU oracle.

Kairos remains a living-world/routing reference rather than automatic mechanical authority.

The inspected Narrative tree still does not expose a local Caelo source pack. No Caelo-specific rule is inferred from that absence.

## Pass 262 unresolved blockers

- Define the concrete AutoPTU-to-Ouros transport/authentication mechanism; no cryptographic signing is currently claimed.
- Define stable subject binding shared by the battle handoff and ecological lineage ledger.
- Identify which semantic result records AutoPTU-Java can already emit directly and which require a new result API.
- Build a per-result capability-admission matrix tied to exact tests/contracts, not broad family names.
- Decide persistence and operational handling for ingress receipts and quarantined results.
- Pin the Minecraft/Cobblemon/Craftics production versions and verify adapter transport/playback behavior against them.
