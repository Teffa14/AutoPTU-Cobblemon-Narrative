# Ouros Drinking-Water Treatment & Distribution Continuity Extension

Status: PROPOSED systems design. Not established canon.
Date: 2026-08-28
Research provenance: `research/2026-08-28-drinking-water-treatment-distribution-scan-107.md`

## Purpose

This extension gives Ouros persistent operational state for drinking-water treatment and delivery without creating a chemistry, plumbing or hydraulic simulator.

It starts only after an authored source-water handoff exists and ends at a service point or downstream-system handoff.

Existing systems retain authority:

- Water Management owns dams, reservoirs, source water, intakes, channels, diversions and managed raw-water operations.
- Waste/Sanitation owns wastewater, contamination observations, pollution-source claims and waste-treatment processes.
- Science/Care own their relevant testing, health interpretation and care consequences.
- Technology/Energy owns generic technical assets and technical repair dependencies.
- Facility Maintenance owns inspection, repair and work orders for physical assets.
- Infrastructure Outage owns multi-service cascade, fallback coordination and staged multi-network restoration.
- Civic/Public Works owns major public projects, funding and collective decisions.
- Public Notices / Communications own notices and message delivery.
- Residential, Hospitality, Care, Agriculture, Manufacturing, Fire Response and other downstream systems own what restored water availability means to their own service.

Drinking-Water Continuity owns the operational chain between those authorities: which treatment/distribution system exists, which authored stages are available, which paths are authorized, what service sectors are receiving supply, what verification supports the current state, and what fallback or restoration sequence is active.

## 1. Stable system identity

```yaml
drinking_water_system:
  drinking_water_system_id: null
  name_refs: []
  geographic_scope_ids: []
  source_water_handoff_ids: []
  treatment_facility_ids: []
  treated_storage_asset_ids: []
  distribution_node_ids: []
  service_sector_ids: []
  operator_institution_ids: []
  outage_dependency_refs: []
  historical_system_refs: []
  current_system_state: UNKNOWN
  last_verified_at: null
  canon_reference_ids: []
```

A system may outlive a treatment technology, operator, source or distribution layout. Never replace stable identity merely because the current arrangement changes.

Candidate system states are descriptive only:

- UNKNOWN
- NORMAL
- DEGRADED
- LIMITED
- ALTERNATE_SUPPLY
- PARTIALLY_OFFLINE
- OFFLINE
- RESTORING
- TESTING
- DECOMMISSIONED

These states do not imply health, chemistry or pressure values.

## 2. Source-water handoff

This extension never invents its own source-water truth.

```yaml
source_water_handoff:
  handoff_id: null
  drinking_water_system_id: null
  managed_water_system_ref: null
  source_connection_ref: null
  receiving_facility_id: null
  availability_state: UNKNOWN
  quality_observation_refs: []
  restriction_refs: []
  effective_from: null
  effective_until: null
  verified_at: null
```

Water Management remains authoritative for source availability and controlled connections.

A source-water handoff can be AVAILABLE while treatment remains OFFLINE. A treatment plant can be READY while the source handoff remains unavailable.

## 3. Treatment facility

```yaml
drinking_water_treatment_facility:
  treatment_facility_id: null
  drinking_water_system_id: null
  location_id: null
  maintenance_asset_refs: []
  source_handoff_ids: []
  authored_treatment_stage_ids: []
  treated_water_handoff_ids: []
  operator_institution_id: null
  operational_state: UNKNOWN
  current_restriction_ids: []
  verification_ids: []
  history_event_ids: []
  canon_reference_ids: []
```

Suggested operational states:

- UNKNOWN
- AVAILABLE
- LIMITED
- ISOLATED
- OUT_OF_SERVICE
- UNDER_MAINTENANCE
- TESTING
- RESTORING
- DECOMMISSIONED

Physical building access, asset condition, treatment operation and output verification remain separate.

## 4. Authored treatment stage

A real or fictional Ouros plant may have an ordered treatment sequence only when canon establishes it.

```yaml
drinking_water_treatment_stage:
  treatment_stage_id: null
  treatment_facility_id: null
  stage_order: null
  stage_role_description: null
  input_stage_or_handoff_ref: null
  output_stage_or_handoff_ref: null
  technical_asset_refs: []
  required_dependency_refs: []
  current_state: UNKNOWN
  bypass_authorization_refs: []
  verification_ids: []
  last_transition_at: null
```

Possible state vocabulary:

- UNKNOWN
- READY
- RUNNING
- LIMITED
- BYPASSED_AUTHORIZED
- PAUSED
- ISOLATED
- FAULTED
- UNDER_MAINTENANCE
- TESTING
- VERIFIED

The schema supports a stage description such as filtration or disinfection only if canon establishes that process at that facility. It does not prescribe a universal treatment train.

## 5. Treatment operation and verification

Planning, execution and output verification must remain separate.

```yaml
treatment_operation:
  treatment_operation_id: null
  treatment_facility_id: null
  applicable_stage_ids: []
  source_handoff_id: null
  authorized_by_refs: []
  planned_window: null
  execution_state: PLANNED
  started_at: null
  ended_at: null
  exception_refs: []
  output_handoff_id: null
  verification_ids: []
```

Suggested execution states:

- PLANNED
- READY
- RUNNING
- PAUSED
- INTERRUPTED
- PHYSICALLY_COMPLETE
- VERIFYING
- VERIFIED_FOR_HANDOFF
- NOT_VERIFIED
- CANCELLED
- SUPERSEDED

Critical rule:

`PHYSICALLY_COMPLETE != VERIFIED_FOR_HANDOFF`.

A machine animation, control-panel interaction, redstone change or visual color change can never skip verification.

## 6. Quality evidence boundary

This layer may hold references to quality evidence but does not invent laboratory truth.

```yaml
drinking_water_quality_clearance:
  clearance_id: null
  subject_ref: null
  intended_use_scope: null
  evidence_refs: []
  issuing_authority_ref: null
  issued_at: null
  valid_window: null
  clearance_state: UNKNOWN
  restriction_refs: []
```

Candidate states:

- UNKNOWN
- PENDING
- CLEARED_FOR_AUTHORED_USE
- RESTRICTED
- NOT_CLEARED
- SUPERSEDED
- EXPIRED

Science, Care, Sanitation or another canon-approved authority owns the underlying diagnosis/testing rules. This extension records the operational consequence for delivery.

Never infer safety from:

- clear appearance;
- blue Minecraft water;
- lack of odor;
- Pokémon drinking from it;
- Water-type presence;
- a functioning pump;
- a completed repair;
- a prior clearance outside its authored scope/window.

## 7. Treated-water handoff

```yaml
treated_water_handoff:
  treated_water_handoff_id: null
  treatment_facility_id: null
  receiving_storage_or_node_id: null
  operational_availability: UNKNOWN
  quality_clearance_ref: null
  effective_from: null
  effective_until: null
  verification_ids: []
```

The handoff is where treatment operation becomes eligible to feed distribution. It does not guarantee every downstream sector or endpoint.

## 8. Treated storage

```yaml
treated_water_storage_asset:
  storage_asset_id: null
  drinking_water_system_id: null
  location_id: null
  maintenance_asset_ref: null
  upstream_handoff_ids: []
  downstream_node_ids: []
  broad_availability_band: UNKNOWN
  broad_reserve_band: UNKNOWN
  quality_clearance_ref: null
  current_restriction_ids: []
  last_verified_at: null
```

Broad reserve bands may be used for continuity only:

- UNKNOWN
- LOW
- CONSTRAINED
- NORMAL_RANGE
- HIGH

They are not volume, pressure, duration or flow calculations.

A storage asset can contain water while distribution from it remains unavailable.

## 9. Distribution node and authored link

```yaml
drinking_water_distribution_node:
  node_id: null
  drinking_water_system_id: null
  node_type: null
  location_id: null
  technical_asset_refs: []
  upstream_link_ids: []
  downstream_link_ids: []
  operational_state: UNKNOWN
  last_verified_at: null
  restriction_ids: []
```

```yaml
drinking_water_distribution_link:
  link_id: null
  from_node_id: null
  to_node_id: null
  technical_asset_refs: []
  current_availability: UNKNOWN
  isolation_state: UNKNOWN
  verification_ids: []
  last_transition_at: null
```

Candidate node types are descriptive:

- TREATMENT_EXIT
- STORAGE
- PUMP_OR_TRANSFER_NODE
- DISTRIBUTION_JUNCTION
- SECTOR_ENTRY
- SERVICE_CONNECTION
- MONITORING_POINT
- TEMPORARY_CONNECTION

Do not infer hidden links because Minecraft pipes touch each other or because two facilities are nearby.

## 10. Distribution path

```yaml
drinking_water_distribution_path:
  path_id: null
  drinking_water_system_id: null
  source_handoff_or_storage_ref: null
  ordered_link_ids: []
  target_sector_ids: []
  authorization_refs: []
  current_state: UNKNOWN
  verification_ids: []
  supersedes_path_id: null
```

Possible states:

- UNKNOWN
- AVAILABLE
- LIMITED
- ISOLATED
- BLOCKED
- TESTING
- VERIFIED
- SUPERSEDED

A `VERIFIED` path says only that the authored path passed its defined operational verification. It does not certify each customer's endpoint.

## 11. Service sector

```yaml
drinking_water_service_sector:
  service_sector_id: null
  drinking_water_system_id: null
  geographic_scope_ids: []
  active_path_ids: []
  endpoint_ids: []
  dependent_system_refs: []
  supply_availability: UNKNOWN
  quality_clearance_ref: null
  restriction_ids: []
  fallback_supply_ids: []
  last_verified_at: null
```

Suggested supply states:

- UNKNOWN
- NORMAL
- DEGRADED
- INTERMITTENT
- LIMITED
- ALTERNATE_SUPPLY
- OFFLINE
- RESTORING
- TESTING

Do not collapse this into a global city water flag.

## 12. Service point / endpoint

```yaml
drinking_water_service_point:
  service_point_id: null
  service_sector_id: null
  location_or_facility_id: null
  endpoint_role: null
  owner_system_ref: null
  connection_state: UNKNOWN
  observed_delivery_state: UNKNOWN
  quality_clearance_ref: null
  last_observation_ids: []
  restriction_ids: []
```

A sector can be normal while one building endpoint is unavailable. A building can receive water while its own service remains restricted for another reason.

The downstream owner decides what that endpoint enables.

Examples:

- Care decides whether a clinic can resume a procedure.
- Hospitality decides which guest services return.
- Residential decides household utility state.
- Fire Response decides operational readiness of any authored firefighting-water dependency.
- Manufacturing decides whether a production process can resume.

## 13. Observations are scoped evidence

```yaml
drinking_water_service_observation:
  observation_id: null
  subject_ref: null
  observation_point_id: null
  observer_id: null
  observed_at: null
  observation_kind: null
  qualitative_value: null
  measured_value_ref: null
  evidence_refs: []
  confidence: UNKNOWN
```

Candidate kinds:

- DELIVERY_PRESENT
- DELIVERY_ABSENT
- DELIVERY_INTERMITTENT
- VISUAL_APPEARANCE
- ODOR_REPORT
- EQUIPMENT_RESPONSE
- STORAGE_STATE
- LEAK_OR_BREAK_OBSERVATION
- QUALITY_SAMPLE_REF
- ENDPOINT_FUNCTION

An observation is never a diagnosis. Different reports may all be correct when they refer to different locations or times.

## 14. Isolation event

```yaml
drinking_water_isolation_event:
  isolation_event_id: null
  affected_node_or_link_ids: []
  reason_claim_ids: []
  authorization_refs: []
  intended_scope_ids: []
  executed_at: null
  execution_state: PLANNED
  verification_ids: []
  release_event_id: null
```

Isolation can protect unaffected sectors while a local fault is assessed. The system must not infer actual hydraulic effects that were not authored and observed.

## 15. Temporary and alternate supply

```yaml
drinking_water_fallback_supply:
  fallback_supply_id: null
  supported_sector_or_endpoint_ids: []
  source_ref: null
  delivery_method_description: null
  intended_use_scope: null
  quality_clearance_ref: null
  activation_state: STANDBY
  activated_at: null
  deactivated_at: null
  capacity_band: UNKNOWN
  restriction_ids: []
  review_due_at: null
  history_event_ids: []
```

Possible states:

- STANDBY
- PREPARING
- ACTIVE
- ACTIVE_LIMITED
- UNAVAILABLE
- EXHAUSTED_OR_ENDED
- TESTING
- CLOSED

No litres, runtime or household allocation is invented.

A temporary distribution point can later become a remembered landmark or civic space without remaining an active utility asset.

## 16. Restoration sequence

```yaml
drinking_water_restoration_sequence:
  restoration_sequence_id: null
  incident_or_outage_ref: null
  drinking_water_system_id: null
  prerequisite_refs: []
  ordered_checkpoint_ids: []
  current_checkpoint_id: null
  fallback_refs: []
  blocked_by_refs: []
  status: PLANNED
```

Useful conceptual checkpoints:

1. source-water handoff available;
2. affected treatment assets isolated/repaired;
3. authored treatment stages operational;
4. treated-water handoff verified;
5. storage/distribution path available;
6. affected path tested/verified;
7. service sector verified;
8. endpoint or downstream-system handoff issued;
9. temporary supply reviewed/removed or retained by a new decision.

Not every system needs every checkpoint. Canon defines actual topology.

Critical separations:

`SOURCE_AVAILABLE != TREATMENT_AVAILABLE`

`TREATMENT_RUNNING != OUTPUT_VERIFIED`

`OUTPUT_VERIFIED != DISTRIBUTION_PATH_VERIFIED`

`PATH_VERIFIED != SECTOR_VERIFIED`

`SECTOR_VERIFIED != EVERY_ENDPOINT_READY`

`WATER_DELIVERED != DOWNSTREAM_SERVICE_RESUMED`

## 17. Restoration reports can disagree without anyone lying

A statement such as “water was back at 08:10” needs scope.

Possible legitimate timestamps include:

- treatment restarted;
- treated-water handoff passed verification;
- a storage asset began receiving supply;
- a sector received delivery;
- a particular service point first observed delivery;
- a quality restriction was lifted;
- a downstream facility resumed its own operation.

Store provenance and scope instead of forcing one timestamp into a universal truth field.

## 18. Legacy systems and place memory

A decommissioned treatment hall, pump house, storage tower, public tap, abandoned distribution corridor or old service point remains a world object.

Possible later roles:

- heritage/industrial-history site;
- wildlife habitat;
- workshop or storage reuse;
- emergency fallback connection;
- public landmark;
- research/inspection site;
- route landmark;
- source of obsolete maps and mistaken assumptions;
- location where older residents remember a prior service topology.

Recommissioning requires current inspection and verification. Historical operation never proves present usability.

## 19. Pokémon agency and utility work

Any Pokémon performing work needs individual identity, role/assignment and governing mechanical evidence when mechanics matter.

Never infer from species or Type that a Pokémon can:

- purify water;
- detect contamination;
- pump water;
- pressurize a network;
- operate valves;
- safely enter a treatment process;
- repair pipes;
- carry unlimited water;
- provide public service indefinitely.

Flavor, Pokédex text or an animation may inspire a candidate role. It cannot create a PTU rule.

## 20. Encounter contract — Treatment Plant Access Withdrawal

Narrative premise:

A treatment facility is isolated after a disturbance. Staff need a safe access corridor before inspection and verification can resume.

FULL intended version wants:

- multiple withdrawal/protection routes;
- Intercept and forced movement;
- generalized reactions around access control;
- reviewed technical/water-edge zones if governing mechanics exist;
- objective-aware AI;
- authoritative Minecraft/Cobblemon playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

REDUCED version:

Isolate the relevant treatment stages before combat. Evacuate operators, maintenance staff and nonparticipating Pokémon. Keep water-process equipment, chemical treatment, pumps and controls outside tactical interaction. AutoPTU receives explicit combatants in a reviewed dry access yard/corridor. Victory marks only the immediate access corridor secured. Inspection, repair, testing and output verification happen afterward under their owner systems.

## 21. Encounter contract — Service Reservoir Perimeter

Narrative premise:

A treated-water storage site needs inspection after a local incident, but wild Pokémon occupy the surrounding access route.

FULL intended version wants:

- route protection/withdrawal objectives;
- Intercept/forced movement;
- generalized reactions;
- elevation or water-edge terrain only when reviewed;
- possible equipment/restricted zones if rules exist;
- objective-aware AI;
- semantic playback.

Current profile: REDUCED.

REDUCED version:

Keep stored water, hatches, controls and technical equipment outside the BattleSpec. Treat the tank/reservoir itself as protected scenery. Battle occurs on stable adjacent ground. Victory permits the operator to attempt inspection later; it does not prove water quality, storage integrity, distribution availability or service restoration.

## 22. Encounter contract — Temporary Water Point Perimeter

Narrative premise:

An alternate distribution point is active during a localized outage. A separate Pokémon disturbance threatens access while residents and staff are present.

FULL intended version wants:

- civilian withdrawal/protection;
- route-control objectives;
- Intercept and complete forced movement;
- generalized reactions;
- objective-aware AI;
- adapter/playback;
- any spill/slip/vehicle/equipment zone only with exact governing mechanics.

Current profile: REDUCED.

REDUCED version:

Suspend public distribution before combat and evacuate residents, workers, containers and nonparticipants. Freeze the fallback-supply state during battle. AutoPTU resolves a conventional static encounter nearby. Winning can make the immediate approach safe; it cannot allocate water, certify it, complete distribution or decide when public service resumes.

## 23. Noncombat scenario — Five Taps, Three Stories

A district reports contradictory restoration experiences.

Playable sequence:

- collect timestamped observations from multiple service points;
- identify which service sectors and paths each point belongs to;
- distinguish supply absence from local endpoint failure;
- compare treatment/output verification with distribution restoration;
- find whether an alternate supply or old service connection explains one report;
- hand unresolved quality interpretation to its authoritative system;
- update the operational topology only when evidence supports it.

Possible resolution:

No witness lied. Two service points recovered through the primary path, one used a fallback, one had a local building fault, and one observation was made before the relevant sector verification.

## 24. Long-term arc support

A water-service arc should revisit the same assets and communities across time.

Possible sequence:

- establish ordinary public taps, facility dependencies and operator routines;
- introduce a local treatment or distribution limitation;
- activate a temporary supply arrangement;
- let the temporary arrangement create new social routines or a landmark;
- restore treatment before every endpoint recovers;
- revisit old reports during a later unrelated incident;
- discover that a retired connection, old pump house or former water point still matters culturally or operationally.

Do not represent this with a single `water_level` or `infrastructure_level` progression score.

## 25. Minecraft/Cobblemon authority boundary

Safe presentation candidates, subject to adapter/API review:

- treatment buildings and basins as geometry;
- storage towers/tanks;
- authored pipes, valves, pump buildings and service points as visual assets;
- public taps/fountains where canon supports them;
- barriers, notices and temporary distribution sites;
- workers and individually authored supporting Pokémon;
- sounds, particles, lights and control displays;
- Pokémon models, forms, poses, animations and cries;
- UI, networking, tracking and persistence hooks.

Adapter requirements include:

- stable system/facility/stage/node/link/sector/service-point IDs;
- authoritative state projection into block/entity presentation;
- reviewed world-to-AutoPTU arena conversion;
- persistence across unload/reload;
- semantic playback of battle results without granting battle authority to Cobblemon.

Minecraft/Cobblemon must never decide:

- that touching pipes create a distribution link;
- that flowing water proves service availability;
- that blue/clear water is potable;
- that a pump animation proves successful treatment or delivery;
- that redstone proves valve or network state;
- that a bucket or tank determines authorized quantity;
- that drinking applies healing;
- that dirty-looking water applies Poison or another status;
- that current or water blocks apply forced movement;
- that a Water-type Pokémon purifies water;
- that a Poison-type is safe in contamination;
- that nearby entities are workers or combatants;
- that Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or result.

Authority remains:

`Ouros world/water-service state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## 26. Canon-status policy

Everything in this extension is PROPOSED architecture.

The following remain UNKNOWN until separately approved:

- which Ouros settlements have centralized drinking-water systems;
- source types and source-to-system mappings;
- treatment technologies and stage sequences;
- operators and institutions;
- quality-clearance practices and intended-use categories;
- distribution topology;
- fallback arrangements;
- public access norms;
- technologies for storage/pumping/monitoring;
- legacy/decommissioned assets;
- Pokémon utility roles.

No example schema, state name or encounter establishes those facts.

## 27. Mechanical non-inference gates

Do not create any of the following without exact governing evidence:

- drinking-water healing;
- dehydration mechanics;
- contamination damage or Poison;
- pressure/flow arithmetic;
- pipe/tank HP;
- burst-pipe knockback;
- slip zones;
- current zones;
- drowning or suffocation;
- treatment chemistry effects;
- Water-type utility bonuses;
- Poison-type contamination immunity;
- Move-to-pumping or Move-to-purification conversion;
- Trainer Feature utility-operation checks;
- equipment collision/damage;
- automated Minecraft treatment.

Worldbuilding can progress while all of these remain unknown.