# Emergency Services, Dispatch & Incident Coordination Layer

Status: proposed systems architecture. Not established Ouros canon.

## Purpose

This layer owns operational response coordination after a report or crisis need exists. It does not own the hazard itself. `crisis-rescue-recovery-layer.md` remains authoritative for hazard/crisis state; this layer owns intake, triage, assignment, staging, unit availability, handoffs, mutual aid, operational objectives and demobilization.

## Core separation

```text
incident/hazard truth
→ incoming report/request
→ intake/triage
→ dispatch decision
→ assigned resource
→ response timeline
→ handoff / transfer
→ demobilization
→ after-action review
```

No arrow proves the next state automatically.

A dispatched unit does not prove the report was accurate. Arrival does not prove access. Battle victory does not prove the incident objective was completed.

## Relationship to existing layers

- Crisis owns hazard state and crisis phases.
- Communications owns message/channel delivery.
- Workplaces owns staffing, shifts and qualifications.
- Technology/Infrastructure owns vehicles, stations, communications equipment and utilities.
- Care owns clinical treatment and patient recovery.
- Travel owns route availability and transport services.
- Supply Chains owns consumables, equipment stock and replenishment.
- Credentials owns permission/qualification claims.
- Agreements owns mutual-aid agreements when they exist.
- Public Memory owns later remembrance.
- Cases owns suspicious cause/evidence investigations.
- Pokémon Agency owns any responder Pokémon’s individual agency and partnership state.

## Core objects

```yaml
emergency_service:
  service_id: null
  service_type: null
  institution_id: null
  coverage_area_ids: []
  station_ids: []
  unit_ids: []
  dispatch_center_ids: []
  mutual_aid_refs: []
  policy_version_id: null
  active: true

response_unit:
  unit_id: null
  service_id: null
  unit_type: null
  staffing_refs: []
  pokemon_participant_ids: []
  equipment_refs: []
  home_station_id: null
  current_location_id: null
  readiness_state: AVAILABLE
  qualification_claim_refs: []
  current_assignment_id: null

incident_request:
  request_id: null
  received_at: null
  source_actor_id: null
  source_channel_id: null
  reported_location_id: null
  reported_problem: null
  verification_state: UNVERIFIED
  priority_assessment_id: null
  linked_crisis_id: null
  linked_case_id: null

priority_assessment:
  assessment_id: null
  request_id: null
  assessed_at: null
  assessor_id: null
  severity_band: null
  uncertainty: null
  resource_needs: []
  assumptions: []
  revision_of: null

dispatch_assignment:
  assignment_id: null
  incident_request_id: null
  unit_id: null
  assigned_at: null
  objective_refs: []
  route_plan_ref: null
  status: ASSIGNED
  status_history: []

incident_operation:
  operation_id: null
  crisis_id: null
  objective_ids: []
  participating_service_ids: []
  staging_site_ids: []
  command_or_coordination_roles: []
  unit_assignments: []
  resource_requests: []
  handoff_records: []
  completed_objectives: []
  unresolved_objectives: []
  demobilization_records: []
  after_action_review_ids: []
```

## Unit readiness states

Suggested coarse states:

- AVAILABLE
- ASSIGNED
- EN_ROUTE
- STAGED
- OPERATING
- TRANSFERRING
- RETURNING
- OUT_OF_SERVICE
- RESTOCKING
- MAINTENANCE
- TRAINING

These are operational states only. They do not grant PTU bonuses.

## Incident objectives

Objectives should be explicit world-state targets such as:

- VERIFY_REPORT
- REACH_SITE
- ESTABLISH_ACCESS
- EVACUATE_AREA
- LOCATE_MISSING_ACTOR
- EXTRACT_ACTOR
- STABILIZE_INFRASTRUCTURE
- RESTORE_COMMUNICATION
- DELIVER_RESOURCE
- TRANSFER_PATIENT
- PROTECT_ROUTE
- CONTAIN_LOCAL_HAZARD
- HANDOFF_CUSTODY
- DEMOBILIZE

Each objective needs completion evidence from the owning system.

Example: `TRANSFER_PATIENT` requires Care/Transport handoff state. AutoPTU cannot mark it complete merely because nearby hostile combatants were defeated.

## Dispatch and triage

Triage is an assessment under uncertainty.

```yaml
triage_revision:
  request_id: null
  observed_facts: []
  unverified_claims: []
  severity_band: null
  resource_request: []
  changed_because: null
```

A later revision does not erase the earlier decision. Chronicle should preserve why a unit was or was not sent based on what was known at that time.

## Multiple simultaneous incidents

The system must support resource contention.

Example:

```text
Unit A already OPERATING at bridge collapse
+ Unit B OUT_OF_SERVICE
+ second fire request arrives
→ dispatch center requests mutual aid
→ neighboring service accepts one objective
→ original service keeps its own authority
```

This can create narrative consequence without inventing incompetence or villainy.

## Mutual aid

Mutual aid does not merge organizations.

```yaml
mutual_aid_activation:
  activation_id: null
  agreement_ref: null
  requesting_service_id: null
  assisting_service_id: null
  requested_capabilities: []
  accepted_scope: []
  start_at: null
  end_at: null
  authority_boundaries: []
```

If no prior agreement exists, emergency cooperation can still be proposed as an authored/world-state action, but the generator must not invent legal authority.

## Responder Pokémon

A Pokémon participating in an emergency service remains a persistent Pokémon individual.

Institutional participation does not imply:
- ownership by the service;
- unlimited availability;
- automatic obedience;
- universal carrying capacity;
- immunity to hazards;
- Water-type = firefighter;
- Flying-type = rescue aircraft;
- Psychic-type = medical scanner.

Any mechanical use requires the individual’s authoritative PTU/Caelo capabilities and current AutoPTU support.

## Staging and handoffs

Staging is a world-state coordination function, not a tactical buff.

Handoffs should preserve responsibility and custody changes:

```yaml
handoff_record:
  handoff_id: null
  object_or_actor_id: null
  from_actor_or_unit_id: null
  to_actor_or_unit_id: null
  handoff_type: null
  occurred_at: null
  location_id: null
  accepted: null
  unresolved_conditions: []
```

Useful handoffs include patient transfer, rescued Pokémon transfer, evidence transfer, cargo transfer and operational sector transfer. Each still defers to Care, Pokémon Agency, Cases or Supply Chains for substantive authority.

## Training, drills and readiness

Drills can create persistent readiness evidence:

- response time observations;
- communication gaps;
- equipment failures;
- outdated maps;
- staffing gaps;
- incorrect assumptions;
- successful mutual-aid handoffs;
- revised plans.

A successful drill does not grant combat XP or a Trainer Feature unless governing mechanics explicitly support it.

## After-action review

After an operation, store:

```yaml
after_action_review:
  review_id: null
  operation_id: null
  factual_timeline_refs: []
  objective_results: []
  communication_findings: []
  resource_findings: []
  access_findings: []
  safety_findings: []
  unresolved_questions: []
  corrective_actions: []
  disputed_interpretations: []
```

Reviews can produce future training, equipment, infrastructure or policy projects. They cannot rewrite the incident record.

## Minecraft projection

Minecraft may display stations, alarms, vehicles, staging areas, responders and route closures. It must not become authoritative for:
- unit availability;
- dispatch priority;
- emergency authority;
- patient status;
- evacuation completion;
- hazard severity;
- responder qualification;
- resource inventory;
- Pokémon consent/agency.

## Battle integration guardrail

Before a battle begins, the world layer should freeze the tactical problem it can legally represent.

Example reduced flow:

```text
report received
→ responders dispatched
→ civilians evacuated in world state
→ hazard boundary frozen
→ actual combatants enter AutoPTU
→ battle transcript returns
→ incident objectives re-evaluated by world systems
```

The battle result may remove one obstruction. It does not automatically resolve the incident.

## Hard non-inferences

Do not infer:
- siren/alarm -> confirmed emergency;
- dispatch -> report truth;
- responder uniform -> universal authority;
- leadership role -> Command Skill or Trainer Feature;
- Water Move -> firefighting value;
- healing Move -> clinical treatment permission;
- Flying/Sky -> legal passenger rescue;
- victory -> evacuation complete;
- Fainted hostile -> route safe;
- unit unavailable -> institutional failure;
- delayed response -> negligence;
- repeated incidents -> conspiracy;
- mutual aid -> merged faction;
- responder Pokémon -> institutional property.

## Canon status

This entire layer is proposed architecture. No specific Ouros fire brigade, rescue service, emergency number, dispatch center, command structure, certification system or legal authority is canon until reviewed.