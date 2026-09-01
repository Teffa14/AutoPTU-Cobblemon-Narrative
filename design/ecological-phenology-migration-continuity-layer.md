# Ouros Ecological Phenology & Migration Continuity Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Date: 2026-09-01
Research basis: `research/2026-09-01-ecological-phenology-migration-corridors-scan-178.md`

## Purpose

Ouros already stores individual observations, persistent wild collectives, seasonal route references, regional clocks and route state. This layer supplies the missing temporal ecology grammar that connects them.

It answers questions such as:
- When does a recurring ecological event usually happen?
- How confident is that expectation?
- Was the event genuinely absent, or merely not detected?
- Is a visible concentration a temporary aggregation, a persistent collective or an ordinary population sample?
- Which locations function as corridors, stopovers, roosts or observation stations at different times?
- Which human services should change temporarily because wildlife movement is expected?
- What can the player learn by repeating the same transect instead of fighting the first visible group?

It must never infer ecological truth from raw Cobblemon spawn density.

## 1. Ownership boundary

This layer extends existing systems instead of duplicating them.

Existing owner -> this layer consumes/produces:
- observation layer -> comparable observation series;
- wild-collective layer -> migration/aggregation state references;
- route layer -> corridor accessibility and temporary advisories;
- communications -> forecasts, warnings and corrections;
- local knowledge -> actor-specific expectations and uncertainty;
- public memory -> remembered first arrivals, unusual years and stewardship traditions;
- regional clocks -> bounded migration/aggregation windows when warranted;
- settlement/service systems -> temporary operating changes;
- AutoPTU encounter authority -> exact tactical participants only after an encounter is authorized.

## 2. Core distinctions

Permanent rules:

`OBSERVATION_SAMPLE != POPULATION_STATE`

`OBSERVED_COUNT != TRUE_ABUNDANCE`

`NOT_OBSERVED != CONFIRMED_ABSENCE`

`TEMPORARY_AGGREGATION != PERSISTENT_COLLECTIVE`

`MIGRATION_CORRIDOR != TERRITORY`

`SEASONAL_PATTERN != WEATHER_CAUSATION`

`FORECAST != WORLD_TRUTH`

`COBBLEMON_SPAWN != ECOLOGY_AUTHORITY`

## 3. Phenology record

Phenology describes recurring timing in biological/ecological events without requiring a rigid real-world calendar.

```yaml
ecological_phenology_record:
  phenology_id: null
  subject_type: null
  subject_refs: []
  event_type: null
  location_ids: []
  expected_time_band: null
  expected_season_or_calendar_refs: []
  candidate_environmental_correlates: []
  first_observed_event_ids: []
  latest_observed_event_ids: []
  observation_series_ids: []
  recurrence_model: unknown
  confidence: provisional
  uncertainty_reasons: []
  supersedes_phenology_id: null
  status: ACTIVE
```

Candidate `event_type` values:
- ARRIVAL
- DEPARTURE
- CORRIDOR_PASSAGE
- STOPOVER_USE
- ROOST_USE
- NEST_SITE_OCCUPANCY where supported
- DISPERSAL
- TEMPORARY_AGGREGATION
- FORAGING_PULSE
- RESOURCE_USE
- DAY_NIGHT_ACTIVITY_SHIFT
- FORM_OR_APPEARANCE_SHIFT where species canon supports it
- VOCALIZATION_WINDOW
- UNKNOWN_RECURRING_EVENT

Do not generate breeding/reproductive phenology merely because a group appears seasonally.

## 4. Comparable observation series

A time series is valid only if its observations preserve sampling context.

```yaml
ecological_observation_series:
  series_id: null
  subject_refs: []
  location_ids: []
  protocol_id: null
  observation_ids: []
  sampling_effort_records: []
  comparable_dimensions:
    time_of_day: true
    route_segment: true
    duration: true
    observer_method: true
    disturbance_band: true
    environmental_context: true
  known_protocol_changes: []
  interpretation_claim_ids: []
```

Examples of effort metadata:
- observation duration band;
- transect completed/partial;
- fixed-point watch versus moving survey;
- visibility/noise limitations;
- number of observers;
- equipment availability;
- player disturbance;
- ferry/road traffic;
- weather observation only, not mechanical weather effects.

A count from a ten-minute roadside watch must not be directly compared to a full-day station transect without qualification.

## 5. Detection and absence

Absence requires explicit semantics.

```yaml
detection_result:
  observation_id: null
  subject_ref: null
  result: null
  effort_quality: null
  detectability_notes: []
  confidence: null
```

Candidate results:
- DETECTED
- NOT_DETECTED
- CONFIRMED_PRESENT_BY_INDIRECT_EVIDENCE
- POSSIBLE_TRACE
- OBSERVATION_BLOCKED
- INSUFFICIENT_EFFORT

`CONFIRMED_ABSENT` should be rare and require a specific evidence standard defined by the relevant institution/protocol.

Narrative generators should prefer `NOT_DETECTED` unless evidence truly supports stronger language.

## 6. Migration corridor state

A route can function as a corridor for part of a year or under specific conditions.

```yaml
migration_corridor_state:
  corridor_id: null
  route_or_location_ids: []
  subject_refs: []
  function: CORRIDOR
  expected_window_refs: []
  current_phase: null
  latest_detection_ids: []
  bottleneck_location_ids: []
  stopover_location_ids: []
  human_crossing_conflict_ids: []
  stewardship_action_ids: []
  route_advisory_ids: []
  confidence: null
```

Candidate phases:
- OUTSIDE_EXPECTED_WINDOW
- PRE_WINDOW
- POSSIBLE_ARRIVAL
- ACTIVE_PASSAGE
- TAPERING
- DEPARTED
- DELAYED_OR_NOT_DETECTED
- ROUTE_SHIFT_SUSPECTED
- LOST_TRACK

These phases are ecological/world state. They do not alter movement speed or combat legality by themselves.

## 7. Stopover state

A stopover can matter even when no persistent collective resides there.

```yaml
migration_stopover_state:
  stopover_id: null
  location_id: null
  subject_refs: []
  current_use_state: null
  expected_window_refs: []
  resource_dependency_claim_ids: []
  disturbance_ids: []
  infrastructure_overlap_ids: []
  observed_arrival_ids: []
  observed_departure_ids: []
```

Candidate use states:
- UNUSED_OR_OUTSIDE_WINDOW
- POSSIBLE_USE
- ACTIVE_USE
- HIGH_CONCENTRATION
- DEPARTING
- RECENTLY_DEPARTED
- DISTURBED
- SHIFTED_TO_ALTERNATE_SITE
- UNKNOWN

## 8. Temporary aggregation classification

Visible concentration alone is not sufficient to define why Pokémon are gathered.

```yaml
temporary_aggregation_record:
  aggregation_id: null
  location_ids: []
  detected_subject_refs: []
  first_detection_id: null
  latest_detection_id: null
  size_band_observed: null
  persistence_estimate: unknown
  linked_collective_ids: []
  candidate_driver_claim_ids: []
  disturbance_state: null
  status: ACTIVE
```

Safe labels:
- TEMPORARY_AGGREGATION
- MASS_PRESENCE
- REPEATED_LOCAL_CONCENTRATION
- MULTIPLE_GROUPS_PRESENT
- UNKNOWN_CONCENTRATION

Unsafe automatic labels:
- INVASION
- OVERPOPULATION
- BREEDING_SWARM
- AGGRESSIVE_OUTBREAK
- PLAGUE

Those require evidence and may imply mechanics/lore not established.

## 9. Environmental correlates

Phenology often depends on multiple correlated variables.

```yaml
ecology_correlate_claim:
  claim_id: null
  phenology_id: null
  variable_type: null
  observed_value_or_band: null
  supporting_observation_ids: []
  contradicting_observation_ids: []
  relationship_claim: null
  confidence: null
```

Candidate `relationship_claim` values:
- COINCIDENT
- ASSOCIATED
- PREDICTIVE_CANDIDATE
- POSSIBLE_TRIGGER
- CAUSAL_UNKNOWN
- DISCONFIRMED

Examples:
- seasonal calendar band;
- temperature band;
- wind direction;
- rainfall state;
- tide/water-state observation;
- flowering/fruiting/resource availability;
- human traffic level;
- service noise;
- construction state.

The design stores observed environmental context. It does not invent PTU weather penalties or exact causal thresholds.

## 10. Forecast object

Institutions can make forecasts without becoming omniscient.

```yaml
ecological_forecast:
  forecast_id: null
  issuer_id: null
  subject_refs: []
  location_ids: []
  predicted_window: null
  confidence_band: null
  evidence_refs: []
  assumptions: []
  issued_at: null
  revision_history: []
  outcome_state: PENDING
```

Possible outcome states:
- OBSERVED_WITHIN_WINDOW
- OBSERVED_EARLIER
- OBSERVED_LATER
- NOT_DETECTED
- WINDOW_OBSCURED
- ROUTE_SHIFT_SUSPECTED
- FORECAST_WITHDRAWN

Forecast accuracy should affect institutional knowledge, not grant magic certainty.

## 11. Ecological calendar

A regional ecological calendar is a collection of uncertain recurring windows.

```yaml
ecological_calendar:
  calendar_id: null
  region_or_district_id: null
  phenology_ids: []
  public_entries: []
  restricted_or_sensitive_entries: []
  revision_event_ids: []
  current_cycle_id: null
```

The calendar can support:
- research planning;
- school fieldwork;
- route advisories;
- ferry/service adjustments;
- festival timing if separately canonized;
- conservation/stewardship tasks;
- encounter provisioning windows.

It must not expose sensitive nest locations or rare individual identities by default.

## 12. Human operations overlap

Recurring wildlife movement can change ordinary services.

```yaml
ecology_service_overlap:
  overlap_id: null
  phenology_or_corridor_id: null
  service_or_asset_id: null
  conflict_type: null
  active_window_refs: []
  mitigation_options: []
  decision_event_ids: []
  observed_effect_ids: []
```

Candidate conflict types:
- SHARED_PATH
- NOISE_DISTURBANCE
- LIGHT_DISTURBANCE
- DOCK_OR_FERRY_TRAFFIC
- MARKET_OR_FOOD_WASTE
- FARM_RESOURCE_OVERLAP
- RESEARCH_PRESSURE
- PUBLIC_CROWDING
- MAINTENANCE_WINDOW

Mitigation remains operational unless exact PTU mechanics are required.

## 13. Stewardship without ownership

Ecological stewardship actions may include:
- temporary route signage;
- limiting maintenance during a narrow window;
- relocating observation points;
- documenting a crossing;
- removing ordinary debris where legally/physically safe;
- coordinating public viewing distance;
- keeping a stopover access corridor clear;
- reporting an injured/separated individual to an appropriate care/field actor.

These actions do not imply humans own or command the wild group.

## 14. Disturbance versus detectability

A change in sightings can mean behavior changed, detectability changed, observers changed, or abundance changed.

```yaml
detectability_change_claim:
  subject_refs: []
  location_ids: []
  observed_change: null
  candidate_explanations: []
  evidence_ids: []
  unresolved: true
```

Example:
Fewer Pokémon are seen beside the ferry after a schedule change.

Possible explanations:
- group changed timing;
- group shifted route;
- noise makes observation harder;
- actual abundance decreased;
- the comparison used different observation effort.

The world should not choose one explanation from spawn counts alone.

## 15. Player observation pressure

Repeated player presence can itself become disturbance.

The existing collective disturbance model should record:
- repeated close approach;
- bait/feeding;
- camera/observation proximity where relevant;
- battles;
- capture attempts;
- path blocking;
- crowd attraction caused by publicizing a location.

Phenology records can then note that a later shift occurred after pressure without assuming causation.

## 16. Separated individual handoff

A moving group may create an individual welfare case.

Pipeline:
1. observe an individual separated from an expected moving group;
2. assign a persistent Pokémon identity only if narrative persistence is warranted;
3. record condition through care/observation systems without inventing status effects;
4. estimate likely group route from existing evidence;
5. provide non-combat reunion options where feasible;
6. if combat occurs, instantiate only exact relevant participants;
7. write back reunion/continued separation based on world facts and authoritative results.

No kinship, leadership or ownership is inferred.

## 17. Encounter provisioning interface

Temporal ecology may make an encounter possible; it does not resolve it.

```yaml
ecology_encounter_candidate:
  source_phenology_id: null
  source_corridor_or_aggregation_id: null
  location_id: null
  time_window_valid: false
  visible_subgroup_description: null
  persistent_member_candidates: []
  species_candidates_from_authoritative_ecology: []
  encounter_reason: null
  battle_required: false
  mechanics_audit_required: true
```

Rules:
- candidate generation reads server-owned ecological state;
- Cobblemon spawn tables cannot author the migration event;
- species/forms/levels/moves/abilities/items/features come from authoritative provisioning;
- a migration can be observed without battle;
- a battle with one subgroup does not instantiate or defeat the whole migration.

## 18. World Pulse behavior

Do not simulate every population continuously.

Background updates are eligible when:
- a phenology window opens/closes;
- a forecast revision condition occurs;
- a known corridor becomes blocked/open;
- a strong environmental correlate changes;
- a human service changes during an active window;
- a tracked collective reaches a lifecycle transition;
- player observation/disturbance creates evidence;
- an authored regional event changes habitat state.

Safe transitions:
- forecast confidence changes;
- current phase advances from pre-window to possible arrival;
- a public advisory is posted/withdrawn;
- a stopover changes active/inactive state;
- route-shift suspicion is created;
- a research assignment opens;
- a temporary aggregation ends.

Unsafe background transitions without evidence:
- species extinction;
- breeding success/failure;
- collective death;
- exact population collapse;
- disease outbreak;
- mechanical injury/status;
- invented migration destination.

## 19. Quest generation grammar

Phenology quests should originate from a knowledge gap or operational overlap.

Good triggers:
- expected arrival not yet detected;
- two observation series disagree;
- a known passage overlaps repair work;
- ferry/dock traffic may obscure or disturb observations;
- a stopover shows new pressure;
- a separated individual is found;
- a temporary aggregation appears in an unexpected site;
- an old archive forecast no longer matches current observations.

Poor triggers:
- `spawn 8 Pokémon because the player needs combat`;
- `migration happens because the quest board needs content`;
- `the group attacks because it is wild`;
- `rare Pokémon appears because the player is high level` without authoritative ecology.

## 20. Full versus reduced encounter design

For every mechanically rich ecological encounter, record:
- narrative premise;
- full intended tactical version;
- exact permanent capability families required;
- current evidence classification;
- reduced version that preserves premise using world-state/observation and only audited combat if needed;
- allowed writeback from victory/defeat;
- facts combat cannot establish.

This prevents Minecraft presentation from becoming a substitute PTU engine.

## 21. Marea integration points

Canon-backed anchors available now:
- Estación Mirador;
- Mirador transect trailhead;
- weather mast;
- Sendero del Vidrio;
- seasonal crossing;
- Puerto Bruma ferry landing;
- Marea Field Office;
- Tideglass Archive;
- Loma Clara field school and producer lane.

Canon-backed resident roles useful for this layer:
- Nerea: longitudinal ecological/weather observations;
- Ema: transects and field-note preparation;
- Mara: route checks and wildlife incidents;
- Mina: practical weather and ferry-route observations;
- Lia: arrival/departure operations;
- Pia/Taro: records, editions and historical comparison;
- Jo: observation teaching;
- Oren: care handoff when a real welfare case exists.

No specific migratory species or ecological event is canonized by identifying these integration points.

## 22. Minecraft/Cobblemon projection boundary

Minecraft may render:
- visible Pokémon actors;
- signs/boards;
- observation posts;
- route barriers;
- field-note objects;
- ferry/service state;
- changing environmental dressing.

Server-owned Ouros state decides:
- whether a migration/aggregation exists;
- which group/individual identity is being projected;
- what the player observed;
- which ecological phase is active;
- whether an encounter candidate exists;
- which consequences persist.

Entity unload, despawn, chunk loading, Cobblemon AI or random spawn density cannot author ecological departure, death, route change or population decline.

## 23. PTU/Caelo mechanical boundary

This design does not define:
- Survival/Pokémon Education checks;
- encounter tables;
- species habitat legality;
- movement speeds/capabilities;
- capture legality;
- Pack Mon behavior;
- weather effects;
- hazard damage;
- stealth/detection math;
- breeding seasons;
- migration bonuses;
- form changes;
- battle positioning rules.

Any mechanically resolved version must use exact PTU/Caelo source definitions and current AutoPTU support.

## 24. Recommended implementation order

1. comparable observation-series records;
2. detection/absence semantics;
3. phenology records and forecast revision history;
4. Marea transect ledger using existing sites;
5. corridor/stopover phase state;
6. public route/service advisories;
7. temporary aggregation classification;
8. ecology encounter-candidate handoff;
9. safe visible projection in Minecraft;
10. richer tactical corridor encounters only after required capability families are verified.

The first implementation can be entirely non-combat and still make Marea visibly more alive.