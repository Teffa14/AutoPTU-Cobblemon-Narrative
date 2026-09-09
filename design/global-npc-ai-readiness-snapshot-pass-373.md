# Global NPC AI readiness snapshot — Pass 373

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository head inspected before writing: `68b92f7bb91951b53697277a4c348e142d8abde4`.

Read-only AutoPTU-Java head: `a0e7a0089f3cb3dce1f8b82fd92c6b99f64a2207` (merge #413, generic round-start Ability lifecycle hook).

Read-only AutoPTU Python head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives.
6. full turn/round lifecycle — PARTIAL. Java merge #413 adds a generic authoritative round-start Ability lifecycle hook, but one lifecycle hook does not establish the full turn/round lifecycle.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Merge #413 executes the round-start dispatch plan through `RoundStartAbilityEffectRegistry`; unsupported families remain explicit unhandled invocations. This strengthens round-start orchestration evidence without verifying all Ability behavior.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies such as intercept-to-inform, escort damaged cargo, preserve samples, rescue-first, reroute-after-objective and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for authoritative narrative objective acknowledgement, persistent cargo/resource identity and end-to-end playback.

## Pass 373 world-agent boundary

The reduced Pass 373 narrative case requires no AutoPTU battle capability.

The new narrative runtime closes a standalone provenance seam after Pass 287 / Pass 284: successful delivery materialization can now retain receiver, claim, root and wake trigger, and consumed replan triggers can retain agent, reason, source, due time, priority and processed batch after the pending trigger has disappeared.

This is not yet integrated into V14 coherent world persistence. No claim is made that a restart of the full world already validates the new ledger under the same digest.

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED`