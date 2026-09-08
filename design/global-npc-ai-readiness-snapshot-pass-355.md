# Global NPC AI / AutoPTU readiness snapshot — Pass 355

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

## Narrative repository head inspected

Base inspected before Pass 355: `6bfb6275482dee88be7021ba7c9dc81ee38f8914`.

The recursive repository tree was inspected before writing. Pass 354 had already integrated Pass 339 reservations and Pass 342 requests into world checkpoint V6. Pass 355 extends the standalone resource checkpoint boundary to Pass 343 handoff authorization and custody transfer history. Global V6 integration of this new V2 bundle is intentionally deferred to the next durability slice.

## AutoPTU-Java live evidence

Read-only repository head inspected: `306a7b21b888b3326877043bb4475a6c44edda47`, merge of PR #405, `Execute baseline Intimidate through combat-stage pipeline`.

PR #405 routes baseline Intimidate Attack Combat Stage mutation through the authoritative `CombatStageMutationService`, records the once-per-round marker in server-owned temporary state, emits a semantic `CombatStageChangedEvent`, and compares the resulting state/events against a pinned Python fixture.

The PR body explicitly limits scope. Clear Body, Flower Veil, Mirror Armor, Defiant and related prevention/reaction ordering remain follow-up work before Intimidate can be considered a complete round-start Ability path.

This is stronger evidence than Pass 354 for one representative Ability effect. It does not prove the complete Ability family, complete reaction family or full round lifecycle.

Previous Arena Trap evidence remains: authoritative holder discovery, target projection, effect planning, stateful Slowed mutation and round-start handler integration exist for that representative contract. Complete Slowed expiration/cleanup and all movement consumers remain unverified.

## AutoPTU Python oracle

Read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head commit states that the change is presentation-only and does not alter battle rules or outcomes. Python remains the authoritative parity oracle while the Java port is incomplete.

## Capability classification

Targeting / footprints / range / LoS: VERIFIED within previously audited ordinary contracts. Arena Trap and Intimidate add narrow representative evidence only.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. The rich Pass 355 carrier/interception variant remains gated.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy / initiative: VERIFIED for audited primitives. Explicit tactical pickup, drop and handoff actions still need their own legal contracts.

Full turn/round lifecycle: PARTIAL. Intimidate now has current-round/once-per-round trigger evidence and baseline effect execution; Arena Trap has round-start dispatch evidence. The complete lifecycle remains unproven.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap can apply Slowed authoritatively; complete expiration/cleanup and all status consumers remain unverified.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact family. PR #405 specifically leaves several prevention/reaction interactions for later differential work.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Arena Trap and baseline Intimidate have stronger representative paths but do not justify category-wide promotion.

Items: PARTIAL and individually gated.

Trainer Features / perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary legal-action scope. Cargo-specific interaction actions remain undefined.

AI tactical policy: BLOCKING for delivery-first, escort, protect-carrier, intercept-to-stop, preserve-resource and disengage-after-objective behavior.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for cargo/objective semantics and complete authoritative playback/acknowledgement.

## Pass 355 encounter implication

`The Transfer Before the Restart` has a reduced version that requires no AutoPTU battle. It uses semantic time, resource request/handoff history, checkpoint persistence, memory/belief, communication and ordinary world travel.

The mechanically rich courier version requires only the capability families it actually uses. Ordinary positioning can rely on verified base movement. Interception or forced displacement requires complete movement. Round deadlines require full lifecycle. Persistent conditions require status lifecycle. Environmental complications retain their own terrain/weather/hazard/zone/reaction gate. Moves, Abilities, Items and Trainer Features remain individually gated.

No missing PTU mechanic may be implemented inside the Minecraft adapter to make this encounter work.

## Open engine questions

Intimidate still needs differential coverage for prevention/reaction interactions such as Clear Body, Flower Veil, Mirror Armor, Defiant and any other oracle-visible cases before a complete Ability path can be claimed.

Arena Trap still needs complete Slowed expiration/cleanup evidence and proof that all relevant movement consumers respect it.

Objective-aware tactical policy remains a blocker for delivery, protection, interception and escape objectives whose success condition is not elimination.

Minecraft/Cobblemon/Craftics still needs end-to-end authoritative cargo/objective playback if such semantics are introduced.

## Open Ouros durability questions

Pass 355 freezes `OUROS_NPC_RESOURCE_CHECKPOINT_V2` with Pass 343 authorization/custody history, but world checkpoint V6 still embeds the earlier V1 resource bundle.

The next durability slice should advance the coherent world checkpoint with V2 while restoring V6 with an empty handoff ledger rather than inferred history.

Passes 344–352 still need incremental codecs: failed attempts, appointments, reschedules, allocation admission/decisions/application, notice obligations/links and related provenance.

`tools/global_npc_resource_checkpoint.py` and `tools/global_npc_world_resource_checkpoint.py` are still not named explicitly in the workflow path filter. The current change is exercised because `tests/test_global_npc_*.py` triggers the suite; isolated future edits to the checkpoint tool should eventually receive explicit path coverage.
