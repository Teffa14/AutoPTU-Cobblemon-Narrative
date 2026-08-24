# Ouros Paleontology, Taphonomy & Fossil Localities Layer

Status: Proposed systems design. Not established canon.

## Purpose

This layer owns fossil evidence as geological-biological world state. It does not replace Archaeology, Geology, Taxonomy, Museums, Science, Research Ethics or Pokémon Agency.

The core problem is that a fossil is valuable because of both the physical specimen and the context in which it was found. Removing it can permanently destroy part of that context unless the world records locality, stratigraphy, orientation, matrix and associated evidence first.

## Core separation

Use this chain:

ancient organism/activity → preservation process → fossil-bearing context → field observation → locality/context record → collection/excavation → preparation → identification → taphonomic/stratigraphic interpretation → public interpretation → optional restoration handoff

Keep these states independent:
- physical fossil specimen;
- body versus trace fossil;
- exact locality;
- stratigraphic context;
- excavation context;
- preparation state;
- taxonomic determination;
- taphonomic hypothesis;
- paleoenvironment interpretation;
- museum collection state;
- public exhibit label;
- any living restored Pokémon.

## 1. Fossil locality

```yaml
fossil_locality:
  fossil_locality_id: null
  location_id: null
  parent_geologic_unit_id: null
  discovery_event_id: null
  coordinate_precision: null
  access_policy_refs: []
  exposure_type: null
  locality_revision_ids: []
  stratigraphic_section_ids: []
  fossil_occurrence_ids: []
  field_campaign_ids: []
  disturbance_event_ids: []
  current_condition: null
  sensitive_location: false
```

Possible exposure types:
- NATURAL_OUTCROP
- ROAD_CUT
- RIVER_BANK
- COASTAL_CLIFF
- CAVE
- MINE_OR_QUARRY
- CONSTRUCTION_EXPOSURE
- EROSION_WINDOW
- GLACIAL_EXPOSURE
- OTHER

A locality may remain scientifically important after the visible fossil has been removed.

## 2. Locality revision

```yaml
fossil_locality_revision:
  revision_id: null
  fossil_locality_id: null
  timestamp: null
  observed_extent: null
  exposed_surfaces: []
  obscured_surfaces: []
  erosion_state: null
  stabilization_state: null
  access_state: null
  mapping_refs: []
  supersedes_revision_id: null
```

Minecraft terrain changes can alter the projection, but the server-owned revision is authoritative.

## 3. Stratigraphic section

```yaml
stratigraphic_section:
  section_id: null
  fossil_locality_id: null
  measured_by_ids: []
  measurement_method: null
  reference_datum_id: null
  layer_ids: []
  correlation_claim_ids: []
  documentation_refs: []
  uncertainty_notes: []
```

Each layer should be independently addressable.

```yaml
stratigraphic_layer:
  layer_id: null
  section_id: null
  relative_position: null
  lithology_observations: []
  sedimentary_structure_observations: []
  thickness_observation: null
  fossil_occurrence_ids: []
  dating_claim_ids: []
  depositional_environment_claim_ids: []
```

Do not convert a layer label directly into an absolute date unless the relevant Geology/Science evidence exists.

## 4. Fossil occurrence

A fossil occurrence records a thing observed in context before removal.

```yaml
fossil_occurrence:
  occurrence_id: null
  fossil_locality_id: null
  layer_id: null
  observation_id: null
  fossil_kind: BODY|TRACE|OTHER
  field_description: null
  orientation_observation: null
  articulation_state: null
  completeness_observation: null
  matrix_description: null
  associated_occurrence_ids: []
  spatial_relationships: []
  extraction_state: IN_SITU
  specimen_id: null
  documentation_refs: []
```

A footprint, burrow, coprolite-like trace, trackway or feeding trace can be scientifically important without containing body material.

## 5. Fossil specimen identity

```yaml
fossil_specimen:
  specimen_id: null
  source_occurrence_id: null
  item_instance_id: null
  extraction_event_id: null
  current_custody_ref: null
  collection_link_id: null
  preparation_state: null
  preparation_event_ids: []
  identification_record_ids: []
  taphonomic_observation_ids: []
  imaging_refs: []
  sample_subdivision_ids: []
  current_condition: null
```

The specimen does not become a new object merely because matrix is removed or pieces are reassembled.

## 6. Field extraction event

```yaml
fossil_extraction_event:
  extraction_event_id: null
  occurrence_id: null
  actor_ids: []
  authorization_refs: []
  reason: null
  pre_extraction_documentation_refs: []
  stabilization_method: null
  removed_matrix_refs: []
  container_or_jacket_id: null
  custody_handoff_refs: []
  damage_observations: []
  timestamp: null
```

Extraction is not automatically the correct choice. Documentation-only or in-situ preservation may be preferable.

## 7. Preparation history

```yaml
fossil_preparation_event:
  preparation_event_id: null
  specimen_id: null
  actor_ids: []
  facility_id: null
  timestamp: null
  starting_state: null
  actions: []
  newly_exposed_features: []
  detached_fragment_ids: []
  consolidant_or_material_refs: []
  condition_changes: []
  imaging_before_refs: []
  imaging_after_refs: []
```

Preparation can reveal new anatomy and invalidate earlier identifications without making the original field notes false.

## 8. Identification and taxonomy handoff

```yaml
fossil_identification_record:
  identification_record_id: null
  specimen_or_occurrence_id: null
  proposed_taxon_ref: null
  determination_level: null
  evidence_refs: []
  comparator_refs: []
  confidence: null
  author_ids: []
  timestamp: null
  supersedes_record_id: null
```

Taxonomy owns accepted/revised classification. Paleontology owns the fossil-specific determination event and its context.

Do not create a new species/form mechanically because a fossil looks different.

## 9. Taphonomic observations and hypotheses

```yaml
taphonomic_observation:
  taphonomic_observation_id: null
  specimen_or_occurrence_id: null
  observation_type: null
  description: null
  imaging_refs: []
  measured_features: []
  timestamp: null
```

Candidate observation types:
- ARTICULATED
- DISARTICULATED
- ABRADED
- BROKEN
- WEATHERED
- SCAVENGE_MARK_LIKE
- TRANSPORT_ORIENTATION
- MINERAL_REPLACEMENT
- COMPRESSION
- IMPRESSION
- BORING_OR_BURROW_ASSOCIATION
- BURN_OR_HEAT_ALTERATION_LIKE
- OTHER

```yaml
taphonomic_hypothesis:
  hypothesis_id: null
  subject_ids: []
  proposition: null
  evidence_ids: []
  counterevidence_ids: []
  alternative_hypothesis_ids: []
  confidence: null
  current_status: PROPOSED
```

Do not use a single mark to declare predation, combat, wildfire, transport or cause of death.

## 10. Fossil assemblage

```yaml
fossil_assemblage:
  assemblage_id: null
  locality_id: null
  layer_ids: []
  occurrence_ids: []
  sampling_effort_refs: []
  preservation_bias_notes: []
  taxonomic_summary_refs: []
  paleoenvironment_claim_ids: []
```

An assemblage is evidence, not a direct census of an ancient ecosystem.

## 11. Paleoenvironment interpretation

```yaml
paleoenvironment_claim:
  claim_id: null
  locality_or_layer_ids: []
  proposition: null
  evidence_ids: []
  counterevidence_ids: []
  modern_analogue_refs: []
  climate_refs: []
  confidence: null
  author_ids: []
  revision_history: []
```

Possible claims can concern:
- ancient river/floodplain;
- lake;
- reef/coastal setting;
- forest;
- dryland;
- volcanic setting;
- cave;
- wetland;
- open marine environment.

These are Science/Geology interpretations, not automatic biome assignments.

## 12. Trace fossils and trackways

Trace fossils need persistent geometry.

```yaml
trace_fossil_feature:
  trace_feature_id: null
  occurrence_id: null
  feature_type: null
  mapped_geometry_ref: null
  sequence_order_claim: null
  maker_taxon_hypothesis_ids: []
  behavior_hypothesis_ids: []
  preservation_state: null
```

A trackway can support movement/behavior hypotheses without proving exact Speed, gait mechanics, group leadership or battle behavior.

## 13. Sensitive sites

Some localities should not expose exact coordinates publicly.

Reasons can include:
- active erosion;
- fragile trace fossils;
- excavation in progress;
- unauthorized collection risk;
- cultural overlap with Sacred Sites or Archaeology;
- nesting/current habitat above the fossil layer;
- research restrictions.

Use Research Ethics, Land Tenure and Conservation for access authority.

## 14. Restoration / revival boundary

A Fossil restoration system is not assumed to exist everywhere.

If future canon and PTU/Caelo rules authorize restoration:

```text
fossil specimen
  -> restoration authorization
  -> technical procedure
  -> result assessment
  -> living pokemon_entity_id
  -> Pokemon Agency / Care / Identity
```

The living Pokémon is never merely a museum object.

Do not infer:
- ownership from specimen custody;
- behavior from fossils alone;
- prehistoric environment tolerance from modern battle Type;
- restored Pokémon personality from reconstruction claims;
- perfect genetic identity with the extinct source population.

## 15. Minecraft projection

Minecraft may show:
- exposed fossil-like blocks;
- field grids;
- jackets/crates;
- preparation benches;
- display casts;
- marked protected surfaces;
- trackway geometry.

Minecraft must not decide:
- whether the object is scientifically a fossil;
- specimen identity;
- layer age;
- species determination;
- whether context was legally/documentationally preserved;
- whether the locality respawns fossils;
- restoration eligibility;
- excavation Skill checks.

Block destruction is not a valid fossil-acquisition transaction by itself.

## 16. Chronicle behavior

Routine work can compress:
- catalog updates;
- matrix preparation;
- photography;
- ordinary measurements;
- storage checks.

Expose detail when:
- a new locality appears;
- context is threatened;
- an identification changes;
- preparation reveals unexpected anatomy;
- two layers correlate differently than expected;
- a public exhibit conflicts with new evidence;
- a trace fossil changes behavioral interpretation;
- a restoration request creates an ethical/custody decision.

## 17. Cross-layer handoffs

Paleontology -> Geology: stratigraphy, dating, depositional context.

Paleontology -> Taxonomy: fossil determination/reclassification.

Paleontology -> Museums: accession, conservation, loans, exhibition.

Paleontology -> Science: hypothesis testing, paleoenvironment interpretation.

Paleontology -> Research Ethics: sampling/destructive analysis.

Paleontology -> Land Tenure/Conservation: access and site protection.

Paleontology -> Visual Records/Metrology: field imaging and measurement provenance.

Paleontology -> Pokémon Agency: only after a canon-authorized restoration produces a living Pokémon.

## 18. Mechanical guardrails

The narrative layer does not create:
- Paleontologist benefits;
- Pokémon Education/Survival checks;
- excavation DCs;
- fossil drop tables;
- restoration times/costs;
- revived Pokémon stats, Nature, Ability, Moves or Level;
- capture eligibility;
- cave-in/falling-rock damage;
- Rough Terrain from matrix/rubble;
- tool or equipment bonuses;
- ancient Ability/Move inference;
- Rock/Ground typing from sediment;
- custom fossil Items.

Project evidence currently lists `Paleontologist` as `missing_runtime_mapping`, so any mechanical benefit tied to that Edge/Feature remains under `Trainer Features/perks` and must be verified before use.

## 19. Implementation blockers outside battle core

`FOSSIL_LOCALITY_STATE`
Persistent locality and revisions.

`STRATIGRAPHIC_CONTEXT_STATE`
Layer identity, measured sections and correlations.

`FOSSIL_OCCURRENCE_LEDGER`
In-situ occurrence state before extraction.

`SPECIMEN_IDENTITY_AND_CUSTODY`
Persistent specimen identity through field, preparation and collections.

`TAPHONOMY_EVIDENCE_GRAPH`
Observations and competing hypotheses.

`ASSEMBLAGE_AND_SAMPLING_STATE`
Preservation/sampling bias separated from population inference.

`PALEOENVIRONMENT_INTERPRETATION_STATE`
Evidence-backed ancient-environment claims.

`FOSSIL_TO_MUSEUM_HANDOFF`
Accession/conservation without losing field provenance.

`FOSSIL_TO_LIVING_POKEMON_HANDOFF`
Only if restoration is explicitly canon/rules-authorized.

`PALEONTOLOGY_TO_MINECRAFT_PROJECTION`
Visible excavation without turning blocks into rules authority.

## 20. Canon questions left open

- Which regions of Ouros expose fossil-bearing formations?
- Which extinct Pokémon or ancient organisms are known before play begins?
- Does Ouros use Fossil restoration, and how rare/regulated is it?
- Which institutions conduct field paleontology?
- Who can authorize excavation or destructive sampling?
- Which localities are public versus restricted?
- How much geological time/stratigraphy is authored versus procedurally generated?
- How does Caelo modify Paleontologist, fossil discovery or restoration?
- What exact PTU mechanics govern Fossil revival and resulting Pokémon state?

No Caelo-specific answer was recovered reliably during this pass. Super PTU Online Helper was not exposed as an invocable capability.