# Global NPC action interruption provenance contract — Pass 381

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE

## Purpose

Pass 380 preserves replayable travel arrival under V18. A different causal outcome already exists in the semantic travel runtime: after an action has started, the planned edge can become unavailable and `advance_travel` can return `REPLAN_REQUIRED`.

Pass 381 preserves that transition without calling it failure, cancellation or mission completion.

`ACTION_STARTED -> TRAVEL_REPLAN_REQUIRED`

`TRAVEL_REPLAN_REQUIRED != ACTION_FAILED`

`TRAVEL_REPLAN_REQUIRED != ACTION_CANCELED`

`TRAVEL_REPLAN_REQUIRED != OBJECTIVE_FAILED`

## Owner

`OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1`

The owner records a replayable interruption tied to one `TRAVEL_EDGE_STARTED` action start.

It retains the exact source action-start identity, selected plan identity, agent/intent/target identity, semantic minute, started travel state and the route-edge state observed at interruption time.

The route-edge snapshot at interruption may legitimately differ from the route-edge snapshot at departure. That difference is the point of the event.

## Admission rule

The first admitted interruption kind is `TRAVEL_REPLAN_REQUIRED`.

It is admitted only when replaying the existing semantic travel function from the preserved started state with the interruption-time route edges returns `REPLAN_REQUIRED`.

An ordinary `TRAVEL_IN_PROGRESS`, `ARRIVED`, `REQUEST_AUTOPTU`, `PROJECT_LOCAL_TRAVEL` or `HOLD_AUTOPTU` result cannot be relabeled as an interruption.

## Cross-owner validation

Every interruption must resolve to an existing action start with matching selection, agent, intent and target. It cannot precede that start or occur after the recovered semantic minute.

The agent and started-travel snapshots must match the source action-start owner. Route conditions at interruption are independent evidence because availability, knowledge or permission can change after departure.

## Recovery boundary

The standalone owner supports snapshot/restore and deterministic replay. It is not yet included in V18.

A later coherent checkpoint may include it only after cross-validating against the restored action-start ledger.

Migration from older checkpoints must not invent historical interruptions from a currently blocked route, a later replan, a changed location, a missed objective or dialogue about trouble on the road.

## Narrative boundary

A recorded interruption proves that the currently planned semantic route could no longer continue under the route facts supplied at that moment. It does not prove why the underlying world fact changed unless a separate authoritative owner supplies that provenance.

The resulting replan may choose another route, wait, seek information, request help, abandon the objective or do something unrelated. Those later decisions remain separate events.

## Engine boundary

This reduced world-agent transition does not require AutoPTU tactical execution. If a later encounter explains the route change physically, every battle dependency must be admitted independently using the permanent engine capability categories. No representative move, Ability, status, terrain effect or reaction promotes an entire family.

## Next boundaries

Integrate interruption provenance into a coherent checkpoint after V18. Then define failure and cancellation only when the world runtime exposes authoritative replayable transitions for them. Objective completion/failure must remain a separate owner. `AUTOPTU_RESOLVED` still requires an exact replayable session-resolution event tied to the accepted binding.
