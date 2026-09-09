# Global NPC world action-start provenance checkpoint contract — Pass 378

Status: IMPLEMENTED FOUNDATION
Date: 2026-09-09
Canon effect: NONE

## Purpose

Pass 377 made replayable action-start provenance durable as a standalone owner. Pass 378 places that history inside coherent world recovery.

`OUROS_NPC_WORLD_CHECKPOINT_V17` extends V16 with `OUROS_NPC_ACTION_START_PROVENANCE_V1` under the same SHA-256 recovery unit.

The preserved causal chain is now:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED`

The next boundary remains explicit:

`ACTION_STARTED != ACTION_COMPLETED != ACTION_SUCCEEDED`

For structured mechanics:

`PLAN_SELECTED -> REQUEST_AUTOPTU -> AUTOPTU_BINDING_ACCEPTED -> AUTOPTU_RESOLVED`

## Coherent recovery rule

The V17 world snapshot contains the complete V16 payload plus the action-start ledger.

Restore first validates the V17 digest, restores and replays every action-start record, reconstructs V16 through its own restore path, then validates every start against the recovered plan-selection ledger at the recovered semantic minute.

An action-start record therefore cannot survive coherent recovery if:

- its linked plan selection disappeared;
- actor, selected intent or target provenance no longer match;
- its start predates plan selection;
- its start comes from a future semantic minute;
- its captured travel departure no longer replays to `DEPART_NOW` and the same post-start travel state;
- its captured AutoPTU transition no longer replays to the same concrete `AUTOPTU_BOUND` binding;
- the same plan selection claims duplicate starts of one start kind.

## Migration

V16 and older checkpoints restore through V17 with an empty `ActionStartProvenanceLedger`.

Migration does not infer historical action start from:

- current NPC location;
- an edge already in progress;
- arrival at a destination;
- current `AUTOPTU_BOUND` mode;
- a later encounter result;
- dialogue, memory or testimony;
- Minecraft/Cobblemon presentation state.

This intentionally permits a legacy world to know its current state without fabricating the missing transition history.

## Mechanical boundary

Pass 378 adds world persistence only. It adds no PTU or Caelo battle rule.

`TRAVEL_EDGE_STARTED` proves the existing world-travel contract crossed its departure boundary. It does not prove arrival, route safety or tactical movement.

`AUTOPTU_BINDING_ACCEPTED` proves only that the world-agent layer accepted a concrete structured-resolution binding. AutoPTU remains authoritative for tactical legality, turns, damage, statuses, moves, Abilities, Items, Trainer Features and battle outcome.

Minecraft/Cobblemon/Craftics remains a presentation/adapter layer and cannot synthesize a missing action-start record from animation or entity position.

## Explicit non-claims

V17 does not establish:

- action completion or failure;
- successful arrival;
- AutoPTU session completion or result ingress;
- objective success;
- acknowledgement by another NPC;
- tactical policy support for escort, rescue, cargo or non-KO objectives;
- a canonical Ouros expedition, route, institution or encounter.

The next bounded provenance seam is action terminal state: completion, failure and AutoPTU result ingress must remain distinct from action start.