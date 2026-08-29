# Public Research Scan — Formal Education, Enrollment, Course & Assessment Continuity — Pass 134

Status: RESEARCH / PROVENANCE ONLY. Not canon.
Date: 2026-08-29

## Purpose

This scan supports a missing Ouros continuity layer between the existing mentorship/clubs system and broader institutional world state: formal educational institutions, enrollment, course participation, supervised field work, assessment, transfer, completion and alumni continuity.

It does not establish compulsory schooling, age bands, tuition, degrees, licenses, school boards, examination law, Trainer certification, graduation requirements or a universal academy model for Ouros.

The repository already has strong support for mentorship, clubs, cohorts and learning communities. The missing question is how a formal institution can remember that a learner entered a program, attended specific activities, completed or missed particular requirements, transferred between sites, submitted work, received a scoped assessment and later became an alumnus without turning school state into PTU character progression.

## Repository overlap check

The recursive repository inventory and adjacent learning material were inspected before topic selection.

Relevant existing material includes:

- `design/social-bonds-mentorship-clubs-layer.md`
- `design/credentials-authorizations-recognition-extension.md`
- `design/accessibility-participation-accommodations-layer.md`
- `design/research-science-fieldwork-continuity-extension.md` where applicable
- `design/crisis-rescue-recovery-layer.md`
- `design/evacuation-shelter-reunification-departure-continuity-extension.md`
- existing archives, privacy, transport, care and institutional-continuity material
- engine readiness through Pass 133

Searches for school, academy, student, enrollment, attendance, curriculum and graduation did not reveal an existing dedicated formal-education continuity layer.

This pass therefore focuses on institutional learning records and state transitions, not on replacing mentorship or inventing mechanical advancement.

## Source A — Naranja/Uva Academy: broad-age enrollment, tracks, classes and independent study

Sources:
https://bulbapedia.bulbagarden.net/wiki/Naranja_Academy
https://bulbapedia.bulbagarden.net/wiki/Uva_Academy

Publicly documented Pokémon patterns:

- the academy is a persistent institution with faculty, classrooms, dormitories, laboratories, a nurse office, cafeteria and schoolyard;
- learners can come from different regions and different age groups;
- multiple study tracks and subject areas coexist;
- some lessons include Pokémon;
- the player is enrolled while also undertaking a large independent-study project outside the building;
- student identity persists across ordinary classes, field activity, dormitory life and regional travel.

Reusable design lesson:

`ENROLLED_AT_INSTITUTION`, `ASSIGNED_TO_COHORT`, `REGISTERED_FOR_COURSE`, `PRESENT_AT_ACTIVITY`, `SUBMITTED_WORK` and `COMPLETED_PROGRAM` should be distinct facts.

Ouros transformation:

A learner can remain an enrolled student while temporarily absent from campus, undertaking an approved field project or studying through another site. A course can be complete while the overall program remains open. A person can use institutional facilities without being enrolled in every course offered there.

Not imported:

- Paldea's institution;
- its 805-year history;
- named staff or students;
- Treasure Hunt plot content;
- specific tracks;
- school governance;
- dormitory rules;
- exam rewards;
- any protected dialogue.

## Source B — Paldea classes and exams: teaching event, assessment event and reward are separable

Sources:
https://bulbapedia.bulbagarden.net/wiki/Naranja_Academy
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Scarlet_and_Violet/Part_3

Publicly documented pattern:

Scarlet/Violet supports multiple classes, midterm examinations and final examinations. Passing tests and completing all classes can trigger rewards.

Reusable lesson:

The institution should preserve:

- lesson participation;
- assessment attempt;
- assessment result;
- requirement satisfaction;
- completion decision;
- reward or recognition event.

These should not collapse into one `PASSED_SCHOOL` flag.

Ouros transformation:

An assessment can be completed without deciding a PTU Skill Rank. A course result can exist without granting an Edge or Feature. A learner can satisfy one institution's authored requirement while still lacking an unrelated credential or game-mechanical prerequisite.

Useful invariants:

- `ATTENDED_LESSON != LEARNED_MECHANICAL_FEATURE`
- `ASSESSMENT_PASSED != TRAINER_LEVEL_INCREASED`
- `COURSE_COMPLETE != PROGRAM_COMPLETE`
- `PROGRAM_COMPLETE != LICENSE_GRANTED`
- `REWARD_ISSUED != ACADEMIC_RESULT`

Not imported:

- Paldea exam questions;
- numeric pass thresholds;
- Candy rewards;
- course count;
- automatic mechanical progression.

## Source C — Pokémon Trainers' School: specialist classes and shared institutional facilities

Sources:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Trainer%27s_School
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_academy

Publicly documented patterns include beginner education, battle instruction, contest instruction, medical study, field trips, libraries, training fields and supervised interaction with Pokémon.

Reusable lesson:

One institution can host multiple learning modes:

- lecture;
- supervised practice;
- simulation;
- field observation;
- research assignment;
- battle practice;
- care practice;
- presentation;
- quiz or assessment.

Ouros transformation:

Store an `activity_kind` and an owning course/program rather than assuming every educational scene is a classroom lecture or battle.

Do not infer professional authority from participation. Attending a medical lesson does not make a student a clinician. Participating in battle studies does not create League rank. Using a rental Pokémon does not create ownership.

## Source D — Pokémon Summer Academy: temporary programs, teams, rental Pokémon and field reports

Sources:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Summer_Academy
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Triathlon

Publicly documented patterns:

- a bounded one-week educational program;
- temporary student teams;
- rental Pokémon used for activities;
- supervised field observation;
- reports/presentations assessed afterward;
- safety boundaries around research sites;
- a completion certificate after the program;
- team competition coexisting with individual learning.

Reusable lessons:

Temporary educational participation does not require permanent enrollment. Custody of a teaching Pokémon does not imply ownership. Observation can be assessed without capture. Team score and individual academic completion can differ.

Useful invariants:

- `TEMPORARY_PROGRAM_PARTICIPANT != PERMANENT_STUDENT`
- `RENTAL_POKEMON_ASSIGNED != OWNERSHIP_TRANSFERRED`
- `FIELD_ACTIVITY_STARTED != FIELD_ACTIVITY_COMPLETED`
- `TEAM_SCORE != INDIVIDUAL_COMPETENCY`
- `CERTIFICATE_ISSUED != PTU_FEATURE_GRANTED`

## Source E — Blueberry Academy: exchange, residential learning and specialized institutional identity

Source:
https://bulbapedia.bulbagarden.net/wiki/Blueberry_Academy

Publicly documented patterns:

- a sister institution can receive exchange students;
- a school can have a distinct specialization;
- dormitory, classroom, club and field environments can be part of one educational system;
- an institution can host specialized ecological infrastructure used for study and exploration.

Reusable lesson:

`HOME_INSTITUTION`, `HOST_INSTITUTION`, `EXCHANGE_PLACEMENT`, `COURSE_RECORD` and `RETURN_TO_HOME_INSTITUTION` should remain distinct.

Ouros transformation:

A transfer or exchange can preserve the base enrollment while adding a temporary host placement. The host may create attendance and assessment records that later return to the base institution. No universal credit-transfer rule is assumed.

## Source F — PTU community academy campaign discussion

Source:
https://www.reddit.com/r/PokemonTabletop/comments/9nrfy4/help_need_campaign_ideas_for_a_pokemon_academy/

A public PTU GM described an academy campaign and solicited alternatives to repetitive school-plot clichés. Community responses included clubs, technical projects, simulated disaster-response coursework and practical scenarios where combat could be one solution among several.

Reusable lesson:

School campaigns become stronger when curriculum creates recurring social groups and bounded practical problems instead of turning every lesson into a mandatory tactical fight.

Ouros transformation:

Formal education can generate:

- supervised field projects;
- club collaborations;
- temporary placements;
- research demonstrations;
- public exhibitions;
- infrastructure exercises;
- service-learning projects;
- peer teaching;
- remedial opportunities;
- capstone investigations.

Combat is optional and must obey ordinary engine readiness.

This source is community design experience, not PTU rules authority.

## Source G — temporary enrollment during emergency closures

Source:
https://www2.education.vic.gov.au/pal/enrolment/guidance/temporary-enrolments-emergency-school-closures

Used only as information architecture.

The public guidance separates:

- base school;
- host school;
- temporary enrollment;
- transfer of necessary student information;
- attendance recorded at the host;
- later return or alternative arrangement.

Reusable lesson:

An interruption should not force an educational identity reset.

Ouros transformation:

A crisis can create a temporary learning placement while preserving the base institution and prior records. The host can produce local attendance/activity records. Later reconciliation can merge the history without pretending the learner was permanently enrolled at two institutions for the same purpose.

Not imported:

- Victorian law;
- compulsory attendance rules;
- CASES21;
- child-protection procedure;
- government-school powers;
- eligibility rules.

## Source H — student-record continuity and transfer evidence

Sources:
https://www.vic.gov.au/about-student-enrolment-records
https://www.education.gov.au/transferring-student-data-interstate

Used only as record/provenance references.

Public patterns:

- enrollment records can remain historically important long after attendance ends;
- other artifacts such as attendance rolls, transfer notes, reports, class photographs and yearbooks can corroborate a learner's presence;
- transfer systems distinguish the sending institution, receiving institution and information package.

Reusable lesson:

Educational history should be reconstructible from multiple evidence channels and should preserve source/provenance.

Ouros transformation:

An old school record can support a historical mystery without becoming omniscient truth. A yearbook may prove presence at an event but not course completion. A transfer note may prove a handoff occurred but not that every local requirement was accepted.

## PTU/Caelo source cross-check

Project-accessible PTU rule data was checked for education-related mechanical concepts.

Visible source evidence includes:

- `Researcher` requiring an Education Skill at Novice Rank;
- `Breadth of Knowledge` interacting with Education Skill Edges;
- `Instruction` modifying Assisted Skill Checks using Education Skills;
- `Scholar` affecting several Education Skill checks;
- `Mentor` requiring two relevant skills and spending Tutor Points to teach supported Moves;
- `Lessons`, `Move Tutor` and related Mentor Features providing exact rule-governed tutoring behavior.

These rules establish mechanical education/tutoring concepts, but they do not establish a universal school system.

Therefore keep UNKNOWN unless a governing source explicitly provides it:

- school admission check;
- grade calculation;
- attendance requirement;
- course credit;
- graduation threshold;
- universal diploma;
- academic rank converting directly to Skill Rank;
- school lesson automatically granting an Edge or Feature;
- exam victory granting Trainer Level;
- battle result as general academic assessment;
- Trainer Class as a degree;
- Pokémon Education Skill as universal academic standing;
- General Education Skill as universal school year placement.

Institutional learning records must remain narrative/world state unless an exact PTU/Caelo mechanical rule is deliberately invoked.

## Cross-source synthesis

Reusable continuity chain:

`institution -> authored program -> enrollment/placement -> course registration -> activity participation -> evidence/submission -> assessment -> requirement decision -> completion/transfer -> alumni/history`

Each transition can carry its own timestamp, scope and provenance.

This allows legitimate discrepancies:

- a student appears in a class photograph but never registered for that course;
- a host institution records attendance while the base institution still owns the main enrollment;
- field work was completed but the report was never submitted;
- an assessment was passed but the program had another unresolved requirement;
- a learner completed the program but a certificate was issued later;
- a course was retaken under a revised curriculum;
- two institutions describe the same placement differently because one records attendance and the other records credit recognition.

## Narrative structures extracted

### Cohort without forced friendship

Students repeatedly share classes, dorms, fieldwork and projects. Relationship labels still require actual social evidence.

### Practical assessment without combat default

A field task can assess observation, planning, presentation or safe execution. Battle may occur only when fiction and engine contracts support it.

### Interrupted semester

Weather, infrastructure, crisis or travel disrupts a site. Education continues through revised schedules, temporary locations or host institutions where local canon supports those options.

### Exchange placement

A learner remains linked to a home institution while accumulating a bounded host-institution history.

### Alumni continuity

Graduates can return as visitors, mentors, staff, competitors, donors or critics without automatically possessing institutional authority.

### Curriculum history

Institutions can change programs over decades. Old classrooms, field stations, course names and archived projects become environmental storytelling.

## NPC archetypes extracted

### Registrar Who Knows Which Record Answers Which Question

Can distinguish enrollment, attendance, course registration and completion without treating one document as universal truth.

### Field Instructor

Owns a supervised activity, safety scope and assessment rubric where canon establishes one, but does not control unrelated institutional decisions.

### Returning Alumnus

Carries memory of an older curriculum and may misremember present rules.

### Exchange Coordinator

Tracks home institution, host placement and unresolved transfer questions without deciding mechanical Trainer progression.

### Student Who Completed the Work but Missed the Paperwork

Creates a low-stakes provenance problem rather than an automatic failure or conspiracy.

### Teacher With Two Roles

May teach and also occupy a battle, research, care or civic role. Authority remains scoped to the role active in the current decision.

## Battle implementation implications

Most education content should remain outside battle.

Potential rich scenes include evacuating a field class, protecting access to a research exercise or clearing a route before students can return to a practical site.

Full versions can depend on:

- Intercept/escort movement;
- phased withdrawal;
- protected zones or environmental reactions;
- objective-aware AI;
- semantic adapter/playback.

Reduced versions should pause the educational activity first, remove students, instructors, records, rental Pokémon and assessment objects from BattleSpec, then use conventional combat to decide immediate physical access only.

A battle must never automatically award a grade, course completion, diploma, Trainer Level, Skill Rank, Edge, Feature, Move, credential or enrollment status.

## Research-to-canon boundary

Everything in this file is research synthesis.

No school, academy, compulsory-education regime, age range, curriculum, semester, exam threshold, diploma, tuition system, dormitory rule, exchange agreement, student-record law, teacher credential or graduation requirement becomes Ouros canon through this scan.

Promotion requires explicit regional/institutional canon approval plus PTU/Caelo and implementation review where mechanics are involved.