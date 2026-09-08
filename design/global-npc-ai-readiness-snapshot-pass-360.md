# Global NPC AI / AutoPTU readiness snapshot — Pass 360

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

Narrative base inspected before writing: `61e197e975a95ced7a72029c78048e3f7378d241`. The recursive repository tree, current focus, canon governance, Passes 339 and 342–359, communication provenance, resource checkpoint codecs, world checkpoint integration, regression tests and CI path triggers were inspected before implementation.

## AutoPTU-Java live evidence

Read-only head inspected: `bcdab77cc407919b407c7048bdc862f58e2a97f0`, merge of PR #407, `Freeze Intimidate Flower Veil spatial prevention`.

That PR differentially verifies Intimidate against Flower Veil and Flower Veil [Errata] for the audited spatial radii, outside-radius behavior, Grass-type qualification, final Attack Combat Stage and ordered semantic events through the authoritative Combat Stage path.

The PR explicitly leaves Mirror Armor reflection and Defiant/Competitive post-apply reactions outside the slice. That evidence therefore strengthens one Ability interaction without promoting Abilities or reactions as complete categories.

Previous Arena Trap evidence still covers authoritative holder resolution, candidate projection, effect planning, stateful `Slowed` mutation and round-start dispatch for that representative Ability. Complete `Slowed` expiration/cleanup and proof that all relevant movement consumers respect the state remain open.

## AutoPTU Python oracle

Read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head is presentation-only and does not provide evidence for a battle-rule promotion.

## Capability classification

Targeting / footprints / range / LoS: VERIFIED within previously audited ordinary contracts. Flower Veil supplies exact spatial prevention evidence, not universal coverage.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy / initiative: VERIFIED for audited primitives. Cargo, pickup, drop and handoff tactical actions still need explicit contracts.

Full turn / round lifecycle: PARTIAL. Arena Trap and Intimidate provide representative round-start / once-per-round evidence, not complete lifecycle coverage.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap can apply `Slowed` authoritatively, but complete expiration/cleanup remains unverified.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact family. Flower Veil spatial prevention is verified for the audited Intimidate interaction. Reflection and post-apply reaction families remain open.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated.

Items: PARTIAL and individually gated.

Trainer Features / perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary scope; cargo/objective/interception-specific actions still require explicit legality contracts.

AI tactical policy: BLOCKING for delivery-first, retry, escort, protect-carrier, intercept-to-inform, rerouting, preserve-resource and disengage-after-objective behavior.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for cargo/objective semantics and authoritative acknowledgement.

## Pass 360 durability scope

`OUROS_NPC_WORLD_CHECKPOINT_V9` can now recover Pass 345 appointment notices alongside the world information queue. When appointment history is supplied, it embeds `OUROS_NPC_RESOURCE_CHECKPOINT_V4`; callers that intentionally omit the appointment owner retain the V3 resource shape and restore an explicit empty appointment ledger.

For each restored appointment notice, V9 cross-validates the associated communication envelope by event identity, sender, receiver, source claim and creation time. The resource owner still does not store delivery state. Queued, local-ack, delivered and failed states remain owned by `InformationEventQueue`.

This closes the Pass 359 seam where the resource record and communications record could both survive independently without proving they referred to the same sender/recipient relationship.

The CI path filter now explicitly includes the resource checkpoint codecs and world/resource checkpoint adapter so future changes to those modules trigger the global regression suite directly.

## Pass 360 encounter implication

`The Confirmation That Reached the Wrong Person` has a reduced version with no AutoPTU dependency. It can run through semantic time, resource history, communication provenance, memory/belief, travel, failed attempts and checkpoint recovery.

Its rich interception variant may use verified base movement for ordinary positioning. Tactical interception, forced separation or cargo displacement requires complete movement and remains PARTIAL. Round deadlines require full turn/round lifecycle and remain PARTIAL. Persistent conditions require status lifecycle. Weather, hazards, zones and reactions preserve their exact family gates. Moves, Abilities, Items and Trainer Features remain individually gated.

If any rich dependency is unavailable, the same premise can resolve with semantic travel and communication without moving missing PTU rules into Minecraft.

## Remaining durability seams

Pass 346 reschedule successor history is the next resource checkpoint boundary. Passes 347–352 allocation admission/resolution/application, displacement and notice provenance remain later boundaries.

Arrival evidence from travel and inventory/cargo binding also remain separate owners that should not be inferred during restore.

## Open engine questions

Intimidate still needs Mirror Armor reflection and Defiant/Competitive post-apply reactions. Arena Trap still needs complete `Slowed` expiration/cleanup evidence. Objective-aware tactical policy, cargo legality, interception semantics and Minecraft cargo/objective playback remain blockers for rich courier/escort variants.
