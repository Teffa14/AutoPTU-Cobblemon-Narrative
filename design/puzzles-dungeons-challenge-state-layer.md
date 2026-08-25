# Puzzles, Dungeons & Persistent Challenge State Layer

Status: PROPOSED SYSTEM / NON-CANON
Pass: 173
Date: 2026-08-25

## Scope

This layer owns persistent authored challenge state: puzzle definitions, challenge instances, mechanism elements, clue/revelation structure, attempts, accepted solution routes, state transitions, reset behavior, bypasses, accessibility alternatives, fail-forward outcomes and handoffs to other authorities.

It does not own the physical truth of a building, the rules of a PTU Move/Skill/Feature, credentials, archaeology, language translation, battle outcomes, Minecraft block truth or the institutional meaning of passing a challenge.

A puzzle can use objects from other systems without taking their authority.

## Authority boundary

Authoritative flow:

`challenge definition -> instance/revision -> presentation state -> actor interaction request -> validation against authored constraints -> state transition -> consequence/handoff -> persistent history`

Existing authorities remain responsible for their domains:

- Architecture owns rooms, doors, structures, damage and physical revisions.
- Material Culture owns persistent objects, provenance and custody.
- Digital Systems owns terminals, accounts and digital state.
- Languages owns inscriptions, translations and language knowledge.
- Archaeology/Paleontology owns excavation context and interpretation.
- Wayfinding owns route guidance and signage.
- Credentials owns eligibility/access authority.
- Battle Institutions owns Gym/League competitive authority and official battle meaning.
- Accessibility owns accommodation requirements and accessible-route truth.
- Cases/Science owns evidence and interpretation outside the authored challenge.
- Pokémon Agency owns individual identity, agency and custody.
- AutoPTU owns PTU battle legality/results when a battle occurs.
- Minecraft/Cobblemon/Craftics presents the result and forwards interaction intent; it does not decide challenge truth.

## Core principles

### Persistent state, not disposable minigame state

A mechanism may remain altered after the party leaves. A restored gate may still be open five years later. A Gym challenge may reset after each challenger. A festival puzzle may exist only during one event edition. Persistence and reset policy are authored properties.

### Challenge state, world state and knowledge state remain separate

A door can physically be open while an old map says it is sealed. A mechanism can be solved while one character has not observed the new state. A translated clue can be wrong while the original inscription remains unchanged.

### No single-solution assumption

A challenge definition can describe several accepted progress routes. It may also permit adjudicated emergent solutions. Required campaign progression should not depend on one obscure interaction unless an authored fail-forward route exists.

### Failure writes history

An unsuccessful attempt can consume time, expose a clue, damage a replaceable component, lock one route temporarily, trigger review, reveal another node or simply remain an unsuccessful attempt. Failure should create a recoverable state rather than a softlock.

### Battle outcome is input, not challenge authority

AutoPTU can return an authoritative battle result. The challenge layer decides whether that result satisfies a condition. Defeating a Pokémon never opens a door by convention.

## Core records

### `CHALLENGE_DEFINITION`

Stable authored identity for a reusable challenge.

Suggested fields:

- `challenge_definition_id`
- `title`
- `challenge_family`: `MECHANISM|ROUTE|RIDDLE|INVESTIGATION|INSTITUTIONAL_TEST|COOPERATIVE_TASK|SEQUENCE|RESOURCE_ALLOCATION|OTHER`
- `owning_institution_or_site_ref`
- `purpose`
- `definition_revision_ids`
- `canon_status`
- `authoring_notes`

The definition can survive many instances and revisions.

### `CHALLENGE_DEFINITION_REVISION`

Versioned rules for one historical form of the challenge.

Suggested fields:

- `revision_id`
- `challenge_definition_id`
- `effective_window`
- `entry_conditions`
- `state_schema`
- `mechanism_element_refs`
- `revelation_refs`
- `accepted_solution_route_refs`
- `failure_outcome_refs`
- `reset_policy_ref`
- `accessibility_route_refs`
- `battle_handoff_refs`
- `supersedes`

Old revisions remain available for historical attempts.

### `CHALLENGE_INSTANCE`

One active or historical occurrence.

Examples: one Gym challenger’s run, one expedition into an ancient lock system, one festival edition, one player-built trial.

Suggested fields:

- `challenge_instance_id`
- `definition_revision_id`
- `location_refs`
- `opened_at`
- `closed_at_optional`
- `participant_refs`
- `initial_state_revision_id`
- `current_state_revision_id`
- `attempt_ids`
- `outcome_state`: `OPEN|COMPLETED|FAILED_FOR_INSTANCE|ABANDONED|SUSPENDED|BYPASSED|UNRESOLVED`
- `institutional_result_ref_optional`

`COMPLETED` means the challenge contract was satisfied. It does not grant a Badge, credential or reward unless another authority says so.

### `MECHANISM_ELEMENT`

Stable identity for an interactive element used by a challenge.

Possible classes:

- lever/switch/control;
- movable object;
- door/gate;
- rotating element;
- pressure or position sensor;
- inscription or display;
- light/sound indicator;
- container/key interface;
- route segment;
- terminal;
- Pokémon-mediated station;
- evaluator station.

Suggested fields:

- `element_id`
- `physical_asset_ref_optional`
- `presentation_asset_refs`
- `interaction_contract_ids`
- `current_element_state_ref`
- `maintenance_authority_ref_optional`
- `visibility_policy`

A Minecraft lever can represent this element. Its raw redstone state never becomes authoritative by itself.

### `CHALLENGE_STATE_REVISION`

Immutable snapshot of meaningful challenge state after a transition.

Suggested fields:

- `state_revision_id`
- `challenge_instance_id`
- `parent_revision_id_optional`
- `timestamp`
- `element_state_map`
- `opened_route_refs`
- `closed_route_refs`
- `revealed_information_refs`
- `consumed_resource_refs`
- `temporary_lock_refs`
- `state_reason`
- `source_transition_id`

This enables rollback for technical corruption without pretending failed in-world attempts never happened.

### `INTERACTION_CONTRACT`

Defines what an actor may request of one element and which authority validates it.

Suggested fields:

- `interaction_contract_id`
- `element_id`
- `request_kind`
- `required_world_state`
- `required_authority_checks`
- `resource_reservation_refs_optional`
- `result_transition_refs`
- `rejection_reason_catalog`

Examples include turn, push, inspect, read, insert, remove, repair, compare, answer, activate, wait, request_help.

The contract may reference a canonical PTU Skill/Capability/Item requirement only when validated against project rules material.

### `REVELATION`

A conclusion or useful fact the challenge can communicate.

Suggested fields:

- `revelation_id`
- `statement_or_fact_ref`
- `importance`: `OPTIONAL|USEFUL|PROGRESSION_CRITICAL`
- `clue_path_ids`
- `proactive_delivery_refs_optional`
- `actor_knowledge_write_policy`

For progression-critical revelations, design should normally provide redundant clue paths.

### `CLUE_PATH`

One independent route toward a revelation or valid action.

Suggested fields:

- `clue_path_id`
- `revelation_id`
- `source_ref`
- `access_condition`
- `required_interpretation_optional`
- `translation_ref_optional`
- `independence_group`
- `historical_revision_scope`

Source dependency matters. Three copies of the same note are not three independent clues.

### `SOLUTION_ROUTE`

One authored valid way to satisfy or bypass part of a challenge.

Suggested fields:

- `solution_route_id`
- `challenge_revision_id`
- `entry_state_predicate`
- `required_transition_sequence_or_constraints`
- `alternative_requirements`
- `result_state`
- `classification`: `INTENDED|ALTERNATE|INSTITUTIONAL_BYPASS|ACCESSIBILITY_EQUIVALENT|EMERGENT_APPROVED`

Do not expose hidden solution data to clients that have not earned it.

### `EMERGENT_SOLUTION_ADJUDICATION`

Records a player-created approach not prewritten as a solution route.

Suggested fields:

- `adjudication_id`
- `challenge_instance_id`
- `proposal_summary`
- `referenced_world_assets`
- `required_rules_checks`
- `decision`: `ACCEPTED|PARTIALLY_ACCEPTED|REJECTED|NEEDS_MORE_INFORMATION`
- `decision_reason`
- `result_transition_ref_optional`
- `precedent_scope`: `THIS_INSTANCE|THIS_REVISION|PROPOSE_FOR_FUTURE_REVISION`

Acceptance does not silently rewrite every future instance.

### `CHALLENGE_ATTEMPT`

One bounded attempt or meaningful interaction sequence.

Suggested fields:

- `attempt_id`
- `challenge_instance_id`
- `participant_refs`
- `started_at`
- `ended_at`
- `starting_state_revision_id`
- `interaction_event_refs`
- `battle_result_refs_optional`
- `ending_state_revision_id`
- `outcome`
- `feedback_refs`

### `RESET_POLICY`

Explicit reset semantics.

Possible modes:

- `NO_AUTOMATIC_RESET`
- `RESET_AFTER_ATTEMPT`
- `RESET_AFTER_COMPLETION`
- `RESET_BY_STAFF`
- `RESET_AFTER_TIME_WINDOW`
- `PARTIAL_RESET`
- `WORLD_PERSISTENT`

Suggested fields include retained state, reset authority, resource restoration policy and history-preservation rule.

Resetting presentation never deletes attempt history.

### `FAIL_FORWARD_OUTCOME`

Defines meaningful state after failure.

Possible outcomes:

- reveal hint;
- open alternate node;
- record institutional failure without blocking regional travel;
- consume time;
- request staff assistance;
- require repair;
- suspend one route temporarily;
- trigger optional combat;
- preserve partial progress;
- allow retreat and later return;
- mark `UNRESOLVED`.

There is no universal punishment table.

### `ACCESSIBILITY_EQUIVALENT_ROUTE`

Authoritative equivalent route when the original presentation creates an avoidable access barrier.

Suggested fields:

- `equivalent_route_id`
- `challenge_revision_id`
- `barrier_context`
- `alternative_presentation_or_interaction`
- `equivalence_scope`
- `institutional_approval_ref`

Examples may include non-color indicators, captions/text equivalents, slower interaction windows, alternate physical routes or staff-assisted interface. This record does not invent a disability or medical fact about any player character.

### `BATTLE_HANDOFF_CONTRACT`

Defines the exact relationship between challenge and AutoPTU.

Suggested fields:

- `handoff_id`
- `trigger_state_predicate`
- `battle_spec_ref`
- `world_state_frozen_for_battle`
- `battle_result_fields_consumed`
- `post_battle_transition_rules`
- `reduced_version_ref_optional`

The challenge layer must consume only authoritative battle results. Minecraft animations, entity death visuals or client victory screens cannot write challenge completion directly.

## Dungeon graph

A dungeon is represented as a graph of persistent world nodes rather than one monolithic minigame.

Possible node types:

- approach;
- threshold;
- exploration room;
- mechanism room;
- clue/archive room;
- social/evaluator node;
- battle node;
- rest/safe node;
- alternate route;
- shortcut;
- exit;
- post-completion changed-state node.

Edges can depend on world state, challenge state, credentials, time, physical access or other existing authorities.

This supports returning years later to a changed dungeon without recreating it from zero.

## Softlock prevention

Progression-critical challenge definitions should be audited for:

- at least one reachable solution under intended starting state;
- recovery after each destructive or consuming interaction;
- redundant access to critical revelations;
- no required consumable that can be permanently lost without replacement/bypass;
- no hidden dependency on an unloaded Minecraft entity;
- reset/recovery contract after server restart;
- multiplayer concurrency behavior;
- disconnect/rejoin behavior;
- alternative route when an accessibility accommodation is required;
- explicit policy if an essential NPC/Pokémon is unavailable;
- escape/retreat route unless intentional confinement is separately authored and safe.

A technical corruption can roll back to the last valid challenge-state revision. That rollback is an infrastructure recovery action, not an in-world time reversal.

## Multiplayer concurrency

A challenge may be:

- party-shared;
- per-player;
- per-team;
- globally shared;
- institutionally serialized;
- cooperative with independent contributions.

The definition must state which one.

Two players manipulating the same mechanism require server-owned ordering. Last-writer-wins client behavior is prohibited for authoritative state.

## Player-created institutions and puzzles

Player-built clubs/businesses may eventually author challenges if canon permits. The system should separate:

- author/editor authority;
- test instance;
- published revision;
- participant records;
- moderation/safety review;
- reward authority;
- physical build ownership.

A player who owns the Minecraft building does not automatically gain authority to issue League credentials or PTU rewards.

## PTU mechanical boundary

PTU Skills, Capabilities, Items, Moves, Abilities and Features remain rules-owned.

A challenge may say “this route accepts a validated canonical capability that satisfies X,” but it cannot fabricate the capability.

Do not infer:

- high Focus automatically solves riddles;
- Technology Education opens every machine;
- Pokémon Education identifies every symbol;
- Perception reveals every hidden object;
- Telepathy gives the solution;
- Teleport bypasses every barrier;
- Groundshaper opens ruins;
- Strength breaks any door;
- a Move with a similar name supplies an overworld effect;
- Creative Action permits arbitrary reality editing.

The accessible AutoPTU corpus includes Creative Action handling and PTU rulebook references for creative use of capabilities/skills in combat. That supports adjudication only within the actual rules boundary; it does not create a universal puzzle mechanic.

## Minecraft/Cobblemon/Craftics boundary

Minecraft may present:

- block changes;
- animations;
- sounds;
- particles;
- doors;
- moving decorative objects;
- UI prompts;
- interactable proxies;
- NPC/Pokémon presence;
- challenge status summaries.

Minecraft must not decide:

- whether the puzzle is solved;
- whether a clue was understood;
- whether an actor has a canonical PTU capability;
- whether an item is valid/consumed;
- whether a battle result satisfies the challenge;
- which hidden solution route applies;
- whether a reset is authorized;
- whether a Badge/credential/reward is earned.

Redstone can mirror current state for presentation. It is never the source of truth.

## Chronicle value

Challenge state becomes valuable over years when:

- a Gym changes its challenge between Leaders;
- an old mechanism is repaired and becomes mundane infrastructure;
- a ruin opens a shortcut used by later generations;
- a museum reproduces an old puzzle as an educational exhibit;
- a former challenger remembers an obsolete revision;
- accessibility improvements become part of institutional history;
- a bypass discovered by players becomes officially incorporated later;
- a player-founded institution publishes new revisions;
- an old challenge is retired but preserved in archives;
- a once-dangerous dungeon becomes a public route after stabilization.

## Canon posture

Pass 173 establishes the challenge-state framework only.

It does not establish a canonical Gym puzzle, dungeon, ancient mechanism, trap, reward, riddle language, League rule, challenge institution or Minecraft implementation.

All concrete examples remain proposed until separately canon-approved.