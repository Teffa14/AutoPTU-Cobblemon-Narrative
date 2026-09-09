# Global NPC AI readiness snapshot — Pass 374

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository head inspected before writing: `88e3ee3e8d4414c21337f9c8583fa7a1ba4a7c49`.

Read-only AutoPTU-Java head: `a0e7a0089f3cb3dce1f8b82fd92c6b99f64a2207` (merge #413, generic round-start Ability lifecycle hook).

Read-only AutoPTU Python head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives.
6. full turn/round lifecycle — PARTIAL. Java merge #413 adds an authoritative generic round-start Ability dispatch hook, but that evidence covers only one lifecycle seam.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. The current registry/lifecycle evidence strengthens selected round-start interactions without verifying the full family.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including escort, preserve-cargo, intercept-to-inform, rescue-first, reroute-after-objective and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for authoritative objective acknowledgement, persistent cargo/resource identity and end-to-end playback.

## Pass 374 world-agent boundary

Pass 374 integrates the Pass 373 DeliveryReplanProvenanceLedger into coherent world persistence as `OUROS_NPC_WORLD_CHECKPOINT_V15`.

The recovery unit now validates the structured causal chain from a delivered envelope through evidence materialization and consumed replan provenance under the same digest as V14 world state.

The new checkpoint still does not prove acknowledgement, acceptance, selected plan, action start or AutoPTU outcome.

The reduced Pass 374 narrative case requires no AutoPTU tactical capability.

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED`
