# Engine readiness snapshot — Pass 253

Status: LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-04
Narrative dependency target: recurring wild individual recognition and optional follow/pursuit

## Read-only engine evidence inspected

AutoPTU-Java live head inspected for this pass: `23ac19915d5b71bbae52d7e089741579527cdc81`, `Freeze forced movement landing across move producers (#341)`.

This is additional evidence for forced-movement landing consequences across several move producers. It does not demonstrate the full complete-movement family, every reaction/hazard interaction, or all move-specific behavior.

AutoPTU Python live head inspected for this pass: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest relevant change remains presentation/coordinate synchronization evidence rather than new rules-family coverage.

Neither read-only repository was modified by Pass 253.

## Permanent capability categories

Targeting/footprints/range/LoS — VERIFIED within currently audited contracts. Needed by the rich recognition encounter only if detection, targets or tactical sight lines are mechanically adjudicated.

Base movement legality — VERIFIED within currently audited contracts. Needed for a mechanically adjudicated follow/pursuit.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL. Needed if pursuit uses interception or other complete-movement interactions. Current forced-movement landing evidence is representative, not family-complete.

Core calculations — VERIFIED within currently audited contracts. Not required by the reduced Pass 253 recognition loop.

Action economy/initiative — VERIFIED within currently audited contracts. Relevant only if the rich version enters tactical timing.

Full turn/round lifecycle — PARTIAL. Blocking for a rich tactical pursuit that depends on complete lifecycle semantics.

Full stateful damage pipeline — PARTIAL. Not required unless the encounter escalates to damaging actions.

Status lifecycle — PARTIAL. Not required unless statuses are actually invoked.

Terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING. Required only when the rich route gives these systems mechanical meaning.

Move-specific behavior — PARTIAL. Required only for moves actually used.

Abilities — PARTIAL. Required only for abilities actually used.

Items — PARTIAL. Required only for items actually used.

Trainer Features/perks — PARTIAL. Required if observer skill, interrupts or other Trainer mechanics are given rules authority. Pass 253 does not assume such support.

AI legal-action infrastructure — VERIFIED within currently audited contracts. Needed if an autonomous wild actor chooses legal tactical actions during a rich pursuit.

AI tactical policy — BLOCKING as a complete family. Needed for a rich autonomous pursuit/escape policy.

Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING end-to-end. This is the main dependency for the reduced version because repeated presentation, observation capture, save/load continuity and public/private evidence separation must survive real runtime behavior.

## Pass 253 reduced version

The reduced encounter performs observation capture and identity-hypothesis updates only. No battle opens. No PTU movement, damage, status, move, ability, item or Trainer Feature is required.

Its critical implementation dependency is the Minecraft/Cobblemon/Craftics adapter/playback family plus Ouros persistence. Pass 252 identified concrete Cobblemon save/load event surfaces, but the actual project runtime dependency pin and custom projection-receipt roundtrip remain unverified.

## Pass 253 rich version

A mechanically adjudicated follow/pursuit requires at minimum base movement legality, complete movement when interception or forced movement occurs, full turn/round lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback support.

Add targeting/LoS when detection and sight lines are tactical. Add terrain/weather/hazards/zones/reactions only when route conditions mechanically matter. Add damage/status/Moves/Abilities/Items/Trainer Features only when the selected encounter actually invokes them.

## Blocking questions

The runtime still needs proof that observer-facing records cannot leak internal actor/lease/UUID correlation through adapter or UI payloads.

Ouros still needs a canon decision for any hard individual-identification mechanism. Without that decision, ordinary observations are capped at `PROBABLE_SAME_INDIVIDUAL`.

If Trainer Features or research equipment are later allowed to improve identification, their exact PTU rules and Java parity must be verified before they change confidence transitions.
