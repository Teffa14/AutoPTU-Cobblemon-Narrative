# Education, Academies & Field Practice Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models mentorship, clubs, workplaces, research programs and battle institutions. This layer adds formal learning institutions without turning school attendance into a universal progression system.

It models:

- schools and academies;
- short training programs;
- enrollment and transfer state;
- curriculum graphs;
- instruction events;
- supervised practice;
- field placements;
- assessment evidence;
- academic records;
- exchange programs;
- institutional feedback;
- alumni/exit state.

It does not grant PTU Skills, Edges, Features, Tutor Moves, stats or combat bonuses unless an authoritative rule explicitly does so.

## 1. Core separation

Keep these concepts separate:

- what was taught;
- what the learner attended;
- what the learner practiced;
- what evidence was observed;
- what the institution concluded;
- what PTU mechanics the character actually has.

An academy may consider someone ready to lead a supervised survey while their PTU Skill Rank remains whatever the authoritative character sheet says.

## 2. Education institution

```yaml
education_institution:
  institution_id: null
  name: null
  location_ids: []
  educational_domains: []
  enrollment_modes: []
  facility_ids: []
  staff_role_ids: []
  curriculum_ids: []
  field_partner_institution_ids: []
  public_mandate: null
  access_policy_ref: null
  history_event_ids: []
  status: proposed
```

Institution types may include academy, school, field institute, battle school, vocational program, community course, research training center or short-term workshop.

These are narrative categories until Ouros canon defines them.

## 3. Enrollment record

```yaml
enrollment_record:
  enrollment_id: null
  actor_id: null
  institution_id: null
  mode: full_time|part_time|exchange|visiting|field_only|guest
  program_id: null
  start_time: null
  expected_end_time: null
  actual_end_time: null
  standing: active
  access_scopes: []
  advisor_ids: []
  record_visibility: private
  provenance_refs: []
```

Enrollment does not imply residence. Residence remains owned by the homes/housing layer.

## 4. Curriculum graph

A curriculum is a dependency graph, not a linear level track.

```yaml
curriculum:
  curriculum_id: null
  institution_id: null
  domain: null
  required_module_ids: []
  elective_module_ids: []
  practicum_ids: []
  assessment_ids: []
  capstone_ids: []
  equivalency_rules: []
  revision: null
```

Possible module states:

- available;
- enrolled;
- attended;
- in_progress;
- completed;
- incomplete;
- reassessment_available;
- waived_by_equivalent_evidence;
- superseded.

None of these states are PTU progression by themselves.

## 5. Instruction event

```yaml
instruction_event:
  event_id: null
  institution_id: null
  instructor_ids: []
  learner_ids: []
  module_id: null
  format: lecture|demonstration|workshop|seminar|lab|field_briefing
  knowledge_topics: []
  source_material_refs: []
  attendance_record_ids: []
  world_state_dependencies: []
```

Routine instruction should compress unless a decision, relationship change, discovery or practical consequence occurs.

## 6. Practice record

```yaml
practice_record:
  practice_id: null
  learner_ids: []
  supervisor_ids: []
  module_id: null
  location_id: null
  practice_kind: field|battle|lab|service|craft|performance|research
  objective_refs: []
  observed_actions: []
  authoritative_result_refs: []
  safety_state: null
  feedback_ref: null
  status: planned
```

Practice records describe what happened. They do not convert narrative performance into mechanical stats.

## 7. Competency evidence

```yaml
competency_evidence:
  evidence_id: null
  actor_id: null
  domain: null
  claim: null
  evidence_type: supervised_observation|report|practical_demo|battle_record|project|presentation|equivalent_record
  source_ref: null
  evaluator_ids: []
  confidence: institutional
  valid_from: null
  review_due: null
```

An institution can use this to decide access or supervision level.

It must not claim a PTU Skill Rank unless the authoritative rules source and character state explicitly support that rank.

## 8. Assessment record

```yaml
assessment_record:
  assessment_id: null
  actor_id: null
  institution_id: null
  module_id: null
  assessment_kind: written|oral|practical|field|battle|portfolio|project
  criteria_refs: []
  evidence_refs: []
  result: completed|needs_reassessment|incomplete|waived|withdrawn
  evaluator_ids: []
  feedback_summary: null
  mechanics_result_refs: []
```

Avoid universal numeric grades unless a specific institution canonically uses them.

## 9. Field practice

Field practice is the primary bridge between education and gameplay.

It may connect to:

- ecology observations;
- route surveys;
- supervised encounters;
- archive work;
- excavation documentation;
- crisis drills;
- clinic support;
- public works inspection;
- media assignments;
- contest production;
- conservation surveys;
- infrastructure maintenance observation;
- research replication.

The existing specialist layer owns the actual world state. Education only owns the learning/assessment wrapper.

## 10. Field placement

```yaml
field_placement:
  placement_id: null
  actor_id: null
  education_institution_id: null
  host_institution_id: null
  supervisor_ids: []
  role_scope: []
  permitted_actions: []
  prohibited_actions: []
  start_time: null
  end_time: null
  expected_evidence: []
  status: planned
```

A placement does not automatically grant the host institution's legal authority.

## 11. Supervision state

Possible narrative supervision states:

- observe_only;
- direct_supervision;
- nearby_supervision;
- independent_with_review;
- evaluator_present;
- suspended_pending_review.

These are institutional permissions, not combat modifiers.

## 12. Exchange and transfer

Keep exchange separate from permanent transfer.

```yaml
exchange_record:
  actor_id: null
  home_institution_id: null
  host_institution_id: null
  accepted_module_ids: []
  equivalency_claims: []
  access_start: null
  access_end: null
  housing_ref: null
  status: active
```

One institution may reject another's equivalency without declaring the learner incompetent.

## 13. Cohorts

Cohorts create repeated contact without forcing social labels.

A cohort may form around:

- intake year;
- short course;
- expedition;
- exchange group;
- practicum;
- research project;
- battle seminar;
- disaster-response training.

Cohort membership may generate shared events but never automatic friendship, rivalry or romance.

## 14. Advisors and instructors

An instructor role is distinct from occupational title and PTU class.

Track:

- subject domain;
- institutional assignment;
- availability;
- current modules;
- supervision load;
- authored qualifications;
- relationship history;
- conflicts of responsibility.

A Gym Leader can teach a short course without the Gym becoming an academy. A researcher can supervise a field placement without becoming a permanent professor.

## 15. Instructor capacity

Education consumes staffing capacity.

If instructors are reassigned during a crisis, the institution may:

- postpone a practicum;
- merge groups;
- bring in a guest instructor;
- switch to independent work;
- reduce supervision scope.

This connects directly to the workplace/staffing layer.

## 16. Learning from failure

Routine failure should usually create a new state rather than terminate a character's path.

Possible outcomes:

- feedback;
- targeted practice;
- reassessment;
- alternate evidence route;
- increased supervision;
- peer practice;
- delayed field access;
- revised project scope.

Suspension, expulsion, discipline or loss of enrollment require authored institutional policy and an actual qualifying event.

## 17. Alternative evidence

Do not force battle performance as universal proof of competence.

Possible evidence:

- field report;
- map;
- successful supervised task;
- oral explanation;
- research contribution;
- practical demonstration;
- project deliverable;
- leadership record;
- observation log;
- battle transcript when battle is relevant.

This enables Trainers with different interests to share the same institution.

## 18. Academic record privacy

Suggested visibility scopes:

- private_to_student;
- advisor_and_student;
- module_staff;
- institution_internal;
- placement_host_limited;
- public_credential_only.

Do not expose detailed records globally in multiplayer.

## 19. Institutional record versus public reputation

A formal assessment and public opinion are different.

A learner may:

- perform well but receive little public attention;
- perform poorly in a public exhibition yet satisfy a private practicum criterion;
- have strong public reputation while lacking a specific institutional requirement.

Use the public-memory layer for reputation.

## 20. Campus state

A campus can contain:

- classrooms;
- library/archive;
- clinic;
- cafeteria;
- workshop;
- battle court;
- greenhouse;
- lab;
- club spaces;
- dorms;
- field staging area;
- public hall.

Each facility remains owned by the relevant subsystem when mechanics matter.

## 21. Campus as a living location

An academy should generate real activity.

Possible visible Minecraft state:

- rotating class groups;
- practicum staging;
- notice boards;
- visiting instructors;
- project displays;
- active club rooms;
- exam/practical days;
- field-trip departures;
- library study periods;
- alumni events;
- construction or repair projects.

Do not simulate every class minute-by-minute.

## 22. Institutional projects

Students can contribute to persistent world change through supervised projects.

Examples:

- habitat survey;
- repair documentation;
- local-history archive;
- public safety map;
- festival production;
- community garden;
- route signage audit;
- emergency drill;
- museum cataloguing;
- research replication.

Projects can update other layers after authoritative completion.

## 23. Teaching by advanced players

Experienced PCs may become guest mentors, demonstrators or placement supervisors if canon and player intent support it.

The system must not automatically declare a retired or high-level PC a teacher.

Teaching creates social/institutional state but no free mechanical rewards.

## 24. Education and age

Ouros has not established:

- compulsory schooling;
- minimum Trainer age;
- graduation age;
- adult education policy;
- child travel rules;
- parental consent rules.

Do not infer them from Pokémon canon or real-world schooling.

Programs should remain age-neutral in generated content until Ouros canon specifies otherwise.

## 25. Credentials and licenses

Ouros has not established the authority of diplomas, licenses, certifications or academic titles.

An institution can issue an internal completion record in proposals, but it cannot create legal authority or PTU mechanics unless canon establishes that connection.

## 26. Tutoring and Move teaching boundary

A narrative class cannot teach a Pokémon a Move merely because the subject concerns that Move.

Tutor Moves, inheritance, Features and prerequisites remain governed by PTU/Caelo and authoritative engine data.

If an educational program includes Move tutoring, the exact mechanic must reference the approved tutoring system.

## 27. Assessment and AutoPTU

AutoPTU may provide authoritative battle evidence for a supervised battle assessment.

Useful evidence may eventually include:

- legal action transcript;
- battle outcome;
- team usage;
- objective completion when objective semantics exist;
- observed tactical choices.

The education layer must never alter the transcript to make a student pass or fail.

## 28. Encounter implementation contracts

### Field Practicum: Ravine Survey

Narrative premise:

A supervised cohort must document a route and wild activity before returning with evidence.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING if rescue/interception is tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if ravine hazards enter battle state
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when assessment relies on them
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Route documentation, supervision and hazard avoidance occur in overworld state. If a legal battle occurs, AutoPTU receives a static arena. Assessment uses the completed field report plus authoritative battle result, not invented hazard rules.

### Aptitude Battle Workshop

Narrative premise:

A supervised exercise evaluates planning and execution against a legal opponent.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when used
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for capable authored evaluator behavior
- adapter/playback: BLOCKING

Reduced version:

Use a conventional legal battle with a fixed approved opponent policy or human-authored choices. Institutional feedback refers only to observable battle facts.

### Emergency Drill: Clear the Exit

Narrative premise:

Students participate in a supervised evacuation drill that becomes complicated by a real wild encounter.

FULL version dependencies:

- complete movement/interception/forced movement: BLOCKING for tactical evacuation
- terrain/weather/hazards/zones/reactions: BLOCKING if smoke/debris changes battle rules
- lifecycle: PARTIAL
- tactical AI: BLOCKING
- adapter/playback: BLOCKING
- explicit ESCAPE/PROTECT/CLEAR_ZONE objective semantics: not verified

Reduced version:

The drill evacuation resolves as overworld state. The unexpected battle is static and conventional. After the battle, the drill record incorporates response time and factual choices without pretending civilians were tactical units.

## 29. Engine capability snapshot relevance

The latest Java evidence strengthens status/lifecycle infrastructure through an ordered reusable status-phase registry. It does not prove complete status behavior.

Therefore this layer can safely implement:

- enrollment;
- curriculum;
- schedules;
- attendance;
- assessment records;
- practicum wrappers;
- supervision state;
- academic privacy;
- institutional projects;
- exchange/transfer records.

Mechanically rich practical assessments still require explicit encounter contracts.

## 30. Integration with existing Ouros layers

Education connects to:

- social bonds: mentors, peers, cohorts;
- workplaces: instructors and staffing;
- science: research practica;
- battle institutions: battle instruction and supervised challenges;
- travel: field trips and exchanges;
- housing: dorms and temporary residence;
- media: student publications;
- care: clinic practica;
- conservation: field stewardship;
- civic governance: public-service projects;
- public memory: alumni and institutional history;
- seasonality: academic terms and recurring programs.

It should reference those systems rather than duplicate them.

## 31. Promotion checklist

Before an education concept becomes canon:

1. Confirm the institution exists in Ouros.
2. Confirm who operates it.
3. Confirm program purpose and access scope.
4. Confirm instructors and facilities.
5. Separate curriculum evidence from PTU mechanics.
6. Define privacy and multiplayer visibility.
7. Validate any Move teaching or mechanical progression against PTU/Caelo.
8. Add encounter contracts where practica depend on battle implementation.
9. Confirm Minecraft representation is feasible.
10. Preserve external-source provenance.

## Open questions

- Which educational institutions exist in Ouros at launch?
- Are academies regional, League-connected, private, civic, guild-run or mixed?
- What age rules exist, if any?
- Are there formal diplomas, licenses or credentials?
- Which PTU/Caelo tutoring rules carry into Ouros?
- Can academic evidence satisfy local access requirements without becoming a PTU stat?
- How should reassessment work in multiplayer?
- How do field trips advance when participants are offline?
- Can high-level PCs teach without transferring mechanical benefits?
- What parts of a campus need physical simulation in Minecraft versus abstract state?