# Global NPC AI Readiness Snapshot — Pass 412

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 412 adds explicit `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V5` generation selection for `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1`.

Historical V4 remains a five-owner generation. The existing V4 builder and `PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA` alias retain their prior meaning. New V5 callers must use `build_persistent_world_recovery_manifest_v5()` and supply six same-minute checkpoints.

V5 reconciliation verifies the session checkpoint schema, integrity, semantic minute and exact digest selected by the manifest. A valid same-minute checkpoint from another session generation is rejected. V4 rejects attempted session-owner injection.

This closes exact-generation selection for Ouros-side tactical-session identity. It does not add an AutoPTU battle-state store or resume a mid-turn battle.

## Research and narrative progress

New research sources for this corpus are Clara Fernández-Vara's DiGRA paper on indexical storytelling and the public Pixelmon Kainite project page. The first contributes the abstract design pattern that spatial traces can be gameplay-relevant evidence. The second supports a presentation boundary where a Pokémon experience can be authored inside Minecraft without inheriting every vanilla Minecraft affordance as game authority.

New proposal: `The Wall Remembers the Repair`, status PROPOSED / NON-CANON. Layered repairs at a reused structure become observations with provenance. Physical evidence can establish sequence while motive and cause remain uncertain. The reduced version is world-level investigation only.

No protected plot, character, dialogue, map, puzzle, faction or distinctive implementation is imported.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked. Its Chapter 7, movement/terrain, status, hazards, terrain/weather, campaign/session, encounter and item references remain routing aids. No rule is granted by this pass.

## Live engine evidence

AutoPTU-Java head remains `2e704f13f98ef8984f156bef4e6ec4e8924db87b`, PR #434, `Freeze Ball Fetch AbilityEvent trace parity`. This proves only one narrow structured Ability event seam around Ball Fetch approach Shift.

AutoPTU Python head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; the latest change is presentation-only viewport synchronization.

Both engine repositories remained read-only.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated. PR #434 does not promote the family.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes.

AI tactical policy: BLOCKING for special investigation, rescue, preservation and non-KO objective policies unless separately verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative environmental hazards, non-KO tactical completion and in-flight battle recovery. Authored spatial evidence can be presented without granting the adapter rule authority.

## Current recovery boundary

Ouros can now select the exact durable tactical-session identity owner in the same coherent recovery generation as the five V4 owners. An unresolved `ENGINE_BOUND` session still has no inferred result.

The next high-value seam is an exact V5 post-restore integration that consumes the selected session checkpoint and reconciles it with restored agent bindings in one helper, then a genuine authoritative AutoPTU session-store contract that can distinguish still-active, completed-with-result, unknown/quarantined and explicitly abandoned sessions after crash.
