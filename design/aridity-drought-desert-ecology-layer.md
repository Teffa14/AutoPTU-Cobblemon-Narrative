# Aridity, drought & desert ecology layer

Status: PROPOSED SYSTEM DESIGN. Not canon.

## Purpose

This layer models persistent dryland state without collapsing several different ideas into one `desert` flag.

It connects Meteorology, Freshwater, Soil, Flora, Wild Collectives, Interspecies Ecology, Travel, Conservation, Crisis, Health Surveillance, Light, Astronomy, Agriculture and Minecraft projection.

Its core rule is simple: a dry-looking place, a drought, a dust plume and PTU Sandstorm Weather are separate state.

## State separation

Ouros should preserve this chain:

```text
regional climate / season
        ↓
observed precipitation + evapotranspiration context
        ↓
dryness / drought assessment
        ↓
water-source state + vegetation/soil response
        ↓
route / settlement / ecological consequences
        ↓
actor observations and public interpretation
        ↓
optional battle-environment snapshot
```

No arrow may be skipped merely for dramatic convenience.

## Core objects

### ARID_LANDSCAPE

A persistent regional or subregional dryland unit.

Suggested fields:

```yaml
arid_landscape_id: null
region_id: null
name: null
classification_status: proposed
subunits: []
water_source_ids: []
soil_land_unit_ids: []
vegetation_unit_ids: []
route_ids: []
settlement_ids: []
known_refugia_ids: []
dust_source_zone_ids: []
research_refs: []
canon_status: proposed
```

This object does not grant battle Terrain.

### DRYNESS_REVISION

A versioned description of current dryness relative to an authored or measured baseline.

```yaml
dryness_revision_id: null
landscape_id: null
valid_from: null
valid_to: null
basis: []
precipitation_context: unknown
soil_moisture_context: unknown
surface_water_context: unknown
vegetation_context: unknown
confidence: null
assessment_label: null
supersedes: null
```

The label can remain qualitative until Ouros has a reason for numeric hydrology.

### DROUGHT_ASSESSMENT

An institutional or research conclusion about prolonged abnormal dryness.

```yaml
drought_assessment_id: null
scope_ids: []
issued_by: null
issued_at: null
baseline_window: null
observations_used: []
severity_label: null
confidence: null
expected_review_at: null
supersedes: null
```

A drought assessment is not identical to Weather and is not automatically a Crisis.

### EPHEMERAL_WATER_SITE

A persistent location whose water presence changes over time.

Types may include:
- pool / pothole;
- intermittent reach;
- ephemeral channel;
- seasonal spring or seep;
- temporary wetland pocket;
- artificial temporary watering point if canon permits it.

```yaml
ephemeral_water_site_id: null
location_id: null
site_type: null
capacity_class: null
current_phase: DRY
last_wet_observation_at: null
last_dry_observation_at: null
water_quality_refs: []
habitat_use_refs: []
disturbance_refs: []
access_state: null
```

Suggested `current_phase` values:
- DRY
- DAMP
- FILLING
- WET
- SHRINKING
- UNKNOWN

The phase is coarse world state. It is not a Minecraft block count.

### DROUGHT_REFUGE

A location whose relative importance rises during dry periods.

```yaml
refuge_id: null
location_id: null
resource_type: WATER
reliability_history: []
known_user_groups: []
pressure_state: null
protection_state: null
access_constraints: []
```

`known_user_groups` can contain observed populations, travelers or institutions. It does not create ownership or priority by itself.

### DUST_SOURCE_ZONE

A place capable of producing transported dust under certain conditions.

```yaml
dust_source_zone_id: null
location_id: null
surface_state_refs: []
vegetation_cover_refs: []
soil_refs: []
observed_emission_events: []
source_hypotheses: []
management_refs: []
```

### DUST_EVENT

A transported airborne-material event.

```yaml
dust_event_id: null
observed_at: null
source_status: UNKNOWN
source_zone_ids: []
meteorology_refs: []
footprint_versions: []
visibility_observations: []
health_signal_refs: []
transport_disruption_refs: []
astronomy_observation_refs: []
settled_dust_refs: []
```

A dust event can have an unknown source. Do not fabricate one.

### ARID_PHENOLOGY_WINDOW

A short biological window triggered or correlated with environmental state.

Examples:
- flowering after rain;
- emergence at an ephemeral pool;
- temporary seedling recruitment;
- seasonal/night activity shifts already observed for specific species.

```yaml
arid_phenology_window_id: null
scope_id: null
observed_start: null
observed_end: null
trigger_hypotheses: []
observed_species_ids: []
observation_refs: []
repeat_history: []
```

This object never guarantees a spawn.

## Causal integrations

### Meteorology → Aridity

Meteorology supplies observations and forecasts.

A missed rain event can contribute evidence to a drought assessment, but one dry forecast does not create drought.

### Freshwater → Aridity

Freshwater owns perennial rivers, catchments, groundwater and water-control infrastructure.

This layer owns dryland interpretation and scarcity/refuge state.

A spring declining during drought can be important, but groundwater extraction, infrastructure failure or local geology may remain alternative hypotheses.

### Soil → Dust

Soil owns surface/condition observations.

Dust-source risk can increase when soil is exposed or loose, but Dust is a separate event and requires meteorological transport state.

### Flora → Drought response

Flora owns vegetation identity, flowering, recruitment and succession.

This layer can record dryland pressure or short rain-response windows but cannot decide plant mortality or growth without the Flora state changing.

### Wild ecology → water concentration

A drought refuge may concentrate multiple species or collectives.

That concentration is not automatically:
- a swarm;
- a pack;
- a battle;
- cooperation;
- competition;
- ownership;
- an invitation to capture.

Observed interactions should write into Wild Collective or Interspecies Ecology state.

### Travel → route viability

Arid routes can depend on reliable water, shade, service points, surface stability or dust visibility.

Travel decides route viability from actual world state. This layer must not create arbitrary dehydration timers.

### Crisis → escalation

Drought may become a crisis when explicit consequences cross thresholds defined by authored institutions or world state: water-service failure, agricultural loss, wildfire exposure, health pressure, route disruption or habitat stress.

Drought itself is not automatically a Crisis object.

## Minecraft projection

Minecraft/Cobblemon can present:
- dry/wet variants of coarse water sites;
- vegetation-state variants;
- exposed channel beds;
- dunes/sandy surfaces;
- dust particles or visibility presentation;
- shade structures;
- water-point activity;
- settlement service changes;
- route signage;
- temporary access closures;
- research markers or sensors.

Minecraft must not derive canonical drought state from loaded blocks alone.

A player placing/removing water blocks, vegetation or sand cannot directly change regional drought, ecological baselines or rare-spawn projections.

## Battle projection contract

A battle launched in an arid location receives an immutable, validated battle-environment snapshot.

Potential fields:

```yaml
battle_environment_projection:
  source_location_id: null
  source_revision_ids: []
  weather: null
  terrain: null
  static_blockers: []
  validated_hazards: []
  visibility_context: null
  notes: []
```

Only values supported by authoritative PTU/Caelo rules and AutoPTU-Java may enter the battle core.

The following are not automatic projections:
- drought → Sunny Day;
- desert → Sandstorm;
- dust → Accuracy penalty;
- loose sand → Rough Terrain;
- heat → damage;
- water scarcity → fatigue;
- Trapinch nest → Arena Trap;
- buried Sandile → surprise state;
- Cacnea → Sand Veil active.

## Encounter implementation contracts

### 1. Ephemeral Basin Survey

Narrative premise:
A basin that normally fills after seasonal rain remains dry while neighboring basins briefly hold water. Researchers and local route users disagree whether this is meaningful or normal variation.

Full version:
- waterline or wet/dry zones can change during the scenario;
- wild actors can enter/leave toward remaining water;
- route choices matter;
- objective may be OBSERVE / SAMPLE / WITHDRAW rather than defeat;
- dust or wind can alter visibility only if validated.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
The server resolves the basin phase before combat. Sampling, water observations and wildlife movement remain overworld state. If a confrontation occurs, AutoPTU receives one static dry or wet arena and only current combatants. No drought or dust effects are added.

### 2. Dust Road Closure

Narrative premise:
A dust plume repeatedly crosses a transport corridor. The visible plume occurs far from the suspected source zone, creating competing explanations about roadworks, exposed soil and regional weather.

Full version:
- time-varying visibility context;
- protected route/exit objectives;
- possible moving civilian/transport actors;
- environmental effects only when mechanically validated.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED, but LoS is not visibility
- base movement legality: VERIFIED
- complete movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full lifecycle: PARTIAL
- full stateful damage: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:
Dust closes the road or changes travel timing in world state. Any battle occurs at a sheltered/static location whose visibility is normal unless the engine has an explicitly validated effect. Transport and civilians remain outside the grid.

### 3. Refuge Waterhole Conflict

Narrative premise:
A reliable water point becomes unusually crowded late in a prolonged dry period. Travelers, a research team and several wild populations all need access for different reasons.

Full version:
- multiple actors with non-KO goals;
- withdrawal/protection/access lanes;
- changing occupancy around the water point;
- objective-aware AI;
- potentially terrain or water-edge interactions.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:
Access, sequencing and observation are resolved socially/exploratorily outside AutoPTU. If a battle occurs, the water point is not itself an objective tile; noncombatants and unrelated wild Pokémon stay outside the grid. After the battle, world state records who remained, withdrew or gained temporary access based only on actual outcomes and authored decisions.

## Permanent capability snapshot used by this layer

Based on live AutoPTU-Java evidence for pass 73:

VERIFIED
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

BLOCKING
- complete movement including push/pull/knockback/interception/forced movement;
- terrain / weather / hazards / zones / broad reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

## Aridity-specific implementation blockers

Outside the battle core, this layer requires:
- persistent arid-landscape identity;
- drought/dryness revision history;
- ephemeral-water-site state;
- drought-refuge state;
- dust source/event graph;
- dust-footprint projection;
- arid phenology windows;
- safe Aridity → Freshwater integration;
- safe Aridity → Soil/Flora integration;
- safe Aridity → Cobblemon projection;
- immutable Aridity → Battle environment projection.

## Rules guardrails

The Python AutoPTU oracle currently contains real Sandstorm damage and explicit immunity/Ability handling. That implementation is evidence for that exact battle state, not an overworld desert simulator.

Python also contains a Wilderness Guide desert branch that grants defined temporary effects under the actual Feature. Narrative characters without that Feature do not inherit those effects.

Until exact PTU/Caelo source text is extracted and Java parity exists, this layer must not invent:
- dehydration or heat damage;
- travel water consumption;
- Sandstorm creation from biome state;
- dust Accuracy/Evasion changes;
- sand movement penalties;
- desert immunities;
- quicksand mechanics;
- sun damage;
- fatigue;
- environmental Burned;
- Naturewalk eligibility;
- Burrow behavior;
- rare Pokémon guarantees after rain.

## Canon questions

- Which Ouros regions are arid, semi-arid or seasonally dry?
- Which drylands are old climate regimes versus newer landscape changes?
- Which springs, seeps and ephemeral channels are authored landmarks?
- Which settlements depend on isolated water points?
- Which dust source zones exist before player intervention?
- Which species have authored regional dryland behaviors beyond their species-level Pokédex context?
- How long can drought advance while players are offline?
- Which institutions issue drought assessments, if any?
- What rules govern access to scarce water without creating a universal legal system?
- How will Cobblemon reflect temporary concentration near water without creating a rare-spawn exploit?
