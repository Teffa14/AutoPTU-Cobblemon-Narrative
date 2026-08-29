# Ouros Crop & Plant Health Surveillance, Response and Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Pass: 129

## Purpose

Ouros already tracks agricultural sites, cultivation cycles, harvests, water dependencies, weather, pollution, ecology, conservation, batches and persistent Pokémon identity. This extension adds the missing continuity between a plant-condition report and later recovery:

observation → bounded investigation → sample/diagnostic evidence → affected-scope revision → response/handoff → follow-up → recovery or unresolved closure.

The layer is intentionally narrow. It does not create a universal crop-disease simulator, regulator, pest list, quarantine law, pesticide system or PTU environmental mechanic.

## Authority boundaries

This extension owns:

- persistent plant-health episodes;
- field observations scoped to plant/row/block/site;
- survey purpose and coverage;
- samples and diagnostic provenance when such capability exists;
- competing cause hypotheses;
- affected-scope revisions;
- plant-health actions as records of what actors actually did;
- follow-up observations;
- recovery checkpoints;
- handoffs to systems that own the actual cause or downstream consequence.

Other systems retain authority:

- Food/Agriculture: agricultural-site identity, cultivation cycle, harvest and ordinary farm operation;
- Material Culture: item/material identity;
- Water Management / Drinking Water / Drought: water-source and allocation truth;
- Weather: observations and forecasts;
- Pollution / Air Quality / Wastewater: pollution and environmental-release truth;
- Ecology / Conservation: wild-population, habitat and stewardship truth;
- Settlement–Wild Pokémon Coexistence: reports and mitigation involving wild Pokémon in settlements/managed edges;
- Pokémon Agency / Work Roles: individual Pokémon identity, partnership and documented work role;
- Batch Traceability: distributed or post-production product/batch problem lifecycle;
- Science: research programmes, laboratories and discovery authority where established;
- Care / Community Health: human or Pokémon health consequences;
- Civic Governance / Adjudication / Case: institutional mandates, contested decisions and formal evidence processes;
- AutoPTU/PTU/Caelo: battle mechanics, statuses, Move/Ability/Item/Feature effects.

## Core rule: preserve the epistemic sequence

The world must distinguish what was seen from what was inferred.

```yaml
plant_health_episode:
  episode_id: null
  agricultural_site_refs: []
  first_signal_time: null
  opened_by_actor_ids: []
  opening_observation_refs: []
  current_scope_revision_id: null
  active_hypothesis_ids: []
  sample_ids: []
  diagnostic_record_ids: []
  action_ids: []
  follow_up_observation_ids: []
  recovery_checkpoint_ids: []
  downstream_handoff_ids: []
  status: OPEN
```

A valid episode can remain unresolved. `UNKNOWN_CAUSE` is preferable to an invented diagnosis.

## Spatial scope

Plant-health state must be spatially bounded.

```yaml
plant_health_scope:
  scope_id: null
  episode_id: null
  scope_type: null
  site_id: null
  plot_or_block_refs: []
  row_refs: []
  plant_instance_refs: []
  geometry_ref: null
  authored_at: null
  evidence_refs: []
  uncertainty_refs: []
```

Suggested scope types:

- INDIVIDUAL_PLANT;
- ROW;
- BED;
- GREENHOUSE_BAY;
- ORCHARD_BLOCK;
- FIELD_PLOT;
- AGRICULTURAL_SITE;
- MULTI_SITE_STUDY_AREA;
- OTHER_AUTHORED_SCOPE.

Scope must never expand solely because two sites grow the same crop.

## Condition observations

```yaml
plant_condition_observation:
  observation_id: null
  episode_id: null
  observed_at: null
  observed_by_actor_ids: []
  location_ref: null
  scope_ref: null
  subject_plant_refs: []
  observed_feature_codes: []
  photograph_or_media_refs: []
  measurement_refs: []
  environmental_context_refs: []
  pokemon_presence_refs: []
  confidence_note: null
  interpretation_claim_ids: []
```

Observation vocabulary can include authored visible features such as:

- missing fruit;
- leaf discoloration;
- wilt;
- holes or feeding marks;
- stem damage;
- unusual residue;
- premature fruit drop;
- abnormal growth form;
- dead plant tissue;
- root damage observed during authorized inspection;
- unusual insect/Pokémon presence;
- odor;
- soil-surface change.

These are descriptive. None automatically establishes disease, contamination, causal organism or mechanical status.

## Observation and diagnosis separation

Permanent invariants:

`SYMPTOM_OBSERVED != CAUSE_IDENTIFIED`

`POKEMON_PRESENT != DAMAGE_CAUSED_BY_POKEMON`

`DAMAGE_OBSERVED != INFECTIOUS_DISEASE_CONFIRMED`

`VISIBLE_FUNGUS != DIAGNOSTIC_IDENTITY_CONFIRMED`

`ONE_POSITIVE_SAMPLE != WHOLE_SITE_AFFECTED`

`ONE_NEGATIVE_SAMPLE != WHOLE_SITE_CLEAR`

`REPEAT_OBSERVATION != SPREAD_CONFIRMED`

`ACTION_PERFORMED != ACTION_EFFECTIVE`

`VISIBLE_RECOVERY != HARVEST_RECOVERED`

`HARVEST_LOSS != PERENNIAL_PLANTING_LOST`

## Survey episodes

Borrow only the useful evidence distinction between detection, delimitation and monitoring.

```yaml
plant_health_survey:
  survey_id: null
  episode_id: null
  purpose: null
  requested_by_ids: []
  performed_by_ids: []
  mandate_or_program_ref: null
  planned_scope_ref: null
  actual_coverage_refs: []
  started_at: null
  ended_at: null
  observation_refs: []
  sample_refs: []
  coverage_gap_refs: []
  interpretation_product_ref: null
  status: COMPLETE
```

Suggested purposes:

- DETECTION;
- DELIMITATION;
- MONITORING;
- POST_ACTION_RECHECK;
- RESEARCH_ONLY;
- OTHER_AUTHORED_PURPOSE.

A survey's purpose constrains its conclusion. A monitoring pass designed to revisit three known trees does not prove absence elsewhere.

## Coverage gaps

```yaml
survey_coverage_gap:
  gap_id: null
  survey_id: null
  intended_scope_ref: null
  uncovered_scope_ref: null
  reason_code: null
  created_at: null
  resolved_by_ref: null
```

Possible reasons:

- access unavailable;
- unsafe condition;
- sample unavailable;
- equipment failure;
- staffing constraint;
- weather interruption;
- subject removed before inspection;
- permission not established;
- other authored reason.

Coverage gaps remain evidence. They are not silently treated as negative observations.

## Samples and custody

Only instantiate sample custody when the story or diagnostic process needs it.

```yaml
plant_sample:
  sample_id: null
  episode_id: null
  collected_at: null
  collected_by_actor_ids: []
  source_scope_ref: null
  source_plant_refs: []
  sample_type: null
  collection_method_ref: null
  container_or_seal_ref: null
  current_custody_ref: null
  custody_event_refs: []
  requested_analysis_refs: []
  disposition_ref: null
```

The plant-health layer stores provenance. Laboratory capability and interpretation belong to whatever Science/diagnostic institution canon actually establishes.

## Diagnostic record

```yaml
plant_diagnostic_record:
  diagnostic_record_id: null
  episode_id: null
  sample_refs: []
  observation_refs: []
  question_tested: null
  method_ref: null
  institution_or_actor_refs: []
  completed_at: null
  outcome_code: null
  identified_subject_ref: null
  uncertainty_refs: []
  supersedes_record_id: null
  downstream_handoff_refs: []
```

Suggested neutral outcomes:

- DETECTED_WITHIN_TEST_SCOPE;
- NOT_DETECTED_WITHIN_TEST_SCOPE;
- INCONCLUSIVE;
- SAMPLE_UNSUITABLE;
- DIFFERENT_CAUSE_SUPPORTED;
- MULTIPLE_CAUSES_SUPPORTED;
- OTHER_AUTHORED_RESULT.

`NOT_DETECTED_WITHIN_TEST_SCOPE` must never be rendered as universal absence.

## Cause hypotheses

```yaml
plant_health_hypothesis:
  hypothesis_id: null
  episode_id: null
  hypothesis_type: null
  proposed_at: null
  proposed_by_actor_ids: []
  evidence_for_refs: []
  evidence_against_refs: []
  unresolved_question_refs: []
  status: ACTIVE
```

Candidate hypothesis types are labels only:

- WATER_STRESS;
- WEATHER_STRESS;
- SOIL_OR_SUBSTRATE_CONDITION;
- NUTRIENT_OR_CULTIVATION_CONDITION;
- FEEDING_DAMAGE;
- WILD_POKEMON_INTERACTION;
- NON_POKEMON_ORGANISM;
- INFECTIOUS_AGENT;
- POLLUTION_OR_CHEMICAL_EXPOSURE;
- PLANTING_MATERIAL_SOURCE;
- PHYSICAL_DAMAGE;
- MULTIPLE_CAUSES;
- UNKNOWN;
- OTHER_AUTHORED_CAUSE.

The type labels do not implement rules or establish truth.

## Affected-scope revisions

```yaml
affected_plant_scope_revision:
  revision_id: null
  episode_id: null
  parent_revision_id: null
  authored_at: null
  included_scope_refs: []
  excluded_scope_refs: []
  uncertain_scope_refs: []
  evidence_refs: []
  interpretation_notes: []
  status: CURRENT
```

Earlier revisions remain historical. A map should be reproducible from the evidence known at that time.

Useful state distinctions:

`POSSIBLY_AFFECTED`

`OBSERVED_SYMPTOMS`

`DIAGNOSTIC_SUPPORT`

`NO_CURRENT_EVIDENCE_WITHIN_SURVEY_SCOPE`

`RECOVERING`

`RECOVERED_WITHIN_DEFINED_SCOPE`

`UNKNOWN`

These are narrative evidence states. They are not PTU statuses.

## Plant-health actions

```yaml
plant_health_action:
  action_id: null
  episode_id: null
  action_type: null
  target_scope_refs: []
  initiated_by_actor_ids: []
  authority_or_operational_basis_refs: []
  started_at: null
  completed_at: null
  material_or_equipment_refs: []
  pokemon_participant_refs: []
  expected_observation_refs: []
  actual_follow_up_refs: []
  status: null
```

Possible authored action labels:

- INCREASE_OBSERVATION;
- PAUSE_HARVEST_FOR_REVIEW;
- ISOLATE_PLANTING_MATERIAL;
- PRUNE_OR_REMOVE_AFFECTED_MATERIAL;
- ALTER_IRRIGATION_OR_CULTIVATION;
- CLEAN_OR_SERVICE_EQUIPMENT;
- LIMIT_ACCESS_TO_BOUNDED_AREA;
- REFER_TO_ECOLOGY_OR_COEXISTENCE;
- REFER_TO_WATER_OR_POLLUTION;
- REFER_TO_SCIENCE;
- REFER_TO_BATCH_TRACEABILITY;
- REPLANT_AFTER_REVIEW;
- OTHER_AUTHORED_ACTION.

These labels record actions. They do not create regulatory power. If an action requires compulsory authority, a valid mandate reference must already exist in canon.

## Action effectiveness

```yaml
plant_health_action_review:
  review_id: null
  action_id: null
  reviewed_at: null
  follow_up_observation_refs: []
  comparison_baseline_refs: []
  outcome: null
  uncertainty_refs: []
  next_action_refs: []
```

Suggested outcomes:

- IMPROVEMENT_OBSERVED;
- NO_CLEAR_CHANGE;
- CONDITION_WORSENED;
- DIFFERENT_SCOPE_AFFECTED;
- ACTION_COULD_NOT_BE_EVALUATED;
- MORE_TIME_OR_DATA_REQUIRED;
- OTHER_AUTHORED_OUTCOME.

Correlation must not be promoted to causal certainty without evidence.

## Recovery model

Recovery is multidimensional.

```yaml
plant_health_recovery_checkpoint:
  checkpoint_id: null
  episode_id: null
  checkpoint_type: null
  scope_refs: []
  recorded_at: null
  evidence_refs: []
  owner_system_ref: null
  status: ACHIEVED
```

Candidate checkpoint types:

- NEW_SYMPTOMS_NOT_OBSERVED_IN_MONITORED_SCOPE;
- PLANT_VIGOR_IMPROVED;
- DIAGNOSTIC_RECHECK_COMPLETE;
- AFFECTED_MATERIAL_REMOVED;
- REPLANTING_COMPLETE;
- HARVEST_RESUMED;
- NORMAL_CULTIVATION_ROUTINE_RESUMED;
- TEMPORARY_ACCESS_LIMIT_ENDED;
- DOWNSTREAM_BATCH_REVIEW_COMPLETE;
- ECOLOGY_HANDOFF_COMPLETE;
- WATER_OR_POLLUTION_HANDOFF_COMPLETE;
- EPISODE_CLOSED_WITH_UNKNOWN_CAUSE;
- OTHER_AUTHORED_CHECKPOINT.

`EPISODE_CLOSED` should contain a reason and must not imply that every downstream effect disappeared.

## Harvest and batch boundary

Before harvest, this layer can preserve plant condition and whether a harvest decision was paused or changed by the agricultural owner.

After harvest:

- physical produce/batch identity belongs to Food/Material provenance;
- distributed problem containment belongs to Batch Traceability;
- transport belongs to Courier/Transport;
- health consequences belong to Care/Community Health;
- disposal belongs to the appropriate Waste/Agriculture owner.

The same episode may link to all of those without duplicating them.

## Ecology and wild Pokémon boundary

A wild Pokémon observation can be relevant evidence. It cannot be converted automatically into pest classification.

```yaml
pokemon_crop_interaction_observation:
  interaction_observation_id: null
  pokemon_entity_or_population_ref: null
  identity_confidence: null
  observed_at: null
  location_ref: null
  behavior_observed: null
  crop_condition_ref: null
  direct_contact_observed: false
  damage_event_observed: false
  causal_claim_ids: []
  ecology_handoff_ref: null
  coexistence_handoff_ref: null
```

Direct observation of feeding can support a bounded claim that feeding occurred. It still does not prove every symptom in the site has the same cause.

## Pokémon work participation

Pokémon may contribute to agricultural work only through established individual capability/work records.

Possible narrative roles:

- carry tagged samples;
- assist with visual inspection under handler direction;
- operate ordinary equipment if its work role supports it;
- monitor a known route or plot;
- perform a specific Move when authoritative rules and local procedure explicitly permit that use.

Never infer capability from Type or species stereotype.

## Temporal continuity

Every episode should preserve at least these timestamps when available:

- first observed signal;
- first report;
- first verified observation;
- survey start/end;
- sample collection;
- diagnostic completion;
- scope revision;
- action start/completion;
- follow-up observation;
- harvest consequence;
- recovery checkpoint;
- closure.

This enables mysteries where several NPCs use the same word such as “started,” “spread,” “treated,” or “ended” for different legitimate dates.

## Provenance-aware map products

A plant-health map can show:

- directly observed points;
- sampled points;
- interpreted affected area;
- uncertainty area;
- unsurveyed gaps;
- prior revisions.

Rendered map cells must never be rewritten as direct field observations.

## Quest grammar

Plant-health stories should usually start from ordinary agricultural continuity rather than a dramatic outbreak.

Useful opening signals:

- one row harvested poorly;
- a caretaker notices a pattern unlike last year;
- fruit disappears only on particular mornings;
- a greenhouse bay changes after equipment maintenance;
- two farms report similar symptoms but use different water sources;
- a nursery shipment and an old orchard share a cultivar but not a supplier;
- a wild Pokémon route changes at the same time as crop damage;
- an old photograph reveals the same symptom decades earlier.

Escalation comes from evidence and consequences, not from automatically increasing combat difficulty.

## Mystery templates

### Five Times the Orchard “Recovered”

Five records may refer to:

1. last new visible symptom in the monitored row;
2. completion of pruning/removal;
3. first negative recheck within test scope;
4. return to ordinary cultivation;
5. first normal harvest window.

All five dates can be correct.

### Three Brown Rows, Two Causes

Three rows show similar discoloration. One follows irrigation stress. One has a diagnosed biological cause. The third remains uncertain. Shared appearance does not require one universal explanation.

### The Pokémon Seen Every Morning

A recurring Pokémon is visible near damaged plants. Camera timing, feeding evidence, crop maps and alternative food sources eventually show whether it feeds on the crop, passes through the area, or is responding to the same upstream condition.

### The Map Changed After Lunch

Field observers worked offline in two sectors. A midday map omitted an affected area because records had not yet been uploaded. The later revision is more complete without proving anyone hid the first result.

## Long-form arc pattern: A Valley Learns to Look Closely

Phase one establishes growers, seasonal routines, individual Pokémon work roles, water sources and normal variation.

Phase two introduces small, inconsistent symptoms. Different sites form different hypotheses.

Phase three adds bounded surveys, sample provenance and one or more owner-system handoffs. The initially popular explanation may remain plausible, weaken or split into multiple causes.

Phase four produces differentiated actions rather than one valley-wide switch. Some sites change cultivation. Another coordinates with Ecology. A third discovers a Water or Pollution dependency. A nursery or batch may require separate traceability.

Phase five records recovery unevenly. One orchard resumes harvest. One plot is replanted. One investigation closes without perfect causal certainty. A temporary inspection path or cooperative routine becomes permanent social infrastructure.

A later season can reactivate old observations and compare them with the new episode instead of resetting the valley.

## Encounter concept: Orchard Survey Perimeter

Narrative premise: conflicting plant-health reports require a bounded reinspection, but an unrelated hostile encounter threatens the access perimeter.

Full intended form may include:

- staff withdrawal through orchard rows;
- Intercept or forced displacement;
- protected survey lanes;
- temporary access zones;
- generalized reactions at crossings;
- objective-aware PROTECT/WITHDRAW/CLEAR_ROUTE AI;
- exact governed environmental effects if a source and engine contract exist;
- semantic Minecraft playback of staff withdrawal and later survey resumption.

Permanent capability classification:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for changing protected lanes, environmental exposure or generalized crossing reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version: READY.

The survey pauses before BattleSpec creation. Staff, samples, equipment, controlled plants and noncombatant Pokémon remain outside the tactical grid. AutoPTU receives static reviewed geometry and explicit combatants selected by Ouros. Battle victory may secure immediate access. It cannot complete the survey, identify a cause, change the affected scope or prove recovery.

## Encounter concept: Nursery Block Diversion

Narrative premise: planting material under review must remain undisturbed while a conventional threat appears near the nursery access route.

Full intended form could require protected objects, escort-like movement, forced movement, zone boundaries, reaction ordering and tactical policy.

Reduced version: READY.

The controlled planting block and all samples are placed physically outside BattleSpec. Custody/access state is resolved first by the owning systems. The encounter occurs on a static exterior approach. Victory only secures the immediate route. It cannot clear, condemn, release, destroy or transfer planting material.

## Encounter concept: Pollinator Edge Reinspection

Narrative premise: repeat crop symptoms overlap a habitat edge used by wild Pokémon, and evidence must be gathered without turning presence into guilt.

Full intended form could involve moving wildlife, nonlethal displacement goals, protected habitat cells, reactions, environmental zones and objective-aware AI. Each such mechanic requires exact governing capability.

Reduced version: READY.

Ecology/Coexistence resolves wildlife movement first. Plant-health personnel withdraw. Any subject under observation remains outside BattleSpec unless Ouros independently selects it as a legitimate combatant based on current world facts. AutoPTU resolves a normal battle on static geometry. Inspection and causal assessment occur later.

## Mechanical guardrails

This layer does not define:

- crop HP;
- plant-disease battle statuses;
- infectious tactical spread;
- spore/pollen clouds;
- windborne hazard movement;
- generic Poison exposure;
- generic accuracy/LoS effects from pollen;
- pest aggro rules;
- automatic capture/removal success;
- pesticides as Items;
- pruning or treatment Moves;
- Grass/Bug/Poison Type immunities or competencies;
- plant-health Skill DCs;
- Trainer Feature regulatory authority.

If future canon uses one of these, the exact PTU/Caelo/AutoPTU rule and engine family must be referenced.

## Minecraft / Cobblemon boundary

Minecraft/Cobblemon can present:

- differently staged crop blocks;
- damaged-looking plants where Ouros has authored that observation;
- sample flags and inspection markers;
- temporary fences or signs;
- workers and trained Pokémon performing already-decided routines;
- revised map boards;
- recovered/replanted visual variants;
- wildlife sightings selected by Ouros world state.

Minecraft crop age does not become the authoritative cultivation cycle. Block breakage does not prove crop damage cause. Bonemeal does not establish recovery. Poison particles do not create PTU poisoning. Nearby Bug or Grass Pokémon do not become pests or experts. Cobblemon BattleState does not decide plant-health truth, combatants, legality, HP/status, positions or downstream outcomes.

## Implementation-safe world-to-battle pattern

1. Ouros resolves current agricultural, plant-health, wildlife and institutional facts.
2. It records observations, scopes and uncertainty before battle.
3. Survey staff, samples, controlled planting material and noncombatants are moved or paused in world state.
4. Static reviewed geometry is selected.
5. Ouros explicitly selects combatants.
6. AutoPTU resolves only verified/supported battle rules.
7. The battle result returns as one bounded fact.
8. Plant Health, Agriculture, Ecology, Water, Pollution, Batch or other owners decide downstream state.
9. A later survey or observation determines whether any plant-health condition changed.

## Canon questions deliberately unresolved

- Which Ouros institutions or professions perform plant-health diagnostics?
- Which regions maintain formal surveillance programmes?
- What crops, orchards and nurseries are established in canon?
- Which diagnostic tools exist at each technology level?
- Which actors can authorize compulsory isolation, destruction or movement controls, if anyone?
- What privacy/commercial rules apply to farm observations?
- How are disputed diagnoses reviewed?
- Which historic crop-health episodes shaped settlement patterns?
- Which individual Pokémon have established agricultural or diagnostic roles?
- Do any sacred, medicinal or culturally important plants require special stewardship?

No answer is assumed by this extension.
