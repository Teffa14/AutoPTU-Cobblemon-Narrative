# Global NPC AI Readiness Snapshot — Pass 288

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository evidence

Pass 288 adds executable public-publication receipt expansion without creating universal NPC knowledge.

Executable evidence:
- `tools/global_npc_publication.py`
- `implementation/global-npc-publication-broadcast-fixture-v1.json`
- `tests/test_global_npc_publication.py`

A public publication consumes explicit publisher/source claim, service, scope, topic, channel and optional retention state. Eligible persistent actors are expanded in bounded stable batches and scheduled through the existing `InformationEventQueue`. Individual ledger mutation still occurs only when delivery completes. Scope/service mismatch, disabled reception or expired retention cannot create a receipt.

This implementation complements the older Pass 161 broadcast-continuity architecture; it does not replace ownership of programs, episodes, transmissions, corrections or network topology.

## Read-only AutoPTU-Java evidence

Live `main` inspected at:
`6fbfb06ad662c7adb55ce46dded5bfd5789986f7`

Head commit:
`Extract declarative TURN_END temporary-effect refresh (#366)`

Observed narrow evidence:
- a reusable `TemporaryEffectRefreshLifecycleHook` now replaces an effect family with a fresh entry at an explicit lifecycle hook point;
- ACTOR and ALL_COMBATANTS scopes exist in the new helper;
- the built-in TURN_END registry now separates `extra_action` cleanup from `last_turn_round` refresh;
- dedicated tests cover the declarative refresh behavior.

This strengthens evidence for reusable temporary-effect/lifecycle infrastructure. It still does not verify the complete turn/round lifecycle, status lifecycle, stateful damage pipeline or every effect owner family.

## Read-only AutoPTU Python evidence

Live `main` inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head remains:
`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly describes itself as presentation-only and states that battle rules/outcomes do not change.

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

No family is promoted from the new TURN_END refresh seam alone.

## Pass 288 dependency interpretation

Public publication expansion, receipt scheduling, retention filtering and belief arrival are Ouros world-simulation functions. They require no AutoPTU tactical capability.

The reduced Public Warning / Divergent Reception loop can run through publication, receipt, knowledge, replanning, travel and schedule state only.

If a late warning creates a structured encounter, that encounter inherits exactly the selected mechanics:
- targeting / footprints / range / LoS for line/range/footprint-sensitive geometry;
- base movement legality for ordinary capability traversal;
- complete movement for interception/push/pull/knockback/forced movement;
- core calculations for deterministic battle arithmetic;
- action economy / initiative for structured action timing;
- full turn / round lifecycle for delayed/phase/round-scoped behavior;
- full stateful damage pipeline for persistent HP/damage hooks;
- status lifecycle for timed/persistent statuses;
- terrain / weather / hazards / zones / reactions for those environmental mechanics;
- move-specific behavior, Abilities, Items and Trainer Features/perks only when individually authored;
- AI legal-action infrastructure for legal option construction;
- AI tactical policy for autonomous tactical selection;
- Minecraft / Cobblemon / Craftics adapter/playback for visible end-to-end authoritative playback.

## PTU / Caelo / Kairos authority

Pass 288 adopts no new PTU, Caelo or Kairos rule. Public-media access, scope filtering, retention and expansion budgets are explicit Ouros MMO simulation policy.

`SOURCE_HAS_RULE != OUROS_USES_RULE`

## Open implementation risks

- persistent/indexed audience membership for very large populations rather than caller-supplied candidate sets;
- durable persistence of publication expansion cursors and materialized-receipt guards;
- corrections/retractions wired through actual Media information-revision objects;
- fairness and aging across simultaneous large publications and private communication backlog;
- replan budgets after a large public event creates many legitimate wake-ups;
- durable memory ledgers;
- forgetting, deception and source confusion;
- resource/inventory-aware intent generation;
- belief-aware dialogue/context projection;
- production Minecraft acknowledgement for local public surfaces;
- scale tests with thousands of eligible named agents.
