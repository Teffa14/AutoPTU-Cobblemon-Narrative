# Global NPC AI readiness snapshot — Pass 377

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository baseline inspected before writing: `041dde6724fcc3689c7b001377b982484c79415f`.

Read-only AutoPTU-Java head inspected: `948f42cfcfd34000087cb0667b4926c9aa2c8df4` (merge #414, admitted round-start Ability dispatch wired into the authoritative lifecycle after round-start Trainer Feature dispatch).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives.
6. full turn/round lifecycle — PARTIAL. Java merge #414 verifies one admitted round-start Ability ordering seam after Trainer Feature dispatch; it does not establish the complete lifecycle family.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Current round-start wiring improves confidence only for specifically admitted content.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including rescue-first, protect-cargo, escort, search, route-clearing, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent route/cargo identity, rescue objectives, non-KO objective acknowledgement and authoritative end-to-end playback.

## Pass 377 world-agent boundary

Pass 377 adds standalone `OUROS_NPC_ACTION_START_PROVENANCE_V1` after the V16 plan-selection recovery seam.

The owner proves two executable start families using replayable existing contracts:

`PLAN_SELECTED -> TRAVEL_EDGE_STARTED`

and

`PLAN_SELECTED -> REQUEST_AUTOPTU -> AUTOPTU_BINDING_ACCEPTED`

It does not yet place this owner under the coherent V16 world digest.

The causal chain remains:

`DELIVERED != MATERIALIZED != REPLAN_TRIGGERED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED != ACTION_SUCCEEDED`

A planned departure, reserved departure minute or waiting travel state is not an action start. An AutoPTU request is not a binding acceptance. A binding acceptance is not a battle outcome.

The reduced Pass 377 narrative case requires no AutoPTU tactical capability.

## PTU / Caelo boundary

Internal source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List when available.

Pass 377 introduces no battle rule, species placement, regional fact or capability promotion. Public research informs world-state and encounter structure only.
