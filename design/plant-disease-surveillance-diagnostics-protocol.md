# Plant Disease Surveillance & Diagnostics Protocol — Pass 159

Status: PROPOSED SYSTEMS EXTENSION. Not canon.

Authority note: this protocol does not replace Flora/Agriculture, IPM, fungal ecology, Soil, Irrigation, Toxicology, Biosecurity, Science, Metrology, Botanical Gardens, Food Safety or Research Ethics. It owns the evidence chain used when plant decline must be investigated across those authorities.

## Purpose

Plant symptoms are often non-specific. Ouros needs to preserve what was observed before deciding what caused it.

Use this chain:

`plant/site state -> symptom/sign observation -> survey effort -> sample provenance -> diagnostic hypothesis -> test/result -> scoped diagnosis assessment -> intervention handoff -> follow-up`

Do not collapse this into `sick_plant = pathogen`.

## 1. Plant health case

```yaml
plant_health_case:
  case_id: null
  plant_or_population_refs: []
  site_ref: null
  opened_at: null
  symptom_observation_refs: []
  sign_observation_refs: []
  survey_refs: []
  sample_refs: []
  hypothesis_refs: []
  assessment_refs: []
  intervention_refs: []
  followup_refs: []
  case_state: OPEN
  provenance_refs: []
```

Suggested case states:

- OPEN
- MONITORING
- DIAGNOSTIC_WORKUP
- CAUSE_PARTIALLY_RESOLVED
- CAUSE_RESOLVED_FOR_SCOPE
- MANAGEMENT_ACTIVE
- CLOSED_WITH_UNCERTAINTY
- CLOSED

Closing a case does not erase uncertainty or raw evidence.

## 2. Symptoms and signs

```yaml
plant_symptom_observation:
  observation_id: null
  host_ref: null
  site_ref: null
  observed_at: null
  observer_ref: null
  symptom_class: null
  affected_part: null
  spatial_pattern_ref: null
  severity_band: null
  progression_state: unknown
  image_or_sample_refs: []
  confidence: null
```

Possible symptom classes include discoloration, wilting, dieback, lesion, deformity, reduced growth, premature drop, root decline, reproductive failure or unknown abnormality.

```yaml
plant_sign_observation:
  observation_id: null
  host_ref: null
  site_ref: null
  observed_at: null
  observer_ref: null
  sign_description: null
  candidate_organism_refs: []
  fungal_occurrence_ref: null
  sample_refs: []
  identification_state: UNRESOLVED
```

A symptom is a plant response. A sign is evidence of a candidate organism or process. Neither is a diagnosis by itself.

If the sign is fungal, Pass 72/158 remains the fungal-occurrence authority.

## 3. Surveillance and coverage

```yaml
plant_health_survey:
  survey_id: null
  program_ref: null
  target_scope: null
  site_or_route_refs: []
  started_at: null
  ended_at: null
  method_revision_ref: null
  effort_band: null
  host_coverage_ref: null
  spatial_coverage_ref: null
  season_context_ref: null
  weather_context_ref: null
  access_gaps: []
  observation_refs: []
  non_detection_scope: null
  quality_flags: []
```

Rules:

- `NOT_DETECTED` is scoped to survey design and method.
- absence claims require stronger evidence than a missed observation.
- a later better survey may change confidence without invalidating the earlier survey as a historical record.
- loaded Minecraft plant count is never survey coverage.

## 4. Sample provenance

```yaml
plant_diagnostic_sample:
  sample_id: null
  case_id: null
  source_host_ref: null
  source_location_ref: null
  collected_at: null
  collector_ref: null
  material_kind: null
  symptomatic_tissue_included: null
  healthy_margin_included: null
  collection_method_ref: null
  storage_condition_refs: []
  custody_refs: []
  laboratory_or_station_ref: null
  test_result_refs: []
  remaining_material_state: null
```

A sample result never floats free from its source plant, collection time and method.

Research Ethics owns invasive/restricted collection authorization. Museums/Botanical Gardens own later institutional collection custody where relevant.

## 5. Diagnostic tests

```yaml
diagnostic_test_result:
  test_result_id: null
  sample_id: null
  target_scope: null
  method_ref: null
  method_revision: null
  performed_at: null
  performed_by_ref: null
  result_state: null
  detection_limit_notes: []
  quality_control_refs: []
  uncertainty_notes: []
  supersedes_result_id: null
```

Suggested result states:

- DETECTED
- NOT_DETECTED
- INCONCLUSIVE
- INVALID
- MIXED_SIGNAL
- IDENTIFICATION_PENDING

`DETECTED` proves a detection under the recorded method. It does not automatically prove disease causation.

## 6. Diagnostic hypotheses

```yaml
plant_health_hypothesis:
  hypothesis_id: null
  case_id: null
  hypothesis_type: null
  candidate_cause_ref: null
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  unresolved_tests: []
  confidence: unknown
  state: OPEN
  reviewed_at: null
  supersedes_id: null
```

Candidate hypothesis families:

- INFECTIOUS_ORGANISM
- ARTHROPOD_OR_ANIMAL_PRESSURE
- WATER_DEFICIT_OR_EXCESS
- IRRIGATION_OR_SALINITY
- NUTRIENT_OR_SOIL_CONDITION
- TEMPERATURE_OR_WEATHER_INJURY
- AIR_QUALITY_OR_DEPOSITION
- TOXIC_OR_CHEMICAL_EXPOSURE
- ROOT_OR_PHYSICAL_DAMAGE
- CULTIVATION_OR_HANDLING
- MIXED_CAUSE
- UNKNOWN

Owning layers decide the underlying physical state. This protocol preserves the diagnostic reasoning.

## 7. Diagnosis assessment

```yaml
plant_diagnosis_assessment:
  assessment_id: null
  case_id: null
  scope_ref: null
  conclusion_ref: null
  conclusion_state: UNRESOLVED
  evidence_refs: []
  alternative_hypothesis_refs: []
  confidence: null
  reviewer_refs: []
  reviewed_at: null
  review_due_at: null
```

Suggested conclusion states:

- UNRESOLVED
- POSSIBLE
- PROBABLE
- SUPPORTED_FOR_SCOPE
- CONFIRMED_FOR_SCOPE
- RULED_OUT_FOR_SCOPE
- MIXED_CAUSATION_SUPPORTED

`FOR_SCOPE` matters. A confirmed diagnosis in one nursery batch does not automatically classify every plant in the valley.

## 8. Incidence and severity

Incidence and severity remain different observations.

```yaml
plant_health_extent_revision:
  revision_id: null
  case_id: null
  survey_ref: null
  incidence_band: null
  severity_band: null
  affected_area_ref: null
  host_scope_ref: null
  estimate_method_ref: null
  uncertainty_notes: []
```

A small number of severely affected plants and a large number of mildly affected plants are different situations.

Exact percentages are not required unless the campaign has adequate measurement support.

## 9. Intervention handoffs

This protocol may recommend a handoff. It does not execute other systems' powers.

Examples:

- altered irrigation -> Irrigation/Freshwater/Groundwater;
- crop-pressure management -> IPM;
- fungal occurrence management -> Pass 72/158 + relevant authority;
- movement/containment of material -> Biosecurity;
- chemical/toxic concern -> Toxicology;
- living collection hold -> Botanical Gardens;
- affected food lot -> Food Safety/Supply Chains;
- research sampling -> Research Ethics/Science;
- disposal or waste -> Waste/Sanitation.

```yaml
plant_health_intervention_ref:
  intervention_ref_id: null
  case_id: null
  owning_system_ref: null
  action_ref: null
  rationale_refs: []
  authorized_at: null
  followup_due_at: null
```

Treatment success can increase confidence in a hypothesis only when the intervention is sufficiently specific and alternative explanations are considered. It never retroactively rewrites the original uncertainty.

## 10. Follow-up

```yaml
plant_health_followup:
  followup_id: null
  case_id: null
  observed_at: null
  survey_or_observation_refs: []
  symptom_change_state: null
  new_sign_refs: []
  new_test_refs: []
  intervention_context_refs: []
  assessment_revision_ref: null
```

Recovery may be slow, partial, uneven or unrelated to the intervention. A plant can remain visibly damaged after the causal process has stopped.

## 11. Pokémon boundaries

Pokémon may be:

- observed near affected plants;
- confirmed feeding, digging, trampling or otherwise influencing the site;
- associated with a fungal occurrence;
- participating voluntarily in survey/work through Working Pokémon/Pokémon Agency;
- involved in an exact PTU battle mechanic during an independent confrontation.

Do not infer:

- species presence = disease source;
- Poison type = toxin source;
- Grass type = plant-health expertise;
- Bug type = pest;
- fungal-associated Pokémon = pathogen;
- Powder/Spore visual effect = environmental infection;
- healing Move = plant treatment;
- battle victory = diagnosis or quarantine authority.

## 12. PTU terminology collision: Blight

PTU has a concrete combat `Blight Condition` in specific rules material. Plant pathology also uses ordinary-language terms such as blight.

The world-state protocol must never map one to the other by name.

Use explicit IDs and namespaces:

- `plant_health_diagnosis:*`
- `ptu_condition:blight`

No string matching.

## 13. Minecraft projection

Minecraft may show:

- discolored leaves or crops;
- marked plots;
- sample stations;
- restricted greenhouse rows;
- pruning/removal work;
- diagnostic signage;
- seasonal recovery.

Minecraft may not decide:

- diagnosis;
- pathogen identity;
- causal attribution;
- survey coverage;
- sample result;
- plant mortality history;
- quarantine authority;
- PTU Status;
- ecological eradication;
- spawn changes.

Block replacement cannot cure a case. Chunk reload cannot reset it.

## 14. Encounter contracts

### Orchard Diagnostic Survey

FULL: researchers revisit an orchard where two symptom patterns overlap while resident wildlife may withdraw through the survey area.

Dependencies when used tactically:

- complete movement for researchers/wildlife crossing or withdrawal;
- AI tactical policy for `WITHDRAW`, `PROTECT_RESEARCHER`, `CLEAR_ROUTE` or `REACH_EXIT`;
- adapter/playback for survey points, civilians and world-state handoff;
- terrain/weather/hazards/zones/reactions only if the orchard itself has an exact verified tactical effect.

REDUCED: survey, sampling and wildlife movement resolve in world state. Any separate confrontation uses a static safe arena. Diagnosis continues afterward.

### Nursery Quarantine Transfer

FULL: staff move a documented batch through a controlled route while an independent wildlife conflict develops nearby.

Dependencies: complete movement, tactical AI and adapter/playback. Items are PARTIAL if any protective/handling equipment must have battle semantics.

REDUCED: material custody, staff movement and containment remain outside battle. AutoPTU handles only the independent static conflict.

### Forest Dieback Transect After Storm

FULL: a survey route crosses storm-damaged forest while technicians need protected access and resident Pokémon attempt to leave.

Dependencies: complete movement; terrain/weather/hazards/zones/reactions if debris/weather changes tactical state; tactical AI; adapter/playback.

REDUCED: close the unsafe transect, take samples at a safe edge, resolve movements outside combat and use a conventional static encounter only if necessary.

### Diagnostic Review Meeting

Non-combat by default. Science, Flora, Soil, Irrigation, IPM, fungi, Toxicology, Metrology and Biosecurity compare evidence. `UNRESOLVED` is a valid outcome.

## 15. Engine non-inferences

Current engine progress does not authorize:

- plant-disease Status;
- environmental Poisoned;
- ambient Spore/Sleep;
- infected-plant hazard zones;
- contagion between battlefield tiles;
- treatment Items not present in PTU;
- disease-driven terrain changes;
- AI diagnosis;
- Minecraft-side PTU rules.

If a concrete Move, Ability, Item, Status or Trainer Feature appears in an encounter, require evidence for that exact mechanic. Do not promote a whole capability family from one representative contract.

## 16. Canon gates

Ouros still needs authored decisions on:

- important crop/tree diseases or whether most remain generic;
- plant-health institutions and laboratories;
- quarantine or movement-control authority;
- diagnostic technology level by region;
- public versus sensitive plant-health records;
- important historic dieback events;
- whether any Pokémon have authored roles in diagnosis, survey or plant care;
- exact PTU/Caelo rules relevant to botanical work.

Until those decisions exist, cases remain proposed and evidence-scoped.