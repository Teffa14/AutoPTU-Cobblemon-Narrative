# Global NPC AI Readiness Snapshot — Pass 333

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records the live mechanical evidence used by the derelict-fishing-gear / Puerto Bruma recovery work in Pass 333. AutoPTU-Java and AutoPTU remain read-only evidence sources. The narrative repository is the only writable destination.

Ratings remain conservative. A newly verified Trainer Feature sub-contract does not establish family-wide Feature coverage, and an ordinary movement/LoS contract does not establish aquatic rescue, entanglement or dynamic hazards.

## Narrative repository inspection basis

The complete recursive repository tree at narrative head `d8bfeef7fe30df4811c604b9c7188e62a45aacea` was inventoried before authoring.

The pass then reviewed:

- `CURRENT_FOCUS.md`;
- canon governance;
- `canon/ouros-playable-foundation-v1.md`;
- the current Pass 332 readiness snapshot;
- `sources/kairos/KAIROS_SOURCE_INDEX.md`;
- repository-wide searches for ghost gear, derelict fishing gear, abandoned/lost/discarded gear, nets, entanglement and related ownership/recovery concepts;
- recent ecology, material-provenance and evidence contracts to avoid creating a duplicate owner.

No dedicated derelict-fishing-gear / ghost-fishing provenance owner was found.

Pass 333 deliberately grows from established Marea Interior canon instead of inventing another disconnected region. Puerto Bruma, Marea Field Office, Tideglass Archive, Mara Veyra, Dr. Nerea Sol and Taro Min are reused as existing anchors. The proposed incident remains non-canon.

## Live read-only heads

### AutoPTU-Java

Current main head observed during Pass 333:

`257f58218204169ad8bd035772a4b4750ecc556e`

Commit / PR lineage:

`Add Python-parity Trainer Feature effect batching (#392)`

This is newer than the Pass 332 evidence.

Narrow verified evidence from the commit:

- a reusable `TrainerFeatureEffectBatch` composes effect payloads for one Trainer Feature;
- effect payloads execute in declaration order through the authoritative registry;
- only applied effects contribute to the aggregate result;
- target aggregation preserves first occurrence while deduplicating later repeats;
- zero, one and multiple applied effects receive explicit aggregate behavior;
- the workflow freezes this behavior against the pinned Python oracle and reruns the transactional Trainer Feature execution contract;
- the Python oracle pin for this parity lineage remains `16d228efa63aabecb67fa788959a359aac7f8f03`.

Live GitHub checks observed on the head include completed successful parity, Java-core, round-start and other contract jobs. No failure conclusion was found in the retrieved head check set.

Boundary:

This is meaningful progress inside Trainer Feature execution infrastructure. It still does not establish every Feature, trigger, prerequisite, frequency/resource rule, context rule or interaction. It does not authorize any rescue, fishing, rope, net, item or environmental Feature in Pass 333.

### AutoPTU Python

Current main head observed during Pass 333:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

Its commit message explicitly says the change is presentation-only and changes no battle rules or outcomes. It creates no mechanical promotion for Pass 333.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts already established by the engine project.

Pass 333 boundary:

Ordinary LoS does not establish underwater visibility, spray, netting as concealment, target acquisition through water, rescue targeting or line interactions.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Pass 333 boundary:

Ordinary movement does not establish swimming, wading, climbing rigging, moving on floating gear or unstable dock-edge traversal.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Rich Pass 333 dependencies include:

- current-driven movement;
- dragging/pulling gear;
- rescue movement;
- interception;
- forced displacement;
- knockback near unsafe edges.

The reduced version avoids these requirements.

### core calculations

Rating: VERIFIED for ordinary audited deterministic combat calculations.

Pass 333 adds no gear-tension, cutting, rescue, drowning or environmental formula.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

A normal battle can use these primitives. A special `cut net`, `free subject`, `stabilize gear` or specialist rescue action requires authoritative rules evidence rather than narrative invention.

### full turn / round lifecycle

Rating: PARTIAL.

Existing round-start and Trainer Feature infrastructure is useful but does not establish all phases or arbitrary delayed environmental state.

Rich Pass 333 dependencies include timed gear shifts, changing currents, staged machinery, delayed failures and multi-phase rescue windows.

### full stateful damage pipeline

Rating: PARTIAL.

Any impact, crushing, collision, environmental or gear-caused damage must go through authoritative stateful damage handling. Minecraft may not author HP changes.

### status lifecycle

Rating: PARTIAL.

A real restraint, entanglement or persistent exposure condition would require verified PTU status behavior. Pass 333 defines no tactical `ENTANGLED` status.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Rich Pass 333 dependencies include dynamic water, unsafe dock edges, net hazard zones, moving debris, reaction windows and temporary exclusion areas with tactical effect.

Each requires exact evidence. The reduced version represents unsafe space as static blocked geometry or world-state access restrictions.

### move-specific behavior

Rating: PARTIAL.

Every Move used to cut, free, pull, push, manipulate water, alter terrain, rescue, sense through water or interact with gear remains individually gated.

### abilities

Rating: PARTIAL.

No Ability receives rescue, anti-entanglement, aquatic navigation or gear-manipulation authority from flavor alone.

### items

Rating: PARTIAL.

No rope, cutter, float, hook, recovery rig, net or protective equipment receives tactical behavior without authoritative rule evidence and implementation coverage.

### Trainer Features / perks

Rating: PARTIAL.

PR #392 advances a narrow but important slice:

- generic Feature effect-payload batching now has a Python-parity contract;
- declaration order and aggregate target/result semantics are frozen;
- head checks observed for the new commit are successful in the retrieved set.

Family-wide promotion is still not justified. Pass 333 assumes no Feature can perform specialist rescue or gear interaction unless that exact Feature and trigger are later verified.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This supports standard legal battle choices. It does not prove rich non-defeat objectives.

### AI tactical policy

Rating: BLOCKING for the general rich behavior of the full Pass 333 encounter.

Examples:

- prioritize freeing/protecting a subject over defeating an opponent;
- avoid damaging recovery gear or trapped wildlife;
- escort workers;
- retreat from a moving hazard;
- hold an exclusion line;
- accept `site safe for recovery` as success without defeating all actors.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter may render authoritative gear, barriers, workers, wildlife and recovery aftermath. It must not become an alternate movement, entanglement, rescue, damage, status, ownership, ecology or NPC-knowledge engine.

## Pass 333 reduced-version readiness

`The Net That Kept Fishing` can proceed in reduced form now because its main play loop lives in persistent-object provenance, world observations, archive evidence and institutional decisions.

Use now:

- stable gear/object IDs;
- timed position observations;
- faded identifier observations;
- archive/registry query results;
- explicit loss reports where they exist;
- honest `record not found in searched collection` results;
- direct wildlife/habitat observations;
- feature-scoped access decisions;
- recovery assessments and recovery events between scenes;
- custody lineage;
- explicit report delivery and NPC knowledge;
- ordinary static battle geometry when combat is needed;
- ordinary verified targeting, base movement, calculations, action economy/initiative and legal-action infrastructure.

Avoid until verified:

- tactical net entanglement;
- live current simulation;
- automatic drifting gear;
- rescue/interception/dragging mechanics;
- custom cutting actions;
- drowning/scalding/exposure rules;
- dynamic hazard zones;
- adapter-authored wildlife injury;
- adapter-authored successful recovery;
- ownership or liability inferred from a texture/identifier.

## PTU / Caelo source state

The inspected narrative source inventory continues to expose comparative Kairos material under `sources/kairos`.

The Kairos index routes future source checks toward Fishing, movement/terrain, status afflictions, hazards, terrain/weather, ecosystem guidance, encounter construction and gear/items. The index explicitly says those references are routing aids and do not authorize Ouros rules.

No adopted `sources/caelo` rules source was found during Pass 333.

Accordingly, this pass authors no numeric or mechanical rules for:

- Fishing;
- nets or ropes;
- entanglement;
- escape checks;
- Swim/wading;
- currents;
- drowning;
- cutting gear;
- environmental damage;
- rescue actions;
- Moves;
- Abilities;
- Items;
- Trainer Features.

## Category changes in Pass 333

No family-wide rating changes.

The live Java evidence improved from PR #391 to PR #392 and now verifies a narrower Trainer Feature effect-batching contract in addition to the earlier planning/binding seams. Trainer Features/perks remain PARTIAL because broad execution coverage is still absent.

The main Pass 333 progress is narrative/world architecture and canon-connected content: Puerto Bruma now has a non-canon adventure candidate and reusable persistent-object recovery contract that can run in reduced form without duplicating missing PTU mechanics in Minecraft.