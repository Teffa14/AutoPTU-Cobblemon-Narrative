# Community Aid, Volunteer Capacity & Mutual Support Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models employment, clubs, crisis response, civic decisions, appointments, credentials, finance, procurement, public events and public memory. This extension covers a narrower missing lifecycle: people choosing to help with a bounded community need without that participation automatically becoming employment, permanent membership, formal authority or proof of professional qualification.

The layer owns participation intent, availability, helper intake, role matching, temporary commitments, check-in, handoff, withdrawal and contribution history. The specialist system that owns the underlying problem remains authoritative.

## Core separation

Keep these concepts distinct:

- a need exists;
- someone asks for help;
- an actor offers to help;
- the actor is available;
- the actor is suitable for one role;
- the actor is authorized for one role;
- the actor commits to one window;
- the actor actually checks in;
- the actor performs an observed contribution;
- the actor completes, hands off or withdraws;
- the owning system completes the underlying project;
- others know about the contribution.

None of these states implies employment, friendship, moral virtue, authority, mechanical progression or future obligation.

## 1. Community aid need

```yaml
community_aid_need:
  aid_need_id: null
  owner_system: null
  owner_state_ref: null
  coordinating_institution_id: null
  location_refs: []
  purpose_summary: null
  requested_role_slots: []
  requested_resource_refs: []
  start_window: null
  expected_end_window: null
  current_state: draft
  participation_risk_band: ordinary
  public_call_ref: null
  dependency_refs: []
  history_event_refs: []
```

Suggested states:

- DRAFT
- VALIDATED
- CALL_OPEN
- PARTIALLY_COVERED
- COVERED
- ACTIVE
- PAUSED
- NEED_CHANGED
- CALL_CLOSED
- HANDED_BACK
- COMPLETED_BY_OWNER_SYSTEM
- CANCELED
- ARCHIVED

`COMPLETED_BY_OWNER_SYSTEM` matters. Helpers can finish their assignments while the actual repair, event, crisis, survey or service remains incomplete.

## 2. Aid role slot

```yaml
aid_role_slot:
  role_slot_id: null
  aid_need_id: null
  role_label: null
  task_scope: []
  location_scope_refs: []
  requested_headcount: null
  qualification_refs: []
  credential_scope_refs: []
  supervision_requirement: null
  equipment_refs: []
  access_refs: []
  risk_band: ordinary
  role_state: open
```

A role slot describes the permitted task. It does not create competence.

Examples of potentially low-risk roles when the owner system permits them:

- direct visitors toward the correct desk;
- distribute already-authorized supplies;
- carry labeled non-specialist materials;
- record attendance;
- sort ordinary donated goods;
- prepare a public room before an event;
- collect litter in an open safe zone;
- read public notices to visitors;
- deliver food to an authorized staging table;
- observe a route segment and report visible conditions.

Examples that require specialist-system validation rather than generic volunteer status:

- medical treatment;
- structural assessment;
- electrical isolation;
- formal evidence handling;
- hazardous-material handling;
- rescue inside an active hazard zone;
- protected-site access;
- regulated research procedures;
- official battle adjudication;
- authority to detain, inspect or compel another actor.

## 3. Helper offer

```yaml
helper_offer:
  helper_offer_id: null
  aid_need_id: null
  actor_id: null
  offered_role_refs: []
  availability_windows: []
  stated_limits: []
  equipment_offer_refs: []
  transport_limit_refs: []
  qualification_claim_refs: []
  credential_refs: []
  status: offered
  source_event_ref: null
```

Suggested statuses:

- OFFERED
- PENDING_REVIEW
- ACCEPTED_FOR_ROLE
- WAITLISTED
- DECLINED_FOR_ROLE
- WITHDRAWN_BEFORE_COMMITMENT
- EXPIRED

`DECLINED_FOR_ROLE` is not a negative social judgment. The actor may be unsuitable for that task and suitable for another one.

## 4. Availability is time-scoped

```yaml
helper_availability:
  actor_id: null
  available_window: null
  location_constraint_refs: []
  existing_commitment_refs: []
  self_reported_limits: []
  transport_state_ref: null
  current_state: available
```

Possible states:

- AVAILABLE
- AVAILABLE_WITH_LIMITS
- COMMITTED_ELSEWHERE
- TRAVEL_BLOCKED
- UNAVAILABLE
- UNKNOWN

The generator must not assume an actor is available because they helped previously or are physically nearby.

## 5. Suitability and role review

```yaml
helper_role_review:
  review_id: null
  helper_offer_id: null
  role_slot_id: null
  qualification_checks: []
  credential_checks: []
  equipment_checks: []
  supervision_available: false
  result: suitable|suitable_with_supervision|alternate_role|insufficient_evidence|not_suitable
  decision_ref: null
  reviewer_ref: null
```

Willingness does not waive qualification requirements. Friendship with an organizer does not waive them either.

## 6. Aid commitment

```yaml
aid_commitment:
  commitment_id: null
  aid_need_id: null
  actor_id: null
  role_slot_id: null
  planned_start: null
  planned_end: null
  actual_start: null
  actual_end: null
  supervisor_ref: null
  check_in_required: false
  status: planned
  handoff_required: false
  source_ref: null
```

Suggested lifecycle:

`PLANNED -> CONFIRMED -> CHECKED_IN -> ACTIVE -> COMPLETED | HANDED_OFF | WITHDRAWN | RELEASED | CANCELED`

A planned helper is not counted as physically present until check-in or another observed arrival event occurs.

## 7. Contribution episode

```yaml
contribution_episode:
  contribution_id: null
  commitment_id: null
  actor_id: null
  role_slot_id: null
  observed_actions: []
  output_refs: []
  issue_refs: []
  handoff_refs: []
  start_time: null
  end_time: null
  source_refs: []
```

Record observable work rather than a hidden altruism score.

Good records:

- sorted 12 labeled supply crates during the evening window;
- covered the public information table from 18:00 to 19:00;
- walked the east path and submitted three route observations;
- delivered prepared meals from an authorized kitchen to the staging site;
- left after the first hour and handed the attendance sheet to another helper.

Do not derive:

- friendship;
- generosity;
- heroism;
- loyalty;
- political support;
- employment status;
- permanent role ownership;
- PTU experience or progression.

## 8. Helper withdrawal and release

```yaml
aid_participation_end:
  participation_end_id: null
  commitment_id: null
  end_type: completed|handed_off|withdrew|released|site_closed|role_removed|need_canceled
  stated_reason_ref: null
  coverage_needed: false
  handoff_ref: null
  followup_ref: null
  time: null
```

A helper may leave. The system records operational consequences, not invented moral interpretation.

The generator may create a new coverage need if the role remains necessary. It must not automatically create conflict with organizers or other helpers.

## 9. Handoff

```yaml
aid_handoff:
  handoff_id: null
  from_actor_id: null
  to_actor_id: null
  role_slot_id: null
  task_state_refs: []
  observations_transferred: []
  material_custody_refs: []
  warning_refs: []
  unresolved_questions: []
  completed_time: null
```

Knowledge does not teleport between shifts. A helper who arrives later knows only what was communicated, independently observed or already public.

## 10. Cohorts and physical representation

Large efforts should use aggregate capacity when individual identity does not matter.

```yaml
aid_helper_cohort:
  cohort_id: null
  aid_need_id: null
  role_slot_id: null
  planned_count: null
  checked_in_count: null
  active_count: null
  released_count: null
  represented_actor_ids: []
```

Minecraft can materialize only the relevant helpers while retaining aggregate counts for queue pressure, coverage and world continuity.

The physical position of an NPC near a volunteer table does not prove that they signed up, checked in or accepted a task.

## 11. Existing staff and volunteers

Workplaces owns employees and occupational assignments. This layer may reference staff who coordinate helpers, but must not merge the two populations.

```yaml
participation_origin:
  paid_staff: false
  institutional_assignment: false
  community_aid_commitment: true
```

The same actor can have several roles at different times. Each role keeps its own provenance.

An employee helping outside their shift is not automatically volunteering; the employment/assignment context must be known.

## 12. Clubs and recurring groups

A club may organize a community project, but membership and aid participation are separate.

A non-member can help. A member can decline. A club's standing project may create recurring aid needs without turning every member into scheduled labor.

## 13. Crisis integration

During an active emergency:

- Crisis owns hazard truth, evacuation, staging and response priorities;
- Credentials/authorizations own specialist access;
- Workplaces owns professional staff;
- Care owns medical decisions;
- Travel owns route state;
- this extension only coordinates helpers in roles the owner system has explicitly made available.

Uncredentialed helpers must not be generated inside an active hazard merely to make a rescue scene dramatic.

## 14. Events, cleanup and ordinary return

Temporary Event Operations may create aid needs for setup, information desks, accessibility support, teardown or cleanup. Public Space/Waste/Maintenance owns the post-event physical state.

A useful lifecycle is:

`event activity -> aid cleanup call -> helper commitments -> contribution episodes -> owner-system inspection -> ordinary-return handoff`

Helpers finishing does not prove the park, venue or street is ready to reopen.

## 15. In-kind support

Food, equipment, materials and money remain specialist objects.

```yaml
in_kind_aid_reference:
  aid_need_id: null
  contributor_id: null
  item_or_batch_ref: null
  custody_transfer_ref: null
  destination_owner_system: null
```

This layer can say that an actor offered a batch of blankets or prepared meals. Material Culture, Food, Procurement, Courier, Finance or Shared Equipment decides identity, custody, acceptance and use.

## 16. Recognition and public memory

A coordinating body may publish thanks if its communication policy allows it.

Public recognition is a publication event, not a mechanical reward.

The system must not create:

- hidden reputation points;
- friendship bonuses;
- discounts;
- priority access;
- Trainer Features;
- Skill Rank growth;
- Badge progress;
- formal credential scope;
- guaranteed future favors.

Any later benefit needs its own authorized system and provenance.

## 17. Receiving aid does not create debt

Receiving community help must not create a relationship debt or obligation unless actors explicitly establish one.

A household whose walkway was cleared, a traveler given directions or an event receiving cleanup help does not automatically owe the helpers money, loyalty, votes, friendship or future labor.

## 18. Pokémon agency boundary

A Pokémon is an actor, not equipment or a generic labor capability.

Before assigning a Pokémon a contribution role, require relevant evidence such as:

- individual observed behavior;
- relationship/agency state;
- authoritative movement capability;
- relevant Move/Ability/Capability/Skill evidence where mechanics matter;
- supervision/consent structure established by the applicable system.

Never infer construction, lifting, medical, rescue, navigation, detection or logistics competency from species/type alone.

Assisting does not imply capture or ownership.

## 19. Overcommitment and fatigue

Narrative availability may become limited because an actor already has commitments. That can create schedule conflicts and coverage needs.

Do not create PTU penalties, status effects, exhaustion damage, reduced Accuracy or mechanical fatigue unless PTU/Caelo and the engine explicitly support that exact rule.

## 20. Recurring aid network

Repeated projects can create a persistent coordination history without creating a new faction automatically.

```yaml
community_support_history:
  scope_ref: null
  prior_aid_need_refs: []
  recurring_helper_actor_ids: []
  recurring_cohort_refs: []
  known_role_preferences: []
  known_availability_patterns: []
  successful_handoff_refs: []
  unresolved_capacity_gaps: []
```

These are observed patterns only. A person who has helped three times can still say no the fourth time.

## 21. Scene compression

Compress routine aid when:

- role assignment is clear;
- adequate coverage exists;
- no important relationship or knowledge handoff is changing;
- no scarce resource is involved;
- there is no meaningful decision;
- no dependency is failing.

Expand into a scene when:

- coverage is insufficient;
- several roles need different qualifications;
- a helper withdraws and the task still matters;
- the need changes after people already committed;
- physical custody or important knowledge must hand off;
- a volunteer and staff role are being confused;
- helpers disagree about boundaries;
- an incident makes the site unsafe;
- repeated participation creates a meaningful callback.

## 22. Minecraft projection

Possible visible projections:

- sign-up board tied to a real aid call;
- staging table;
- labeled role stations;
- a few representative helper NPCs;
- stored supplies already accepted by the owning system;
- changing headcount/coverage UI;
- closed volunteer table after the call ends;
- cleanup traces disappearing only after owner-system completion.

The projection follows world state. Breaking a sign or moving an NPC cannot silently edit commitments, qualifications or project completion.

## 23. Mechanically rich encounter contract

### Volunteer Staging-Site Evacuation

Full intent:

A community support site must close while helpers withdraw through multiple exits and professional responders protect the route.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if unsafe zones affect tactics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal/protection priorities;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

The aid coordinator closes the site before battle. Helpers, supplies and noncombatants leave through world state. Commitments change to PAUSED or RELEASED as appropriate. AutoPTU then resolves a conventional static battle in the cleared perimeter. Crisis/Event/Maintenance determines reopening afterward. Winning does not check helpers back in or complete the underlying aid need.

### Community Cleanup Wildlife Conflict

Full intent:

A cleanup crew and wild Pokémon occupy overlapping parts of a public space. The intended scene supports orderly withdrawal, protected material piles, multiple exits and territorial/escape behavior.

Full version additionally needs complete movement, objective-aware AI, possible zones/reactions and adapter synchronization.

Reduced version:

Cleanup pauses. Helpers and collected materials are removed from the tactical grid. A static encounter occurs only if de-escalation fails and a battle is genuinely required. Ecology/Public Space decides afterward whether the route, timing or cleanup method changes. Battle victory does not establish that the Pokémon caused earlier litter or damage.

### Rota Reconciliation

No combat required.

The player compares offers, confirmed commitments, check-ins, cancellations, handoffs and timestamps to determine why a role was uncovered. Possible outcomes include duplicate signup, stale availability, a valid withdrawal, a role reassignment or a missed handoff.

This scene can execute before the Minecraft combat adapter exists.

## Canon questions

Before promoting specific implementations, Ouros still needs canon decisions about:

- which cultures/institutions use formal volunteer calls;
- whether recurring mutual-aid groups exist;
- what terminology they use;
- which tasks accept public helpers;
- what specialist roles require credentials;
- who may open or close an aid call;
- whether any participation records are public;
- what privacy rules apply to recipients;
- whether compensation/reimbursement exists for any role;
- how meals, transport or equipment for helpers are provided;
- how Pokémon participation is culturally understood;
- whether any region has formal civic-service expectations.

Until reviewed, all names, policies and concrete organizations remain non-canon.