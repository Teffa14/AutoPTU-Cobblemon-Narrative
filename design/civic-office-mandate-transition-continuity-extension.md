# Civic Office, Mandate & Transition Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Date: 2026-08-29

## Purpose

This extension preserves institutional continuity when an authored civic or organizational role changes holder, becomes temporarily vacant, receives acting coverage, or delegates a bounded responsibility.

It operates only after another canon source has established that the role exists and has a mandate.

It does not define elections, appointments, inheritance, terms, removal procedures, councils, mayors, League government or any universal political model.

## Ownership boundaries

Civic Governance owns civic bodies, proposals, consultations, decision procedures and public-works authorization.

Credentials/Authorization owns credentials and access where those systems already govern them.

Archives/Records owns preserved records, access and provenance.

Public Notices owns publication and notice state.

Workplace/Institution owners manage staffing and ordinary role coverage.

Memorial/Absence/Succession surfaces a vacancy created by absence or confirmed loss.

Public Adjudication owns review or contested decisions where a canon body has that mandate.

This extension owns the continuity bridge between an existing role-holder state and the effective transfer, acting coverage, delegation, handoff and pending-work lineage that follows.

## Core principle

An office and its holder are separate persistent objects.

```yaml
institutional_office:
  office_id: null
  institution_id: null
  public_title: null
  mandate_ref: null
  geographic_scope_refs: []
  service_scope_refs: []
  governing_transition_rule_ref: null
  current_holder_ref: null
  current_holder_state_ref: null
  active_delegation_refs: []
  institutional_channel_refs: []
  office_record_collection_ref: null
  canon_reference_ids: []
```

The existence of this object creates no authority by itself. `mandate_ref` must point to authored canon.

## Holder episode

Every period in which an actor occupies or covers an office is versioned.

```yaml
office_holder_episode:
  holder_episode_id: null
  office_id: null
  actor_id: null
  holder_kind: PERMANENT
  source_decision_ref: null
  effective_from: null
  expected_end: null
  effective_until: null
  mandate_scope_ref: null
  public_notice_refs: []
  credential_refs: []
  predecessor_episode_ref: null
  successor_episode_ref: null
  status: ACTIVE
```

Candidate `holder_kind` values are descriptive and require a governing local rule:

- PERMANENT
- ACTING
- INTERIM
- DELEGATED_FOR_SCOPE
- CARETAKER
- UNKNOWN

These labels do not carry universal powers.

## Transition episode

```yaml
office_transition_episode:
  transition_id: null
  office_id: null
  trigger_ref: null
  governing_rule_ref: null
  prior_holder_episode_ref: null
  candidate_or_successor_refs: []
  result_or_selection_ref: null
  result_known_at: null
  authority_effective_at: null
  outgoing_authority_ends_at: null
  incoming_holder_episode_ref: null
  acting_coverage_refs: []
  delegation_refs: []
  record_handoff_ref: null
  credential_handoff_ref: null
  pending_matter_handoff_ref: null
  notice_refs: []
  unresolved_questions: []
  status: OPEN
```

Possible status values:

- EXPECTED
- OPEN
- RESULT_KNOWN
- HANDOVER_IN_PROGRESS
- EFFECTIVE
- PARTIALLY_COMPLETE
- COMPLETE
- DISPUTED
- CANCELLED
- UNKNOWN

Status names record workflow state only. They do not create legal meaning.

## Mandatory temporal separations

The system must preserve distinct clocks when the local institution actually uses them.

`RESULT_KNOWN != AUTHORITY_EFFECTIVE`

`OUTGOING_TERM_END != RECORDS_PHYSICALLY_TRANSFERRED`

`NEW_HOLDER_EFFECTIVE != PUBLIC_DIRECTORY_UPDATED`

`CREDENTIAL_ISSUED != CREDENTIAL_ACTIVE`

`OLD_CREDENTIAL_INACTIVE != OLD_RECORD_ARCHIVED`

`FIRST_MEETING_HELD != TRANSITION_COMPLETE`

A settlement can therefore contain temporarily inconsistent public artifacts without any record being fraudulent.

## Governing transition route

```yaml
transition_route:
  transition_rule_id: null
  office_id: null
  rule_type: AUTHORED
  initiating_conditions: []
  eligible_actor_rule_ref: null
  selecting_body_ref: null
  selection_method_ref: null
  effective_time_rule_ref: null
  acting_coverage_rule_ref: null
  challenge_or_review_ref: null
  source_canon_ref: null
```

The generator must never populate `selection_method_ref` from genre expectations.

It cannot assume:

- election;
- appointment;
- heredity;
- seniority;
- promotion;
- duel;
- League rank;
- Gym status;
- wealth;
- faction popularity;
- Trainer level.

## Acting coverage

Temporary coverage must preserve its own scope.

```yaml
acting_coverage:
  acting_id: null
  office_id: null
  actor_id: null
  source_rule_ref: null
  source_event_ref: null
  effective_from: null
  effective_until: null
  allowed_scope_refs: []
  excluded_scope_refs: []
  routine_service_refs: []
  exceptional_decision_refs: []
  reporting_obligation_refs: []
  status: ACTIVE
```

Important invariants:

`ACTING_HOLDER != PERMANENT_SUCCESSOR`

`ROUTINE_COVERAGE != FULL_MANDATE`

`VACANCY != SERVICE_STOPPED`

`SERVICE_CONTINUES != ALL_DECISIONS_ALLOWED`

`ACTING_AUTHORITY_EXPIRED != PRIOR_ACTION_ERASED`

## Delegation packet

Delegation transfers a bounded task or decision scope without transferring the office.

```yaml
office_delegation:
  delegation_id: null
  office_id: null
  delegating_holder_episode_ref: null
  delegate_actor_id: null
  delegated_scope_refs: []
  retained_scope_refs: []
  starts_at: null
  expires_at: null
  termination_trigger_refs: []
  notice_refs: []
  resulting_action_refs: []
  status: ACTIVE
```

Required boundaries:

`DELEGATION_GRANTED != OFFICE_TRANSFERRED`

`ONE_PROJECT_DELEGATED != ALL_PROJECTS_DELEGATED`

`DELEGATE_VISIBLE != DELEGATE_IS_SUCCESSOR`

`DELEGATION_ENDED != RESULT_REVERSED`

## Record handoff

```yaml
office_record_handoff:
  handoff_id: null
  office_id: null
  outgoing_holder_episode_ref: null
  incoming_holder_episode_ref: null
  office_record_collection_ref: null
  item_manifest_refs: []
  restricted_record_refs: []
  personal_material_refs: []
  custody_events: []
  access_events: []
  missing_reference_refs: []
  archived_snapshot_ref: null
  completed_at: null
  status: PENDING
```

Possible status values:

- PENDING
- INVENTORIED
- PARTIAL_TRANSFER
- CUSTODY_TRANSFERRED
- ACCESS_CONFIGURED
- COMPLETE
- DISPUTED
- UNKNOWN

Required boundaries:

`OFFICE_RECORD != PERSONAL_RECORD`

`CUSTODY_TRANSFERRED != PUBLIC_ACCESS`

`ARCHIVED != DELETED_FROM_HISTORY`

`MISSING_FROM_HANDOFF != DESTROYED`

`OUTGOING_HOLDER_HAS_COPY != OUTGOING_HOLDER_HAS CURRENT_AUTHORITY`

## Institutional channels

A public desk, notice board, mailbox, radio frequency, portal or account can belong to the office rather than the individual.

```yaml
institutional_channel_continuity:
  channel_id: null
  office_id: null
  prior_operator_refs: []
  current_operator_refs: []
  archived_content_ref: null
  current_content_ref: null
  access_credential_refs: []
  public_identity_state: ACTIVE
  transition_events: []
```

A channel may continue while its operator changes.

Minecraft representation of a sign or NPC does not determine channel authority.

## Pending matters

Projects and decisions can span holder episodes.

```yaml
pending_matter_handoff:
  handoff_id: null
  office_id: null
  transition_id: null
  matter_refs: []
  matter_state_at_transition: []
  prior_decision_refs: []
  pending_deadline_refs: []
  delegated_scope_refs: []
  receiving_actor_refs: []
  review_required_refs: []
  continuity_notes: []
```

Each matter keeps the owner system that already governs it.

Examples:

- Construction keeps project phase.
- Civic Governance keeps proposal/decision state.
- Conservation keeps management objective state.
- Public Adjudication keeps review state.
- Maintenance keeps work order state.
- Temporary Events keeps event preparation state.

The transition layer only records who must receive context and which authority applies after the effective time.

## Decision lineage across holders

A decision made by a valid prior holder remains a historical decision unless an authored review, expiry or replacement route changes it.

```yaml
cross_holder_decision_lineage:
  decision_id: null
  deciding_holder_episode_ref: null
  mandate_ref_at_decision_time: null
  decision_effective_from: null
  implementation_owner_ref: null
  successor_review_ref: null
  superseding_decision_ref: null
```

Required boundaries:

`NEW_HOLDER != OLD_DECISION_VOID`

`OLD_DECISION_EXISTS != NEW_HOLDER_ENDORSES_IT`

`IMPLEMENTED_UNDER_SUCCESSOR != DECIDED_BY_SUCCESSOR`

`REVIEW_STARTED != DECISION_REVERSED`

## Public notice continuity

Public-facing identity may lag behind effective state.

Useful artifacts:

- office door nameplate;
- public directory;
- notice-board signature;
- meeting agenda;
- archived website/account;
- service desk roster;
- project update;
- historical plaque.

Each has its own timestamp and owner.

`OLD_NAME_VISIBLE != OLD_HOLDER_CURRENT`

`NEW_NAME_POSTED != EVERY_BACKEND_HANDOFF_COMPLETE`

`NOTICE_SIGNED_BEFORE_TRANSITION != NOTICE_PUBLISHED_BEFORE_TRANSITION`

## Faction and NPC continuity

A transition can alter relationship edges without rewriting character identity.

Candidate persistent changes:

- an outgoing holder returns to an ordinary profession;
- a former rival remains a committee member or civic participant;
- an incoming holder inherits a project they opposed while campaigning;
- a long-serving operator becomes the practical memory source;
- an acting holder returns to their prior role;
- archive staff become important because two administrations used different record conventions.

The system must not infer resentment, loyalty, corruption or grief without authored evidence.

## Noncombat scene grammar

### Handover morning

1. establish current office holder and effective clock;
2. inventory records and active matters;
3. identify unresolved access or missing references;
4. transfer only authorized custody/access;
5. publish updated public information through the proper owner;
6. later revisit the office and show persistent changes.

### Acting week

1. vacancy or temporary absence occurs;
2. governing rule activates bounded coverage;
3. routine services continue;
4. an exceptional request exposes the acting limit;
5. another owner or authored decision route handles that question;
6. acting episode closes without implying permanent succession.

### Project across administrations

1. old holder participates in valid decision;
2. project begins or awaits implementation;
3. transition occurs;
4. pending-matter packet preserves commitments and unresolved questions;
5. successor reviews only where a valid review path exists;
6. implementation or supersession produces visible world change;
7. archives preserve both administrations' records.

## Mystery grammar

### Two Names on One Office

One directory updates at authority-effective time. Another updates after the first meeting. Both records are historically correct for their own timestamps.

### The Signature After the Term

A notice carries the outgoing holder's signature but was posted after the transition. Investigation shows it was signed before the effective date and queued for publication.

### The Project Nobody “Started”

Proposal approval occurred under one holder, procurement under acting coverage and physical construction under the successor. Residents remember three different starts.

### The Acting Holder Who Could Not Sign

The acting actor validly handled routine operations but one exceptional decision remained outside the temporary scope.

## Long-term story arc — A Town Learns Which Things Belong to the Office

Phase 1 establishes an ordinary office through practical routines rather than exposition.

Phase 2 introduces a known future transition or temporary absence.

Phase 3 reveals institutional seams: old signage, pending matters, one incomplete handoff packet and staff with different pieces of context.

Phase 4 lets the players help reconstruct records, deliver a handoff, inspect a pending project or clarify a delegated scope.

Phase 5 shows the new holder making one genuinely new decision while inherited work continues separately.

Phase 6 revisits the town months later. Some visual details changed, some projects continued unchanged, former candidates or office-holders still have ordinary lives, and archives preserve the earlier period.

The arc works regardless of whether the local transition is electoral, appointed, rotational or another canon-approved form.

## Encounter contract — Transition Archive Handoff Perimeter

Narrative premise:

An unrelated conflict blocks physical access while an authorized records handoff is scheduled. The records themselves must not become tactical loot.

### Full intended version

Potential mechanics:

- protected courier/records route;
- Intercept and escort movement;
- phased withdrawal of staff;
- protected zones or reactions around a secure entrance;
- objective-aware AI using `PROTECT`, `WITHDRAW` or `CLEAR_ROUTE`;
- semantic adapter playback for handoff pause/resume state.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL where ordinary legal statuses occur
- terrain/weather/hazards/zones/reactions — BLOCKING when protected zones/reactions matter
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full status: BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Contract:

- Ouros pauses the records handoff before BattleSpec construction;
- records, manifests, credentials, couriers, clerks and noncombatants leave the tactical space or remain behind secured world-state boundaries;
- BattleSpec contains only explicit legal combatants and static geometry;
- victory secures immediate physical access only;
- the authorized record owner resumes or reschedules the handoff afterward.

Forbidden transitions:

- victory => records authenticated;
- victory => custody transferred;
- victory => office authority effective;
- victory => credentials activated;
- victory => transition complete.

## Encounter contract — Public Meeting Evacuation

Narrative premise:

A public meeting connected to a transition must evacuate because of an unrelated tactical incident.

### Full intended version

Potential mechanics:

- active civilian withdrawal;
- protected exits;
- Intercept or forced displacement;
- timed departure waves;
- objective-aware tactical policy;
- semantic Minecraft playback.

Dependencies use the same permanent categories above. Complete movement and lifecycle are PARTIAL; terrain/zones/reactions, tactical policy and adapter/playback are BLOCKING when used.

### Reduced version

Status: READY.

Ouros adjourns the meeting and removes all attendees, records and officials from BattleSpec first. A static battle then occurs in a cleared adjacent area.

Victory cannot:

- decide a vote;
- choose an office-holder;
- satisfy quorum;
- count as public support;
- complete consultation;
- alter an authored transition rule.

## Encounter contract — Pending Project Access Diversion

Narrative premise:

A project inherited across a transition cannot be inspected because a conventional conflict blocks the route.

### Full intended version

The rich version may use escort, route protection, forced movement, hazards and objective-aware AI.

### Reduced version

Status: READY.

Inspectors remain outside BattleSpec. Players clear a static chokepoint. The project owner decides later whether inspection occurs.

Victory does not approve, cancel, inherit, review or complete the project.

## PTU/Caelo guardrails

The extension introduces no tactical political mechanics.

Unknown unless validated by exact source and current implementation:

- universal election/social influence checks;
- office eligibility based on Trainer class;
- battle as an office-selection method;
- Badges as civic mandate;
- Pokémon species as automatic office agents;
- Aura/Psychic truth verification;
- universal Command/Charm/Guile thresholds for public support;
- Trainer Features that create governmental authority;
- Loyalty as constituency support;
- Items or Moves that authenticate civic records.

A battle contract may affect only physical access or safety unless an independently authored world rule says more.

## Minecraft/Cobblemon boundary

Minecraft can display:

- changed desk occupant;
- old and new nameplates with timestamps;
- boxes or shelves representing records already placed by Ouros;
- updated notice boards;
- changed NPC schedules;
- archived office rooms;
- a former office-holder elsewhere in town;
- project boards spanning two holder episodes.

It cannot decide:

- who holds office;
- whether authority is effective;
- whether a credential is valid;
- whether a delegation exists;
- whether a record transfer occurred;
- whether a notice was received;
- whether a decision remains valid;
- who may vote or select a successor.

Cobblemon/Minecraft BattleState remains outside combatant selection, legality, HP/status, tactical positions and all civic facts.

## Promotion gate

Before promoting any Ouros-specific office or transition practice to canon, require explicit answers for:

- institution and geography;
- office title;
- mandate;
- holder-selection rule;
- vacancy/acting rule;
- effective-time rule;
- delegation authority;
- record custody/access;
- credential lifecycle;
- public notice practice;
- review/challenge route if any;
- relationship to League, Gym, settlement, faction or other institutions;
- Minecraft-visible representation.

No missing answer should be filled from generic real-world assumptions.