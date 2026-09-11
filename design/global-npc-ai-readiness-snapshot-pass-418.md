# Global NPC AI readiness snapshot — Pass 418

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 418 starts from narrative main `249660b57235e3f786e597b61f8487b46694fa6e` after Pass 417. Canon files were left unchanged. AutoPTU-Java and AutoPTU were inspected read-only.

Implemented seam

`tools/autoptu_world_consequence_transaction.py` adds an idempotent transaction boundary after semantic result admission/recording. One explicit mapper can project only named semantic payload fields from the exact authoritative result associated with a RESULT_RECORDED or RETIRED AutoPTU session. Unknown payload fields fail closed. Exact replay is a no-op; conflicting replay is rejected.

This layer records a transaction only. It does not mutate world-agent, ecology, site, relationship, inventory or Minecraft state.

Regression

`tests/test_global_npc_autoptu_world_consequence_transaction.py` covers exact mapping, idempotent replay, unknown payload fields, missing required fields, wrong result identity, wrong result type, unresolved sessions and conflicting replay.

Research and proposal

Research: `research/2026-09-10-partial-return-consequence-scan-418.md`

Proposal: `proposals/2026-09-10-what-you-bring-back-changes-what-comes-next-pass-418.md`

Both remain outside canon.

Live AutoPTU-Java evidence

Inspected main: `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merge PR #441, `Freeze replacement initiative insertion oracle`, committed September 11, 2026 UTC.

The change freezes Python-runtime observations for `_insert_replacement_initiative`, including duplicate/no-entry no-ops, natural future insertion, already-passed insertion with and without immediate allowance, tie behavior and an empty-round case. The merge adds the oracle/export path to the parity workflow.

This is useful evidence for replacement initiative semantics. It does not by itself prove Java parity for every initiative path and does not promote action economy/initiative to a complete family.

Live AutoPTU evidence

Inspected main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest commit remains the August 29, 2026 viewport-resize coordinate synchronization explicitly described as presentation-only with no battle rules or outcomes change.

Capability posture for new encounter concepts

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited paths.
Action economy/initiative: PARTIAL; replacement initiative now has a frozen oracle seam.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited actions.
AI tactical policy: BLOCKING for specialized objective policies without dedicated contracts.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives and in-flight recovery.

Next implementation seam

Consume a committed world consequence transaction in one named owner subsystem. That executor must preserve transaction identity/provenance and remain idempotent. It must not reopen the semantic payload or derive hidden tactical facts. A small observation/obligation owner is preferable before attempting Injury, status or other PTU-persistent consequences whose producing capability paths remain incomplete.

Separate unresolved paths

Engine authority `UNKNOWN` and `EXPLICITLY_ABANDONED` still require their own durable policies. Neither should be routed through ordinary semantic completion or world consequence mapping.
