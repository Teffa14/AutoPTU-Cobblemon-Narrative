# Global NPC plan-selection provenance contract — Pass 375

Status: DESIGN / IMPLEMENTATION CONTRACT
Date: 2026-09-09
Canon impact: NONE

## Purpose

Preserve enough decision-time context to prove which world-agent agenda decision was selected after a specific consumed ReplanBatch.

Pass 374 already makes delivery-to-replan provenance durable. This pass begins the next owner without changing the planner's policy.

## New owner

`OUROS_NPC_PLAN_SELECTION_PROVENANCE_V1`

Implementation:

`tools/global_npc_plan_selection_provenance.py`

The owner records one append-only PlanSelectionRecord containing:

- stable selection ID;
- ReplanBatch identity and semantic minute;
- trigger IDs, reasons, source refs and highest priority;
- decision-time NpcAgentState snapshot;
- the exact goals, needs, scheduled commitments and situational intents supplied to replanning;
- active-intent continuity context;
- the resulting AgendaDecision, source type/ref, score, handoff and reason codes.

## Ownership boundary

The existing `choose_agenda_intent` / `replan_from_batch` logic remains authoritative for world-agent agenda arbitration.

The provenance owner does not calculate a different score and does not choose a different winner. Validation reconstructs the saved inputs and calls the existing planner again. If the persisted result no longer matches deterministic replay, restore fails closed.

This distinction is required:

`TRIGGER_CONSUMED != PLAN_SELECTED != ACTION_STARTED != ACTION_SUCCEEDED`

A selected structured-mechanics intent may request an AutoPTU handoff. Recording that selection does not prove that the handoff was accepted or that any battle mechanic occurred.

## Link to Pass 373/374 provenance

Every trigger in a persisted selection must have a matching ConsumedReplanRecord.

The consumed record must match:

- actor;
- processed semantic minute;
- replan batch key.

A bare completed trigger ID is insufficient evidence.

## Replay rule

A PlanSelectionRecord is valid only when the saved inputs reproduce the same AgendaDecision under the current authoritative planner implementation.

This detects tampering or drift in:

- selected intent;
- decision score;
- source attribution;
- handoff state;
- reason codes;
- candidate input state;
- continuity context.

Planner-policy migrations remain possible, but they must be explicit. A future change that intentionally alters historical deterministic arbitration needs a schema migration or compatibility policy rather than silent reinterpretation.

## Migration rule

This pass introduces standalone provenance only. No world-checkpoint migration is defined yet.

A future coherent-world checkpoint must add this owner explicitly. Older checkpoints must restore with an empty plan-selection ledger. They must not reconstruct historical choices from current agenda, location, action state, AutoPTU bindings or outcomes.

## Test obligations

Regression coverage must prove:

- a multi-candidate decision records all supplied input families;
- snapshot/restore reproduces the same winner;
- selected-result tampering fails;
- candidate-context tampering that changes the winner fails;
- unconsumed triggers fail cross-owner validation;
- batch-key mismatch fails;
- future selections fail against restored semantic time;
- duplicate selections fail.

## Canon and mechanics boundary

This contract changes persistence architecture only. It does not establish a region, faction, NPC, quest or historical event.

PTU/Caelo remains authoritative for battle rules. AutoPTU-Java and AutoPTU remain read-only from this task.
