# Global NPC AI Readiness Snapshot — Pass 403

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

## Concrete change

Pass 403 adds bounded holder-history coverage.

`tools/global_npc_holder_history_coverage.py` introduces `HolderHistoryCoverageBaseline` and derives expected holder state from one authoritative semantic cut plus later `ResourceHolderTransitionLedger` events.

The derivation deliberately ignores holder transitions at or before the baseline when deciding forward completeness. Earlier history can remain incomplete without weakening a later bounded proof.

`tools/world_resource_history_reconciliation.py` now accepts `holder_history_coverage_baselines` and can emit conflict-grade evidence from a baseline plus later journal continuity.

`tools/global_npc_persistent_world_post_restore.py` forwards the same evidence through the existing post-restore activation gate.

The legacy `complete_holder_history_resource_ids` path remains for compatibility, but a caller cannot mix it with bounded baselines in one reconciliation call.

## Safety boundary

Pass 402 still supplies the production call-site audit for known low-level holder mutators. Pass 403 depends on that journal-aware boundary for events after a baseline.

The new baseline does not prove anything about holder history before its own semantic cut.

It also does not yet have a dedicated persistent checkpoint owner. Provenance must identify the authoritative cut-state source used to issue the baseline.

## Narrative progress

New research used two previously unrecorded SkyTemple anchors for this scan:

- Pokémon Mystery Dungeon: The Bright Future, for returning to a world whose present condition reflects successful earlier events;
- Pokémon Mystery Dungeon: Explorers of the Spirit, for redesigned expedition spaces and temporary companions intended to expand encounter possibilities rather than become default liabilities.

`Second Survey Season` transforms those structures into an original Ouros proposal. A previously successful route intervention becomes the starting condition for a later comparative survey. Old and current observations may both be correct at different semantic cuts.

Status remains PROPOSED / NON-CANON.

## PTU/Caelo/Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid only. Potentially relevant families include Researcher, Chronicler, Climatologist, Survivalist, Topographer, movement/terrain, hazards, weather, encounters and boss design.

Pass 403 approves no Skill, Edge, Feature, class benefit, Item effect, hazard, weather modifier, carrying rule or tactical interrupt.

## Live engine evidence

AutoPTU-Java read-only head: `cf1e19c2ffb07ebd044d1d36348e88a67d5e413e`, merge #426, `Freeze authoritative switch transaction order`.

That evidence remains narrow to the audited switch transaction sequence and its already verified supporting seams. It does not complete switching, movement, lifecycle, Abilities or Trainer Features.

AutoPTU Python read-only head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only.

## Capability classification for Second Survey Season

Targeting/footprints/range/LoS: VERIFIED only inside previously audited scopes.

Base movement legality: VERIFIED only inside previously audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only inside previously audited scopes.

Action economy/initiative: PARTIAL overall; audited primitives exist.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only inside ordinary audited scopes.

AI tactical policy: BLOCKING for survey-first, preserve-evidence, protect-specialist, rescue-first, avoid-damaging-site, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for persistent site revisions, evidence interaction, environmental objective state, specialist acknowledgement and authoritative non-KO completion.

## Next highest-value seam

Issue holder-history baselines deterministically from a coherent `WorldResource` catalog checkpoint and preserve enough generation provenance to validate them after restart.

In-flight AutoPTU recovery remains the larger independent blocker: stable battle/session identity and authoritative tactical result persistence are still required before the persistent world can recover through an unfinished battle.
