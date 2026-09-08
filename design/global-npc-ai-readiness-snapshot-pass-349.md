# Global NPC AI readiness snapshot — Pass 349

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-08

## Narrative repository evidence

Starting head inspected recursively: `3113238619de917b810dba5e9d8983864332ba15`.

Pass 349 adds an allocation-application seam after Pass 348. The new layer preserves the original Pass 339 reservation ledger while producing a deterministic operational projection for an authorized displacement decision.

Implementation evidence added in this pass:
- `tools/global_npc_resource_allocation_application.py`;
- `tests/test_global_npc_resource_allocation_application.py`;
- `implementation/global-npc-resource-allocation-application-regression-v1.json`;
- `design/global-npc-resource-allocation-application-contract-pass-349.md`;
- `research/2026-09-08-allocation-displacement-provenance-scan-349.md`;
- `proposals/2026-09-08-the-booking-in-the-old-ledger-case-349.md`;
- Global NPC AI workflow trigger updated for the new module.

`Global NPC AI Regressions` run #221 on implementation head `c7fa942aa6edcd69644de8b4c15e6d5ea76126fb` completed successfully before this snapshot commit.

## Read-only AutoPTU-Java evidence

Live head inspected: `bc7a39a2d28d1571c11bdebacca358fa0a8bb0e3`, merge of PR #399, `Project Arena Trap targets from authoritative runtime content`.

Direct commit evidence confirms:
- `ArenaTrapRuntimeCandidateProjection` consumes server-owned `BattleRuntimeState`, `CombatantRuleContentRegistry`, `MovementProfile` and core `Targeting.chebyshevDistance`;
- Minecraft/Cobblemon adapters do not provide a pre-resolved Arena Trap target or immunity list;
- runtime projection carries affiliation/activity, HP, distance, types, abilities, PTU capabilities, numeric Sky and numeric Burrow into the language-neutral targeting contract;
- oracle parity includes capability-backed Levitate and movement-speed cases;
- the head has 77 Actions runs; sampled head runs are completed successfully.

Interpretation:
This is strong evidence for one narrow Ability target/candidate projection seam. It does not prove stateful Arena Trap application, the entire Slowed lifecycle, all Ability behavior, complete movement or tactical objective policy.

## Read-only AutoPTU Python evidence

Live head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The head commit states that its change is presentation-only and does not alter battle rules or outcomes. No capability family is promoted from this Python head.

## Permanent capability classification

Targeting / footprints / range / LoS: VERIFIED within previously audited ordinary contracts. PR #399 strengthens authoritative runtime candidate projection for Arena Trap but remains a narrow Ability case.

Base movement legality: VERIFIED within previously audited ordinary movement contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Numeric movement representation and Arena Trap candidate projection do not establish carrying, interception, rescue, forced displacement or all movement interactions.

Core calculations: VERIFIED within previously audited ordinary deterministic arithmetic contracts.

Action economy / initiative: VERIFIED for audited primitives. Exact pickup, drop, handoff, guard, escort or cargo-preservation actions remain individually gated.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap target/runtime projection does not establish complete Slowed application, duration, stacking or cleanup.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL. Air Lock has a narrow stateful round-start slice and Arena Trap has stronger target eligibility/runtime projection; neither establishes the Ability family as complete.

Items: PARTIAL. A Narrative `WorldResource` must not be treated as a PTU Item without exact source/content identity and Java evidence.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope.

AI tactical policy: BLOCKING for escort, protect-carrier, delivery-first, preserve-instrument, route-priority and disengage-after-objective behavior.

Minecraft / Cobblemon / Craftics adapter and playback: PARTIAL / BLOCKING end-to-end. PR #399 is positive architectural evidence because the adapter does not author Arena Trap targeting semantics, but full battle/world playback remains incomplete.

## Pass 349 encounter impact

The reduced `The Booking in the Old Ledger` case requires no AutoPTU capability. It depends on semantic world state, reservations, conflict assessment, authorized allocation decision, allocation application, communications, memory/belief and replanning only when the chosen branch uses notification or stale knowledge.

The rich route-interruption version remains gated by exact tactical needs. Escort/interception/carrying depends on complete movement and tactical policy. Round deadlines depend on full lifecycle. Damage to a mechanically represented objective depends on the stateful damage pipeline. Any status, weather, hazard, reaction, Move, Ability, Item or Trainer Feature remains gated by its exact capability family.

## Unresolved mechanics and canon questions

- exact Caelo policy for institutional displacement of an already-valid reservation;
- whether application itself should create an explicit notification obligation or a later coordinator should own that bridge;
- how to represent a displacement reason in downstream UI without flattening it into ordinary holder cancellation;
- whether an affected reservation holder has appeal/review rights under any authored institution;
- how repeated allocation applications become evidence for the existing Procurement owner without automatically creating or approving a purchase;
- checkpoint integration for Pass 339 and Pass 342–349 resource ledgers;
- exact PTU/Caelo identity of any field instrument later intended to act as a mechanical Item;
- tactical cargo/escort objective support;
- stateful Arena Trap effect and status-lifecycle completion;
- full Minecraft/Cobblemon/Craftics presentation of historical booking versus current operational allocation state.

No unresolved item is promoted to canon or engine readiness.
