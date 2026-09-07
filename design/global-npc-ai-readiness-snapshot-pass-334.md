# Global NPC AI Readiness Snapshot — Pass 334

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records the live mechanical evidence used by the submerged-heritage / wreck-context work in Pass 334. AutoPTU-Java and AutoPTU remain read-only evidence sources. The narrative repository is the only writable destination.

No family-wide capability promotion is made from representative mechanics.

## Narrative repository inspection basis

Before authoring, Pass 334 inventoried the complete recursive repository tree at narrative head `f660b81f38acd82b9abfadf8dfb97f4279a0c5b6` and ran repository-wide searches for shipwreck, wreck, salvage, submerged archaeology/heritage, abandoned vessel and Sea Mauville-related terms.

Focused reads included:

- `CURRENT_FOCUS.md`;
- `README.md` and the mechanical-source boundary;
- `canon/README.md`;
- the complete current `canon/` directory inventory;
- `canon/marea-interior-map-resident-network-v2.md`;
- `sources/kairos/KAIROS_SOURCE_INDEX.md`;
- `design/global-npc-ai-readiness-snapshot-pass-333.md`;
- current live heads of AutoPTU-Java and AutoPTU.

No dedicated submerged-cultural-resource / wreck-context owner was found.

Pass 334 reuses established Puerto Bruma, Tideglass Archive and existing resident roles as optional bindings while keeping the wreck/object incident explicitly non-canon.

## Live read-only heads

### AutoPTU-Java

Current main head observed during Pass 334:

`257f58218204169ad8bd035772a4b4750ecc556e`

Commit / PR lineage:

`Add Python-parity Trainer Feature effect batching (#392)`

This is unchanged from Pass 333.

Narrow evidence retained:

- `TrainerFeatureEffectBatch` composes effect payloads in declaration order;
- only applied effects contribute to aggregate results;
- aggregate targets preserve first occurrence under de-duplication;
- parity is frozen against Python oracle commit `16d228efa63aabecb67fa788959a359aac7f8f03`;
- the workflow reruns the transactional Trainer Feature execution contract.

Boundary:

This does not verify family-wide Trainer Feature behavior, all triggers/prerequisites/frequencies/resources, underwater actions, survey actions, recovery actions or specialist archaeology/diving behavior.

### AutoPTU Python

Current main head observed during Pass 334:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly describes itself as presentation-only and says battle rules/outcomes do not change. It creates no rules promotion for Pass 334.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

Pass 334 boundary:

This does not establish underwater visibility, water-mediated LoS, obscuration by suspended material, target acquisition across water surfaces or unusual wreck geometry.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Pass 334 boundary:

This does not establish Swim, Dive, underwater movement, climbing wreck structure, air management or navigation through submerged spaces.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Rich Pass 334 dependencies include currents, drifting debris, rescue movement, interception, forced displacement and knockback around unsafe structure.

Reduced Pass 334 avoids these mechanics.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle calculations.

Pass 334 adds no pressure, oxygen, salvage, archaeology, structural-integrity or conservation formulas.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

A normal battle can use those primitives. Special `survey`, `document`, `stabilize`, `recover`, `lift`, `secure` or similar actions require explicit rules contracts before becoming tactical actions.

### full turn / round lifecycle

Rating: PARTIAL.

Rich dependencies include timed survey windows, current/visibility phases, delayed structural failure, staged recovery and environmental changes during a round.

### full stateful damage pipeline

Rating: PARTIAL.

Any collapse, impact, fall, crushing or environmental damage requires authoritative stateful damage handling. Minecraft may not write HP/injury outcomes.

### status lifecycle

Rating: PARTIAL.

No custom drowning, pressure, restrained, trapped, exposed or similar status is authored by this pass.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Rich dependencies include dynamic water, unstable structural zones, debris hazards, current zones, changing access and reaction windows.

The reduced implementation uses static blocked geometry and world-state access decisions instead.

### move-specific behavior

Rating: PARTIAL.

Every Move used to manipulate water, structure, debris, lighting, rescue, sensing or recovery remains individually gated.

### abilities

Rating: PARTIAL.

No Ability gains underwater breathing, archaeological sensing, wreck navigation, rescue or recovery authority from flavor alone.

### items

Rating: PARTIAL.

Dive gear, ropes, lights, survey devices, lifting equipment, cameras, conservation tools and similar equipment receive no tactical effects without authoritative rules and implementation evidence.

### Trainer Features / perks

Rating: PARTIAL.

PR #392 strengthens a narrow Feature effect-batching contract, but no Researcher, Chronicler, Survivalist or other Feature receives invented survey/archaeology benefits. Family-wide promotion remains unjustified.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This supports ordinary legal battle choices. It does not prove site-preservation, escort, survey or withdrawal objectives.

### AI tactical policy

Rating: BLOCKING for the rich encounter's general non-defeat behavior.

Examples include:

- protect a specialist rather than pursue maximum damage;
- preserve fragile site context;
- withdraw when environmental risk changes;
- avoid attacking non-hostile resident Pokémon;
- complete documentation and leave;
- recover one authorized object rather than loot the area;
- accept safe withdrawal or survey completion as success.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter may render authoritative site geometry, objects, Pokémon, survey markers and aftermath. It may not infer identity, ownership, historical interpretation, recovery permission, current-driven movement, statuses, damage, NPC knowledge or successful survey/recovery from presentation state.

## Pass 334 reduced-version readiness

`The Timber Without a Wreck` can proceed in reduced form now because its core loop uses world evidence rather than underwater tactical rules.

Use now:

- stable object IDs;
- timed position and condition observations;
- archive searches and source copies;
- explicit testimony provenance;
- relationship claims between object and possible source/site;
- remote/non-intrusive survey results as semantic world events;
- survey-map revisions;
- ecological observations kept separate from historical interpretation;
- feature-scoped access decisions;
- specialist recovery/conservation events between scenes when later canon permits them;
- explicit information delivery and NPC knowledge;
- ordinary static AutoPTU encounters using currently verified basic contracts.

Avoid until verified/canonized:

- live underwater movement;
- water-specific LoS rules;
- currents and forced movement;
- drowning/pressure/oxygen systems;
- tactical excavation or salvage actions;
- custom archaeology/survey Skill checks;
- dynamic collapse or debris hazards;
- adapter-authored object recovery;
- ownership or recovery authority inferred from an archive match;
- item value inferred from historical significance;
- automatic Pokémon behavior inferred from a wreck habitat label.

## PTU / Caelo source state

The narrative source inventory inspected in Pass 334 continues to expose comparative Kairos material under `sources/kairos`.

The Kairos source index points toward movement/terrain, hazards, terrain/weather, Researcher/Survivalist/other utility classes, encounter creation and Items. The index explicitly states that its references are routing aids rather than Ouros rules acceptance.

No adopted `sources/caelo` directory was found in the inspected repository state.

Pass 334 therefore authors no numeric/mechanical rules for:

- Swim or Dive;
- underwater vision;
- drowning, pressure or oxygen;
- currents;
- climbing or unstable wreck movement;
- excavation;
- navigation;
- archaeology/survey checks;
- carrying/lifting recovered objects;
- salvage or ownership;
- environmental damage;
- Pokémon sensing;
- Moves;
- Abilities;
- Items;
- Trainer Features.

## Category changes in Pass 334

No family-wide rating changes.

AutoPTU-Java and AutoPTU heads are unchanged from Pass 333. The mechanical contribution of this pass is therefore dependency precision rather than capability promotion.

The narrative contribution is a new reusable site-context owner that can support a future underwater dungeon while already functioning as an archive, shoreline, investigation and stewardship loop using the current engine boundary.