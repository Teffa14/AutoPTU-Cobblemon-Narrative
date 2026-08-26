# Ouros Infrastructure Outage & Restoration Extension

Status: proposed systems design. Not established canon.

## Purpose

`technology-energy-infrastructure-layer.md` already owns technical assets, networks, faults, maintenance, fallback plans and technical operations. `facility-maintenance-repair-inspection-extension.md` owns condition assessment and work orders for individual facilities. `civic-governance-public-works-layer.md` owns major collective decisions and new works.

This extension covers a narrower operational gap: multi-service outages and recovery. It records what area lost service, which dependency edges caused the loss, what backups are active, which downstream services are affected, what restoration sequence is possible, and what must be verified before normal operation is declared.

It should make outages legible and persistent without turning Ouros into a real-time utility simulator.

## 1. Service zone

```yaml
infrastructure_service_zone:
  zone_id: null
  network_id: null
  geographic_scope_ids: []
  source_node_ids: []
  distribution_node_ids: []
  dependent_service_ids: []
  critical_dependency_refs: []
  fallback_refs: []
  current_availability: unknown
  current_incident_ids: []
  last_verified_at: null
  canon_reference_ids: []
```

Suggested availability bands:
- UNKNOWN
- NORMAL
- DEGRADED
- INTERMITTENT
- BACKUP_ONLY
- PARTIAL
- OFFLINE
- RESTORING
- TESTING

These bands describe service availability. They do not describe physical condition of every asset in the zone.

## 2. Dependency edge

```yaml
infrastructure_dependency_edge:
  edge_id: null
  upstream_id: null
  downstream_id: null
  dependency_type: authored
  minimum_condition: null
  fallback_refs: []
  observed_effect_when_lost: []
  verification_refs: []
  canon_reference_ids: []
```

A dependency may be:
- essential for any operation;
- essential only for full capacity;
- replaceable by a fallback;
- dependent on staffing or material supply as well as infrastructure.

Do not infer edges simply because two facilities are nearby.

## 3. Outage incident

```yaml
infrastructure_outage_incident:
  outage_id: null
  first_observed_at: null
  reporting_observation_ids: []
  affected_zone_ids: []
  suspected_origin_ids: []
  confirmed_origin_ids: []
  affected_dependency_edge_ids: []
  current_extent_state: unconfirmed
  isolation_event_ids: []
  backup_activation_ids: []
  downstream_impact_ids: []
  restoration_plan_id: null
  verification_ids: []
  closed_at: null
```

Suggested extent states:
- UNCONFIRMED
- CONFIRMED_LOCAL
- CONFIRMED_MULTI_ZONE
- BOUNDED
- CHANGING
- RESTORING
- CLOSED

The outage record must not assume sabotage, weather, overload, Pokémon interference or equipment failure until evidence supports a cause.

## 4. Service availability observation

```yaml
service_availability_observation:
  observation_id: null
  zone_or_service_id: null
  observer_id: null
  observed_at: null
  observed_state: null
  symptoms: []
  evidence_refs: []
  confidence: unknown
```

Examples:
- lights out on two blocks;
- one lift unavailable;
- water pressure reduced;
- refrigeration switched to backup;
- communication terminal offline;
- pump audible but no downstream flow.

These observations help bound the incident. They are not diagnoses.

## 5. Cascade packet

A cascade packet makes downstream effects explicit.

```yaml
infrastructure_cascade_packet:
  cascade_id: null
  outage_id: null
  origin_ref: null
  edge_path: []
  affected_subject_id: null
  resulting_state: null
  first_effective_at: null
  fallback_applied: false
  owner_system: null
```

Example:

```text
intake obstruction
  -> pumping network DEGRADED
  -> storage reserve BACKUP_ONLY
  -> clinic water service NORMAL temporarily
  -> market wash-water LIMITED
```

The owner system remains authoritative for the final service consequence. Infrastructure reports that supply changed; Care decides what the clinic can actually provide.

## 6. Backup continuity state

```yaml
backup_continuity_state:
  backup_id: null
  supported_zone_or_service_ids: []
  activation_trigger: null
  activated_at: null
  capacity_band: null
  restricted_functions: []
  material_dependency_refs: []
  staffing_dependency_refs: []
  review_trigger: null
  current_state: standby
```

Possible states:
- STANDBY
- STARTING
- ACTIVE
- ACTIVE_LIMITED
- UNAVAILABLE
- EXHAUSTED_OR_ENDED
- TESTING
- RETURNED_TO_STANDBY

The extension intentionally avoids inventing fuel quantities, battery duration or numeric reserve time.

## 7. Isolation and switching event

```yaml
network_switching_event:
  switching_id: null
  network_id: null
  authorized_operator_ids: []
  action_type: null
  affected_node_ids: []
  previous_state: null
  intended_state: null
  reason_claim_ids: []
  executed_at: null
  verification_refs: []
```

Candidate action types:
- ISOLATE
- DE_ENERGIZE
- BYPASS
- TRANSFER_SOURCE
- SHED_LOAD
- RECONNECT
- ENTER_SAFE_MODE

Only commands supported by the authored technical asset/network may exist. The generator must not invent electrical or hydraulic operations.

## 8. Restoration plan

```yaml
infrastructure_restoration_plan:
  restoration_plan_id: null
  outage_id: null
  coordinating_operator_ids: []
  prerequisite_refs: []
  candidate_step_ids: []
  selected_step_order: []
  blocked_step_ids: []
  priority_decision_ref: null
  fallback_end_conditions: []
  verification_requirements: []
  current_step_id: null
  status: planned
```

Useful statuses:
- PLANNED
- WAITING_ON_ACCESS
- WAITING_ON_STAFF
- WAITING_ON_MATERIAL
- ISOLATING
- RESTORING_SOURCE
- RESTORING_DISTRIBUTION
- RESTORING_ZONES
- VERIFYING
- MONITORING
- COMPLETE
- REVISED

A plan can change when new evidence appears.

## 9. Restoration checkpoint

```yaml
restoration_checkpoint:
  checkpoint_id: null
  restoration_plan_id: null
  subject_id: null
  expected_state: null
  observed_state: null
  evidence_refs: []
  passed: false
  downstream_release_ids: []
  unresolved_notes: []
```

Restoration should be gated by evidence rather than a single “power on” event.

Examples:
- source stable;
- distribution node responding;
- zone receiving supply;
- backup safely transferred off;
- dependent facility completed its own restart check;
- no new contradictory observations during the monitoring window.

## 10. Downstream release contract

When infrastructure supply returns, dependent systems receive a handoff rather than automatic normalization.

```yaml
service_restoration_handoff:
  handoff_id: null
  infrastructure_subject_id: null
  dependent_system: null
  dependent_subject_id: null
  availability_state: null
  restored_at: null
  verification_refs: []
  owner_action_required: true
```

Examples:
- Care checks refrigeration/clinic readiness;
- Travel checks lifts, signals or terminal operation;
- Communications checks relay/message service;
- Storefront checks whether service can reopen;
- Residential checks household access/utilities;
- Facility Maintenance checks local equipment after supply returns;
- Waste/Sanitation checks pumps, treatment or collection dependencies;
- Event Operations checks temporary systems before reopening an event area.

## 11. Priority and authority boundary

The technical graph can expose that only two of four loads can be restored immediately. It cannot decide who deserves priority unless an authored operator procedure or civic/emergency authority already exists.

Store:
- physical capacity;
- available switching options;
- fallback state;
- dependency consequences;
- technical constraints.

Refer the priority decision to:
- civic governance;
- crisis command;
- facility operator procedure;
- other canon-approved authority.

Do not create a hidden morality score for service priority.

## 12. Outage communication

An outage and a public notice are separate objects.

Communications owns:
- who was notified;
- which message was sent;
- delivery and correction state;
- public framing.

Infrastructure owns:
- current technical availability;
- affected zones;
- restoration evidence.

A stale outage notice may remain visible after service changes. That discrepancy can itself create a small investigation or trust issue.

## 13. Cross-network interdependency

Networks may depend on one another.

Examples that require authored edges:
- pumping equipment requires power;
- communications equipment requires power;
- an energy source requires water flow;
- a treatment process requires a transport delivery;
- backup generation requires staff/material support;
- a transport-control system requires communications.

Do not infer a universal dependency model for every settlement.

A multi-network incident should preserve separate states for each system rather than creating one global `infrastructure_down=true` flag.

## 14. Ecology during shutdown and restart

Long outages can alter light, noise, heat, water flow, access and human traffic. Pokémon may use those changes.

Store observations through existing ecology systems. When restoration materially changes a newly occupied space, emit a conservation/ecology review rather than silently despawning Pokémon.

Co-location still does not prove causation.

## 15. Minecraft representation

Safe representations include:
- lights or machinery switching to inactive visual states;
- closed lift/door access tied to authoritative service state;
- backup equipment appearing when activated;
- temporary notices and barriers;
- technicians at actual affected nodes;
- partial district lighting;
- changed ambient sound;
- a control room board showing zones as NORMAL/DEGRADED/OFFLINE;
- restored sections returning in stages.

Unsafe shortcuts include:
- redstone topology becoming the authoritative utility simulation;
- Minecraft lightning automatically creating PTU damage;
- visual electricity becoming a hazard without AutoPTU support;
- a powered block proving a facility is safe;
- chunk unload resetting an outage;
- arbitrary despawning as a substitute for evacuation or service-state ownership.

## 16. Routine compression

Do not materialize every switch operation.

Surface a restoration scene when at least one meaningful decision exists:
- incident extent is uncertain;
- multiple causes fit the observations;
- a backup preserves some but not all functions;
- several technically valid restoration sequences have different world consequences;
- a downstream owner needs verification;
- an ecological conflict appears during restart;
- access to the relevant node is blocked;
- a past repair/player decision changes current redundancy;
- public information disagrees with current service state.

## 17. Encounter contract A — Switchyard Access Restoration

Narrative premise:

A distribution node must remain isolated until operators can safely reach it. Wild or hostile Pokémon occupy the access corridor after the outage changed local activity.

Full version may include:
- changing powered/unpowered zones;
- reach/protect objective;
- restricted control points;
- electrical or machinery hazards only where PTU/Caelo supports them;
- interception/forced movement around narrow access;
- tactical AI that understands access denial and withdrawal;
- synchronized adapter playback.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL where legal effects apply
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Operators complete isolation before combat. The battle occurs in a static reviewed access area with no live electrical hazards, switching objectives or forced movement. After the battle, authorized operators perform the restoration step in overworld state and the next checkpoint becomes available.

## 18. Encounter contract B — Flooded Conduit Isolation

Narrative premise:

A service corridor has taken on water while a separate Pokémon incident blocks inspection. The network must remain isolated until the corridor is safe to assess.

Full version may include:
- changing water/terrain state;
- dynamic unsafe zones;
- withdrawal or rescue objective;
- forced movement if governing rules support current/water effects;
- objective-aware AI;
- infrastructure controls represented during combat.

Dependency state is the same as Contract A, with particular reliance on the BLOCKING environmental and complete-movement families.

Reduced version:

Close the corridor and remove workers first. Keep water depth/contamination as world-state evidence rather than tactical terrain. Resolve any remaining combat in an adjacent static arena. Inspection and pumping remain separate infrastructure/facility actions afterward.

## 19. Noncombat pattern — Restoration Board

A district has several affected services and limited restoration capacity.

Playable sequence:
1. collect availability observations;
2. confirm which outages share a dependency path;
3. identify active backups and their restrictions;
4. expose technically valid restoration sequences;
5. obtain the required authority decision when priorities conflict;
6. execute selected switching/repair handoffs;
7. verify each restored zone;
8. issue downstream handoffs;
9. preserve the outage and restoration history for future callbacks.

This pattern can run now as world-state logic without new tactical engine capabilities.

## 20. Canon/rules safeguards

Do not infer:
- exact grid voltage, pressure, flow, load or capacity;
- engineering standards;
- operator licensing;
- mandatory restoration deadlines;
- legal right to disconnect or prioritize a customer;
- quantitative backup duration;
- economic compensation;
- negligence or sabotage;
- Pokémon technical competence from type/species alone;
- combat effects from utility state.

Those require canon, governing PTU/Caelo rules or implementation evidence.

## 21. Implementation value

This extension lets Minecraft show a district recovering in pieces instead of flipping instantly from broken to normal. It also gives other Ouros systems explicit infrastructure handoffs, making one incident capable of producing coherent consequences across Care, Travel, Communications, Storefronts, Housing, Events, Sanitation and Ecology without any one subsystem stealing authority from the others.
