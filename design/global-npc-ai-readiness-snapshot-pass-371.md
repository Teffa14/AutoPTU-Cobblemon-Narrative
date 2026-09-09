# Global NPC AI readiness snapshot — Pass 371

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository head inspected before writing: `e9f2a75be93e94bd5768c7f14dd22f221baba38d`.

Read-only AutoPTU-Java head: `50879211895641d740bb0e389ada075c98f366af` (merge #411, Intimidate / Minus [SwSh] reaction parity).

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
11. abilities — INDIVIDUALLY GATED. Java merge #411 strengthens evidence for the exact Intimidate / Minus [SwSh] nested Combat Stage reaction path and related event provenance; it does not verify the Ability family.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies such as intercept-to-inform, escort, preserve-equipment, reroute-after-objective and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for authoritative narrative objective acknowledgement, cargo/resource identity and end-to-end playback.

## Pass 371 narrative boundary

The reduced delivered-but-unacted communication scenario needs no AutoPTU battle capability. The richer field-interception version must declare every tactical dependency it selects rather than treating one representative reaction or movement test as family-wide support.

`MESSAGE_DELIVERED != CURRENT_RECALL != ACKNOWLEDGED != REPLAN_TRIGGERED != PLAN_CHANGED`

Pass 287 provides executable delivery-to-knowledge/replan coordination for managed world agents, while Pass 370 provides coherent persistence through transport provenance. A future checkpoint integration may validate their cross-owner causal relationship, but this snapshot does not claim that seam is implemented globally.
