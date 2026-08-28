# Engine Readiness Snapshot — Pass 98

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or setting canon.
Date: 2026-08-28

## Scope

Pass 98 adds wildfire/fire-response incident continuity: verified reports, sectors, operational attempts, evacuation/access references, residual-fire review, reignition evidence, re-entry separation and post-fire handoffs.

Narrative baseline before Pass 98 writes: `df343eea2e9d8d11dbe33cadb88087c86738ecdf`.

Read-only evidence inspected:

- full recursive Narrative repository tree, confirmed untruncated;
- existing Crisis, Forestry and Weather architecture;
- Pass 97 readiness snapshot;
- AutoPTU-Java head `39b81222af080dd5b2db9b3efdfe742b746d5f5d`;
- AutoPTU head `699adf5a50936d9759479dc9bc41a2b8b0a4c0ef`;
- AutoPTU implementation evidence for named Burn/Fire/Weather effects;
- permanent Cobblemon authority boundary already established by the project.

## Live engine delta

AutoPTU-Java has not advanced beyond #255 in the inspected evidence. #255 freezes a specific `_attempt_intercept` orchestration path against a pinned Python oracle. It verifies ordering/check/resource/position checkpoints for that path, including melee forced movement.

That evidence remains narrow. It does not prove:

- all Intercept variants in all contexts;
- competing reactions;
- generalized reaction ordering;
- broad knockback;
- every Push/Pull/forced-movement source;
- environmental displacement;
- dynamic hazard-triggered movement;
- complete Move/Ability/Item/Trainer Feature hook coverage;
- objective-aware tactical behavior;
- full semantic transcript/playback parity.

AutoPTU advanced to `699adf5a50936d9759479dc9bc41a2b8b0a4c0ef` with Career lazy-route failure recovery. The change adds a visible recovery boundary for route bundle load failures and protects saved Career state. It does not add tactical battle capability.

No permanent category is promoted in Pass 98.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Family-level geometry/range/LoS evidence remains sufficient for Narrative readiness. This does not provide smoke-specific visibility rules.

`base movement legality`

Base movement and established movement-mode legality remain verified. Dynamic flame fronts, collapsing terrain and emergency vehicle movement are outside this category.

`core calculations`

Existing stat, damage-base, type, stage and accuracy primitives remain verified. They do not define environmental wildfire damage.

`action economy/initiative`

Typed action budget and deterministic initiative/order remain verified.

`AI legal-action infrastructure`

Legal-action generation remains verified as infrastructure. It does not supply emergency/withdrawal tactics.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Push/Pull and the Intercept path have substantial evidence, but family-wide forced movement/reaction coverage remains incomplete. Fire-driven displacement has no verified generic implementation.

`full turn/round lifecycle`

PARTIAL. Existing phases/action budgets do not establish all lifecycle behavior required for changing hazard states, delayed effects or multi-round environmental transitions.

`full stateful damage pipeline`

PARTIAL. Named battle damage behavior exists, but a complete family-wide pipeline for every interaction remains unfinished. No generic world-fire-to-damage mapping is verified.

`status lifecycle`

PARTIAL. Burn and other representative statuses exist in PTU/AutoPTU evidence, while complete status-controller coverage is not verified. Environmental smoke/fire cannot apply Burn merely because the status exists.

`move-specific behavior`

PARTIAL. Representative Moves cannot stand in for complete registry coverage. A Move with Fire or Water typing does not automatically gain wildfire interaction.

`abilities`

PARTIAL. Individual Ability implementations exist; they do not prove universal interaction with world fire, smoke or heat.

`items`

PARTIAL. Representative Item behavior does not establish full content coverage or emergency equipment rules.

`Trainer Features/perks`

PARTIAL. Intercept-related Features/perks and other representatives do not establish full hook coverage or firefighting/rescue Features.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for mechanically rich wildfire encounters. Dynamic flames, smoke/visibility, heat, embers, ash, spreading sectors, burning structures, residual hot spots, collapsing trees, wind-driven effects and tactical exclusion areas require exact PTU/Caelo rules and verified engine contracts before they may affect battle.

`AI tactical policy`

BLOCKING. The engine can enumerate legal actions but does not yet establish objective-aware policy for withdrawal, perimeter protection, route clearing, territorial retreat, preserving escape corridors or avoiding environmental danger.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. Minecraft/Cobblemon can present fire/smoke/world geometry, but the authoritative adapter remains unfinished. Native fire ticks, block spread, water extinguishing and nearby entities must never resolve PTU or Ouros incident state.

## Encounter readiness — Ridge Fireline Withdrawal

Full intended form wants multiple withdrawal routes, Intercept/forced movement, dynamic restricted sectors, optional verified fire/smoke/heat zones, battlefield-weather handoff, tactical AI and authoritative playback.

Current profile: REDUCED.

Safe reduced form:

- evacuate crew/civilians before combat;
- close the active incident sector in Ouros world state;
- use a reviewed static clearing or road approach;
- keep fire, smoke, embers, heat, collapse and changing weather mechanically outside the grid;
- select combatants explicitly in Ouros;
- let AutoPTU resolve combat only;
- let Fire Response/Crisis/Travel decide later operational state and reopening.

## Encounter readiness — Evacuation Junction Perimeter

Full intended form wants CLEAR_ROUTE/WITHDRAW/PROTECT-like objectives, competing reactions, route-control movement, possibly changing zones, tactical AI and playback.

Current profile: REDUCED.

Safe reduced form:

- complete evacuee movement before battle;
- stop ordinary traffic through world state;
- remove workers, vehicles and noncombatants from the grid;
- use a static legal arena;
- do not run moving fire fronts or live escort rules;
- battle outcome may secure the immediate junction only;
- route owner retains closure/reopening authority.

## Encounter readiness — Mop-Up Patrol Contact

Full intended form wants residual heat/smoke zones, withdrawal/territorial objectives, exact Move/Ability interactions with any validated environment, tactical AI and playback.

Current profile: REDUCED.

Safe reduced form:

- responders leave the residual-hotspot area before tactical contact;
- combat occurs on verified stable/cold perimeter ground;
- residual-fire state remains unchanged by victory;
- no visual smoke or Minecraft fire applies PTU effects;
- post-battle patrol/verification remains an operational action.

## PTU/Caelo boundary

PTU/AutoPTU evidence confirms named mechanics including Burn, Fire-type attacks, Weather and individual Move/Ability interactions. That evidence is insufficient to infer a universal environmental-fire subsystem.

Still unresolved or unsupported for these concepts:

- generic wildfire/fire-block damage;
- smoke-specific LoS/Accuracy effects;
- automatic Burn from environmental exposure;
- ember/ash statuses;
- heat/exhaustion or smoke inhalation;
- fire-spread timing/math;
- burning-object/structure HP;
- falling-tree/collapse rules;
- water-volume suppression math;
- Move-to-suppression conversion;
- Fire-type environmental immunity;
- Water-type firefighting competence;
- rescue/carry/extraction action rules;
- firefighting Skill checks;
- emergency equipment bonuses;
- wind-driven environmental forced movement.

Any exact Caelo location/environment effect can be used only when its governing source explicitly establishes it and the corresponding engine contract is verified.

## Minecraft/Cobblemon consequences

Safe reuse candidates:

- buildings, forests, roads and ordinary world geometry;
- controlled visual fire/smoke/particle states;
- barriers, signs, lights, camps and props;
- weather/day-night presentation;
- Pokémon models/forms/poses/animations/cries;
- maps/notices/UI;
- networking, entity tracking and persistence hooks;
- reversible block presentation after Ouros authorizes the world-state change.

Adapter work is required for:

- stable incident/sector/access-area to world-geometry bindings;
- projecting authoritative closures into visible barriers/signs;
- separating native fire visuals from incident truth;
- converting reviewed safe geometry to AutoPTU cells;
- stable actor identity across chunk unload/reload;
- authoritative battle event playback.

Minecraft/Cobblemon must never decide:

- who is a combatant from proximity;
- incident spread from native fire spread;
- suppression success from water/fire block interaction;
- HP/status/damage from native fire ticks;
- forced movement from particles/weather visuals;
- responder assignment from species/type;
- route reopening;
- ecological recovery;
- battle result.

Authority remains:

`Ouros fire/crisis state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## Pass 98 readiness conclusion

The new layer can ship operational continuity, report reconciliation, drills, response assignments, partial closures, residual-fire review, re-entry separation, post-fire handoffs and all reduced encounter forms without inventing PTU mechanics.

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

Pass 98 intentionally leaves open regional fire ecology/frequency, response institutions and authority, warning/re-entry terminology, technology, water/resource systems, Pokémon responder roles, suspicious-cause investigation, prescribed/managed burning practices and cultural memory. None are promoted to canon by this snapshot.