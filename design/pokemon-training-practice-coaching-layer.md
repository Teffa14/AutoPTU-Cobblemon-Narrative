# Pokémon training, practice and coaching layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs persistent Trainer-Pokémon practice without turning narrative repetition into free PTU progression.

This layer owns the world-state history of practical training sessions:

- why the session happened;
- who participated;
- what was being practiced;
- which setup or cue was used;
- what each participant attempted;
- what was observed;
- what feedback was offered;
- what changed in the next attempt;
- whether the behavior generalized to another context;
- whether a real PTU mechanical transaction occurred.

It does not own levels, Tutor Points, Move legality, Poke Edges, Skills, Capabilities, stats, Loyalty, Features, Abilities, action economy or battle outcomes.

Those remain governed by PTU/Caelo and AutoPTU.

## Core separation

Keep these concepts separate:

1. training objective;
2. practice setup;
3. cue or instruction;
4. attempted behavior;
5. observed result;
6. participant response;
7. coach interpretation;
8. next-session adjustment;
9. transfer/generalization evidence;
10. authoritative mechanical change.

A Pokémon can perform a drill successfully while gaining no mechanical benefit.

A Pokémon can gain a legal Poke Edge through an authoritative progression transaction even if the narrative session was ordinary.

A Trainer can believe that a drill caused the improvement while the engine records the actual PTU cause separately.

## Relationship to existing layers

### Social Bonds / Mentorship

Owns the mentor relationship, trust/respect history and Trainer-to-Trainer learning relationship.

This layer owns the actual practice session.

A mentor can design a drill without becoming the Pokémon's owner or commander.

### Education

Owns curriculum, enrollment, formal instruction, practicum and institutional assessment.

This layer may be referenced by an education `practice_record` when the practicum involves Pokémon training.

### Pokémon Agency

Owns identity, custody, partnership, observed cooperation/refusal and agency.

Training never creates ownership, obedience or consent.

### Care / Welfare

Owns welfare observations, health state, diagnosis and recovery.

A training session may stop because Care state says continuing is inappropriate.

The training layer must never diagnose injury, fear or exhaustion by itself.

### Battle Institutions

Owns official challenge contracts, results, rankings and rematches.

A formal loss may create a practice objective, but the practice session is not itself an official rematch.

### Social Learning

Owns evidence that behavior transmitted between Pokémon.

A Pokémon copying another during one drill is only an observed event until transmission evidence is sufficient.

### Cognition / Tool Use

Owns individual problem solving and object manipulation.

Training can present a task; cognition owns the interpretation of problem-solving behavior.

### Working Pokémon

Owns institutional assignments and role performance.

Practice for a workplace role can be logged here, while the assignment remains owned by Working Pokémon.

## Primary objects

### TRAINING_PROGRAM

Optional persistent wrapper for a multi-session objective.

```yaml
training_program:
  training_program_id: null
  status: PROPOSED
  trainer_actor_ids: []
  pokemon_entity_ids: []
  coach_actor_ids: []
  objective_ids: []
  origin_refs: []
  started_at: null
  ended_at: null
  current_phase: null
  authoritative_mechanics_refs: []
  welfare_review_refs: []
  provenance_refs: []
```

A program is not required for casual practice.

### TRAINING_OBJECTIVE

Represents the narrow problem being worked on.

```yaml
training_objective:
  training_objective_id: null
  subject_ids: []
  objective_type: null
  target_description: null
  origin_evidence_refs: []
  success_criteria_description: null
  mechanics_target_refs: []
  current_assessment: OPEN
  created_at: null
  retired_at: null
```

Possible narrative objective types:

- COORDINATION
- TIMING
- POSITIONING
- CUE_RESPONSE
- MOVEMENT_PATTERN
- TARGET_SELECTION
- MOVE_EXECUTION_PRACTICE
- ENVIRONMENT_FAMILIARIZATION
- CARE_COOPERATION
- WORK_TASK_PRACTICE
- PERFORMANCE_REHEARSAL
- RECOVERY_RETURN_TO_PRACTICE
- REMATCH_PREPARATION
- UNKNOWN_OR_EXPLORATORY

These categories do not grant mechanics.

### TRAINING_SESSION

```yaml
training_session:
  training_session_id: null
  training_program_id: null
  location_id: null
  start_time: null
  end_time: null
  participant_actor_ids: []
  pokemon_entity_ids: []
  coach_actor_ids: []
  objective_ids: []
  setup_revision_id: null
  planned_attempt_ids: []
  actual_attempt_ids: []
  authoritative_battle_ref: null
  care_state_refs: []
  participation_events: []
  outcome_summary: null
  mechanics_transaction_refs: []
  privacy_scope: null
  provenance_refs: []
```

A session may contain no battle.

### TRAINING_SETUP_REVISION

Represents the physical or procedural setup.

```yaml
training_setup_revision:
  setup_revision_id: null
  location_id: null
  setup_kind: SPARRING | TARGET_DRILL | OBSTACLE | SIMULATION | CARE_STATION | WORK_STATION | ROUTE | WATER | AIR | OTHER
  equipment_item_ids: []
  simulated_problem_refs: []
  environment_refs: []
  fidelity_claims: []
  safety_constraints: []
  created_at: null
  supersedes_id: null
```

A simulated hazard remains a simulation unless the battle engine actually instantiates that mechanic.

A web-like target prop is not Sticky Web.

A water pool is not automatically Water Terrain.

A moving dummy is not a combatant.

### PRACTICE_ATTEMPT

```yaml
practice_attempt:
  attempt_id: null
  session_id: null
  subject_id: null
  objective_id: null
  cue_ref: null
  setup_revision_id: null
  start_time: null
  observed_actions: []
  observed_result: null
  result_band: NOT_ATTEMPTED | PARTIAL | COMPLETED | INTERRUPTED | DISENGAGED | INVALID_SETUP
  authoritative_action_refs: []
  observer_ids: []
  notes: []
```

`COMPLETED` means the described practice criterion was observed.

It does not mean permanent mastery.

### TRAINING_CUE

A cue is a persistent communication convention when the players/authors choose to make it significant.

```yaml
training_cue:
  cue_id: null
  trainer_actor_id: null
  pokemon_entity_id: null
  modality: VERBAL | GESTURE | WHISTLE | LIGHT | TOUCH | OBJECT | POSITIONAL | OTHER
  description: null
  introduced_at: null
  observation_refs: []
  current_use_state: ACTIVE | OCCASIONAL | RETIRED | UNCERTAIN
  privacy_scope: null
```

Hard guardrails:

- a cue is not a PTU Command action by default;
- knowing a cue does not grant battle control;
- a new custodian does not automatically know the cue;
- a Pokémon responding once does not prove universal reliability;
- cue records should remain optional to avoid excessive microstate.

### TRAINING_FEEDBACK

```yaml
training_feedback:
  feedback_id: null
  session_id: null
  coach_actor_id: null
  subject_scope_ids: []
  observation_refs: []
  interpretation: null
  recommended_change: null
  confidence: null
  accepted_by_refs: []
```

Feedback is a claim.

Two competent coaches can disagree.

### TRAINING_ADJUSTMENT

```yaml
training_adjustment:
  adjustment_id: null
  objective_id: null
  prior_attempt_refs: []
  change_type: SETUP | CUE | PACE | PARTNER | DISTANCE | COMPLEXITY | ENVIRONMENT | REST_INTERVAL | OTHER
  description: null
  applied_from: null
  outcome_refs: []
```

Narrative adjustments never modify AC, DB, stats, movement or capabilities directly.

### TRANSFER_OBSERVATION

Records whether a practiced behavior appears under different conditions.

```yaml
transfer_observation:
  transfer_observation_id: null
  pokemon_entity_id: null
  training_objective_id: null
  source_setup_ref: null
  new_context_ref: null
  behavior_observed: null
  similarity_band: HIGH | MEDIUM | LOW | UNKNOWN
  observer_ids: []
  authoritative_action_refs: []
  interpretation_state: OPEN
```

This supports long-term callbacks without manufacturing a `mastery` stat.

## Training lifecycle

A useful default lifecycle is:

OBSERVED_PROBLEM
→ OBJECTIVE_CREATED
→ SETUP_SELECTED
→ ATTEMPT
→ OBSERVATION
→ FEEDBACK
→ ADJUSTMENT
→ REPEAT_OR_STOP
→ FIELD_TRANSFER
→ REVIEW

Not every session uses every phase.

Routine maintenance practice should compress.

## Origin of a training objective

Objectives should come from actual world state.

Valid sources include:

- previous battle transcript;
- coach observation;
- Trainer request;
- work-role requirement;
- care/cooperative-care requirement;
- route or environment problem;
- upcoming challenge;
- new Move or Poke Edge already gained mechanically;
- change after Evolution;
- new equipment;
- failure to generalize a prior routine;
- player-authored personal goal.

The generator must not create a weakness solely because it wants a training quest.

## Battle transcript -> training objective

A formal battle can create a bounded review.

Example:

```yaml
origin_evidence:
  type: BATTLE_TRANSCRIPT
  battle_id: battle_1042
  observation: repeated_failed_positioning_before_area_attacks
```

A coach may then propose:

```yaml
objective:
  type: POSITIONING
  target_description: practice leaving clustered formation before predictable area pressure
```

The training layer must not conclude that the Pokémon lacks Intelligence, Loyalty or courage.

## Mechanical progression gate

PTU has explicit mechanisms for Pokémon progression.

Project data currently includes examples such as:

- Accuracy Training;
- Capability Training;
- Advanced Mobility;
- Skill Improvement;
- Underdog's Lessons;
- Expand Horizons;
- other Mentor/Tutor/Poke Edge effects.

Therefore:

```text
practice session
!=
mechanical progression
```

If a legal rules transaction occurs:

```yaml
mechanics_transaction_ref:
  authority: AUTOPTU_OR_RULES_SERVICE
  transaction_type: POKE_EDGE | TUTOR | MOVE_LEARN | LEVEL | FEATURE_EFFECT | OTHER
  source_rule_ref: null
  before_state_ref: null
  after_state_ref: null
```

The narrative layer may describe the event around that change.

It may not produce the change itself.

## Move practice

A session may target a Move only if the wording preserves mechanical truth.

Allowed narrative states:

- preparing to learn if governing rules permit it;
- practicing a Move already known;
- practicing timing/aim/positioning around a known Move;
- rehearsing a combination concept;
- observing a legal Tutor transaction;
- testing whether a newly learned Move fits a strategy.

Forbidden automatic writes:

- add Move;
- remove Move;
- lower AC;
- increase DB;
- expand Range;
- change Frequency;
- add Keywords;
- bypass Move Slot limits;
- invent Combo mechanics.

## Cue response and autonomy

A Pokémon may respond to a cue during practice.

This does not establish permanent obedience.

Store observations such as:

- responded immediately;
- responded after repetition;
- performed different behavior;
- disengaged;
- remained near Trainer but did not perform task;
- initiated target behavior before cue;
- followed another Pokémon instead;
- left session area.

Avoid hidden `obedience_score` or `training_score` unless later rules explicitly require one.

## Voluntary participation

Participation should be recordable without anthropomorphizing every action.

Possible observations:

- approached setup after cue;
- entered station without physical guidance;
- remained for three attempts;
- moved away;
- returned after pause;
- accepted equipment fitting;
- refused to enter container;
- completed one step but not another.

Interpretation belongs to Pokémon Agency/Care when required.

Do not convert refusal into Loyalty loss.

## Session stop conditions

A session may stop because:

- objective completed for the day;
- Trainer chooses to stop;
- Pokémon disengages;
- scheduled facility time ends;
- weather/route state changes;
- coach changes plan;
- Care state requires stop;
- equipment fails;
- location becomes unavailable;
- an unrelated event interrupts;
- authoritative battle state makes continuation inappropriate.

Stopping is a normal outcome.

## Intensity is not progression

Do not model a universal `training_intensity` scalar that grants more progression.

A long or harsh session is not automatically better.

A short session can be valuable.

A failed session can reveal a bad setup.

An easy session can preserve a routine.

A no-progress session can still create relationship or historical continuity.

## Rest and readiness boundary

This layer does not create fatigue, stamina depletion, HP loss or Injury from narrative practice.

If the training uses a real AutoPTU battle, authoritative battle state applies normally.

If the session is descriptive or uses non-mechanical props, no combat resource changes are invented.

Care owns recovery interpretation.

## Training after Evolution

Evolution can create an authored reason to revisit old practice:

- different body dimensions;
- different movement capabilities;
- different Move list;
- new Ability;
- changed equipment fit;
- different visual communication.

The system must read the actual post-Evolution mechanics.

It must not assume that Evolution erases prior cues, memories, partnership or routines.

## Multiple Trainers / multiplayer

Several players may contribute to one session.

Track roles such as:

- primary Trainer;
- coach;
- sparring partner;
- observer;
- equipment operator;
- safety support.

A coach helping with practice gains no custody or command authority.

A second player cannot rewrite another player's Pokémon relationship state.

## Training facilities

Facilities may include:

- Gym practice room;
- Battle Club;
- academy yard;
- pool;
- climbing hall;
- flying field;
- rescue drill site;
- care station;
- workshop practice bay;
- public field;
- private yard;
- temporary camp.

Facility state may include:

- booking;
- equipment availability;
- safety restrictions;
- staff support;
- maintenance;
- access permissions;
- current configuration.

No facility grants mechanics merely because of its label.

## Equipment and simulation fidelity

A training prop should carry its own identity when persistent.

Examples:

- target board;
- moving dummy;
- practice gate;
- mock web launcher;
- shallow pool;
- balance platform;
- marked lane;
- protective barrier;
- care station marker.

The system should record what the prop is intended to simulate.

It must never silently convert the prop into the PTU mechanic being imitated.

## Practice partners

A partner may be:

- another owned Pokémon;
- a willing wild persistent Pokémon when the scenario supports it;
- coach Pokémon;
- NPC Trainer Pokémon;
- controlled dummy/prop;
- the environment.

Participation does not transfer ownership.

A wild Pokémon helping once does not become a permanent training service.

## Sparring

Three modes should remain distinct:

### Mechanical spar

A real AutoPTU battle with authoritative HP, actions, Moves and results.

### Reduced mechanical drill

A conventional battle used to represent a larger exercise while non-combat training objectives remain world state.

### Narrative rehearsal

No combat mechanics are invoked. Observations are descriptive only.

The mode must be explicit so nobody assumes a narrative drill changed HP or progression.

## Training combinations

Ouros may remember that two Pokémon practiced a sequence.

Example:

```yaml
sequence_claim:
  participants: [pokemon_a, pokemon_b]
  sequence_description: one creates opening, second follows
  observed_in_practice: true
  observed_in_battle: false
```

This does not create:

- combo damage;
- shared initiative;
- simultaneous actions;
- linked Accuracy;
- automatic follow-up;
- Pack Mon;
- reaction entitlement.

A future mechanics system must define any such effect explicitly.

## Coaching styles

NPC coaches may have authored philosophies.

Examples:

- repetition-heavy;
- scenario-based;
- observation-first;
- battle-review focused;
- playful exploration;
- environmental adaptation;
- cooperative-care focused;
- self-directed problem solving.

These are narrative identity.

No coaching style grants a multiplier.

## Practice culture and regional history

Training culture can become durable worldbuilding.

Examples:

- a Gym keeps old practice apparatus from previous Leaders;
- a port city uses balance and footing drills because decks are common workplaces;
- a mountain academy emphasizes route judgment before battle technique;
- a rescue organization has standardized handoff drills;
- a town preserves a traditional practice field that predates the League;
- an old coach's methods remain in notebooks even after being revised.

Culture can persist while mechanical rules remain universal.

## Training records and privacy

Suggested visibility bands:

- PRIVATE_PAIR;
- COACH_SHARED;
- TEAM_SHARED;
- INSTITUTIONAL;
- PUBLIC_DEMONSTRATION;
- COMPETITIVE_PUBLIC.

A private drill should not automatically become opponent knowledge.

An official public battle can become legal observation through Battle Institutions.

## Knowledge boundaries

A rival should only know a training detail if it was:

- observed directly;
- shared by a participant;
- published;
- demonstrated publicly;
- inferable from a later public battle;
- available through a legitimate institutional record.

AI tactical policy must not read private practice state as omniscient battle knowledge.

## Routine training compression

Routine sessions should often compress into a short Chronicle event.

Example:

`Morning practice at East Gym. Same positioning drill. No new issue observed. Session ended normally.`

Do not manufacture a crisis or progression every time.

Detailed play becomes valuable when:

- the objective changes;
- a new behavior appears;
- a participant refuses/disengages;
- a coach identifies competing explanations;
- equipment/facility state matters;
- an authoritative progression event occurs;
- a recurring rival/mentor observes the session;
- a world event interrupts;
- field transfer is tested.

## Long-term training history

A `training_program_id` may persist for months or years.

The system should preserve revision history.

An objective can move through states such as:

- OPEN;
- ACTIVE;
- PAUSED;
- REFRAMED;
- TRANSFER_TESTING;
- ROUTINE_MAINTENANCE;
- RETIRED;
- UNRESOLVED.

Do not force `MASTERED` as a universal terminal state.

## Failure-forward training

Failure should often create information rather than a stat penalty.

A session may reveal:

- setup too difficult;
- cue ambiguous;
- coach hypothesis unsupported;
- body plan mismatch;
- environment too different;
- participant uninterested;
- timing problem;
- partner mismatch;
- the supposed weakness was not reproducible.

That information can change future plans.

## Encounter contract — Rematch Preparation Circuit

### Premise

After a formal loss, a coach converts two observed problems into a small practice circuit before the player decides whether to request a rematch.

### FULL version

The exercise contains moving sparring partners, area-pressure simulations and objective markers. Pokémon must reposition, protect lanes, withdraw from threatened areas and execute practice goals while the coach adjusts the setup between rounds.

### Dependencies

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if moving pressure, interception or forced repositioning is required;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL when actual sparring damage is used;
- status lifecycle — PARTIAL if exact statuses are used;
- terrain/weather/hazards/zones/reactions — BLOCKING as a complete family if the circuit uses real tactical zones/hazards/reaction drills;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for TRAIN_OBJECTIVE / PROTECT_LANE / WITHDRAW / RETEST behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

### REDUCED version

Keep drill criteria, props and coach feedback in world state. Run one conventional static spar using only legal AutoPTU choices. After the battle, compare the transcript to the objective and record observations. No custom hazard or combo mechanics.

## Encounter contract — Pair Coordination Drill

### Premise

Two Pokémon that will participate in an upcoming Doubles event practice spacing and role handoffs.

### FULL version

The coach changes objective markers and opposing pressure. The pair must reposition without clustering, alternate protected routes and respond to different threat shapes.

### Dependencies

FULL requires BLOCKING tactical AI for role/objective-aware decisions and may require BLOCKING complete movement/environmental family if live zones, interception or forced movement are present. Move/Ability/Item/Feature specifics remain PARTIAL by exact mechanic.

### REDUCED version

Use a legal static Multi Battle. Record spacing, target choices and repeated patterns from the authoritative transcript. Any conclusion about coordination remains narrative evidence. No combo bonus is created.

## Encounter contract — Cooperative Care Practice

### Premise

A persistent Pokémon is being familiarized with a routine care procedure or transport setup.

### FULL version

The Pokémon may approach, pause, leave, return and interact with stations while staff react without turning the session into combat.

### Dependencies

This is primarily a world-state scenario. A future rich simulation would need AI tactical policy and adapter/playback for voluntary non-combat objectives. It does not require damage/status mechanics unless an independent incident creates a battle.

### REDUCED version

Resolve each step as observations in world state. If the Pokémon disengages, stop. No battle is opened merely because a training criterion was not completed.

## Encounter contract — Environmental Familiarization

### Premise

A Trainer prepares a Pokémon for a known route condition such as shallow water, darkness, a narrow platform or unusual footing.

### FULL version

Only use the actual environmental mechanic when PTU/Caelo and AutoPTU verify it.

### REDUCED version

Represent the environment visually and narratively, use base movement legality where already verified, and keep unsupported penalties/effects outside combat. The practice history can still matter as Chronicle evidence without granting a bonus.

## Engine boundary

Training is an overworld/narrative system.

AutoPTU-Java should receive only authoritative battle state and legal character mechanics.

Minecraft/Cobblemon/Craftics should receive renderable practice objects and event playback.

Neither layer should calculate free progression from repetition counts.

## New overworld blockers

- `TRAINING_PROGRAM_STATE`
- `TRAINING_OBJECTIVE_HISTORY`
- `TRAINING_SESSION_LEDGER`
- `TRAINING_SETUP_REVISIONS`
- `PRACTICE_ATTEMPT_OBSERVATIONS`
- `TRAINING_CUE_HISTORY`
- `COACH_FEEDBACK_PROVENANCE`
- `TRAINING_ADJUSTMENT_HISTORY`
- `TRANSFER_GENERALIZATION_OBSERVATIONS`
- `TRAINING_TO_PTU_MECHANICS_TRANSACTION_HANDOFF`
- `TRAINING_TO_CARE_WELFARE_HANDOFF`
- `TRAINING_TO_BATTLE_TRANSCRIPT_REVIEW`
- `TRAINING_TO_MINECRAFT_PLAYBACK`

These belong to persistent world state, not the battle rules engine.

## Hard non-inferences

Do not infer:

- repetitions -> XP;
- hours -> level;
- drills -> Tutor Points;
- sparring -> Poke Edge;
- coach present -> Mentor Feature;
- target practice -> Accuracy Training;
- obstacle practice -> Capability Training;
- route running -> Advanced Mobility;
- studying a Move -> learning the Move;
- successful attempt -> mastery;
- failed attempt -> Loyalty loss;
- refusal -> disobedience;
- harsh session -> better progression;
- training facility -> stat multiplier;
- equipment -> Item effect;
- simulated hazard -> PTU hazard;
- practiced combo -> simultaneous action;
- repeated cue response -> permanent obedience;
- training partner -> ownership;
- private practice record -> opponent knowledge.

## Canon questions still open

- What training institutions exist in Ouros before the players arrive?
- Does the League regulate or certify any practice facilities?
- Which coaching traditions are regionally authored?
- How much private training history is stored in multiplayer?
- Can players create reusable training facilities or drills?
- Which cues/routines deserve persistent identity versus short session notes?
- How does a Pokémon's training history follow it through transfer, release or retirement while preserving privacy and agency?
- Which Caelo rules alter Mentor, tutoring, Poke Edges, training times or progression?
- Does Caelo authorize any mechanical benefit specifically from downtime practice?

Until those questions are answered, this layer remains world-state architecture only.