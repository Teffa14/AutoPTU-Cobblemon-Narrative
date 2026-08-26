# Engine Readiness Snapshot — Pass 179

Status: ENGINE EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-26
Narrative scope: Pokémon courtship, mate choice and pair formation

## Read-only engine heads inspected

AutoPTU-Java head inspected:

`38eb8966ecdc2295cabff932ad1f09d3e82ed6f5`

Latest inspected slice:

`Freeze effective Accuracy and Evasion stage projection (#216)`

That slice freezes how the pinned Python oracle projects effective Accuracy and Evasion state through calculations. It is evidence for a narrow Combat Stage/calculation contract. It does not add courtship behavior, mate-choice AI, wild social policy, relationship state, breeding resolution or Minecraft playback.

AutoPTU Python head inspected:

`218f272e73acf54e0feb5ac2e8f304d53c0fb3c2`

Latest inspected change is Career validation work and does not change battle-readiness conclusions.

Python still exposes an `Infatuated` volatile-status path. The inspected `StatusController` includes handling for an Infatuated status skip under a Trainer Feature exception. That proves Infatuation is a real rules/battle concept in the oracle. It does not make ecological courtship equivalent to Infatuation.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

Evidence remains consistent with the current AutoPTU-Java README and recent parity work.

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

Recent Java progress through Combat Stage mutation/projection and Move Special work is real but narrow. One representative Ability, Status path, secondary effect or stage mutation does not promote an entire family.

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions as a complete family
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

AutoPTU-Java README continues to list forced movement, reactions, terrain, hazards, remaining hook registries, tactical AI and Craftics/Cobblemon integration as unfinished.

## Pass 179 mechanics boundary

Courtship, pair formation and mate choice are narrative/world-state systems.

They must not be implemented by reusing battle mechanics with similar names.

Explicit prohibitions:

`courtship -> Infatuated`

`display -> Attract`

`visual preference -> Accuracy/Evasion stage`

`scent display -> lure roll`

`pair association -> shared initiative`

`pair association -> Pack Mon`

`pair separation -> Loyalty penalty`

`display-site crossing -> Intercept trigger`

`reproductive association -> capture bonus`

`Minecraft heart particles -> PTU breeding transaction`

## Encounter dependency matrix

### Display-Site Crowd Evacuation — FULL

Targeting / footprints / range / LoS: VERIFIED.

Base movement legality: VERIFIED.

Complete movement: BLOCKING. Dynamic civilian evacuation, non-hostile wild withdrawal and interception-aware crossing require more than ordinary Shift legality.

Core calculations: VERIFIED for ordinary battle calculations used by a separate confrontation.

Action economy / initiative: VERIFIED.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL if any exact Status mechanic is invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING if shoreline, darkness, crowd buffers or other environmental state changes tactical legality/effects.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING. The scene requires non-KO objectives such as `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `AVOID_WILDLIFE` and `PROTECT_VISITOR`.

Minecraft / Cobblemon / Craftics adapter/playback: BLOCKING.

REDUCED contract:

Public Space and Conservation evacuate visitors and allow wild Pokémon to withdraw in world state before battle. AutoPTU receives only a static legal arena and real combatants. The courtship episode records interruption independently of the battle result.

### Courtship-Site Restoration Survey — FULL

Targeting / footprints / range / LoS: VERIFIED for a conventional confrontation.

Base movement legality: VERIFIED.

Complete movement: BLOCKING for mobile researchers, crossing and voluntary withdrawal.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Lifecycle / damage / Status / Move / Ability / Item / Trainer Feature families: PARTIAL when invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING if water, mud, vegetation, visibility or protected cells become tactical mechanics.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `REACH_OBSERVATION_POINT`, `WITHDRAW`, `PROTECT_RESEARCHER` and non-hostile wildlife behavior.

Adapter/playback: BLOCKING.

REDUCED contract:

Pause observation before combat, remove researchers, resolve wildlife position and site use in world state, freeze geometry, then run a static battle only if an independent threat remains. Victory cannot make the Pokémon adopt the restored court.

### Pair-Separation During Migration Stopover — FULL

Targeting / footprints / range / LoS: VERIFIED.

Base movement legality: VERIFIED.

Complete movement: BLOCKING because participants may independently cross, withdraw, rejoin or leave while tactical actors are present.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Lifecycle, damage, Status, Move, Ability, Item and Trainer Feature families: PARTIAL when used.

Terrain / weather / hazards / zones / reactions: BLOCKING when storm, current, debris or other stopover conditions have tactical effects.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `CROSS`, `WITHDRAW`, `REJOIN_GROUP`, `AVOID_CONFLICT` or persistent non-hostile objectives.

Adapter/playback: BLOCKING.

REDUCED contract:

Migration resolves arrivals, departures and temporary separation before a battle snapshot exists. Courtship state records only what was observed. Any unrelated confrontation runs separately.

### What Was the Display For? — NON-COMBAT

No battle-engine capability is required.

This investigation consumes evidence from Photography, Soundscapes, Passive Acoustics, Olfactory Landscapes, Spatial Ecology, Community Science, Research Ethics and Courtship state.

A PTU Skill may affect what a character can notice or analyze only when the governing PTU/Caelo rule supports that exact use. No generic “correct interpretation” check is invented.

## Attract / Infatuation evidence boundary

Public PTU 1.05 references define Attract and Infatuation as explicit mechanics. The Python runtime includes Infatuated state handling.

Therefore:

- a mechanical Attract use is possible only through authoritative rules execution;
- a mechanical Infatuated state is battle state;
- neither can be inferred from ecology;
- a wild pair can exist without either mechanic ever appearing;
- an Infatuated combatant does not acquire a persistent pair-association record after battle unless independent narrative evidence supports one.

The same boundary applies to Cute Charm, Oblivious, Contest stats and Charm.

## Minecraft adapter boundary

Minecraft/Cobblemon may eventually render:

- visible gatherings at a display site;
- light/sound/scent presentation already authorized by world state;
- approach or withdrawal animations;
- public viewing infrastructure;
- known persistent individuals.

It must not derive:

- pair formation from proximity;
- mating from heart particles;
- preference from pathfinding;
- rejection from despawn;
- parentage from shared spawn location;
- breeding eligibility from Cobblemon species compatibility alone;
- Infatuation from animations;
- display-site success from redstone state.

## Engine changes observed since Pass 178

The newest inspected Java commit is `38eb8966...`, which freezes effective Accuracy and Evasion stage projection against the pinned Python oracle. It follows the earlier seven-Combat-Stage authoritative mutation work.

This improves confidence in a calculation boundary only. No permanent capability category changes status in Pass 179.

The newest inspected Python head `218f272e...` is Career validation work. It does not change the tactical capability map.

## Unresolved mechanical questions

- exact Caelo changes, if any, to Attract, Infatuation, Cute Charm, Oblivious or breeding compatibility;
- whether the final Ouros ruleset permits any non-combat use of Attract-like mechanics;
- whether Charm or Pokémon Education has an authored role in studying courtship without becoming a deterministic mate-choice roll;
- whether any Feature legitimately modifies wild social interactions;
- whether future AI policy will support persistent non-hostile objectives and voluntary withdrawal;
- whether any Minecraft/Cobblemon breeding implementation will exist and, if so, how it hands off to PTU/Caelo authoritative resolution.

## Canon questions

- which Ouros populations have authored courtship displays;
- which display sites exist at campaign start;
- whether any public festivals are already built around them;
- what information is public versus protected;
- which associations between known persistent Pokémon are established canon;
- which signals or displays are culturally interpreted differently by local communities;
- how much seasonal change can advance offline.

No answer above is established by this snapshot.