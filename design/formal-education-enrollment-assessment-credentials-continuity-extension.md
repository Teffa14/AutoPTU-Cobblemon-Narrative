# Formal education, enrollment, assessment & credentials continuity extension

Status: PROPOSED systems design. Not established Ouros canon.
Date: 2026-08-31

## Purpose

Ouros already has mentorship, clubs, research, employment, identity, archives and battle institutions. It needs a separate continuity layer for formal or institutionally organized learning so that enrollment, courses, field assignments, assessment, completion, credentials, transfers and alumni history can persist without turning narrative schooling into PTU progression.

This layer is dormant unless canon establishes an educational institution, programme or recognized learning process.

It does not create universal schooling, compulsory attendance, age bands, semesters, tuition, diplomas, national curricula or standardized exams.

## Authority boundaries

Social Bonds/Mentorship owns interpersonal mentoring relationships.

Clubs owns voluntary persistent group membership and club projects.

Human Identity owns personal identity and name continuity.

Employment owns staff tenure and workplace relationship.

Archives owns preservation and access to records and artifacts.

Scientific Research owns research-project evidence and claims.

Battle Institutions owns formal battle challenge contracts and competitive results.

Finance owns fees, scholarships or payments if canon creates them.

Material Culture owns physical books, uniforms, instruments and issued objects.

This layer owns only the educational relationship and academic-history facts linking those domains.

## Core entities

### educational_institution

Suggested fields:

institution_id
name_ref
institution_type
location_ids
operating_period
recognized_program_ids
facility_refs
staff_role_refs
archive_ref
status
canon_authority_ref

Institution type is authored, not inferred. Examples may include academy, village school, field institute, conservatory, technical school, mobile school or adult-learning hall.

### education_program

program_id
institution_id
title_ref
program_version
entry_rule_ref
completion_rule_ref
credential_rule_ref
required_component_refs
optional_component_refs
fieldwork_policy_ref
valid_from
valid_to
status

A programme version matters. A person enrolled under an older curriculum should not be retroactively judged against a later one.

### enrollment_episode

enrollment_id
learner_id
program_id
application_ref
accepted_at
started_at
ended_at
end_reason
attendance_status
cohort_ref
provenance_refs

Application, acceptance and actual start are separate events.

### course_or_learning_component

component_id
program_id
title_ref
component_type
version
instructor_role_refs
learning_outcome_refs
prerequisite_rule_ref
assessment_rule_ref
fieldwork_refs
valid_from
valid_to

Component type may include classroom, workshop, laboratory, field placement, expedition, supervised practice, project or independent study when canon supports it.

### learner_component_episode

episode_id
learner_id
component_id
enrolled_at
participation_status
completed_at
withdrawn_at
completion_status
provenance_refs

Participation does not prove competence.

### learning_assignment

assignment_id
component_episode_id
assignment_type
issued_at
due_at
artifact_refs
world_event_refs
submission_ref
completion_state
assessment_ref

Assignments may create durable outputs such as maps, reports, recordings, specimens, repaired equipment, exhibitions or field observations. Those outputs remain governed by their native domains.

### assessment_episode

assessment_id
learner_id
component_or_program_ref
assessment_type
rule_version_ref
attempt_number
scheduled_at
performed_at
evaluator_refs
evidence_refs
result_state
result_detail_ref
appeal_or_review_ref

Do not invent a numeric grade model globally. Institutions may use pass/fail, narrative evaluation, practical demonstration, portfolio, oral exam or other canon-authored methods.

### programme_completion_record

completion_id
learner_id
program_id
curriculum_version_ref
requirements_snapshot_ref
completion_date
completion_state
missing_component_refs
provenance_refs

Completion records participation against programme requirements. They do not automatically award credentials.

### education_credential

credential_id
holder_id
program_id
awarding_institution_id
credential_type_ref
awarded_at
credential_version
status
physical_or_digital_record_refs
revocation_or_revision_ref

Credential type and authority require canon.

### academic_record_version

record_id
learner_id
institution_id
record_version
issued_at
component_history_refs
assessment_refs
completion_refs
credential_refs
correction_refs
provenance_refs

A later corrected record does not erase the earlier record's historical existence.

### recognition_episode

recognition_id
credential_or_learning_ref
requesting_actor_id
recognizing_institution_id
rule_ref
requested_at
reviewed_at
result
recognized_scope
reason_ref

Recognition can be partial, conditional, refused or unresolved if canon authorizes those states.

### transfer_episode

transfer_id
learner_id
from_institution_id
to_institution_id
requested_at
record_package_ref
recognized_component_refs
unrecognized_component_refs
new_program_ref
status

Transfer does not imply seamless credit or equivalent curriculum.

### alumni_relationship

alumni_id
person_id
institution_id
program_ref
basis_ref
active_from
status
return_event_refs
role_transition_refs

Alumni status may support callbacks and access only where canon explicitly permits it.

## Permanent separations

APPLICATION_SUBMITTED != ACCEPTED

ACCEPTED != ENROLLED

ENROLLED != ATTENDING_NOW

ATTENDED != COMPLETED

COMPLETED_COMPONENT != PASSED_ASSESSMENT

ASSESSMENT_TAKEN != PASSED

PROGRAM_REQUIREMENTS_COMPLETED != CREDENTIAL_AWARDED

CREDENTIAL_AWARDED != CREDENTIAL_RECOGNIZED_EVERYWHERE

TRANSCRIPT_EXISTS != CREDENTIAL_EXISTS

ACADEMIC_RECORD != CANONICAL_TRUTH ABOUT PRIVATE COMPETENCE

FIELD_ASSIGNMENT_COMPLETED != WORLD_PROBLEM_SOLVED

SCHOOL_ENROLLMENT != PTU_SKILL_RANK

COURSE_COMPLETION != EDGE

GRADUATION != FEATURE

DIPLOMA != TRAINER_CLASS

TEACHER_EMPLOYMENT != MENTOR_FEATURE

BATTLE_VICTORY != COURSE_PASS unless an explicit authored assessment rule and governing mechanics say so

ALUMNI != STAFF

STUDENT_ID_CARD != CURRENT_AUTHORITY

MINECRAFT_NPC_IN_CLASSROOM != CANONICAL_ENROLLMENT

MINECRAFT_BOOK != CANONICAL_TRANSCRIPT

## Learning provenance

Ouros should record where evidence of learning came from when useful:

formal institution
non-formal organized training
mentorship
apprenticeship
field experience
self-study
family or community practice
research work
employment practice

These categories do not create mechanical competency. They only preserve provenance for later authored recognition or narrative callbacks.

## Institutional calendars

A school can have terms, rotations, seasonal sessions or rolling enrollment if canon establishes them. The core model should use dated episodes rather than assume semesters.

A calendar may create:

course start windows
field exercise periods
project deadlines
assessment periods
breaks
graduation or completion ceremonies
facility closures
alumni events

Calendar events remain narrative scheduling state. They do not alter initiative, Action Economy or PTU rest rules.

## Student equipment and permissions

Institutions may issue temporary equipment, room access, laboratory access, library privileges or field permissions.

Use Material Culture and authority/custody layers for the object or permission itself.

The education layer records why the person received it and when that educational basis changes.

STUDENT_CUSTODY != OWNERSHIP

COURSE_ACCESS != PERMANENT_ACCESS

GRADUATION != EQUIPMENT_TRANSFER

## Staff and instructors

An instructor is an employment or institutional-role fact.

A person may teach a course without possessing the PTU Mentor Feature unless PTU/Caelo mechanics separately establish that Feature.

Likewise, a character with Mentor may mechanically tutor Pokémon without being an employee of a school.

## Educational assignments as world hooks

Assignments can create playable objectives while preserving authority boundaries.

Examples:

survey a route and submit a map
observe a migration without disturbing it
prepare a public exhibition
repair a piece of training equipment
interview residents about local history
assist a research station
complete supervised field practice
produce a safety plan for a local event

The world result and the academic result are separate.

A team might fail the original field objective but submit an excellent analysis of why. Another team might achieve the field objective but fail to document it adequately.

## Encounter contracts

### Field Practicum Route Incident

Intended full version:

Students move through a supervised field practicum while an unexpected threat creates route-control, withdrawal and protection decisions. Full implementation may require complete movement including Intercept and forced movement, full lifecycle, terrain/weather/hazards/zones/reactions, individually audited moves/abilities/items/Trainer Features, AI tactical policy and adapter/playback.

Status: BLOCKED for the rich version.

Reduced version:

The practicum team and noncombatant supervisors leave BattleSpec before initiative. AutoPTU resolves an ordinary audited battle controlling only the immediate route. Narrative may record IMMEDIATE_PRACTICUM_ROUTE_CLEAR after victory. This does not complete the practicum or pass any student.

### Laboratory Evacuation Exercise Interrupted

Intended full version:

A scheduled drill becomes complicated by an actual tactical threat, creating evacuation, protected-object and hazard objectives.

Dependencies: complete movement, escort/protection semantics, lifecycle, terrain/weather/hazards/zones/reactions, tactical policy, semantic playback, plus exact content parity.

Status: BLOCKED.

Reduced version:

Students, instructors and equipment are removed from BattleSpec before initiative. AutoPTU resolves only access to the immediate laboratory perimeter. Narrative may record IMMEDIATE_LABORATORY_ACCESS_CLEAR. The drill result and any academic assessment remain separate.

### Assessment Site Access Incident

Intended full version:

An assessment location becomes temporarily inaccessible while an encounter is active. The rich version may involve timed access, protected evaluators and route control.

Dependencies: complete movement, lifecycle, tactical objectives, possible hazards/reactions, adapter/playback.

Status: BLOCKED.

Reduced version:

The actual assessment occurs only after the ordinary encounter. AutoPTU can return IMMEDIATE_ASSESSMENT_SITE_APPROACH_CLEAR. It cannot decide whether the learner passes.

### Field Project Artifact Recovery Perimeter

Intended full version:

A submitted or in-progress project artifact lies within a dangerous area, potentially creating protected-object recovery and carrying objectives.

Dependencies: protected-object carrying, complete movement, lifecycle, hazards/zones/reactions where applicable, AI tactical policy and semantic playback.

Status: BLOCKED.

Reduced version:

The artifact remains static outside BattleSpec. AutoPTU resolves only immediate area control. Narrative may record IMMEDIATE_PROJECT_ARTIFACT_APPROACH_CLEAR. Retrieval, authenticity and academic credit require later narrative actions.

## Generator rules

The generator may create educational opportunities only from established institutions, programmes, staff roles, calendars, world needs and learner history.

It must not invent a school merely because a PC needs training.

It must not invent a credential because a character has high Skills.

It must not convert a narrative lesson into Skill Ranks, Edges, Features, Tutor Points, Moves, Ability changes or other PTU progression.

It must not infer competence solely from enrollment, attendance, uniform, title or diploma.

It must not infer failure, expulsion or dropout merely from absence.

It must not rewrite an old transcript when a curriculum changes.

## Minecraft/Cobblemon boundary

Minecraft and Cobblemon may render campuses, classrooms, schedules, signs, books, uniforms, dormitories, NPC positions, blackboards, laboratories and ceremonies.

They may not establish who is canonically enrolled, what was taught, whether an assessment was passed, which qualification was awarded or whether another institution recognizes it.

Loaded NPC count is not class enrollment.

A lectern book is not a transcript unless Ouros links it to an academic_record_version.

A scoreboard value is not a grade unless the narrative authority layer authored that assessment result.

## Canon questions left open

Which educational institutions actually exist in Ouros?

Which are formal, non-formal or community-run?

Do any issue credentials?

Do institutions recognize one another's credentials or learning?

Are there Trainer-specific schools, general schools, specialist institutes or adult-learning institutions?

What ages or life stages attend each institution, if any restrictions exist?

How are Pokémon included in education without reducing them to equipment or curriculum assets?

Which facilities provide dormitories, field stations, laboratories or libraries?

What privacy rules govern learner records?

Can PCs enroll, teach, transfer, withdraw, return or found an institution?

Which Caelo institutions and rules, if any, already answer some of these questions?