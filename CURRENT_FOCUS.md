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
- generic crowds may remain aggregate; persistence is required only when an individual matters;
- event-driven wake-up is preferred over global per-tick replanning for persistent world agents;
- information recipients must be explicit; shared faction membership never implies broadcast knowledge;
- private communication overload defers due work by default instead of silently destroying world information.

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

Directional relationships, provenance-backed social change, explicit faction duties/permissions, non-hive-mind knowledge and rivalry-to-AutoPTU boundaries have executable coverage.

Pass 281 travel layer:
- `design/global-npc-world-travel-contract.md`
- `tools/global_npc_travel.py`
- `implementation/global-npc-travel-fixture-v1.json`
- `tests/test_global_npc_travel.py`

World-route planning, travel-time reservation, deterministic ETA, off-screen semantic movement, knowledge/permission-gated routes, replanning, no-teleport lateness, local projection boundaries and AutoPTU interruption handoff have executable coverage.

Pass 282 memory / belief / communication layer:
- `design/global-npc-memory-belief-communication-contract.md`
- `tools/global_npc_memory.py`
- `implementation/global-npc-memory-belief-communication-fixture-v1.json`
- `tests/test_global_npc_memory.py`

Per-agent claim ledgers, explicit information transfer, report attenuation, provenance lineage, duplicate-source suppression, contradictory evidence and deterministic belief assessment have executable coverage. Shared faction membership still does not create hive-mind knowledge.

Pass 283 event-driven information propagation layer:
- `design/global-npc-event-driven-information-propagation-contract.md`
- `tools/global_npc_information_network.py`
- `implementation/global-npc-information-propagation-fixture-v1.json`
- `tests/test_global_npc_information_network.py`

Semantic-time message queues, channel latency/availability, due-only processing, deterministic delivery order, provenance-preserving relays, same-root suppression, local projection acknowledgement and idempotent in-process delivery have executable coverage. Delivery results expose sender/receiver identity for selective downstream routing.

Pass 284 event-triggered replanning layer:
- `design/global-npc-event-triggered-replanning-contract.md`
- `tools/global_npc_replanning.py`
- `implementation/global-npc-event-replanning-fixture-v1.json`
- `tests/test_global_npc_event_replanning.py`

Meaningful semantic changes can wake only affected named agents. Multiple simultaneous triggers for one agent coalesce into one agenda reevaluation while preserving cause/provenance. Replan triggers persist across snapshot/restore and completed triggers do not replay. Successful information delivery can update private knowledge and make a new world intent eligible without polling every NPC.

Pass 285 audience / recipient resolution layer:
- `design/global-npc-audience-recipient-resolution-contract.md`
- `tools/global_npc_audience.py`
- `implementation/global-npc-audience-resolution-fixture-v1.json`
- `tests/test_global_npc_audience.py`

A sender can rank explicit communication recipients from directional relationships, explicit institutional receiving duties, reachability, proximity/contact opportunity, topic relevance and role relevance under a deterministic fanout budget. Shared faction membership alone contributes no audience and cannot broadcast private knowledge.

Pass 286 durable communication runtime:
- `design/global-npc-communication-runtime-contract.md`
- `tools/global_npc_communication_runtime.py`
- updated `tools/global_npc_information_network.py`
- `implementation/global-npc-communication-runtime-fixture-v1.json`
- `tests/test_global_npc_communication_runtime.py`

Audience selections can now schedule real private envelopes through deterministic channels. The information queue persists pending deliveries, delivery status, delivered IDs and local-ack waits across snapshot/restore. Budgeted processing exposes deferred backlog and preserves undelivered private events instead of dropping them under load.

The immediate next slices should deepen direct delivery-to-replanning coordination, public/broadcast/publication channels with explicit audience expansion and retention policy, sustained-load fairness/backlog aging, durable memory-ledger persistence, forgetting and memory revision, deception/source confusion, resource/inventory-aware intents, belief-aware dialogue/context projection and production Minecraft acknowledgement. These systems must consume the same global agenda/travel/social/memory/information/replanning state rather than fork per region.

Do not make the next NPC-AI pass Marea-specific unless Marea is only being used to test the global contract.
