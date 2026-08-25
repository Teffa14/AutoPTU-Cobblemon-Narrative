# Ouros Managed Fisheries & Aquatic Harvest Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

This layer owns managed aquatic harvest, recreational fishing pressure, catch/release records, fishery-dependent monitoring, stock-assessment revisions and scoped management decisions.

It exists because several earlier systems intentionally stop at its boundary:

- Freshwater owns rivers, flows, reservoirs and surface/groundwater links.
- Lake Limnology owns bathymetry, water-column state, turnover, oxygen, transparency and ecological observations. It explicitly reserves harvest/access policy for Fisheries.
- Estuaries owns tidal/salinity state.
- Maritime/Open Ocean own marine routes and pelagic/coastal physical context.
- Migration owns recurring population movement and stopovers.
- Conservation owns population/ecological stewardship outside the harvest-management process.
- Wild Collectives owns persistent group identity.
- Pokémon Agency owns individual Pokémon identity, capture, partnership, custody and agency.
- Food, Supply Chains and Markets own downstream food/material/commodity state only after an authorized handoff exists.

The layer does not establish whether Ouros societies harvest Pokémon for food, whether only non-Pokémon aquatic resources are harvested, or whether some fisheries are exclusively catch-and-release. Those are canon decisions.

## Core authority chain

Use this chain:

`population/ecological observations -> fishery activity + effort -> assessment revision -> management objective -> scoped control -> interaction/harvest records -> landing/release disposition -> downstream handoff -> monitoring -> later assessment`

Never collapse this to:

`catch count -> population size -> quota`.

## 1. Fishery management unit

A management unit is an institutional/ecological scope, not automatically a biological species or a legal jurisdiction.

```yaml
fishery_management_unit:
  fishery_unit_id: null
  name: null
  subject_species_refs: []
  subject_population_refs: []
  habitat_system_refs: []
  migration_pattern_refs: []
  spatial_scope_ref: null
  participating_institution_refs: []
  management_objective_refs: []
  assessment_revision_refs: []
  control_revision_refs: []
  activity_history_refs: []
  landing_site_refs: []
  confidence_in_unit_definition: provisional
  source_refs: []
```

Possible unit interpretations:

- LOCAL_WATERBODY
- RIVER_REACH
- ESTUARY_COMPLEX
- COASTAL_STOCK
- MIGRATORY_STOCK
- MULTISPECIES_FISHERY
- RECREATIONAL_ACTIVITY_AREA
- TRADITIONAL_HARVEST_AREA
- DATA_LIMITED_PROVISIONAL_UNIT
- UNKNOWN

A management unit can later be split or merged without rewriting old records.

## 2. Biological stock claims versus management units

Do not assume `fishery_management_unit == biological_population`.

```yaml
stock_identity_claim:
  claim_id: null
  fishery_unit_id: null
  proposed_population_refs: []
  claim_type: ONE_STOCK
  evidence_refs: []
  conflicting_claim_refs: []
  confidence: null
  valid_from_event_id: null
  supersedes_claim_id: null
```

Candidate claim types:

- ONE_STOCK
- MULTIPLE_STOCKS
- MIXED_STOCK
- SEASONALLY_MIXED
- MANAGEMENT_PROXY_ONLY
- UNKNOWN

Taxonomy, Conservation Genetics, Migration and Island Biogeography may contribute evidence. Fisheries does not invent new species/forms or biological populations.

## 3. Fishery activity

An activity record describes what people attempted, not what exists in the ecosystem.

```yaml
fishery_activity:
  activity_id: null
  fishery_unit_id: null
  activity_type: null
  started_at: null
  ended_at: null
  actor_or_group_refs: []
  vessel_or_site_refs: []
  method_or_gear_ref: null
  effort_record_ref: null
  location_scope_ref: null
  target_claim_refs: []
  interaction_refs: []
  landing_refs: []
  observer_or_monitor_refs: []
  weather_context_ref: null
  water_state_refs: []
  source_refs: []
```

Candidate activity types:

- RECREATIONAL_ANGLING
- SCIENTIFIC_SAMPLING
- SUBSISTENCE_HARVEST
- COMMERCIAL_HARVEST
- COMMUNITY_EVENT
- EMERGENCY_RESOURCE_USE
- NON_EXTRACTIVE_SURVEY
- UNKNOWN

A category exists only if canon permits it in that region.

## 4. Effort record

Catch without effort is incomplete evidence.

```yaml
fishery_effort_record:
  effort_id: null
  activity_id: null
  duration_band: null
  participant_count_band: null
  vessel_count_band: null
  method_or_gear_ref: null
  deployment_count_band: null
  distance_or_area_sampled_band: null
  search_time_band: null
  environmental_context_refs: []
  reporting_completeness: unknown
  confidence: null
```

The simulation should usually use qualitative bands unless exact numbers materially matter.

Possible bands:

- VERY_LOW
- LOW
- MODERATE
- HIGH
- VERY_HIGH
- UNKNOWN

Do not calculate stock abundance directly from a Minecraft count, catch count or one effort record.

## 5. Interaction record

Each encounter with an aquatic organism is separate from final disposition.

```yaml
fishery_interaction:
  interaction_id: null
  activity_id: null
  observed_subject_ref: null
  species_or_taxon_claim_ref: null
  persistent_pokemon_entity_id: null
  target_status: TARGET | NON_TARGET | UNKNOWN
  interaction_method_ref: null
  condition_observation_refs: []
  disposition_ref: null
  evidence_refs: []
  confidence: null
```

This supports non-target/bycatch records without labeling the subject a pest.

## 6. Disposition and release

```yaml
fishery_disposition:
  disposition_id: null
  interaction_id: null
  state: null
  occurred_at: null
  location_ref: null
  handling_observation_refs: []
  custody_handoff_ref: null
  later_observation_refs: []
  source_refs: []
```

Candidate states:

- RELEASED_AT_SITE
- RELEASED_ELSEWHERE_AUTHORIZED
- LANDED_RESOURCE
- SCIENTIFIC_SAMPLE_HANDOFF
- CAPTURE_PROCESS_REFERRED_TO_POKEMON_AGENCY
- ESCAPED_OR_LOST_CONTACT
- UNKNOWN

`RELEASED_AT_SITE` does not mean `KNOWN_UNHARMED`.

If the subject is a Pokémon, capture/ownership/custody belongs to Pokémon Agency. A fishery disposition can refer the interaction to that system but cannot create ownership.

## 7. Landing record

A landing is a recorded handoff from fishery activity into downstream resource systems.

```yaml
fishery_landing:
  landing_id: null
  fishery_unit_id: null
  activity_id: null
  landed_at: null
  landing_site_ref: null
  resource_batch_refs: []
  reported_quantity_band: null
  verified_quantity_band: null
  species_composition_claim_refs: []
  provenance_refs: []
  receiving_system_refs: []
  documentation_state: null
```

Potential downstream authorities:

- Food/Food Safety
- Supply Chains
- Markets
- Material Culture
- Science/Museums for authorized samples

This object remains dormant for Pokémon-as-food or other sensitive uses unless Ouros canon explicitly establishes them.

## 8. Independent survey record

Fisheries needs evidence that does not originate from ordinary harvest activity.

```yaml
fishery_independent_survey:
  survey_id: null
  fishery_unit_id: null
  method_ref: null
  sampling_design_ref: null
  started_at: null
  ended_at: null
  station_or_transect_refs: []
  effort_ref: null
  observation_refs: []
  environmental_context_refs: []
  coverage_assessment: null
  limitations: []
  source_refs: []
```

Methods may be extractive or non-extractive, but the layer does not invent their PTU mechanics.

## 9. Stock assessment revision

An assessment is an interpretation of available evidence, not hidden omniscient truth.

```yaml
stock_assessment_revision:
  assessment_revision_id: null
  fishery_unit_id: null
  assessment_date: null
  method_family: null
  input_activity_refs: []
  input_survey_refs: []
  biological_observation_refs: []
  ecosystem_context_refs: []
  abundance_assessment_band: unknown
  recruitment_assessment_band: unknown
  harvest_pressure_assessment_band: unknown
  confidence: null
  major_data_gaps: []
  alternative_interpretation_refs: []
  review_state: null
  supersedes_revision_id: null
```

Suggested method families:

- DATA_LIMITED
- INDEX_BASED
- MULTI_INDEX
- DEMOGRAPHIC_STRUCTURED
- EXPERT_SYNTHESIS
- UNKNOWN

Do not expose exact stock numbers unless the fiction and methodology support them.

## 10. Catch/effort index

A catch-per-effort style index can exist as an institution-produced observation.

```yaml
catch_effort_index_revision:
  index_revision_id: null
  fishery_unit_id: null
  period_ref: null
  source_activity_refs: []
  standardization_method_ref: null
  effort_definition_ref: null
  index_band: null
  caveat_refs: []
  confidence: null
```

It must never be treated as a direct population counter.

Potential confounders include:

- different gear;
- changing target behavior;
- different sites;
- weather or water conditions;
- schooling/aggregation;
- improved experience/technology;
- reporting changes;
- closure effects;
- changed effort.

## 11. Management objective

```yaml
fishery_management_objective:
  objective_id: null
  fishery_unit_id: null
  objective_type: null
  adopted_at: null
  evidence_refs: []
  institution_refs: []
  review_window_ref: null
  status: ACTIVE
```

Possible objective types:

- MAINTAIN_MONITORING
- REDUCE_PRESSURE
- PROTECT_SPAWNING_WINDOW
- PROTECT_NON_TARGET_SPECIES
- SUPPORT_RECREATIONAL_ACCESS
- MAINTAIN_TRADITIONAL_USE
- REBUILD_DEPLETED_STOCK
- DATA_COLLECTION_FIRST
- TEMPORARY_CRISIS_RESPONSE

These labels do not establish laws or rights by themselves.

## 12. Scoped control revision

Do not model all fishery management as a quota.

```yaml
fishery_control_revision:
  control_revision_id: null
  fishery_unit_id: null
  control_type: null
  spatial_scope_ref: null
  temporal_scope_ref: null
  activity_scope_ref: null
  method_scope_ref: null
  subject_scope_refs: []
  rationale_claim_ref: null
  authority_ref: null
  effective_from: null
  effective_until: null
  review_event_ref: null
  supersedes_revision_id: null
```

Potential controls, only if canon authorizes them:

- MONITOR_ONLY
- TEMPORARY_AREA_CLOSURE
- SEASONAL_CLOSURE
- METHOD_RESTRICTION
- EFFORT_LIMIT
- BAG_OR_RETENTION_LIMIT
- CATCH_AND_RELEASE_ONLY
- RESEARCH_ONLY_ACCESS
- NO_HARVEST
- EMERGENCY_OPENING

A control can be valid institutionally even while its ecological rationale is later revised.

## 13. Spawning-run protection

Migration/Nesting/Lake/Estuary layers own observed reproductive or movement patterns. Fisheries may reference those observations when creating management controls.

Do not write:

`season = spring -> closure = true`

Use:

`observed recurring reproductive/movement pattern -> assessment -> authored management decision -> scoped control revision`

If phenology changes, the control may become mismatched and require review.

## 14. Non-target interactions and bycatch

```yaml
non_target_interaction_summary:
  summary_id: null
  fishery_unit_id: null
  period_ref: null
  interaction_refs: []
  affected_subject_refs: []
  method_or_gear_refs: []
  disposition_breakdown: []
  evidence_quality: null
  mitigation_refs: []
```

A non-target Pokémon interaction can create:

- monitoring;
- gear/method review;
- route changes;
- seasonal review;
- welfare follow-up;
- conservation handoff.

It does not make the Pokémon hostile or create capture rights.

## 15. Recreational and community fishing

Recreational fishing and public competitions can be managed as recurring activities separate from extractive harvest.

Link to:

- Festivals/Observances for event identity;
- Public Space for crowds and access;
- Markets for vendors;
- Public Memory for famous past catches or rivalries;
- Training/Education for demonstrations;
- Pokémon Agency for any actual capture.

A public competition can use an event-specific rule set without changing regional fishery policy.

## 16. Emergency resource use

A crisis can create a temporary authorized use of aquatic resources.

Record:

- why it began;
- scope;
- intended end condition;
- monitoring;
- downstream use;
- later review.

Do not let an emergency measure silently become permanent because players benefited once.

## 17. Fishery institutions and local knowledge

Fishers, harbor workers, researchers, market workers and residents can accumulate valuable observations.

Their claims remain evidence with provenance.

Examples:

- "the first run is later than it used to be";
- "we now need twice as long for the same landing";
- "this bay has been quiet since the storm";
- "the same marked individual appeared again".

None becomes scientific truth merely because the speaker is experienced. Conversely, institutional datasets do not automatically invalidate local longitudinal knowledge.

## 18. Persistent Pokémon identity

If a known Pokémon participates in a fishing interaction, preserve its `pokemon_entity_id`.

Possible chronology:

`observed in survey -> hooked/released -> re-observed next season -> later seen during migration -> later forms partnership`

The first release never creates custody. Later partnership never rewrites the earlier wild state.

## 19. Minecraft/Cobblemon projection

Minecraft is presentation and interaction input, not fishery authority.

Never infer from:

- loaded aquatic entity count;
- spawn density around players;
- fishing loot tables;
- bobber success;
- chunk unload/despawn;
- client-side particles;
- a chest of fish-like items;
- a player repeatedly fishing the same block;
- Cobblemon encounter tables alone.

Allowed direction:

`world fishery/ecology state -> coarse spawn/presentation choices when an authorized adapter exists`.

Forbidden direction:

`loaded/spawned/caught entities -> authoritative stock abundance`.

## 20. PTU fishing boundary

PTU 1.05 has an explicit Fishing procedure and Fishing Rod equipment. This layer does not replace those rules.

If an authored scene requires actual fishing mechanics, invoke the validated PTU procedure when the project has a tested authoritative path.

Until then:

- world-state fisheries can progress without simulating individual casts;
- an NPC report can describe fishing activity without running PTU checks;
- a player's attempt that materially requires Fishing mechanics must not be resolved by an invented Minecraft minigame;
- a fishing success roll must never write directly to stock abundance.

## 21. FULL and REDUCED encounter contract

Mechanically rich fisheries encounters should state both forms.

### FULL

May require:

- actors crossing or withdrawing through water;
- non-hostile wildlife objectives;
- protected lanes/areas;
- moving boats or equipment;
- dynamic currents/weather;
- tactical gear interactions;
- capture/release decisions;
- complex reactions.

Each required family must be individually validated.

### REDUCED

Resolve fishery/ecology operations first in world state:

- stop fishing activity;
- move civilians/workers out;
- release or secure non-target organisms outside the grid when no battle rule is needed;
- freeze water/boat/gear state;
- choose a static arena;
- battle only if a separate confrontation remains;
- resume management/research after the authoritative battle result.

The reduced version must preserve the narrative premise rather than replacing it with "defeat everything."

## 22. Explicit non-inferences

This layer does not authorize:

- Pokémon-as-food canon;
- killing wild Pokémon for ordinary resource loops;
- stock abundance from catch count;
- catch success from loaded spawns;
- capture eligibility from fishery access;
- ownership from landing;
- release survival from the word `released`;
- release injury from the word `hooked`;
- Water-type = fishery resource;
- aquatic Pokémon = edible;
- Swim = fishing proficiency;
- Schooling = fishery stock truth;
- Pack Mon = school behavior;
- capture/KO/despawn = population removal;
- fishing closure = spawning proof;
- spawning observation = automatic closure;
- fishing gear = PTU Item effect unless exact rules exist;
- nets/lines = Stuck/Trapped/Restrained without validated mechanics;
- water current = forced movement;
- rough water = Accuracy penalty;
- deep water = drowning;
- Minecraft fishing loot = resource provenance.

## 23. Canon promotion checklist

Before any fishery becomes canon, define at minimum:

- region/waterbody;
- subject resource/population;
- whether activity is recreational, scientific, subsistence, commercial or mixed;
- responsible institutions;
- legal/operational authority if any;
- what is known versus estimated;
- current assessment state;
- current controls;
- how Pokémon capture/agency is separated;
- downstream commodity rules if applicable;
- multiplayer authority;
- PTU/Caelo rules required for player-facing fishing actions.

## 24. Initial cross-layer handoffs

### Lake -> Fisheries

Lake supplies:
- bathymetry/depth context;
- temperature/oxygen profiles;
- turnover/bloom state;
- ecological observations.

Fisheries supplies:
- activity/effort;
- harvest/access controls;
- stock assessment interpretation.

### Migration -> Fisheries

Migration supplies:
- corridor/episode timing;
- stopover use;
- movement-wave observations.

Fisheries may create a scoped response, but does not rewrite the migration episode.

### Fisheries -> Conservation

Fisheries may report:
- pressure assessment;
- non-target interactions;
- stock concerns;
- monitoring gaps.

Conservation owns broader population/ecosystem stewardship.

### Fisheries -> Markets/Supply Chains/Food

Only an authorized landing/resource handoff creates downstream stock.

A market listing must never be used backwards to infer aquatic abundance.

### Fisheries -> Pokémon Agency

Any capture, partnership, custody or individual-Pokémon disposition must use Pokémon Agency.

## 25. Long-horizon value

This system is most useful when a fishery can become quieter and more competent over time.

A good five-year Chronicle may show:

- better surveys;
- fewer false conclusions from catch data;
- controls that adapt to migration timing;
- a recurring festival that continues safely;
- fewer non-target interactions;
- more reliable release observations;
- institutions resolving normal years without generating quests.

Success should reduce unnecessary crisis content rather than permanently escalate it.