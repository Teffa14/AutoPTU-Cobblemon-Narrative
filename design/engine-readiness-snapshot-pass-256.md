# Engine readiness snapshot — Pass 256

Status: EVIDENCE SNAPSHOT
Date: 2026-09-04
Narrative effect: documents implementation dependencies only; changes no canon or PTU rules.

## Live read-only engine evidence

AutoPTU-Java head inspected: `faf25d7473920f4bd2e03520553f5db5da20abd8`, merge PR #344, "Compose move and damage hooks from current main".

The change moves EffectiveMoveHookRegistry, DamageModifierHookRegistry, PreDamageReactionHookRegistry and PostDamageHookRegistry into BattleRuntimeDependencies and verifies preservation of injected registries. This is concrete evidence that more move/damage hook seams now compose through the authoritative runtime dependency object. It strengthens runtime composition. It does not establish complete move-specific parity, the full stateful damage pipeline, all reactions, all Abilities or all lifecycle behavior.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only coordinate synchronization after viewport resize. No new rules evidence.

## Permanent capability categories

targeting/footprints/range/LoS — VERIFIED within audited contracts.

base movement legality — VERIFIED within audited contracts.

complete movement including push/pull/knockback/interception/forced movement — PARTIAL.

core calculations — VERIFIED within audited contracts.

action economy/initiative — VERIFIED within audited contracts.

full turn/round lifecycle — PARTIAL.

full stateful damage pipeline — PARTIAL. Runtime damage hook composition improved, but composition is not complete semantic parity.

status lifecycle — PARTIAL.

terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING outside verified slices.

move-specific behavior — PARTIAL. Runtime effective-move hooks are now injectable/composed, but every authored Move still requires exact evidence.

abilities — PARTIAL.

items — PARTIAL.

Trainer Features/perks — PARTIAL.

AI legal-action infrastructure — VERIFIED within audited contracts.

AI tactical policy — BLOCKING as a complete family.

Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING end-to-end.

## Pass 256 reduced ecology encounter

The individual habituation/sensitization fixture requires no tactical AutoPTU family. Ouros owns individual response history and the distinction between shared disturbance pressure and individual response state. Pass 248 consumes the resulting projection contribution. Minecraft/Cobblemon/Craftics is required to present the different exposure outcomes in-world.

## Pass 256 rich encounter

Structured pursuit or interception requires targeting/LoS, base movement, action economy/initiative, full lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement becomes exact when interception, blocking, push/pull or forced movement occurs. Terrain/weather/hazards/zones/reactions becomes exact only when a scene uses them. Damage/status/Moves/Abilities/Items/Trainer Features become exact dependencies only when invoked.

## Blocking questions

1. Which species-policy fields define plausible response ranges without turning fixture values into canon?
2. Which individual-history fields are persistent enough to drive later projection while remaining invisible to player-facing knowledge?
3. Which adapter observations can distinguish quiet coexistence, close approach, pursuit and physical handling reliably?
4. What recovery/forgetting model is appropriate for response history, and when should old exposures lose influence?
5. What exact Java evidence is required before a flee/avoid/tolerate response can cross from ecology projection into tactical AI policy?