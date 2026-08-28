# Ouros Stormwater, Drainage & Flood-Control Continuity Extension

Status: PROPOSED systems design. Not established canon.
Date: 2026-08-28
Research provenance: `research/2026-08-28-stormwater-drainage-flood-control-continuity-scan-108.md`

## Purpose

This extension gives Ouros persistent operational state for stormwater collection, drainage and local flood-control infrastructure without creating a rainfall-runoff or hydraulic simulator.

It answers questions such as:

- which authored drainage system and catchment sector exists;
- which inlet, culvert, conveyance link, storage asset, pump or outfall is available;
- what obstruction or flooding was actually observed;
- what temporary mitigation is active;
- which sector has visibly drained;
- what still needs inspection or verification;
- which road, building, habitat or public-space owner must make the next decision.

## 1. Authority boundary

Existing systems retain authority.

Weather owns forecasts, rainfall and observed weather conditions.

Water Management owns rivers, reservoirs, managed channels, diversions and other managed freshwater systems.

Waste/Sanitation owns sanitary wastewater, wastewater treatment, contamination observations and pollution claims.

Road Operations owns road, bridge, underpass and detour access/reopening.

Facility Maintenance owns condition, inspection, repair and technical work orders for physical assets.

Infrastructure Outage owns cross-service dependencies, fallback coordination and multi-network restoration.

Crisis/Rescue owns emergency response, evacuation, missing-person cases and recovery operations.

Civic/Public Works owns projects, approvals and long-term infrastructure decisions.

Conservation/Wildlife owns habitat and ecological interpretation.

Stormwater Continuity owns only the authored drainage path and its operational history between rainfall/runoff collection points and authorized receiving handoffs.

## 2. Stable drainage-system identity

```yaml
stormwater_system:
  stormwater_system_id: null
  name_refs: []
  geographic_scope_ids: []
  catchment_sector_ids: []
  inlet_ids: []
  conveyance_link_ids: []
  culvert_ids: []
  storage_asset_ids: []
  pump_station_ids: []
  outfall_ids: []
  operator_institution_ids: []
  power_dependency_refs: []
  downstream_water_system_refs: []
  historical_system_refs: []
  current_system_state: UNKNOWN
  last_verified_at: null
  canon_reference_ids: []
```

Suggested descriptive states:

- UNKNOWN
- NORMAL
- DEGRADED
- CONSTRAINED
- PARTIALLY_BLOCKED
- PARTIALLY_OFFLINE
- OFFLINE
- TEMPORARY_CONFIGURATION
- RESTORING
- TESTING
- DECOMMISSIONED

The state does not imply flow rate, flood probability or engineering capacity.

## 3. Catchment sector

```yaml
stormwater_catchment_sector:
  catchment_sector_id: null
  stormwater_system_id: null
  geographic_scope_ids: []
  collection_point_ids: []
  active_path_ids: []
  storage_asset_ids: []
  observed_surface_water_state: UNKNOWN
  operational_drainage_state: UNKNOWN
  restriction_ids: []
  downstream_owner_refs: []
  last_observation_ids: []
  last_verified_at: null
```

Possible broad surface-water observations:

- UNKNOWN
- DRY_OBSERVED
- PONDING_OBSERVED
- FLOODING_OBSERVED
- RECEDING_OBSERVED
- RECENTLY_DRAINED

Possible operational drainage states:

- UNKNOWN
- AVAILABLE
- DEGRADED
- LIMITED
- BLOCKED
- PUMP_DEPENDENT
- TEMPORARY_DRAINAGE
- RESTORING
- TESTING

A dry street can coexist with an unverified drainage sector.

## 4. Collection point / inlet

```yaml
stormwater_inlet:
  inlet_id: null
  stormwater_system_id: null
  catchment_sector_id: null
  location_id: null
  inlet_form: authored_or_unknown
  receiving_link_id: null
  maintenance_asset_ref: null
  access_state: UNKNOWN
  observed_intake_state: UNKNOWN
  obstruction_observation_ids: []
  inspection_ids: []
  last_verified_at: null
```

Suggested observations:

- UNKNOWN
- CLEAR_OBSERVED
- PARTIALLY_OBSTRUCTED
- OBSTRUCTED
- SUBMERGED
- INACCESSIBLE
- INTAKE_OBSERVED
- NO_INTAKE_OBSERVED

`CLEAR_OBSERVED` says nothing about the downstream link.

A leaf pile, debris pile, nesting material or Pokémon nearby can be recorded as an observation. It is not a causal conclusion.

## 5. Conveyance link

```yaml
stormwater_conveyance_link:
  link_id: null
  stormwater_system_id: null
  from_node_ref: null
  to_node_ref: null
  link_form: authored_or_unknown
  maintenance_asset_ref: null
  current_availability: UNKNOWN
  blockage_observation_ids: []
  isolation_refs: []
  verification_ids: []
  last_transition_at: null
```

Possible authored forms include storm sewer, open drain, ditch, channel, culvert connection or another canon-supported solution.

Do not infer hidden network links because Minecraft pipes, trenches or water blocks touch.

## 6. Culvert / crossing drainage asset

```yaml
stormwater_culvert:
  culvert_id: null
  stormwater_system_id: null
  road_or_travel_asset_refs: []
  upstream_node_ref: null
  downstream_node_ref: null
  maintenance_asset_ref: null
  operational_state: UNKNOWN
  debris_or_obstruction_observation_ids: []
  post_event_inspection_ids: []
  restriction_refs: []
  last_verified_at: null
```

Suggested states:

- UNKNOWN
- AVAILABLE
- DEGRADED
- OBSTRUCTED
- DAMAGED_OR_SUSPECTED
- ISOLATED
- UNDER_MAINTENANCE
- TESTING
- VERIFIED
- DECOMMISSIONED

Critical boundary:

`WATER_RECEDED != CULVERT_VERIFIED != ROAD_REOPENED`.

Road Operations decides road access after it consumes the relevant evidence.

## 7. Stormwater storage / attenuation asset

```yaml
stormwater_storage_asset:
  storage_asset_id: null
  stormwater_system_id: null
  location_id: null
  storage_form: authored_or_unknown
  maintenance_asset_ref: null
  upstream_link_ids: []
  downstream_link_ids: []
  broad_storage_state: UNKNOWN
  operational_state: UNKNOWN
  overflow_observation_ids: []
  ecology_refs: []
  access_restriction_ids: []
  last_verified_at: null
```

Possible broad storage bands:

- UNKNOWN
- EMPTY_OR_NEAR_EMPTY
- AVAILABLE
- OCCUPIED
- HIGH
- AT_AUTHORED_LIMIT
- OVERFLOW_OBSERVED

These are continuity bands only. They are not volume or design-capacity calculations.

The schema may represent a basin, pond, tank, low area or another authored form. It does not establish that any particular technology exists in Ouros.

## 8. Drainage pump station

```yaml
stormwater_pump_station:
  pump_station_id: null
  stormwater_system_id: null
  location_id: null
  maintenance_asset_refs: []
  power_dependency_ref: null
  upstream_node_refs: []
  downstream_node_refs: []
  current_state: UNKNOWN
  operating_record_ids: []
  verification_ids: []
  restriction_ids: []
```

Suggested states:

- UNKNOWN
- STANDBY
- READY
- RUNNING
- LIMITED
- FAULTED
- ISOLATED
- UNDER_MAINTENANCE
- TESTING
- VERIFIED
- DECOMMISSIONED

Critical separation:

`PUMP_RUNNING != UPSTREAM_AREA_DRAINED`.

Power availability, pump readiness, successful operation, downstream path availability and observed drainage remain separate facts.

## 9. Outfall / receiving handoff

```yaml
stormwater_outfall:
  outfall_id: null
  stormwater_system_id: null
  location_id: null
  receiving_system_ref: null
  upstream_link_ids: []
  operational_state: UNKNOWN
  restriction_ids: []
  observation_ids: []
  verification_ids: []
  ecology_interface_refs: []
```

An outfall may hand off to a Water Management, coastal, river or other authored receiving system.

Stormwater Continuity does not infer receiving-water quality, ecological harm or legal authorization from visible discharge.

## 10. Drainage path

```yaml
stormwater_drainage_path:
  drainage_path_id: null
  stormwater_system_id: null
  source_collection_refs: []
  ordered_link_or_asset_refs: []
  target_storage_or_outfall_ref: null
  authorization_refs: []
  current_state: UNKNOWN
  verification_ids: []
  supersedes_path_id: null
```

Suggested states:

- UNKNOWN
- AVAILABLE
- DEGRADED
- BLOCKED
- ISOLATED
- TEMPORARY
- TESTING
- VERIFIED
- SUPERSEDED

A path is authored. It is never reconstructed automatically from Minecraft geometry.

## 11. Flood / ponding observation

```yaml
surface_water_observation:
  observation_id: null
  geographic_scope_id: null
  related_catchment_sector_ids: []
  observed_at: null
  observer_id: null
  observation_kind: null
  broad_extent_band: UNKNOWN
  affected_asset_refs: []
  evidence_refs: []
  weather_observation_refs: []
  possible_cause_claim_ids: []
  confidence: UNKNOWN
```

Possible kinds:

- PONDING
- STREET_FLOODING
- UNDERPASS_FLOODING
- PROPERTY_EDGE_FLOODING
- CHANNEL_OVERTOPPING_OBSERVED
- DRAINAGE_BACKUP_OBSERVED
- RAPID_RECESSION
- SLOW_RECESSION
- UNKNOWN_SURFACE_WATER

The layer stores what was observed, not a guessed hydraulic cause.

`RAINFALL_OBSERVED != FLOODING_CONFIRMED`.

`FLOODING_OBSERVED != CAUSE_CONFIRMED`.

## 12. Blockage / obstruction observation

```yaml
stormwater_obstruction_observation:
  obstruction_observation_id: null
  subject_asset_ref: null
  observed_at: null
  observer_id: null
  observed_material_description: null
  evidence_refs: []
  access_effect_observed: null
  causal_claim_ids: []
  removal_operation_refs: []
  verification_ids: []
```

Do not infer vandalism, negligence, Pokémon responsibility, waste source or deliberate sabotage from an obstruction alone.

Waste/Sanitation or Case systems may investigate provenance where appropriate.

## 13. Temporary pumping / bypass / diversion

```yaml
stormwater_temporary_mitigation:
  mitigation_id: null
  affected_sector_ids: []
  mitigation_kind: authored
  temporary_asset_refs: []
  alternate_path_refs: []
  activation_state: PLANNED
  activated_at: null
  capacity_band: UNKNOWN
  dependency_refs: []
  restriction_refs: []
  review_due_at: null
  removal_or_handoff_refs: []
  history_event_ids: []
```

Possible states:

- PLANNED
- READY
- ACTIVE
- ACTIVE_LIMITED
- PAUSED
- FAILED_OR_UNAVAILABLE
- TESTING
- DEACTIVATING
- CLOSED

A temporary pump, ditch, barrier or alternate path can become a remembered landmark or future emergency asset after the incident ends.

No flow amount or runtime is invented.

## 14. Restoration sequence

```yaml
stormwater_restoration_sequence:
  restoration_sequence_id: null
  incident_or_outage_ref: null
  stormwater_system_id: null
  affected_sector_ids: []
  prerequisite_refs: []
  ordered_checkpoint_ids: []
  current_checkpoint_id: null
  blocked_by_refs: []
  temporary_mitigation_refs: []
  status: PLANNED
```

Potential checkpoints, only where applicable:

1. active weather threat reduced or operating window established;
2. emergency access restrictions established;
3. inlet/culvert/affected asset inspected;
4. obstruction isolated or removed where authorized;
5. drainage path restored or temporary path activated;
6. pump/other technical dependency verified where applicable;
7. affected surface-water area observed as receding/drained;
8. drainage sector operationally verified;
9. Road/Residential/Commercial/Care or other downstream owner reviews its own state;
10. temporary mitigation is removed, retained or converted by a separate decision.

Critical separations:

`RAIN_STOPPED != FLOOD_RECEDING`

`FLOOD_RECEDING != DRAINAGE_PATH_VERIFIED`

`INLET_CLEAR != DOWNSTREAM_AVAILABLE`

`PUMP_RUNNING != SECTOR_DRAINED`

`SECTOR_DRAINED != SECTOR_VERIFIED`

`SECTOR_VERIFIED != ROAD_REOPENED`

`ROAD_DRY != BUILDING_READY`

## 15. Contradictory reports and provenance

Statements such as “the flooding ended at 14:00” need scope.

Possible legitimate timestamps include:

- rain stopped;
- peak surface water was observed;
- one intersection became passable;
- a pump began operation;
- an obstruction was cleared;
- an underpass drained;
- a culvert passed inspection;
- a drainage sector passed verification;
- a road restriction was lifted;
- a building reopened.

Store the subject, location, time and evidence rather than overwriting them with one universal recovery timestamp.

## 16. Ecology boundary

A drainage corridor may also be habitat or a movement route.

Conservation/Wildlife may reference:

- repeated Pokémon use;
- nesting or shelter observations;
- displacement after flooding;
- new use of a retention area;
- conflict between maintenance access and habitat use.

Stormwater Continuity never infers ecological harm, benefit, ownership, hostility or causal responsibility from presence alone.

A Pokémon repeatedly seen before flooding may be a clue. It is not automatically a predictor or cause.

## 17. Legacy drainage and place memory

A decommissioned drain, culvert, pump house, channel, retention basin or old outfall remains a place.

Later uses may include:

- wildlife habitat;
- service access;
- walking route;
- industrial-history evidence;
- temporary emergency bypass;
- misunderstood old map feature;
- informal neighborhood landmark;
- archaeological or infrastructure-history evidence;
- reused public space.

Historical operation never proves current usability.

## 18. Pokémon participation boundary

Any Pokémon performing operational work needs individual identity, assignment and exact governing evidence where mechanics matter.

Never infer from species, Type, body shape, animation or flavor that a Pokémon can:

- sense floods;
- predict rainfall;
- clear drains;
- remove arbitrary debris;
- operate pumps;
- swim safely in floodwater;
- resist contamination;
- carry unlimited loads;
- excavate culverts;
- divert water;
- repair infrastructure;
- work indefinitely for an institution.

A source may inspire a candidate role. It cannot create a PTU rule.

## 19. Encounter contract — Flooded Underpass Withdrawal

Narrative premise:

An underpass is already closed after surface flooding. A hostile or territorial encounter develops near the safe approach while responders need to withdraw from the immediate area.

FULL intended version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

The full form would need validated wet/flooded zones, possible environmental displacement only if an exact rule exists, withdrawal objectives, generalized reactions, tactical policy and semantic playback.

Current authoring profile: REDUCED.

REDUCED version:

Close the underpass in world state before battle. Keep floodwater, vehicles, responders, civilians and pumping equipment outside BattleSpec. Select combatants explicitly on a reviewed dry static approach. Victory establishes only that the immediate safe approach is secure. Drainage, inspection and road reopening proceed separately.

## 20. Encounter contract — Culvert Access Perimeter

Narrative premise:

A culvert needs post-storm inspection, but a territorial situation blocks the service approach.

FULL intended version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

The full version particularly wants route protection, withdrawal/territorial policy, generalized reactions and reviewed edge/water/debris zones if mechanically supported.

Current authoring profile: REDUCED.

REDUCED version:

Inspectors remain outside the tactical scene. The culvert interior, flowing water, debris and equipment are noninteractive. AutoPTU receives a static dry service-path arena. Winning may allow an inspection team to approach later. It does not clear, repair or verify the culvert.

## 21. Encounter contract — Temporary Pump Site Perimeter

Narrative premise:

A temporary drainage pump or bypass is active after flooding. The operational site needs a safe perimeter while the technical process continues outside tactical resolution.

FULL intended version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Active hoses, cables, moving water, energized equipment, mud or vehicle interactions require exact environmental/tactical contracts and therefore remain outside the current safe profile.

Current authoring profile: REDUCED.

REDUCED version:

Freeze the temporary mitigation state before battle. Evacuate workers and ordinary residents. Keep pump, hoses, water, vehicles and technical assets outside the grid. Use an adjacent static arena. Battle outcome cannot start, stop, repair or verify the drainage operation.

## 22. Minecraft/Cobblemon authority boundary

Safe presentation reuse, subject to actual API review, may include:

- streets, gutters, drains and manholes as geometry/props;
- culverts, channels, basins and pump buildings;
- temporary barriers, cones, hoses and signs;
- authored water-level visuals;
- rain, sounds and particles;
- Pokémon overworld entities, models, forms, poses, animations and cries;
- workers/NPCs;
- UI, networking, entity tracking and persistence hooks.

Adapter-required behavior includes:

- stable stormwater-system/sector/asset IDs;
- projection of authoritative closures and temporary configurations;
- binding inspected assets to world locations;
- reviewed world-to-BattleSpec conversion;
- semantic playback of battle results without transferring world-state authority to Minecraft.

Minecraft/Cobblemon must never decide:

- drainage topology because blocks touch;
- system capacity from visible pipe size;
- flooding from native water spread alone;
- culvert blockage from item entities alone;
- road reopening because water blocks disappeared;
- pump success from redstone or animation;
- PTU current, drowning, slipping, collision, debris or electric damage;
- forced movement from flowing water;
- Pokémon flood-warning ability from species identity;
- combatants from nearby entities;
- HP/status/position/legality/result through Cobblemon BattleState or controller logic.

Binding remains:

`Ouros stormwater/world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## 23. Canon-status policy

Everything in this extension is PROPOSED architecture.

Specific drainage systems, sewer separation, culverts, pumps, basins, operators, flood-control practices, technology, access rules and maintenance institutions remain UNKNOWN until canon-approved.

No schema example creates a setting fact or PTU mechanic.