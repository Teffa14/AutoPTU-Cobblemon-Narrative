# Engine readiness snapshot — Pass 241

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Purpose: classify dependencies for ecology-driven world events without extrapolating from representative mechanics.

## Read-only repositories inspected

### AutoPTU-Java

Live `main` inspected at:

`2ca8552c640c582c98e7a2cc4667a29426b8173a`

Commit: `Wire forced movement into shared landing consequences (#336)`.

Evidence includes shared runtime movement landing application, forced movement routed through shared landing consequences, stateful consequence ordering tests, trap landing parity gating and forced-movement landing integration tests.

Interpretation: this is meaningful evidence for one forced-movement/landing path. It does not prove complete push/pull/knockback/interception/forced-movement coverage, full hazard coverage or full reaction coverage.

### AutoPTU

Live `main` inspected at:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains presentation-only viewport coordinate synchronization and explicitly states that battle rules/outcomes do not change.

No new mechanical evidence from AutoPTU changes the readiness classification.

## Permanent capability categories

### targeting / footprints / range / LoS

State: VERIFIED within audited contracts.

Reduced Pass 241 world-event evaluation does not consume this family. A rich pursuit/defense encounter may.

### base movement legality

State: VERIFIED within audited contracts.

Not needed for event-state evaluation. Required for structured movement.

### complete movement including push/pull/knockback/interception/forced movement

State: PARTIAL.

The current Java forced-movement landing seam is verified as a slice only. Rich event variants using corridor interception or forced displacement remain dependent on direct mechanic evidence.

### core calculations

State: VERIFIED within audited contracts.

Reduced Pass 241 event evaluation can use world-service arithmetic without AutoPTU. PTU checks/calculations are consumed only when the active rules profile explicitly invokes them.

### action economy / initiative

State: VERIFIED within audited contracts.

Not required by the reduced event. Required for structured combat.

### full turn / round lifecycle

State: PARTIAL.

A rich event with timed tactical objectives or phase transitions cannot assume this family complete.

### full stateful damage pipeline

State: PARTIAL.

Not required by the reduced event. Required if the structured variant allows damaging combat.

### status lifecycle

State: PARTIAL.

Not required unless the authored tactical variant uses statuses.

### terrain / weather / hazards / zones / reactions

State: MIXED / PARTIAL / BLOCKING outside verified slices.

Pass 241 world-state may reference ecological weather/terrain context without requiring tactical weather/terrain mechanics. A rich encounter that makes those facts mechanical must declare the exact dependencies.

### move-specific behavior

State: PARTIAL.

Validate every Move selected for a structured event.

### abilities

State: PARTIAL.

Validate every Ability selected for a structured event.

### items

State: PARTIAL.

World-service equipment can remain outside battle if it does not pretend to resolve PTU Item mechanics. Tactical Item behavior requires direct evidence.

### Trainer Features / perks

State: PARTIAL.

No blanket Feature support is assumed. Any intervention bonus using a Feature requires exact implementation evidence.

### AI legal-action infrastructure

State: VERIFIED within audited contracts.

Required when wildlife enters structured tactical play.

### AI tactical policy

State: BLOCKING as a complete family.

The rich event variant requires objective-aware behavior if wildlife must prioritize fleeing, guarding, maintaining separation or preserving a corridor rather than merely choosing a legal attack/action.

### Minecraft / Cobblemon / Craftics adapter and playback

State: PARTIAL / BLOCKING end-to-end.

Pass 241 requires adapter seams for:

- projecting event-driven activity/visibility changes without changing population truth;
- keeping Pass 239 lease identity stable;
- emitting observable symptoms into Pass 240 evidence capture;
- presenting authorized route/access state;
- starting explicit AutoPTU handoff when structured conflict begins;
- applying semantic results back to persistent ecology.

The complete end-to-end path is not yet proven.

## Pass 241 reduced-version verdict

READY FOR WORLD-STATE IMPLEMENTATION independent of missing battle families.

The deterministic fixture can be consumed by an Ouros event evaluator now. It requires persistent ecology variables, event-instance persistence, observation/knowledge integration and intervention mutation seams. No tactical category is inherently required.

Minecraft-visible production use remains constrained by adapter/playback integration, but the core event evaluator does not need to wait for it.

## Rich-version blockers

A rich Sendero crossing encounter remains gated by:

- complete movement if interception/forced displacement/corridor control is authored;
- full turn/round lifecycle for timed phases;
- damage/status pipelines when applicable;
- exact terrain/weather/hazard/zone/reaction slices used;
- exact Moves, Abilities, Items and Trainer Features selected;
- AI tactical policy for ecology-aware objectives;
- Minecraft/Cobblemon/Craftics end-to-end playback/writeback.

## No category promotion

Pass 241 promotes no permanent engine capability category. The live Java evidence remains a verified forced-movement landing slice only.