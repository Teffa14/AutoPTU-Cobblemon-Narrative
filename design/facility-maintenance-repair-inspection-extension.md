# Ouros Facility Maintenance, Repair & Inspection Extension

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models settlement infrastructure, civic public works, material provenance, staffing, technology, housing, crises and service availability. This extension adds a persistent operational lifecycle for facilities after they exist: condition observations, faults, assessments, work orders, dependencies, temporary restrictions, repairs, verification, reopening and deferred maintenance.

It is intentionally narrower than public works. It should make a clinic room, bridge section, shop premises, workshop, ferry landing, field station, storage building, shelter or other authored facility feel maintained over time without creating a universal construction simulator.

## 1. Facility asset

```yaml
facility_asset:
  facility_id: null
  location_id: null
  facility_type: authored
  operator_actor_or_institution_ids: []
  service_ids: []
  physical_condition: unknown
  operational_state: unknown
  access_state: normal
  known_fault_ids: []
  open_work_order_ids: []
  last_assessment_id: null
  temporary_overlay_ids: []
  dependency_ids: []
  history_event_ids: []
  canon_reference_ids: []
```

Suggested coarse physical conditions:
- UNKNOWN
- SOUND
- WORN
- DAMAGED
- HEAVILY_DAMAGED
- UNDER_REPAIR
- RESTORED

These are narrative state bands, not structural-engineering calculations.

Suggested operational states:
- OPERATING
- LIMITED
- CLOSED
- RELOCATED_TEMPORARILY
- WAITING_ON_DEPENDENCY
- UNDER_WORK
- VERIFYING
- REOPENING

Physical condition and operational state must remain separate.

## 2. Condition observation

```yaml
facility_condition_observation:
  observation_id: null
  facility_id: null
  observer_id: null
  observed_at: null
  area_ref: null
  observation_type: null
  description_claim_id: null
  evidence_refs: []
  immediate_restriction_recommended: false
  confidence: unknown
```

An observation is not automatically a diagnosis. “Water under the wall” is an observation. “The foundation is failing” is a technical claim that requires evidence or an authored specialist.

## 3. Fault record

```yaml
facility_fault:
  fault_id: null
  facility_id: null
  first_observed_at: null
  affected_area_refs: []
  suspected_cause_claim_ids: []
  confirmed_cause_claim_ids: []
  severity_band: unknown
  service_effect_ids: []
  access_effect_ids: []
  recurrence_count: 0
  related_prior_fault_ids: []
  assessment_ids: []
  status: open
```

Suggested statuses:
- OPEN
- UNDER_ASSESSMENT
- MONITORED
- TEMPORARILY_MITIGATED
- REPAIR_PLANNED
- REPAIRING
- VERIFYING
- RESOLVED
- ACCEPTED_DEFERRED
- ESCALATED

Cause remains separate from public belief or first impressions.

## 4. Assessment

```yaml
facility_assessment:
  assessment_id: null
  facility_id: null
  fault_ids: []
  assessor_ids: []
  authority_basis: authored
  observed_conditions: []
  evidence_refs: []
  diagnosis_claim_ids: []
  uncertainty_notes: []
  recommended_actions: []
  recommended_restrictions: []
  followup_trigger: null
```

The extension does not invent who is legally qualified to inspect a structure. Assessor roles and authority must come from canon, institutional state or explicit project data.

## 5. Work order

```yaml
maintenance_work_order:
  work_order_id: null
  facility_id: null
  fault_ids: []
  requested_by_ids: []
  coordinating_actor_ids: []
  work_type: null
  scope_refs: []
  dependency_ids: []
  required_material_instance_ids: []
  required_service_ids: []
  assigned_worker_ids: []
  access_restrictions: []
  temporary_service_plan_ids: []
  status: planned
  verification_requirements: []
  completion_event_id: null
```

Suggested work types:
- inspect;
- clean;
- service;
- repair;
- replace;
- reinforce;
- restore;
- relocate temporarily;
- decommission;
- monitor.

No work type implies a legal building-code category.

## 6. Dependency graph

A repair is generated only from real dependencies.

Examples:

```text
ferry landing repair
  -> requires route access
  -> requires work crew
  -> requires material delivery
  -> restricts boarding area
  -> creates temporary embarkation point if one exists
  -> may affect passenger-service state
```

```text
clinic room leak
  -> requires source assessment
  -> may require utility shutdown
  -> may relocate one service temporarily
  -> may require material replacement
  -> requires cleanup/verification before reopening
```

Dependencies may reference staffing, supply routes, public works, technology, transport, conservation or housing state.

## 7. Temporary mitigation

A workaround can reduce consequences without resolving the underlying fault.

```yaml
facility_mitigation:
  mitigation_id: null
  facility_id: null
  fault_ids: []
  action_refs: []
  start_time: null
  end_trigger: null
  service_state_effects: []
  access_state_effects: []
  unresolved_risk_notes: []
```

Examples include closing one room, moving a counter, rerouting entry, installing temporary barriers, shifting a service outdoors, adding monitoring or restricting capacity.

Temporary mitigation must not silently mark the fault resolved.

## 8. Maintenance overlay in Minecraft

A worksite is an overlay on an existing place.

```yaml
facility_work_overlay:
  overlay_id: null
  facility_id: null
  work_order_id: null
  visible_props: []
  closed_access_refs: []
  rerouted_access_refs: []
  temporary_npc_role_refs: []
  temporary_signage_refs: []
  temporary_service_refs: []
  active_from: null
  removal_trigger: null
```

Possible visible changes:
- barriers;
- scaffolding;
- boarded area;
- tarps;
- temporary supports;
- workbench or staged materials;
- rerouted door;
- temporary service desk;
- posted notice;
- changed lighting/power state;
- reopened area after verification.

Minecraft renders authoritative state. Block breakage by itself must not create or resolve structural faults.

## 9. Verification and reopening

```yaml
facility_verification:
  verification_id: null
  facility_id: null
  work_order_id: null
  verifier_ids: []
  evidence_refs: []
  requirement_results: []
  unresolved_items: []
  outcome: pending
  operational_state_after: null
```

Possible outcomes:
- PASS_FULL
- PASS_LIMITED
- NEEDS_MORE_WORK
- MONITOR
- REFER_FOR_REVIEW

Reopening can be partial. A repaired building may restore one service while another dependency remains unavailable.

## 10. Deferred maintenance

```yaml
deferred_maintenance_item:
  deferred_id: null
  facility_id: null
  fault_id: null
  deferral_reason_claim_ids: []
  current_mitigation_id: null
  review_trigger: null
  known_service_effects: []
  known_access_effects: []
  escalation_conditions: []
  status: active
```

Deferral creates future state rather than a hidden countdown to random failure. Escalation must come from explicit conditions or later observations.

## 11. Recurring maintenance without chore spam

Routine upkeep should compress.

Materialize a scene only when at least one meaningful decision exists, such as:
- which service remains open;
- whether to accept a temporary relocation;
- which dependency to solve first;
- whether evidence supports escalation;
- whether ecological timing changes the work plan;
- whether an old workaround is still acceptable;
- whether a recurring fault suggests a different cause;
- whether a repair creates a new access or service tradeoff.

Do not create quests for every cleaning cycle, inspection or consumable replacement.

## 12. Facility history

```yaml
facility_history_event:
  event_id: null
  facility_id: null
  event_type: null
  timestamp: null
  related_fault_ids: []
  related_work_order_ids: []
  state_before: null
  state_after: null
  public_record_ids: []
  player_involvement_refs: []
```

Useful event types:
- FAULT_REPORTED
- ACCESS_RESTRICTED
- SERVICE_LIMITED
- WORK_STARTED
- TEMPORARY_RELOCATION
- WORK_COMPLETED
- VERIFICATION_FAILED
- REOPENED
- RECURRING_FAULT
- DECOMMISSIONED
- REPLACED

History persists even when the physical overlay disappears.

## 13. Pokémon participation gate

Pokémon may participate in maintenance only when governing state supports the specific capability.

The generator must not infer:
- cutting from claws;
- lifting from body size;
- electrical work from Electric typing;
- welding from Fire typing;
- water pumping from Water typing;
- excavation from Ground typing;
- safe flight lifting from a Flying type;
- structural sensing from species flavor.

A legal Move, Ability, movement capability, authored profession relationship or explicit setting rule must support the task where mechanics matter.

Narrative observation can still show Pokémon nearby, assisting handlers or participating in nonmechanical routines when canon supports that role.

## 14. Boundary with civic public works

Use this extension when a facility already exists and the core issue is operational condition, upkeep, fault resolution or reopening.

Use `civic-governance-public-works-layer.md` when the decision is about a major future public change, major allocation, competing designs, land use, new facility construction, replacement policy or other collective choice requiring authored civic authority.

A maintenance fault may escalate into a public-works proposal if repair is no longer sufficient.

## 15. Boundary with crisis/recovery

Use `crisis-rescue-recovery-layer.md` while immediate safety, evacuation, search/rescue or disaster stabilization dominates.

Once the acute incident is stable, damaged facilities can emit fault/work-order objects here.

## 16. Boundary with commercial, residential and workplace systems

Commercial layer owns whether a shop can provide a service. This layer owns why the premises may be physically restricted and what repair work is active.

Residential layers own occupancy and household suitability. This layer owns a specific facility fault or repair if the home itself needs work.

Workplace layer owns staff roles and shifts. This layer can depend on those roles but does not grant professions or qualifications.

## 17. Encounter contract A — Active Worksite Collapse

Narrative premise:

A maintenance site becomes tactically dangerous while workers are present. The intended encounter focuses on opening safe routes, keeping combatants away from unstable areas and stopping a wild or hostile actor from worsening the situation.

Full-version dependencies:
- targeting / footprints / range / LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy / initiative;
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle where specific legal effects apply;
- terrain / weather / hazards / zones / reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter/playback.

Reduced version:

Evacuate all workers before tactical resolution. Freeze geometry and mark all unstable areas as nonparticipating narrative state rather than engine hazards. Run a static legal battle in the safe portion of the site. The authoritative result determines whether work resumes, remains suspended or escalates to another assessment.

## 18. Encounter contract B — Closed Utility Room Containment

Narrative premise:

A closed service room contains a Pokémon or hostile actor interfering with restoration. The objective in the full version may include containment, withdrawal routes and avoiding damage to active equipment.

Full-version dependencies include complete movement, terrain/hazards/zones/reactions, objective-aware tactical AI and adapter/playback in addition to the currently verified core targeting/movement/calculation/action-space families.

Reduced version:

Shut down the relevant service in narrative state. Remove noncombatants and dynamic equipment interactions. Instantiate a static room or adjacent safe arena and resolve only legal combatants. Service restoration happens afterward through facility state, not through invented combat-object rules.

## 19. Noncombat pattern — Recurring Fault Review

A facility has experienced the same symptom more than once.

Playable sequence:
1. compare current and historical observations;
2. check prior work orders and material provenance;
3. identify whether the previous repair addressed cause or symptom;
4. inspect staffing/supply/utility dependencies;
5. produce a new assessment or escalation recommendation;
6. update maintenance history.

This can run now because it is primarily evidence/world-state logic.

## 20. Canon and rules safeguards

Do not infer:
- property ownership;
- building-code jurisdiction;
- legal inspection authority;
- contractor licensing;
- warranties;
- negligence;
- criminal fault;
- repair prices;
- labor rates;
- exact structural calculations;
- mandatory repair deadlines;
- Pokémon labor legality;
- PTU mechanical bonuses from a repaired facility.

All such facts require canon or governing rule evidence.

## 21. Implementation value

The extension is immediately useful for persistent Minecraft worldbuilding because it creates visible intermediate states between “normal” and “rebuilt.” A route, clinic, shop, station, field base or residence can visibly carry repair history and service consequences while AutoPTU remains authoritative only for actual tactical rules.

Mechanically rich worksite battles must continue to use explicit full/reduced contracts until complete movement, hazards/reactions, tactical AI and adapter/playback are verified.