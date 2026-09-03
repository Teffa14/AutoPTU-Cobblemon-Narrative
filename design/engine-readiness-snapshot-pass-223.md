# Engine readiness snapshot — pass 223

Status: AUDIT SNAPSHOT
Date: 2026-09-03

## Repositories inspected

Narrative main before this pass: `e67971fc27537a1d3d133a5f0c310bdb97dd6984`.

AutoPTU-Java read-only head: `c62e59beb9472116e55f36d5814fa1ef1f95ced6` (`Add authoritative tile-trap state store (#331)`).

Python AutoPTU read-only head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation coordinate synchronization only).

## Permanent battle capability families

1. Targeting/footprints/range/LoS — VERIFIED within previously audited contracts.
2. Base movement legality — VERIFIED within previously audited contracts.
3. Complete movement incl push/pull/knockback/interception/forced movement — PARTIAL.
4. Core calculations — VERIFIED within previously audited contracts.
5. Action economy/initiative — VERIFIED within previously audited contracts.
6. Full turn/round lifecycle — PARTIAL.
7. Full stateful damage pipeline — PARTIAL.
8. Status lifecycle — PARTIAL.
9. Terrain/weather/hazards/zones/reactions — BLOCKING as a complete family when required.
10. Move-specific behavior — PARTIAL.
11. Abilities — PARTIAL.
12. Items — PARTIAL.
13. Trainer Features/perks — PARTIAL.
14. AI legal-action infrastructure — VERIFIED within previously audited contracts.
15. AI tactical policy — BLOCKING as a complete policy.
16. Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING for complete end-to-end world feedback.

## Pass 223 boundary

The new `ABSTRACT_ECOLOGICAL_CONFLICT` resolver intentionally does not call AutoPTU. It computes aggregate world pressure and therefore does not require battle families 1–15 for off-screen resolution.

It must not be used as evidence that any battle capability is implemented.

When a concrete fight is witnessed/promoted to a BattleSpec, normal battle dependencies apply to every mechanic used.

The primary implementation blocker for the full pass-223 experience is world-runtime ecology persistence plus category 16 manifestation: population/strength state must persist, and semantic habitat/NPC changes must be projected reliably into Minecraft/Cobblemon without making the adapter authoritative.

## New Java evidence

Java #331 adds an authoritative tile-trap state store and deterministic trap snapshot ordering. That is useful evidence for one stateful tactical subsystem. It does not promote complete movement, terrain/hazards/zones/reactions, Move behavior, Features or tactical AI to globally complete.

## Unverified interfaces exposed by pass 223

- exact mapping from Ouros wild `progression_band` / combat exposure to legal PTU Level;
- progression writeback from an actual AutoPTU battle to a persistent wild individual;
- world-runtime abstract predation transition contract;
- semantic vegetation/habitat state adapter;
- managed-development-zone monitoring and institutional response state;
- reliable cross-ecosystem relocation transfer for a persistent dangerous outlier;
- NPC observation/report generation from ecology state without exposing server omniscience.

These are world/integration requirements, not new permanent battle categories.