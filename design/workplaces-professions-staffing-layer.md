# Workplaces, Professions & Staffing Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models institutions and services, but those institutions need people and Pokémon who actually keep them running.

This layer models ordinary work without turning every occupation into a PTU class or every shift into a quest.

The goals are:

- make services depend on plausible staffing;
- let NPC careers change over time;
- support work-related story hooks without constant grind;
- let players understand why a service is available, delayed or unavailable;
- preserve ordinary life between major arcs;
- keep occupational identity separate from PTU mechanics.

## 1. Occupation is not a Trainer Class

A narrative occupation is a world-state role.

Examples:

- baker
- ferry engineer
- archive clerk
- field technician
- courier
- clinic receptionist
- mechanic
- reporter
- ranger aide
- researcher
- groundskeeper
- construction worker
- nursery attendant
- market inspector
- line cook

None of those titles automatically grants:

- a Skill Rank;
- a Trainer Class;
- an Edge;
- a Feature;
- a Move;
- a Capability;
- a combat bonus;
- a crafting result;
- a legal authority.

Mechanical competence must come from PTU/Caelo and current implementation state.

## 2. Core objects

### WORKPLACE

```yaml
workplace_id: null
institution_id: null
location_id: null
service_domains: []
operational_state: normal
required_role_slots: []
current_staffing: []
work_backlog_ids: []
shift_template_ids: []
training_capacity: null
critical_dependency_ids: []
public_hours_claim: null
actual_availability: null
history_event_ids: []
```

### OCCUPATIONAL_ROLE

```yaml
role_id: null
role_name: null
workplace_id: null
role_domain: null
responsibilities: []
qualification_requirements: []
authority_scope: []
mechanical_claims: []
status: active
```

A role can exist even when vacant.

### WORK_ASSIGNMENT

```yaml
assignment_id: null
actor_ids: []
workplace_id: null
role_id: null
assignment_type: routine|temporary|coverage|training|fieldwork|project
start_time: null
expected_end_time: null
actual_end_time: null
status: planned
priority: normal
source_reason: null
world_state_dependencies: []
```

### SHIFT_COMMITMENT

```yaml
shift_id: null
actor_id: null
workplace_id: null
role_id: null
window_start: null
window_end: null
status: scheduled
coverage_actor_id: null
handoff_required: false
```

This is coarse world scheduling, not payroll simulation.

### QUALIFICATION_CLAIM

```yaml
qualification_claim_id: null
actor_id: null
domain: null
claim_source: self|institution|record|license|mentor|observation
claim_text: null
confidence: unresolved
mechanics_reference: null
provenance_refs: []
```

A title or reputation does not prove a PTU Skill Rank.

## 3. Staffing capacity

A service should have a bounded ability to operate.

Possible staffing states:

- fully staffed
- thin coverage
- understaffed
- specialist unavailable
- training-heavy
- emergency coverage
- temporarily closed

This state can affect:

- opening hours;
- waiting time;
- which services are available;
- whether field assignments can be accepted;
- whether an NPC is present;
- whether another institution must provide support.

It must not create invented PTU penalties or bonuses.

## 4. Work backlog

Workplaces can accumulate unresolved work when demand exceeds capacity.

```yaml
work_backlog_item:
  backlog_id: null
  workplace_id: null
  work_type: null
  source_event_id: null
  priority: normal
  required_role_ids: []
  required_resource_ids: []
  status: queued
  consequence_if_delayed: []
```

Examples:

- ferry inspections delayed after a storm;
- archive requests piling up during a public investigation;
- clinic referrals waiting for a specialist;
- repair orders accumulating after a blackout;
- festival permits creating extra administrative load;
- workshop commissions delayed by missing materials.

A backlog is a story generator only when it intersects player interests or world consequences.

## 5. Handoffs

Knowledge should not teleport between workers.

A handoff can transfer:

- task state;
- observations;
- unresolved questions;
- access keys/credentials;
- physical custody;
- responsibility;
- warnings.

Poor handoff may create uncertainty, but the generator must not assume incompetence or misconduct without evidence.

## 6. Training state

Workplace training is different from PTU character progression.

A training record may store:

```yaml
training_record:
  learner_id: null
  supervisor_id: null
  workplace_id: null
  role_domain: null
  training_tasks: []
  observed_events: []
  demonstrated_world_competencies: []
  unresolved_mechanics_requirements: []
  status: in_progress
```

This can change narrative trust or assignment eligibility inside an institution.

It cannot directly grant PTU Edges, Features, Skill Ranks or Moves.

## 7. Multiple roles per character

A character may simultaneously be:

- Gym Leader;
- bakery owner;
- parent;
- club mentor;
- civic representative;
- seasonal event judge.

Availability should depend on current commitments.

Changing one role does not erase the others.

## 8. Career history

Important NPCs can maintain a career timeline.

```yaml
career_record:
  actor_id: null
  entries:
    - role_id: null
      workplace_id: null
      start_time: null
      end_time: null
      exit_reason: null
      event_refs: []
```

Allowed exit reasons must be authored or evidenced.

Do not invent:

- firing;
- resignation;
- retirement;
- promotion;
- disciplinary action;
- injury;
- death.

## 9. Temporary coverage

Temporary coverage can make the world feel alive.

Examples:

- a café employee covers a festival booth;
- a mechanic is reassigned to emergency transport repairs;
- a researcher temporarily joins a field expedition;
- a nurse assists another town during a crisis;
- a Gym Trainer helps staff a public event.

This changes where an NPC is expected to be.

It should not automatically create a quest.

## 10. Service continuity

Institutions should survive individual absence when redundancy exists.

A workplace may have:

- primary specialist;
- deputy;
- trainee;
- partner institution;
- emergency contractor;
- reduced-service mode.

This prevents every missing NPC from shutting down an entire region.

## 11. Institutional knowledge

Some knowledge belongs to a workplace rather than one person.

Examples:

- maintenance manual;
- clinic procedure;
- route schedule;
- archive index;
- supplier list;
- emergency contact tree;
- recipe book;
- survey protocol.

Institutional knowledge can be incomplete, outdated or dependent on experienced workers.

This integrates with the media/information, technology, science, food, care and travel layers.

## 12. Workplace culture

Workplace culture may be authored through observable practices:

- how shifts hand off;
- whether training is formal;
- whether workers rotate duties;
- how much autonomy junior staff receive;
- whether mistakes are documented;
- whether outsiders are welcomed;
- how Pokémon participate.

Do not reduce culture to one morale score.

## 13. Pokémon participation in work

Pokémon can participate as persistent actors rather than generic labor tokens.

Record:

- individual Pokémon identity;
- current handler/partner where relevant;
- assignment;
- observed suitability;
- required legal Capability/Move/Ability when mechanics matter;
- work history;
- refusal/withdrawal events if explicitly observed;
- care/recovery implications.

Do not infer that a species is automatically suitable just because a videogame job requested its Type.

Do not invent energy output, lifting capacity, production yield or working duration.

## 14. Pokémon agency boundary

A Pokémon being owned does not mean the narrative system can freely commit it to indefinite work.

Ouros should preserve explicit player choice for PC-owned Pokémon assignments.

NPC-owned or institutional Pokémon may have authored routines.

Repeated refusal, fear, fatigue or avoidance can be recorded as observation but should not be converted into a diagnosis or personality claim without evidence.

## 15. Work postings

A posting is institutional demand, not necessarily a playable quest.

```yaml
work_posting:
  posting_id: null
  workplace_id: null
  role_or_task: null
  reason: null
  required_qualifications: []
  duration_class: null
  status: open
  applicant_ids: []
  gameplay_conversion: none
```

Possible conversions:

- background staffing change;
- NPC career event;
- player side job;
- full quest;
- club project;
- temporary assignment.

## 16. Player employment

If players take jobs, the narrative layer should track:

- employer/institution;
- role;
- schedule commitments;
- completed assignments;
- public responsibilities;
- conflicts with other commitments;
- relationships created through work;
- exit history.

Do not automatically convert employment into salary math, XP, Skills or Features until canon rules exist.

Routine shifts should compress.

Meaningful shifts should surface only when something changes.

## 17. Work conflict

A workplace conflict does not automatically mean villainy.

Possible causes:

- resource shortage;
- incompatible priorities;
- unclear authority;
- outdated procedure;
- staffing shortage;
- training gap;
- schedule conflict;
- institutional disagreement;
- safety concern;
- conflicting interpretations of evidence.

The antagonist layer should be used only when actual opposed goals or harmful actions exist.

## 18. Service demand pulses

Existing world events can temporarily alter demand.

Examples:

- festival -> hospitality, transport and sanitation demand;
- storm -> repair, clinic and communications workload;
- migration -> ranger/research staffing;
- tournament -> venue, security, food and transport staffing;
- public investigation -> archive/media/case workload;
- construction project -> technicians, surveyors and logistics.

This lets existing systems create staffing consequences without new random events.

## 19. NPC schedule abstraction

Use three levels:

1. baseline pattern;
2. current commitments;
3. player-proximate materialization.

Do not simulate every minute.

Example:

```yaml
npc_schedule:
  actor_id: npc_42
  baseline:
    weekday_day: workplace_a
    weekday_evening: home
  commitments:
    - assignment_id: repair_17
      override_window: 2026-08-21T10:00/16:00
  materialization_policy: nearby_or_story_relevant
```

## 20. Retirement and succession

A worker leaving a role creates a succession question only when the role matters.

Possible outcomes:

- internal promotion;
- trainee takes over;
- external hire;
- role split between staff;
- service reduced;
- institution restructures;
- vacancy persists.

Do not decide a PC's retirement or post-career life automatically.

## 21. Integration with existing layers

Workplaces connect to:

- social bonds: coworkers, mentors, supervisors;
- material culture: workshops and commissions;
- food: kitchens, farms, hospitality;
- care: clinics and provider capacity;
- technology: maintenance crews;
- travel: transport operators;
- media: reporters and editors;
- science: lab staff and field teams;
- civic governance: public-service staffing;
- conservation: ranger/steward teams;
- cases: investigators and evidence custodians;
- crises: emergency staffing and mutual aid;
- public memory: long-serving workers and institutional history.

## 22. Minecraft representation

Possible visible state:

- staffed/unstaffed counters;
- rotating NPC presence;
- closed sections;
- queue or notice board state;
- active worksite props;
- trainee/supervisor pairs;
- repair scaffolding;
- temporary festival staffing;
- workers moving between nearby stations;
- Pokémon visibly assisting with authored tasks.

Do not require every worker to remain loaded in a chunk.

## 23. Encounter dependency boundary

Most workplace stories should resolve outside combat.

When battle intersects a workplace, use the permanent engine capability categories and provide FULL/REDUCED contracts.

Never duplicate missing PTU rules in Minecraft scripts.

## 24. Canon boundaries still unresolved

Ouros has not yet established:

- labor law;
- wage standards;
- contracts;
- unions;
- guild authority;
- licenses;
- occupational certification systems;
- retirement systems;
- workweek norms;
- child labor rules;
- Pokémon labor rights;
- compensation for Pokémon participation.

Do not silently import a modern real-world labor system.

These require deliberate canon decisions.

## 25. Promotion checklist

Before any workplace concept becomes canon:

1. Confirm the workplace actually exists in Ouros.
2. Confirm its institutional owner/operator.
3. Confirm role names and responsibilities.
4. Separate narrative qualification from PTU mechanics.
5. Check player/Pokémon agency implications.
6. Confirm any schedule or service impact is feasible in Minecraft.
7. Add encounter dependency contracts if combat is involved.
8. Preserve provenance for any externally inspired structure.