# Engine readiness snapshot — Pass 263

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU inspected read-only.

AutoPTU-Java head remains `136c8d9a7d124849954748c780b12a0e1faf28e0`, merge of PR #347, `Route AoE move specials through runtime composition`.

The live evidence inspected in Pass 263 continues to show internal action-result/event flow and dependency-composed runtime hooks. PR #347 routes AoE move-special registry creation through `BattleRuntimeDependencies`. This is concrete evidence for that composition seam. It does not establish a stable public AutoPTU→Ouros semantic-result API, a stable Ouros battle subject binding, complete move-specific behavior, complete AoE semantics, full damage, status lifecycle or tactical policy.

AutoPTU Python oracle remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. No new rule evidence was identified in this pass.

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

No category is promoted in Pass 263.

## Pass 263 admission implications

A correct stable subject binding is necessary but not sufficient to import durable battle aftermath.

An integration-only `BATTLE_HANDOFF_CORRELATION_RECEIPT` can be represented without claiming HP, Injury, status, population or tactical truth. The Pass 263 fixture tests this envelope/binding behavior only and explicitly does not claim live production transport.

Persistent HP/Injury consequences remain blocked from production admission because full turn/round lifecycle and the full stateful damage pipeline remain PARTIAL. Any move-specific behavior, Ability, Item, Trainer Feature, terrain/reaction, targeting or movement mechanic materially involved in the producing path is an additional exact dependency.

Persistent status remains quarantined because status lifecycle remains PARTIAL.

A simple voluntary relocation can eventually use a narrow base-movement admission because base movement is VERIFIED; forced/disputed movement cannot inherit that admission while complete movement remains PARTIAL.

Legal-action provenance can use the VERIFIED AI legal-action infrastructure for exact audited paths, but it cannot be promoted into tactical-intent or tactical-quality provenance because AI tactical policy remains BLOCKING.

## Encounter versions

Reduced battle-aftermath loop: stable Ouros subject + opaque battle-session correlation + integration receipt + playback. Durable HP/Injury/status aftermath remains absent. Primary blocker is Minecraft/Cobblemon/Craftics adapter/playback transport and the lack of a live Java semantic-result export API.

Full version: add exact admitted result paths. Injury requires lifecycle + stateful damage; persistent status adds status lifecycle; forced movement adds complete movement; weather/hazard/reaction consequences add their mixed/blocking family; move/Ability/Item/Trainer Feature results add those respective partial families; autonomous tactical causation adds AI tactical policy.

## PTU/Caelo/Kairos boundary

PTU remains the selected mechanical baseline under project policy. Kairos remains a living-world/routing reference rather than automatic mechanical authority. The inspected Narrative evidence still does not expose a local Caelo source pack, so no Caelo-specific rule is inferred.

## Unresolved blockers

- Define and implement a stable public Java semantic-result export surface rather than inferring state from internal runtime events.
- Implement the private Ouros battle-subject binding ledger and handoff token lifecycle in production code.
- Define real AutoPTU↔Ouros/Craftics transport/authentication.
- Pin Minecraft/Cobblemon/Craftics production versions.
- Create exact admission records tying each result type and producer revision to concrete Java tests/contracts.
- Decide operator/recovery policy for quarantined results and battle finalization with unresolved receipts.
