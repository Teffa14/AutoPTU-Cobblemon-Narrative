# Pokémon Cognition, Problem Solving, and Tool Use Layer

Status: PROPOSED SYSTEM DESIGN. Not canon.
Pass: 133
Date: 2026-08-23

## Purpose

This layer gives Ouros a conservative way to remember individual Pokémon problem solving, object manipulation, tool manufacture/use, strategy switching, persistence, and task-specific behavioral flexibility.

It does not create a universal intelligence statistic.

PTU 1.05 explicitly removed the old Intelligence Capability. The world therefore stores observable behavior and uncertainty instead of reconstructing an unofficial replacement.

## Authority boundary

This layer owns:

- individual problem-context history;
- observed attempts and strategies;
- task-specific success/failure;
- object manipulation observations;
- proposed tool-use observations;
- changes of strategy after failure or environmental change;
- repeated performance by the same persistent Pokémon;
- evidence that a behavior may be novel for that individual;
- task-version history for longitudinal studies.

It does not own:

- Pokémon identity, custody, partnership, release, or agency: Pokémon Agency owns those;
- physical object identity and provenance: Material Culture owns those;
- transmission between individuals: Social Learning owns that;
- research authorization and welfare: Research Ethics owns that;
- scientific hypotheses/publication: Science owns that;
- generic crafting rules: PTU/Caelo mechanics must authorize those;
- battle AI policy: AutoPTU owns that when implemented;
- block interactions as rules: Minecraft is projection/presentation only.

## Core principle

Store the event before the interpretation.

Preferred chain:

`problem context -> available affordances -> observed attempt -> object/action sequence -> immediate result -> strategy revision -> later repeat -> interpretation`

Do not compress this into:

`pokemon_intelligence = 8`

## Core entities

### COGNITIVE_TASK_CONTEXT

A persistent description of a problem situation that can be revisited.

Suggested fields:

- `task_context_id`
- `location_id`
- `created_at_world_time`
- `task_version_id`
- `goal_description_observed`
- `available_object_ids`
- `relevant_access_points`
- `environment_revision_refs`
- `human_intervention_state`
- `research_protocol_id` if formal study
- `status`

The goal can be observer-defined without assuming the Pokémon represents the goal in the same way.

### TASK_VERSION

Used when the environment changes.

Examples:

- latch orientation changes;
- one access route is blocked;
- object weight changes;
- food is moved behind a different barrier;
- a familiar bridge is removed;
- an old tool is unavailable.

Suggested fields:

- `task_version_id`
- `task_context_id`
- `valid_from`
- `valid_to`
- `changed_affordances`
- `change_provenance`

### PROBLEM_SOLVING_OBSERVATION

One observation of one Pokémon interacting with one task version.

Suggested fields:

- `observation_id`
- `pokemon_entity_id`
- `task_version_id`
- `observer_id`
- `observed_at`
- `method`
- `attempt_sequence_refs`
- `outcome`
- `latency_band`
- `interruption_state`
- `prior_exposure_known`
- `confidence`
- `notes`

### STRATEGY_ATTEMPT

A coarse, behaviorally described attempt.

Examples:

- pull object toward opening;
- push object under gap;
- strike latch repeatedly;
- abandon direct route and circle around;
- wait for another actor to open access;
- carry a specific object to the task site;
- modify an object before using it.

Suggested fields:

- `attempt_id`
- `observation_id`
- `ordinal`
- `action_description`
- `object_ids`
- `result`
- `continued_or_abandoned`

Do not encode invisible mental states such as `understood_causality=true` from a single successful attempt.

### OBJECT_MANIPULATION_EVENT

Records physical interaction with a persistent object.

Suggested fields:

- `event_id`
- `pokemon_entity_id`
- `item_instance_id`
- `action_type`
- `from_location`
- `to_location`
- `modification_observed`
- `damage_observed`
- `purpose_hypothesis_ids`
- `timestamp`

Material Culture remains authoritative for the object's physical state and provenance.

### TOOL_USE_ASSESSMENT

A scientific/narrative assessment that an observed object interaction plausibly qualifies as tool use under the project's chosen definition.

Suggested fields:

- `assessment_id`
- `observation_ids`
- `item_instance_ids`
- `functional_goal_claim`
- `external_object_requirement_met`
- `manipulation_requirement_met`
- `alternative_explanations`
- `confidence`
- `assessed_by`
- `assessed_at`

This is an interpretation. It does not create a PTU Item or weapon rule.

### STRATEGY_REVISION_EVENT

Records evidence that the same individual changes approach after conditions change or a prior approach fails.

Suggested fields:

- `revision_event_id`
- `pokemon_entity_id`
- `task_context_id`
- `from_strategy_description`
- `to_strategy_description`
- `trigger_observed`
- `time_between_attempts`
- `confidence`

### INDIVIDUAL_BEHAVIOR_REPERTOIRE

A summary index derived from observations, not a stat block.

Examples of entries:

- `uses loose stones to hold orchard gate open — repeated, high confidence`
- `carries preferred metal object to scrap pile — repeated, purpose uncertain`
- `opens north workshop latch — observed twice, exact method changed after repair`

Never summarize as `smart`, `stupid`, `IQ`, or `Intelligence rank`.

## Novelty and innovation

Use conservative labels:

- `NEW_TO_OBSERVERS`
- `NEW_TO_THIS_INDIVIDUAL_AS_FAR_AS_KNOWN`
- `POSSIBLE_INDIVIDUAL_INNOVATION`
- `PRIOR_EXPERIENCE_UNKNOWN`
- `SPECIES_TYPICAL_BEHAVIOR_POSSIBLE`
- `SOCIAL_EXPOSURE_POSSIBLE`

Only Social Learning can later assess whether the behavior spread through observation/transmission.

A first observation is never equivalent to first performance.

## Tool identity and versions

When a Pokémon manufactures or modifies a persistent external object:

1. Material Culture creates or updates the `item_instance_id`.
2. This layer records the manipulation/manufacture sequence.
3. The item may have successive physical revisions.
4. The Pokémon's continued association with the item is recorded as observed behavior, not ownership unless another layer establishes ownership/custody.

Tinkatink-inspired scenarios are therefore capable of preserving:

scrap provenance -> hammer version A -> loss/damage -> new material acquisition -> hammer version B -> later museum/archive significance

without inventing a crafting recipe or damage profile.

## Affordances and morphology

A task must preserve what actions were physically possible.

Relevant contextual facts may include:

- object size/weight relative to the Pokémon;
- reach;
- grasping/contact surfaces;
- water/air/ground access;
- opening size;
- height;
- whether an object can be carried at all;
- whether a path is traversable under verified world rules.

Failure can be caused by physical mismatch rather than lack of understanding.

Success can be caused by a highly obvious affordance rather than sophisticated reasoning.

Do not use species body-plan flavor to invent PTU Capabilities.

## Persistence and memory

Ouros may compare behavior over long intervals without declaring a memory mechanic.

Valid observation:

`same pokemon_entity_id used the same latch-opening sequence after 14 months`

Possible interpretation:

`retention of a learned solution`

Alternative explanations remain possible:

- reacquisition by trial;
- unobserved repeated use;
- strong environmental affordance;
- species-typical routine.

No memory roll or retention bonus is created here.

## Human-designed cognitive studies

Formal experiments require Research Ethics authorization.

Preferred design principles:

- non-harmful;
- voluntary participation where agency/behavior can be respected;
- clear stop conditions;
- no deprivation mechanic invented for a reward;
- no dangerous trap merely to create data;
- preserve failed attempts;
- change one relevant affordance at a time when possible;
- preserve prior-exposure uncertainty;
- avoid over-testing one individual just because it is narratively important.

## Overworld problem solving

This layer is most useful outside combat.

Examples:

- a wild Pokémon repeatedly opens a gate in an unexpected way;
- an institutional partner learns a new route after a lift is removed;
- a released former partner uses an old object differently years later;
- a Tinkatink-like Pokémon rebuilds a tool from locally available material;
- a Pokémon uses a floating object to cross or access something, if world-state evidence supports it;
- a workshop adapts because a recurring wild visitor manipulates unsecured parts.

The world can remember all of these without turning them into Trainer commands.

## Minecraft projection

Minecraft may display:

- persistent objects;
- changed object positions;
- damaged or revised tools;
- opened/closed gates;
- evidence left after a problem-solving event;
- replayable observation markers where appropriate.

Minecraft must not own:

- cognitive success rules;
- tool-use classification;
- Pokémon intent;
- PTU crafting;
- arbitrary block-breaking permission;
- lock bypass;
- pathfinding truth;
- tactical AI policy.

If the server resolves a world-state behavior while the chunk is unloaded, Minecraft later renders the resulting authoritative state.

## Social Learning handoff

A behavior moves toward Pass 125 only when another Pokémon's acquisition becomes relevant.

Example sequence:

1. Pokémon A independently opens a feeder latch.
2. Chronicle records A's attempts.
3. Pokémon B is later present while A performs the method.
4. B subsequently performs a similar method.
5. Social Learning records a transmission observation/hypothesis.
6. This cognition layer continues to own each individual's task-performance history.

Do not retroactively label A's original solution culturally transmitted unless evidence supports it.

## Encounters and engine boundaries

### Workshop Latch Study — FULL

Premise:

A recurring wild Pokémon has learned to enter a workshop through a maintenance latch. A repair changes the mechanism. During a disturbance, the Pokémon tries multiple access strategies while other actors create tactical pressure.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if object interaction changes routes during battle or actors intercept movement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if used;
- terrain/weather/hazards/zones/reactions — BLOCKING if interactable spaces create tactical zones/reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if the manipulated tool becomes mechanically relevant;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `SOLVE_OBJECTIVE`, `TRY_ALTERNATIVE`, `WITHDRAW`, or `REACH_ACCESS_POINT` behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED:

Resolve the Pokémon's attempts and latch outcome as world state before combat. If a confrontation remains, freeze the workshop geometry and open a conventional static AutoPTU battle. The battle does not decide whether the Pokémon understood the latch.

### Floodgate Debris Problem — FULL

Premise:

A persistent Pokémon has previously moved loose debris to reach a dry refuge. A changed water-control state makes the familiar solution ineffective.

Primary dependencies:

- complete movement — BLOCKING for live movable objects/displacement;
- terrain/weather/hazards/zones/reactions — BLOCKING if water/debris changes tactical spaces;
- AI tactical policy — BLOCKING for trying and revising environmental solutions;
- Minecraft/Cobblemon/Craftics playback — BLOCKING.

REDUCED:

Hydrology and problem solving resolve in overworld state. The selected refuge/access state is frozen before any battle.

### Tool Recovery at Scrap Yard — FULL

Premise:

A persistent Pokémon returns to retrieve or rebuild an object from a scrap yard while workers and another Pokémon create a conflict over access.

Dependencies become rich only if the tool is manipulated inside battle. Otherwise the object and provenance remain world state.

REDUCED:

Material selection, tool revision, worker response, and Pokémon agency resolve outside battle. AutoPTU receives only the independent confrontation.

### The Multi-Access Box

Primary mode is non-combat research.

A harmless research apparatus has several access methods. Across years, methods are changed or blocked and observations are compared.

No battle-engine dependency is required unless an unrelated confrontation occurs.

## Non-inferences

Pass 133 must never infer:

- problem solved -> high general intelligence;
- problem failed -> low intelligence;
- tool use -> Technology Education;
- repeated solution -> perfect memory;
- apparent planning -> Trainer Command rank;
- group coordination -> social transmission;
- object carried -> ownership;
- object modified -> valid PTU crafted item;
- hammer flavor -> weapon stats;
- rock launched -> generic ranged attack;
- opened gate -> universal lock bypass;
- changed strategy -> tactical AI implementation exists;
- object moved in Minecraft -> legal PTU forced movement;
- Oranguru behavior -> Trainer Orders;
- Tinkatink manufacture -> generic crafting recipe;
- successful observation -> consent for further study.

## World-state blockers

Implementation outside the battle core still needs:

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
- `COGNITION_TO_SOCIAL_LEARNING_HANDOFF`;
- `COGNITION_TO_RESEARCH_ETHICS_HANDOFF`;
- `COGNITION_TO_MINECRAFT_PROJECTION`.

## Canon questions left open

- Which Pokémon populations begin with authored object-use behaviors?
- Which individual behaviors should be discovered only through play?
- How much problem solving should advance while chunks are unloaded?
- Which world objects are safe for autonomous Pokémon manipulation?
- Can player-built puzzle apparatuses become research tools?
- What evidence threshold should Ouros require before calling an event tool use?
- How should known prior training affect interpretation?
- Which species-specific behaviors are canon versus only research candidates?
- How much historical behavioral detail should Archives retain?

## PTU/Caelo gate

The project PTU 1.05 changelog explicitly says the Intelligence Capability was removed.

No generic Intelligence mechanic is introduced.

No Caelo-specific cognition/tool-use rule was recovered reliably in an invocable source during this pass. Super PTU Online Helper was unavailable.

Do not invent puzzle DCs, Intelligence ranks, memory checks, crafting rolls, tool bonuses, improvised weapon rules, autonomous Trainer Orders, or cognition-based battle modifiers.