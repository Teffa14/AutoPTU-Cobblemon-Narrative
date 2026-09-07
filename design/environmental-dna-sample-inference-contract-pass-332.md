# Environmental DNA Sample & Inference Contract — Pass 332

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-07

## Purpose

Define how Ouros represents environmental-DNA style observations without converting sample results into omniscient species-location truth, invented PTU mechanics or Minecraft entity authority.

This contract is region-neutral and reusable by research, ecology, infrastructure, archive and institutional questlines.

## Core invariants

`SAMPLE_ID != SUBJECT_ID`

`DNA_DETECTED != SUBJECT_CURRENTLY_PRESENT`

`SAMPLE_LOCATION != SOURCE_LOCATION`

`SPECIES_DETECTION != INDIVIDUAL_IDENTIFICATION`

`DETECTION != ABUNDANCE`

`DETECTION != BREEDING_POPULATION`

`NEGATIVE_SAMPLE != SPECIES_ABSENT`

`LAB_RESULT != FIELD_PROVENANCE`

`DERIVED_DISTRIBUTION_MAP != RAW_SAMPLE_SET`

`MINECRAFT_ENTITY_PRESENT != ECOLOGICAL_OCCUPANCY`

`MINECRAFT_ENTITY_ABSENT != ECOLOGICAL_ABSENCE`

## Authoritative evidence chain

A sample-derived claim should preserve this lineage where applicable:

`source organism/species -> shedding event -> environmental medium -> transport/decay/resuspension -> collection event -> sample custody -> processing event -> assay result -> analyst interpretation -> communication/publication -> explicit receipt -> institutional decision -> follow-up evidence`

The runtime does not need to simulate every hidden physical step continuously. Hidden steps may be authored world truth while observations remain partial.

## Sample record

Recommended fields:

- `sample_id`;
- `collection_feature_id`;
- `collection_semantic_time`;
- `collector_actor_id`;
- `medium_kind` such as water, sediment, soil or air when canonically supported;
- `container_or_batch_id`;
- `custody_events[]`;
- `processing_events[]`;
- `assay_id` or analysis method reference;
- `result_kind`;
- `target_species_claim` if applicable;
- `quality_or_control_refs[]`;
- `source_provenance_refs[]`;
- `notes` that remain claims rather than hidden truth.

No field should silently write the current position of a Pokémon.

## Result semantics

A result can be represented as an observation claim with explicit scope.

Candidate semantic result kinds:

- `TARGET_SIGNAL_DETECTED`;
- `TARGET_SIGNAL_NOT_DETECTED`;
- `RESULT_INCONCLUSIVE`;
- `CONTROL_FAILURE`;
- `SAMPLE_INVALIDATED`;
- `REPEAT_REQUIRED`.

These are research/world semantics, not PTU statuses.

## Presence inference

Presence inference belongs in an interpretation layer rather than the raw result.

Candidate inference scope can preserve:

- species identity being considered;
- spatial area being inferred;
- time window;
- evidence references;
- alternative explanations;
- confidence state;
- author/analyst;
- revision lineage.

A high-confidence inference still does not create an entity or guarantee encounter availability.

## Positive result handling

A positive result may justify:

- repeat sampling;
- broader upstream/downstream sampling;
- field observation;
- temporary monitoring;
- a bounded access or works decision;
- publication with uncertainty;
- archive update.

It does not automatically justify:

- exact source location;
- exact individual identity;
- a count;
- capture authority;
- hostility;
- encounter spawn;
- habitat ownership;
- breeding-status claims.

## Negative result handling

A negative result is evidence about one sample under one protocol and context.

It may weaken a presence hypothesis. It cannot by itself erase prior positive results, direct sightings or historical records.

Repeated negatives can strengthen an inference only through an explicit interpretation step that preserves sampling scope and conditions.

## Transport and persistence boundary

Environmental transport may be authored as world state without fluid simulation.

Example authored facts:

- material from feature A can reach feature B during a defined hydrologic state;
- sediment at feature C can retain old material longer than the water column;
- a high-flow event can resuspend stored material;
- a side channel can become disconnected between scenes.

These facts inform evidence interpretation. They do not create tactical water mechanics unless separately admitted by AutoPTU capability evidence.

## Custody and archive boundary

Sample custody is explicit world history.

A sample can be collected correctly, transferred, delayed, mislabeled, invalidated, retested or archived. Each event remains queryable.

Archive lookup can provide external evidence to an NPC. It does not rewrite that NPC's personal memory.

## Communication and publication boundary

Laboratory completion, analyst interpretation, institutional notice and public publication are separate events.

The existing global NPC communication architecture remains authoritative for delivery and receipt.

A public statement such as “species detected in the district” may be a legitimate summary with lower spatial precision than the underlying sample. It must retain lineage to the interpretation that produced it.

A later correction or narrowing is a new publication event. Earlier recipients do not automatically receive the new version.

## World-agent AI use

The global planner may reason over evidence available to each actor and produce intents such as:

- collect repeat sample;
- deliver sample;
- request raw results;
- compare sample batches;
- inspect collection feature;
- interview local observer;
- review historical records;
- publish bounded notice;
- issue correction;
- defer a stronger conclusion;
- request AutoPTU for a tactical interruption.

It may not read hidden species occupancy unless that actor has legitimate evidence granting the claim.

## Battle handoff

Sample collection and ecological inference remain world-level systems.

If a tactical interruption occurs, Ouros sends only battle-relevant state through the existing AutoPTU handoff. AutoPTU does not decide sample meaning or ecological source truth.

Allowed reduced example:

A wild confrontation blocks access to a sampling feature. AutoPTU resolves an ordinary audited battle. The world can record immediate safe access after battle if supported by the encounter contract. It cannot record “species source confirmed” merely because a Pokémon appeared in combat.

## Reduced implementation profile

Safe reduced version:

- authored sample collection events;
- unique sample IDs;
- explicit custody;
- delayed analysis;
- positive/negative/inconclusive result events;
- explicit analyst interpretation;
- explicit recipient delivery;
- publication/revision lineage;
- repeat sampling;
- direct field observations;
- feature-scoped decisions;
- ordinary audited targeting, base movement, calculations, action economy/initiative and legal-action infrastructure if combat is required.

No live eDNA simulation is required.

## Full encounter dependency matrix

### targeting / footprints / range / LoS

Ordinary audited use: VERIFIED within existing engine contracts.

Rich dependency: concealment by vegetation, spray, darkness or sensor-assisted acquisition requires specific evidence beyond ordinary LoS.

### base movement legality

Ordinary audited use: VERIFIED.

Rich dependency: wading, swimming, climbing, squeezing or specialized bank traversal is not inferred.

### complete movement including push / pull / knockback / interception / forced movement

Rating dependency: PARTIAL.

Needed for rescue, interception, current-driven movement, forced displacement or unstable-edge interactions.

### core calculations

Ordinary audited deterministic combat math: VERIFIED.

Sample confidence, assay interpretation and transport inference are world/research semantics rather than combat calculations.

### action economy / initiative

Ordinary audited primitives: VERIFIED.

### full turn / round lifecycle

Rating dependency: PARTIAL.

Needed for timed sampling windows, delayed water changes, recurring weather or environmental scheduling during battle.

### full stateful damage pipeline

Rating dependency: PARTIAL.

Needed for falls, debris, current impact or other environmental damage.

### status lifecycle

Rating dependency: PARTIAL.

Needed for any persistent tactical exposure or condition. This contract defines no contamination, wetness, tracking or research status.

### terrain / weather / hazards / zones / reactions

Rating dependency: MIXED / PARTIAL / BLOCKING by subfamily.

Needed for dynamic water edges, rain, unstable banks, protected zones, reactive environmental effects or hazards.

### move-specific behavior

Rating dependency: PARTIAL.

Every Move used for sensing, concealment, terrain change, displacement, rescue or sample/equipment interaction requires individual verification.

### abilities

Rating dependency: PARTIAL.

Species flavor never grants environmental detection or eDNA authority.

### items

Rating dependency: PARTIAL.

Field samplers, filters, laboratory gear or protective equipment do not receive tactical behavior unless authoritative rules and implementation evidence support it.

### Trainer Features / perks

Rating dependency: PARTIAL.

Researcher or other Trainer Features require individual authoritative validation and engine coverage.

### AI legal-action infrastructure

Ordinary audited infrastructure: VERIFIED.

### AI tactical policy

General rich observation/protect-equipment/rescue/non-defeat policy: BLOCKING.

### Minecraft / Cobblemon / Craftics adapter/playback

Rating dependency: PARTIAL / BLOCKING end-to-end.

The adapter may render sample stations, researchers, Pokémon and result-driven world changes. It may not infer ecological occupancy from spawned entities, create laboratory results or duplicate PTU tactical resolution.

## PTU / Caelo / Kairos boundary

The inspected source inventory exposes `sources/kairos/KAIROS_SOURCE_INDEX.md` as comparative routing material. It points toward Researcher and other utility classes, ecosystem guidance, movement, hazards and terrain/weather in the supplied Kairos compilation while explicitly warning that Kairos is not automatic Ouros law.

No adopted `sources/caelo` rules source was visible during Pass 332.

Before any mechanical implementation, verify authoritative project rules for Researcher/Skills, field sampling, sensing, movement, water, weather, Moves, Abilities, Items and Trainer Features.

## Canon boundary

This contract defines architecture only. It does not establish a laboratory, assay technology, species, waterway, institution, settlement, ecological connection or quest outcome in Ouros canon.
