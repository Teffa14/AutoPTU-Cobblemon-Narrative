# Ouros Alpine Mountain & Elevation Zonation Layer

Status: proposed systems design. Not established Ouros canon.

Pass: 84.

## Purpose

This layer gives mountain systems persistent identity across elevation bands, slope aspects, treeline, passes, staging sites and alpine/subalpine ecology.

It complements rather than replaces:

- Cryosphere for snowpack, glaciers and freeze/thaw;
- Meteorology for weather observations and forecasts;
- Travel for routes and transport services;
- Cartography for maps and route knowledge;
- Soil for erosion/compaction/substrate state;
- Flora for vegetation communities and succession;
- Freshwater for headwaters and meltwater;
- Geology for substrate/rock history;
- Architecture for huts, stations and mountain structures;
- Tourism for visitor pressure;
- Crisis for rescue/closure response.

It does not define climbing DCs, altitude sickness, falling damage, high-altitude Weather, cliff cover, movement penalties, Mountable eligibility, Naturewalk, Wilderness Guide effects or other PTU mechanics.

## 1. Persistent mountain identity

```yaml
mountain_system:
  mountain_system_id: null
  approved_name: null
  aliases: []
  region_refs: []
  geology_refs: []
  catchment_refs: []
  cryosphere_refs: []
  vertical_zone_ids: []
  slope_sector_ids: []
  pass_ids: []
  staging_site_ids: []
  landmark_ids: []
  route_refs: []
  observation_refs: []
  historical_revision_refs: []
  current_projection_revision_id: null
```

The mountain remains the same entity while trails, snowline, treeline, stations and ecological use change.

## 2. Vertical ecological zones

Use coarse ecological bands rather than per-block elevation simulation.

```yaml
mountain_vertical_zone:
  zone_id: null
  mountain_system_id: null
  zone_type: null
  approximate_elevation_range_ref: null
  aspect_scope_refs: []
  vegetation_refs: []
  snow_persistence_refs: []
  habitat_refs: []
  route_refs: []
  observation_refs: []
  revision_id: null
```

Candidate zone types:

- LOWER_MONTANE
- UPPER_MONTANE
- SUBALPINE_FOREST
- TREELINE_ECOTONE
- ALPINE_MEADOW
- ALPINE_TALUS
- ALPINE_RIDGE
- SNOWBED_COMPLEX
- SUMMIT_ZONE
- OTHER_AUTHORED

These are ecological/world-state categories. They never create PTU Terrain automatically.

## 3. Slope sectors and aspect

A mountain should not have one environmental state at each elevation.

```yaml
mountain_slope_sector:
  slope_sector_id: null
  mountain_system_id: null
  aspect_class: null
  slope_class: null
  exposure_class: null
  shelter_refs: []
  snow_persistence_refs: []
  vegetation_refs: []
  soil_refs: []
  route_refs: []
  observation_refs: []
```

Candidate aspect classes:

- NORTH_FACING
- SOUTH_FACING
- EAST_FACING
- WEST_FACING
- RIDGELINE
- BASIN
- LEE_SLOPE
- WINDWARD_SLOPE
- COMPLEX

Aspect can explain different vegetation or snow histories on two sides of the same massif. It does not create mechanical Accuracy, Speed or Weather effects.

## 4. Treeline as a revisable ecotone

```yaml
treeline_revision:
  treeline_revision_id: null
  mountain_system_id: null
  effective_window_ref: null
  sector_geometries: []
  observed_patch_refs: []
  vegetation_refs: []
  snow_history_refs: []
  disturbance_refs: []
  evidence_refs: []
  interpretation_refs: []
  supersedes_revision_id: null
```

Treeline should be represented as a transition band with local exceptions.

The system must preserve previous revisions for historical maps, photography, science and Chronicle callbacks.

## 5. Mountain passes

Pass identity is persistent even when route usability changes.

```yaml
mountain_pass:
  pass_id: null
  mountain_system_id: null
  endpoint_refs: []
  route_ref: null
  physical_geometry_ref: null
  access_state_ref: null
  snow_state_ref: null
  slope_stability_ref: null
  weather_exposure_ref: null
  maintenance_ref: null
  service_refs: []
  closure_refs: []
  observation_refs: []
```

Travel remains authoritative for whether a route can currently be traversed.

The mountain layer supplies environmental context and persistent identity.

## 6. Staging sites

```yaml
mountain_staging_site:
  staging_site_id: null
  mountain_system_id: null
  site_type: null
  structure_ref: null
  elevation_zone_ref: null
  route_refs: []
  staffing_refs: []
  service_refs: []
  shelter_state_ref: null
  supply_state_ref: null
  communications_ref: null
  observation_refs: []
  public_memory_refs: []
```

Candidate site types:

- TRAILHEAD
- HUT
- CABIN
- SURVEY_STATION
- WEATHER_STATION
- CABLE_STATION
- SHELTER
- PATROL_POST
- RESEARCH_PLATFORM
- INFORMAL_CAMP
- SUMMIT_STATION

A staging site may become a recurring social node without becoming automatic healing or fast travel.

## 7. Mountain observations

```yaml
mountain_observation:
  observation_id: null
  mountain_system_id: null
  slope_sector_id: null
  vertical_zone_id: null
  observed_at: null
  observer_ids: []
  observation_type: null
  observed_state: {}
  instrument_refs: []
  source_refs: []
  uncertainty: null
```

Possible observation types:

- TREELINE_POSITION
- SNOWBED_PERSISTENCE
- BLOOM_WINDOW
- WILDLIFE_USE
- TRAIL_CONDITION
- ROCKFALL_EVIDENCE
- WIND_EXPOSURE
- VISIBILITY
- SPRING_STATE
- HUMAN_USE
- ROUTE_MARKER_STATE
- LANDMARK_CHANGE

Observation does not equal interpretation.

## 8. Elevation-linked ecology

Species presence may differ by zone, season, aspect or route use.

Record evidence such as:

```yaml
mountain_pokemon_use_observation:
  observation_id: null
  pokemon_entity_id: null
  species_ref: null
  collective_ref: null
  zone_ref: null
  sector_ref: null
  behavior_tags: []
  observed_at: null
  source_refs: []
  uncertainty: null
```

Do not infer:

- that a Pokémon belongs permanently to that elevation;
- that a group has Pack Mon;
- that the largest member is leader;
- that a mountainous Pokédex description grants traversal to a Trainer;
- that mountain residence grants Naturewalk;
- that a Pokémon seen on a steep slope can carry passengers there.

## 9. Expedition segmentation

A long ascent should be decomposable into legs.

```yaml
mountain_expedition_leg:
  leg_id: null
  expedition_ref: null
  start_site_ref: null
  end_site_ref: null
  route_ref: null
  vertical_zone_refs: []
  known_conditions_refs: []
  supply_dependency_refs: []
  observation_objectives: []
  optional_detour_refs: []
  unresolved_risk_refs: []
```

This supports a Sky-Peak-like structural lesson without copying its exact station system.

Each leg can have its own closure, weather, ecology and social state while still belonging to one mountain expedition.

## 10. Mountain state changes over years

Potential persistent changes include:

- treeline shift;
- snowbed persistence change;
- route rerouting;
- shelter construction or abandonment;
- cable/service installation;
- wildfire scar;
- landslide or erosion;
- new spring observation;
- visitor-pressure change;
- habitat use change;
- restored trail;
- closed shortcut;
- changed summit access;
- new monitoring station;
- changed public memory or naming.

These should be causal and versioned.

## 11. Minecraft projection

The server-authoritative mountain state can project to Minecraft through coarse variants:

- vegetation palette by band;
- persistent snow/snowbed variants;
- trail open/closed presentation;
- route markers;
- staging structures;
- damaged/restored structures;
- observation equipment;
- temporary closures;
- visual slope-sector differences;
- visitor/NPC cohort presence;
- wildlife presence derived from ecology systems.

Loaded blocks do not become the source of truth for treeline, route history or ecological state.

## 12. Battle snapshot boundary

A mountain encounter should freeze a deterministic tactical snapshot before AutoPTU starts.

The snapshot may safely use already-verified geometry and static blockers.

It may not infer:

- cliff-edge knockback;
- falling damage;
- rockfall hazards;
- wind displacement;
- snow movement penalties;
- altitude damage;
- changing fog/visibility;
- dynamic avalanche terrain;
- mountain-specific Accuracy penalties;
- automated Naturewalk;
- climbing movement;
- shelter cover;
- summit buffs.

Any of those require exact PTU/Caelo authority and implementation evidence.

## 13. Encounter contract — Treeline Survey Dispute

Narrative premise:

Two research teams mapped different treelines on opposite slopes and both datasets appear internally consistent. Players need to inspect slope/aspect, old photographs, weather history and route changes before deciding whether the records actually conflict.

FULL version:

- moving across elevation bands during the encounter;
- multiple elevation platforms;
- changing visibility/wind zones;
- withdrawal routes;
- objective-aware AI that can disengage rather than fight to KO;
- world-state writeback from protected survey points.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED for static geometry;
- base movement legality: VERIFIED for current static surface;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for rich edge/disengagement behavior;
- terrain/weather/hazards/zones/reactions: BLOCKING for wind/visibility/elevation effects;
- AI tactical policy: BLOCKING for survey/withdraw objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

Resolve surveying in overworld state. If combat occurs, freeze one safe slope sector into a static arena with no altitude, wind or cliff mechanics. Afterwards write the observed survey result back to the mountain graph.

## 14. Encounter contract — Pass Shelter Evacuation

Narrative premise:

A mountain shelter becomes temporarily unusable while several route users and Pokémon groups need access to the same pass.

FULL version needs:

- protected/exit zones;
- multiple safe paths;
- noncombatant movement;
- interception/forced movement rules if relevant;
- objective-aware withdrawal/protection AI;
- dynamic environmental conditions only if separately verified.

REDUCED version:

Resolve evacuation and routing before battle. Keep civilians and noncombatant Pokémon outside the grid. Use a static legal combat if a real confrontation remains.

## 15. Encounter contract — Summit Relay Failure

Narrative premise:

A communications relay at a summit stops reporting while weather stations below remain operational. Players must determine whether the failure is power, maintenance, environmental damage, signal path or something else.

FULL version can eventually include:

- interactable relay objective;
- severe weather projection;
- changing zones;
- tactical withdrawal;
- objective-aware AI.

REDUCED version:

The relay investigation, weather and repair remain overworld state. Any battle occurs on a static cleared platform. Relay success is committed after the battle through the world-state system.

## 16. Rules boundary

The available Python AutoPTU evidence contains a specific Wilderness Guide branch for `mountain`/`cave`. That feature proves only its exact authored behavior when the Trainer legally has and activates it.

It does not authorize generic mountain mechanics.

Before implementing climbing, falling, altitude, cliff edges, wind, snow, exposure or mountain traversal, extract the exact PTU/Caelo rules and verify Java support.

## 17. Promotion checklist

A proposed mountain can enter canon only after:

1. geographic placement is approved;
2. geology and hydrology do not conflict with existing maps;
3. authored elevation bands are coherent with regional climate;
4. named routes and staging sites have provenance;
5. important Pokémon relationships are authored or evidence-backed;
6. tourism/conservation/institutional roles are consistent;
7. any mechanical effects have explicit PTU/Caelo authority;
8. AutoPTU dependencies are classified honestly;
9. Minecraft projection does not become rules authority;
10. the mountain remains compatible with future state revisions.