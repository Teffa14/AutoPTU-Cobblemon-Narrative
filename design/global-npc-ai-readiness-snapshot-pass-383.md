# Global NPC AI readiness snapshot — Pass 383

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative baseline inspected before writing: `48f644e7b22948f085be6b48823197a2fda5c2e8` (Pass 382).

Read-only AutoPTU-Java head inspected: `60b6cf2de552b6a3a77ca94131b43aa0613bfc01` (merge #417, generic Transform/Impostor transformation-state copy parity against the pinned Python oracle).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Repository/canon inspection

The current focus remains the global NPC/world-agent system. Canon governance still requires research, proposals, design and canon to remain separate. The current source inventory exposes Kairos/PTU routing through `sources/kairos/KAIROS_SOURCE_INDEX.md`; those references remain comparison/routing evidence rather than automatic Ouros acceptance.

Repository-wide searches found no dedicated archaeological-site context/stratigraphy/evidence layer before this pass.

Pass 383 therefore adds a reusable proposed archaeological-site evidence/context design and one non-canon narrative candidate. It does not change `canon/`.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; no blanket lifecycle inference.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Java merge #417 adds concrete parity evidence for the reusable Transform/Impostor transformation-state copy payload: copying the full seven-stage combat-stage snapshot when applicable and replacing the temporary copied ability. Target selection, RNG, once-per-entry guards, action economy and semantic events remain outside that resolver, so the Ability family is not promoted globally.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including rescue-first, protect-cargo/equipment/noncombatants/evidence, escort, search, route-clearing, area-documentation, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent route/site/objective/cargo/evidence identity, non-KO objective acknowledgement and authoritative end-to-end result playback.

No category is promoted globally from one representative mechanic.

## Pass 383 narrative boundary

The new proposed design introduces a reusable distinction between:

- portable finds;
- fixed site features;
- find/context records;
- actor interpretations;
- physical site revisions over semantic time.

This is world-state/narrative architecture. It does not implement PTU archaeology rules or create a new tactical subsystem.

The reduced version of `The Room Beneath the Room` requires no AutoPTU handoff. It can run on persistent site identity, semantic time, ordinary travel, private knowledge/provenance, communication and explicit site-state revisions.

## Rich encounter dependency note

A richer ruin encounter may use ordinary audited targeting/base movement/core calculations/action-economy primitives only within verified scopes.

If it adds collapsing floors, drag/rescue, knockback, interception or forced movement, complete-movement support is PARTIAL and exact mechanics must be verified.

If it adds timed cave-ins, flood phases, dust zones, unstable terrain, reactions, delayed environmental effects or similar mechanisms, terrain/weather/hazards/zones/reactions and full lifecycle support are exact-family dependencies and remain partial/blocking until verified.

Persistent/complex statuses require status-lifecycle evidence. Specific Moves, Abilities, Items and Trainer Features remain individually gated.

## Checkpoint status

`OUROS_NPC_WORLD_CHECKPOINT_V19` remains the latest coherent world-agent checkpoint inspected in this pass. Pass 383 does not alter checkpoint code.

The two demonstrated travel branches remain:

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_REPLAN_REQUIRED`

Archaeological observation/context history proposed here does not yet have an executable persistence owner. Until such an owner exists, it must not be treated as restart-safe implementation merely because the design is documented.

## Unresolved mechanical and canon questions

Failure and cancellation still need live replayable transitions before provenance owners can be justified. Objective completion/failure remains separate from arrival/interruption. `AUTOPTU_RESOLVED` remains blocked until a replayable session-resolution event can be tied to the exact accepted binding.

For the Pass 383 archaeological candidate, unresolved canon fields include location, historical builder/culture, institution/ownership, access policy, species/habitat, cause of exposure and the actual meaning of the lower feature.

A future implementation pass should create a small deterministic site-evidence ledger only if it can preserve observation, context, site revision and interpretation separately without duplicating the existing memory/provenance systems.
