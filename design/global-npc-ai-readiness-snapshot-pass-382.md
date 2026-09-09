# Global NPC AI readiness snapshot — Pass 382

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative baseline inspected before writing: `4ba9469bd920b617999056657ea57de7fb81ac85` (Pass 381).

Read-only AutoPTU-Java head inspected: `3a6be5d6a70fbce05e693495d02300d6948100c2` (merge #416, production round-start Intimidate rollover trace against the pinned Python oracle).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; current Java evidence strengthens only the specific production rollover seam.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Intimidate is concrete evidence for Intimidate, not blanket Ability support.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including rescue-first, protect-cargo/equipment/noncombatants, escort, search, route-clearing, calming/redirecting, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent route/site/objective/cargo identity, rescue/non-KO objective acknowledgement and authoritative end-to-end result playback.

No category is promoted globally from one representative mechanic.

## Pass 382 boundary

Pass 382 adds `OUROS_NPC_WORLD_CHECKPOINT_V19` and places `OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1` under the same coherent digest as V18.

The coherent checkpoint now supports two demonstrated action-outcome branches:

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_REPLAN_REQUIRED`

V19 rejects a snapshot where the same action-start identity owns both branches. This remains a narrow causal-consistency rule over currently admitted replayable outcomes rather than a general terminal-state machine.

The interruption remains distinct from action failure, cancellation and objective failure.

## Checkpoint status

V19 is the proposed latest coherent world checkpoint for this branch. Migration from V18 and older checkpoints restores an empty interruption ledger rather than inferring history from current route state or later consequences.

Restore cross-validates interruption rows against recovered action-start provenance and semantic time after validating the V19 digest and rebuilding V18.

## Encounter dependency note

The Pass 382 proposal `The Detour That Reopened Behind Them` has a world-agent-only reduced version requiring no tactical mechanic.

Its rich version can use ordinary audited targeting/base movement/calculations/action-economy primitives only within verified scopes. Push/pull/knockback/interception/forced movement, complex status, dynamic terrain/weather/hazards/zones/reactions, move-specific control, Abilities, Items and Trainer Feature interrupts remain gated by exact evidence.

Search, escort, route-clearing, protect-equipment/noncombatant, rescue-first, objective-aware withdrawal and disengage-after-objective remain AI tactical-policy blockers. Minecraft/Cobblemon/Craftics remains partial/blocking for persistent route/closure/objective identity and authoritative non-KO result playback.

## Unresolved mechanical and canon questions

Failure and cancellation still need live replayable transitions before they can receive provenance owners. Objective completion/failure remains separate from travel arrival or interruption. `AUTOPTU_RESOLVED` remains blocked until a replayable session-resolution event can be tied to the exact accepted binding.

The Pass 382 narrative candidate does not choose an Ouros/Caelo route, institution, species, closure cause or communication technology. Those remain canon decisions and must be resolved from internal authority before promotion.
