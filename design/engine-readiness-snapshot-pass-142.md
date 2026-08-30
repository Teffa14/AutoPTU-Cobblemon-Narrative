# Engine Readiness Snapshot — Pass 142

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-30

This snapshot records repository inspection, live engine evidence and permanent capability dependencies checked while adding road-vehicle, fleet-assignment, inspection and serviceability continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 142:

`faedfc5b9d3e49e8707e2c2df7904bcf4c9b9fbb`

The complete recursive narrative tree was inspected before topic selection and returned `truncated: false`.

The selected gap was checked against:

- Travel, Transport & Expedition;
- Road Passenger Transport Services Continuity;
- Roads, Bridges & Detours Operational Continuity;
- Shared Equipment, Lending & Issued Assets;
- Facility Maintenance, Repair & Inspection;
- Fuel Supply, Storage & Distribution;
- Request, Dispatch, Response & Resource Continuity;
- Material Culture;
- Finance / Sponsorship / Risk;
- Human Identity / Credentials / Workplaces;
- Pokémon Agency / Work Role;
- PTU/Caelo source scan;
- Pass 141 engine-readiness snapshot.

Road Passenger Transport already references vehicle assets and owns run/service truth, but repository inspection found no dedicated owner for persistent road-vehicle identity, fleet-number history, owner/operator/custody separation, vehicle-specific defect and inspection chronology, serviceability restriction/release, substitution lineage or retirement/repurposing.

The new extension is deliberately narrow. It does not own roads, passenger-service schedules, generic equipment checkout, workshop facilities, fuel logistics, personnel qualification, finance or Pokémon agency.

## Research relevance

Public Pokémon material supplied high-level continuity patterns rather than mechanics:

- Rotom Bike shows one travel asset whose configuration/capability presentation changes over time without requiring a new identity every time.
- Flying Taxi shows that one transport-service concept can use different Pokémon assets in different regions and can adapt to local ecological constraints.
- broader bicycle/Ride systems reinforce that access to a mobility mode, physical ownership and operating assignment are separate concepts.

A public PTU community discussion around mount movement, attacks of opportunity and shared spaces was treated only as evidence that mounted movement semantics are ambiguous enough to require exact governing contracts rather than narrative invention.

Operational public sources supplied provenance architecture:

- stable physical-vehicle identity separated from local plate/fleet labels;
- owner/control/operator separated from driver;
- defect report separated from diagnosis;
- inspection separated from later condition;
- repair separated from return-to-service release;
- out-of-service separated from retirement;
- fleet lifecycle and spare/substitute management separated from passenger-service identity.

No external law, VIN system, inspection period, license, recall process or vehicle technology becomes Ouros canon.

## AutoPTU-Java live evidence

Current head inspected:

`5f8c23950e5689a771b9c9d0772e7cc60e9a8197`

Commit:

`Add server-owned terrain skill-check resolver (#282)`

No newer AutoPTU-Java commit was present during Pass 142.

The live commit remains meaningful localized evidence for the reusable terrain-context skill-check bonus associated with the covered Intercept path. `TerrainSkillCheckBonusResolver` handles the exact covered Survivalist/Naturewalk gate and eligible skill labels represented by current parity tests.

This evidence does not establish any road-vehicle mechanic.

It also does not verify:

- generalized terrain objects;
- dynamic traffic lanes;
- moving platforms;
- vehicle footprints as mobile combat entities;
- vehicle speed/acceleration/braking;
- collision damage;
- boarding/disembarking during initiative;
- passenger/rider shared-space semantics;
- vehicle cover;
- generalized reactions;
- broad Push/Pull/Knockback;
- every forced-movement source;
- escort semantics;
- objective-aware tactical AI;
- semantic vehicle/fleet playback.

No permanent capability category is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 142.

The commit remains presentation-only: cached Pixi dimensions are synchronized after viewport resize so tactical sprite destinations use live renderer geometry. It explicitly does not change battle rules or outcomes.

It does not establish semantic adapter/playback for vehicle identity, fleet membership, inspection, serviceability, substitution, road-service assignment, boarding or departure.

## Permanent capability map — Pass 142

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Static reviewed BattleSpecs can rely on current targeting/spatial-legality evidence. This does not verify mobile road-vehicle footprints.

`base movement legality`

Baseline conventional movement remains verified on static tactical spaces. It does not establish movement inside/on moving vehicles or road-traffic simulation.

`core calculations`

Previously established parity-backed baseline remains verified. It does not provide vehicle collision/durability calculations.

`action economy/initiative`

Baseline action economy and initiative remain verified for conventional combatants. They do not define driver turns, vehicle actions, boarding windows or service-departure timing.

`AI legal-action infrastructure`

Legal action enumeration/validation remains verified. It does not provide policy for escorting staff, clearing a depot exit, protecting a loading bay or avoiding a moving vehicle.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

Specific Intercept paths have strong evidence, including server-owned terrain-context inputs. The combined family remains partial. Broad Push, Pull, Knockback, all forced-movement sources, generalized escort movement, edge/collision semantics and vehicle displacement remain unverified.

`full turn/round lifecycle`

Ordinary tactical progression exists. Staged withdrawal, timed boarding, vehicle movement phases and synchronized traffic/work-zone objectives are not established as a complete family.

`full stateful damage pipeline`

Substantial implementation exists, but family completeness has not been established. It must not be repurposed into vehicle HP or collision damage without explicit contracts.

`status lifecycle`

Use only exact implemented combat statuses. Pass 142 creates no generic `OUT_OF_SERVICE`, `DEFECT_REPORTED`, `VEHICLE_RESTRICTED` or `UNDER_REPAIR` tactical status.

`move-specific behavior`

Representative Move coverage does not establish interactions with road vehicles, moving platforms, collisions or technical equipment.

`abilities`

Representative Ability coverage remains partial. No Ability grants generic driving, vehicle repair, towing, propulsion or inspection authority.

`items`

Items remain partial. A vehicle, inspection record, route card, workshop tag or fleet identifier is not automatically a PTU combat Item.

`Trainer Features/perks`

The Survivalist/Naturewalk terrain-context resolver remains localized evidence. The full family is partial. No Feature creates generic driver qualification, roadworthiness authority or vehicle-maintenance certification.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The permanent family remains blocking. Rich road-vehicle scenes may need protected depot lanes, passing-traffic zones, moving hazards, collision boundaries, loading zones or generalized reactions. The narrow terrain skill-check helper does not verify any of those semantics.

`AI tactical policy`

Rich variants may require `PROTECT`, `WITHDRAW`, `CLEAR_ROUTE`, `HOLD_POSITION`, `AVOID_VEHICLE` or escort-aware decisions. Legal-action infrastructure does not supply those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

No live evidence establishes semantic projection of vehicle identity, fleet number, owner/operator relation, current assignment, defect state, inspection result, maintenance/release, substitution, boarding state or departure.

## PTU/Caelo mechanical guardrails

The project source scan supports travel, Jobs, persistent locations and exact authored environmental mechanics where governing sources define them. It does not establish a universal road-vehicle tactical subsystem.

Remain UNKNOWN until exact source/tests/contracts establish them:

- generic vehicle HP, Armor or DR;
- road-vehicle movement per round;
- acceleration/braking/turning;
- collision/ramming damage;
- moving-platform coordinates;
- passengers sharing vehicle spaces;
- boarding/disembarking during initiative;
- vehicle cover;
- pushing/pulling/knockback of vehicles;
- crash/ejection/fall transitions;
- road chases;
- generic vehicle repair/inspection checks;
- Technology Education as universal vehicle authority;
- Trainer Classes/Features as driver/inspector licenses;
- species/Type/Move/Ability as automatic driving, towing, propulsion or maintenance competence.

No narrative encounter may invent these semantics.

## Encounter review — Depot Exit Perimeter

Narrative premise:

A road-service or work vehicle is otherwise cleared for assignment but an unrelated tactical threat occupies the immediate depot exit.

Full intended dependencies:

- targeting/footprints/range/LoS — VERIFIED for static reviewed geometry;
- base movement legality — VERIFIED for conventional static movement;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic lanes/zones/generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Vehicle remains parked and noninteractive.
2. Driver, mechanics and passengers leave the tactical space before BattleSpec creation.
3. Fleet assignment, inspection and serviceability state freeze.
4. Ouros selects explicit legitimate combatants.
5. AutoPTU receives reviewed static yard geometry.
6. Tactical victory may create only `IMMEDIATE_DEPOT_EXIT_CLEAR`.
7. The owning transport/dispatch system separately decides whether the vehicle departs.

`TACTICAL_VICTORY != VEHICLE_RELEASED`.

`TACTICAL_VICTORY != RUN_STARTED`.

`DEPOT_EXIT_CLEAR != VEHICLE_SERVICEABLE`.

## Encounter review — Roadside Inspection Withdrawal

Narrative premise:

A condition check/inspection is already underway when an independent tactical threat makes the roadside work area unsafe.

Full intended dependencies follow the same permanent map. Escort/Intercept/forced movement are PARTIAL. Dynamic roadside hazards/zones/reactions, objective-aware tactical policy and semantic playback remain BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Road traffic/service is stopped or separated before battle under the relevant world owner.
2. Inspector, driver, private records and tools withdraw.
3. Vehicle remains static background geometry or outside the tactical footprint.
4. No vehicle HP, cover, collision or destructible-object rule is invented.
5. AutoPTU resolves a conventional static encounter.
6. Victory creates `IMMEDIATE_ROADSIDE_WORK_AREA_CLEAR` only.
7. Inspection resumes afterward from preserved evidence and chronology.

`TACTICAL_VICTORY != INSPECTION_PASSED`.

`TACTICAL_VICTORY != DEFECT_CONFIRMED`.

`WORK_AREA_CLEAR != RETURN_TO_SERVICE_APPROVED`.

## Encounter review — Substitute Vehicle Loading Bay Chokepoint

Narrative premise:

A replacement vehicle has been selected because the original asset is unavailable, but an independent threat blocks the loading bay or safe approach.

Full intended dependencies:

Rich boarding-zone movement, escort, vehicle motion and objective policy require the PARTIAL/BLOCKING families above.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Passengers remain outside BattleSpec.
2. Original and substitute vehicle states freeze.
3. No boarding occurs during battle.
4. Ouros selects explicit combatants.
5. AutoPTU resolves a conventional encounter on static geometry.
6. Victory creates `IMMEDIATE_LOADING_BAY_CLEAR` only.
7. Road Passenger Transport separately resumes boarding, revises the run or cancels it according to current world state.

`LOADING_BAY_CLEAR != BOARDING_AUTHORIZED`.

`SUBSTITUTE_PRESENT != SUBSTITUTE_ASSIGNED`.

`SUBSTITUTE_ASSIGNED != SERVICE_DEPARTED`.

## Reduced-version implementation rule

The vehicle-continuity layer may advance now because reduced encounters do not require AutoPTU to simulate vehicles.

World-state owners resolve before battle:

- vehicle identity;
- owner/operator/custody;
- fleet membership;
- service assignment;
- inspection/defect evidence;
- serviceability restriction/release;
- passengers and crew;
- road/service state;
- vehicle location.

Battle receives explicit combatants and static reviewed geometry.

Battle outputs only narrow physical access/perimeter facts.

World-state owners resume afterward.

This keeps Minecraft/Cobblemon/Craftics from duplicating missing PTU rules and prevents battle presentation from becoming world authority.

## Minecraft/Cobblemon/Craftics boundary

Presentation may display authored facts such as parked vehicles, depot bays, livery changes, workshop overlays, route cards, barriers, old fleet numbers and retired/repurposed vehicles.

It may not infer:

- vehicle identity from entity UUID alone;
- roadworthiness from visible model state;
- operator from livery alone;
- assignment from physical location;
- repair completion from animation;
- service departure from despawn;
- inspection result from a sign/item;
- combatant status from proximity;
- collision or vehicle damage from Minecraft physics.

Cobblemon BattleState remains non-authoritative for combatants, legality, HP/status, tactical position and world consequences.

## Canon questions left open

Pass 142 deliberately does not decide:

- which Ouros regions use road vehicles;
- prevalence of private versus public vehicles;
- road-vehicle technologies and energy sources;
- registration/identifier systems;
- fleet-number conventions;
- inspection regimes;
- roadworthiness standards;
- driver qualifications;
- maintenance institutions;
- rental/lease systems;
- accessibility requirements;
- recall/safety-notice structures;
- retirement/disposal practices;
- named recurring vehicles, fleets, depots or operators;
- individual Pokémon work roles involving vehicles.

Those remain canon-authoring decisions.

## Pass 142 conclusion

The narrative repository can safely add vehicle/fleet continuity now as PROPOSED world-state architecture.

Rich tactical vehicle scenes remain blocked by exact missing families. Reduced static variants are READY and preserve the narrative premise without making AutoPTU, Minecraft or Cobblemon responsible for unsupported vehicle rules.

Permanent capability status remains unchanged from Pass 141.