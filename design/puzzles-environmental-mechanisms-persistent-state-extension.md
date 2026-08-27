# Puzzles & Environmental Mechanisms Persistent-State Extension

Status: proposed systems design. Not established Ouros canon.

Date introduced: 2026-08-27, Pass 78.

## Purpose

`design/mission-dungeon-grammar.md` already defines a minimal puzzle contract. This extension gives puzzles and environmental mechanisms durable state so they can survive revisits, repairs, bypasses, partial completion and later world events without becoming disposable reset-on-entry minigames.

The layer owns puzzle/mechanism semantics, transition history, clue provenance, reset behavior, bypass records and feedback requirements. It does not take authority away from Travel, Cartography, Archaeology, Technology, Maintenance, Digital Systems, Ecology, Credentials or AutoPTU.

Core principle:

A puzzle is a stateful part of a place. The player should be able to observe what exists, act on it, perceive what changed and return later to a world that remembers the result.

## 1. Puzzle system record

```yaml
puzzle_system:
  puzzle_id: null
  location_id: null
  site_or_facility_ref: null
  status: ACTIVE
  semantic_purpose: null
  current_state_id: null
  mechanism_ids: []
  clue_ids: []
  dependency_ids: []
  output_refs: []
  reset_policy_id: null
  bypass_policy_id: null
  feedback_contract_id: null
  solution_history: []
  revision_history: []
  world_truth_refs: []
  canon_status: proposed
```

Suggested statuses:

- DORMANT
- ACTIVE
- PARTIALLY_SOLVED
- SOLVED
- BYPASSED
- DISABLED
- DAMAGED
- UNDER_REPAIR
- RECONFIGURED
- UNKNOWN

`SOLVED` should describe a current authored state, not an eternal property. A mechanism can later be repaired, reset, altered or disconnected for a causal reason.

## 2. Mechanism instance

A mechanism is an exact persistent object or logical control surface.

```yaml
mechanism:
  mechanism_id: null
  puzzle_id: null
  object_or_structure_ref: null
  zone_id: null
  mechanism_type: null
  observable_state: null
  semantic_state: null
  allowed_interaction_refs: []
  output_refs: []
  reversible: null
  current_condition_ref: null
  authority_owner_ref: null
  last_transition_id: null
```

Possible descriptive types:

- SWITCH
- LEVER
- ROTARY_CONTROL
- PRESSURE_PLATE
- MOVABLE_OBJECT
- GATE
- DOOR
- VALVE
- PUMP
- COUNTERWEIGHT
- MIRROR_OR_LIGHT_ELEMENT
- SYMBOL_PANEL
- MANUAL_OVERRIDE
- RESET_CONTROL
- REMOTE_CONTROL
- SEQUENCE_READER
- MECHANICAL_LOCK
- DIGITAL_INTERFACE
- NATURAL_ENVIRONMENTAL_ELEMENT

These labels do not create mechanical behavior by themselves.

## 3. Puzzle state snapshot

Some mechanisms are history-dependent. Store enough information to reconstruct why the current configuration exists.

```yaml
puzzle_state:
  state_id: null
  puzzle_id: null
  mechanism_states: {}
  solved_module_ids: []
  active_output_refs: []
  blocked_output_refs: []
  persistent_world_changes: []
  last_input_sequence_refs: []
  reached_at_event_id: null
  reached_by_actor_ids: []
  verification_state: CONFIRMED
```

A current switch arrangement alone may be insufficient if earlier inputs affected outputs that were not later overwritten.

## 4. Transition record

Every accepted semantic change should be traceable.

```yaml
puzzle_transition:
  transition_id: null
  puzzle_id: null
  from_state_id: null
  input_ref: null
  actor_ids: []
  validation_refs: []
  accepted: null
  to_state_id: null
  output_events: []
  world_state_writes: []
  feedback_event_ids: []
  timestamp_ref: null
  provenance_refs: []
```

Rejected inputs may also create feedback records when useful, but should not spam Chronicle history for every accidental click.

## 5. Dependency graph

Large puzzles can be non-linear.

```yaml
puzzle_dependency:
  dependency_id: null
  source_module_or_state_ref: null
  target_module_or_output_ref: null
  relation: null
  required_state_refs: []
  optional: false
```

Candidate relations:

- ENABLES
- DISABLES
- UNLOCKS
- REVEALS
- POWERS
- ROUTES_TO
- CONTRIBUTES_TO_AGGREGATE
- REQUIRES
- EXCLUDES
- ALTERNATIVE_TO

Independent modules should remain independently solved unless the authored mechanism has a causal reset that affects them.

## 6. Clue provenance

A puzzle clue is an observation or information packet, not an omniscient answer flag.

```yaml
puzzle_clue:
  clue_id: null
  puzzle_id: null
  source_ref: null
  observation_ref: null
  available_at_state_refs: []
  supports_inference_refs: []
  does_not_establish: []
  language_or_symbol_ref: null
  actor_knowledge_requirements: []
  reliability_notes: null
```

Possible clue sources:

- physical wear;
- diagrams;
- maintenance notes;
- repeated motifs;
- color or shape grouping;
- sound;
- light;
- sightline;
- old survey;
- public sign;
- witness account;
- previous configuration photograph;
- actor demonstration;
- environmental consequence.

A historical manual can be obsolete without being false about the configuration that existed when it was written.

## 7. Feedback contract

Every important transition must be perceptible enough to verify.

```yaml
puzzle_feedback_contract:
  feedback_contract_id: null
  accepted_input_feedback: []
  rejected_input_feedback: []
  state_change_feedback: []
  completion_feedback: []
  remote_output_feedback: []
  accessibility_refs: []
  replay_or_recheck_method: null
```

Design requirements:

- an accepted control should show or sound that it moved or registered;
- a rejected interaction should explain failure through an appropriate local cue when possible;
- a changed passage should have a discoverable cue even if it is off-camera;
- completion should be distinguishable from another intermediate state;
- important information should not depend exclusively on one sensory channel when the setting can plausibly provide alternatives;
- a player should be able to re-check the current state without intentionally breaking the solution.

A puzzle may hide the consequence's exact location. It should not hide whether anything happened.

## 8. Reset policy

Reset is part of world logic.

```yaml
puzzle_reset_policy:
  reset_policy_id: null
  puzzle_id: null
  reset_type: null
  trigger_refs: []
  target_state_id: null
  preserves_module_ids: []
  clears_module_ids: []
  requires_authorization_ref: null
  creates_world_event: false
  consequence_refs: []
```

Candidate reset types:

- NONE
- MANUAL_LOCAL
- MANUAL_MASTER
- AUTHORIZED_SERVICE
- ROOM_REENTRY
- SITE_REENTRY
- TIMED
- POWER_CYCLE
- REPAIR_RECONFIGURATION
- WORLD_EVENT

Do not use automatic reset-on-reload merely because it is easy to implement if the fiction says the mechanism physically changed.

## 9. Anti-softlock requirement

Before implementation, author a state-graph review.

```yaml
softlock_review:
  puzzle_id: null
  reachable_states_checked: false
  unrecoverable_states: []
  reset_paths: []
  alternate_progression_paths: []
  destructive_bypass_paths: []
  intentional_hard_lock_refs: []
  review_complete: false
```

A permanent hard lock can exist only when it is an intentional world consequence and the larger campaign has a reviewed continuation path. Accidental unwinnable states fail review.

## 10. Bypass policy

Alternate solutions should be explicit rather than improvised exceptions.

```yaml
puzzle_bypass:
  bypass_id: null
  puzzle_id: null
  method_type: null
  requirement_refs: []
  capability_validation_refs: []
  resulting_state_id: null
  physical_trace_refs: []
  consequence_refs: []
  reversible: null
```

Possible methods:

- ALTERNATE_ROUTE
- AUTHORIZED_OVERRIDE
- REPAIR
- DISASSEMBLY
- CAPABILITY_ASSISTED
- DESTRUCTIVE_BREACH
- TEMPORARY_WORKAROUND
- EXTERNAL_POWER_OR_SERVICE

A bypass should often produce a different state rather than silently mark the canonical solution as completed.

Example:

A forced door can become `BYPASSED/DAMAGED`, leaving a Maintenance record and changing later access, while a properly operated mechanism becomes `SOLVED/OPERABLE`.

## 11. Pokémon capability solutions

Pokémon can participate when the exact individual has governing evidence for the required action.

```yaml
capability_solution:
  solution_id: null
  puzzle_id: null
  actor_id: null
  governing_rule_refs: []
  authoritative_capability_refs: []
  required_world_conditions: []
  validated: false
  resulting_transition_ref: null
```

Forbidden shortcuts include:

- species stereotype;
- elemental type alone;
- visual size alone;
- Move name interpreted beyond its rules;
- Cobblemon animation treated as a capability grant.

If the rule is uncertain, leave the solution proposed and unresolved.

## 12. Actor knowledge versus player knowledge

A player may recognize a franchise motif that the character has never encountered. Ouros should not require external trivia as the sole solution path.

When knowledge matters, provide at least one in-world path through:

- observed clues;
- records;
- local expertise;
- research;
- translation;
- prior visits;
- legitimate character knowledge.

A Skill check, Feature or other PTU mechanic cannot be invented as a generic “solve puzzle” button. Exact checks require source validation.

## 13. Multi-room and remote mechanisms

A control may change another zone.

Store the causal edge explicitly:

```yaml
remote_output:
  source_mechanism_id: null
  target_zone_id: null
  target_object_ref: null
  output_state: null
  feedback_refs: []
  map_update_ref: null
```

This enables:

- central gatehouses;
- water routing;
- power distribution;
- lifts;
- rotating bridges;
- multiple sealed wings;
- remote shutters;
- distributed temple/ruin modules.

Technology/Energy Infrastructure owns operational network truth when the mechanism is part of an active utility. This layer only owns the puzzle-facing state machine and interaction history.

## 14. Aggregate completion

Independent modules may contribute to a larger state.

```yaml
aggregate_puzzle_state:
  aggregate_id: null
  puzzle_id: null
  contributor_module_ids: []
  completed_module_ids: []
  threshold_policy: null
  active_site_outputs: []
  completion_event_id: null
```

Possible policies:

- ALL_REQUIRED
- ANY_ONE
- SPECIFIC_COMBINATION
- ORDER_INDEPENDENT_ALL
- CHOICE_LOCKS_OTHER_PATHS

Do not invent mathematical combination puzzles solely to create complexity. The relation should be learnable from the place or its records.

## 15. Persistent environmental outputs

A puzzle can change:

- route topology;
- water routing;
- bridge orientation;
- lift availability;
- lighting;
- ventilation presentation;
- access doors;
- machinery state;
- public route availability;
- visible habitat configuration;
- soundscape;
- signage state;
- maintenance needs;
- ecological disturbance;
- archival interpretation.

The affected system owns the downstream consequence.

For example, a mechanism can emit `route_output_changed`; Travel decides whether the route is actually traversable. If a pump restarts, Technology or Maintenance owns operational service state. If habitat changes, Ecology records the observation and resulting state.

## 16. Revisit and reconfiguration

Puzzle history should support later changes.

```yaml
puzzle_revision:
  revision_id: null
  puzzle_id: null
  cause_event_id: null
  previous_configuration_ref: null
  new_configuration_ref: null
  changed_mechanism_ids: []
  old_clues_affected: []
  new_clue_refs: []
  public_information_refs: []
```

Possible causes:

- repair;
- vandalism or damage when canonically established;
- restoration;
- ecological occupation;
- institutional retrofit;
- storm/flood event;
- archaeological intervention;
- deliberate security reconfiguration;
- power/infrastructure change.

An old guide can therefore become stale while remaining historically valid.

## 17. Puzzle history and public knowledge

Chronicle/public-memory integration can retain:

- first documented solution;
- known bypasses;
- repairs;
- warnings;
- public diagrams;
- popular but outdated explanations;
- a previous inaccessible wing;
- a famous accidental discovery.

Public knowledge never overwrites current physical truth. The player may arrive with a correct description of last year's configuration and still need to inspect today's mechanism.

## 18. Noncombat puzzle implementation

Pure overworld puzzle logic can advance before the tactical adapter exists.

The authoritative flow should be:

`Ouros puzzle state -> reviewed world-state transition -> Minecraft/Cobblemon presentation`

Minecraft/Cobblemon can collect an interaction request and render the result. The semantic transition should be server-owned and reconstructable after reconnect/reload.

Safe reuse can include:

- block/structure variants;
- doors and visible mechanisms;
- sound events;
- particles;
- entity animation;
- interaction UI;
- networking;
- collision/geometry as observations;
- persistent visual props.

A client-only piston movement or redstone state must not silently become the canonical record if Ouros cannot reconstruct it.

## 19. Battle boundary

Puzzle state is world state. Once a mechanism changes tactical facts, AutoPTU must own those facts.

Examples requiring battle capability review:

- rotating floor changes legal tactical tiles;
- gate opens/closes LoS during a round;
- current pushes combatants;
- switch creates damaging zone;
- puzzle applies status;
- delayed mechanism triggers at phase boundary;
- object can be activated using battle action economy;
- AI reasons about operating or defending controls.

Minecraft/Cobblemon must not apply these effects independently.

## 20. Capability mapping for puzzle-battle hybrids

Use the permanent categories exactly.

A static arena selected after an overworld puzzle can often use only the capabilities required by the ordinary battle itself.

Dynamic push/pull, conveyor movement, rotating platforms that relocate actors or current-driven displacement require:

- complete movement including push/pull/knockback/interception/forced movement.

Active floor effects, weather-linked machinery, damage zones, reaction traps or changing battlefield environment require:

- terrain/weather/hazards/zones/reactions;
- full turn/round lifecycle when timing matters;
- full stateful damage pipeline or status lifecycle when effects cause damage/status.

Mechanically activated objects may additionally require:

- action economy/initiative;
- relevant item/move/ability/Trainer Feature families when the interaction uses those rules;
- adapter/playback support.

Autonomous opponents that understand puzzle objectives require:

- AI legal-action infrastructure;
- AI tactical policy.

## 21. Reduced-version doctrine

When full tactical mechanism support is unavailable, preserve the premise by moving the mechanism decision outside battle.

Approved patterns include:

- solve the puzzle first, then freeze a static reviewed arena;
- choose one of several static arena variants based on overworld state;
- split a dynamic encounter into ordinary battles separated by mechanism checkpoints;
- remove noncombatants and interactable objectives from tactical state;
- finish the battle, then resume puzzle operation as a separate world interaction.

Forbidden substitutes include:

- Minecraft directly damaging combatants when a trap fires;
- teleporting AutoPTU actors because a piston moved visually;
- Cobblemon battle state deciding whether a gate blocks targeting;
- arbitrary status application from block contact;
- hidden scripted extra turns to simulate machinery.

## 22. Encounter concept — Rotating Platform Interruption

Full version:

A large mechanism rotates sections of the arena during a conflict. Legal paths, cover and access change as the system advances. If rotation physically relocates actors, the encounter also requires forced-movement and landing/collision legality.

Required families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when actors relocate;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- terrain/weather/hazards/zones/reactions for dynamic battlefield topology/environment rules;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks as used;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

Operate the platform before battle. The chosen orientation becomes one static reviewed arena. It remains mechanically fixed until AutoPTU finishes resolution. Afterward the world mechanism may operate again.

## 23. Encounter concept — Gatehouse Override Under Pressure

Full version:

Participants must reach and activate controls while opponents can contest access. Gate states alter routes and LoS during the same tactical encounter.

Key dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- terrain/weather/hazards/zones/reactions for dynamic gate/zone state;
- complete movement if interception/forced relocation is used;
- AI legal-action infrastructure;
- AI tactical policy for objective-aware opponents;
- adapter/playback;
- other partial combat families as required by selected rosters.

Reduced version:

Resolve controls in the overworld or at explicit checkpoints between ordinary battles. Each gate configuration maps to a static arena. No gate changes tactical legality mid-battle.

## 24. Noncombat concept — Three Chambers, Any Order

Three independent rooms each establish one part of a central mechanism. Each completed room changes a persistent ambient cue near the center. The rooms can be solved in any order.

This can be implemented as world-state logic without new combat capability families if none of the solution paths invoke unverified PTU mechanics.

## 25. Anti-false-completion rules

- one functioning switch does not prove a robust puzzle framework;
- redstone can animate a mechanism but does not own Ouros semantic state;
- a block collision map does not prove tactical terrain support;
- a visible moving platform does not prove forced movement;
- an environmental sound does not prove a status or hazard;
- a Cobblemon Pokémon animation does not grant a field capability;
- a solved puzzle state cannot be inferred from an open client-side door alone;
- a successful battle does not automatically solve, repair or reset the mechanism;
- external franchise knowledge cannot be the sole mandatory clue path;
- a wrong puzzle input cannot mutate PTU HP/status without authoritative mechanical support.

## 26. Canon boundary

This extension defines architecture only. It does not establish:

- which Ouros ruins contain mechanisms;
- what civilization or institution built them;
- which technologies exist regionally;
- which Pokémon species are associated with them;
- whether any mechanism has supernatural origin;
- who owns, maintains or controls access;
- which exact PTU/Caelo capabilities can operate them;
- any canonical puzzle answer.

Those decisions remain proposed until reviewed.
