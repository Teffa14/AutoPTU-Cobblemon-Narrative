# Engine readiness snapshot — pass 185

Status: DESIGN EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-01

This file records only the live evidence inspected for this narrative pass. AutoPTU-Java and AutoPTU remain read-only. A representative mechanic never promotes an entire capability family.

## Live heads inspected

AutoPTU-Java: `1acb773545966affce865ec3f250ff02faccae57`

Latest commit: `Route forced movement through shared runtime dependencies (#317)`. It introduces an immutable `BattleRuntimeDependencies` composition snapshot and routes forced-movement resolution through canonical combatant rule content. Tests cover target rule content, source/target ownership separation, empty dependencies, and compatibility with the previous registry boundary.

This is meaningful architectural progress for forced-movement rule composition. It does not demonstrate every Push, Pull, Knockback, Interception, collision, partial-stop, footprint, reaction, ordering, terrain, or content interaction.

AutoPTU: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains Career/presentation-only: viewport resize synchronization for tactical sprite destinations. Its commit message explicitly states that battle rules and outcomes do not change. No capability family is promoted from this evidence.

## Permanent capability classification

### VERIFIED for the audited contracts currently evidenced

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` here means the repository contains tested contracts sufficient for the bounded uses previously audited. It does not mean every move/content combination in the family has parity.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

The latest Java slice strengthens complete-movement composition only in the forced-movement prevention seam. Complete movement remains PARTIAL.

### BLOCKING when a concept requires the complete family

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

The RPG/world adapter may already support useful non-tactical physical objects and persistence surfaces in other evidence snapshots. That does not establish full tactical adapter/playback parity.

## Pass-185 concept audit

### Non-combat provisioning seeds

`One Coil Short`, `Mirador Field Kit Checkout`, `Restock Arrived, Inspection Pending`, `Brin's Reserve Shelf`, `Field School Packing Block`, and other ordinary stock/custody loops require no BattleSpec if implemented as authoritative world-state interactions.

Their main implementation dependencies are narrative/world persistence, object projection, custody/provenance, institutional authority, communications, and UI. They must not fabricate PTU Item effects.

### Last Crate at Upper Bend — full intended version

Dependencies:

- targeting/footprints/range/LoS — VERIFIED for audited contracts, REQUIRED
- base movement legality — VERIFIED for audited contracts, REQUIRED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL, REQUIRED if tactical carrier protection/displacement/interception/collision/partial-stop behavior is used
- core calculations — VERIFIED for audited contracts, REQUIRED
- action economy/initiative — VERIFIED for audited contracts, REQUIRED
- full turn/round lifecycle — PARTIAL, REQUIRED
- full stateful damage pipeline — PARTIAL, REQUIRED
- status lifecycle — PARTIAL, REQUIRED when selected content can apply statuses
- terrain/weather/hazards/zones/reactions — BLOCKING as a complete family, REQUIRED if route conditions affect battle state
- move-specific behavior — PARTIAL, REQUIRED and roster-audited
- abilities — PARTIAL, REQUIRED and roster-audited
- items — PARTIAL, REQUIRED only when selected tactical Items are used; logistical cargo remains outside BattleSpec
- Trainer Features/perks — PARTIAL, REQUIRED when selected Trainers use them
- AI legal-action infrastructure — VERIFIED for audited contracts, REQUIRED
- AI tactical policy — BLOCKING, REQUIRED when actors must reason about escort/protection/withdrawal goals
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING as a complete family, REQUIRED for faithful in-world tactical execution

Full-version readiness: BLOCKED.

### Reduced version

The crate, carrier, workers, allocation, delivery, inspection, and route logistics stay outside BattleSpec. Any battle occurs separately on stable terrain with an audited roster and without unsupported dynamic hazards, escort units, cargo objectives, weather phases, or non-audited forced-movement interactions.

This form can advance as soon as the exact selected battle roster is proven against the existing VERIFIED/PARTIAL contracts. No family-wide assumption is permitted.

Allowed tactical handoffs remain narrow: `IMMEDIATE_PATH_CLEAR` or `IMMEDIATE_WILD_THREAT_WITHDREW`.

## PTU item boundary for provisioning

The provisioning layer must treat exact PTU mechanical Items conservatively because the Items capability family remains PARTIAL in Java. A mundane crate, ingredient, spare part, notebook, rope, container, lamp component, or field kit does not gain PTU effects through naming similarity.

When a proposed kit eventually includes a real PTU Item, implementation must identify the canonical PTU source/content entry and the Java contract for that exact item before relying on its mechanics.

Narrative may track custody or reservation of a PTU Item as a world fact, but battle effect execution remains AutoPTU authority.

## Caelo evidence

Literal GitHub code search for `Caelo` across Narrative, AutoPTU-Java and AutoPTU returned no result in this pass. No logistics, commerce, crafting, supply, reserve, expedition, or item-access doctrine is inferred from that absence.

## Unresolved mechanical questions

The current pass leaves open whether any exact PTU mechanics should govern carrying capacity for field kits, whether mundane consumables need item-level simulation, which PTU Items are appropriate for ordinary Marea work, whether equipment damage has an existing oracle contract, and how world-owned item custody will map into the eventual Minecraft/Cobblemon/Craftics adapter without duplicating battle inventory authority.

These questions do not block the non-combat provisioning layer. They block only designs that try to give those objects mechanical PTU effects or move them into BattleSpec.