# Global NPC goal / need / schedule contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-world-agent-ai-contract.md`

## Purpose

Give every named world agent the same region-neutral agenda model for durable goals, internal maintenance pressures, commitments and interruptions.

This contract governs world-level intent selection. It does not create PTU tactical policy.

## Agenda inputs

### Durable goal

Required fields:
- stable `goal_id`;
- world intent kind;
- priority;
- progress and target progress;
- knowledge/permission gates where required;
- optional target reference;
- local-projection and structured-mechanics flags.

A completed goal stops generating candidate work. Completion must be recorded by the subsystem that owns the relevant world outcome; planner selection alone does not advance progress.

### Need

Required fields:
- stable `need_id`;
- world intent kind used to address it;
- current pressure;
- activation threshold;
- critical threshold.

Needs are Ouros world-agent state. They are not PTU Status Afflictions and do not alter battle stats unless a separate adopted mechanic explicitly does so.

### Scheduled commitment

Required fields:
- stable `commitment_id`;
- world intent kind;
- semantic start/end;
- priority;
- soft/hard classification;
- optional grace window;
- knowledge/permission gates;
- optional target and handoff requirements.

States are `UPCOMING`, `DUE`, `GRACE`, `MISSED`.

Only Ouros semantic time may advance these states. Wall clock, Minecraft ticks, chunk load/unload and client presence are not schedule authority.

### Situational intent

Events may contribute an intent only through information/context the NPC legally possesses. Hidden quest truth, hidden ecology truth and other agents' private state remain unavailable.

## Selection

All eligible agenda candidates enter the existing deterministic world-intent utility layer.

A small continuity bonus may favor the currently active intent to reduce rapid oscillation. It must remain finite: a critical need, hard commitment or genuinely higher-priority event can interrupt current activity.

Stable tie-breaking remains mandatory for deterministic replay.

`CONTINUITY != UNINTERRUPTIBLE_SCRIPT`

## Missed commitments

Passing the effective deadline does not move the NPC to the destination retroactively.

A missed commitment creates a follow-up candidate such as reporting, rescheduling or other content-defined consequence.

`MISSED_SCHEDULE != TELEPORT`

`MISSED_SCHEDULE != COMPLETED_OFFSCREEN`

Whether another NPC learns of the miss is handled by communication/observation, not global omniscience.

## Off-screen behavior

Off-screen named agents may select and progress world actions whose outcomes do not need unresolved local geometry or PTU mechanics.

A commitment requiring local projection can become due while the NPC is off-screen, but that does not grant eligibility to perform a local-only action. Travel planning and later projection must resolve the gap.

## AutoPTU boundary

A goal, need, commitment or event may select an intent that needs structured mechanics. The output is `REQUEST_AUTOPTU`.

While `AUTOPTU_BOUND`, agenda replanning holds until semantic results return.

This contract does not authorize tactical target selection, footprints/range/LoS resolution, movement legality, forced movement, initiative, damage, statuses, terrain/reactions, Move behavior, Abilities, Items, Trainer Features or tactical AI policy.

## Minecraft/Cobblemon boundary

Minecraft can display working, walking, resting, meeting, waiting and other chosen local activity. It can provide navigation/presentation feedback to the world layer.

A Minecraft entity is not required for the persistent agenda to exist. Despawn does not cancel commitments. Chunk reload does not reset needs or goals.

## Scaling

Full durable agenda state is required for named persistent/recurring NPCs that matter to world continuity.

Generic crowds may use aggregate schedules and population activity bands. Promotion from aggregate background actor to persistent NPC must create explicit identity/state rather than pretending the actor always had hidden individual history.

## Current executable seam

- `tools/global_npc_ai.py`: `DurableGoal`, `NeedState`, `ScheduledCommitment`, `PlanningContext`, `choose_agenda_intent`.
- `implementation/global-npc-goal-need-schedule-fixture-v1.json`.
- `tests/test_global_npc_goals_needs_schedules.py`.

## Status boundary

This is a proposed implementation contract. Fixture values do not establish canon NPCs, regions, jobs, meal/rest requirements or schedules.
