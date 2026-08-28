# Ouros Winter Mountain Pass, Snow & Avalanche Operations Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until explicitly approved.

## Purpose

Ouros already has Weather forecasts and observations, Travel routes, Road operational state, Crisis response, Facility Maintenance, Geology and Conservation. This extension adds persistent winter-mountain evidence between those systems.

It answers practical continuity questions:

- Which mountain sector is being discussed?
- What snow, ice or avalanche evidence was actually observed there?
- What did a forecast or local report say, and when?
- Was a route merely covered, physically cleared, assessed, restricted or reopened?
- Did new accumulation supersede an earlier clearing operation?
- Did snow create a temporary route while burying another one?
- What winter state remains after the dramatic scene ends?

This layer is deliberately not a snow physics simulator, avalanche simulator or cold-survival subsystem.

## 1. Authority boundary

Winter Mountain Operations owns authored winter-sector observations, assessed winter operational state, snow-clearing history, avalanche-event observation records and winter access evidence.

Weather owns atmospheric observations, forecasts and forecast revisions.

Seasonality owns recurring seasonal expectations and phenology.

Road Operations owns road/crossing access state.

Travel owns route topology, journeys and mode viability.

Crisis owns emergency activation, evacuation, search/rescue, stabilization and recovery coordination.

Facility Maintenance/Public Works own engineered asset condition, repair and major projects.

Geology owns terrain/material interpretation where relevant.

Conservation/Wildlife owns ecological interpretation.

Public Notices owns published signs/bulletins as information objects.

No subsystem may infer tactical PTU effects from a winter label.

## 2. Persistent mountain sector identity

```yaml
winter_mountain_sector:
  sector_id: null
  location_scope_ids: []
  route_segment_refs: []
  elevation_band_ref: authored_or_unknown
  slope_or_landform_refs: []
  shelter_or_staging_refs: []
  observation_point_refs: []
  known_access_ref_ids: []
  conservation_overlap_refs: []
  sacred_or_heritage_refs: []
  history_event_ids: []
  canon_status: proposed
```

A sector is a stable world reference. Its snow, access and observation history may change without generating a new location.

Do not infer numerical elevation, slope angle or avalanche susceptibility unless authored evidence exists.

## 3. Winter observation

```yaml
winter_condition_observation:
  observation_id: null
  sector_id: null
  observed_at_world_time: null
  observer_actor_or_institution_ref: null
  observation_type: authored
  reported_condition_tags: []
  measurement_refs: []
  media_or_document_refs: []
  weather_observation_refs: []
  location_precision: null
  verification_state: UNVERIFIED
  contradictory_observation_ids: []
  supersedes_observation_ids: []
  provenance_refs: []
```

Candidate descriptive observation types:

- SNOW_COVER
- NEW_ACCUMULATION
- DEEP_DRIFT
- ICY_SURFACE
- BLOWING_SNOW
- VISIBILITY_REPORT
- SLIDE_DEBRIS
- AVALANCHE_OBSERVED
- COLLAPSE_OR_CRACK_REPORT
- CORNICE_OR_OVERHANG_REPORT
- BLOCKED_ENTRANCE
- TEMPORARY_SNOW_BRIDGE_OR_ACCESS
- CLEARING_PROGRESS
- REACCUMULATION
- CONDITION_UNKNOWN

These tags are descriptive evidence. They are not PTU terrain, status or hazard objects.

## 4. Forecast and observation remain different

Weather may provide a forecast product for heavy snow, warming, wind or another condition.

Winter Operations may use that product as evidence for an assessment.

A forecast does not create snow on a particular sector. A weather warning does not itself close a pass. A later observation does not retroactively change what a traveler knew earlier.

Store exact issue/receipt times when knowledge matters.

## 5. Winter operational assessment

```yaml
winter_sector_assessment:
  assessment_id: null
  sector_id: null
  assessed_at_world_time: null
  assessor_ref: null
  source_observation_ids: []
  source_forecast_ids: []
  data_gap_notes: []
  assessed_condition_band: null
  identified_problem_claim_ids: []
  recommended_access_action_refs: []
  recommended_recheck_trigger: null
  status: CURRENT
  superseded_by_assessment_id: null
  provenance_refs: []
```

Suggested coarse condition bands only:

- UNKNOWN
- ROUTINE_WINTER
- DEGRADED
- SIGNIFICANT_CONCERN
- ACCESS_NOT_RECOMMENDED
- POST_EVENT_REVIEW
- INSUFFICIENT_EVIDENCE

These are narrative operational bands. They are not copied real-world danger scales and have no automatic legal or mechanical power.

## 6. Snow clearing as an operation, not a state shortcut

```yaml
winter_clearing_operation:
  operation_id: null
  sector_or_route_ref: null
  requested_at: null
  started_at: null
  completed_at: null
  operator_refs: []
  equipment_or_work_asset_refs: []
  source_obstruction_observation_ids: []
  cleared_extent_ref: null
  post_work_observation_ids: []
  verification_ref: null
  superseded_by_new_condition_ids: []
  status: PLANNED
```

Candidate statuses:

- PLANNED
- STAGED
- ACTIVE
- PAUSED
- PHYSICALLY_COMPLETE
- VERIFYING
- SUPERSEDED_BY_NEW_ACCUMULATION
- CANCELLED

Hard rule:

`PHYSICALLY_COMPLETE != OPEN`

Road/Travel owners still decide access from the current evidence.

## 7. Observed avalanche event

```yaml
observed_snow_slide_event:
  event_id: null
  first_reported_at: null
  observed_at_or_window: null
  origin_sector_ref: null
  affected_sector_refs: []
  observation_ids: []
  debris_or_blockage_refs: []
  affected_route_refs: []
  missing_or_impacted_actor_case_refs: []
  cause_claim_ids: []
  verification_state: OPEN
  response_case_refs: []
  clearing_refs: []
  history_event_id: null
```

An observed avalanche or snow slide is a world event, not a tactical attack.

Do not infer:

- damage;
- forced movement;
- burial depth;
- survival state;
- injury;
- cause;
- trigger;
- recurrence probability.

Those require explicit evidence and, where tactical, verified mechanics.

## 8. Temporary winter access

Snow can alter topology in both directions.

```yaml
winter_temporary_access:
  access_id: null
  sector_id: null
  created_or_exposed_by_observation_ids: []
  route_connection_refs: []
  access_description_ref: null
  effective_from: null
  last_verified_at: null
  closure_or_loss_trigger_refs: []
  current_state: UNKNOWN
  notice_refs: []
  history_event_ids: []
```

Candidate states:

- OBSERVED
- ASSESSED_USABLE
- RESTRICTED
- LOST_TO_NEW_CONDITIONS
- CLOSED
- NO_LONGER_PRESENT

A snowbank, frozen surface or seasonal drift does not automatically become traversable merely because Minecraft geometry permits movement across it.

## 9. Shelter and refuge continuity

Existing buildings, caves or camps may act as winter refuges only when world state supports that use.

```yaml
winter_refuge_use:
  refuge_use_id: null
  location_or_asset_ref: null
  effective_window: null
  operator_or_steward_refs: []
  access_route_refs: []
  availability_state: UNKNOWN
  communications_state_ref: null
  supply_or_service_refs: []
  occupancy_event_refs: []
  closure_reason_refs: []
```

This layer records winter use. Housing, Hospitality, Crisis or another owner controls the underlying facility and services.

## 10. Winter route decision handoff

Recommended chain:

```text
Weather forecast/observation
-> winter-sector observation
-> winter operational assessment
-> route-owner access decision
-> Travel graph viability
-> public notice / actor knowledge
-> later observation
-> reassessment
```

Clearing, rescue and maintenance can enter the chain without collapsing these distinctions.

## 11. Reopening sequence

A robust sequence may be:

```text
obstruction/event observed
-> restriction enacted by owner
-> clearing or mitigation
-> post-work observation
-> winter reassessment
-> infrastructure inspection if needed
-> access decision
-> Travel viability update
-> public-information update
```

Not every case requires every step. The system records which steps actually occurred.

New snowfall can invalidate one or more earlier steps without deleting them from history.

## 12. Community observation and provenance

A skier, hiker, courier, resident, Ranger, worker, researcher or traveler may submit useful evidence.

Their report should retain:

- exact source;
- time;
- location precision;
- what was directly observed;
- what was inferred;
- media/document references;
- verification state.

A local report can be correct without being authoritative. An official bulletin can later be superseded without having been negligent.

## 13. Ecology boundary

Winter can alter where wild Pokémon are observed.

Possible observations:

- lower-elevation appearance during cold periods;
- aggregation near sheltered terrain;
- avoidance of a recently disturbed sector;
- use of a closed route;
- return after melt;
- tracks crossing an access corridor.

Winter Operations records the observation context. Conservation/Wildlife owns claims about migration, habitat, disturbance or population effects.

Never infer avalanche prediction ability, snow safety, rescue competence or cold immunity from species Type or appearance.

## 14. Public memory and seasonal routine

Repeated seasonal operations can become part of place identity.

Examples:

- a pass that usually closes for part of winter;
- a refuge that opens only during a maintained season;
- a local clearing crew known by residents;
- a temporary winter path remembered after it disappears;
- an old avalanche path encoded in stories or signage;
- a business whose season follows pass accessibility.

These become history events and social continuity, not a generic winter reputation score.

## 15. Recommended history events

```text
FIRST_WINTER_OBSERVATION
ASSESSMENT_ISSUED
ASSESSMENT_REVISED
ACCESS_RESTRICTED
SECTOR_CLOSED
CLEARING_STARTED
CLEARING_PAUSED
CLEARING_COMPLETED
NEW_ACCUMULATION_SUPERSEDED_CLEARING
SLIDE_REPORTED
SLIDE_VERIFIED
TEMPORARY_ACCESS_OBSERVED
TEMPORARY_ACCESS_APPROVED
TEMPORARY_ACCESS_LOST
POST_EVENT_REVIEW_STARTED
PARTIAL_REOPENING
FULL_REOPENING
SEASONAL_CLOSURE_ENDED
```

## 16. PTU/Caelo guardrail

PTU 1.05 explicitly supports Slow Terrain and lists deep snow and even ice as examples that may qualify. That permits authored battle maps to mark reviewed squares as Slow Terrain when the governing rules and scenario establish that terrain.

It does not authorize automatic conversion of all overworld snow blocks into Slow Terrain.

PTU also has Hail Weather and Ice moves such as Blizzard and Avalanche. Their existence does not establish generic environmental snowfall, avalanche, burial, wind or cold mechanics.

Before any full winter tactical encounter, verify every specific surface/effect against PTU/Caelo and current AutoPTU contracts.

## 17. Encounter contract — Pass Closure Withdrawal

Narrative premise:

A mountain sector is already being closed when a hostile or territorial encounter threatens the final withdrawal route for staff or travelers.

Full intended version may use:

- reviewed deep-snow Slow Terrain;
- multiple withdrawal routes;
- Intercept and forced movement;
- changing visibility only if exact rules exist;
- a dynamic exclusion sector only if zones/reactions are verified;
- objective-aware AI favoring withdrawal, separation or route denial;
- authoritative playback.

Permanent capability requirements:

```yaml
requirements:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Current authoring profile: REDUCED.

Reduced version:

Complete the closure and ordinary withdrawal in Ouros world state before battle. Remove travelers, staff, vehicles/equipment and nonparticipating Pokémon. Use a reviewed static safe shoulder, clearing, shelter approach or interior space. Snow remains visual unless exact Slow Terrain squares are intentionally authored and current movement support is verified. No avalanche, blowing-snow, falling, burial or changing-weather mechanic runs during combat. The result can secure the immediate area only; the winter assessment and route owner decide reopening.

## 18. Encounter contract — Slide Debris Search Perimeter

Narrative premise:

After a verified snow slide, a search/recovery perimeter is established. A separate territorial or hostile contact occurs near one safe access edge.

Full intended version could require:

- protected search lanes;
- CLEAR_ROUTE/WITHDRAW/PROTECT-like goals;
- reactions and complete forced movement;
- authored snow terrain;
- exact burial/extraction mechanics if ever supported;
- AI that understands perimeter and escape goals;
- faithful adapter playback.

Current authoring profile: REDUCED.

Reduced version:

Crisis completes any active rescue/search movement outside the battle. The actual debris field and unknown search subjects remain outside the tactical grid. Combat occurs on a verified stable perimeter. Winning does not locate, injure, rescue or recover anyone and does not clear the route. Search, rescue, evidence review and clearing resume afterward through their owner systems.

## 19. Encounter contract — Winter Refuge Approach

Narrative premise:

A refuge is operational during poor conditions. A conflict develops near an approach while occupants remain inside.

Full intended version may want:

- reviewed Slow Terrain;
- protected approach/withdrawal objectives;
- weather or visibility effects only when verified;
- tactical AI;
- adapter playback.

Current authoring profile: REDUCED.

Reduced version:

Keep occupants inside and make the approach operationally closed. Resolve any battle in a static reviewed area with no environmental cold, snowfall or avalanche effects. Refuge availability is never determined by KO outcome alone.

## 20. Noncombat investigation — Five Winter Reports, Three Sectors

Several reports appear contradictory: one says the pass was clear, another reports deep snow, another describes slide debris, and two public notices use different place names.

Playable investigation:

- reconcile sector IDs and local names;
- compare observation timestamps;
- distinguish cleared roadway from slopes above it;
- identify whether new accumulation occurred after clearing;
- compare notice publication time against later field evidence;
- retain ambiguity if one report cannot be geolocated.

No battle mechanics are required.

## 21. Long arc — A Pass Learns Its Winter

Stage 1 establishes ordinary warm-season travel and the people who depend on the corridor.

Stage 2 introduces the first seasonal assessment, small access changes and a refuge or observation routine.

Stage 3 produces a closure, new accumulation or verified slide that changes journeys without destroying the mountain location.

Stage 4 follows clearing, local observations and ecological consequences while access remains partial.

Stage 5 reopens one sector while another remains restricted or temporary.

Stage 6 lets a snow-created route, temporary refuge practice, changed business routine or wildlife observation outlast the original disruption.

Stage 7 returns in a later season. Old observations, route names and closure history become evidence for a new decision.

The place accumulates winter history without a `winter_level` or hidden safety score.

## 22. Minecraft/Cobblemon boundary

Likely SAFE_REUSE, subject to concrete API review:

- snow/ice blocks and mountain geometry as presentation;
- particles, sky, fog-like presentation, sounds and day/night visuals;
- barriers, signs, shelters and worksite props;
- Pokémon overworld entities, models, forms, poses, animations and cries;
- maps/UI;
- world coordinates, networking, tracking and persistence hooks.

ADAPTER_REQUIRED:

- stable sector IDs bound to world geometry;
- projecting authoritative closures and temporary access into barriers/signs;
- converting reviewed tactical snow/ice surfaces into exact AutoPTU terrain cells;
- keeping overworld weather separate from PTU Weather unless a validated handoff exists;
- stable actor identity through chunk unload/reload;
- authoritative battle event playback.

BATTLE_AUTHORITY_FORBIDDEN:

- Minecraft powder-snow or ice behavior deciding PTU movement without mapping;
- native weather applying PTU Hail, damage or status;
- block updates causing avalanche damage or forced movement;
- nearby entities becoming combatants from proximity;
- Cobblemon BattleState choosing participants, HP, statuses, positions, legality or result;
- visual clearing automatically reopening Travel state.

Authority remains:

`Ouros winter/world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## 23. Canon questions retained as UNKNOWN

- regional snow climates and mountain passes;
- seasonal closure customs;
- winter-assessment institutions;
- warning terminology;
- clearing technology and staffing;
- permanent/temporary refuges;
- communications at remote elevations;
- local sacred/protected restrictions;
- individual Pokémon winter-work roles.

## 24. Mechanical questions retained as UNKNOWN

- exact criteria for converting authored overworld deep snow/ice into PTU Slow Terrain;
- snow-specific LoS/Accuracy effects;
- environmental Hail mapping;
- cold exposure;
- avalanche displacement/damage;
- burial/suffocation;
- rescue/extraction/carry rules;
- cornice/fall rules;
- changing snowpack during rounds;
- snow-clearing Move/Capability conversions;
- Pokémon environmental cold immunity beyond exact governing effects.

Do not invent answers for implementation convenience.