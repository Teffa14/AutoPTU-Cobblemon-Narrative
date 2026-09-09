# Global NPC world action terminal provenance checkpoint contract — Pass 380

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE

## Purpose

Pass 379 introduced replayable terminal evidence for semantic travel destination arrival, but kept it outside the coherent V17 world checkpoint. Pass 380 places that terminal owner under the same integrity digest as the causal history on which it depends.

`OUROS_NPC_WORLD_CHECKPOINT_V18` is the first coherent world checkpoint that can preserve the demonstrated chain through travel arrival.

## Demonstrated causal chain

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

The last transition is narrow. It proves semantic arrival at the selected travel destination. It does not establish generic action success or mission completion.

## Build rule

Before V18 is serialized:

1. action-terminal provenance validates against the exact action-start ledger;
2. each terminal must be no later than the checkpoint semantic minute;
3. V17 is built normally with its delivery, replanning, plan-selection and action-start provenance;
4. the terminal ledger is added to that payload;
5. one SHA-256 covers the full V18 payload.

A terminal ledger that cannot cross-validate against the action starts is rejected before persistence.

## Restore rule

V18 restore:

1. verifies the outer digest;
2. restores and internally replays `OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1`;
3. reconstructs a valid V17 payload and restores it through the existing V17 owner;
4. validates every terminal against the restored action-start provenance and recovered semantic minute.

Re-signing a structurally altered snapshot does not make it historical evidence. Replay or cross-owner mismatch still fails closed.

## Migration rule

V17 and earlier checkpoints migrate with an empty `ActionTerminalProvenanceLedger`.

Migration must not synthesize terminal history from:

- current location;
- a travel object that happens to be at its destination;
- later dialogue or knowledge;
- current inventory or samples;
- mission/objective state;
- current AutoPTU binding;
- tactical result ingress;
- Minecraft/Cobblemon presentation state.

Unknown history remains unknown.

## Current admitted terminal

Only `TRAVEL_DESTINATION_ARRIVED` is admitted because semantic travel already exposes a deterministic replayable `ARRIVED` transition.

The terminal must retain its source action-start ID, source selection ID, agent/intent/target identity, semantic minute and exact travel replay evidence.

## Explicit non-claims

`TRAVEL_DESTINATION_ARRIVED != OBJECTIVE_COMPLETED`

`TRAVEL_DESTINATION_ARRIVED != ACTION_SUCCEEDED`

`TRAVEL_DESTINATION_ARRIVED != HANDOFF_COMPLETED`

`TRAVEL_DESTINATION_ARRIVED != SAMPLE_PRESERVED`

`AUTOPTU_BINDING_ACCEPTED != AUTOPTU_RESOLVED != AUTOPTU_RESULT_INGRESSED`

Pass 380 adds no synthetic AutoPTU terminal and no tactical truth.

## Narrative use

A restored world can now support stories where all parties agree that a team reached a place while disagreeing, with legitimate evidence, about what happened after arrival. The missing causal seam can be investigation content rather than an inferred result.

## Mechanics boundary

The reduced use of V18 needs only the world-agent contracts that already produce selection, semantic travel start and deterministic arrival.

A richer tactical scene must name every engine family it uses. Ordinary audited targeting, base movement, calculations, action-economy primitives and legal-action infrastructure remain usable only within verified scopes. Push/pull/knockback/interception/forced movement, complex status, dynamic hazards/weather/zones/reactions, move-specific behavior, Abilities, Items and Trainer Feature interrupts remain gated by their exact evidence.

Narrative-objective policies such as escort, protect-equipment, search, rescue-first, route-clearing, objective-aware withdrawal and disengage-after-objective remain blocked at AI tactical policy unless live engine evidence verifies the exact policy. Minecraft/Cobblemon/Craftics remains partial/blocking for persistent objective identity and authoritative non-KO result playback.

## Next boundaries

- terminal failure and cancellation provenance;
- terminal semantics for non-travel world actions;
- a replayable `AUTOPTU_RESOLVED` owner tied to the exact accepted binding/session;
- causal binding between tactical resolution and semantic-result ingress;
- separate objective-completion provenance so arrival cannot silently become mission success.
