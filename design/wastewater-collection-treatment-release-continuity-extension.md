# Ouros Wastewater Collection, Treatment & Release Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon.
Date: 2026-08-28
Research provenance: `research/2026-08-28-wastewater-collection-treatment-release-continuity-scan-116.md`

## Purpose

This extension specializes the existing Waste, Sanitation, Recycling & Pollution layer for persistent sanitary-wastewater operations. It preserves authored collection networks, operational handoffs, treatment progress, verification, release history, temporary arrangements and restoration without creating a hydraulic, chemistry, disease or regulatory simulator.

The parent Waste/Sanitation layer remains authoritative for waste streams, contamination observations, pollution-source claims and generic sanitation incidents. This extension owns the detailed operational continuity of an authored wastewater system.

## Authority boundaries

Stormwater Continuity owns rainfall/runoff drainage, storm inlets, storm-drain paths, flood-control assets and local surface-water drainage.

Drinking-Water Continuity owns potable-water treatment and distribution.

Water Management owns rivers, reservoirs, canals and managed receiving-water systems.

Infrastructure Outage owns cross-service cascade, fallback coordination and multi-network restoration.

Facility Maintenance owns inspection, repair and work orders for physical assets.

Technology/Energy owns generic technical dependencies and power availability.

Waste/Sanitation/Pollution owns contamination observations, source claims, cleanup and waste-material lineage.

Conservation, Fisheries, Care, Food/Agriculture and other downstream systems own ecological, health and service consequences.

Public Notices / Communications own message publication and delivery.

Civic/Public Works owns major projects, policy decisions and long-term infrastructure changes.

## Stable system identity

```yaml
wastewater_system:
  wastewater_system_id: null
  name_refs: []
  geographic_scope_ids: []
  collection_sector_ids: []
  conveyance_link_ids: []
  lift_or_pump_station_ids: []
  treatment_facility_ids: []
  release_handoff_ids: []
  operator_institution_ids: []
  upstream_service_refs: []
  downstream_receiving_system_refs: []
  historical_system_refs: []
  current_system_state: UNKNOWN
  last_verified_at: null
  canon_reference_ids: []
```

Possible descriptive states:

- UNKNOWN
- NORMAL
- DEGRADED
- LIMITED
- PARTIALLY_OFFLINE
- TEMPORARY_CONFIGURATION
- OFFLINE
- RESTORING
- TESTING
- DECOMMISSIONED

These states never imply flow rate, capacity, treatment efficiency or environmental safety.

## Collection sector

```yaml
wastewater_collection_sector:
  collection_sector_id: null
  wastewater_system_id: null
  geographic_scope_ids: []
  source_connection_ids: []
  active_collection_path_ids: []
  lift_or_pump_station_ids: []
  operational_state: UNKNOWN
  overflow_observation_ids: []
  restriction_ids: []
  last_verified_at: null
```

A collection sector can be available while one source connection is isolated. A building can remain restricted after the sector has recovered for reasons owned by another system.

## Source connection

```yaml
wastewater_source_connection:
  source_connection_id: null
  collection_sector_id: null
  location_or_facility_id: null
  owner_system_ref: null
  receiving_link_ref: null
  connection_state: UNKNOWN
  isolation_refs: []
  observation_ids: []
  last_verified_at: null
```

Suggested states include UNKNOWN, AVAILABLE, LIMITED, ISOLATED, BLOCKED_OR_SUSPECTED, UNDER_MAINTENANCE, TESTING and VERIFIED.

The existence of a connection never proves that wastewater is currently moving through it.

## Authored conveyance link

```yaml
wastewater_conveyance_link:
  link_id: null
  wastewater_system_id: null
  from_node_ref: null
  to_node_ref: null
  link_form: authored_or_unknown
  maintenance_asset_ref: null
  current_availability: UNKNOWN
  obstruction_or_failure_observation_ids: []
  isolation_refs: []
  verification_ids: []
  last_transition_at: null
```

The system may author gravity sewer, force main, channel or another setting-appropriate form only when canon establishes it. Minecraft adjacency never creates topology.

## Collection path

```yaml
wastewater_collection_path:
  collection_path_id: null
  wastewater_system_id: null
  source_sector_or_connection_refs: []
  ordered_link_or_station_refs: []
  receiving_treatment_or_handoff_ref: null
  current_state: UNKNOWN
  authorization_refs: []
  verification_ids: []
  supersedes_path_id: null
```

Suggested states: UNKNOWN, AVAILABLE, DEGRADED, LIMITED, ISOLATED, BLOCKED, TEMPORARY, TESTING, VERIFIED and SUPERSEDED.

`COLLECTION_PATH_AVAILABLE != EVERY_SOURCE_CONNECTION_AVAILABLE`.

## Lift / pump station

```yaml
wastewater_lift_or_pump_station:
  station_id: null
  wastewater_system_id: null
  location_id: null
  upstream_link_ids: []
  downstream_link_ids: []
  maintenance_asset_refs: []
  power_dependency_ref: null
  current_state: UNKNOWN
  operating_record_ids: []
  verification_ids: []
  restriction_ids: []
```

Possible states: UNKNOWN, STANDBY, READY, RUNNING, LIMITED, FAULTED, ISOLATED, UNDER_MAINTENANCE, TESTING, VERIFIED and DECOMMISSIONED.

Critical boundary:

`PUMP_RUNNING != FLOW_PATH_VERIFIED`.

A running animation, powered block or redstone state cannot certify network operation.

## Treatment facility

```yaml
wastewater_treatment_facility:
  treatment_facility_id: null
  wastewater_system_id: null
  location_id: null
  incoming_handoff_ids: []
  authored_treatment_stage_ids: []
  output_handoff_ids: []
  residue_stream_refs: []
  maintenance_asset_refs: []
  operator_institution_id: null
  operational_state: UNKNOWN
  restriction_ids: []
  verification_ids: []
  history_event_ids: []
```

Suggested states: UNKNOWN, AVAILABLE, LIMITED, ISOLATED, OUT_OF_SERVICE, UNDER_MAINTENANCE, TESTING, RESTORING and DECOMMISSIONED.

The extension does not define a universal treatment train.

## Authored treatment stage

```yaml
wastewater_treatment_stage:
  treatment_stage_id: null
  treatment_facility_id: null
  stage_order: null
  stage_role_description: null
  input_ref: null
  output_ref: null
  technical_asset_refs: []
  dependency_refs: []
  current_state: UNKNOWN
  bypass_or_alternate_refs: []
  verification_ids: []
  last_transition_at: null
```

A stage name such as screening, settling or another process may appear only when canon establishes it at that facility. This schema never imports real treatment chemistry or efficiency.

## Treatment operation

```yaml
wastewater_treatment_operation:
  treatment_operation_id: null
  treatment_facility_id: null
  applicable_stage_ids: []
  incoming_handoff_ref: null
  execution_state: PLANNED
  started_at: null
  ended_at: null
  exception_refs: []
  output_handoff_ref: null
  verification_ids: []
```

Suggested states: PLANNED, READY, RUNNING, PAUSED, INTERRUPTED, PHYSICALLY_COMPLETE, VERIFYING, VERIFIED_FOR_HANDOFF, NOT_VERIFIED, CANCELLED and SUPERSEDED.

Critical boundary:

`WASTEWATER_RECEIVED != TREATMENT_COMPLETE != OUTPUT_VERIFIED`.

## Output verification

```yaml
wastewater_output_verification:
  verification_id: null
  subject_ref: null
  intended_handoff_scope: null
  evidence_refs: []
  issuing_authority_ref: null
  verified_at: null
  valid_window: null
  verification_state: UNKNOWN
  restriction_refs: []
```

Possible states: UNKNOWN, PENDING, VERIFIED_FOR_AUTHORED_HANDOFF, RESTRICTED, NOT_VERIFIED, SUPERSEDED and EXPIRED.

This record references evidence. It does not invent laboratory findings, contaminant thresholds or legal compliance.

## Release / receiving handoff

```yaml
wastewater_release_handoff:
  release_handoff_id: null
  wastewater_system_id: null
  treatment_or_bypass_source_ref: null
  receiving_system_ref: null
  receiving_location_ref: null
  authorization_state: UNKNOWN
  output_verification_ref: null
  effective_from: null
  effective_until: null
  observed_release_event_ids: []
  restriction_ids: []
```

Suggested authorization states: UNKNOWN, PENDING, AUTHORIZED_FOR_AUTHORED_SCOPE, RESTRICTED, NOT_AUTHORIZED, SUSPENDED and SUPERSEDED.

`OUTPUT_VERIFIED != RELEASE_HANDOFF_AUTHORIZED`.

`RELEASE_HANDOFF_AUTHORIZED != RELEASE_OBSERVED_COMPLETE`.

The downstream owner receives a handoff. Wastewater Continuity never directly writes habitat damage, illness, drinking-water contamination or fisheries closure.

## Overflow / bypass observation

```yaml
wastewater_overflow_or_bypass_observation:
  observation_id: null
  subject_system_or_asset_ref: null
  location_id: null
  observed_at: null
  observer_id: null
  observation_kind: null
  broad_extent_band: UNKNOWN
  evidence_refs: []
  suspected_pathway_refs: []
  possible_cause_claim_ids: []
  confirmed_cause_refs: []
  downstream_handoff_refs: []
  confidence: UNKNOWN
```

Candidate observation kinds: OVERFLOW_OBSERVED, BYPASS_REPORTED, BACKUP_OBSERVED, UNEXPECTED_RELEASE_OBSERVED, ODOR_REPORT, DISCOLORATION_REPORT and UNKNOWN_ANOMALY.

An observation is not a diagnosis.

`OVERFLOW_OBSERVED != CAUSE_CONFIRMED`.

`BYPASS_RECORDED != ENVIRONMENTAL_HARM_ESTABLISHED`.

## Monitoring coverage and gaps

```yaml
wastewater_monitoring_record:
  monitoring_record_id: null
  subject_ref: null
  monitoring_point_id: null
  observation_window: null
  evidence_refs: []
  coverage_state: UNKNOWN
  reported_operational_state: null
  gap_reason_ref: null
  supersedes_record_id: null
```

Possible coverage states: UNKNOWN, ACTIVE, PARTIAL, GAP, OFFLINE, RESTORED and NOT_APPLICABLE.

A monitoring gap remains `UNKNOWN_FOR_INTERVAL`. It does not prove normal operation or failure.

## Isolation event

```yaml
wastewater_isolation_event:
  isolation_event_id: null
  affected_asset_or_path_ids: []
  reason_claim_ids: []
  authorization_refs: []
  intended_scope_ids: []
  execution_state: PLANNED
  executed_at: null
  verification_ids: []
  release_or_reconnection_event_id: null
```

Isolation can protect the rest of an authored network while investigation or repair proceeds. No hydraulic effect is inferred beyond authored/observed state.

## Temporary routing / holding / service arrangement

```yaml
wastewater_temporary_arrangement:
  arrangement_id: null
  affected_sector_or_asset_ids: []
  arrangement_kind: authored
  temporary_asset_refs: []
  alternate_path_refs: []
  activation_state: PLANNED
  activated_at: null
  dependency_refs: []
  restriction_refs: []
  review_due_at: null
  deactivation_or_handoff_refs: []
  history_event_ids: []
```

Suggested states: PLANNED, READY, ACTIVE, ACTIVE_LIMITED, PAUSED, UNAVAILABLE, TESTING, DEACTIVATING and CLOSED.

No storage amount, pump rate or safe duration is invented.

## Restoration sequence

```yaml
wastewater_restoration_sequence:
  restoration_sequence_id: null
  incident_or_outage_ref: null
  wastewater_system_id: null
  affected_sector_ids: []
  prerequisite_refs: []
  ordered_checkpoint_ids: []
  current_checkpoint_id: null
  temporary_arrangement_refs: []
  blocked_by_refs: []
  status: PLANNED
```

Possible conceptual checkpoints, only where applicable:

1. affected area isolated and safe access established;
2. collection links/stations inspected;
3. failed physical asset repaired by Facility Maintenance;
4. power or other upstream dependency restored;
5. collection path tested and verified;
6. treatment stages returned to authored operation;
7. output verification completed for the intended handoff;
8. release/receiving handoff restored;
9. collection sector verified;
10. downstream owner systems review their own consequences;
11. temporary arrangements are removed, retained or converted by separate decision.

Critical separations:

`POWER_RESTORED != STATION_VERIFIED`

`REPAIR_COMPLETE != ASSET_VERIFIED`

`ASSET_VERIFIED != COLLECTION_PATH_VERIFIED`

`COLLECTION_PATH_VERIFIED != TREATMENT_VERIFIED`

`TREATMENT_VERIFIED != RELEASE_HANDOFF_RESTORED`

`NETWORK_VERIFIED != DOWNSTREAM_SYSTEM_RECOVERED`

## Provenance and apparently conflicting reports

A statement such as “the sewer was back at 11:20” needs a subject and scope.

Legitimate timestamps can include power restored, station restarted, link cleared, path verification, treatment restart, treatment verification, release-handoff restoration, sector verification or downstream facility reopening.

Store each observation independently. Do not overwrite history with a single recovery timestamp.

## Legacy network and place memory

Decommissioned pump houses, treatment galleries, old access shafts, abandoned links, former outfalls and retired temporary sites remain world objects.

They may later become habitat, research locations, industrial-history evidence, service passages, emergency fallback infrastructure, landmarks, archives problems or misunderstood map features.

Historical operation never proves present usability.

## Pokémon agency boundary

A Pokémon can be observed repeatedly inside or near infrastructure. A specific individual can hold a canon-approved work role. Neither fact creates unsupported mechanics.

Never infer from species, Type, Pokédex flavor or animation that a Pokémon can clear blockages, detect contaminants, process sewage, operate pumps, resist every contaminant, survive every confined environment, purify output or work indefinitely.

## Encounter contract — Lift Station Access Withdrawal

Narrative premise: a wastewater lift/pump station is already isolated after a disturbance. Staff must withdraw from the immediate access corridor before inspection can continue.

Full intended version may use moving withdrawal actors, Intercept, forced movement, generalized reactions, restricted technical zones, objective-aware AI and semantic playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if an exact legal environmental effect applies
- status lifecycle — PARTIAL if an exact legal condition applies
- terrain/weather/hazards/zones/reactions — BLOCKING for technical/wet/confined zones or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for withdrawal/protection objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version: complete staff withdrawal and station isolation before BattleSpec creation. Keep pumps, wet wells, wastewater, controls and technical machinery outside the grid. Use a reviewed static dry approach. Winning secures the immediate access only; it does not restart, repair or verify the station.

## Encounter contract — Treatment Gallery Perimeter

Narrative premise: a treatment facility needs one service corridor secured while operators keep the process isolated.

Full intended version becomes mechanically rich only if active treatment surfaces, machinery, liquids, barriers or timed technical changes affect battle state. Those effects require exact PTU/Caelo rules plus terrain/hazard/reaction, lifecycle, damage/status and adapter support as appropriate.

Reduced version: freeze treatment state before combat, evacuate operators and controlled material, make technical equipment inert scenery or exclude it, and use a static reviewed corridor. Victory cannot complete treatment, clear output or authorize release.

## Encounter contract — Outfall Inspection Diversion

Narrative premise: an inspection party is diverted by a territorial or hostile situation near an already restricted receiving-handoff access route.

Full intended version may require protection/escort policy, Intercept, forced movement, changing access zones, current or water-edge mechanics if explicitly authorized, generalized reactions and semantic playback.

Reduced version: finish the environmental restriction and inspection-party withdrawal before BattleSpec. Use stable dry ground away from active discharge or receiving water. Winning only makes the immediate perimeter available for later inspection.

## Immediately executable exploration — The Old Alignment Under the Market

A current utility map, a retired network plan and local staff terminology disagree about the name and path of an old sewer alignment beneath a redeveloped district.

The exploration uses stable access points, archive records, photographs, maintenance history, persistent IDs and actor testimony. It can execute with current world systems without dynamic flow, gas, disease, contamination or moving machinery.

The premise survives if no battle occurs.

## PTU/Caelo unknowns

Do not invent universal rules for wastewater current, drowning/suffocation, contamination damage, Poison, infection, gas exposure, low-oxygen effects, slippery cells, pump suction, pressure, moving machinery, confined-space penalties, treatment chemistry, sewer depth, automatic Poison/Water-type immunity, species-derived contamination detection or Move/Ability/Item/Trainer Feature-powered treatment.

Any future mechanical version must cite an exact governing rule and current engine contract for every permanent capability family involved.

## Minecraft/Cobblemon/Craftics boundary

Minecraft may present pipes, access covers, pump buildings, treatment structures, gates, control props, barriers, signage, water-like visuals, particles, sounds, NPC workers and Pokémon.

Visual pipe contact does not create network topology. Redstone does not prove a pump or treatment stage is operational. Water color does not prove contamination or safety. Native liquid flow does not create PTU forced movement. Minecraft drowning, poison, suffocation or fall damage does not substitute for AutoPTU. A door opening does not authorize access or release.

Ouros owns persistent world facts and selected combatants. AutoPTU owns tactical legality, positions, HP/status and outcome. The adapter only presents authoritative state.

## Canon promotion questions

Before any wastewater proposal becomes canon, decide which settlements have sewer systems, their authored technology and topology, operators, treatment facilities, receiving handoffs, combined/separate relationships with stormwater where applicable, access practices, temporary arrangements, legacy sites, public-information conventions and individual Pokémon roles.

Mechanical environmental effects remain a separate PTU/Caelo and implementation decision.