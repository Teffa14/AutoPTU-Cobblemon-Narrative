# Global NPC AI Readiness Snapshot — Pass 406

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

Pass 406 persists the future-facing `HolderHistoryCoverageBaseline` certificates introduced by Pass 403–405 through `OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1`.

The checkpoint stores one baseline per resource in deterministic order, protects the generation with SHA-256, and rejects duplicate baseline/resource identities, future baselines, future checkpoint generations, malformed records and tampering. It remains an independent owner for this pass. The outer persistent-world recovery manifest has not yet been upgraded to select its digest, so restore code must not silently treat an independently restored baseline checkpoint as manifest-selected evidence.

The recovery boundary remains non-circular. A certificate issued after safe activation at semantic cut T can support continuity only after T. Persisting that certificate does not make pre-T history complete and does not allow it to validate the catalog generation from which it was originally issued.

Research added two source anchors that were not previously processed as named primary sources in the repository: Pokémon Mystery Dungeon Eternal Elemental and Pokémon Synthesis Version. Their structures were transformed into the proposed `The Surveys That Disagree` arc, where optional fieldwork performed in different orders produces different evidence sets and later institutional disagreement can be resolved through provenance instead of an omniscient reputation score.

PTU/Caelo/Kairos remains reference-only. No new Skill, Edge, Feature, Move, Ability, Item, hazard, terrain or weather rule is granted by this pass.

Live engine evidence inspected on 2026-09-10: AutoPTU-Java `main` is `f60c1b76c397176b90bbee85af68ca785ae3abab`, merge PR #429, `Freeze Ball Fetch switch behavior`. This is evidence for one Ball Fetch interaction in the audited switch path. It does not complete the abilities family or switching. AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7` with presentation-only latest changes.

Capability status for new encounter concepts remains conservative. Targeting/footprints/range/LoS: VERIFIED only in audited scopes. Base movement legality: VERIFIED only in audited scopes. Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Core calculations: VERIFIED only in audited scopes. Action economy/initiative: PARTIAL. Full turn/round lifecycle: PARTIAL. Full stateful damage pipeline: PARTIAL. Status lifecycle: PARTIAL. Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. Move-specific behavior: individually gated. Abilities: individually gated despite the new Ball Fetch seam. Items: individually gated. Trainer Features/perks: individually gated. AI legal-action infrastructure: verified only for audited ordinary scopes. AI tactical policy: BLOCKING for objective-aware investigation/rescue/preservation behavior. Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for persistent objective state, evidence interaction and authoritative non-KO completion.

Next recovery seam: introduce a new outer manifest generation that selects the baseline checkpoint digest together with the holder-transition checkpoint at the same semantic cut, then validate cross-owner chronology before using restored certificates for bounded history.

Independent high-impact blocker: stable AutoPTU battle/session identity and authoritative recovery of an in-flight tactical resolution after crash/restart.
