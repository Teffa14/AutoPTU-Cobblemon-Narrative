# Global NPC AI readiness snapshot — Pass 376

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository baseline inspected before writing: `58fbf3b624ff19b55e2d567c3f103d88166aea76`.

Read-only AutoPTU-Java head inspected: `948f42cfcfd34000087cb0667b4926c9aa2c8df4` (merge #414, round-start Ability dispatch wired into the authoritative lifecycle registry after round-start Trainer Feature dispatch).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives.
6. full turn/round lifecycle — PARTIAL. Java merge #414 verifies the ordering seam that dispatches admitted round-start Abilities after round-start Trainer Features; it does not prove the whole lifecycle family.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Round-start lifecycle wiring improves confidence only for content admitted through that verified seam.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including escort, preserve-equipment, rescue-first, route-clearing, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for authoritative objective acknowledgement, persistent route/cargo identity, changing hazard presentation and end-to-end playback.

## Pass 376 world-agent boundary

Pass 376 integrates the Pass 375 `PlanSelectionProvenanceLedger` into coherent world persistence as `OUROS_NPC_WORLD_CHECKPOINT_V16`.

The recovery unit now validates plan-selection replay and its consumed-trigger provenance under the same digest as V15 delivery/materialization/replan history.

The new boundary is:

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED != ACTION_SUCCEEDED`

Plan selection is now restart-durable. Action start is still a separate unimplemented provenance owner.

The reduced Pass 376 narrative case requires no AutoPTU tactical capability.

## PTU / Caelo boundary

Internal source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List when available.

Pass 376 changes world-agent persistence only. It introduces no battle rule, species placement, regional fact or mechanical promotion. The Java lifecycle evidence remains scoped to its verified seam and does not upgrade the full Ability, reaction or lifecycle families.
