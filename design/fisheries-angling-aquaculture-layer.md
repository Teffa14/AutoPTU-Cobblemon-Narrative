# Fisheries, Angling & Aquaculture Layer — Pass 70

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU/Caelo mechanic is established by this document.

## Purpose

This layer models human/Pokémon use of aquatic populations without collapsing hydrology, ecology, fishing effort, capture, food production and conservation into one state.

Freshwater remains authoritative for water-system state. Maritime remains authoritative for sea lanes and vessels. Food remains authoritative for food batches and culinary provenance. Conservation remains authoritative for protected-area management. AutoPTU remains authoritative for battle and capture mechanics.

## Core separation

Keep these separate:

- aquatic population or collective state;
- fishing/angling effort;
- encounter method;
- observed catch;
- retained/released/captured outcome;
- harvest/resource batch;
- fishery-management decision;
- hatchery/aquaculture production state;
- stocking/release intervention;
- public belief;
- tactical PTU state.

A low catch rate does not prove a population decline.

A caught Pokémon is not automatically captured into a Trainer roster.

A stocked population is not automatically a restored wild population.

## FISHERY_PROFILE

```yaml
fishery_id: null
water_system_refs: []
maritime_region_refs: []
settlement_refs: []
target_population_refs: []
non_target_population_refs: []
operator_or_steward_ids: []
recreational_access_state: unknown
commercial_or_food_use_state: unknown
research_access_state: unknown
seasonal_rule_refs: []
current_management_measure_ids: []
observation_ids: []
history_refs: []
canon_status: proposed
```

A `FISHERY_PROFILE` is a coordination object. It does not imply ownership of the water, ownership of wild Pokémon or a particular legal system.

## FISHING_EFFORT_RECORD

```yaml
effort_record_id: null
fishery_id: null
actor_or_group_ids: []
start_time: null
end_time: null
method_ref: null
location_or_zone_id: null
gear_instance_refs: []
weather_ref: null
water_state_ref: null
effort_class: null
observation_refs: []
```

Possible coarse effort classes:

- INCIDENTAL
- LIGHT
- MODERATE
- HIGH
- EVENT_SURGE
- RESEARCH_SAMPLING

These labels support narrative comparison. They do not create catch probabilities.

## ANGLING_EVENT

```yaml
angling_event_id: null
effort_record_id: null
pokemon_entity_id: null
species_claim: null
encounter_method: rod|line|net|trap|hand|other
hooked_or_contacted: false
battle_ref: null
capture_ref: null
sample_ref: null
outcome: observed|escaped|released|captured|retained_resource|care_transfer|unknown
condition_observations: []
source_refs: []
```

The event records what happened. Mechanical capture remains an AutoPTU/PTU result when applicable.

## CATCH_OBSERVATION

Catch data is evidence, not population truth.

```yaml
catch_observation_id: null
fishery_id: null
time_window: null
zone_id: null
method_ref: null
effort_ref: null
species_or_collective_ref: null
count_or_class: null
size_or_stage_claims: []
release_count_or_class: null
retained_count_or_class: null
quality_flag: null
observer_ids: []
```

Repeated observations can support a stock assessment, but the assessment remains a versioned interpretation.

## STOCK_ASSESSMENT

```yaml
stock_assessment_id: null
population_ref: null
assessment_time: null
evidence_refs: []
assessment_method_ref: null
abundance_class: unknown
trend_claim: unknown
recruitment_claim: unknown
spawning_claim: unknown
uncertainty: null
reviewer_ids: []
status: draft|reviewed|superseded
```

Suggested abundance/trend labels stay coarse until canon provides stronger methods.

Never calculate exact stock size from loaded Cobblemon entities.

## MANAGEMENT_MEASURE

```yaml
management_measure_id: null
fishery_id: null
measure_type: seasonal_closure|zone_closure|method_restriction|effort_limit|research_only|safety_closure|other
objective_refs: []
scope_refs: []
start_time: null
end_condition: null
issuing_institution_ref: null
review_event_refs: []
public_notice_refs: []
```

The reason matters. A spawning closure, pollution closure and safety closure can look identical at a gate while having different consequences.

## BYCATCH_OR_NON_TARGET_EVENT

```yaml
non_target_event_id: null
fishery_id: null
effort_ref: null
pokemon_or_population_ref: null
contact_type: hooked|netted|disturbed|entangled|other
observed_condition: null
release_or_care_ref: null
case_ref: null
followup_refs: []
```

Do not infer Injury, Status or mortality without authoritative evidence.

## GEAR_AND_TECHNIQUE

Fishing gear should use material provenance and item authority.

```yaml
fishing_gear_instance:
  gear_id: null
  gear_type_claim: null
  mechanical_item_ref: null
  maker_ref: null
  material_provenance_refs: []
  owner_claim_refs: []
  current_custody_ref: null
  maintenance_refs: []
  local_technique_refs: []
  rules_validation_required: true
```

Local techniques can be traditions or learned practices without automatically granting a modifier.

## AQUACULTURE_SITE

```yaml
aquaculture_site_id: null
site_type: pond|hatchery|raceway|coastal_pen|research_facility|other
location_id: null
operator_ids: []
water_dependency_refs: []
infrastructure_refs: []
staffing_refs: []
stock_cohort_ids: []
care_case_refs: []
biosecurity_refs: []
capacity_state: unknown
current_cycle_state: null
```

No exact growth rate, density, feed requirement or production yield is implied.

## CULTURE_COHORT

```yaml
culture_cohort_id: null
aquaculture_site_id: null
species_ref: null
individual_pokemon_ids: []
origin_refs: []
parentage_refs: []
start_time: null
life_stage_claim: null
health_signal_refs: []
intended_outcome: care|research|release|food_resource|unknown
current_count_class: null
```

Named or narratively important Pokémon remain individual entities. Background cohorts can remain coarse.

## STOCKING_RELEASE_EVENT

```yaml
stocking_event_id: null
source_site_id: null
source_cohort_id: null
release_location_id: null
release_time: null
released_individual_ids: []
released_count_class: null
objective_refs: []
monitoring_plan_ref: null
biosecurity_review_ref: null
pokemon_agency_review_ref: null
```

Release is an intervention. It does not set `restoration_success = true`.

## POST_RELEASE_MONITORING

Track later evidence:

- tagged or individually identified returns;
- survival observations;
- habitat use;
- movement;
- reproduction claims;
- interaction with wild cohorts;
- fishing vulnerability;
- unexpected ecological effects.

A hatchery-origin Pokémon can later become part of a wild collective while retaining provenance.

## SPAWNING_WINDOW

```yaml
spawning_window_id: null
population_ref: null
location_refs: []
seasonality_refs: []
observed_behavior_refs: []
expected_window_ref: null
current_confidence: null
management_measure_refs: []
```

Do not infer spawning only from calendar date. Use authored ecology plus observation.

## FOOD / RESOURCE HANDOFF

When aquatic material becomes food or another resource, create a provenance handoff into the Food/Material layer.

Do not treat a Pokémon entity and a food batch as the same object.

Veluza-like naturally discarded biological material is especially important: resource provenance may exist without capture, ownership transfer or death.

## TOURNAMENT_OR_FESTIVAL_FISHING

Fishing events can plug into Public Events and Sports/Competition layers.

Keep separate:

- participation eligibility;
- fishing effort;
- official score/result;
- capture/retention outcome;
- public reception;
- ecological pressure;
- post-event monitoring.

A competition should not automatically grant access to protected populations.

## PLAYER KNOWLEDGE

A player can know:

- local fishers report fewer bites;
- a tagged individual was seen downstream;
- a closure notice is active;
- a hatchery release occurred;

without knowing the actual stock trend.

Use the existing knowledge/provenance layers.

## Minecraft/Cobblemon projection

Minecraft may render:

- fishing locations;
- boats;
- hatchery ponds;
- fishers;
- nets/gear as props;
- visible Pokémon samples;
- closures/signs;
- release events;
- market or festival activity.

Minecraft must not become the source of truth for:

- stock abundance;
- spawning success;
- capture legality;
- fishery quotas;
- hatchery production;
- catch probability;
- ecological recovery.

## PTU/Caelo boundary

This layer does not define:

- rod/bait bonuses;
- Fishing Skill checks;
- Survival DCs;
- capture modifiers;
- hooked/grappled effects;
- net attacks;
- fish-size mechanics;
- food yields;
- hatchery growth;
- stocking bonuses;
- aquatic Trainer Features.

Those require exact PTU/Caelo source extraction and engine evidence.

## Encounter contract A — Spawning Reach Closure

Narrative premise: a seasonal closure is active after repeated spawning observations. A public event upstream creates pressure on the closed reach.

Full version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — BLOCKING if actors cross or withdraw dynamically
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if exact effects occur
- terrain/weather/hazards/zones/reactions — BLOCKING for protected zones/current-sensitive movement
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Resolve closure compliance, visitors and aquatic movement in overworld state. If conflict becomes battle, freeze a static shoreline map and include only real combatants. The spawning area is narrative/world state, not a damaging or movement-modifying zone.

## Encounter contract B — Hatchery Intake Failure

Narrative premise: a hatchery intake stops functioning during a release window. Staff need access while wild Pokémon gather around altered flow.

Full version adds dynamic water/interaction objectives and therefore depends on terrain/weather/hazards/zones/reactions, tactical AI and adapter/playback.

Reduced version:

Resolve the intake asset through Infrastructure/Freshwater state before combat. Use a stable arena if wild behavior becomes confrontational. No water-current damage or automatic status effects.

## Encounter contract C — Fishing Festival Overflow

Narrative premise: a popular annual fishing event creates more effort than expected and produces unusual catch observations.

Full version can eventually support moving boats, multiple noncombatants, fishing objectives and withdrawal behavior. Those require complete movement, objective-aware tactical AI and adapter support.

Reduced version:

Run the competition as an overworld/event system. Store effort and catch observations. Open AutoPTU only for a discrete legal battle. Official event scoring remains outside the battle transcript.

## Canon promotion gate

Before any fishery becomes canon, review:

- target populations and ecology;
- local fishing culture;
- ownership/access assumptions;
- capture/harvest rules;
- conservation conflicts;
- Food-system implications;
- Biosecurity implications;
- PTU/Caelo mechanics;
- Cobblemon projection feasibility.
