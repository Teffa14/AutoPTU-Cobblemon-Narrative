# Engine Readiness Snapshot — Pass 68

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.
Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`b705561395b0ae776740e9207b44c1c53856f326`

Latest inspected commit:

`Project authoritative runtime state into Pokemon initiative candidates (#101)`

Canonical URL:

https://github.com/Teffa14/AutoPTU-Java/commit/b705561395b0ae776740e9207b44c1c53856f326

New bounded evidence since Pass 67:

- Java now projects canonical combatant state into Pokémon initiative candidates through `RuntimeInitiativePokemonCandidateFactory`;
- resolved Speed reads status-aware stats from authoritative runtime state;
- selected Weather/Terrain-dependent initiative Ability resolution is consumed as semantic input;
- HP, abilities, temporary effects, active state and Trainer/controller identity are read from server-owned state;
- callers provide semantic context instead of precomputed initiative totals;
- dedicated tests cover the projection boundary.

This further strengthens the already-VERIFIED `action economy / initiative` family and reinforces server authority.

It does not prove:

- complete turn/round lifecycle;
- complete Trainer turns;
- complete status/Ability/Feature timing;
- full damage resolution;
- a battlefield light/darkness model;
- actor-specific visibility;
- darkness-generated Blinded or Accuracy behavior;
- Glow, Darkvision or Blindsense parity;
- terrain/hazard/zone environment execution;
- forced movement/interception;
- tactical AI policy;
- Minecraft/Cobblemon adapter behavior.

A semantic `weather` or `terrainName` input used by initiative calculation is not evidence of a complete environment subsystem.

## Python AutoPTU live evidence

Current inspected Python `main` head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible work remains Career-focused.

No new Python tactical subsystem changed the permanent capability map during this run.

## PTU evidence relevant to Pass 68

Official PTU public design material includes a Gym where:

- Darkvision;
- Blindsense;
- Glow Capability;
- Blinded;
- darkness that increases as torches extinguish

are explicit encounter considerations.

Source:
https://pokemontabletop.com/gym-design-signature-elements/

This proves that exact PTU light/vision mechanics exist in authored contexts.

It does not prove that Java implements them.

The complete primary Caelo source corpus was not reliably retrievable during this run for an exact darkness/visibility extraction. No Caelo-specific modifier is invented here.

## Permanent capability map

| Permanent capability family | Pass 68 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Geometry, targeting, footprints and LoS coverage exist. LoS does not prove low-light perception. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement, interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed flow plus parity-tested ordering, rebuild/advance, atomic install and canonical combatant projection exist. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete Trainer/status/Ability/Feature/reaction/delayed coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Several damage/post-damage slices exist while full damage remains unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Selected semantic consumers do not establish a complete battlefield environment or lighting system. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog does not. |
| Trainer Features / perks | PARTIAL | Infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy for withdraw, protect, avoid-zone, light-seeking/avoidance or interactables remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not own Minecraft projection/playback. |

## Pass 68-specific blockers

`OVERWORLD_LIGHTSCAPE_STATE = BLOCKING`

The server needs persistent coarse illumination state independent of loaded Minecraft block light.

`OVERWORLD_LIGHT_SOURCE_REGISTRY = BLOCKING`

Natural, artificial, biological, beacon and emergency light sources need identity, schedule and provenance.

`OVERWORLD_LIGHT_OBSERVATION_PROVENANCE = BLOCKING`

Light measurements and visual observations need timestamped context.

`OVERWORLD_ARTIFICIAL_LIGHT_ECOLOGY = BLOCKING`

Ecological response to artificial light needs evidence-backed world-state transitions rather than direct spawn multipliers.

`OVERWORLD_BIOLOGICAL_LIGHT_EVENTS = BLOCKING`

Persistent visual displays need observation records without assuming communication meaning or mechanical effect.

`OVERWORLD_NIGHT_ACTIVITY_BASELINES = BLOCKING`

Nocturnal activity needs coarse baseline/history before anomalies can be inferred.

`OVERWORLD_LIGHTING_INFRASTRUCTURE = BLOCKING`

Beacons, streetlights, stadium lights and emergency routes need integration with Technology/Public Works and service state.

`OVERWORLD_LIGHT_TO_ASTRONOMY = BLOCKING`

Local sky glow must affect observation feasibility without changing the celestial event itself.

`OVERWORLD_LIGHT_TO_ECOLOGY = BLOCKING`

Lightscape revisions need safe read contracts for wild populations and collectives.

`OVERWORLD_LIGHT_TO_COBBLEMON = BLOCKING`

Minecraft torch/block light must not become a direct encounter/spawn control surface.

`OVERWORLD_LIGHT_TO_BATTLE = BLOCKING`

A validated semantic projection is required before world light becomes PTU visibility, Blinded or another mechanical state.

`OVERWORLD_LIGHT_TO_MINECRAFT = BLOCKING`

Minecraft may render light, darkness, beams and fixture state, but rendered brightness must not become rules authority.

## Critical distinction: LoS versus visibility

`targeting / footprints / range / LoS = VERIFIED`

This means the engine can reason about geometric line of sight.

It does not mean the engine has proved:

- vision range in darkness;
- actor-specific perception;
- light-source radius;
- Darkvision;
- Blindsense;
- Glow;
- Blinded from darkness;
- glare;
- fog plus darkness interaction;
- visual stealth.

A future light system must not overload LoS with these meanings.

## Encounter dependency review

### Beacon Failure at North Harbor

Full version:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement / interception / forced movement — BLOCKING when active harbor lanes or protected movement matter
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- lifecycle — PARTIAL
- damage pipeline — PARTIAL
- statuses — PARTIAL if any exact condition is used
- terrain / weather / hazards / zones / reactions — BLOCKING for darkness/fog/light mechanics
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Reduced version:

Resolve beacon state, harbor closure and noncombatant movement before battle. Freeze one static dock arena. Keep night as presentation only. Apply no Accuracy, Blinded, stealth or vision modifier from lighting.

### Dark Corridor Survey

Full version:

- static geometry/base movement/core/initiative — VERIFIED
- actor-specific low-light visibility — BLOCKING
- lifecycle/damage/status/Ability/item/Feature behavior — PARTIAL as applicable
- environment zones/reactions — BLOCKING
- tactical AI — BLOCKING for avoid-light/cross-corridor goals
- adapter/playback — BLOCKING

Reduced version:

Run ecological observation in overworld. If combat occurs, open a conventional static encounter with normal readable visibility. Store lightscape data only as research provenance.

### Flickerwood Signals

Full version:

- geometry — VERIFIED
- base movement — VERIFIED
- dynamic mechanical darkness / Glow / Darkvision / Blindsense — BLOCKING pending rules extraction and implementation
- lifecycle — PARTIAL if signals change during combat
- status — PARTIAL only where an exact Move/Ability applies one
- tactical AI — BLOCKING for lure/withdraw/investigate goals
- adapter/playback — BLOCKING

Reduced version:

Observe light displays before or after combat. If confrontation occurs, use a static arena and standard battle visibility. Biological glow causes no automatic Sleep, attraction, Accuracy changes or Blinded.

## Pass 68 rule cautions

Do not infer or invent:

- Minecraft light level as PTU vision range;
- automatic Blinded in a dark-looking scene;
- generic darkness Accuracy penalties;
- stealth bonuses from darkness;
- Darkvision from nocturnal species lore;
- Glow from Pokédex flavor unless authoritative PTU state has it;
- Illuminate as a universal overworld flashlight;
- Flash as a generic exploration mechanic without source validation;
- light pollution as a direct spawn multiplier;
- all nocturnal species being attracted to darkness;
- all predators benefiting from artificial light;
- Fire/Electric Pokémon automatically supplying institutional lighting;
- lighthouse Pokémon automatically obeying service commands;
- fog plus darkness penalties without exact rules;
- Moon phase combat bonuses;
- visual darkness hiding required accessibility information.

## Pass 68 conclusion

The latest Java commit improves authoritative projection into initiative. It strengthens a family already marked VERIFIED and does not materially change the blockers relevant to dynamic light/darkness encounters.

Lightscape worldbuilding can advance safely now through persistent source state, infrastructure, observations, ecological hypotheses, dark-sky management, biological light records and reduced static encounters.

Mechanically dynamic darkness remains gated behind exact PTU/Caelo rules plus environment/visibility execution, lifecycle where state changes over time, tactical AI and Minecraft adapter/playback.
