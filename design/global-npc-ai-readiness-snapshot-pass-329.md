# Global NPC AI Readiness Snapshot — Pass 329

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records the mechanical evidence used by the volcanic-ash remobilization work in Pass 329. AutoPTU-Java and AutoPTU are read-only evidence sources for this task. The narrative repository is the only writable destination.

Category ratings remain conservative. A representative mechanic, event seam, move, Trainer Feature, or hazard does not establish family-wide support.

## Live read-only heads

### AutoPTU-Java

Current main head observed during this pass:

`925b20b84f94e2f24564873252277f0e7143c1f7`

Commit / PR lineage: `Freeze Trainer Feature dispatcher traversal parity (#390)`.

Verified narrow evidence from the live commit:

- deterministic Trainer Feature event-dispatch planning;
- preservation of trainer insertion order;
- collection across features, edges, and known features;
- first-occurrence de-duplication;
- enabled filtering;
- trigger normalization;
- invocation order;
- parity workflow against a pinned Python oracle.

The implementation comments explicitly keep prerequisite checking, context matching, frequency/availability, resource handling, and concrete effect application outside this planner. This is therefore evidence for a traversal/dispatch contract, not proof of full Trainer Feature semantics.

The parity workflow pins Python oracle commit:

`16d228efa63aabecb67fa788959a359aac7f8f03`

That oracle pin is recorded separately from the live Python main head below.

### AutoPTU Python

Current main head observed during this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

Its commit message explicitly states that the change is presentation-only and changes no battle rules or outcomes. It therefore supplies no new mechanical promotion for Pass 329.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for the ordinary audited contracts already established by the engine project.

Pass 329 boundary: dynamic volcanic-ash obscuration, particulate visibility, wind-driven visibility change, or evolving LoS are not covered by that ordinary verification. A full ash encounter remains gated until those behaviors have explicit contracts/tests.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Pass 329 boundary: ash-specific traction, deep deposits, unstable ash surfaces, wet-ash footing, or special terrain costs are not inferred from ordinary movement support.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Pass 329 dependencies: gust displacement, debris transport, slides, wet-ash flow displacement, rescue, interception, forced evacuation movement, and similar rich interactions remain gated.

### core calculations

Rating: VERIFIED for ordinary audited deterministic calculations.

Pass 329 adds no new arithmetic contract.

### action economy / initiative

Rating: VERIFIED for the ordinary audited primitives.

Pass 329 adds no promotion.

### full turn / round lifecycle

Rating: PARTIAL.

Existing round-start semantic/dispatch evidence is useful but does not establish all phases, all start/end hooks, arbitrary delayed effects, environment scheduling, reaction windows, or complete lifecycle parity.

Pass 329 dependencies: timed gusts, changing ash zones, recurring machinery, delayed collapse, rainfall transitions, or environment phases during combat remain gated.

### full stateful damage pipeline

Rating: PARTIAL.

Pass 329 dependencies: falling debris, collapse, impact, heat, abrasion, or any environmental damage must use verified stateful damage behavior rather than adapter-authored HP changes.

### status lifecycle

Rating: PARTIAL.

Pass 329 dependencies: any persistent exposure, impairment, or other real tactical condition requires a verified status lifecycle. No ash-specific status is authored by this pass.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Pass 329 dependencies include dynamic ash fields, wind, wet-debris zones, unstable ground, shelter zones, changing hazard boundaries, environmental reactions, and rainfall-driven tactical changes. Each subfamily must be verified on its own evidence.

### move-specific behavior

Rating: PARTIAL.

Every move that would interact with wind, terrain, weather, particulate matter, displacement, cleanup, shelter, or environmental state remains individually gated.

### abilities

Rating: PARTIAL.

No Ability receives ash, wind, weather, terrain, sensing, immunity, or environmental authority from narrative flavor alone.

### items

Rating: PARTIAL.

No Item receives cleanup, protection, sensing, terrain, weather, or environmental mechanics without rules evidence and implementation coverage.

### Trainer Features / perks

Rating: PARTIAL.

PR #390 materially improves narrow traversal/dispatch parity evidence. It does not complete prerequisites, context, frequency, resources, effects, every trigger, every Feature, or end-to-end interaction behavior.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This rating does not mean the tactical policy knows how to choose rich environmental objectives.

### AI tactical policy

Rating: BLOCKING for the general rich behaviors required by a full Pass 329 encounter.

Examples still requiring policy support include evacuation, escort, shelter-seeking, rescue, civilian protection, dynamic hazard avoidance, work objectives, and decisions where defeating all opponents is not the tactical goal.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter can present world/tactical state where contracts exist. It must not become an alternative rules engine for ash visibility, wind, terrain, damage, statuses, forced movement, hazards, reactions, NPC knowledge, or institutional decisions.

## Pass 329 reduced-version readiness

The reduced `The Road Swept Clean Twice` loop can proceed without waiting for the blocked families because its central problem lives in world-state provenance and institutional decision-making.

Use:

- persistent feature IDs;
- authored between-scene ash-transfer events;
- explicit observation provenance;
- explicit report delivery/receipt;
- feature-scoped access states;
- decision/review lineage;
- static legal battle geometry when combat is necessary;
- ordinary verified targeting, base movement, calculations, action economy/initiative, and legal-action infrastructure.

Do not require:

- dynamic ash-cloud LoS;
- wind displacement;
- live debris or lahar movement;
- environmental damage;
- ash exposure statuses;
- hazard reactions;
- rescue/interception mechanics;
- autonomous evacuation policy;
- adapter-authored mechanics.

This preserves the narrative premise while keeping missing PTU behavior out of Minecraft/Cobblemon/Craftics.

## PTU / Caelo source state

The inspected narrative repository continues to expose the existing Kairos comparative source material. No adopted `sources/caelo` rules source was found in the current internal inventory during Pass 329.

Accordingly, Pass 329 does not invent mechanical values for ash, visibility, wind, rain, traction, terrain, damage, statuses, skill checks, sensing, Moves, Abilities, Items, or Trainer Features.

## No category promotions in Pass 329

AutoPTU-Java main remains at the same #390 traversal-parity evidence used by Pass 328, and AutoPTU Python remains on its presentation-only head. Pass 329 therefore makes no family-wide promotion.

The meaningful progress in this pass is architectural and narrative: the world layer can now preserve material provenance and secondary transfer history while rich tactical behavior remains explicitly gated.
