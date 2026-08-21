# Geomagnetism, Magnetic Navigation & Interference Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 81

## Purpose

This layer gives magnetic-field state a persistent identity without turning magnetism into a generic Electric-type effect.

It owns regional/local magnetic observations, field revisions, magnetic-navigation context, instrument interference, anomaly investigations and the world-state consequences of geomagnetic events.

## Authority boundary

This layer does not replace:

- Astronomy for celestial events and visible aurora context;
- Meteorology for weather;
- Technology for electrical grids, machines and device state;
- Communications for message delivery and radio services;
- Cartography for maps and route products;
- Travel/Aerial/Maritime for route eligibility;
- Geology for magnetic minerals and bedrock;
- Science for hypotheses, datasets and publication;
- Pokémon Agency for individual Pokémon identity and behavior;
- AutoPTU for Magnet Pull, Magnet Rise, Magnetic Flux, damage, movement or any exact combat effect.

Minecraft/Cobblemon may present compasses, aurora, instruments and magnetic Pokémon. Loaded entities and client visuals do not define authoritative field state.

## Core separation

Do not collapse:

physical magnetic field -> observation -> local anomaly -> interpretation -> navigation correction -> technology consequence -> Pokémon observation -> public belief -> tactical battle state.

Examples:

- a compass can be wrong without a supernatural anomaly;
- an old map can be correct for the date it was published;
- a Probopass near a failed instrument does not prove causation;
- an aurora does not create PTU Weather;
- a Magnemite does not become a portable generator by narrative implication;
- a magnetic Pokémon does not gain arbitrary metal-object control;
- a magnetic anomaly does not automatically evolve Magneton or Nosepass.

## MAGNETIC_REGION

```yaml
magnetic_region_id: null
region_ids: []
field_revision_ids: []
observatory_ids: []
local_anomaly_ids: []
magnetic_navigation_profile_ids: []
known_sensitive_infrastructure_ids: []
source_refs: []
canon_status: proposed
```

A magnetic region is coarse world state. It may cross settlement, political or ecological boundaries.

## MAGNETIC_FIELD_REVISION

```yaml
magnetic_field_revision_id: null
magnetic_region_id: null
valid_from: null
valid_to: null
measurement_basis_refs: []
declination_class: null
inclination_class: null
intensity_class: null
spatial_model_ref: null
confidence: null
supersedes_id: null
source_refs: []
```

Ouros does not need a full physics simulator. Store the minimum field model required by navigation, science and incident logic.

Historical revisions remain valid historical records.

## MAGNETIC_OBSERVATORY

```yaml
magnetic_observatory_id: null
location_id: null
institution_id: null
instrument_ids: []
reference_station_ids: []
interference_buffer_ref: null
operational_state: online|degraded|offline|calibrating|unknown
maintenance_refs: []
data_series_refs: []
```

An observatory can fail, drift or be locally contaminated without the regional field changing.

## MAGNETIC_OBSERVATION

```yaml
magnetic_observation_id: null
observed_at: null
location_ref: null
observer_or_instrument_ids: []
measurement_type: direction|intensity|inclination|declination|anomaly|qualitative|other
value_ref: null
instrument_state_ref: null
nearby_interference_refs: []
source_refs: []
quality_flag: null
```

Observation and interpretation remain separate.

## MAGNETIC_ANOMALY

```yaml
magnetic_anomaly_id: null
location_or_area_ref: null
first_observed_at: null
last_observed_at: null
observation_ids: []
state: active|intermittent|resolved|historical|unconfirmed
spatial_extent_ref: null
cause_hypothesis_ids: []
affected_system_refs: []
pokemon_observation_refs: []
```

`anomaly` means deviation from expected local behavior, not magic.

## MAGNETIC_CAUSE_HYPOTHESIS

```yaml
magnetic_cause_hypothesis_id: null
anomaly_or_incident_ref: null
proposed_driver_type: geology|infrastructure|pokemon|instrument_error|geomagnetic_event|unknown|other
proposed_driver_ref: null
supporting_evidence_ids: []
contradicting_evidence_ids: []
confidence: null
status: proposed|supported|weakened|rejected|unresolved
```

A Pokémon hypothesis must reference an actually observed individual/species and authored behavior. It cannot be generated from Type alone.

## MAGNETIC_NAVIGATION_PROFILE

```yaml
magnetic_navigation_profile_id: null
area_ref: null
valid_period_ref: null
field_revision_id: null
correction_ref: null
reliability_class: ordinary|variable|caution|unreliable|unknown
map_edition_refs: []
source_refs: []
```

This object connects geomagnetism to Cartography/Travel.

It does not decide whether a specific actor can navigate. Skills, instruments, visibility and route state remain separate authorities.

## NAVIGATION_OBSERVATION

```yaml
navigation_observation_id: null
actor_ids: []
observed_at: null
location_ref: null
instrument_ref: null
map_ref: null
expected_bearing_ref: null
observed_bearing_ref: null
field_revision_ref: null
interpretation_ref: null
```

Two competent navigators can disagree because they used different map editions or corrections.

## ELECTROMAGNETIC_INTERFERENCE_INCIDENT

```yaml
em_interference_incident_id: null
location_or_asset_ref: null
started_at: null
ended_at: null
affected_device_ids: []
observed_symptoms: []
field_observation_ids: []
nearby_pokemon_ids: []
nearby_infrastructure_ids: []
cause_hypothesis_ids: []
service_consequence_ids: []
status: open|mitigated|resolved|unresolved
```

A nearby Pokémon is evidence of proximity, not evidence of responsibility.

## GEOMAGNETIC_EVENT

```yaml
geomagnetic_event_id: null
started_at: null
ended_at: null
regional_extent_refs: []
observation_refs: []
aurora_visibility_refs: []
navigation_impact_refs: []
communication_impact_refs: []
power_impact_refs: []
public_information_refs: []
science_refs: []
```

Geomagnetic events are world-state events.

They do not become PTU Weather without a separate verified rule contract.

## AURORA_OBSERVATION

```yaml
aurora_observation_id: null
geomagnetic_event_id: null
location_ref: null
observed_at: null
visibility_context_ref: null
photo_record_ids: []
pokemon_observation_ids: []
public_event_refs: []
```

Aurora can feed Astronomy, Tourism, Photography and Public Memory.

It does not imply Fairy/Psychic behavior or Legendary activity.

## POKEMON_MAGNETIC_BEHAVIOR_OBSERVATION

```yaml
pokemon_magnetic_behavior_observation_id: null
pokemon_entity_id: null
species_id: null
observed_at: null
location_ref: null
behavior_class: orientation|hovering|signal|metal_attraction|device_interference|gathering|other
observation_ref: null
field_revision_ref: null
mechanical_effect_ref: null
source_refs: []
```

`mechanical_effect_ref` stays null unless an authoritative PTU/AutoPTU effect was actually resolved.

## Magnetic-field Pokémon guardrails

### Nosepass / Probopass

Species lore may justify navigation or interference hypotheses.

It does not authorize:

- infinite compass accuracy;
- metal-object forced movement;
- device shutdown radius;
- evolution rules;
- Magnet Pull unless the creature actually has and uses the relevant PTU mechanic.

### Magnemite / Magneton / Magnezone

Species lore may justify electromagnetic observation and research.

It does not authorize:

- power generation rates;
- network access;
- radio decoding;
- environmental levitation rules;
- evolution through any locally authored anomaly without PTU/Caelo confirmation.

### Clefairy gatherings

A gathering may have an authored anomaly only when the world state explicitly records that phenomenon.

The system must not generate magnetic anomalies from every Clefairy spawn.

## Integration with existing layers

### Astronomy

Astronomy owns celestial-event timing and sky context.

Geomagnetism can attach an aurora event to an observed magnetic disturbance.

### Technology

Technology owns device/network operational state.

Geomagnetism can create an external-driver hypothesis or event input.

Technology decides what actually failed.

### Communications

Communications owns whether radio/data channels degrade or fail.

A geomagnetic event may supply a causal input, not the final delivery result.

### Cartography and Travel

This layer provides time/location-specific magnetic correction state.

Cartography stores it in map editions. Travel uses route knowledge and actor capabilities.

### Geology

Geology owns magnetic-mineral bodies and substrate.

A local crustal anomaly may reference those records.

### Science

Science owns hypotheses, replication, publication and confidence changes.

### Public Memory / Media

A spectacular aurora or navigation incident can become public history. Public belief must not overwrite field truth.

## Minecraft projection

Minecraft may present:

- compass behavior through a server-approved UI layer;
- observatory buildings and instruments;
- aurora/sky effects;
- device-failure visuals;
- warning boards;
- magnetic Pokémon gathering near authored sites;
- changed route guidance.

Minecraft must not independently calculate:

- field truth;
- declination history;
- device interference;
- evolution eligibility;
- PTU Magnet Pull;
- damage;
- movement restriction;
- rare-spawn modifiers.

## Anti-exploit policy

Players must not be able to create infinite anomalies or rare encounters by placing metal blocks, redstone, compasses or electrical machinery.

Player construction can create an `INTERFERENCE_SOURCE_CANDIDATE` only when the server's technology/geomagnetic systems recognize the installation at a coarse authored scale.

Loaded Magnemite/Probopass entities never define regional field truth.

## Encounter contract A — Observatory Calibration Failure

Narrative premise:

A regional observatory begins reporting an abrupt directional anomaly after nearby construction and repeated Probopass sightings. The team must establish whether the issue is field change, local interference, equipment movement or another cause.

FULL version:

- instrument stations as interactable objectives;
- localized magnetic zones if PTU rules justify them;
- Steel combatants affected only by exact verified mechanics;
- protect/inspect objectives;
- AI that can defend, retreat or disrupt equipment;
- semantic Minecraft playback.

Required permanent capability families:

- targeting/footprints/range/LoS: VERIFIED foundation;
- base movement legality: VERIFIED foundation;
- complete movement including forced movement/interception: BLOCKING if magnetic displacement or escort lanes are used;
- core calculations: VERIFIED foundation;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if a verified status is involved;
- terrain/weather/hazards/zones/reactions: BLOCKING for any magnetic zone;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

All calibration, interference and field-state investigation occurs in overworld/world state. If a battle occurs, the server freezes one ordinary arena and uses no magnetic zone or device mechanic.

## Encounter contract B — Compass Pass

Narrative premise:

An old route map and modern compass disagree in a mountain pass. Travelers blame a new anomaly, but the actual cause remains unresolved.

FULL version:

- navigation objective under time pressure;
- dynamic route choices;
- possible local magnetic-navigation disruptions;
- non-KO escape/reach objectives;
- tactical AI for wild Pokémon using the same route.

Required families:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement/interception: BLOCKING for dynamic route pressure;
- action economy/initiative: VERIFIED;
- lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if the field changes tactical movement;
- AI legal actions: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version:

Navigation is resolved before combat from map edition + field revision + validated PTU/Caelo checks. Any battle uses static geometry and no compass modifier.

## Encounter contract C — Aurora Relay Night

Narrative premise:

A rare aurora coincides with degraded relay service across several settlements. The players must keep a remote station operating while the cause of each failure remains under investigation.

FULL version:

- relay components as interactables;
- timed service objectives;
- communications/power consequences;
- optional Pokémon encounters around the site;
- no magnetic battle effect unless independently verified.

Required families:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle: PARTIAL;
- move/ability/item/Feature families: only if selected content needs them, each PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for protect/disable/withdraw goals;
- adapter/playback: BLOCKING.

REDUCED version:

Aurora, relay degradation and repair remain world state. AutoPTU only resolves a standard combat if a distinct confrontation occurs.

## Canon promotion gates

Before any magnetic system becomes canon, review:

- whether Ouros has a global magnetic model comparable to a normal planetary field;
- which regions have authored local anomalies;
- whether any observatory network exists;
- which Pokémon/location relationships are canon;
- whether special magnetic-field evolution exists in the project's PTU/Caelo interpretation;
- how compass/map correction is exposed to players;
- privacy/security implications for infrastructure incidents;
- exact PTU mechanics before tactical use.

## Explicit non-inferences

Do not infer:

- Electric-type = magnetic sensing;
- Steel-type = attracted by every field;
- Magnet Pull = environmental magnetism;
- Magnezone lore = extraterrestrial contact;
- aurora = Weather;
- aurora = Legendary event;
- compass error = anomaly;
- device failure = Probopass/Magnemite fault;
- special magnetic field = automatic evolution;
- magnetic field = forced movement;
- metal-rich geology = battle modifier.