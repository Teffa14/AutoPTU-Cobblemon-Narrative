# Global NPC AI / AutoPTU readiness snapshot — Pass 361

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

Narrative base inspected before writing: `46704a54881fd40377eda4f61dbad03149838e08`. The recursive repository inventory, current resource/checkpoint chain, Pass 345 appointment ownership, Pass 346 rescheduling contract, downstream Passes 347–352, Pass 360 communication binding and relevant tests were inspected before implementation.

AutoPTU-Java live evidence

Read-only head inspected: `e4e907349993a14c4c652f3dba58ff49db28ff79`, merge of PR #408, `Freeze Intimidate Mirror Armor runtime reflection parity`.

PR #408 adds a deterministic differential fixture for Intimidate hitting a Mirror Armor target. It compares both combatants' final Attack stages, the once-per-round Intimidate marker, and ordered reflection/combat-stage/Intimidate semantic events through the real Java Intimidate and Combat Stage pipelines. The PR explicitly adds no Minecraft/Cobblemon/Craftics rule logic.

This promotes only the audited Intimidate/Mirror Armor reflection interaction. Defiant/Competitive post-apply reactions and unrelated Ability interactions remain separately gated.

Previous Arena Trap evidence still covers representative round-start holder resolution, target projection, effect planning and authoritative `Slowed` mutation. Complete `Slowed` expiration/cleanup and proof that all movement consumers respect it remain open.

AutoPTU Python oracle

PR #408 pins differential evidence to AutoPTU commit `16d228efa63aabecb67fa788959a359aac7f8f03` for the audited Mirror Armor fixture. This is oracle evidence for that case, not permission to treat the entire Python implementation as a complete contract for every capability family.

Capability classification

Targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts. Existing Flower Veil and current Mirror Armor work add exact Ability-interaction evidence, not universal coverage.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy/initiative: VERIFIED for audited primitives. Cargo, pickup, redirect and tactical interception still need explicit action contracts.

Full turn/round lifecycle: PARTIAL. Arena Trap and Intimidate provide representative round-start/once-per-round evidence only.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap can apply `Slowed`; complete expiration/cleanup remains unverified.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family. Mirror Armor reflection is now verified for the audited Intimidate case. Defiant/Competitive and unrelated reactions remain open.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary scope; objective/cargo/interception-specific actions still require explicit legality contracts.

AI tactical policy: BLOCKING for rendezvous-first, intercept-to-inform, rerouting, delivery-first, protect-carrier, preserve-resource and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end for timed rendezvous, cargo/objective semantics and authoritative acknowledgement.

Pass 361 durability scope

`OUROS_NPC_RESOURCE_CHECKPOINT_V5` persists Pass 346 proposal, decision and authorization-replacement lineage on top of V4 appointment history. Restore verifies that the successor authorization exactly expresses the accepted proposal while preserving the original authorization as superseded history. V1–V4 produce an empty reschedule ledger instead of inferred history.

World-level integration remains open. `OUROS_NPC_WORLD_CHECKPOINT_V9` does not yet embed V5 or cross-check a restored reschedule decision against delivery of its source RESCHEDULE_REQUEST in the same world snapshot.

Encounter implication

`The Rendezvous That Moved` has a reduced version with no AutoPTU dependency. The rich interception version remains gated by complete movement, exact lifecycle/environmental mechanics used, objective-aware AI policy and Minecraft/Cobblemon/Craftics objective playback. Mirror Armor parity does not alter those gates.
