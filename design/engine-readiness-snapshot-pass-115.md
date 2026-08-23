# Engine Readiness Snapshot — Pass 115

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `cdb229db787ac93f28745f796c1d9944546676cc`

Newest relevant Java evidence:

- the generic Trainer Feature effect registry now includes parity-backed `apply_status` and `remove_status` handlers;
- tested status-effect cases include creating a status entry, refreshing a shorter duration, preserving a longer existing duration, appending stacked duplicate entries, removing named duplicate entries and removing all statuses;
- those handlers operate on canonical `BattleRuntimeState` status entries;
- prior slices already established ordered stacked status storage plus generic Trainer Feature prerequisites, context gates, frequency/cooldown, resources, usage bookkeeping, target scopes, trainer-target scopes, heal, Combat Stage, temporary HP and AP effect primitives.

This is meaningful evidence for Trainer Feature infrastructure and status-state mutation. It does not demonstrate the complete Trainer Feature catalog, complete status lifecycle, all status immunities/durations, social mechanics or workplace mechanics.

AutoPTU `main`: `0d1cc8f3bd791485ed52f7b5e9cd63c0965ad944`

The newest Python commit inspected adds Generation 9 PBS files to the Career/Vercel runtime. Recent Python changes remain Career/persistence/UI oriented and do not justify a tactical capability promotion.

## Java README evidence

The live Java README still lists as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative mechanics remain representative only.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
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

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 115.

## Trainer Feature status-effect evidence boundary

The latest Java slice proves a narrow generic payload contract for applying and removing status entries from canonical runtime state, including tested stacked-entry behavior.

It does not prove:

- every Trainer Feature with a status effect is represented in Java;
- every PTU status can legally be applied by a generic payload;
- all immunity/prevention rules are complete;
- all status durations and expiry rules are complete;
- every stacked-status interaction is correct;
- social or institutional state can create a PTU status;
- workplace safety observations can create hazards or statuses;
- collective-action state has any battle effect.

Therefore both `status lifecycle` and `Trainer Features / perks` remain PARTIAL.

## Why worker representation is not a battle subsystem

Nothing inspected in AutoPTU-Java proves:

- worker-association membership;
- representative authority;
- member voting or dissent;
- collective negotiation;
- safety-committee procedure;
- workplace hazard-report review;
- work stoppages;
- mutual-aid commitments;
- professional standards;
- employment rights;
- workplace morale;
- crowd behavior;
- worker/Pokémon representation;
- legal status of collective action.

These are overworld/institutional responsibilities.

AutoPTU receives only a tactical battle when a separate incident genuinely creates one.

## Pass 115 encounter dependency map

### Mine Ventilation Stop-Work — FULL

Narrative objective:
Protect a safe staging area and allow workers/wild Pokémon to leave while a separately observed workplace concern remains under technical review.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if air conditions or protected routes become tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Resolve the stop-work, technical readings and worker evacuation in world state. Freeze a safe staging arena and run only actual combatants. No air-quality status, panic behavior or workplace hazard is invented.

### Ferry Crew Mutual-Aid Transfer — FULL

Narrative objective:
Keep a temporary mutual-aid handoff moving while a separate Pokémon disturbance blocks a loading approach.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if storm residue or route conditions receive tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `CLEAR_ROUTE`, `PROTECT`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Complete the technician/equipment handoff outside battle. Move all noncombatants and cargo to safe world-state positions. Use a static battle only if a confrontation remains.

### Workshop Association Archive Firebreak — FULL

Narrative objective:
Protect evacuation routes and selected archive/tool assets while members handle priorities through world-state decisions.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if fire, smoke or protected areas receive tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT_OBJECT`, `EVACUATE`, `REACH_EXIT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Resolve evacuation, custody and archive/tool priorities before battle. Keep those assets outside the grid or as noninteractive world-state objects. Run a static confrontation in an already-cleared section.

## New overworld blockers introduced by Pass 115

These belong outside AutoPTU-Java:

- `WORKER_ASSOCIATION_STATE`
- `ASSOCIATION_MEMBERSHIP_HISTORY`
- `REPRESENTATION_MANDATE_STATE`
- `MEMBER_POSITION_AND_DISSENT_PRIVACY`
- `ASSOCIATION_DECISION_HISTORY`
- `WORKER_OBSERVATION_LEDGER`
- `SAFETY_CONCERN_CASE_STATE`
- `COLLECTIVE_PROPOSAL_STATE`
- `COLLECTIVE_POSITION_HISTORY`
- `COLLECTIVE_ACTION_EVENT_STATE`
- `MUTUAL_AID_COMMITMENT_STATE`
- `FORMER_WORKER_INSTITUTIONAL_MEMORY`
- `WORKER_ASSOCIATION_TO_WORKPLACES_HANDOFF`
- `WORKER_ASSOCIATION_TO_AGREEMENTS_HANDOFF`
- `WORKER_ASSOCIATION_TO_GOVERNANCE_HANDOFF`
- `WORKER_ASSOCIATION_TO_INSTITUTIONAL_REVIEW_HANDOFF`
- `WORKER_ASSOCIATION_TO_MEDIA_COMMUNICATION_HANDOFF`
- `WORKER_ASSOCIATION_TO_MINECRAFT_PROJECTION`
- `WORKER_ASSOCIATION_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 115

Do not infer:

- association membership -> combat bonus;
- guild membership -> Trainer Class, Feature, Edge or Skill Rank;
- safety concern -> confirmed hazard;
- safety concern -> PTU status/zone;
- worker observation -> confirmed cause;
- majority position -> unanimous belief;
- spokesperson -> authority outside the granted scope;
- work stoppage -> crime, sabotage or hostile faction;
- management disagreement -> antagonist state;
- collective action -> morale buff/debuff;
- worker group -> Pack Mon, swarm or tactical team mechanics;
- professional standard -> mechanical crafting bonus;
- mutual aid -> infinite supplies or free services;
- former worker -> current access/authority;
- PC employment -> mandatory association membership;
- human association -> authority to represent Pokémon;
- Pokémon ownership -> consent to indefinite work;
- Pokémon refusal -> fear, Injury, abuse or equipment fault;
- generic Trainer Feature status effects -> workplace/social status subsystem;
- generic Trainer Feature execution primitives -> full Trainer Feature catalog;
- Minecraft crowd/meeting visuals -> association decision state.

## PTU/Caelo validation state

No reliable primary Caelo corpus was available as an invocable source during this run.

Super PTU Online Helper was not exposed as an invocable capability.

No PTU/Caelo mechanic for unions, guild authority, worker representation, collective bargaining, work stoppages or safety committees was validated.

Potentially relevant exact rules for Charm, Command, Guile, Intuition, professional Features, crafting Features or Pokémon communication remain pending and must be checked only if a future encounter actually invokes them.

No social Skill roll should be allowed to erase worker agency, force collective agreement, establish legal authority or decide the truth of a safety claim.
