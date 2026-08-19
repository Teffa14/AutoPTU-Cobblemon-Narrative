# Engine Readiness Snapshot — Pass 30

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination

## Live Java head inspected

AutoPTU-Java head during this pass:

`957e7eaa0ce056b8fc6f2f66aba7f24440c2c2be`

Commit: `Consume pending status skips after phase hooks (#55)`

The latest bounded evidence still strengthens lifecycle/status integration:

- lifecycle hooks can emit pending status-skip requests;
- ordered hook resolution aggregates them;
- the authoritative current actor consumes them;
- parity tests compare ordering against Python.

No newer Java commit was present during this pass.

This does not establish:

- the complete status controller;
- every phase-triggered status;
- reactions;
- Trainer Features;
- full move/ability/item registries;
- objective-aware AI;
- Minecraft playback.

## Java README evidence

The current README continues to state that Python AutoPTU is authoritative while the port is incomplete.

Major unfinished families explicitly include:

- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Live Python head inspected

AutoPTU head observed during this pass:

`afa7c993b624a6dd612f259a720b1a74bc03720b`

Latest commit observed:
`Career: club continuity, automatic training and Pokémon longevity`

This is Career/API gameplay work. It does not provide evidence that the tactical Java categories below have advanced.

Python remains the source oracle, but Python behavior cannot be treated as already available in Java or Minecraft.

## Permanent capability classification

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

### BLOCKING for mechanically rich encounter design

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Pass-30 relevance

The workplace/staffing layer is mostly world-state work and can progress without tactical engine expansion.

Safe narrative/world-state work now:

- workplaces;
- occupational roles;
- staffing rosters;
- coarse schedules;
- shift commitments;
- temporary assignments;
- training records;
- qualification claims;
- backlogs;
- handoffs;
- career history;
- NPC availability;
- institutional knowledge;
- service-capacity state.

None of those require the battle engine to fabricate PTU mechanics.

## Encounter dependency table

### Line Crew Access

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if tactical protection/interception is used
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if worksite effects alter the grid
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: workers remain outside the tactical grid. Players clear a static legal encounter, then world state advances the crew's access/repair assignment.

### Warehouse Evacuation

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- stateful damage/status/move/ability/item families: PARTIAL when relied upon
- terrain/weather/hazards/zones/reactions: BLOCKING
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version: evacuation resolves as overworld/world state before combat. AutoPTU only handles the static encounter blocking the final route.

### Loading Bay Disruption

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING if equipment or combatants displace units
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL for timed windows
- stateful damage/status/move/ability/item families: PARTIAL when used
- terrain/weather/hazards/zones/reactions: BLOCKING if machinery or cargo creates tactical objects/zones
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- explicit HOLD_ZONE/CLEAR_ZONE objective semantics: not yet verified

Reduced version: cargo stays outside battle state. A conventional static battle clears the loading area, and shipment state advances only after staffing, route and service dependencies pass.

## Occupational-role boundary

Narrative occupational roles are not PTU Trainer Classes.

Safe claims:

- an NPC works as a mechanic;
- an NPC is scheduled at a ferry terminal;
- an institution considers someone qualified for a local responsibility;
- a trainee is supervised;
- a worker has years of documented service;
- a role is vacant;
- a workplace has a backlog.

Unsafe without PTU/Caelo validation:

- assigning a Skill Rank from the job title;
- granting Edges or Features through employment;
- deciding a repair check DC;
- inventing Command/Technology/Medicine bonuses;
- treating institutional certification as a mechanical class;
- giving a Pokémon extra capabilities because it works in a certain industry.

## Pokémon-work boundary

Official Pokémon sources establish narrative precedent for Pokémon participating in jobs.

That does not establish any Ouros mechanic for:

- work stamina;
- labor duration;
- production yield;
- carrying capacity;
- salary/reward;
- type-based job suitability;
- EXP for working;
- automatic move learning;
- workplace injury;
- institutional ownership.

Those remain canon/mechanics decisions.

## Schedule boundary

Coarse NPC schedules do not require battle lifecycle support.

However, battle turn phases must never be reused as overworld work clocks.

The two timing systems have different semantics.

## Minecraft boundary

Verified tactical movement does not prove:

- persistent NPC work schedules;
- cross-chunk worker movement;
- workplace staffing UI;
- shift handoffs;
- dynamic shop/clinic/transport opening logic;
- queues;
- job boards;
- worker-Pokémon animation routines;
- offline assignment completion;
- persistent workplace inventories;
- player employment UI.

Those remain world/adapter implementation tasks.

## No-inference rules for Pass 30

- A mechanic title does not grant Technology Education.
- A nurse title does not grant Medicine Education.
- A courier title does not grant movement bonuses.
- A supervisor title does not grant Command bonuses.
- A worker absence does not imply kidnapping or sabotage.
- A staffing shortage does not create a Skill penalty by itself.
- Training does not grant PTU progression unless an authoritative rule says it does.
- A Pokémon assigned to work does not gain EXP or EVs from the Galar Poké Job system.
- Type alone does not prove job suitability.
- A workplace backlog does not create random combat.
- A shift schedule is not a battle lifecycle mechanic.
- One implemented Java lifecycle/status contract does not upgrade the full lifecycle or status categories.