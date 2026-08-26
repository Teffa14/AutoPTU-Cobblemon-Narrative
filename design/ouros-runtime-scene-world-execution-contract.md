# Ouros Runtime Scene & World Execution Contract

Status: PROPOSED IMPLEMENTATION ARCHITECTURE / NON-CANON
Pass: 182
Date: 2026-08-26

## Purpose

This contract converts approved Ouros world state and encounter design into server-executable scene state without moving PTU authority into Minecraft.

Existing narrative layers answer what exists, what changed and what an encounter means. This layer answers how a Minecraft/Cobblemon server materializes that truth, accepts player interaction, advances a scene, hands a battle to AutoPTU and persists the result safely.

This is intentionally below `design/ouros-narrative-architecture.md`, `design/encounter-implementation-contracts.md` and domain-specific systems such as `design/puzzles-dungeons-challenge-state-layer.md`.

## Ownership boundary

### Ouros runtime owns

- stable world-event and scene-instance identity;
- persistent actor identity references;
- authored trigger predicates;
- scene-node legality;
- server-authoritative interaction ordering;
- world-state reads/writes;
- actor materialization intent;
- dialogue-state selection;
- scene scheduling and offline progression policy;
- battle-request creation;
- battle-result ingestion according to an explicit contract;
- Chronicle outputs;
- idempotency and recovery state.

### AutoPTU-Java owns

- legal combatants and battle state once a battle is instantiated;
- PTU targeting, movement, calculations, action economy and every other implemented battle rule;
- AI legal choices and, when implemented, tactical selection;
- deterministic authoritative battle state changes;
- semantic battle events and final battle result.

### Minecraft/Cobblemon/Craftics adapter owns

- binding stable Ouros/AutoPTU IDs to current runtime entities;
- block/entity/UI presentation;
- receiving player interaction intent;
- materializing and dematerializing authored actors;
- playing approved animations, poses, sounds, particles and dialogue UI;
- translating arena coordinates for battle playback;
- acknowledging playback completion;
- reconnect/reload reconstruction from server-owned state.

The adapter does not infer ecology, relationships, challenge completion, PTU legality or canon truth from entity behavior.

## Runtime record set

### `WORLD_PROCESS_INSTANCE`

One persistent process that may outlive loaded chunks or player sessions.

```yaml
world_process_instance:
  process_instance_id: null
  process_definition_id: null
  definition_revision: null
  owning_system_ref: null
  location_refs: []
  started_at: null
  current_state: null
  current_revision: 0
  next_due_at: null
  offline_policy: PAUSE_WHEN_UNLOADED | ADVANCE_BY_PERSISTENT_CLOCK | ADVANCE_BY_WORLD_SERVICE | RECOMPUTE_ON_MATERIALIZATION
  active_scene_instance_ids: []
  source_event_refs: []
  canon_status: null
```

A migration, rehabilitation program, recurring festival or institutional procedure can be a process. Loaded Minecraft entities are optional presentations of it.

### `SCENE_DEFINITION`

Versioned executable graph for a bounded scene.

```yaml
scene_definition:
  scene_definition_id: null
  revision: 1
  premise_ref: null
  owning_system_refs: []
  entry_predicates: []
  participant_slots: []
  nodes: []
  terminal_nodes: []
  battle_handoff_ids: []
  recovery_policy_ref: null
  multiplayer_mode: PARTY_SHARED | PER_PLAYER | PER_TEAM | GLOBAL_SERIALIZED | GLOBAL_SHARED
```

### `SCENE_INSTANCE`

Server-owned current state of one run.

```yaml
scene_instance:
  scene_instance_id: null
  scene_definition_id: null
  definition_revision: 1
  current_node_id: null
  state_revision: 0
  participant_bindings: {}
  world_zone_bindings: {}
  local_variables: {}
  accepted_operation_ids: []
  pending_effect_ids: []
  battle_session_ref: null
  started_at: null
  updated_at: null
  outcome: ACTIVE | COMPLETED | SUSPENDED | FAILED_RECOVERABLY | ABANDONED
```

### `ACTOR_ENTITY_BINDING`

Connects a persistent Ouros actor to a transient Minecraft/Cobblemon object.

```yaml
actor_entity_binding:
  actor_ref: pokemon:cedar-watchog-01
  actor_kind: POKEMON | NPC | TRAINER | OTHER
  persistent_identity_authority: pokemon_agency
  materialization_state: UNMATERIALIZED | MATERIALIZING | MATERIALIZED | UNLOADING | ERROR
  minecraft_dimension: null
  minecraft_entity_uuid: null
  cobblemon_pokemon_uuid: null
  expected_location_ref: null
  presentation_profile_ref: null
  binding_revision: 0
  last_confirmed_at: null
```

A missing Minecraft entity does not delete the actor. A newly loaded entity does not create a new actor unless an owning system explicitly creates one.

### `WORLD_ZONE`

Server-authored spatial trigger or presentation area.

```yaml
world_zone:
  zone_id: null
  location_ref: null
  dimension_ref: null
  shape: AABB | POLYGON_PRISM | BLOCK_SET | RADIUS
  geometry_revision: null
  trigger_roles: []
  battle_arena_ref_optional: null
  visibility_policy: null
```

Battle LoS and battle coordinates are not reused as world-zone semantics.

### `SCENE_TRIGGER`

```yaml
scene_trigger:
  trigger_id: null
  trigger_type: PLAYER_ENTER_ZONE | PLAYER_EXIT_ZONE | ENTITY_CALLBACK | CLOCK_DUE | WORLD_STATE_CHANGED | PRIOR_TRANSITION | BATTLE_RESULT | SERVER_RECOVERY
  source_ref: null
  predicate_ref: null
  debounce_policy: null
  consume_policy: ONCE_PER_INSTANCE | ONCE_PER_ACTOR | REPEATABLE | EDGE_TRIGGERED
```

Proximity or chunk load only matters when an authored trigger says it matters.

### `SCENE_NODE`

```yaml
scene_node:
  node_id: null
  enter_predicates: []
  on_enter_effects: []
  interaction_offers: []
  timed_transitions: []
  observation_outputs: []
  exit_transitions: []
  fallback_transition: null
```

A node is executable state, not a paragraph of narration.

### `INTERACTION_OFFER`

```yaml
interaction_offer:
  offer_id: null
  request_kind: OBSERVE | TALK | INSPECT | ACKNOWLEDGE | ACTIVATE | WAIT | WITHDRAW | REQUEST_HELP | START_BATTLE | OTHER
  actor_scope: null
  target_ref: null
  visible_if: []
  legal_if: []
  rejection_reason_refs: []
  accepted_transition_ref: null
  rules_check_ref_optional: null
```

PTU Skills, Capabilities, Moves, Items, Abilities and Trainer Features may appear only through validated rules checks. The scene runtime cannot invent them.

### `WORLD_EFFECT_COMMAND`

Every effect is server-owned and idempotent.

```yaml
world_effect_command:
  effect_id: null
  operation_id: null
  effect_type: MATERIALIZE_ACTOR | DEMATERIALIZE_ACTOR | SET_PRESENTATION_STATE | SET_DIALOGUE_NODE | SET_INTERACTION_ENABLED | SET_BLOCK_PRESENTATION | PUBLISH_NOTICE | REMOVE_NOTICE | SCHEDULE_TRANSITION | WRITE_WORLD_STATE | APPEND_CHRONICLE | REQUEST_BATTLE | OTHER
  target_ref: null
  payload_ref: null
  authoritative_source_ref: null
  retry_policy: IDEMPOTENT_RETRY | MANUAL_RECOVERY | NO_RETRY
  status: PENDING | APPLIED | ACKNOWLEDGED | FAILED
```

The adapter may retry presentation safely because the operation ID is stable.

## Scene transition contract

A transition commits in this order:

1. Receive a trigger or interaction request.
2. Resolve the current `scene_instance` revision.
3. Validate scene-node and world-state predicates server-side.
4. Reserve any scarce external state if required.
5. Create a transition with a unique operation ID.
6. Commit narrative/world-state changes.
7. Queue adapter presentation effects.
8. Advance the scene revision.
9. Append an audit/Chronicle record when appropriate.
10. Acknowledge presentation separately.

Presentation failure after step 6 does not reverse authoritative truth automatically. Recovery reconstructs the presentation from current state.

## Optimistic-concurrency rule

Every interaction request includes the scene revision the client observed.

```yaml
interaction_request:
  scene_instance_id: null
  observed_scene_revision: 12
  actor_ref: null
  offer_id: null
  client_request_id: null
```

If the server is now at revision 13, it rejects or rebases according to the authored interaction policy. Client-side last-writer-wins is prohibited.

## Materialization contract

Materialization is a projection of existing state.

Required sequence:

`persistent actor selected -> materialization request -> adapter creates/binds entity -> binding confirmed -> presentation state applied`

For a Cobblemon Pokémon, the future adapter should preserve a stable relationship between the Ouros `pokemon_entity_id`, the Cobblemon Pokémon record where applicable and the current `PokemonEntity` world object.

If the chunk unloads:

`MATERIALIZED -> UNLOADING -> UNMATERIALIZED`

The actor remains alive in Ouros state unless an authoritative domain event says otherwise.

## Dialogue contract

Dialogue content is addressed by stable keys rather than embedded into scene code.

```yaml
dialogue_request:
  dialogue_profile_ref: npc:warden-mira
  dialogue_node_key: cedar_alarm.after_signal
  context_refs:
    - scene:cedar_alarm:instance
    - observation:alarm_2026_08_26
  allowed_response_offer_ids:
    - inspect_watch_point
    - withdraw_from_meadow
```

The adapter can present Cobblemon dialogue/UI. The server still validates every response.

## Battle handoff

### Request

```yaml
battle_handoff_request:
  handoff_id: null
  scene_instance_id: null
  scene_revision: null
  battle_contract_ref: null
  battle_spec_ref: null
  participant_actor_refs: []
  combatant_bindings: []
  arena_snapshot_ref: null
  world_state_snapshot_refs: []
  expected_result_fields: []
  idempotency_key: null
```

The scene freezes any world facts required by the battle contract. The adapter does not resample mutable world state halfway through an AutoPTU action.

### Result ingestion

```yaml
battle_result_ingest:
  handoff_id: null
  authoritative_battle_session_id: null
  final_state_hash: null
  outcome_fields: {}
  event_stream_ref: null
  accepted_by_scene_revision: null
```

Only declared result fields may cause scene transitions.

Examples:
- `battle_completed`
- `winner_side`
- `combatant_withdrawal_state`
- later, exact objective fields once AutoPTU supports them authoritatively.

Minecraft entity death, a victory screen or a client animation cannot satisfy the handoff.

## Reduced-runtime contract

A reduced encounter is still a real implementation. It must define exactly what happens outside battle and exactly what AutoPTU resolves.

Bad reduction:

`wild Pokémon retreat automatically because Minecraft pathfinding moved them away`

Good reduction:

`scene transition commits wildlife withdrawal in Ouros state -> adapter plays authored departure presentation -> optional hostile combatants are bound to a static AutoPTU battle -> result returns -> scene commits aftermath`

The reduction is explicit, testable and persistent even though tactical group withdrawal is not yet implemented.

## Offline and unloaded-world behavior

Every process or scene with time dependence declares one policy.

`PAUSE_WHEN_UNLOADED` is appropriate for a physical interaction requiring present players.

`ADVANCE_BY_PERSISTENT_CLOCK` is appropriate for scheduled institutions or authored natural phases when the governing layer already supports the time transition.

`ADVANCE_BY_WORLD_SERVICE` is appropriate when a simulation/service evaluates state without Minecraft chunks.

`RECOMPUTE_ON_MATERIALIZATION` is appropriate for presentation-only state derived from authoritative records.

Never use `entity_tick_count` or chunk uptime as implicit world chronology.

## Recovery and rollback

Technical recovery is not in-world time reversal.

Persist at minimum:
- latest committed scene revision;
- current node;
- participant bindings by persistent ID;
- accepted client request IDs;
- applied effect operation IDs;
- pending adapter acknowledgements;
- active battle handoff ID;
- scheduled transitions.

On server restart:

1. load committed scene state;
2. reconcile bindings;
3. replay only unapplied idempotent presentation effects;
4. never reissue an already accepted reward/state mutation;
5. reconnect to an active authoritative battle session or mark explicit recovery state;
6. resume from the committed node.

## Required tests for every executable scene

Each machine-readable scene should have test vectors for:
- normal entry and completion;
- duplicate trigger delivery;
- duplicate interaction request;
- disconnect/rejoin;
- server restart between world-state commit and presentation acknowledgement;
- actor entity unload/reload;
- invalid/stale scene revision;
- multiplayer simultaneous interaction where applicable;
- battle request issued once;
- duplicate battle result delivery;
- reduced-version path when a required capability is unavailable;
- Chronicle/world-state writeback exactly once.

## Capability boundary

Pass 182 does not promote engine families.

Current permanent map remains:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

The purpose of this contract is to turn the final blocking adapter family into a concrete implementation target rather than a generic label.

## First implementation target

`implementation/vertical-slices/cedar-meadow-alarm-network-v1.yaml` defines the first complete reduced-runtime scene derived from existing Ouros research.

It is deliberately small enough to prototype while still proving:
- persistent wild Pokémon identity;
- server-owned zone trigger;
- materialization binding;
- observable scene behavior;
- player interaction;
- Chronicle writeback;
- explicit departure state;
- optional static AutoPTU battle handoff;
- reconnect/restart safety.

Passing this slice means the researched world has begun to execute. It does not mean the full Minecraft adapter category is VERIFIED.