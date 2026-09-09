# Global NPC AI readiness snapshot — Pass 372

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository head inspected before writing: `ee23635d369f7fa6c659cae5534e79157d30e762`.

Read-only AutoPTU-Java head: `c5713b41c99a1b969c7d934fc38d35acd0295d6a` (merge #412, Intimidate registered in the generic round-start Ability registry after parity gates).

Read-only AutoPTU Python head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Java merge #412 registers the exact Intimidate round-start effect in the generic registry after prior parity work. This strengthens that specific runtime path and does not verify the Ability family or every round-start Ability.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies such as intercept-to-inform, escort, preserve-cargo, rescue-first, reroute-after-objective and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for authoritative narrative objective acknowledgement, persistent cargo/resource identity and end-to-end playback.

## Pass 372 boundary

The reduced provenance investigation requires no AutoPTU battle capability. The richer interception/rescue version must declare each tactical mechanic independently.

World-agent evidence inspected in this pass shows that V14 preserves communications and the coordinator/replan snapshot, while Pass 287 performs delivery materialization and wake scheduling. The unresolved issue is structured durable provenance after a replan trigger has been consumed. This snapshot does not claim that the new persistence seam is implemented.

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED`