# Engine Readiness Snapshot — Pass 122

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `87fbcb2ab75b4642c762017a037a6c0dccb9d8ad` — `Bridge real interception sequence into PRE-target registry (#268)`.

AutoPTU current head: `10412030fb7da0f83f37b2dbdd7f8d6e4bc4e9ba` — `Career: deduplicate corrupt Pokemon records during recovery`.

AutoPTU-Java has not advanced since Pass 121. AutoPTU has advanced by one Career/browser-recovery hardening commit. The new AutoPTU commit preserves the first valid persisted Pokémon record for each duplicate ID during recovery and adds regression coverage. It does not add tactical battle capability.

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

No category is promoted by Pass 122.

## Existing Intercept evidence remains bounded

The Java head still verifies one concrete Intercept route through the PRE-target registry and authoritative Move pipeline. A successful interception can move the interceptor to the resolved interception position, preserve the declared target as historical context, replace the effective defender and continue resolution. A failed attempt leaves target and position unchanged.

This remains strong evidence for that path only.

It does not establish:
- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- every Intercept window;
- generalized competing reaction ordering;
- every Move/Ability/Item/Trainer Feature registration;
- objective-aware tactical policy;
- environmental hazard execution;
- semantic adapter playback.

## Pass 122 building-assessment readiness

The building-safety continuity model itself requires no new battle capability.

These objects are world-state/provenance data:
- assessed structures;
- spatial assessment scopes;
- condition observations;
- technical assessments;
- use restrictions;
- occupancy/use authorizations;
- reevaluation triggers;
- revision edges;
- evidence gaps;
- public notices;
- maintenance/residential/service handoffs.

The mysteries `Five Dates on One Door`, `Three Inspectors, Two Authorities`, `Four Notices, One Building` and the exploration `The Closed Floor Above the Market` can run on current world-state infrastructure when all traversed geometry is explicitly stable and authorized.

## Full encounter dependency assessment

### Assessment Team Withdrawal

Targeting/footprints/range/LoS — VERIFIED baseline.

Base movement legality — VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL if Intercept, escort positioning or forced displacement matters.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL when the withdrawal uses timed windows or phased departure.

Full stateful damage pipeline — PARTIAL for ordinary governed combat effects.

Status lifecycle — PARTIAL when chosen legal effects apply status.

Terrain/weather/hazards/zones/reactions — BLOCKING if restriction cells change, unstable areas have tactical effects or generalized reactions guard the route.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL.

Trainer Features/perks — PARTIAL.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT/WITHDRAW behavior.

Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic withdrawal and restriction-boundary playback.

Reduced form readiness: READY. Complete the assessment-team withdrawal in Ouros world state before BattleSpec creation. Exclude noncombatants, equipment and restricted scopes. Resolve a conventional battle on static reviewed geometry.

### Partial Reopening Perimeter

The full concept becomes dependent on PARTIAL complete movement when civilians or combatants must be intercepted or displaced around the boundary.

It becomes directly BLOCKING on terrain/weather/hazards/zones/reactions if the boundary is an engine zone, changes during the encounter or crossing it causes generalized reactions.

It depends on BLOCKING AI tactical policy if enemies or allies must understand a KEEP_OUT/PROTECT/WITHDRAW objective.

It depends on BLOCKING adapter/playback if scoped closure/reopening and civilian withdrawal must be represented semantically during battle.

Reduced form readiness: READY. Temporarily close the public-facing scope first, remove civilians, exclude the restricted area and run a static legal encounter in authorized geometry. Post-battle reopening remains a world-state decision.

### Reinspection After a Secondary Event

A full active-damage version is currently BLOCKING where it uses changing cells, falling debris, unstable floors, collapse zones or generalized reactions.

Delayed secondary changes depend on PARTIAL full turn/round lifecycle.

Any falling-object, crushing, collapse or exposure damage would depend on PARTIAL full stateful damage pipeline plus an exact governing PTU/Caelo rule that has not been established here.

Any automatic status consequence would depend on PARTIAL status lifecycle plus an exact governing rule.

Forced displacement depends on PARTIAL complete movement.

Protection/withdrawal objectives depend on BLOCKING AI tactical policy.

Authoritative environmental playback depends on BLOCKING Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced form readiness: READY. End the secondary event before BattleSpec creation, keep newly uncertain scopes inaccessible and use only stable reviewed geometry. The building remains `REEVALUATION_REQUIRED` regardless of battle victory.

## PTU/Caelo boundary

The internal source scan continues to support environmental mechanical identity only when a governing source explicitly defines the effect. Caelo's authored environmental effects do not establish a universal damaged-building subsystem.

Remain UNKNOWN without exact evidence:
- universal collapse checks;
- structural HP;
- falling-debris damage;
- unstable-floor mechanics;
- rubble difficult terrain;
- crushing;
- rescue/carry actions;
- building-entry Skill DCs;
- demolition rules;
- aftershock tactical timing;
- smoke/fire/flood effects inside structures beyond exact sourced effects;
- species-derived collapse prediction;
- Type-derived structural immunity;
- Move-based universal repair or demolition;
- Trainer Feature-based universal inspection authority.

Public PTU homebrew suggestions about collapsing terrain remain research inspiration only and do not fill these gaps.

## Boundary with existing narrative systems

Facility Maintenance already owns faults, work orders, repairs and verification.

Residential continuity already owns habitability, displacement and household return.

Crisis/Rescue already owns acute evacuation, rescue and stabilization.

Civic Governance already owns major future public decisions and reconstruction proposals.

Hazard-specific systems own the initiating earthquake, fire, slope failure, flood, volcanic event or other cause.

Pass 122 therefore adds no competing repair or crisis engine. It stores scoped assessment/reentry state between those systems.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render:
- damaged and restored building variants;
- barriers;
- alternate doors;
- notices;
- scaffolding;
- restricted floors;
- reopened plazas;
- NPC workers/assessors;
- individual Pokémon routines;
- persistent ruins.

Those visuals remain presentation.

Block damage does not produce a structural assessment. Replacing blocks does not authorize occupancy. A posted sign does not override authoritative state. Falling blocks do not implement PTU damage. Native entity collision does not implement forced movement. Potion effects do not define structural exposure. Cobblemon BattleState remains outside combatant selection, legality, HP/status, tactical positions and outcome authority.

## Readiness result

Narrative/world-state: READY for scoped building assessments, partial reopening, reassessment, revision-history mysteries, adaptive-reuse callbacks and repair-to-reentry handoffs.

Reduced static encounters: READY on the current verified baseline, subject to ordinary implemented mechanics of the selected combatants.

Full Assessment Team Withdrawal: PARTIAL/BLOCKING due to complete movement, lifecycle, reactions/zones, tactical policy and playback.

Full Partial Reopening Perimeter: PARTIAL/BLOCKING when dynamic boundaries, withdrawal, generalized reactions or objective-aware behavior matter.

Full Reinspection After a Secondary Event: BLOCKING for active structural hazards/changing cells; additional PARTIAL movement/lifecycle/damage/status dependencies apply only when exact governed mechanics are authored.

## Unresolved mechanical questions

- Does project PTU/Caelo evidence define any exact structural collapse, debris, rubble, crushing or unstable-floor mechanics that should be registered rather than treated narratively?
- How will generalized reaction ordering compose with changing hazard/restriction zones?
- How will tactical AI represent PROTECT, WITHDRAW and KEEP_OUT/CLEAR_ROUTE objectives?
- How will a BattleSpec identify a reviewed stable subset of a larger damaged Minecraft structure without allowing the adapter to decide safety?
- Which semantic events must playback consume for evacuation, boundary changes and post-battle access changes?
- Are there exact Moves, Abilities, Items or Trainer Features that legally interact with structures, debris or repair, and what scopes do their rules permit?

Until exact contracts and tests answer those questions, reduced variants remain the implementation-safe route.