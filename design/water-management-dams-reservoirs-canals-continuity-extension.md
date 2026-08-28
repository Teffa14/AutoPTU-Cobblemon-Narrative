# Ouros Water Management, Dams, Reservoirs & Canals Continuity Extension

Status: PROPOSED systems design. Not established canon.
Date: 2026-08-28

## Purpose

This layer gives Ouros persistent operational state for managed freshwater systems without creating a hydraulic simulator.

It covers dams, reservoirs, intake points, channels, canals, gates, spillways, diversion structures, managed ponds and other water-control assets only where canon later establishes them.

Existing systems retain authority:

- Civic/Public Works owns project approval, funding and public decisions.
- Facility Maintenance owns condition, inspection, repair and work orders.
- Infrastructure Outage owns multi-service availability and restoration dependencies.
- Weather owns forecasts and observed weather conditions.
- Geology owns geological interpretation and ground conditions.
- Conservation and interspecies ecology own ecological interpretation.
- Agriculture owns crop/cultivation state and agricultural outcomes.
- Fisheries owns aquatic harvest and stewardship.
- Travel/Road Operations owns route consequences.
- Public Notices owns published notices/signage.
- Technology/Energy owns technical systems such as generation where applicable.

Water Management owns the operational state that connects those facts: what water-control asset exists, what operating configuration is authorized, what was actually executed, what was observed upstream/downstream, and what verification supports the current baseline.

## 1. Stable managed-water identity

```yaml
managed_water_system:
  water_system_id: null
  name_refs: []
  geographic_scope_ids: []
  source_waterbody_ids: []
  downstream_waterbody_ids: []
  asset_ids: []
  service_area_ids: []
  ecological_context_ids: []
  public_works_project_ids: []
  operator_institution_ids: []
  current_operating_regime_id: null
  history_event_ids: []
  canon_reference_ids: []
```

A system can exist before a current operator and survive changes of purpose.

## 2. Water-control asset

```yaml
water_control_asset:
  asset_id: null
  water_system_id: null
  asset_type: null
  location_id: null
  maintenance_asset_ref: null
  public_access_profile_ids: []
  controlled_connection_ids: []
  operational_state: UNKNOWN
  last_verified_at: null
  observation_ids: []
  restriction_ids: []
  canon_reference_ids: []
```

Candidate `asset_type` values are descriptive only:

- DAM
- WEIR
- INTAKE
- OUTLET
- GATE
- SPILLWAY
- CANAL_SEGMENT
- DIVERSION_CHANNEL
- DISTRIBUTION_BRANCH
- MANAGED_POND
- RESERVOIR_ACCESS_STRUCTURE
- MONITORING_POINT

Do not assume any type exists in canon merely because the schema supports it.

Suggested operational states:

- UNKNOWN
- AVAILABLE
- LIMITED
- RESTRICTED
- OUT_OF_SERVICE
- INSPECTION
- TESTING
- RESTORING
- DECOMMISSIONED

This describes operational usability, not structural condition.

## 3. Managed connection

```yaml
managed_water_connection:
  connection_id: null
  upstream_node_id: null
  downstream_node_id: null
  controlling_asset_ids: []
  intended_function_refs: []
  current_availability: UNKNOWN
  access_or_use_restriction_ids: []
  last_verified_at: null
```

This is a graph edge. It does not simulate litres per second.

## 4. Operating regime

```yaml
water_operating_regime:
  regime_id: null
  water_system_id: null
  valid_from: null
  valid_until: null
  authorization_refs: []
  target_state_refs: []
  scheduled_operation_ids: []
  ecological_constraint_refs: []
  service_constraint_refs: []
  supersedes_regime_id: null
  status: PROPOSED
```

Suggested status values:

- PROPOSED
- AUTHORIZED
- ACTIVE
- SUSPENDED
- SUPERSEDED
- CLOSED

An authorized regime may define broad goals such as maintain irrigation availability, preserve a minimum downstream connection, or keep a reservoir below a seasonal threshold. Exact numeric thresholds require canon/rules evidence.

## 5. Scheduled operation versus executed operation

Never collapse planning and execution.

```yaml
water_operation:
  operation_id: null
  regime_id: null
  asset_id: null
  planned_window: null
  intended_transition: null
  authorized_by_refs: []
  execution_state: PLANNED
  executed_at: null
  executor_ids: []
  resulting_asset_state: null
  evidence_refs: []
  exception_refs: []
```

Execution states:

- PLANNED
- READY
- DEFERRED
- CANCELLED
- EXECUTED
- PARTIAL
- FAILED
- VERIFYING
- CLOSED

A control-board command or Minecraft redstone change is not proof of execution unless the authoritative world-state transition records it.

## 6. Water-state observation

```yaml
managed_water_observation:
  observation_id: null
  water_system_or_asset_id: null
  observation_point_id: null
  observer_id: null
  observed_at: null
  observation_kind: null
  qualitative_state: null
  measured_value_ref: null
  evidence_refs: []
  confidence: UNKNOWN
```

Possible observation kinds:

- LEVEL
- FLOW_PRESENT
- FLOW_ABSENT
- LEAKAGE
- BLOCKAGE
- TURBIDITY_OR_APPEARANCE
- BANK_OR_CHANNEL_CONDITION
- WILDLIFE_USE
- ACCESS_CONDITION
- EQUIPMENT_RESPONSE

Narrative may store measurements when sourced. It should not invent conversion formulas or infer causes from one reading.

## 7. Water availability versus water quality

These remain separate.

```yaml
managed_water_service_state:
  service_state_id: null
  service_area_id: null
  availability: UNKNOWN
  quality_case_ref: null
  source_connection_ids: []
  fallback_ids: []
  observed_at: null
```

A canal can carry water that is unsuitable for a particular use. A supply can be clean but unavailable. Water quality diagnosis belongs to the relevant care/science/sanitation authority.

## 8. Reservoir continuity

```yaml
reservoir_state:
  reservoir_id: null
  water_system_id: null
  broad_level_band: UNKNOWN
  shoreline_access_state: null
  submerged_feature_refs: []
  habitat_context_ids: []
  current_restriction_ids: []
  last_observation_ids: []
```

Broad level bands may be used for narrative continuity:

- UNKNOWN
- VERY_LOW
- LOW
- NORMAL_RANGE
- HIGH
- VERY_HIGH

They are descriptive bands. They do not create mechanical depth, current or flood effects.

Changing level may expose or cover a shoreline feature only after an explicit world-state transition.

## 9. Diversion and temporary bypass

```yaml
water_diversion:
  diversion_id: null
  source_connection_id: null
  alternate_connection_ids: []
  reason_refs: []
  authorized_window: null
  current_state: PLANNED
  downstream_effect_observation_ids: []
  removal_or_review_due_at: null
  history_event_ids: []
```

A temporary bypass can outlive the incident that created it and become socially/ecologically significant. Removing it later can therefore create a new decision rather than an automatic cleanup step.

## 10. Ecological response is evidence, not a switch

Wild Pokémon presence, nesting, migration, feeding, spawning or avoidance near managed water can be recorded through existing wildlife/ecology systems.

Do not infer:

- motive from presence;
- population change from one encounter;
- ecological harm from one complaint;
- ecological success from one sighting;
- permission to operate/close an asset from wild Pokémon behavior alone.

The causal chain needs observations and review.

## 11. Agriculture integration

Agricultural sites may reference `water_system_id`, `connection_id` or service states through their existing `water_dependency_ids`.

Water Management can say that supply to an agricultural branch is AVAILABLE, LIMITED or OFFLINE.

Agriculture decides whether a cultivation cycle changes. Narrative must not apply automatic yield penalties or bonuses.

## 12. Infrastructure outage integration

A managed-water failure can become an infrastructure outage when it affects broader services. Use the existing outage layer for zone impact, fallback and restoration sequence.

Water Management remains the source for the exact managed-water operational edge.

Example:

`intake blocked -> branch connection unavailable -> agricultural service zone degraded -> greenhouse fallback activated`

Each arrow must reference an authored dependency edge.

## 13. Public works and maintenance integration

A new dam, canal or diversion requires Public Works approval if the canon treats it as a civic project.

Maintenance may repair a gate. Water Management does not mark the connection restored until operational verification succeeds.

Therefore:

`repair complete != operation verified != service restored != public restriction lifted`

## 14. Legacy infrastructure

A decommissioned channel or reservoir does not disappear.

Possible later uses:

- wildlife habitat;
- walking route;
- research site;
- emergency bypass;
- heritage landscape;
- informal crossing;
- agricultural drainage;
- settlement boundary;
- archaeological or industrial-history evidence.

Recommissioning requires review of current conditions and accumulated uses.

## 15. Information and provenance

Posted schedules, old maps, maintenance logs, operator statements and downstream observations are information sources. They can disagree.

Use timestamps and provenance instead of a hidden truth score.

A mystery may legitimately end with a bounded uncertainty such as “the gate command was issued, but no surviving observation proves when downstream flow resumed.”

## 16. Encounter contract — Gatehouse Withdrawal

Narrative premise:
A managed-water facility must be cleared after a wild disturbance while staff protect access to the control building.

FULL version wants:

- multiple withdrawal routes;
- Intercept and forced movement;
- route protection/denial;
- meaningful restricted zones if rules support them;
- possibly water-edge or machinery hazards;
- objective-aware AI;
- authoritative adapter/playback.

Capability dependencies:

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
Suspend all gate operations first. Evacuate workers and ordinary residents. Keep controls, gates and water outside tactical interaction. Use a static dry arena with only explicitly selected participants. AutoPTU resolves battle; Water Management later decides whether testing can resume.

## 17. Encounter contract — Canal Service Path Conflict

Narrative premise:
A maintenance crew cannot reach a blocked canal segment because territorial wild Pokémon are occupying the service approach.

FULL version wants route-clearing/withdrawal objectives, possible narrow-path zones, Intercept/forced movement and tactical AI that values access rather than KO.

Current profile: REDUCED.

REDUCED version:
Close the affected canal segment in world state. Workers stay outside combat. The tactical arena is a static adjacent clearing or dry service path. Victory can make the approach temporarily safe; it does not remove the blockage, repair the channel or restore supply.

## 18. Encounter contract — Emergency Diversion Perimeter

Narrative premise:
A temporary diversion is active during an incident and staff must keep an access corridor clear while noncombat water operations continue elsewhere.

FULL version wants:

- route-control/protection objectives;
- reactions and complete movement;
- potentially dynamic water/weather/hazard zones;
- tactical AI;
- adapter/playback.

Current profile: REDUCED.

REDUCED version:
Execute or suspend the diversion before combat as an authoritative world-state action. Keep water, pumps, gates, staff and equipment outside the grid. Battle occurs on stable nearby terrain. The result cannot change diversion state automatically.

## 19. Minecraft/Cobblemon authority boundary

Safe presentation candidates, subject to API review:

- reservoirs and canals as world geometry;
- water blocks and visual level bands;
- gates, sluices, fences and signs;
- particles, sounds and weather presentation;
- Pokémon overworld entities, models, forms, poses and cries;
- UI, networking, tracking and synchronization.

Adapter-required functions include:

- binding world locations to stable water-system and asset IDs;
- projecting authoritative closures/restrictions into barriers/signage;
- representing an authoritative broad reservoir state without letting block state become source-of-truth;
- mapping reviewed dry geometry into AutoPTU cells;
- maintaining identity across unload/reload.

Minecraft/Cobblemon must never decide:

- whether a gate operation succeeded;
- actual service restoration from redstone/block state;
- combatants from nearby entities;
- PTU HP/status/position;
- current/flood/drowning damage;
- forced movement from visual water;
- ecological causation;
- project approval;
- battle outcome;
- reopening.

Authority remains:

`Ouros managed-water/world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## 20. Canon-status policy

Everything in this extension is PROPOSED architecture.

Concrete dams, reservoirs, canals, institutions, operating standards, water rights, hydropower, irrigation customs and regional technologies remain UNKNOWN until separately canon-approved.

No rule or setting fact becomes canon by appearing in an example schema.