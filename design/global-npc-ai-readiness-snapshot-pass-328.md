# Global NPC AI Readiness Snapshot — Pass 328

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Read-only engine heads checked

AutoPTU-Java main: `925b20b84f94e2f24564873252277f0e7143c1f7`
Commit: `Freeze Trainer Feature dispatcher traversal parity (#390)`.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
Commit: `Career: keep battle coordinates synced after viewport resize (#237)`; commit message explicitly states presentation only and no battle-rule or outcome change.

The Java PR #390 adds a deterministic Trainer Feature event dispatch plan and parity fixture against pinned Python oracle `16d228efa63aabecb67fa788959a359aac7f8f03`. The commit itself states that the planner mirrors collection, de-duplication, enabled filtering, trigger normalization, and invocation order. Prerequisite, context, frequency, resource, and effect handling remain in server-owned execution infrastructure.

This is meaningful evidence for dispatch traversal. It is not evidence that all Trainer Feature effects are ported or correct.

## Capability assessment

### targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts

No promotion for steam, vapor, spray, glare, underwater vision, or other environmental obscurement.

### base movement legality — VERIFIED within audited ordinary contracts

No promotion for slick mineral crust, unstable thermal ground, special hot-surface traversal, or environment-driven route changes.

### complete movement including push/pull/knockback/interception/forced movement — PARTIAL

Still required for general forced slides, vent displacement, rescue/interception, pushes near hazardous ground, and other movement interactions.

### core calculations — VERIFIED within audited ordinary contracts

This does not prove an environmental-damage pipeline.

### action economy/initiative — VERIFIED within audited ordinary contracts

No promotion for arbitrary environmental interrupts or reaction windows.

### full turn/round lifecycle — PARTIAL

Existing round-start seams remain useful. They do not prove complete start/end lifecycle, delayed environmental effects, all phase transitions, or arbitrary scheduled hazards.

### full stateful damage pipeline — PARTIAL

No general promotion. Hydrothermal, fall, crushing, or other environment-originated damage remains gated.

### status lifecycle — PARTIAL

No general promotion. Burn or custom exposure conditions remain gated.

### terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by subfamily

No general promotion for dynamic steam, hot zones, unstable ground, timed vents, changing hazard boundaries, or hazard reactions.

### move-specific behavior — PARTIAL

Representative implemented Moves do not imply category completeness. Verify each Move used by a narrative encounter.

### abilities — PARTIAL

Representative Abilities do not imply category completeness. Species flavor cannot substitute for a verified Ability contract.

### items — PARTIAL

No general promotion.

### Trainer Features/perks — PARTIAL, with new traversal-parity evidence

PR #390 strengthens evidence for deterministic collection/de-duplication/filtering/trigger normalization/invocation ordering. Concrete Feature effects, prerequisites, context, frequency, resources, and full lifecycle coverage are not thereby verified.

### AI legal-action infrastructure — VERIFIED within audited ordinary contracts

No promotion for dynamic environmental-legality reasoning unless relevant contracts/tests prove it.

### AI tactical policy — BLOCKING for general complex environmental objectives

General autonomous rescue, retreat through changing hazards, civilian protection, feature manipulation, or multi-objective hydrothermal encounters remain blocking.

### Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING end-to-end

Presentation can visualize authoritative outcomes. It must not originate PTU legality, damage, conditions, feature causality, or NPC knowledge.

## Pass 328 encounter profile

Reduced `The Spring That Went Cold` can run without new engine capabilities beyond ordinary verified combat seams because hydrothermal state changes occur through narrative world events between scenes and unsupported sectors can be represented as static blocked geometry.

The intended full version requires additional evidence for environmental obscurement, complete movement, full lifecycle, stateful environmental damage, status lifecycle, hazard/zone/reaction behavior, and any specific Moves, Abilities, Items, or Trainer Features selected later.

## Source-material boundary

The narrative repository inspection did not surface an adopted `sources/caelo` mechanical source. Existing Kairos material remains comparative where the project already documents it. Do not replace authoritative PTU/Caelo mechanics with public campaign posts, Pokédex flavor, Minecraft behavior, or assumptions from representative Java implementations.

## Promotion decision

No permanent capability family is promoted by Pass 328.

The only live delta recorded here is stronger, narrowly scoped Trainer Feature dispatch-traversal parity evidence from Java PR #390.