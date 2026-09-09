# Global NPC AI readiness snapshot — Pass 378

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository baseline inspected before writing: `f0bdc38aebe5c26999ddb4ea4200aed55112781c`.

Read-only AutoPTU-Java head inspected: `6cc66d91d286fab06365cf37d88dd04038589195` (merge #415, oracle-backed authoritative round-start rollover parity for round number, initiative order/cursor and first actor after rollover).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives. Java merge #415 strengthens the authoritative round-rollover initiative seam specifically.
6. full turn/round lifecycle — PARTIAL. Merge #415 verifies rollover round/initiative state against the pinned Python oracle; it does not establish all round-start/end effects, nested reactions or lifecycle families.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Existing admitted round-start Ability work remains evidence for those exact paths only.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including rescue-first, protect-cargo/equipment, escort, search, route-clearing, calming/redirecting, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent route/objective/cargo identity, rescue/non-KO objective acknowledgement and authoritative end-to-end result playback.

No category is promoted globally from one representative mechanic.

## Pass 378 world-agent boundary

Pass 377 added standalone `OUROS_NPC_ACTION_START_PROVENANCE_V1` after V16 plan selection.

Pass 378 integrates that owner into coherent world persistence as `OUROS_NPC_WORLD_CHECKPOINT_V17`.

The recovery chain now reaches:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED`

V17 validates action-start replay and its plan-selection provenance under the same digest as V16.

Supported start families remain deliberately narrow:

- `TRAVEL_EDGE_STARTED`, proven by replaying the semantic world-travel departure;
- `AUTOPTU_BINDING_ACCEPTED`, proven by replaying the concrete world-agent binding transition after a selected `REQUEST_AUTOPTU` handoff.

Neither start family proves completion or success.

## Migration rule

V16 and older world checkpoints migrate with empty action-start provenance.

Current location, active travel, current AutoPTU binding, later battle state or Minecraft presentation cannot be used to synthesize missing historical start records.

## Encounter dependency note

The Pass 378 proposal `The Crossing With No Result` has a world-agent-only reduced version that does not require AutoPTU.

Its full version is mechanically gated by the exact capabilities used. A narrow crossing that relies only on ordinary audited targeting/movement/calculations has fewer blockers. Adding forced movement, interception, reactive terrain, flooding phases, complex statuses, move-specific control effects, Ability-triggered terrain, Trainer Feature interrupts or objective-aware tactical withdrawal requires those exact capability families to be verified first.

## Next boundary

The next provenance seam is terminal execution state.

`ACTION_STARTED != ACTION_COMPLETED != ACTION_FAILED != ACTION_SUCCEEDED`

For AutoPTU:

`AUTOPTU_BINDING_ACCEPTED != AUTOPTU_RESOLVED != AUTOPTU_RESULT_INGRESSED`

A future pass should preserve those transitions without inferring them from current location, cleared encounters, dialogue or presentation state.