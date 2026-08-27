# Worksite Safety, Near-Miss & Incident Learning Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

This extension gives persistent workplaces a preventive safety lifecycle before a problem becomes a full crisis and after an incident returns to ordinary operations.

It connects existing staffing, maintenance, equipment, credentials, observations, communications and crisis systems. It does not create universal safety law, occupational regulation, liability, discipline, engineering rules or PTU tactical hazards.

The core objective is to let a workshop, mine, dock, clinic backroom, research station, construction site, archive work area, ferry landing or other workplace accumulate operational memory through observations, close calls, restrictions, corrective actions and verified changes.

## Ownership boundaries

Workplaces/Staffing owns roles, shifts, assignments, staffing capacity, training state and ordinary handoffs.

Facility Maintenance owns physical condition, technical faults, assessment, repair scope, work orders and facility reopening.

Shared Equipment owns exact equipment custody, checkout, inspection-pending and availability.

Credentials owns qualifications and authorization scope.

Crisis/Rescue owns active emergencies, evacuation, shelters, crisis response and recovery when normal operations break down at crisis scale.

Case/Authority owns formal evidence/custody when suspected wrongdoing or an authorized formal case exists.

This extension owns preventive observations, near-miss continuity, work-area restrictions, safety briefings, corrective-action tracking and the explicit safety-side return-to-work handoff.

## 1. Safety observation

```yaml
work_safety_observation:
  observation_id: null
  workplace_id: null
  area_ref: null
  observer_id: null
  observed_at: null
  work_assignment_ref: null
  description_claim_ref: null
  evidence_refs: []
  immediate_exposure_state: unknown
  suggested_action_claim_refs: []
  related_prior_observation_ids: []
  status: OPEN
```

An observation records what was noticed. It does not establish technical cause, legal responsibility, negligence or a PTU Hazard.

Examples:

- a cart repeatedly rolls farther than expected on one section of floor;
- a warning light is intermittent;
- wild Pokémon are entering a staging path during the same time window each day;
- water appears near a workbench after rain;
- two shifts use different names for the same shutoff point;
- a temporary barrier has been moved from its documented position.

## 2. Near miss / close call

```yaml
work_near_miss:
  near_miss_id: null
  workplace_id: null
  area_ref: null
  occurred_at: null
  involved_actor_ids: []
  involved_pokemon_ids: []
  work_assignment_refs: []
  equipment_instance_refs: []
  event_sequence_claim_refs: []
  observed_outcome: no_confirmed_injury
  potential_consequence_claim_refs: []
  immediate_actions: []
  evidence_refs: []
  review_state: OPEN
```

A near miss is useful because circumstances nearly produced a harmful outcome. It does not require inventing a numerical risk score.

`no_confirmed_injury` must not be used to overwrite Care records if injury evidence exists elsewhere.

## 3. Incident handoff

If an event causes injury, major facility damage, evacuation, missing actors, service-wide shutdown or other crisis-scale consequences, the extension creates a handoff instead of absorbing the emergency.

```yaml
safety_incident_handoff:
  handoff_id: null
  source_observation_or_near_miss_ids: []
  crisis_ref: null
  care_ref: null
  maintenance_fault_refs: []
  case_ref: null
  equipment_refs: []
  preserved_evidence_refs: []
  status: HANDED_OFF
```

The safety history stays available later for corrective-action review.

## 4. Work-area state

```yaml
work_area_safety_state:
  area_state_id: null
  workplace_id: null
  area_ref: null
  state: NORMAL
  basis_refs: []
  effective_at: null
  authority_ref: null
  affected_work_assignment_ids: []
  allowed_activity_refs: []
  restricted_activity_refs: []
  temporary_control_ids: []
  review_trigger: null
```

Suggested states:

- NORMAL
- CAUTION
- RESTRICTED
- STOPPED
- ASSESSMENT_ONLY
- CORRECTIVE_WORK_ONLY
- VERIFYING
- RETURN_READY

These labels are narrative operating states. They do not establish a universal Ouros legal framework.

No generator may invent who has authority to set STOPPED. `authority_ref` must point to authored institutional state, an existing role, a credential/authorization or explicit scenario authority.

## 5. Temporary control

```yaml
work_safety_control:
  control_id: null
  workplace_id: null
  area_ref: null
  source_refs: []
  control_type: authored
  visible_world_changes: []
  procedural_changes: []
  staffing_changes: []
  access_changes: []
  start_time: null
  end_trigger: null
  status: ACTIVE
```

Possible authored controls include rerouting foot traffic, reducing simultaneous work, relocating a staging point, pausing one task, increasing supervision, marking an area, changing equipment availability or moving a work phase to another location.

A control reduces or changes exposure. It never proves that the underlying cause is resolved.

## 6. Review packet

```yaml
safety_review:
  review_id: null
  source_observation_ids: []
  source_near_miss_ids: []
  incident_handoff_ids: []
  reviewer_ids: []
  reviewer_authority_refs: []
  evidence_refs: []
  timeline_event_refs: []
  contributing_factor_claims: []
  disputed_claim_ids: []
  unresolved_questions: []
  corrective_action_ids: []
  status: IN_PROGRESS
```

The review may identify multiple contributing conditions. It must preserve uncertainty.

Examples of evidence:

- shift handoffs;
- equipment checkout and condition history;
- maintenance records;
- photographs;
- weather observations;
- public notices;
- access logs where canonically available;
- work assignments;
- witness/testimony packets;
- prior safety observations.

The review must not create a hidden culprit field.

## 7. Corrective action

```yaml
safety_corrective_action:
  corrective_action_id: null
  workplace_id: null
  source_review_id: null
  action_type: authored
  owner_actor_or_role_refs: []
  dependency_refs: []
  maintenance_work_order_refs: []
  equipment_action_refs: []
  staffing_or_training_refs: []
  signage_or_notice_refs: []
  world_overlay_refs: []
  verification_requirements: []
  status: PLANNED
  completed_at: null
```

Corrective actions can hand work to Maintenance, Staffing, Equipment, Procurement, Credentials, Communications or other owners.

Examples:

- revise a physical route;
- repair or replace equipment;
- alter a shift handoff template;
- move a staging point;
- schedule a recurring inspection;
- revise an authored briefing;
- add a visible indicator;
- change which role must be present for a task;
- redesign a work sequence.

Completion means the action happened. It does not automatically mean the site is safe to resume every activity.

## 8. Safety briefing and learned state

```yaml
work_safety_briefing:
  briefing_id: null
  workplace_id: null
  shift_or_assignment_refs: []
  issued_at: null
  presenter_ids: []
  source_refs: []
  observable_points: []
  acknowledged_actor_ids: []
  unresolved_questions: []
```

This records information transfer, not mind-reading. An actor who was absent from the briefing does not gain the knowledge automatically.

A later shift can receive a revised handoff because of an earlier close call. That change becomes environmental storytelling when the player notices a new barrier, route, check, tag, marked floor, equipment location or briefing habit.

## 9. Verification and return to work

```yaml
safety_return_review:
  return_review_id: null
  workplace_id: null
  area_ref: null
  source_review_id: null
  corrective_action_ids: []
  maintenance_verification_refs: []
  equipment_inspection_refs: []
  verifier_ids: []
  verifier_authority_refs: []
  evidence_refs: []
  unresolved_items: []
  outcome: PENDING
  allowed_activity_refs_after: []
  area_state_after: null
```

Possible outcomes:

- RETURN_FULL
- RETURN_LIMITED
- KEEP_RESTRICTED
- FURTHER_ASSESSMENT
- ESCALATE

A repaired machine, completed battle or absent Pokémon never reopens a workplace by itself.

## 10. Operational hazard versus PTU Hazard

The phrase `operational hazard` may appear in prose, but the data model should prefer `safety observation`, `unsafe condition claim` or `work-area restriction` to avoid confusing world state with the PTU tactical Hazard family.

A wet floor, loose rock, unstable shelf, energized conduit or moving cart can exist as overworld state without receiving tactical combat effects.

If an encounter makes such a condition alter movement, damage, Accuracy, forced displacement, reactions or zones, the exact PTU/Caelo rule and engine capability must be verified first.

## 11. Pokémon participation

A Pokémon may be present in ordinary work when canon and actor state support that relationship.

The extension may record:

- actor/Pokémon work association;
- observed task participation;
- supervision state;
- route/access changes made for coexistence;
- non-mechanical occupational routine.

It may not infer:

- Skill Ranks from species;
- Trainer Features;
- Move effects not actually known;
- Ability effects outside their rules;
- legal authority;
- willingness or consent from species stereotype;
- safe lifting, cutting, electrical, fire, flight or rescue capacity from type alone.

Mechanically relevant capability claims require PTU/Caelo evidence plus current engine support where battle/runtime behavior is involved.

## 12. Persistent story grammar

A useful recurring loop:

`baseline -> signal -> observation -> temporary restriction -> review -> corrective action -> verification -> return -> callback`

The callback matters. On a later visit, the player should be able to see at least one durable consequence:

- a route changed;
- a machine moved;
- a sign revised;
- a work pair changed;
- a briefing habit exists;
- an old temporary control remains because the permanent fix is delayed;
- a near-miss report becomes relevant to a new but not necessarily identical event.

## 13. Mysteries without automatic misconduct

Safety history supports grounded mysteries:

- the same symptom appears on two shifts but has different causes;
- three reports look independent but share one original observer;
- a repair solved one condition while exposing an older one;
- equipment custody shows that the suspected device was not present during one event;
- a weather window explains timing without proving cause;
- a changed routine moved exposure elsewhere.

The generator must permit `insufficient evidence` and `multiple contributing factors` as valid outcomes.

## 14. Minecraft representation

Minecraft should render authored state:

- barriers;
- alternate paths;
- inactive equipment props;
- work zones;
- notices;
- changed NPC locations;
- closed doors;
- supervised work groups;
- cleanup or repair aftermath.

Breaking or placing a block manually must not create authoritative safety findings, clear restrictions or complete corrective actions unless an adapter contract explicitly maps that interaction.

## 15. Encounter contract: Scaffold-Line Evacuation

Narrative premise:

A work crew reports repeated movement in a temporary elevated work area. During assessment, wild Pokémon activity or another authored threat forces the assessment team to withdraw. The safety question remains separate from the battle question.

Intended full version:

- workers/assessors withdraw through changing safe routes;
- some cells/areas become unavailable as the assessment changes;
- protected equipment or access points matter;
- knockback/interception can change who reaches safety;
- environment conditions may matter tactically if backed by PTU/Caelo rules;
- opponents may prefer territory/escape over KO;
- transcript/playback preserves positions and objective outcomes.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including forced movement/interception: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full lifecycle: PARTIAL;
- full stateful damage: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic work-area danger;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:

The responsible actor stops work before combat. Workers and assessors leave the unstable section through world state. The questionable area is closed and excluded from the tactical map. AutoPTU receives a static conventional arena in a safe perimeter. After the authoritative battle result, assessment resumes. Victory does not determine the physical cause or authorize reopening.

## 16. Encounter contract: Loading-Bay Near Miss Follow-Up

Narrative premise:

A loading movement nearly struck a worker or Pokémon. Review later identifies a recurring timing conflict. During a controlled follow-up, a separate Pokémon encounter interrupts the area.

Intended full version wants moving workers/cargo, protected routes, potential interruption, objective-aware AI and exact adapter playback. Those depend on complete movement, dynamic zones/reactions, tactical AI and adapter support, all currently BLOCKING.

Reduced version:

The bay is emptied first. Cargo and workers exist only in world state. AutoPTU resolves the local encounter on a static map. The team then reconstructs the near miss using timestamps, work assignments, custody records and observations.

## 17. Non-combat encounter: Five Reports, Four Events

Five safety reports appear to document five separate close calls. Timeline reconstruction shows that two reports describe the same event from different shifts because the first handoff lacked a stable event reference.

Possible outcomes include:

- four real events with one duplicate report;
- three events plus two independent observations of a recurring condition;
- a maintenance change splitting one condition into two different ones;
- insufficient evidence.

This can run immediately because it depends on provenance and world-state records rather than tactical mechanics.

## Canon questions

Before canon adoption, Ouros still needs explicit answers for:

- which institutions maintain formal safety records;
- whether any role has stop-work authority and under what scope;
- what ordinary workers can do when they observe a dangerous condition;
- what kinds of sites require formal verification before resuming work;
- how privacy applies to incident reports;
- whether labor organizations or worker representatives exist;
- what terminology cultures/regions use;
- which Pokémon work arrangements are normal, exceptional or prohibited;
- where engineering, medical or legal authority lives.

Until then all structures in this file remain system candidates.