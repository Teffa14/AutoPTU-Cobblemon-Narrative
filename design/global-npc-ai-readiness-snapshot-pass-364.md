# Global NPC AI Readiness Snapshot — Pass 364

Status: DESIGN / LIVE EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-08

## Narrative/world-state progress

Pass 364 adds `OUROS_NPC_WORLD_CHECKPOINT_V11` through `tools/global_npc_world_resource_admission_checkpoint.py`. V11 places Pass 347 historical reschedule-conflict admission inside the same global integrity boundary as semantic time, NPC state, knowledge, communications and Pass 339–346 resource lineage.

V10 migration returns an empty admission ledger. No conflict assessment is inferred from current availability or later allocation outcomes.

## Read-only engine evidence

AutoPTU-Java main inspected at `d617d1dac6ca60c09f614d278629462658016327`, merge PR #409, `Freeze Intimidate Defiant and Competitive reaction parity`.

PR #409 adds deterministic differential coverage for Intimidate interacting with Defiant and Competitive. It compares final Attack/Special Attack Combat Stages, the once-per-round marker and ordered semantic events through the real POST_APPLY hook registry. The PR explicitly adds no Minecraft/Cobblemon/Craftics rule logic.

This is stronger evidence for those exact post-Combat-Stage reaction interactions. It does not establish the complete Abilities family, every Combat Stage reaction or the general terrain/weather/hazard reaction system.

AutoPTU Python main inspected at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head change is presentation-only and does not change battle rules or outcomes.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within ordinary audited contracts. Do not extrapolate from representative moves to universal move behavior.

Base movement legality: VERIFIED within audited ordinary movement scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Rich escort/carrier/interception scenes remain gated by exact contracts.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy/initiative: VERIFIED for audited primitives; specialized feature interrupts remain separately gated.

Full turn/round lifecycle: PARTIAL. Existing round-start and once-per-round slices do not prove the complete lifecycle.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Intimidate→Mirror Armor, Defiant and Competitive provide specific reaction evidence only.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. Specific Intimidate prevention/reflection/post-apply interactions now have differential evidence; family-wide coverage remains incomplete.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited legal actions. Cargo, observation-objective and resource-specific actions need explicit contracts.

AI tactical policy: BLOCKING for protect-carrier, preserve-resource, complete-reading, rendezvous-first, reroute, intercept-to-inform and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for cargo, timed observation and objective semantics end-to-end.

## Pass 364 encounter consequence

`The Empty Slot That Used to Be Taken` can run without AutoPTU. Its reduced field version depends on world-state persistence, travel, communications and scheduling only.

A tactical version can safely use ordinary audited targeting, movement, calculations and initiative within their verified scopes. Forced movement, environmental zones, persistent status pressure, weather phases, Ability-specific reactions, cargo-aware AI and Minecraft objective playback must remain individually gated.

## PTU / Caelo boundary

The project source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List when available. Pass 364 changes persistence architecture and proposes a location-neutral field scenario; it establishes no PTU/Caelo rule or setting fact.

## Next implementation seam

Pass 348 allocation decisions remain the next distinct owner. Persistence should record who decided, their authority provenance, the conflict/admission record they considered and the selected course without allowing Pass 349 application to rewrite the decision history.