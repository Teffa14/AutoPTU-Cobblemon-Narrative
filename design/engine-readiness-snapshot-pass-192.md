# Engine Readiness Snapshot — Pass 192

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: `2a1c209f29d01a98f517718bc5347b9db50bf95a`

Read-only engine repositories:
- AutoPTU-Java head inspected: `b54560dbfca4c9ae1d502113e87d526737a6b48c`
- AutoPTU head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live Java change since pass 191

Commit `b54560dbfca4c9ae1d502113e87d526737a6b48c` binds `BattleRuntimeDependencies` through authoritative direct move execution, area move execution, delayed-hit execution, and production move-resolution seams so post-hit forced movement receives the shared authoritative dependency snapshot.

This is meaningful evidence that forced-movement rule-content dependencies are now threaded farther through production execution rather than only existing at an isolated helper boundary.

It does not prove complete movement as a family.

Still not demonstrated as one verified complete matrix by this commit:
- Push coverage;
- Pull coverage;
- Knockback coverage;
- Interception coverage;
- collisions;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering across all forced-movement forms;
- terrain-mediated displacement;
- every combination of those behaviors with move-specific, Ability, Item, and Trainer Feature content.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains contract-scoped. It does not mean every edge case or every content interaction in the category exists.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

The new Java head improves the first category's composition evidence but does not promote it.

### BLOCKING when a concept requires the complete family

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

These labels mean Narrative should not design a full encounter as runnable merely because one representative mechanic exists elsewhere.

## Pass 192 encounter disposition

Encounter: `Open Field-School Session at Glass Bend`

Full version depends on:
- targeting/footprints/range/LoS: VERIFIED for audited contracts;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL and blocking for corridor interception/displacement richness;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected roster uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING when route conditions are represented tactically;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for competent autonomous tactical behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING for faithful end-to-end world execution.

Disposition: FULL VERSION BLOCKED.

Reduced version remains viable because learners, lesson state, withdrawal, educational evidence, and route context stay in Narrative world state. Any remaining threat is compiled as a separate ordinary battle using only audited content and stable geometry.

## Education-specific mechanical boundary

The PTU source set contains real mechanical concepts involving Pokémon Education, Mentor, Tutor Points, Poké Edges, Skill ranks, Move tutoring, and defined Features.

No evidence inspected in this pass proves a complete engine subsystem that turns Narrative lesson attendance into any of those effects.

Therefore:
- classroom attendance must never mutate PTU Skills;
- a quiz must never award a Skill Rank;
- a lesson must never grant a Feature or Edge;
- a teaching scene must never spend Tutor Points unless an authoritative PTU mechanic explicitly executes it;
- Jo's `Mentor` class concept does not allow Narrative to emulate Mentor effects.

This is an engine boundary, not merely a lore preference.

## AutoPTU Python evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head states that the change synchronizes presentation coordinates after viewport resize and does not change battle rules or outcomes. No permanent capability category is promoted from that evidence.

## Caelo unresolved

No indexed live evidence inspected this pass establishes:
- formal education law;
- compulsory schooling;
- admissions or age rules;
- trainer licensing via school;
- examinations with regional legal effect;
- accreditation or certificates;
- field-school credentials;
- educational authority hierarchy.

Narrative must keep these uncertain until sourced.
