# Pokémon Work Role Participation Extension

Status: proposed systems design. Not established Ouros canon.

Research basis: `research/2026-08-27-pokemon-work-role-participation-scan-83.md`

## Purpose

Ouros already has a workplace/staffing layer and a Pokémon agency/partnership layer. This extension connects them around one exact Pokémon participating in one exact work task over time.

The goal is to make workplaces visibly depend on persistent Pokémon actors without turning Pokémon into generic labor resources, assigning occupations by species/type, inventing productivity statistics, or allowing Minecraft/Cobblemon presence to create work or battle authority.

## Scope boundary

This extension owns:

- Pokémon work-assignment identity;
- assignment windows and status;
- task-requirement references;
- evidence used to justify participation;
- handler/supervisor scope;
- observed participation events;
- pauses, withdrawal and transfer/handoff history;
- links to welfare/safety state;
- work-history summaries.

It does not own:

- the workplace or human staffing model;
- Pokémon ownership/custody/party mechanics;
- PTU Loyalty or obedience;
- medical diagnosis/treatment;
- worksite safety authority;
- project completion or service output;
- wages, labor law, compensation or employment rights;
- Moves, Abilities, Capabilities or Trainer Features;
- battle participants or tactical state.

Those remain with their existing systems.

## Core separation

Keep these facts distinct:

```text
persistent Pokémon identity
        ↓
current association/custody/residence
        ↓
workplace task requirement
        ↓
evidence-backed assignment decision
        ↓
active participation window
        ↓
observed participation events
        ↓
work output owned by another system
        ↓
work-history record
```

No step authorizes the next one automatically.

A Pokémon can live at a workplace without being on assignment. A Pokémon can be assigned without gaining new PTU mechanics. A completed assignment does not prove ownership, friendship, Loyalty, expertise in every related task or willingness to repeat it.

## 1. Pokémon work assignment

```yaml
pokemon_work_assignment:
  assignment_id: null
  pokemon_id: null
  workplace_id: null
  project_or_service_ref: null
  role_label: null
  task_scope_refs: []
  requirement_profile_ref: null
  eligibility_evidence_refs: []
  supervisor_actor_ids: []
  handler_scope_ref: null
  equipment_refs: []
  planned_start: null
  planned_end: null
  actual_start: null
  actual_end: null
  status: PLANNED
  pause_reason_refs: []
  withdrawal_event_ref: null
  handoff_refs: []
  safety_refs: []
  care_refs: []
  output_refs: []
  provenance_refs: []
```

Suggested status values:

- PLANNED
- READY_FOR_REVIEW
- ACTIVE
- PAUSED
- LIMITED
- WITHDRAWN
- HANDED_OFF
- COMPLETE
- CANCELED
- SUPERSEDED

`COMPLETE` only means the bounded assignment ended as recorded. It does not assert that the entire project or service succeeded.

## 2. Task requirement profile

A workplace should describe the task before choosing a Pokémon.

```yaml
task_requirement_profile:
  requirement_id: null
  workplace_id: null
  task_description: null
  world_task_type: null
  required_observed_competencies: []
  mechanical_evidence_required: []
  environment_constraints: []
  equipment_requirements: []
  supervision_requirements: []
  safety_dependencies: []
  care_constraints: []
  acceptable_substitution_policy_ref: null
  mechanics_review_required: false
```

Examples of precise requirements:

- can traverse the actual water route currently used by the service;
- has demonstrated ability to carry this category of container safely under supervision;
- has the authoritative Move/Capability required by a reviewed field procedure;
- is already trained on the site's signaling routine;
- can enter the work zone under the current safety plan;
- can use a specific issued device whose compatibility was verified.

Bad requirement:

`requires Electric-type`.

Better requirement:

`requires verified illumination capability for the night inspection procedure`.

If PTU/Caelo defines an exact mechanical requirement, link to that evidence rather than replacing it with narrative shorthand.

## 3. Capability evidence snapshot

Assignments can depend on evidence that changes later.

```yaml
pokemon_work_capability_snapshot:
  snapshot_id: null
  pokemon_id: null
  captured_at: null
  authoritative_mechanical_refs: []
  observed_work_history_refs: []
  supervised_trial_refs: []
  known_move_refs_relevant_to_task: []
  known_ability_refs_relevant_to_task: []
  movement_capability_refs: []
  equipment_compatibility_refs: []
  unresolved_claims: []
```

This snapshot is evidence for the assignment decision, not a duplicate Pokémon stat block.

Evolution, Move changes, injury/recovery, new equipment or changed site conditions may require a new review. Do not silently carry forward the old decision forever.

## 4. Eligibility decision

```yaml
work_participation_review:
  review_id: null
  assignment_id: null
  reviewer_or_institution_id: null
  requirement_profile_ref: null
  evidence_snapshot_ref: null
  decision: APPROVED | APPROVED_WITH_LIMITS | MORE_EVIDENCE_REQUIRED | NOT_APPROVED | PAUSED
  limits: []
  rationale_refs: []
  mechanics_review_refs: []
  timestamp: null
```

The decision should be explainable from explicit evidence.

No hidden productivity, intelligence, obedience or species score is permitted.

## 5. Handler and supervision scope

Working alongside a Pokémon does not grant unlimited authority over it.

```yaml
work_supervision_scope:
  scope_id: null
  assignment_id: null
  supervisor_ids: []
  permitted_task_categories: []
  permitted_locations: []
  permitted_windows: []
  emergency_stop_actor_ids: []
  mechanical_command_ref: null
  temporary_partnership_ref: null
  handoff_allowed_to: []
  status: ACTIVE
```

This can support:

- one familiar handler only;
- a trained group of supervisors;
- a temporary institutional partnership;
- a PC explicitly assigning one of their Pokémon for a bounded task;
- a wild Pokémon cooperating for one operation without capture.

It cannot invent Command mechanics or override PTU Loyalty.

## 6. Participation events

Record small observable facts.

```yaml
pokemon_work_participation_event:
  event_id: null
  assignment_id: null
  pokemon_id: null
  timestamp: null
  location_id: null
  event_type: CHECKED_IN | TASK_STARTED | TASK_STEP_OBSERVED | PAUSED | WITHDREW | RESUMED | HANDED_OFF | TASK_WINDOW_ENDED
  observation_refs: []
  supervisor_refs: []
  authoritative_mechanics_refs: []
  output_refs: []
```

Examples:

- carried three marked containers from staging to the approved shelf;
- performed the established signal after a handler cue;
- stopped at the boundary of a closed work zone;
- left the task area after a loud equipment fault;
- returned after the area reopened;
- completed one survey circuit.

These observations do not automatically become emotion, Loyalty, fatigue diagnosis or global competence.

## 7. Pause and withdrawal

A pause is a normal state transition, not a failure state.

Potential evidence-backed reasons:

- worksite closure;
- handler unavailable;
- care/recovery restriction;
- equipment unavailable;
- changed environment;
- task completed early;
- temporary partnership scope ended;
- explicit PC choice;
- observed refusal/withdrawal;
- assignment under review;
- project/service suspended.

Never invent a psychological explanation merely to make the transition dramatic.

## 8. Handoff and substitution

A substitution must compare the new individual against the task requirements.

```yaml
pokemon_work_handoff:
  handoff_id: null
  from_assignment_id: null
  to_assignment_id: null
  outgoing_pokemon_id: null
  incoming_pokemon_id: null
  task_state_ref: null
  equipment_custody_refs: []
  briefing_refs: []
  new_eligibility_review_ref: null
  timestamp: null
```

Same species does not waive the new review.

A new Pokémon may need:

- a different route;
- a supervised trial;
- different equipment;
- a different handler;
- a reduced task scope;
- no assignment at all.

## 9. Work history

Important Pokémon can accumulate occupational history without gaining an occupational class.

```yaml
pokemon_work_history:
  pokemon_id: null
  assignment_ids: []
  workplaces: []
  observed_task_categories: []
  supervisor_history: []
  pause_withdrawal_refs: []
  safety_event_refs: []
  care_event_refs: []
  public_summary_refs: []
```

This history can create callbacks and credible future opportunities.

It does not grant XP, Features, Skills, Moves or passive bonuses unless governing rules explicitly do so through an authoritative subsystem.

## 10. Work output handoff

The owning system decides whether meaningful work succeeded.

Examples:

- a Maintenance work order may cite participation events but still require inspection before closure;
- a Courier route may cite a transport partner but still need a delivery handoff;
- a Conservation survey may cite field assistance but Science/Conservation evaluates the evidence;
- a Care facility may record an assistance routine, but Care owns patient outcomes;
- a public-works project may record material moved, while Civic/Maintenance owns construction status.

This prevents the participation layer from becoming a universal task-resolution engine.

## 11. Safety and welfare integration

Safety state can pause an assignment without changing the Pokémon's general relationship state.

Worksite Safety owns:

- unsafe-area restrictions;
- incident/near-miss review;
- temporary controls;
- return-to-work authorization.

Care owns:

- health observations;
- diagnosis/treatment;
- recovery readiness where medically relevant.

This extension stores links only.

A work label never overrides a closed area, care restriction or authoritative mechanical condition.

## 12. Pokémon agency integration

Every assignment references the same persistent Pokémon identity used by `pokemon-agency-partnership-release-layer.md`.

Important invariants:

- custody does not imply assignment;
- assignment does not imply ownership;
- ownership does not imply unlimited work scope;
- temporary partnership may permit one bounded task without capture;
- release does not erase prior work history;
- former workplace association can remain historical after rehoming or retirement;
- a wild helper can repeatedly cooperate while remaining wild.

## 13. PC-owned Pokémon

For player-controlled Pokémon, assignments require explicit player intent when the player is available to decide.

The system should never automatically commit a PC Pokémon to:

- an overnight shift;
- indefinite institutional work;
- a hazardous assignment;
- a battle;
- a transfer of custody;
- an equipment loan;
- a remote expedition.

A world simulation may remember a prior standing arrangement only when that arrangement itself was explicitly established and remains valid.

## 14. Institutional and NPC-associated Pokémon

NPC/institutional Pokémon may have authored recurring work patterns.

Use schedule abstraction:

- baseline routine;
- current assignment override;
- player-proximate materialization.

An unloaded chunk does not end the assignment. A loaded entity does not begin one.

## 15. Wild helpers

Wild Pokémon may participate through a temporary-partnership or observed-cooperation record.

Possible examples:

- returns during a seasonal cleanup;
- assists with one rescue window;
- guides researchers through a familiar route;
- moves debris during a habitat event;
- warns staff through an established observable signal.

Do not call this employment, ownership, domestication or permanent service unless canon establishes such a relationship.

## 16. Minecraft/Cobblemon representation

Follow `design/cobblemon-runtime-authority-boundary.md`.

Safe reuse opportunities, after concrete API review, include:

- Pokémon models/forms/textures;
- persistent overworld entities;
- pose/animation surfaces;
- walking/swimming/flying presentation;
- cries and sounds;
- particles;
- interaction prompts;
- item/block props;
- entity tracking;
- client synchronization;
- networking;
- menus/status displays;
- worksite blocks and geometry;
- custom/addon animations mapped to an Ouros-owned work state.

The Cobblemon Poser system is especially relevant for presenting idle, movement, look and authored named animations. Animation is presentation only.

Forbidden inference examples:

- entity standing by machine -> assignment ACTIVE;
- Pokémon playing an animation -> task mechanically completed;
- Pokémon nearby -> eligible replacement worker;
- Pokémon has battle-side Cobblemon Move state -> Ouros work capability accepted without authoritative review;
- entity despawns -> assignment ended;
- entity attacks nearby threat -> automatically enrolled as AutoPTU combatant.

## 17. Battle boundary

A workplace incident may create a battle, but work assignment state never selects battle participants by itself.

Required flow:

`Ouros work/world state -> Ouros encounter composition -> explicit BattleSpec -> AutoPTU state/result -> adapter -> Cobblemon presentation -> reviewed world-state writeback`

Nearby workers, working Pokémon, clients and supervisors remain noncombatants unless Ouros explicitly includes them in the encounter manifest.

No work-role bonus may modify tactical state unless it corresponds to a verified PTU/Caelo rule and an AutoPTU implementation path.

## 18. Mechanically rich encounter profile — Worksite Withdrawal With Partner Pokémon

Narrative premise:

A routine worksite must suspend operations after a local Pokémon conflict or environmental interruption. Humans and working Pokémon need to clear the active area.

Intended full version:

- several noncombatants withdraw toward safe exits;
- some working Pokémon may be explicit tactical participants only if Ouros selects them;
- access lanes can matter;
- Intercept/forced movement may matter near chokepoints;
- the opponent AI may prefer withdrawal/territorial goals rather than KO;
- tactical environmental effects apply only if PTU/Caelo and AutoPTU support them;
- playback keeps work-state actors distinct from combatants.

Capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle as required by roster;
- terrain/weather/hazards/zones/reactions if environment becomes tactical;
- move-specific behavior;
- abilities;
- items where relevant;
- Trainer Features/perks where relevant;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:

- work stops before battle creation;
- humans and every non-selected working Pokémon evacuate through Ouros world state;
- assignments become PAUSED, HANDED_OFF or RELEASED_FROM_WINDOW as appropriate;
- Ouros freezes a reviewed static arena;
- AutoPTU receives only the explicitly selected combatants;
- ordinary legal battle resolution occurs;
- after battle, Worksite Safety/Maintenance/Workplaces determine whether activity resumes;
- no escort, crowd, scripted Intercept, work-role bonus or environmental damage is emulated in Minecraft.

## 19. Mechanically rich encounter profile — Service Route Partner Interruption

Narrative premise:

A Pokémon participating in a transport, survey or delivery service is present when a route becomes contested.

Full version may need:

- ESCAPE/CLEAR_ROUTE/PROTECT objective logic;
- complete movement and Intercept;
- terrain/weather when the route actually maps to PTU mechanics;
- tactical AI that understands retreat or route denial;
- adapter playback of the persistent partner and service state.

Reduced version:

The service pauses in world state. The working Pokémon remains outside the tactical grid unless Ouros explicitly selects it as a legal combatant. If selected, its work assignment grants no tactical bonus. AutoPTU resolves the battle conventionally, then Travel/Courier/Science/Conservation decides whether the service continues.

## 20. Noncombat encounter — Assignment Suitability Review

This can execute as world-state content now.

Inputs:

- task requirement;
- work history;
- current authoritative mechanical references;
- supervised trial observations;
- equipment compatibility;
- safety/care constraints;
- supervisor availability.

Possible outcomes:

- approved;
- approved for narrower scope;
- supervised trial required;
- delayed pending equipment;
- rejected for this task;
- assignment no longer needed.

No battle capability is required unless the trial itself invokes PTU mechanics.

## 21. Anti-false-completion rules

- a known Move does not prove all uses of that Move are legal outside battle;
- one lifting/carrying scene does not prove a universal carrying capacity;
- a species entry does not prove every individual can perform a specialized task;
- repeated successful assignments do not create a hidden productivity bonus;
- refusal does not alter Loyalty unless the authoritative system does so;
- an authored animation does not resolve the task;
- worksite geometry does not become PTU terrain automatically;
- Cobblemon battle state does not decide whether a working Pokémon fights;
- one implemented Intercept sub-contract does not prove full reactive interception.

## 22. Canon questions intentionally unresolved

- Which Ouros cultures and institutions commonly assign Pokémon to work?
- What terminology do they use: partner, worker, assistant, service Pokémon, crew member, something else?
- What consent/agency expectations are culturally or legally established?
- Which institutions maintain formal training/work records?
- Are there roles that require a specific human supervisor or handler qualification?
- How are wild recurring helpers understood socially?
- Are compensation, rest, duty limits or retirement practices formalized anywhere?
- Which work tasks have authoritative PTU/Caelo mechanical requirements?
- Which Cobblemon APIs can safely project work poses/routines without adopting battle state?

Until reviewed, all answers remain proposed or unknown.