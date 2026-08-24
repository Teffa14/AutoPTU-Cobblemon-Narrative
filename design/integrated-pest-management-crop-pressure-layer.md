# Ouros Integrated Pest Management & Crop Pressure Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

This layer owns agricultural pest-management decisions after Food/Agriculture establishes a managed site or resource and before any intervention writes consequences into Ecology, Toxicology, Biosecurity or Food Safety.

It exists because crop damage, organism presence, causal attribution and management action are different facts.

The design target is a believable agricultural world where farms can have recurring ecological problems without turning every wild Pokémon into an enemy, every field into a battle map or every sighting into a quest.

## Core separation

Preserve this chain:

physical crop/site state -> observed damage or pressure -> candidate cause -> scoped management assessment -> monitoring -> action threshold -> intervention decision -> intervention event -> follow-up -> ecological/agricultural consequence

Never collapse the chain into `pest_seen = problem_solved_by_removal`.

## Pest is a scoped management label

`PEST` must never be stored as a permanent species property.

A management assessment is scoped to:

- location;
- managed resource or objective;
- time/season;
- evidence;
- severity;
- acceptable-loss or action threshold policy;
- reviewing institution or operator.

The same species may be harmful to an orchard during fruiting, neutral at the field edge and useful after harvest. A wild Pokémon may also be present at a damaged site without causing the damage.

```yaml
pest_management_assessment:
  assessment_id: null
  site_id: null
  managed_resource_ref: null
  cultivation_cycle_id: null
  candidate_actor_scope_ids: []
  observed_pressure_ids: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  management_label: UNDER_REVIEW
  confidence_band: unknown
  action_threshold_revision_id: null
  decision_state: MONITOR
  reviewed_at: null
  provenance_refs: []
```

Suggested management labels:

- UNDER_REVIEW
- NON_TARGET
- BENEFICIAL_OR_NEUTRAL
- PRESSURE_SOURCE_CONFIRMED
- PRESSURE_SOURCE_SUSPECTED
- INCIDENTAL_PRESENCE
- MANAGEMENT_TARGET

These labels are local management states. They are not taxonomy, disposition, morality or PTU mechanics.

## Damage observations

Agricultural damage should be observed before it is explained.

```yaml
crop_pressure_observation:
  observation_id: null
  site_id: null
  resource_ref: null
  location_scope: null
  observed_at: null
  observer_id: null
  observation_method: null
  pressure_type: null
  severity_band: null
  affected_fraction_band: null
  sample_or_image_refs: []
  candidate_cause_ids: []
  direct_cause_observed: false
  uncertainty_notes: []
```

Candidate pressure types:

- fruit or seed removal;
- leaf feeding;
- root disturbance;
- stem damage;
- sap feeding;
- nest/burrow interference;
- trampling;
- contamination claim;
- storage loss;
- pollination disruption claim;
- unknown loss.

A missing crop can have other causes: harvest error, weather, disease, irrigation failure, theft, spoilage, wildlife or bad records. Those alternatives remain open until evidence narrows them.

## Scouting and monitoring

One sighting is evidence of one sighting.

```yaml
scouting_event:
  scouting_event_id: null
  program_id: null
  site_id: null
  method: null
  route_or_plot_ids: []
  started_at: null
  completed_at: null
  effort_state: null
  observation_ids: []
  weather_context_id: null
  crop_stage_ref: null
  detection_limit_notes: []
  coverage_gaps: []
```

Possible methods include visual transects, traps that do not mechanically capture Pokémon, cameras, field signs, damage sampling, interviews with workers and repeated fixed-point observations.

The world must preserve effort. `NOT_DETECTED` never equals `ABSENT` without appropriate evidence.

## Action thresholds

Ouros should avoid calendar-driven automatic intervention.

```yaml
action_threshold_revision:
  threshold_revision_id: null
  program_id: null
  effective_from: null
  target_scope: null
  crop_or_resource_stage: null
  evidence_requirements: []
  pressure_band_trigger: null
  exceptions: []
  rationale_refs: []
  supersedes_id: null
```

A threshold can change when:

- cultivation stage changes;
- the site objective changes;
- better monitoring exists;
- non-target effects become known;
- a new ecological relation is discovered;
- prior interventions performed poorly;
- climate/seasonality shifts the baseline.

Thresholds do not create exact crop-loss numbers unless the project later authors a quantitative agricultural economy.

## Intervention records

Interventions are world-state actions with provenance.

```yaml
management_intervention:
  intervention_id: null
  program_id: null
  assessment_id: null
  intervention_type: null
  target_scope: null
  start_at: null
  end_at: null
  actor_ids: []
  method_refs: []
  authorization_refs: []
  affected_area_ids: []
  expected_outcome_claims: []
  non_target_monitoring_ids: []
  followup_due_at: null
  outcome_state: PENDING
  downstream_case_ids: []
```

Candidate intervention types:

- SITE_SANITATION_OR_RESOURCE_REMOVAL
- PHYSICAL_EXCLUSION
- ROUTE_OR_ACCESS_CHANGE
- CROP_TIMING_OR_CULTURAL_CHANGE
- HABITAT_EDGE_MODIFICATION
- MANUAL_REMOVAL_NON_POKEMON
- COEXISTENCE_OR_DIVERSION
- BIOLOGICAL_CONTROL_PROPOSAL
- TRANSLOCATION_PROPOSAL
- CHEMICAL_CONTROL_PROPOSAL
- TEMPORARY_HOLD_OR_CLOSURE
- NO_ACTION_MONITOR_ONLY

`BIOLOGICAL_CONTROL_PROPOSAL` and `TRANSLOCATION_PROPOSAL` require Biosecurity/Conservation handoff before execution.

`CHEMICAL_CONTROL_PROPOSAL` requires an authored material plus Toxicology and relevant environmental authorities. This layer cannot create toxicity, status effects or contamination rules.

## Beneficial and non-target organisms

Managed landscapes contain organisms that are not management targets.

```yaml
non_target_observation:
  observation_id: null
  intervention_id: null
  actor_scope_id: null
  relation_to_site: unknown
  pre_intervention_state_ref: null
  post_intervention_state_ref: null
  possible_effect_claim_ids: []
  evidence_ids: []
```

A predator, pollinator, decomposer or scavenger may be useful in one context and create pressure in another. Interspecies Ecology owns the broader relationship.

Do not label all Bug-types as pests or all predators as biological control agents.

## Pokémon participation and agency

A wild Pokémon can be:

- observed near damage;
- confirmed performing a behavior that affects a crop;
- displaced by another event;
- diverted by changing resource access;
- part of a recurring coexistence arrangement;
- incidentally present;
- a participant in an institutional management role only through Working Pokémon/Pokémon Agency.

Management never grants ownership.

Capture is not a generic pest-management action. A battle result does not authorize relocation, custody or long-term ecological writeback.

## Resistance and adaptation

If repeated management appears less effective, store an open claim rather than procedural genetic resistance.

```yaml
management_effectiveness_review:
  review_id: null
  intervention_family: null
  prior_event_ids: []
  observed_outcome_ids: []
  effectiveness_trend: unknown
  resistance_hypothesis_id: null
  alternative_explanations: []
  review_state: OPEN
```

Alternative explanations may include weather, application failure, changed crop stage, immigration, altered habitat or monitoring changes.

No resistance stat is created.

## Post-intervention review

Every meaningful intervention should eventually answer:

- did the observed pressure change?
- did the target organism’s local use change?
- did the crop/site condition change?
- were there non-target observations?
- did another problem appear?
- was the original causal hypothesis strengthened or weakened?

`INTERVENTION_COMPLETED` is not `SUCCESS`.

## Cross-layer authority

Food/Agriculture: site, crop/resource, cultivation stage, harvest consequence.

Interspecies Ecology: predator/prey/resource relations and population-scale ecological pressure.

Flora/Soil: vegetation and land condition.

Biosecurity: introductions, translocation and biological-control release risk.

Toxicology/Air Quality/Freshwater/Soil: hazardous agents and environmental exposure.

Food Safety: downstream batches and food-service consequences.

Pokémon Agency/Working Pokémon: individual agency, custody, institutional participation.

Cases: theft, sabotage or wrongdoing only when evidence supports a case. A crop loss is not a crime by default.

## Minecraft projection

Minecraft/Cobblemon is presentation, not agricultural truth.

Never infer:

- loaded wild entity count -> infestation size;
- crop blocks missing -> Pokémon damage;
- placing crops -> guaranteed pest spawn;
- killing/despawning entities -> pressure solved;
- fences/doors -> exclusion effectiveness without world-state revision;
- particles -> chemical exposure;
- a Pokémon standing in a field -> management target.

The server should project coarse signs such as damaged rows, monitoring flags, exclusion mesh, diversion feeding sites or closed plots from authoritative state.

## Encounter contracts

### Orchard Threshold Survey — FULL

Premise: repeated fruit loss has crossed the current monitoring threshold, but the cause is still disputed. Scouts need to complete transects while wild Pokémon move through orchard lanes.

Requires:

- complete movement for moving scouts/wildlife and protected lanes;
- AI tactical policy for WITHDRAW, CROSS, PROTECT_SCOUT and REACH_EXIT objectives;
- Minecraft/Cobblemon/Craftics adapter/playback;
- terrain/weather/hazards/zones/reactions only if orchard structures or environmental effects become tactical mechanics.

REDUCED: scouting and wildlife movement resolve in world state. If a confrontation remains, freeze a conventional orchard-edge arena and battle only actual combatants. The survey conclusion is written afterward from evidence, not from who won.

### Greenhouse Exclusion Breach — FULL

Premise: an exclusion barrier has failed and multiple organisms entered a greenhouse. Staff must secure propagation stock while distinguishing incidental visitors from the actual pressure source.

Requires complete movement, AI tactical policy and adapter/playback. Any broken-glass or chemical hazard requires the environmental family and exact validated rules.

REDUCED: staff secure samples and close unaffected compartments before battle. AutoPTU receives a dry static compartment with no invented glass, toxin or crop hazards.

### Beneficial Edge Conflict — FULL

Premise: a field-edge organism blamed for crop loss may actually be suppressing another pressure source. A rushed removal would destroy the evidence needed to resolve the relationship.

Requires complete movement and tactical AI if actors must withdraw/protect a monitoring point while avoiding unnecessary engagement, plus adapter/playback.

REDUCED: ecological actors are moved outside battle by world state. A static independent encounter may occur, but the ecological relation stays unresolved until monitoring data is reviewed.

### Threshold Review Meeting

No combat capability is inherently required. Operators compare scouting, crop state and ecological evidence and may legitimately decide `NO_ACTION_MONITOR_ONLY`.

## Mechanical non-inferences

This layer does not authorize:

- crop damage as HP damage;
- pest Pokémon as hostile AI by default;
- Bug-type vulnerability/resistance rules for agriculture;
- Sweet Scent as a spawn-control command;
- Bug Bite as automatic crop loss;
- Harvest/Honey Gather as field-yield simulation;
- Poison-type immunity to pesticides;
- pesticide narrative text as Poisoned/Badly Poisoned;
- a spray cloud as Weather/hazard;
- biological control as automatic predation AI;
- capture/KO as a permanent population-control result.

## Canon questions intentionally left open

- Which Ouros regions have managed agriculture at launch?
- Which crop pressures and beneficial associations are authored rather than procedural?
- Which institutions provide scouting or agricultural extension-like support?
- Can player businesses establish management programs and thresholds?
- Are any chemical controls present in canon at all?
- What translocation/biological-control practices are allowed?
- How much crop-loss detail should remain qualitative?
- Which exact PTU/Caelo rules, if any, apply to agricultural activities rather than battles?
