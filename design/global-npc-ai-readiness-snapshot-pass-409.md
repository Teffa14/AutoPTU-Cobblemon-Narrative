# Global NPC AI Readiness Snapshot — Pass 409

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 409 advances the holder-history recovery chain from single-cut validation to explicit generation rollover.

`carry_forward_issued_holder_history_baselines()` persists only certificates emitted by a safe `PersistentWorldPostRestoreValidation`. A certificate retains the semantic cut at which its holder fact was established even when carried inside a later `OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1` generation.

This preserves the distinction between checkpoint time and certification time. A baseline issued at T and stored in a checkpoint at T+N still proves holder state only at T. Recovery at T+N must replay every later holder transition before it can validate the current catalog.

The new regression covers two consecutive advancements and a discontinuous-journal rejection. It also verifies that rollover cannot backdate a checkpoint before the validated recovery cut.

## Research and narrative progress

New public research anchors are `Pokémon: A Farfetch'd Story 2` for the abstract value of party-dependent environmental affordances outside ordinary wild combat, plus `A Short Hike` design material for dense landmark guidance, flexible goals and optional discoveries embedded directly in traversal.

Repository-wide duplicate checks excluded heavily processed sources before writing. No characters, plots, maps, field abilities, progression objects, puzzles or distinctive source content are imported.

New proposal: `The Path Depends on Who Came With You`, status PROPOSED / NON-CANON. It treats route availability as a consequence of actual party knowledge, permissions, relationships, ordinary resources and eventually verified mechanical capabilities. The reduced version requires no new PTU battle mechanic.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid rather than active rules authority. Potentially relevant source areas include Survivalist, Topographer, Backpacker, Skills/Edges/Features, movement/terrain, mounts, hazards/weather, encounter construction and Items/Gear.

No shortcut bonus, field action, Move effect, Ability traversal effect, Item power, Trainer Feature or special movement permission is promoted by Pass 409. Exact mechanics still require source-level verification and engine admission under `design/ouros-source-authority-and-species-policy.md`.

## Live engine evidence

AutoPTU-Java head inspected: `70b20f502e34c4d3a3130a6a661476858330543e`, merge PR #433, `Materialize generic approach Shift ability effects`, dated 2026-09-10.

The change adds `AbilityApproachShiftEffectExecutor`. It delegates movement legality to the existing ability approach-Shift executor, applies a named temporary effect to each holder that successfully shifts, and returns an ordered semantic descriptor. The Ball Fetch oracle-parity test now checks movement, ability/target identity and the temporary marker.

This strengthens one narrow Ability-triggered legal-approach-movement plus temporary-effect seam. It does not complete Abilities, complete movement, forced movement, action economy, initiative, full lifecycle, status lifecycle, hazards/zones/reactions, Trainer Features or tactical policy.

AutoPTU Python head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only viewport coordinate synchronization and explicitly does not change battle rules or outcomes.

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

Abilities: PARTIAL / individually gated. Pass 409 recognizes only the narrow Java approach-Shift temporary-effect seam.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Specialized traversal, manipulate-obstacle, carry and rescue actions need explicit admission if they become tactical.

AI tactical policy: BLOCKING for bypass-first, escort-first, rescue-first, preserve-equipment, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative route-affordance projection, persistent interactable state, companion-specific environmental actions and non-KO completion.

## Next seams

The next recovery slice should prove rollover through a complete later V4 manifest generation containing all five selected owner digests, rather than stopping at the post-restore owner contracts.

The larger independent blocker remains stable AutoPTU battle/session identity and authoritative recovery for a tactical resolution that was in flight during a crash. Minecraft and persistent-world state must not infer the tactical outcome.
