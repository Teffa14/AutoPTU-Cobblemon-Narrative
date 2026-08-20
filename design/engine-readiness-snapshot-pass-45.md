# Engine Readiness Snapshot — Pass 45

Status: implementation evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only from this repository.

Inspected AutoPTU-Java head: `2543881dd5863d7a4b01336dadc24a3be40fd6aa`

Inspected Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

## Permanent capability boundary

One implemented representative still does not prove an entire subsystem.

### VERIFIED

- targeting / footprints / range / line of sight
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING for concepts that require the whole family

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / broad reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## New Java evidence since Pass 44

Two commits landed after the previous snapshot.

### `0af71f13a3066c22fb03aee5d864d53ab01619e4`

This commit ports Plus/Minus spatial combat-stage reactions.

The visible commit summary adds:

- generic combat-stage hook suppression options;
- an authoritative spatial Ability radius query;
- recursive hook-suppression propagation;
- Plus/Minus spatial stage reactions;
- Python-oracle fixtures and parity tests.

Implications:

- Abilities gain more tested representatives.
- Spatial Ability queries now have stronger infrastructure evidence.
- Combat-stage reaction infrastructure covers another narrow family.

No broad family is complete.

### `2543881dd5863d7a4b01336dadc24a3be40fd6aa`

This commit adds a post-damage Ability hook family with Python parity.

The inspected diff adds:

- `PostDamageHook` contract;
- authoritative `PostDamageHookContext`;
- ordered `PostDamageHookRegistry`;
- additive `PostDamageHookResult`;
- semantic rule-effect events;
- parity-tested adjacent Aqua Boost, Ignition Boost and Thunder Boost behavior;
- a spatial query for allied Ability holders within radius;
- CI integration for Python-oracle fixture export.

Implications:

- full stateful damage pipeline gains another real post-damage slice;
- Abilities gain additional implemented representatives;
- some spatial aura behavior is now authoritative in Java;
- semantic effect-event coverage improves.

## No category promotion

Abilities remain PARTIAL.

The new Ability work does not prove:

- every Ability;
- entry/switch/exit effects;
- contact effects;
- all damage-triggered effects;
- weather or terrain creation;
- status interactions;
- item interactions;
- Trainer Feature interactions;
- every aura radius or stacking rule.

Full stateful damage remains PARTIAL.

A post-damage flat-bonus hook does not prove:

- every modifier ordering point;
- all shields/reductions;
- recoil;
- drain;
- substitute-like effects;
- delayed damage;
- status damage integration;
- item and Feature modifiers;
- every recursive or multi-target interaction.

Terrain/weather/hazards/zones/broad reactions remains BLOCKING.

The existence of spatial queries and stage/post-damage reactions does not prove:

- terrain creation or mutation;
- weather lifecycle;
- zone ownership/control;
- hazard placement/removal;
- attacks of opportunity;
- interception;
- forced-movement reactions;
- dynamic environmental triggers.

## Java README boundary

The current AutoPTU-Java README still states that the project is a Java core library rather than a Minecraft mod and that Python remains the source oracle while the port is incomplete.

Its high-level incomplete areas still include:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move/ability/item/perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The README boundary is intentionally broader than individual commits. The newer commits are real progress inside those larger unfinished families.

## Python evidence

The newest inspected Python AutoPTU head remains `e4bb0ca38b7018710af476ce365d515a387de4e7`.

Its newest visible commits are Career-layer roster recovery changes and do not justify any tactical category promotion.

Python remains the source oracle for slices being ported.

## Pass 45 relationship-mechanics check

A code search across the current AutoPTU-Java and AutoPTU repositories for terms around `loyalty`, `obedience`, `command` and Trainer/Pokémon relationship handling returned no direct implementation evidence during this pass.

Therefore these exact mechanics are unverified:

- PTU Loyalty rank storage;
- Loyalty-driven Command checks;
- obedience/disobedience resolution;
- battle command refusal;
- release procedure;
- transfer/rehoming procedure;
- temporary Trainer authority over another Pokémon;
- institutional Pokémon command authority.

This matters even though several permanent categories are VERIFIED or PARTIAL.

A category-level `core calculations: VERIFIED` does not imply that every possible PTU calculation, including Loyalty/Command checks, has been implemented.

## Pass 45 encounter dependencies

### Temporary Ally at the Floodgate

Reduced version:

- temporary assistance resolves through narrative/world state;
- helper Pokémon remains outside the tactical grid unless an existing legal battle representation is explicitly available;
- AutoPTU receives a standard static encounter.

Full version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING when protecting routes or displacing units
- core calculations: VERIFIED generally; temporary-partner and Command mechanics unverified
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/broad reactions: BLOCKING for flood dynamics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for autonomous allied objective behavior
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

### Former Partner at the Orchard

Reduced version:

- former partner remains a world-state/NPC Pokémon;
- historical association does not grant battle command authority;
- any combat uses a separate static legal encounter.

Full version concerns:

- ordinary targeting/base movement/core/action infrastructure can use VERIFIED slices;
- any Loyalty/Command/obedience behavior is unverified;
- autonomous ally/neutral behavior needs AI tactical policy: BLOCKING;
- habitat hazards need terrain/weather/hazards/zones/reactions: BLOCKING;
- Minecraft persistence and identity playback: BLOCKING.

### Transfer Station Breakdown

Reduced version:

- custody, handoff and paperwork remain outside the grid;
- players resolve a static legal encounter if combat occurs;
- transfer continues afterward through world state.

Full version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING for escort play
- core calculations: VERIFIED generally; transfer/Loyalty-specific mechanics unverified
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if infrastructure failure becomes tactical
- move behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

## Implementation priorities exposed by Pass 45

The new narrative layer does not require immediate battle-engine work for most world-state functionality.

The important future implementation questions are:

1. decide where PTU/Caelo Loyalty and obedience live architecturally;
2. add authoritative persistent Pokémon identity across party/world transitions;
3. define irreversible transfer/release authority in multiplayer;
4. implement objective-aware allied/neutral tactical AI before temporary partners fight autonomously;
5. preserve association/custody metadata through the Minecraft/Cobblemon adapter;
6. continue full damage/Ability/lifecycle parity without over-promoting those families.

## Permanent classification after Pass 45

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / broad reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback
