# Radio, Wireless Propagation & Communications Layer

Status: PROPOSED SYSTEMS DESIGN. NON-CANON. Pass 123.

## Purpose

This layer specializes the physical and operational reach of wireless communications in Ouros.

It does not replace Media/Communications, which remains authoritative for information packets, channels, sender/recipient state, delivery and acknowledgement. It does not replace Technology/Energy/Infrastructure, which remains authoritative for the physical condition, maintenance, power dependencies and faults of towers, repeaters, devices and backhaul assets.

This layer owns the question between those systems: given functioning or degraded wireless assets, where and under what conditions can a wireless service plausibly operate, and can different networks actually interoperate?

## Authority boundary

This layer does not own:
- message truth, publication or editorial framing;
- message delivery receipts;
- device ownership or digital account authority;
- asset maintenance or electrical-service truth;
- magnetic-field truth;
- weather truth;
- map truth outside communications coverage products;
- PTU Electric Terrain, Electric-type Moves, device damage, Status effects or jamming mechanics;
- Minecraft client signal icons as authoritative state.

It may consume:
- Technology asset state;
- Communications channel definitions;
- Meteorology conditions;
- Architecture/building revisions;
- Flora/canopy changes;
- Alpine/terrain geography;
- Geomagnetism interference evidence;
- Emergency Services operational requirements;
- Metrology/calibration state for measurement instruments.

## Core separation

Do not collapse:

physical radio assets -> configuration/topology -> propagation context -> observed coverage -> modeled coverage revision -> interoperability -> channel availability -> message-delivery attempt.

A tower can be online while a valley has no usable signal.

A field device can receive a broadcast while being unable to transmit back.

Two institutions can each have functioning systems and still lack direct interoperability.

One successful contact does not prove a reliable route.

A coverage map can be valid for its publication date and become obsolete later.

## WIRELESS_SERVICE

```yaml
wireless_service:
  wireless_service_id: null
  service_name: null
  operator_institution_ids: []
  communication_channel_refs: []
  radio_site_ids: []
  repeater_ids: []
  relay_link_ids: []
  interoperability_profile_ids: []
  coverage_revision_ids: []
  fallback_plan_ids: []
  current_service_state: unknown
  canon_status: proposed
```

A wireless service is a logical service, not a claim that Ouros uses any real-world frequency or protocol.

Candidate service roles:
- regional field communications;
- local institutional communications;
- public broadcast;
- emergency coordination;
- research telemetry;
- transport operations;
- expedition communications;
- event coordination;
- remote-site monitoring.

## RADIO_SITE

```yaml
radio_site:
  radio_site_id: null
  location_id: null
  operator_id: null
  technology_asset_refs: []
  supported_service_ids: []
  site_role: transmitter|receiver|repeater|relay|broadcast|monitoring|gateway|mixed
  elevation_context_ref: null
  surrounding_structure_refs: []
  surrounding_vegetation_refs: []
  access_state_ref: null
  operational_state_ref: null
```

Technology owns whether the equipment works. This layer owns how the site participates in the wireless topology.

A visible tower does not prove every actor can use it.

## RELAY_LINK

```yaml
relay_link:
  relay_link_id: null
  from_site_id: null
  to_site_id: null
  service_ids: []
  expected_path_class: direct|repeated|gateway|unknown
  propagation_profile_ref: null
  current_state: usable|degraded|intermittent|blocked|unknown
  observation_refs: []
  last_verified_at: null
```

A relay link can fail while both endpoint sites remain operational.

## PROPAGATION_PROFILE_REVISION

Ouros should use a coarse model, not RF simulation.

```yaml
propagation_profile_revision:
  propagation_profile_id: null
  wireless_service_id: null
  area_ref: null
  valid_from: null
  valid_to: null
  terrain_context_refs: []
  building_context_refs: []
  vegetation_context_refs: []
  weather_context_refs: []
  expected_reach_class: strong|ordinary|marginal|intermittent|unknown
  known_shadow_area_refs: []
  model_basis_refs: []
  confidence: null
  supersedes_id: null
```

The revision is a model. It does not overwrite observations.

Changes that can justify a new revision include:
- a new high-rise or industrial building;
- vegetation growth or removal;
- a new relay;
- decommissioned infrastructure;
- altered terrain or landslide geometry;
- seasonal foliage;
- changed equipment configuration;
- new survey evidence.

## COVERAGE_OBSERVATION

```yaml
coverage_observation:
  coverage_observation_id: null
  wireless_service_id: null
  observed_at: null
  location_ref: null
  device_or_instrument_ref: null
  actor_or_team_ids: []
  observation_type: receive|transmit|two_way|broadcast|telemetry|latency|dropout|qualitative
  result: usable|marginal|intermittent|failed|unknown
  environmental_context_refs: []
  instrument_state_ref: null
  source_refs: []
```

One observation is local evidence, not a regional coverage declaration.

## COVERAGE_ASSESSMENT

```yaml
coverage_assessment:
  coverage_assessment_id: null
  wireless_service_id: null
  area_ref: null
  effective_period_ref: null
  observation_ids: []
  propagation_profile_id: null
  coverage_class: reliable|mixed|marginal|dead_zone|unknown
  uncertainty: null
  reason_claim_ids: []
  public_product_refs: []
```

A `dead_zone` means the specified service was not reliably available under the assessed conditions. It does not prove the cause.

## INTERFERENCE_INCIDENT

```yaml
wireless_interference_incident:
  incident_id: null
  service_ids: []
  location_or_area_ref: null
  started_at: null
  ended_at: null
  observed_symptoms: []
  observation_refs: []
  nearby_asset_refs: []
  nearby_pokemon_refs: []
  geomagnetism_incident_refs: []
  cause_hypothesis_ids: []
  current_state: open|mitigated|resolved|unresolved
```

Nearby Electric-, Steel- or magnetic-associated Pokémon are proximity evidence only.

## INTERFERENCE_HYPOTHESIS

```yaml
interference_hypothesis:
  hypothesis_id: null
  incident_id: null
  proposed_cause_type: configuration|equipment_fault|other_service|environment|geomagnetic|pokemon|congestion|unknown|other
  proposed_cause_ref: null
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  confidence: null
  status: proposed|supported|weakened|rejected|unresolved
```

No hypothesis becomes sabotage, Pokémon fault or world truth without evidence.

## INTEROPERABILITY_PROFILE

```yaml
interoperability_profile:
  interoperability_profile_id: null
  participating_service_ids: []
  participating_institution_ids: []
  valid_from: null
  valid_to: null
  compatibility_state: direct|gateway_required|procedure_required|partial|unavailable|unknown
  supported_information_types: []
  gateway_refs: []
  procedure_refs: []
  exercise_or_incident_evidence_refs: []
  limitations: []
```

Two agencies carrying radios do not imply interoperability.

A temporary gateway can solve one incident without permanently merging the networks or institutions.

## CHANNEL_LOAD_EPISODE

```yaml
channel_load_episode:
  load_episode_id: null
  wireless_service_id: null
  started_at: null
  ended_at: null
  area_ref: null
  demand_driver_refs: []
  observed_effects: []
  mitigation_refs: []
  delivery_consequence_refs: []
```

Potential drivers include festivals, tournaments, evacuation, tourism surges or large research operations.

Congestion is not a battle debuff.

## FIELD_REPEATER_DEPLOYMENT

```yaml
field_repeater_deployment:
  deployment_id: null
  portable_asset_ref: null
  requested_by_id: null
  deployed_by_ids: []
  planned_location_ref: null
  actual_location_ref: null
  service_ids: []
  started_at: null
  ended_at: null
  coverage_observation_refs: []
  operational_state_ref: null
  recovery_state: planned|deployed|active|failed|retrieved|lost|unknown
```

Deployment can be a meaningful expedition objective without giving the device tactical HP or a magical radius.

## FALLBACK_COMMUNICATION_PLAN

```yaml
fallback_communication_plan:
  fallback_plan_id: null
  institution_or_operation_id: null
  primary_service_ids: []
  trigger_conditions: []
  fallback_channel_refs: []
  fallback_route_refs: []
  contact_point_refs: []
  check_in_schedule_refs: []
  last_exercised_at: null
  known_limitations: []
```

A fallback can use courier, fixed check-in points, local service or another existing channel. It does not require a new fictional technology.

## RADIO_QUIET_OR_RESTRICTED_USE_AREA

This object is optional and remains disabled until Ouros canon establishes a relevant institution or research practice.

```yaml
radio_quiet_area:
  area_id: null
  purpose_ref: null
  requesting_institution_id: null
  authority_basis_ref: null
  affected_service_ids: []
  time_window_refs: []
  exception_refs: []
  public_notice_refs: []
  canon_enabled: false
```

Do not import real-world spectrum law.

## Coverage history and Chronicle

Coverage maps should be versioned.

A city can grow around a once-clear relay path. A forest can regain canopy. A tower can be retired. A new tunnel can create a transport dead zone. A storm can remove a relay while local devices continue working within the settlement.

Chronicle stores these transitions. It does not rewrite old reports.

## Interaction with Media/Communications

This layer exposes channel availability and reach constraints.

Media/Communications still performs:
- message creation;
- sender/recipient resolution;
- send/delivery/acknowledgement state;
- publication;
- corrections;
- public information spread.

Example flow:

`message created -> intended channel selected -> wireless service availability checked -> interoperability checked -> delivery attempt -> Media stores result`

## Interaction with Technology/Energy

Technology owns:
- whether a transmitter is powered;
- whether its hardware is damaged;
- maintenance;
- component replacement;
- configuration assets;
- backhaul dependencies.

This layer can observe that `radio_site_12` is operational but its downstream valley coverage is still degraded.

## Interaction with Geomagnetism and Meteorology

A geomagnetic event or unusual atmospheric condition can become a cause hypothesis only when the relevant authority establishes that physical event.

This layer records the communication consequence.

It never creates geomagnetic or weather truth itself.

## Interaction with Rotom and technical Pokémon

Rotom, Magnemite, Magneton, Probopass and other Pokémon can participate only through authored behavior and observed events.

Examples that are safe:
- a Rotom inhabits a specific compatible device;
- a Magnemite group is observed near an interference site;
- a technical team tests service before and after those Pokémon leave;
- a Pokémon voluntarily assists a technician under an established institutional relationship.

Unsafe shortcuts:
- Electric type -> repeater bonus;
- Rotom -> administrator access;
- magnetic Pokémon -> confirmed interference;
- Thunder -> destroyed electronics;
- Electric Terrain -> radio jam;
- Pokémon presence -> network ownership.

## Minecraft projection

Minecraft can render:
- towers;
- antennas;
- relay huts;
- portable field units;
- maintenance work;
- visual signal indicators;
- maps showing estimated coverage;
- public notices;
- changed infrastructure after damage/repair.

The server/world-state layer remains authoritative.

A client-side “signal bars” UI is presentation only.

Chunk loading cannot create or erase coverage history.

## Battle boundary

Radio coverage is overworld/institutional state.

It does not modify:
- Accuracy;
- initiative;
- Command;
- Move legality;
- AI perception;
- damage;
- Electric-type effects;
- item use;
- Trainer Feature availability;
- LoS.

AutoPTU targeting LoS is geometric battle LoS. It does not prove radio propagation.

The new Java spatial status-prevention hooks use battle geometry for Ability radii. They do not provide an overworld propagation engine.

## Encounter contracts

### Relay Ridge Access — FULL

Premise: a field team must reach a relay site during a regional communications failure while another conflict makes the approach unsafe.

Needed capability families:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if technicians move tactically;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle/damage/status/moves/abilities/items/Trainer Features: according to selected combatants, generally PARTIAL families;
- terrain/weather/hazards/zones/reactions: BLOCKING only if the ridge itself has validated tactical environmental mechanics;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for PROTECT/CLEAR_ROUTE/REACH_OBJECTIVE;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: technicians remain outside the grid. Technology isolates the relay into a safe maintenance state. If confrontation remains, AutoPTU receives a static access platform. Service restoration is verified afterward through coverage observations; winning the battle does not restore signal automatically.

### Festival Channel Saturation — FULL

Premise: a recurring festival overloads a local wireless service while a separate wildlife or security incident requires coordination.

Needed capability families:
- complete movement: BLOCKING if crowds/noncombatants move through the tactical space;
- AI tactical policy: BLOCKING for evacuation/withdrawal/route-clearing goals;
- adapter/playback: BLOCKING for crowd and communications-state presentation;
- environment family only if a separate validated hazard is active.

REDUCED: crowd routing and channel load resolve in world state before battle. A cleared plaza or side street becomes the static arena. Communications degradation affects what institutions know and when, not combat stats.

### Emergency Interoperability Bridge — FULL

Premise: two response organizations have functioning but incompatible systems. A portable gateway/repeater must be deployed at a chokepoint during an ongoing incident.

Needed capability families:
- complete movement: BLOCKING for equipment carriers and moving objectives;
- AI tactical policy: BLOCKING for PROTECT/REACH_OBJECTIVE/CLEAR_ROUTE;
- items: PARTIAL only if the device is ever represented as a PTU item rather than world-state equipment;
- adapter/playback: BLOCKING;
- other combat families follow actual combatants.

REDUCED: the gateway is deployed before combat begins and remains outside tactical authority. The battle protects a static location. After combat, Communications and this layer test whether the bridge actually works. Victory cannot establish interoperability by itself.

## New overworld blockers

- `WIRELESS_SERVICE_REGISTRY`
- `RADIO_SITE_TOPOLOGY`
- `RELAY_LINK_STATE`
- `PROPAGATION_PROFILE_REVISIONS`
- `COVERAGE_OBSERVATION_LEDGER`
- `COVERAGE_ASSESSMENTS`
- `DEAD_ZONE_HISTORY`
- `WIRELESS_INTERFERENCE_INCIDENT_GRAPH`
- `INTERFERENCE_HYPOTHESIS_GRAPH`
- `INTEROPERABILITY_PROFILE_STATE`
- `CHANNEL_LOAD_EPISODES`
- `FIELD_REPEATER_DEPLOYMENTS`
- `FALLBACK_COMMUNICATION_PLANS`
- `COVERAGE_TO_COMMUNICATION_CHANNEL_HANDOFF`
- `TECHNOLOGY_TO_WIRELESS_SERVICE_HANDOFF`
- `GEOMAGNETISM_TO_INTERFERENCE_HANDOFF`
- `METEOROLOGY_TO_PROPAGATION_CONTEXT_HANDOFF`
- `RADIO_TO_MINECRAFT_PRESENTATION`
- `RADIO_TO_EMERGENCY_SERVICES_HANDOFF`

## Hard non-inferences

Do not infer:
- tower online -> full coverage;
- tower visible -> usable service;
- device has signal -> message delivered;
- successful contact once -> reliable coverage;
- no signal -> sabotage;
- no signal -> broken tower;
- dead zone -> intentional jamming;
- two radios -> interoperability;
- repeater powered -> repeater configured correctly;
- broadcast received -> two-way communication works;
- old coverage map -> current coverage;
- Electric-type Pokémon -> generator/repeater/jammer;
- Rotom -> network administrator;
- Electric Terrain -> wireless interference;
- battle LoS -> radio propagation;
- Java spatial Ability radius -> overworld signal radius;
- Minecraft redstone/device state -> PTU rule truth;
- battle victory -> service restored.

## Canon questions left open

Ouros still needs authored decisions on:
- technology level by region;
- whether regional wireless services exist everywhere or only in developed corridors;
- who operates public broadcast and field services;
- whether emergency organizations share infrastructure;
- whether dedicated research/telemetry networks exist;
- whether any radio-quiet areas exist;
- what kinds of portable field equipment exist;
- which Pokémon have institutional technical roles;
- whether player clubs/businesses may operate local services;
- privacy expectations for wireless communications.

No frequencies, signal ranges, licenses, jamming rules, equipment Skill DCs or PTU modifiers are established here.