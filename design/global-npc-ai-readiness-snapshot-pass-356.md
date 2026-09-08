# Global NPC AI / AutoPTU readiness snapshot — Pass 356

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

## Narrative repository head inspected

Base inspected before Pass 356: `4be107124d451ffe5612704f2b3ea355ff1306a5`.

The recursive repository tree was inspected before writing. Pass 355 had already validated the standalone `OUROS_NPC_RESOURCE_CHECKPOINT_V2` with Pass 343 handoff authorization and custody-transfer history. Pass 356 integrates that V2 bundle into coherent world checkpoint V7 while preserving V6 compatibility with an empty handoff ledger.

## AutoPTU-Java live evidence

Read-only repository head inspected: `93d90167ae73191e38916c6a64914c66fd3c3e84`, merge of PR #406, `Freeze Intimidate target-owned prevention interactions`.

PR #406 differentially exercises Intimidate against four target-owned Combat Stage prevention Abilities: Clear Body, Full Metal Body, White Smoke and Hyper Cutter. It compares final Attack Combat Stage plus ordered prevention/Intimidate semantic events with the pinned Python oracle through the existing authoritative Intimidate execution path.

The PR explicitly leaves Flower Veil spatial prevention, Mirror Armor reflection and Defiant/Competitive post-apply reactions for later work. No controller or Minecraft adapter rule logic is added.

This strengthens one representative Ability path and part of the reactions/prevention surface. It does not establish complete Ability coverage, complete reaction coverage or complete round lifecycle coverage.

Previous Arena Trap evidence remains: authoritative holder discovery, target projection, effect planning, stateful Slowed mutation and round-start handler integration exist for that representative contract. Complete Slowed expiration/cleanup and proof that all movement consumers respect it remain unverified.

## AutoPTU Python oracle

Read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head commit states that the change is presentation-only and does not alter battle rules or outcomes. Python remains the authoritative parity oracle while the Java port is incomplete.

## Capability classification

Targeting / footprints / range / LoS: VERIFIED within previously audited ordinary contracts. Arena Trap and Intimidate add narrow representative evidence only.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. The rich Pass 356 courier/interception variant remains gated.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy / initiative: VERIFIED for audited primitives. Explicit tactical pickup, drop and handoff actions still need their own legal contracts.

Full turn/round lifecycle: PARTIAL. Intimidate has current-round/once-per-round trigger and prevention-path evidence; Arena Trap has round-start dispatch evidence. The complete lifecycle remains unproven.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap can apply Slowed authoritatively; complete expiration/cleanup and all status consumers remain unverified.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact family. PR #406 verifies four target-owned prevention interactions only. Spatial prevention, reflection and post-apply reaction families remain open.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Arena Trap and Intimidate have stronger representative paths but do not justify category-wide promotion.

Items: PARTIAL and individually gated.

Trainer Features / perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary legal-action scope. Cargo-specific interaction actions remain undefined.

AI tactical policy: BLOCKING for delivery-first, escort, protect-carrier, intercept-to-stop, preserve-resource, reroute and disengage-after-objective behavior.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for cargo/objective semantics and complete authoritative playback/acknowledgement.

## Pass 356 encounter implication

`The Crate That Crossed the Save` has a reduced version that requires no AutoPTU battle. It uses semantic time, reservations, resource requests, handoff history, coherent checkpoint restore, memory/belief, communication and ordinary world travel.

The mechanically rich courier version requires only the capability families it actually uses. Ordinary positioning can rely on verified base movement. Interception or forced displacement requires complete movement. Tactical cargo interactions require action economy plus legal-action contracts. Round deadlines require full lifecycle. Persistent conditions require status lifecycle. Environmental complications retain their own terrain/weather/hazard/zone/reaction gate. Moves, Abilities, Items and Trainer Features remain individually gated.

No missing PTU mechanic may be implemented inside the Minecraft adapter to make this encounter work.

## Open engine questions

Intimidate still needs Flower Veil spatial prevention, Mirror Armor reflection, Defiant/Competitive post-apply reactions and any other oracle-visible nested interactions before a complete Ability path can be claimed.

Arena Trap still needs complete Slowed expiration/cleanup evidence and proof that all relevant movement consumers respect it.

Objective-aware tactical policy remains a blocker for delivery, protection, interception, rerouting and escape objectives whose success condition is not elimination.

Minecraft/Cobblemon/Craftics still needs end-to-end authoritative cargo/objective playback if such semantics are introduced.

## Open Ouros durability questions

World checkpoint V7 now includes Pass 339 reservations, Pass 342 requests and Pass 343 handoff authorization/custody history in one integrity boundary.

Passes 344–352 still need incremental codecs: failed attempts, appointments, reschedules, allocation admission/decisions/application, notice obligations/links and related provenance.

The global workflow still relies on test/design path changes to trigger checkpoint regressions. Explicit path-filter entries for `tools/global_npc_resource_checkpoint.py` and `tools/global_npc_world_resource_checkpoint.py` remain a worthwhile reliability follow-up.
