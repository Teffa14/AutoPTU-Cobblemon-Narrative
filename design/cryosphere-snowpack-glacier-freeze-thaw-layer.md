# Ouros Cryosphere, Snowpack, Glacier & Freeze-Thaw Layer

Status: PROPOSED SYSTEMS ARCHITECTURE. Not established Ouros canon.

Pass: 65
Date: 2026-08-20

## Purpose

Cold landscapes in Ouros need persistent state between weather events.

Snowfall should be able to accumulate into a route condition. A winter's snowpack should be able to influence spring runoff. A glacier should retain identity while its edge moves. Frozen ground should be able to thaw and affect a building, road or wetland. An avalanche path should remain a known landscape feature after the snow settles.

This layer provides that continuity.

It does not create PTU cold, snow, ice, avalanche or exposure mechanics.

## Existing layers remain authoritative for their own concerns

This layer connects to existing systems rather than replacing them.

Seasonality owns expected seasonal cycles and calendar state.

Meteorology owns current weather observations, models and forecasts.

Freshwater owns catchments, streams, lakes, groundwater and water-control assets.

Travel owns route graphs, services, journeys and route eligibility.

Crisis owns emergency response, missing-actor searches and recovery operations.

Conservation owns protected areas, habitat management and restoration.

Geology owns substrate, excavation context and geological sites.

Cartography owns maps, editions, route traces and actor knowledge.

Architecture owns physical structures, versions and adaptive reuse.

AutoPTU owns tactical rules when a battle begins.

Minecraft/Cobblemon displays a projection of world state. It does not become the source of truth for snowpack, glacier mass, route safety or battle mechanics.

## Core separation

Keep these states separate:

1. Cryosphere truth — current regional snow, ice, glacier and frozen-ground state.
2. Observation — what a person, station, Pokémon or instrument actually observed.
3. Interpretation — what an actor thinks the observations mean.
4. Forecast / hazard assessment — a time- and place-scoped prediction.
5. Route / service state — whether travel is currently available under existing rules.
6. Ecological response — observed or modeled changes in habitat and Pokémon presence.
7. Infrastructure response — damage, maintenance, closure or adaptation.
8. Tactical projection — the frozen battlefield state passed to AutoPTU, if validated.

A forecast does not become truth merely because an institution published it.

A Minecraft snow block does not prove a deep snowpack.

An icy texture does not prove a PTU hazard.

## CRYOSPHERE_REGION

A regional container links cold-state objects without forcing every place to use the same seasonal pattern.

```yaml
cryosphere_region_id: null
region_id: null
active_snowpack_ids: []
glacier_ids: []
permafrost_patch_ids: []
seasonal_ice_cover_ids: []
avalanche_path_ids: []
cold_route_refs: []
monitoring_station_refs: []
catchment_refs: []
current_revision: 1
source_refs: []
```

A warm region can have only a high-elevation cryosphere region. A polar or alpine region can contain many.

Do not assume a universal four-season model.

## SNOWPACK_STATE

Snowpack is persistent accumulated state rather than current weather.

```yaml
snowpack_id: null
area_ref: null
valid_from: null
valid_to: null
coverage_class: UNKNOWN
relative_depth_class: UNKNOWN
layer_summary: []
surface_state: UNKNOWN
recent_weather_refs: []
observation_refs: []
confidence: UNKNOWN
supersedes: null
```

Suggested coarse coverage classes:

- NONE
- PATCHY
- CONTINUOUS_SHALLOW
- CONTINUOUS_MODERATE
- CONTINUOUS_DEEP
- UNKNOWN

These are narrative/world-state categories. They do not produce movement modifiers.

Possible surface descriptions can include fresh, wind-affected, crusted, melting or unknown. These descriptions require evidence and remain non-mechanical unless a validated rules contract consumes them.

### Snowpack versions

Never rewrite an old snowpack record when conditions change.

Create a new revision.

This enables:

- comparing this winter with previous winters;
- validating forecasts;
- explaining later meltwater changes;
- reconstructing route history;
- preserving research provenance.

## SNOW_LAYER_OBSERVATION

A field observation should reveal a local sample, not the entire mountain.

```yaml
observation_id: null
snowpack_id: null
location_ref: null
observed_at: null
observer_ids: []
method_ref: null
layer_notes: []
surface_notes: []
uncertainty_notes: []
media_refs: []
source_refs: []
```

Two observations can disagree because they were made on different aspects, elevations or times.

Do not collapse disagreement into one average unless a research method explicitly does so.

## GLACIER_BODY

A glacier has persistent identity across changing geometry.

```yaml
glacier_id: null
region_id: null
name_state: null
terminus_versions: []
coverage_versions: []
accumulation_state: UNKNOWN
loss_state: UNKNOWN
trend_assessment_refs: []
meltwater_connection_refs: []
adjacent_lake_refs: []
exposed_site_refs: []
historical_map_refs: []
observation_refs: []
```

The visible glacier edge in Minecraft is a version of the glacier state.

It is not the glacier's identity.

### Glacier trend

Use coarse trend states until actual world simulation exists:

- ADVANCING_OBSERVED
- STABLE_WITHIN_OBSERVATION
- RETREATING_OBSERVED
- MIXED_OR_UNCERTAIN
- UNKNOWN

Trend requires observations across time.

A warm day does not make a glacier `RETREATING_OBSERVED` by itself.

## GLACIER_TERMINUS_VERSION

```yaml
terminus_version_id: null
glacier_id: null
effective_at: null
geometry_ref: null
measurement_method: null
observation_refs: []
confidence: null
supersedes: null
```

This can power historical maps and long-term Minecraft changes without modifying old Chronicle entries.

## GLACIAL_LAKE

A lake associated with a glacier must connect to Freshwater.

```yaml
glacial_lake_id: null
freshwater_body_ref: null
glacier_refs: []
formation_state: UNKNOWN
water_level_class: UNKNOWN
containment_type_claims: []
outlet_refs: []
monitoring_refs: []
hazard_assessment_refs: []
```

Do not generate an outburst merely because the lake exists.

Any sudden-drainage event needs world-state cause/evidence and Crisis integration.

## FREEZE_THAW_STATE

Freeze/thaw is a transition state for water, soil or infrastructure context.

```yaml
freeze_thaw_id: null
area_ref: null
material_context: null
state: UNKNOWN
last_transition_at: null
observation_refs: []
infrastructure_refs: []
hydrology_refs: []
```

Possible narrative states:

- FROZEN
- PARTIALLY_THAWED
- THAWED
- REFREEZING
- VARIABLE
- UNKNOWN

These are world descriptions only.

They do not grant Slow Terrain, Rough Terrain, Tripped, Frozen or any other PTU effect.

## PERMAFROST_PATCH

```yaml
permafrost_patch_id: null
area_ref: null
known_extent_ref: null
active_layer_state: UNKNOWN
seasonal_observation_refs: []
structure_dependency_refs: []
hydrology_dependency_refs: []
ecology_refs: []
```

Permafrost can connect to:

- foundation movement;
- drainage changes;
- wetland state;
- roads;
- buried archaeological/geological material;
- vegetation change.

Every connection requires a causal record. Do not use permafrost as generic environmental damage flavor.

## SEASONAL_ICE_COVER

Frozen lakes, rivers or wetlands need a separate object from snow cover.

```yaml
ice_cover_id: null
water_body_ref: null
coverage_state: UNKNOWN
observation_window: null
observation_refs: []
route_permission_ref: null
public_notice_refs: []
```

The system must not infer load-bearing safety from appearance.

If Ouros later supports travel over seasonal ice, eligibility must come from an authored institutional/rules contract, not visual thickness.

## AVALANCHE_PATH

An avalanche path is persistent landscape identity.

```yaml
avalanche_path_id: null
area_ref: null
runout_geometry_ref: null
historical_event_refs: []
habitat_refs: []
route_intersection_refs: []
structure_refs: []
current_assessment_ref: null
```

An avalanche path can simultaneously be:

- habitat;
- a travel constraint;
- a survey location;
- part of local history;
- a hazard under specific conditions.

It is not permanently `dangerous=true`.

## AVALANCHE_ASSESSMENT

```yaml
assessment_id: null
avalanche_path_ids: []
issued_at: null
valid_window: null
spatial_scope: null
snowpack_refs: []
weather_refs: []
observation_refs: []
assessment_class: null
uncertainty_notes: []
issuer_ref: null
```

This is a forecast product.

The exact assessment scale is a future canon decision. Do not import real-world danger scales as a game rule by default.

## CRYOSPHERE_OBSERVATION

Use a general observation object for measurements or sightings that do not fit snow layers.

```yaml
cryosphere_observation_id: null
observation_type: null
location_ref: null
observed_at: null
observer_ids: []
value_or_class: null
instrument_ref: null
quality_notes: []
source_refs: []
```

Examples:

- snowline elevation estimate;
- glacier terminus marker;
- frozen-lake extent;
- spring melt onset;
- ice cave opening;
- avalanche debris extent;
- permafrost thaw observation;
- meltwater discharge observation.

## DEGLACIATION_PATCH

Newly exposed terrain should not jump from `ice` to generic mature biome.

```yaml
deglaciation_patch_id: null
former_glacier_id: null
exposed_since: null
substrate_ref: null
succession_state: NEWLY_EXPOSED
observation_refs: []
pokemon_presence_refs: []
plant_presence_refs: []
conservation_refs: []
```

Possible coarse succession states:

- NEWLY_EXPOSED
- EARLY_COLONIZATION
- DEVELOPING_PATCH
- ESTABLISHED_HABITAT
- UNKNOWN

These stages must be evidence-driven and region-specific.

## COLD_ROUTE_STATE

Travel needs a route-facing projection rather than reading raw snow directly.

```yaml
cold_route_state_id: null
route_id: null
valid_from: null
status: UNKNOWN
reason_refs: []
cryosphere_refs: []
service_refs: []
shelter_refs: []
forecast_refs: []
last_verified_at: null
```

Possible route statuses remain owned by the Travel layer.

The cryosphere layer only supplies causes/evidence such as:

- snow accumulation;
- freeze-thaw damage;
- avalanche assessment;
- seasonal ice state;
- exposed crevasse field;
- glacier movement;
- meltwater crossing.

## Shelters and cold-route infrastructure

Cold travel can make route infrastructure meaningful.

Examples:

- cabins;
- ranger posts;
- route markers;
- emergency caches;
- maintenance depots;
- lift stations;
- weather/snow stations;
- bridge or tunnel portals.

These are Architecture/Infrastructure assets.

The Cryosphere layer records why they matter to a cold route.

### Anti-softlock contract

A route state transition must not trap a player in invalid geography without a defined recovery path.

Before a cold route can close around active players, one of the following must exist:

- valid return path;
- valid onward path;
- safe shelter plus later reopening rule;
- authorized extraction;
- instance/checkpoint recovery policy.

Fast travel cannot silently ignore the closure unless Travel explicitly permits it.

## Weather → snowpack contract

Meteorology can send verified weather events into cryosphere state.

Example:

```text
snowfall observation
  -> accumulation update candidate
  -> cryosphere validation
  -> new SNOWPACK_STATE revision
```

Meteorology does not directly set route closure or PTU terrain.

Likewise, one warm day does not erase the snowpack.

## Snowpack → Freshwater contract

Melt is a bridge event.

```yaml
melt_event_id: null
snowpack_refs: []
valid_window: null
melt_class: null
catchment_reach_refs: []
observation_refs: []
```

Freshwater then owns the receiving water response.

This supports delayed consequences such as:

- earlier spring peak;
- lower late-season flow;
- wetland reconnection;
- reservoir refill;
- route crossing change.

No water quantity formula is assumed.

## Glacier → Geology / Archaeology contract

Retreat or collapse can expose material.

Exposure event:

```yaml
ice_exposure_event_id: null
glacier_id: null
location_ref: null
discovered_at: null
exposed_object_or_site_refs: []
provenance_refs: []
access_state: null
```

Possible outputs include:

- fossil-bearing layer;
- geological contact;
- old infrastructure;
- historical object;
- cave entrance;
- no significant discovery.

The discovery does not transfer ownership.

## Cryosphere ecology

Cold-state ecology should use observed relationships rather than generic Ice-type logic.

Potential world-state links:

- fresh-snow availability for a species that uses it;
- snowline-associated seasonal movement;
- food-resource loss after a storm;
- use of avalanche-path openings;
- colonization of deglaciated ground;
- access to frozen wetlands;
- retreat from heavily trafficked winter routes.

Never infer:

- all Ice-type Pokémon prefer deep snow;
- all Fire-type Pokémon avoid cold regions;
- a species' battle Ability controls its regional habitat;
- Snow weather should spawn because Ice Pokémon are present.

## Cold archaeology and paleontology

Perennial snow/ice can preserve context.

A discovered specimen should retain:

- exact discovery location;
- ice/glacier context;
- discoverer;
- extraction method;
- custody chain;
- storage requirements if authored;
- later interpretation.

Melting ice can create urgency because context may change, but the system must not invent a countdown without world-state support.

## Winter culture and recreation

Snow and ice can support ordinary life:

- seasonal markets;
- local races;
- ice routes;
- snow sculpture;
- winter observatories;
- community maintenance days;
- school surveys;
- seasonal festivals.

These must be original Ouros traditions if promoted to canon.

A frozen surface used recreationally still needs independent route/access assessment where safety matters.

## Minecraft projection

Do not simulate every snow layer or glacier cell as authoritative world state.

Use coarse spatial patches and versioned geometry.

Potential visual projections:

- snow-cover classes;
- snowline;
- glacier terminus;
- marked avalanche paths;
- frozen-water surface;
- route markers;
- seasonal barriers;
- meltwater channels;
- exposed moraine or rock;
- shelters and monitoring stations.

The server state must survive unloaded chunks.

Minecraft weather and snow blocks are presentation/input observations, not canonical state by themselves.

## Accessibility

Snowstorms and whiteout presentation must preserve critical information through more than one channel.

Possible equivalents:

- high-contrast route markers;
- map route state;
- text warning;
- subtitles for marker beacons;
- waypoint shape differences;
- optional reduced-particle presentation;
- explicit shelter direction.

Do not make a required puzzle depend solely on distinguishing white-on-white visual cues.

## Tactical projection boundary

A cryosphere state can become battle state only through a reviewed projection contract.

Required flow:

```text
regional cryosphere revision
  -> encounter author selects relevant facts
  -> PTU/Caelo mechanical review
  -> Java capability review
  -> frozen BattleSpec projection
  -> AutoPTU resolves battle
  -> semantic result writes back to world state
```

Minecraft cannot invent the missing rules between those steps.

## Mechanical non-inference rules

Narrative snow or ice never automatically creates:

- Frozen;
- Tripped;
- Slowed;
- Vulnerable;
- Accuracy/Evasion penalties;
- cold damage;
- hypothermia;
- snow blindness;
- initiative penalties;
- forced movement;
- fall damage;
- avalanche damage;
- crevasse damage;
- drowning;
- Hail/Snow Weather;
- Ice-type immunity;
- Fire-type weakness to ambient cold.

Python AutoPTU contains specific snow/hail, tundra and Frozen Domain behavior. Only those exact mechanics, after Java parity or an approved governing contract, may become tactical effects.

## Encounter contract A — Windslab Traverse

Narrative premise:

A survey party must cross a high route whose snowpack changed after wind and new snowfall. The objective is to inspect markers and reach a safe shelter while wild Pokémon activity continues nearby.

### FULL version

Could require:

- targeting / footprints / range / LoS;
- base movement legality;
- complete movement if sliding, displacement or interception can occur;
- core calculations;
- action economy / initiative;
- full lifecycle if conditions change by round;
- full damage/status only for actual legal attacks/effects;
- terrain / weather / hazards / zones / reactions for changing snow hazards;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- legal-action infrastructure;
- tactical AI for REACH_SHELTER / WITHDRAW / AVOID_ZONE behavior;
- Minecraft adapter/playback.

### REDUCED version

Resolve snowpack assessment and route selection before battle.

Freeze one stable shelf as the tactical arena.

Keep avalanche risk, deep snow and wind as world-state/presentation only.

If a real conflict occurs, AutoPTU receives only actual combatants and static geometry.

The party's crossing outcome is resolved after the battle through Travel/Cryosphere state.

## Encounter contract B — Meltwater Ice Cave

Narrative premise:

Seasonal melt exposes a cave entrance near a retreating ice edge. Researchers need to inspect a newly visible chamber while water conditions continue changing outside.

### FULL version

Could require changing terrain, meltwater hazards, route-to-exit objectives, forced movement, environmental reactions and tactical AI.

### REDUCED version

Choose and validate one cave revision before battle.

Water level and unstable ice do not change during the encounter.

Research, mapping and extraction occur in overworld state. If combat occurs, use static blockers and a normal legal encounter.

## Encounter contract C — Snowbound Relay Cabin

Narrative premise:

A route relay cabin stops reporting during a storm. The problem may be equipment failure, blocked access, absent staff, wildlife or several ordinary causes at once.

### FULL version

Could require weather-linked visibility, shelter zones, protection/withdrawal objectives, dynamic entrances and tactical AI.

### REDUCED version

Resolve storm, access and cabin condition before the battle.

If combat occurs, use the cabin and immediate exterior as fixed geometry. Weather remains visual unless exact PTU/Java effects are approved.

## Persistent writeback after cryosphere encounters

Battle result should not rewrite regional snow state automatically.

Potential writeback includes:

- route temporarily cleared;
- observation collected;
- actor displaced;
- equipment damaged or recovered;
- shelter access restored;
- Pokémon individual relocated;
- new evidence about a hazard;
- no cryosphere change.

The cryosphere only changes when a relevant event actually modifies it.

## Offline advancement

Use coarse scheduled transitions rather than continuous block simulation.

Possible scheduled processes:

- snowpack accumulation review after significant weather;
- spring melt phase update;
- seasonal lake-ice review;
- glacier terminus update at long intervals;
- permafrost seasonal active-layer update;
- route reopening review;
- succession update on deglaciated patches.

Player absence should not cause irreversible personal failure solely because a real-world timer advanced.

## Canon decisions required later

Before promotion, define:

- which Ouros regions contain glaciers, perennial snow or permafrost;
- which routes operate only in winter or summer;
- which institutions monitor snow and ice;
- whether avalanche forecasting exists and how it is communicated;
- which shelters and transport services are already established;
- which winter traditions are authored regional culture;
- how quickly glaciers can visibly change in world time;
- how Cobblemon populations respond to snowpack without becoming exploitable;
- exact PTU/Caelo rules for Snow/Hail, Frozen, tundra, Naturewalk and any environmental cold effects.

## Implementation blockers outside AutoPTU-Java

`OVERWORLD_CRYOSPHERE_STATE = BLOCKING`

`OVERWORLD_SNOWPACK_VERSIONING = BLOCKING`

`OVERWORLD_GLACIER_GEOMETRY_HISTORY = BLOCKING`

`OVERWORLD_FREEZE_THAW_STATE = BLOCKING`

`OVERWORLD_AVALANCHE_ASSESSMENT = BLOCKING`

`OVERWORLD_DEGLACIATION_SUCCESSION = BLOCKING`

`OVERWORLD_CRYOSPHERE_TO_FRESHWATER = BLOCKING`

`OVERWORLD_CRYOSPHERE_TO_TRAVEL = BLOCKING`

`OVERWORLD_CRYOSPHERE_TO_COBBLEMON = BLOCKING`

`OVERWORLD_CRYOSPHERE_TO_BATTLE = BLOCKING`

`OVERWORLD_CRYOSPHERE_TO_MINECRAFT = BLOCKING`

These belong to persistent world-state and adapter infrastructure, not the battle core.
