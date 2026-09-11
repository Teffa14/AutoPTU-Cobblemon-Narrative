# Global NPC AI Readiness Snapshot — Pass 415

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 415 adds a conservative follow-up planner for validated AutoPTU engine-authority reports.

The new planner creates explicit intents without changing the restored session ledger. A completed engine report advances to `RECORD_ADMITTED_RESULT` only when its exact result reference is independently present in the admitted semantic-result set. Otherwise it remains `HOLD_PENDING_RESULT_ADMISSION`.

`ACTIVE` remains engine-bound. `UNKNOWN` is isolated for quarantine review without inventing an outcome. Explicit abandonment remains held behind a separate abandonment policy boundary and cannot become a win, loss, draw, forfeit, void or retirement in this pass.

Executable files:

- `tools/autoptu_engine_authority_transition_plan.py`
- `tests/test_global_npc_autoptu_engine_authority_transition_plan.py`
- `design/autoptu-engine-authority-transition-plan-contract-pass-415.md`

## Narrative research completed

New provenance was recorded for Pokémon Hollow Woods and Pokémon Lithic Veil after repository searches found no prior title matches for those sources.

The resulting proposal, `The Place Has More Than One Custodian`, treats overlapping institutional interests, observations and records as separate provenance-bearing world state. It remains PROPOSED / NON-CANON.

Files:

- `research/2026-09-10-overlapping-stewardship-hidden-route-scan-415.md`
- `proposals/2026-09-10-the-place-has-more-than-one-custodian-pass-415.md`

## Live engine evidence

AutoPTU-Java inspected head: `befea9488953a07e510b5ad9152abaa314ae1332`, merge PR #438, `Register parity-safe Ball Fetch post-entry handler`, dated 2026-09-11 UTC.

This registers the proven Ball Fetch post-entry handler in the production switch dispatcher and retains unported post-entry families as pending. Evidence is narrow. It strengthens Ball Fetch plus switch post-entry composition and event publication only.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains presentation-only.

Neither engine repository was modified.

## Permanent capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited paths.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated. Ball Fetch evidence does not promote the family.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only in ordinary audited scopes.

AI tactical policy: BLOCKING for specialized objective policies without explicit implementation evidence.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative tactical objectives, non-KO completion and recovery of an in-flight battle.

## Next implementation seam

The next safe seam is an executor that consumes only `RECORD_ADMITTED_RESULT` intents, records the exact admitted result against the exact session, and proves idempotency before any world-agent ownership is released.

`UNKNOWN` and `EXPLICITLY_ABANDONED` still need distinct durable policy/provenance contracts. They must not share the normal completed-result path.
