# Global NPC AI / AutoPTU readiness snapshot — Pass 362

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

Narrative base inspected before writing: `cbd541155dd079a343200ccc6c7b69bede4bf420`. The recursive repository inventory, canon governance, current focus, Kairos/PTU source routing, Pass 339–361 resource/checkpoint chain, appointment communication ownership, Pass 346 live reschedule decision rule, downstream Passes 347–352 and CI triggers were inspected before implementation.

AutoPTU-Java live evidence

Read-only head inspected: `e4e907349993a14c4c652f3dba58ff49db28ff79`, merge of PR #408, `Freeze Intimidate Mirror Armor runtime reflection parity`.

The audited evidence remains specific to Intimidate interacting with Mirror Armor through the Java runtime and differential oracle. It compares final Attack stages, the Intimidate once-per-round marker and ordered semantic reflection/combat-stage/ability events. It does not establish universal Ability, reaction or adapter coverage.

Previous Arena Trap evidence remains representative for round-start holder resolution, target projection, effect planning and authoritative `Slowed` mutation. Complete `Slowed` expiration/cleanup and proof across every movement consumer remain open.

AutoPTU Python oracle

Read-only head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its current change is presentation-only and does not promote any rule capability.

Capability classification

Targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts. Exact Ability interactions remain individually gated.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy/initiative: VERIFIED for audited primitives. Cargo, timed rendezvous and intercept-to-inform actions still need explicit contracts.

Full turn/round lifecycle: PARTIAL. Representative round-start and once-per-round Ability evidence does not prove complete lifecycle support.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap can apply `Slowed`; complete expiration/cleanup remains unverified.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family. Intimidate/Mirror Armor reflection is verified only for that audited interaction.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary scope; interception, cargo and objective-specific actions require dedicated legality contracts.

AI tactical policy: BLOCKING for rendezvous-first, intercept-to-inform, rerouting, delivery-first, protect-carrier, preserve-resource and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end for timed rendezvous, cargo/objective semantics, interception objectives and authoritative acknowledgement.

Pass 362 durability scope

`OUROS_NPC_WORLD_CHECKPOINT_V10` embeds Pass 361 `OUROS_NPC_RESOURCE_CHECKPOINT_V5` when reschedule history is supplied. Restore reconstructs the world and resource owners, reuses Pass 360 appointment/envelope provenance validation, and additionally requires every persisted reschedule decision to have a source `RESCHEDULE_REQUEST` whose restored communication status is `DELIVERED`.

The resource ledger does not acquire delivery ownership. A later successor authorization is not accepted as evidence that the request arrived. V9 restores appointment history with an empty reschedule ledger; older world versions continue to preserve only the history they actually stored.

CI scope

`global-npc-ai.yml` now names `tools/global_npc_resource_reschedule_checkpoint.py` explicitly for both push and pull-request path filters, so future changes to the V5 codec trigger the global regression suite even when no other covered file changes.

Encounter implication

`The Change That Only One Person Received` has a reduced version with no AutoPTU dependency. Its richer interception variant remains gated by complete movement when tactical interception is used, full lifecycle for round deadlines, exact environmental mechanics, objective-aware AI policy and Minecraft/Cobblemon/Craftics playback. No representative Ability slice changes those gates.

Next persistence seam

Pass 347 conflict admission is the next unpersisted resource owner. Its future codec must preserve that an overlapping proposed successor was admitted for allocation review without treating the read as an allocation decision or modifying reservations during restore.
