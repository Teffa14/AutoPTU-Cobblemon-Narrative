# Engine Readiness Snapshot — Pass 32

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination

## Live Java head inspected

AutoPTU-Java head during this pass:

`5576e433b7b2f9e87fad7c669bd008b992b9bb62`

Commit:
`Add reusable status phase effect registry (#57)`

Relevant evidence:

- reusable phase-scoped status-effect contract;
- ordered canonical status-phase registry;
- lifecycle hook integration;
- ordered alias/registration behavior;
- pending status-skip propagation;
- parity tests for this bounded contract.

This strengthens lifecycle/status infrastructure.

It does not establish complete status coverage or promote the status family to VERIFIED.

## Current Java README evidence

The AutoPTU-Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

The README still lists unfinished work for:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The repository is still intentionally a Java battle-core library rather than a Minecraft mod.

## Live Python head inspected

Latest observed AutoPTU head during this pass:

`2e824854851df766e77fd65dbfc1d713bdf268e5`

Commit:
`Career: make preseason gating fail-safe and capture optional`

Recent Python changes observed around this head concern the Career/preseason/automatic-training/capture-outing product flow.

They do not establish new Java tactical capability.

Python remains the rules oracle where the migration contract uses it, but Python behavior is not equivalent to Java or Minecraft implementation readiness.

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

## Delta from Pass 31

Java head is unchanged from Pass 31.

Therefore no permanent capability category is promoted or demoted.

Python advanced through Career-focused commits, but none of those commits is evidence for Java battle capability.

No inference is permitted from the Career UI/gameplay work into Ouros regional-travel or recognition mechanics.

## Pass-32 relevance

The interregional mobility/recognition layer is primarily persistent overworld and institutional state.

Safe implementation-independent work includes:

- region profiles;
- visit records;
- arrival/departure state;
- visitor purpose;
- host contacts;
- orientation records;
- institutional invitations;
- recognition claims;
- reciprocal-access agreements;
- cross-region referrals;
- return-visit callbacks;
- visitor influx state;
- public/private record portability metadata.

None of those systems requires battle-turn lifecycle.

## Regional state versus battle state

Do not use:

- battle rounds as travel time;
- turn phases as arrival workflow;
- status hooks as regional access checks;
- battle initiative as transport scheduling;
- AI legal-action generation as NPC travel planning.

Those concepts belong to different runtime layers.

## Encounter dependency table

### Port Arrival Disturbance

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if crowd lanes/interception are tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if terminal hazards/dynamic zones matter
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- CLEAR_ROUTE/PROTECT objective semantics: not verified

REDUCED version:

Evacuate visitors in overworld state before battle creation. AutoPTU receives a static legal arena with normal combatants. Reopening the terminal is a world-state writeback after authoritative resolution.

### Joint Boundary Survey

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING only when tactical rescue/interception is required
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL when damage matters
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if transition-zone conditions modify combat
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

REDUCED version:

The survey and inter-institution comparison remain overworld/research state. Any battle uses a fixed arena and supported mechanics only.

### Tournament Transfer Chokepoint

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if route hazards enter battle state
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- ESCORT/BREAK_THROUGH objective semantics: not verified

REDUCED version:

Transport and competitor movement stay outside battle state. A static battle may block one route. Travel resumes or reroutes after the authoritative encounter result.

## Recognition boundary

Battle transcripts can eventually provide portable factual evidence such as:

- who participated;
- legal actions emitted;
- authoritative outcome;
- public match record when the battle institution publishes it.

A transcript does not establish:

- cross-region Badge equivalency;
- local qualification;
- visitor permission;
- tournament seeding;
- employment authority;
- conservation access;
- academic equivalency;
- residence;
- legal status.

Those remain institutional/world-state decisions.

## Travel capability boundary

Java verifies substantial base movement legality for tactical grids.

That does not prove:

- overworld mount eligibility;
- interregional Fly/Surf travel;
- ferry capacity;
- carrying passengers;
- long-distance endurance;
- regional travel permissions;
- Minecraft traversal playback.

Any Pokémon-assisted regional travel must still validate authoritative PTU/Caelo capability state plus the future overworld adapter.

## Crowd/event boundary

A high-volume visitor event is an aggregated world-state load.

Current verified battle capabilities do not prove:

- crowd simulation;
- civilian pathfinding;
- tactical evacuation;
- escort objectives;
- protected-unit AI;
- moving chokepoints;
- event attendance playback in Minecraft.

Reduced encounters should remove noncombatant visitors from the grid before battle.

## Access-control boundary

Minecraft adapter/playback remains BLOCKING.

Therefore current Java evidence does not establish:

- terminal gates;
- access-control UI;
- visitor registration;
- private records synchronization;
- institution invitation checks;
- regional arrival events;
- transport hub state;
- mixed-permission multiplayer handling.

These belong to the future world adapter/application layer.

## No-inference rules for Pass 32

- Region does not mean sovereign state.
- Crossing a regional boundary does not imply a border checkpoint.
- A Badge does not grant travel permission unless canon says so.
- A public battle result does not grant local qualification.
- A visitor is not a resident.
- A long stay is not automatically permanent residence.
- A host contact is not a legal sponsor unless such a system exists.
- A research invitation does not grant unrestricted site access.
- A medical referral does not reveal private records globally.
- Cross-region fame does not create universal NPC recognition.
- Foreign Pokémon are not automatically restricted, invasive or illegal.
- Java base movement does not prove overworld long-distance travel.
- The status-phase registry does not make status lifecycle VERIFIED.
- Python Career progression does not prove interregional progression rules.
