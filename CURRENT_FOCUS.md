# Current Ouros Development Focus

Status: ACTIVE
Date amended: 2026-09-05

## Primary implementation focus

Build the global NPC / world-agent AI used by persistent and recurring NPCs everywhere in Ouros.

Authoritative working directive:
- `design/global-npc-world-agent-ai-contract.md`

The global system must cover NPC identity, goals, needs, schedules, obligations, relationships, factions/institutions, permissions, knowledge, memory, risk, travel, communication, world-level decisions, local projection and explicit AutoPTU handoff.

Marea, Sendero, Puerto Bruma and any other authored place are content bindings and regression sites only. They must not define the core NPC AI architecture.

`LOCAL_FIXTURE != GLOBAL_NPC_AI`

## Ecology status

The ecology program remains an ACTIVE mandatory subsystem and an important input into NPC decisions:
- `design/ecology-development-program.md`
- `design/global-species-interaction-graph.md`

However, this file supersedes the old ecology-only project-focus restriction. Ecology no longer monopolizes every Ouros development pass.

Do not continue producing Marea-specific NPC governance, stewardship or institutional passes merely because they are attached to ecology. Local ecology work is justified when it validates a reusable global subsystem or closes an actual ecology implementation gap.

NPC AI must also work for non-ecology goals such as work, travel, training, commerce, social relationships, rivalry, investigations, logistics, faction obligations and emergencies.

## Global NPC invariants

- one region-neutral core planner for all persistent/recurring NPCs;
- no Marea/Sendero special cases in core AI;
- NPCs are non-omniscient and act only on knowledge available to them;
- named NPCs persist and can plan while off-screen without a Minecraft entity;
- Minecraft/Cobblemon is presentation, not NPC identity or decision authority;
- world-agent AI does not duplicate AutoPTU tactical AI;
- structured mechanics require an explicit `REQUEST_AUTOPTU` handoff;
- while AutoPTU owns resolution, the world planner must not compete with it;
- deterministic replay is required for identical agent state;
- generic crowds may remain aggregate; persistence is required only when an individual matters.

## Current executable foundation

Base planner:
- `tools/global_npc_ai.py`
- `implementation/global-npc-ai-agent-fixture-v1.json`
- `tests/test_global_npc_ai.py`

Pass 279 agenda layer:
- `design/global-npc-goal-need-schedule-contract.md`
- `implementation/global-npc-goal-need-schedule-fixture-v1.json`
- `tests/test_global_npc_goals_needs_schedules.py`

Durable goals, need pressure, semantic-time commitments, finite intent continuity and missed-commitment follow-up have executable coverage.

Pass 280 social layer:
- `design/global-npc-social-relationship-faction-contract.md`
- `tools/global_npc_social.py`
- `implementation/global-npc-social-relationship-faction-fixture-v1.json`
- `tests/test_global_npc_social_relationships_factions.py`

Directional relationships, provenance-backed social change, explicit faction duties/permissions, non-hive-mind knowledge and rivalry-to-AutoPTU boundaries now have executable coverage.

The immediate next slice should implement world travel planning and reservation of travel time so schedules and social commitments cannot teleport NPCs between locations. After that, deepen memory revision, NPC-to-NPC communication, dialogue projection and scalable event scheduling. All must consume the same global agenda rather than fork per region.

Do not make the next NPC-AI pass Marea-specific unless Marea is only being used to test the global contract.
