# Global NPC Selective Decision Consequence Repair Contract

Status: DESIGN CONTRACT / EXECUTABLE FOUNDATION
Pass: 312
Date: 2026-09-06

## Purpose

A reviewed decision may have produced several downstream world consequences. A later correction must be able to change the specific consequence that depended on the reviewed decision without silently rewinding unrelated history.

This contract extends:
- `global-npc-assessment-decision-dependency-contract.md`;
- `global-npc-assessment-decision-review-contract.md`;
- the non-omniscient knowledge and provenance rules in `CURRENT_FOCUS.md`.

## Core invariant

`DECISION_REVIEW != WORLD_RESET`

A review outcome creates authority to evaluate downstream effects. It does not by itself change routes, permissions, money, reputation, relationships, schedules, faction standing, publications or memories.

Each operational consequence must be represented explicitly and repaired explicitly.

## Executable objects

`DecisionConsequence` records one effect produced by one historical decision. It preserves:
- stable consequence ID;
- source decision ID;
- consequence family;
- affected subject;
- semantic application time;
- authored value reference.

`ConsequenceRepair` records one later action against one consequence. Supported actions are:
- `RETAIN`;
- `AMEND`;
- `CEASE`.

Historical consequence and repair rows are append-only. `effective_consequence()` derives current operational state from that history.

## Review compatibility

A `DEFER` review cannot change a consequence.

A `MAINTAIN` review may only `RETAIN` the consequence.

An `AMEND` review may `AMEND` or `RETAIN` a consequence. `AMEND` requires an explicit replacement value reference.

A `RESCIND` review may `CEASE` the consequence. It may `RETAIN` the consequence only when an explicit `independent_basis_ref` explains why that same operational effect still has a separate current basis.

A rescinded decision cannot be used through this seam to invent a new amended consequence. That requires a new decision or another authored authority path.

## Selectivity

A repair targets exactly one `consequence_id`.

If a route restriction produced a closed gate, a public notice, a cancelled delivery and a trust loss, ceasing the gate does not:
- remove the public notice;
- restore the cancelled delivery;
- refund money;
- change a relationship;
- retract a publication;
- erase anyone's memory.

Those are separate facts with separate provenance and require their own repair seams.

## Independent basis rule

A consequence can outlive rescission of its original decision only when the retaining actor records another basis.

Example: a road restriction originally rested on a custody concern. The custody concern is corrected and the restriction is rescinded. A later structural inspection independently shows the bridge is unsafe. The gate may remain closed, but its continuing closure must reference the structural inspection rather than pretending the original custody basis is still valid.

The current runtime stores the independent basis reference. Validation that the referenced inspection, permission or world fact really exists belongs to the future typed consequence adapters for that domain.

## Time and identity guards

A consequence cannot predate its source decision.

A repair cannot predate either the consequence or the review that authorizes it.

A review may only repair consequences created by the decision it reviewed.

Once a consequence is `CEASED`, this V1 seam cannot reactivate it. Reopening a ceased effect must be represented by a new consequence or later explicit extension rather than mutating history.

## Persistence

`DecisionConsequenceRepairRegistry` has schema `OUROS_NPC_DECISION_CONSEQUENCE_REPAIR_V1`.

Its snapshot preserves all consequence rows and repair rows. Atomic world-checkpoint integration is still unresolved and must be added before this subsystem is considered crash-consistent with the full NPC world state.

## Boundaries

This layer does not itself mutate:
- `RelationshipState`;
- faction membership or permissions;
- information/publication receipt;
- inventory or economy;
- Minecraft blocks/entities;
- route graphs;
- AutoPTU battle state.

Future adapters may consume effective consequence state and apply domain-specific mutations with their own provenance and idempotency contracts.

## Narrative use

This contract supports stories where a corrected report changes only part of the world response. It also allows legitimate persistence of an effect under a new independent basis, which is important for investigations where an accusation was wrong but a separate hazard was real.
