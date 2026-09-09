# Global NPC AI readiness snapshot — Pass 384

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative baseline inspected before writing: `e30ca2e3ebf6c54e9bb1dc5062a22e5bd7ab3ec0` (Pass 383).

Read-only AutoPTU-Java head inspected: `de73c857d3ae3c20b47f34d1355b2b95dc590ffd` (merge #418, deterministic Impostor target-selection parity against Python).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Repository/canon inspection

The recursive repository tree, CURRENT_FOCUS, canon governance, Pass 383 archaeology design/research/proposal files, current provenance owners/tests, global-NPC CI and Kairos/PTU source routing were inspected before writing.

Pass 383 explicitly identified missing executable ownership for archaeological site revision/observation/context/interpretation history. Pass 384 closes a bounded subset of that gap with `OUROS_SITE_EVIDENCE_LEDGER_V1`.

No file under `canon/` changes in this pass.

## New executable evidence owner

`tools/global_npc_site_evidence.py` now preserves three replayable record families: physical site revisions, actor observations tied to one revision, and interpretations tied to explicit observations.

Revision chains are same-site, chronological and non-forking in V1. Observations cannot predate their physical revision. Interpretations cannot consume future observations or mix sites. Same-actor same-site interpretation supersession does not mutate the earlier observation.

Snapshot/restore uses the same validation paths as live recording. Optional world-time validation rejects evidence from the future.

This ledger remains standalone and is not yet under `OUROS_NPC_WORLD_CHECKPOINT_V19`.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; dedicated narrative-objective actions require explicit admission.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Java merge #418 proves deterministic nearest-active-opponent selection for the pinned Impostor path using active/alive/opposing-team filtering, Chebyshev distance and combatant-id tie breaking. It does not prove the whole Ability family.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for protect-evidence, documentation-first, rescue-first, escort, search, stabilization-first, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent evidence identity, site-revision projection, interaction acknowledgement, non-KO objective state and authoritative end-to-end playback.

No category is promoted globally from one representative mechanic.

## Reduced versus rich narrative implementation

The Pass 384 case `The Foundation That Made Both Maps Correct` can run in reduced form without AutoPTU. It requires persistent site identity, semantic time, site-evidence records and existing world-agent travel/knowledge/communication seams where NPC participation is used.

The rich form adds tactical pressure only when exact engine dependencies are admitted. Forced movement depends on complete movement. Timed collapse or flood phases depend on full lifecycle plus exact terrain/hazard support. Dedicated protect/document/escort behavior remains blocked by AI tactical policy. Specific Moves, Abilities, Items and Trainer Features remain individually gated.

## Internal authority boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes Researcher, Paleontologist, Topographer, movement, terrain and encounter material to supplied PTU/Kairos sources. The index is not itself a rules grant. Pass 384 therefore records evidence state and actor claims but introduces no new PTU skill check, Feature behavior, item behavior, species distribution or encounter rule.

## Next seams

The immediate safe continuation is checkpoint integration for `OUROS_SITE_EVIDENCE_LEDGER_V1`, but only after deciding whether the ledger belongs inside the global NPC coherent checkpoint or a broader world-state checkpoint owner.

A separate future seam should connect world observations to private NPC knowledge through explicit provenance-preserving materialization events. Direct database visibility must not create omniscience.

Portable-find custody should integrate with existing evidence-custody/resource owners rather than creating a duplicate inventory chain.

Geometry and spatial relationships remain refs in V1. A richer spatial model should wait until the Minecraft/Cobblemon projection contract can preserve stable evidence identity across block/state changes.
