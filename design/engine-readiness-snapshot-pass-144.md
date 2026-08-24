# Engine readiness snapshot — pass 144

Status: implementation-readiness evidence for narrative design. Not Ouros canon.

## Live repositories inspected

AutoPTU-Java head inspected: `359c31638448f23b6da230679988e42f21777abc` — `Port Perception pre-damage reaction (#172)`.

AutoPTU Python head inspected: `0d56ea7b5a2b99a96f7ac4ca40b405e0ffbf83b8` — `Career: recover corrupt persisted competitive totals (#82)`.

The Python change is Career persistence work and does not promote a tactical capability family.

AutoPTU-Java README still states that Python AutoPTU remains authoritative while the Java port is incomplete. It still lists core combat state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, full transcript parity, tactical AI and Minecraft/Cobblemon adapter work as incomplete.

## New Java evidence since pass 143

The latest Java slice ports one Perception pre-damage reaction path.

The tested contract demonstrates, for that representative mechanic:

- Perception checks authoritative Ability state and suppression;
- the reaction requires a server-owned `perception_ready` temporary effect;
- an optional out-of-turn decision happens before that readiness is consumed;
- round-scoped `perception_used` state can block repeat use;
- a second optional decision can authorize the movement reaction;
- safe-tile reaction movement is applied to authoritative combatant position;
- the reaction movement does not spend the combatant's normal Shift action;
- successful movement can cancel the incoming hit;
- the reaction records its own round-scoped usage state;
- Mold Breaker interaction is represented for this contract.

This is strong evidence for one specific pre-damage reaction path and one authoritative reaction movement application.

It is not evidence for:

- generic reaction support;
- generic dodge/evasion training mechanics;
- interception;
- Push/Pull execution;
- knockback;
- collision/falling;
- movement-triggered hazards;
- arbitrary out-of-turn actions;
- training-objective AI;
- practice progression;
- Minecraft training playback.

## Permanent capability map

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
- terrain / weather / hazards / zones / reactions as a complete family
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

Do not promote a category because one representative mechanic works.

## PTU progression evidence relevant to training

The project PTU data currently exposes explicit Pokémon progression rules including examples such as:

- `Skill Improvement`;
- `Accuracy Training`;
- `Capability Training`;
- `Advanced Mobility`;
- `Underdog's Lessons`;
- `Expand Horizons` under its Mentor prerequisite.

These mechanics have explicit prerequisites and/or Tutor Point costs.

Therefore narrative training cannot recreate them through repetition counts, elapsed hours or descriptive success.

A training record may reference an authoritative PTU transaction after that transaction actually changes mechanical state.

`practice_attempt.completed` is never enough by itself.

## Pass 144 encounter dependency review

### Rematch Preparation Circuit — FULL

Requires:

- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base movement legality;
- BLOCKING complete movement if the circuit requires interception, moving objectives or forced repositioning;
- VERIFIED core calculations;
- VERIFIED action economy/initiative;
- PARTIAL full lifecycle;
- PARTIAL stateful damage when real sparring damage is used;
- PARTIAL status lifecycle when exact statuses are used;
- BLOCKING terrain/weather/hazards/zones/reactions if real zones, hazards or reaction drills are part of the setup;
- PARTIAL move-specific behavior;
- PARTIAL abilities;
- PARTIAL items;
- PARTIAL Trainer Features/perks;
- VERIFIED AI legal-action infrastructure;
- BLOCKING AI tactical policy for TRAIN_OBJECTIVE / PROTECT_LANE / WITHDRAW / RETEST behavior;
- BLOCKING adapter/playback.

REDUCED: keep props, criteria and coach feedback in world state. Use one static legal AutoPTU spar and inspect the transcript afterward. No custom progression, hazard or combo mechanics.

### Pair Coordination Drill — FULL

The intended version needs tactical AI that understands spacing and practice objectives rather than simply selecting legal actions.

It also depends on complete movement if objective markers, interception or live route pressure matter.

The complete environment/reaction family remains blocking when dynamic zones or reaction-heavy drills are used.

REDUCED: use a legal static Multi Battle. Record spacing and target choices from the authoritative transcript. No combo or shared-action effect is created.

### Cooperative Care Practice — FULL

This is primarily an overworld interaction problem.

A rich version needs:

- BLOCKING AI tactical policy for voluntary non-combat approach/disengage/return behavior;
- BLOCKING adapter/playback for stations, body positioning and observable choices.

It does not inherently require battle damage or statuses.

REDUCED: resolve attempts as world-state observations and stop/change the session if the Pokémon disengages.

### Route Transfer Test — FULL

Requires VERIFIED base movement legality for supported movement modes.

It becomes dependent on BLOCKING complete movement if interception, forced movement or objective routing is required.

If route conditions produce real tactical environmental effects, it also depends on BLOCKING terrain/weather/hazards/zones/reactions as a family.

It requires BLOCKING AI tactical policy for field-transfer objectives and BLOCKING adapter/playback.

REDUCED: resolve the route condition outside combat, freeze a static arena if a confrontation occurs, then record any observed transfer separately.

## Training-specific non-inferences

Do not infer:

- repetitions -> XP;
- training hours -> Levels;
- target drills -> Accuracy Training;
- obstacle courses -> Capability Training;
- route running -> Advanced Mobility;
- repeated task performance -> Skill Improvement;
- studying or rehearsing a Move -> learning the Move;
- one successful trial -> mastery/generalization;
- coach title -> Mentor Feature;
- private coaching -> Trainer Feature eligibility;
- harsh practice -> faster progression;
- failed attempt -> Loyalty loss;
- refusal/disengagement -> mechanical disobedience;
- sparring -> Tutor Points;
- simulated Sticky Web/Weather/terrain -> actual tactical field state;
- practiced combinations -> simultaneous actions or linked damage;
- practice partner -> ownership/custody;
- wild participation -> capture eligibility;
- private training record -> opponent battle knowledge;
- newest Perception reaction support -> generic dodge-training system;
- Perception reaction movement -> complete reaction family;
- Perception safe-tile movement -> generic forced movement/interception.

## Training and battle transcript boundary

A battle transcript can provide evidence for a training objective.

Examples:

- repeated clustering before area attacks;
- repeated target-selection pattern;
- repeated missed timing window when the relevant Move behavior is authoritative;
- legal movement route used in several turns.

The training system may create an interpretation from those events.

It cannot rewrite the battle result or infer private motives.

After training, a later transcript may become transfer evidence.

The system should compare observations rather than grant a hidden improvement score.

## PTU/Caelo boundary

Project PTU-derived data confirms explicit Poke Edges and Mentor-linked progression concepts.

Pass 144 did not recover a complete authoritative Caelo corpus defining downtime training, training-time requirements, modified Poke Edge rules, tutoring restrictions or coaching mechanics.

Super PTU Online Helper was not exposed as an invocable tool during this run.

No Caelo rule or helper output is invented.

Before any narrative training event changes mechanics, the governing rule must be found in the project source set and implemented/validated through the authoritative mechanics path.

## New overworld blockers

- `TRAINING_PROGRAM_STATE`
- `TRAINING_OBJECTIVE_HISTORY`
- `TRAINING_SESSION_LEDGER`
- `TRAINING_SETUP_REVISIONS`
- `PRACTICE_ATTEMPT_OBSERVATIONS`
- `TRAINING_CUE_HISTORY`
- `COACH_FEEDBACK_PROVENANCE`
- `TRAINING_ADJUSTMENT_HISTORY`
- `TRANSFER_GENERALIZATION_OBSERVATIONS`
- `TRAINING_PRIVACY_AND_OPPONENT_KNOWLEDGE`
- `TRAINING_TO_PTU_MECHANICS_TRANSACTION_HANDOFF`
- `TRAINING_TO_CARE_WELFARE_HANDOFF`
- `TRAINING_TO_BATTLE_TRANSCRIPT_REVIEW`
- `TRAINING_TO_EDUCATION_PRACTICUM_HANDOFF`
- `TRAINING_TO_WORKING_POKEMON_HANDOFF`
- `TRAINING_TO_MINECRAFT_PLAYBACK`

These belong to persistent world-state services rather than AutoPTU-Java battle rules.

## Outcome

Pass 144 can advance immediately as persistent narrative architecture.

Routine practice and cooperative-care sessions can be represented entirely in world state.

Rematch preparation and pair-coordination concepts can use reduced static battles with the current verified core capabilities while keeping coaching objectives and transcript review outside the grid.

Mechanically richer drills remain explicitly gated behind the exact movement, environment/reaction, tactical-AI and adapter families that are still incomplete.