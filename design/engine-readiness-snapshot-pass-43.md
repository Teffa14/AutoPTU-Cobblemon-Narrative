# Engine Readiness Snapshot — Pass 43

Status: implementation evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only from this repository.

Inspected AutoPTU-Java head: `6eef56913a0727e997bad39b961e2b03d8085d76`

Inspected Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

## Why this snapshot exists

Narrative content must not treat one working representative mechanic as proof that an entire subsystem is implemented.

The permanent capability families remain the project boundary for encounter design.

## Current capability map

### VERIFIED

These families have broad enough direct evidence to support their currently defined basic contracts.

- targeting / footprints / range / line of sight
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

Important limits still apply. `base movement legality` does not mean complete movement. `AI legal-action infrastructure` does not mean tactical decision quality.

### PARTIAL

These families have meaningful implementation slices and parity evidence, but remain incomplete.

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING for concepts that require the full family

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / broad reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## New live evidence since Pass 42

AutoPTU-Java commit `6eef56913a0727e997bad39b961e2b03d8085d76` centralizes authoritative combat-stage mutation.

The slice adds:

- `CombatStageMutationResult`;
- an authoritative `CombatStageMutationService`;
- clamped base mutation before post-apply reactions;
- canonical lookup of attacker and target state;
- reaction execution through the combat-stage hook registry;
- explicit retention of starting, requested, base-applied, base and final stage values;
- tests for Simple reacting to the actual applied delta;
- oracle contracts showing recursive stage-changing mechanics such as Defiant/Competitive exist in Python and are expected to re-enter the authoritative stage pipeline.

This is strong evidence for the combat-stage mutation boundary and for one class of ability-triggered reaction.

It does not prove:

- every Ability that reacts to stage changes;
- every Trainer Feature that modifies stages;
- all Move effects that raise/lower stages;
- complete general reaction handling;
- forced movement reactions;
- attacks of opportunity;
- hazard reactions;
- weather reactions;
- zone-control reactions.

Therefore no permanent capability family is promoted in Pass 43.

## Java README evidence

The current AutoPTU-Java README still marks these large areas incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The README explicitly states that Minecraft/Cobblemon/Craftics should consume the Java core rather than own PTU rules.

## Python head evidence

The newest Python AutoPTU commits inspected in this pass are Career-layer changes. They do not change the tactical capability classification used by this repository.

Python remains the rules oracle while the Java port is incomplete.

## Pass 43 encounter dependencies

### Lost Survey Marker

Reduced version can run before full tactical support because surveying, route correction and equipment state remain in the overworld.

For the intended full version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/forced movement: BLOCKING if unstable slopes cause displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected combatants require it
- terrain/weather/hazards/zones/reactions: BLOCKING if unstable terrain has mechanical effects
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for equipment-avoidance/protection behavior
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

### Cave Traverse Mapping

Reduced version can use overworld mapping plus a static battle chamber.

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING when ledges, rescue repositioning, push/pull or interception matter
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- full stateful damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for unstable cave mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for route/escape goals
- Minecraft/Cobblemon/Craftics playback: BLOCKING

### Moving Front Survey

Reduced version keeps ecological movement and survey resolution outside battle.

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING for corridor and withdrawal objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- full stateful damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when seasonal conditions alter tactical legality
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for non-KO movement objectives
- Minecraft/Cobblemon/Craftics playback: BLOCKING

## Cartography-specific implementation conclusion

Most of Pass 43 does not require AutoPTU.

The following can be built as narrative/world-state features before the tactical port is complete:

- versioned map artifacts;
- map editions;
- spatial knowledge state;
- per-player discovery state;
- route traces;
- landmark records;
- map corrections;
- player annotations;
- shared/redacted map layers;
- historical maps;
- ecological map overlays;
- crisis map overlays;
- map provenance and archive integration.

The tactical engine becomes relevant only when mapping objectives are embedded inside a battle.

Minecraft integration remains necessary for the final presentation of per-player markers, physical signs, map walls, discovered POIs and private/shared annotation scopes.

## No-inference rules for future passes

- One combat-stage mutation service does not make all reactions complete.
- Simple parity does not make Abilities complete.
- Link Features and Defense Mastery do not make Trainer Features complete.
- basic Swim/Sky/Overland legality does not make full overworld navigation complete.
- battle LoS does not make overworld scouting or survey visibility complete.
- a static tactical map does not imply Minecraft can synchronize persistent world geometry.
- a map/UI feature in Minecraft must never become the authority for PTU movement or combat legality.
