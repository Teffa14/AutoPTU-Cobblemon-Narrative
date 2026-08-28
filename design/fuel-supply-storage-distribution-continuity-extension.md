# Ouros Fuel Supply, Storage & Distribution Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon. Creates no PTU rules.
Date: 2026-08-28
Research provenance: `research/2026-08-28-fuel-supply-storage-distribution-continuity-scan-109.md`.

## Purpose

This extension preserves operational continuity for an authored fuel system when a region actually has one.

It covers the sequence after an accepted supply enters the fuel system and before a downstream consumer can rely on that supply:

accepted supply → operating storage → allocation/release → internal transfer/loading readiness → distribution handoff → local delivery/service-point state → downstream availability handoff.

It does not decide which fuels exist in Ouros. It does not create extraction, refining, combustion, pricing, safety, pollution or battle mechanics.

## Authority boundary

This layer owns:

- persistent fuel-system identity;
- terminal/depot/service-point identity;
- operating-storage state specific to the fuel service;
- supply-lot bindings to externally owned item/batch identity;
- broad stock-availability observations;
- allocation and release state;
- internal transfer readiness;
- loading/distribution readiness;
- local service-sector availability;
- temporary supply arrangements;
- shortage and recovery observations;
- staged restoration of fuel service;
- legacy/decommissioned fuel-site history.

It references but does not own:

- extraction or production — Manufacturing, Material Culture or later authored resource systems;
- sourcing, order, receipt and acceptance — Procurement;
- item/batch identity and rules-bearing effects — Material Culture/PTU/Caelo;
- batch holds, quarantine, recall and correction — Batch Traceability;
- general putaway/picking/staging — Storage/Warehousing when that workflow is used;
- shipment legs and custody transfer — Courier, Port, Rail, Road or other transport owner;
- customer payment and contracts — Finance/Agreements;
- public-facing shop/service offer — Storefront/Commercial Services;
- generic technical asset condition and repair — Technology/Facility Maintenance;
- outages across multiple services — Infrastructure Outage;
- fire incidents — Wildfire/Fire Response;
- worker restrictions and near misses — Worksite Safety;
- spill, waste, contamination and cleanup — Waste/Sanitation/Pollution and Conservation as applicable;
- public access/closure — owning Road, Port, Facility or Civic system;
- Pokémon work assignments — Pokémon Work;
- combat mechanics — AutoPTU.

## 1. Fuel system

```yaml
fuel_supply_system:
  fuel_system_id: null
  authored_fuel_kind_ref: null
  geographic_scope_ids: []
  operator_actor_or_institution_ids: []
  accepted_supply_interface_ids: []
  terminal_or_depot_ids: []
  distribution_path_ids: []
  service_sector_ids: []
  service_point_ids: []
  downstream_consumer_refs: []
  current_service_state: UNKNOWN
  active_shortage_episode_ids: []
  temporary_supply_ids: []
  canon_reference_ids: []
  provenance_refs: []
```

`authored_fuel_kind_ref` must point to approved world/material data. The generator may not invent gasoline, diesel, coal, gas, biomass or any other fuel because a scene needs energy.

## 2. Accepted supply handoff

A supply enters this layer only after the owner of procurement/production/transport establishes the relevant handoff.

```yaml
fuel_supply_handoff:
  handoff_id: null
  fuel_system_id: null
  source_owner_ref: null
  material_or_batch_refs: []
  aggregate_supply_ref: null
  accepted_at: null
  receiving_facility_id: null
  custody_ref: null
  external_hold_refs: []
  observation_refs: []
  status: ACCEPTED_FOR_FUEL_SYSTEM
```

Suggested states:

- AWAITING_EXTERNAL_ACCEPTANCE
- ACCEPTED_FOR_FUEL_SYSTEM
- HELD_BY_EXTERNAL_AUTHORITY
- REDIRECTED
- REJECTED_BY_OWNER
- SUPERSEDED

Acceptance does not prove that the supply is available for release.

## 3. Fuel terminal or depot

```yaml
fuel_terminal:
  terminal_id: null
  fuel_system_id: null
  location_id: null
  operator_ids: []
  storage_group_ids: []
  receiving_interface_ids: []
  distribution_interface_ids: []
  internal_transfer_path_ids: []
  utility_dependency_ids: []
  maintenance_dependency_ids: []
  access_dependency_ids: []
  safety_dependency_ids: []
  current_operating_state: UNKNOWN
  verification_refs: []
  history_event_ids: []
```

Suggested operating states:

- UNKNOWN
- OPERATIONAL
- CONSTRAINED
- RECEIPT_PAUSED
- RELEASE_PAUSED
- DISTRIBUTION_PAUSED
- ACCESS_RESTRICTED
- ISOLATED
- MAINTENANCE
- TESTING
- CLOSED
- DECOMMISSIONED
- REPURPOSED

A terminal can contain supply while release or distribution remains unavailable.

## 4. Operating storage group

This is a fuel-service operational view. Material/batch identity remains externally owned.

```yaml
fuel_storage_group:
  storage_group_id: null
  terminal_id: null
  authored_material_scope_refs: []
  external_storage_location_refs: []
  observed_supply_presence_refs: []
  external_hold_refs: []
  current_availability_band: UNKNOWN
  reserved_allocation_refs: []
  release_ready_refs: []
  last_verified_at: null
```

Broad availability bands:

- UNKNOWN
- AVAILABLE
- CONSTRAINED
- RESERVED
- HELD
- UNAVAILABLE

No numeric capacity, volume, pressure, mass, energy content or consumption rate is created here.

Hard separation:

`FUEL_PRESENT != AVAILABLE`.

Supply may be physically present but reserved, held, inaccessible, unverified or awaiting another authority.

## 5. Supply observation

```yaml
fuel_supply_observation:
  observation_id: null
  subject_id: null
  observer_id: null
  observed_at: null
  geographic_or_facility_scope_refs: []
  observed_state_claim: null
  quantity_claim_ref: null
  evidence_refs: []
  confidence: UNKNOWN
```

Examples:

- service point reports unavailable supply;
- depot reports constrained release;
- delivery arrived but has not completed external handoff;
- reserve is present but allocated elsewhere;
- one sector reports normal availability while another reports interruption.

A shortage observation does not prove hoarding, theft, sabotage, market manipulation, production failure or transport failure.

## 6. Allocation record

Allocation records which downstream purpose a verified supply portion is reserved for when authored authority requires it.

```yaml
fuel_allocation:
  allocation_id: null
  fuel_system_id: null
  source_storage_group_id: null
  beneficiary_sector_or_consumer_refs: []
  allocation_basis_ref: null
  authority_ref: null
  created_at: null
  effective_window_ref: null
  material_scope_refs: []
  current_state: PROPOSED
  release_ref: null
```

Suggested states:

- PROPOSED
- AUTHORIZED
- RESERVED
- RELEASE_REQUESTED
- RELEASED
- PARTIALLY_FULFILLED
- FULFILLED
- CANCELLED
- SUPERSEDED

This layer records an allocation only when a legitimate authority already exists. It cannot invent rationing law, emergency priority or moral preference.

`ALLOCATED != RELEASED`.

## 7. Release record

```yaml
fuel_release:
  release_id: null
  allocation_or_request_ref: null
  storage_group_id: null
  material_scope_refs: []
  authorized_by_ref: null
  authorized_at: null
  physically_prepared_at: null
  loading_readiness_ref: null
  external_handoff_ref: null
  status: AUTHORIZED
```

Lifecycle:

AUTHORIZED → PREPARING → RELEASE_READY → AWAITING_EXTERNAL_HANDOFF → HANDED_OFF_EXTERNAL.

Branches:

HELD, BLOCKED_ACCESS, BLOCKED_EQUIPMENT, CANCELLED, SUPERSEDED.

`RELEASED/RELEASE_READY != DELIVERED`.

The transport owner records the external movement and custody leg.

## 8. Internal transfer readiness

```yaml
fuel_internal_transfer:
  transfer_id: null
  terminal_id: null
  source_storage_group_id: null
  destination_interface_or_group_id: null
  material_scope_refs: []
  authorization_ref: null
  started_at: null
  physically_complete_at: null
  verification_refs: []
  status: PLANNED
```

Suggested states:

PLANNED, READY, IN_PROGRESS, PHYSICALLY_COMPLETE, VERIFIED_COMPLETE, PAUSED, BLOCKED, CANCELLED, SUPERSEDED.

No flow rate or technical procedure is implied.

`PHYSICALLY_COMPLETE != VERIFIED_COMPLETE`.

## 9. Distribution path

A path records authored operational connectivity, not Minecraft adjacency.

```yaml
fuel_distribution_path:
  path_id: null
  fuel_system_id: null
  origin_interface_ref: null
  destination_sector_or_service_point_refs: []
  transport_owner_ref: null
  route_or_link_refs: []
  dependency_refs: []
  current_path_state: UNKNOWN
  last_verified_at: null
  temporary_reroute_refs: []
```

Possible states:

- UNKNOWN
- AVAILABLE
- CONSTRAINED
- INTERRUPTED
- REROUTED
- TESTING
- VERIFIED
- SUSPENDED

The path may represent an abstract authored relationship. It does not define a pipeline or road vehicle unless canon does.

## 10. Fuel service sector

```yaml
fuel_service_sector:
  sector_id: null
  fuel_system_id: null
  geographic_scope_ids: []
  normal_path_ids: []
  alternate_path_ids: []
  service_point_ids: []
  downstream_consumer_refs: []
  current_availability: UNKNOWN
  availability_observation_ids: []
  temporary_supply_refs: []
  last_verified_at: null
```

Suggested availability:

- UNKNOWN
- NORMAL
- CONSTRAINED
- LIMITED
- TEMPORARY_SUPPLY
- INTERRUPTED
- RESTORING
- TESTING

A service sector is an operational scope, not a combat zone.

## 11. Service point

A service point may be a roadside outlet, institutional fueling point, heating-fuel handoff, industrial endpoint or other authored interface.

```yaml
fuel_service_point:
  service_point_id: null
  fuel_system_id: null
  location_id: null
  operator_ref: null
  supported_material_refs: []
  source_path_ids: []
  facility_dependency_refs: []
  storefront_or_service_ref: null
  current_supply_state: UNKNOWN
  current_operating_state: UNKNOWN
  latest_observation_refs: []
```

Hard separation:

`SUPPLY_AVAILABLE != SERVICE_POINT_OPERATING`.

A service point can have supply but be closed, inaccessible or technically unavailable. It can also be open while the relevant supply is unavailable.

## 12. Downstream consumer handoff

```yaml
fuel_downstream_handoff:
  handoff_id: null
  source_service_point_or_sector_id: null
  downstream_owner_system: null
  downstream_subject_id: null
  delivered_or_available_at: null
  material_scope_ref: null
  verification_refs: []
  owner_action_required: true
```

Examples:

- Infrastructure Outage receives evidence that backup-generation supply is available;
- Hospitality receives evidence that an authored heating fuel has arrived;
- Transport receives evidence relevant to an authored vehicle service;
- Manufacturing receives evidence that an input supply is available.

The downstream owner still decides whether its own service can operate.

`DELIVERED != DOWNSTREAM_SERVICE_READY`.

## 13. Shortage episode

```yaml
fuel_shortage_episode:
  shortage_id: null
  fuel_system_id: null
  first_observation_ids: []
  affected_sector_ids: []
  affected_service_point_ids: []
  suspected_cause_claim_ids: []
  confirmed_cause_refs: []
  active_allocation_refs: []
  temporary_supply_refs: []
  downstream_impact_refs: []
  recovery_checkpoint_ids: []
  current_state: UNCONFIRMED
```

Suggested states:

- UNCONFIRMED
- CONFIRMED_LOCAL
- CONFIRMED_MULTI_SECTOR
- BOUNDED
- MITIGATING
- RESTORING
- MONITORING
- CLOSED

The shortage record must keep cause claims separate from observations.

## 14. Temporary supply arrangement

```yaml
temporary_fuel_supply:
  temporary_supply_id: null
  fuel_system_id: null
  supported_sector_or_consumer_refs: []
  source_ref: null
  distribution_path_ref: null
  temporary_service_point_ref: null
  authorization_ref: null
  began_at: null
  review_at: null
  end_condition_refs: []
  current_state: PLANNED
  history_refs: []
```

States may include PLANNED, READY, ACTIVE_LIMITED, ACTIVE, CONSTRAINED, ENDING, ENDED, SUPERSEDED.

Temporary infrastructure can gain narrative identity without silently becoming permanent canon.

## 15. Recovery sequence

```yaml
fuel_service_recovery:
  recovery_id: null
  shortage_or_outage_ref: null
  prerequisite_refs: []
  accepted_supply_checkpoint_refs: []
  terminal_readiness_refs: []
  release_readiness_refs: []
  path_verification_refs: []
  sector_verification_refs: []
  service_point_verification_refs: []
  downstream_handoff_refs: []
  monitoring_refs: []
  current_stage: PLANNED
```

A useful generic sequence is:

supply available → receiving/terminal available → release authorized → path available → sector verified → service point verified → downstream owner checks its service.

No step may be skipped because a Minecraft prop changed appearance.

## 16. Legacy and decommissioned sites

```yaml
fuel_site_history_event:
  history_event_id: null
  facility_or_service_point_id: null
  event_type: null
  effective_at: null
  source_refs: []
  successor_use_refs: []
  environmental_handoff_refs: []
  public_memory_refs: []
```

Candidate event types:

OPENED, EXPANDED, CONSTRAINED, PARTIALLY_CLOSED, DECOMMISSIONED, CLEANUP_REFERRED, REPURPOSED, DEMOLISHED, PRESERVED.

Decommissioning does not prove cleanup, contamination, safety, access or demolition.

## 17. Ecology and environmental handoff

Fuel infrastructure may correlate with changed traffic, noise, light, water use, industrial remnants or contamination claims.

This layer may record a link to observations. It must not decide environmental causation.

If a spill, pollution or habitat issue is observed, hand it to the existing Pollution/Conservation systems with provenance intact.

## 18. Fire and safety handoff

A fuel facility can be the location of a fire or safety incident, but this layer does not simulate ignition, combustion, explosion, smoke, exposure or suppression.

If a fire is actually observed, Fire Response owns the incident.

If a work restriction, near miss or technical isolation is required, Worksite Safety and Facility/Technology own those states.

Fuel presence alone never creates a tactical hazard.

## 19. Pokémon involvement

```yaml
fuel_system_pokemon_assignment:
  assignment_id: null
  pokemon_id: null
  role_ref: null
  facility_or_service_point_refs: []
  task_scope_refs: []
  voluntary_state: UNKNOWN
  governing_capability_refs: []
  governing_move_refs: []
  governing_ability_refs: []
  governing_item_refs: []
  governing_feature_refs: []
  evidence_refs: []
  mechanical_validation_state: UNRESOLVED
```

Never infer competence from Type, species, appearance, animation or proximity.

A Fire-type does not automatically ignite fuel. A Water-type does not automatically suppress a fire. An Electric-type does not automatically power pumping or transfer equipment. A Pokémon able to carry something does not automatically have legal handling or work authority.

## 20. Provenance mysteries

Fuel service naturally creates apparently contradictory but simultaneously valid reports.

Examples:

- a terminal reports supply present while a service point reports unavailable;
- a driver reports a completed delivery while the downstream service remains offline;
- a reserve is physically present but already allocated;
- one neighborhood reports restored availability before another;
- an old map shows a depot that is now decommissioned or repurposed.

Resolve these through IDs, timestamps, scopes, handoff states and source evidence. Do not use a hidden truth score.

## 21. Encounter contract A — Fuel Depot Access Withdrawal

Narrative premise:

An operational incident has stopped transfer work. Workers and nonparticipants must withdraw while a separate hostile encounter blocks a reviewed access route.

Full intended version may include:

- multiple withdrawal/protection routes;
- Intercept and other forced movement where exact rules support them;
- generalized reaction windows;
- restricted technical zones;
- tactical AI that understands withdrawal and protection;
- semantic Minecraft/Cobblemon/Craftics playback.

If active fuel equipment, fire, fumes, spills or moving vehicles become mechanically relevant, the encounter additionally depends on exact governing PTU/Caelo rules and the `terrain/weather/hazards/zones/reactions` family. No generic fuel hazard may be invented.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL when exact legal effects are used
- terrain/weather/hazards/zones/reactions — BLOCKING for active technical/fuel hazards or generalized reactions
- move-specific behavior — PARTIAL as used
- abilities — PARTIAL as used
- items — PARTIAL as used
- Trainer Features/perks — PARTIAL as used
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

Stop and isolate fuel operations before battle. Evacuate workers, nonparticipant Pokémon, vehicles and handling equipment. Fuel assets remain outside BattleSpec or inert non-targetable scenery. Ouros selects combatants explicitly and gives AutoPTU a static reviewed access arena. Victory changes only immediate access/security state. Terminal verification and service recovery resume afterward in world state.

## 22. Encounter contract B — Delivery Yard Perimeter

Narrative premise:

An accepted distribution handoff is paused because the yard perimeter is contested. The cargo must not become a battle reward or target by implication.

Full intended version can require:

- route protection;
- withdrawal/escort behavior;
- Intercept/forced movement;
- generalized reactions;
- tactical AI;
- semantic playback;
- active vehicle/equipment zones only if governing rules exist.

Reduced version:

Freeze custody at the last verified external handoff. Keep cargo, drivers, workers, vehicles and transfer equipment outside the grid. Combat occurs in an adjacent static perimeter. Victory can permit the transport/storage owners to resume their workflow later. It does not load, unload, transfer custody, prove delivery or change allocation.

## 23. Encounter contract C — Isolated Service Point Diversion

Narrative premise:

A local service point has been isolated after an operational concern. A separate Pokémon conflict affects a safe approach while travelers are redirected elsewhere.

Full intended version can require:

- protect/withdraw objectives;
- multiple routes;
- generalized reactions;
- reviewed terrain or technical zones;
- objective-aware AI;
- adapter playback.

Reduced version:

Close the service point before combat. Move customers and staff away. Keep pumps, tanks, heating equipment or other fuel-specific assets mechanically inert. Battle occurs on reviewed nearby ground. Winning can secure access for a later inspection; it cannot reopen the service point or establish that supply is safe/available.

## 24. Immediate noncombat content available now

Without adding tactical rules, Ouros can use:

- stable fuel-system, terminal, depot and service-point IDs;
- accepted-supply handoffs;
- broad presence/availability observations;
- allocation/release provenance;
- path and sector states;
- local shortage observations;
- temporary supply arrangements;
- staged recovery checkpoints;
- decommissioning and repurposing history;
- downstream availability handoffs;
- contradictory reports resolved through scope and timestamps;
- ecology/pollution/fire/safety handoffs to existing owners;
- individual Pokémon work assignments with unresolved mechanical validation.

## 25. Minecraft/Cobblemon boundary

Safe presentation reuse can include:

- depot and service-point buildings;
- tanks, containers, pipes/hoses and pumps as visual props;
- signs, barriers, lights and status boards;
- vehicles as presentation assets when available;
- workers and travelers;
- Pokémon models, forms, poses, animations and cries;
- UI, networking, entity tracking and persistence hooks;
- decommissioned or repurposed industrial scenery.

The adapter must preserve stable narrative IDs and project authoritative service state.

Unsafe shortcuts:

- a tank block proving supply exists;
- a gauge texture creating quantity truth;
- redstone proving transfer or terminal readiness;
- a hose visually connected proving a handoff;
- an item entity entering a chest proving delivery;
- native Minecraft fire creating PTU Fire damage/Burn;
- native explosions creating PTU blast damage;
- smoke particles creating status penalties;
- flowing liquid applying forced movement;
- Cobblemon BattleState choosing combatants or outcomes;
- a nearby Pokémon gaining a job or mechanical effect by species/Type.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and results. Minecraft/Cobblemon/Craftics presents and plays back authorized state.

## 26. Canon questions intentionally left open

- Which regions use stored fuels at all?
- What kinds of fuel exist and for what purposes?
- Are systems centralized, local, imported, produced domestically or mixed?
- Which settlements have terminals, depots or small service points?
- What institutions operate them?
- Do any regions use heating-fuel delivery?
- What forms of transportation depend on fuel rather than Pokémon, electricity or another source?
- What emergency allocation authorities exist, if any?
- Which legacy industrial sites remain visible?
- What environmental histories are canon-approved?
- Which individual Pokémon have authored roles in fuel operations?

## 27. Mechanical questions intentionally unresolved

- Any exact PTU/Caelo rule for generic fuel handling.
- Fuel as a tactical Item or targetable object.
- Generic ignition, combustion, explosion or fumes.
- Spill movement or contamination effects.
- Heating/thermal exposure.
- Vehicle fuel consumption.
- Generator or machinery consumption.
- Move/Ability/Item/Trainer Feature interactions with fuel assets.
- Technical-object HP or destruction.
- Complete competing-reaction ordering.
- Objective-aware protection/withdrawal policy.
- Semantic Minecraft/Cobblemon/Craftics playback.

No answer is inferred until rules and implementation evidence support it.
