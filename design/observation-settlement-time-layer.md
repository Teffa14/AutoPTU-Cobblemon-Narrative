# Ouros Observation, Settlement & Time Layer

Status: Proposed systems design. Not established canon.

## Purpose

This layer extends the existing narrative architecture with three systems that were still thin:
- knowledge gained from observing Pokémon and environments;
- settlements that improve through people, services and infrastructure;
- bounded time pressure that changes world state in understandable ways.

The goal is to create more gameplay between `walk somewhere` and `start battle`.

## 1. Observation Events

Observation is a distinct interaction type.

```yaml
observation_event:
  observation_id: null
  observer_ids: []
  location_id: null
  timestamp: null
  species_refs: []
  pokemon_entity_ids: []
  environmental_state_ids: []
  behavior_tags: []
  interaction_tags: []
  evidence_ids: []
  disturbance_level: none
  confidence: provisional
  source_refs: []
```

Possible behavior tags:
- feeding;
- nesting;
- territorial;
- courtship;
- migration;
- play;
- hunting;
- scavenging;
- guarding;
- social hierarchy;
- fear response;
- tool/object use;
- symbiosis;
- competition;
- response to weather;
- response to human activity.

Tags are descriptive narrative metadata. They do not alter species rules.

## 2. Knowledge Records

Do not represent all knowledge as a single numeric meter.

```yaml
knowledge_record:
  subject_id: null
  holder_id: null
  knowledge_type: null
  facts_confirmed: []
  hypotheses: []
  observations: []
  contradiction_ids: []
  confidence: null
  provenance: []
```

Suggested knowledge types:
- species;
- individual_pokemon;
- habitat;
- route;
- dungeon;
- faction;
- historical;
- environmental;
- technical;
- medical;
- mythic.

### Knowledge rule

Knowledge unlocks choices only where the known fact is relevant.

Examples:
- recognizing signs of migration;
- predicting a likely nesting area;
- knowing a safe path through a hazard;
- identifying that two witness claims conflict;
- preparing for an observed behavior pattern;
- qualifying for a research assignment.

Knowledge should not automatically reveal hidden world truth.

## 3. Field Reports

A player can turn observations into institutionally useful reports.

```yaml
field_report:
  report_id: null
  author_ids: []
  institution_id: null
  subject_ids: []
  observation_ids: []
  claim_ids: []
  evidence_quality: null
  review_status: pending
  accepted_facts: []
  disputed_facts: []
  outputs: []
```

Potential outputs:
- research standing;
- new assignment access;
- updated local guidance;
- settlement policy change;
- conservation action;
- new route warning;
- rumor correction;
- new investigation node.

Direct PTU bonuses are out of scope unless separately reviewed.

## 4. Disturbance-aware wildlife

Observation should care whether the player changed the scene.

```yaml
wildlife_observation_context:
  player_distance_band: null
  visible_to_subject: false
  noise_level: low
  food_or_bait_used: false
  move_used: false
  capture_attempted: false
  battle_started: false
```

This allows the same species to generate different observations depending on whether it is calm, alarmed, interacting naturally or responding to player interference.

The system must never infer a species-wide rule from one anecdotal observation without sufficient evidence.

## 5. Research Opportunity Generator

Research jobs should originate from missing or contradictory knowledge.

```yaml
research_opportunity:
  subject_ids: []
  knowledge_gap: null
  conflicting_claim_ids: []
  relevant_locations: []
  suggested_observation_conditions: []
  requester_ids: []
  urgency: low
  mechanics_review_required: false
```

Candidate questions:
- Why has this species changed route?
- Which environmental state triggers this behavior?
- Why are two normally competing species sharing a habitat?
- Is a rumor about an aggressive population actually true?
- Which route is being used at night?
- What disturbed this nesting site?

The system asks questions; it does not pre-author the answer unless world truth already contains one.

## 6. Settlement Capability Model

A settlement is represented by the people and systems currently able to function there.

```yaml
settlement_capability:
  settlement_id: null
  housing: null
  food_supply: null
  medicine: null
  transport: null
  research: null
  training: null
  trade: null
  crafting: null
  communications: null
  public_safety: null
  ecological_health: null
```

Values can be ordinal bands during early implementation.

Capabilities should be calculated from concrete sources such as residents, facilities, supply links and current world state.

## 7. Resident Roles

Important residents can provide settlement functions.

```yaml
resident_role:
  npc_id: null
  settlement_id: null
  role_tags: []
  service_ids: []
  dependencies: []
  personal_goals: []
  relocation_constraints: []
  availability_state: present
```

Examples of role tags:
- healer;
- researcher;
- merchant;
- mechanic;
- cook;
- transporter;
- guide;
- trainer;
- breeder;
- artisan;
- guard;
- administrator;
- performer.

Residents remain characters with motives. They are not interchangeable upgrade tokens.

## 8. Settlement Upgrade Causality

A facility should improve because something happened in the world.

```yaml
settlement_upgrade:
  upgrade_id: null
  settlement_id: null
  sponsor_ids: []
  prerequisite_states: []
  resource_requirements: []
  resident_requirements: []
  completion_events: []
  service_changes: []
  visual_changes: []
  secondary_effects: []
  future_hooks: []
```

Secondary effects matter.

A better road might:
- improve trade;
- increase visitors;
- disturb wildlife;
- attract a competing faction;
- make a distant service viable;
- create a new patrol requirement.

Upgrades should create new state, not only larger numbers.

## 9. Settlement Recovery

Crisis damage can temporarily remove capabilities.

Possible causes:
- flood;
- fire;
- faction attack;
- supply interruption;
- ecological hazard;
- resident departure;
- infrastructure failure;
- dungeon disturbance.

Recovery may require different activity lanes:
- rescue;
- repair;
- gathering;
- negotiation;
- research;
- battle;
- transport;
- social support.

This lets one event produce meaningful multiplayer work without cloning one quest for everyone.

## 10. Regional Clocks

Time pressure should be represented explicitly.

```yaml
regional_clock:
  clock_id: null
  region_ids: []
  label: null
  current_stage: 0
  max_stage: 0
  advance_conditions: []
  delay_conditions: []
  regress_conditions: []
  stage_outputs: {}
  visibility: partial
  evidence_surfaces: []
```

Clock examples:
- wildfire spreading;
- storm approaching;
- migrating herd passing through;
- faction excavation nearing completion;
- bridge deterioration;
- settlement food shortage;
- tournament registration closing;
- rescue survivability decreasing.

## 11. Clock Legibility

Players should usually receive evidence that a clock exists before severe consequences occur.

Evidence surfaces can include:
- visible environmental change;
- NPC warnings;
- maps;
- weather reports;
- damaged infrastructure;
- faction activity;
- Pokémon movement;
- dwindling supplies;
- direct countdown when the fiction supports one.

Hidden clocks are acceptable for mysteries, but they should not be used to punish players for information they had no fair way to discover.

## 12. Action Windows

Some scenarios can use bounded action windows rather than continuous timers.

```yaml
action_window:
  window_id: null
  time_band: morning
  available_activity_slots: null
  travel_costs: {}
  actions_taken: []
  end_of_window_events: []
```

This is useful for expeditions, disasters, festivals or defense scenarios where players need to choose priorities.

Do not make the entire persistent world operate on a restrictive three-actions-per-day loop.

## 13. Maintenance State

Certain player-supported assets need occasional upkeep.

```yaml
maintenance_state:
  asset_id: null
  condition: stable
  dependencies: []
  last_maintained_event_id: null
  degradation_causes: []
  current_problems: []
  failure_outputs: []
```

Candidate assets:
- bridge;
- research outpost;
- safehouse;
- communications relay;
- irrigation system;
- transport service;
- dungeon seal;
- settlement generator;
- habitat barrier.

Maintenance should create occasional decisions, not chores on a rigid timer.

## 14. Base Preparation Scenarios

A temporary expedition or defense base may have preparation choices.

```yaml
base_state:
  base_id: null
  location_id: null
  shelter: null
  supplies: null
  medical_support: null
  communications: null
  defenses: []
  escape_routes: []
  known_threats: []
  unknown_threat_evidence: []
```

Preparation can influence later encounter context, available recovery, route options or evacuation capacity.

No direct combat modifier is valid until mechanically reviewed.

## 15. Causal Regional Problems

Regional arcs should preserve causal chains.

```yaml
regional_problem:
  problem_id: null
  root_causes: []
  intermediate_states: []
  affected_locations: []
  affected_species: []
  affected_factions: []
  affected_services: []
  visible_symptoms: []
  intervention_points: []
  escalation_clocks: []
```

Players can then solve symptoms, causes or both.

Different groups may intervene at different nodes without receiving identical objectives.

## 16. Objective Feasibility Check

Before a procedural mission is surfaced, verify that the requested verbs are executable in the current world.

```yaml
objective_feasibility:
  objective_id: null
  required_locations_reachable: false
  required_npcs_available: false
  required_services_available: false
  required_world_objects_present: false
  required_capabilities_possible: false
  combat_adapter_available: false
  blockers: []
```

This check should prevent quests that refer to unavailable NPCs, sealed locations with no legal access, mechanics not implemented in AutoPTU, or objects the Minecraft layer cannot represent.

## 17. Dense-world preference

Before creating a new location, the generator should check whether an existing place can support the content through changed state.

Selection preferences:
1. existing location with unresolved state;
2. existing location transformed by a world event;
3. existing location newly accessible through capability, faction or infrastructure state;
4. genuinely new location when geography or story requires one.

This increases callbacks and reduces disposable map sprawl.

## 18. Personal Hook Convergence

Shared arcs can begin through different player-specific entrances.

```yaml
hook_convergence:
  shared_problem_id: null
  entry_hooks:
    - character_id: null
      reason: null
      source_event_ids: []
  convergence_nodes: []
```

Examples:
- a researcher notices anomalous migration;
- a courier experiences a blocked road;
- a battler meets displaced aggressive Pokémon;
- a faction member receives a transport-security request.

The same world problem becomes relevant through each character's own life.

## 19. Surprise without premise invalidation

Plot twists may change understanding of events, but generated content should not routinely invalidate the player's selected profession, goals or character concept.

A twist should preferably say:
`the situation was larger/different than you understood`

rather than:
`the campaign you chose does not actually exist`.

This is a narrative safety rule derived from public PTU retrospective experience.

## 20. PTU/Caelo boundary

This layer defines narrative state only.

Observation or field research may call into legal PTU/Caelo Skills and Pokémon capabilities, but this file does not redefine them.

Before using any mechanical resolution, validate against the supplied project sources and AutoPTU implementation:
- Skill names and uses;
- Pokémon capabilities;
- movement/traversal;
- status and hazard rules;
- crafting/item interactions;
- combat actions;
- encounter and capture rules;
- experience/rewards;
- any Caelo-specific rules intentionally adopted by Ouros.

## 21. Implementation priority

Recommended order:
1. observation event schema;
2. knowledge records;
3. field reports;
4. settlement capability calculation;
5. resident roles and service dependencies;
6. regional clocks;
7. settlement upgrades/recovery;
8. objective feasibility check;
9. dense-world location selection;
10. personal hook convergence.

These systems increase meaningful non-combat play while strengthening the world-state pipeline already defined elsewhere in the repository.
