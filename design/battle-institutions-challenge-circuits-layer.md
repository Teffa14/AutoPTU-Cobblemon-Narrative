# Ouros Battle Institutions & Challenge Circuits Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models institutions, public memory, recurring events, arena state, rival memory, alternative encounter objectives and performance circuits. This layer adds the battle-centered institutional layer: Gyms, Dojos, battle schools, tournament committees, invitational events, formal challenge records, rematches, qualifications and post-League-style mastery venues.

The goal is to make formal battling feel like part of the world rather than a sequence of isolated boss fights.

## 1. Battle institution object

```yaml
battle_institution:
  institution_id: null
  institution_type: null
  location_ids: []
  public_role: null
  challenge_philosophy: null
  operating_body_ids: []
  current_leadership_ids: []
  staff_ids: []
  trainee_ids: []
  venue_ids: []
  official_formats: []
  qualification_outputs: []
  public_titles: []
  traditions: []
  historical_records: []
  current_status: open
  mechanics_review_required: true
```

Candidate types:
- GYM
- DOJO
- BATTLE_SCHOOL
- LEAGUE_OFFICE
- TOURNAMENT_COMMITTEE
- INVITATIONAL_VENUE
- MASTERY_FACILITY
- CLUB_ARENA
- EXHIBITION_HALL

The canonical Ouros set remains undecided.

## 2. Institution role is separate from battle format

A Gym can also be:
- a school;
- community training center;
- research partner;
- emergency shelter;
- local employer;
- youth club;
- historical institution;
- civic landmark.

A formal battle format can be hosted by multiple institutions.

This avoids tying every piece of battle content to one organizational hierarchy.

## 3. Challenge philosophy

A memorable challenge should test a legible concept.

```yaml
challenge_philosophy:
  philosophy_id: null
  institution_id: null
  lesson_tags: []
  preferred_arena_patterns: []
  preferred_objective_types: []
  scouting_signals: []
  teaching_outputs: []
```

Example lesson tags, kept system-neutral:
- positioning;
- adaptation;
- switching judgment;
- terrain awareness;
- protection;
- endurance;
- tempo;
- resource discipline;
- capture judgment;
- coordination;
- information management;
- risk management.

These tags never grant modifiers. They describe design intent.

## 4. Formal challenge contract

Every official challenge should have a reviewed rules contract before AutoPTU starts the battle.

```yaml
challenge_contract:
  contract_id: null
  institution_id: null
  format_version: null
  challenger_ids: []
  opponent_ids: []
  team_policy_ref: null
  trainer_participation_policy_ref: null
  item_policy_ref: null
  arena_profile_ref: null
  objective_profile_ref: null
  win_conditions_ref: null
  loss_conditions_ref: null
  draw_policy_ref: null
  withdrawal_policy_ref: null
  rematch_policy_ref: null
  qualification_effect_ref: null
  reward_policy_ref: null
  public_record_policy: null
  mechanics_review_required: true
```

Narrative generation can choose among approved contracts. It cannot invent their mechanical contents.

## 5. Challenge states

```yaml
challenge_state:
  challenge_id: null
  contract_id: null
  lifecycle_state: registered
  scheduled_time: null
  preparation_window: null
  participants_present: []
  prebattle_public_info: []
  result_ref: null
  postbattle_review_ref: null
```

Suggested lifecycle:
- ELIGIBLE
- REGISTERED
- PREPARING
- READY
- ACTIVE
- COMPLETED
- WITHDRAWN
- VOIDED
- ARCHIVED

Voided should exist for technical or procedural failures without treating the battle as a loss.

## 6. Scouting boundary

Formal challenge preparation may use public and legally observed information.

```yaml
challenge_scouting:
  subject_id: null
  observer_id: null
  public_style_tags: []
  observed_battle_refs: []
  confirmed_team_reveals: []
  arena_public_info: []
  rumors: []
  private_information: []
```

Hard rule:
- battle AI may not read world truth or private opponent loadout unless the scenario explicitly grants that information;
- a Leader can remember Moves, tactics or team members actually revealed in earlier public battles;
- a challenger may study public recordings or reports if those records exist;
- rumors remain claims, not truth.

## 7. Challenger battle history

```yaml
formal_battle_record:
  battle_record_id: null
  battle_result_ref: null
  institution_id: null
  event_id: null
  format_version: null
  participant_ids: []
  public_result: null
  objective_result: null
  revealed_information: []
  witnessed_by: []
  qualification_outputs: []
  title_outputs: []
  public_memory_outputs: []
  rematch_of: null
```

The record should not duplicate the full AutoPTU combat log. It points to the authoritative result and stores narrative/institutional consequences.

## 8. Post-battle review

Losses and draws should create useful state without fabricating buffs.

```yaml
postbattle_review:
  review_id: null
  battle_record_id: null
  observed_turning_points: []
  player_visible_lessons: []
  institution_feedback: []
  optional_training_hooks: []
  rematch_conditions: []
  unresolved_rules_questions: []
```

Possible hooks:
- practice against a known arena interaction;
- seek a mentor who specializes in a relevant skill;
- obtain public information about a format;
- try an exhibition match;
- use a different approved team composition;
- return after another world-state goal.

No hook grants an automatic combat bonus.

## 9. Rematch memory

```yaml
rematch_state:
  rematch_id: null
  previous_battle_record_ids: []
  challenger_changes_observed: []
  opponent_changes_public: []
  arena_changes_public: []
  format_changes_public: []
  legal_memory_refs: []
```

A rematch should change because state changed, not because enemies silently received arbitrary numerical scaling.

Potential causes:
- different approved roster profile;
- different challenge contract;
- changed institution leadership;
- changed venue state;
- newly public strategies;
- player chooses a different legal team;
- challenge serves a higher qualification tier.

## 10. Challenge roster profiles

Ouros may need institutions to serve Trainers at different progression stages. That must be explicit rather than hidden rubber-banding.

```yaml
challenge_roster_profile:
  profile_id: null
  institution_id: null
  eligibility_rule_ref: null
  approved_team_ref: null
  approved_ai_policy_ref: null
  intended_challenge_band: null
  disclosure_policy: null
  mechanics_review_required: true
```

The narrative layer must not invent level suppression, stat normalization, custom powers or unseen buffs to make a roster fit.

## 11. Exhibition battles

Exhibitions are formal but non-qualification events.

```yaml
exhibition_event:
  exhibition_id: null
  host_institution_id: null
  participant_ids: []
  purpose_tags: []
  contract_ref: null
  public_result_policy: null
  qualification_effect: none
```

Purposes:
- teaching;
- charity;
- celebration;
- demonstration;
- staff evaluation;
- mentor/student practice;
- public entertainment;
- testing a new approved format.

An exhibition result may affect public memory but should not silently grant a Badge or rank.

## 12. Training exercises

Training content should focus on a narrow question and end quickly.

```yaml
training_exercise:
  exercise_id: null
  host_id: null
  lesson_tags: []
  setup_ref: null
  completion_condition_ref: null
  formal_battle: false
  repeatable: false
  mechanics_review_required: true
```

Avoid turning training into an infinite farming loop. Repeatable drills should become compressed or capped once the learning content is exhausted.

## 13. Qualification graph

Ouros should represent qualification as data rather than assume eight Badges.

```yaml
qualification_node:
  qualification_id: null
  name: null
  granting_institution_ids: []
  prerequisite_refs: []
  recognized_by: []
  expires: false
  season_ref: null
  next_qualification_ids: []
  alternative_routes: []
```

Possible future uses:
- Gym credentials;
- tournament placement;
- academy certification;
- invitational qualification;
- mastery symbols;
- regional licenses.

Canonical routes require human worldbuilding approval.

## 14. Challenge circuit

```yaml
battle_circuit:
  circuit_id: null
  host_body_id: null
  institution_ids: []
  season_id: null
  qualification_graph_ref: null
  event_ids: []
  ranking_policy_ref: null
  championship_event_id: null
  record_archive_id: null
```

A circuit may be:
- permanent;
- seasonal;
- invitational;
- regional;
- interregional;
- institution-specific.

## 15. Ranking and titles

Ranking, qualification and public prestige are separate.

A Trainer can:
- qualify without being famous;
- be famous without holding a high formal rank;
- hold an old title while inactive;
- have a strong local record but little regional recognition.

```yaml
competitive_standing:
  actor_id: null
  circuit_id: null
  current_tier_ref: null
  qualification_ids: []
  active_titles: []
  historical_titles: []
  season_record_ref: null
  public_standing_ref: null
```

Exact ranking math remains an approved policy outside narrative generation.

## 16. Tournament object

```yaml
tournament:
  tournament_id: null
  event_id: null
  host_institution_ids: []
  format_version: null
  qualification_policy_ref: null
  participant_ids: []
  bracket_policy_ref: null
  round_states: []
  active_player_matches: []
  resolved_nonplayer_matches: []
  public_record_ref: null
```

Tournament design rule:
Do not force the narrative system to fully simulate every NPC-vs-NPC battle. Exact NPC results require either an approved simulation policy, imported authoritative result or human-authored outcome.

## 17. Match narrative budget

Tournaments can become repetitive if every battle receives equal narrative weight.

Prioritize full scene treatment when at least one condition applies:
- active player participates;
- recurring rival participates;
- qualification depends on the result;
- unusual approved format;
- public controversy;
- significant relationship consequence;
- major record attempt;
- arena state matters to future world state.

Other matches may exist as records and public results.

## 18. Battle facility / mastery venue

A mastery venue can host rotating approved formats without changing regional League canon.

```yaml
mastery_venue:
  venue_id: null
  institution_id: null
  available_format_refs: []
  rotation_policy_ref: null
  record_types: []
  recurring_master_ids: []
  title_or_symbol_policy_ref: null
  eligibility_ref: null
```

Useful design functions:
- post-circuit challenge;
- experimentation with unusual approved rules;
- repeatable high-level content;
- records and streaks;
- cross-regional visitors;
- testing AutoPTU objective modes.

Videogame Battle Frontier rules are not imported automatically.

## 19. Gym / institution staffing and succession

```yaml
battle_staff_role:
  actor_id: null
  institution_id: null
  role_type: null
  status: active
  qualification_refs: []
  mentor_ids: []
  trainee_ids: []
```

Candidate roles:
- Leader;
- Gym Trainer;
- referee;
- registrar;
- arena technician;
- medic;
- analyst;
- instructor;
- security;
- event coordinator.

Leadership can change while the institution preserves records, traditions, debts and controversies.

## 20. Institution readiness

A battle institution can be narratively open while formal challenges are unavailable.

```yaml
institution_readiness:
  institution_id: null
  venue_ready: true
  staff_ready: true
  medical_support_ready: true
  registration_open: true
  event_conflict_ids: []
  closure_reason_refs: []
```

Potential state changes:
- arena under repair;
- staff absent;
- crisis duty;
- tournament preparation;
- weather/route access problem;
- investigation hold;
- leadership transition.

This lets world events matter without deleting the institution.

## 21. Battle institution and settlement integration

A major Gym or arena may affect:
- visitor traffic;
- lodging;
- local jobs;
- transport demand;
- training services;
- shops;
- public celebrations;
- sponsorships;
- local prestige;
- youth programs;
- emergency response capacity.

Conversely, settlement state can affect whether the venue operates normally.

## 22. Battle records as public culture

Formal results can feed the existing public-memory layer.

Possible outputs:
- local recognition;
- rival attention;
- invitations;
- historical records;
- records broken;
- exhibition requests;
- interview or media interest;
- alumni status;
- sponsor interest candidate;
- public controversy.

The battle result itself remains authoritative from AutoPTU or the approved tournament resolver.

## 23. Anti-farming guardrail

Repeated easy battles should not automatically produce infinite prestige or qualification progress.

Narrative generation should consult an approved ranking/reward policy that can consider:
- opponent relevance;
- format relevance;
- first-time achievement;
- event tier;
- season state;
- repetition;
- record significance.

The narrative layer cannot invent numerical diminishing returns.

## 24. Rival integration

Recurring competitive rivals can exist across institutions.

A rival history may record:
- formal results;
- exhibitions;
- public titles;
- revealed tactics;
- mutual invitations;
- training overlaps;
- team changes publicly seen;
- sportsmanship incidents;
- shared mentors.

Private emotions remain outside automatic inference.

## 25. Minecraft representation

Battle institutions can appear physically through:
- registration desks;
- waiting areas;
- practice courts;
- arena gates;
- leader offices;
- trophy displays;
- title boards;
- bracket boards;
- viewing stands;
- classrooms;
- staff rooms;
- repair states;
- event decorations;
- archived posters;
- challenger queues.

The visible venue should reflect lifecycle and readiness state.

## 26. AutoPTU integration contract

Before an official battle begins, the narrative layer should hand AutoPTU only reviewed references:
- participant IDs;
- legal Pokémon/team refs;
- approved challenge contract;
- arena profile;
- objective profile;
- AI policy ref;
- public/replay policy.

AutoPTU returns:
- authoritative outcome;
- battle event/log ref;
- revealed-information events;
- withdrawal/draw/surrender state if supported;
- objective resolution;
- mechanical consequences.

Narrative systems then create institutional/public consequences from that authoritative output.

## 27. PTU / Caelo boundary

The project source set remains authoritative for:
- League battle initiative;
- Trainer participation;
- legal Features and Orders;
- item use;
- challenge rewards;
- significance/experience;
- capture legality;
- arena interaction;
- Gym/Dojo progression;
- rematch mechanics if defined;
- any Caelo-specific restrictions.

This layer must not create:
- custom Moves;
- custom Orders;
- Badge powers;
- stat normalization;
- Power Limiter effects;
- hidden level scaling;
- arbitrary boss HP;
- item allowances;
- ranking points;
- Badge thresholds;
- tournament seeding math;
- healing between rounds;
- roster legality.

All such mechanics require governing-source and implementation review.

## 28. Implementation priority

Recommended order:
1. formal battle record;
2. challenge contract schema;
3. institution readiness;
4. rematch links;
5. public scouting boundary;
6. post-battle review hooks;
7. qualification graph;
8. tournament/event integration;
9. mastery venue records;
10. ranking/title policy integration.

This order gives Ouros trustworthy battle history before adding automated competitive progression.
