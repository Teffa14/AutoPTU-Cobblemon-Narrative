# Recurring Rival Agency and Progression Layer

Status: PROPOSED SYSTEMS DESIGN. NOT CANON.
Date: 2026-09-01

## Purpose

This layer gives recurring competitive NPCs durable agency outside isolated battles. It connects existing questline, relationship, schedule, institution, public-memory and battle-record systems without replacing them.

The core requirement is simple: a rival must remain a person when no battle is happening.

## 1. Rival profile

```yaml
rival_profile:
  rival_profile_id: null
  actor_id: null
  status: candidate
  rivalry_origin_ref: null
  rivalry_scope: null
  current_competitive_role: null
  persistent_pokemon_ids: []
  public_style_tags: []
  current_agenda_ref: null
  current_activity_ref: null
  current_location_ref: null
  challenge_availability_ref: null
  formal_battle_history_refs: []
  informal_competition_refs: []
  cooperation_history_refs: []
  conflict_history_refs: []
  witnessed_change_refs: []
  unresolved_tensions: []
  canon_review_required: true
```

A rival profile does not create friendship, hostility, romance, jealousy, admiration or resentment. Those require explicit authored evidence.

## 2. Rivalry scope

Candidate scopes:

- competitive peer;
- aspirational challenger;
- senior benchmark;
- local circuit counterpart;
- professional peer;
- ideological competitor;
- friendly sparring partner;
- temporary event rival;
- multi-season recurring challenger.

Scope describes authored framing. It grants no bonus.

## 3. Independent agenda

```yaml
rival_agenda:
  agenda_id: null
  actor_id: null
  goal_type: null
  goal_statement: null
  supporting_world_facts: []
  active_task_refs: []
  blocker_refs: []
  progress_evidence_refs: []
  player_relevance: incidental
  next_review_at: null
```

The player may intersect the agenda, help it, obstruct it or ignore it.

`RIVAL_AGENDA != PLAYER_QUEST`.

A rival can complete ordinary steps without the player when world state and schedule support it.

## 4. Challenge availability

```yaml
rival_challenge_availability:
  actor_id: null
  state: unavailable
  reason_ref: null
  available_contract_refs: []
  earliest_window: null
  location_refs: []
  requires_registration: false
  requires_world_condition_refs: []
  refusal_reason_public: null
```

Suggested states:

- UNAVAILABLE_DUTY
- UNAVAILABLE_TRAVEL
- UNAVAILABLE_RECOVERY
- UNAVAILABLE_EVENT_CONFLICT
- AVAILABLE_INFORMAL
- AVAILABLE_EXHIBITION
- AVAILABLE_FORMAL
- SCHEDULED
- ACTIVE
- COOLDOWN

Cooldown is narrative scheduling state only. It must not invent PTU recovery timing.

## 5. Rival encounter purpose

Every full battle proposal should declare a narrative purpose.

```yaml
rival_encounter_purpose:
  encounter_id: null
  purpose_tags: []
  changed_world_state_expected: []
  changed_public_info_expected: []
  changed_rival_state_expected: []
  full_battle_required: false
```

Useful purpose tags:

- first benchmark;
- rematch after public change;
- qualification intersection;
- mentor evaluation;
- disputed style test;
- shared-event consequence;
- farewell or return;
- role transition;
- tournament pairing;
- voluntary practice.

If the battle changes nothing beyond adding another win/loss row, prefer compression or postpone it.

## 6. Competitive history

The formal battle record remains owned by the battle-institutions layer.

This layer stores references and rival-specific interpretation boundaries.

```yaml
rival_competitive_history:
  rival_profile_id: null
  formal_record_refs: []
  informal_record_refs: []
  revealed_information_refs: []
  witnessed_style_changes: []
  recurring_venue_refs: []
  shared_event_refs: []
```

No private tactics can be inferred from unseen data.

## 7. Offscreen progression

```yaml
rival_progression_event:
  progression_event_id: null
  actor_id: null
  event_type: null
  started_at: null
  resolved_at: null
  location_refs: []
  evidence_refs: []
  public_outputs: []
  authored_character_outputs: []
  battle_profile_review_required: false
```

Candidate event types:

- TRAINING_BLOCK_COMPLETED
- DUTY_ASSIGNMENT_COMPLETED
- TOURNAMENT_ENTERED
- TOURNAMENT_RESULT_IMPORTED
- TRAVEL_COMPLETED
- CERTIFICATION_EARNED
- ROLE_CHANGED
- PARTNER_EVOLUTION_AUTHORED
- EQUIPMENT_CHANGE_AUTHORED
- PUBLIC_STYLE_CHANGE_OBSERVED
- COOPERATION_EVENT_COMPLETED

Offscreen progression may alter world and character state only through explicit policies or authored events. It cannot fabricate AutoPTU battle outcomes.

## 8. NPC-versus-NPC battle boundary

If a rival enters a tournament while the player is elsewhere, the narrative layer cannot invent exact PTU combat results unless an approved resolver exists.

Valid approaches:

- imported authoritative result;
- approved lightweight simulation policy;
- human-authored result;
- unresolved bracket state;
- non-battle progression event.

`OFFSCREEN_RIVAL_PROGRESS != FABRICATED_DICE`.

## 9. Persistent Pokémon integration

Use `canon/npc-pokemon-dynamic-progression-v1.md`.

Persistent Pokémon identity survives.

Encounter-derived level and legal moves come from the canon scaling policy plus authoritative PTU/Caelo data and AutoPTU validation.

Rival progression cannot silently:

- evolve a Pokémon;
- change species/form;
- grant a TM;
- choose a new Ability;
- change Nature;
- add an Item;
- add a Trainer Feature;
- add an illegal Move.

Those require their governing policies.

## 10. Observable development

Character change should be represented through evidence.

Examples:

- changed schedule;
- changed workplace responsibility;
- changed public battle style;
- new documented training practice;
- changed care behavior toward Pokémon;
- changed cooperation choice;
- different response to a repeated situation;
- role transition;
- public apology or correction if authored;
- new institutional trust evidenced by delegated responsibility.

A single event can support interpretation but should not automatically close a private-emotion question.

## 11. Rival and relationship separation

A `RIVAL` questline and a `RELATIONSHIP` questline may share episodes while retaining distinct state.

Possible combinations:

- competitive respect with little personal closeness;
- friendship without active competition;
- unresolved personal conflict with formal sportsmanship;
- temporary cooperation between antagonistic competitors;
- mentor/student relationship that later becomes peer competition.

No scalar meter should collapse these states.

## 12. Rival and character separation

A rival's own `CHARACTER` arc continues even when the player stops competing.

Example structure:

```text
CHARACTER: Jace seeks greater responsibility at the Battle Yard
RIVAL: Jace and player build a recurring competitive history
COMPETITIVE: both enter a local exhibition series
RELATIONSHIP: they negotiate boundaries around training and challenge requests
```

One event may advance several graph edges without duplicating state.

## 13. Challenge refusal

A rival should be able to say no through world state.

Legitimate reasons include:

- working;
- scheduled maintenance;
- assisting another resident;
- traveling;
- recovering under actual governed care state;
- already registered for another event;
- venue unavailable;
- challenge contract not currently valid.

Refusal should not be interpreted automatically as fear, dislike or loss of rivalry.

## 14. Rival request generation

Challenge requests should be traceable to a trigger.

Candidate triggers:

- player enters an approved competitive event;
- rival completes a relevant training block;
- public record changes;
- shared mentor schedules an exhibition;
- venue reopens after repair;
- prior rematch condition becomes satisfied;
- player publicly demonstrates a new legal tactic;
- rival returns from travel;
- seasonal circuit opens.

No random challenge spam solely because a cooldown expired.

## 15. Scouting memory

Future rival AI may use only information legally available through the existing challenge scouting boundary.

Potential legal inputs:

- Moves revealed in prior observed battles;
- public team members;
- public recordings;
- known arena preferences;
- previous objective choices;
- public challenge contract.

Private current loadout remains inaccessible unless the scenario grants it.

## 16. Tactical dependency contract

A rival narrative episode can be mechanically light or tactically rich.

### Light version

Conversation, registration, observation, schedule changes, public record review, travel and noncombat cooperation require no BattleSpec.

### Full rival battle

Dependencies depend on selected roster and format.

Required baseline families:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content uses statuses;
- move-specific behavior for selected Moves;
- abilities for selected Abilities;
- items if Items are permitted;
- Trainer Features/perks if Trainers participate with those Features;
- AI legal-action infrastructure;
- AI tactical policy for credible rival behavior;
- Minecraft/Cobblemon/Craftics adapter/playback for faithful in-world presentation.

Complete movement becomes required whenever selected content includes Push, Pull, Knockback, Interception, forced movement, collision-sensitive movement or related interactions.

Terrain/weather/hazards/zones/reactions becomes required whenever the approved venue or selected content uses those mechanics.

## 17. Reduced parity-safe rival battle

A reduced battle can preserve the narrative premise by selecting an audited contract and roster that avoid unsupported families.

Constraints may include:

- stable open arena;
- no dynamic weather;
- no hazards/zones/reactions;
- no forced-movement content unless specifically verified;
- no Items unless audited;
- no Trainer Feature interrupts unless audited;
- no unsupported statuses;
- only Moves and Abilities whose exact behavior is covered by current contracts;
- AI choices restricted to legal infrastructure if tactical policy is not yet parity-ready.

The reduction changes the battle contract, not the rival's personality or world premise.

## 18. Battle output boundary

AutoPTU may return:

- authoritative winner/draw/withdrawal state when supported;
- combat logs;
- revealed mechanical information;
- HP/status/injury outputs governed by the engine;
- objective result when supported.

Narrative may then write:

- formal battle record;
- public result;
- rematch link;
- witnessed style evidence;
- schedule consequences;
- new dialogue availability;
- authored character reflection hooks.

Narrative may not infer friendship, humiliation, fear, forgiveness or permanent hierarchy from the outcome alone.

## 19. Minecraft representation

Useful physical projections:

- Jace training at a marked yard fixture;
- posted exhibition schedule;
- challenge registration ledger;
- public result board;
- rival absent from the yard because a world-state duty moved him elsewhere;
- visible partner Pokémon bound to persistent identity;
- archived posters from prior events;
- equipment or arena layout changes supported by world state.

Minecraft pathing, chunk unload or entity death cannot create rival progression.

## 20. Long-term arc shape

A durable rival arc can use phases such as:

1. NOTICE — player and NPC become aware of each other's competitive relevance.
2. FIRST_TEST — a bounded encounter establishes public evidence.
3. PARALLEL_WORK — both pursue separate goals.
4. REINTERSECTION — a new shared event makes another contest meaningful.
5. ROLE_CHANGE — one actor's responsibilities change.
6. COOPERATION_OR_CONFLICT — competition intersects a noncompetitive problem.
7. MATURE_RIVALRY — rematches happen because both choose them or institutions pair them, not because the story needs filler.
8. DIVERGENCE — rivalry can become dormant without deleting history.

These are narrative phases, not mandatory linear progression.

## 21. Anti-repetition rules

Do not schedule a full rival fight merely because:

- the player entered a new town;
- enough time elapsed;
- the rival has a new level;
- the player won the previous fight;
- a quest slot needs combat.

Prefer a full battle when it exposes new mechanical, institutional, public or character state.

## 22. Canon promotion checklist

Before promoting a rival profile:

- actor already exists or new actor is separately reviewed;
- rivalry origin is explicit;
- current role fits established responsibilities;
- no private emotion is inferred;
- persistent Pokémon IDs are correct;
- encounter policy does not conflict with dynamic-progression canon;
- challenge contracts are mechanically auditable;
- offscreen outcomes do not fabricate AutoPTU results;
- relationship and character arcs remain separable;
- Caelo-specific assumptions are identified and sourced.
