# Working Pokémon, Institutional Roles & Task Partnerships Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already allows institutions to have staff and already treats important Pokémon as persistent actors with agency. The missing layer is the durable state between those systems: a Pokémon performing a bounded task for a workplace, service, project or institution.

This layer must let a Pokémon build a work history without becoming equipment, an interchangeable species template, an employee record, a permanent institutional asset or a source of invented PTU mechanics.

It supports:

- routine work that should usually compress;
- temporary assignments;
- on-call or emergency participation;
- relief/replacement teams;
- workplace training and supervised practice;
- equipment handoffs;
- observed acceptance, hesitation, refusal and withdrawal;
- role review and retirement;
- institutional continuity after a famous working Pokémon leaves;
- one-time help from wild Pokémon without capture.

## Authority boundaries

This layer owns institutional role/task participation for Pokémon.

It does not replace neighboring authorities.

Pokémon Agency owns:

- persistent Pokémon identity;
- custody and residence;
- Trainer/Pokémon associations;
- observed cooperation/refusal history outside this work-specific context;
- mechanical Loyalty/Command references when authoritative;
- release and rehoming continuity.

Workplaces owns:

- workplace identity;
- service domains;
- staffing demand;
- human occupational roles;
- shift/backlog state;
- operational availability.

Credentials/Permissions owns formal qualifications or permissions when Ouros canon defines them.

Care/Welfare owns health, diagnosis, treatment and care state.

Aging/Retirement owns broader life-stage and role-transition history.

Material Culture/Items owns harnesses, tools, uniforms, carts, radios and other physical equipment.

Domain layers such as Emergency Services, Rail, Postal, Fisheries or Water Service own the service operation itself.

AutoPTU owns battle legality, combat commands, mechanical Capabilities, Skills, Moves, Abilities, Items, Features and results.

## Core separation

Use this state chain:

```text
institutional need
        ↓
task request
        ↓
role requirements
        ↓
individual eligibility evidence
        ↓
participation opportunity
        ↓
observed acceptance / refusal / unavailable state
        ↓
work assignment
        ↓
participation events
        ↓
outcome / interruption / handoff
        ↓
role review
        ↓
historical work record
```

No arrow grants mechanical competence or emotional state by itself.

## 1. Pokémon work role

A role is an institutional task definition, not a Pokémon species.

```yaml
pokemon_work_role:
  work_role_id: null
  institution_id: null
  workplace_id: null
  role_name: null
  service_domain: null
  task_scope: []
  permitted_locations: []
  supervision_mode: direct|team|remote|none_defined
  qualification_requirement_refs: []
  authoritative_mechanics_requirement_refs: []
  equipment_requirement_refs: []
  welfare_constraint_refs: []
  battle_control_scope_ref: null
  role_status: proposed|active|paused|retired
  provenance_refs: []
```

Examples:

- freight-handling partner at a depot;
- route-inspection partner;
- rescue-search partner;
- nursery support partner;
- ferry-deck helper;
- construction-material handling partner;
- field-survey companion;
- archive retrieval helper;
- temporary flood-response helper.

A role never means every Pokémon of a named species qualifies.

## 2. Task request

The institution should ask for work before a Pokémon is assigned.

```yaml
pokemon_task_request:
  task_request_id: null
  institution_id: null
  workplace_id: null
  requested_role_id: null
  task_description: null
  location_ids: []
  start_window: null
  end_window: null
  expected_duration_band: null
  priority: routine|time_sensitive|emergency
  required_mechanics_refs: []
  required_equipment_refs: []
  supervision_requirement: null
  requested_candidate_ids: []
  status: open|filled|withdrawn|expired|cancelled
  source_event_id: null
```

This supports a Poké-Job-like institutional request without importing Sword/Shield rewards, duration formulas or Type-based job optimization.

## 3. Individual eligibility evidence

Species lore can make a role plausible. It cannot complete eligibility.

```yaml
work_eligibility_assessment:
  assessment_id: null
  pokemon_id: null
  work_role_id: null
  assessed_at: null
  authoritative_capability_refs: []
  qualification_refs: []
  observed_task_history_refs: []
  equipment_fit_refs: []
  environment_compatibility_refs: []
  welfare_constraint_refs: []
  result: eligible|eligible_with_limits|not_eligible|unknown
  assessor_id: null
  provenance_refs: []
```

A Pokédex statement such as Machoke helping with heavy goods can justify authoring such a job in the world. It cannot provide carrying limits, work speed or permission for a particular individual.

## 4. Participation opportunity

Before an assignment begins, preserve whether participation was actually offered and what was observed.

```yaml
work_participation_opportunity:
  opportunity_id: null
  pokemon_id: null
  task_request_id: null
  offered_by_actor_id: null
  offered_at: null
  observed_response: approached|engaged|remained|hesitated|withdrew|refused|unavailable|unknown
  observation_refs: []
  mechanical_command_ref: null
  resulting_assignment_id: null
```

`observed_response` is factual metadata. It does not assign emotions, Loyalty or consent to unrelated future tasks.

## 5. Work assignment

```yaml
pokemon_work_assignment:
  assignment_id: null
  pokemon_id: null
  work_role_id: null
  task_request_id: null
  assignment_kind: routine|temporary|on_call|training|relief|emergency|one_time
  assigned_start: null
  expected_end_condition: null
  actual_end: null
  team_actor_ids: []
  supervisor_actor_id: null
  institution_responsibility_ref: null
  equipment_assignment_refs: []
  battle_control_scope_ref: null
  status: planned|accepted|active|paused|interrupted|completed|declined|ended
  interruption_reason_ref: null
  provenance_refs: []
```

The assignment can end without failure.

Examples:

- task completed;
- Pokémon withdrew;
- weather closed the site;
- equipment no longer fit;
- another team took over;
- the service changed;
- the Pokémon retired;
- the institution cancelled the job.

## 6. Participation event

A long assignment should accumulate specific observations rather than a vague “worked well” score.

```yaml
work_participation_event:
  participation_event_id: null
  assignment_id: null
  pokemon_id: null
  timestamp: null
  task_step: null
  location_id: null
  observed_action: null
  observed_result: null
  interruption_ref: null
  mechanical_resolution_ref: null
  equipment_refs: []
  observer_refs: []
  provenance_refs: []
```

Useful observations:

- moved one specified crate;
- stopped before entering a corridor;
- returned to a known station after a route inspection;
- accepted a harness;
- removed or resisted an accessory;
- waited while a teammate completed a step;
- left the task area during an alarm;
- rejoined after a break;
- declined one repeated attempt.

Do not procedurally infer:

- pride;
- laziness;
- loyalty;
- resentment;
- “work ethic”;
- fear;
- boredom;
- friendship with staff;
- permanent consent.

## 7. Workload ledger

Ouros may need longitudinal workload history without inventing fatigue points.

```yaml
pokemon_workload_ledger:
  pokemon_id: null
  period_start: null
  period_end: null
  assignment_refs: []
  active_work_windows: []
  off_duty_windows: []
  travel_windows: []
  emergency_deployment_count: null
  interrupted_assignment_count: null
  care_review_refs: []
  notes: null
```

This ledger supports story continuity such as “this Pokémon has covered six storm deployments this year.”

It does not create:

- exhaustion damage;
- fatigue Status;
- stat penalties;
- mandatory rest intervals;
- work-capacity numbers.

Any such mechanics require PTU/Caelo authority.

## 8. Equipment assignment and fit

Physical work gear is first-class persistent material state.

```yaml
work_equipment_assignment:
  equipment_assignment_id: null
  pokemon_id: null
  item_instance_ids: []
  work_role_id: null
  issued_at: null
  fit_assessment_ref: null
  accepted_use_observation_refs: []
  removed_at: null
  condition_refs: []
  returned_to_inventory_ref: null
```

A harness, vest, cart or radio can be necessary for the world-state job while still having no PTU Item effect.

Evolution can invalidate fit without automatically invalidating the role. Refit, redesign or role review can happen afterward.

## 9. Relief coverage and handoff

Pokémon workers must not be treated as interchangeable units.

```yaml
work_handoff:
  handoff_id: null
  outgoing_assignment_id: null
  incoming_assignment_id: null
  task_state_refs: []
  equipment_handoff_refs: []
  route_or_site_knowledge_refs: []
  unresolved_warning_refs: []
  completed_at: null
```

A successor can inherit responsibility and information.

It does not inherit:

- the outgoing Pokémon's identity;
- relationships;
- public reputation;
- memories;
- Loyalty;
- mechanical build;
- species-specific assumptions.

## 10. Temporary wild assistance

A wild Pokémon may participate in one bounded task.

```yaml
temporary_work_partnership:
  temporary_work_id: null
  pokemon_id: null
  institution_or_actor_id: null
  task_request_id: null
  observed_entry_event_id: null
  task_scope: []
  custody_changed: false
  capture_changed: false
  expected_end_condition: null
  observed_exit_event_id: null
```

This is useful for:

- local wildlife helping clear a flood obstruction;
- a wild Flying Pokémon relaying one emergency message;
- a resident Pokémon guiding workers around a hazard;
- a familiar wild Pokémon temporarily assisting a survey.

Completion does not grant capture eligibility, ownership, Loyalty or future availability.

## 11. Role review

```yaml
pokemon_work_role_review:
  review_id: null
  pokemon_id: null
  work_role_id: null
  review_reason: routine|equipment_change|evolution|incident|care_change|retirement|service_change|other
  evidence_refs: []
  outcome: continue|continue_with_limits|pause|change_role|end_role|unknown
  effective_at: null
  author_actor_id: null
```

This record can hand off to the Aging/Retirement layer when a role ends because of a longer-term transition.

A review does not diagnose health. Care owns diagnosis.

## 12. Retirement and post-role continuity

Work retirement is a role transition.

A retired Pokémon may:

- remain with the same Trainer;
- remain resident at the institution;
- move to another home;
- take a different role;
- participate in occasional public events;
- continue non-work routines;
- become a research or public-memory subject;
- stop participating institutionally entirely.

Retirement does not mean death, weakness, release or relationship loss.

## 13. Institutional authority versus battle control

Work authority must never silently become PTU command authority.

A dispatcher may assign a rescue role.

A station manager may request a routine task.

A technician may ask a partnered Pokémon to interact with equipment.

None of those facts alone establish that the person can legally issue combat Orders or control the Pokémon inside AutoPTU.

When a working Pokémon enters battle, the encounter contract must resolve `battle_control_scope_ref` from authoritative PTU/Caelo/party state.

## 14. Workplaces integration

Workplaces should consume this layer for Pokémon-specific staffing.

Example:

```yaml
workplace_staffing_projection:
  workplace_id: MERIDIAN_FREIGHT_HALL
  human_assignment_refs: []
  pokemon_work_assignment_refs: []
  available_service_capacity_claim: null
  coverage_notes: null
```

A Pokémon being absent can reduce a service if the role is genuinely required. It should not automatically create a quest. The service can:

- use relief coverage;
- reduce scope;
- reschedule work;
- use a human/mechanical alternative;
- temporarily close one function.

## 15. Care and welfare integration

This layer may record that a welfare review exists or that an assignment was paused after one.

It must not diagnose or treat.

Examples of safe state:

- role paused pending care review;
- equipment use stopped after observed discomfort;
- work window shortened by institutional policy;
- Pokémon unavailable during treatment.

Unsafe procedural inference:

- “refused task therefore injured”;
- “worked many shifts therefore exhausted”;
- “old therefore medically unfit.”

## 16. Historical work culture

Pokémon work can affect culture and institutions over decades.

Examples:

- a construction technique attributed historically to Conkeldurr;
- a freight hall designed around large partnered Pokémon even after mechanization;
- a rescue unit keeping old harnesses in a museum after changing methods;
- a station maintaining a retired Pokémon's route board as public history;
- a guild continuing a technique originally learned through human-Pokémon collaboration.

Historical attribution remains a claim unless evidence supports it.

## 17. Public reputation

A famous working Pokémon can become a public figure, but the Fandom/Public Memory layers own that attention.

The work record should preserve the operational facts.

Public claims such as:

- “never missed a shift”;
- “saved the station”; or
- “was fired”

may be true, false, incomplete or disputed.

## 18. Minecraft/Cobblemon projection

Minecraft is presentation and interaction, not work-state authority.

Do not infer a work assignment because a loaded Pokémon:

- stands near a workstation;
- wears a cosmetic;
- is leashed;
- follows an NPC;
- sits in a vehicle;
- has a species associated with a job;
- has a name tag matching a staff roster.

Likewise, chunk unloading cannot end the assignment or erase the workload ledger.

The server should project current work state into Minecraft with bounded visible behaviors and then write back only validated events.

## 19. Routine compression

Successful routine work should usually compress.

A recurring assignment can advance from one validated period to the next without simulating every crate, patrol, shift or delivery.

Surface narrative when something changes:

- first assignment;
- first refusal/withdrawal observation;
- equipment change;
- service disruption;
- emergency deployment;
- handoff;
- role conflict;
- evolution affecting equipment/site access;
- retirement;
- return after a long absence;
- public misunderstanding;
- unexpected cross-layer consequence.

## 20. Anti-exploit rules

The system must not permit players to:

- farm XP by assigning endless jobs;
- generate Items/rewards by repeating narrative shifts;
- bypass capture or Loyalty rules through employment;
- force wild Pokémon into persistent roles through repeated proximity;
- create qualifications by placing a Pokémon at a workplace;
- duplicate institutional workers through chunk reloads;
- use employment to bypass roster/storage limits;
- obtain automatic battle control over institutional Pokémon;
- claim a species-wide job bonus without individual mechanical evidence.

## 21. Encounter design boundary

Working Pokémon can be part of battle scenes, but their occupational objective and tactical behavior are separate.

FULL versions may require:

- moving task partners;
- escorts and protected routes;
- withdrawal or task-abandonment decisions;
- interacting with work equipment;
- objective-aware AI;
- environmental hazards;
- semantic Minecraft playback.

REDUCED versions should resolve the work process first in world state, remove noncombat workers/equipment from tactical exposure, freeze a legal arena and let AutoPTU resolve only the actual combatants.

## 22. Capability-family mapping

For mechanically rich work encounters, classify dependencies under the permanent engine map:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

A work role never promotes any family.

## 23. Mechanical non-inferences

Do not infer:

- Machoke Pokédex work lore -> PTU Lift/carry capacity;
- Timburr construction lore -> legal building action;
- Conkeldurr concrete lore -> Technology Education or crafting Feature;
- Electric type -> certified power-grid worker;
- Water type -> potable-water worker;
- Fire type -> safe furnace operator;
- Flying type -> passenger transport eligibility;
- Psychic type -> dispatcher/telecommunications access;
- captured -> on duty;
- assigned -> obedient in battle;
- work refusal -> low Loyalty;
- repeated work -> XP;
- long tenure -> veteran bonus;
- uniform/harness -> Armor or Item effect;
- retirement -> stat loss.

## 24. World-state implementation contracts

Future implementation should expose at least:

- `POKEMON_WORK_ROLE_STATE`;
- `POKEMON_TASK_REQUEST_STATE`;
- `POKEMON_WORK_ELIGIBILITY_ASSESSMENT`;
- `WORK_PARTICIPATION_OPPORTUNITY_STATE`;
- `POKEMON_WORK_ASSIGNMENT_STATE`;
- `POKEMON_WORKLOAD_LEDGER`;
- `WORK_EQUIPMENT_ASSIGNMENT_STATE`;
- `WORK_HANDOFF_STATE`;
- `TEMPORARY_WILD_WORK_PARTNERSHIP`;
- `POKEMON_WORK_ROLE_REVIEW`;
- `WORKPLACE_TO_POKEMON_AGENCY_HANDOFF`;
- `WORKING_POKEMON_TO_CARE_HANDOFF`;
- `WORKING_POKEMON_TO_MINECRAFT_PROJECTION`;
- `WORKING_POKEMON_TO_BATTLE_CONTROL_HANDOFF`.

## 25. Canon questions deliberately left open

This layer does not decide:

- whether Pokémon are legally employees, partners, contractors or something else;
- whether Pokémon receive money, goods, care, housing or no formal compensation;
- whether work participation requires a Trainer/custodian's approval;
- how a Pokémon's own agreement is established in canon;
- which institutions may house working Pokémon;
- which jobs have formal qualification standards;
- what workload limits exist;
- what retirement policies exist;
- whether any profession-specific PTU Features apply;
- how carrying, lifting, mounted transport or task-specific Capabilities work;
- whether wild Pokémon may enter recurring institutional roles.

Those decisions require canon review and, where mechanical, authoritative PTU/Caelo validation.
