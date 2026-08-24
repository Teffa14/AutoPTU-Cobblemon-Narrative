# Pokémon play, enrichment and exploratory behavior layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs a persistent layer for voluntary recreation and enrichment that does not collapse into training, welfare diagnosis, social-bond scoring or mechanical progression.

Care already recognizes enrichment as a welfare concern. This layer supplies the behavior and opportunity history that Care can reference.

It owns:

- observed play episodes;
- recreational and exploratory opportunity sets;
- observed approaches, interaction, pauses and disengagement;
- persistent recreational-object use;
- play-partner episodes;
- changes in preferences or participation over time;
- uncertainty when rough interaction may be play, conflict or both;
- transitions from free play into training, care, feeding or other systems.

It does not own:

- mechanical HP, Injuries, Status or healing;
- diagnosis or welfare conclusions;
- Loyalty/Friendship;
- ownership/custody/partnership;
- XP, Levels, Tutor Points or Poke Edges;
- training progression;
- social-learning conclusions;
- tool-use conclusions;
- species-wide behavioral rules;
- tactical AI.

## Core separation

Keep these distinct:

1. opportunity existed;
2. Pokémon could physically access it;
3. Pokémon approached it;
4. interaction occurred;
5. observer classified the interaction as possible play;
6. play continued, paused or ended;
7. another participant joined or left;
8. the activity later changed function;
9. Care or Science interpreted the observation;
10. authoritative PTU mechanical state.

A ball lying in a yard does not prove enrichment occurred.

A Pokémon ignoring it during one observation window does not prove dislike.

A Pokémon repeatedly playing with it does not gain a mechanical bonus.

## Relationship to existing layers

### Care / Welfare

Care owns welfare interpretation, health observations, diagnosis and treatment.

This layer can provide records such as:

`used_three_of_four_available_options`

or:

`no_play_observed_during_two_hour_window`

Care decides whether those observations matter alongside appetite, rest, health, environment and other evidence.

No play metric is a diagnosis.

### Pokémon Agency

Pokémon Agency owns persistent identity, partnership, custody and observed cooperation/refusal.

This layer records observable choices without inventing internal motive.

A Pokémon may disengage from play at any time.

Disengagement never creates a Loyalty loss or disobedience state.

### Training / Practice

Training owns goal-directed practice.

The same object can be used in both systems.

Free activity:

`pokemon chases bouncing ball without required criterion`

Training activity:

`trainer asks pokemon to stop at marked line after ball release and records success criterion`

When the purpose changes, create a training reference. Do not rewrite the earlier episode.

### Social Learning

Social Learning owns claims that behavior transmitted between individuals.

One Pokémon joining another's activity is only co-participation until evidence supports transmission.

### Cognition / Tool Use

Cognition owns problem-solving and tool-use assessment.

Object play is not automatically tool use.

### Material Culture

Material Culture owns persistent toys, ropes, balls, structures or other physical items.

This layer owns interaction history with those objects.

### Breeding / Juvenile Care

Breeding/Nursery owns Eggs, juveniles, custody and developmental-care state.

This layer can record juvenile play without defining developmental milestones.

### Diel / Seasonality / Environment

Other layers own day/night, weather, snow, water, vegetation or other physical opportunities.

This layer records how Pokémon interacted with those conditions.

Snow does not become a play mechanic simply because a Pokémon was observed sliding on it.

## Primary objects

### PLAY_EPISODE

```yaml
play_episode:
  play_episode_id: null
  status: OBSERVED
  started_at: null
  ended_at: null
  location_id: null
  pokemon_entity_ids: []
  wild_collective_refs: []
  nearby_nonparticipant_ids: []
  human_actor_ids: []
  opportunity_set_id: null
  play_domain_tags: []
  object_refs: []
  environment_refs: []
  observation_ids: []
  recording_refs: []
  classification_confidence: null
  transition_state: null
  provenance_refs: []
```

Candidate play domains:

- LOCOMOTOR
- OBJECT
- SOCIAL
- ROUGH_AND_TUMBLE
- CHASE
- ENVIRONMENTAL_EXPLORATION
- WATER_OR_SNOW_RECREATION
- SELF_DIRECTED
- MIXED
- UNCERTAIN

These are descriptive classifications, never mechanical tags.

### ENRICHMENT_OPPORTUNITY_SET

Represents what was available during a bounded time/context.

```yaml
enrichment_opportunity_set:
  opportunity_set_id: null
  location_id: null
  valid_from: null
  valid_until: null
  target_scope_refs: []
  option_ids: []
  access_constraints: []
  care_review_refs: []
  safety_review_refs: []
  environmental_context_refs: []
  provenance_refs: []
```

An opportunity set records choice architecture.

It does not require interaction.

### ENRICHMENT_OPTION

```yaml
enrichment_option:
  option_id: null
  option_type: OBJECT | SPACE | SURFACE | WATER | SHELTER | FORAGING_OPPORTUNITY | SOCIAL_ACCESS | OTHER
  physical_ref: null
  description: null
  available_state: AVAILABLE
  introduced_at: null
  removed_at: null
  removal_reason: null
  mechanics_refs: []
```

Possible availability states:

- AVAILABLE
- TEMPORARILY_UNAVAILABLE
- REMOVED_FOR_SAFETY
- UNDER_REPAIR
- RETIRED
- UNKNOWN

`mechanics_refs` remains empty unless a real PTU object/effect exists.

### OPTION_INTERACTION_OBSERVATION

```yaml
option_interaction_observation:
  observation_id: null
  pokemon_entity_id: null
  opportunity_set_id: null
  option_id: null
  observed_at: null
  state: APPROACHED | INTERACTED | PAUSED | DISENGAGED | REAPPROACHED | NO_INTERACTION_OBSERVED
  interaction_description: null
  duration_band: null
  nearby_actor_refs: []
  confounder_refs: []
  recording_refs: []
  confidence: null
```

Hard rule:

`NO_INTERACTION_OBSERVED` does not mean refusal or dislike.

### PLAY_INVITATION_OBSERVATION

Stores a visible interaction without claiming internal intent.

```yaml
play_invitation_observation:
  observation_id: null
  initiator_id: null
  recipient_ids: []
  observed_signal_description: null
  prior_pattern_ref: null
  recipient_response: APPROACHED | JOINED | REMAINED | MOVED_AWAY | INTERRUPTED | UNKNOWN
  observer_interpretation: null
  confidence: null
```

The label `invitation` can remain provisional when the signal has not been behaviorally validated for that species/individual.

### PLAY_PARTNER_EPISODE

```yaml
play_partner_episode:
  play_partner_episode_id: null
  play_episode_id: null
  participant_ids: []
  participant_species_refs: []
  previous_contact_refs: []
  role_change_observations: []
  voluntary_reengagement_observations: []
  withdrawal_observations: []
  conflict_transition_refs: []
  classification: SOCIAL_PLAY_POSSIBLE
  confidence: null
```

This never creates friendship, pair bond, kinship, faction membership or interspecies mutualism.

### PLAY_CLASSIFICATION_ASSESSMENT

Used when observers need to distinguish possible play from another interaction.

```yaml
play_classification_assessment:
  assessment_id: null
  episode_id: null
  evidence_refs: []
  candidate_states:
    PLAY_LIKELY: null
    CONFLICT_LIKELY: null
    MIXED_OR_TRANSITIONAL: null
    FUNCTIONAL_BEHAVIOR_LIKELY: null
    UNRESOLVED: null
  assessor_ids: []
  method_refs: []
  current_conclusion: UNRESOLVED
  reviewed_at: null
```

Different researchers or caretakers may disagree.

The disagreement persists as provenance.

## Recreational object history

A toy can acquire a durable story.

Example:

`BALL_017`

Year 1: introduced in nursery yard.

Year 2: repaired after seam failure.

Year 3: one persistent Pokémon repeatedly selects it while others ignore it.

Year 5: moved to a community care facility.

Year 8: retired from use and retained as an archive object because of documented local history.

The object never grants a PTU Item effect unless its authoritative mechanical definition says so.

## Preference state

Do not store a permanent scalar such as:

`likes_ball = 83`

Instead derive provisional preference observations from bounded contexts.

```yaml
preference_observation:
  preference_observation_id: null
  pokemon_entity_id: null
  compared_option_ids: []
  context_ref: null
  observation_window: null
  selected_option_ids: []
  unselected_option_ids: []
  repeated_choice_refs: []
  interpretation: null
  confidence: null
  expires_or_review_after: null
```

Preference can change by life stage, season, health, social context, environment or prior experience.

## Play transitions

A scene can change function.

Supported transition labels:

- PLAY_TO_TRAINING
- PLAY_TO_FEEDING
- PLAY_TO_CONFLICT
- PLAY_TO_REST
- PLAY_TO_CARE
- PLAY_TO_EXPLORATION
- PLAY_TO_TOOL_USE_INVESTIGATION
- PLAY_TO_SOCIAL_LEARNING_INVESTIGATION
- ENDED_WITHOUT_TRANSITION

The transition links to the receiving layer.

It does not retroactively redefine the earlier activity.

## Rough-and-tumble and conflict

Do not build a universal aggression classifier.

Store observable evidence.

Examples:

- repeated approach after pause;
- alternation of chasing roles;
- one participant moving away and remaining away;
- escalation to an authoritative battle action;
- Injury or mechanical damage only if actually produced through legal mechanics;
- calls/signals only when observed;
- intervention by a caregiver.

A battle beginning after play does not prove the earlier activity was secretly hostile.

## Wild Pokémon play

Wild individuals and collectives can have play episodes without becoming owned, tame or capturable.

Examples:

- juveniles chasing floating leaves;
- several individuals repeatedly using a slope;
- object manipulation near a riverbank;
- mixed-species play during a temporary seasonal aggregation.

Loaded Cobblemon count is not population truth.

A player placing toys in a biome must not directly increase spawn quantity or rare-spawn probability.

Any persistent ecological effect requires evidence and the appropriate ecology layer.

## Institutional enrichment

Facilities may maintain enrichment programs.

Possible sites:

- nursery;
- sanctuary;
- clinic recovery yard;
- research facility;
- working-Pokémon rest area;
- lodging property that accommodates Pokémon;
- club/community space.

Suggested state:

```yaml
enrichment_program:
  program_id: null
  facility_id: null
  scope_refs: []
  opportunity_set_ids: []
  rotation_history: []
  care_review_refs: []
  participant_observation_refs: []
  maintenance_refs: []
  status: ACTIVE
```

An enrichment program is not a training program.

If the institution begins using performance objectives, the relevant sessions move into Training.

## Choice and control guardrail

Where feasible, provide multiple options and preserve the ability to disengage.

Do not generate a compulsory “play session” because the calendar says welfare is due.

A facility can record that an opportunity was available even if the Pokémon did not use it.

This allows Care to reason from real history without turning recreation into a chore for the player.

## Routine compression

Routine successful recreation should compress.

Detailed scenes become visible when:

- a Pokémon selects a new option;
- a previously used option stops being used;
- a new participant joins;
- an individual disengages unexpectedly in combination with other relevant observations;
- an object breaks or moves;
- activity intersects training, cognition, social learning, care or ecology;
- a seasonal environment opens/closes a play opportunity;
- a player explicitly chooses to spend time observing or participating.

Otherwise Chronicle can write a compact observation summary.

## Minecraft projection

Minecraft may render:

- balls and toys;
- climbing or resting structures;
- water/snow/sand surfaces;
- open yards;
- shade/shelter;
- Pokémon moving between options;
- maintenance state.

Minecraft is presentation, not authority.

Do not infer:

- item use from proximity alone;
- preference from pathfinding alone;
- play from random entity movement alone;
- friendship from co-location;
- welfare from animation frequency;
- mechanical Item effects from rendered props;
- training success from animation;
- social learning from mimic-like animation;
- spawn modification from placed enrichment.

## PTU mechanical boundary

Ordinary play/enrichment never directly writes:

- XP;
- Levels;
- Tutor Points;
- Poke Edges;
- Moves;
- stats or Combat Stages;
- HP or temporary HP;
- Injuries;
- Status;
- Loyalty/Friendship;
- Skills;
- Features;
- Abilities;
- Contest Stats;
- battle action resources.

If an external game gives benefits for recreation, that game-specific reward is inspiration only.

Any Ouros mechanical change requires a governing PTU/Caelo rule and an authoritative AutoPTU transaction.

## Encounter contract: Nursery Yard Escalation

Narrative premise:

A mixed group is using a yard. Rough interaction becomes difficult for staff to classify, and an unrelated external threat or genuine escalation may create a combat situation.

FULL version requires:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING when participants withdraw/re-enter dynamically;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full lifecycle: PARTIAL;
- stateful damage: PARTIAL if combat begins;
- status lifecycle: PARTIAL when exact status effects appear;
- terrain/weather/hazards/zones/reactions: BLOCKING as a complete family if protected play zones or reactions matter tactically;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL if real mechanical items are used;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW / REENGAGE / PROTECT / DEESCALATE objectives;
- adapter/playback: BLOCKING.

REDUCED version:

Staff end the recreation period and move noncombatants away through world state. If an independent combat remains, AutoPTU receives a static legal arena and only the actual combatants. The classification of the earlier episode remains unresolved or separately assessed.

## Encounter contract: Riverside Object Play Spillover

Narrative premise:

Wild Pokémon repeatedly use floating or rolling objects near a route. Their movement occasionally crosses human traffic and becomes a route-management problem.

FULL version depends primarily on BLOCKING complete movement, BLOCKING AI tactical policy and BLOCKING adapter/playback for non-hostile movement goals.

If changing water/current becomes tactical, it additionally depends on BLOCKING terrain/weather/hazards/zones/reactions as a complete family.

REDUCED version:

Resolve the play episode and route crossing in overworld state. Pause traffic or redirect actors. If another confrontation occurs, freeze one shoreline state and run a conventional static battle. No current, toy or play bonus enters AutoPTU.

## Encounter contract: Enrichment Yard Equipment Failure

Narrative premise:

A persistent recreational structure fails while Pokémon are present. The important outcome is evacuation, inspection, repair and whether individuals later choose to use the revised setup.

FULL version requires BLOCKING complete movement for dynamic evacuation, BLOCKING tactical AI for WITHDRAW/REACH_EXIT and BLOCKING adapter/playback. Environmental mechanics enter only if a validated tactical hazard exists.

REDUCED version:

Close the yard and evacuate through world state. Freeze any subsequent battle away from the damaged structure. Architecture/Material Culture handles repair. This layer later records reintroduction and choice observations.

## Non-combat contract: Choice Trial

Provide several safe enrichment options and observe voluntary interaction over a bounded window.

No battle required.

No hidden success threshold.

Useful output:

- options available;
- options approached/used;
- order of interaction;
- disengagement/re-engagement;
- context;
- observation uncertainty.

This is an ideal recurring activity to compress after the first few meaningful sessions.

## New overworld blockers

- `PLAY_EPISODE_HISTORY`
- `ENRICHMENT_OPPORTUNITY_SETS`
- `ENRICHMENT_OPTION_STATE`
- `OPTION_INTERACTION_OBSERVATIONS`
- `PLAY_PARTNER_EPISODES`
- `PLAY_CLASSIFICATION_ASSESSMENTS`
- `PREFERENCE_OBSERVATION_HISTORY`
- `RECREATIONAL_OBJECT_USAGE_HISTORY`
- `PLAY_TO_TRAINING_HANDOFF`
- `PLAY_TO_CARE_HANDOFF`
- `PLAY_TO_COGNITION_HANDOFF`
- `PLAY_TO_SOCIAL_LEARNING_HANDOFF`
- `PLAY_TO_MATERIAL_CULTURE_HANDOFF`
- `PLAY_TO_MINECRAFT_PLAYBACK`

These belong to persistent world-state services rather than the AutoPTU battle core.

## Canon questions left open

- Which Ouros institutions provide structured enrichment?
- Which populations/species have authored play behavior at campaign start?
- How much individual preference state should be discoverable by players?
- How should facilities handle enrichment for very large, aquatic, flying, burrowing or otherwise specialized Pokémon?
- How long should an unobserved preference remain usable as evidence?
- Can player-created facilities design enrichment programs?
- Which play observations are private care data versus public research observations?
- Which Caelo rules, if any, modify rest, play, Loyalty, training or welfare?

Until those questions are answered, this layer remains descriptive and observational.
