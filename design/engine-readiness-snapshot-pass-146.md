# Engine readiness snapshot — Pass 146

Status: implementation-facing evidence snapshot for narrative design. AutoPTU-Java and AutoPTU are read-only in this task.

## Live evidence inspected

AutoPTU-Java head inspected: `359c31638448f23b6da230679988e42f21777abc` — `Port Perception pre-damage reaction (#172)`.

The slice adds a specific PRE-damage Perception reaction with authoritative temporary-effect state, optional out-of-turn decisions, safe-tile movement, round-scoped usage and hit cancellation. It is parity-tested against Python for that contract.

AutoPTU-Java README still explicitly lists as unfinished:
- core combatant/grid battle state;
- full damage pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python head inspected from current commits: `a868d8a95b467030187482c4bf61da600bab912d`. Recent work is Career persistence recovery for malformed inventory/relationship/competitive/money state and does not justify a tactical category promotion.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Evidence: Java README marks range, areas, footprints, target anchors and LoS complete; later area/multi-target slices continue using authoritative geometry.

`base movement legality`

Evidence: Java README marks Shift movement legality and Jump movement complete for the listed Overland/Swim/Sky/terrain-cost/blocker/Wallrunner/sprint/landing cases.

`core calculations`

Evidence: damage-base table, type effectiveness, stages, accuracy stages, weather DB primitive, crit probability, Burn, modifiers, rounding, accuracy resolution and combat-stat resolution are listed as ported primitives. This does not mean the full stateful damage pipeline is complete.

`action economy/initiative`

Evidence: typed turn flow/action budget, deterministic initiative, Trick Room/League ordering and declared-action ordering are listed complete; later multi-target execution consumes a declaration/action/frequency once under its specific contract.

`AI legal-action infrastructure`

Evidence: deterministic legal action-space contract exists for Shift, direct targets, SELF/FIELD, tile AoE, footprints, LoS and action-budget filtering. This is legality enumeration, not tactical decision quality.

### PARTIAL

`full turn/round lifecycle`

Multiple initiative, round-start, delayed-hit, temporary-effect and reaction-order slices have parity evidence, but full lifecycle parity is not declared complete.

`full stateful damage pipeline`

Core calculations and several execution paths exist, but README explicitly leaves full damage resolution incomplete.

`status lifecycle`

Individual prevention/application/removal contracts have accumulated evidence, but the full status controller remains unfinished.

`move-specific behavior`

Delayed hits, area/multi-target execution and other representative contracts exist. The full Move registry/catalog does not.

`abilities`

Specific Abilities including prevention and PRE-damage reaction cases are ported. The full Ability registry/catalog is not.

`items`

Individual item-related boundaries exist in prior evidence; the complete item hook registry is not declared complete.

`Trainer Features/perks`

Generic prerequisites/context/frequency/resources/targets/effect/bookkeeping infrastructure and representative effects exist. Catalog-wide Feature parity is not established.

### BLOCKING AS COMPLETE FAMILIES

`complete movement including push/pull/knockback/interception/forced movement`

Java has base Shift/Jump legality and specific reaction movement. It does not have the complete family. Parsing or applying a narrow movement instruction/reaction does not prove generic forced movement/interception/collision behavior.

`terrain/weather/hazards/zones/reactions`

Semantic environment state and particular reaction paths exist, but README still lists terrain, hazards and reactions among unfinished systems. Treat the family as blocking for narrative concepts that require general dynamic environment/reaction behavior.

`AI tactical policy`

The legal choice list exists. Scoring/policy over that list remains explicitly unfinished.

`Minecraft/Cobblemon/Craftics adapter/playback support`

The Java README states the adapter comes after a parity-safe vertical slice. It is not complete.

## Pass 146 encounter dependencies

### Nesting Shore Evacuation — FULL

Required:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING only when tide/storm/fragile-ground behavior is mechanically active.

Why reduced version works sooner: civilians and young leave the tactical problem through world-state resolution; the nest is excluded from the grid; only actual combatants enter a static legal arena.

### Juvenile at the Road Crossing — FULL

Required:
- base movement legality — VERIFIED but insufficient alone;
- complete movement — BLOCKING for crossing objectives/interception/actors moving through threatened space;
- AI tactical policy — BLOCKING for `CROSS`, `REACH_GROUP`, `WITHDRAW`;
- adapter/playback — BLOCKING for traffic, juvenile/group projection and objective state;
- environment family only if the road itself has an exact validated tactical effect.

Reduced version resolves traffic closure and crossing in overworld state and uses AutoPTU only for a separate static conflict.

### Colony Monitoring After Storm — FULL

Required:
- targeting/LoS — VERIFIED if combat occurs;
- base movement — VERIFIED;
- complete movement — BLOCKING for technicians/wildlife moving between protected points;
- environment family — BLOCKING if debris, water, fragile ground or dynamic exclusion zones are tactical;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version uses fixed safe survey points and resolves equipment/site state outside combat.

### Dependency Assessment

No battle dependency. It belongs to world-state observation, Research Ethics, Photography, Science and this new nesting layer. It may legitimately remain unresolved.

## Narrow reaction evidence does not promote the family

The Perception slice at Java head is important: it uses server-owned state, optional decisions, authoritative movement and hit cancellation. It still does not prove:
- generic reaction discovery/dispatch for all effects;
- nest-defense reactions;
- parental interrupts;
- interception;
- Push/Pull execution;
- knockback/collision;
- movement-triggered hazards;
- AI capable of deciding ecological withdrawal/protection objectives.

Pass 146 therefore does not use Perception or Telepathy as a shortcut for parental-care encounters.

## Wild nesting implementation blockers outside battle core

`WILD_REPRODUCTIVE_SITE_STATE`
Persistent site identity and revisions.

`NESTING_EPISODE_STATE`
Season/episode history independent of loaded entities.

`EGG_YOUNG_OBSERVATION_LEDGER`
Counts, individual IDs when justified, uncertainty and observation method.

`PARENTAL_CARE_OBSERVATION_STATE`
Observed provisioning/shelter/guarding without automatic parentage.

`DEPENDENCY_AND_POST_NATAL_STATE`
Nest departure, dependency and post-natal habitat kept distinct.

`NATAL_DISPERSAL_STATE`
Movement from natal site without conflating it with seasonal Migration.

`MONITORING_EFFORT_AND_DISTURBANCE`
Camera/direct-survey effort and observer effects.

`WILD_EGG_TO_CUSTODY_HANDOFF`
Explicit Crisis/Ethics/Care -> Breeding/Egg transaction when intervention is justified.

`NESTING_TO_COBBLEMON_PROJECTION`
Visible young/nests must not become census, parentage or spawn truth.

`NESTING_TO_BATTLE_SNAPSHOT`
Protected/excluded ecological state must be frozen before tactical resolution unless the Java core later owns exact mechanics.

## PTU/Caelo unresolved

The exposed project sources confirm that the existing narrative Breeding/Egg layer must defer offspring species, inheritance, Egg Moves, hatch timing and related effects to authoritative PTU/Caelo mechanics.

This pass did not recover a reliable Caelo-specific source defining wild nesting, parental-care mechanics, juvenile independence or natal dispersal. Super PTU Online Helper was not exposed as an invocable capability. No output was invented for either source.

Do not add until verified:
- parentage mechanics from observation;
- Egg pickup/capture rules;
- nest-defense bonuses;
- juvenile combat penalties;
- parental reaction interrupts;
- species-wide abandonment timers;
- wild hatch timers;
- custody/ownership through rescue;
- spawn modifiers from nest blocks or player-built habitat.
