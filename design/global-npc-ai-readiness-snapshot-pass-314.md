# Global NPC / Encounter Readiness Snapshot — Pass 314

Status: DESIGN EVIDENCE / NON-CANON
Date: 2026-09-06
Pass: 314

## Read-only engine evidence

AutoPTU-Java live head inspected during this pass: `ae2a9c9a105615291b12ef9f24c8ab483e2aa187`.

The head aligns round history rotation after initiative rebuild and adds a post-initiative round-start hook plus a Python oracle/parity gate for that ordering seam. This strengthens evidence for one lifecycle/history ordering contract. It does not verify the full turn/round lifecycle, dynamic terrain transitions, forced movement, all damage/injury behavior or adapter playback.

AutoPTU Python live head inspected during this pass: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

That head explicitly describes a presentation-only viewport-coordinate synchronization fix and states that battle rules/outcomes do not change. No capability promotion is justified from it.

Both engine repositories remained read-only in Pass 314.

## Permanent capability categories

Targeting / footprints / range / LoS: VERIFIED within audited contracts.

Base movement legality: VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited contracts.

Action economy / initiative: VERIFIED within audited contracts.

Full turn / round lifecycle: PARTIAL. The Java round-history ordering seam is useful evidence but does not close the family.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by subfamily.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING for general autonomous tactical policy.

Minecraft / Cobblemon / Craftics adapter and playback support: PARTIAL / BLOCKING end-to-end.

## Pass 314 encounter impact

The reduced Three-Gate Waterworks does not need a capability promotion. Gate and water states change between scenes through authored world-state transitions. Flooded routes are graph constraints rather than tactical current zones. No forced movement, environmental HP damage, persistent water status, reaction rescue or mid-round hydraulic update is required.

A tactical encounter in the reduced version can remain on stable dry nodes and use verified targeting, basic movement, core calculations and initiative, subject to the exact authored move/action contracts.

The full version is blocked from treating these features as authoritative until narrower evidence exists:

Current-driven displacement requires complete movement / forced movement.

Mid-round gate or water changes require verified lifecycle ordering plus terrain/hazard state transitions.

Hydraulic environmental harm requires the full stateful damage path used by that hazard.

Rescue reactions require the relevant reaction/interception family.

Dynamic flooded/current zones require terrain/hazard/zone support plus adapter playback.

Autonomous Pokémon or NPC rescue tactics require AI tactical policy beyond legal-action filtering.

Visible Minecraft/Cobblemon gate and water changes require an authoritative adapter/world-state path rather than narrative-side duplication.

## Mechanical questions carried forward

Locate and verify the authoritative PTU/project rules for Swim-related traversal, rescue and any current interaction before assigning numerical behavior.

Locate Caelo source material, if available to the wider project, before adopting any Caelo overlay relevant to water, hazards, inspection or movement. The inspected narrative repository exposes Kairos material but no Caelo directory.

Verify exact PTU Skills or Trainer Features before using a mechanical roll to diagnose civil infrastructure or interpret evidence.

Verify species behavior before a Pokémon's habitat or movement pattern becomes a deterministic clue.

Do not infer full lifecycle, movement or hazard coverage from the Java head's single round-history ordering seam.
