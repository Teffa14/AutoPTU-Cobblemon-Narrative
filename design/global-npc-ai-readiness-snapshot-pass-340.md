# Global NPC AI readiness snapshot — Pass 340

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

Pass 340 adds an executable operational-readiness bridge between the existing Maintenance/Shared Equipment authority and the Pass 338/339 global resource planner.

AutoPTU-Java and AutoPTU were inspected read-only. Only the narrative repository was modified.

No family-wide combat capability is promoted from a representative mechanic.

## Narrative inspection basis

Narrative `main` began this pass at `fc0f194f11f1b92db5e54926d86ddd3702ccc894`.

Before writing, the recursive repository tree and relevant owners were inspected. The key pre-existing authorities are `design/shared-equipment-lending-issued-assets-extension.md`, `design/facility-maintenance-repair-inspection-extension.md`, Pass 338 resource availability and Pass 339 reservation lifecycle.

Shared Equipment already says Maintenance owns readiness work and exposes `readiness_record_ref`. Facility Maintenance already owns observations, faults, assessment, work orders, repair and verification. Pass 339 explicitly states that return does not prove a resource is undamaged, calibrated, refilled or otherwise ready for future use.

Pass 340 therefore adds only an adapter. It does not duplicate those lifecycles.

## New executable narrative evidence

Added:

- `tools/global_npc_resource_readiness.py`
- `tests/test_global_npc_resource_readiness.py`
- `implementation/global-npc-resource-readiness-fixture-v1.json`
- `design/global-npc-resource-operational-readiness-bridge-pass-340.md`
- `research/2026-09-07-operational-readiness-field-equipment-scan-340.md`
- `proposals/2026-09-07-the-instrument-that-was-ready-yesterday-case-340.md`

The V1 bridge consumes stable owner-supplied readiness records with semantic validity windows. It projects blocking outcomes into Pass 338's generic planner view without mutating the source resource or technical record. It preserves exact status, source reference and reason outside that lossy planner projection.

Explicit readiness can be required by a caller. Missing or expired readiness then blocks as UNKNOWN. LIMITED is conservative in V1 because domain-specific acceptable limitations are not inferred globally.

## Live read-only engine heads

### AutoPTU-Java

Observed `main` head:

`83ec9610ef83a7d71186a404ef509faa317109d1`

Merge: `Add round-start ability effect execution for Air Lock` (PR #396).

PR #396 adds a server-owned round-start Ability effect registry/executor and freezes Air Lock against the pinned Python oracle. Its PR contract states that Air Lock emits `weather_suppress` events per holder without mutating battle weather. Arena Trap, Intimidate and Impostor remain explicit unhandled plan entries until their stateful effects are frozen separately. No adapter-side PTU rules are added.

This is stronger evidence for one Ability family and one round-start/weather seam. It does not prove complete Abilities, complete weather behavior or the full turn/round lifecycle.

### AutoPTU Python

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

The head remains `Career: keep battle coordinates synced after viewport resize (#237)` and explicitly states that the change is presentation-only with no battle-rule or outcome change.

## PTU / Caelo boundary

Exact tactical mechanics remain sourced from the project's PTU/Core/Pokédex/Caelo boundary. Public equipment-quality material and PTU community material are narrative/design evidence only.

Pass 340 defines no calibration Skill check, Technology/Education DC, Item activation, measurement bonus, repair action, equipment-damage rule, Pokémon labor capability, Move effect, Ability effect or Trainer Feature.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

The reduced readiness bridge has no targeting dependency. A field instrument that targets a creature, tile or zone requires its own verified behavior.

### base movement legality

Rating: VERIFIED for ordinary audited movement.

Pass 340 moves no actor or resource automatically.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Only a rich field encounter involving carrying, rescue, interception or forced displacement depends on this family.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle arithmetic.

Semantic readiness-window comparison is world logistics rather than PTU combat math.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Readiness projection consumes no invented tactical action. Any in-combat instrument use/pass/equip action remains individually gated.

### full turn / round lifecycle

Rating: PARTIAL.

PR #396 proves another narrow round-start execution seam for Air Lock. It does not establish full lifecycle coverage. Pass 340 readiness time runs on world semantic time.

### full stateful damage pipeline

Rating: PARTIAL.

V1 does not damage equipment or actors.

### status lifecycle

Rating: PARTIAL.

Operational-readiness states are world-resource states, not PTU Status Afflictions.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

PR #396 adds concrete Air Lock weather-suppression event evidence but explicitly does not mutate battle weather and does not prove the complete weather/hazard/zone/reaction family.

### move-specific behavior

Rating: PARTIAL.

No Move behavior is inferred.

### abilities

Rating: PARTIAL.

PR #396 materially advances Air Lock round-start effect execution. Arena Trap, Intimidate and Impostor remain unhandled plan entries according to the merged PR description, and other Ability families remain outside this evidence.

### items

Rating: PARTIAL and individually gated.

An operationally ready `WorldResource` can be mundane. If it later maps to a PTU Item, world readiness does not prove tactical legality or effect implementation.

### Trainer Features / perks

Rating: PARTIAL and individually gated.

Technical readiness never grants a Trainer Feature.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

The reduced bridge filters world prerequisites only. It does not add invented tactical equipment actions.

### AI tactical policy

Rating: BLOCKING for rich resource-objective behavior.

Protecting an instrument, transferring it under pressure, withdrawing with it, preserving a survey objective or preferring observation to defeat remains outside current rich tactical-policy evidence.

### Minecraft / Cobblemon / Craftics adapter/playback

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft may render equipment condition/readiness UI after receiving authoritative state. It cannot make an instrument technically ready because the player picked it up, because an animation completed or because a client-side indicator is green.

## Reduced-version readiness

The Pass 340 bridge is world-agent executable and does not require AutoPTU.

Required inputs are stable resource IDs, semantic time and owner-supplied readiness records. The bridge then reuses Pass 338 resource gating and the existing global planner.

## Rich encounter dependencies

The optional field encounter in `The Instrument That Was Ready Yesterday` preserves the fixed dependency audit. Ordinary targeting/base movement/core arithmetic/action primitives remain VERIFIED within their audited scope; complete movement, lifecycle, damage and status remain PARTIAL; terrain/weather/hazards/zones/reactions remains MIXED/PARTIAL/BLOCKING; Moves, Abilities, Items and Trainer Features remain PARTIAL and individually gated; tactical policy remains BLOCKING for non-defeat equipment objectives; adapter/playback remains PARTIAL/BLOCKING end-to-end.

PR #396 does not remove those gates simply because Air Lock now has one frozen effect path.

## Unresolved questions

Resource-system work still includes resource-acquisition/request intents, institutional pools and delegated authority, quantity/capacity booking, waitlists/fairness, transfer/travel integration, consumable decrement, checkpoint persistence, player inventory binding and capability-scoped LIMITED readiness.

Maintenance integration still needs an explicit event/query seam that maps owner-specific verification records to the coarse bridge without allowing the global planner to fabricate technical conclusions.

Canon remains unresolved for any institution-specific equipment, inspection authority, instrument type, calibration cadence, readiness policy, measurement protocol or field scenario.
