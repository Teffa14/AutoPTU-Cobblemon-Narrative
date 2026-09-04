# Engine readiness snapshot — Pass 249

Status: LIVE EVIDENCE SNAPSHOT
Canon effect: NONE
Date: 2026-09-04

## Read-only engine heads inspected

AutoPTU-Java main: `cc247607ffa28969990465945e814ccd4545fa51` — Freeze Naturewalk forced-movement trap block (#339).

The live commit contains a regression for forced movement landing on a tile trap when the target has Naturewalk. It verifies that movement can resolve, the trap remains, Slowed is not applied, and a reduced semantic `trap_block` event is exposed for that exact tested path.

This is evidence for that slice only. It does not establish complete forced movement, complete terrain/hazard behavior, complete Ability behavior, or full reaction coverage.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — Career viewport coordinate synchronization after resize.

That commit is presentation-only and does not alter battle rules or outcomes.

Neither engine repository was modified by Pass 249.

## Capability classification

Targeting / footprints / range / LoS: VERIFIED within the currently audited contracts.

Base movement legality: VERIFIED within the currently audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. The Java landing/trap/Naturewalk regression proves a narrow forced-movement landing consequence path, not the family.

Core calculations: VERIFIED within the currently audited contracts.

Action economy / initiative: VERIFIED within the currently audited contracts.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING outside tested slices.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL. Naturewalk evidence is representative of one tested interaction only.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING as a complete family.

Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end.

## Pass 249 dependency result

The reduced indirect-sign investigation loop requires no AutoPTU combat capability. It requires the Ouros population/projection/observation contracts plus an adapter capable of consuming a presentation decision without inventing ecological truth.

The direct-entity path requires the adapter to preserve Pass 239 ordering: counted source selection, atomic lease reservation, materialization, UUID correlation, release/reconciliation.

The uncorrelated-native-entity branch is still BLOCKING at the adapter layer because no live evidence in the inspected engine repositories proves the exact Cobblemon hook for suppressing, hiding, despawning or otherwise isolating an uncontrolled native entity from authoritative interaction.

A rich pursuit/interception version additionally depends on base movement, complete movement, lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Targeting/range/LoS, terrain/zones/reactions, damage, statuses, Moves, Abilities, Items and Trainer Features are required only when the authored encounter invokes those exact families.

## Current implementation seam

Pass 249 now defines and regression-tests the authority behavior expected at the seam:

projection envelope → presentation arbitration → indirect evidence or counted-source lease → Cobblemon presentation → sanitized observation/reconciliation.

What remains unverified is the actual Minecraft/Cobblemon runtime hook that executes these decisions. No narrative fixture is allowed to claim that hook exists until adapter code/tests prove it.

## Open questions

- exact adapter behavior for an uncorrelated native entity;
- presentation budget/rate limiting for indirect signs;
- whether individual attribution of off-screen evidence is ever safe or necessary;
- species-specific validation for signs such as calls, tracks or nesting evidence;
- the physical lower Sendero forage resource remains unresolved canon.
