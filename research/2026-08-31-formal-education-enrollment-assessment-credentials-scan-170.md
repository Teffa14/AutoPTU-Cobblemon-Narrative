# Formal education, enrollment, assessment & credentials research — Pass 170

Status: RESEARCH ONLY / NON-CANON
Date: 2026-08-31

## Scope

This pass investigates persistent educational institutions and learner histories: enrollment, attendance, courses, field assignments, assessment, completion, qualifications, transfers, alumni relationships, records and recognition.

Nothing in this note establishes that Ouros has compulsory schooling, universities, standard diplomas, age-banded classes, tuition, grades, semesters, national curricula or universal Trainer academies. Those remain canon decisions.

Existing repository inspection found adjacent authority in Social Bonds/Mentorship/Clubs, Human Identity, Workplaces/Employment, Archives, Battle Institutions and Scientific Research. No dedicated formal-education continuity layer was found by searches for school, academy, curriculum, enrollment, semester, graduation, transcript, course, credential and related terms. The new design should therefore connect those layers rather than absorb them.

## Pokémon franchise patterns

### Naranja/Uva Academy: institution plus broad participation

Bulbapedia's Naranja Academy summary records an old institution in Mesagoza, classes concerning Pokémon, students from multiple regions and a wide range of ages, distinct study tracks, dormitories, laboratories, staff spaces and an independent Treasure Hunt project.

Source: https://bulbapedia.bulbagarden.net/wiki/Naranja_Academy

Reusable structure for Ouros:

- one institution may host multiple tracks and age groups;
- attendance can coexist with independent field activity;
- school identity, course participation and personal adventure history are separate continuities;
- facilities can anchor recurring NPC schedules and institutional memory;
- field projects can produce world-state consequences without every lesson becoming a combat encounter.

Do not import Naranja/Uva names, faculty, exact curriculum, school history or plot.

### Paldean Winds: an assignment can become public work

Pokémon's official Paldean Winds finale describes three academy students asked by Director Clavell to produce a video for incoming and transfer students. Their project incorporates academy life, Treasure Hunt experiences and regional people and places.

Source: https://www.pokemon.com/uk/news/episode-4-of-pokemon-paldean-winds-now-available

Reusable structure:

- coursework can require collaboration with the world outside campus;
- an assignment can produce an artifact that survives the class;
- institutional commissioning, student authorship, source material and public reception remain distinct;
- a finished project can later become Archive or Media provenance.

### Ranger School: education tied to distinct occupational routes

Pokémon Ranger: Shadows of Almia presents a boarding Ranger School where students can train toward Ranger, Operator or Mechanic roles. Student Rangers use limited school-issued Capture Stylers.

Source: https://bulbapedia.bulbagarden.net/wiki/Ranger_School

Reusable structure:

- one institution can prepare several related professions;
- learner status can carry temporary equipment or permissions that end or change later;
- graduation, employment and professional authority should remain separate events;
- school-issued equipment should have custody and return history rather than become permanent property by default.

Do not import Capture Styler rules into PTU/Caelo.

### Rustboro Trainers' School: instructional site as onboarding surface

The Rustboro Pokémon Trainers' School teaches basic battle information and uses a blackboard to explain status conditions.

Source: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Trainers%27_School

Reusable structure:

- beginner institutions can teach practical safety and common knowledge;
- a school can be useful even when it does not issue major qualifications;
- instructional content can change over time as accepted knowledge changes.

### Alola Trainers' School: alumni remain institutionally relevant

The Alola Trainers' School identifies Ilima as a graduate who continues to visit and is admired by students.

Source: https://bulbapedia.bulbagarden.net/wiki/Trainers%27_School_%28Alola%29

Reusable structure:

- alumni status can persist independently from current enrollment;
- former students can return as guests, mentors, evaluators or community figures;
- later prestige should not rewrite what the person actually completed while enrolled.

## PTU community pattern

A public PokémonTabletop discussion describes an academy-based PTU campaign structured around semesters, recurring school problems, clubs, simulated Ranger exercises and graduation goals.

Source: https://www.reddit.com/r/PokemonTabletop/comments/9nrfy4/help_need_campaign_ideas_for_a_pokemon_academy/

Useful high-level lessons:

- school campaigns work better when classes, clubs, field exercises and personal problems generate different kinds of play;
- simulated emergencies can provide objective variety without requiring every exercise to represent an actual regional disaster;
- a school calendar can create recurring cohorts and institutional callbacks;
- academic progress should not be reduced to repeated 1v1 battles.

This is community practice, not PTU rules authority.

## Education-record and qualification patterns

### Completion, assessment and certification are separate

UNESCO's ISCED terminology distinguishes assessment of learning outcomes, completion of an education programme and certification. A learner can participate in all programme components without necessarily receiving a qualification; certification records achievement following an assessment procedure.

Source: https://isced.uis.unesco.org/wp-content/uploads/sites/15/2021/09/ISCED-T-consultation-draft-EN.pdf

Reusable state grammar:

- COURSE_ATTENDED != COURSE_PASSED
- PROGRAM_COMPONENTS_COMPLETED != QUALIFICATION_AWARDED
- ASSESSMENT_TAKEN != ASSESSMENT_PASSED
- COMPLETION != CERTIFICATION

### Formal, non-formal and informal learning should remain distinguishable

UNESCO's Global Convention defines learning outcomes and distinguishes formal, non-formal and informal learning, while its lifelong-learning work emphasizes recognition across different learning contexts.

Sources:
- https://www.unesco.org/en/legal-affairs/global-convention-recognition-qualifications-concerning-higher-education
- https://www.uil.unesco.org/en/strengthening-recognition-validation-and-accreditation-all-forms-learning-outcomes

Reusable structure:

A person may know something because of school, apprenticeship, mentorship, family practice, field experience or self-study. Narrative provenance should preserve how the competence was evidenced instead of forcing all knowledge into school records.

### A qualification and its explanatory record are different artifacts

The European Diploma Supplement is designed to explain a qualification's institution, level, content and results, but explicitly does not substitute for the original qualification and does not guarantee recognition elsewhere.

Sources:
- https://education.ec.europa.eu/education-levels/higher-education/inclusive-and-connected-higher-education/diploma-supplement
- https://europass.europa.eu/en/stakeholders/education-and-training/issuing-diploma-supplements

Reusable state grammar:

- CREDENTIAL_EXISTS != CREDENTIAL_RECOGNIZED_HERE
- TRANSCRIPT_EXISTS != QUALIFICATION_EXISTS
- RECORD_EXPLAINS_QUALIFICATION != RECORD_IS_QUALIFICATION
- RECOGNITION_REQUESTED != RECOGNITION_GRANTED

No European legal or institutional system is imported into Ouros.

## PTU/Caelo mechanical cross-check

Project-source search found explicit PTU mechanical surfaces for Education Skills, Scholar, Mentor, Lessons, Move Tutor, PokéManiac, Ace Trainer and other Features. For example, Mentor has explicit prerequisites and tutor-point effects, while Scholar directly modifies Education Skill checks. These are mechanics and cannot be granted merely because a character attends school or receives a narrative certificate.

Project evidence: the supplied source index exposes General Education, Medicine Education, Occult Education, Pokémon Education and Technology Education as Skills, plus Features whose prerequisites and effects reference them.

Therefore this pass adopts these hard boundaries:

- SCHOOL_ENROLLMENT != SKILL_RANK_GAIN
- COURSE_COMPLETION != EDGE_GAIN
- GRADUATION != FEATURE_GAIN
- DIPLOMA != TRAINER_CLASS
- TEACHER_TITLE != MENTOR_FEATURE
- PRACTICAL_EXAM != AUTOMATIC_PTU_CHECK
- SCHOOL_BATTLE_WIN != MECHANICAL_PROGRESSION unless governing PTU/Caelo rules explicitly award it

Caelo-specific education institutions, credential rules, school-related Features or progression remain UNKNOWN until verified against the exact supplied Caelo documents.

## Design lessons for Ouros

A durable education layer should preserve the learner's institutional history without pretending to know their private competence. It should remember what was assigned, attempted, observed, assessed, completed, awarded and later recognized.

The most useful narrative consequence is continuity. A teacher can remember an old project. A laboratory can still contain equipment from a previous cohort. A field report can become research evidence. A former student can return as staff. A qualification can be accepted in one institution and questioned in another. A learner can leave without being a failure, return years later, or complete only part of a programme.

The layer should also support schools that do not resemble modern universities. A village seasonal school, Ranger-like field academy, craft conservatory, monastery, mobile expedition school, battle institute, adult-learning hall or research apprenticeship can all use the same continuity primitives if canon authorizes them.

## Originality boundary

This pass borrows only abstract structures: multi-track institutions, field assignments, alumni continuity, temporary student permissions, assessment/completion/certification separation, record provenance and recognition workflows.

It does not copy named Pokémon characters, academy plots, class dialogue, exam questions, quests, proprietary school layouts or distinctive story sequences.