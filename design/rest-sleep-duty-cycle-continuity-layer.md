# Rest, Sleep & Duty-Cycle Continuity Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Pass: 196

## Purpose

This layer gives Ouros persistent state for ordinary rest, sleep, planned waiting, interrupted downtime, wake events and responsibility handoffs across day boundaries.

It exists so schedules and expeditions can behave like a lived world without turning beds into universal heal buttons or adding an unsupported fatigue simulator.

PTU/AutoPTU remains authoritative for every mechanical consequence of Rest and Extended Rest.

## 1. Three clocks must remain separate

Ouros can track three related but different facts:

```yaml
world_time:
  current_world_timestamp: null

narrative_rest_interval:
  interval_id: null
  actor_id: null
  location_id: null
  planned_start: null
  actual_start: null
  planned_end: null
  actual_end: null
  observed_activity_refs: []
  interruption_event_ids: []
  resumed_from_interval_id: null
  rest_claim_state: RECORDED
  mechanics_adjudication_ref: null

mechanical_rest_resolution:
  resolution_ref: null
  authority: AutoPTU
  input_interval_refs: []
  result_state: UNRESOLVED
```

Narrative can author the first two. It may store the third only as an external authoritative result.

A world-time jump does not itself create a valid rest interval. A valid narrative interval does not itself authorize PTU recovery.

## 2. Rest interval states

Recommended narrative states:

- PLANNED
- STARTED
- INTERRUPTED
- RESUMED
- COMPLETED
- CANCELLED
- UNKNOWN_END

These describe history, not PTU eligibility.

Do not add `HEALED`, `EXTENDED_REST_COMPLETE`, `AP_RESTORED` or similar mechanical labels unless they are exact outputs returned by the governing rules engine.

## 3. Activity evidence

PTU defines Rest in terms of activity. Narrative therefore needs enough provenance for an authoritative resolver to make a later decision without pretending that Narrative owns the rule.

```yaml
rest_activity_observation:
  observation_id: null
  interval_id: null
  observer_or_system_ref: null
  activity_type: null
  started_at: null
  ended_at: null
  source_event_ids: []
  confidence: null
  notes: null
```

Candidate descriptive activity types:

- SLEEPING
- QUIET_SITTING
- MEAL
- LIGHT_CONVERSATION
- WATCH_DUTY
- TRAVEL
- FIELDWORK
- TRAINING
- MEDICAL_TREATMENT
- UNKNOWN

These labels do not decide whether an activity satisfies PTU Rest. That determination belongs to authoritative mechanics and can depend on context.

## 4. Sleep record

Sleep is useful world information even when no battle mechanics are involved.

```yaml
sleep_record:
  sleep_record_id: null
  actor_id: null
  location_id: null
  start_event_id: null
  wake_event_id: null
  expected_wake_ref: null
  interruption_ids: []
  privacy_scope: PRIVATE_BY_DEFAULT
  source_refs: []
```

Do not expose private sleep schedules globally unless there is a world reason the information is known.

Do not infer health, mood, impairment or negligence from sleep duration without explicit governed evidence.

## 5. Waiting is a deliberate world action

A player may sometimes choose to wait for a later service, observation window or appointment.

```yaml
wait_request:
  wait_request_id: null
  requester_id: null
  current_location_id: null
  target_condition_ref: null
  requested_until: null
  interruption_policy: null
  active_clock_refs: []
  world_events_eligible_during_wait: []
  result_event_id: null
```

Potential target conditions:

- NAMED_TIME
- SERVICE_OPENING
- ACTOR_EXPECTED_AVAILABLE
- OBSERVATION_WINDOW
- TRANSPORT_DEPARTURE
- WEATHER_REVIEW_TIME
- AUTHORED_EVENT_TIME

Waiting should be offered when it compresses non-significant time. It should not erase active deadlines, ongoing emergencies or world events whose progression is already established.

## 6. Bounded overnight progression

When time advances, the world may process only state that already has a legitimate owner and clock.

Examples:

- a scheduled ferry arrival may occur;
- an existing delivery may enter custody;
- a known report can be copied or delivered by an assigned actor;
- an NPC can move from one schedule slot to another;
- an ecological observation window can open or close;
- an existing repair or service review time may be reached.

Time advancement must not spontaneously create:

- a disaster;
- an antagonist;
- a death;
- a theft;
- a relationship change;
- a battle result;
- a newly invented ecological event;
- a completed investigation.

The relevant subsystem must already contain the causal state.

## 7. Duty assignment

A named person can hold an ordinary responsibility during a bounded period.

```yaml
duty_assignment:
  assignment_id: null
  institution_or_project_id: null
  actor_id: null
  role_ref: null
  scope_refs: []
  starts_at: null
  planned_end: null
  actual_end: null
  current_state: PLANNED
  predecessor_assignment_id: null
  successor_assignment_id: null
  handoff_record_id: null
  exception_contact_ids: []
```

Suggested states:

- PLANNED
- ACTIVE
- HANDOFF_PENDING
- ENDED
- INTERRUPTED
- CANCELLED

A duty assignment is an operational fact. It grants no PTU Feature, Skill Rank, institutional promotion or legal authority beyond already established scope.

## 8. Handoff record

A day boundary becomes useful when responsibility carries information across it.

```yaml
duty_handoff:
  handoff_id: null
  from_actor_id: null
  to_actor_id: null
  institution_or_project_id: null
  occurred_at: null
  active_task_refs: []
  unresolved_question_refs: []
  knowledge_packet_refs: []
  custody_refs: []
  equipment_refs: []
  exception_refs: []
  acknowledged_by_ids: []
```

The handoff transfers only the information or responsibility that is actually included.

`HANDOFF_OCCURRED != SUCCESSOR_KNOWS_EVERYTHING_PREDECESSOR_KNOWS`.

## 9. Actor availability

Schedules require more resolution than present/absent.

```yaml
actor_availability:
  actor_id: null
  timestamp_or_window: null
  availability_state: null
  location_ref: null
  reason_ref: null
  contact_route_refs: []
```

Candidate states:

- AVAILABLE
- WORKING_BUSY
- OFF_DUTY
- RESTING
- SLEEPING
- TRAVELING
- FIELD_ASSIGNMENT
- PRIVATE_TIME
- UNAVAILABLE_AUTHORED_REASON
- UNKNOWN

Availability state is presentation/interaction routing. It does not create a medical status.

## 10. Interruptions

An interruption is an event with provenance.

```yaml
rest_interruption:
  interruption_id: null
  interval_id: null
  event_id: null
  occurred_at: null
  actor_response: null
  new_activity_ref: null
  later_resume_interval_id: null
```

Do not merge separated periods into one continuous interval simply because the actor eventually returned to bed or camp.

A mechanics resolver receives the actual interval history.

## 11. No fatigue subsystem by implication

This layer intentionally does not contain:

- fatigue points;
- exhaustion stages;
- sleep debt;
- alertness modifiers;
- morale loss from interrupted sleep;
- accuracy/evasion penalties at night;
- automatic initiative penalties after waking;
- generic insomnia;
- mandatory hours of sleep.

If PTU/Caelo contains a specific mechanic that should be implemented later, add it through a reviewed authority boundary rather than deriving it from these narrative records.

## 12. Ordinary narrative sleep versus PTU Sleep status

The same English word must not collapse two different domains.

A character who goes to bed is narratively sleeping.

PTU `Sleep` is a mechanical Status Condition with rules owned by PTU/AutoPTU.

```text
ORDINARY_SLEEP_STATE
  -> world schedule / presentation

PTU_SLEEP_STATUS
  -> authoritative mechanical state
```

Narrative bedtime does not apply the PTU status. A move or effect applying PTU Sleep does not by itself establish that an actor completed ordinary overnight rest.

## 13. Mechanical rest handshake

When AutoPTU-Java eventually exposes a verified rest resolver, Narrative should call it through an explicit request/result boundary.

Candidate request shape:

```yaml
rest_adjudication_request:
  actor_or_pokemon_id: null
  interval_refs: []
  authoritative_pre_rest_state_ref: null
  ruleset_ref: null
  content_refs: []
```

Candidate response storage:

```yaml
rest_adjudication_result:
  result_id: null
  authority_ref: null
  accepted_interval_refs: []
  rejected_or_nonqualifying_refs: []
  authoritative_state_delta_ref: null
  emitted_event_refs: []
```

Narrative should not recompute the HP, Injury, AP, Status or Move-frequency changes from prose.

## 14. Lodging integration

A lodging record can offer a place to sleep or wait.

It does not guarantee:

- safety under all events;
- healing;
- privacy beyond the establishment's actual state;
- uninterrupted rest;
- Pokémon Center services;
- mechanical camp bonuses.

Boarding rooms in Puerto Bruma can therefore be meaningful physical spaces without becoming a substitute for Oren's clinic or for PTU rest adjudication.

## 15. Travel and expedition integration

`travel-transport-expedition-layer.md` already supports staging sites and expeditions.

This layer can attach rest and duty records to those existing objects:

```yaml
expedition_rest_plan:
  expedition_id: null
  staging_site_id: null
  planned_interval_refs: []
  duty_assignment_ids: []
  departure_target_ref: null
  contingency_refs: []
```

Watch assignments are narrative responsibilities unless PTU/Caelo explicitly gives them mechanics.

No watch order grants perception, initiative or anti-ambush bonuses by default.

## 16. Time-specific observation

Research or field episodes may depend on a time window when current evidence supports it.

Examples:

- a first-light route inspection;
- an evening interview block already on Taro's schedule;
- a ferry arrival window;
- a nocturnal observation that has actual ecology support;
- a pre-opening market handoff.

Time-specific content should usually provide at least one of these alternatives:

- wait/compress until the window;
- pursue another evidence lane;
- return later;
- obtain a record from an actor who attended;
- miss the live observation but preserve the world consequence.

The system should not force real-time waiting.

## 17. Player offline boundary

A multiplayer/server implementation must keep client connectivity separate from character state.

- logging out does not put the character to bed;
- disconnecting does not satisfy PTU Rest;
- a server restart does not advance the world night unless the authoritative clock explicitly advances;
- reconnecting does not reroll overnight events;
- a Minecraft bed use animation is only an interaction request until Ouros accepts a world-time/rest transition.

## 18. Minecraft/Cobblemon presentation

Possible projections:

- bed or cot interaction;
- tent/camp props;
- dimmed or closed service spaces;
- sleeping animation if supported;
- wake-up placement;
- changed NPC schedule after time advance;
- handoff note/board props;
- campfire or lighting as presentation where authored.

The adapter cannot decide mechanical rest completion, healing, PTU Sleep status, actor negligence, or which off-screen world tasks completed.

## 19. Quest and story value

Rest becomes interesting when it intersects another state:

- leaving before a report arrives versus waiting for it;
- joining an early observation versus following a different lead;
- a delayed ferry changing tomorrow's staff availability;
- a field team choosing to stage overnight rather than return;
- a handoff preserving one unresolved discrepancy;
- a resident being off duty when the player seeks them;
- a task continuing through a different worker rather than freezing.

Routine bedtime should compress.

## 20. Marea application boundary

Current canon safely supports:

- Ivo's pre-dawn purchasing rhythm;
- Taro's interview evenings;
- Sela/Jace morning maintenance versus later public sessions;
- Nerea/Ema field observation timing;
- ferry arrival/departure schedules through Lia/Mina;
- boarding rooms in Puerto Bruma;
- expedition/staging possibilities on Sendero del Vidrio when a specific authored episode establishes them.

Current canon does not establish:

- round-the-clock staffing;
- a curfew;
- mandatory watches;
- a standard inn operator;
- regional labor law;
- a generic campsite on Sendero;
- a fixed sleep schedule for every resident.

## 21. Rich encounter contract — Pre-Dawn Camp Withdrawal at Sendero

Narrative premise:

A field party has staged overnight for a legitimate early observation or route task. Before departure, a localized wild confrontation makes the immediate approach unsafe. The story question is whether the team can withdraw or clear the immediate approach without converting the camp, sleeping actors or research purpose into battle-owned truth.

### Full intended version

World layer:

- camp/staging-site state;
- who is currently awake, resting or already withdrawn;
- equipment/custody state;
- planned observation purpose;
- departure target;
- existing ecology source for the wild actor;
- interrupted rest records;
- later handoff/replan state.

Potential tactical layer:

- static camp-edge geometry;
- protection of an exit corridor;
- positioning around obstacles;
- Interception or forced movement if exact content causes it;
- visibility, terrain or hazards only if the authoritative tactical family supports them;
- objective-aware withdrawal behavior only when AI policy supports it.

Permanent capability dependencies:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL and blocking where the objective relies on those interactions;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected battle content uses statuses; ordinary narrative sleep must never be mapped to PTU Sleep automatically;
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, uneven camp terrain, weather, zones or reactions affect legality/outcomes;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL when exact battle items participate;
- Trainer Features/perks: PARTIAL; exact Features that alter opening actions, movement or rest require individual verification;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for reliable objective-aware withdrawal, corridor control or avoidance of noncombatant areas;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING for faithful full projection and return to persistent camp state.

Disposition: FULL VERSION BLOCKED.

### Reduced executable version

Keep all sleeping/resting actors, camp equipment and investigation semantics outside BattleSpec.

Before combat:

1. Narrative records the interruption time.
2. Noncombatants are moved to a safe world-state position through authored event logic.
3. Select only battle-ready combatants with audited legal sheets.
4. Use stable geometry and omit tactical darkness/weather/hazards unless verified.

AutoPTU resolves one ordinary audited battle.

Allowed narrow results:

- `IMMEDIATE_CAMP_APPROACH_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_FIELD_TEAM_CAN_WITHDRAW`

Narrative then decides whether the party resumes rest, abandons the observation window, changes duty assignments or departs later.

Battle output must never directly write:

- Extended Rest completion;
- HP/AP/Move-frequency recovery outside authoritative mechanics;
- ordinary sleep quality;
- exhaustion;
- PTU Sleep status from bedtime;
- research success;
- population hostility;
- permanent route safety.

## 22. Current engine evidence

AutoPTU-Java head inspected for pass 196: `09fc8bcf22c18d3106718a9d98005aae501a41d4`.

The newest commit freezes a Python semantic-event contract for Insectoid Utility + Wallclimber forced-movement prevention. The commit itself says Java can preserve prevention provenance internally without yet exposing that Python event. This strengthens one content-specific parity contract and leaves the broader movement/Trainer Feature families incomplete.

No Java search hit for a Rest/Extended Rest resolver was found under those names during this pass. Do not interpret source prose presence as runtime support.

AutoPTU remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, with presentation-only head changes.

## 23. Caelo questions before promotion

Resolve from authoritative Caelo sources before asserting:

- regional rest-rule overrides;
- camping procedures;
- required night watches;
- travel curfews;
- lodging obligations;
- labor/rest requirements;
- settlement quiet-hour customs;
- night-specific route restrictions;
- any additional recovery mechanics.

## 24. Implementation recommendation

Implement `Mirador First-Light Handoff` before any mechanical Rest interaction.

Acceptance target:

- an authored observation window spans a day boundary;
- Nerea and Ema have separate availability and knowledge records;
- a handoff transfers only recorded observations/questions;
- the player can attend, wait, return later or receive the resulting record;
- nobody receives mechanical recovery from the scene;
- missing the live window does not erase the observation from world history if another actor legitimately performed it.