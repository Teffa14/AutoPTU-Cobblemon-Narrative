# Global NPC world action-interruption provenance checkpoint contract — Pass 382

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE

## Purpose

Pass 381 introduced replayable `TRAVEL_REPLAN_REQUIRED` evidence after a real travel action start but kept that evidence outside the coherent V18 checkpoint. Pass 382 places the interruption owner under the same integrity digest as the causal history it depends on.

`OUROS_NPC_WORLD_CHECKPOINT_V19` is the first coherent checkpoint that can preserve both demonstrated action outcomes currently supported by the world-agent travel runtime: destination arrival and route interruption.

## Demonstrated branches

V19 can preserve:

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

or

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_REPLAN_REQUIRED`

These are mutually exclusive outcomes for the same action-start identity.

`TRAVEL_REPLAN_REQUIRED != ACTION_FAILED`

`TRAVEL_REPLAN_REQUIRED != ACTION_CANCELED`

`TRAVEL_DESTINATION_ARRIVED != OBJECTIVE_COMPLETED`

## Owner

`OUROS_NPC_WORLD_CHECKPOINT_V19`

V19 contains the complete V18 payload plus `OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1` under one SHA-256 digest.

Restore first validates the V19 digest, restores the interruption ledger, reconstructs and validates V18, then cross-validates interruption rows against the restored action-start owner and recovered semantic minute.

## Outcome exclusivity

One action-start ID cannot simultaneously own a terminal-arrival record and an interruption record.

That contradiction is rejected during build and restore even if a modified snapshot has been re-signed with a valid digest.

This rule is deliberately narrow. It does not define every future terminal family. It protects only the outcome families currently admitted by authoritative replayable world transitions.

## Migration

Restoring V18 or an older checkpoint through the V19 API produces an empty interruption ledger.

Migration does not infer historical interruption from current route closure, present NPC location, a later plan, dialogue, mission state, world damage or another downstream observation.

## Narrative boundary

A coherent interruption proves that the actor had already begun the recorded travel action and that continuation of the planned route produced `REPLAN_REQUIRED` under the preserved interruption-time route conditions.

It does not establish the external cause of that route change. A separate world owner must establish whether the cause was storm damage, infrastructure work, authority closure, lost permission, ecological disturbance, sabotage or another fact.

## Engine boundary

The reduced interruption branch runs entirely in world-agent semantic travel and requires no AutoPTU tactical resolution.

A later physical encounter at the interruption site must declare its dependencies individually using the permanent capability categories. No representative move, Ability, status, weather effect, terrain interaction or reaction promotes its entire category.

## Next boundaries

Failure and cancellation remain blocked until live replayable transitions exist for them. Objective completion/failure remains separate from execution outcome. `AUTOPTU_RESOLVED` still requires an exact replayable resolution event tied to the accepted binding rather than inference from a later result ingress.
