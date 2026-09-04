# Engine readiness snapshot — Pass 255

Status: EVIDENCE SNAPSHOT
Date: 2026-09-04
Narrative effect: documents implementation dependencies only; changes no canon or PTU rules.

## Live read-only engine evidence

AutoPTU-Java head inspected: `371b8cdf7c7ec29d3c7b41140e6b052010747bdd`, merge PR #342, "Compose landing and status hooks through authoritative runtime dependencies".

The change composes `StatusApplicationHookRegistry` and `MovementLandingHookRegistry` through `BattleRuntimeDependencies` and verifies that forced-movement landing consumes the composed registries. This is concrete evidence for runtime composition of that landing/status seam. It does not prove complete movement, all statuses, all hazards, all reactions, all Abilities or all Move producers as complete families.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only coordinate synchronization after viewport resize. No new rules evidence.

## Permanent capability categories

targeting/footprints/range/LoS — VERIFIED within audited contracts.

base movement legality — VERIFIED within audited contracts.

complete movement including push/pull/knockback/interception/forced movement — PARTIAL. Forced-movement landing coverage and runtime hook composition improved, but the family is not complete.

core calculations — VERIFIED within audited contracts.

action economy/initiative — VERIFIED within audited contracts.

full turn/round lifecycle — PARTIAL.

full stateful damage pipeline — PARTIAL.

status lifecycle — PARTIAL. Runtime status hooks are composed in the new Java evidence, but representative hook integration does not establish full lifecycle parity.

terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING outside verified slices. Landing trap seams are stronger; the category remains incomplete.

move-specific behavior — PARTIAL; validate each authored Move.

abilities — PARTIAL; validate each authored Ability.

items — PARTIAL; validate each authored Item.

Trainer Features/perks — PARTIAL. No live Java evidence was found that authorizes Skill Stunt, Journey of Skill or another Feature to modify Pass 254/255 field identification.

AI legal-action infrastructure — VERIFIED within audited contracts.

AI tactical policy — BLOCKING as a complete family.

Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING end-to-end.

## Pass 255 reduced encounter

The observation-disturbance fixture requires no tactical AutoPTU capability family. Ouros owns evidence provenance and disturbance-pressure writes. Pass 248 owns pressure-to-projection policy. Minecraft/Cobblemon/Craftics is required only when the interaction becomes a real visible field observation.

## Pass 255 rich encounter

Structured shadowing/pursuit requires targeting/LoS, base movement, full lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement is additionally required for interception/blocking/forced movement. Terrain/weather/hazards/zones/reactions becomes exact only when an authored condition modifies the approach. Damage/status/Moves/Abilities/Items/Trainer Features are exact dependencies only when invoked.

## Blocking questions

1. Which adapter observations can reliably classify passive, distant and close approaches without Minecraft becoming ecology authority?
2. What species/context policy maps an accepted observation impact into disturbance pressure? Fixture deltas are not canon.
3. What quiet/recovery conditions are authoritative for pressure decay?
4. Does canon approve a Sendero research institution, protected observation protocol or physical-marking authority?
5. Which exact PTU Skills/Features, if any, can improve evidence quality once Java parity for those uses is verified?