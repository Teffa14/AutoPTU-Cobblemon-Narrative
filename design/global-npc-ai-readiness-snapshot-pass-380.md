# Global NPC AI readiness snapshot — Pass 380

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository baseline inspected before writing: `dcc951d3c38a2b4d8cb98ec875721ec4332b31c1` (Pass 379).

Read-only AutoPTU-Java head inspected: `3a6be5d6a70fbce05e693495d02300d6948100c2` (merge #416, production round-start Intimidate rollover trace against the pinned Python oracle).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Live Java evidence added since Pass 379

Merge #416 extends the pinned Python round-start fixture with a real BattleState Intimidate scenario and compares it against the production Java rollover path. The differential freezes final Attack stage, once-per-round Intimidate usage and ordered CombatStage/Ability events.

This strengthens evidence for the exact round-start Intimidate rollover seam. It does not establish complete Ability support, complete reaction handling or the full turn/round lifecycle.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; the prior rollover evidence and merge #416 strengthen a specific production round-start trace.
6. full turn/round lifecycle — PARTIAL. Round rollover plus the specific Intimidate trace do not cover every start/end effect, nested reaction, action reset or lifecycle family.
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

## Pass 380 boundary

Pass 380 adds `OUROS_NPC_WORLD_CHECKPOINT_V18` and places `OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1` under the same coherent digest as V17.

The durable causal chain recovered by one checkpoint now reaches:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

The current terminal remains deliberately narrow. V18 cross-validates it against the restored action-start ledger and recovered semantic minute. V17 and older checkpoints migrate with empty terminal history rather than reconstructing it from later state.

## Non-claims

Travel arrival does not establish mission success, objective completion, handoff completion, sample/equipment preservation, AutoPTU resolution, tactical result ingress or Minecraft playback completion.

For structured battle ownership the boundary remains:

`AUTOPTU_BINDING_ACCEPTED != AUTOPTU_RESOLVED != AUTOPTU_RESULT_INGRESSED`

No replayable global-NPC `AUTOPTU_RESOLVED` owner is introduced by this pass.

## Encounter dependency note

The Pass 380 proposal `The Survey Camp With No Survey Result` has a world-agent-only reduced version. It requires no tactical mechanic.

Its full optional version can use ordinary audited targeting/base movement/calculations/action-economy primitives only within verified scopes. Push/pull/knockback/interception/forced movement, complex status, dynamic terrain/weather/hazards/zones/reactions, move-specific control, Abilities, Items and Trainer Feature interrupts remain gated by their exact categories.

Search, escort, protect-equipment/noncombatant, objective-aware withdrawal and disengage-after-objective remain AI tactical-policy blockers. Minecraft/Cobblemon/Craftics remains partial/blocking for persistent site/objective/equipment identity and authoritative non-KO result playback.

## Next boundary

Define replayable terminal failure/cancellation separately from arrival and objective success.

After that, define a separate objective-completion owner rather than treating physical arrival as completion. `AUTOPTU_RESOLVED` should be added only when the live handoff/session path exposes a replayable resolution event that can be tied to the exact accepted binding.
