# Global NPC Assistance Active Replacement Start Contract — Pass 453

Status: IMPLEMENTED SUPPORT CONTRACT
Canon effect: NONE
Date: 2026-09-12

## Purpose

Pass 452 admitted pre-start viability evidence for the currently active replacement generation. The existing Pass 439 start owner still resolved only original commitments.

Pass 453 bridges the existing start ledger to an active replacement leaf without creating a parallel start-state model.

## Contract

`arm_active_replacement_start_watch(...)` resolves the full assistance lineage and fails unless the requested commitment is the current leaf. It stores the ordinary `AssistanceCommitmentStartWatch` and schedules the responder-only `SCHEDULE_DUE` wake at the replacement start minute.

`assess_active_replacement_start(...)` evaluates the latest viability evidence for that same leaf at the exact active start minute. `BLOCKED` becomes `BLOCKED_AT_START`; `AT_RISK` becomes `AT_RISK_AT_START`; no evidence or a latest `RESTORED` record produces no adverse assessment.

The assessment preserves the exact viability observation, constraint, evidence and provenance. Superseded generations cannot receive new watches or assessments.

## Boundaries

This pass does not alter any commitment, create another replacement, choose a disposition, send a message, reserve travel, grant access, allocate resources, move an actor, assign blame, change relationships, complete assistance or invoke AutoPTU.

The historical root remains durable while only the current lineage leaf governs the watched start.

## Mechanical capability posture

This bridge requires no battle capability family. Any later structured scene must independently declare targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

No family is promoted by this pass.

## Verification

`tests/test_global_npc_assistance_replacement_start.py` covers exact-minute assessment, active-leaf enforcement, restoration, idempotent watch replay and side-effect boundaries.
