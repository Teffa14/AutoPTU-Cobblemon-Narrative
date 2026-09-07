# Global NPC AI Readiness Snapshot — Pass 332

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records the live mechanical evidence used by the environmental-DNA/sample-provenance work in Pass 332. AutoPTU-Java and AutoPTU remain read-only evidence sources. The narrative repository is the only writable destination.

Ratings remain conservative. One implemented mechanic, dispatch seam, Feature, hazard or event hook does not establish family-wide support.

## Repository inspection basis

The narrative repository recursive tree at `437c0228c949a3d17c7675b2b4f9b02483dba2e3` was inventoried before authoring. `CURRENT_FOCUS.md`, canon governance, the playable foundation, the current Kairos source index, Pass 331, recent environmental/investigation material and repository-wide searches for environmental DNA, eDNA, genetic samples, metabarcoding, sample contamination and presence inference were reviewed.

No dedicated sample-to-species-presence provenance owner was found. Existing communications, archives, ecology and observation systems remain dependencies rather than duplicate owners.

Canon is unchanged.

## Live read-only heads

### AutoPTU-Java

Current main head observed during Pass 332:

`7cd6e7f8193d302e56bb5107f43491cefd3fe8e0`

Commit / PR lineage: `Bind Trainer Feature dispatch plans to server-owned content (#391)`.

Narrow verified evidence:

- server-owned `TrainerFeatureDispatchCatalog` binds the already-frozen dispatch plan to rich Feature definitions inside authoritative Java core;
- Minecraft/Cobblemon/Craftics adapters may identify/render but do not supply Feature definitions while battle rules resolve;
- duplicate trainer identities fail instead of producing ambiguous bindings;
- dispatch order and first-win Feature-definition binding are tested;
- this slice does not establish complete Trainer Feature execution, prerequisites, context, frequency/resources, every trigger or every Feature.

The recorded Python-oracle basis for this Trainer Feature parity lineage remains distinct from current Python main:

`16d228efa63aabecb67fa788959a359aac7f8f03`

### AutoPTU Python

Current main head observed during Pass 332:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

Its commit message explicitly states that the change is presentation-only and changes no battle rules or outcomes. It creates no mechanical promotion for Pass 332.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts already established by the engine project.

Pass 332 boundary: dense vegetation, spray, darkness, sensor-assisted acquisition, eDNA-based target acquisition or using a sample result to bypass ordinary LoS are not covered.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Pass 332 boundary: specialized swimming, wading, climbing, squeezing or unstable-bank traversal is not inferred.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Pass 332 rich dependencies include rescue, interception, current-driven displacement and unstable-edge movement.

### core calculations

Rating: VERIFIED for ordinary audited deterministic combat calculations.

Assay confidence, sample quality, transport inference and species-presence interpretation remain world/research semantics rather than combat math.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Pass 332 adds no category-wide promotion.

### full turn / round lifecycle

Rating: PARTIAL.

Existing round-start semantic and Trainer Feature seams remain useful but do not establish all phases, delayed effects, environmental schedules or timed sampling windows.

### full stateful damage pipeline

Rating: PARTIAL.

Pass 332 rich dependencies can include fall, debris, current or environmental damage. Adapter-authored HP changes remain prohibited.

### status lifecycle

Rating: PARTIAL.

Any persistent tactical exposure or condition requires verified status behavior. Pass 332 defines no contamination, wetness, research or detection status.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Pass 332 rich dependencies can include rain, moving water edges, unstable banks, protected observation zones, debris and reaction windows. Each subfamily requires its own evidence.

### move-specific behavior

Rating: PARTIAL.

Every Move used for sensing, concealment, terrain alteration, displacement, rescue or equipment interaction remains individually gated.

### abilities

Rating: PARTIAL.

No Ability receives laboratory, species-detection, tracking, navigation or environmental-DNA authority from flavor alone.

### items

Rating: PARTIAL.

No sampler, filter, field instrument, laboratory device or protective equipment receives PTU tactical behavior without authoritative rules evidence and implementation coverage.

### Trainer Features / perks

Rating: PARTIAL.

PR #391 materially improves authoritative Feature-content binding after frozen dispatch planning. It still does not prove complete execution, prerequisite/context/frequency/resource handling, every trigger or every Feature.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This rating does not establish rich protect-equipment, rescue, observation or non-defeat policy.

### AI tactical policy

Rating: BLOCKING for the general rich behaviors required by a full Pass 332 field encounter.

Examples include protecting a researcher or sample kit, holding an observation objective, retreating instead of defeating a wild subject, rescuing an actor and responding to dynamic water hazards.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter may present authoritative world/tactical state where contracts exist. It must not become an alternate ecology, laboratory, species-presence, movement, damage, status, knowledge or Trainer Feature rules engine.

## Pass 332 reduced-version readiness

The reduced `The Species That Was There Yesterday` loop can proceed now because its central problem lives in world-state evidence, sample provenance and NPC knowledge rather than live laboratory or fluid simulation.

Use:

- persistent sample IDs;
- collection feature and semantic time;
- explicit collector identity;
- custody and processing lineage;
- positive, negative, inconclusive or invalidated result events;
- result time distinct from collection and receipt time;
- analyst interpretations with evidence references and revision lineage;
- explicit report/publication receipt;
- repeat samples;
- direct field observations;
- feature-scoped institutional decisions and later revisions;
- ordinary verified targeting, base movement, calculations, action economy/initiative and legal-action infrastructure if combat is necessary.

Do not require:

- live DNA shedding or decay simulation;
- simulated fluid transport;
- automatic species-location inference;
- sample-derived encounter spawning;
- special sensor targeting;
- rich rescue/interception/current movement;
- dynamic environmental schedules;
- persistent custom exposure conditions;
- adapter-authored ecological truth;
- adapter-authored NPC knowledge.

## PTU / Caelo source state

The inspected narrative source inventory continues to expose comparative Kairos material under `sources/kairos`. The source index routes utility classes including Researcher, ecosystem guidance, movement, hazards and terrain/weather into the supplied compilation while explicitly warning that these are routing aids rather than automatic Ouros rules.

No adopted `sources/caelo` rules source was found during Pass 332.

Accordingly, Pass 332 authors no numerical or mechanical rules for Researcher, Perception, Survival, Education Skills, sample collection, laboratory analysis, species detection, movement, water, weather, contamination, sensing, Moves, Abilities, Items or Trainer Features.

## Category changes in Pass 332

No family-wide rating changes.

AutoPTU-Java and AutoPTU heads are unchanged from Pass 331. The progress in Pass 332 is narrative/world architecture: sample-derived ecological evidence now has a provenance-safe contract and a reduced investigation loop that can operate without forcing missing tactical mechanics into Minecraft/Cobblemon/Craftics.
