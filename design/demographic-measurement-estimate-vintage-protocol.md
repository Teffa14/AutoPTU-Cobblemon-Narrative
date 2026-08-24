# Demographic Measurement & Estimate Vintage Protocol

Status: PROPOSED EXTENSION to `design/demography-migration-population-change-layer.md`. Not a replacement layer and not established canon.
Pass: 149

## Purpose

Pass 60 owns population, residence, temporary presence, commuters, displacement and migration. This protocol adds only the measurement/versioning contract needed when several observations or publications describe that population differently.

## 1. Preserve four different objects

```text
raw observation
measurement/survey event
estimate revision
published demographic claim
```

A later estimate may reuse old observations, add new inputs or apply a new method. The old estimate remains historically queryable because NPCs may have made decisions from it.

## 2. Estimate revision

```yaml
population_estimate_revision:
  estimate_revision_id: null
  population_profile_id: null
  reference_time: null
  published_at: null
  geography_revision_id: null
  method_revision_id: null
  input_observation_ids: []
  estimate_value_or_band: null
  uncertainty: null
  coverage_notes: []
  supersedes_id: null
  publication_ref: null
```

Do not use more numeric precision than the evidence supports.

## 3. Method revision

```yaml
demographic_method_revision:
  method_revision_id: null
  institution_id: null
  method_name: null
  valid_from: null
  valid_to: null
  inclusion_scope: null
  exclusion_scope: null
  treatment_of_temporary_presence: null
  treatment_of_commuters: null
  treatment_of_displacement: null
  known_biases_or_limits: []
  provenance_refs: []
```

Method changes can explain a discontinuity without any real population jump.

## 4. Geography revision

```yaml
demographic_geography_revision:
  geography_revision_id: null
  settlement_or_zone_id: null
  boundary_ref: null
  valid_from: null
  valid_to: null
  changed_area_refs: []
  reason_ref: null
  provenance_refs: []
```

Two totals for “the same town” may refer to different boundaries. Land Tenure/Governance/Cartography own the authoritative boundary; this protocol records which revision an estimate used.

## 5. Coverage record

```yaml
survey_coverage_record:
  coverage_id: null
  survey_or_observation_id: null
  target_scope: null
  observed_scope: null
  inaccessible_scope: []
  missing_data_notes: []
  duplication_risk_notes: []
  temporary_absence_notes: []
  quality_state: null
```

Missing coverage increases uncertainty. It never creates an automatic population decline.

## 6. Historical query rules

Chronicle should support:

- “What population estimate was current on this date?”
- “What do we estimate now for that same historical date?”
- “Which boundary did that publication use?”
- “Which observations were unavailable when the old estimate was issued?”

Those questions may return different numbers without contradiction.

## 7. Actor privacy

Aggregate estimates should not expose actor-level residence histories unless another authority and privacy policy permits it. Published numbers must not become a backdoor for sensitive inference.

## 8. Minecraft boundary

Ambient NPC density may be generated from a population band, time of day and temporary-presence state. The reverse direction is forbidden: rendered or loaded NPC counts never update estimates.

## 9. Battle boundary

This protocol has no combat effects. Survey disputes, staged returns or temporary surges can lead to independent encounters, but demographic measurement remains world state.

No estimate may create morale, Initiative, Accuracy, terrain, wild-spawn or Trainer Feature modifiers.

## 10. Handoff to Pass 60

Pass 60 remains authoritative for population meaning and migration state. This protocol supplies `estimate_revision_id`, `method_revision_id`, `geography_revision_id` and `coverage_id` references that Pass 60 can attach to `population_profile`, `population_observation` and `published_population_claim` objects without duplicating their responsibilities.