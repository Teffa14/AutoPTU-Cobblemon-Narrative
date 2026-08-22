# Lake Limnology, Stratification & Inland-Water Ecology Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanical effect is established by this document.

Pass: 91

## Purpose

This layer gives Ouros persistent internal state for lakes and reservoirs.

The existing Freshwater layer remains responsible for catchments, inflows/outflows, groundwater links, water-control assets, floodplain connectivity and broad water-regime state.

This layer begins at the lake boundary and answers different questions:

- what is happening inside the water column;
- how conditions vary by depth and zone;
- whether the lake is mixed or stratified;
- how oxygen, temperature, transparency and biological observations change through time;
- where observations were actually taken;
- how lake-internal changes affect ecology, research, fisheries, tourism and settlement decisions.

## Core separation

Never collapse these into one state:

- lake identity;
- basin morphology;
- lake level;
- water-column mixing state;
- depth-specific temperature observation;
- depth-specific dissolved-oxygen observation;
- transparency/clarity observation;
- nutrient observation;
- bloom observation;
- bloom-cause hypothesis;
- littoral habitat condition;
- Pokémon observation;
- public advisory;
- tactical PTU terrain/weather/hazard state.

A lake can be visually clear while deep water is oxygen-poor.

A lake can have a surface bloom while deeper layers remain physically different.

A low-oxygen reading at one station does not prove the entire lake is hypoxic.

## Persistent objects

### LAKE_SYSTEM

```yaml
lake_id: null
name: null
freshwater_system_id: null
lake_type: natural|reservoir|caldera|glacial|karst|oxbow|other
region_ids: []
shoreline_revision_ref: null
bathymetry_revision_ref: null
inflow_reach_ids: []
outflow_reach_ids: []
groundwater_edge_ids: []
connected_wetland_ids: []
connected_settlement_ids: []
connected_fishery_ids: []
history_refs: []
canon_status: proposed
```

Lake identity remains stable even when level, shoreline, stratification or ecology changes.

### LAKE_BATHYMETRY_REVISION

Bathymetry should be coarse enough for game state.

```yaml
bathymetry_revision_id: null
lake_id: null
valid_from: null
valid_to: null
source_refs: []
max_depth_class: shallow|moderate|deep|unknown
basin_zones: []
known_dropoffs: []
known_shelves: []
uncertainty_notes: []
```

Do not generate a one-block-accurate depth model unless a gameplay system genuinely needs it.

### LAKE_ECOLOGICAL_ZONE

Suggested zone types:

- LITTORAL;
- OPEN_WATER_SURFACE;
- PELAGIC;
- DEEP_WATER;
- BOTTOM;
- INFLOW_DELTA;
- OUTFLOW_ZONE;
- SPRING_INFLUENCE_ZONE;
- ARTIFICIAL_INTAKE_ZONE;
- OTHER.

```yaml
lake_zone_id: null
lake_id: null
zone_type: null
spatial_ref: null
depth_band: null
active_revision_ref: null
```

A zone is ecological/world-state structure. It does not map automatically to PTU Terrain.

### WATER_COLUMN_STATE

```yaml
water_column_state_id: null
lake_id: null
valid_from: null
valid_to: null
mixing_state: mixed|developing_stratification|stratified|partial_mixing|turnover|ice_stratified|unknown
confidence: null
basis_refs: []
```

This object records a reviewed state, not one raw measurement.

### DEPTH_PROFILE_OBSERVATION

```yaml
profile_id: null
lake_id: null
station_id: null
observed_at: null
observer_ids: []
method_ref: null
measurements:
  - depth_band: null
    temperature: null
    dissolved_oxygen: null
    conductivity: null
    turbidity: null
    chlorophyll_proxy: null
quality_flag: null
source_refs: []
```

One profile remains one observation.

### TRANSPARENCY_OBSERVATION

```yaml
transparency_observation_id: null
lake_id: null
station_id: null
observed_at: null
method: secchi|visual|instrument|other
value: null
units: null
quality_flag: null
```

Visibility in the water column does not become battle Accuracy or LoS without an explicit PTU rule and engine implementation.

### BLOOM_OBSERVATION

```yaml
bloom_observation_id: null
lake_id: null
observed_at: null
zone_ids: []
observer_ids: []
visual_description: null
sample_refs: []
classification_status: unclassified|suspected|identified|ruled_out
public_visibility: internal|restricted|public
```

A surface discoloration may be recorded before any organism or cause is identified.

### BLOOM_HYPOTHESIS

```yaml
bloom_hypothesis_id: null
bloom_observation_ids: []
hypothesis_type: nutrient_input|thermal_stratification|long_residence_time|sediment_release|biological_shift|upstream_input|other
supporting_evidence_refs: []
contradicting_evidence_refs: []
status: proposed|supported|weakened|rejected|unresolved
```

Do not infer toxicity from color alone.

### LAKE_OXYGEN_ASSESSMENT

```yaml
assessment_id: null
lake_id: null
valid_at: null
zone_or_depth_refs: []
assessment: normal|low|very_low|anoxic|heterogeneous|unknown
basis_profile_ids: []
reviewer_ids: []
confidence: null
```

Assessment scope must remain explicit.

### LAKE_TURNOVER_EVENT

```yaml
turnover_event_id: null
lake_id: null
start_time: null
end_time: null
trigger_context_refs: []
observed_profile_refs: []
state_before: null
state_after: null
notes: []
```

Turnover is a world event. It does not inherently produce a battle field effect.

## Causal handoffs

### Freshwater → Lake

Potential inputs:

- inflow level/flow changes;
- sediment pulses;
- nutrient observations;
- reservoir drawdown;
- groundwater inflow changes;
- flood reconnection.

The lake layer evaluates internal consequences separately.

### Meteorology → Lake

Potential inputs:

- prolonged heat;
- wind conditions;
- cold periods;
- ice-cover context;
- storm mixing opportunity.

Weather does not directly write `bloom=true` or `oxygen=low`.

### Stormwater / Sanitation / Agriculture / Wildfire → Lake

These systems may provide potential source events or measured inputs.

The lake layer records where and when those inputs reached the lake and what observations followed.

### Lake → Fisheries

Potential outputs:

- changed observed distribution;
- temporary survey need;
- spawning-area concern;
- deep-water access concern;
- evidence supporting a management review.

Do not change catch rates or stock state merely because a limnology observation changed.

### Lake → Health Surveillance

A confirmed or suspected hazard can produce a public-health signal or advisory review.

Never expose private patient records through the lake layer.

### Lake → Tourism / Public Space

Potential outcomes:

- shoreline closure;
- restricted swimming/boating area;
- educational program;
- observation event;
- temporary rerouting;
- public interpretation conflict.

### Lake → Cobblemon

Only through a controlled projection layer.

Potential coarse consequences may eventually include:

- habitat suitability changes;
- depth-zone availability;
- seasonal presence windows;
- shoreline congregation opportunities.

Loaded entity counts never become lake population truth.

## Knowledge model

Different actors may know different slices of the same lake.

Example:

- local fisher knows fish have shifted shallower;
- university team has a deep oxygen profile;
- clinic knows several visitors became ill after contact;
- town office has an old water-quality bulletin;
- public rumor says the lake is poisoned;
- actual cause remains unresolved.

Store these separately.

## Longitudinal research loop

A lake becomes more valuable narratively when observations accumulate.

Suggested loop:

```text
baseline profile
→ seasonal revisit
→ anomaly
→ repeat measurement
→ competing hypotheses
→ source investigation
→ intervention or no action
→ next seasonal profile
→ revised interpretation
```

Null results matter.

A survey that finds no expected change can be a meaningful outcome.

## Lake morphology and history

Lake basins can retain historical state.

Possible records:

- old shoreline;
- former inlet;
- submerged road;
- drowned structure;
- old bathymetric map;
- previous reservoir level;
- restored littoral shelf;
- sediment accumulation area.

Historical maps remain valid for their date rather than being overwritten.

## Pokémon observations

Species observations should remain evidence-based.

Examples of valid records:

- repeated surface congregation at a known station;
- absence from a previously used littoral zone;
- changed depth of observations;
- unusual timing of activity;
- repeated use of an inflow area;
- a known individual returning to the same shoreline.

Invalid automatic conclusions:

- `Water-type present = water quality good`;
- `Poison-type present = contamination`;
- `Magikarp at surface = oxygen crisis`;
- `Gyarados aggressive = pollution`;
- `Quagsire absent = lake damaged`.

## Quest generation rules

Generate a lake quest only when at least one meaningful state difference exists.

Good triggers:

- profile diverges from baseline;
- two stations disagree;
- turnover occurs earlier/later than expected;
- bloom appears in only one basin;
- deep oxygen drops while shoreline looks normal;
- an inflow plume reaches the lake;
- public advisory conflicts with newer evidence;
- old bathymetry causes a survey error;
- fish/Pokémon observations shift zones;
- restoration project reaches a review milestone.

Avoid generating filler from routine sampling that found nothing unusual unless the null result itself changes a hypothesis.

## Encounter implementation contracts

### 1. Deep Station Recovery

Narrative premise:
A profiling buoy or deep-water sampler stops transmitting during a period when the lake's lower layer is poorly understood.

FULL version:
- lake zones represented in encounter state;
- depth/visibility context where rules support it;
- moving watercraft or platform positions;
- objective to recover/secure equipment without defeating all wildlife;
- wild Pokémon can withdraw toward legal exits;
- dynamic environment only when authoritative PTU rules exist.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED for static geometry;
- base movement legality: VERIFIED for basic legal movement;
- complete movement/forced movement/interception: BLOCKING if moving platforms/currents/withdrawal paths matter;
- terrain/weather/hazards/zones/reactions: BLOCKING for depth/visibility/current field effects;
- AI tactical policy: BLOCKING for RECOVER_OBJECT / WITHDRAW / AVOID_ZONE behavior;
- adapter/playback: BLOCKING for lake-state projection.

REDUCED version:
The overworld resolves boat position, sampling and wildlife movement first. If conflict occurs, AutoPTU receives a fixed platform/shoreline arena and only the actual combatants.

### 2. Littoral Bloom Survey

Narrative premise:
A visible surface bloom appears near one shoreline while other stations remain clear.

FULL version:
- shoreline sampling objectives;
- noncombatants/researchers outside or protected within encounter state;
- water/shore zones;
- withdrawal or protect-sampler goals;
- any toxicity only from validated PTU mechanics.

Dependencies:
- environment family: BLOCKING for dynamic water/bloom zones;
- tactical AI: BLOCKING for non-KO objectives;
- movement family: BLOCKING if actors must cross changing water edges;
- status lifecycle: PARTIAL, but no environmental status inference is allowed;
- adapter/playback: BLOCKING.

REDUCED version:
Sampling and bloom state remain outside battle. A standard shoreline encounter may occur independently, with no bloom-derived mechanical effect.

### 3. Turnover Night Survey

Narrative premise:
Researchers expect a seasonal mixing event and need observations from several stations during a narrow window.

FULL version:
- timed multi-station objective;
- moving route or platform state;
- changing battlefield environment only if a future authoritative contract supports it;
- wildlife responds to legal tactical state, not narrative labels.

Dependencies:
- full turn/round lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- complete movement: BLOCKING for moving platforms/current displacement;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version:
The timing and stations are handled as overworld world state. Any battle is a conventional static encounter at one station and does not simulate turnover mechanically.

## Mechanical guardrails

The Python oracle contains a specific `Secret Power` mapping where freshwater/pond/creek/river/lake context can resolve a defined move-specific effect.

This proves only that exact rule path.

Do not infer:

- lake terrain penalties;
- oxygen damage;
- hypoxia statuses;
- bloom Poisoned;
- visibility penalties;
- depth pressure;
- current knockback;
- underwater drowning;
- temperature damage;
- automatic Rain Weather;
- automatic Water Terrain;
- rare-spawn bonuses.

## Canon gates

Before any lake becomes canon, author or review:

- lake identity and geography;
- baseline morphology;
- major inflows/outflows;
- historical human/Pokémon use;
- known settlements/institutions;
- authored species associations;
- whether any historic bloom/oxygen event already occurred;
- whether the lake has cultural or mythic meaning;
- public-access norms;
- source/copyright review.

## Implementation recommendation

Keep lake simulation coarse and event-driven.

Recommended authoritative cadence:

- water-column state updates at meaningful seasonal/weather thresholds;
- profiles only when measurements exist or modeled state explicitly requires a revision;
- Pokémon/ecological responses in coarse windows;
- Minecraft visual changes only from committed state revisions;
- battle snapshots frozen at encounter start.

Do not run a per-tick limnology simulator.
