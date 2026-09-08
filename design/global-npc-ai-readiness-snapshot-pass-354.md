# Global NPC AI / AutoPTU readiness snapshot — Pass 354

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

## Narrative repository head inspected

Base inspected before Pass 354: `c4b97c4eea20d80eda560911a3b41e47c780fbf2`.

Pass 353 had already frozen standalone persistence for reservations and resource requests but had not put them inside the atomic world checkpoint. Pass 354 addresses that narrow durability gap through `OUROS_NPC_WORLD_CHECKPOINT_V6` in `tools/global_npc_world_resource_checkpoint.py`.

## AutoPTU-Java live evidence

Read-only repository head inspected: `59dadcd6a3671ea962eacf7a14acf4305e9e85f7`, merge of PR #404, `Freeze Python Intimidate trigger lifecycle contract`.

PR #404 adds a server-owned `IntimidateTriggerContract` with parity against the pinned Python oracle. The verified contract checks whether the holder is active, conscious, has Intimidate, joined during the current round and has not already used Intimidate during that round. It then selects adjacent active, conscious opponents within Chebyshev distance 1 in authoritative combatant order.

The PR explicitly stops before Attack Combat Stage mutation and semantic effect execution. It therefore strengthens an Ability trigger/lifecycle and targeting seam without proving the full Intimidate effect or the complete Ability family.

Previous live evidence remains relevant: Arena Trap has authoritative target projection, effect planning, stateful Slowed application and round-start dispatch. That representative path still does not prove every Ability or the complete status lifecycle.

## AutoPTU Python oracle

Read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The head commit describes its change as presentation-only and states that battle rules and outcomes do not change. Python remains the pinned oracle for parity work while the Java port is incomplete.

## Capability classification

Targeting / footprints / range / LoS: VERIFIED within previously audited ordinary contracts. PR #404 adds narrow evidence for Intimidate adjacent-opponent selection; it does not promote all Ability or Move-specific targeting.

Base movement legality: VERIFIED within the audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Cargo/interception branches in Pass 354 remain gated.

Core calculations: VERIFIED within the audited deterministic arithmetic scope.

Action economy / initiative: VERIFIED for audited primitives. Special cargo pickup/drop/handoff actions still need explicit contracts.

Full turn/round lifecycle: PARTIAL. PR #404 strengthens current-round join/once-per-round trigger gating for one Ability. Previous Arena Trap work strengthens round-start dispatch. The whole lifecycle is not yet verified.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap can authoritatively apply Slowed, but complete expiration/cleanup and all consumers remain unverified.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Arena Trap and Intimidate now have stronger representative contracts, but neither justifies category-wide readiness.

Items: PARTIAL and individually gated.

Trainer Features / perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within the audited ordinary legal-action scope. New cargo/objective actions require their own legal definitions.

AI tactical policy: BLOCKING for delivery-first, escort, protect-carrier, intercept-to-inform, preserve-resource and disengage-after-objective behavior.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for new cargo/objective semantics and complete playback/acknowledgement.

## Pass 354 encounter implication

`The Request After the World Woke` has a reduced version that requires no AutoPTU battle. It uses persistent world time, reservations, requests, schedules, communication and later allocation logic.

A full tactical delivery version can use ordinary targeting and base movement only where those verified scopes suffice. Interception, forced movement, cargo ownership, round deadlines, persistent status effects, environmental zones, Ability effects or Trainer interrupts each retain their exact capability dependency.

No mechanic is promoted because one representative test exists.

## Open engine questions

Intimidate still needs the Attack Combat Stage mutation/effect path frozen and implemented against Python, including any prevention/reaction interactions that matter to the oracle.

Arena Trap still needs complete Slowed expiration/cleanup evidence and proof that all relevant movement consumers respect the status.

Objective-aware tactical policy remains the largest blocker for encounters where success is delivery, escape, protection or interception rather than elimination.

Minecraft/Cobblemon/Craftics still needs end-to-end authoritative playback for any new world-to-battle cargo/objective contract.

## Open Ouros durability questions

Pass 354 persists only Pass 339 reservations and Pass 342 requests inside the new V6 integration entrypoint.

Passes 343–352 still need incremental checkpoint codecs and cross-ledger validation.

The global workflow path filter does not yet name `tools/global_npc_resource_checkpoint.py` or `tools/global_npc_world_resource_checkpoint.py` explicitly; current Pass 354 changes are still exercised because the new `tests/test_global_npc_*.py` path triggers the suite. A later maintenance slice should make the tool-path trigger explicit.
