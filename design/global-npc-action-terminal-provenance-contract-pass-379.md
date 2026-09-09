# Global NPC action terminal provenance contract — Pass 379

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE

## Purpose

Pass 378 proves that a selected world-agent action can have a durable, replayable start under V17. Pass 379 introduces a separate standalone owner for terminal execution evidence without upgrading every action family to completed, failed or successful.

`OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1` initially supports only semantic travel destination arrival because `global_npc_travel.advance_travel` already exposes a deterministic `ARRIVED` transition.

## Causal boundary

The supported chain is:

`PLAN_SELECTED -> TRAVEL_EDGE_STARTED -> TRAVEL_DESTINATION_ARRIVED`

The following remain distinct:

`ACTION_STARTED != ACTION_COMPLETED != ACTION_FAILED != ACTION_SUCCEEDED`

Pass 379 proves one narrow completed travel state. It does not define generic mission success.

For structured mechanics:

`AUTOPTU_BINDING_ACCEPTED != AUTOPTU_RESOLVED != AUTOPTU_RESULT_INGRESSED`

No AutoPTU terminal transition is added until a replayable global-NPC/runtime contract can prove it.

## Record

An `ActionTerminalRecord` preserves:

- stable terminal ID;
- source action-start ID;
- source plan-selection ID;
- agent and intent identity;
- terminal semantic minute;
- exact terminal kind;
- target reference;
- replay evidence.

For `TRAVEL_DESTINATION_ARRIVED`, replay evidence includes the source agent snapshot, the already-started travel state, route edges, resulting decision kind/edge and terminal travel state.

## Admission rule

A travel terminal can be recorded only when:

1. the source start is `TRAVEL_EDGE_STARTED`;
2. terminal time is not earlier than start time;
3. replaying `advance_travel` from the preserved started state at the terminal minute returns `ARRIVED`;
4. the resulting current node equals the plan destination;
5. restored terminal state is byte-structurally equivalent to the replayed state.

An in-progress journey does not count. A planned ETA does not count. Current location observed later does not count.

## Cross-owner validation

Validation against `ActionStartProvenanceLedger` requires:

- the referenced start still exists;
- selection, agent, intent and target match;
- terminal time follows start time;
- the terminal's agent, started-travel and route evidence exactly match the source start evidence;
- one action start cannot acquire multiple terminal-arrival records;
- no terminal record may come from later than the recovered semantic minute.

A terminal record with internally replayable but source-divergent inputs fails closed.

## Persistence

The standalone owner snapshots as `OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1`.

Restore validates each row by replay. A later world-checkpoint pass should place this owner under the same coherent digest as V17. Older checkpoints must migrate with an empty terminal ledger; terminal history must not be synthesized from present position or later consequences.

## Reduced narrative use

A story can now distinguish:

- expedition selected;
- departure actually occurred;
- destination actually reached;
- objective at that destination still unresolved.

This reduced path needs no AutoPTU mechanics.

## Full encounter dependency rule

A tactical consequence after arrival must name every capability family it uses. Ordinary audited targeting, base movement, calculations, action-economy primitives and legal-action infrastructure can support only their verified scopes. Forced movement, interception, complex status, weather phases, hazards/reactions, move-specific effects, Abilities, Items or Trainer Feature interrupts remain gated by those exact families.

Objective-aware rescue, escort, search, protect-equipment, route-clearing and withdrawal remain blocked by AI tactical policy evidence unless current engine tests prove the specific behavior. Minecraft/Cobblemon/Craftics still needs authoritative objective identity and playback/result integration for full deployment.

## Open boundaries

- coherent world-checkpoint integration after V17;
- terminal failure/cancellation provenance;
- terminal semantics for non-travel world actions;
- AutoPTU resolved-session provenance;
- binding an admitted semantic-result ingress receipt to the exact AutoPTU start/session;
- distinguishing travel arrival from mission/objective success.
