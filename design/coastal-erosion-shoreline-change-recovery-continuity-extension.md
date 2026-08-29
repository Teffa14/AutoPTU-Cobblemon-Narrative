# Ouros Coastal Erosion, Shoreline Change & Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until explicitly approved.

This extension preserves coastal-edge observations, versioned shoreline knowledge and long-term recovery. It does not establish that any named Ouros coast is eroding, define coastal engineering, simulate sediment physics or create PTU environmental rules.

## Purpose

Ouros already models maritime regions, tides, sea lanes, navigation aids, roads, weather, stormwater, geology, slope instability, conservation, public works and travel.

A remaining gap exists when the physical coastal edge itself changes persistently.

The world needs to remember:

- which exact shoreline sector was observed;
- what its edge/backshore looked like at a given time;
- whether the observation represents erosion, deposition, overwash, a changed channel, cliff change or simply an uncertain difference;
- what maps and public records believed at each date;
- which access points, habitats, roads, buildings or public spaces received downstream handoffs;
- whether cleanup or repair occurred without restoring the old coastal form;
- whether a temporary access arrangement became permanent;
- what evidence remains years later.

The layer deliberately avoids a universal `coastal_danger` or `erosion_level` scalar.

## 1. Authority boundary

Coastal Change Continuity owns:

- persistent shoreline-sector identity where narratively significant;
- shoreline/backshore observations;
- versioned shoreline-position or morphology claims;
- persistent coastal-change events and observed footprints;
- erosion/deposition/overwash/breach/cliff-change evidence tags when supported;
- observation gaps and revision history;
- access-impact handoffs;
- map/cartography revision handoffs;
- recovery observations and coastal legacy events.

Maritime owns:

- tide, current, swell and sea-state context;
- sea lanes and marine travel context;
- ordinary tidal-access windows;
- marine habitat coordination.

Weather owns atmospheric observations and forecasts.

Stormwater owns drainage networks, stormwater flooding, pumps, culverts and flood-control operations.

Slope Instability owns discrete rock/earth/debris failures on authored slope sectors.

Geology owns geological site identity and interpretation.

Road Operations owns road/bridge closure, detour and reopening.

Travel owns journey viability and topology.

Conservation/Wildlife owns ecological interpretation and stewardship.

Public Works/Facility Maintenance owns engineered work, repair and verification.

Cartography owns map/chart editions and representations.

Public Notices owns dissemination of restrictions/advisories.

Crisis/Rescue owns emergency coordination and evacuation.

Ouros world state owns semantic facts. AutoPTU owns tactical legality and results. Minecraft/Cobblemon/Craftics presents approved state.

## 2. Stable shoreline sector

```yaml
shoreline_sector:
  shoreline_sector_id: null
  maritime_region_ref: null
  location_scope_ids: []
  adjacent_land_location_ids: []
  adjacent_water_location_ids: []
  road_or_travel_refs: []
  public_space_refs: []
  infrastructure_refs: []
  habitat_overlap_refs: []
  geology_refs: []
  slope_sector_refs: []
  monitoring_or_observation_point_refs: []
  current_interpretation_id: null
  history_event_ids: []
  canon_status: proposed
```

A sector is an addressable world object, not a numerical coastal model.

Do not infer:

- shoreline trend;
- erosion rate;
- sediment volume;
- wave exposure;
- hazard probability;
- tactical terrain effects.

## 3. Shoreline observation

```yaml
shoreline_observation:
  observation_id: null
  shoreline_sector_id: null
  observed_at_world_time: null
  observer_ref: null
  observation_method_ref: null
  directly_observed_claims: []
  inferred_claims: []
  edge_or_feature_refs: []
  geographic_precision: null
  media_or_document_refs: []
  tide_or_marine_condition_refs: []
  weather_refs: []
  slope_event_refs: []
  stormwater_refs: []
  comparison_observation_refs: []
  verification_state: UNVERIFIED
  provenance_refs: []
```

Candidate descriptive observation tags:

- BEACH_EDGE_CHANGE_OBSERVED
- BACKSHORE_CHANGE_OBSERVED
- DUNE_OR_RIDGE_CHANGE_OBSERVED
- SEDIMENT_DEPOSITION_OBSERVED
- OVERWASH_DEPOSIT_OBSERVED
- NEW_OR_CHANGED_CHANNEL_OBSERVED
- COASTAL_CLIFF_EDGE_CHANGE_OBSERVED
- ACCESS_POINT_CHANGE_OBSERVED
- EXPOSED_FEATURE_OBSERVED
- SUBMERGED_FEATURE_OBSERVED
- NO_CONFIRMED_CHANGE_AT_OBSERVATION_POINT
- CONDITION_UNKNOWN

The tags describe evidence only. They produce no automatic terrain, damage or movement effect.

## 4. Observation scope and condition normalization

Shoreline observations can be misleading when compared without context.

```yaml
shoreline_observation_context:
  context_id: null
  observation_id: null
  marine_condition_refs: []
  tide_state_ref: null
  weather_state_refs: []
  visibility_ref: null
  observation_position_ref: null
  comparison_basis_ref: null
  uncertainty_notes: []
```

Hard rule:

`DIFFERENT_VISIBLE_WATERLINE != PERSISTENT_SHORELINE_CHANGE`

Ordinary tide or temporary sea state can alter the visible edge. Persistent coastal-change claims require appropriate evidence rather than screenshot comparison alone.

## 5. Versioned shoreline interpretation

```yaml
shoreline_interpretation:
  interpretation_id: null
  shoreline_sector_id: null
  effective_at_world_time: null
  source_observation_ids: []
  source_map_or_record_ids: []
  interpretation_claims: []
  change_kind_claims: []
  confidence: null
  data_gap_refs: []
  downstream_handoff_ids: []
  status: CURRENT
  superseded_by_id: null
  provenance_refs: []
```

Possible `change_kind_claims` may include:

- EROSION_CLAIM
- DEPOSITION_OR_ACCRETION_CLAIM
- OVERWASH_CLAIM
- BREACH_OR_NEW_CHANNEL_CLAIM
- CLIFF_EDGE_RETREAT_CLAIM
- RECOVERY_OR_REBUILDING_CLAIM
- MIXED_OR_SPATIALLY_VARIABLE_CHANGE
- CHANGE_UNCLASSIFIED

These are claims with provenance, not hidden truth flags.

## 6. Coastal-change event

```yaml
coastal_change_event:
  coastal_change_event_id: null
  first_reported_at: null
  observed_time_or_window: null
  affected_shoreline_sector_ids: []
  observation_ids: []
  event_context_refs: []
  footprint_revision_ids: []
  cause_claim_ids: []
  road_or_travel_handoff_ids: []
  maritime_handoff_ids: []
  habitat_handoff_ids: []
  infrastructure_handoff_ids: []
  public_space_handoff_ids: []
  cartography_handoff_ids: []
  crisis_case_refs: []
  verification_state: OPEN
  legacy_event_id: null
  provenance_refs: []
```

An event can span several observations without assuming one uniform effect across the coast.

## 7. Footprint revisions

```yaml
coastal_change_footprint_revision:
  footprint_revision_id: null
  coastal_change_event_id: null
  revision_time: null
  included_sector_ids: []
  boundary_claim_refs: []
  source_observation_ids: []
  excluded_or_unknown_sector_ids: []
  confidence: null
  supersedes_revision_id: null
  provenance_refs: []
```

The first footprint may be incomplete.

Later evidence can extend, narrow or split it.

Never silently replace earlier event knowledge.

## 8. Cause claims

```yaml
coastal_change_cause_claim:
  cause_claim_id: null
  coastal_change_event_id: null
  claimant_ref: null
  claim_type: null
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  confidence: null
  status: OPEN
  adjudicating_authority_ref: null
  resolved_at: null
```

Potential claimed contributors can reference:

- waves/sea state;
- tide or water level;
- weather event;
- slope failure;
- sediment movement;
- construction or public works;
- altered drainage;
- biological activity;
- unknown/multiple factors.

Temporal proximity does not prove causation.

A Pokémon observed digging, nesting, moving material or abandoning a site may be relevant evidence. Species or Type never establishes cause by itself.

## 9. Access-point continuity

```yaml
coastal_access_point:
  coastal_access_point_id: null
  shoreline_sector_id: null
  access_type: null
  stable_location_ref: null
  physical_state: UNKNOWN
  current_access_state: UNKNOWN
  verification_ref: null
  travel_connection_refs: []
  maritime_access_refs: []
  accessibility_refs: []
  restriction_refs: []
  history_event_ids: []
```

Candidate access types:

- BEACH_ENTRY
- FOOTPATH_ENTRY
- BOARDWALK_ENTRY
- BOAT_LANDING
- CAVE_OR_GROTTO_THRESHOLD
- SERVICE_ACCESS
- OBSERVATION_ACCESS
- EMERGENCY_ACCESS
- OTHER_AUTHORED_ACCESS

Hard rules:

`FEATURE_VISIBLE != ACCESS_VERIFIED`

`ACCESS_POINT_PHYSICALLY_PRESENT != ACTOR_TRAVEL_VIABLE`

`COASTAL_CHANGE_OBSERVED != ACCESS_AUTOMATICALLY_CLOSED`

Travel, Maritime, Accessibility and relevant owners decide usability.

## 10. Map and document continuity

Cartography remains owner of maps, but coastal change needs explicit handoff history.

```yaml
shoreline_cartography_handoff:
  handoff_id: null
  shoreline_sector_id: null
  coastal_change_event_ref: null
  source_observation_refs: []
  affected_map_or_chart_refs: []
  requested_revision_scope: null
  requested_at: null
  cartography_response_ref: null
  public_notice_ref: null
```

An old map can remain historically correct.

Candidate map states belong in Cartography, but the coastal layer preserves why a revision was requested.

## 11. Recovery sequence

```yaml
coastal_recovery_sequence:
  recovery_sequence_id: null
  coastal_change_event_id: null
  shoreline_sector_ids: []
  cleanup_handoff_refs: []
  repair_or_public_works_refs: []
  habitat_review_refs: []
  access_review_refs: []
  repeated_observation_refs: []
  map_revision_refs: []
  temporary_arrangement_refs: []
  current_state: OPEN
  closed_at: null
```

Candidate state vocabulary:

- INITIAL_OBSERVATION
- IMPACTS_UNDER_REVIEW
- TEMPORARY_ACCESS_OR_MITIGATION
- CLEANUP_OR_WORK_ACTIVE
- REPEATED_OBSERVATION_ACTIVE
- ACCESS_REVIEW_ACTIVE
- FUNCTION_PARTIALLY_RECOVERED
- LONG_TERM_MONITORING
- CLOSED_WITH_NEW_COASTAL_BASELINE

This sequence is narrative coordination. It does not perform engineering or ecological decisions.

## 12. Recovery does not mean reset

Hard rules:

`WEATHER_EVENT_ENDED != SHORELINE_RECOVERED`

`DEBRIS_OR_SAND_CLEARED != SHORELINE_RESTORED`

`ACCESS_REOPENED != OLD_GEOMETRY_RESTORED`

`DUNE_OR_BEACH_REFORMED != PREVIOUS_SHAPE_RESTORED`

`MAP_UPDATED != EVERY_ACTOR_KNOWS_NEW_MAP`

A recovered coast may have a new stable path, new beach edge, changed habitat, relocated business access or retired infrastructure.

## 13. Temporary arrangements

```yaml
coastal_temporary_arrangement:
  arrangement_id: null
  shoreline_sector_id: null
  trigger_event_ref: null
  arrangement_type: null
  operator_or_steward_refs: []
  location_ref: null
  activated_at: null
  intended_end_condition_ref: null
  current_state: ACTIVE
  downstream_service_refs: []
  social_use_observation_refs: []
  later_disposition_ref: null
```

Possible types:

- TEMPORARY_WALKWAY
- RELOCATED_BEACH_ACCESS
- TEMPORARY_BOAT_HANDOFF
- OBSERVATION_PLATFORM
- TEMPORARY_BARRIER
- RELOCATED_MARKET_OR_SERVICE_EDGE
- ALTERNATE_TRAIL

A temporary arrangement can acquire social importance before its technical need ends.

## 14. Habitat and Pokémon observations

```yaml
coastal_pokemon_observation:
  observation_id: null
  shoreline_sector_id: null
  pokemon_or_collective_ref: null
  observed_at: null
  observed_behavior_claims: []
  location_ref: null
  shoreline_observation_refs: []
  habitat_handoff_ref: null
  observer_ref: null
  confidence: null
  provenance_refs: []
```

Possible observations:

- nesting edge no longer used;
- new sandbar used for resting;
- repeated return to a newly exposed object;
- route shifted after public access moved;
- temporary barrier used as perch;
- individual repeatedly waits at a former landing.

Conservation/Wildlife decides ecological meaning.

Do not infer:

- species-wide shoreline sensing;
- erosion prediction;
- automatic habitat preference from Type;
- cause of coastal change;
- environmental immunity.

## 15. Persistent coastal legacy

```yaml
coastal_legacy_event:
  legacy_event_id: null
  coastal_change_event_ref: null
  stable_reference_name: null
  historical_shoreline_refs: []
  current_shoreline_refs: []
  retired_access_refs: []
  replacement_access_refs: []
  heritage_or_memory_refs: []
  ecology_refs: []
  infrastructure_refs: []
  recurring_character_refs: []
  open_question_refs: []
```

A vanished path, buried sign, old pier footing, exposed foundation, former dune line or obsolete beach name can remain meaningful after physical change.

## 16. Public knowledge and conflicting reports

Different actors may describe the same coastline differently because they observed:

- different sectors;
- different tide states;
- different dates;
- different features;
- different map editions;
- different meanings of “beach returned” or “road open.”

Use provenance, timestamps, scopes and feature IDs.

Do not create a universal `truth_score`.

## 17. Long-term recurring content

A shoreline sector can generate low-intensity stories between major events:

- repeated photography from the same viewpoint;
- old map reconciliation;
- maintenance of temporary access;
- public debate about a path or boardwalk;
- habitat observation;
- rediscovery of exposed objects;
- changed courier/tourism routes;
- family memories tied to a vanished beach edge;
- map editions that still circulate;
- local naming that survives physical change.

This prevents coastal content from existing only as a disaster event.

## 18. Minecraft/Cobblemon presentation contract

The adapter may present:

- authored shorelines and beaches;
- dunes/ridges;
- cliff edges;
- exposed or buried props;
- old/new paths;
- boardwalks;
- barriers;
- survey/observation markers;
- temporary platforms;
- NPC crews;
- Pokémon;
- water, sand, debris and vegetation visuals;
- notice boards and map UI;
- before/after world builds when Ouros authorizes the state change.

Minecraft state never proves the world fact by itself.

Hard boundaries:

- sand block fall does not create an erosion event;
- Minecraft water spread does not calculate shoreline change;
- a waterline moving because of rendering/mod behavior does not update Ouros geography;
- broken blocks do not prove storm damage;
- native swimming does not prove PTU Swim legality;
- native knockback/current physics do not apply PTU forced movement;
- cactus/suffocation/fall/drowning/fire damage never substitutes for AutoPTU damage;
- Cobblemon BattleState cannot choose combatants, legality, HP/status, positions or outcome.

## 19. Encounter contract — Dune Access Withdrawal

Narrative premise:

A coastal access route has been restricted after a documented change. Workers or visitors are leaving while territorial/hostile actors create a conflict near the safe edge.

FULL intended version can include:

- withdrawal/protection objective;
- temporary restricted cells;
- Intercept;
- forced movement where exact rules permit it;
- reactions;
- unstable/soft/wet/overwash zones only if governing mechanics exist;
- changing access if the environment evolves by round;
- tactical AI aware of evacuation/protection;
- semantic Minecraft playback.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if access changes or timed withdrawal matters
- full stateful damage pipeline: PARTIAL if an exact environmental damage source exists
- status lifecycle: PARTIAL if an exact legal condition exists
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

REDUCED current version:

Complete the environmental change and ordinary withdrawal before BattleSpec creation. Keep unstable dunes, active water, workers, visitors and nonparticipating Pokémon outside the tactical grid. Use a static reviewed dry clearing, parking edge, hardened path or already-stable segment. A battle result may secure the immediate access perimeter only. It cannot validate the shoreline, reopen the beach or complete recovery.

## 20. Encounter contract — Newly Exposed Structure Perimeter

Narrative premise:

Coastal change exposes an old foundation, sign, wreck fragment or other authored object. Multiple actors converge before custody, heritage or safety review is complete.

FULL intended version may require:

- protect/withdraw/hold-area objective;
- interactable evidence or custody object;
- changing tide/access only when exact support exists;
- reactions and interception;
- terrain/hazard zones if surf, unstable substrate or debris have tactical effects;
- tactical AI reasoning about the objective;
- semantic playback.

REDUCED current version:

The exposed object remains outside battle state and is not loot. Custody is frozen during combat. Resolve a static perimeter battle on reviewed ground. Found Property, Archives/Heritage or another owner system determines later custody. Victory does not award the object or prove its identity.

## 21. Encounter contract — Former Beach Road Diversion

Narrative premise:

A path or minor coastal road that once bordered the beach now runs beside a changed shoreline. A temporary alternative route creates a territorial or hostile contact.

FULL intended version may add:

- route objective;
- moving noncombatants;
- dynamic restricted cells;
- wave/overwash or collapsing-edge hazards only with exact governing support;
- objective-aware AI;
- semantic playback.

REDUCED current version:

Road/Travel resolves the detour before combat. Noncombatants remain off-grid. The battle uses one static verified junction or inland segment. The coastline remains world-state context. Victory cannot reopen or realign the route.

## 22. Exploration contract — The Line Behind the Dunes

This exploration can run now without environmental battle mechanics.

Premise:

Several generations of maps, family photographs, tourism brochures and public works records show different positions for a familiar beach edge and access path.

Current executable structure:

- locate stable historical viewpoints;
- compare dated photographs;
- reconcile old and current map editions;
- identify retired access markers;
- interview residents/workers about names and uses;
- record Pokémon observations without inferring cause;
- follow only currently verified routes;
- keep unstable/unknown sectors outside accessible geometry.

Future rich version could add changing tide windows, soft substrate, dynamic surf, unstable cliff edges or moving sand only after exact PTU/Caelo and engine contracts exist.

## 23. Canon promotion checklist

Before a coastal-change candidate becomes canon:

1. A named region/shoreline sector is explicitly approved.
2. The physical change has dated world evidence.
3. Tide/temporary visible-waterline effects have been separated from persistent change.
4. Cause claims remain claims unless an authority/evidence resolves them.
5. Downstream road, maritime, ecology, housing, public-space and infrastructure effects are delegated to owner systems.
6. Old records/maps remain preserved rather than rewritten.
7. Pokémon behavior is observation unless a governing source establishes more.
8. Any battle effect has exact PTU/Caelo authority.
9. Every required engine family is verified at the needed scope.
10. Minecraft/Cobblemon presentation follows Ouros/AutoPTU authority.

## 24. Canon status

This document introduces architecture only.

No Ouros shoreline, dune, beach, island, coastal settlement, erosion event, historic storm, restoration program, institution, property boundary, species role or environmental battle rule becomes canon through Pass 115.