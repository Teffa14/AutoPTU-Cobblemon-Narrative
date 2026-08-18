# Care, recovery and Pokémon welfare layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs a persistent care layer between tactical battle resolution and narrative world state.

AutoPTU determines legal combat outcomes. The care layer records what happens afterward without fabricating healing, Injury removal, status recovery, Medicine effects or treatment legality.

The layer also supports non-combat welfare: rest, safe housing, wild-Pokémon treatment, specialist referrals, clinic capacity, convalescence, enrichment and ecological health signals.

## Core separation

Always keep these distinct:

1. mechanical health state;
2. observed condition;
3. diagnosis or hypothesis;
4. treatment plan;
5. treatment actually completed;
6. narrative recovery state;
7. public knowledge of the case.

Example:

A Pokémon limps after a battle.

`observable: favors_left_leg`

This does not automatically mean:

`mechanical_injury: leg_fracture`

or:

`diagnosis: fracture`

or:

`public_fact: trainer injured Pokémon through negligence`

Each claim needs its own authority and provenance.

## Primary objects

### CARE_CASE

Persistent record for an entity receiving or requiring care.

Suggested schema:

```yaml
care_case_id: null
subject_id: null
subject_type: POKEMON | TRAINER | WILD_POKEMON
origin_event_refs: []
mechanical_state_refs: []
observations: []
diagnoses: []
treatment_orders: []
treatment_events: []
facility_id: null
care_team_ids: []
status: OPEN | STABILIZED | RECOVERING | REFERRED | DISCHARGED | CLOSED
privacy_scope: PRIVATE
opened_at: null
closed_at: null
```

The object never invents mechanical state. `mechanical_state_refs` point to authoritative AutoPTU/PTU records.

### CARE_FACILITY

A persistent location or service capable of providing one or more kinds of care.

```yaml
facility_id: null
location_id: null
facility_type: POKEMON_CENTER | CLINIC | HOSPITAL | FIELD_STATION | SHELTER | SANCTUARY | MOBILE_CARE
service_tags: []
staff_ids: []
specialties: []
capacity_state: NORMAL
supply_state_refs: []
transport_links: []
referral_links: []
world_state_dependencies: []
```

`facility_type` is descriptive until Ouros canon defines institutions.

No service tag grants a mechanical effect by itself.

### CARE_PROVIDER

Represents an NPC, PC, institution or verified Pokémon participant involved in care.

```yaml
provider_id: null
actor_id: null
provider_role: CLINICIAN | NURSE | FIELD_MEDIC | CARETAKER | TECHNICIAN | COUNSELOR | TRANSPORT | SPECIALIST | VOLUNTEER
verified_mechanical_qualifications: []
world_specialties: []
affiliations: []
availability_state: null
```

Narrative occupation and mechanical qualifications are separate.

A person described as a nurse does not automatically receive Medicine Skill ranks, Edges or Features.

## Mechanical authority boundary

The care layer may read:
- HP;
- Injuries;
- persistent status state;
- legal restorative use;
- battle events;
- action history;
- validated Features/Edges/Skills;
- current Pokémon capabilities.

The care layer may not directly write those values unless it is calling an authoritative PTU/AutoPTU service specifically designed to perform that legal change.

Narrative events such as `received_care`, `visited_clinic` or `resting_at_center` do not heal anything on their own.

## Recovery lifecycle

Proposed lifecycle:

INCIDENT
→ ASSESSMENT
→ STABILIZATION
→ TREATMENT
→ RECOVERY
→ READINESS_CHECK
→ DISCHARGE
→ FOLLOW_UP

Not every case needs every phase.

Routine Center use may compress almost entirely.

A significant Injury, unknown condition, wildlife cluster or facility disruption may expose more of the lifecycle as playable content.

## Routine healing compression

Routine legal healing should remain fast in the narrative interface when no interesting decision exists.

Example:

Player reaches an operating Center with no unusual condition and requests standard treatment.

System:
1. validate facility availability;
2. call authoritative healing/recovery routine;
3. advance required world time if applicable;
4. record treatment event;
5. resume play.

Do not manufacture a quest every time the player needs ordinary care.

## Recovery as world time

When governing rules require time, treatment should interact with the existing world clock.

Possible consequences:
- transport departure missed;
- contest registration closes;
- weather window changes;
- NPC schedule advances;
- faction operation progresses;
- another team member becomes available for a local activity.

The generator may use those consequences only when the relevant clocks already exist.

## Clinic capacity

Facilities can have operational states independent of healing rules.

Suggested capacity states:
- NORMAL
- BUSY
- STRAINED
- OVERLOADED
- PARTIAL_SERVICE
- CLOSED

Causes may include:
- crisis influx;
- staff absence;
- supply interruption;
- infrastructure failure;
- wildlife incident;
- festival crowding;
- transport disruption;
- regional outbreak authored by canon/event state.

Capacity may influence queueing, referrals or narrative access, but it must not change PTU healing values unless an explicit rule says so.

## Referral graph

Not every facility should solve every problem.

A local clinic may refer to:
- a regional hospital;
- species specialist;
- toxicology lab;
- breeder/nursery expert;
- rehabilitation site;
- Ranger/rescue organization;
- research institution;
- specialized Center.

This turns care infrastructure into part of the travel and settlement graph.

## Wild-Pokémon care

Wild Pokémon can receive care without becoming owned.

Suggested case states:

```yaml
wild_patient:
  persistent_entity_id: null
  capture_status: WILD
  consent_behavior_observations: []
  safe_release_location_id: null
  home_collective_id: null
  return_conditions: []
```

Important rules:
- treatment does not grant ownership;
- transport to a clinic does not grant capture rights;
- a healed wild Pokémon may leave;
- repeated return to a facility can become observed behavior, not automatic friendship;
- release location must consider current ecology and collective state.

## Welfare observation

Welfare is represented through evidence-rich observations before any interpretation.

Examples:
- eating normally;
- refusing offered food;
- sleeping frequently;
- grooming;
- seeking isolation;
- initiating play;
- avoiding a stimulus;
- willingly entering a familiar safe area;
- repeated pacing;
- responding normally to handler cues.

These observations can support authored assessments.

The generator must not assign hidden emotions, trauma diagnoses, loyalty changes or personality rewrites from one observation.

## Rest and enrichment

Some spaces exist primarily for recovery and quality of life rather than medical treatment.

Possible facility features:
- quiet garden;
- species-appropriate water area;
- exercise yard;
- shaded rest area;
- grooming station;
- supervised social area;
- training-free day program;
- sensory enrichment;
- temporary boarding.

These are narrative/environmental features unless later tied to explicit mechanics.

## Rehabilitation

Rehabilitation differs from instant treatment.

A rehabilitation plan may track authored milestones such as:
- tolerates short walks;
- resumes normal feeding;
- returns to light training;
- accepts handling again;
- safely uses a movement capability;
- rejoins its normal social group.

These milestones must never replace PTU checks or mechanical readiness.

A Pokémon can be mechanically healed while an authored story arc about trust, conditioning or adaptation continues.

## Caregiver workload and institutional memory

Important caregivers can have schedules, specialties and limits.

A clinic may remember:
- frequent route injuries;
- recurring seasonal cases;
- a species it often treats;
- a past crisis;
- a facility upgrade;
- a shortage;
- a former trainee now working elsewhere.

Institutional memory can create hooks without exposing private patient information.

## Medical privacy

Care cases require stronger privacy than ordinary rumor state.

Suggested visibility:
- SUBJECT_ONLY
- SUBJECT_AND_CARE_TEAM
- PARTY_SHARED
- INSTITUTION_INTERNAL
- PUBLIC_AGGREGATE
- PUBLIC_BY_CONSENT

Do not automatically publish:
- exact Injury count;
- diagnoses;
- treatment history;
- private Trainer health state;
- inferred causes;
- sensitive relationship information.

Public aggregate data may state something like:

“the clinic has treated many Poison-type exposure cases from Route 6 this week”

without identifying patients.

## Population-health signals

A facility can aggregate care events into ecological or infrastructure clues.

Proposed `health_signal`:

```yaml
signal_id: null
facility_id: null
location_scope: []
observation_type: null
case_count_band: null
confidence: LOW | MEDIUM | HIGH
source_case_ids_private: []
public_summary: null
related_hazard_ids: []
related_ecology_ids: []
```

Examples:
- repeated burns from one industrial zone;
- respiratory symptoms after a cave opens;
- nesting injuries near construction;
- unusual fatigue among a migrating population;
- multiple Trainers arriving dehydrated from the same route.

The signal creates an investigation opportunity, not an automatic causal conclusion.

## Care-driven quest grammar

Useful objective verbs:
- ASSESS
- STABILIZE
- ESCORT_PATIENT
- DELIVER_SUPPLY
- LOCATE_SPECIALIST
- TRACE_EXPOSURE
- BUILD_SAFE_ROUTE
- OBSERVE_RECOVERY
- REOPEN_FACILITY
- SUPPORT_RELEASE
- VERIFY_ENVIRONMENT
- RESTORE_SERVICE
- CHECK_ON_PATIENT
- STAFF_TEMPORARILY

Do not generate `CURE`, `REMOVE_INJURY` or similar mechanical verbs unless the rules engine exposes a legal action for that exact state.

## Care and crisis integration

The crisis layer can create demand.
The care layer handles patients and facility state.
The settlement layer handles long-term service changes.
The material layer handles supply provenance.
The travel layer handles evacuation/referral routes.
The case layer may investigate negligence, contamination or sabotage if evidence supports it.
The ecology layer may receive aggregate health signals.

These systems should exchange state instead of each independently inventing consequences.

## Care and social integration

Care scenes can reveal relationships through observable actions:
- someone waits at the clinic;
- someone brings supplies;
- someone volunteers;
- a mentor visits;
- a rival checks on the patient;
- a Pokémon stays nearby.

The system records those actions.

It does not infer love, forgiveness, guilt, trauma or friendship without authored evidence.

## Minecraft representation

Possible physical expressions:
- Center reception;
- treatment room access state;
- waiting area;
- ambulance/rescue transport;
- outdoor recovery garden;
- temporary field clinic;
- supply shelves changing during shortages;
- NPC shift changes;
- wild patient resting in a protected enclosure;
- notice board showing aggregate advisories;
- closed wing during infrastructure damage.

Persistent patients should retain entity identity even if represented abstractly while unloaded.

## AutoPTU writeback

Battle end should emit a bounded care-relevant summary rather than prose inference.

Example:

```yaml
battle_medical_summary:
  battle_id: null
  participant_id: null
  hp_end: null
  injuries_end: null
  persistent_statuses: []
  fainted: false
  significant_rules_events: []
```

The narrative layer can then decide whether routine healing, rest, referral or an authored medical story is appropriate.

## Anti-exploit rules

Do not let players farm narrative benefits by repeatedly injuring/healing Pokémon.

Potential safeguards:
- routine cases have low/no narrative weight;
- callbacks require contextual significance, not treatment count;
- institutional reputation comes from meaningful contribution, not healing loops;
- wild-patient encounters require valid world events or ecology state;
- special referrals require actual conditions, not repeated Center visits.

## Canon boundary

Before any care system becomes canon, humans must approve:
- institution types and names;
- Trainer vs Pokémon treatment norms;
- privacy expectations;
- wild-Pokémon handling policy;
- sanctuary/boarding policy;
- specialist roles;
- whether Centers are free and how available they are;
- how Caelo-specific healing modifications carry into Ouros.

## Mechanical review checklist

Before implementation verify against supplied PTU/Caelo sources and AutoPTU:
- Injury acquisition and removal;
- natural healing;
- extended rest;
- Pokémon Center timing;
- daily Injury-removal limits;
- restorative items;
- bandages/poultices;
- Medicine Education;
- Medic Training and relevant Features/Edges;
- fainting rules;
- status removal;
- trainer healing;
- Pokémon healing;
- any Caelo homebrew changes;
- server persistence of post-battle health state.

## Design outcome

A good care layer makes damage matter without making recovery tedious.

It creates continuity between battle, travel, ecology and settlement life while preserving PTU as the authority for what healing actually does.
