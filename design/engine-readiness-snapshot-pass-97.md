# Engine Readiness Snapshot — Pass 97

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`f3f9884b1142ff1a99dbf647bcf342ba6768bb39`

Latest relevant Java change:
`Expire temporary Trainer AP and reset actions at round start`

Observed behavior in this slice:
- `TrainerRuntimeState` now owns temporary AP grants with amount, expiry round and source metadata;
- spending AP consumes temporary grants first in deterministic order;
- expired temporary AP is removed during round progression;
- Trainer action budgets reset at `ROUND_START` through the lifecycle hook registry;
- representative behavior is frozen against the Python oracle with dedicated parity tests.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/f3f9884b1142ff1a99dbf647bcf342ba6768bb39

The parent Java head was Pass 96's `66d82a5beb767ec8dd32803b5d08afaad3d454aa`, which added selected round-scoped temporary-effect expiry.

Java README still states that the port is incomplete. It explicitly leaves full battle state, full damage, status controller, terrain/hazards/forced movement/reactions, complete Move/Ability/Item/perk/Trainer Feature registries, full transcript parity, tactical AI and Minecraft/Cobblemon adapter work unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its latest visible change remains Career-oriented and does not justify changing the tactical capability map.

The full primary Caelo corpus was not reliably retrievable for rail/vehicle rules in this run. No Caelo-specific train, vehicle, collision, boarding or rail Terrain rule is asserted.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Established static geometry, footprint, range and geometric LoS contracts remain verified at project level.

Pass 97 non-inference:
- a train carriage does not create moving geometry inside battle;
- a platform edge does not create falling mechanics;
- a rail signal does not change LoS;
- a moving train does not shift target anchors unless an explicit future battle contract supports that behavior.

A REDUCED onboard encounter may safely freeze one carriage/interior revision as static battle geometry.

#### base movement legality

Established Shift/Jump and Overland/Swim/Sky legality remain verified.

Pass 97 non-inference:
- walking beside rails does not create a rail movement mode;
- boarding a train is not a Shift;
- changing carriages on a moving train is not automatically ordinary Overland movement;
- stepping off a platform does not gain a special movement rule.

#### core calculations

Established calculation primitives remain verified.

Pass 97 adds no rail-specific damage, speed, braking or collision calculation.

#### action economy / initiative

Established action economy and initiative remain verified.

The newest Java slice strengthens round-level Trainer AP/action reset ownership.

Pass 97 non-inference:
- timetable priority is not initiative;
- dispatcher priority is not Speed;
- a train approaching does not create extra actions or an initiative deadline by itself.

#### AI legal-action infrastructure

Deterministic legal-choice generation remains verified.

This does not prove that AI can understand rail-specific goals such as leaving a crossing, protecting a passenger, escaping through carriages or keeping a corridor clear.

### PARTIAL

#### full turn / round lifecycle

Lifecycle has growing representative evidence for phase progression, initiative, field progression, delayed-hit maturity, temporary-effect expiry and now Trainer temporary-AP/action reset at round start.

Still PARTIAL because these slices do not prove every START/END trigger, duration, interrupt, delayed Move, Status, Ability, Feature or transcript interaction.

Pass 97 distinction:
Battle round lifecycle does not implement train timetables, route slots, station clocks or journey progression.

#### full stateful damage pipeline

Representative authoritative resolution paths exist, including delayed-hit re-entry work from earlier passes.

Still PARTIAL because the Java README explicitly leaves full damage unfinished.

No collision, crush, electrified-rail or moving-vehicle damage is introduced by Pass 97.

#### status lifecycle

Representative status application/phase/cleanup behavior exists.

Still PARTIAL because the complete status controller is unfinished.

A delayed train, crowded platform or moving carriage cannot create Flinch, Tripped, Stuck, Slowed or any other PTU status through narrative state alone.

#### move-specific behavior

Representative Move behavior and delayed-hit contracts exist.

Still PARTIAL because the full Move library is not ported.

No Move is assumed to manipulate railway switches, stop trains, destroy rails or gain special power inside a carriage unless exact PTU/Caelo text and implementation support it.

#### abilities

Representative Ability hooks exist with parity tests.

Still PARTIAL because the registry is incomplete.

Pass 97 does not infer:
- Electric-type/Ability = rail power source;
- Magnet Pull = control of trains or track hardware;
- Run Away = crossing-withdrawal AI;
- Soundproof = immunity to train alarms;
- Levitate = immunity to collision or platform risk.

#### items

Representative held-item behavior exists.

Still PARTIAL because broad coverage remains incomplete.

Ticket, key, pass, cargo manifest, signal token or rail tool are narrative/world objects unless an authoritative PTU item definition says otherwise.

#### Trainer Features / perks

Representative Feature infrastructure exists and the latest Java slice strengthens Trainer AP lifecycle state.

Still PARTIAL because full Feature/perk coverage, Orders and interrupts remain incomplete.

No railway staff role grants a Skill rank, Feature or AP benefit by itself.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still BLOCKING as a complete family.

Pass 97 implications:
- a train cannot force-move combatants along a track;
- a closing door cannot push an actor;
- an onboard pursuit cannot rely on complete interception/disengagement semantics;
- a crossing encounter cannot guarantee autonomous withdrawal through a protected lane;
- a platform-edge encounter cannot use knockback/falling safely.

#### terrain / weather / hazards / zones / reactions

Still BLOCKING as a complete family.

Canonical field-state primitives and representative round progression exist, but the Java README still leaves terrain/hazards/reactions unfinished.

Pass 97 does not infer:
- rail = Rough Terrain;
- moving train = forced-movement zone;
- third rail = electric hazard;
- platform edge = falling hazard;
- signal aspect = field effect;
- carriage = special room effect;
- freight cargo = cover;
- crossing gate = reaction trigger;
- bad weather = automatic track hazard.

#### AI tactical policy

Still BLOCKING.

No current evidence proves AI goals such as:
- CLEAR_CROSSING;
- WITHDRAW_FROM_TRACK;
- PROTECT_PASSENGER;
- PROTECT_CARGO;
- REACH_NEXT_CARRIAGE;
- AVOID_PLATFORM_EDGE;
- HOLD_SAFE_ZONE;
- ESCAPE_TRAIN;
- NONLETHAL_DISENGAGE.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still BLOCKING.

No verified adapter contract currently turns persistent rail-network state, moving trains, service slots, station platforms, crossings or timetable state into authoritative battle snapshots and semantic playback without duplicating rules.

## Pass 97 specific overworld blockers

`RAIL_NETWORK_STATE`
Persistent network/operator/corridor identity.

`TRACK_SEGMENT_TOPOLOGY_AND_REVISION`
Versioned physical track topology and current operating state.

`RAIL_ROUTE_SLOT_STATE`
Coarse dispatcher-owned movement reservations and conflicts.

`STATION_PLATFORM_STATE`
Usability, assignment, passenger access and information state.

`TIMETABLE_VERSIONING`
Planned service versions separated from actual movement history.

`TRAIN_INSTANCE_LOCATION`
Server-owned train position/milestone without requiring per-tick physical simulation.

`TRANSFER_CONNECTION_STATE`
Inter-service connection outcomes and accessibility requirements.

`RAIL_FREIGHT_LEG`
Transport leg referencing existing custody/provenance state.

`GRADE_CROSSING_STATE`
Rail/road/path interface and incident history.

`RAIL_INCIDENT_AND_RECOVERY`
Causal operational disruption and restoration.

`RAIL_TO_TRAVEL_HANDOFF`
Travel must consume validated service/path state rather than assuming rail fast travel.

`RAIL_TO_TECHNOLOGY_HANDOFF`
Signals, switches, power and failures must reference technical assets rather than being duplicated here.

`RAIL_TO_MINECRAFT_PROJECTION`
Visible tracks, trains, boards and barriers must be projections of server state.

`RAIL_TO_BATTLE_SNAPSHOT`
Only mechanically validated aspects may enter a BattleSpec.

## Encounter dependency summary

### Grade Crossing Obstruction — FULL

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version is viable earlier by holding the train outside the tactical scene and resolving only a static crossing encounter.

### Yard Transfer Interruption — FULL

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- lifecycle;
- stateful damage;
- statuses;
- move-specific behavior;
- abilities/items/Features only when exact mechanics are used.

BLOCKING:
- complete movement/interception;
- terrain/hazards/zones/reactions;
- AI tactical policy;
- adapter/playback.

Reduced version freezes rail and freight movement before combat and uses a safe static yard section.

### Onboard Investigation Escalation — FULL

VERIFIED in a frozen interior:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full lifecycle;
- full stateful damage;
- statuses;
- move-specific behavior;
- abilities/items/Features as required.

BLOCKING for the intended dynamic version:
- complete movement/interception;
- terrain/hazards/zones/reactions if carriage state changes tactically;
- AI tactical policy;
- adapter/playback.

Reduced version treats the train as an overworld moving location/clock and freezes one carriage graph if a battle starts.

## Why no capability promotion occurred

The new Java evidence is meaningful: Trainer temporary AP and action reset now participate in the authoritative `ROUND_START` lifecycle with Python parity.

That strengthens confidence in the existing PARTIAL lifecycle and Trainer Feature/perk infrastructure.

It does not prove:
- all Trainer Features;
- all AP grant/spend interactions;
- full lifecycle ordering;
- movement reactions;
- moving vehicles;
- objective AI;
- train physics;
- railway terrain/hazards;
- Minecraft playback.

Therefore no permanent category changes state in Pass 97.

## Unresolved mechanical and canon questions

- Does Ouros launch with rail at all, and in which regions?
- What propulsion/technology is canon?
- Are passenger and freight networks separate or shared?
- Do any Pokémon work with railway institutions, and what is the nature of that partnership?
- What exact PTU/Caelo rules, if any, govern vehicles, passengers, collisions, moving platforms or vehicle pursuits?
- Are tickets merely world access tokens or governed by a larger economic/legal system?
- How should a server represent train location without per-tick simulation across unloaded chunks?
- Can a moving train ever host a tactical battle, or should all rail battles use frozen interior snapshots?
- How are group travel, missed connections and offline passengers handled in multiplayer?
- Which rail incidents are public information and which remain operational/private?
- How should rail corridors interact with Cobblemon ecology without allowing train schedules to become rare-spawn farming tools?

No answer is promoted to canon by this snapshot.
