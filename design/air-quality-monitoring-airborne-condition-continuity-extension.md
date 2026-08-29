# Ouros Air-Quality Monitoring & Airborne-Condition Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension preserves operational continuity for outdoor air monitoring and airborne-condition interpretation without becoming an environmental combat simulator or a medical rules engine.

It owns monitoring sites, bounded observations, monitoring gaps, versioned spatial products, airborne plume observations, episode grouping, temporary monitoring deployments and handoffs to systems that own consequences.

It does not decide pollution source, health diagnosis, fire behavior, volcanic activity, weather, route closure, workplace safety, facility occupancy or PTU tactical effects.

## Authority boundaries

Existing authorities remain intact.

`waste-sanitation-recycling-pollution-layer.md` owns generic contamination observations, pollution source claims and cleanup.

`wildfire-fire-response-incident-continuity-extension.md` owns wildfire/structural-fire incidents and their smoke observations.

`volcanic-monitoring-eruption-ashfall-recovery-continuity-extension.md` owns volcanic activity, plume evidence and ground ashfall observations.

Weather owns meteorological observations and forecasts.

Community Health owns cluster investigation. Care owns individual health state, diagnosis and treatment.

Public Notices / Communications own authorization, distribution and receipt of notices.

Road, Rail, Aviation, Maritime, Travel, Workplace, Education, Events, Facilities, Conservation and other owner systems decide their own restrictions and reopening.

AutoPTU owns battle legality and tactical resolution. Ouros owns world facts and combatant selection. Minecraft/Cobblemon/Craftics provide representation and playback only.

## Core invariants

`MONITOR_OPERATING != COMPLETE_COVERAGE`

`NO_READING != CLEAN_AIR`

`POINT_OBSERVATION != REGION_WIDE_CONDITION`

`SPATIAL_PRODUCT_CELL != DIRECT_OBSERVATION`

`PLUME_OBSERVED != GROUND_LEVEL_IMPACT_CONFIRMED`

`VISIBLE_HAZE != SOURCE_CONFIRMED`

`ODOR_REPORTED != TOXICITY_CONFIRMED`

`AIR_CONDITION_ASSESSMENT != HEALTH_DIAGNOSIS`

`ASSESSMENT_ISSUED != NOTICE_DELIVERED`

`NOTICE_DELIVERED != EVERY_ACTOR_RECEIVED_OR_UNDERSTOOD`

`OUTDOOR_CONDITION != INDOOR_CONDITION`

`AIR_CONDITION_IMPROVED != DOWNSTREAM_RESTRICTION_CLEARED`

`POKEMON_BEHAVIOR_CHANGED != POLLUTION_CAUSE_OR_SENSING_CONFIRMED`

These are mandatory state separations.

## 1. Monitoring network

```yaml
air_monitoring_network:
  network_id: null
  public_name_ids: []
  operator_actor_or_institution_ids: []
  region_scope_ids: []
  monitor_site_ids: []
  temporary_deployment_ids: []
  supported_observation_class_refs: []
  data_product_ids: []
  communications_ref_ids: []
  maintenance_ref_ids: []
  current_coverage_claim_ids: []
  provenance_refs: []
  canon_status: proposed
```

A network can combine permanent and temporary observations if setting canon supports those technologies and institutions.

The existence of a network does not imply uniform geographic coverage.

## 2. Monitoring site

```yaml
air_monitoring_site:
  site_id: null
  network_id: null
  location_id: null
  operator_actor_ids: []
  observation_method_refs: []
  authored_subject_refs: []
  operational_state: STATUS_UNKNOWN
  coverage_claim_ids: []
  last_observation_ids: []
  quality_review_ref_ids: []
  maintenance_ref_ids: []
  communications_ref_ids: []
  monitoring_gap_ids: []
  provenance_refs: []
```

Candidate operational states:

- OPERATING
- DEGRADED
- OFFLINE
- ACCESS_BLOCKED
- DATA_DELAYED
- UNDER_REVIEW
- STATUS_UNKNOWN

A site can be physically intact and still have delayed or unavailable data. A site can also operate while providing only one authored observation class.

Do not infer pollutant lists, sensor technology, measurement units or precision without canon.

## 3. Air observation

```yaml
air_observation:
  observation_id: null
  site_or_observer_id: null
  network_id: null
  location_ref: null
  observed_at: null
  observation_class_ref: null
  observed_value_or_band_ref: null
  method_ref: null
  quality_or_confidence_ref: null
  raw_evidence_refs: []
  source_context_refs: []
  interpreted_by_product_ids: []
  downstream_handoff_ids: []
  provenance_refs: []
```

Observation classes must be authored. Examples may include an instrument reading, visibility observation, odor report, particulate observation, airborne-material observation or another setting-supported category.

Narrative generation cannot invent a concentration, threshold, health category or chemical identity merely because a scene needs urgency.

## 4. Monitoring gap

```yaml
air_monitoring_gap:
  gap_id: null
  site_or_network_id: null
  start_at: null
  end_at: null
  reason_state: UNKNOWN
  known_reason_ref: null
  affected_observation_classes: []
  affected_coverage_claim_ids: []
  substitute_observation_refs: []
  later_reconstruction_refs: []
  provenance_refs: []
```

Suggested reason states:

- EQUIPMENT_OFFLINE
- COMMUNICATION_DELAY
- ACCESS_BLOCKED
- MAINTENANCE
- RECORD_NOT_RECEIVED
- QUALITY_REVIEW_HOLD
- UNKNOWN

A gap must remain visible. Later reconstruction can add evidence but does not rewrite the historical fact that decision-makers lacked the reading at the time.

## 5. Airborne plume observation

```yaml
airborne_plume_observation:
  plume_observation_id: null
  observed_at: null
  observation_method_ref: null
  observed_extent_claim_ref: null
  elevation_or_vertical_scope_claim_ref: null
  appearance_claims: []
  possible_source_context_refs: []
  ground_condition_observation_refs: []
  confidence_ref: null
  provenance_refs: []
```

This object is intentionally an observation claim.

A visual, satellite-equivalent, lookout or other authored observation of a plume does not prove that every ground location beneath the represented extent has the same air condition.

Source attribution remains with Pollution/Case or the relevant incident authority.

## 6. Spatial interpretation product

```yaml
air_condition_product:
  product_id: null
  issuer_actor_or_institution_id: null
  issued_at: null
  valid_from: null
  valid_until: null
  spatial_scope_ids: []
  source_observation_ids: []
  source_plume_observation_ids: []
  interpretation_method_ref: null
  condition_band_ref: null
  known_gap_ids: []
  confidence_or_quality_ref: null
  supersedes_product_id: null
  superseded_by_product_id: null
  notice_handoff_ids: []
  owner_system_handoff_ids: []
  provenance_refs: []
```

The product can represent a map, bulletin, sector assessment or another setting-approved summary.

Hard rules:

- preserve the inputs used at issue time;
- preserve old versions after revision;
- do not turn interpreted map cells into fabricated monitor readings;
- do not silently fill uncovered areas;
- do not invent calibrated numeric probability or concentration unless canon supports it.

## 7. Air-condition episode

```yaml
air_condition_episode:
  episode_id: null
  region_scope_ids: []
  opened_at: null
  current_state: OBSERVING
  trigger_observation_ids: []
  product_ids: []
  plume_observation_ids: []
  source_incident_context_refs: []
  pollution_case_refs: []
  monitoring_gap_ids: []
  temporary_deployment_ids: []
  downstream_handoff_ids: []
  closure_or_transition_ref: null
  legacy_event_ids: []
  provenance_refs: []
  canon_status: proposed
```

Candidate operational states:

- OBSERVING
- UNDER_REVIEW
- ELEVATED_ATTENTION
- MONITORING_EXPANDED
- IMPROVING_UNDER_CURRENT_EVIDENCE
- ROUTINE_MONITORING_RETURN
- CLOSED_FOR_CURRENT_REVIEW

These are narrative workflow states. They are not health categories, legal alert levels or PTU statuses.

An episode can exist with an unknown source.

## 8. Temporary monitoring deployment

```yaml
temporary_air_monitoring_deployment:
  deployment_id: null
  episode_id: null
  location_id: null
  operator_ids: []
  reason_ref: null
  equipment_or_method_refs: []
  deployed_at: null
  operational_from: null
  removed_at: null
  observation_ids: []
  coverage_claim_ids: []
  maintenance_refs: []
  transition_or_legacy_ref: null
  provenance_refs: []
```

A temporary site can later be removed, retained, replaced or become a social landmark without silently becoming permanent technical infrastructure.

## 9. Downstream handoff

```yaml
air_condition_handoff:
  handoff_id: null
  source_product_or_observation_id: null
  receiving_system_ref: null
  receiving_actor_or_institution_id: null
  sent_at: null
  received_at: null
  acknowledged_at: null
  subject_scope_ref: null
  requested_review_ref: null
  owner_decision_ref: null
  status: PREPARED
  provenance_refs: []
```

Possible statuses:

- PREPARED
- SENT
- RECEIVED
- ACKNOWLEDGED
- UNDER_OWNER_REVIEW
- OWNER_DECISION_RECORDED
- CLOSED

The receiving owner may choose a different response from another institution given the same evidence.

Examples:

- an event organizer relocates activities;
- a school alters an outdoor schedule;
- an aviation authority reviews visibility/air-operation concerns under its own rules;
- a workplace changes operations;
- Care/Community Health reviews health signals;
- Conservation reviews species observations;
- Crisis evaluates whether a broader response is warranted.

The air-quality layer records the handoff, not the downstream decision.

## 10. Pokémon observations

```yaml
air_condition_pokemon_observation:
  observation_id: null
  pokemon_actor_or_population_ref: null
  location_id: null
  observed_at: null
  observed_behavior_ref: null
  comparison_baseline_ref: null
  related_air_observation_ids: []
  ecology_handoff_ref: null
  causal_claim_ref: null
  provenance_refs: []
```

Examples of valid narrative facts:

- an individual Pokémon stopped visiting a rooftop during a documented episode;
- a flock used a different overnight location;
- a particular working Pokémon refused an outdoor assignment;
- a species returned to a district after a long period.

None of these observations automatically prove:

- source attribution;
- toxicity;
- health effect;
- prediction;
- pollution sensing;
- species-wide immunity or vulnerability;
- willingness to perform monitoring work.

## 11. Historical continuity

Air monitoring should produce useful history even after conditions improve.

Possible legacy facts:

- an old monitoring roof remains on maps after instruments moved;
- a temporary site becomes a permanent community science location;
- residents still refer to a district by an old episode name;
- an institution changes its event calendar after a prior episode;
- a later investigation reuses photographs, monitor logs or notices from years earlier;
- a formerly polluted district recovers socially before its reputation does, or vice versa.

Historical products and observations remain queryable with their original scope and provenance.

## 12. Mysteries from provenance rather than hidden truth scores

Good air-quality mysteries can arise from records that use different subjects.

Example: three correct statements can coexist.

- the ridge monitor reported no notable change;
- a valley sensor reported a different condition;
- a public map showed an interpreted band between them.

The resolution comes from monitor location, product inputs, issue time and spatial scope.

Do not manufacture sabotage or falsification merely because records differ.

## 13. Exploration use

A former monitoring station can support exploration through:

- old site logs;
- photographs;
- instrument mounts;
- archived map editions;
- maintenance history;
- changed roof access;
- former staff testimony;
- Pokémon occupancy changes;
- temporary structures later repurposed.

This can run without any tactical airborne hazard. The location may be fully safe and static while the records reveal a meaningful environmental history.

## 14. Battle implementation boundary

The default world-state layer does not create tactical smoke, gas, haze or exposure.

A rich encounter may eventually use an airborne condition only if the governing PTU/Caelo source defines the exact effect and the runtime verifies every required capability family.

Potential dependencies include:

- targeting/footprints/range/LoS when a validated condition changes visibility or legal targeting;
- complete movement if withdrawal, Intercept, forced movement or changing access is active;
- full turn/round lifecycle for phased or delayed condition changes;
- full stateful damage pipeline if exposure causes damage;
- status lifecycle if an exact condition applies a status;
- terrain/weather/hazards/zones/reactions for spatial airborne zones, reactions or dynamic restrictions;
- move-specific behavior, abilities, items and Trainer Features/perks for any exact rule interaction;
- AI tactical policy for PROTECT, WITHDRAW, CLEAR_ROUTE or zone-aware behavior;
- adapter/playback for semantic smoke/haze/monitoring presentation synchronized to authoritative state.

No one representative mechanic proves these complete families.

## 15. Minecraft/Cobblemon/Craftics boundary

The adapter may present:

- monitoring stations;
- rooftop equipment;
- temporary sensor props;
- signs and bulletin boards;
- smoke, haze, dust or mist particles;
- distant plumes;
- lighting/sky presentation;
- NPC crews;
- Pokémon behavior already decided by Ouros;
- UI maps and notices.

Presentation never creates authority.

Particles do not apply a status. Render distance does not become PTU LoS. Minecraft fog does not change accuracy. A campfire or fire block does not establish a regional air episode. A chimney particle does not prove source attribution. Entity proximity does not calculate exposure. Cobblemon BattleState does not decide combatants, legality, HP/status, positions or outcomes.

## Canon questions left open

Pass 119 does not decide:

- which Ouros regions operate formal air-monitoring networks;
- what technologies they use;
- which airborne subjects they can measure;
- whether quantitative units or public condition bands exist;
- who owns environmental assessment authority;
- what institutions receive or publish assessments;
- whether indoor monitoring exists and how it is governed;
- historical pollution episodes;
- regional industrial practices;
- species-specific observational relationships;
- any universal health or tactical effect.

Those remain explicit canon decisions rather than generated assumptions.