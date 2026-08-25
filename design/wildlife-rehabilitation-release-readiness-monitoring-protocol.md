# Wildlife rehabilitation, release readiness & post-release monitoring protocol

Status: PROPOSED SUBORDINATE PROTOCOL. Not established Ouros canon.
Date: 2026-08-25

## Purpose and authority boundary

This protocol extends existing Ouros authorities. It does not replace them.

Care owns diagnosis, treatment, clinical/narrative recovery and facility capacity.

Pokémon Agency owns persistent Pokémon identity, custody, associations and release as an identity-preserving transition.

Conservation owns release/relocation policy, stewardship, release locations and population/ecological management.

Biosecurity owns disease/pathway screening where relevant.

Research Ethics owns intrusive monitoring and study authorization.

Wild Collectives, Migration and Conservation Genetics own population/group consequences.

This protocol owns the evidence and operational history between a possible release transition and observed post-release outcomes.

## Core separation

Keep this chain explicit:

```text
CARE STABILITY
→ READINESS REVIEW
→ RELEASE/RELOCATION AUTHORITY REVIEW
→ SITE REVIEW
→ METHOD + CONTINGENCY PLAN
→ RELEASE ATTEMPT
→ POST-RELEASE OBSERVATION
→ SCOPED OUTCOME ASSESSMENT
```

Each stage can pause, fail, be revised or remain unresolved.

Hard rules:

- stable in care does not mean release-ready;
- release-ready does not mean release-authorized;
- authorized does not mean physically released;
- released does not mean successfully established;
- return to care does not automatically mean failure;
- non-detection does not mean death;
- approach to humans does not automatically mean habituation, tameness, friendship or Loyalty;
- staying near a release enclosure does not prove inability to survive;
- leaving immediately does not prove successful adaptation.

## 1. Rehabilitation program

A rehabilitation program groups an individual Pokémon's transition work without duplicating the care case.

```yaml
rehab_program:
  rehab_program_id: null
  pokemon_entity_id: null
  care_case_id: null
  stewardship_area_id: null
  origin_event_refs: []
  opened_at: null
  current_phase: CARE | READINESS_REVIEW | PRE_RELEASE | RELEASED_MONITORING | RETURNED_TO_CARE | CLOSED
  coordinating_actor_ids: []
  authority_refs: []
  unresolved_questions: []
  privacy_scope: null
  canon_status: proposed
```

`care_case_id` remains the authority for treatment. This program may read a bounded readiness-relevant summary from Care but cannot rewrite HP, Injury, Status, diagnosis or treatment state.

## 2. Readiness review

Readiness is multidimensional evidence, never one numeric score.

```yaml
release_readiness_assessment:
  assessment_id: null
  rehab_program_id: null
  assessed_at: null
  assessor_actor_ids: []
  mechanical_readiness_refs: []
  care_readiness_refs: []
  mobility_observation_refs: []
  feeding_foraging_observation_refs: []
  orientation_navigation_observation_refs: []
  social_context_observation_refs: []
  avoidance_habituation_observation_refs: []
  species_population_context_refs: []
  uncertainty_notes: []
  disposition: READY_FOR_SITE_REVIEW | NOT_READY | READY_WITH_SUPPORT_CANDIDATE | NEEDS_MORE_EVIDENCE | NOT_APPLICABLE
```

The listed dimensions are possible evidence categories, not mandatory universal tests.

A species whose normal ecology does not involve group living should not be failed for lack of social integration. A Pokémon that receives prepared food during care should not automatically be labelled unable to forage.

## 3. Behavioral observations before release

Record the smallest defensible fact.

Examples:

- accepted a naturally available food item during one supervised observation;
- ignored offered human food during three observations;
- repeatedly approached staff when a specific feeding cart arrived;
- used a known movement capability in a safe enclosure;
- withdrew from an unfamiliar human;
- remained beside the enclosure gate after it opened;
- joined a known conspecific group during a supervised transition;
- did not interact with the group during the observation window.

Do not automatically infer:

- wants to stay;
- wants to leave;
- is tame;
- is afraid of humans;
- has forgotten how to survive;
- has accepted a new Trainer;
- has rejected a former Trainer;
- is ready to breed;
- has a specific Loyalty value.

## 4. Habituation and dependency assessment

These are interpretations requiring repeated evidence and context.

```yaml
human_dependency_assessment:
  assessment_id: null
  pokemon_entity_id: null
  observation_window: null
  evidence_refs: []
  feeding_context_refs: []
  approach_context_refs: []
  response_to_unfamiliar_humans_refs: []
  alternative_resource_refs: []
  interpretation: UNRESOLVED | LOW_CONCERN | POSSIBLE_CONCERN | MATERIAL_CONCERN
  confidence: LOW | MEDIUM | HIGH
  review_after: null
```

Never use species reputation alone to assign habituation.

A Pokémon that returns to a care site may be responding to food, shelter, another Pokémon, a familiar person, route geometry or an unknown driver. Preserve competing hypotheses.

## 5. Release-site assessment

Conservation remains the authority for whether release/relocation is permitted. This protocol stores operational evidence about a candidate site.

```yaml
release_site_assessment:
  site_assessment_id: null
  rehab_program_id: null
  location_id: null
  assessed_at: null
  habitat_state_refs: []
  known_population_refs: []
  collective_refs: []
  migration_refs: []
  biosecurity_refs: []
  access_disturbance_refs: []
  food_resource_observation_refs: []
  shelter_resource_refs: []
  seasonality_refs: []
  route_connectivity_refs: []
  monitoring_feasibility_refs: []
  unresolved_risks: []
  operational_fit: SUITABLE_CANDIDATE | CONDITIONAL_CANDIDATE | NOT_SUITABLE | UNRESOLVED
```

The site does not become suitable because Minecraft visually resembles the species' biome.

## 6. Release method

Method labels are operational descriptions only.

```yaml
release_plan:
  release_plan_id: null
  rehab_program_id: null
  authorized_release_ref: null
  site_assessment_id: null
  planned_window: null
  method: DIRECT_RELEASE | SOFT_RELEASE | STAGED_TRANSITION | RETURN_TO_ORIGIN | OTHER_AUTHORED_METHOD
  pre_release_support: []
  post_release_support: []
  support_taper_conditions: []
  monitoring_plan_ref: null
  contingency_plan: null
  stop_conditions: []
  responsible_actor_ids: []
  status: DRAFT | APPROVED | PAUSED | EXECUTED | CANCELLED
```

No method has an inherent mechanical bonus.

`SOFT_RELEASE` does not create a PTU buff, a permanent spawn point or ownership claim.

## 7. Support infrastructure

Possible authored support can include:

- temporary shelter;
- acclimation enclosure;
- temporary feeding station;
- water provision;
- observation hide;
- remote sensor;
- protected access window;
- temporary visitor closure.

All support has an owner authority and a removal/taper plan when appropriate.

Minecraft renders the current support revision. Placing a feeder block cannot create a legal support program or manipulate authoritative spawn state.

## 8. Release attempt

```yaml
release_attempt:
  release_attempt_id: null
  rehab_program_id: null
  release_plan_id: null
  pokemon_entity_id: null
  timestamp: null
  location_id: null
  custody_before_ref: null
  release_mechanical_ref: null
  gate_or_container_opened_at: null
  observed_response_refs: []
  physical_departure_state: DEPARTED | REMAINED_NEAR_SITE | RETURNED_TO_SUPPORT | INTERRUPTED | UNKNOWN
  custody_after_ref: null
  incident_refs: []
```

The event preserves what physically happened. It does not author emotional meaning.

If governing PTU/Caelo/Cobblemon mechanics require an explicit mechanical release transaction, `release_mechanical_ref` must point to that authoritative result. The narrative protocol cannot manufacture it.

## 9. Post-release monitoring series

```yaml
post_release_monitoring_series:
  series_id: null
  rehab_program_id: null
  pokemon_entity_id: null
  started_at: null
  planned_methods: []
  observation_effort_records: []
  direct_observation_refs: []
  telemetry_observation_refs: []
  camera_trap_refs: []
  field_sign_refs: []
  public_report_refs: []
  collective_observation_refs: []
  non_detection_records: []
  intervention_refs: []
  last_review_at: null
  status: ACTIVE | REDUCED_INTENSITY | PAUSED | ENDED | LOST_TO_FOLLOWUP
```

A telemetry observation is still an observation with method limits. It does not expose thoughts, HP, Status, exact diet, social state or ownership.

## 10. Non-detection

Each non-detection should preserve effort.

```yaml
monitoring_non_detection:
  event_id: null
  series_id: null
  time_window: null
  method: null
  searched_area_refs: []
  effort_band: null
  equipment_state_ref: null
  environmental_limits: []
  result: NOT_DETECTED
```

`NOT_DETECTED` never becomes `DEAD`, `LEFT_REGION` or `RECAPTURED` without separate evidence.

## 11. Return and recapture

A Pokémon may return voluntarily to support infrastructure or may require a new care intervention.

```yaml
post_release_return_event:
  return_event_id: null
  rehab_program_id: null
  pokemon_entity_id: null
  timestamp: null
  location_id: null
  event_kind: VOLUNTARY_RETURN | FOUND_IN_DISTRESS | AUTHORIZED_RECAPTURE | TEMPORARY_RECARE | UNKNOWN_RETURN
  observation_refs: []
  mechanical_capture_or_custody_ref: null
  care_case_ref: null
  interpretation_refs: []
```

Hard rules:

- a voluntary return does not restore ownership;
- a recapture for care does not erase the release attempt;
- a second release keeps the same persistent Pokémon identity;
- repeated returns can become a longitudinal pattern without being labelled failure.

## 12. Outcome assessment

Outcome assessments must declare their scope.

```yaml
release_outcome_assessment:
  outcome_assessment_id: null
  rehab_program_id: null
  assessed_at: null
  evidence_window: null
  evidence_refs: []
  monitoring_effort_ref: null
  dimensions:
    survival_or_persistence: UNKNOWN
    independent_resource_use: UNKNOWN
    movement_or_range_use: UNKNOWN
    social_integration_if_relevant: NOT_APPLICABLE
    reproduction_if_relevant: NOT_ASSESSED
  overall_interpretation: UNRESOLVED | EARLY_POSITIVE_EVIDENCE | MATERIAL_CONCERN | RETURNED_TO_CARE | MONITORING_COMPLETE
  limitations: []
```

Avoid `SUCCESS/FAILURE` as the only field.

A program can close because its monitoring objective is complete even when some dimensions remain unknown.

## 13. Release windows and timing

Potential world-state dependencies:

- migration window;
- breeding/nesting season;
- weather window;
- food/resource availability;
- road/visitor pressure;
- wildfire/flood recovery;
- ferry/transport availability;
- staffing;
- monitoring equipment availability.

A delayed release can be a correct operational choice rather than a narrative setback.

Do not invent species-specific calendar requirements unless authored or sourced.

## 14. Juveniles and dependency

Pass 146 remains authoritative for wild juvenile/dependency observations.

Pass 162 may read those assessments when a juvenile enters rehabilitation.

It must not infer orphanhood from adult absence, determine parentage, create hatch timers or decide independence from age alone.

Potential release paths can include:

- return to known natal area;
- reunification attempt if authorized and evidence supports it;
- staged release after dependency review;
- continued care;
- sanctuary/other authored placement.

No path is automatic.

## 15. Persistent former patients

A released Pokémon may later appear in:

- Migration observations;
- Wild Collective state;
- conservation surveys;
- urban wildlife records;
- nesting observations;
- fisheries or shoreline monitoring;
- public memory;
- a later care case;
- a former-Trainer encounter if such history exists.

All systems should reference the same `pokemon_entity_id` where identity is confirmed.

## 16. Institutional memory

Facilities should remember meaningful release history without publishing private cases by default.

Possible aggregate records:

- releases attempted by season;
- broad reasons for delayed release;
- monitoring completion bands;
- recurrent release-site disruptions;
- infrastructure improvements;
- recurring species-specific care needs when evidence exists.

Do not expose individual medical details automatically.

## 17. Generator grammar

Useful objective verbs:

- REVIEW_READINESS
- VERIFY_RELEASE_SITE
- PREPARE_RELEASE_WINDOW
- MOVE_SUPPORT_EQUIPMENT
- OBSERVE_RELEASE
- MONITOR
- LOCATE_SIGNAL
- VERIFY_NON_DETECTION
- RETRIEVE_DEVICE
- REDUCE_SUPPORT
- RETURN_TO_CARE
- COMPARE_RELEASE_SITES
- DOCUMENT_REUNION
- CLOSE_MONITORING

Avoid generic `RELEASE_POKEMON` when the mechanical/custody transition is not authoritative.

## 18. Minecraft/Cobblemon boundary

Minecraft may display:

- rehabilitation enclosure;
- temporary acclimation pen;
- feeding/water support;
- observation hide;
- monitoring station;
- visible closure signs;
- persistent Pokémon entity when loaded;
- release-site environmental revision.

Minecraft may not decide:

- readiness;
- ownership;
- release legality;
- survival outcome;
- habituation;
- dependency;
- exact home range;
- return/failure status;
- population establishment;
- release-site suitability.

Entity despawn is not death, migration or failed release.

## 19. Encounter contract — Release Site Evacuation

Narrative premise:

A planned release window is disrupted by a separate hazard or hostile incident. Staff need to protect the release candidate and leave the site without turning the Pokémon into a battle asset.

FULL dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING for staff/candidate evacuation and protected routes;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when exact statuses are used;
- terrain/weather/hazards/zones/reactions: BLOCKING if the disrupting hazard changes tactics;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `PROTECT_CANDIDATE`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED:

The protocol pauses release. World state moves the candidate and staff to a safe location before combat. AutoPTU resolves a static conventional encounter elsewhere. Release readiness and authorization remain unchanged unless the hazard itself changes site evidence afterward.

## 20. Encounter contract — Telemetry Retrieval at Ridge

Narrative premise:

A monitoring device stops reporting after a released Pokémon was last observed near a difficult ridge. The objective is to recover or inspect the device and determine what can actually be concluded.

FULL dependencies:

- VERIFIED baseline targeting/base movement/core/action/AI legality;
- complete movement: BLOCKING if traversal, escort or dynamic withdrawal matters;
- terrain/weather/hazards/zones/reactions: BLOCKING if cliffs, weather or unstable terrain have tactical effects;
- AI tactical policy: BLOCKING for `REACH_DEVICE`, `PROTECT_RESEARCHER`, `WITHDRAW`;
- adapter/playback: BLOCKING;
- exact Move/Ability/Item/Feature families remain PARTIAL when invoked.

REDUCED:

Travel/Wayfinding resolves the field approach outside battle. If a separate confrontation occurs, the team fights on a static safe map. The recovered device then feeds Visual Records/Metrology/Monitoring. A broken device produces `MONITORING_GAP`, not a conclusion about the Pokémon.

## 21. Encounter contract — Return to the Rehabilitation Yard

Narrative premise:

A previously released Pokémon appears again at the facility during a period of heavy visitor activity. Staff need to preserve space while determining whether the return indicates distress, ordinary route use, attraction to a resource or something unresolved.

FULL dependencies:

- complete movement: BLOCKING for crowd/wildlife rerouting;
- AI tactical policy: BLOCKING for non-hostile `WITHDRAW`, `REACH_SAFE_AREA`, `CLEAR_ROUTE` behavior;
- adapter/playback: BLOCKING for crowds, gates and semantic objectives;
- environmental family only if a real validated hazard is present.

REDUCED:

Public Space/Facility state redirects visitors first. Staff observe without forcing capture. Any independent hostile encounter occurs on a separate static arena. The Pokémon's return remains an observation until Care/Conservation/Pokémon Agency review it.

## 22. Non-combat scenario — Release Readiness Review

No battle engine dependency.

Reviewers compare:

- care summary;
- behavioral observations;
- site conditions;
- origin/location evidence;
- current population/collective state;
- biosecurity findings;
- monitoring capacity;
- previous release attempts;
- unresolved risks.

Valid outcomes include READY, READY_WITH_SUPPORT_CANDIDATE, NOT_READY, NEEDS_MORE_EVIDENCE or PAUSED_FOR_SITE_REASON.

The meeting should be able to end without generating a field quest.

## 23. Anti-exploit rules

- Repeated admission/release does not generate reputation or rewards by count.
- A player cannot force a release candidate into party state through proximity or care history.
- Feeding a wild patient does not create Loyalty.
- Building a pen does not create a spawn point.
- Destroying a monitoring device does not erase the Pokémon's history.
- Recapture for care cannot be used to manufacture new capture rewards.
- Release-site rarity cannot create capture bonuses.
- Post-release observations should be sparse enough to avoid turning telemetry into omniscient tracking.

## 24. Promotion gate

Before this protocol becomes canon, reviewers must decide:

- which institutions can operate rehabilitation programs;
- who has release/relocation authority;
- whether any formal release-readiness criteria are authored by region/species;
- what technology exists for telemetry/monitoring;
- how long records remain private;
- how post-release support is governed;
- how wild Pokémon custody works;
- exact PTU/Caelo capture/release/Loyalty/Command/Medicine interactions;
- Cobblemon persistent-entity semantics across release and unload/reload.

## Design outcome

A good release story does not end when a gate opens.

The world should remember why a Pokémon entered care, what evidence supported release, what was attempted, what was actually observed afterward and what remains unknown—while preserving the same individual and never inventing mechanics that belong to PTU/Caelo.