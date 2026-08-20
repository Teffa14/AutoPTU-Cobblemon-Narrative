# Downtime, Hobbies & Personal Projects Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs a way to represent personal life between major quests without converting every quiet moment into filler, grind or mechanical progression.

This layer owns voluntary personal-time state:

- downtime windows;
- personal routines;
- hobbies;
- small self-directed projects;
- leisure preferences;
- recurring casual activities;
- personal collections;
- journals/scrapbooks;
- neighborhood habits;
- low-stakes shared activities;
- routine deviations that can become hooks when supported by evidence.

It does not own medical recovery, employment, formal education, clubs, food mechanics, homes, competitions or relationship labels. Those remain in their existing layers.

## 1. Core separation

Keep these concepts separate:

- free time exists;
- an actor chooses an activity;
- the activity occurs;
- a mechanical subsystem resolves any rules-bearing action;
- a personal project changes state;
- an observer learns something;
- a Chronicle memory is created;
- a relationship changes, if supported;
- the actor's private feelings, unless authored.

Example:

A Trainer spends an evening sketching Pokémon near a pond.

Valid records:

- the Trainer was at the pond;
- the Trainer made a sketch;
- a Wooper repeatedly approached the same bank;
- another NPC joined for twenty minutes;
- a finished sketchbook page now exists.

Invalid automatic conclusions:

- the Trainer gained Perception;
- the Wooper likes the Trainer;
- the NPC became a friend;
- sketching restored AP/HP;
- the scene grants XP because it happened.

## 2. Downtime window

```yaml
downtime_window:
  downtime_id: null
  actor_ids: []
  start_time: null
  end_time: null
  location_id: null
  reason: voluntary|between_tasks|waiting|travel_pause|scheduled_rest|other
  available_activity_tags: []
  active_world_state_refs: []
  chosen_activity_ids: []
  compressed: true
  provenance_refs: []
```

A downtime window says discretionary time exists. It does not apply PTU rest/healing rules by itself.

## 3. Personal routine

```yaml
personal_routine:
  routine_id: null
  actor_id: null
  activity_kind: null
  usual_location_ids: []
  usual_time_pattern: null
  companions_optional: []
  known_since: null
  recurrence_strength: occasional|regular|strong
  current_state: active|paused|changed|ended|unknown
  evidence_refs: []
  privacy: private|shared|public
```

Routines should be authored or learned from repeated observations. The system must not invent a routine after one occurrence.

A routine is descriptive state, not an obligation.

## 4. Hobby profile

```yaml
hobby_profile:
  hobby_id: null
  actor_id: null
  hobby_kind: null
  participation_level: casual|regular|dedicated|unknown
  started_at: null
  location_refs: []
  tool_item_refs: []
  related_project_ids: []
  related_actor_ids: []
  public_visibility: private|known|public
  authored_preference: null
  evidence_refs: []
```

Hobbies may include drawing, reading, gardening, model building, casual fishing, photography, collecting, board/card games, cooking for pleasure, music practice, walking, puzzle solving, decorating or any canon-supported local pastime.

A hobby does not automatically become a profession, club, competitive discipline or mechanical training track.

## 5. Personal project

```yaml
personal_project:
  project_id: null
  owner_actor_ids: []
  title: null
  project_kind: craft|collection|decoration|journal|restoration|study|creative|garden|mapping|other
  started_at: null
  current_phase: idea|started|active|paused|complete|abandoned
  milestone_refs: []
  required_world_state_refs: []
  material_refs: []
  output_refs: []
  blocker_refs: []
  visibility: private|shared|public
  mechanics_review_required: false
  provenance_refs: []
```

Projects should use bounded milestones rather than repetitive action counters unless a governing subsystem explicitly requires them.

Examples:

- restore an old bicycle;
- complete a sketchbook of a neighborhood;
- decorate a rented room;
- build a model lighthouse;
- organize old family photographs;
- maintain a personal garden;
- compile a travel scrapbook;
- make a set of non-mechanical gifts;
- reconstruct a broken personal keepsake.

## 6. Project milestone

```yaml
project_milestone:
  milestone_id: null
  project_id: null
  description: null
  prerequisite_refs: []
  completion_evidence_refs: []
  completed_at: null
  output_refs: []
  world_state_changes: []
```

A milestone can be resolved by another layer:

- crafting system validates an item repair;
- archive layer validates a document scan;
- food layer validates a recipe event;
- cartography layer validates a map survey;
- social layer records a collaborator;
- Minecraft presentation updates the room after approved state changes.

Downtime owns the personal-project wrapper, not those subsystem rules.

## 7. Casual shared activity

```yaml
casual_activity:
  activity_id: null
  participant_ids: []
  activity_kind: null
  location_id: null
  start_time: null
  end_time: null
  voluntary: true
  observed_actions: []
  shared_output_refs: []
  mechanics_result_refs: []
  notable_fact_refs: []
  chronicle_weight: low
```

Examples:

- picnic;
- cards;
- walk;
- casual puzzle;
- campfire conversation;
- neighborhood cleanup;
- movie/show viewing where canonically supported;
- noncompetitive fishing;
- decorating;
- shared cooking for leisure.

Participation alone does not create friendship, romance, trust or Loyalty.

## 8. Personal collection

Collections should use the existing item/provenance layers for physical objects.

This layer only records the personal project and curation intent.

```yaml
personal_collection:
  collection_id: null
  curator_actor_id: null
  collection_kind: null
  item_refs: []
  display_location_refs: []
  acquisition_event_refs: []
  completion_rule: authored_optional
  public_visibility: private|shared|public
  project_id: null
```

Possible collections:

- postcards;
- sketches;
- local badges that are not League badges;
- found photographs with lawful custody;
- non-mechanical souvenirs;
- pressed plants where conservation rules allow;
- model Pokémon;
- books;
- recipes;
- event programs.

Collecting never bypasses ownership, conservation or custody rules.

## 9. Journal and scrapbook state

The Chronicle stores structured world history. A personal journal stores an actor's authored or player-authored perspective.

```yaml
personal_journal_entry:
  entry_id: null
  actor_id: null
  timestamp: null
  referenced_event_ids: []
  authored_text_ref: null
  attached_record_refs: []
  privacy: private
  interpretation_only: true
```

For PCs, free-text thoughts require player authorship.

The system may generate a neutral prompt such as “record today's expedition” but must not write private feelings into the PC's journal without explicit player direction.

## 10. Routine deviation

A deviation becomes meaningful only when a baseline exists.

```yaml
routine_deviation:
  deviation_id: null
  routine_id: null
  expected_window: null
  observed_difference: null
  observation_ref: null
  explanation_state: unknown
  candidate_cause_refs: []
  investigation_hook_eligible: false
```

Example:

A baker who usually feeds Pidove behind the shop every morning does not appear today.

The system can record the absence. It cannot assume illness, kidnapping, death or danger.

Only linked evidence can escalate the deviation into a case, welfare check, travel explanation, staffing issue or other active content.

## 11. Leisure preference

Preferences should be explicit or evidenced.

```yaml
leisure_preference:
  actor_id: null
  activity_tag: null
  stance: enjoys|avoids|neutral|unknown
  evidence_type: authored|explicit_statement|repeated_choice|observation
  evidence_refs: []
  confidence: null
  privacy: null
```

For PCs, only explicit player choices/statements can establish internal preference.

Repeated participation can establish “often participates” without establishing “enjoys”.

## 12. Pokémon participation

A Pokémon may participate in downtime without the layer asserting emotional or mechanical effects.

Valid observations:

- repeatedly chooses a particular resting place;
- joins a game when invited;
- leaves an activity early;
- carries the same toy/object several times;
- watches another Pokémon perform an activity;
- returns to a garden at a recurring time.

Invalid automatic effects:

- Friendship increase;
- Loyalty increase;
- obedience increase;
- training XP;
- permanent Skill/Capability changes;
- mood diagnosis;
- ownership transfer.

Those require governing rules or authored state.

## 13. Routine compression policy

Routine actions should normally compress.

Expand a downtime action into a scene when at least one condition is true:

- player explicitly chooses to focus on it;
- a new participant changes the social context;
- a project reaches a milestone;
- a routine deviation is observed;
- an unresolved world-state issue intersects it;
- a Pokémon displays new observable behavior;
- a meaningful choice appears;
- a location changed since the last visit;
- a new piece of information becomes available;
- the scene creates an irreversible or persistent output.

Otherwise record only necessary state and move on.

## 14. Anti-grind rule

The generator must not create repeated hobby chores solely to consume player time.

Bad pattern:

- water the same plant ten times;
- play the same minigame twenty times;
- visit the same NPC daily to increment a hidden meter;
- repeat an identical walk until a cutscene unlocks.

Preferred pattern:

- project advances because enough time passed and prerequisites were met;
- a new milestone appears when world state changes;
- repetition is summarized;
- only novel decisions become playable scenes.

## 15. Offline advancement

Some projects can advance while the player is offline if the project definition allows it.

Examples:

- paint dries;
- a non-mechanical garden grows according to the agriculture layer;
- an artisan finishes an already-authorized commission;
- a scheduled delivery arrives if transport remains operational.

Offline advancement cannot:

- resolve player choices;
- spend unapproved scarce resources;
- create PTU progression;
- transfer ownership;
- force relationships;
- complete a dangerous encounter;
- cause irreversible personal consequences without an authored policy.

## 16. Connection to Chronicle

Downtime should generate fewer, lower-weight Chronicle events than major quests.

Promote a quiet event to Chronicle when it becomes useful history, for example:

- a project completed;
- a recurring tradition started;
- a personal object gained provenance;
- a location became personally significant through repeated visits;
- a Pokémon showed a repeated behavioral pattern;
- an NPC consistently participated;
- a later event directly references the routine.

Do not store every cup of tea.

## 17. Connection to World Pulse

World Pulse can move around downtime without hijacking it.

Possible intersections:

- weather cancels a walk;
- transport disruption changes a regular market visit;
- migration changes what appears near a hobby site;
- a festival temporarily replaces a routine;
- a workplace shift leaves an NPC unavailable;
- a crisis causes a personal project to pause;
- recovery reopens a favorite location.

The world can affect personal life. It should not turn every quiet activity into a crisis.

## 18. Minecraft presentation

Possible lightweight representations:

- NPCs appearing at recurring leisure spots;
- Pokémon using favorite resting/playing locations;
- gradual room decoration;
- project objects changing visual phase;
- journals/scrapbooks as UI records;
- benches, fishing spots, game tables and hobby workspaces;
- personal collection displays;
- ambient casual gatherings;
- temporary camps.

Schedules should remain coarse. Do not simulate every NPC minute-by-minute.

## 19. Encounter integration contract

Downtime content should usually avoid combat unless the world actually produces it.

When combat occurs, the downtime premise stays outside battle authority.

Example flow:

1. player chooses evening picnic;
2. world state determines location and participants;
3. a wild-collective or faction state produces a legitimate encounter;
4. AutoPTU resolves battle under its own rules;
5. downtime/world-state layer records interruption and aftermath.

The picnic does not create custom combat bonuses unless PTU/Caelo explicitly authorizes them.

## 20. Full/reduced encounter pattern

### Picnic Site Disturbance

Narrative premise:

A recurring picnic site overlaps with a changing wild-Pokémon route.

Full version:

- moving wild groups;
- optional withdraw/protect-area objectives;
- environmental zones;
- autonomous retreat behavior;
- picnic objects represented as noncombat interactables.

Reduced version:

- migration/route conflict resolved in overworld state;
- picnic objects removed from battle authority;
- if conflict becomes combat, use a static legal arena and normal victory/withdrawal procedures currently supported;
- write encounter result back to wild-collective and routine state.

### Evening Walk Chokepoint

Narrative premise:

A character's regular walk intersects a temporary route obstruction and an unrelated encounter.

Full version:

- route objective;
- dynamic blockers;
- retreat/escort behavior where relevant;
- scenario-aware AI.

Reduced version:

- route choice and obstruction handled in overworld;
- any battle is instantiated separately on a static legal map;
- routine state records that the usual route changed.

### Shoreline Hobby Night

Narrative premise:

A small recurring fishing/sketching gathering encounters unusual activity near the water.

Full version:

- shoreline/water zones;
- current/weather state if rules validate it;
- objective-aware wild behavior;
- optional withdrawal rather than defeat-all.

Reduced version:

- observation and hobby activity remain overworld state;
- no invented fishing mechanics;
- if battle occurs, use existing static Swim/land geometry only where current movement legality supports it.

## 21. Capability dependencies

Mechanically rich downtime encounters may depend on the permanent capability categories.

Current design policy:

- targeting/footprints/range/LoS: use only for actual battle geometry;
- base movement legality: usable for ordinary represented movement;
- complete movement including push/pull/knockback/interception/forced movement: required if a hobby encounter depends on displacement or escort interception;
- core calculations: ordinary verified battle calculations only;
- action economy/initiative: ordinary battle flow;
- full turn/round lifecycle: needed for timed/phase-sensitive versions;
- full stateful damage pipeline: required for complex damage interactions;
- status lifecycle: required for status-driven premises;
- terrain/weather/hazards/zones/reactions: required for dynamic campsite/weather/current/hazard combat;
- move-specific behavior: required for exact Move-driven interactions;
- abilities: required for exact Ability-driven interactions;
- items: required for mechanical item effects;
- Trainer Features/perks: required for exact Feature-driven interactions;
- AI legal-action infrastructure: enough to enumerate legal conventional actions;
- AI tactical policy: required for protect/retreat/escort/objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: required for final overworld/battle presentation integration.

## 22. Rules boundary

This layer cannot invent:

- rest/healing amounts;
- AP refresh;
- daily-frequency refresh;
- Friendship/Loyalty gains;
- Training Feature effects;
- Tutor Move effects;
- camp supplies;
- food buffs;
- crafting yields;
- hobby XP;
- hobby Skill bonuses;
- fishing checks;
- capture modifiers;
- Egg incubation effects;
- mood bonuses;
- battle buffs from relaxation;
- fatigue penalties from skipping leisure.

Those must come from PTU/Caelo and current AutoPTU implementation.

## 23. Canon boundary

Automated generation can propose:

- hobbies;
- routines;
- project opportunities;
- local leisure sites;
- casual social scenes;
- personal collections;
- low-stakes callbacks.

It cannot silently establish a PC's hobby, preference, private journal content, family tradition or emotional attachment.

Those require player-authored evidence or approved canon.
