# Engine Readiness Snapshot — Pass 139

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to the working-Pokémon institutional-role concepts added in Pass 139. Both engine repositories remain read-only for this task.

A representative mechanic never promotes an entire capability family by itself.

## Inspected heads

AutoPTU-Java:

`defabdc87b1f366508cc00b80215689de2a528bd`

Latest inspected commit:

`Bind TILE choices to authoritative area targets (#168)`

This slice composes a legal TILE move choice with the current authoritative runtime state before expanding effective combatant targets. It revalidates that the Move belongs to the actor, action/frequency is still available, the exact tile choice remains legal, and then derives target IDs from current area geometry, footprints, blockers, LoS and HP eligibility. Minecraft/Cobblemon cannot supply those authoritative targets.

This strengthens an already VERIFIED targeting/action-space boundary. It does not add work objectives, object manipulation, service-partner AI, escort behavior or institutional role semantics.

AutoPTU Python:

`6369b246d84eed173417dfaf01399f1286565ab5`

Latest inspected Python commit:

`Career: isolate Vercel from full battle server (#77)`

This isolates Career deployment behind a thin Vercel entrypoint and adds deployment-focused coverage. It does not change the tactical classifications below.

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

Recent pre-damage reaction, TILE targeting and narrow movement slices reduce specific gaps. They do not override the repository-level boundary.

## Working-Pokémon mechanics boundary

Pass 139 introduces no new PTU mechanic.

The following are overworld/institutional state outside AutoPTU:

- Pokémon work roles;
- task requests;
- work assignment lifecycle;
- observed acceptance/refusal;
- staffing availability;
- shift history;
- workload ledgers;
- relief coverage;
- workplace handoffs;
- work equipment issue/return;
- role reviews;
- institutional retirement;
- temporary wild work partnerships;
- public work reputation.

AutoPTU becomes authoritative only when a Pokémon actually enters a battle and the encounter needs battle-control scope, legal actions or mechanical consequences.

A work assignment never creates battle command authority.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

The current Java head strengthens this family further by binding a currently legal TILE choice to authoritative area targets at execution time.

This can support static combat inside a freight hall, construction yard or floodgate site.

It cannot decide which work Pokémon is on duty, where a noncombat worker should evacuate, or whether a task assignment is valid.

### base movement legality — VERIFIED

Ordinary Shift/Jump legality remains parity-backed for the ported scope.

A working Pokémon that is an actual combatant can use validated ordinary movement.

This does not implement job-route traversal, escort objectives or moving cargo.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Recent Java work exposes narrow reaction movement and recognizes Push/Pull instruction metadata, but the README still leaves forced movement unfinished.

Pass 139 FULL encounters with live evacuations, escorts, task partners crossing threatened spaces, movable cargo or interception remain dependent on this family.

### core calculations — VERIFIED

Core arithmetic/stat/type primitives remain verified for the ported scope.

Occupation, tenure, work history, public reputation, a harness or species job lore cannot modify these calculations without exact mechanics.

### action economy/initiative — VERIFIED

Action budget and initiative infrastructure remain verified.

Work steps such as loading cargo, inspecting a gate, signing a handoff or starting a machine are not combat actions unless an authoritative mechanic maps them into battle.

### full turn/round lifecycle — PARTIAL

Round lifecycle, delayed effects, temporary effects and selected reaction paths have concrete parity-backed slices.

The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

The authoritative Move pipeline now includes selected pre-damage reaction composition, but the README still marks full damage incomplete.

Machinery failure, cargo impact, construction debris or floodgate hardware cannot create custom damage by narrative declaration.

### status lifecycle — PARTIAL

Selected application, prevention, suppression and timing paths exist.

Workload, refusal, old age, a long shift or a workplace alarm do not create Fatigue, Sleep, Confusion, Fear or any other Status.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction coverage is expanding, but this permanent combined family remains incomplete.

A workshop floor, construction trench, moving machine, flooded gate, hot furnace or electrical room does not create tactical terrain/hazards unless an exact supported mechanic exists.

### move-specific behavior — PARTIAL

Representative Move families and target-resolution paths exist, but catalog coverage remains incomplete.

Any working-Pokémon encounter using a particular Move depends on parity for that Move and its side effects.

### abilities — PARTIAL

Selected Ability families have parity-backed behavior.

Pokédex work flavor does not become an Ability. Machoke work lore, Timburr construction lore or Conkeldurr concrete lore grants no mechanical workplace effect.

### items — PARTIAL

Item coverage remains incomplete.

Harnesses, carts, radios, uniforms, work gloves, station keys and ordinary tools remain narrative material objects unless deliberately mapped to validated PTU Items.

### Trainer Features/perks — PARTIAL

Generic Trainer Feature infrastructure and selected effect families exist, but the catalog remains incomplete.

A foreman, dispatcher, engineer, handler or trainer receives no Feature solely from occupational title.

### AI legal-action infrastructure — VERIFIED

Legal battle-choice construction/filtering remains verified. The latest Java slice further ensures selected TILE choices are revalidated against current authoritative state before targets are expanded.

This does not provide work-objective reasoning.

### AI tactical policy — BLOCKING

No complete policy exists for Pass 139 goals such as:

- `EVACUATE`;
- `CLEAR_ROUTE`;
- `PROTECT_WORKER`;
- `PROTECT_TASK_PARTNER`;
- `REACH_TASK_POINT`;
- `WITHDRAW`;
- `REACH_STAGING`;
- `PROTECT_HANDOFF`.

A legal-action list is not an objective-aware worker/rescue AI.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer authoritative work state from:

- a Pokémon standing near a workstation;
- a leash or cosmetic;
- a named entity;
- a cart or minecart;
- an NPC following the Pokémon;
- a workplace block palette;
- species identity;
- loaded-entity presence.

The adapter must never invent PTU job bonuses, command authority, movement rules or work completion.

## Pass 139 encounter dependencies

### Freight Hall Evacuation During Equipment Failure — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live evacuation/interception and mobile protected actors;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if exact supported effects invoke it;
- terrain/weather/hazards/zones/reactions — BLOCKING if the equipment failure creates tactical hazards;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if actual PTU Items are present;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Shut down equipment and evacuate all noncombat workers/work Pokémon in world state. Freeze cargo and machinery. AutoPTU receives a static legal arena with actual combatants only. Workplaces/Manufacturing/Infrastructure resolve repair and service restoration after battle. Victory does not repair equipment or establish root cause.

### Floodgate Temporary Partnership — FULL

The richest version needs a temporary Pokémon task partner to reach a work point or withdraw while water/gate state may also matter.

Primary blockers:

- complete movement — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if current/water/gate state becomes tactical.

Other combat families remain subject to the exact Moves/Abilities/Items/Features used.

REDUCED:

Resolve the temporary wild Pokémon's assistance in world state before battle. Keep it off-grid unless authoritative battle state independently allows participation. Resolve any remaining confrontation as a static battle. The help ends with the task and does not create capture, ownership, Loyalty or permanent employment.

### Construction Yard Shift Handoff — FULL

Primary blockers:

- complete movement for live team transfer/interception;
- AI tactical policy for `REACH_STAGING`, `PROTECT_HANDOFF`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback;
- terrain/weather/hazards/zones/reactions only if an exact validated construction hazard exists.

REDUCED:

Freeze construction, perform the handoff in world state, remove workers/work Pokémon and movable equipment from tactical exposure, then open a static battle only if conflict remains. Resume the task afterward from the preserved handoff state.

### Worker Refuses Assignment

Non-combat by default.

No battle capability is required to record a Pokémon declining or not engaging with a task. The institution may use relief coverage, delay the job, offer a different task, request a separate care review when independent evidence exists, or end the role.

Refusal itself must never become a combat trigger, Status, Loyalty penalty or forced capture.

## Pass 139 world-system blockers

The narrative layer identifies these implementation contracts as needed before full Minecraft realization:

- `POKEMON_WORK_ROLE_STATE`;
- `POKEMON_TASK_REQUEST_STATE`;
- `POKEMON_WORK_ELIGIBILITY_ASSESSMENT`;
- `WORK_PARTICIPATION_OPPORTUNITY_STATE`;
- `POKEMON_WORK_ASSIGNMENT_STATE`;
- `POKEMON_WORKLOAD_LEDGER`;
- `WORK_EQUIPMENT_ASSIGNMENT_STATE`;
- `WORK_HANDOFF_STATE`;
- `TEMPORARY_WILD_WORK_PARTNERSHIP`;
- `POKEMON_WORK_ROLE_REVIEW`;
- `WORKPLACE_TO_POKEMON_AGENCY_HANDOFF`;
- `WORKING_POKEMON_TO_CARE_HANDOFF`;
- `WORKING_POKEMON_TO_MINECRAFT_PROJECTION`;
- `WORKING_POKEMON_TO_BATTLE_CONTROL_HANDOFF`.

These belong to the persistent world layer, not AutoPTU-Java.

## Non-inferences locked by Pass 139

Do not infer:

- employment/assignment -> ownership;
- capture -> on-duty availability;
- institutional housing -> ownership;
- assignment -> battle command authority;
- species/type -> individual qualification;
- Machoke -> quantified carrying capacity;
- Timburr/Conkeldurr -> construction/crafting rules;
- Electric type -> power-grid certification;
- Water type -> water-service qualification;
- Flying type -> passenger transport eligibility;
- work refusal -> low Loyalty;
- many shifts -> fatigue Status;
- many shifts -> XP or Skill growth;
- harness/uniform -> PTU Item effect;
- retirement -> stat loss or death;
- temporary wild help -> capture eligibility;
- loaded entity at workplace -> authoritative staffing state.

## Unresolved mechanical/canon questions

Still unresolved:

- what Ouros calls formal Pokémon work participation;
- whether institutions compensate Pokémon and in what form;
- how recurring participation is authorized;
- whether a Trainer/custodian can accept work on a Pokémon's behalf;
- how Pokémon refusal/acceptance should be represented when no explicit communication exists;
- what workload/rest policies are canon;
- whether institutional Pokémon can be battle-controlled by staff and under which PTU rules;
- which roles require validated Capabilities, Skills, Features or equipment;
- exact PTU/Caelo carrying/lifting/mount/task mechanics;
- how evolution changes equipment fit and task eligibility;
- whether wild Pokémon can hold recurring institutional roles;
- whether work affects Loyalty, training or progression under any project-specific Caelo rule.

The full project Caelo corpus was not reliably available in this run. Super PTU Online Helper was not exposed as an invocable capability. No mechanics are invented to fill those gaps.
