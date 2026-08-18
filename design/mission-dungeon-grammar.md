# Ouros Mission & Dungeon Grammar

Status: Proposed systems design. Not established canon.

## Purpose

This document converts research patterns into implementation-facing structures for quest generation, dungeon authoring and persistent-world progression.

The goal is controlled variety. Ouros should produce adventures that feel causally grounded in the world, mechanically compatible with PTU/Caelo, and different enough from recent player activity to avoid repetitive procedural content.

## Mission assembly pipeline

A mission should be assembled in this order:

1. Read current world state.
2. Select a source of pressure or opportunity.
3. Select a requester or discoverable trigger.
4. Identify affected entities and location.
5. Choose an activity grammar.
6. Add optional complications only if supported by state.
7. Define success, partial-success and failure-forward states.
8. Define Chronicle/world-state outputs.
9. Run mechanics review for anything that enters PTU resolution.
10. Expose the mission through a diegetic surface such as an NPC, board, rumor, message, event or discovered clue.

## Mission sources

Every mission candidate should have a causal source.

```yaml
mission_source:
  type: null
  source_entity_id: null
  source_world_state_ids: []
  evidence: []
```

Candidate source types:
- NPC need
- faction objective
- profession assignment
- ecological disturbance
- settlement state
- discovered clue
- player promise
- unresolved Chronicle event
- dungeon state change
- world event
- rival action
- rumor verified by another fact

A mission without a causal source should normally be rejected.

## Activity grammar

Missions are sequences of activity blocks, not fixed scripts.

Proposed block types:
- TALK
- INVESTIGATE
- TRAVEL
- TRACK
- SEARCH
- EXPLORE
- PUZZLE
- CAPTURE
- BATTLE
- ESCORT
- PROTECT
- RESCUE
- DELIVER
- REPAIR
- GATHER
- NEGOTIATE
- INFILTRATE
- SURVIVE
- OBSERVE
- CHOOSE
- REPORT
- RETURN

A mission can be represented as:

```yaml
blocks:
  - type: TALK
    required: true
  - type: TRAVEL
    required: true
  - type: INVESTIGATE
    required: true
  - type: CHOOSE
    required: true
  - type: BATTLE
    required: false
  - type: RETURN
    required: true
```

The generator should avoid adding BATTLE as a default mandatory block. PTU supports rich tactical combat, but social, exploration, research and Pokémon-capability play should remain valid adventure content.

## Mission experience vector

Track recent activity per player or party.

```yaml
experience_vector:
  combat: 0
  exploration: 0
  social: 0
  investigation: 0
  puzzle: 0
  capture: 0
  traversal: 0
  emotional_stakes: 0
  world_consequence: 0
  novelty: 0
```

Values can be ordinal rather than mathematically precise at first.

Generation rule:
Prefer mission candidates that differ meaningfully from the weighted recent-history vector unless continuity strongly requires repetition.

Example:
If the last three adventures were combat-heavy, a mystery, negotiation, research expedition or environmental traversal receives additional selection weight.

## Request surfaces

A request can arrive through different in-world channels:
- settlement job board
- guild/profession office
- personal NPC request
- faction contact
- emergency event
- rumor
- discovered object
- radio/news equivalent if canon supports it
- recurring rival
- automated infrastructure alert if setting supports it

The surface affects tone and trust but should not define mission mechanics.

## Profession progression

Profession systems can provide an alternative progression spine.

```yaml
profession_state:
  profession_id: null
  rank: 0
  trust: 0
  completed_categories: {}
  failed_categories: {}
  known_contacts: []
  permissions: []
  sensitive_mission_access: []
```

Rank may influence access to jobs, information and locations. It should not automatically grant PTU mechanical bonuses unless separately designed and reviewed.

## Player-seed intake

Player-authored events, rumors and subplots can become candidate material.

```yaml
player_seed:
  seed_id: null
  origin_event_id: null
  creator_character_id: null
  entities: []
  claims: []
  unresolved_questions: []
  reuse_scope: world
  status: candidate
```

Rules:
- preserve provenance;
- never assert another PC's thoughts, motives or future actions;
- treat player claims as beliefs until world canon confirms them;
- human review may promote high-impact seeds into authored arcs.

## Dungeon grammar

A dungeon is a persistent location state machine, not only a sequence of rooms.

Minimum layers:

### Layer A — Navigation

Tracks:
- entrances
- exits
- shortcuts
- vertical transitions
- locked or capability-gated paths
- one-way paths
- temporary closures

### Layer B — Environment

Tracks:
- terrain identity
- weather or atmospheric state
- hazards
- visibility
- machinery
- water/lava/ice/vegetation or other physical states
- PTU-relevant battlefield tags awaiting rules validation

### Layer C — Interaction

Tracks:
- puzzles
- switches
- movable objects
- clues
- containers
- repairable structures
- alternate capability solutions

### Layer D — Ecology / Occupation

Tracks:
- wild Pokémon populations
- nesting or migration
- faction camps
- NPC presence
- boss/guardian state
- resource extraction

### Layer E — Chronicle State

Tracks what previous expeditions changed:
- opened passages
- destroyed structures
- solved mechanisms
- rescued inhabitants
- defeated or displaced agents
- removed resources
- discovered secrets
- placed markers

## Puzzle contract

Every puzzle definition should include recovery semantics.

```yaml
puzzle:
  puzzle_id: null
  observable_state: []
  interactables: []
  goal_state: []
  reset_method: null
  hint_sources: []
  alternate_solutions: []
  capability_hooks: []
  failure_effects: []
  combat_interaction: none
```

Design rules:
- Avoid permanent softlocks.
- If experimentation can make the puzzle unwinnable, provide reset behavior.
- Hints should exist in-world where possible.
- PTU Pokémon capabilities can offer alternate solutions only when the Pokémon actually has the relevant capability.
- A bypass can create a different consequence rather than simply skipping content.

## Dungeon revisit states

Suggested state stages:
- UNKNOWN
- DISCOVERED
- ACTIVE
- PARTIALLY_EXPLORED
- CLEARED
- OCCUPIED
- CHANGED
- DORMANT
- REACTIVATED

A cleared dungeon can later transition to OCCUPIED or CHANGED based on world events. The original boss should not simply respawn without a causal reason.

## Failure-forward model

Failure should generally create a new state rather than delete progress.

Possible outputs:
- requester loses trust
- rival arrives first
- faction gains territory
- target escapes
- hazard worsens
- reward decreases
- alternate clue becomes necessary
- rescue requires a second expedition
- location access changes
- time-sensitive event advances

Some outcomes can be hard failures when the fiction demands it, but the narrative system should not default to replaying the same mission unchanged.

## NPC operational memory

NPC memory should prioritize actionable facts.

```yaml
npc_memory:
  npc_id: null
  current_location_id: null
  current_goal: null
  relationship_edges: []
  obligations: []
  grievances: []
  witnessed_events: []
  secrets_known: []
  promises: []
  last_interaction_event_id: null
```

Generated dialogue should query these facts rather than inventing a full biography every time.

## PTU / Caelo mechanics boundary

The grammar describes narrative shape only.

Before BATTLE, CAPTURE, hazardous traversal or capability-dependent resolution becomes executable content, validate against the supplied project sources and the actual AutoPTU implementation.

Required checks may include:
- legal Pokémon species/forms;
- levels and encounter balance;
- legal Moves and Abilities;
- movement capabilities;
- Naturewalk and related terrain interactions;
- environmental status effects;
- initiative and action economy;
- capture rules;
- rewards and experience;
- Caelo-specific homebrew intended for Ouros.

## Minecraft / Cobblemon mapping

Mission and dungeon state should expose simple world-facing events:
- spawn NPC
- despawn NPC
- enable dialogue branch
- open/close passage
- set block/structure variant
- change encounter population profile
- add/remove sign, notice or marker
- enable dungeon entrance
- alter faction presence
- trigger AutoPTU encounter request

This document intentionally avoids committing to a specific mod API until implementation work begins.
