# Formal Education, Enrollment, Course & Assessment Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29
Research provenance: `research/2026-08-29-formal-education-enrollment-course-assessment-continuity-scan-134.md`

## Purpose

This extension gives Ouros a durable model for formal learning institutions without turning school participation into automatic PTU advancement.

It owns the continuity between an authored educational institution and the learner's institutional history: enrollment, placement, course registration, attendance/participation, supervised practical work, assessment, requirement satisfaction, transfer, completion and alumni state.

It does not own:

- friendship, mentorship or club relationships;
- PTU Trainer Level, Skill Ranks, Edges, Features or Tutor mechanics;
- professional licensing or credentials outside the educational institution;
- research truth;
- medical diagnosis;
- housing/dorm ownership;
- transport service;
- crisis response;
- institutional governance;
- battle outcomes.

Those remain with their existing owners.

## 1. Institutional identity

Suggested record:

```yaml
education_institution:
  institution_id: null
  name: null
  institution_kind: authored_local_value
  location_refs: []
  operating_status: unknown
  program_ids: []
  cohort_ids: []
  facility_refs: []
  archive_refs: []
  governance_ref: null
  credential_refs: []
  canon_status: proposed|canon_approved
  provenance_refs: []
```

`institution_kind` has no universal enum until Ouros canon establishes actual regional educational forms.

## 2. Program state

```yaml
education_program:
  program_id: null
  institution_id: null
  name: null
  effective_from: null
  effective_to: null
  requirement_set_ref: null
  course_ids: []
  placement_options: []
  completion_authority_ref: null
  status: proposed|active|paused|retired
  provenance_refs: []
```

A program version is historical state. Curriculum changes should create a new effective version instead of rewriting earlier student history.

## 3. Enrollment episode

```yaml
enrollment_episode:
  enrollment_id: null
  learner_id: null
  institution_id: null
  program_id: null
  enrollment_kind: primary|temporary|exchange|guest|other_authored
  home_institution_id: null
  host_institution_id: null
  start_at: null
  expected_end_at: null
  ended_at: null
  status: pending|active|paused|completed|transferred|withdrawn|unknown
  provenance_refs: []
```

Core invariant:

`ENROLLED != PRESENT_ON_CAMPUS`

Enrollment is an institutional relationship. Physical presence is an event.

## 4. Cohort membership

Existing social-bonds infrastructure already supports cohorts. This extension should reference it rather than duplicate social state.

```yaml
education_cohort_link:
  learner_id: null
  cohort_id: null
  enrollment_id: null
  start_at: null
  end_at: null
  role: learner|peer_mentor|other_authored
```

Cohort membership creates repeated-contact opportunities. It does not create friendship, rivalry or intimacy automatically.

## 5. Course instance

```yaml
course_instance:
  course_instance_id: null
  program_id: null
  course_definition_ref: null
  title: null
  term_or_window_ref: null
  instructor_role_refs: []
  location_refs: []
  activity_ids: []
  assessment_ids: []
  requirement_refs: []
  status: planned|active|paused|completed|cancelled
  provenance_refs: []
```

A course definition can persist across years while each offering has its own staff, dates and locations.

## 6. Registration

```yaml
course_registration:
  registration_id: null
  learner_id: null
  course_instance_id: null
  enrolled_at: null
  status: registered|waitlisted|active|completed|withdrawn|incomplete|unknown
  decision_ref: null
  provenance_refs: []
```

`REGISTERED != ATTENDED`

`REGISTERED != PASSED`

`WITHDRAWN != FAILED`

The meaning of each status must come from the institution's authored rules.

## 7. Educational activity

```yaml
education_activity:
  activity_id: null
  course_instance_id: null
  activity_kind: lecture|seminar|lab|fieldwork|practice|simulation|presentation|project|battle_practice|other_authored
  scheduled_start: null
  scheduled_end: null
  location_ref: null
  supervisor_refs: []
  participant_scope_ref: null
  safety_scope_ref: null
  rental_or_custody_refs: []
  battle_spec_ref: null
  status: planned|active|paused|completed|cancelled
  provenance_refs: []
```

The `battle_practice` value describes institutional intent only. Any actual tactical encounter must still be legal under AutoPTU.

## 8. Participation record

```yaml
activity_participation:
  participation_id: null
  activity_id: null
  learner_id: null
  state: expected|present|late|excused_absence|unexcused_absence|partial|remote|unknown
  observed_from: null
  observed_to: null
  evidence_refs: []
  notes_visibility: institution_scoped
```

This is factual attendance/participation state, not a moral judgment.

Avoid global labels such as `TRUANT` unless a specific institution and canon rule explicitly define them.

## 9. Fieldwork and supervised practicals

Practical education can reference existing owners:

- Ecology/Conservation for observation sites;
- Research/Science for samples and findings;
- Care for clinical environments;
- Battle Institutions for formal competitive contexts;
- Agriculture, Construction, Maintenance, Public Space, Transport or other systems for service-learning placements.

Education owns only the educational wrapper: assignment, supervision, participation, submission and assessment.

Example:

```yaml
practical_assignment:
  assignment_id: null
  course_instance_id: null
  learner_id: null
  host_owner_ref: ecology_case_123
  task_scope: observe_and_report
  start_at: null
  due_at: null
  completion_evidence_refs: []
  assessment_ref: null
```

## 10. Submission state

```yaml
submission_record:
  submission_id: null
  assignment_id: null
  learner_id: null
  submitted_at: null
  artifact_refs: []
  revision_number: 1
  status: submitted|returned_for_revision|accepted_for_review|withdrawn
  provenance_refs: []
```

`WORK_PERFORMED != WORK_SUBMITTED`

`WORK_SUBMITTED != WORK_ASSESSED`

This allows low-stakes procedural stories where the learning occurred but the evidence package is incomplete.

## 11. Assessment event

```yaml
assessment_event:
  assessment_id: null
  course_instance_id: null
  learner_id: null
  assessment_kind: written|oral|practical|presentation|portfolio|battle_based_if_authored|other_authored
  attempted_at: null
  assessor_refs: []
  rubric_ref: null
  evidence_refs: []
  result_state: pending|satisfied|not_yet_satisfied|incomplete|invalidated|unknown
  review_ref: null
  provenance_refs: []
```

The schema deliberately avoids a universal numeric grade.

Local canon may add scales later.

## 12. Academic result versus PTU mechanics

Hard boundary:

```text
ACADEMIC_RESULT != PTU_ADVANCEMENT
```

A course may narratively certify that a learner completed an authored educational requirement.

It cannot automatically:

- raise General Education;
- raise Pokémon Education;
- grant Researcher;
- grant Mentor;
- grant Instruction or Scholar;
- teach a Move;
- spend or create Tutor Points;
- grant an Edge;
- grant a Feature;
- increase Trainer Level.

If a PTU rule-governed advancement or tutoring event occurs, record it as a separate mechanical transaction linked to the educational context.

## 13. Requirement decision

```yaml
program_requirement_state:
  learner_id: null
  program_id: null
  requirement_ref: null
  state: unresolved|satisfied|not_satisfied|waived_if_authored|superseded
  decision_at: null
  authority_ref: null
  evidence_refs: []
```

A single passed assessment should not complete an entire program unless the authored requirement graph says it does.

## 14. Completion event

```yaml
program_completion_event:
  completion_event_id: null
  enrollment_id: null
  learner_id: null
  program_id: null
  effective_at: null
  authority_ref: null
  decision_basis_refs: []
  certificate_or_record_ref: null
  status: completed|not_completed|pending_review
```

`PROGRAM_COMPLETED != CERTIFICATE_PHYSICALLY_ISSUED`

The archival record can exist before a commemorative object is printed or presented.

## 15. Transfer and exchange

```yaml
education_transfer:
  transfer_id: null
  learner_id: null
  sending_institution_id: null
  receiving_institution_id: null
  transfer_kind: permanent|temporary|exchange|emergency_host|other_authored
  requested_at: null
  effective_at: null
  information_packet_ref: null
  recognition_decision_refs: []
  return_expected: false
  returned_at: null
  provenance_refs: []
```

Important distinctions:

- `INFORMATION_SENT != INFORMATION_RECEIVED`
- `INFORMATION_RECEIVED != CREDIT_RECOGNIZED`
- `HOST_ATTENDANCE != HOME_PROGRAM_COMPLETION`
- `EXCHANGE_STARTED != HOME_ENROLLMENT_ENDED`

## 16. Emergency continuity

Crisis may interrupt a school site without ending the institution.

Possible states:

- site closed;
- course relocated;
- temporary host placement;
- fieldwork postponed;
- remote/alternate participation where technology and canon permit;
- term window revised;
- assessment rescheduled.

Crisis owns the emergency facts. Education owns the learning-continuity response.

`SCHOOL_BUILDING_CLOSED != INSTITUTION_CLOSED`

`INSTITUTION_REOPENED != EVERY_COURSE_RESUMED`

## 17. Accessibility and accommodations

Use the existing accessibility layer.

Education may reference an approved accommodation or participation adjustment but should not infer disability, diagnosis or private medical information.

Store only the minimum institutional fact required for the educational decision.

## 18. Pokémon in education

Possible authored roles include:

- learner's partner;
- institution-owned or institution-custodied teaching Pokémon;
- rental Pokémon for supervised practice;
- wild Pokémon observed in fieldwork;
- staff partner Pokémon;
- research subjects where an existing owner system permits it.

Hard boundaries:

- `ASSIGNED_FOR_CLASS != OWNED_BY_STUDENT`
- `OBSERVED_IN_FIELDWORK != AVAILABLE_FOR_CAPTURE`
- `POKEMON_PRESENT_IN_CLASS != STUDENT_PARTNER`
- `SPECIES_TYPICALLY_USED_FOR_TASK != INDIVIDUAL_CAPABILITY_VERIFIED`

## 19. Rental/teaching Pokémon custody

When a teaching activity uses a Pokémon not owned by the learner, reference Pokémon Agency/custody state.

Educational participation does not create:

- ownership;
- permanent party membership;
- capture permission;
- breeding permission;
- Move Tutor permission beyond exact PTU rules and owner consent.

## 20. Staff roles and scoped authority

A person can simultaneously be:

- instructor;
- researcher;
- Gym/League actor;
- clinician;
- administrator;
- club mentor;
- public official.

Each decision must identify the role and mandate used.

`TEACHER != UNIVERSAL_AUTHORITY`

A battle instructor cannot approve a medical placement merely because the same NPC works at the institution.

## 21. Alumni state

```yaml
alumni_link:
  learner_id: null
  institution_id: null
  program_id: null
  completion_ref: null
  alumni_since: null
  current_relationship: inactive|visitor|mentor|staff|donor|critic|other_authored
  public_visibility: authored_scope
```

Alumni status supports callbacks without implying loyalty, donations, employment or authority.

## 22. Curriculum history

Preserve retired course definitions and old program versions.

This enables environmental storytelling through:

- renamed classrooms;
- obsolete field stations;
- old course manuals;
- alumni photographs;
- archived project reports;
- converted laboratories;
- former dormitory wings;
- old battle courts used for new purposes.

## 23. Privacy

Student records may contain scoped information.

Suggested visibility classes:

- learner_private;
- instructor_need_to_know;
- institution_internal;
- transfer_packet_scoped;
- public_directory_if_authored;
- alumni_public_if_authored.

No private educational record becomes public because Minecraft renders the learner nearby.

## 24. Mystery grammar

Formal education supports mysteries based on records and chronology rather than villainy.

Examples:

- a yearbook shows attendance but the enrollment register does not because the learner was a temporary guest;
- a field report was completed before a course registration correction;
- a host academy records a completed practical while the home academy still shows the requirement pending;
- an instructor changed mid-term and two rubrics remain in the archive;
- a course title changed while the course identifier stayed stable;
- a certificate date differs from the effective completion date.

## 25. Quest generation

Useful state-driven triggers:

- unresolved transfer recognition;
- missing fieldwork artifact;
- reopened practical site;
- returning alumnus;
- temporary classroom relocation;
- course project that intersects a current ecological/infrastructure issue;
- archived curriculum connected to a present mystery;
- exchange cohort arrival;
- capstone presentation;
- student club project requiring an institutional handoff.

Routine attendance should compress.

## 26. Encounter contract — Field Class Withdrawal

Full intended version:

A supervised class is interrupted near a practical site. The objective is safe withdrawal while instructors preserve accountability and avoid turning students into tactical objectives.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if combat occurs
- status lifecycle — PARTIAL for ordinary legal statuses
- terrain/weather/hazards/zones/reactions — BLOCKING for live protected corridors/environmental reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version: READY.

Ouros pauses the educational activity, removes students, instructors, rental Pokémon, samples and records from BattleSpec, then creates a conventional static encounter at the perimeter.

Victory can restore immediate access. It cannot award academic credit or complete the fieldwork.

## 27. Encounter contract — Practical Site Access Diversion

Full intended version:

A course needs access to a field site, laboratory annex or training ground while an unrelated tactical obstruction occupies the approach.

Rich version may require escort, protected zones and objective-aware AI.

Reduced version: READY.

Learners remain off-grid. A conventional battle clears or fails to clear the route. The institution decides afterward whether the practical can proceed.

Forbidden transition:

`VICTORY != PRACTICAL_COMPLETED`

## 28. Encounter contract — Exchange Arrival Perimeter

Full intended version:

An exchange cohort arrives while a separate incident affects the receiving perimeter.

Rich version may need staged movement, escort and semantic playback.

Reduced version: READY.

Travel/education world state resolves arrival and custody of records first or pauses it safely. Students and luggage remain outside BattleSpec. Combat affects only immediate access.

Forbidden transitions:

- victory => exchange placement accepted
- victory => records recognized
- victory => dorm assignment valid
- victory => course credit granted

## 29. Minecraft/Cobblemon representation

Safe after Ouros decides state:

- schedules on notice boards;
- different NPC cohorts at different times;
- classroom use changes;
- dormitory assignments;
- archived class photographs;
- old field equipment;
- temporary classrooms after a closure;
- exchange students appearing for a bounded period;
- alumni returning for events;
- course-project changes visible in the world.

Minecraft must not infer:

- enrollment from presence in a classroom;
- completion from standing near a teacher;
- attendance from chunk loading;
- ownership from a Pokémon following a student;
- a passing grade from a battle win;
- transfer recognition from inventory contents;
- Skill Rank from educational props.

## 30. PTU/Caelo boundary

Current project-accessible PTU evidence includes exact education-related Skills, Edges and Features such as Researcher, Breadth of Knowledge, Instruction, Scholar and Mentor.

Those mechanics remain authoritative only when their prerequisites, action costs, targets and effects are satisfied.

Formal education world state cannot approximate them.

If a school scene invokes `Instruction`, `Mentor`, `Move Tutor` or another PTU mechanic, the engine transaction must use the real rule. The narrative record may later point to the successful mechanical event.

## Promotion rules

Before any formal-education proposal becomes canon, verify:

1. institution and region are approved;
2. program purpose is authored;
3. enrollment/transfer procedure is not invented from real-world law;
4. student age assumptions are explicit where relevant;
5. privacy scope exists;
6. academic results do not fabricate PTU advancement;
7. Pokémon custody/ownership is authoritative;
8. any battle-linked activity has a readiness-compatible reduced form;
9. external inspiration remains transformed and attributed.

## Open canon questions

- Which Ouros regions have formal schools or academies?
- Are they age-specific, mixed-age, vocational, League-linked, community-run or something else?
- Which institutions offer residential study?
- Which permit exchange placements?
- What learning records do they retain?
- Which records are public?
- What completion concepts exist?
- Do any programs connect to professional credentials?
- How are field activities supervised?
- How are teaching Pokémon owned or custodied?
- Which historical institutions have closed, merged or changed curriculum?
- Which current NPCs are students, staff or alumni?

None of these answers are established by this design file.