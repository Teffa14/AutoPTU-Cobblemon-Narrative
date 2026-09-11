# Global NPC AI readiness snapshot — Pass 419

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 419 starts from narrative main `67158f716b5529d0990e24bfa0643c0d415b6e45` after Pass 418. The recursive repository tree, current focus, canon inventory, recent research/proposals and relevant observation/evidence and AutoPTU consequence files were inspected before writing. Canon files were left unchanged. AutoPTU-Java and AutoPTU were inspected read-only.

Implemented seam

`tools/autoptu_world_observation_owner.py` consumes only committed `FIELD_OBSERVATION` consequences from the Pass 418 transaction boundary. It records transaction identity, durable session identity, authoritative result reference, objective reference, outcome, optional evidence reference and provenance. It never re-reads tactical state or the original AutoPTU payload.

The owner accepts only `objective_ref`, `outcome` and optional `evidence_ref`. Extra fields fail closed. Exact replay is idempotent. Conflicting replay under the same transaction identity is rejected.

Regression

`tests/test_global_npc_autoptu_world_observation_owner.py` covers exact application, idempotent replay, wrong consequence kind, unsupported fields, missing semantic fields, blank optional evidence and conflicting replay.

Research and proposal

Research: `research/2026-09-11-investigation-handoff-evidence-scan-419.md`

Proposal: `proposals/2026-09-11-the-next-investigator-gets-the-record-not-the-memory-419.md`

Both remain outside canon.

New public sources

Pokémon Memories, Eevee Expo thread by AppleRowlet, started April 16, 2026. Reusable high-level pattern: later viewpoint plus changed world plus inherited records does not require inherited knowledge.

The Case of the Golden Idol design interview on GameDeveloper. Reusable high-level pattern: concrete evidence and player-built hypotheses can remain separate while later evidence eliminates or revises earlier theories.

No characters, plots, dialogue, locations, puzzles or distinctive content were imported.

Live AutoPTU-Java evidence

Inspected main: `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merge PR #441, `Freeze replacement initiative insertion oracle`, committed September 11, 2026 UTC.

This strengthens a bounded replacement-initiative seam. Action economy/initiative remains PARTIAL because one frozen insertion oracle does not establish every initiative and action-economy path.

Live AutoPTU evidence

Inspected main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its newest change remains presentation-only viewport-coordinate synchronization with no battle rules or outcomes change.

Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited paths.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary actions.
AI tactical policy: BLOCKING for specialized evidence-first, protect-witness, retrieval-first and objective-aware withdrawal policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives and in-flight recovery.

Next implementation seam

Connect a committed world observation to one explicit knowledge-delivery or obligation-creation contract. The downstream event must cite the observation transaction and preserve receiver identity and provenance. It must not infer knowledge for every faction member and must not reopen hidden tactical state.

Separate unresolved paths

Engine authority `UNKNOWN` and `EXPLICITLY_ABANDONED` still require separate durable policies. Persistent Injury/status consequences should remain deferred until their producing AutoPTU paths are sufficiently verified.
