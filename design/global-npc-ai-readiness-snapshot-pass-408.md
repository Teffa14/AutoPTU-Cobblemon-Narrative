# Global NPC AI Readiness Snapshot — Pass 408

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 408 connects the holder-history coverage baseline owner selected by `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4` to post-restore WorldResource reconciliation.

`validate_persistent_world_post_restore()` now accepts the exact selected `OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1` snapshot. It restores the checkpoint, verifies the V4-selected SHA-256 generation and semantic minute, and passes eligible historical baselines into the existing bounded holder-history replay.

The integration preserves the anti-circularity boundary established in Pass 405. A baseline whose own `at_tick` equals the current recovery semantic minute is not used to prove that same current catalog. Only baselines strictly earlier than the current cut become historical reconciliation evidence. Same-cut baselines remain future-facing certificates for later generations.

A selected older baseline plus continuous later holder transitions can now confirm the current holder. A contradiction blocks activation. A transition whose `from_actor_id` breaks continuity still fails closed inside bounded coverage derivation.

V1-V3 recovery paths cannot inject the V4 baseline owner. Legacy explicit complete-holder IDs remain a separate compatibility path and cannot be combined with restored bounded baselines.

## Regression coverage

`tests/test_global_npc_v4_holder_baseline_reconciliation.py` covers successful replay from an older selected baseline through a later holder handoff, current-holder conflict against bounded replay, rejection of a different valid baseline checkpoint generation, exclusion of same-cut baselines from current-cut proof, and failure when V4-selected baseline state is missing.

The existing global regression suite remains the integration gate for this slice.

## Research and narrative progress

New research anchors are the Pokémon Sky Blue public project index for abstract order-flexible exploration across locally distinct spaces, plus the GDC 2024 session `Relic Ruins: Creating Environmental Puzzles for Horizon Forbidden West` for environmental-puzzle iteration, readability and compact exploration questions. No protected characters, plot, regions, Fakemon, layouts or distinctive content are imported.

Repeated sources including Pokémon Tectonic, Monomyth, Nova, Crossroads, Pokopia, Stalactite and long-running PTU actual-play anchors were deliberately not reprocessed.

New proposal: `Survey Recess Network`, status PROPOSED / NON-CANON. It attaches a possible cross-site investigation structure to existing Sendero del Vidrio, Estación Mirador and Tideglass Archive facts without establishing that any hidden site exists.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid. This pass does not promote Researcher, Chronicler, Librarian, Paleontologist, Survivalist, Topographer, Skills, Edges, Features, Items, hazards, terrain/weather rules, movement permissions or puzzle checks into Ouros mechanics. Any exact rule still requires source-level verification and engine admission.

## Live engine evidence

AutoPTU-Java head inspected: `52439df965145702ddbd5f4a3a65857ea1080918`, merge PR #431, `Add generic ability approach Shift execution`.

The change adds a generic server-owned executor for effective Ability holders to make a legal Shift toward one combatant. Destination legality remains delegated to the existing canonical Shift resolver. Oracle parity is demonstrated against Ball Fetch sequential approach behavior from pinned Python evidence.

This improves one narrow Ability-triggered movement seam. It does not complete the Abilities family, complete movement, push/pull, knockback, interception, forced movement, action economy, initiative, lifecycle, hazards, Trainer Features or tactical objective policy.

AutoPTU Python head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is presentation-only viewport coordinate synchronization and explicitly does not change battle rules or outcomes.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL as a complete family.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated. Pass 408 recognizes the new narrow Java Ability-approach seam without broadening family readiness.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary action scopes; specialized investigation/rescue/puzzle actions remain unadmitted unless separately implemented.

AI tactical policy: BLOCKING for investigate-first, preserve-evidence, solve-before-engage, protect-observer, rescue-first, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for persistent environmental puzzle state, authoritative clue/objective interaction and non-KO completion.

## Next seams

The next persistent-world slice should exercise generation advancement explicitly: recover a baseline that was issued at an earlier cut, replay all later holder transitions into a newer coherent generation, then issue a replacement future-facing baseline only after the newer cut is validated.

The larger independent blocker remains stable AutoPTU battle/session identity and authoritative recovery for a tactical resolution that was in flight during a crash. Minecraft and persistent-world state must not infer the outcome.
