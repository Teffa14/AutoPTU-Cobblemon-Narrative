# Ouros World Agency Layer

Status: Proposed systems design. Not established canon.

## Purpose

The existing Ouros architecture already defines world state, Chronicle memory, reputation, ecological causality, mission assembly, dungeon state and failure-forward behavior.

This document adds the missing agency layer: systems that let factions, NPCs, important Pokémon, battle environments and investigations evolve without waiting for a player to activate a scripted quest.

The goal is a world that can act, remember, hide information, react unevenly, and create new situations from prior state.

## 1. World Pulse

A World Pulse is a bounded simulation step for narrative actors.

It does not need to run every Minecraft tick. It can run after important events, on a game-day boundary, on server maintenance intervals, or when a region is loaded for narrative evaluation.

Suggested pipeline:

```yaml
world_pulse:
  pulse_id: null
  timestamp: null
  affected_regions: []
  candidate_actors: []
  actions_evaluated: []
  actions_applied: []
  visible_consequences: []
  rumor_outputs: []
  chronicle_events: []
```

Pulse rules:

1. Read current canonical state.
2. Determine which actors have active goals.
3. Filter actions by resources, reach, knowledge and current blockers.
4. Select only a small number of meaningful changes.
5. Apply world-state consequences.
6. Generate evidence and rumors only where someone could plausibly notice the change.
7. Record provenance.

The system should prefer legible consequences over invisible simulation complexity.

## 2. Faction Actor Model

A faction needs more than a reputation score.

```yaml
faction:
  faction_id: null
  status: active
  public_identity: null
  doctrines: []
  public_goals: []
  hidden_goals: []
  assets: []
  services: []
  constituencies: []
  rivals: []
  allies: []
  internal_groups: []
  known_locations: []
  active_fronts: []
  resource_state: {}
  public_reputation: {}
  player_relationships: {}
```

### Design principle

A credible faction should usually have at least one reason ordinary people tolerate, need, respect or join it.

Possible benefits:
- protection;
- research;
- transport;
- employment;
- conservation;
- medical support;
- infrastructure;
- entertainment;
- training;
- trade;
- disaster response;
- political representation.

A faction can cause harm while still supplying something real. This creates conflicts that support negotiation and reform rather than only extermination.

## 3. Faction Fronts 2.0

The existing proposal introduces faction fronts as visible pressures. This layer formalizes them.

```yaml
faction_front:
  front_id: null
  faction_id: null
  location_ids: []
  goal: null
  method_tags: []
  stage: 0
  max_stage: 0
  momentum: 0
  resource_cost: {}
  prerequisites: []
  blockers: []
  opposition_ids: []
  public_visibility: low
  evidence_outputs: []
  state_changes_by_stage: {}
  completion_state: null
  collapse_states: []
```

Possible front types:
- expand service;
- recruit;
- investigate;
- excavate;
- restore habitat;
- exploit resource;
- monopolize trade;
- smuggle;
- patrol;
- occupy;
- influence election or civic decision;
- build infrastructure;
- suppress information;
- sponsor sport/contest activity;
- establish research presence.

A front can advance, stall, retreat, transform, split or finish.

Ignoring a front must not always advance it. Resource shortages, rival action, ecological problems, internal conflict or public resistance can also alter its course.

## 4. Influence Map

Binary territory ownership is too coarse for most Ouros content.

Use layered influence.

```yaml
location_influence:
  location_id: null
  faction_id: null
  presence: 0
  legitimacy: 0
  infrastructure: 0
  intelligence: 0
  economic_reach: 0
  security_reach: 0
  local_support: 0
```

These values can be ordinal bands rather than exact percentages.

Example consequences:
- low presence: occasional contacts or rumors;
- moderate presence: recurring NPCs, jobs, supplies, scouts;
- strong infrastructure: services or visible buildings;
- strong intelligence: faction hears about local events faster;
- strong security: patrols, checkpoints or protection;
- low legitimacy + high security: coercive control rather than accepted authority.

A single location can contain multiple factions with different types of influence.

## 5. Actor Knowledge Boundary

Every intelligent actor should operate from its own knowledge state.

```yaml
actor_knowledge:
  actor_id: null
  confirmed_facts: []
  observed_events: []
  received_claims: []
  inferences: []
  false_beliefs: []
  secrets: []
  last_updated: null
```

### Hard rule

Narrative AI and battle AI must not silently use `world_truth` as actor knowledge.

NPCs may be wrong.
Factions may act on propaganda.
Rivals may misread player strategy.
A witness may only know part of an event.

This rule is necessary for mysteries, deception, surprise and fair recurring rivals.

## 6. Evidence Graph

Investigation should operate on explicit evidence rather than arbitrary dialogue unlocks.

```yaml
evidence:
  evidence_id: null
  evidence_type: physical
  source_location_id: null
  source_actor_id: null
  observed_by: []
  supports_claim_ids: []
  weakens_claim_ids: []
  authenticity: unknown
  accessibility: public
  discoverability_hooks: []
  lost_or_destroyed: false
```

```yaml
claim:
  claim_id: null
  statement: null
  truth_status: unknown
  claimant_ids: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  required_revelation: false
```

### Mystery robustness

For any revelation required to continue a major investigation, author several independent paths to it.

Those paths may include:
- witness testimony;
- physical trace;
- Pokémon behavior;
- records;
- environmental evidence;
- faction activity;
- surveillance or observation;
- a related location;
- a second incident.

Do not require one successful Skill Check to preserve the entire arc.

PTU Skill Checks can determine quality, speed, risk, interpretation or extra information while the scenario retains alternate leads.

## 7. Investigation Nodes

A node is any place, person, event, organization or evidence cluster that can lead to other nodes.

```yaml
investigation_node:
  node_id: null
  node_type: location
  discoverable_from: []
  clues_out: []
  facts_available: []
  blockers: []
  risks: []
  faction_interest: []
  world_state_dependencies: []
```

The generator should build networks instead of linear clue chains.

A dead-end lead can exist when other viable leads remain. Dead ends can create atmosphere, reveal character, expose faction behavior or set traps without collapsing progression.

## 8. Arena State Machine

The current location model gains a battle-facing state layer.

```yaml
arena_state:
  arena_id: null
  source_location_id: null
  base_environment: null
  active_state: null
  temporary_overlays: []
  interactables: []
  hazards: []
  legal_transitions: []
  discovered_interactions: []
  persistent_outputs: []
```

### Transition object

```yaml
arena_transition:
  transition_id: null
  from_state: null
  to_state: null
  trigger_type: null
  required_rule_reference: null
  consumes_object: false
  reversible: false
  duration: null
```

Triggers can eventually include:
- legal Move;
- legal Ability;
- legal Capability;
- battlefield object;
- environmental event;
- scripted phase change.

No transition becomes executable until PTU/Caelo legality and AutoPTU support are verified.

## 9. Encounter Objectives

Combat should support objectives beyond elimination when the fiction calls for it.

Narrative objective types:
- DEFEAT;
- SURVIVE;
- ESCAPE;
- PROTECT;
- HOLD_ZONE;
- REACH_LOCATION;
- DISABLE_OBJECT;
- ACTIVATE_OBJECT;
- INTERRUPT;
- CAPTURE_TARGET;
- RESCUE_TARGET;
- RECOVER_ITEM;
- DELAY_ENEMY;
- FORCE_RETREAT;
- NEGOTIATE_UNDER_PRESSURE.

These are narrative categories. They do not define unreviewed combat rules.

```yaml
encounter_objective:
  objective_type: null
  success_condition: null
  partial_success_conditions: []
  failure_condition: null
  time_pressure: null
  protected_entities: []
  objective_objects: []
  mechanics_review_required: true
```

## 10. Boss Identity Stack

A boss encounter should derive identity from more than HP and damage.

```yaml
boss_encounter:
  boss_entity_ids: []
  narrative_goal: null
  player_goal: null
  arena_state_id: null
  objective_ids: []
  phase_triggers: []
  reinforcement_rules: []
  retreat_logic: []
  surrender_logic: []
  persistent_consequences: []
```

Boss uniqueness can come from:
- objective pressure;
- arena interaction;
- allied units;
- mobility;
- information asymmetry;
- protection duties;
- changing terrain;
- faction reinforcements;
- moral or social stakes;
- escape conditions.

Stat inflation should never be the only identity tool.

## 11. Persistent Pokémon Entity Memory

Story-significant Pokémon can exist as persistent world entities instead of disposable encounter instances.

```yaml
pokemon_entity_memory:
  pokemon_entity_id: null
  species_ref: null
  trainer_or_group_id: null
  known_names: []
  home_locations: []
  relationship_edges: []
  fears: []
  comforts: []
  learned_social_behaviors: []
  witnessed_events: []
  unresolved_needs: []
  adaptation_milestones: []
  last_seen_event_id: null
```

This layer is narrative. Legal stats, Moves, Abilities and capabilities remain in PTU/AutoPTU data.

## 12. Pokémon Bond Arcs

A bond arc is a sequence of state changes around one persistent Pokémon.

Potential use cases:
- rescue recovery;
- displacement after habitat loss;
- rebuilding trust after mistreatment;
- adapting to a settlement;
- learning to cooperate with a new Trainer;
- recurring wild Pokémon relationship;
- recovering from a frightening event;
- social conflict within a Pokémon group.

```yaml
pokemon_bond_arc:
  bond_arc_id: null
  pokemon_entity_id: null
  participants: []
  starting_state: []
  milestones: []
  interaction_types: []
  setbacks: []
  completion_states: []
  future_hooks: []
```

Progress should be event-driven rather than a generic hidden number whenever possible.

Examples of meaningful milestones:
- accepts food from a specific character;
- chooses to remain nearby;
- enters battle voluntarily;
- returns after being released;
- tolerates a feared environment;
- initiates interaction;
- protects another entity;
- accepts a new home.

Exact loyalty or mechanical bonuses require separate rules review.

## 13. Relationship Effects

Existing multidimensional reputation is extended with explicit consequences.

```yaml
relationship_effect:
  relationship_id: null
  trigger_state: []
  effect_type: null
  effect_payload: {}
  reversible: true
  visibility: hidden
```

Effect types may include:
- private_information;
- job_offer;
- faction_introduction;
- support_presence;
- negotiation_modifier_candidate;
- public_statement;
- refusal;
- rival_escalation;
- rescue_attempt;
- gift_or_service_candidate.

Anything with direct PTU modifiers remains a candidate until mechanics approval.

## 14. Participation Lanes

Ouros multiplayer should allow different motivations to coexist.

```yaml
participation_profile:
  character_id: null
  recent_lanes: []
  preferred_lanes: []
  avoided_lanes: []
  active_commitments: []
```

Candidate lanes:
- battle;
- capture;
- social;
- investigation;
- exploration;
- profession;
- faction;
- contest;
- research;
- crafting/economy;
- dungeon;
- authored_main_arc.

This profile should guide recommendations, not lock players out of other activities.

Shared-world events can intentionally intersect lanes. A research player might discover the clue that creates a raid for combat-focused players; a contest celebrity might gain access to an NPC needed by an investigation group.

## 15. Structured Transcript Ingestion

Future Discord/RP ingestion should produce three layers:

### Raw provenance
- original message IDs;
- author IDs;
- timestamps;
- channel/thread IDs;
- attachments;
- raw text.

### Extracted scene state
- participants;
- location;
- declared actions;
- observed results;
- claims;
- discoveries;
- relationships;
- unresolved questions.

### Canonized event state
Only validated facts become Chronicle/world-state events.

The system must preserve uncertainty when a transcript contains IC lies, jokes, hypotheses or conflicting accounts.

## 16. Safety against runaway simulation

Autonomous world actors can create noise if every faction changes every pulse.

Use a narrative budget.

```yaml
world_pulse_budget:
  max_major_changes: 2
  max_minor_changes: 5
  max_new_hooks: 3
  max_rumors: 5
```

Exact values are placeholders.

Selection priority should consider:
- proximity to active players;
- unresolved player consequences;
- urgency;
- faction momentum;
- narrative novelty;
- whether the change can be represented in Minecraft;
- whether the result creates understandable player-facing evidence.

## 17. PTU/Caelo mechanical boundary

This document introduces state and orchestration concepts only.

Before any generated encounter becomes executable, verify:
- legal species/form;
- level and encounter balance;
- Moves and Abilities;
- capabilities;
- movement;
- initiative/action economy;
- terrain interaction;
- status effects;
- capture rules;
- boss/raid reward logic;
- any Caelo-specific homebrew intentionally retained by Ouros;
- actual AutoPTU engine support.

Mystery content must also respect character knowledge. Capabilities such as tracking, aura reading, special senses or terrain movement may provide valid investigation options only when the involved character or Pokémon actually has them.

## 18. Implementation priority

Recommended order:

1. actor knowledge boundary;
2. evidence/claim graph;
3. faction fronts and World Pulse;
4. influence map;
5. encounter-objective schema;
6. arena state machine;
7. persistent Pokémon entity memory;
8. bond arcs;
9. relationship effects;
10. participation-lane recommendation.

This order gives Ouros better narrative correctness before adding more generative volume.
