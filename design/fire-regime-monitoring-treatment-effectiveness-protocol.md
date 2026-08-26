# Fire-Regime Monitoring & Treatment-Effectiveness Protocol

Status: PROPOSED PROTOCOL EXTENSION. Not established Ouros canon.
Pass: 178
Date: 2026-08-26

Authority note: `wildfire-fire-ecology-landscape-recovery-layer.md` from Pass 64 remains the authoritative fire-ecology layer. This protocol only deepens monitoring provenance, treatment-effectiveness review, repeated-fire chronology and comparability across revisions. It must not create a second `fire_event`, `fire_scar`, `burn_patch`, `fire_regime_profile`, planned-fire authority or recovery authority.

## Scope

Pass 64 already owns ignition/cause hypotheses, active fronts, smoke, burn severity, refugia, fire regimes, planned fire, displacement, recovery and post-fire watershed coupling.

Pass 178 adds four narrower capabilities:

1. versioned monitoring series around existing Pass 64 fire objects;
2. explicit treatment objectives and later outcome assessment;
3. repeated-fire / reburn chronology without overwriting older scars;
4. comparability review when methods, maps or monitoring coverage change.

## Monitoring-series extension

```yaml
fire_monitoring_series:
  series_id: null
  pass64_fire_or_unit_refs: []
  purpose: null
  method_revision_ids: []
  station_or_plot_ids: []
  observation_windows: []
  baseline_refs: []
  post_event_refs: []
  coverage_notes: []
  comparability_assessment_ids: []
  responsible_institution_ids: []
```

A series can continue through multiple fires or planned treatments.

## Method revisions

```yaml
fire_monitoring_method_revision:
  method_revision_id: null
  valid_from: null
  valid_to: null
  measured_domains: []
  sampling_design: null
  instrument_refs: []
  spatial_resolution: null
  known_limitations: []
  predecessor_revision_id: null
```

Changing method does not invalidate the earlier data. It can reduce or alter comparability.

## Observation-event provenance

```yaml
fire_effect_observation:
  observation_id: null
  series_id: null
  observed_at: null
  location_ref: null
  domain: null
  method_revision_id: null
  raw_record_refs: []
  derived_product_refs: []
  field_validation_refs: []
  quality_state: null
  uncertainty_notes: []
```

Remote Sensing owns image acquisition and derived raster products. Photography owns image provenance. Flora, Soil, Water and Wildlife own their domain-specific ecological observations. This protocol only links them into a fire-monitoring series.

## Treatment objectives

Pass 64 `planned_fire_project.objective_ids` remains authoritative. Pass 178 adds versioned objective definitions so later reviews can determine what was actually being tested.

```yaml
fire_treatment_objective:
  objective_id: null
  project_id: null
  objective_type: null
  target_scope: null
  target_condition: null
  evaluation_method_refs: []
  decision_window: null
  uncertainty_notes: []
```

Possible descriptive objective types include fuel-pattern change, habitat-structure objective, invasive-plant objective, cultural-landscape objective or research objective. No real-world management threshold is copied into Ouros.

## Treatment outcome assessment

```yaml
fire_treatment_outcome_assessment:
  assessment_id: null
  project_id: null
  objective_id: null
  valid_as_of: null
  evidence_refs: []
  result_state: null
  tradeoff_refs: []
  unintended_effect_refs: []
  followup_recommendation_refs: []
  supersedes_assessment_id: null
```

Suggested result states:

- `TOO_EARLY_TO_ASSESS`
- `OBJECTIVE_SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `OBJECTIVE_NOT_SUPPORTED`
- `MIXED_OUTCOME`
- `INSUFFICIENT_EVIDENCE`
- `UNRESOLVED`

Operational completion is not one of these ecological conclusions.

## Reburn chronology

Pass 64 fire events and scars remain unchanged. Pass 178 can add explicit relationships between them.

```yaml
fire_history_overlap:
  relation_id: null
  earlier_fire_event_id: null
  later_fire_event_id: null
  overlap_geometry_ref: null
  interval_between_events: null
  pre_later_event_state_refs: []
  post_later_event_observation_refs: []
  interpretation_refs: []
```

The relation records overlap. It does not infer that the first fire caused the later severity, protected the patch or increased/decreased risk.

## Fire-regime assessment revisions

Pass 64 `fire_regime_profile` remains the authored regional expectation. Pass 178 can attach scientific revisions to the evidence behind that profile.

```yaml
fire_regime_evidence_review:
  review_id: null
  regime_id: null
  valid_as_of: null
  evidence_window: null
  fire_event_refs: []
  archive_refs: []
  remote_sensing_refs: []
  monitoring_series_refs: []
  interpretation_changes: []
  unresolved_gaps: []
```

A new review may change confidence in frequency, seasonality, severity pattern or spatial mosaic while leaving the authored regime profile untouched until canon authority chooses to revise it.

## Comparability assessment

```yaml
fire_series_comparability:
  assessment_id: null
  source_series_or_product_refs: []
  comparable_domains: []
  noncomparable_domains: []
  caveats: []
  correction_or_crosswalk_refs: []
  status: null
```

This is needed when:

- plot locations change;
- sensors or field protocols change;
- remote-sensing products are reprocessed;
- coverage improves;
- old records are digitized;
- boundaries of a management unit change.

## Fire-history interpretation rules

Preserve these distinctions:

- fire perimeter versus burn severity;
- severity versus recovery;
- treatment completed versus objective achieved;
- vegetation response versus wildlife response;
- public narrative versus scientific map;
- no observation versus no change;
- reburn overlap versus causal effect;
- planned area versus actual footprint;
- old severity map versus newer reprocessed map.

## Reduced implementation model

Pass 178 does not require a tactical wildfire simulator. Most monitoring and treatment-review scenes can resolve entirely in world state.

For combat-adjacent scenes:

1. Pass 64 and Crisis freeze the authoritative fire state;
2. researchers, civilians and background wildlife are moved outside battle authority;
3. hazardous fire/smoke/runoff effects remain narrative unless exact validated PTU mechanics exist;
4. AutoPTU resolves only the independent battle;
5. monitoring/review continues afterward.

## Minecraft boundary

Minecraft may display charred terrain, regrowth, monitoring plots, closures and treatment boundaries.

Minecraft never authors:

- monitoring success;
- treatment success;
- burn severity;
- regime revision;
- recovery state;
- reburn causality;
- fire spread history from vanilla block ticks.

## Canon questions left open

- Which Pass 64 fire regimes are eventually authored as Ouros canon?
- Which institutions operate monitoring networks?
- What methods and technology exist?
- Are planned burns used anywhere in Ouros?
- Which historic fire records exist before the campaign?
- Which treatment objectives are culturally legitimate in each region?
- Which PTU/Caelo environmental fire mechanics, if any, are part of the final ruleset?

Until answered, this protocol is infrastructure only.