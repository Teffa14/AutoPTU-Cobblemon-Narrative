# Global NPC publication revision delivery contract

Status: PROPOSED / EXECUTABLE CONTRACT
Date: 2026-09-05
Scope: region-neutral persistent world-agent infrastructure

## Purpose

Connect public publication revision lineage to the existing audience, information-delivery and selective-replanning systems.

This contract composes existing Pass 282–289 systems. It does not create a second memory model, a second transport queue or a second NPC planner.

## Core invariant

A later editorial revision is a new public information event.

For a revision R2 that supersedes R1:

- R1 remains in publication history.
- prior R1 receipts remain in recipient history.
- R1-derived NPC decisions remain causally valid historical records.
- R2 resolves its audience from current service/scope/topic/receiving state.
- R2 produces independent receipt envelopes.
- only completed R2 deliveries may update recipient knowledge and trigger replanning.

`REVISION_REGISTERED != REVISION_RECEIVED`

`CURRENT_EDITORIAL_VERSION != UNIVERSAL_NPC_BELIEF`

`RECEIVED_R1 != RECEIVES_R2`

## Runtime composition

`PublicationRevisionRuntime` owns only coordination state:

- a `PublicationRevisionRegistry`;
- a per-publication bounded-expansion cursor;
- a delivery-event to publication mapping;
- per-agent publication receipt lineage.

It delegates:

- audience filtering and bounded fanout to `global_npc_publication.py`;
- transmission, latency, channel failure, backpressure and ledger delivery to `global_npc_information_network.py`;
- memory/provenance to `global_npc_memory.py`;
- selective wake-up and agenda evaluation to `global_npc_world_event_coordinator.py`;
- revision validation/current editorial version to `global_npc_publication_revision.py`.

## Audience rule

Each publication revision resolves its audience independently at expansion time.

A correction may use a different scope or channel while retaining publisher, service and topic identity required by the revision registry. Current recipient eligibility controls who gets a receipt.

The runtime must support all four meaningful states for a named NPC:

1. received original and current revision;
2. received original but missed current revision;
3. missed original but received current revision;
4. received neither.

No state may be collapsed into another.

## Delivery rule

Scheduling a receipt does not update knowledge.

A revision counts as received only after the existing information queue returns `DELIVERED` for the mapped receipt event. Failed, deferred or local-ACK-waiting deliveries do not enter received lineage and cannot wake the NPC as though the information arrived.

## Belief rule

The runtime records delivery lineage only. It never deletes previous claims from a `KnowledgeLedger` and never forces a belief result.

A recipient who holds incompatible claims can remain `CONTESTED`. A retraction states that a publisher withdrew an earlier publication. It does not prove the inverse proposition unless a separately sourced claim establishes it.

## Persistence rule

The runtime snapshot schema is `OUROS_NPC_PUBLICATION_REVISION_RUNTIME_V1`.

The snapshot preserves:

- revision registry state;
- bounded expansion cursors;
- receipt-event mappings;
- per-agent received publication IDs.

The information queue and replan queue keep their own persistence contracts. This runtime must not duplicate their snapshots.

A production restart still needs a higher-level atomic persistence coordinator covering all participating subsystem snapshots. That remains unresolved.

## Determinism

Given identical registry, audience members, queue/channel state, semantic minute, fanout budget and cursors, expansion order and delivery mappings must be deterministic.

## Region neutrality

Core code cannot contain authored place or faction conditionals. Region content supplies service, scope, topic, channel and audience membership data.

## PTU / AutoPTU boundary

Publication, receipt, memory and world-agent replanning are Ouros world-simulation behavior. They do not implement PTU combat rules.

If a delivered revision changes a world intent into a mechanically structured encounter, the existing explicit AutoPTU handoff remains mandatory.

### Capability dependencies for the reduced information-only version

No tactical engine family is required beyond existing world-agent infrastructure.

### Capability dependencies for mechanically rich consequences

Use only the families actually invoked by the encounter:

- targeting/footprints/range/LoS — required when the consequence needs tactical targeting or sight geometry;
- base movement legality — required for structured tactical movement;
- complete movement — required for push/pull/knockback/interception/forced movement;
- core calculations — required for PTU numerical resolution;
- action economy/initiative — required once structured turns begin;
- full turn/round lifecycle — required for phase/round-dependent consequences;
- full stateful damage pipeline — required for authoritative damage/injury consequences;
- status lifecycle — required for persistent combat statuses;
- terrain/weather/hazards/zones/reactions — required when those mechanics affect resolution;
- move-specific behavior — required for any special Move semantics beyond generic contracts;
- abilities — required for Ability-driven effects;
- items — required for Item-driven effects;
- Trainer Features/perks — required for Trainer interrupts or modifiers;
- AI legal-action infrastructure — required for machine-selected legal tactical options;
- AI tactical policy — required for autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback — required for complete in-world projection/acknowledgement.

No representative implementation promotes an entire family.
