# Ouros Irrigation & Agricultural Water Delivery Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Pass: 155

## Purpose

This layer owns the operational path that delivers water from an already-valid source to a managed agricultural destination. It exists between Freshwater/Groundwater and Food/Agriculture.

It does not define regional water law, crop growth formulas, PTU Water effects, navigation, drinking-water service or groundwater truth.

## Authority boundary

Freshwater owns rivers, streams, reservoirs, flow and broad surface-water state.
Groundwater owns aquifers, wells, pumping and drawdown.
Food/Agriculture owns farms, orchards, crop state and cultivation response.
Land Tenure owns authored access and use permissions.
Inland Waterways owns navigability, locks and vessel operations.
Irrigation owns delivery operations from source handoff to field application and immediate return-flow observations.

## Core separation

```text
source state
  -> authorized/available irrigation intake
  -> delivery request
  -> schedule / rotation / delivery window
  -> diversion event
  -> conveyance network state
  -> turnout / control-point operation
  -> measured field delivery
  -> field application record
  -> tailwater / seepage observation
  -> Freshwater or Groundwater handoff
  -> crop-response handoff to Agriculture
```

No arrow is automatic.

A wet canal does not prove a field was irrigated.
A dry field does not prove the source failed.
A scheduled delivery does not prove diversion occurred.
A turnout opening does not prove the measured volume reached its destination.
A successful crop does not prove the delivery records were correct.

## Persistent irrigation system

```yaml
irrigation_system:
  irrigation_system_id: null
  name: null
  source_handoff_refs: []
  main_conveyance_asset_refs: []
  delivery_zone_ids: []
  operator_refs: []
  maintenance_authority_refs: []
  active_operating_revision_id: null
  historic_revision_ids: []
  source_refs: []
  canon_status: proposed
```

Candidate system forms include gravity-fed ditch networks, canal/lateral systems, pumped systems, local reservoir-fed distribution, spring-fed garden systems, orchard micro-distribution and mixed authored systems.

These are narrative/operational classifications. They grant no mechanical bonuses.

## Network assets

```yaml
irrigation_asset:
  asset_id: null
  irrigation_system_id: null
  asset_type: null
  location_ref: null
  upstream_asset_refs: []
  downstream_asset_refs: []
  physical_state_ref: null
  operational_state: unknown
  measurement_device_refs: []
  current_configuration_ref: null
  maintenance_history_refs: []
  source_refs: []
```

Candidate asset types:
- diversion_point;
- headgate;
- main_canal;
- lateral;
- ditch;
- turnout;
- flume_or_crossing;
- pump_station;
- balancing_pond;
- field_inlet;
- tailwater_ditch;
- return_outfall;
- other_authored.

Physical existence and operational state remain separate.

## Delivery request and schedule

```yaml
irrigation_delivery_request:
  request_id: null
  destination_ref: null
  requester_ref: null
  crop_or_land_use_ref: null
  requested_window: null
  requested_amount_band: null
  priority_basis_ref: null
  authorization_ref: null
  status: requested
  source_refs: []
```

```yaml
irrigation_delivery_window:
  delivery_window_id: null
  irrigation_system_id: null
  destination_refs: []
  starts_at: null
  ends_at: null
  planned_source_refs: []
  planned_route_asset_refs: []
  operating_notes: []
  revision_reason_ref: null
  status: planned
```

A rotation or priority basis is stored only when canon or an authored agreement defines it. The layer never invents universal water rights.

## Diversion and conveyance

```yaml
irrigation_diversion_event:
  diversion_event_id: null
  source_handoff_ref: null
  intake_asset_id: null
  started_at: null
  ended_at: null
  observed_flow_records: []
  operator_refs: []
  configuration_refs: []
  delivery_window_refs: []
  interruption_refs: []
  confidence: null
```

```yaml
conveyance_observation:
  observation_id: null
  segment_ref: null
  observed_at: null
  observer_ref: null
  upstream_measurement_ref: null
  downstream_measurement_ref: null
  apparent_loss_band: null
  suspected_cause_refs: []
  evidence_refs: []
  certainty: unknown
```

Possible apparent causes include seepage, evaporation, leak/breach, unrecorded diversion, measurement error, changed configuration or incomplete records. None is inferred from the shortfall alone.

## Turnouts and control points

A turnout is a persistent operating asset, not merely a Minecraft gate block.

```yaml
irrigation_control_event:
  control_event_id: null
  asset_id: null
  occurred_at: null
  operator_ref: null
  prior_configuration_ref: null
  new_configuration_ref: null
  intended_destination_refs: []
  measurement_refs: []
  reason_ref: null
  authorization_ref: null
```

A control action can be correct and still fail to produce the expected field delivery because other parts of the system changed.

## Field delivery and application

```yaml
field_delivery_record:
  field_delivery_id: null
  destination_ref: null
  delivery_window_ref: null
  started_at: null
  ended_at: null
  inlet_asset_refs: []
  measured_delivery_refs: []
  estimated_amount_band: null
  coverage_observations: []
  interruption_refs: []
  operator_notes: []
  status: observed
```

```yaml
field_application_observation:
  application_observation_id: null
  destination_ref: null
  observed_at: null
  method_descriptor: null
  wet_area_ref: null
  dry_area_ref: null
  ponding_refs: []
  runoff_refs: []
  soil_observation_refs: []
  crop_state_ref: null
  interpretation_status: unresolved
```

The irrigation layer records what water did operationally. Food/Agriculture determines what that means for cultivation.

## Tailwater and return flow

```yaml
irrigation_return_flow_observation:
  return_flow_observation_id: null
  source_field_delivery_refs: []
  observed_at: null
  pathway_type: surface_tailwater | suspected_subsurface | drain_return | unknown
  location_ref: null
  destination_water_ref: null
  measurement_refs: []
  water_quality_observation_refs: []
  confidence: null
  handoff_refs: []
```

Surface observations can be handed to Freshwater. Suspected deep percolation or delayed groundwater return is handed to Groundwater for interpretation.

Irrigation never declares aquifer recharge solely because water disappeared from a field.

## Drought and constrained delivery

Aridity/Drought may change source availability and operational pressure. Irrigation can respond through versioned schedules, shorter windows, alternative sources already authorized by other layers or temporary delivery plans.

Do not invent:
- universal seniority rules;
- emergency expropriation;
- fixed percentages;
- crop priority law;
- automatic conflict between upstream and downstream users.

## Pokémon participation

Pokémon participation must create explicit actor records.

```yaml
pokemon_irrigation_participation:
  participation_id: null
  pokemon_entity_id: null
  role_ref: null
  starts_at: null
  ends_at: null
  observed_tasks: []
  workload_refs: []
  refusal_or_pause_refs: []
  agency_handoff_refs: []
  source_refs: []
```

Species, Type and Moves do not establish capacity. A Lotad that carries water once does not become an irrigation asset. An institutional assignment belongs to Working Pokémon and Pokémon Agency.

## Minecraft / Cobblemon projection

Minecraft may display canals, ditches, gates, pumps, wet fields, dry laterals, maintenance crews and temporary closures.

Minecraft never determines:
- delivery authorization;
- measured volume;
- crop water requirement;
- operator intent;
- source truth;
- return-flow attribution;
- Pokémon workload;
- PTU Terrain or Status.

Player block edits require a world-state transaction before they become an authoritative revision. Chunk reload cannot restore an old canal configuration.

## Encounter contracts

### Headgate Failure During Delivery Window

Full version: technicians must reach multiple controls while water routes and safe paths can change; wildlife may withdraw through the same corridor.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING;
- action economy/initiative: VERIFIED;
- full lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if water or mud changes tactical access;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for PROTECT_TECHNICIAN, REACH_CONTROL, WITHDRAW;
- Minecraft/Cobblemon/Craftics playback: BLOCKING.

Reduced version: shut the intake and move technicians/wildlife outside combat using world state. Freeze a dry legal arena. Resolve only a conventional confrontation. Resume repair and delivery accounting afterward.

### Canal Breach at Orchard Reach

Full version: breach geometry, moving water, debris and actors crossing away from the damaged reach.

Dependencies: complete movement BLOCKING; environmental family BLOCKING; tactical AI BLOCKING; adapter/playback BLOCKING. Core targeting/calculations/action economy use VERIFIED foundations.

Reduced version: Freshwater/Irrigation freeze the breach and isolate the orchard reach first. Battle occurs on a static adjacent map. Winning does not repair the breach or restore crop delivery.

### Wildlife at the Lateral During Drought Rotation

Full version: workers need access while a wild group uses the lateral as temporary water habitat and should prefer WITHDRAW/CROSS rather than fight to KO.

Dependencies: complete movement BLOCKING; AI tactical policy BLOCKING; adapter/playback BLOCKING. Environmental mechanics are required only if water depth or mud matters tactically.

Reduced version: ecology and access are resolved first. If conflict remains, use a static battle with only actual combatants. Capture/KO never counts as successful irrigation management.

## Permanent engine boundary

Current live evidence at Pass 155:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING as complete families:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

A representative reaction, Move special or forced-movement instruction never promotes its whole category.

## Canon questions left open

- Which Ouros regions use irrigation at all?
- Which systems predate the players?
- Which sources are surface water, groundwater or mixed?
- Who operates headgates and turnouts?
- Are delivery rotations institutional, contractual, customary or region-specific?
- How much operational detail should advance offline?
- Which agricultural sites have known tailwater or recharge links?
- Which Pokémon have authored voluntary roles in agricultural water work?
- What PTU/Caelo rules, if any, govern overworld Water Move use, mud, currents or agricultural work?
