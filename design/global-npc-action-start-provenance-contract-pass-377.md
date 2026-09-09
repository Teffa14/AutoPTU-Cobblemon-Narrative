# Global NPC action-start provenance contract — Pass 377

Status: IMPLEMENTED FOUNDATION
Date: 2026-09-09
Canon effect: NONE

## Purpose

Pass 376 made `PLAN_SELECTED` restart-durable. Pass 377 adds a separate append-only owner for the first executable transition after selection.

The required causal boundary is:

`PLAN_SELECTED != ACTION_STARTED != ACTION_SUCCEEDED`

For structured mechanics the finer boundary is:

`PLAN_SELECTED -> REQUEST_AUTOPTU -> AUTOPTU_BINDING_ACCEPTED -> AUTOPTU_RESOLVED`

A request alone does not prove that AutoPTU accepted ownership.

## Implemented owner

`tools/global_npc_action_start_provenance.py`

Schema: `OUROS_NPC_ACTION_START_PROVENANCE_V1`

The standalone ledger currently admits two action-start families because both can be replayed against existing authoritative world-agent contracts without inventing a new execution system.

### TRAVEL_EDGE_STARTED

Evidence includes:
- linked Pass 375 plan selection;
- decision-time agent snapshot;
- pre-start `TravelState`;
- relevant route-edge definitions;
- replayed `DEPART_NOW` decision;
- post-start travel state with `edge_started_minute`.

A reserved departure time, travel plan, destination choice or `WAIT_BEFORE_DEPARTURE` result does not count as start.

### AUTOPTU_BINDING_ACCEPTED

Evidence includes:
- linked plan selection whose handoff is `REQUEST_AUTOPTU`;
- pre-binding agent state;
- concrete binding reference;
- replayed post-binding state in `AUTOPTU_BOUND` mode.

This proves only that the world-agent boundary accepted the structured-resolution binding. It does not prove battle initialization, tactical legality, any move, damage, result or playback.

## Cross-owner validation

Every action start must reference an existing `PlanSelectionRecord` for the same actor and selected intent. Target provenance must match. Start time cannot precede selection or exceed the restored semantic minute.

Duplicate action-start records of the same kind for one selection fail closed.

## Restore policy

Restore replays the captured start transition using existing travel or AutoPTU-binding functions. If the recorded transition no longer reproduces the persisted evidence, restore fails closed.

No migration may infer historical action starts from current location, completed travel, current `AUTOPTU_BOUND` state, dialogue, encounter results or later world state.

## Explicit non-claims

The ledger does not claim:
- action completion;
- action success;
- PTU legality or battle outcome;
- Minecraft animation or projection;
- acknowledgement by another actor;
- arrival at a destination;
- completion of an AutoPTU session.

World-checkpoint integration remains a later bounded slice. Pass 377 implements and tests the standalone provenance owner only.
