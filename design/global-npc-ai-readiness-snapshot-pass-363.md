# Global NPC AI / AutoPTU readiness snapshot — Pass 363

Status: LIVE EVIDENCE SNAPSHOT
Canon authority: NONE
Date: 2026-09-08

Narrative base inspected before writing: `f376ad039cc29ce675d3aba0fcdaba0791f4f4d5`. The recursive repository inventory, source-authority policy, playable canon, Pass 339–362 durability chain, Pass 347 admission, downstream Passes 348–352, current tests and CI triggers were checked before implementation.

AutoPTU-Java read-only head: `e4e907349993a14c4c652f3dba58ff49db28ff79`, merge of PR #408. Evidence remains specific to Intimidate/Mirror Armor runtime reflection parity. It does not establish universal Ability, reaction or adapter coverage.

AutoPTU Python read-only head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The head change remains presentation-only and does not promote rule capability.

Capability classification remains conservative.

Targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts.
Base movement legality: VERIFIED within audited ordinary scope.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED within audited deterministic arithmetic scope.
Action economy/initiative: VERIFIED for audited primitives; objective-specific pickup, guard, reroute and timed logistics actions remain individually gated.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL; Arena Trap `Slowed` application has evidence, while complete expiration/cleanup and all movement consumers remain open.
Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family; Intimidate/Mirror Armor reflection is evidence only for that audited interaction.
Move-specific behavior: PARTIAL and individually gated.
Abilities: PARTIAL and individually gated.
Items: PARTIAL and individually gated.
Trainer Features/perks: PARTIAL and individually gated.
AI legal-action infrastructure: VERIFIED within audited ordinary scope; cargo/interception/objective actions require dedicated legality contracts.
AI tactical policy: BLOCKING for resource-first, escort, rerouting, preserve-resource, intercept-to-inform and disengage-after-objective behavior.
Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end for cargo, timed objectives, rerouting and authoritative acknowledgement.

Pass 363 adds `OUROS_NPC_RESOURCE_CHECKPOINT_V6` as a standalone durability boundary. A resolved Pass 347 CLEAR or CONFLICT assessment can now be captured with an assessment tick and exact reservation evidence, then restored without recomputing history from the current reservation state.

The checkpoint validates proposal, authorization, resource identity, bounded-window provenance, overlap structure and same-purpose classification. Later reservation cancellation or release does not erase the old conflict because reservation history remains present. Restore does not choose priority or apply Pass 348/349 effects.

V1–V5 restore an explicit empty admission ledger. Historical conflict facts are never inferred from later decisions, current availability, memory or dialogue.

CI now names both new durability modules in push and pull-request path filters.

Encounter implication: `The Conflict That Was Gone by Morning` has a reduced world-state version with no AutoPTU dependency. Its rich alternate-route version remains gated by complete movement for tactical displacement/interception, full lifecycle for round deadlines, exact environment families, objective-aware AI policy and Minecraft/Cobblemon/Craftics playback.

Next persistence seam: integrate resource checkpoint V6 into a new coherent world checkpoint so captured admissions share the same recovery digest and semantic time as NPC knowledge, communications and reschedule lineage. Pass 348 allocation-resolution persistence should remain a later owner rather than being merged into admission.
