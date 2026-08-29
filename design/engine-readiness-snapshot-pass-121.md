# Engine Readiness Snapshot — Pass 121

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `87fbcb2ab75b4642c762017a037a6c0dccb9d8ad` — `Bridge real interception sequence into PRE-target registry (#268)`.

AutoPTU current head: `4ffd878e42051b9f8679ba3331ed7b69ee1ac4c1` — `Career: deduplicate corrupt active roster recovery`.

Neither repository has advanced since Pass 120. Existing evidence therefore remains valid and bounded.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No category is promoted by Pass 121.

## Existing Intercept evidence

The Java head continues to verify one concrete Intercept path through the PRE-target registry and authoritative Move pipeline. A successful interceptor can move to its resolved interception position, preserve the originally declared target, replace the effective defender and continue resolution. A failed attempt leaves target and position unchanged.

This is not evidence for broad Push/Pull, broad Knockback, every forced-movement source, all Intercept windows, environmental displacement, generalized competing reaction ordering, every Move/Ability/Item/Trainer Feature registration or tactical objective policy.

## Pass 121 drought/scarcity dependency assessment

The continuity model itself requires no new battle capability. Scarcity episodes, observation bundles, monitoring gaps, assessment revisions, cause claims, allocation handoffs, temporary supply arrangements, low-water exposed features and subsystem-specific recovery checkpoints are world-state data.

The exploration `The Road Under the Reservoir` and provenance mysteries can run with the current baseline because the playable area can be authored as static inspected geometry and all uncertain environmental effects can remain world state.

Reduced forms of Reservoir Margin Withdrawal, Exposed Causeway Perimeter and Temporary Water Point Diversion can also run now if noncombatants, controlled water, unstable terrain and operational infrastructure are resolved before BattleSpec creation.

## Full encounter dependencies

Reservoir Margin Withdrawal requires PARTIAL complete movement when Intercept, escorting or forced displacement matters. It requires PARTIAL full turn/round lifecycle if the withdrawal has timed windows. If mud, retreating water, unstable shoreline or exclusion zones change tactical cells, terrain/weather/hazards/zones/reactions is directly BLOCKING. Objective-aware PROTECT/WITHDRAW behavior depends on BLOCKING AI tactical policy. Semantic civilian relocation depends on BLOCKING adapter/playback support.

Exposed Causeway Perimeter requires BLOCKING terrain/weather/hazards/zones/reactions if cells become unstable, inundated, slippery or otherwise tactically meaningful. Any fall, collapse, exposure, fatigue or status effect also requires the exact governing PTU/Caelo rule and the appropriate PARTIAL damage/status/lifecycle families. Static geometry alone does not establish those mechanics.

Temporary Water Point Diversion requires PARTIAL complete movement and BLOCKING AI tactical policy if civilians are actively rerouted during combat. Generalized reaction behavior remains BLOCKING through the terrain/weather/hazards/zones/reactions family where reaction windows are needed. Queue, capacity, custody and water-service rules stay outside AutoPTU.

## PTU/Caelo boundary

The internal source scan supports environmental mechanical identity only where a governing source explicitly defines the effect. It does not establish a generic drought simulation.

Remain UNKNOWN without exact evidence: dehydration, thirst, fatigue from scarcity, dry-ground penalties, dust LoS/accuracy effects, groundwater movement, water-volume creation by Moves, Rain Dance as reliable civic drought resolution, the Drought Ability as regional climate authority, Sunny Day as long-term hydrology, species-derived water finding or drought prediction, crop-yield mechanics, drought-driven ecological damage, water carrying under combat rules, and drought-specific Move/Ability/Item/Trainer Feature interactions.

The existence of a named Move or Ability with weather language does not authorize a settlement-scale or season-scale world-state effect.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render dry streambeds, changing shorelines, exposed roads, temporary water points, queues, signs, NPC routines, individual Pokémon, particles, rain and water blocks.

Those visuals do not become authority. Rain rendering does not close a scarcity episode. Water blocks do not prove potable supply, source recovery or custody. Buckets do not establish service capacity. Native hunger or potion effects do not implement PTU dehydration. Biome state does not establish drought. Cobblemon BattleState remains outside combatant selection, legality, HP/status, positions and outcome authority.

## Readiness result

Narrative/world-state: READY for scarcity investigations, staggered recovery, provenance mysteries, temporary-arrangement stories, historical low-water exploration and cross-system consequence handoffs.

Reduced static encounters: READY on the current verified baseline, subject to the ordinary implemented mechanics of chosen combatants.

Full Reservoir Margin Withdrawal: PARTIAL/BLOCKING due to complete movement, lifecycle, objective-aware AI and any environmental zones.

Full Exposed Causeway Perimeter: BLOCKING when dynamic terrain or environmental effects matter; additional PARTIAL damage/status/lifecycle dependencies apply only if exact governed effects are authored.

Full Temporary Water Point Diversion: PARTIAL/BLOCKING due to complete movement, generalized reactions, objective-aware AI and semantic playback.

## Unresolved mechanical questions

- Which exact PTU/Caelo rules, if any, govern dehydration, thirst or prolonged dry conditions?
- How will dynamic environmental cells compose with normal movement and forced movement?
- What generalized reaction ordering contract will govern protection and withdrawal scenes?
- How will tactical AI express PROTECT, WITHDRAW and CLEAR_ROUTE objectives?
- Which semantic events must the adapter consume to show evacuation, rerouting or service-state changes without becoming authority?
- Which exact Move/Ability/Item/Trainer Feature registrations can affect water availability or dry environments, and at what scale?

Until those questions have contracts and tests, reduced variants remain the implementation-safe path.