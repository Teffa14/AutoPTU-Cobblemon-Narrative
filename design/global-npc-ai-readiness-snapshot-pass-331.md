# Global NPC AI Readiness Snapshot — Pass 331

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records the live mechanical evidence used by the wildlife-telemetry work in Pass 331. AutoPTU-Java and AutoPTU remain read-only evidence sources. The narrative repository is the only writable destination.

Ratings remain conservative. One implemented mechanic, dispatch seam, Feature, hazard or event hook does not establish family-wide support.

## Repository inspection basis

The narrative repository recursive tree was inventoried before authoring. `CURRENT_FOCUS.md`, canon governance, the previous readiness snapshot and repository-wide searches for telemetry, tracking collars, radio tags, directional receivers and triangulation were reviewed.

No dedicated wildlife-telemetry provenance owner was found. Existing infrastructure, communications and research layers remain reusable dependencies rather than duplicate owners.

## Live read-only heads

### AutoPTU-Java

Current main head observed during Pass 331:

`7cd6e7f8193d302e56bb5107f43491cefd3fe8e0`

Commit / PR lineage: `Bind Trainer Feature dispatch plans to server-owned content (#391)`.

Narrow verified evidence remains the same as Pass 330:

- server-owned `TrainerFeatureDispatchCatalog` binds frozen dispatch invocations to rich authoritative Feature definitions;
- rule content remains inside Java core rather than Minecraft/Cobblemon/Craftics adapters;
- planner order, identity and metadata binding are preserved;
- the slice does not yet establish complete Trainer Feature execution, prerequisites, frequency/resource handling, every trigger or every Feature.

The recorded Python oracle basis for this parity lineage remains:

`16d228efa63aabecb67fa788959a359aac7f8f03`

Keep that oracle pin distinct from current Python main.

### AutoPTU Python

Current main head observed during Pass 331:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

Its commit message states that the change is presentation-only and changes no battle rules or outcomes. It creates no mechanical promotion for Pass 331.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts already established by the engine project.

Pass 331 boundary: dense foliage, special sensor targeting, intermittent visibility, concealment, signal-based target acquisition or using telemetry to bypass ordinary LoS are not covered.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Pass 331 boundary: specialized climbing, swimming, squeezing, unstable-slope traversal or terrain-specific tracking movement is not inferred.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Pass 331 rich dependencies include falls, rescue/interception, forced displacement and moving-subject interactions beyond ordinary movement.

### core calculations

Rating: VERIFIED for ordinary audited deterministic calculations.

Telemetry error, triangulation uncertainty and signal strength are world/research data in this pass, not combat math.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Pass 331 adds no category-wide promotion.

### full turn / round lifecycle

Rating: PARTIAL.

Existing round-start semantic/Trainer Feature seams remain useful but do not establish all phases, delayed effects, environmental schedules or observation windows.

Pass 331 rich dependencies include timed field observation windows, delayed equipment events or recurring environmental changes during combat.

### full stateful damage pipeline

Rating: PARTIAL.

Pass 331 rich dependencies include fall, impact or environmental damage. Adapter-authored HP changes remain prohibited.

### status lifecycle

Rating: PARTIAL.

Any persistent tactical exposure or condition requires verified status behavior. Pass 331 defines no tracking, stress, signal or field status.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Pass 331 rich dependencies can include dense vegetation, storms, unstable ground, moving hazards, observation zones and reaction windows. Each subfamily requires its own evidence.

### move-specific behavior

Rating: PARTIAL.

Every Move used for sensing, concealment, terrain alteration, pursuit, displacement, rescue or equipment interaction remains individually gated.

### abilities

Rating: PARTIAL.

No Ability receives tracking, radio detection, navigation, sensing or telemetry authority from flavor alone.

### items

Rating: PARTIAL.

No collar, receiver, field instrument or protection device receives PTU tactical behavior without authoritative rules evidence and implementation coverage.

### Trainer Features / perks

Rating: PARTIAL.

PR #391 materially improves authoritative Feature-content binding after frozen dispatch planning. It still does not prove complete execution, prerequisite/context/frequency/resource handling, every trigger or every Feature.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This rating does not establish rich wildlife pursuit, rescue or protect-equipment policy.

### AI tactical policy

Rating: BLOCKING for the general rich behaviors required by a full Pass 331 field encounter.

Examples include escorting a researcher, protecting equipment, pursuing without cornering a wild subject, retreating, rescuing an injured actor and maintaining observation objectives while threatened.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter may present authoritative world/tactical state where contracts exist. It must not become an alternate telemetry, movement, sensory, damage, status, knowledge or Trainer Feature rules engine.

## Pass 331 reduced-version readiness

The reduced `The Signal That Stayed Behind` loop can proceed now because its central problem lives in world-state evidence, provenance and NPC knowledge rather than live GPS/radio simulation.

Use:

- persistent subject IDs;
- separate device IDs;
- authored assignment and detachment state;
- between-scene raw fix, failed-fix and radio-bearing observations;
- observation time distinct from receipt time;
- derived map/track versions with source lineage;
- independent sightings;
- explicit report/publication receipt;
- device recovery;
- belief and interpretation lineage;
- feature-scoped institutional decisions and revisions;
- ordinary verified targeting, base movement, calculations, action economy/initiative and legal-action infrastructure if combat is necessary.

Do not require:

- live radio propagation;
- simulated GPS satellites or signal strength;
- automatic route interpolation;
- sensor-based target acquisition;
- rich pursuit/rescue/interception;
- dynamic hazard scheduling;
- persistent tracking conditions;
- adapter-authored subject movement history;
- adapter-authored NPC knowledge.

## PTU / Caelo source state

The inspected narrative source inventory continues to expose comparative Kairos material under `sources/kairos`. No adopted `sources/caelo` rules source was found during Pass 331.

Accordingly, Pass 331 authors no numerical or mechanical rules for tracking, signal range, device accuracy, Perception, Survival, Technology Education, movement, pursuit, capture, sensing, weather interference, Moves, Abilities, Items or Trainer Features.

## Category changes in Pass 331

No family-wide rating changes.

AutoPTU-Java and AutoPTU heads are unchanged from Pass 330. The progress in Pass 331 is narrative/world architecture: wildlife telemetry now has a provenance-safe observation contract and a reduced quest loop that can operate without forcing missing tactical mechanics into Minecraft/Cobblemon/Craftics.
