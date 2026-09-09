# Global NPC world plan-selection provenance checkpoint — Pass 376

Status: DESIGN / IMPLEMENTATION CONTRACT
Date: 2026-09-09
Canon impact: NONE

## Purpose

Pass 375 made plan selection replayable but standalone. Pass 376 places that history inside coherent world recovery.

`OUROS_NPC_WORLD_CHECKPOINT_V16` extends V15 with `OUROS_NPC_PLAN_SELECTION_PROVENANCE_V1` under the same SHA-256 recovery unit.

The preserved causal chain is now:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED`

The following facts remain later owners and must not be inferred:

`PLAN_SELECTED != ACTION_STARTED != AUTOPTU_HANDOFF != ACTION_SUCCEEDED`

## Validation boundary

A restored selection must still replay from its persisted agent snapshot, goals, needs, commitments, situational intents, active-intent continuity and replan batch.

Every trigger used by the selection must still have structured consumed-trigger provenance for the same actor, semantic minute and batch key.

The selection cannot come from a semantic minute later than the restored world instant.

The whole selection ledger is covered by the V16 digest. Re-signing a tampered snapshot does not bypass causal validation against the restored V15 delivery/replan provenance.

## Migration

V15 and earlier snapshots restore with an empty `PlanSelectionProvenanceLedger`.

Recovery does not reconstruct a historical decision from:

- current agenda;
- current location;
- current active intent;
- completed trigger IDs;
- later travel or interaction state;
- AutoPTU results;
- dialogue or memory that happens to mention the decision.

Those signals can be later evidence, but they do not replace the original plan-selection owner.

## Canon and mechanics boundary

This checkpoint is global NPC infrastructure. It adds no Ouros geography, institution, character, Pokémon species, PTU rule or Caelo fact.

AutoPTU and AutoPTU-Java remain read-only dependencies. A selected intent that needs structured combat still requires the existing explicit AutoPTU handoff. Persisting a plan selection never authorizes the narrative layer to resolve missing PTU mechanics itself.
