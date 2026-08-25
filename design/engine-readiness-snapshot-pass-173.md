# Engine Readiness Snapshot — Pass 173

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-25
Narrative focus: persistent puzzles, dungeons, challenge state, clue redundancy, fail-forward and safe battle handoffs.

## Read-only engine evidence inspected

AutoPTU-Java main head inspected: `fb93d3a4e6633d17a5a79f3095b141f887d4f258` — `Run generic secondary statuses in live move resolution (#209)`.

This slice derives effect-roll inputs from effective move metadata, carries effective metadata into secondary-status resolution, registers generic secondary-status Move Specials in live resolution and adds parity/integration tests against the Python oracle.

Its recent parents also:

- carry the authoritative accuracy roll into live Move Specials;
- compose runtime secondary-status requests;
- route those requests through canonical status-application prevention.

This is concrete evidence for a growing but narrow live Move-Special secondary-Status path.

It does not demonstrate:

- the full Status lifecycle;
- every secondary effect;
- full Move Special coverage;
- complete Ability/Item/Trainer Feature interaction coverage;
- generic dungeon mechanisms;
- arbitrary environmental triggers;
- puzzle state;
- moving walls/platforms;
- trap systems;
- objective-aware tactical AI;
- Minecraft puzzle authority or playback.

AutoPTU-Java README still explicitly leaves incomplete:

- core combatant/grid battle state;
- full damage-resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- remaining Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic-event/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python main head inspected: `df327530562ce4315f523316239d80a917111078` — `Test: eliminate trainer RNG fallback flake (#121)`.

That commit seeds a scripted test fallback deterministically and explicitly states that production mechanics remain unchanged. It provides no capability promotion.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No permanent category is promoted in Pass 173.

## PTU/Caelo evidence relevant to this pass

The accessible AutoPTU project corpus contains a Creative Action implementation whose internal rulebook basis points to PTU Core sections for creative use of abilities/capabilities/skill checks, capability action limits and complex stunts involving Focus with another Skill.

This supports the existence of adjudicated creative actions in PTU. It does not define a universal puzzle procedure, lockpicking subsystem, riddle check, trap framework, dungeon action economy or automatic Skill-based bypass.

The project corpus also exposes canonical Skills, Capabilities, Moves, Items, Abilities and Trainer Features. A challenge may reference an exact mechanic only after its real rule is validated.

No reliable primary Caelo rule was recovered in this run for universal puzzles, ancient mechanisms, traps, locks, Gym trials or dungeon interaction. No Caelo mechanic is invented.

Super PTU Online Helper was not available as an invocable runtime capability.

## Puzzle state is not battle state

The following challenge facts never write PTU battle state automatically:

- a lever position;
- a door being open;
- a clue being discovered;
- a riddle response;
- an institutional evaluator decision;
- a failed attempt;
- a solved mechanism;
- an alternate route;
- a reset;
- a bypass;
- a repaired mechanism.

Likewise, battle facts do not determine challenge truth unless the authored handoff contract explicitly consumes them.

`opponent defeated` does not imply `door opened`.

`battle won` does not imply `Gym challenge passed`.

`Move used` does not imply `mechanism activated`.

`high Skill rank` does not imply `puzzle solved`.

## Encounter dependency matrix

### Floodgate Logic Chamber — FULL

Targeting/footprints/range/LoS: VERIFIED for ordinary combat.

Base movement legality: VERIFIED for ordinary legal shifts.

Complete movement: BLOCKING. Required if gate state changes routes during combat, combatants/technicians must cross or withdraw, interception matters, or water produces forced movement.

Core calculations: VERIFIED for supported ordinary calculations.

Action economy/initiative: VERIFIED.

Full turn/round lifecycle: PARTIAL whenever complete lifecycle state matters.

Full stateful damage pipeline: PARTIAL whenever damage occurs.

Status lifecycle: PARTIAL for any exact Status. The floodgate puzzle itself applies none.

Terrain/weather/hazards/zones/reactions: BLOCKING if moving water, pressure zones, changing passability, environmental damage or reactions have tactical effects.

Move-specific behavior: PARTIAL when an exact Move is essential.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features/perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `REACH_CONTROL`, `WITHDRAW`, `PROTECT_TECHNICIAN`, `AVOID_GATE_PATH`, `CLEAR_ROUTE`.

Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: Challenge State resolves the gate configuration before battle. Freshwater/Infrastructure freezes a safe static chamber. Technicians leave. Any independent combat occurs on a fixed legal arena. Battle actions cannot change valve/puzzle state.

### Rotating Archive Hall — FULL

Targeting/footprints/range/LoS: VERIFIED for ordinary static geometry only.

Base movement legality: VERIFIED for ordinary static geometry.

Complete movement: BLOCKING if walls/paths change during combat or custodians move through contested space.

Core calculations: VERIFIED.

Action economy/initiative: VERIFIED.

Full lifecycle and full stateful damage: PARTIAL when invoked.

Status lifecycle: PARTIAL for exact Status only.

Terrain/weather/hazards/zones/reactions: BLOCKING if moving walls, protected cells or environmental interactions alter tactical legality.

Move-specific behavior / abilities / items / Trainer Features: PARTIAL when exact mechanics are invoked.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `PROTECT_CUSTODIAN`, `REACH_EXIT`, `CLEAR_ROUTE`, `AVOID_COLLECTION`.

Adapter/playback: BLOCKING.

REDUCED: Challenge State stops the mechanism at one validated configuration. Archives/Museums moves staff and fragile material out. AutoPTU receives a static room only.

### Partner Coordination Trial — FULL

Ordinary targeting, base movement legality, core calculations, action economy and AI legal-action infrastructure: VERIFIED where ordinary combat is actually used.

Complete movement: BLOCKING for synchronized station movement, crossing, withdrawal or interception.

AI tactical policy: BLOCKING for non-hostile objectives including `REACH_STATION`, `WAIT`, `COOPERATE`, `WITHDRAW`.

Adapter/playback: BLOCKING.

Terrain/weather/hazards/zones/reactions: BLOCKING only if station zones or environmental state have tactical mechanical effects.

Trainer Features/perks / abilities / items / move-specific behavior: PARTIAL if the trial permits an exact PTU mechanic.

No Loyalty, obedience or Command mechanic is invented by the challenge.

REDUCED: station choices resolve through world-state interactions. A final optional spar begins only after all puzzle state is frozen. Partner refusal opens an authored alternate route when the challenge definition provides one.

### The Three-Clue Ruin — NON-COMBAT / OPTIONAL STATIC COMBAT

The clue network itself requires no battle capability.

Languages, Archaeology, Archives/Oral History and Challenge State may expose independent clue paths and still leave historical interpretation unresolved.

If a separate confrontation occurs, it is handed to AutoPTU as an ordinary static battle. Winning does not determine archaeological truth.

## Hybrid puzzle-battle blocker rules

A concept depends on complete movement when it needs any of the following inside the battle itself:

- moving platforms;
- rotating rooms;
- push/pull into controls;
- knockback through doors;
- interception around an escort/objective;
- forced movement from water/conveyors/wind;
- dynamically changing traversable cells.

A concept depends on terrain/weather/hazards/zones/reactions when it needs:

- pressure plates as tactical zones;
- environmental damage;
- collapsing cells;
- persistent elemental zones;
- live water/current rules;
- reaction windows tied to mechanisms;
- trap triggers with battle consequences.

A concept depends on AI tactical policy when non-player actors must pursue semantic objectives rather than merely choose legal attacks/shifts.

The Minecraft/Cobblemon/Craftics adapter remains BLOCKING for all full versions requiring authoritative world interactions or playback.

## Recent Java evidence must not be over-generalized

`fb93d3a4...` proves live execution for a generic secondary-Status Move-Special path under tested conditions.

`412ec8f8...` carries authoritative accuracy into that path.

`d365642c...` composes runtime secondary-status handling.

They do not prove:

- every Status;
- every Move Special;
- environmental Status application;
- arbitrary mechanism hooks;
- generic pressure plates;
- dungeon traps;
- complete reaction handling;
- complete forced movement;
- puzzle interaction transactions;
- tactical objective AI;
- adapter playback.

## Pass 173 world-state blockers

Outside battle parity, the narrative/integration stack still needs implementations for:

- challenge-definition persistence;
- challenge revision history;
- challenge-instance persistence;
- immutable state revisions;
- mechanism-element identity;
- interaction contracts;
- clue/revelation graphs;
- source-dependency handling;
- accepted solution routes;
- emergent-solution adjudication;
- attempt history;
- reset policy;
- fail-forward outcomes;
- accessibility-equivalent routes;
- multiplayer concurrency/order;
- battle handoff contracts;
- dungeon node graphs;
- challenge-state rollback/recovery;
- Challenge State -> Minecraft presentation;
- Minecraft interaction request -> Challenge State validation.

## Mechanical guardrails

Do not create:

- universal puzzle DCs;
- universal lockpicking;
- automatic riddle solving from Focus;
- automatic machine bypass from Technology Education;
- automatic secret detection from Perception;
- automatic translation from Pokémon Education;
- automatic barrier bypass from Teleport/Groundshaper/Strength;
- redstone truth;
- block-break-as-solution authority;
- trap damage without validated mechanics;
- pressure-plate battle zones without environment support;
- arbitrary Status from puzzle failure;
- Battle victory -> challenge success by convention;
- challenge success -> Badge/credential/reward without institutional authority.

## Promotion decision

No permanent capability category changes state in Pass 173.