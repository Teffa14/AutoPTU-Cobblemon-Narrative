# Global NPC AI Readiness Snapshot — Pass 330

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records the live mechanical evidence used by the karst hidden-drainage work in Pass 330. AutoPTU-Java and AutoPTU are read-only evidence sources for this task. The narrative repository is the only writable destination.

Ratings remain conservative. A representative mechanic, dispatch seam, Feature, hazard, or event hook does not establish family-wide support.

## Live read-only heads

### AutoPTU-Java

Current main head observed during this pass:

`7cd6e7f8193d302e56bb5107f43491cefd3fe8e0`

Commit / PR lineage: `Bind Trainer Feature dispatch plans to server-owned content (#391)`.

Verified narrow evidence from the live commit and PR description:

- new server-owned `TrainerFeatureDispatchCatalog` binds the previously frozen Trainer Feature dispatch plan back to rich rule definitions;
- rule content remains inside authoritative Java core instead of Minecraft/Cobblemon/Craftics adapters;
- planner insertion order and first-occurrence-wins identity are preserved across features, edges, and known features;
- trainer-class metadata and known Feature IDs are carried into bound invocations;
- duplicate trainer IDs are rejected instead of bound ambiguously;
- tests cover ordered binding, first-win selection, runtime-kind preservation, metadata propagation, and unmatched triggers.

The PR explicitly states that this slice does not yet wire `ROUND_START_EFFECTS`. `TrainerRuntimeState` still stores canonical Feature names while execution needs rich definitions. The catalog supplies the authoritative content-binding seam for a later execution slice.

This therefore strengthens Trainer Feature content ownership and dispatch binding. It does not prove concrete Feature execution, prerequisites, frequency/resource handling, every trigger, or full Trainer Feature semantics.

The PR records Python oracle basis:

`16d228efa63aabecb67fa788959a359aac7f8f03`

Keep that oracle pin separate from the live Python main head below.

### AutoPTU Python

Current main head observed during this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

The commit message explicitly states that the change is presentation-only and changes no battle rules or outcomes. It supplies no new mechanical promotion for Pass 330.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts already established by the engine project.

Pass 330 boundary: cave darkness, mist, spray, underwater sight, changing occlusion, narrow-portal special cases, or hidden-target behavior are not covered by ordinary LoS verification.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Pass 330 boundary: climbing, swimming, squeezing, slippery cave surfaces, submerged traversal, cave-specific terrain costs, or low-clearance movement are not inferred from ordinary support.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Pass 330 dependencies include currents, falls, rescue/interception, collapse displacement, forced channel movement, and moving-water effects.

### core calculations

Rating: VERIFIED for ordinary audited deterministic calculations.

Pass 330 adds no new arithmetic contract.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Pass 330 adds no promotion.

### full turn / round lifecycle

Rating: PARTIAL.

Existing round-start event/dispatch seams and Trainer Feature planning/binding are useful but do not establish all phases, delayed effects, environment scheduling, reaction windows, changing access, or complete lifecycle parity.

Pass 330 dependencies include timed flooding, delayed collapse, recurring environmental pulses, changing cave routes, or scheduled cave events during combat.

### full stateful damage pipeline

Rating: PARTIAL.

Pass 330 dependencies include fall, collapse, impact, crushing, drowning-like, or other environmental damage. These must use verified authoritative damage behavior rather than adapter-authored HP changes.

### status lifecycle

Rating: PARTIAL.

Any persistent tactical exposure or condition requires verified status behavior. Pass 330 defines no cave, contamination, drowning, pressure, or darkness status.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Pass 330 dependencies include moving water zones, unstable ground, collapse hazards, shelter, changing boundaries, environmental triggers, and reaction windows. Each subfamily must be validated independently.

### move-specific behavior

Rating: PARTIAL.

Every Move used for water control, cave traversal, illumination, displacement, digging, sensing, rescue, terrain alteration, or environmental interaction remains individually gated.

### abilities

Rating: PARTIAL.

No Ability receives cave, groundwater, current, sensing, darkness, movement, immunity, or navigation authority from narrative flavor alone.

### items

Rating: PARTIAL.

No Item receives cave-navigation, tracing, illumination, water, protection, rescue, or sensing mechanics without rules evidence and implementation coverage.

### Trainer Features / perks

Rating: PARTIAL.

PR #391 materially improves authoritative content binding after the already frozen traversal/dispatch planner. It still does not wire round-start execution or prove prerequisites, context, frequency, resources, concrete effects, all triggers, or all Features.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This rating does not establish rich cave-survival or investigation policy.

### AI tactical policy

Rating: BLOCKING for the general rich behaviors required by a full Pass 330 cave encounter.

Examples include rescue, escort, retreat, investigation-under-threat, dynamic hazard avoidance, protecting sampling equipment, navigating changing routes, and objectives where defeating all opponents is not the goal.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter may present authoritative world/tactical state where contracts exist. It must not become an alternate hydrology, movement, damage, status, sensory, knowledge, or Trainer Feature rules engine.

## Pass 330 reduced-version readiness

The reduced `The Stream That Vanished Uphill` loop can proceed now because its central logic lives in world-state evidence and institutional knowledge rather than live groundwater simulation.

Use:

- persistent feature IDs;
- hidden authored connection edges;
- between-scene trace events;
- separate receptor observations;
- explicit provenance and sampling windows;
- explicit report/publication receipt;
- belief and interpretation lineage;
- feature-scoped decisions and revisions;
- static cave route edges;
- ordinary verified targeting, base movement, calculations, action economy/initiative, and legal-action infrastructure when combat is necessary.

Do not require:

- dynamic subsurface fluid simulation;
- cave darkness modifiers;
- currents or forced movement;
- swimming/drowning rules;
- live flooding;
- cave collapse damage;
- persistent contamination/exposure statuses;
- hazard reactions;
- rescue/interception mechanics;
- autonomous dynamic-hazard policy;
- adapter-authored hydrologic truth.

This keeps the investigation playable while missing PTU behavior stays out of Minecraft/Cobblemon/Craftics.

## PTU / Caelo source state

The inspected narrative repository continues to expose the Kairos comparative source inventory under `sources/kairos`. No adopted `sources/caelo` rules source was found during Pass 330.

Accordingly, Pass 330 authors no numerical or mechanical rules for Swim, climbing, squeezing, darkness, water pressure, currents, drowning, contamination, Perception/Survival/Education checks, Pokémon sensing, Moves, Abilities, Items, or Trainer Features.

## Category changes in Pass 330

No family-wide rating changes.

AutoPTU-Java advanced from #390 to #391. The new evidence is meaningful but narrow: Trainer Feature dispatch plans can now bind to exact server-owned rich content without delegating rule definitions to adapters. Trainer Features/perks remain PARTIAL because execution and broader semantic coverage are still incomplete.

AutoPTU Python remains on its presentation-only main head. The central progress of Pass 330 therefore remains narrative/world architecture plus a fresher, more precise engine evidence snapshot.
