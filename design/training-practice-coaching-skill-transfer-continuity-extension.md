# Ouros Training, Practice, Coaching & Skill-Transfer Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-30
Research provenance: `research/2026-08-30-training-practice-coaching-skill-transfer-scan-158.md`

## Purpose

Ouros already has mentorship relationships, formal education, battle institutions, scouting, downtime and PTU progression boundaries. This extension owns a narrower missing continuity: a practice objective across one or more sessions, what activities actually occurred, what was observed, what feedback was given, how the plan changed, and whether a separate governing mechanical transaction was later authorized.

It does not own mentorship relationships, school enrollment, formal challenge qualification, battle results, scouting knowledge, PTU advancement or tactical AI.

## 1. Core practice thread

```yaml
training_thread:
  training_thread_id: null
  learner_refs: []
  partner_pokemon_refs: []
  coach_refs: []
  host_institution_ref: null
  practice_site_refs: []
  objective_refs: []
  source_prompt_refs: []
  current_plan_ref: null
  session_refs: []
  feedback_refs: []
  demonstration_refs: []
  progression_transaction_refs: []
  state: PROPOSED | ACTIVE | PAUSED | REVISED | SATISFIED_NARRATIVELY | RETIRED
  canon_status: proposed | canon_approved
  provenance_refs: []
```

A training thread can exist without any mechanical reward. `SATISFIED_NARRATIVELY` means the authored practice objective reached its own closure. It does not grant a PTU benefit.

## 2. Learning objective

```yaml
practice_objective:
  objective_id: null
  training_thread_id: null
  author_or_requester_refs: []
  objective_kind: TACTICAL_CONCEPT | COORDINATION | ROUTINE | FIELD_SKILL_CONTEXT | MOVE_TUTOR_CONTEXT | RETRAINING_CONTEXT | PERFORMANCE | OTHER_AUTHORED
  description: null
  evidence_expected_refs: []
  mechanics_gate_ref: null
  created_at: null
  superseded_by: null
```

Examples of system-neutral tactical concepts include spacing, timing, switching judgment, target prioritization, resource discipline and communication. These labels never modify calculations or AI weights by themselves.

## 3. Source prompt

A plan should have a reason.

```yaml
training_prompt:
  prompt_id: null
  source_kind: POSTBATTLE_REVIEW | SCOUTING_CLAIM | MENTOR_SUGGESTION | SELF_SELECTED | COURSE_ACTIVITY | CLUB_PROJECT | UPCOMING_FORMAT | FIELD_EVENT | OTHER
  underlying_ref: null
  observed_issue_or_goal: null
  created_at: null
  visibility_scope: null
```

Competitive Scouting owns the underlying knowledge if the prompt came from replay analysis. Battle Institutions owns the battle review. Social Bonds owns the mentor relationship. This extension only references those facts.

## 4. Practice plan

```yaml
practice_plan:
  plan_id: null
  training_thread_id: null
  objective_refs: []
  exercise_refs: []
  intended_sequence: []
  participant_refs: []
  planned_site_refs: []
  equipment_or_asset_refs: []
  intended_battle_contract_refs: []
  scheduled_window_refs: []
  review_points: []
  mechanics_review_required: true
  created_at: null
  retired_at: null
  supersedes_plan_ref: null
```

A plan describes intent. It cannot guarantee attendance, availability, legal roster state, access to a Tutor mechanic or successful learning.

## 5. Exercise reference, not duplicate ownership

Battle Institutions already defines `training_exercise` for institutional contexts. Formal Education already defines educational activities. Clubs and mentors can create exercises through their owners.

This extension uses a reference wrapper:

```yaml
practice_exercise_ref:
  exercise_ref_id: null
  owner_system: BATTLE_INSTITUTION | EDUCATION | CLUB | MENTORSHIP | DOWNTIME | LOCAL_AUTHORED
  underlying_ref: null
  intended_objective_refs: []
  tactical_contract_ref: null
  repeat_policy_ref: null
```

A local authored exercise may exist only when it does not invent PTU mechanics.

## 6. Practice session

```yaml
practice_session:
  session_id: null
  training_thread_id: null
  plan_ref: null
  exercise_ref: null
  started_at: null
  ended_at: null
  location_ref: null
  participant_refs: []
  pokemon_participant_refs: []
  observer_refs: []
  battle_spec_refs: []
  battle_result_refs: []
  activity_evidence_refs: []
  interruption_ref: null
  completion_state: PLANNED | STARTED | COMPLETED | PARTIAL | CANCELLED | INTERRUPTED
  provenance_refs: []
```

`SESSION_COMPLETED` means the scheduled activity occurred. It says nothing about permanent competence.

## 7. Observation during practice

```yaml
practice_observation:
  observation_id: null
  session_id: null
  observer_id: null
  subject_refs: []
  observed_at: null
  observation_kind: TACTICAL_EVENT | ROUTINE_EXECUTION | COMMUNICATION_EVENT | ERROR | SUCCESS | ADAPTATION | OTHER
  description: null
  authoritative_event_ref: null
  certainty: OBSERVED | SUPPORTED | UNCERTAIN
  visibility_scope: null
```

If the claim depends on combat, the strongest source is an authoritative AutoPTU semantic event or result. A visual animation alone cannot certify a hidden Move, Ability, Feature, HP value or tactical cause.

## 8. Coach feedback

```yaml
coach_feedback:
  feedback_id: null
  training_thread_id: null
  session_ref: null
  coach_or_observer_id: null
  observation_refs: []
  feedback_text: null
  recommendation_tags: []
  confidence_band: LOW | MEDIUM | HIGH | REVIEWED
  created_at: null
  later_revision_ref: null
  visibility_scope: null
```

Feedback is an attributed claim. A respected coach can be mistaken, incomplete or focused on a different goal.

Hard rule:

`COACH_FEEDBACK != CANONICAL_OPTIMAL_TACTIC`

## 9. Demonstration record

```yaml
practice_demonstration:
  demonstration_id: null
  training_thread_id: null
  objective_ref: null
  session_ref: null
  evidence_refs: []
  demonstration_scope: null
  outcome: DEMONSTRATED | PARTIAL | NOT_DEMONSTRATED | INCONCLUSIVE
  conditions_ref: null
  observed_by: []
  created_at: null
```

A demonstration proves only what the evidence supports under the recorded conditions.

`DEMONSTRATED_ONCE != MASTERED`

`NOT_DEMONSTRATED != INCAPABLE`

## 10. Plan revision

```yaml
training_revision:
  revision_id: null
  training_thread_id: null
  prior_plan_ref: null
  new_plan_ref: null
  trigger_refs: []
  revision_reason: null
  created_at: null
```

Useful triggers include a new battle, evolution, changed roster, changed challenge contract, coach disagreement, unavailable facility, injury/care restriction if source-backed, or a learner choosing a different priority.

Historical plans remain in the Chronicle. A revised plan does not retroactively make earlier practice irrational.

## 11. Mechanical progression gate

Narrative continuity may request or reference a governing transaction. It never grants the transaction itself.

```yaml
training_mechanics_gate:
  mechanics_gate_id: null
  requested_effect_kind: MOVE_TUTOR | MENTOR_LESSON | RETRAINING | EDGE | FEATURE | SKILL_CHANGE | STAT_CHANGE | OTHER_SOURCE_BACKED
  governing_source_ref: null
  governing_engine_contract_ref: null
  eligibility_state: UNKNOWN | INELIGIBLE | ELIGIBLE_PENDING_TRANSACTION | COMPLETED_BY_AUTHORITY
  transaction_ref: null
  reviewed_at: null
```

The authoritative progression owner must validate prerequisites, costs, Tutor Points, action frequency, legal target, level or other governing conditions.

## 12. Mechanical transaction handoff

When a legitimate PTU/Caelo mechanical event occurs, link it rather than reinterpret the practice history.

```yaml
training_progression_link:
  training_thread_id: null
  mechanics_gate_ref: null
  authoritative_transaction_ref: null
  effective_at: null
  narrative_context_only: true
```

The causal statement is narrow: the transaction occurred in this training context. The narrative system does not claim that the number of sessions mechanically caused it unless the adopted rule explicitly says so.

## 13. Repetition and anti-farming

Repeated practice can remain meaningful socially or diagnostically after mechanical reward eligibility is exhausted.

```yaml
practice_repeat_state:
  exercise_ref: null
  learner_ref: null
  informative_repetitions: []
  compressed_repetition_count: null
  governing_reward_policy_ref: null
  next_distinct_learning_condition: null
```

Rules:

1. Do not create infinite XP, Tutor Points, Features, ranks, prestige or relationship gains from repetition.
2. Compress low-information repetition when no new fact, choice, social event or governing transaction occurs.
3. Preserve notable exceptions such as a new participant, changed roster, new constraint or first successful demonstration.
4. A practice session may still be roleplayed after rewards are unavailable.

## 14. Coach disagreement

Two coaches may disagree without one being secretly wrong.

```yaml
training_advice_conflict:
  conflict_id: null
  training_thread_id: null
  feedback_refs: []
  shared_evidence_refs: []
  differing_assumption_refs: []
  learner_decision_ref: null
  later_observation_refs: []
```

This produces useful player choice. The engine must not expose a hidden “correct coach” marker unless canon evidence eventually establishes one.

## 15. Training venue continuity

The venue itself belongs to its institution/location owner. This extension can link recurring use.

Useful persistent facts:

- which exercises are currently available;
- instructor schedule references;
- equipment availability references;
- temporary closure or relocation;
- archived session notices;
- recurring learner cohorts;
- changed practice layout after an authored facility event.

`VENUE_OPEN != COACH_AVAILABLE`

`COACH_AVAILABLE != MECHANICAL_TUTOR_ELIGIBLE`

## 16. Pokémon agency boundary

A Pokémon participating in training remains an actor with existing partnership/custody state.

Training participation cannot establish:

- ownership transfer;
- permanent roster assignment;
- capture permission;
- breeding permission;
- mechanical Loyalty change;
- consent to every future drill;
- Move eligibility outside the governing source.

`TRAINED_WITH_ACTOR != OWNED_BY_ACTOR`

## 17. Practice battle classification

```yaml
practice_battle_link:
  session_id: null
  battle_spec_ref: null
  governing_contract_ref: null
  formal_record_eligible: false
  injury_policy_ref: null
  reward_policy_ref: null
  result_ref: null
```

The battle contract must explicitly define whether the practice match is an exhibition, ordinary spar, formal challenge, simulation or another approved category.

`SPARRING_WIN != FORMAL_QUALIFICATION`

`TRAINING_BATTLE != FORMAL_BATTLE_RECORD`

## 18. Roster boundary

A practice roster can be chosen for a drill without becoming the roster for a future Gym, tournament or mission.

`PRACTICE_ROSTER != FORMAL_CHALLENGE_ROSTER`

The future encounter must perform its own eligibility and participant selection through Ouros/AutoPTU contracts.

## 19. Scouting integration

Competitive Scouting may create a prompt such as “practice against a revealed positioning pattern.”

Training may record that such a drill occurred.

Neither layer may then claim the future opponent will repeat that pattern. Scouting staleness remains in force.

`PRACTICED_COUNTER != FUTURE_COUNTER_GUARANTEED`

## 20. Formal education integration

A course can require practice or assess a practical. Education owns attendance, submission and academic assessment. This extension can own the learner's continuing practice thread when it extends beyond one course activity.

`COURSE_PRACTICAL_COMPLETED != PTU_ADVANCEMENT`

## 21. Mentorship integration

Social Bonds owns whether a mentor relationship exists. This extension owns the bounded exercise history attached to that relationship.

A stranger can coach one session without becoming a permanent mentor. A mentor can remain important while being unavailable for current practice.

`COACHED_ONCE != MENTOR_RELATIONSHIP`

`MENTOR_RELATIONSHIP != CURRENT_MECHANICAL_MENTOR_ACTION`

## 22. Downtime integration

Downtime can allocate fictional time to practice. This extension records what the allocated activity actually produced as narrative evidence.

No generic conversion from elapsed hours to mechanical power is authored here.

## 23. Practice without combat

Training content should not require battle.

Examples:

- review a replay with a coach;
- walk a positioning diagram on an empty court;
- rehearse signals with a partner Pokémon;
- identify legal options from a fixed board state;
- practice equipment setup;
- teach a novice a procedure;
- compare two prior battles;
- run a field observation routine.

These can generate memories, feedback and demonstrations without AutoPTU.

## 24. Encounter contract — Pressure Drill: Protect the Marker

Premise:

A coach wants to test spacing and protection decisions around a marked location during a controlled spar.

Full intended version:

- objective-aware protect/deny behavior;
- Intercept and forced movement where legal selected content uses them;
- reaction windows if the exercise depends on them;
- full lifecycle for an objective that changes between rounds;
- tactical AI that understands the drill's protect/deny objective;
- authoritative playback.

Reduced version:

- the marker is static scenery outside BattleSpec semantics;
- explicit combatants use a conventional audited battle contract;
- static geometry only;
- the coach records observations after the battle;
- no claim that the marker itself was tactically protected by engine rules.

Permitted narrative output: `STATIC_SPARRING_COMPLETED` plus specific authoritative observations.

Forbidden transition: `SPARRING_COMPLETED => PROTECTION_MASTERY`.

## 25. Encounter contract — Positioning Labyrinth Scrimmage

Premise:

A practice court uses fixed barriers to make routes and range choices visible.

Full intended version:

- changing barriers or zones;
- possible forced movement and reaction interactions;
- round-based layout changes;
- AI tactical policy aware of route-control objectives.

Reduced version:

- fixed blockers established before initiative;
- ordinary legal movement and targeting;
- no dynamic walls, hazards or scripted displacement;
- coach feedback is based only on observed battle events.

Permitted output: `FIXED_LAYOUT_SCRIMMAGE_COMPLETED`.

## 26. Encounter contract — Partner Rotation Exercise

Premise:

Several learners practice adapting to different partners across a session.

Full intended version:

- staged participant changes under one exercise lifecycle;
- controlled handoffs between rounds;
- potentially different tactical policies by partner;
- authoritative continuity of state where the approved contract requires it.

Reduced version:

- each pairing is a separate BattleSpec;
- Ouros performs an overworld/session checkpoint between battles;
- no HP/status/initiative/resource state crosses BattleSpecs unless an explicit verified contract authorizes it;
- each result is linked to the same training thread.

Permitted output: a sequence of bounded battle results and observations.

## 27. Encounter contract — Intercept Demonstration

Premise:

An instructor demonstrates a situation where Intercept may legally matter, then lets learners review what occurred.

Full intended version:

- actual AutoPTU Intercept logic;
- selected content whose Intercept dependencies are verified;
- authoritative candidate discovery, ordering, line geometry, Shift legality, RNG/resource consumption and displacement;
- reaction/lifecycle support as required by the exact rule path;
- playback that mirrors semantic engine output.

Reduced version:

- use a static reviewed encounter that does not require Intercept to complete;
- if Intercept occurs through the verified current engine path, record it;
- never script a replacement Intercept in Minecraft to guarantee the lesson.

`INTENDED_LESSON != REQUIRED_SCRIPTED_OUTCOME`

## 28. Permanent capability dependency model

All mechanically rich training encounters must classify against the same project families:

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
- Minecraft/Cobblemon/Craftics adapter/playback support.

An implemented Intercept slice does not promote complete movement or generalized reactions.

## 29. Minecraft/Cobblemon/Craftics boundary

Safe presentation after Ouros decides state may include:

- coaches and learners occupying a training venue;
- practice markers and static obstacles;
- notice boards and session schedules;
- visible demonstrations replayed from authoritative events;
- Pokémon models, animation, cries and movement for presentation;
- equipment and venue changes;
- post-session dialogue and notes.

Minecraft/Cobblemon/Craftics must not decide:

- who is a combatant;
- whether a practice objective was mastered;
- PTU HP/status/damage;
- legal Moves, Tutor effects, Features or Items;
- Intercept candidates or outcome;
- mechanical advancement;
- whether feedback is correct;
- formal qualification;
- future tactical AI policy.

## 30. PTU/Caelo unresolved boundary

Remain UNKNOWN until source-checked and approved for Ouros:

- exact training-derived XP policies;
- exact Caelo downtime/training changes, if any;
- Tutor Point generation and refresh policy under the adopted source set;
- Mentor/Move Tutor availability and NPC eligibility;
- retraining availability and any Caelo changes;
- injury policy for sparring and exhibitions;
- mechanical Loyalty consequences of training;
- exact rules for teaching Trainer Skills, Edges or Features if any;
- any generic coaching bonus;
- any universal practice-time threshold that grants advancement.

## 31. Promotion rules

A proposed training fact may become canon only when:

1. the session or event actually occurred;
2. participants and location are consistent with world state;
3. attributed feedback remains a claim unless separately proven;
4. any battle result comes from AutoPTU or an approved resolver;
5. any mechanical advancement has its own authoritative transaction;
6. no Minecraft/Cobblemon battle authority leaked into the decision;
7. external inspiration remains transformed and attributed.

## Conclusion

This extension lets Ouros remember training as lived history rather than a button that converts time into power. Coaches can teach, learners can practice, plans can change, sessions can matter socially and tactically, and source-backed PTU progression can occur when legitimately authorized without collapsing those separate layers into one hidden progression meter.