# Vector Ecology & Vector-Borne Surveillance Protocol

Status: PROPOSED SYSTEM / NON-CANON
Pass: 172
Date: 2026-08-25

## Scope

This protocol owns vector-specific surveillance provenance: survey/trap effort, vector observations, pooled or individual vector samples, pathogen-test links, host-contact observations, transmission hypotheses and follow-up after interventions.

It does not own clinical diagnosis, outbreak truth, population truth, biosecurity origin, toxicology, environmental treatment, public-health authority, Pokémon ownership, capture permission or battle mechanics.

## Authority boundary

Authoritative handoff:

`surveillance question -> method/deployment -> actual effort -> vector observation/sample -> test result -> host-contact evidence -> transmission hypothesis -> Outbreak/Health handoff -> authorized intervention elsewhere -> follow-up surveillance`

Existing systems remain authoritative:

- Outbreak/Health Surveillance decides case definitions, surveillance cases, health hypotheses, diagnoses and control measures.
- Biosecurity decides origin, arrival pathway, establishment and spread of introduced populations.
- Community Science decides provenance and validation of public submissions.
- Taxonomy decides identification/classification.
- Metrology and Timekeeping decide instrument calibration and timestamp correction.
- Diel Activity and Seasonality decide temporal activity patterns.
- Urban Wildlife, Freshwater, Stormwater, Wetlands and other ecology layers own habitat state.
- Toxicology owns hazardous chemical exposure and decontamination.
- Research Ethics owns subject/site authorization and secondary use.
- Pokémon Agency owns persistent individual identity, custody and agency.

## Core records

### `VECTOR_SURVEILLANCE_PROGRAM`

Persistent programme identity.

Suggested fields:

- `program_id`
- `sponsoring_institution_ids`
- `surveillance_question`
- `target_vector_taxa_or_group`
- `target_pathogen_or_hazard_claim_optional`
- `geographic_scope`
- `start_date`
- `end_date_or_open`
- `method_revision_ids`
- `quality_policy_revision_id`
- `sample_policy_revision_id`
- `privacy_policy_revision_id`
- `handoff_authority_refs`
- `status`

The programme is allowed to monitor without establishing that a transmission cycle exists.

### `VECTOR_METHOD_REVISION`

Versioned collection or observation method.

Suggested fields:

- `method_revision_id`
- `method_family`: `TRAP|DRAG|FLAG|VISUAL_SEARCH|HOST_EXAMINATION|LARVAL_SURVEY|EGG_SURVEY|OTHER`
- `target_stage_or_behavior`
- `attractant_or_bait_if_any`
- `deployment_duration_spec`
- `placement_spec`
- `collection_interval_spec`
- `handling_spec`
- `known_selectivity_notes`
- `supersedes`

Changing method can break comparability even if the programme name remains unchanged.

### `VECTOR_DEPLOYMENT`

One trap, transect, drag, search station or other bounded field deployment.

Suggested fields:

- `deployment_id`
- `program_id`
- `method_revision_id`
- `location_id`
- `start_time_raw`
- `end_time_raw`
- `corrected_time_refs`
- `device_or_material_refs`
- `operator_refs`
- `environment_context_refs`
- `planned_effort`
- `actual_effort`
- `failure_or_interruption_refs`
- `retrieval_state`

Possible retrieval states:

- `COMPLETED`
- `PARTIAL`
- `DEVICE_LOST`
- `DEVICE_DAMAGED`
- `ACCESS_PREVENTED`
- `INVALID_FOR_METHOD`
- `UNRESOLVED`

### `VECTOR_OBSERVATION`

Observed specimen(s) or sign associated with documented effort.

Suggested fields:

- `observation_id`
- `deployment_id`
- `taxon_claim_ref`
- `life_stage_claim`
- `sex_claim_if_relevant`
- `count_claim_or_band`
- `condition_notes`
- `host_association_observed_optional`
- `media_refs`
- `specimen_refs`
- `quality_state`

A count from a selective trap is not automatically a population count.

### `VECTOR_SURVEY_COVERAGE_REVISION`

Describes where/when meaningful detection opportunity existed.

Dimensions may include:

- geography;
- habitat;
- time of day;
- season;
- life stage;
- method;
- access;
- weather;
- operator availability;
- trap loss/failure;
- target taxa.

Possible outcome language:

- `DETECTED`
- `NOT_DETECTED_WITH_DOCUMENTED_EFFORT`
- `NO_SURVEY_COVERAGE`
- `SAMPLING_INCOMPLETE`
- `METHOD_NOT_SUITABLE_FOR_TARGET`
- `UNRESOLVED`

Never infer absence from `NO_SURVEY_COVERAGE`.

### `VECTOR_POOL_SAMPLE`

A laboratory/sample object containing multiple field specimens.

Suggested fields:

- `pool_sample_id`
- `source_observation_ids`
- `source_deployment_ids`
- `taxon_scope`
- `life_stage_scope`
- `specimen_count`
- `pooling_method_revision_id`
- `collection_window`
- `collection_geography`
- `custody_refs`
- `storage_condition_refs`
- `lab_submission_ref`

A pool intentionally sacrifices individual attribution. Preserve that uncertainty.

### `VECTOR_PATHOGEN_TEST_RESULT`

Scoped analytical result.

Suggested fields:

- `test_result_id`
- `sample_id`
- `target_claim`
- `test_method_revision_id`
- `performed_at`
- `laboratory_ref`
- `result`: `DETECTED|NOT_DETECTED|INCONCLUSIVE|INVALID|PENDING`
- `quality_control_refs`
- `confirmatory_test_refs`
- `revision_parent_optional`

`DETECTED` means detected in the tested sample under the method. It does not identify which member of a pooled sample carried the target.

### `VECTOR_INDEX_OR_ESTIMATE_REVISION`

Optional derived surveillance product.

Use only when a programme actually has a defined method.

Suggested fields:

- `estimate_revision_id`
- `metric_definition_revision_id`
- `input_deployment_ids`
- `input_sample_ids`
- `time_window`
- `geographic_scope`
- `taxon_scope`
- `estimate_or_band`
- `uncertainty`
- `comparability_notes`
- `supersedes`

No universal “vector risk score” is defined by this protocol.

### `HOST_CONTACT_OBSERVATION`

Evidence of physical contact or a plausible contact opportunity.

Suggested fields:

- `contact_observation_id`
- `vector_or_taxon_ref`
- `host_ref_or_host_class`
- `time_window`
- `location_ref`
- `contact_type_claim`
- `directly_observed`
- `evidence_refs`
- `confidence`

Examples may include feeding, attachment, repeated approach or shared microhabitat when actually observed.

Contact is not transmission.

### `VECTOR_TRANSMISSION_HYPOTHESIS`

A scientific hypothesis, never direct world truth.

Suggested fields:

- `hypothesis_id`
- `vector_taxon_or_population_ref`
- `pathogen_or_agent_claim`
- `host_scope`
- `geographic_scope`
- `time_window`
- `supporting_vector_evidence_refs`
- `supporting_host_contact_refs`
- `supporting_health_refs`
- `contradicting_evidence_refs`
- `status`: `OPEN|SUPPORTED|WEAKENED|REJECTED|UNRESOLVED`
- `last_reviewed_at`

No species becomes globally tagged `VECTOR=true` because one local hypothesis is supported.

### `VECTOR_INTERVENTION_HANDOFF`

Request/recommendation passed to the authority that can actually act.

Possible destination authorities:

- Outbreak/Health;
- Water/Stormwater;
- IPM/Agriculture;
- Biosecurity;
- Conservation;
- Public Works;
- Waste/Sanitation;
- Land Tenure;
- Institutional Review;
- Toxicology if a chemical intervention is proposed.

Suggested fields:

- `handoff_id`
- `evidence_refs`
- `proposed_scope`
- `proposed_action_class`
- `destination_authority`
- `status`
- `decision_ref_optional`

Surveillance cannot authorize its own intervention merely because it detected a vector.

### `VECTOR_FOLLOWUP_ASSESSMENT`

Versioned evaluation after an action or environmental change.

Suggested dimensions:

- comparable effort available?;
- vector detections changed?;
- pathogen detections changed?;
- host-contact observations changed?;
- health cases changed?;
- non-target effects observed?;
- alternative explanations remain?;
- monitoring should continue?;

Lower trap counts alone do not establish intervention success.

## Evidence logic

The protocol must preserve these non-equivalences:

`vector present != pathogen present`

`pathogen detected in vector pool != every vector positive`

`pathogen-positive vector != host contacted`

`host contact != transmission`

`transmission != infection confirmed`

`infection != symptoms`

`symptoms != vector-borne cause`

`no trap detections != vector absent`

`fewer loaded entities != successful control`

## Pokémon-specific guardrails

A Pokémon can have authored feeding, biting, attachment or blood-feeding behavior without being a disease vector.

Do not infer vector competence from:

- Bug type;
- Poison type;
- biting Moves;
- Leech Life;
- Poison Fang;
- Toxic;
- blood-feeding Pokédex flavor;
- cave/urban habitat;
- contact with another Pokémon;
- an observed PTU Status.

A Poison-type Pokémon is never presumed contaminated, infectious or culpable because of type.

## PTU mechanical boundary

The project corpus confirms skills such as Medicine Education, Pokémon Education, Survival and Perception exist.

Pass 172 does not define:

- trapping DCs;
- pathogen-identification DCs;
- epidemiology DCs;
- treatment rolls;
- bite-to-infection chances;
- disease Status Conditions;
- immunity from Type;
- vector-control Moves;
- lab equipment bonuses.

If a battle uses an exact PTU Move, Ability, Item, Status or Trainer Feature, the relevant engine family remains required and must be supported by current parity evidence.

## Minecraft/Cobblemon boundary

Minecraft is presentation and interaction, not surveillance authority.

Do not infer:

- loaded entity count -> abundance;
- despawn -> mortality/control;
- captured/KO entities -> reduced vector population;
- trap block contents -> scientific result;
- particle effects -> infection;
- biome tag -> vector status;
- bite animation -> transmission;
- chunk unload -> absence;
- Poison/Bug spawn density -> health risk.

World state may project coarse visual conditions after authoritative surveillance decisions.

## Longitudinal Chronicle hooks

This protocol becomes valuable over years when:

- trap methods change;
- urban drainage changes;
- wetlands expand or contract;
- winters become warmer/colder;
- public reporting improves;
- a suspected vector is exonerated;
- pathogen detections appear before health cases;
- health cases occur without positive vector samples;
- intervention changes one metric but not another;
- an old pooled sample is retested with a later method.

The world should be able to revise its interpretation without rewriting the original observations.

## Canon posture

Pass 172 establishes no canonical vector species, pathogen, disease cycle, intervention programme, laboratory, endemic region or public-health authority.

Everything remains proposed until separately canon-approved.