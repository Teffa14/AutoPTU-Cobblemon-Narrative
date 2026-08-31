# Human Employment, Recruitment, Tenure & Separation Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Research basis: `research/2026-08-31-human-employment-recruitment-tenure-separation-scan-164.md`

## Purpose

Ouros already knows what workplaces exist, what occupational roles they need, which staff are present, what assignments are active and what career entries important NPCs accumulated. This extension adds provenance for the human employment relationship itself.

The design supports persistent transitions from an open need through recruitment, selection, offer, acceptance, start, active tenure, leave or temporary coverage, return, separation and later succession or rehire.

It does not establish labor law, wage standards, contracts, dismissal rights, unions or a payroll simulator. It also does not convert employment into PTU progression.

## Authority boundary

This extension owns:

- human employment opportunities tied to an existing workplace/role;
- applications or other authored candidacies;
- selection episodes and their recorded outcomes;
- offers and offer revisions;
- acceptance, decline, withdrawal and expiration events;
- actual tenure start/end;
- onboarding state;
- responsibility-scope changes during a tenure;
- leave/return episodes when canon uses those concepts;
- evidence-backed separation records;
- rehire and successor links;
- references to compensation commitments owned by Finance;
- employment-record revisions and provenance.

This extension does not own:

- workplace definitions, staffing capacity, shifts or work assignments — Workplaces owns them;
- mechanical money, payment settlement or account balances — Finance owns them;
- Skills, Edges, Trainer Classes, Features, Moves or progression — PTU/Caelo and AutoPTU own them;
- qualifications and credentials as facts — Credentials owns them;
- training outcomes — Training/Formal Education own them;
- human identity/name authority — Human Identity owns it;
- organization membership or faction allegiance — Organization/Faction owns it;
- civic office authority — Civic Office owns it;
- equipment custody — Shared Equipment/appropriate custody layers own it;
- workplace safety — Worksite Safety owns it;
- Pokémon work assignments — Pokémon Work Role Participation owns them;
- legal enforceability or employment rights — no Ouros authority exists yet unless later canon establishes one.

## Core separation

```text
workplace staffing need
        ↓
employment opportunity
        ↓
application/candidacy
        ↓
selection episode
        ↓
employment offer
        ↓
acceptance/decline/expiry
        ↓
pre-start/onboarding preparation
        ↓
employment tenure starts
        ↓
active role + responsibility changes
        ↓
leave/coverage/return if applicable
        ↓
separation
        ↓
vacancy/handoff/successor/rehire
```

Every arrow requires explicit evidence. No state implies the next state automatically.

## 1. Employment opportunity

```yaml
employment_opportunity:
  opportunity_id: null
  workplace_id: null
  occupational_role_id: null
  staffing_need_ref: null
  opportunity_type: VACANCY | ADDITIONAL_SLOT | TEMPORARY_COVERAGE | SEASONAL | PROJECT | SUCCESSION_SEARCH
  created_at: null
  public_posting_ref: null
  referral_route_refs: []
  qualification_requirement_refs: []
  schedule_expectation_ref: null
  compensation_reference_ref: null
  status: OPEN
  close_event_ref: null
  provenance_refs: []
```

Suggested states:

- DRAFT
- OPEN
- PAUSED
- CLOSED_FILLED
- CLOSED_UNFILLED
- WITHDRAWN
- SUPERSEDED

A staffing need can exist without a public posting. A posting can remain visible after the underlying opportunity closed if the Public Notice or Media layer has not yet updated the artifact.

## 2. Application or candidacy

```yaml
employment_application:
  application_id: null
  opportunity_id: null
  actor_id: null
  submitted_at: null
  submission_route: null
  credential_refs: []
  experience_claim_refs: []
  availability_claim_ref: null
  requested_condition_refs: []
  status: RECEIVED
  withdrawal_event_ref: null
  provenance_refs: []
```

Possible states:

- DRAFT
- RECEIVED
- UNDER_REVIEW
- MORE_INFORMATION_REQUESTED
- WITHDRAWN
- NOT_SELECTED
- SELECTED_FOR_OFFER
- CLOSED

Application data records what was presented. It does not prove every claim true. Qualification validation remains evidence-based through Credentials, Training, Observation or other owning systems.

## 3. Selection episode

```yaml
employment_selection_episode:
  selection_id: null
  opportunity_id: null
  considered_application_ids: []
  decision_actor_or_body_ids: []
  governing_selection_rule_ref: null
  evidence_reviewed_refs: []
  interview_or_trial_refs: []
  decision: null
  selected_actor_id: null
  alternate_actor_ids: []
  decided_at: null
  provenance_refs: []
```

Do not invent a competitive score, exam, interview DC or fairness standard. The governing process is authored by the institution if canon needs one.

`SELECTED_FOR_OFFER` does not mean employed.

## 4. Employment offer

```yaml
employment_offer:
  offer_id: null
  opportunity_id: null
  selected_actor_id: null
  employer_institution_id: null
  workplace_id: null
  role_id: null
  issued_at: null
  proposed_start_at: null
  proposed_end_at: null
  responsibility_scope_refs: []
  schedule_expectation_ref: null
  compensation_commitment_refs: []
  condition_refs: []
  offer_version: 1
  supersedes_offer_ref: null
  status: ISSUED
  response_deadline: null
  provenance_refs: []
```

Suggested states:

- DRAFT
- ISSUED
- REVISED
- ACCEPTED
- DECLINED
- WITHDRAWN_BY_EMPLOYER
- EXPIRED
- SUPERSEDED

A revised offer preserves the earlier version. Do not silently rewrite history.

## 5. Offer response

```yaml
employment_offer_response:
  response_id: null
  offer_id: null
  actor_id: null
  response: ACCEPT | DECLINE | REQUEST_CHANGE | WITHDRAW_CANDIDACY
  response_at: null
  condition_or_note_refs: []
  provenance_refs: []
```

Acceptance establishes that the actor accepted the recorded offer version. It does not prove that the tenure began.

## 6. Pre-start and onboarding

```yaml
employment_prestart_episode:
  prestart_id: null
  accepted_offer_id: null
  actor_id: null
  planned_start_at: null
  actual_start_at: null
  onboarding_task_refs: []
  required_credential_refs: []
  equipment_issue_refs: []
  orientation_refs: []
  supervisor_actor_ids: []
  status: PENDING
  delay_reason_refs: []
  provenance_refs: []
```

Possible states:

- PENDING
- IN_PROGRESS
- START_READY
- START_DELAYED
- CANCELED_BEFORE_START
- COMPLETE

This stage can explain why a person has accepted a job but is not yet expected on the normal roster.

Onboarding tasks never grant PTU mechanics automatically.

## 7. Employment tenure

```yaml
employment_tenure:
  tenure_id: null
  actor_id: null
  employer_institution_id: null
  workplace_id: null
  role_id: null
  source_offer_id: null
  start_event_ref: null
  actual_start_at: null
  planned_end_at: null
  actual_end_at: null
  responsibility_scope_refs: []
  schedule_relationship_refs: []
  compensation_commitment_refs: []
  supervisor_or_reporting_refs: []
  active_leave_episode_refs: []
  amendment_refs: []
  separation_ref: null
  status: ACTIVE
  provenance_refs: []
```

Suggested states:

- PENDING_START
- ACTIVE
- TEMPORARILY_INACTIVE
- ON_AUTHORED_LEAVE
- TRANSFER_PENDING
- ENDED
- SUPERSEDED

A tenure is the relationship episode. Individual shifts and assignments still belong to Workplaces.

## 8. Responsibility change

```yaml
employment_tenure_amendment:
  amendment_id: null
  tenure_id: null
  effective_at: null
  change_type: RESPONSIBILITY | SCHEDULE_RELATIONSHIP | WORKPLACE_TRANSFER | ROLE_CHANGE_PENDING | SUPERVISION | OTHER_AUTHORED
  previous_state_refs: []
  new_state_refs: []
  reason_refs: []
  creates_new_tenure: false
  provenance_refs: []
```

Material role changes should usually create a new tenure rather than overwrite the previous one. Small responsibility changes can remain amendments.

Promotion is never inferred from responsibility growth unless the institution explicitly records a promotion or new role.

## 9. Leave and temporary inactivity

Ouros has not established a universal leave entitlement. The architecture can still record an authored temporary absence when one exists.

```yaml
employment_leave_episode:
  leave_id: null
  tenure_id: null
  leave_type_label: null
  authorized_by_ref: null
  planned_start_at: null
  actual_start_at: null
  planned_return_at: null
  actual_return_at: null
  coverage_assignment_refs: []
  status: PLANNED
  provenance_refs: []
```

Allowed generic states:

- PLANNED
- ACTIVE
- RETURNED
- EXTENDED
- CANCELED
- SUPERSEDED

Do not generate legal categories or entitlements. `leave_type_label` is authored world language only.

A missed shift does not automatically create a leave episode.

## 10. Return episode

```yaml
employment_return_episode:
  return_id: null
  leave_id: null
  tenure_id: null
  actual_return_at: null
  role_scope_after_return_refs: []
  schedule_after_return_ref: null
  handback_refs: []
  status: COMPLETE
  provenance_refs: []
```

Return may restore the prior arrangement, a modified arrangement or only part of the old responsibilities. Workplaces owns the resulting assignments and schedule.

## 11. Separation

```yaml
employment_separation:
  separation_id: null
  tenure_id: null
  actor_id: null
  employer_institution_id: null
  separation_type: UNSPECIFIED | RESIGNATION | RETIREMENT | DISMISSAL | FIXED_END | TRANSFER | ROLE_ELIMINATED | MUTUAL_AUTHORED | OTHER_AUTHORED
  notice_or_decision_ref: null
  effective_at: null
  last_active_work_ref: null
  handoff_refs: []
  credential_return_refs: []
  equipment_return_refs: []
  outstanding_compensation_refs: []
  successor_ref: null
  evidence_refs: []
  status: RECORDED
  provenance_refs: []
```

The type must come from explicit evidence. If evidence only establishes that employment ended, use `UNSPECIFIED`.

Do not infer firing from abrupt absence, retirement from age, resignation from a farewell, misconduct from access revocation or death from disappearance.

## 12. Rehire and recurrence

```yaml
employment_rehire_link:
  prior_tenure_id: null
  later_tenure_id: null
  actor_id: null
  same_employer: null
  same_workplace: null
  same_role: null
  gap_start: null
  gap_end: null
  provenance_refs: []
```

A returning worker receives a new tenure episode. Prior experience remains historical evidence but does not automatically restore old authority, credentials or PTU mechanics.

## 13. Succession link

```yaml
employment_succession_link:
  predecessor_tenure_id: null
  successor_tenure_id: null
  role_id: null
  workplace_id: null
  overlap_window: null
  handoff_refs: []
  vacancy_period_ref: null
  provenance_refs: []
```

This link says one tenure followed another in the same role lineage. It does not imply mentorship, approval, inheritance of reputation or identical duties.

## 14. Compensation link

Employment can reference Finance without duplicating it.

```yaml
employment_compensation_link:
  tenure_id: null
  compensation_term_ref: null
  finance_commitment_ids: []
  finance_payment_event_ids: []
  disputed_finance_ref: null
  last_reconciled_at: null
```

Core rule:

`COMPENSATION_PROMISED != COMPENSATION_PAID`

`COMPENSATION_PAID != MECHANICAL_BALANCE_UPDATED` unless the authoritative money system records that transaction.

Do not compute salary, overtime, taxes, deductions, leave pay, severance or benefits until governing canon and mechanics exist.

## 15. Employment record revision

Corrections should preserve lineage.

```yaml
employment_record_revision:
  revision_id: null
  target_record_ref: null
  correction_type: TYPO | IDENTITY_LINK | DATE_CORRECTION | STATUS_CORRECTION | SOURCE_ADDED | INTERPRETATION_REVISED
  prior_value_ref: null
  new_value_ref: null
  reason_ref: null
  changed_at: null
  provenance_refs: []
```

A corrected start date does not erase the fact that an older roster or article carried the earlier date.

## 16. Important invariants

```text
VACANCY_EXISTS != PUBLIC_POSTING_EXISTS
APPLICATION_RECEIVED != ELIGIBLE
ELIGIBLE != SELECTED
SELECTED != OFFER_ISSUED
OFFER_ISSUED != OFFER_ACCEPTED
OFFER_ACCEPTED != TENURE_STARTED
TENURE_STARTED != ROLE_MASTERED
EMPLOYMENT != PTU_TRAINER_CLASS
EMPLOYMENT != LEGAL_AUTHORITY
ONE_SHIFT_ABSENCE != LEAVE
LEAVE != SEPARATION
SEPARATION != DISMISSAL
ROLE_ENDED != WORKPLACE_CLOSED
TRANSFER != PRIOR_TENURE_ERASED
PROMOTION != PTU_PROGRESSION
COMPENSATION_PROMISED != COMPENSATION_PAID
CREDENTIAL_HELD != EMPLOYMENT_ACTIVE
UNIFORM_WORN != EMPLOYMENT_PROVEN
ONBOARDING_COMPLETED != FEATURE_GAINED
BATTLE_WON != HIRED
BATTLE_WON != PROMOTED
SKILL_CHECK_SUCCESS != EMPLOYMENT_OFFER_ACCEPTED
```

## 17. Multiple simultaneous roles

An actor can hold more than one employment tenure or combine employment with other identities.

Examples:

- clinic employee and seasonal event worker;
- reporter and club organizer;
- mechanic and volunteer responder;
- Gym Trainer and café employee;
- researcher employed by one institution while serving as a temporary expedition collaborator elsewhere.

Availability derives from actual commitments. Do not merge unrelated relationships into one employer record.

## 18. Institutional continuity after departure

A separation may create:

- a vacancy;
- temporary coverage;
- redistribution of duties;
- a backlog;
- an external search;
- a successor overlap period;
- reduced service;
- no immediate operational effect if redundancy exists.

Workplaces owns the staffing consequence. Employment records only explain the human relationship transition.

## 19. Knowledge and handoff

A departing worker may transfer task state, documentation, keys, equipment, warnings and unresolved questions through existing owning systems.

Employment separation does not guarantee a complete handoff. It also does not imply sabotage when a handoff is incomplete.

An ex-worker can retain historical knowledge without retaining present authority.

## 20. PC employment agency

For a player character, the system must never silently:

- submit a job application;
- accept an offer;
- resign;
- retire;
- agree to a transfer;
- extend a leave;
- accept compensation terms;
- volunteer for a hazardous assignment;
- convert a temporary job into permanent employment.

Those transitions require explicit player intent when the player is available to decide.

Routine work may compress after a standing arrangement exists, but major relationship changes must surface.

## 21. PTU/Caelo boundary

Public PTU material confirms that occupationally named Trainer Classes exist as explicit mechanical classes. Therefore employment labels must never grant mechanics by semantic similarity.

UNKNOWN until exact project-source review:

- any generic profession or employment subsystem;
- downtime earnings rules adopted by Caelo;
- universal job-performance Skill Checks;
- employment-based Trainer XP;
- promotion thresholds tied to Trainer Level, Skills or Badges;
- class/Feature benefits tied to an employer;
- retirement mechanics;
- salary or wage formulas;
- employment consequences for Loyalty;
- any Caelo-specific guild, League, researcher, ranger or professional employment rules.

If an employment story needs one of these, the exact PTU/Caelo source and AutoPTU implementation must be reviewed first.

## 22. Minecraft/Cobblemon representation

Minecraft/Cobblemon/Craftics may present already-authoritative employment state through:

- posted vacancy boards;
- staff uniforms or badges;
- employee presence at a workstation;
- orientation scenes;
- supervisor/newcomer pairs;
- staff-only doors whose access state comes from Ouros;
- handoff props;
- returned equipment;
- roster boards;
- closed counters caused by staffing state;
- former workers appearing later in ordinary civilian contexts.

Presentation cannot derive employment truth.

Forbidden inferences:

- NPC behind counter -> employee;
- uniform skin -> active tenure;
- entity missing from shift -> resigned;
- credential item in inventory -> current authority;
- workstation animation -> assignment completed;
- Cobblemon battle participation -> promotion eligibility;
- Minecraft advancement -> professional qualification;
- item transfer -> compensation paid unless Finance says so.

## 23. Battle contract — First-Day Access Interruption

Narrative premise:

A new worker and supervisor are approaching a workplace when a local tactical conflict blocks access.

Full version may include protected noncombatant movement, withdrawal paths, changing access lanes and objective-aware opponents.

Permanent capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline as selected attacks require;
- status lifecycle as selected content requires;
- terrain/weather/hazards/zones/reactions if the site condition is tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

Ouros moves the new worker and supervisor out of BattleSpec before initiative and freezes a static approach. AutoPTU resolves only explicitly selected combatants. The only permitted world-facing result is `IMMEDIATE_WORKPLACE_APPROACH_CLEAR`.

`IMMEDIATE_WORKPLACE_APPROACH_CLEAR != EMPLOYMENT_STARTED`

The actual first day begins only through the employment/workplace state after access and schedule conditions are reevaluated.

## 24. Battle contract — Shift Handover Perimeter

Narrative premise:

A threat appears during the overlap between outgoing and incoming staff.

Full version may need withdrawal/protection objectives, noncombatant route control, Intercept/forced movement interactions and tactical AI that understands a safe handover objective.

Reduced version:

The handover pauses. Outgoing and incoming noncombatant staff move to safe world-state locations before initiative. Credentials, equipment and task custody remain with their existing systems. AutoPTU may return only `IMMEDIATE_HANDOVER_PERIMETER_CLEAR`.

`BATTLE_WON != HANDOVER_COMPLETE`

`BATTLE_WON != RESPONSIBILITY_TRANSFERRED`

## 25. Battle contract — Departure-Day Equipment Return Perimeter

Narrative premise:

A worker whose tenure is ending is returning issued property when a separate local incident occurs.

Full version may need protected-object carrying, escort, complete movement, lifecycle and objective-aware AI.

Reduced version:

The equipment is secured outside BattleSpec before combat. AutoPTU receives no employment object or equipment-custody objective and may return only `IMMEDIATE_RETURN_POINT_ACCESS_CLEAR`.

`ACCESS_CLEAR != EQUIPMENT_RETURN_ACCEPTED`

`EQUIPMENT_RETURNED != TENURE_END_REASON_PROVEN`

## 26. Battle contract — Emergency Coverage Access Chokepoint

Narrative premise:

A staff member assigned to temporary emergency coverage cannot reach a thinly staffed service location because a local confrontation blocks the route.

Full version may require escort/withdrawal, route objectives, active hazards or weather and tactical AI that values clearing access rather than maximizing damage.

Reduced version:

The worker remains outside BattleSpec. AutoPTU resolves a static route confrontation and may return `IMMEDIATE_COVERAGE_ROUTE_CLEAR`.

Workplaces then decides whether the worker actually arrives and whether service capacity changes.

`BATTLE_WON != COVERAGE_STARTED`

`COVERAGE_STARTED != SERVICE_FULLY_RESTORED`

## 27. Noncombat readiness

The following stories require no tactical implementation:

- vacancy/posting history;
- application and offer episodes;
- first-day onboarding;
- role or responsibility changes;
- authored leave and return;
- evidence-backed separation;
- successor overlap;
- former-employee callbacks;
- compensation commitment references;
- correction of employment records;
- a career spanning several institutions.

These can advance now as narrative world state.

## 28. Canon questions unresolved

Before promotion to canon, decide only where needed:

- which institutions actually employ people rather than use membership, service, volunteering or public office relationships;
- whether opportunities are public, referral-based or appointed;
- which qualification systems apply to which roles;
- what employment language each region uses;
- whether temporary, seasonal or fixed-duration roles exist;
- whether formal leave concepts exist and in what institutions;
- what compensation relationships exist;
- whether payroll/banking infrastructure exists;
- what separation categories institutions record;
- what hiring privacy exists;
- which records become public;
- whether any labor-law layer should ever be authored;
- whether Pokémon can hold any employment-like status rather than bounded work participation;
- which PTU/Caelo professional mechanics are actually used and implemented.

## Conclusion

This extension gives Ouros durable human career provenance without turning employment into a legal simulator or a progression engine. A person can be considered, selected, hired, delayed, onboarded, transferred, absent, returned, separated, rehired or succeeded while each transition remains evidence-backed and compatible with existing workplace, finance, identity, training and engine authority boundaries.
