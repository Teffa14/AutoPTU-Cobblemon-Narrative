# Hydraulic Dungeon Implementation Contract

Status: DESIGN CONTRACT / NON-CANON
Date: 2026-09-06
Pass: 314

## Goal

Define the boundary between a proposed hydraulic exploration space and the current tactical engine so narrative work can advance without asking the Minecraft/Cobblemon adapter to invent missing PTU behavior.

This contract does not approve a region, institution, species roster or history.

## Narrative invariants

The central premise must survive both implementation tiers.

The player enters a hydraulically connected facility through multiple routes, learns cause and effect from physical evidence, reconstructs why downstream state is contradictory and makes a repair or allocation decision with persistent consequences.

The reduced tier cannot replace the mystery with a different story. It removes unsupported tactical simulation only.

## Reduced tier

Gate state changes happen between scenes as authored deterministic world transitions.

Water state changes route graph availability. `FLOODED` can block an edge. `DRY` or `OPEN` can expose an edge. Those labels describe narrative/world state and do not create PTU statuses.

No water current performs forced movement.

No gate transition occurs at a battle phase boundary.

No environmental water damage enters the HP/injury pipeline.

No reaction rescue, interception, delayed hazard pulse or dynamic zone is required.

No custom wet, soaked, drowning, pressure or slip condition is introduced.

A tactical encounter, if present, occurs on stable nodes and uses only capability families already verified for the authored action.

## Full tier dependencies

Targeting/footprints/range/LoS: needed for cross-channel attacks, rescue targets or platform interactions. Audit status: VERIFIED within current audited contracts.

Base movement legality: needed for normal traversal on stable surfaces. Audit status: VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement: needed before current can move an actor or rescue/interception can change position. Audit status: PARTIAL.

Core calculations: needed for deterministic tactical arithmetic. Audit status: VERIFIED.

Action economy/initiative: needed for structured tactical choices. Audit status: VERIFIED.

Full turn/round lifecycle: needed before gate and water states can change reliably at turn/round boundaries. Audit status: PARTIAL.

Full stateful damage pipeline: needed before environmental hazards can apply authoritative battle harm. Audit status: PARTIAL.

Status lifecycle: needed only for explicitly authored persistent conditions. Audit status: PARTIAL. No hydraulic status is approved here.

Terrain/weather/hazards/zones/reactions: needed for flooded/current zones, unstable surfaces, surge hazards and reactive rescue. Audit status: MIXED / PARTIAL / BLOCKING by subfamily.

Move-specific behavior: needed only when a named Move changes the scene. Audit status: PARTIAL.

Abilities: needed only when a named Ability changes movement, water, terrain or weather. Audit status: PARTIAL.

Items: needed only for mechanically active equipment. Audit status: PARTIAL.

Trainer Features/perks: needed only when a Feature changes inspection, movement, rescue, legality or timing. Audit status: PARTIAL.

AI legal-action infrastructure: needed for autonomous actors to filter illegal actions. Audit status: VERIFIED.

AI tactical policy: needed for general autonomous hazard avoidance, rescue prioritization and positioning. Audit status: BLOCKING for general policy.

Minecraft/Cobblemon/Craftics adapter/playback support: needed for authoritative visual/world execution of gates, water changes, forced movement and combat consequences. Audit status: PARTIAL / BLOCKING end-to-end.

## Promotion rule

A representative implementation does not promote an entire capability family.

Before the full waterworks uses current-driven displacement, the exact forced-movement contract must have tests or equivalent evidence.

Before timed flooding is used during combat, the exact lifecycle hook and ordering must be verified.

Before environmental harm is used, the exact stateful damage path and relevant injury/faint consequences must be verified.

Before a Move, Ability, Item or Trainer Feature affects the environment, that exact behavior must be authored against the authoritative PTU/project source and verified in the engine.

## Project-source boundary

PTU and project-approved overlays remain authoritative for mechanics. This contract does not infer numerical rules from public fan projects or actual plays.

The inspected narrative repository contains `sources/kairos`. No Caelo source directory was identified during this pass. Any Caelo-specific hydraulic, swimming, inspection or environmental rule therefore remains UNVERIFIED until the actual project material is located and checked.

## Environmental readability rules

Each gate operation must communicate at least one immediate local effect.

Remote changes should have stable visual or documentary clues so the player can predict them rather than brute-force combinations.

The same physical trace should not prove more than it can support. Fresh tool wear can establish recent manipulation, not identity or intent. A water mark can establish prior water extent, not the exact cause by itself.

Pokémon behavior can contribute evidence only after the relevant species behavior and communication assumptions are source-backed.

## Persistence boundary

A future adapter may turn a solved hydraulic state into durable route/world-object state. Until such an adapter is authoritative, proposal documents should describe intended persistent consequences without claiming that Minecraft water blocks, gates or route topology already rehydrate end-to-end.

This prevents the narrative layer from becoming a second authority over physical world state.
