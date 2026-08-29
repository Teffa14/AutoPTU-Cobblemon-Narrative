# Engine Readiness Snapshot — Pass 118

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.
Date: 2026-08-29

## Read-only repositories inspected

AutoPTU-Java head inspected:

`87fbcb2ab75b4642c762017a037a6c0dccb9d8ad`

Latest commit/PR #268: `Bridge real interception sequence into PRE-target registry`.

AutoPTU head inspected:

`b0a5769b79f2e7b7bd18fb1e0c87ee42a145d4c6`

Latest merge/PR #227: `Career: lazy-load the preseason market gate`.

Neither read-only repository was modified by Pass 118.

## Change since Pass 117

AutoPTU-Java has no newer head than Pass 117. Its latest evidence remains the concrete core-only Intercept path integrated through the PRE-target registry and authoritative Move pipeline.

AutoPTU advanced from `7b4c3d603bd8c2ddd0b47faf7b8691c307e259f9` to `b0a5769b79f2e7b7bd18fb1e0c87ee42a145d4c6`. The new work lazy-loads the Career preseason market gate and adjacent optional Career UI/economy code. It is performance/loading work and provides no new tactical capability evidence.

Pass 118 therefore makes no capability promotion or demotion.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Why medical transport does not change the map

Most medical-transport continuity is world-state orchestration:

- request chronology;
- assignment;
- unit state;
- route linkage;
- scene contact;
- destination acceptance;
- diversion;
- handoff;
- turnaround;
- historical records.

These can progress without introducing a new battle mechanic.

Rich tactical versions become demanding only when patients, staff, stretchers, vehicles, loading operations or evacuation routes remain active inside BattleSpec.

## Complete movement remains PARTIAL

The Java runtime currently proves a specific Intercept sequence that can:

- enter PRE-target processing;
- use the existing interception spatial/RNG/resource sequence;
- move a successful interceptor to its resolved interception position;
- preserve original target context;
- replace the effective defender;
- emit semantic target-replacement evidence;
- proceed through target-bound Move preparation and the authoritative Move pipeline;
- leave target/position unchanged on a failed attempt.

This remains narrower than the movement required by a generic medical escort scenario.

Still unverified as complete families:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- carrying another actor;
- stretcher movement;
- movement of multi-actor protected objects;
- collision/landing behavior across all sources;
- environmental displacement;
- all Intercept triggers/windows/candidate sources;
- vehicle movement integrated with tactical legality;
- generalized competing reactions.

Therefore medical escort/withdrawal cannot treat complete movement as VERIFIED.

## Terrain/weather/hazards/zones/reactions remains BLOCKING

A transport scene might eventually include:

- protected loading corridor;
- active road hazard;
- unstable terrain;
- weather-exposed transfer point;
- changing exclusion cells;
- reaction protection around a withdrawing subject;
- moving vehicle boundary;
- technical hazard around rescue equipment.

Current evidence does not establish a generalized authoritative family covering those concepts.

A static road/lobby/bay can be represented as ordinary geometry only when no unverified environmental effect is attached to it.

## Full turn/round lifecycle remains PARTIAL

A rich medical-withdrawal battle might depend on:

- boarding completes after N lifecycle events;
- a route opens/closes at a phase boundary;
- a transport departs after a protected sequence;
- a timed diversion window expires;
- a delayed hazard changes the safe path.

No current evidence proves every lifecycle seam and ordering interaction needed for those scenarios. Reduced versions therefore complete the medical movement in world state before BattleSpec.

## Damage/status remain PARTIAL

Medical narrative context cannot manufacture tactical health rules.

Pass 118 does not infer:

- transported patient receives healing;
- stabilization is a status;
- loading/unloading applies damage;
- movement of an injured actor changes Injury state;
- vehicle collision uses Minecraft damage;
- sirens or stress apply a status;
- a medical Pokémon's presence removes status;
- a healing Move may be applied outside its exact governing rule.

Ordinary combat continues using the existing partial damage/status coverage. Any medical or environmental effect requires exact PTU/Caelo evidence plus current runtime tests.

## AI legal actions versus tactical policy

AI legal-action infrastructure remains VERIFIED as the infrastructure that can expose legal actions.

Medical transport encounters commonly need policy goals such as:

- PROTECT_SUBJECT;
- WITHDRAW;
- CLEAR_ROUTE;
- HOLD_CORRIDOR;
- ESCAPE;
- INTERPOSE;
- preserve access while another actor leaves.

There is no live evidence that the tactical policy understands these objectives, values a protected noncombatant, coordinates withdrawal or chooses positions around a departing unit.

AI tactical policy therefore remains BLOCKING.

## Adapter/playback remains BLOCKING

The current Java semantic event work does not prove a Minecraft/Cobblemon/Craftics adapter that can reliably:

- reconstruct authoritative BattleSpec state;
- animate Intercept without applying mechanics twice;
- animate protected withdrawal;
- move/animate a transport vehicle as playback only;
- represent a handoff boundary without deciding its world-state completion;
- synchronize reconnect/reload during a staged encounter;
- preserve exact combatant identity and positions;
- write the final authoritative result back into Ouros world state.

Cobblemon BattleState remains forbidden as combat authority.

## Pass 118 authoring boundary

Currently authorable without missing tactical families:

- medical transport services as world institutions;
- transport requests and dispatch chronology;
- unit availability and assignment history;
- scene-arrival versus subject-contact state;
- transport decision records supplied by Care authority;
- destination requests and acceptance;
- planned and urgent transport missions;
- diversion history;
- arrival versus handoff distinction;
- inter-facility referral/retrieval coordination;
- unit turnaround state;
- temporary pickup/transfer points;
- public service notices;
- service-history mysteries;
- static exploration of current/former stations;
- long-term route and institution memory.

Not currently justified from live battle evidence:

- generic stretcher/carry mechanics;
- patient escort inside combat as a generalized system;
- moving medical vehicle as a tactical object;
- vehicle collision rules;
- emergency right-of-way mechanics;
- protected-corridor reaction systems;
- dynamic road closure cells inside rounds;
- generic transport stabilization/healing;
- objective-aware AI evacuation/protection;
- semantic Minecraft vehicle/escort playback.

## Encounter 1 — Roadside Pickup Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL if exact validated status behavior is used
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized protection/reaction zones or active roadside hazards
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Current profile: REDUCED.

Reduced version:

Complete subject boarding and medical-unit departure before BattleSpec. Keep subject, crew and vehicle out of the grid. Resolve a static conventional encounter with explicit combatants on the cleared roadside area. Battle victory may secure the immediate pickup area after departure; it cannot heal, change destination acceptance, complete receiving handoff or reset unit readiness.

## Encounter 2 — Transfer Bay Perimeter

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: PARTIAL for Intercept/forced movement around a protected route
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if transfer windows change during rounds
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL for exact existing statuses only
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized protected/restricted zones and reaction ordering
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protected-corridor behavior
- adapter/playback: BLOCKING

Current profile: REDUCED.

Reduced version:

Complete the care handoff behind a secure authored boundary before combat. Remove patient, staff and transport unit from BattleSpec. Use a static exterior approach. The battle can establish `IMMEDIATE_TRANSFER_BAY_PERIMETER_SECURED`; it cannot perform or reverse the already recorded handoff.

## Encounter 3 — Diversion Junction

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: PARTIAL for escort/interception/forced movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed departure/route windows
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL where exact status rules apply
- terrain/weather/hazards/zones/reactions: BLOCKING for changing route cells or generalized reactions
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for ESCAPE/PROTECT/CLEAR_ROUTE
- adapter/playback: BLOCKING for moving vehicle/route semantics

Current profile: REDUCED.

Reduced version:

The medical unit has already completed its diversion in world state and is absent from BattleSpec. Players face only an explicit hostile subgroup at a static junction. Victory may improve later route state only through the route owner's normal handoff process. It does not rewrite the transport mission's previous chronology.

## Exploration — The Station That Moved Twice

Current profile: EXECUTABLE AS WORLD EXPLORATION.

Required state:

- persistent service/institution identity;
- dated addresses and location aliases;
- map editions;
- archived notices;
- photographs or equivalent records;
- route history;
- testimony provenance.

No tactical family is required unless a separate battle is authored.

## PTU/Caelo mechanical unknowns for Pass 118

Current project evidence does not establish universal rules for:

- ambulance or emergency-vehicle operation;
- emergency right-of-way;
- dispatch priority mechanics;
- clinical triage mechanics;
- transport stabilization;
- patient deterioration during travel;
- stretcher movement;
- generic carrying of an incapacitated actor;
- boarding/unboarding another actor;
- multi-actor movement formations;
- vehicle acceleration/speed/collision;
- moving-vehicle battle maps;
- air/water medical transport;
- Pokémon-powered patient transport;
- species-derived medical qualifications;
- generic use of healing Moves during transport;
- generic Medicine Education checks for dispatch/referral;
- Trainer Feature interrupts protecting a patient unless exact rules exist;
- tactical handoff actions;
- transport completion triggered by defeating enemies.

These remain UNKNOWN rather than being fabricated in the narrative layer or adapter.

## Minecraft/Cobblemon/Craftics authority boundary

Allowed presentation:

- medical bases and loading bays;
- parked or authoritatively animated vehicles;
- field tents and pickup markers;
- staff/NPCs and individually authored Pokémon;
- static stretchers/equipment props;
- route signage and service notices;
- lights, sounds, particles and UI;
- departure/arrival cinematics driven by Ouros state.

Forbidden authority:

- entity entering vehicle completes patient custody;
- Minecraft pathfinding completes dispatch or arrival;
- vehicle movement decides route legality;
- collision deals authoritative PTU damage;
- potion/Cobblemon healing performs transport stabilization;
- redstone proves a unit is operational;
- vehicle proximity establishes care handoff;
- Cobblemon BattleState selects combatants or medical subjects;
- Minecraft death/faint state decides transport requirement.

Governing direction remains:

Ouros world facts -> AutoPTU battle specification/resolution where battle exists -> adapter -> Minecraft/Cobblemon presentation.

## Promotion gates

Roadside Pickup Withdrawal can move beyond reduced form only when the exact required slices are verified, including protected withdrawal/escort semantics, any necessary forced movement or Intercept behavior, objective-aware tactical policy, generalized reaction ordering if used and semantic playback for the resulting state.

Transfer Bay Perimeter requires comparable protection/reaction and adapter support if handoff actors remain on-grid.

Diversion Junction additionally requires verified moving-route/escort semantics if the medical unit itself remains tactical.

None of these missing mechanics is necessary to preserve the narrative premise. The reduced versions therefore remain the preferred current implementation profile.

## Readiness conclusion

Pass 118 adds a substantial world-state capability without overstating battle readiness. Medical transport and referral continuity are primarily chronology, route linkage, institutional handoff and service-state problems. Rich escort or moving-vehicle battles remain gated by the exact permanent capability families they would consume.

The permanent capability map is unchanged from Pass 117.
