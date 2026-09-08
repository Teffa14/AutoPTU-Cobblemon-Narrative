# Global NPC AI / AutoPTU readiness snapshot — Pass 358

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

Narrative base inspected before writing: `741dba9833da7f2f58c88d9fb797e9f9f24c0bfe`. The recursive repository tree was inspected first. Pass 357 added `OUROS_NPC_RESOURCE_CHECKPOINT_V3` for failed handoff attempts while leaving the coherent world checkpoint at V7. Pass 358 integrates that V3 history into world recovery as V8.

AutoPTU-Java live evidence

Read-only head inspected: `bcdab77cc407919b407c7048bdc862f58e2a97f0`, merge of PR #407, `Freeze Intimidate Flower Veil spatial prevention`.

The live PR differentially verifies Intimidate against standard Flower Veil and Flower Veil [Errata], including the documented spatial radii, outside-radius behavior, Grass-type requirement, final Attack Combat Stage and ordered prevention/Intimidate events. It uses the existing authoritative CombatStageMutationService prevention path. No Minecraft/Cobblemon/Craftics rule logic is added.

PR #407 explicitly leaves Mirror Armor reflection and Defiant/Competitive post-apply reactions for later work before Intimidate can be considered a complete ROUND_START handler.

Previous Arena Trap evidence still covers authoritative holder resolution, target projection, effect planning, stateful Slowed mutation and round-start dispatch for that representative Ability. Complete Slowed expiration/cleanup and proof across all movement consumers remain open.

AutoPTU Python oracle

Read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its current commit states that the change is presentation-only and does not alter battle rules or outcomes.

Capability classification

Targeting / footprints / range / LoS: VERIFIED within previously audited ordinary contracts. PR #407 strengthens exact distance-aware Ability prevention evidence, not universal targeting coverage.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy / initiative: VERIFIED for audited primitives. Cargo/pickup/drop/handoff interactions still need explicit legal contracts.

Full turn / round lifecycle: PARTIAL. Arena Trap and Intimidate provide representative round-start/once-per-round evidence, but category-wide lifecycle remains unproven.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap applies Slowed authoritatively but complete expiration/cleanup remains unverified.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact family. Flower Veil spatial prevention is now verified for the audited Intimidate interaction. Reflection and post-apply reactions remain open.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Intimidate has stronger prevention coverage, but PR #407 itself identifies remaining interaction families.

Items: PARTIAL and individually gated.

Trainer Features / perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary scope; cargo/handoff actions remain undefined.

AI tactical policy: BLOCKING for retry, delivery-first, escort, protect-carrier, interception, preserve-resource, reroute and disengage-after-objective objectives.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for cargo/objective semantics and complete authoritative acknowledgement.

Pass 358 encounter implication

`The Attempt That Survived With the World` has a reduced version with no AutoPTU dependency. It uses semantic time, request/authorization/attempt provenance, coherent checkpoint restore, travel, communication, memory/belief and replanning.

A rich retry encounter can use verified base movement for ordinary positioning. Interception or forced displacement requires complete movement. Round deadlines require full lifecycle. Persistent conditions require status lifecycle. Environmental mechanics keep their exact terrain/weather/hazard/zone/reaction gate. Moves, Abilities, Items and Trainer Features remain individually gated. Missing PTU behavior cannot be pushed into Minecraft merely to make the scene work.

Open Ouros durability questions

World checkpoint V8 now includes Pass 344 failed attempts in the same coherent recovery boundary as reservations, requests and handoffs. Passes 345–352 still need incremental checkpoint codecs for appointment state, reschedules, allocation admission/decision/application and allocation-notice provenance.

Travel-derived arrival evidence, relationship consequences, inventory/cargo binding and long-history compaction remain separate owners.

Open engine questions

Intimidate still needs Mirror Armor reflection and Defiant/Competitive post-apply reactions. Arena Trap still needs complete Slowed expiration/cleanup evidence. Objective-aware tactical policy and Minecraft cargo/objective playback remain blockers for rich retry/escort variants.
