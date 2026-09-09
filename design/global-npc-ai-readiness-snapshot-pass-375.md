# Global NPC AI readiness snapshot — Pass 375

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository baseline inspected before writing: `b8302ba5b6ac63627bc9c68f7e107f184c6b6772`.

Read-only AutoPTU-Java head inspected: `948f42cfcfd34000087cb0667b4926c9aa2c8df4` (merge #414, round-start Ability dispatch wired into the authoritative lifecycle registry after Trainer Feature round-start dispatch).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives.
6. full turn/round lifecycle — PARTIAL. Java merge #414 places the round-start Ability hook in the authoritative lifecycle registry with explicit ordering after round-start Trainer Features, but this verifies a lifecycle seam rather than the whole lifecycle family.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. The new lifecycle wiring increases confidence for admitted round-start Ability content, but does not verify all Abilities.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including rescue-first, protect-vulnerable-target, preserve-equipment, route-clearing, escort and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for authoritative objective acknowledgement, persistent rescue-target/cargo identity, changing hazard presentation and end-to-end playback.

## Pass 375 world-agent boundary

Pass 375 adds standalone plan-selection provenance after the V15 delivery/replan recovery boundary.

The new owner can preserve the exact decision-time world-agent input set and replay the existing planner to verify the persisted AgendaDecision. It can also require each trigger in the selection batch to have structured consumed-trigger provenance from Pass 373/374.

This does not yet place plan-selection provenance under the coherent V15 world digest.

The reduced Pass 375 narrative case requires no AutoPTU tactical capability.

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED != ACTION_SUCCEEDED`

## PTU / Caelo boundary

Internal source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List when available.

Pass 375 changes world-agent provenance only. It does not promote any PTU combat capability and does not treat the Java round-start wiring as proof that the full Ability or reaction families exist.
