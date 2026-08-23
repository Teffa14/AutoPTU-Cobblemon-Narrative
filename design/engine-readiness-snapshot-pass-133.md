# Engine Readiness Snapshot — Pass 133

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live implementation evidence relevant to the Pass 133 cognition/problem-solving concepts. AutoPTU-Java and AutoPTU are read-only sources for this task.

A representative implemented mechanic never promotes an entire capability family by itself.

## Inspected engine heads

AutoPTU-Java:

`aefc058328a9217d634477835a4851d521aaeccb`

Latest inspected commit:

`Apply reaction movement authoritatively (#162)`

AutoPTU Python:

`8f003f5fa60b8d596c7f76daebb4c6a20235d53a`

Latest inspected Python commit:

`Career: normalize persisted battle recovery ids (#71)`

The Python change is Career recovery/resilience work. It does not alter the tactical classification below.

## Java evidence relevant to this pass

The latest Java slice remains the narrow authoritative reaction-movement application introduced in Pass 132 evidence.

Verified behavior for that slice includes:

- reachability derived from canonical battle grid/movement profile;
- selection of a safe destination under the frozen area-escape contract;
- canonical combatant position mutation;
- `ShiftResolvedEvent` emission;
- no spending of the actor's normal Shift budget for that specific reaction movement;
- displacement cap / fit checks for that contract;
- unchanged state if no safe destination exists.

This is meaningful movement/reaction progress.

It does not provide a generic system for autonomous environmental problem solving, interactable objects, tactical tool use, movable puzzle pieces, goal revision, or objective-aware AI.

## Java README boundary

The current README still explicitly lists as unfinished:

- full combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- full move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The architecture statement remains that Minecraft/Cobblemon/Craftics should consume the Java library rather than own PTU rules.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Geometry, anchors, footprints, range, affected areas, and line-of-sight have substantial parity-backed coverage.

This does not imply cognitive visibility, awareness, object understanding, or knowledge of a puzzle goal.

### base movement legality — VERIFIED

Shift legality and movement-profile primitives are verified for the ported scope.

This does not prove autonomous route planning around changing environmental objectives.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

The applied reaction-escape path is real but narrow.

Generic Push/Pull execution, knockback, interception, collision chains, falling, movement-triggered environmental interactions, and broad forced movement remain incomplete.

Movable puzzle objects therefore cannot be delegated to this category yet.

### core calculations — VERIFIED

Core calculation primitives remain verified for the ported scope.

No calculation primitive should be reinterpreted as cognition or problem-solving ability.

### action economy/initiative — VERIFIED

Action budgets and initiative infrastructure have substantial parity-backed coverage.

No extra action or initiative bonus is granted for intelligence, tool use, puzzle success, or familiarity.

### full turn/round lifecycle — PARTIAL

Round transitions, selected cleanup, delayed-hit maturity, phase ordering, and other slices exist.

The entire lifecycle remains incomplete.

### full stateful damage pipeline — PARTIAL

Significant stateful damage behavior exists, including delayed-hit and hook paths.

The README still marks full damage as incomplete.

### status lifecycle — PARTIAL

Status state and several prevention/application slices exist.

No problem-solving state is a Status.

### terrain/weather/hazards/zones/reactions — BLOCKING

Some semantic field state and one applied reaction movement path exist.

The combined family remains incomplete. A puzzle object, latch, debris pile, tool cache, water level, or workshop machine must not become a custom tactical zone or reaction merely because the narrative describes it.

### move-specific behavior — PARTIAL

Representative Move contracts exist. The Move catalog is incomplete.

Observed Pokémon tool use does not create a Move.

### abilities — PARTIAL

Many individual Ability hooks have parity evidence.

Species flavor about intelligence, command, manufacturing, or object use does not create an Ability implementation.

### items — PARTIAL

Item coverage remains incomplete.

A persistent world object only becomes a tactical PTU Item if the authoritative rules and implementation support that exact use.

### Trainer Features/perks — PARTIAL

Broad generic Feature infrastructure exists, but the concrete catalog remains incomplete.

Problem-solving observations do not grant Technology Education, Researcher, Mentor, Commander, or any other Feature/Class behavior.

### AI legal-action infrastructure — VERIFIED

The engine can construct/filter legal battle choices under the ported contracts.

This does not mean an AI can decide why to move an object, try an alternative solution, protect a research subject, or pursue a non-combat task goal.

### AI tactical policy — BLOCKING

There is no complete objective-aware policy for cognition-heavy goals such as:

- `SOLVE_OBJECTIVE`;
- `TRY_ALTERNATIVE`;
- `REACH_ACCESS_POINT`;
- `RETRIEVE_OBJECT`;
- `CARRY_OBJECT`;
- `WITHDRAW`;
- `PROTECT_RESEARCHER`;
- `REACH_REFUGE`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists yet.

Minecraft must not decide whether a Pokémon understood a latch, legally fabricated an item, has authority to move an object, or can perform an unsupported PTU action.

## Pass 133 encounter dependencies

### Workshop Latch Study — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if route-changing object manipulation/interception occurs in battle;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if used;
- terrain/weather/hazards/zones/reactions — BLOCKING if interactables create live tactical state;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if the manipulated object is mechanically active;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED:

Resolve attempts and latch outcome as world state before combat. Freeze geometry. If a confrontation remains, run a conventional static battle. The transcript does not decide what the Pokémon understood.

### Floodgate Debris Problem — FULL

Primary blockers:

- complete movement for live object displacement/route changes;
- terrain/weather/hazards/zones/reactions if water/debris becomes tactical;
- AI tactical policy for environmental objective solving;
- Minecraft/Cobblemon/Craftics playback.

REDUCED:

Hydrology and cognition resolve first in world state. AutoPTU receives the resulting static safe geometry.

### Tool Recovery at Scrap Yard — FULL

If the object remains narrative/world-state only, a conventional battle can occur independently.

If the tool is carried, used, modified, or contested mechanically inside battle, dependencies include:

- complete movement — BLOCKING for object-carry/displacement objectives;
- items — PARTIAL if the object has PTU item behavior;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- all normal PARTIAL combat families used by the confrontation.

REDUCED:

Material selection, tool revision, worker response, and Pokémon agency resolve outside battle. AutoPTU receives only the static confrontation.

### Multi-Access Study

Primary mode is non-combat.

No tactical dependency is required.

Research Ethics owns authorization/stop conditions. Science owns protocol/conclusions. Pass 133 owns task-specific behavior observations. Social Learning receives later evidence only if transmission becomes relevant.

## Cognition-specific non-inferences

Pass 133 must not infer:

- puzzle solved -> general Intelligence;
- puzzle failed -> low Intelligence;
- repeated success -> perfect memory;
- tool use -> Technology Education;
- object manufacture -> PTU crafting;
- tool -> valid Held Item or weapon;
- object carried -> ownership;
- gate opened -> universal lock bypass;
- rock launched -> generic ranged Move;
- apparent planning -> AI tactical policy exists;
- group coordination -> social learning;
- Oranguru command-like behavior -> Trainer Orders;
- Tinkatink hammer behavior -> weapon stats;
- Minecraft block interaction -> legal PTU action;
- reaction movement slice -> complete autonomous problem solving;
- legal-action generation -> objective reasoning.

## PTU rule boundary

The project copy of `PTU changelog 1.05.txt` explicitly states that the Intelligence Capability was removed.

Therefore Pass 133 intentionally does not create a replacement stat, rank, Skill, roll, or modifier.

The available project search did not expose a reliable Caelo-specific cognition/tool-use rule. Super PTU Online Helper was not available as an invocable capability.

Do not invent:

- Intelligence ranks;
- puzzle DCs;
- memory checks;
- cognition bonuses;
- arbitrary tool-use rolls;
- crafting recipes/yields;
- improvised weapon mechanics;
- lockpicking by species flavor;
- autonomous Orders;
- social-learning battle bonuses.

## World-state blockers introduced by Pass 133

Outside the battle core, implementation still needs:

- `COGNITIVE_TASK_CONTEXT_STATE`;
- `TASK_VERSION_HISTORY`;
- `PROBLEM_SOLVING_OBSERVATION_LEDGER`;
- `STRATEGY_ATTEMPT_HISTORY`;
- `OBJECT_MANIPULATION_EVENT_HISTORY`;
- `TOOL_USE_ASSESSMENT_STATE`;
- `STRATEGY_REVISION_HISTORY`;
- `INDIVIDUAL_BEHAVIOR_REPERTOIRE_INDEX`;
- `PRIOR_EXPOSURE_UNCERTAINTY`;
- `COGNITION_TO_MATERIAL_CULTURE_HANDOFF`;
- `COGNITION_TO_POKEMON_AGENCY_HANDOFF`;
- `COGNITION_TO_SOCIAL_LEARNING_HANDOFF`;
- `COGNITION_TO_RESEARCH_ETHICS_HANDOFF`;
- `COGNITION_TO_SCIENCE_HANDOFF`;
- `COGNITION_TO_MINECRAFT_PROJECTION`.

## Recommended implementation strategy

For narrative authors now:

1. keep problem-solving state in the overworld/Chronicle;
2. preserve task versions and actual attempts;
3. keep object identity/provenance in Material Culture;
4. use persistent `pokemon_entity_id` rather than replacing the individual with a behavior token;
5. hand transmission evidence to Social Learning only when it exists;
6. resolve environment/object manipulation before battle when possible;
7. freeze static geometry before AutoPTU;
8. do not encode cognition as custom damage, status, initiative, AI score, Item, Feature, or terrain;
9. use FULL encounter concepts as future contracts and REDUCED versions as current implementation targets.
