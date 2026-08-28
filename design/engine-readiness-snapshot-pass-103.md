# Engine Readiness Snapshot — Pass 103

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 103 adds proposed continuity for organized manufacturing: facilities, production lines/cells, orders, production runs, work-in-process, interruptions, quality holds/releases, rework, staged restart and industrial-site history.

Narrative baseline before Pass 103 writes: `2726706fae57fe89637bfe70ac73a0547d98b76a`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. The inventory confirmed prior coverage for Material Culture/Crafting, Procurement, Batch Traceability, Workplaces, Maintenance, Infrastructure Outages, Worksite Safety, Waste/Sanitation, Commercial Services and transport/logistics. This pass therefore adds production continuity rather than duplicating existing crafting or supply-chain authority.

## Live engine evidence

AutoPTU-Java head inspected: `e202a4fae092cd2732642b07f1f73813e75a0326`.

New Java evidence since Pass 102:
- #258 “Compose intercept candidate sequence authoritatively”.
- The change adds authoritative composition/parity coverage for the sequence of Intercept candidate attempts and gates it against the Python oracle.

This strengthens the specific Intercept orchestration path beyond #256/#257, which already covered authoritative battle RNG and mutation ordering for attempts.

It still does not verify the full permanent category `complete movement including push/pull/knockback/interception/forced movement`.

Still outside family-wide verified coverage:
- broad Push/Pull behavior across all sources;
- broad Knockback behavior across all sources;
- competing/generalized reactions;
- reaction ordering outside the frozen Intercept path;
- every forced-movement source;
- environmental displacement;
- complete Move/Ability/Item/Trainer Feature integration;
- tactical objective policy;
- semantic Minecraft/Cobblemon playback.

AutoPTU Python head inspected: `a348c24e189dd3aba5d36a2013f61b7b60067e7a`.

Its latest merged work guards Career season-training browser-storage access. This is client/Career stability work and adds no tactical battle-family evidence.

No permanent capability category is promoted in Pass 103.

## PTU/Caelo production boundary

The existing Narrative Material Culture layer correctly treats executable production/crafting as mechanically validated against recipe/rule references, actor prerequisites, tools/facilities, inputs, timing/frequency and implementation support.

No inspected governing evidence establishes a universal PTU/Caelo industrial subsystem for assembly-line throughput, conveyor mechanics, generic machine HP, factory-capacity arithmetic, defect rates, jams, overheating, worker productivity, automated redstone crafting or industrial accident damage.

Production continuity therefore remains world state. If a concrete production step creates a PTU item or uses a PTU Move/Ability/Item/Trainer Feature, that exact mechanic must already exist or remain explicitly unresolved.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`
Verified for reviewed static arenas. Factory walls, aisles and machinery only enter tactical geometry after explicit arena review.

`base movement legality`
Verified for ordinary static movement. This does not create conveyor transport, evacuation semantics, vehicle motion or machine interactions.

`core calculations`
Verified calculation primitives remain available. No industrial heat, pressure, machine-force or accident arithmetic is implied.

`action economy/initiative`
Verified typed action budget/order remains available.

`AI legal-action infrastructure`
Verified legal-action enumeration remains available. It does not choose evacuation, production-protection or civilian-safety objectives.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`
PARTIAL. Java #258 strengthens authoritative Intercept candidate sequencing on top of #256/#257. It does not verify the family broadly enough for moving machinery, industrial knockback, competing reactions or environmental displacement.

`full turn/round lifecycle`
PARTIAL.

`full stateful damage pipeline`
PARTIAL. No machine collision, industrial heat, crushing, electrical or chemical damage is introduced by Pass 103.

`status lifecycle`
PARTIAL. Alarm, panic, fatigue, contamination, heat stress or similar industrial concepts are not PTU statuses unless governing rules explicitly establish them.

`move-specific behavior`
PARTIAL. A Move cannot be generalized into welding, lifting, machining, cooling, powering, cutting, assembly or quality testing.

`abilities`
PARTIAL. An Ability does not automatically qualify a Pokémon for production work or industrial hazards.

`items`
PARTIAL. Machinery, tools, components, status boards and work-in-process are world objects unless authoritative item rules apply.

`Trainer Features/perks`
PARTIAL. No broad manufacturing/engineering/industrial Feature family has been established by this pass.

### BLOCKING

`terrain/weather/hazards/zones/reactions`
BLOCKING for live conveyors, hot zones, energized equipment, moving machinery, environmental process hazards, generalized protective reactions or dynamically changing industrial terrain.

`AI tactical policy`
BLOCKING for withdrawal, corridor protection, perimeter defense, civilian avoidance and objective-aware factory encounters.

`Minecraft/Cobblemon/Craftics adapter/playback support`
BLOCKING for authoritative facility/line/run/WIP bindings, world-to-arena conversion and semantic playback.

## Encounter readiness

### Line Shutdown Withdrawal

Full intended form requires protective withdrawal, multiple routes, Intercept/forced movement, generalized reactions, objective-aware AI and playback. Any active machinery/process hazard additionally requires the environmental family.

Current profile: REDUCED.

Safe form:
Ouros stops the production line before encounter creation. Workers, WIP, machinery and nonparticipant Pokémon are removed from tactical participation. AutoPTU receives explicit combatants in a reviewed static aisle or exterior yard. Victory secures only the immediate route. Restart remains world state owned by Manufacturing/Maintenance/Safety.

### Loading Bay Production Hold

Full intended form may require protected routes, generalized reactions, forced movement, live vehicle/equipment hazards, objective-aware AI and playback.

Current profile: REDUCED.

Safe form:
Manufacturing/Logistics freeze custody at the last verified handoff. Cargo, vehicles, forklifts and workers remain outside the grid. AutoPTU receives explicit participants in a static perimeter. Victory does not transfer custody, dispatch goods or complete delivery.

### Reconfiguration Cell Perimeter

Full intended form may require reviewed terrain, route control, reactions, forced movement, energized-equipment zones/hazards, tactical AI and playback.

Current profile: REDUCED.

Safe form:
The cell is de-energized before battle. Staff and test equipment remain outside the BattleSpec. The tactical result secures access only. Testing, verification and line readiness occur afterward in world state.

## Immediate noncombat readiness

Usable immediately as proposed narrative state:
- persistent production-facility identity;
- line/cell configuration history;
- production orders and run lifecycle;
- work-in-process persistence;
- dependency-driven interruption;
- quality review/release provenance;
- rework/disposition history;
- staged restart after maintenance or outages;
- narrative capacity bands without invented throughput math;
- public tours versus restricted production;
- downstream scarcity pressure without automatic economic formulas;
- facility closure, mothballing and repurposing;
- individual Pokémon work assignments without species-level inference.

## Minecraft/Cobblemon consequence

Binding architecture remains:

`Ouros world/production state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe presentation reuse includes factory/workshop geometry, conveyors, decorative machinery, doors, lights, sounds, particles, storage props, Pokémon models/forms/poses/animations/cries, NPCs, UI, networking, tracking and persistence hooks.

Adapter work is required for stable facility/line/run/WIP identity, authoritative state projection, entity/world-record binding, reviewed arena conversion and semantic battle playback.

Minecraft/Cobblemon must never decide that:
- production completed because redstone activated;
- an item entity became manufactured because it crossed a conveyor;
- output passed quality because it entered a chest;
- repair completed because a block changed;
- a Pokémon is a worker because it stands beside machinery;
- native fire/lava/electric/collision behavior applies PTU damage or status;
- everyone inside the factory is a combatant;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or battle result.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which regions have organized factories, refineries, fabrication sites or workshop networks?
- Which products are local, imported or regionally concentrated?
- What industrial technologies exist?
- Which institutions operate major production facilities?
- What labor, safety, environmental and public-access norms exist?
- Which old industrial sites have been closed, preserved or repurposed?
- Which individual Pokémon have production roles and what explicit evidence authorizes each role?

## Unresolved mechanical questions

- exact PTU/Caelo rules for any proposed industrial crafting action;
- whether any governing source establishes machinery, engineering or production-capacity mechanics;
- whether any Move/Ability/Item/Trainer Feature can explicitly perform a specific production task;
- handling of industrial hazards if a future encounter needs them;
- whether machines are ever tactical objects with HP/state, and under which rules;
- objective-aware withdrawal/protection policy;
- adapter handling for animated machinery without giving Minecraft battle authority.

No answer is invented by this snapshot.
