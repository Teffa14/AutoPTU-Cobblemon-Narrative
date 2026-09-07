# Karst Hidden Drainage Tracing Observation Contract — Pass 330

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-07

## Purpose

Define a reusable world-state contract for hidden hydrologic connections between surface sinks, cave reaches, wells, springs, seeps, and other persistent features without turning surface geography, Minecraft water blocks, or one tracer test into global truth.

This contract supports investigations, monitoring, spill-response continuity, cave exploration, institutional revision, and later tactical handoff while preserving the current Ouros rule that NPC knowledge is explicit and non-omniscient.

## Core invariants

`SURFACE_PROXIMITY != SUBSURFACE_CONNECTIVITY`

`TRACE_RECOVERED != COMPLETE_PATH_KNOWN`

`EXPECTED_OUTLET != ACTUAL_OUTLET`

`NEGATIVE_WINDOW != PERMANENT_DISCONNECTION`

`HYDROLOGIC_CONNECTION != NPC_KNOWLEDGE_OF_CONNECTION`

`MINECRAFT_WATER_PATH != AUTHORITATIVE_HYDROLOGY`

A connection can exist in authoritative world state before any actor knows it. A hypothesis can be reasonable without being true. A test result can revise confidence without rewriting the observations that produced the earlier hypothesis.

## Persistent world objects

### Hydrologic feature

Each sink, spring, well, cave receptor site, seep, subterranean stream reach, surface stream segment, drainage crossing, or dependent intake receives a stable `feature_id`.

Minimum fields:

- `feature_id`
- `feature_kind`
- `region_id`
- `location_ref`
- `current_access_state`
- `current_authored_physical_state`
- `observation_history_refs`
- `institutional_owner_or_steward_refs`
- `canon_status`

Feature identity persists even if flow, access, use, or interpretation changes.

### Hidden connection edge

Authoritative world state may contain a hidden edge between persistent features.

Minimum fields:

- `connection_id`
- `from_feature_id`
- `to_feature_id`
- `directionality`
- `connection_kind`
- `authored_condition_scope`
- `world_truth_status`
- `evidence_refs`
- `canon_status`

The connection graph is not automatically exposed to NPCs or the player.

### Trace event

A trace event represents one bounded test.

Minimum fields:

- `trace_event_id`
- `test_medium_or_marker_id`
- `injection_feature_id`
- `injection_semantic_time`
- `authored_context_ref`
- `receptor_set`
- `test_authority_or_team_id`
- `protocol_record_ref`
- `canon_status`

No PTU numerical mechanics are implied by the marker/test representation.

### Receptor observation

Each receptor result is a separate observation.

Minimum fields:

- `observation_id`
- `trace_event_id`
- `receptor_feature_id`
- `observation_time`
- `result_state`
- `source_actor_or_device_id`
- `confidence_or_quality_note`
- `provenance_root`

Suggested narrative result states:

- `POSITIVE_RECOVERY`
- `NEGATIVE_WITHIN_WINDOW`
- `INCONCLUSIVE`
- `NOT_SAMPLED`
- `SAMPLE_COMPROMISED`

These are world/research evidence labels, not PTU statuses.

## Evidence and interpretation

A positive recovery can support a connection claim scoped to the test context. It does not automatically establish:

- exact underground geometry;
- universal flow direction under every condition;
- travel time under every season;
- exclusivity of the connection;
- the source of an unrelated spring change;
- safety or contamination status;
- tactical movement legality.

A negative observation must preserve its sampling window and receptor context. It cannot become `NO_CONNECTION` without additional authored evidence.

Institutional interpretation should reference the evidence set used. Later evidence can create a revised interpretation while the prior report remains historically queryable.

## Knowledge and communication integration

Use the existing global NPC information architecture.

Observation flow:

`WORLD_EVENT_OR_TEST -> OBSERVATION -> REPORT/PUBLICATION -> EXPLICIT_RECIPIENT -> DELIVERY -> RECEIVER_EVIDENCE -> BELIEF/DECISION`

Shared faction membership never broadcasts tracer results.

A revised map, corrected notice, emergency advisory, or new positive recovery is a new information event. An NPC can validly possess the old connection hypothesis without receiving the revision.

Archive lookup provides external evidence. It does not silently become personal memory.

## Institutional decision model

Decisions should be scoped to concrete features and evidence sets.

Examples:

- monitor a newly identified resurgence;
- restrict a cave reach while sampling continues;
- revise a spill-response plan for a route crossing;
- protect a recharge feature;
- sample a community well;
- reopen one surface route while keeping another feature under monitoring;
- publish an updated connection map.

Each decision preserves:

- `decision_id`
- `decision_time`
- `authority_actor_or_institution`
- `affected_feature_ids`
- `evidence_refs`
- `decision_state`
- `review_trigger`
- `revision_parent_id` when applicable.

Revision creates lineage rather than retroactive replacement.

## Delayed-result and revisit support

Trace results can mature after a quest step ends. A pending test can therefore create later world events:

- delayed positive receptor recovery;
- second trace under a different authored condition;
- discovery of a new seep/resurgence;
- revised recharge-area hypothesis;
- updated maintenance or emergency obligations;
- changed NPC belief after explicit delivery.

The delayed result must remain deterministic under identical world state and semantic time inputs.

## Reduced implementation contract

The reduced version requires no simulated subsurface fluid flow.

Author hidden connectivity and test outcomes as world state. Resolve trace events between scenes. Use existing persistent feature IDs, explicit observations, reports, publications, archives, recipient delivery, belief, decisions, and revisions.

Static cave traversal can use authored route edges. Unsupported submerged or unstable spaces remain closed or abstracted rather than resolved through Minecraft physics.

If a battle occurs, hand off only a static tactical map whose legal geometry does not depend on missing cave/water mechanics.

## Full tactical dependency contract

When a karst encounter adds rich tactical behavior, classify each dependency explicitly:

- targeting/footprints/range/LoS: ordinary support is verified; darkness, mist, spray, submerged sight, changing occlusion, or narrow-portal special behavior require specific evidence.
- base movement legality: ordinary support is verified; climbing, swimming, squeezing, slippery rock, cave-specific costs, or submerged movement require separate verification.
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for currents, falls, rescue, interception, collapse displacement, or forced channel movement.
- core calculations: VERIFIED for ordinary audited deterministic calculations.
- action economy/initiative: VERIFIED for ordinary audited primitives.
- full turn/round lifecycle: PARTIAL; required for timed flooding, delayed collapse, recurring pulses, changing cave access, or environmental phase logic.
- full stateful damage pipeline: PARTIAL; required for environmental fall, collapse, crushing, impact, drowning-like, or similar HP changes.
- status lifecycle: PARTIAL; required for any persistent tactical exposure/condition.
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by subfamily; required for moving water zones, unstable ground, collapse hazards, shelter, reactions, or environmental triggers.
- move-specific behavior: PARTIAL; verify each interaction independently.
- abilities: PARTIAL; verify each interaction independently.
- items: PARTIAL; verify each interaction independently.
- Trainer Features/perks: PARTIAL; verify each interaction independently.
- AI legal-action infrastructure: VERIFIED for ordinary audited legal actions.
- AI tactical policy: BLOCKING for general rescue, escort, retreat, investigation-under-threat, dynamic hazards, and non-defeat objectives.
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end for dynamic authoritative cave/environment behavior.

## PTU / Caelo boundary

The current repository source inventory contains Kairos comparative material and no adopted `sources/caelo` rules source. This design contract therefore defines no DCs, movement costs, Swim behavior, drowning rules, visibility modifiers, cave-navigation bonuses, contamination effects, sensory privileges, Move effects, Ability effects, Item effects, or Trainer Feature mechanics.

Any such mechanical rule requires authoritative source validation plus AutoPTU implementation evidence before admission.

## Canon boundary

This contract defines architecture only. It does not establish a specific Ouros karst region, cave, spring, settlement, species population, groundwater connection, institutional authority, or incident. Those remain proposal fields until explicit canon promotion.
