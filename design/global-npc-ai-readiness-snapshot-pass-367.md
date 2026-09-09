# Global NPC AI readiness snapshot — Pass 367

Status: EVIDENCE SNAPSHOT. NOT CANON.
Date: 2026-09-08

Narrative starting head inspected recursively: `19f10fb239411ad0a459c8dfab98aa9e024b1571`.

Pass 367 persists Pass 349 allocation-application history in standalone resource checkpoint V8. It does not modify PTU mechanics or either engine repository.

## Read-only engine evidence

AutoPTU-Java head inspected: `eaaed3abdc6f2f1d884d71324a4fe9f5186b1b50`, merge of PR #410. The latest slice freezes differential parity for the specific Intimidate -> Simple reaction through the real POST_APPLY registry, including final Combat Stage state, once-per-round marker and event ordering. This remains interaction-specific evidence.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit explicitly changes presentation behavior only and does not change battle rules or outcomes.

## Permanent capability categories

Targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts.

Base movement legality: VERIFIED within previously audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Tactical interception, carrier displacement and full forced movement remain gated.

Core calculations: VERIFIED within previously audited ordinary deterministic scope.

Action economy/initiative: VERIFIED for audited primitives. Cargo, pickup, drop, handoff, guard and bespoke objective actions remain individually gated.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family. Intimidate reaction slices do not justify a category-wide promotion.

Move-specific behavior: individually gated / PARTIAL.

Abilities: individually gated / PARTIAL.

Items: individually gated / PARTIAL.

Trainer Features/perks: individually gated / PARTIAL.

AI legal-action infrastructure: VERIFIED for ordinary audited action-generation scope. Objective/cargo actions require dedicated contracts.

AI tactical policy: BLOCKING for intercept-to-inform, preserve-resource, protect-carrier, reroute and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for cargo identity, timed objective acknowledgement and authoritative end-to-end playback.

## PTU / Caelo boundary

Internal source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List where available. Pass 367 adds persistence architecture, provenance research and a non-canon encounter proposal only.

No representative mechanic is treated as proof that a whole capability family exists.
