# Global NPC AI readiness snapshot — Pass 381

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative baseline inspected before writing: `a14d2425e45bb4dbe0bb88c451d51060559f7214` (Pass 380).

Read-only AutoPTU-Java head inspected: `3a6be5d6a70fbce05e693495d02300d6948100c2` (merge #416, production round-start Intimidate rollover trace against the pinned Python oracle).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; the current Java trace strengthens only the specific production rollover seam.
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

## Pass 381 boundary

Pass 381 adds standalone `OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1` for the existing deterministic semantic-travel transition `REPLAN_REQUIRED` after a real `TRAVEL_EDGE_STARTED` action start.

The new demonstrable branch is:

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_REPLAN_REQUIRED`

This branch sits beside the already coherent V18 arrival branch:

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

The interruption owner does not call `REPLAN_REQUIRED` failure, cancellation, objective failure or mission completion.

The interruption is replayed using the source started-travel state plus route-edge state observed at interruption time. That edge snapshot may differ legitimately from departure conditions.

## Checkpoint status

V18 remains the latest coherent world checkpoint. Pass 381 interruption provenance is standalone and is not yet covered by the V18 digest.

A later checkpoint must cross-validate the interruption ledger against restored action-start provenance and recovered semantic time. Migration may not reconstruct interruptions from later blocked routes, current position, replan history or dialogue.

## Encounter dependency note

The Pass 381 proposal `The Road That Stopped Being a Road` has a world-agent-only reduced version requiring no tactical mechanic.

Its full version can use ordinary audited targeting/base movement/calculations/action-economy primitives only within verified scopes. Push/pull/knockback/interception/forced movement, complex status, dynamic terrain/weather/hazards/zones/reactions, move-specific control, Abilities, Items and Trainer Feature interrupts remain gated by exact evidence.

Search, escort, route-clearing, protect-equipment/noncombatant, rescue-first, objective-aware withdrawal and disengage-after-objective remain AI tactical-policy blockers. Minecraft/Cobblemon/Craftics remains partial/blocking for persistent route/closure/objective identity and authoritative non-KO result playback.

## Next boundary

Integrate `OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1` into a checkpoint after V18. Define actual failure and cancellation only from live replayable transitions, and keep objective completion/failure separate from execution state. `AUTOPTU_RESOLVED` remains blocked until a replayable session-resolution event can be tied to the exact accepted binding.
