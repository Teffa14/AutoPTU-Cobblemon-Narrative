# Ouros Request / Dispatch / Response Resource Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29
Research provenance: `research/2026-08-29-request-dispatch-response-resource-continuity-scan-138.md`

## Purpose

This extension preserves the operational continuity between a need becoming known and a resource returning to availability after acting on it.

It exists because Ouros already has owners for the meaning of incidents, communications, staffing, missions and domain-specific outcomes, but no neutral layer currently preserves the full assignment timeline across those systems.

The extension may be used for crisis response, field inspections, search teams, repair crews, Rangers if canon establishes them, volunteer coordinators, transport support, scientific field teams or other institutional work.

It does not establish that any particular service, dispatcher, Ranger organization, emergency number, command hierarchy or radio technology exists in Ouros.

## Ownership boundaries

### Crisis / Rescue

Owns crisis truth, active impacts, unresolved needs, response phase, search/rescue state and crisis closure.

This extension may receive a `need_ref` from Crisis and preserve which resource was requested or assigned to that need.

It never decides that an actor is missing, trapped, rescued or safe.

### Communications / Media

Owns message transmission, delivery, acknowledgement and communications-service availability.

This extension may reference communication events as evidence that an assignment was sent or acknowledged.

It must not infer successful message delivery because an assignment record exists.

### Workplaces / Staffing

Owns roles, shifts, capacity, staff availability and ordinary work assignments.

This extension can reserve or consume a resource after the staffing owner says the resource is eligible to be assigned.

It does not invent qualifications or force an off-duty actor into service.

### Mission Grammar

Owns player-facing mission construction and request surfaces.

This extension provides operational state that Mission Grammar may expose. A mission journal is a view over these facts, not their authority.

### Domain owners

Grid, Roads, Building Safety, Emergency Medical Transport, Wildfire, Water, Research, Pokémon Agency and other domain owners decide what actually happened in their domains.

A field resource reporting “complete” is an event. The relevant owner decides whether its own completion condition is satisfied.

## Core invariants

`REQUEST_RECEIVED != REQUEST_VERIFIED`

`REQUEST_VERIFIED != REQUEST_ACTIONABLE`

`REQUEST_ACTIONABLE != RESOURCE_AVAILABLE`

`RESOURCE_REQUESTED != RESOURCE_ASSIGNED`

`RESOURCE_ASSIGNED != ASSIGNMENT_ACKNOWLEDGED`

`ASSIGNMENT_ACKNOWLEDGED != RESOURCE_DEPARTED`

`RESOURCE_DEPARTED != RESOURCE_ARRIVED`

`RESOURCE_ARRIVED != INCIDENT_RESOLVED`

`FIELD_COMPLETION_REPORTED != DOMAIN_COMPLETION_CONFIRMED`

`RESOURCE_CLEAR != RESOURCE_AVAILABLE_AGAIN`

`DISPATCHED_TO_LOCATION != AUTHORIZED_FOR_ALL_ACTIONS_AT_LOCATION`

`NO_CONTACT != FAILED_ASSIGNMENT`

`LATE_RESPONSE != NEGLIGENCE`

`DUPLICATE_REPORT != DUPLICATE_INCIDENT`

`SAME_INCIDENT != SAME_ASSIGNMENT`

## 1. Request intake episode

```yaml
response_request:
  request_id: null
  received_at: null
  receiving_institution_id: null
  receiving_channel_ref: null
  source_actor_or_system_ref: null
  source_contact_ref: null
  reported_need_type: null
  reported_location_refs: []
  reported_actor_refs: []
  claims: []
  uncertainty_notes: []
  information_state: RECEIVED
  clarification_event_ids: []
  linked_domain_case_refs: []
  duplicate_candidate_refs: []
  supersedes_request_id: null
  provenance_refs: []
```

Candidate `information_state` values:

- RECEIVED
- RECEIVED_INCOMPLETE
- CLARIFICATION_REQUIRED
- ACTIONABLE
- REFERRED_TO_OWNER
- DUPLICATE_CANDIDATE
- SUPERSEDED
- CLOSED_NO_ACTION
- UNKNOWN

The request preserves what was reported at that time. Later truth must not rewrite it.

## 2. Clarification event

```yaml
request_clarification:
  clarification_id: null
  request_id: null
  occurred_at: null
  actor_or_system_id: null
  question_scope: null
  information_added: []
  information_corrected: []
  unresolved_questions: []
  communication_event_refs: []
  resulting_information_state: null
```

A clarification can correct a location or count without implying that the original reporter lied.

## 3. Operational priority decision

Priority exists only where a canon institution has an authored process for it.

```yaml
response_priority_decision:
  priority_decision_id: null
  request_or_need_ref: null
  deciding_actor_or_policy_ref: null
  decided_at: null
  information_snapshot_refs: []
  priority_label: null
  scope: null
  reason_summary: null
  next_review_trigger: null
  supersedes_decision_id: null
```

No default numeric scale is proposed.

Priority labels are local vocabulary owned by the institution or domain.

A later escalation produces a new decision; it does not rewrite the earlier one.

## 4. Response resource

A response resource is an operational package that can be assigned.

```yaml
response_resource:
  resource_id: null
  owner_institution_id: null
  resource_kind: null
  actor_ids: []
  equipment_asset_refs: []
  vehicle_or_transport_refs: []
  role_or_qualification_refs: []
  home_location_id: null
  current_status: UNKNOWN
  current_assignment_ids: []
  availability_constraint_refs: []
  status_event_ids: []
```

A resource can be:

- one actor;
- a standing team;
- a temporary team;
- a crew plus equipment;
- a vehicle and operators;
- another canon-defined unit.

This extension does not define what composition is valid for any profession.

## 5. Resource status event

```yaml
resource_status_event:
  status_event_id: null
  resource_id: null
  occurred_at: null
  observed_or_declared_by: null
  prior_status: null
  new_status: null
  location_ref: null
  assignment_ref: null
  communication_event_ref: null
  reason_ref: null
  confidence: CONFIRMED
```

Candidate neutral states:

- AVAILABLE
- HELD_FOR_ASSIGNMENT
- ASSIGNED
- ACKNOWLEDGED
- PREPARING
- EN_ROUTE
- ARRIVED
- CHECKED_IN
- ENGAGED
- CLEARING
- RETURNING
- REFIT_OR_HANDOFF
- AVAILABLE_AGAIN
- OUT_OF_SERVICE
- UNKNOWN_CONTACT

Institutions may use other vocabulary.

The Chronicle preserves the event sequence even when a dashboard later shows only current state.

## 6. Resource request

A domain owner or coordinator may request capability without yet naming a specific resource.

```yaml
resource_request:
  resource_request_id: null
  originating_need_ref: null
  requesting_owner_id: null
  created_at: null
  requested_scope: null
  requested_resource_kind: null
  required_authority_refs: []
  required_qualification_refs: []
  required_equipment_refs: []
  requested_location_ref: null
  desired_time_window: null
  status: OPEN
  candidate_resource_ids: []
  fulfillment_assignment_ids: []
```

Candidate statuses:

- OPEN
- SEARCHING
- PARTIALLY_FILLED
- FILLED
- TRANSFERRED
- CANCELLED
- NO_LONGER_REQUIRED
- UNFILLED

`RESOURCE_REQUESTED != RESOURCE_PROMISED`.

## 7. Dispatch assignment

```yaml
dispatch_assignment:
  assignment_id: null
  resource_request_id: null
  resource_id: null
  assigned_by_ref: null
  assigned_at: null
  destination_or_staging_ref: null
  task_scope: null
  domain_authority_refs: []
  known_constraints: []
  known_hazards: []
  information_snapshot_refs: []
  delivery_event_ref: null
  acknowledgement_event_ref: null
  assignment_status: ASSIGNED
  transfer_from_assignment_id: null
  transfer_to_assignment_id: null
  closure_event_id: null
```

Candidate assignment states:

- PROPOSED
- ASSIGNED
- SENT
- ACKNOWLEDGED
- DECLINED
- PREPARING
- EN_ROUTE
- ARRIVED
- ACTIVE
- TRANSFER_PENDING
- TRANSFERRED
- CLEARING
- CLOSED
- CANCELLED
- UNKNOWN_CONTACT

A dispatch assignment never grants authority not already referenced through `domain_authority_refs`.

## 8. Acknowledgement

```yaml
assignment_acknowledgement:
  acknowledgement_id: null
  assignment_id: null
  occurred_at: null
  actor_or_resource_id: null
  acknowledgement_type: null
  communication_event_ref: null
  constraints_reported: []
  estimated_departure_or_arrival_claim: null
```

Candidate types:

- RECEIVED
- ACCEPTED
- ACCEPTED_WITH_CONSTRAINT
- DECLINED
- REQUESTED_CLARIFICATION
- UNCONFIRMED

A system may combine RECEIVED and ACCEPTED operationally. The data model keeps them separable when evidence supports the distinction.

## 9. Departure and travel

Travel remains owned by Travel/Transport when route semantics matter.

```yaml
assignment_departure:
  departure_id: null
  assignment_id: null
  resource_id: null
  departed_at: null
  origin_ref: null
  destination_ref: null
  travel_episode_ref: null
  route_claim_ref: null
```

`EN_ROUTE` is an operational state, not proof of exact coordinates.

Minecraft entity position may visualize a known location but does not authoritatively invent route progress.

## 10. Arrival and check-in

```yaml
assignment_arrival:
  arrival_id: null
  assignment_id: null
  resource_id: null
  arrived_at: null
  arrival_location_ref: null
  arrival_observer_ref: null
  check_in_required: false
  check_in_event_id: null
  current_assignment_scope_confirmed: false
```

```yaml
incident_check_in:
  check_in_id: null
  assignment_id: null
  resource_id: null
  occurred_at: null
  location_ref: null
  receiving_actor_or_structure_ref: null
  assignment_scope_ref: null
  communication_event_ref: null
```

A resource may arrive without a formal check-in if local procedure does not require one.

No universal ICS-style structure is canonized.

## 11. Field update

```yaml
field_update:
  field_update_id: null
  assignment_id: null
  occurred_at: null
  source_resource_id: null
  communication_event_ref: null
  observation_claims: []
  status_claims: []
  requested_support: []
  scope_change_request: null
  confidence_notes: []
```

Field updates are reports from the resource. They may cause domain owners to update authoritative state, but they do not do so automatically.

Example:

A repair crew reports that a fallen object has been removed. Roads may then verify and reopen the route. The report alone is not `ROAD_OPEN`.

## 12. Assignment transfer

```yaml
assignment_transfer:
  transfer_id: null
  source_assignment_id: null
  destination_assignment_id: null
  initiated_at: null
  effective_at: null
  outgoing_resource_id: null
  incoming_resource_id: null
  transfer_scope: null
  handoff_record_refs: []
  custody_refs: []
  accepted_by_incoming_ref: null
  status: PENDING
```

Candidate states:

- PENDING
- ACCEPTED
- EFFECTIVE
- PARTIAL
- FAILED
- CANCELLED

`TRANSFER_INITIATED != RESPONSIBILITY_TRANSFERRED`.

## 13. Completion report

```yaml
assignment_completion_report:
  completion_report_id: null
  assignment_id: null
  reported_at: null
  reporting_resource_id: null
  completed_scope_claim: null
  unresolved_scope_claims: []
  domain_result_refs: []
  evidence_refs: []
  recommended_follow_up_refs: []
```

The completion report can be truthful and still not satisfy the authoritative owner’s closure rule.

## 14. Assignment closure

```yaml
assignment_closure:
  closure_id: null
  assignment_id: null
  closed_at: null
  closed_by_ref: null
  closure_reason: null
  domain_completion_refs: []
  remaining_need_refs: []
  transfer_refs: []
  post_assignment_requirements: []
```

Candidate reasons:

- COMPLETED_CONFIRMED
- PARTIAL_SCOPE_COMPLETE
- TRANSFERRED
- CANCELLED_BEFORE_DEPARTURE
- CANCELLED_EN_ROUTE
- NO_LONGER_REQUIRED
- UNABLE_TO_COMPLETE
- SUPERSEDED
- DUPLICATE_MERGED

The original request may remain open even after one assignment closes.

## 15. Release and renewed availability

```yaml
resource_release:
  release_id: null
  resource_id: null
  assignment_id: null
  released_at: null
  released_by_ref: null
  destination_or_next_state: null
  required_post_assignment_steps: []
  next_availability_claim: null
```

Possible post-assignment states:

- RETURNING
- HANDOFF_REQUIRED
- REFIT_REQUIRED
- REST_REQUIRED
- DEBRIEF_REQUIRED
- EQUIPMENT_RETURN_REQUIRED
- AVAILABLE_AGAIN
- OUT_OF_SERVICE

The extension does not invent fatigue mechanics. `REST_REQUIRED` exists only if an authored institutional/world rule creates it.

## 16. Duplicate and related requests

Several requests can refer to the same underlying event.

```yaml
request_relationship:
  relationship_id: null
  request_a_id: null
  request_b_id: null
  relationship_type: null
  decided_at: null
  decided_by_ref: null
  evidence_refs: []
  confidence: null
```

Candidate relationship types:

- POSSIBLE_DUPLICATE
- SAME_DOMAIN_EVENT_CONFIRMED
- RELATED_CASCADE
- DIFFERENT_EVENTS
- UNKNOWN

Merging requests should preserve every original intake record and timestamp.

## 17. Information snapshots

Assignments must preserve what the resource was told at the time.

```yaml
assignment_information_snapshot:
  snapshot_id: null
  assignment_id: null
  created_at: null
  source_request_refs: []
  verified_domain_state_refs: []
  unverified_claim_refs: []
  destination_claim: null
  known_hazard_refs: []
  known_access_refs: []
  privacy_or_disclosure_scope_refs: []
```

Later discoveries append new snapshots or field updates.

Do not silently rewrite the initial briefing.

## 18. Communications loss

If contact is lost:

1. preserve last confirmed resource status;
2. create `UNKNOWN_CONTACT` only when the relevant owner’s process supports that interpretation;
3. preserve attempts to contact as communication events;
4. do not infer injury, abandonment, arrival or mission failure;
5. allow a later delayed update to reconcile chronology.

This produces stories where the player must discover what happened without the world becoming omniscient.

## 19. Multi-assignment travel

One resource may carry several compatible assignments if its owner permits it.

```yaml
multi_assignment_trip:
  trip_id: null
  resource_id: null
  assignment_ids: []
  travel_episode_ref: null
  ordering_policy_ref: null
  current_sequence: []
  deviation_event_ids: []
```

The assignments remain independent. Completing one does not complete the others.

## 20. Mutual support and borrowed resources

A resource can belong to one institution and temporarily support another.

```yaml
support_resource_episode:
  support_episode_id: null
  resource_id: null
  home_owner_id: null
  receiving_owner_id: null
  request_ref: null
  approved_scope: null
  start_at: null
  end_at: null
  authority_refs: []
  return_requirements: []
```

No mutual-aid regime is assumed. This structure activates only where canon establishes such cooperation.

## 21. Player-facing integration

Mission Grammar may expose state through:

- a job board;
- a workplace coordinator;
- a Ranger-style institutional office if canon supports one;
- a personal request;
- a communications message;
- an emergency staging site;
- a field reassignment;
- a delayed request discovered later.

Suggested journal views:

`AVAILABLE REQUEST`

A request exists and the player may be eligible to accept it.

`ASSIGNED`

The player/team has been assigned but has not necessarily departed.

`EN ROUTE`

The world has recorded departure/travel state.

`ON SCENE`

Arrival has been recorded. This does not imply objective completion.

`TRANSFERRED`

Responsibility moved elsewhere.

`CLOSED`

The assignment closed under its owner’s rule.

The UI must not invent these states from player coordinates alone.

## 22. Failure-forward design

Operational failure should usually change state instead of deleting the story.

Examples:

- late arrival → original condition changed; mission becomes assessment or recovery;
- resource unavailable → request remains open or transfers;
- route blocked → dispatch record remains valid while Travel creates a new constraint;
- target already moved → Search/Travel creates a new lead;
- assignment declined → another resource may be requested;
- partial completion → remainder becomes a new or transferred scope;
- communications lost → last confirmed state remains while a check becomes necessary.

## 23. NPC and faction patterns

### The Calm Coordinator

Knows what is confirmed and what is merely reported. Provides confidence without pretending to be omniscient.

### The Field Resource Who Hates Being Double-Booked

Creates believable friction around availability without becoming lazy or antagonistic.

### The Local Expert Who Is Never the Dispatcher

May understand the terrain better than the institution assigning work. Good source of scope corrections and alternate approaches.

### The Resource Keeper

Tracks where teams, vehicles or specialized equipment actually are. Their importance appears during multi-incident days.

### The Returning Crew

Recurring NPC team whose availability changes with previous assignments. They can become familiar world actors without needing to be rivals.

### Competing institutional priorities

Two owners may both need the same limited resource. The story can arise from legitimate priority conflict rather than corruption.

## 24. Quest seeds enabled by the architecture

### The Assignment With No Departure

The board shows a team as assigned. The team acknowledged, but a route restriction prevented departure. The unresolved need survived because another system treated “assigned” as “handled.”

### Three Requests at the Same Bridge

A transport user reports blockage, a Grid worker reports damaged infrastructure and a nearby household reports frightened Pokémon. Evidence may reveal one cascade or several independent problems.

### The Resource That Cleared Twice

One record means “clear of immediate task”; another means “released from the incident.” Both statements are correct.

### The Late Message

A communications outage delays an original request until after the world state changes. The player is sent to verify rather than reenact an obsolete objective.

### The Team That Arrived Before the Assignment

A nearby crew independently encounters the situation and begins only actions it is already authorized to perform. Formal assignment catches up later.

### The Handoff at the Old Staging Site

A transfer is scheduled at a location that has since moved. Both teams follow valid but differently dated information.

## 25. Long-term arc — A Region Learns Where Its Teams Are

Phase 1 establishes ordinary institutional work. Field crews, volunteer teams, inspectors, researchers or Rangers if canonized leave workplaces and return later.

Phase 2 introduces a day with several unrelated requests. The player observes that availability, communications and travel matter as much as raw capability.

Phase 3 introduces one cascade. Several reports partially overlap. One resource is delayed; another reaches the site but lacks authority for part of the problem; a third is redirected.

Phase 4 resolves the immediate event while preserving old request records, changed staffing, borrowed equipment and revised handoff practices.

Phase 5 revisits the system months later. The region may have changed staging habits, contact methods or resource-sharing agreements, but only if those consequences were established through play.

The arc does not require a villain.

## 26. Encounter implementation contracts

### Encounter A — Response Team Withdrawal Corridor

Premise:

A field team is already performing noncombat work when a separate tactical threat emerges. Their current assignment pauses while they withdraw.

Full intended version:

- responders withdraw in stages;
- combatants can protect routes;
- Intercept may matter;
- forced movement near civilians/equipment may matter;
- temporary protected corridor or hazard zones may change tactical choices;
- AI understands WITHDRAW/PROTECT/CLEAR_ROUTE.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline
- base movement legality — VERIFIED baseline
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED baseline
- action economy/initiative — VERIFIED baseline
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for exact legal statuses
- terrain/weather/hazards/zones/reactions — BLOCKING for rich corridor semantics
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED baseline
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced READY version:

1. The field assignment pauses outside battle.
2. Responders, records, controlled equipment and noncombatant Pokémon withdraw before BattleSpec creation.
3. Ouros selects explicit combatants.
4. Static reviewed geometry is supplied to AutoPTU.
5. Tactical victory may create only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR`.
6. Dispatch/domain owners separately decide whether the original team returns, transfers or closes its work.

`TACTICAL_VICTORY != ASSIGNMENT_COMPLETE`.

### Encounter B — Staging-Site Access Chokepoint

Premise:

A resource has been assigned to a staging site, but a separate tactical threat blocks immediate access.

Full intended version dependencies:

Same permanent families as Encounter A, with rich versions requiring protected access lanes, staged arrivals and objective-aware AI.

Reduced READY version:

1. Resource remains outside BattleSpec and status is `ARRIVAL_BLOCKED` or equivalent authored state.
2. AutoPTU resolves only the chokepoint.
3. Victory creates `IMMEDIATE_APPROACH_CLEAR`.
4. The resource owner records arrival/check-in afterward.

Victory never counts as resource arrival, check-in or incident command transfer.

### Encounter C — En-Route Assignment Diversion

Premise:

A travelling response resource is redirected because another urgent problem is discovered nearby.

Full intended version:

Could combine travel, tactical contact, moving escort targets, turn-sensitive decision windows and later reassignment.

Reduced READY version:

1. Travel pauses at an authored location before battle.
2. Dispatch decision occurs in world state.
3. The resource’s noncombat equipment/personnel remain outside BattleSpec unless individually selected as legal combatants.
4. AutoPTU resolves a static encounter.
5. Travel and assignment systems resume afterward.

Battle outcome never decides which incident has higher priority.

### Encounter D — Field Handoff Perimeter

Premise:

Two resources are transferring responsibility when a tactical threat interrupts the physical meeting.

Full intended version:

Could need escort, protected-object zones, reactions, staged withdrawal and handoff-aware AI.

Reduced READY version:

1. Responsibility transfer remains `PENDING` outside battle.
2. Sensitive records/equipment/custody objects remain outside BattleSpec.
3. Both resource groups withdraw if they are not combatants.
4. AutoPTU resolves the perimeter.
5. The handoff resumes separately.

`PERIMETER_CLEAR != HANDOFF_EFFECTIVE`.

## 27. Minecraft / Cobblemon presentation boundary

Minecraft/Cobblemon may visualize:

- an office board;
- a staging area;
- a crew leaving a building;
- a vehicle or mount already selected by Ouros;
- an NPC waiting at a meeting point;
- an empty resource bay;
- equipment being returned;
- a team reappearing after an assignment;
- changed signage or temporary coordination spaces.

Minecraft observations must not create authoritative operational state.

Examples:

- an NPC loaded near a site does not prove arrival;
- a despawn does not prove departure;
- physical proximity between teams does not complete a handoff;
- an entity holding an item does not prove custody transfer;
- a redstone signal does not become an emergency request;
- a chat message does not automatically count as verified dispatch acknowledgement;
- Cobblemon BattleState never selects responders, establishes mission authority or resolves world consequences.

Ouros remains authoritative for combatants and world facts. AutoPTU remains authoritative for tactical battle resolution.

## 28. PTU / Caelo mechanics guardrail

Keep UNKNOWN unless a governing source and current implementation contract verify them:

- universal dispatch or emergency-response actions;
- universal response-time mechanics;
- generic rescue checks;
- generic carry/drag/evacuation checks;
- Command or Focus automatically granting dispatch authority;
- General Education automatically determining incident priority;
- Medicine automatically granting emergency-service authorization;
- Survival automatically locating every reported actor;
- Technology Education automatically operating every communications system;
- Trainer Classes functioning as institutional ranks;
- Features granting universal command authority;
- Pokémon species granting responder qualification;
- Type-based automatic occupational competence;
- Abilities/Moves automatically detecting incidents, authenticating reports or deciding priority;
- initiative order acting as dispatch order;
- battle victory closing a request or assignment.

## 29. Canon questions deliberately left open

- Which Ouros institutions can receive response requests?
- Do any regions have dedicated dispatch centers?
- Are jobs assigned centrally, locally, informally or through mixed systems?
- Does a Ranger-like institution exist anywhere?
- Which services use formal check-in at incidents?
- Which response-resource states are publicly visible?
- What information is private?
- Who can prioritize competing requests?
- What authority can be delegated during an incident?
- Which organizations share resources?
- What technologies support field communication?
- What happens when communications are unavailable?
- Which recurring crews, Rangers, volunteers or field teams are canon NPCs?
- Are response records archived, and by whom?

## 30. Canon-promotion rule

Everything in this document remains PROPOSED until an Ouros authority document explicitly promotes a specific institution, procedure, vocabulary, resource type, jurisdiction or historical incident.

The continuity schema can be adopted without canonizing any particular emergency-services model.