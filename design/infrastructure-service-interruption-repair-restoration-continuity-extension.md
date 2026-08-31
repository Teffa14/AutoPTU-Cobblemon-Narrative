# Ouros Infrastructure, Service Interruption, Repair & Restoration Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros persistent continuity for infrastructure and the services that depend on it without inventing a universal engineering simulator, utility law, repair skill or hazard engine.

It tracks what an asset is, what service it is authored to support, what interruption occurred, what was assessed, what temporary workaround exists, what repair was performed, and what scope of service was later restored.

The layer exists because physical condition, operational state and service consequence are different facts.

## Existing authority boundaries

Travel, Rail, Road, Aviation, Ports, Ferry, Ropeway and Transit systems own journeys, schedules, route use and transport service state inside their existing contracts.

Workplace systems own staff, assignments and ordinary job continuity.

Civic, Institutional, Credential and Adjudication systems own mandates, authorization, offices, inspections or approvals when canon has established them.

Material Culture owns physical item identity, components, custody and provenance.

Science, Environment, Water, Air, Weather and Conservation systems own observed environmental conditions and scientific interpretation within their scopes.

Emergency/Disaster systems own emergency episodes where they already exist.

Case and Investigation systems own evidence, causal claims and hypotheses.

AutoPTU owns tactical state and outcomes covered by BattleSpec and verified mechanics.

Minecraft/Cobblemon/Craftics owns presentation and playback only.

This extension owns longitudinal infrastructure/service continuity between those systems.

## Infrastructure asset record

```yaml
infrastructure_asset:
  asset_id: null
  canonical_name: null
  asset_type: null
  location_ref: null
  operator_or_caretaker_refs: []
  owner_claim_refs: []
  functional_role_refs: []
  service_dependency_ids: []
  component_refs: []
  current_condition: UNKNOWN
  current_operational_state: UNKNOWN
  commissioned_event_ref: null
  decommission_event_ref: null
  repurpose_event_refs: []
  provenance_refs: []
  chronicle_event_ids: []
  canon_status: proposed
```

Candidate asset types are descriptive only: GENERATION_SITE, SUBSTATION, PUMP, WATERWORK, BRIDGE, TUNNEL, SIGNAL_SITE, COMMUNICATION_RELAY, STATION, WORKSHOP, STORAGE_SUPPORT, ROAD_STRUCTURE, FIELD_STATION, OTHER_AUTHORED_ASSET.

Do not create gameplay statistics merely because an asset has a type.

## Condition and operation are separate axes

Candidate physical condition values:

- UNKNOWN
- INTACT
- DEGRADED
- DAMAGED
- PARTIALLY_REPAIRED
- REPAIRED
- REBUILT
- REMOVED

Candidate operational states:

- UNKNOWN
- OPERATIONAL
- DEGRADED_OPERATION
- INTERRUPTED
- ISOLATED
- UNDER_ASSESSMENT
- REPAIR_IN_PROGRESS
- TEMPORARY_OPERATION
- RESTORED_OPERATION
- DECOMMISSIONED
- REPURPOSED

Hard boundaries:

`ASSET_INTACT != OPERATIONAL`

`ASSET_DAMAGED != SERVICE_INTERRUPTED`

`ASSET_REPAIRED != OPERATIONAL`

`OPERATIONAL != FULL_CAPACITY`

`DECOMMISSIONED != DESTROYED`

`REPURPOSED != HISTORICAL_IDENTITY_ERASED`

## Authored service dependency

```yaml
service_dependency:
  dependency_id: null
  source_asset_ref: null
  dependent_service_or_location_ref: null
  dependency_type: null
  dependency_scope: null
  alternate_source_refs: []
  active_from: null
  active_until: null
  evidence_or_authority_refs: []
  canon_status: proposed
```

A dependency must be authored or established by evidence. Proximity is not enough.

`NEAR_ASSET != DEPENDS_ON_ASSET`

If an alternate source exists, an asset interruption does not automatically produce a downstream outage.

## Service interruption episode

```yaml
service_interruption:
  interruption_id: null
  affected_asset_refs: []
  affected_service_refs: []
  reported_start: null
  confirmed_start: null
  observed_scope_refs: []
  suspected_cause_refs: []
  confirmed_cause_refs: []
  alternate_service_refs: []
  status: OPEN
  provenance_refs: []
  chronicle_event_ids: []
```

Candidate states:

- REPORTED
- CONFIRMED
- PARTIAL
- WIDESPREAD
- STABILIZED
- TEMPORARILY_SERVICED
- RESTORATION_IN_PROGRESS
- RESTORED_WITH_LIMITATIONS
- RESTORED
- CLOSED

The words PARTIAL and WIDESPREAD describe authored scope, not automatic topology inference.

`OUTAGE_REPORTED != OUTAGE_SCOPE_PROVEN`

`SERVICE_INTERRUPTED != CAUSE_KNOWN`

`CAUSE_SUSPECTED != CAUSE_CONFIRMED`

## Condition assessment

```yaml
condition_assessment:
  assessment_id: null
  asset_ref: null
  assessor_refs: []
  assessment_time: null
  accessible_area_refs: []
  observation_refs: []
  inaccessible_area_refs: []
  condition_claim_refs: []
  recommended_action_refs: []
  qualification_or_authority_refs: []
  provenance_refs: []
```

An assessment records what was actually observable. It is not omniscient.

`ASSESSMENT_COMPLETE_FOR_ACCESSIBLE_AREA != ENTIRE_ASSET_KNOWN`

`TECHNICIAN_PRESENT != AUTHORIZED_TO_OPERATE`

`EXPERTISE_CLAIMED != QUALIFICATION_CANONIZED`

## Isolation and stabilization event

```yaml
infrastructure_stabilization_event:
  event_id: null
  asset_ref: null
  event_type: null
  affected_component_refs: []
  performed_by_refs: []
  start_time: null
  completion_time: null
  resulting_state_refs: []
  authority_or_work_order_refs: []
  provenance_refs: []
```

Candidate types:

- POWER_ISOLATION
- FLOW_ISOLATION
- ACCESS_CLOSURE
- SHORING
- TEMPORARY_BARRIER
- SAFE_STAGING_ESTABLISHED
- MANUAL_BYPASS
- OTHER_AUTHORED_STABILIZATION

These labels do not create technical mechanics. They record authored events.

`POWER_OFF != SAFE_TO_ENTER`

`ACCESS_CLOSED != STRUCTURE_UNSAFE`

`STABILIZED != REPAIRED`

## Work order

```yaml
infrastructure_work_order:
  work_order_id: null
  asset_ref: null
  requested_scope_refs: []
  requesting_actor_or_org_ref: null
  authorized_scope_refs: []
  assigned_actor_or_org_refs: []
  status: PROPOSED
  prerequisite_refs: []
  created_at: null
  authorized_at: null
  started_at: null
  completed_at: null
  acceptance_or_inspection_refs: []
  provenance_refs: []
```

Candidate states:

- PROPOSED
- REQUESTED
- AUTHORIZED
- SCHEDULED
- BLOCKED
- IN_PROGRESS
- WORK_REPORTED_COMPLETE
- INSPECTION_PENDING
- ACCEPTED
- CLOSED
- CANCELLED

`WORK_ORDER_EXISTS != WORK_STARTED`

`WORK_REPORTED_COMPLETE != WORK_ACCEPTED`

`WORK_ACCEPTED != SERVICE_RESTORED`

This extension does not invent who has authority to authorize or accept work.

## Repair episode

```yaml
repair_episode:
  repair_episode_id: null
  asset_ref: null
  work_order_ref: null
  repair_scope_refs: []
  component_refs: []
  technician_or_team_refs: []
  material_batch_refs: []
  start_time: null
  end_time: null
  observed_result_refs: []
  unresolved_issue_refs: []
  resulting_condition: null
  provenance_refs: []
```

Repair can alter the asset while leaving service interrupted.

`REPAIR_COMPLETE != SERVICE_RESTORED`

`PART_REPLACED != ROOT_CAUSE_SOLVED`

`VISIBLE_DAMAGE_FIXED != HIDDEN_DAMAGE_ABSENT`

## Temporary bypass or substitute service

```yaml
temporary_service:
  temporary_service_id: null
  interruption_ref: null
  substitute_asset_or_process_refs: []
  service_scope_refs: []
  capacity_or_limitation_claim_refs: []
  start_time: null
  expected_end_time: null
  actual_end_time: null
  operator_refs: []
  dependency_changes: []
  provenance_refs: []
```

Examples can include a generator, detour, temporary bridge, rented pump, alternate relay, manual dispatch process or reduced-capacity station configuration when those facts are authored.

`TEMPORARY_SERVICE != PERMANENT_REPAIR`

`TEMPORARY_SERVICE_ACTIVE != ORIGINAL_ASSET_OPERATIONAL`

`EXPECTED_END_TIME != ACTUAL_END_TIME`

A temporary workaround can become historically important without automatically becoming permanent infrastructure.

## Restoration event

```yaml
service_restoration_event:
  restoration_event_id: null
  interruption_ref: null
  restored_service_refs: []
  restoration_scope: null
  restoration_time: null
  source_asset_refs: []
  temporary_service_refs: []
  acceptance_or_verification_refs: []
  remaining_limitation_refs: []
  provenance_refs: []
```

Candidate scopes:

- TEST_SERVICE
- CRITICAL_ONLY
- PARTIAL
- REDUCED_CAPACITY
- FULL_AUTHORED_SCOPE
- TEMPORARY
- UNKNOWN

`SERVICE_RESTORED != ORIGINAL_CONFIGURATION`

`PARTIAL_RESTORATION != FULL_RESTORATION`

`RESTORED_TO_CRITICAL_USERS != RESTORED_TO_ALL_USERS`

A later event can upgrade the scope without rewriting earlier restoration history.

## Decommissioning and repurposing

```yaml
asset_transition_event:
  transition_id: null
  asset_ref: null
  transition_type: null
  effective_time: null
  prior_function_refs: []
  new_function_refs: []
  retained_component_refs: []
  removed_component_refs: []
  operator_change_refs: []
  authority_refs: []
  provenance_refs: []
```

Candidate types:

- DECOMMISSIONED
- MOTHBALLED
- PARTIALLY_ABANDONED
- REPURPOSED
- REBUILT_FOR_NEW_FUNCTION
- DEMOLISHED

`ABANDONED_IN_COMMON_SPEECH != OWNERLESS`

`OLD_MAP_FUNCTION != CURRENT_FUNCTION`

`DECOMMISSIONED != SAFE_FOR_PUBLIC_ACCESS`

## Player-facing presentation

A world-facing infrastructure panel may expose only discovered or public facts such as:

- service available / limited / interrupted;
- public closure;
- temporary route or substitute service;
- known repair stage;
- published restoration estimate if one exists;
- visible work activity;
- known historical function.

Do not expose hidden causes, secret component failure, unknown safety status, undiscovered dependencies or internal certainty scores.

## Chronicle events

Useful Chronicle facts include:

- `INFRA_ASSET_COMMISSIONED`
- `INFRA_SERVICE_INTERRUPTION_REPORTED`
- `INFRA_SERVICE_INTERRUPTION_CONFIRMED`
- `INFRA_ASSET_ISOLATED`
- `INFRA_ASSESSMENT_RECORDED`
- `INFRA_WORK_AUTHORIZED`
- `INFRA_REPAIR_STARTED`
- `INFRA_TEMPORARY_SERVICE_STARTED`
- `INFRA_REPAIR_REPORTED_COMPLETE`
- `INFRA_SERVICE_PARTIALLY_RESTORED`
- `INFRA_SERVICE_RESTORED`
- `INFRA_ASSET_DECOMMISSIONED`
- `INFRA_ASSET_REPURPOSED`

Every event keeps provenance and timestamps. Later corrections append rather than erase.

## Narrative invariants

`FACILITY_DAMAGED != SERVICE_INTERRUPTED`

`SERVICE_INTERRUPTED != CAUSE_KNOWN`

`ACCESS_CLEARED != REPAIR_COMPLETE`

`REPAIR_COMPLETE != SERVICE_RESTORED`

`SERVICE_RESTORED != ORIGINAL_CONFIGURATION`

`TEMPORARY_BYPASS != PERMANENT_REPAIR`

`MAP_MARKS_LINE != LINE_CURRENTLY_ACTIVE`

`DECOMMISSIONED != OWNERLESS`

`POWER_OFF != SAFE_TO_ENTER`

`WORK_ORDER_EXISTS != WORK_STARTED`

`OUTAGE_REPORTED != ALL_AFFECTED_USERS_KNOWN`

`BATTLE_WON != EQUIPMENT_FIXED`

`MOVE_USED_NEAR_INFRASTRUCTURE != REPAIR_AUTHORITY`

`MINECRAFT_BLOCK_CHANGED != OUROS_ASSET_STATE_CHANGED`

## Battle boundary

Infrastructure assets and semantic objectives remain outside BattleSpec unless an exact AutoPTU mechanic models the relevant object as a legitimate combatant/target under a verified contract.

Ouros decides the pre-battle infrastructure state and the explicit roster.

AutoPTU may return bounded tactical facts such as:

- `IMMEDIATE_SUBSTATION_APPROACH_CLEAR`
- `IMMEDIATE_PUMP_ACCESS_CORRIDOR_CLEAR`
- `IMMEDIATE_INSPECTION_STAGING_AREA_CLEAR`
- `IMMEDIATE_REPAIR_CONVOY_APPROACH_CLEAR`

Those facts do not authorize repair or restoration.

Minecraft/Cobblemon/Craftics may display already-decided blackout lighting, blocked routes, equipment models, work crews, temporary bypasses and later restored presentation. It cannot use redstone, entity AI, physics, lava, block destruction or Cobblemon battle state to decide infrastructure condition, hazard damage, restoration, combatants or PTU outcomes.

## Canon-status rule

All schemas and examples in this extension remain PROPOSED until a canon review adopts specific assets, institutions, dependencies, procedures or histories.

Research citations belong in the paired research scan. Canon files should reference approved facts rather than external research prose.