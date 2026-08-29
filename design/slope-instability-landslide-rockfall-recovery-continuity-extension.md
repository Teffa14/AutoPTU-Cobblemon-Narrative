# Ouros Slope Instability, Landslide & Rockfall Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until explicitly approved.

This extension preserves slope-specific evidence and continuity. It does not establish that any named Ouros region is landslide-prone, define engineering standards, simulate geotechnical physics or create PTU environmental rules.

## Purpose

Ouros already has systems for Geology, Weather, Seismic Monitoring, Volcanic Monitoring, Winter Mountain Operations, Stormwater, Wildfire, Roads, Travel, Crisis/Rescue, Facility Maintenance and Public Works.

A remaining gap exists between those systems when rock, earth or debris moves downslope.

The world needs to remember:

- which exact slope sector was observed;
- what was directly seen versus inferred;
- whether movement actually occurred;
- what area was known to be affected at a particular time;
- which roads, structures, habitats or services received downstream handoffs;
- whether debris was merely removed or the source area was assessed;
- whether stabilization work was completed and independently verified;
- whether route or site owners subsequently changed access;
- what evidence remains years after the incident.

The layer intentionally avoids a universal `landslide_danger` score.

## 1. Authority boundary

Slope Instability Continuity owns:

- persistent slope-sector identity where narratively significant;
- slope-condition observations;
- slope monitoring records and monitoring gaps;
- slope assessments and revisions;
- observed landslide, rockfall and non-snow debris-movement events;
- source-area and affected-footprint observations;
- slope-specific blockage/impact handoffs;
- stabilization-work handoffs;
- post-work slope verification handoffs;
- slope-event history and legacy state.

Geology owns:

- geological site identity;
- formation/material interpretation;
- geological context;
- excavation/resource-frontier state;
- authored site disturbance and scientific geological claims.

Weather owns atmospheric observations, forecasts and revisions.

Seismic Monitoring owns earthquake events, seismic observations and earthquake notices.

Volcanic Monitoring owns volcanic episodes, ashfall and volcanic hazard observations. Lahars or explicitly volcanic mass-flow events remain there unless an authored cross-system reference is needed.

Winter Mountain Operations owns snow/ice avalanche and snow-slide continuity.

Stormwater owns drainage networks, stormwater flooding, culverts, inlets, pumps and flood-control operations.

Wildfire owns fire incidents and fire-response state.

Road Operations owns road/crossing restriction, detour and reopening state.

Travel owns regional topology, journey selection and travel viability.

Crisis/Rescue owns evacuation, search, rescue and emergency coordination.

Facility Maintenance/Public Works own technical asset condition, work orders, physical repair/stabilization projects and verification procedures for engineered assets.

Conservation/Wildlife owns ecological interpretation.

Public Notices owns published warnings, signs and bulletins as information objects.

The slope layer consumes and emits handoffs. It does not replace these authorities.

## 2. Stable slope-sector identity

```yaml
slope_sector:
  sector_id: null
  location_scope_ids: []
  geology_site_refs: []
  road_segment_refs: []
  travel_connection_refs: []
  water_or_drainage_refs: []
  infrastructure_refs: []
  habitat_overlap_refs: []
  settlement_overlap_refs: []
  observation_point_refs: []
  monitoring_node_refs: []
  active_assessment_id: null
  history_event_ids: []
  canon_status: proposed
```

A sector is a stable narrative reference, not a numerical geotechnical model.

Do not infer:

- slope angle;
- material strength;
- susceptibility;
- stability factor;
- runout distance;
- probability of failure;
- tactical terrain effects.

Those require authored evidence or governing mechanics.

## 3. Slope observation

```yaml
slope_observation:
  observation_id: null
  sector_id: null
  observed_at_world_time: null
  observer_ref: null
  observation_type: authored
  directly_observed_claims: []
  inferred_claims: []
  location_precision: null
  media_or_document_refs: []
  measurement_refs: []
  weather_refs: []
  seismic_refs: []
  volcanic_refs: []
  water_refs: []
  worksite_refs: []
  verification_state: UNVERIFIED
  supersedes_observation_ids: []
  contradictory_observation_ids: []
  provenance_refs: []
```

Candidate descriptive observation types may include:

- NEW_CRACK_OR_SEPARATION_REPORT
- ROCKFALL_DEBRIS_OBSERVED
- FALLEN_BLOCK_OR_BOULDER_OBSERVED
- EARTH_OR_DEBRIS_MOVEMENT_OBSERVED
- SLOPE_DEFORMATION_REPORT
- BLOCKED_ROUTE_OBSERVED
- CHANGED_DRAINAGE_OBSERVED
- EXPOSED_SURFACE_OBSERVED
- MOVEMENT_SOUND_OR_DUST_REPORT
- NO_VISIBLE_CHANGE_AT_OBSERVATION_POINT
- CONDITION_UNKNOWN

These labels are evidence tags only. They do not produce tactical effects.

## 4. Monitoring record and gaps

```yaml
slope_monitoring_record:
  monitoring_record_id: null
  sector_id: null
  monitoring_node_ref: null
  observation_window_start: null
  observation_window_end: null
  data_state: UNKNOWN
  observation_refs: []
  transmission_refs: []
  review_state: UNREVIEWED
  provenance_refs: []
```

Suggested data states:

- OBSERVATIONS_AVAILABLE
- PARTIAL_OBSERVATIONS
- UNKNOWN_FOR_INTERVAL
- NODE_OFFLINE
- DATA_PENDING_REVIEW
- NO_RELEVANT_CHANGE_REPORTED

Hard rule:

`NO_RELEVANT_CHANGE_REPORTED != SLOPE_PROVEN_STABLE`

A sensor or observer covers an authored scope. It does not make the entire region known.

## 5. Versioned slope assessment

```yaml
slope_assessment:
  assessment_id: null
  sector_id: null
  assessed_at_world_time: null
  assessor_ref: null
  source_observation_ids: []
  external_event_refs: []
  data_gap_refs: []
  current_interpretation_claims: []
  access_recommendation_refs: []
  stabilization_recommendation_refs: []
  recheck_trigger_refs: []
  confidence: null
  status: CURRENT
  superseded_by_assessment_id: null
  provenance_refs: []
```

Assessments are versioned claims.

They are not hidden truth.

An assessment can change after new photographs, field observations, monitoring data or downstream evidence arrives without making the earlier assessment fraudulent.

Avoid a universal scalar such as `SAFE`, `DANGER_4` or `92% STABLE` unless a future canon authority deliberately defines one.

## 6. Observed slope-failure event

```yaml
slope_failure_event:
  event_id: null
  event_kind: authored_or_unknown
  first_reported_at: null
  observed_time_or_window: null
  source_sector_refs: []
  observation_ids: []
  source_footprint_observation_ids: []
  affected_footprint_observation_ids: []
  material_description_claims: []
  movement_description_claims: []
  cause_claim_ids: []
  affected_asset_handoff_ids: []
  blockage_handoff_ids: []
  crisis_case_refs: []
  verification_state: OPEN
  history_event_id: null
  provenance_refs: []
```

Possible authored event labels include:

- ROCKFALL
- ROCK_SLIDE
- EARTH_SLIDE
- DEBRIS_SLIDE
- DEBRIS_FLOW
- SLOPE_COLLAPSE
- COMPLEX_MOVEMENT
- MASS_MOVEMENT_UNKNOWN

The label describes the world event only when evidence supports it.

It grants no damage, movement, burial or terrain rule.

## 7. Cause claims remain separate

A slope failure may occur after:

- heavy rainfall;
- snowmelt;
- earthquake shaking;
- volcanic activity;
- erosion;
- changed drainage;
- excavation;
- construction;
- vegetation loss;
- wildfire;
- Pokémon activity;
- multiple contributing conditions;
- unknown conditions.

These are possible claims, not automatic causes.

```yaml
slope_cause_claim:
  claim_id: null
  event_id: null
  proposed_cause_ref: null
  evidence_refs: []
  claimant_ref: null
  issued_at: null
  confidence: null
  review_state: OPEN
  superseded_by_claim_id: null
```

Hard rule:

`EVENT_AFTER_RAIN != RAIN_PROVEN_CAUSE`

Likewise:

`POKEMON_OBSERVED_NEARBY != POKEMON_CAUSED_FAILURE`

## 8. Evolving footprint evidence

Early reports may know only that a road is blocked. Later mapping may identify the source slope, runout/deposition area and other affected assets.

```yaml
slope_footprint_observation:
  footprint_observation_id: null
  event_id: null
  footprint_kind: SOURCE_AREA_OR_AFFECTED_AREA_OR_DEPOSITION
  geometry_ref: null
  observed_or_derived_at: null
  source_refs: []
  location_precision: null
  confidence: null
  supersedes_footprint_observation_ids: []
  provenance_refs: []
```

Never overwrite the first footprint silently.

A map produced two hours after an event may be useful and incomplete. A later map can refine it while preserving what actors knew at the earlier time.

## 9. Blockage and impact handoff

The slope layer records what appears to have been affected and hands the consequence to the owner system.

```yaml
slope_impact_handoff:
  handoff_id: null
  event_id: null
  affected_system_ref: null
  affected_asset_or_scope_refs: []
  supporting_observation_ids: []
  created_at: null
  recipient_authority_ref: null
  receipt_state: UNKNOWN
  downstream_case_ref: null
```

Examples:

- Road Operations receives a blocked-segment handoff;
- Rail Operations receives a track-corridor handoff;
- Communications receives a damaged-link observation;
- Power receives an affected-line observation;
- Water receives a source/intake/pipe concern;
- Stormwater receives a drainage obstruction concern;
- Conservation receives habitat-change evidence;
- Crisis receives missing/injured/trapped-person reports;
- Workplace systems receive an affected worksite observation.

The slope event never declares those systems recovered.

## 10. Debris removal is not slope stabilization

This distinction is permanent.

```text
DEBRIS_REMOVED != SLOPE_ASSESSED
SLOPE_ASSESSED != STABILIZATION_REQUIRED
STABILIZATION_WORK_COMPLETE != SLOPE_VERIFIED
SLOPE_VERIFIED != ROAD_REOPENED
ROAD_REOPENED != ALL_DOWNSTREAM_SYSTEMS_RECOVERED
```

A road crew may clear material enough to inspect a segment while the source slope remains restricted.

A slope may be assessed and require no stabilization while the road still needs unrelated repair.

A stabilization project may finish while verification is pending.

A verified slope condition does not automatically reopen a route because Road Operations owns access.

## 11. Stabilization handoff

```yaml
slope_stabilization_handoff:
  handoff_id: null
  sector_id: null
  event_id: null
  assessment_ref: null
  work_owner_ref: null
  work_project_ref: null
  requested_scope_ref: null
  handoff_state: OPEN
  completion_observation_refs: []
  verification_ref: null
  returned_at: null
```

The slope layer does not invent engineering work.

Facility Maintenance, Public Works or another canon-authorized technical owner defines the actual project and evidence.

Possible presentation may include barriers, drainage work, retaining structures, scaling, anchors, vegetation, changed alignments or other solutions only when canon authors them.

## 12. Access review handoff

```yaml
slope_access_review_handoff:
  review_handoff_id: null
  sector_id: null
  affected_route_or_site_refs: []
  current_assessment_ref: null
  stabilization_verification_refs: []
  residual_unknown_refs: []
  route_or_site_owner_ref: null
  decision_ref: null
  status: PENDING
```

The access owner can choose:

- remain closed;
- limited access;
- controlled access;
- reopen one direction/approach;
- use a detour;
- permanently retire the alignment;
- commission more evidence;
- another authored option.

Slope Instability records the handoff and resulting decision reference. It does not make the access decision itself.

## 13. Cascading events without authority collapse

A slope failure can create a chain such as:

```text
rainfall observation
-> slope movement observed
-> road blocked
-> stream partially obstructed
-> settlement detour activated
-> courier route changes
-> habitat observations change
-> debris cleared
-> slope assessed
-> route remains closed for unrelated pavement damage
-> temporary detour becomes socially important
```

Each arrow can be owned by a different system.

This is intentional. A dramatic event should connect world systems without becoming a master switch that directly mutates everything.

## 14. Boundary with winter avalanche

If the governing event is moving snow/ice, Winter Mountain Operations owns it.

If the governing event is rock, earth or debris, Slope Instability Continuity owns it.

Mixed events require explicit authoring. Do not classify from Minecraft block palette alone.

An avalanche exposing unstable rock can produce a later slope observation without transferring the avalanche event into this layer.

## 15. Boundary with volcanic mass flows

Volcanic Monitoring owns lahars, eruption-generated slope events or volcanic-debris processes when the volcanic episode is the governing context.

Slope Instability may receive a cross-reference for downstream access or long-term slope evidence.

Avoid duplicate primary event IDs.

## 16. Boundary with Stormwater/flooding

Stormwater owns drainage and flooding.

A debris flow can obstruct a culvert or channel. The slope layer records the debris movement/footprint and sends a handoff. Stormwater decides network condition and flood-control operations.

A flood that erodes a slope can send evidence in the opposite direction.

## 17. Pokémon participation and agency boundary

Individual Pokémon may legitimately appear as:

- residents of a slope or cliff habitat;
- displaced wild actors after an event;
- observers whose movement was recorded;
- trained partners assisting an established work role;
- search/rescue participants when governing capability supports it;
- subjects of rumors or local folklore;
- possible causal actors only when direct evidence and governing rules support the claim.

Do not infer from species or Type:

- landslide prediction;
- geotechnical sensing;
- immunity to rock/debris impacts;
- safe navigation of unstable slopes;
- excavation authority;
- rock-clearing ability;
- stabilization work competence;
- automatic causation.

The Pokémon Work and Agency layers preserve individual history. PTU/Caelo and AutoPTU govern mechanical capabilities.

## 18. Actor knowledge and public information

Actual world state, expert assessment, published notices and individual knowledge remain separate.

Example:

- a courier saw one boulder at 07:10;
- a road notice closed the corridor at 07:30;
- a mapper documented a larger debris field at 09:20;
- a local resident still calls the closed road by its pre-event name;
- a tourist map published last month continues to show the old connection.

No discrepancy automatically means deception.

Use source, timestamp, scope and effective period.

## 19. Legacy slope event

```yaml
slope_legacy_event:
  legacy_id: null
  original_event_id: null
  sector_refs: []
  former_route_refs: []
  current_route_refs: []
  remaining_feature_refs: []
  monitoring_refs: []
  memorial_or_public_memory_refs: []
  ecology_refs: []
  heritage_refs: []
  old_map_refs: []
  later_reassessment_refs: []
```

A former slide can leave:

- an abandoned switchback;
- a relocated road;
- a widened clearing;
- a new wet area or changed drainage pattern;
- a debris fan;
- a monitoring station;
- a local nickname;
- a memorial;
- a habitat edge;
- a maintenance routine;
- an old business district that lost through-traffic;
- a new settlement path created by the detour.

Recovery does not reset the landscape.

## 20. Recommended history events

```text
SLOPE_OBSERVATION_RECORDED
MONITORING_GAP_OPENED
MONITORING_RESTORED
ASSESSMENT_ISSUED
ASSESSMENT_REVISED
MOVEMENT_REPORTED
FAILURE_EVENT_VERIFIED
FOOTPRINT_REVISED
ROUTE_IMPACT_HANDOFF_CREATED
DOWNSTREAM_IMPACT_HANDOFF_CREATED
DEBRIS_CLEARING_STARTED
DEBRIS_CLEARING_COMPLETED
STABILIZATION_REQUESTED
STABILIZATION_WORK_COMPLETED
SLOPE_VERIFICATION_RECORDED
ACCESS_REVIEW_REQUESTED
PARTIAL_ACCESS_DECIDED
FULL_ACCESS_DECIDED
ALIGNMENT_RETIRED
LEGACY_REVIEW_OPENED
```

## 21. Encounter contract — Switchback Withdrawal

Narrative premise:

A mountain road is already under restriction after recent slope movement. A separate hostile or territorial contact develops while the final workers or travelers withdraw from a verified safe edge.

Full intended version may include:

- multiple withdrawal routes;
- Intercept and forced displacement;
- authored falling-rock or exclusion zones;
- temporary route loss during rounds;
- objective-aware AI favoring withdrawal/protection rather than KO;
- authoritative semantic playback.

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

Complete ordinary withdrawal before BattleSpec creation. Exclude unstable slope, active debris, vehicles, workers and nonparticipating Pokémon. Use a reviewed static turnout or road section with no falling-rock, sliding, collapse or changing-zone rules. Ouros selects combatants. AutoPTU resolves the fixed battle. Victory can establish only `IMMEDIATE_SAFE_EDGE_SECURED`. Slope assessment and Road Operations still decide the corridor state.

## 22. Encounter contract — Survey Marker Perimeter

Narrative premise:

A monitoring/survey team needs temporary access to a stable observation point near a recently changed slope. A conflict develops on the already-inspected perimeter.

Full intended version could use:

- a protection objective around observers or equipment;
- narrow route choices;
- Intercept/forced movement;
- dynamic restricted cells if slope conditions change;
- reactions;
- tactical policy that values exclusion and retreat;
- semantic playback.

Current authoring profile: REDUCED.

Reduced version:

Complete survey setup or withdrawal outside combat. Keep instruments and unstable sectors outside the tactical grid. Resolve battle on a static inspected platform/clearing. Equipment cannot be damaged or activated tactically unless a future exact object contract exists. Winning secures the immediate perimeter only; it does not validate measurements or change the slope assessment.

## 23. Encounter contract — Debris Fan Diversion

Narrative premise:

A previous slope event left a persistent debris fan near a travel connection or settlement edge. A later encounter occurs there after the moving event is over.

Full intended version becomes mechanically rich only if designers want loose footing, mud, rolling material, dust, new flow, changing cover or forced displacement.

Those effects require the exact relevant families:

- terrain/weather/hazards/zones/reactions: BLOCKING;
- complete movement: PARTIAL for displacement/sliding;
- full turn/round lifecycle: PARTIAL for delayed or phased changes;
- full stateful damage pipeline: PARTIAL if debris causes damage;
- status lifecycle: PARTIAL if dust/mud creates conditions;
- move-specific behavior/abilities/items/Trainer Features: PARTIAL when interacting;
- AI tactical policy: BLOCKING for changing-risk reasoning;
- adapter/playback: BLOCKING.

Reduced version:

Treat the legacy debris fan as static, reviewed terrain with no special tactical effect. Use ordinary geometry only. The historical event remains relevant through maps, route history, ecology and NPC memory rather than environmental combat scripting.

## 24. Investigation — Four Maps, One Moving Boundary

An old route map, first-response sketch, later survey and current public map appear inconsistent.

Playable evidence:

- stable sector IDs;
- old and new route alignments;
- observation timestamps;
- footprint versions;
- photograph locations;
- route closure times;
- maintenance/stabilization records;
- witness scopes;
- public-notice publication times.

Possible outcomes include:

- every map was correct for its date;
- an early footprint was incomplete;
- a road name moved with the replacement alignment;
- two events were incorrectly merged in local memory;
- uncertainty remains because one observation cannot be geolocated.

No hidden truth score is needed.

## 25. Long arc — A Valley Learns Its Slopes

Stage 1 establishes ordinary travel, farms/homes/workplaces, seasonal weather, known cliff paths and recurring Pokémon observations.

Stage 2 records small observations that may or may not matter. Different actors interpret them differently.

Stage 3 a slope failure or major rockfall occurs only if canon/event generation authorizes it. Immediate consequences are handed to the correct owner systems.

Stage 4 route changes and temporary arrangements alter social geography. A detour may help one settlement and hurt another.

Stage 5 debris clearing, assessment and possible stabilization happen as separate operations. The source slope can remain restricted after the road surface is physically cleared.

Stage 6 access returns partially, permanently changes alignment or remains closed. Downstream systems recover on their own timelines.

Stage 7 months or years later, an old observation, abandoned road, changed habitat, monitoring post or remembered detour becomes relevant again.

The valley accumulates history without `slope_level` or `disaster_progress`.

## 26. Minecraft/Cobblemon/Craftics boundary

Likely SAFE_REUSE, subject to concrete API review:

- cliffs, scree, boulders, exposed rock, debris and road geometry as presentation;
- barriers, cones, signs, survey markers and monitoring props;
- particles and sounds as presentation;
- NPC crews;
- Pokémon overworld entities, models, forms, poses, animations and cries;
- maps/UI;
- world coordinates;
- networking, entity tracking and persistence hooks.

ADAPTER_REQUIRED:

- stable sector/event/footprint IDs bound to world geometry;
- projecting authoritative closures and access decisions into barriers/signs;
- presenting footprint revisions without replacing historical evidence;
- converting only reviewed static geometry into BattleSpec cells;
- authoritative battle-event playback.

BATTLE_AUTHORITY_FORBIDDEN:

- Minecraft falling blocks applying PTU damage;
- gravel/sand physics deciding a landslide event;
- native knockback resolving forced movement;
- water flow resolving debris-flow movement;
- suffocation blocks applying PTU burial/status without an exact rule;
- block collision deciding tactical legality outside reviewed BattleSpec mapping;
- pathfinding deciding evacuation success;
- a broken road block automatically closing the authoritative travel graph;
- a cleared block pile automatically reopening a road;
- Cobblemon BattleState/controller logic selecting combatants or deciding legality, HP/status, positions or outcome.

Binding direction remains:

`Ouros world facts -> AutoPTU tactical specification/resolution -> adapter -> Minecraft/Cobblemon/Craftics presentation`

## 27. PTU/Caelo guardrail

Current governing material does not establish universal mechanics for:

- natural slope failure timing;
- landslide probability;
- rainfall-trigger thresholds;
- rockfall trajectories;
- falling debris damage;
- burial or suffocation;
- dynamic collapse zones;
- unstable ledge checks;
- mud/debris Slow Terrain by default;
- debris-flow forced movement;
- dust exposure/status;
- structural damage from slope movement;
- automatic Rock/Ground-type environmental immunity;
- species-derived landslide sensing;
- Move/Ability/Item/Trainer Feature slope control without exact rules.

A specific authored location may use a mechanical effect only when an exact governing PTU/Caelo source and current engine contract support that effect.

Otherwise slope conditions remain world state, inert scenery or excluded geometry.

## 28. Canon questions

Future canon may decide:

- which regions contain meaningful unstable slopes;
- which historical failures changed settlements or routes;
- what monitoring technologies and institutions exist;
- what terminology local communities use;
- which authorities can restrict access;
- how stabilization projects are organized;
- whether abandoned slide routes become heritage, habitat or restricted areas;
- how old events shape land use and public memory;
- which individual Pokémon have documented relationships with these sites;
- whether any exact PTU/Caelo mechanics apply to authored slope environments.

Until those decisions exist, the layer preserves uncertainty instead of filling it with contemporary real-world assumptions.
