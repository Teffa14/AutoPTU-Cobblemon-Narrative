# Ouros Island Biogeography, Endemism & Dispersal Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

This layer models islands and archipelagos as persistent ecological systems whose populations can differ because of isolation, habitat, history, dispersal, disturbance and human movement.

It does not define species, regional forms, evolution methods, encounter rarity, capture legality, Swim/Sky travel, ferry rules, migration speed, genetics, speciation, population equations or Minecraft spawn mechanics.

Those remain under authored canon, PTU/Caelo authority, existing world-state layers and implementation evidence.

## 1. Responsibility boundary

This layer owns:
- island and archipelago ecological identity;
- survey coverage by island/habitat;
- occupancy histories;
- colonization/recolonization evidence;
- local extirpation assessments;
- endemism assessments;
- stepping-stone function;
- within-archipelago differentiation claims;
- dispersal-path hypotheses;
- cross-island comparison records.

Other layers remain authoritative for:
- sea lanes and vessels: Maritime;
- pelagic conditions: Open Ocean;
- human-assisted introduction and translocation: Biosecurity;
- protected-area decisions: Conservation;
- individual Pokémon identity: Pokémon Agency;
- wild population/collective behavior: Wild Collective Agency;
- weather/seasonality: Meteorology and Seasonality;
- regional permissions and recognition: Interregional Mobility / Credentials;
- physical island formation: Geology / Volcanism / Coastal Geomorphology;
- tactical resolution: AutoPTU-Java.

## 2. Archipelago identity

```yaml
archipelago:
  archipelago_id: null
  parent_region_id: null
  island_ids: []
  maritime_region_ids: []
  open_ocean_region_ids: []
  major_current_refs: []
  seasonal_cycle_ids: []
  public_map_ids: []
  research_program_ids: []
  conservation_program_ids: []
  biosecurity_case_ids: []
  historical_record_ids: []
```

An archipelago is a coordination object. It does not imply:
- one government;
- one culture;
- one League authority;
- one climate;
- one habitat type;
- one encounter table;
- one shared population of every species.

## 3. Island ecological profile

```yaml
island_ecology_profile:
  island_id: null
  archipelago_id: null
  area_class: null
  isolation_context: null
  habitat_unit_ids: []
  freshwater_refs: []
  coastal_refs: []
  elevation_refs: []
  settlement_ids: []
  harbor_ids: []
  transport_connection_ids: []
  survey_program_ids: []
  population_occurrence_ids: []
  introduced_population_ids: []
  protected_area_ids: []
  last_revision_event_id: null
```

`area_class` and `isolation_context` are descriptive categories, not formulas.

Candidate area classes:
- ISLET
- SMALL_ISLAND
- MEDIUM_ISLAND
- LARGE_ISLAND
- COMPLEX_ISLAND

Candidate isolation contexts:
- NEAR_NEIGHBOR
- INNER_CHAIN
- OUTER_CHAIN
- REMOTE
- SEASONALLY_CONNECTED
- HUMAN_CONNECTED
- UNKNOWN

These labels must not directly modify spawn rates or encounter levels.

## 4. Survey effort is separate from ecological truth

```yaml
island_survey_effort:
  survey_id: null
  island_id: null
  habitat_unit_ids: []
  start_time: null
  end_time: null
  observer_ids: []
  method_refs: []
  target_taxa_or_species: []
  effort_class: null
  coverage_notes: null
  detection_limitations: []
  source_record_ids: []
```

Candidate effort classes:
- INCIDENTAL
- RAPID
- PARTIAL
- SEASONAL
- REPEATED
- LONG_TERM
- COMPREHENSIVE_FOR_SCOPE

A species absent from a low-effort survey is not absent from the island.

## 5. Population occurrence

```yaml
island_population_occurrence:
  occurrence_id: null
  species_id: null
  population_id: null
  island_id: null
  habitat_unit_ids: []
  first_confirmed_event_id: null
  last_confirmed_event_id: null
  current_assessment: null
  seasonal_pattern_ref: null
  abundance_assessment_ref: null
  provenance_ids: []
  uncertainty_notes: null
```

Candidate current assessments:
- PRESENT_CONFIRMED
- PRESENT_SEASONAL
- PRESENT_INTERMITTENT
- PRESENCE_UNCERTAIN
- NOT_RECENTLY_DETECTED
- LOCALLY_EXTIRPATED_PROVISIONAL
- LOCALLY_EXTIRPATED_CONFIRMED
- HISTORICAL_ONLY
- UNKNOWN

`LOCALLY_EXTIRPATED_CONFIRMED` must require a reviewed assessment. Procedural generation cannot set it from a short absence.

## 6. Colonization and recolonization evidence

```yaml
colonization_case:
  colonization_case_id: null
  species_or_population_ref: null
  destination_island_id: null
  earliest_evidence_ids: []
  prior_absence_evidence_ids: []
  candidate_pathway_ids: []
  natural_dispersal_hypothesis_ids: []
  human_assisted_hypothesis_ids: []
  confidence_state: null
  establishment_assessment_id: null
  review_event_ids: []
```

A first observation is not automatically a colonization event.

Required question:
Was the population newly arrived, newly detectable or simply previously missed?

## 7. Dispersal pathway

```yaml
dispersal_pathway:
  pathway_id: null
  origin_area_ids: []
  destination_area_ids: []
  intermediate_area_ids: []
  pathway_type: null
  evidence_ids: []
  species_scope: []
  season_refs: []
  weather_refs: []
  oceanography_refs: []
  human_transport_refs: []
  confidence: null
```

Candidate pathway types:
- DIRECT_FLIGHT
- COASTAL_HOP
- OPEN_WATER_SWIM
- CURRENT_ASSISTED
- RAFTING_OR_FLOATING
- STORM_DISPLACEMENT
- STEPPING_STONE
- HUMAN_TRANSPORT_POSSIBLE
- HUMAN_TRANSPORT_CONFIRMED
- UNKNOWN

These labels are ecological hypotheses. They do not grant PTU capabilities.

## 8. Stepping-stone island/site

A small island can matter without supporting a permanent large population.

```yaml
stepping_stone_function:
  stepping_stone_id: null
  site_id: null
  archipelago_id: null
  species_or_population_refs: []
  function_type: null
  observed_use_ids: []
  seasonal_window_ids: []
  dependency_strength: unknown
  alternative_site_ids: []
  current_condition_ref: null
```

Candidate function types:
- RESTING
- ROOSTING
- FEEDING
- NESTING
- FRESHWATER_ACCESS
- SHELTER
- CURRENT_BREAK
- REEF_REFUGE
- UNKNOWN

One observed use does not prove regional dependency.

## 9. Endemism assessment

```yaml
endemism_assessment:
  endemism_assessment_id: null
  taxon_or_population_ref: null
  geographic_scope: null
  assessment_type: null
  supporting_survey_ids: []
  historical_record_ids: []
  comparison_region_ids: []
  unresolved_range_questions: []
  confidence: null
  reviewer_ids: []
  revision_history_ids: []
```

Candidate assessment types:
- ISLAND_ENDEMIC_CANDIDATE
- ISLAND_ENDEMIC_SUPPORTED
- ARCHIPELAGO_ENDEMIC_CANDIDATE
- ARCHIPELAGO_ENDEMIC_SUPPORTED
- LOCALLY_DISTINCT_POPULATION
- RANGE_LIMITED_WITHIN_REGION
- INSUFFICIENT_DATA

Important:
`endemic` is a geographic assessment, not a rarity tier or mechanical tag.

No mechanical consequence follows automatically from endemism.

## 10. Population differentiation claim

Nearby islands may support populations that differ in behavior, timing, morphology or resource use.

```yaml
population_differentiation_claim:
  claim_id: null
  species_id: null
  population_a_id: null
  population_b_id: null
  observed_difference_type: null
  evidence_ids: []
  alternative_explanations: []
  mechanical_species_difference_ref: null
  status: HYPOTHESIS
```

Candidate difference types:
- ACTIVITY_TIMING
- RESOURCE_USE
- HABITAT_USE
- MIGRATION_TIMING
- BODY_SIZE_OBSERVATION
- COLOR_OR_MARKING_OBSERVATION
- VOCALIZATION_PATTERN
- SOCIAL_PATTERN
- FORM_CONFIRMED_BY_AUTHORITY
- OTHER

Only `FORM_CONFIRMED_BY_AUTHORITY` can point to a recognized form/mechanical species record.

The narrative system cannot invent a new form from repeated visual differences.

## 11. Local extinction and turnover

Island populations can disappear locally without the species becoming globally extinct.

```yaml
local_extirpation_assessment:
  assessment_id: null
  population_id: null
  island_id: null
  baseline_refs: []
  last_confirmed_event_id: null
  search_effort_ids: []
  candidate_cause_ids: []
  status: PROVISIONAL
  review_ids: []
```

Candidate status:
- PROVISIONAL
- STRONGLY_SUPPORTED
- CONFIRMED_BY_CANON_REVIEW
- REVERSED_AFTER_REDETECTION

A future rediscovery does not erase the historical assessment. It creates a new revision.

## 12. Recolonization

```yaml
recolonization_event:
  event_id: null
  population_or_species_ref: null
  island_id: null
  detection_ids: []
  possible_source_island_ids: []
  pathway_hypothesis_ids: []
  establishment_state: unknown
  monitoring_plan_id: null
```

Natural recolonization and assisted reintroduction must remain separate.

Biosecurity owns assisted movement by people or institutions.

## 13. Natural versus human-assisted arrival

The system should support competing hypotheses.

Example:
- storm-carried arrival;
- repeated natural dispersal;
- ferry cargo hitchhiker;
- intentional release;
- old population missed by surveys.

No hypothesis becomes truth merely because it is narratively dramatic.

## 14. Archipelago comparison project

```yaml
archipelago_comparison_project:
  project_id: null
  research_program_id: null
  island_ids: []
  comparison_dimensions: []
  standardized_method_refs: []
  dataset_ids: []
  current_claim_ids: []
  null_result_ids: []
  public_output_ids: []
```

Useful dimensions:
- occupancy;
- seasonal timing;
- habitat use;
- resource use;
- local abundance;
- nesting/roost use;
- behavioral observations;
- introduced-species pressure;
- restoration response.

## 15. Island-specific baselines

Do not force every island to share one regional baseline.

A reasonable architecture is:

`archipelago baseline`
+ `island baseline`
+ `habitat baseline`
+ `seasonal revision`
+ `current observation`.

This lets two islands experience the same storm but produce different consequences.

## 16. Natural dispersal must not become a capability shortcut

Narrative statement:
`this species appears to move among islands`.

Mechanical conclusion:
unknown until validated.

Possible mechanisms may include:
- individual Sky/Swim movement;
- long-distance behavior not represented by battle movement values;
- drifting/rafting;
- storm displacement;
- transport by another organism;
- human movement;
- historical colonization with no current exchange.

Therefore:
`species observed on islands A and B` does not imply `individual can travel A <-> B on demand`.

## 17. Island forms and mechanical identity

Regional/form differences must be authoritative data.

Pass 89 may record:
- observed local appearance;
- local ecological association;
- historical claims;
- suspected differentiation;
- confirmed mechanical form ID if external authority already defines it.

Pass 89 cannot create:
- new Type;
- new Ability;
- new base stats;
- new Move access;
- new evolution method;
- new regional form;
- new species.

## 18. Integration with Biosecurity

Natural arrival and introduced arrival can look similar at first.

When human-assisted arrival becomes plausible, create or link a Biosecurity case.

The same occurrence can therefore have:
- an island occupancy record;
- a colonization case;
- a Biosecurity pathway hypothesis;
- a conservation assessment;
- a public rumor.

They remain separate records.

## 19. Integration with Conservation

Conservation can consume:
- endemism assessments;
- stepping-stone function;
- extirpation risk;
- survey gaps;
- assisted-colonization proposals;
- habitat condition.

Conservation decides management actions.

Pass 89 does not create access bans or capture restrictions itself.

## 20. Integration with Maritime and Open Ocean

Maritime supplies:
- routes;
- harbors;
- vessels;
- service state.

Open Ocean supplies:
- pelagic conditions;
- large-scale water context;
- current/sea-state observations when available.

Pass 89 may consume those states as evidence for connectivity hypotheses.

It must not overwrite them.

## 21. Integration with Seasonality and Weather

Some inter-island occupancy may be seasonal.

A missing population may be explained by:
- phenology;
- migration timing;
- weather displacement;
- temporary habitat loss;
- survey timing.

Therefore seasonal context is required before declaring extirpation.

## 22. Player knowledge

Each player can have a different archipelago map and ecological understanding.

Possible knowledge states:
- island known, habitat unsurveyed;
- population rumored;
- population observed once;
- repeated surveys completed;
- endemism candidate known;
- reviewed scientific assessment known;
- sensitive coordinates redacted.

Multiplayer sharing must use Communications/Science permissions rather than global knowledge teleportation.

## 23. Minecraft projection

Minecraft should represent current state through:
- island geometry;
- habitat mosaics;
- visible settlements;
- selected persistent Pokémon entities;
- coarse population projection;
- field stations;
- signs/maps;
- seasonal variants;
- protected or research infrastructure where canon supports it.

Loaded entities are presentation, not population truth.

Despawning a Pokémon does not create local extinction.

Spawning one Pokémon does not prove colonization.

## 24. Cobblemon projection and anti-exploit rule

Future spawn projection should consume server-side population state.

Players must not be able to manufacture an endemic population by:
- repeatedly loading chunks;
- moving blocks;
- planting one resource patch;
- releasing one Pokémon;
- parking a boat;
- forcing despawns;
- farming encounter rerolls.

Any ecological response should use coarse state, revision windows and anti-exploit thresholds.

## 25. World-time advancement

Island occupancy can advance offline only through coarse events.

Examples:
- seasonal arrival window opens;
- survey window closes;
- storm creates a plausible dispersal event;
- habitat restoration reaches review date;
- no detections accumulate across repeated independent surveys.

Do not simulate every individual crossing every hour.

## 26. Quest generation hooks

Strong quest hooks include:
- compare the same species on three islands;
- determine whether a new observation is colonization or survey gap;
- restore a stepping-stone site;
- verify a suspected local extirpation;
- map a seasonal island occupancy pattern;
- investigate whether a ferry route is a dispersal pathway;
- monitor a population after natural recolonization;
- evaluate a proposed assisted colonization with Conservation/Biosecurity;
- resolve two maps that disagree because their surveys occurred in different years.

## 27. Encounter contract A — Stepping-Stone Survey

Narrative premise:
A small uninhabited island may be an important seasonal stopover for a flying or marine population.

Reduced version:
- survey/arrival state is resolved in overworld;
- the battle map is a static coastal/rocky arena;
- only Pokémon actually involved in conflict enter AutoPTU;
- migration and departure remain world-state outcomes.

Full version may require:
- complete movement including interception/forced movement if actors cross through the arena;
- terrain/weather/hazards/zones/reactions if surf, wind or changing access matter tactically;
- AI tactical policy for WITHDRAW/REACH_EXIT/PROTECT_SITE;
- Minecraft/Cobblemon/Craftics adapter/playback.

## 28. Encounter contract B — Recolonization Shore

Narrative premise:
A species absent from an island for years is detected again, but the party does not yet know whether the population is established.

Reduced version:
- observation, provenance and population inference happen outside battle;
- if a confrontation occurs, AutoPTU receives a static arena and normal combatants;
- battle result never decides population establishment by itself.

Full version may require:
- movement objectives for withdrawal/escape;
- tactical AI that values leaving rather than KO;
- terrain/weather/hazards if shoreline conditions are mechanically active;
- adapter playback.

## 29. Encounter contract C — Channel Crossing Window

Narrative premise:
A short channel between two islands becomes temporarily usable by a population during a recurring seasonal window.

Reduced version:
- Seasonality/Open Ocean determines the window before combat;
- crossing population movement remains world state;
- any battle uses one frozen snapshot on one side of the crossing.

Full version may require:
- complete movement;
- dynamic water/terrain/weather/zones;
- AI tactical policy for CROSS/WITHDRAW/PROTECT;
- adapter/playback.

## 30. Permanent capability dependency map

VERIFIED for reduced static-battle versions:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when invoked by ordinary combat:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for mechanically rich island-crossing encounters:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## 31. PTU/Caelo guardrails

Before using a concrete mechanic, verify exact text and implementation for:
- Sky;
- Swim;
- Naturewalk;
- Mountable;
- Teleporter;
- capture;
- release;
- relocation/translocation;
- survival/navigation;
- weather;
- terrain;
- any species-specific movement or travel capability.

The complete primary Caelo corpus was not reliably accessible in this runtime. This design does not assert Caelo-specific island mechanics.

## 32. Canon promotion gate

Before promoting island ecology into canon, require:
1. island geography approved;
2. population/species identity approved;
3. provenance attached;
4. natural vs human-assisted arrival reviewed;
5. endemism wording reviewed;
6. no invented Pokémon mechanics;
7. conservation implications reviewed;
8. Cobblemon projection separated from truth state;
9. battle dependencies classified;
10. contradictory historical records preserved rather than silently overwritten.

## 33. Core design principle

An island should not be a biome-shaped container of spawns.

It should be a place with a history of arrivals, disappearances, isolated populations, repeated surveys, local resources, uncertain connections and changing relationships with the rest of the archipelago.