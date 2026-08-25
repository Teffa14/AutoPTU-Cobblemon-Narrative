# Fungal Fruiting, Survey & Harvest Monitoring Protocol — Pass 158

Status: PROPOSED SYSTEMS EXTENSION. Not canon.

Authority note: `design/decomposition-fungi-deadwood-nutrient-cycling-layer.md` from Pass 72 remains the authority for fungal occurrence, root/fungal associations, decomposer activity and deadwood/nutrient-cycling state. Pass 158 adds only a deeper evidence protocol for repeated fungal surveys, fruiting episodes, detectability, occurrence linkage, sampling and harvest pressure. It does not create a second fungal ecology authority.

## Purpose

Pass 72 already establishes the key rule that visible fruiting is evidence rather than the whole fungal organism. This protocol makes that principle operational across multiple seasons and institutions.

Use this evidence chain:

`survey design -> survey effort -> occurrence observation -> fruiting episode revision -> sample/identification -> occurrence-linkage assessment -> longitudinal interpretation -> optional harvest/management review`

## 1. Fungal monitoring series

```yaml
fungal_monitoring_series:
  series_id: null
  location_or_system_ref: null
  target_scope_refs: []
  objective: null
  method_revision_refs: []
  station_or_plot_refs: []
  active_from: null
  active_to: null
  survey_event_refs: []
  source_refs: []
```

A monitoring series can target one known fungal occurrence, a substrate class, a root association, a habitat plot or a broader survey question.

## 2. Survey effort and detectability

Extend Pass 72's `decomposition_observation` and `fungal_occurrence_record` with explicit survey context when absence/presence comparisons matter.

```yaml
fungal_survey_event:
  survey_event_id: null
  series_id: null
  observed_at: null
  observer_refs: []
  method_ref: null
  spatial_coverage_ref: null
  substrate_coverage_refs: []
  duration_or_effort_band: null
  belowground_sampling_included: false
  weather_context_ref: null
  season_context_ref: null
  access_limitations: []
  detections: []
  non_detection_scope: null
  quality_flags: []
```

`NO_FRUITING_BODY_DETECTED` is never equivalent to `FUNGUS_ABSENT`.

A repeated survey can still remain method-limited or season-limited.

## 3. Fruiting episode extension

```yaml
fungal_fruiting_episode:
  fruiting_episode_id: null
  fungal_occurrence_refs: []
  first_detected_at: null
  last_detected_at: null
  spatial_extent_ref: null
  abundance_band: null
  developmental_state_refs: []
  survey_event_refs: []
  substrate_state_refs: []
  weather_or_hydrology_context_refs: []
  disturbance_context_refs: []
  interpretation_refs: []
  confidence: null
```

A fruiting episode describes visible reproductive structures during a window. It does not create or destroy the underlying fungal occurrence.

## 4. Occurrence-linkage assessment

Pass 72 permits multiple fungal occurrence records. Pass 158 adds a way to assess whether observations from different places/times may refer to the same persistent system.

```yaml
fungal_occurrence_linkage_assessment:
  assessment_id: null
  occurrence_refs: []
  relationship_state: UNRESOLVED
  evidence_refs: []
  alternative_explanations: []
  confidence: null
  reviewed_at: null
  supersedes_assessment_id: null
```

Candidate states:

- CONFIRMED_DISTINCT
- LIKELY_DISTINCT
- UNRESOLVED
- POSSIBLE_SAME_SYSTEM
- LIKELY_SAME_SYSTEM
- CONFIRMED_SAME_SYSTEM

Do not infer one giant underground organism from visual continuity alone.

## 5. Sampling and provenance extension

```yaml
fungal_sample_record:
  sample_id: null
  source_occurrence_ref: null
  source_observation_ref: null
  survey_event_ref: null
  collected_at: null
  location_ref: null
  substrate_or_host_ref: null
  material_kind: null
  collection_method_ref: null
  authorization_ref: null
  custody_refs: []
  analysis_refs: []
  remaining_material_state: null
```

Taxonomy owns formal identification/nomenclature. Research Ethics owns intrusive/regulated sampling. Museums/Botanical Gardens may own later collection custody.

A revised identification never rewrites the original sampling location or date.

## 6. Spore observation boundary

```yaml
fungal_spore_observation:
  spore_observation_id: null
  candidate_occurrence_refs: []
  observed_at: null
  location_ref: null
  method_ref: null
  medium_ref: null
  abundance_band: null
  identity_claim_refs: []
  later_growth_refs: []
  confidence: null
```

This is ecological evidence only.

Never map ambient or sampled spores to PTU `Spore`, `Effect Spore`, Sleep, Poisoned or Paralysis without the exact battle rule and runtime contract.

## 7. Harvest monitoring extension

Pass 72 already connects fungi with world ecology. Pass 158 adds a specific observation object for repeated collection pressure when wild mushrooms matter culturally, scientifically or commercially.

```yaml
fungal_harvest_record:
  harvest_record_id: null
  occurrence_or_area_ref: null
  occurred_at: null
  actor_or_group_refs: []
  quantity_band: null
  material_description_ref: null
  authorization_ref: null
  purpose_claim: null
  destination_refs: []
  survey_context_refs: []
  later_observation_refs: []
```

A harvest record proves removal, not population decline.

Market stock does not prove local abundance. A weak fruiting year does not prove overharvest. A closure does not prove depletion.

## 8. PTU mushroom item handoff

PTU contains concrete Mushroom Items and identification rules in the project source corpus. This protocol does not replace them.

Allowed handoff:

`world object/sample candidate -> exact PTU identification/acquisition rule -> authoritative Item state`.

Forbidden handoff:

`Minecraft mushroom block broken -> PTU Mushroom Item granted`.

## 9. Pokémon-associated fungal observations

Species such as Paras/Parasect, Shiinotic and Amoonguss can justify authored ecological observations. Pass 72 remains the fungal occurrence authority; Pokémon Agency remains the individual Pokémon authority.

A Pokémon association record may reference:

- the `pokemon_entity_id`;
- the fungal occurrence;
- observed behavior;
- species-source basis;
- later observations.

It must not replace Moves, Abilities, Status, HP, capture state or agency.

## 10. Minecraft projection

Minecraft may show fruiting bodies, sample markers, retained logs, seasonal visual changes and visitor closures.

Minecraft may not determine:

- fungal identity;
- occurrence linkage;
- fruiting history;
- abundance;
- taxonomic determination;
- edibility;
- toxicity;
- PTU Item identity;
- Status effects;
- spawn changes.

## 11. Encounter contracts

### Fruiting Chamber Survey

FULL: a cave monitoring site produces an unusual fruiting episode after hydrological change while resident Pokémon react to disturbance.

The version only uses environmental spores, darkness or substrate hazards if exact PTU/engine contracts exist. It may require complete movement, environmental family, tactical AI and adapter/playback.

REDUCED: sampling and exposure decisions happen in world state. Researchers leave. Any remaining battle uses static safe geometry with no ambient fungal Status mechanics.

### Deadwood Plot Disturbance

FULL: staff need visitors and wildlife to withdraw from a research plot during a short fruiting window. Complete movement, tactical AI and adapter/playback are the principal blockers.

REDUCED: crowd/wildlife movement resolves outside battle. AutoPTU handles only an independent static confrontation.

### Orchard Root Association Survey

Primarily non-combat. Flora, Soil, Irrigation, IPM, Science, Metrology and Pass 72 fungal records compare competing explanations. A battle cannot establish causation.

### Harvest Closure Dispute

Primarily non-combat. Monitoring series, harvest records, Land Tenure, Markets, Public Memory and Science support the decision. The outcome may remain uncertain.

## 12. Non-inferences

Do not infer:

- visible mushrooms = full fungal organism;
- no visible fruiting = absence;
- fruiting-body count = fungal population size;
- spores = PTU Spore Move;
- touching a mushroom = Effect Spore;
- mycorrhizae = mechanical buff;
- decomposition fungi = structural failure;
- market abundance = local ecological abundance;
- harvest = PTU Item acquisition;
- fungal patch = Rough Terrain or hazard;
- Minecraft particles = powder Move geometry.

## 13. Canon gates

Ouros still needs authored decisions on important fungal sites, foraging traditions, institutions, protected systems, sampling technology and any real fungal hazards. Exact mushroom Items, powder/Spore Moves and Abilities remain downstream PTU/Caelo/runtime questions.
