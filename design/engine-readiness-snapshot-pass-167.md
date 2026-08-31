# Engine Readiness Snapshot — Pass 167

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-08-31
Narrative head before pass: `de62dd3a34ed6d00677f65b501f6a54dd4a82f05`

## Read-only engine heads inspected

AutoPTU-Java:

`4d5d04d95e048e7f27a77dd5cf30a7c12886456e` — merged PR #307, `Block forced movement through defender ability registry`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

Neither engine repository was modified by Pass 167.

## New Java evidence since Pass 166

PR #307 extends the now-bound post-hit forced-movement path with defender-side Ability prevention.

The inspected commit adds a declarative `ForcedMovementPreventionResolution` registry. The current rules include Suction Cups and Sumo Stance blocking PUSH. The resolver receives the already-resolved forced-movement instruction, defender Ability registrations and the Ability-suppression state. When a matching unsuppressed defender Ability blocks that instruction kind, displacement is prevented before the shared displacement engine mutates position.

The change also adds Python-oracle fixture export/parity coverage, CI gating and post-hit seam tests. This is materially stronger than a free-standing representative rule because it participates in the production post-hit path introduced and bound in PRs #305–306.

The evidence improves two permanent families at once: complete movement and Abilities. It still does not prove either family globally.

## Why no category is promoted

Complete movement remains PARTIAL because inspected evidence still does not establish every Push and Pull source, general Knockback, every Intercept ordering interaction, arbitrary forced movement from statuses/terrain/weather/items/features, escort/rescue, protected-object carrying, crowd routing, moving vehicles/platforms or generalized reaction windows.

Abilities remain PARTIAL because a small defender-side forced-movement prevention registry and previously inspected forced-movement modifiers do not establish complete Ability coverage across damage, status, targeting, lifecycle, terrain, reactions and every other rule family.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted in Pass 167.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly describes viewport-coordinate synchronization as presentation-only and states that battle rules and outcomes do not change. It provides no new mechanical readiness evidence for this pass.

## Estate continuity and PTU/Caelo

Repository and engine searches did not establish a universal inheritance, probate, estate, executor, beneficiary or heir mechanic.

Accordingly, private succession remains authored world logic with provenance. No Skill Check, Trainer Class, Feature, Level, Badge, Loyalty value, Pokémon bond, Battle victory or inventory state can establish inheritance unless an exact approved PTU/Caelo rule and authoritative project contract later say so.

Any inherited object that becomes a mechanical PTU Item in battle still depends on the Items family and the exact item's verified implementation. Its provenance does not grant extra effects.

Companion Pokémon remain outside estate-asset semantics.

## Encounter A — Estate Inventory Storage Perimeter

Full capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected combat content requires
- status lifecycle — PARTIAL as selected combat content requires
- terrain/weather/hazards/zones/reactions — BLOCKING when site hazards or reactive protection matter
- move-specific behavior — PARTIAL; selected content audit required
- abilities — PARTIAL; selected content audit required
- items — PARTIAL; selected content audit required
- Trainer Features/perks — PARTIAL; selected content audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect-object/route-control goals
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic protected-object playback

Full status: BLOCKED.

Reduced status: READY at narrative-contract level after ordinary battle-content audit.

Estate assets and records remain outside BattleSpec. AutoPTU may return only `IMMEDIATE_INVENTORY_STORAGE_APPROACH_CLEAR`. That does not authenticate an inventory, locate assets, assign title, validate a claim or close an estate.

## Encounter B — Legacy Transfer Route Interruption

The full version requires complete movement plus escort/protected-object carrying, lifecycle, tactical protect/withdraw policy and semantic playback. Those requirements remain incomplete.

Full status: BLOCKED.

Reduced status: READY after content audit.

The legacy object and courier stay outside BattleSpec. AutoPTU may establish only `IMMEDIATE_LEGACY_TRANSFER_ROUTE_CLEAR`. A later Narrative/Property event must establish whether a handoff actually occurred and what legal or customary effect it had.

## Encounter C — Vacant Homestead Access Incident

A rich version can require dynamic structures, hazards, zones/reactions, object interaction and objective-aware AI.

Full status: BLOCKED whenever those mechanics matter.

Reduced status: READY after content audit.

The property and contents are immutable during the tactical slice. AutoPTU may establish only `IMMEDIATE_PROPERTY_APPROACH_CLEAR`. That result says nothing about occupancy, abandonment, ownership, succession or permission to enter beyond the authored encounter contract.

## Encounter D — Testament Record Recovery Perimeter

Full implementation can require protected-document interaction/carrying, complete movement, lifecycle, hazards/reactions, tactical objective policy and adapter playback.

Full status: BLOCKED.

Reduced status: READY after content audit.

The record remains outside BattleSpec. AutoPTU may establish only `IMMEDIATE_RECORD_STORAGE_ACCESS_CLEAR`. Archives and estate review remain responsible for later access, authentication and relevance.

## Adapter authority

Minecraft/Cobblemon/Craftics can display authored estate objects, sealed storage, inherited spaces and later handoffs. They cannot derive an estate inventory from an entity inventory or chest contents, treat item pickup as ownership transfer, infer inheritance from family NPC proximity, or classify a deceased Trainer's Pokémon as property.

The adapter must never turn despawn, dropped-item cleanup, container generation or player pickup into Chronicle succession facts.

## Readiness conclusion

PR #307 is concrete production-path progress: forced movement can now consult defender Ability prevention before displacement, with Python-oracle parity and tests around the post-hit seam. That narrows another important parity gap while leaving the broader movement and Ability families incomplete.

The private-estate continuity layer itself requires no combat mechanics. Its reduced encounter variants remain feasible because assets, records, custodians, couriers and property semantics stay outside BattleSpec and AutoPTU returns only narrowly scoped tactical facts.