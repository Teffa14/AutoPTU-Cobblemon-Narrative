# Global NPC Assistance Commitment Start Disposition Contract — Pass 440

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 439 records the factual condition when a negotiated assistance window opens while a pre-start risk or blocker still exists. It deliberately leaves policy to the responder.

Pass 440 adds that narrow policy seam.

`OUROS_ASSISTANCE_COMMITMENT_DISPOSITION_LEDGER_V1` records the responder's immediate world-level choice after an adverse start assessment while preserving the original promise and the evidence that made fulfillment difficult.

## Admissible start dispositions

The first contract admits four semantic choices:

- `ATTEMPT_FULFILLMENT`: the responder intends to try to honor the accepted obligation despite the adverse condition;
- `WAIT_FOR_CLEARANCE`: the responder chooses not to proceed yet and waits for the blocking/risk state to change;
- `REQUEST_RENEGOTIATION`: the responder decides that the accepted terms need to change;
- `ABANDON_OBLIGATION`: the responder decides not to continue pursuing fulfillment under the accepted obligation.

These values record intent. They do not execute the resulting world action.

## Required causal chain

A disposition must bind to:

- an existing negotiated assistance commitment;
- the exact `proposal_id` accepted by the requester;
- an existing `AT_RISK_AT_START` or `BLOCKED_AT_START` assessment;
- the same requester and responder;
- the responder as the actor making the choice;
- a semantic minute at or after the start assessment and no later than the accepted end minute;
- a rationale reference;
- explicit provenance.

A caller cannot create a start disposition from a global blocker alone. The adverse condition first has to survive through the start-assessment owner.

## Agreement preservation

Recording a disposition does not mutate the negotiated commitment. Start time, end time, location, scope, alternative metadata and provenance remain unchanged.

This lets the world retain separate facts such as:

1. Teo promised Mara an inspection window.
2. The access route was still blocked when that window opened.
3. Teo chose to request renegotiation.
4. Mara may or may not later receive that request.
5. A new agreement may or may not eventually exist.

No later fact rewrites the earlier ones.

## Communication boundary

`REQUEST_RENEGOTIATION` records only the responder's decision to seek different terms. It does not notify the requester and does not create a counterproposal by itself.

Communication must still use the ordinary information network. New terms must use the existing assistance proposal/decision owners. Failed, delayed or unacknowledged delivery remains distinct from the responder having made the decision.

## Execution boundary

`ATTEMPT_FULFILLMENT` does not start travel, grant access, reserve a route, allocate equipment, admit a tactical action or complete the task.

`WAIT_FOR_CLEARANCE` does not create a timer or clear the blocker.

`ABANDON_OBLIGATION` does not adjudicate blame, relationship consequences or a missed-obligation outcome.

Those effects belong to later owners with their own evidence and policy.

## Mechanical capability posture

The disposition record itself requires no battle capability family.

If `ATTEMPT_FULFILLMENT` later becomes a structured encounter, the exact scene must classify its dependencies independently across targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

No category is promoted by this pass.

## Verification

`tests/test_global_npc_assistance_commitment_disposition.py` covers all four admitted dispositions, responder ownership, exact causal bindings, temporal bounds, agreement preservation, idempotent replay, conflicting identity rejection, one immediate start disposition per commitment, snapshot/restore and a source guard against execution, communication, fault adjudication or AutoPTU entering this owner.
