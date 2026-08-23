# Engine Readiness Snapshot — Pass 138

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to the lodging, hospitality and accommodation concepts added in Pass 138. Both engine repositories remain read-only for this task.

A representative mechanic never promotes an entire capability family by itself.

## Inspected heads

AutoPTU-Java:

`28f141be5471e23f660fb2cda09bab02244ee62e`

Latest inspected commit:

`Run pre-damage reactions in authoritative move pipeline (#167)`

This slice runs the currently supported pre-damage reaction composition inside the authoritative Move pipeline and tests ordering in the live runtime. It follows recent work that derives threatened-area geometry from authoritative state and ports a narrow Telepathy pre-damage reaction path.

AutoPTU Python:

`01a9b1c70af504b77f5b8441f7283d5957987190`

Latest inspected Python commit:

`Career: default compact touch battles to Light Mode (#75)`

This changes Career rendering defaults on compact touch devices while preserving authoritative battle mechanics. It does not alter the tactical classifications below.

## Java README boundary

The current AutoPTU-Java README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The recent reaction slices narrow specific paths. They do not override this repository-level boundary.

## Lodging mechanics boundary

Pass 138 introduces no new battle mechanic.

The following remain world-state concerns outside AutoPTU:

- reservations;
- room assignment;
- room readiness;
- occupancy;
- housekeeping;
- check-in/check-out;
- guest privacy;
- shared accommodation;
- event room blocks;
- emergency lodging allocation;
- Pokémon accommodation requests;
- room keys and property access policy.

Narrative sleeping/resting is not PTU Sleep status.

Lodging does not automatically restore HP, Injuries, Status, AP, temporary HP or any other battle state.

No project-local Caelo evidence recovered in this run established lodging/rest recovery rules.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Substantial parity-backed targeting geometry exists.

This geometry may support a static hotel courtyard, hallway or cleared room if mapped into a battle arena. It cannot determine room capacity, guest assignment or hotel access.

### base movement legality — VERIFIED

Ordinary Shift legality remains verified for the ported scope.

This supports movement by actual combatants in a frozen lodging-area battle map.

It does not support live guest evacuation as an objective by itself.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Narrow reaction movement exists and Push/Pull instructions have been exposed in recent slices, but complete forced movement/interception remains unfinished.

FULL lodging encounters with moving guests, escorts or blocked egress therefore remain dependent on this family.

### core calculations — VERIFIED

Core calculation primitives remain verified for the ported scope.

Room quality, bed type, lodging price, staff service or guest comfort do not modify core battle calculations.

### action economy/initiative — VERIFIED

Action budget and initiative infrastructure remain verified.

Check-in, room assignment, key handoff, packing luggage and ordinary evacuation logistics remain overworld actions unless a future exact combat rule says otherwise.

### full turn/round lifecycle — PARTIAL

Round/lifecycle slices, delayed effects, temporary effects and selected reaction paths exist.

The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

Supported pre-damage reactions now run inside the authoritative Move pipeline.

Full damage remains explicitly unfinished in the Java README.

A utility failure, broken window, damaged furniture or hotel fire cannot create custom damage rules by narrative declaration.

### status lifecycle — PARTIAL

Selected status application/prevention/suppression/timing paths exist.

Sleeping in a bed does not apply Sleep status.

Being tired after travel does not create a Status without an exact rules source.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction implementation is progressing, but this combined family remains incomplete.

A flooded lobby, dark hallway, broken glass, smoke, power outage, balcony edge or crowded corridor does not create tactical effects unless exact supported mechanics exist.

### move-specific behavior — PARTIAL

Representative Move paths exist, but catalog coverage remains incomplete.

Any lodging scenario that invokes a specific Move depends on exact parity for that Move.

### abilities — PARTIAL

Individual Ability families have concrete parity-backed slices.

Species flavor does not grant a Pokémon special hotel access, room suitability, guest-service ability or emergency role.

### items — PARTIAL

Item coverage remains incomplete.

Room keys, luggage, towels, furniture and ordinary guest items are narrative objects unless explicitly mapped to validated PTU items.

### Trainer Features/perks — PARTIAL

Generic Feature infrastructure and selected concrete effects exist, but catalog coverage remains incomplete.

A concierge, innkeeper, porter, hotel manager or housekeeper receives no Trainer Feature by profession alone.

### AI legal-action infrastructure — VERIFIED

Legal battle-choice construction/filtering exists for the ported scope.

It does not understand lodging goals such as guest evacuation, securing exits or escorting staff.

### AI tactical policy — BLOCKING

No complete objective-aware policy exists for Pass 138 goals such as:

- `EVACUATE`;
- `CLEAR_ROUTE`;
- `PROTECT_GUEST`;
- `WITHDRAW`;
- `REACH_EXIT`;
- `PROTECT_STAFF`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer from beds, doors, signs, keys, NPC placement or room decoration:

- authoritative room capacity;
- reservation state;
- occupancy;
- payment completion;
- guest identity;
- private relationships;
- PTU recovery;
- Pokémon accommodation consent;
- hotel authority.

## Pass 138 encounter dependencies

### Hotel Evacuation During a Utility Failure — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live guest/staff movement and interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if exact mechanics invoke it;
- terrain/weather/hazards/zones/reactions — BLOCKING if the utility failure creates a validated tactical hazard;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if exact mechanical items are used;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Resolve guest evacuation, utility shutdown and room reassignment in world state. Remove guests/staff from the grid. Freeze a safe static arena and resolve only actual combatants. Resume lodging operations afterward. Battle victory does not repair the utility.

### Lodge Courtyard Wildlife Disturbance — FULL

Requires live wild withdrawal and potentially guest movement.

Primary blockers:

- complete movement — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Environmental capability family enters only if an exact validated effect exists.

REDUCED:

Move guests inside using world state. Preserve attractant/wildlife observations outside battle. If conflict remains, resolve a conventional static courtyard encounter. Capture or KO does not resolve the underlying cause automatically.

### Lost Room Key / Reservation Dispute

Primarily non-combat.

Identity, reservation state, room assignment and access policy decide the issue. A separate battle can use the verified static subset if needed, but battle outcome cannot establish entitlement to accommodation.

## Pass 138 world-system blockers

The narrative layer identifies these non-battle implementation contracts as needed before full Minecraft realization:

- `LODGING_PROPERTY_STATE`;
- `ACCOMMODATION_UNIT_IDENTITY`;
- `ROOM_CAPACITY_PROFILE`;
- `RESERVATION_LIFECYCLE`;
- `WAITLIST_STATE`;
- `ROOM_ASSIGNMENT_HISTORY`;
- `ROOM_READINESS_STATE`;
- `GUEST_STAY_HISTORY`;
- `SHARED_ACCOMMODATION_STATE`;
- `POKEMON_ACCOMMODATION_HANDOFF`;
- `HOUSE_RULE_REVISION_HISTORY`;
- `ROOM_TURNAROUND_STATE`;
- `EVENT_LODGING_BLOCK`;
- `EMERGENCY_LODGING_CONVERSION`;
- `LODGING_ACCESSIBILITY_MATCH`;
- `LODGING_PRIVACY_BOUNDARY`;
- `LODGING_TO_TRAVEL_HANDOFF`;
- `LODGING_TO_PAYMENTS_HANDOFF`;
- `LODGING_TO_MINECRAFT_PROJECTION`.

These belong outside the battle core.

## Explicit non-inferences for Pass 138

Do not infer:

- bed -> healing;
- bed -> PTU Sleep;
- better room -> combat bonus;
- Pokémon Center room -> automatic HP/Injury/Status recovery;
- house rule -> criminal law;
- room key -> ownership;
- shared room -> friendship/romance/family;
- no vacancy -> narrative obstruction unless capacity state supports it;
- empty Minecraft room -> available room;
- occupied Minecraft room -> authoritative stay;
- large Pokémon -> automatically prohibited;
- flying Pokémon -> automatically needs outdoor accommodation;
- Water-type -> automatically needs a pool;
- staff title -> Trainer Feature;
- guest complaint -> proven misconduct;
- room damage -> identified responsible actor.

## Unresolved mechanics/canon questions

- Which lodging properties exist in Ouros at campaign start?
- Do Pokémon Centers provide overnight lodging in final project canon?
- Which settlements use hotels, inns, hostels, lodges, dormitories, campsites or institutional quarters?
- How detailed should room inventory be for small versus large properties?
- Are lodging prices simulated, qualitative or normally compressed?
- What privacy rules apply to guest histories?
- Which properties have authored Pokémon accommodation facilities?
- How does emergency lodging allocation work institutionally?
- Can player clubs/businesses operate lodging?
- Which PTU/Caelo rules, if any, govern rest, sleep, fatigue or recovery from lodging?
- Which exact mechanics have Java parity if such rules are later adopted?

Super PTU Online Helper was not available as an invocable capability in this run. No output is attributed to it.