# Engine readiness snapshot — pass 145

Status: implementation-readiness evidence for narrative design. Not Ouros canon.

## Live repositories inspected

AutoPTU-Java head inspected: `359c31638448f23b6da230679988e42f21777abc` — `Port Perception pre-damage reaction (#172)`.

AutoPTU Python head inspected: `a868d8a95b467030187482c4bf61da600bab912d` — `Career: recover corrupt persisted inventory (#84)`.

The current Python work is Career persistence/resilience and does not promote a tactical capability family.

Pass 145 also inspected the existing Pass 144 readiness snapshot and adjacent narrative layers before defining play/enrichment dependencies.

## Java evidence retained from pass 144

The current Java head ports one Perception pre-damage reaction path.

For that specific path, evidence shows:

- Ability state and suppression are authoritative;
- readiness/usage state is server-owned;
- optional out-of-turn decisions occur before damage;
- a safe tile is selected from authoritative movement state;
- the combatant can move without spending its normal Shift;
- successful movement can cancel the incoming hit;
- usage is tracked for the round;
- Mold Breaker interaction is represented for the tested contract.

This remains narrow evidence.

It does not establish:

- generic reactions;
- voluntary non-combat movement policy;
- play-partner AI;
- social-play classification;
- de-escalation AI;
- complete withdrawal/escape objectives;
- interception;
- Push/Pull execution;
- knockback;
- collision/falling;
- moving-object physics;
- dynamic recreation objects;
- enrichment state;
- Minecraft play playback.

## Current Python evidence

The latest AutoPTU Python commits sanitize malformed persisted Career state including competitive totals, relationship memory and inventory.

Those are important Career resilience changes but they do not change battle-engine capability classification.

A persisted relationship map in Career must not be confused with the proposed play layer. Play observations never write relationship memory automatically.

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

## Play/enrichment mechanical boundary

Pass 145 introduces no new PTU mechanic.

The narrative layer may record:

- play episode;
- available enrichment options;
- observable interaction;
- approach/disengagement;
- co-participation;
- provisional play/conflict classification;
- object-use history;
- context-specific preference evidence;
- transition into Training, Care, Cognition or Social Learning.

It may not directly write:

- XP;
- Levels;
- Tutor Points;
- Poke Edges;
- Moves;
- Skills;
- stats or Combat Stages;
- HP/temp HP;
- Injuries;
- Status;
- Loyalty/Friendship;
- Features;
- Abilities;
- Items/equipment effects;
- Contest bonuses;
- capture eligibility;
- spawn weights.

Sword/Shield Pokémon Camp awards game-specific rewards for some interactions. Those rewards are not evidence of a PTU mechanic.

## Encounter dependency review

### Nursery Yard Escalation — FULL

Requires:

- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base movement legality;
- BLOCKING complete movement if participants withdraw, re-enter, must be separated or cross threatened space dynamically;
- VERIFIED core calculations;
- VERIFIED action economy/initiative;
- PARTIAL full lifecycle;
- PARTIAL stateful damage if combat begins;
- PARTIAL status lifecycle for exact status effects;
- BLOCKING terrain/weather/hazards/zones/reactions if protected zones, environmental effects or reaction-heavy behavior matter tactically;
- PARTIAL move-specific behavior;
- PARTIAL abilities;
- PARTIAL items when a real mechanical item is used;
- PARTIAL Trainer Features/perks;
- VERIFIED AI legal-action infrastructure;
- BLOCKING AI tactical policy for WITHDRAW / REENGAGE / PROTECT / DEESCALATE or non-hostile objectives;
- BLOCKING adapter/playback.

REDUCED:

End recreation first in world state. Move noncombatants to safety. If an independent confrontation remains, open a static legal AutoPTU arena with only actual combatants. The earlier behavior classification stays outside the grid.

### Riverside Object Play Spillover — FULL

Requires VERIFIED base movement legality for supported standard movement.

It becomes dependent on BLOCKING complete movement if multiple Pokémon need dynamic crossing/withdrawal/interception behavior.

It requires BLOCKING AI tactical policy for non-hostile CROSS, RETURN_TO_GROUP or WITHDRAW goals.

It requires BLOCKING adapter/playback to render object/play state authoritatively.

If currents, changing water or another environmental mechanic matter during battle, it additionally depends on BLOCKING terrain/weather/hazards/zones/reactions as a complete family.

REDUCED:

Resolve recreational movement and route management in overworld state. Freeze one static shoreline state only if a separate battle starts. Recreational objects produce no combat modifier.

### Enrichment Yard Equipment Failure — FULL

Requires BLOCKING complete movement for dynamic evacuation around damaged structures and BLOCKING AI tactical policy for WITHDRAW/REACH_EXIT/PROTECT behavior.

It requires BLOCKING adapter/playback.

Any falling debris, collapse, zone or environmental damage additionally requires the exact mechanic under the currently BLOCKING environment/reaction family.

REDUCED:

Close and evacuate the yard before battle. Run any independent confrontation in a safe static arena. Architecture/Material Culture resolves repair. The play layer records later reintroduction and voluntary use.

### Choice Trial — NON-COMBAT

No AutoPTU dependency.

It records available options and bounded observations.

No hidden mechanical reward is created.

## Play-specific non-inferences

Do not infer:

- play -> XP/Levels;
- play -> Tutor Points or Poke Edges;
- play -> Loyalty/Friendship;
- play -> healing or recovery;
- play -> positive Care diagnosis;
- lack of play -> illness;
- one rough interaction -> combat/aggression;
- one social episode -> friendship/kinship;
- mixed-species play -> ecological mutualism;
- co-participation -> social learning;
- object manipulation -> tool use;
- repeated object choice -> mechanical proficiency;
- enrichment program -> Training program;
- nursery membership -> juvenile mechanical state;
- toy -> PTU Item;
- Minecraft prop proximity -> interaction;
- animation/pathfinding -> preference;
- placed toys -> Cobblemon spawn modifier;
- Perception reaction movement -> generic noncombat withdrawal AI;
- Perception reaction path -> complete reactions family.

## Battle transcript boundary

If free play transitions into a legal battle, the AutoPTU transcript begins at the battle boundary.

The play system may reference that transcript as evidence that an interaction escalated or was interrupted.

It cannot rewrite the preceding behavior as hostile merely because combat later occurred.

Similarly, a training session that begins after free play creates a new Training record. The earlier recreational episode remains intact.

## PTU/Caelo boundary

Pass 145 recovered no complete authoritative Caelo rule defining recreational play, enrichment, welfare bonuses or camp rewards.

Super PTU Online Helper was not exposed as an invocable tool during this run.

No Caelo rule or helper output is invented.

Before any play/enrichment event changes mechanical state, the governing rule must be found in the project's authoritative source set and executed through the validated mechanics path.

## New overworld blockers

- `PLAY_EPISODE_HISTORY`
- `ENRICHMENT_OPPORTUNITY_SETS`
- `ENRICHMENT_OPTION_STATE`
- `OPTION_INTERACTION_OBSERVATIONS`
- `PLAY_INVITATION_OBSERVATIONS`
- `PLAY_PARTNER_EPISODES`
- `PLAY_CLASSIFICATION_ASSESSMENTS`
- `PREFERENCE_OBSERVATION_HISTORY`
- `RECREATIONAL_OBJECT_USAGE_HISTORY`
- `ENRICHMENT_PROGRAM_STATE`
- `PLAY_TO_CARE_HANDOFF`
- `PLAY_TO_TRAINING_HANDOFF`
- `PLAY_TO_COGNITION_HANDOFF`
- `PLAY_TO_SOCIAL_LEARNING_HANDOFF`
- `PLAY_TO_MATERIAL_CULTURE_HANDOFF`
- `PLAY_TO_MINECRAFT_PLAYBACK`

These are world-state services, not AutoPTU-Java battle rules.

## Outcome

Pass 145 can advance immediately without waiting for new battle mechanics.

Most play and enrichment should be represented as optional, compressible overworld observations.

Mechanically rich scenarios retain FULL versions for the intended future simulation and REDUCED versions that move noncombatants and recreation state outside AutoPTU before opening a static legal battle.

This keeps worldbuilding progress independent from missing tactical AI, complete movement and Minecraft playback while preventing the adapter from inventing PTU rules.
