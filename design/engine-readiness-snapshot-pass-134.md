# Engine Readiness Snapshot — Pass 134

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to aging, competitive longevity, retirement and the Pass 134 encounter concepts. Both engine repositories are read-only for this task.

A representative mechanic never promotes an entire capability family by itself.

## Inspected heads

AutoPTU-Java:

`ebfdf7b29da5cdde9b7df7bd6d193ae03f5203f7`

Latest inspected commit:

`Port Telepathy pre-damage reaction (#164)`

Immediately preceding slice:

`8c4dd7f2b3816eed8b4a777b95920369aed85b57` — `Freeze generic pre-damage reaction contract (#163)`

AutoPTU Python:

`8f003f5fa60b8d596c7f76daebb4c6a20235d53a`

Latest inspected Python commit:

`Career: normalize persisted battle recovery ids (#71)`

The latest Python commit is Career recovery/resilience work and does not change the tactical classification below.

## AutoPTU Career longevity evidence

Current read-only Python Career contains a concrete Pokémon competitive-longevity model.

Evidence:

- `CareerPokemon.career_health` is persisted;
- normal stat training does not consume career health;
- intensive Training Kit use consumes `TRAINING_KIT_WEAR`;
- completed seasons can reduce career health according to active workload and tenure;
- long-tenured active Pokémon accrue additional veteran wear under the Career policy;
- inactive PC Pokémon age competitively much more slowly under that policy;
- reaching zero retires the Pokémon from competitive play;
- retirement stores season/reason and removes the Pokémon from the active roster;
- the same Pokémon ID persists after retirement;
- tests explicitly label the outcome competitive retirement rather than death.

Relevant source files:

- `auto_ptu/career/roster.py`
- `tests/test_career_pokemon_longevity.py`

Important boundary:

This evidence is Career-specific. It does not establish PTU biological health, natural lifespan, senescence, age-based stat loss, death, or universal retirement rules. Pass 134 therefore treats `career_health` as one source-system integration state and never as Ouros biological truth.

## Latest Java evidence

The latest Java slice adds a built-in Telepathy pre-damage reaction on top of the generic pre-damage reaction contract.

For the parity-backed Telepathy slice, Java can:

- inspect canonical attacker/defender team state;
- respect Ability suppression;
- respect Mold Breaker registration semantics for this hook;
- request an optional out-of-turn decision;
- require the defender to be inside the threatened area;
- use canonical reaction movement to choose/apply a safe Shift destination;
- preserve the normal Shift action budget for that reaction path;
- emit an Ability event;
- cancel the incoming area hit/damage/type-effectiveness outcome when the reaction succeeds.

This is substantial progress on one pre-damage reaction and one Ability.

It does not prove generic reaction coverage, interception, all forced movement, broad out-of-turn decision policy, arbitrary protect/escort objectives, or complete Ability registries.

## Java README boundary

The current README still explicitly lists as unfinished:

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

Minecraft/Cobblemon/Craftics remains a consumer of Java rules, not a second PTU authority.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Substantial parity-backed geometry coverage exists.

Age, experience and retirement do not change LoS or range without an exact mechanical rule.

### base movement legality — VERIFIED

Shift legality and movement-profile primitives are verified for the ported scope.

No age-based movement modifier is added by Pass 134.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Reaction escape movement exists for a narrow parity-backed path, and forced-movement instruction parsing exists for Push/Pull metadata.

Generic Push/Pull execution, knockback, interception, collision chains, falling, movement-triggered interactions and the complete family remain unfinished.

### core calculations — VERIFIED

Core calculation primitives remain verified for their ported scope.

No calculation primitive should be reinterpreted as age, frailty, veteran experience or retirement.

### action economy/initiative — VERIFIED

Action budgets and initiative infrastructure have substantial parity-backed coverage.

Age and retirement do not grant or remove actions/initiative without a source rule.

### full turn/round lifecycle — PARTIAL

Round transitions, selected cleanup, delayed effects, Trainer Feature phases and other slices exist. The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

Significant damage behavior is ported, including delayed-hit and hook paths. The README still marks full damage incomplete.

Competitive Career wear is not battle damage.

### status lifecycle — PARTIAL

Status state, application/removal and selected prevention paths exist.

Old age, retirement and competitive wear are not Status conditions.

### terrain/weather/hazards/zones/reactions — BLOCKING

Field-state and reaction slices exist, including the Telepathy pre-damage movement reaction.

The combined family remains incomplete. Do not create an `elder zone`, fatigue hazard, age reaction, retirement field effect or route penalty from narrative metadata.

### move-specific behavior — PARTIAL

Representative Move contracts exist; the catalog remains incomplete.

Age does not remove or alter Moves unless an authoritative rules system explicitly says so.

### abilities — PARTIAL

Many individual Ability hooks now have parity evidence, including the latest Telepathy reaction.

Old age does not suppress Abilities. Retirement does not remove them.

### items — PARTIAL

Item coverage remains incomplete.

A cane, brace, old uniform, trophy or retirement gift is not a tactical Item unless the rules support that exact use.

### Trainer Features/perks — PARTIAL

Broad generic Feature infrastructure and selected concrete effects exist. The complete catalog remains incomplete.

Years of service do not grant Mentor, Commander, Athlete, Researcher or other Features.

### AI legal-action infrastructure — VERIFIED

Legal battle-choice construction/filtering is substantially implemented for the ported scope.

It does not decide whether an actor should retire, reduce workload, protect a successor, return for an exhibition or choose a non-combat role.

### AI tactical policy — BLOCKING

No complete objective-aware policy exists for goals relevant to Pass 134 such as:

- `WITHDRAW`;
- `PROTECT_VETERAN`;
- `PROTECT_SUCCESSOR`;
- `REACH_ROUTE_END`;
- `CLEAR_ROUTE`;
- `HOLD_POSITION`;
- `ESCORT`;
- `RETURN_TO_GROUP`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer age, retirement, reduced capability, veteran bonuses, succession, death or care needs from visuals or entity state.

## Pass 134 encounter dependencies

### Veteran Route Survey — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING for live escort/withdrawal/crossing objectives;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if route/weather state becomes tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED:

Resolve the veteran's route choice, functional observations, weather/access and any accommodation in world state. Freeze geometry. If confrontation remains, run a static conventional battle. The transcript never diagnoses age-related decline.

### Exhibition Return — FULL

The narrative premise does not require an age mechanic.

If a retired participant is mechanically eligible for this one event, the combat engine consumes ordinary authoritative combatant state.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING as a full family but avoidable unless invoked by Moves;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if invoked;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for complete autobattler behavior;
- adapter/playback — BLOCKING.

REDUCED:

Keep registration, role scope, consent, audience and post-match retirement state outside battle. Run only a supported conventional battle. A win or loss does not change retirement status automatically.

### Handoff at North Watch — FULL

Primary blockers:

- complete movement — BLOCKING for live protect/withdraw/escort objectives;
- terrain/weather/hazards/zones/reactions — BLOCKING if the route disturbance has tactical effects;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

All ordinary combat families retain their permanent VERIFIED/PARTIAL states.

REDUCED:

Resolve route positions, evacuation, handoff and succession schedule as world state. Freeze a legal arena if a confrontation remains. Battle outcome cannot appoint a successor or cancel retirement.

## Pass 134 non-inferences

Do not infer:

- `career_health` -> biological HP;
- `career_health == 0` -> death;
- retired -> old;
- old -> retired;
- old -> slower movement;
- old -> lower stats;
- old -> lower initiative;
- old -> increased Status susceptibility;
- old -> wise or correct;
- old -> leader;
- old -> mentor;
- old -> socially withdrawn;
- reduced route range -> senescence;
- retirement -> loss of Pokémon partnership;
- retirement -> transfer of custody/ownership;
- retirement -> Ability/Move loss;
- PC storage -> biological rest/recovery;
- Telepathy reaction movement -> generic escort/withdrawal AI;
- one reaction path -> reactions category complete;
- one Career longevity model -> PTU lifespan rules;
- Minecraft age-looking model -> mechanic.

## PTU/Caelo boundary

No reliable project-accessible Caelo rule text defining biological aging, lifespan, retirement or natural death was recovered in this run. No installed GitHub repository matching Caelo was available. Super PTU Online Helper was not exposed as a callable capability.

AutoPTU Career is the only concrete project implementation evidence found for competitive retirement, and its semantics remain explicitly scoped to that Career system.

Until authoritative rules/canon are recovered, Pass 134 must not create:

- lifespan tables;
- age modifiers;
- natural-death rolls;
- recovery penalties;
- veteran bonuses;
- mandatory retirement ages;
- mechanical re-entry rules;
- fertility rules;
- cognitive-decline rules.

## Open implementation questions

- Will Ouros use AutoPTU Career's longevity model directly, map it into a broader career system, or keep it mode-specific?
- Can a Career-retired Pokémon ever become battle-eligible again?
- Does the world need exact ages or only age bands for most actors?
- How are older persistent wild Pokémon identified reliably across despawn/reload?
- Which role transitions advance offline?
- What event authority confirms natural death if the campaign allows it?
- Can multiplayer PCs privately author their own retirement plans without exposing age/health data?
- How will Minecraft present reduced workload or changed routine without turning visuals into mechanical truth?