# Intertidal, Tidepool & Rocky-Shore Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 93

## Purpose

This layer represents the ecological and navigational edge that repeatedly changes between submerged and exposed states during ordinary tides.

It owns persistent intertidal-site identity, coarse tidal exposure zones, tidepool identity, access windows, observations, temporary isolation/reconnection, visitor pressure, disturbance records and handoffs into Travel, Conservation, Cartography and battle snapshots.

It does not own open-ocean conditions, estuarine salinity, shoreline erosion, celestial calculations, weather, combat terrain or Minecraft fluid physics.

## Authority boundary

This layer does not replace:

- Maritime for sea lanes, harbors, vessels and submerged locations;
- Open Ocean for pelagic state and offshore oceanography;
- Estuaries for salinity gradients and tidal wetlands;
- Coastal Geomorphology for physical shoreline revisions, cliffs, dunes, breaches and sediment budgets;
- Coral Reef for persistent reef condition/restoration;
- Seasonality/Astronomy for calendar and celestial state;
- Meteorology for atmospheric conditions;
- Travel/Cartography for route eligibility and map products;
- Conservation/Tourism for access policy, stewardship and visitor management;
- AutoPTU for movement, terrain, hazards, damage and battle resolution.

Minecraft projects the current accessible geometry. Loaded water blocks do not define authoritative tide state.

## Core separation

Keep these distinct:

persistent shore site -> physical shoreline/substrate revision -> tide-state input -> exposed/submerged footprint -> tidepool isolation state -> observation -> ecological interpretation -> visitor/access consequence -> battle snapshot.

Examples:

- low tide can expose a route without creating permanent land;
- a pool can remain after exposure without becoming a separate lake;
- a Binacle cluster on one rock does not define the entire intertidal population;
- a Wimpod colony scattering after disturbance does not prove permanent displacement;
- an empty pool does not prove a population crash;
- a crowded visitor day does not prove ecological damage;
- a slippery-looking rock does not create a PTU movement penalty without a verified mechanic.

## INTERTIDAL_SYSTEM

```yaml
intertidal_system_id: null
coastal_system_id: null
maritime_region_id: null
segment_ids: []
tide_input_ref: null
conservation_refs: []
tourism_refs: []
cartography_refs: []
research_program_ids: []
history_refs: []
canon_status: proposed
```

An intertidal system may span several coastal segments. It is an ecological coordination object, not a jurisdiction.

## INTERTIDAL_SEGMENT

```yaml
intertidal_segment_id: null
intertidal_system_id: null
coastal_segment_ref: null
substrate_class: rocky|mixed|sand_rock|platform|boulder_field|other|unknown
wave_exposure_class: exposed|moderate|sheltered|variable|unknown
zone_profile_ids: []
tidepool_ids: []
access_window_ids: []
observation_ids: []
disturbance_event_ids: []
visitor_pressure_revision_ids: []
habitat_refs: []
```

The segment is coarse. It should not be one Minecraft chunk or one battle grid.

## INTERTIDAL_ZONE_PROFILE

The system may use broad ecological bands when evidence supports them.

```yaml
intertidal_zone_profile_id: null
intertidal_segment_id: null
observed_at: null
zone_class: splash|high|middle|low|mixed|unknown
geometry_ref: null
exposure_character: null
wave_character: null
known_habitat_refs: []
source_refs: []
confidence: null
supersedes_id: null
```

Zone geometry may shift between surveys. Do not hard-code a universal four-strip layout.

## TIDE_STATE_CONSUMPTION

This layer consumes a server-owned tide state from the calendar/astronomy/environment authority.

```yaml
tide_state_ref:
  timestamp: null
  phase_class: rising|high|falling|low|extreme_high|extreme_low|unknown
  level_band: null
  source_ref: null
  confidence: null
```

This layer must not calculate tides from moon graphics rendered by the client.

## INTERTIDAL_EXPOSURE_REVISION

```yaml
intertidal_exposure_revision_id: null
intertidal_segment_id: null
tide_state_ref: null
observed_at: null
exposed_footprint_ref: null
submerged_footprint_ref: null
isolated_pool_ids: []
newly_connected_pool_ids: []
route_candidate_ids: []
source_refs: []
supersedes_id: null
```

Exposure state can change multiple times per world day without creating new location identities.

## TIDEPOOL

```yaml
tidepool_id: null
intertidal_segment_id: null
persistent_geometry_anchor_ref: null
pool_class: high|middle|low|variable|unknown
isolation_history_ids: []
water_observation_ids: []
occupancy_observation_ids: []
research_marker_ids: []
visitor_access_ref: null
stewardship_ref: null
```

A tidepool remains the same persistent object across many fill/drain cycles unless Coastal Geomorphology records a real physical change.

## TIDEPOOL_ISOLATION_EVENT

```yaml
tidepool_isolation_event_id: null
tidepool_id: null
started_at: null
ended_at: null
tide_state_refs: []
observed_water_state: null
connection_state: isolated|partially_connected|connected|unknown
source_refs: []
```

Isolation does not create automatic oxygen, heat, salinity or damage mechanics. Those require dedicated evidence/rules if ever simulated.

## INTERTIDAL_OBSERVATION

```yaml
intertidal_observation_id: null
site_ref: null
observer_id: null
observed_at: null
tide_state_ref: null
zone_profile_ref: null
weather_ref: null
observation_type: occupancy|behavior|substrate_use|feeding|scavenging|nesting|disturbance|water_condition|other
entity_refs: []
collective_refs: []
raw_description: null
media_refs: []
source_refs: []
confidence: null
```

Tide and zone context are mandatory whenever they materially affect what was observable.

## OCCUPANCY HISTORY

Intertidal species presence should use observation history rather than live spawn counts.

A valid sequence may be:

observed at three low tides -> absent during two high-tide surveys -> observed again next month.

That is not contradiction. It is a context-dependent record.

## SPECIES-SPECIFIC BEHAVIOR

Species lore may seed hypotheses or authored regional behavior only where supported.

Examples from research:

- Binacle may use specific rocks and feed during high tide;
- Pyukumuku may occur in warm shallow water and remain exposed for some time;
- Wimpod may form colonies, scavenge and scatter when disturbed.

Do not generalize these into shared rules for all Rock/Water, Water or Bug/Water Pokémon.

## LOW-TIDE ACCESS WINDOW

```yaml
intertidal_access_window:
  access_window_id: null
  intertidal_segment_id: null
  connection_ref: null
  expected_open_ref: null
  observed_open_at: null
  observed_close_at: null
  access_reason: exposed_platform|sandbar|rock_shelf|cave_mouth|pool_edge|other
  route_condition_ref: null
  restriction_refs: []
  source_refs: []
```

Travel remains authoritative for whether a character may use the connection.

A player seeing exposed blocks is not enough to authorize traversal.

## VISITOR PRESSURE

```yaml
intertidal_visitor_pressure_revision:
  revision_id: null
  intertidal_segment_id: null
  valid_period_ref: null
  observed_visitor_level: low|moderate|high|event_surge|unknown
  path_concentration_refs: []
  handling_observation_refs: []
  collection_observation_refs: []
  education_activity_refs: []
  stewardship_response_refs: []
  evidence_refs: []
```

Pressure is not damage. The system should record observed disturbance separately.

## DISTURBANCE EVENT

```yaml
intertidal_disturbance_event:
  disturbance_event_id: null
  intertidal_segment_id: null
  occurred_at: null
  disturbance_type: trampling|collection|construction|pollution|storm_effect|research_handling|unknown
  footprint_ref: null
  observed_effect_refs: []
  suspected_cause_refs: []
  response_refs: []
  confidence: null
```

A suspected cause is never promoted to truth by event creation alone.

## STEWARDSHIP AND RESEARCH

Intertidal sites are strong candidates for:

- repeated transects;
- low-tide research days;
- temporary closures;
- school/academy field practice;
- photography records;
- specimen-free observation;
- cleanup events;
- visitor education;
- recovery monitoring after storms or pollution.

Specimen collection, ownership and removal remain under explicit institutional/custody rules.

## PLAYER KNOWLEDGE

Players may know different tide windows, pool names, paths, access rules or species observations.

A shared map can reveal a location without revealing every private observation.

## MINECRAFT PROJECTION

The server should project the current intertidal revision into Minecraft through coarse authored geometry or controlled block/state changes.

Required protections:

- client-rendered moon phase cannot be tide authority;
- loaded water level cannot become tide truth;
- chunk reload cannot reset a low-tide route to an obsolete state;
- moving/removing one block cannot rewrite a whole intertidal segment;
- player-built water manipulation cannot create ecological truth directly;
- tide-driven spawn opportunities must be server-gated to prevent rare-spawn exploits.

## BATTLE SNAPSHOT POLICY

At battle start, freeze only mechanics that current PTU/AutoPTU evidence supports.

Possible snapshot inputs when implemented and validated:

- static exposed/submerged geometry;
- supported movement modes;
- supported blockers;
- verified field effects;
- verified Weather;
- verified hazards;
- verified objectives.

Never infer:

- wet rock = Slow/Rough Terrain;
- incoming tide = forced movement;
- wave = knockback;
- isolated pool = Water Terrain;
- barnacle-covered rock = damaging hazard;
- sea spray = Accuracy penalty;
- shallow water = automatic Swim check;
- high tide = stat bonus;
- low tide = capture bonus.

## Encounter contract — Low-Tide Shelf Survey

Narrative premise: researchers need one final transect across a shelf exposed only during a short low-tide window. Wild Pokémon are using several pools along the route.

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED baseline;
- complete movement including forced movement/interception: BLOCKING if tide advance or retreat paths move actors;
- core calculations: VERIFIED baseline;
- action economy/initiative: VERIFIED baseline;
- full turn/round lifecycle: PARTIAL if the tide advances on round boundaries;
- full stateful damage pipeline: PARTIAL only for normal verified attacks;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for changing water/exposure or wave zones;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW/REACH_EXIT/PROTECT_POOL objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:

The server chooses a safe low-tide geometry before combat. The tide does not advance during the battle. Researchers and uninvolved wildlife remain outside the grid. AutoPTU runs a static legal encounter. After resolution, world time may advance and the route can close through overworld state.

## Encounter contract — Pool Reconnection

Narrative premise: a disturbance separated several shallow pools longer than expected. The goal is to inspect the site and reopen a blocked water connection without assuming the Pokémon inside need capture.

Full version blockers:

- interactable objective support;
- dynamic water/zone state;
- complete movement if flows displace actors;
- tactical AI for withdrawal/protection;
- adapter/playback.

Reduced version:

The blockage is assessed and modified outside battle. If a territorial encounter occurs, it runs on a fixed adjacent rock platform. Reconnection is applied only after the battle/world-action result is validated.

## Encounter contract — Visitor Surge at Moonpool Point

Narrative premise: an unusually favorable low tide attracts visitors to a sensitive site while a Wimpod colony and several recurring tidepool occupants are active.

Full version blockers:

- civilian/crowd routing;
- complete movement for protected corridors;
- tactical AI for wildlife withdrawal;
- environment/zone mechanics only if separately validated;
- Minecraft playback.

Reduced version:

Visitor movement and stewardship decisions are resolved in overworld state. Any battle occurs after staff clear a static perimeter. Colony movement is ecological state, not combat AI.

## Long-term narrative uses

This layer can support multi-year changes without requiring a villain:

- a pool monitored over dozens of tides;
- a low-tide route that becomes famous, crowded, restricted, restored or physically lost;
- repeated visitor campaigns;
- a species observation that shifts to another zone after shoreline change;
- a research marker becoming a local landmark;
- restoration after a pollution event;
- a former partner or persistent wild Pokémon reappearing at the same pool across seasons.

## Promotion gate

No intertidal object becomes canon merely because this schema exists.

Promotion requires authored regional placement plus review of:

- species/habitat fit;
- tide source and calendar integration;
- conservation/access policy;
- Minecraft projection feasibility;
- any PTU mechanics actually used;
- AutoPTU-Java capability evidence for tactical effects.