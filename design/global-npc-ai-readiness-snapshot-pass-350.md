# Global NPC AI / AutoPTU readiness snapshot — Pass 350

Status: EVIDENCE SNAPSHOT
Date: 2026-09-08

## Read-only engine heads inspected

AutoPTU-Java main: `241f092a9af01e11f430644c37565ea91e7812d6` — merge PR #400, `Freeze Arena Trap effect mutation plan`.

The slice adds `ArenaTrapEffectPlan`, freezing the Python-oracle effect shape after target eligibility: `Slowed`, duration one round, Arena Trap source/source ID, ordered effects per eligible target. The implementation deliberately remains a plan between targeting and runtime mutation and does not couple the contract to status storage or Minecraft/Cobblemon adapters.

This is stronger evidence for one Arena Trap seam. It does not prove status application, expiration/cleanup, full Ability coverage, full lifecycle, or adapter playback.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. The commit explicitly states presentation only and no battle rules or outcomes change.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts. PR #399 remains narrow positive evidence for authoritative Arena Trap candidate projection.

Base movement legality: VERIFIED within previously audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within previously audited deterministic arithmetic.

Action economy/initiative: VERIFIED for audited primitives; tactical pickup/drop/handoff remains individually gated.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. PR #400 freezes an Arena Trap Slowed effect plan but does not establish storage/application/expiration as a complete lifecycle.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Arena Trap now has authoritative candidate projection plus a frozen effect plan; the family remains incomplete.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope.

AI tactical policy: BLOCKING for escort, protect-carrier, preserve-resource, delivery-first and disengage-after-objective goals.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

## Pass 350 narrative impact

The reduced displaced-reservation notice scenario requires no AutoPTU battle capability. A rich field-transport continuation must retain the category gates above. No representative Arena Trap slice promotes a capability family wholesale.
