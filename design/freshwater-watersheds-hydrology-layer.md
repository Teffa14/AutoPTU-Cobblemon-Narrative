# Freshwater, Watersheds & Hydrology Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No mechanical PTU effect is established here.

Pass: 62

## Purpose

This layer gives Ouros a persistent model for freshwater movement and freshwater-dependent places.

It connects meteorology, geology, agriculture, settlements, sanitation, conservation, infrastructure, crisis response, travel and ecology without letting any one of those systems become the source of truth for the entire catchment.

## Core separation

Never collapse these into one state:

- physical water body;
- catchment connectivity;
- current water-regime state;
- infrastructure operation;
- observed measurement;
- forecast/model output;
- water-quality observation;
- ecological response;
- public belief;
- tactical PTU terrain/weather/hazard state.

A river can look full while groundwater is falling.

A wetland can be temporarily dry without being destroyed.

A reservoir can be operational while a downstream habitat is stressed.

A flood can be dangerous to one settlement and ecologically important to another reach.

## Persistent objects

### FRESHWATER_SYSTEM

```yaml
freshwater_system_id: null
name: null
system_type: river|stream|lake|wetland|reservoir|spring|aquifer|canal|floodplain|other
region_ids: []
upstream_edges: []
downstream_edges: []
groundwater_edges: []
connected_habitat_ids: []
connected_settlement_ids: []
connected_infrastructure_ids: []
history_refs: []
canon_status: proposed
```

### CATCHMENT_REACH

A reach is a coarse segment used for causal propagation. It is not one Minecraft chunk.

```yaml
reach_id: null
freshwater_system_id: null
upstream_reach_ids: []
downstream_reach_ids: []
adjacent_floodplain_ids: []
wetland_connection_ids: []
normal_access_state: null
observed_flow_class: unknown
observed_level_class: unknown
```

Suggested coarse states:

- DRY
- ISOLATED_POOLS
- VERY_LOW
- LOW
- NORMAL
- HIGH
- OVERBANK
- FLOODED
- UNKNOWN

These labels are narrative/world-state abstractions. They do not create PTU penalties.

### WATER_REGIME_EVENT

```yaml
water_regime_event_id: null
reach_ids: []
event_type: rainfall_response|release|diversion|drawdown|flood_pulse|seasonal_drying|reconnection|other
start_time: null
end_time: null
source_refs: []
observed_or_planned: observed
confidence: null
```

### WATER_CONTROL_ASSET

Examples include dam, weir, gate, pump, levee, irrigation diversion, reservoir outlet and drainage channel.

```yaml
asset_id: null
asset_type: null
location_id: null
operator_actor_ids: []
operational_state: normal|degraded|offline|manual|unknown
controlled_reach_ids: []
upstream_effect_edges: []
downstream_effect_edges: []
last_verified_at: null
```

Operational state does not itself prove the hydrological effect. The effect must be recorded through a water-regime event or validated model/observation.

### HYDROLOGY_OBSERVATION

```yaml
observation_id: null
location_or_reach_id: null
observed_at: null
observer_ids: []
measurement_type: level|flow|temperature|turbidity|conductivity|visual|spring_output|other
value: null
units: null
method_ref: null
quality_flag: null
source_refs: []
```

Do not convert one measurement into a regional conclusion automatically.

### HYDROLOGY_HYPOTHESIS

Examples:

- reduced groundwater recharge;
- upstream diversion;
- blocked culvert;
- seasonal dry phase;
- dam-operation change;
- rainfall deficit;
- geological leakage;
- instrument failure.

Hypotheses need evidence links and can remain unresolved.

### WATER_USE_DEPENDENCY

```yaml
water_use_dependency_id: null
consumer_type: settlement|farm|workshop|clinic|habitat|transport|research|other
consumer_id: null
source_reach_id: null
use_type: supply|irrigation|cooling|navigation|habitat|sanitation|ceremony|other
minimum_state_claim: null
claim_status: proposed|validated|obsolete
```

Do not invent volumetric requirements until authored.

### FLOODPLAIN_CONNECTION

A floodplain edge becomes active only when world state supports it.

Potential consequences may include:

- temporary route closure;
- wetland reconnection;
- fish/Pokémon movement opportunity;
- sediment deposition;
- field flooding;
- changed access to ruins;
- new temporary habitat;
- infrastructure pressure.

Each consequence requires its own state mutation. No generic “flood = damage” shortcut.

## Causal propagation

Use explicit propagation chains.

Example:

```text
upstream rainfall
→ reservoir inflow rises
→ operator changes release
→ middle reach reconnects to floodplain
→ temporary route closes
→ wetland habitat becomes connected
→ observed Pokémon movement changes
→ downstream survey opportunity appears
```

The generator may propose the next edge only when the preceding state supports it.

## Groundwater interaction

Surface water and groundwater remain separate linked objects.

A spring can weaken while a nearby river still appears normal.

A polluted surface reach can affect groundwater only when the world model contains a valid interaction edge.

A groundwater change may appear downstream after delay.

Do not use groundwater as a narrative magic explanation for any unexplained water problem.

## Reservoir and submerged-history model

A reservoir can preserve earlier geography.

```yaml
reservoir_history:
  pre_inundation_location_ids: []
  inundation_event_ref: null
  relocated_actor_or_institution_refs: []
  submerged_structure_ids: []
  heritage_status_refs: []
  ecological_transition_refs: []
```

Submerged structures can be heritage sites, habitat, hazards or investigation locations. They are not automatically loot dungeons.

## Wetland state

Wetlands should track wetting/drying regime and connectivity, not a binary healthy/unhealthy flag.

Potential state dimensions:

- connection to main channel;
- inundation phase;
- duration of current wet/dry period;
- vegetation condition observation;
- water-quality observations;
- breeding/movement observations;
- visitor/access state.

Ecological conclusions remain evidence-based.

## Irrigation and agriculture

Agriculture may depend on freshwater state, but this layer does not calculate crop yield.

Possible consequences:

- irrigation allocation changes;
- delayed planting;
- alternative crop planning;
- temporary pumping restriction;
- conflict between farms and habitat needs;
- maintenance of channels;
- reuse or return-flow projects.

The agriculture layer owns crop outcomes.

## Settlement and public works interaction

A proposed dam, levee, channel or diversion should pass through existing governance/public-works state.

Hydrology supplies:

- affected reaches;
- known dependencies;
- observed baselines;
- uncertainty;
- possible upstream/downstream consequences.

Governance supplies mandate and decision procedure.

Architecture/infrastructure supplies physical implementation.

No generated project gains legitimacy simply because a hydrology model prefers it.

## Travel interaction

A crossing may have several states:

- bridge open;
- bridge closed;
- ford usable;
- ford unsafe/unknown;
- ferry operating;
- seasonal crossing exposed;
- floodplain route inundated.

Travel consumes those states. This layer does not invent movement checks.

## Conservation interaction

A managed flow can create an ecological opportunity, but no species response is guaranteed unless supported by authored behavior or later observation.

Example:

planned spring release → wetland reconnects → survey sees increased activity.

Do not pre-write “release causes breeding success” unless the regional ecology supports it.

## Sanitation and pollution interaction

Water quantity, flow direction and water quality remain separate dimensions.

Higher flow may dilute a measured concentration without removing the source.

A wetland may filter some material but cannot be treated as an infinite cleanup device.

The waste/pollution layer owns contaminant provenance and treatment.

## Meteorology interaction

Forecast rainfall is not current flow.

Observed rain is not downstream flood state.

Weather can create inputs to a hydrology model. Hydrology then determines resulting freshwater state.

## Minecraft projection

Minecraft should render a coarse authoritative projection, such as:

- water level variant;
- exposed bank;
- flooded path;
- opened/closed sluice visual;
- wetland inundation variant;
- active ferry/ford signage;
- visible reservoir shoreline change.

Loaded blocks must not become the authoritative hydrology model.

Chunk unloading cannot freeze the catchment clock.

## Battle projection

Before an AutoPTU encounter starts, freeze a tactical projection from current world state.

Example contract:

```yaml
battle_projection:
  source_reach_id: river_mid_03
  world_state_revision: 1842
  map_variant: low_water_gravel_bar
  static_blockers: []
  swim_tiles: []
  hazard_effects: []
  dynamic_flow_effects_enabled: false
```

If current Java support cannot execute moving water, currents or flood-zone reactions, those remain presentation/world state only.

Minecraft must never invent knockback, damage, Slowed, Tripped, Poisoned or accuracy modifiers from water appearance.

## Encounter contracts

### 1. Sluice Gate Survey

Narrative premise: a downstream wetland is not reconnecting when expected. Players inspect gauge history, gate operation, debris and upstream conditions.

Full version dependencies:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement incl. forced movement/interception — BLOCKING if current pushes actors;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for moving water or changing inundation;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING if enemies/wild Pokémon pursue retreat/protect goals;
- Minecraft/Cobblemon/Craftics playback — BLOCKING.

Reduced version: investigate in overworld. Freeze the gate and water level before any battle. If a confrontation occurs, use a static legal map with no current effect. Resolve gate manipulation after combat through world-state actions.

### 2. Floodplain Reconnection

Narrative premise: a planned release reconnects an old side channel. Researchers, residents and Pokémon activity respond differently as the water arrives.

Full version adds dynamic terrain/zones and possibly REACH_EXIT/WITHDRAW objectives, currently BLOCKING.

Reduced version: represent reconnection through timed world-state updates. Any encounter uses a map snapshot from one stable phase. Pokémon movement across the catchment is resolved outside battle.

### 3. Dry-Season Ford

Narrative premise: a normally impassable crossing becomes available during low flow, but a new observation questions whether the route is safe for the planned expedition.

Full version may require current-sensitive movement, rescue objectives and tactical AI.

Reduced version: route eligibility is resolved before battle. A battle, if one occurs, uses the exposed ford as a static map. No water-flow penalty is invented.

## Overworld implementation blockers

`OVERWORLD_CATCHMENT_GRAPH = BLOCKING`

Persistent reaches, upstream/downstream edges, wetland/floodplain links and groundwater links are required.

`OVERWORLD_WATER_REGIME_STATE = BLOCKING`

The server needs coarse flow/level/connectivity state with revision history.

`OVERWORLD_WATER_CONTROL_OPERATIONS = BLOCKING`

Dams, pumps, gates, levees and diversions need authoritative operating state separate from Minecraft block position.

`OVERWORLD_HYDROLOGY_OBSERVATION_MODEL = BLOCKING`

Measurements, gauges, sensor quality and uncertainty need persistence.

`OVERWORLD_GROUNDWATER_SURFACE_LINKS = BLOCKING`

Aquifer/spring/river interactions need authored or researched edges rather than narrative invention.

`OVERWORLD_HYDROLOGY_TO_COBBLEMON_PROJECTION = BLOCKING`

Freshwater state may shape spawn context eventually, but loaded Pokémon cannot become the population truth and rarity manipulation must not become exploitable.

`OVERWORLD_HYDROLOGY_TO_BATTLE_PROJECTION = BLOCKING`

The server needs a validated snapshot contract mapping world state into supported AutoPTU terrain/weather/hazard inputs without duplicating rules.

## PTU / Caelo guardrails

Do not invent:

- current speed;
- forced-movement distance;
- drowning or suffocation;
- swimming DCs;
- flood damage;
- water-pressure damage;
- mud penalties;
- fishing modifiers;
- Water-type bonuses;
- rain effects;
- dam-collapse damage;
- evacuation checks;
- irrigation yield bonuses;
- Pokémon abilities to control regional water;
- environmental status application.

The project-supplied Caelo corpus was not reliably retrievable in this runtime, so all exact PTU/Caelo hydrology and terrain interactions remain pending source validation.

## Promotion gate

Before any freshwater concept becomes canon or executable content:

1. regional catchment geography is authored or approved;
2. relevant infrastructure and operators exist in canon;
3. ecological dependencies have evidence;
4. exact PTU/Caelo mechanics are checked;
5. AutoPTU-Java capability dependencies are verified for the exact mechanics used;
6. Minecraft projection has a server-authoritative revision source;
7. no external plot or setting has been transplanted.
