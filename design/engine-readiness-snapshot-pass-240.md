# Engine readiness snapshot — Pass 240

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Purpose: classify implementation dependencies for observation/research/NPC-knowledge concepts without extrapolating from representative mechanics.

## Read-only repositories inspected

### AutoPTU-Java

Live `main` inspected at:

`2ca8552c640c582c98e7a2cc4667a29426b8173a`

Commit: `Wire forced movement into shared landing consequences (#336)`.

Evidence in the commit message/diff lineage includes shared runtime movement landing application, forced movement through shared landing consequences, deterministic/stateful landing consequence tests and trap landing parity work.

Interpretation: this improves an important forced-movement/landing slice. It does not prove complete coverage of push, pull, knockback, interception, all forced movement, all hazards, all reactions or the entire complete-movement family.

### AutoPTU

Live `main` inspected at:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit is presentation-only viewport coordinate synchronization and explicitly states that battle rules/outcomes do not change.

No new mechanical evidence from this repository changes the readiness categories below.

## Permanent capability categories

`VERIFIED` means current audited contracts/tests support using the category within its established scope. It does not imply every content record in that family is implemented unless separately audited.

`PARTIAL` means meaningful implementation exists but the permanent category is not complete.

`BLOCKING` means the full intended concept cannot rely on the category as generally available.

`MIXED` means verified slices coexist with material unverified/blocking areas.

### targeting / footprints / range / LoS

State: VERIFIED within audited engine contracts.

Pass 240 reduced observation ledger does not require tactical LoS. A rich structured visibility encounter may consume this family.

### base movement legality

State: VERIFIED within audited movement contracts.

Reduced observation storage does not depend on it. Rich pursuit does.

### complete movement including push/pull/knockback/interception/forced movement

State: PARTIAL.

The live forced-movement landing integration is concrete progress but cannot be generalized to the entire family.

### core calculations

State: VERIFIED within audited contracts.

Pass 240 uses this only when the active Ouros rules profile invokes PTU checks/calculations.

### action economy / initiative

State: VERIFIED within audited contracts.

Not needed by the reduced field-research loop; structured timed encounters may consume it.

### full turn / round lifecycle

State: PARTIAL.

Any observation encounter with authoritative timed rounds must keep this dependency explicit.

### full stateful damage pipeline

State: PARTIAL.

Not required for noncombat observation. Required if the rich encounter permits damaging combat.

### status lifecycle

State: PARTIAL.

Not required unless a structured encounter explicitly uses statuses.

### terrain / weather / hazards / zones / reactions

State: MIXED / PARTIAL / BLOCKING outside verified slices.

Landing/trap work improves specific seams only. Fog, weather phases, broad zones, reactions and arbitrary hazards must not be assumed complete.

### move-specific behavior

State: PARTIAL.

A rich encounter must list every Move it relies on and validate those behaviors rather than treating the family as complete.

### abilities

State: PARTIAL.

Same rule: explicit Ability dependencies require current contract/test evidence.

### items

State: PARTIAL.

Observation tools that have purely world-service semantics can remain outside battle. PTU Items that alter checks or combat require verified item support.

### Trainer Features / perks

State: PARTIAL.

Perception/Survival/Education skill use must not be confused with blanket Feature support. Any Feature-based research bonus needs direct evidence.

### AI legal-action infrastructure

State: VERIFIED within audited contracts.

Useful only once the ecological interaction becomes structured tactical play.

### AI tactical policy

State: BLOCKING as a complete family.

A wildlife actor that must deliberately hide, flee, regroup, guard young or preserve escape routes cannot depend on generic full tactical policy yet.

### Minecraft / Cobblemon / Craftics adapter and playback support

State: PARTIAL / BLOCKING end-to-end.

Pass 240 specifically needs new adapter-facing seams for observation capture, projection lease correlation and semantic event delivery. Minecraft/Cobblemon may present what a player sees but must not expose hidden ledger truth or author PTU outcomes.

## Pass 240 implementation verdict

The observation/evidence/NPC-knowledge ledger can be implemented as a pure Ouros world-state subsystem now. It has no inherent dependency on unverified battle families.

Automatic overworld evidence capture from actual Cobblemon entities remains blocked on the end-to-end adapter seam. A first implementation can consume explicit semantic observation events from a controlled adapter boundary and use the deterministic JSON fixture as regression input.

The rich pursuit version remains gated by complete movement, full lifecycle where timed turns matter, any terrain/weather/reaction families it elects to use, AI tactical policy and adapter/playback.

## No category promotion

Pass 240 promotes no permanent engine capability category. The latest Java change is recorded as evidence for a forced-movement landing slice only.