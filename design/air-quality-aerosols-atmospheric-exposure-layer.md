# Air Quality, Aerosols & Atmospheric Exposure Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. This document defines narrative/world-state boundaries and implementation contracts. It does not add PTU mechanics.

Pass: 77

## Purpose

Ouros needs one persistent atmospheric layer capable of connecting smoke, dust, volcanic emissions, industrial activity, pollen/spores, visibility, monitoring, exposure and deposition without making Weather, Poisoned, visibility penalties or health effects up from narrative description.

The core principle is causal separation.

`SOURCE -> AIR MASS / PLUME -> OBSERVATION -> INTERPRETATION -> EXPOSURE / DEPOSITION -> CONSEQUENCE`

Each arrow requires evidence or an authored rule. No stage can silently substitute for another.

## Authority boundaries

The world-state server owns:

- atmospheric event identity;
- source claims and evidence;
- coarse plume/airshed state;
- monitoring-station state;
- measurements and provenance;
- public advisory state;
- possible exposure events;
- deposition records;
- long-term trends;
- links to ecology, health surveillance and infrastructure.

PTU/AutoPTU owns any mechanical battle consequence such as:

- Poisoned;
- Badly Poisoned;
- damage;
- Accuracy changes;
- visibility penalties;
- Weather;
- terrain/hazard behavior;
- immunity/resistance;
- Move/Ability/Feature effects.

Minecraft/Cobblemon owns presentation and world interaction only after the server provides authoritative state:

- haze/fog-like rendering;
- particles;
- sky tint;
- monitor blocks/UI;
- warning signage;
- NPC routines;
- changed service availability;
- visual deposition on surfaces when desired.

Minecraft particles do not create atmospheric truth or PTU effects.

## Core objects

### ATMOSPHERIC_REGION

A coarse spatial unit for air-quality state. It may overlap settlements, catchments or biomes and does not need to match administrative boundaries.

Suggested fields:

```yaml
atmospheric_region_id: null
name: null
geometry_ref: null
neighbor_region_ids: []
vertical_profile_mode: coarse
monitor_ids: []
meteorology_region_refs: []
sensitive_receptor_refs: []
current_episode_ids: []
revision: 0
```

### AIR_QUALITY_EPISODE

A bounded atmospheric event or period worth tracking.

```yaml
air_quality_episode_id: null
start_time: null
end_time: null
status: OBSERVED
constituent_claims: []
source_hypothesis_ids: []
plume_revision_ids: []
observation_ids: []
advisory_ids: []
exposure_event_ids: []
deposition_event_ids: []
confidence: null
source_refs: []
```

Suggested statuses:

- SUSPECTED
- OBSERVED
- UNDER_INVESTIGATION
- ATTRIBUTED_PARTIAL
- ATTRIBUTED
- DISSIPATED
- HISTORICAL

`DISSIPATED` ends the active atmospheric episode. It does not erase deposition or later ecological consequences.

### ATMOSPHERIC_SOURCE_EVENT

A source that may inject material into the atmosphere.

Possible source families:

- WILDFIRE_SMOKE
- DUST
- VOLCANIC_ASH
- VOLCANIC_GAS
- INDUSTRIAL_EMISSION
- WASTE_INCIDENT
- CONSTRUCTION_DUST
- BIOLOGICAL_AEROSOL
- POKEMON_SOURCE
- UNKNOWN

Fields should include source time, source geometry, evidence and uncertainty. A source event does not automatically prove downwind exposure.

### PLUME_REVISION

A coarse versioned estimate of where airborne material is believed to be.

```yaml
plume_revision_id: null
air_quality_episode_id: null
valid_time_start: null
valid_time_end: null
horizontal_footprint_ref: null
vertical_band: null
relative_intensity_regions: []
meteorology_basis_ref: null
observation_basis_ids: []
model_method_ref: null
confidence: null
```

Do not simulate fluid dynamics. The purpose is causal continuity and route/ecology integration.

### AIR_MONITOR

A persistent device/site/institutional observation point.

```yaml
air_monitor_id: null
location_ref: null
operator_ref: null
monitor_type: FIXED
measures: []
commissioned_at: null
status: OPERATIONAL
calibration_history_ids: []
maintenance_history_ids: []
coverage_notes: []
```

Possible monitor states:

- OPERATIONAL
- DEGRADED
- OFFLINE
- CALIBRATING
- RELOCATED
- RETIRED

A monitor reading is evidence about its location/context. It is not automatically representative of an entire region.

### AIR_OBSERVATION

Stores measured or observed atmospheric information with provenance.

```yaml
air_observation_id: null
observed_at: null
location_ref: null
observer_ref: null
instrument_ref: null
observation_type: PARTICULATE_MEASUREMENT
value: null
units_ref: null
qualitative_value: null
quality_flags: []
source_record_ref: null
```

Observation families can include:

- PARTICULATE_MEASUREMENT
- VISIBILITY
- ODOR_REPORT
- DEPOSITION_SAMPLE
- COLOR / HAZE DESCRIPTION
- CHEMICAL_SAMPLE
- BIOLOGICAL_AEROSOL_SAMPLE
- POKEMON_BEHAVIOR_OBSERVATION

Never convert odor or color directly into chemical identity.

### SOURCE_ATTRIBUTION_HYPOTHESIS

```yaml
source_hypothesis_id: null
air_quality_episode_id: null
candidate_source_event_ids: []
claim: null
supporting_evidence_ids: []
contradicting_evidence_ids: []
confidence: null
status: ACTIVE
```

Several hypotheses may remain alive simultaneously.

### AIR_QUALITY_ADVISORY

A versioned institutional/public communication object.

It should contain:

- issuing institution;
- issue/revision time;
- affected geography;
- stated concern;
- recommended world actions;
- evidence basis;
- expiry/review time;
- publication channels.

An advisory is not world truth. It is an institution's current guidance.

### ATMOSPHERIC_EXPOSURE_EVENT

This object records that an actor or population plausibly occupied an atmospheric footprint.

```yaml
exposure_event_id: null
air_quality_episode_id: null
actor_or_population_ref: null
location_ref: null
start_time: null
end_time: null
exposure_basis: null
confidence: null
health_case_refs: []
```

It does not diagnose illness or apply a Status.

### DEPOSITION_EVENT

Represents material leaving the atmosphere and becoming relevant to another layer.

```yaml
deposition_event_id: null
air_quality_episode_id: null
recipient_ref: null
recipient_layer: SOIL
mode: DRY
observation_ids: []
constituent_claims: []
confidence: null
followup_refs: []
```

Recipient layers may include:

- SOIL
- FRESHWATER
- FLORA
- CRYOSPHERE
- ARCHITECTURE / COLLECTION OBJECTS
- MARINE / WETLAND systems

Deposition state should never directly alter PTU Stats.

## Air-quality profile instead of a universal scalar

Avoid:

`air_quality = 47`

Prefer a set of independent, evidence-backed dimensions:

```yaml
atmospheric_profile:
  visibility_condition: HAZY
  particulate_condition: ELEVATED
  odor_condition: REPORTED
  reactive_pollutant_condition: UNKNOWN
  toxic_constituent_claim: UNCONFIRMED
  biological_aerosol_condition: UNKNOWN
  deposition_active: POSSIBLE
  monitoring_coverage: PARTIAL
```

The exact vocabulary can remain qualitative until a reason exists for numerical simulation.

## Temporal model

Air-quality systems need several clocks.

### Acute episode clock

Minutes/hours/days:

- smoke plume;
- dust event;
- industrial release;
- volcanic plume;
- unusual pollen/spore pulse.

### Repeated-exposure clock

Days/weeks:

- recurring inversion-like buildup;
- seasonal smoke;
- repeated traffic/industry episodes;
- recurring biological aerosols.

### Deposition/ecosystem clock

Months/years:

- soil/water nutrient or contaminant accumulation;
- vegetation response;
- altered sensitive habitats;
- monument/material staining;
- recovery after source controls.

Do not resolve all three when an acute plume ends.

## Meteorology relationship

Meteorology provides the atmospheric transport context. Air Quality provides constituents/observations.

Suggested contract:

```text
METEOROLOGY_STATE
  -> wind / stability / precipitation context
  -> AIR_QUALITY transport update
  -> PLUME_REVISION
```

Air Quality does not generate Weather itself.

Precipitation may create a deposition opportunity, but exact chemistry/effect requires authored state and evidence.

## Wildfire relationship

Wildfire emits a potential smoke source.

```text
FIRE_EVENT
  -> ATMOSPHERIC_SOURCE_EVENT
  -> AIR_QUALITY_EPISODE
```

The fire layer retains burn perimeter and fire ecology. Air Quality owns plume/monitor/deposition state.

A smoke episode can continue after flames are controlled.

## Aridity relationship

Aridity can expose a dust source zone. Meteorology determines whether conditions actually produce an airborne episode.

`dry soil` alone does not equal `DUST_EVENT`.

## Volcanism relationship

Volcanism creates ash/gas source events when justified by the volcanic state. Air Quality tracks transported material and monitoring outside the source system.

Ash on the ground later becomes a Soil/Infrastructure/Flora/Cryosphere concern through deposition records.

## Waste/Technology relationship

Industrial or treatment infrastructure can be candidate atmospheric sources.

A monitor spike near an industrial site is not proof that the site caused it. Use source-attribution evidence.

A fault record may create a candidate source event. It does not establish liability.

## Health Surveillance relationship

Health Surveillance can receive exposure context:

```text
AIR_QUALITY_EPISODE
  -> possible EXPOSURE_EVENT
  -> HEALTH_SIGNAL / case investigation if observed
```

Never:

`bad air -> disease`

or

`bad air -> Poisoned`

Medical state remains under the care/health layers and rules authority.

## Flora / ecological relationship

Long-term observation may connect atmospheric conditions with vegetation response. Store correlation and hypothesis separately.

Examples:

- leaf injury observations;
- changed flowering success;
- altered community composition;
- deposition samples;
- reduced growth over several seasons.

Do not infer a cause from one damaged plant.

## Pokémon interaction policy

Pokémon can interact with atmospheric systems only through one of four routes:

1. authored species ecology/lore;
2. observed behavior in the world;
3. validated PTU Move/Ability/Capability/Feature;
4. explicitly authored institutional role.

Examples:

Galarian Weezing may be authored as a species with a pollution-related ecology. That does not define a numeric purification system.

Koffing may be an observed candidate source. That does not establish guilt for an episode.

A Pokémon using the Move `Poison Gas` has a tactical effect defined by rules. That Move does not rewrite regional atmosphere state unless an explicit world-action contract is authored later.

## Monitoring-network design

A good regional network should have imperfections.

Useful causes of uncertainty:

- station offline;
- station relocated;
- valley not covered;
- different instruments;
- calibration drift;
- wind shifts between stations;
- mobile sampler arrives late;
- historical data uses a different method;
- source moves;
- plume is vertically separated from a ground monitor.

This creates investigation without requiring false data or conspiracy.

## Public information

Media/Communications receives advisory/publication objects.

Possible public messages:

- source unknown;
- smoke likely transported from another region;
- elevated particles observed;
- monitoring incomplete;
- advisory revised;
- episode ended;
- deposition study continuing.

Rumors may simplify these messages. The source document remains versioned.

## Multiplayer privacy

Air-quality observations are usually public/aggregate, but health exposure and personal location can be sensitive.

Rules:

- public dashboard may show region-level observations;
- actor-specific exposure remains private by default;
- clinics do not publish patient identities;
- player location history is not inferred from public plume maps;
- research contributors choose whether their exact private-base coordinates are published.

## Minecraft projection

Suggested presentation features after server-side state exists:

- haze intensity bands;
- sky tint;
- optional particles;
- monitor blocks;
- warning boards;
- NPC masks/indoor routines if authored cosmetically;
- closed viewpoints/services;
- surface deposition variants;
- reduced distant landmark visibility.

Accessibility requirements:

A player should not need to identify air quality only by color/haze. Provide equivalent text/icon/caption or instrument feedback.

## Battle snapshot contract

Before a battle starts, world state may produce a proposed atmospheric context.

```yaml
battle_atmosphere_request:
  source_episode_id: null
  local_snapshot_time: null
  observed_world_condition: HAZY
  proposed_ptu_environment_effect: null
  validation_status: UNVALIDATED
```

If no explicit PTU/Caelo rule and Java implementation validates a battle effect, `proposed_ptu_environment_effect` remains null.

The battle then uses ordinary legal mechanics.

### No-inference examples

A smoky Minecraft arena does not apply Poisoned.

Low visibility in world state does not change LoS or Accuracy.

A volcanic gas warning does not apply tick damage.

A Galarian Weezing on the map does not remove an atmospheric episode.

Rain does not automatically cleanse pollution.

A Poison-type is not automatically immune to environmental pollution.

## Encounter contract 1 — Monitor Ridge Retrieval

Premise:

A high-elevation monitor stops transmitting during a regional haze episode. The missing data creates uncertainty about whether the plume entered a sensitive valley.

### FULL version

World layer:

- active air-quality episode;
- evolving plume revision;
- monitor offline state;
- uncertain visibility;
- route/access changes.

Battle requirements if conflict occurs:

- targeting/footprints/range/LoS — VERIFIED geometrically;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING if evacuation/escort/moving front matters;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage — PARTIAL;
- status lifecycle — PARTIAL if status-bearing actors use it;
- terrain/weather/hazards/zones/reactions — BLOCKING for atmospheric hazard/visibility mechanics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

### REDUCED version

Resolve plume, visibility and monitor retrieval in overworld state. If a battle occurs, start after the party reaches a validated static site. No smoke damage, visibility penalty, moving plume or escort objective is inside the grid.

## Encounter contract 2 — Filter House Alarm

Premise:

A treatment/industrial facility reports an air-handling anomaly at the same time nearby monitors show an unusual reading. The investigation must determine whether the facility caused the episode, received pollution from elsewhere, or experienced an unrelated fault.

### FULL version

Could eventually include:

- interactable shutdown/ventilation controls;
- safe/unsafe zones validated by PTU rules;
- changing atmospheric zones;
- protected technicians;
- tactical AI that understands evacuation or control objectives.

Dependencies:

- targeting — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING for dynamic access/interception;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage/statuses — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities/items/features — PARTIAL;
- legal-action AI — VERIFIED;
- tactical AI — BLOCKING;
- adapter/playback — BLOCKING.

### REDUCED version

The facility fault and air-quality investigation remain outside battle. Technicians evacuate before combat. AutoPTU receives a static clean/validated room or yard with no gas mechanics.

## Encounter contract 3 — Haze Over the Marsh

Premise:

A protected wetland becomes hazy for several mornings. Residents blame a nearby works site, but monitoring and wind history leave several plausible sources.

### FULL version

Potential later systems:

- visibility-aware exploration;
- deposition-sensitive ecology;
- mobile sampling;
- wildlife withdrawal rather than forced combat;
- atmospheric battle snapshot if a governing rule exists.

Dependencies:

- targeting/range/LoS — VERIFIED only for geometry;
- base movement — VERIFIED;
- complete movement — BLOCKING if wildlife pathing/interception is tactical;
- core calculations — VERIFIED;
- initiative — VERIFIED;
- lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal actions — VERIFIED;
- tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

### REDUCED version

Sampling, source attribution and wildlife observations are world-state investigation. Any combat is discrete and static, with no invented haze modifier.

## Long-term content engines

Air Quality can generate future material through:

- new monitoring coverage;
- monitor failures;
- revised historical source attribution;
- deposition discovered months later;
- source-control projects;
- changed travel/tourism behavior;
- ecological baselines;
- public-information corrections;
- infrastructure relocation;
- longitudinal research programs.

The system should not generate a crisis every time a monitor changes slightly.

## Implementation blockers outside AutoPTU-Java

`ATMOSPHERIC_REGION_STATE` — BLOCKING.

`AIR_QUALITY_EPISODE_GRAPH` — BLOCKING.

`ATMOSPHERIC_SOURCE_EVENT_STATE` — BLOCKING.

`PLUME_REVISION_STATE` — BLOCKING.

`AIR_MONITOR_NETWORK` — BLOCKING.

`AIR_OBSERVATION_PROVENANCE` — BLOCKING.

`SOURCE_ATTRIBUTION_GRAPH` — BLOCKING.

`AIR_ADVISORY_STATE` — BLOCKING.

`ATMOSPHERIC_EXPOSURE_STATE` — BLOCKING.

`ATMOSPHERIC_DEPOSITION_STATE` — BLOCKING.

`AIR_QUALITY_TO_METEOROLOGY_CONTRACT` — BLOCKING.

`AIR_QUALITY_TO_HEALTH_SURVEILLANCE_CONTRACT` — BLOCKING.

`AIR_QUALITY_TO_ECOLOGY_CONTRACT` — BLOCKING.

`AIR_QUALITY_TO_COBBLEMON_PROJECTION` — BLOCKING.

`AIR_QUALITY_TO_BATTLE_SNAPSHOT` — BLOCKING.

## Canon questions

Before promotion, authors need to decide:

- which regions have meaningful chronic air-quality issues;
- what major historical industrial/volcanic/fire events predate players;
- which institutions monitor the atmosphere;
- what technology level their monitors use;
- whether Galarian Weezing or other species have authored regional roles;
- whether any settlements rely on Pokémon for air handling;
- what pollutants/constituents are useful to name versus keep qualitative;
- what public advisory vocabulary belongs to Ouros;
- which sensitive ecosystems respond to atmospheric deposition;
- how much atmospheric state advances while chunks are unloaded.

## Mechanical questions

Extract and lock authoritative PTU/Caelo rules before implementing any tactical atmospheric effect for:

- Poison Gas;
- Poisoned/Badly Poisoned;
- Overcoat and similar indirect-effect protection where relevant;
- weather-based visibility if any;
- smoke/gas environmental effects if any;
- respiratory/suffocation rules if any;
- Blinded/Accuracy interactions if any;
- Poison-type/Steel-type environmental immunities only where explicitly defined;
- relevant Trainer Features/Capabilities.

Until then, atmospheric world state remains narrative/simulation state and battle arenas receive no invented mechanical penalties.
