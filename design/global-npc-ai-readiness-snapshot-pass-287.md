# Global NPC AI Readiness Snapshot — Pass 287

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository evidence

Pass 287 closes the direct private-delivery-to-world-agent-replanning seam.

Executable evidence:
- `tools/global_npc_world_event_coordinator.py`
- `implementation/global-npc-world-event-coordinator-fixture-v1.json`
- `tests/test_global_npc_world_event_coordinator.py`

The coordinator consumes successful private deliveries, updates only the explicit receiver's world-agent knowledge reference, schedules one knowledge-driven wake-up and evaluates the existing agenda planner for affected agents. Failed/deferred communication does not create knowledge or a wake-up. Duplicate materialization is rejected in-process. An `AUTOPTU_BOUND` receiver continues to return `HOLD_AUTOPTU` rather than allowing world planning to compete with structured resolution.

## Read-only AutoPTU-Java evidence

Live `main` inspected at:
`c3842c6e4c959a2d8fd9fc2704b17c2640afe4d3`

Head commit:
`Add global temporary-effect END phase registry (#365)`

Observed narrow evidence from the live commit:
- a global temporary-effect phase registry exists;
- a global temporary-effect lifecycle hook is wired after the phase envelope;
- the built-in registry contains a concrete END-phase `corrosive_tick` behavior for Corrosive Toxins;
- the implementation checks the effect's round, poison status, applies runtime tick damage, removes the temporary entry and emits an Ability event;
- the commit reports a parity test for that specific Corrosive Toxins END effect.

This is meaningful additional evidence for reusable lifecycle/temporary-effect infrastructure and one Ability-owned effect. It does not verify the complete turn/round lifecycle, full status lifecycle, full damage pipeline or complete Abilities family.

## Read-only AutoPTU Python evidence

Live `main` inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head remains:
`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly states that it is presentation-only and does not change battle rules or outcomes.

## Permanent capability-category audit

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy / initiative: VERIFIED within audited contracts;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING depending on behavior;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for autonomous structured tactical choice;
- Minecraft / Cobblemon / Craftics adapter and playback support: PARTIAL / BLOCKING end-to-end.

No family is promoted because one new representative temporary-effect hook exists.

## Pass 287 dependency interpretation

Normal delivery-to-replanning coordination is an Ouros world-agent function. It requires no AutoPTU tactical capability.

Reduced `Late Warning` consequence loops can execute through semantic world state only: delivery, belief availability, agenda reevaluation, travel replanning and schedule consequence.

A full encounter inherits only the mechanics it actually authors:
- LoS/ranged/footprint-sensitive geometry -> targeting / footprints / range / LoS;
- ordinary capability traversal -> base movement legality;
- interception/push/pull/knockback/forced movement -> complete movement;
- deterministic battle arithmetic -> core calculations;
- action timing/initiative -> action economy / initiative;
- phase/delayed/round-scoped behavior -> full turn / round lifecycle;
- persistent HP/damage-hook behavior -> full stateful damage pipeline;
- persistent status timing -> status lifecycle;
- weather/hazards/zones/reactions -> terrain / weather / hazards / zones / reactions;
- special Move clauses -> move-specific behavior;
- Ability-owned effects -> abilities;
- Item-owned effects -> items;
- Trainer interrupts/features -> Trainer Features / perks;
- legal tactical option construction -> AI legal-action infrastructure;
- autonomous tactical choice -> AI tactical policy;
- visible end-to-end playback -> Minecraft / Cobblemon / Craftics adapter/playback support.

The new Corrosive Toxins END hook does not authorize a narrative concept to assume arbitrary delayed Ability/status interactions are available.

## PTU / Caelo / Kairos authority

Pass 287 adopts no new PTU, Caelo or Kairos rule.

Information delivery, world-agent wake-up, coordinator ordering and semantic replanning remain Ouros MMO simulation policy. The existing authority rule remains binding:

`SOURCE_HAS_RULE != OUROS_USES_RULE`

## Open implementation risks

- durable persistence of NPC knowledge ledgers and the coordinator's delivery-materialization guard;
- public/broadcast/publication channels with explicit audience expansion and retention rules;
- fairness and aging under sustained message/replan backlog;
- explicit replan processing budget at large scale;
- forgetting, memory revision, deception and source confusion;
- resource/inventory-aware intent generation;
- belief-aware dialogue/context projection;
- production local-adapter acknowledgement and result correlation;
- scale tests with thousands of named agents and queued world events.
