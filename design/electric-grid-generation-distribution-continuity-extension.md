# Ouros Electric Grid Generation & Distribution Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Date: 2026-08-28

## Purpose and authority boundary

This document specializes the POWER-network portion of `technology-energy-infrastructure-layer.md`. It does not create a second technology, maintenance, outage, public-works, finance or crisis system.

Technology/Energy remains authoritative for technical assets, generic faults, controls, maintenance dependencies and machine/Pokémon interaction. Infrastructure Outage remains authoritative for multi-service incident propagation and recovery consequences. Facility Maintenance owns repair work. Civic/Public Works owns proposals, authorization structures and new construction where applicable. This extension preserves the operational electrical topology and the evidence that a particular source, path or service sector has actually returned.

No electrical engineering arithmetic or PTU damage rule is invented here.

## 1. Persistent power system

```yaml
power_system:
  power_system_id: null
  geographic_scope_ids: []
  operator_institution_ids: []
  generation_source_ids: []
  node_ids: []
  link_ids: []
  service_sector_ids: []
  authored_normal_path_ids: []
  alternate_path_ids: []
  active_restoration_sequence_ids: []
  current_operational_summary: unknown
  history_event_ids: []
  canon_reference_ids: []
```

The record describes authored topology at narrative resolution. It is not a load-flow model.

## 2. Generation source

```yaml
generation_source:
  source_id: null
  technical_asset_id: null
  site_id: null
  operator_id: null
  source_type: authored
  physical_state: unknown
  operating_state: unknown
  network_connection_state: unknown
  availability_state: unknown
  active_fault_ids: []
  maintenance_ids: []
  test_record_ids: []
  downstream_path_ids: []
  evidence_ids: []
```

Important separation:

`RUNNING != AVAILABLE_TO_NETWORK`.

A machine can be visually active while isolated, testing, disconnected or otherwise unavailable to downstream service.

## 3. Electrical node

```yaml
electrical_node:
  node_id: null
  technical_asset_id: null
  node_type: authored
  location_id: null
  connected_link_ids: []
  served_sector_ids: []
  current_state: unknown
  isolation_state: unknown
  access_state: unknown
  last_verified_at: null
  evidence_ids: []
```

Candidate descriptive node roles may include generation interface, distribution junction, substation, switching point, local service node or backup interface. These labels create no mechanical electrical behavior.

## 4. Authored electrical link

```yaml
electrical_link:
  link_id: null
  from_node_id: null
  to_node_id: null
  corridor_location_ids: []
  technical_asset_ids: []
  normal_role: null
  current_state: unknown
  isolation_state: unknown
  active_fault_ids: []
  inspection_record_ids: []
  verification_record_ids: []
  evidence_ids: []
```

Suggested readable states:

- AVAILABLE
- DEGRADED
- ISOLATED
- UNDER_INSPECTION
- UNDER_REPAIR
- TESTING
- UNAVAILABLE
- DECOMMISSIONED
- UNKNOWN

Minecraft cable geometry never creates or deletes a link record.

## 5. Service sector

```yaml
power_service_sector:
  sector_id: null
  geographic_scope_ids: []
  downstream_service_ids: []
  normal_path_ids: []
  current_supply_path_id: null
  current_supply_state: unknown
  restriction_state: none
  priority_claim_ids: []
  last_verified_at: null
  observation_ids: []
  evidence_ids: []
```

Suggested states:

- NORMAL
- ALTERNATE_SUPPLY
- DEGRADED
- INTERMITTENT
- EMERGENCY_ONLY
- UNSUPPLIED
- VERIFYING
- UNKNOWN

A sector state is scoped. One restored street does not prove settlement-wide restoration.

## 6. Power observation

```yaml
power_observation:
  observation_id: null
  observer_id: null
  observed_at: null
  scope_type: null
  scope_id: null
  observation_type: null
  observed_value_or_description: null
  instrument_or_visual_ref: null
  confidence_band: null
  interpretation_claim_ids: []
  superseded_by_id: null
```

Possible observations include lights visible, equipment running, local loss of service, operator indicator, instrument result or downstream service report.

Observation remains separate from diagnosis and topology truth.

## 7. Isolation and switching record

Narrative state may need to record that authorized operators changed topology without teaching real-world switching procedures.

```yaml
power_switching_record:
  switching_record_id: null
  operator_actor_ids: []
  authority_ref_ids: []
  affected_node_or_link_ids: []
  intended_state_change: null
  requested_at: null
  executed_at: null
  execution_state: planned
  verification_required: true
  verification_record_ids: []
  abort_reason_ids: []
  evidence_ids: []
```

Lifecycle:

`PLANNED -> AUTHORIZED -> EXECUTED -> VERIFYING -> VERIFIED`

Branches may include `ABORTED`, `FAILED_VERIFICATION` or `SUPERSEDED`.

The record never exposes procedural instructions for operating real electrical equipment.

## 8. Verification record

```yaml
power_verification:
  verification_id: null
  subject_type: null
  subject_id: null
  verification_scope: null
  performed_by_ids: []
  observed_at: null
  prerequisite_record_ids: []
  result: unknown
  limitation_notes: []
  downstream_check_ids: []
  evidence_ids: []
```

Possible results:

- PASSED
- PASSED_WITH_LIMITATIONS
- FAILED
- INCONCLUSIVE
- NOT_PERFORMED

`REPAIR_COMPLETE != VERIFIED`.

`ENERGIZED != VERIFIED`.

`SECTOR_VERIFIED != DOWNSTREAM_SERVICE_READY`.

## 9. Restoration sequence

```yaml
power_restoration_sequence:
  restoration_id: null
  incident_id: null
  affected_system_id: null
  stage_ids: []
  current_stage_id: null
  priority_claim_ids: []
  temporary_supply_ids: []
  alternate_path_ids: []
  blocked_dependency_ids: []
  verification_ids: []
  public_information_packet_ids: []
  started_at: null
  completed_at: null
```

Candidate abstract stages:

- ASSESS
- ISOLATE
- REPAIR_OR_BYPASS
- VERIFY_ASSET
- AUTHORIZE_ENERGIZATION
- ENERGIZE_SCOPED_PATH
- VERIFY_PATH
- VERIFY_SECTOR
- CHECK_DOWNSTREAM_SERVICES
- RETURN_TO_NORMAL

These are narrative continuity stages, not real electrical operating instructions.

## 10. Temporary and alternate supply

```yaml
temporary_power_supply:
  temporary_supply_id: null
  source_asset_id: null
  supported_sector_or_service_ids: []
  location_id: null
  activation_state: null
  availability_window: null
  limiting_dependency_ids: []
  operator_ids: []
  verification_ids: []
  retirement_state: active
  history_event_ids: []
```

Temporary supply can become socially persistent even after technical retirement. The physical asset, location, memory and later planning references can survive independently.

## 11. Restoration priorities remain authored claims

This extension can store a priority decision but does not invent who has authority or what must be prioritized.

```yaml
power_restoration_priority_claim:
  claim_id: null
  decision_authority_ref: null
  affected_service_ids: []
  stated_priority_order: []
  rationale_claim_ids: []
  effective_window: null
  evidence_ids: []
```

Civic/Governance, Crisis or institution-specific canon owns the decision authority.

## 12. Legacy and decommissioned topology

Old infrastructure keeps history.

```yaml
legacy_power_topology_record:
  legacy_record_id: null
  former_asset_or_link_ids: []
  former_service_sector_ids: []
  decommissioned_at: null
  known_residual_connection_claim_ids: []
  current_land_use_ids: []
  ecology_link_ids: []
  heritage_or_memory_ids: []
  inspection_ids: []
  current_electrical_state: unknown
```

A drawn line on an old plan does not prove a live connection. A decommissioned corridor may become habitat, public space or industrial heritage without losing provenance.

## 13. Cross-system consequences

This layer can emit scoped state to existing systems:

- Communications may lose or regain a relay dependency;
- Care may regain refrigeration or facility power;
- Transit may regain station systems;
- Manufacturing may move from OFFLINE to TESTING;
- Hospitality or Commercial Services may resume only selected functions;
- Water/Waste systems may recover pumps or treatment assets;
- Public Notices may publish a restoration update;
- Crisis may retire an emergency workaround.

Each downstream system still performs its own readiness check.

## 14. Pokémon participation boundary

```yaml
power_pokemon_role_observation:
  pokemon_id: null
  institution_id: null
  assigned_role_description: null
  observed_task_ids: []
  voluntary_state: unknown
  governing_capability_refs: []
  governing_move_refs: []
  governing_ability_refs: []
  governing_item_refs: []
  evidence_ids: []
  mechanical_validation_state: unresolved
```

Never infer that Electric type, Levitate, an animation or species flavor authorizes generation, switching, sensing, electrical immunity, maintenance or repair.

## 15. Minecraft/Cobblemon boundary

Minecraft/Cobblemon may present:

- generation buildings;
- substations and fenced compounds;
- lines/cables as scenery or mapped assets;
- control-room visuals;
- status lamps and displays;
- temporary generators;
- barriers and work zones;
- technicians;
- Pokémon models/forms/poses/animations/cries;
- sounds and particles;
- UI, networking, tracking and persistence hooks.

Authoritative flow remains:

`Ouros power/world state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Minecraft redstone continuity does not prove service. A lit lamp does not verify a sector. Native lightning, fire, contact damage or collision do not become PTU effects automatically. Cobblemon BattleState/controller logic never selects combatants or owns legality, HP/status, positions or result.

## 16. Encounter concept — Substation Access Withdrawal

Narrative premise: a technical site has already been isolated after an abnormal condition, but a wild or hostile subgroup occupies the external access route while operators need to inspect the perimeter.

FULL intended version:

- multiple withdrawal/protection routes;
- explicit technician-safe corridor objective;
- Intercept and other forced-movement interactions around chokepoints;
- generalized reactions;
- optional authored technical hazard zones only if exact PTU/Caelo mechanics exist;
- objective-aware AI;
- semantic playback.

Permanent dependency categories:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for any live technical/electrical zone or generalized reaction;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

REDUCED version:

The electrical site is isolated before battle. Operators, controls and equipment remain outside BattleSpec. Ouros selects explicit combatants and AutoPTU receives a reviewed static access road/yard. Victory only secures immediate access; Technology/Maintenance/Power Grid perform inspection and verification afterward.

## 17. Encounter concept — Alternate Supply Perimeter

Narrative premise: a temporary supply asset is supporting a limited public service while unrelated conflict or territorial Pokémon activity develops nearby.

FULL intended version:

- protect/withdraw objective around a defined perimeter;
- route control;
- generalized reactions and complete forced movement;
- possible weather/technical zones only with exact mechanics;
- objective-aware AI;
- playback that keeps the temporary asset visually synchronized without granting Minecraft authority.

REDUCED version:

The supply asset and technicians stay outside the tactical grid. Battle occurs on a static neighboring space. Power state is frozen during combat. Victory never changes supply capacity, fuel, service priority or verification state.

## 18. Encounter concept — Legacy Corridor Inspection

Narrative premise: an old mapped connection may still matter to a restoration plan, but the corridor has become habitat and its current physical/electrical state is uncertain.

FULL intended version:

- several approach/withdrawal paths;
- territorial or escape behavior rather than mandatory KO;
- reviewed terrain or environmental zones;
- reactions/forced movement where appropriate;
- objective-aware AI;
- playback.

REDUCED version:

Electrical truth remains UNKNOWN during battle. Inspection happens after a static encounter or noncombat wildlife resolution. No old cable, pylon or block becomes energized, dangerous or mechanically active by inference. Winning does not prove the legacy link exists or is usable.

## 19. Immediate narrative readiness

Usable now without new battle mechanics:

- persistent power-system/source/node/link/sector identity;
- scoped outage and restoration claims;
- source-running versus network-available separation;
- repair versus verification separation;
- path versus sector versus downstream-service verification;
- alternate/temporary supply history;
- versioned field observations;
- legacy/decommissioned topology;
- staged restoration records;
- contradictory reports resolved by scope/timestamp rather than hidden truth scores;
- recurring operator teams and institutional memory;
- cross-system consequences without automatic downstream restoration.

## 20. Canon questions left open

- What power-generation arrangements exist in each Ouros region?
- Which settlements share grids or operate independently?
- Which operators and institutions exist?
- Which restoration-priority rules exist, if any?
- Which legacy sites and corridors are canon?
- What access/privacy rules apply to technical records?
- Which Pokémon individuals participate in power-system work?
- Which world technologies are visible in Minecraft?

## 21. Mechanical questions left open

- exact PTU/Caelo Skill/Capability/Move/Ability/Item/Trainer Feature support for any electrical task;
- legal environmental electricity damage/status, if any;
- electrical equipment as tactical objects;
- technical work-zone hazards;
- objective-aware withdrawal/protection policy;
- complete competing-reaction behavior;
- semantic adapter representation of technical state;
- persistence of any battle-adjacent technical object across unload/save/load.

No answer is invented by this extension.
