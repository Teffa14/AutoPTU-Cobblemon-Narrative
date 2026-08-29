# Engine Readiness Snapshot — Pass 120

Status: EVIDENCE SNAPSHOT. This file records current evidence; it does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head inspected: `87fbcb2ab75b4642c762017a037a6c0dccb9d8ad` — `Bridge real interception sequence into PRE-target registry (#268)`.

AutoPTU current head inspected: `4ffd878e42051b9f8679ba3331ed7b69ee1ac4c1` — `Career: deduplicate corrupt active roster recovery`.

AutoPTU changed since Pass 119. The new work deduplicates repeated persisted `active_roster` IDs during browser recovery while preserving first-slot order and adds regression coverage. This is Career save/recovery hardening. It does not add tactical battle capability.

AutoPTU-Java has not advanced since Pass 119. Existing evidence for the real interception PRE-target bridge remains valid but bounded.

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

No category is promoted by this pass.

## Intercept evidence remains specific

The current Java head demonstrates a real Intercept path through the PRE-target registry. The runtime can execute the interception sequence, move a successful interceptor to the resolved interception position, preserve the originally declared target, replace the effective defender and continue through the authoritative Move pipeline. The associated regression also distinguishes a failed attempt that leaves target/position unchanged.

This supports a concrete Intercept route. It does not verify broad Push/Pull, broad Knockback, every forced-movement source, all Intercept windows, environmental displacement, generalized competing reaction ordering, every Move/Ability/Item/Trainer Feature registration or tactical objective policy.

## Pass 120 aerial-ropeway dependency assessment

World-state continuity for line identity, station identity, service restriction, trip chronology, interruption records, notices, maintenance/weather/rescue handoffs and historical route state does not require new battle capability.

The reduced Lower Station Withdrawal, Interrupted-Line Rescue Staging and Summit Diversion Junction encounters can be authored around static reviewed geometry. Noncombatants and operational machinery are resolved outside BattleSpec. AutoPTU receives explicit combatants and a stable arena.

The intended full forms have materially different requirements.

A withdrawal or escort stream depends on complete movement including interception/forced movement and on AI tactical policy that understands PROTECT/WITHDRAW/CLEAR_ROUTE rather than merely generating legal actions.

A moving or suspended carrier encounter would require exact moving-platform and coordinate semantics. Those are not established by base movement legality. If cabin motion displaces actors, complete forced movement is also implicated.

Wind, swaying, exposed edges, changing boarding areas, mechanical exclusion zones or other tactically meaningful environmental effects depend on terrain/weather/hazards/zones/reactions. That family remains BLOCKING.

Any fall, collision, crush, exposure or delayed environmental injury depends on the exact governing PTU/Caelo rule plus full stateful damage/status/lifecycle support appropriate to that effect. Minecraft native fall/collision behavior is not evidence.

Timed departure, phased interruption or delayed evacuation windows depend on full turn/round lifecycle, currently PARTIAL.

Any specific Move, Ability, Item or Trainer Feature affecting a ropeway scene remains dependent on its own implemented behavior and registration. Representative implementations elsewhere do not grant blanket readiness.

Semantic presentation of carrier departure, line interruption, passenger relocation or service restoration still depends on Minecraft/Cobblemon/Craftics adapter/playback support, currently BLOCKING.

## PTU/Caelo boundary for this pass

The internal source scan supports location-specific mechanical identity only when a governing source explicitly defines the effect. It does not establish generic cable-car, ropeway, gondola, moving-carrier, wind-sway, cable-climbing, aerial rescue or cabin-fall rules.

Therefore remain UNKNOWN: exact carrier speed/capacity, boarding movement, moving-platform combat, wind thresholds, fall rules, collision/crushing, emergency lowering, cable traversal, passenger carrying, species/type immunity, species-derived technical competence and any ropeway-specific Move/Ability/Item/Trainer Feature behavior without exact evidence.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon can present stations, cabins, supports, cables, barriers, queues, signs, particles, sounds, individual Pokémon and visual service-state changes. Those assets do not create tactical rules.

A moving cabin entity does not establish PTU movement. Redstone does not certify service. Minecraft fall damage does not implement PTU damage. Native collision does not create crushing or displacement. Rendered wind does not apply forced movement or accuracy changes. Cobblemon BattleState remains outside combatant selection, legality, HP/status, positions and outcome authority.

## Readiness result for new concepts

`The Station Above the Old Road` and the provenance mysteries are ready at narrative/world-state level with current capabilities.

Reduced static versions of all three Pass 120 encounters are compatible with the current verified baseline when their ordinary combatants use implemented legal mechanics.

Full Lower Station Withdrawal remains dependent on PARTIAL complete movement and BLOCKING AI tactical policy, with BLOCKING reactions/zones if access changes during combat.

Full Interrupted-Line Rescue Staging remains strongly blocked by moving-platform semantics, terrain/hazards/zones/reactions, objective-aware AI and semantic adapter/playback; damage/status/lifecycle become additional exact dependencies if fall, exposure or phased rescue effects are authored.

Full Summit Diversion Junction remains dependent on complete movement, generalized reactions, tactical policy and adapter/playback when the diversion occurs tactically rather than before BattleSpec.

## Unresolved engine questions

- Is there or will there be an authoritative moving-platform coordinate contract?
- How will active environmental displacement compose with normal forced movement and Intercept?
- What generalized reaction ordering contract will govern multiple competing reactions?
- How will objective-aware AI express escort, withdrawal, perimeter defense and route clearing?
- What semantic events must the Minecraft/Cobblemon/Craftics adapter consume for transport motion without becoming authority?
- Which exact Move/Ability/Item/Trainer Feature registrations are verified for any future aerial-transport encounter?

Until those questions have contracts and tests, the reduced variants remain the implementation-safe path.