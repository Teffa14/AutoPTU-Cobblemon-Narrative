# Service Request, Queue, Appointment & Capacity Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE
Pass: 198
Date: 2026-09-02
Canon effect: NONE until explicit promotion.
Research basis: `research/2026-09-02-service-request-queue-appointment-capacity-scan-198.md`

## Purpose

Represent ordinary requests for finite local service capacity without turning every request into a quest, every delay into failure, every schedule into regional law, or every completed appointment into a PTU mechanical effect.

Narrative owns service-lifecycle facts and provenance. Existing domain systems remain authoritative for transport, lodging, custody, competency, archive access, research review, Battle Yard semantics and PTU/Caelo/AutoPTU mechanical results.

## Core records

```yaml
service_request:
  request_id: null
  requester_ref: null
  submitted_to_ref: null
  requested_service_kind: null
  requested_scope: []
  submitted_at: null
  source_ref: null
  claimed_urgency: null
  evidence_refs: []
  dependency_refs: []
  current_state: SUBMITTED
  routing_history_refs: []
  triage_ref: null
  appointment_refs: []
  work_order_refs: []
  result_refs: []
  provenance_refs: []
```

Recommended request states:

- SUBMITTED
- ACKNOWLEDGED
- ROUTING
- NEEDS_INFORMATION
- WAITING_DEPENDENCY
- ACCEPTED
- SCHEDULED
- IN_PROGRESS
- PAUSED
- RESULT_PENDING
- COMPLETED_RECORDED
- DECLINED
- CANCELLED
- UNKNOWN

```yaml
service_routing_event:
  routing_id: null
  request_id: null
  from_ref: null
  to_ref: null
  occurred_at: null
  reason_ref: null
  preserves_original_submission_at: true
  provenance_refs: []
```

Routing does not reset request age unless a specific authored policy explicitly creates a new request.

```yaml
service_triage_record:
  triage_id: null
  request_id: null
  performed_by_ref: null
  performed_at: null
  claimed_urgency: null
  verified_context_refs: []
  local_priority_result: null
  rationale_ref: null
  policy_or_procedure_version_ref: null
  provenance_refs: []
```

This preserves an attributed local scheduling decision. It does not create a universal Caelo priority system.

```yaml
service_capacity_slot:
  slot_id: null
  provider_or_resource_ref: null
  service_kind: null
  window_start: null
  window_end: null
  current_state: AVAILABLE
  assignment_refs: []
  dependency_refs: []
  revision_ref: null
  provenance_refs: []
```

Possible slot states: AVAILABLE, HELD, ASSIGNED, BLOCKED, RELEASED, SUPERSEDED, COMPLETED_WINDOW.

A slot can represent an already-established person, room, berth, bench, equipment set or other capacity. Do not invent exact capacity units where canon has not established them.

```yaml
appointment_instance:
  appointment_id: null
  request_id: null
  provider_ref: null
  requester_refs: []
  location_ref: null
  scheduled_start: null
  scheduled_end: null
  actual_arrival_refs: []
  actual_start: null
  actual_end: null
  current_state: SCHEDULED
  reschedule_from_ref: null
  reschedule_to_ref: null
  interruption_refs: []
  provenance_refs: []
```

Possible appointment states: PROPOSED, HELD, CONFIRMED, SCHEDULED, CHECKED_IN, STARTED, INTERRUPTED, COMPLETED, PROVIDER_UNAVAILABLE, RESCHEDULED, CANCELLED, UNKNOWN.

```yaml
service_work_order:
  work_order_id: null
  request_id: null
  accepted_scope: []
  performing_actor_refs: []
  supervising_actor_refs: []
  resource_refs: []
  material_reservation_refs: []
  started_at: null
  paused_at: null
  resumed_at: null
  closed_at: null
  current_state: ACCEPTED
  dependency_refs: []
  execution_evidence_refs: []
  mechanical_resolution_ref: null
  output_object_or_record_refs: []
  closure_note_ref: null
```

Possible work states: ACCEPTED, READY, BLOCKED, STARTED, PAUSED, RESUMED, WORK_COMPLETE_PENDING_RESULT, CLOSED, CANCELLED.

```yaml
service_result_record:
  result_id: null
  request_id: null
  work_order_id: null
  recorded_by_ref: null
  recorded_at: null
  result_kind: null
  observable_outputs: []
  mechanical_authority_ref: null
  mechanical_result_ref: null
  requester_ack_ref: null
  follow_up_request_refs: []
  correction_refs: []
  provenance_refs: []
```

A result can later be corrected or reopened without deleting the original record.

## Hard boundaries

`REQUEST_SUBMITTED != REQUEST_ACCEPTED`

`REQUEST_ACKNOWLEDGED != REQUEST_SCHEDULED`

`REQUEST_SCHEDULED != SERVICE_STARTED`

`SERVICE_STARTED != SERVICE_COMPLETED`

`WORK_ORDER_CLOSED != RESULT_PERFECT`

`CLAIMED_URGENCY != VERIFIED_PRIORITY`

`QUEUE_POSITION != PRIORITY_RIGHT`

`EARLIER_SUBMISSION != UNIVERSAL_FIRST_PRIORITY`

`SLOT_HELD != APPOINTMENT_OCCURRED`

`APPOINTMENT_OCCURRED != MECHANICAL_EFFECT_APPLIED`

`PROVIDER_UNAVAILABLE != SERVICE_REFUSED`

`REQUEST_REROUTED != REQUEST_RESUBMITTED`

`RESOURCE_RESERVED != RESOURCE_CONSUMED`

`MATERIAL_PRESENT != WORK_READY`

`SERVICE_COMPLETED_OFFSCREEN != PLAYER_OBSERVED_COMPLETION`

`PLAYER_ABSENT != SERVICE_FROZEN`

`NPC_ENTITY_UNLOADED != PROVIDER_UNAVAILABLE`

`MINECRAFT_INTERACTION != AUTHORITATIVE_CHECK_IN`

`VISIBLE_LINE_POSITION != AUTHORITATIVE_QUEUE_POSITION`

## Queue projection

A visible queue is a projection of current records, not sole authority.

```yaml
service_queue_projection:
  projection_id: null
  service_owner_ref: null
  generated_at: null
  governing_policy_or_local_decision_refs: []
  entry_refs: []
  supersedes_projection_ref: null
```

Possible ordering inputs include submission time, appointment window, dependency readiness, verified urgency, provider specialization, explicit reschedule preservation and authored local policy.

Two physical boards may show different revisions. The server retains the current authoritative projection while the stale copy remains historical evidence.

## No universal queue policy

Current Marea canon does not establish one ordering rule for every institution.

The architecture therefore stores decisions rather than inventing doctrine. A routine repair workflow can use a locally authored order while ferry windows, archive review and Battle Yard sessions can rely on different constraints.

## Delay provenance

Recommended descriptive reasons:

- PROVIDER_UNAVAILABLE
- REQUESTER_UNAVAILABLE
- REQUIRED_INFORMATION_MISSING
- MATERIAL_NOT_AVAILABLE
- RESOURCE_CONFLICT
- DEPENDENCY_INCOMPLETE
- TRANSPORT_DELAY
- WEATHER_REVIEW
- AUTHORITY_REVIEW_PENDING
- SAFETY_INTERRUPTION
- PRIORITY_RESEQUENCING
- SCHEDULE_REVISION_CONFLICT
- UNKNOWN

These describe operational state. They do not assign blame.

## Rescheduling

Rescheduling preserves the prior appointment and its provenance.

```yaml
appointment_revision:
  revision_id: null
  prior_appointment_ref: null
  new_appointment_ref: null
  changed_by_ref: null
  changed_at: null
  reason_ref: null
  notification_refs: []
```

An old slot may remain visible on stale correspondence or a board without remaining current.

## Off-screen progression

A service may advance while the player is elsewhere when the request already exists, a legitimate actor owns the step, prerequisites are satisfied, the relevant clock reaches the expected window and the transition does not require a missing mechanical resolver.

Safe examples include a mundane repair already in progress, an authorized copy prepared by Pia, an established equipment check by Ema, or a known schedule record updated by Lia.

Do not fabricate a battle, discovery, relationship change, mechanical effect or missing resource simply because time passed.

## Adjacent-system integration

Correspondence may carry a request, but message delivery does not itself mean accepted work.

Visitor hosting retains temporary-presence and occupancy state. This layer may record an intake request without duplicating lodging authority.

Duty-cycle continuity determines actor availability and handoff. This layer supplies the request/work-order references that can be handed off.

Competency determines whether someone may perform scoped work. Assignment never grants competence.

Custody/provisioning determines physical possession, reservation and consumption. A work order only links those records.

## Mechanical-service handshake

PTU 1.05 explicitly discusses NPC services derived from Features. Narrative therefore needs a hard request/result boundary for mechanically meaningful services.

```yaml
mechanical_service_request:
  narrative_request_id: null
  service_kind: null
  actor_refs: []
  target_refs: []
  requested_effect_ref: null
  ruleset_ref: null
  pre_state_ref: null
  provider_build_ref: null
  content_refs: []

mechanical_service_result:
  authority_ref: null
  legal: null
  result_state_delta_ref: null
  emitted_event_refs: []
  rejection_reason_ref: null
```

Narrative stores the authoritative result. It does not recreate it from prose.

Examples include Move tutoring, Mentor-derived services, governed item transformations, Pokémon training effects and battle/session outcomes.

## Marea applications

Teo Lark can own ordinary repair intake, work-surface scheduling, waiting for parts and pickup/return history. Mechanically governed item construction remains external.

Lia Morn can record requested unloading windows, assignments and revisions while transport state remains separate.

Tideglass can schedule requests for copies, supervised access or review while Taro/Pia retain actual authority.

Mirador can schedule instrument service and review windows without predetermining scientific conclusions.

The Battle Yard can schedule practice requests and yard slots while BattleSpec owns battle outcomes and existing competitive layers own challenge/exhibition semantics.

## Minecraft/Cobblemon/Craftics projection

Useful projections include boards, workbench occupancy, check-in dialogue, held/available signs, schedule revision notices and completed-work pickup markers.

Projection rules:

- UI click requests a transition; it does not author acceptance;
- visible line order is presentation;
- NPC pathing failure cannot create a missed slot;
- chunk unload cannot pause or cancel work;
- duplicate entities cannot create extra providers or bookings;
- block changes cannot cancel a record;
- container visuals cannot author reservation or consumption;
- client-local schedule display cannot supersede server authority.

## Story value

This layer supports ordinary friction with persistent consequences: scarce shared resources, stale schedules, dependency delays, correctly rerouted requests, off-screen completion and requests displaced by a more urgent locally evaluated problem without disappearing.

Do not add a generic efficiency, satisfaction, queue-reputation or service-quality score. Consequences should attach to specific histories and actors.

## Rich encounter — Battle Yard Double-Booked Drill

Narrative premise: two legitimate practice-session histories point to the same Battle Yard window because one visible schedule copy was not updated after a revision. Both parties arrive with reasonable evidence.

Narrative owns both requests, appointment histories, schedule revisions, stale copy, check-in facts, Sela/Jace authority, participant expectations and any rescheduling decision.

If a controlled battle follows, BattleSpec owns only the audited combat procedure.

Permanent capability classification for the full intended version:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL and required only when selected content or drill objectives depend on it;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected content uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if safety zones, reactions, hazards or environment become mechanical;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL when exact battle items participate;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for objective-aware drill behavior or deliberately non-KO priorities;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING for faithful full projection and return.

Disposition: FULL RICH VERSION BLOCKED unless a narrower selected BattleSpec avoids every blocking family and its exact content is separately audited.

### Reduced version

Preserve the double-booking premise unchanged. Narrative resolves the scheduling conflict first. Sela may reschedule one session, run sessions sequentially, convert one slot into observation/discussion, or offer another authored arrangement.

If a battle occurs, run one ordinary audited battle at a time on stable Yard geometry. Keep spectators, schedule disputes and service records outside BattleSpec. Omit unverified zones/reactions. Avoid forced-movement-dependent objectives unless exact selected interactions are verified.

Allowed battle output is the exact authoritative battle result plus a narrow completion marker such as `AUDITED_PRACTICE_BATTLE_COMPLETE` if the integration contract supports it.

Battle output cannot decide booking validity, fault, queue priority, relationship change, future booking preference, rival status, ranking, badge, award or invented training benefit.

Disposition: NARRATIVE PREMISE RUNNABLE NOW; battle portion reducible to audited ordinary content.

## Live engine evidence

Read-only heads inspected for pass 198:

- AutoPTU-Java: `dd8097910da62f98d07047cd0603fa8d858f4c67`
- AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Java #322 adds `RuntimeForcedMovementPreventionSemanticEvents` and tests that map already-resolved Trainer Feature provenance to the pinned semantic-event shape for the Insectoid Utility / Wallclimber prevention case. The new adapter explicitly does not decide legality or prevention.

This improves observability/parity for one forced-movement prevention path. It does not close complete movement or Trainer Features as families. No category is promoted.

## Canon promotion gate

Do not globally decide queue law, cancellation penalties, service prices, ferry ticketing, professional licensing, staffing ratios, deadlines, compensation or service availability beyond current canon and verified mechanics.

## First implementation recommendation

Implement `Two Repairs, One Bench` first.

Use Teo's canon repair role and one explicitly occupied shared work surface without declaring total Repair Row capacity.

The slice should prove that two requests coexist, one can progress while another waits, a dependency can change local ordering with provenance, completion can occur offscreen, pickup stays separate from work completion, no mechanical crafting effect is invented, and Minecraft visuals project rather than author work-order state.