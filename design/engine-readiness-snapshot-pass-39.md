# Engine Readiness Snapshot — Pass 39

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `d49e11fc6558386c55ecf6b40993f5fc1c9ebfcd`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

## New Java evidence since Pass 38

The new Java head adds a parity-safe, phase-scoped Trainer Feature/perk registry.

The commit adds:
- a phase-scoped `PerkPhaseEffect` contract;
- an ordered authoritative `PerkPhaseEffectRegistry`;
- filtering against a Trainer Feature projection;
- global phase hooks;
- lifecycle bridging through `PerkPhaseLifecycleHook`;
- Python-oracle fixture extraction for generic perk registry behavior;
- CI parity checks for the registry contract.

The commit also explicitly states that the Trainer Feature collection is an explicit projection for this bounded slice and that the next integration step is binding it to canonical `BattleRuntimeState`.

This is stronger evidence than Pass 38, where Trainer Features/perks had ordering slots but no dedicated parity-safe registry.

It still does not prove concrete Trainer Feature coverage.

No-inference rules:
- a generic perk registry does not prove any specific Trainer Feature effect is implemented;
- oracle detection of `Defense Mastery` or `Stat Mastery` registration does not prove their full Java mechanical behavior;
- lifecycle bridging does not prove the Trainer Feature projection is canonical runtime state;
- phase-scoped support does not prove non-phase triggers, interrupts, reactions, orders or passive calculations;
- one registry contract does not prove the complete Trainer Feature/perk family.

## Python evidence

The Python head remains `e4bb0ca38b7018710af476ce365d515a387de4e7` in this snapshot.

Its latest repository commits are Career/API-oriented and do not justify changing tactical capability families.

Python remains the authoritative oracle while the Java port is incomplete.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

Caveats:
- verified base movement does not include push/pull/knockback/interception/forced movement;
- core calculation primitives do not equal the full stateful damage pipeline;
- legal-action enumeration does not imply tactical policy quality;
- battle LoS does not establish overworld perception or race-course visibility systems.

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

#### Lifecycle

Lifecycle remains PARTIAL. Java now has typed phases, default STATUS/ABILITY dispatch, delayed-hit infrastructure, histories, status metadata and phase-scoped perk infrastructure. Full BattleSpec -> BattleTranscript coverage, every phase trigger, delayed execution, complete cleanup and family interaction coverage are not complete.

#### Damage

The stateful damage pipeline remains PARTIAL. Calculation primitives and bounded runtime slices exist, but the repository README still lists full damage resolution as unfinished.

#### Status

Status remains PARTIAL. Existing evidence covers bounded Flinch, Confusion/Strange Tempo, metadata, application prevention, ordered phase registries and lifecycle integration. It does not establish the complete status catalog and interactions.

#### Move-specific behavior

Move-specific behavior remains PARTIAL. Generic targeting and move infrastructure do not prove each special-case Move.

#### Abilities

Abilities remain PARTIAL. Representative Ability hooks and ordered phase behavior exist. The complete Ability catalog is not ported.

#### Items

Items remain PARTIAL based on prior representative held-item slices. No new evidence promotes this family.

#### Trainer Features/perks

Trainer Features/perks move from BLOCKING-family to PARTIAL-family in this snapshot because there is now direct Java implementation evidence for an ordered, phase-scoped registry with Python-oracle parity and lifecycle bridging.

This promotion is narrow.

Concrete narrative encounters must still treat a required Trainer Feature as BLOCKING unless that exact Feature behavior is implemented and parity-tested.

The following remain unproven:
- canonical Trainer Feature state binding in `BattleRuntimeState`;
- concrete `Defense Mastery` behavior;
- concrete `Stat Mastery` behavior;
- Orders;
- interrupts;
- reaction-triggered Features;
- non-phase passive effects;
- Trainer Features that modify movement, targeting, damage, status or Items;
- complete Trainer Feature catalog coverage.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

These remain blocking for any full encounter version that depends on them.

## Pass 39 sports/racing boundary

Narrative athletic state can advance without tactical race simulation.

Safe world-state concepts today:
- sport definitions;
- clubs and athletic institutions;
- event schedules;
- course versions;
- registrations;
- practice history;
- records and record provenance;
- public reception;
- athlete careers;
- route closures and rescheduling;
- club rivalries;
- course scouting;
- volunteer/organizer roles.

Mechanics that require explicit PTU/Caelo and/or engine support:
- race DCs;
- opposed race resolution;
- mount eligibility;
- movement speed conversion into race timing;
- fatigue meters;
- collisions;
- drafting;
- legal interference;
- knockback/contact sport;
- tactical checkpoint objectives;
- course hazards;
- live autonomous racers;
- dynamic weather effects;
- objective-aware AI;
- sport-specific Trainer Features;
- Minecraft race playback.

## Race no-inference rules

### Movement

Verified Shift movement is sufficient evidence that Java can reason about basic legal movement in a tactical grid.

It is not evidence for:
- a complete race simulator;
- simultaneous racers;
- overtaking rules;
- collisions;
- drafting;
- checkpoint objectives;
- path-planning policy;
- mount/passenger synchronization;
- arbitrary overworld speed.

### Mounts

Public PTU material confirms mounted play and Rider mechanics exist.

Do not infer that Java currently implements:
- `Mountable` legality;
- saddles;
- rider/mount combined state;
- mounted Skills;
- Rider Features;
- passenger position;
- mounted race collision.

These require exact source extraction plus implementation evidence.

### Trainer Features

Pass 39 promotes the broad category to PARTIAL because of the new registry infrastructure.

A sports encounter cannot use an Athlete, Rider, Tumbler or other Trainer Feature effect mechanically until the exact Feature is ported and parity-tested.

Narrative labels such as `coach`, `rider`, `athlete` or `racer` do not grant those Features.

## Pass 39 encounter dependencies

### Switchback Relay

FULL version:
- targeting/footprints/range/LoS — VERIFIED only if target selection is used
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING for contact/overtaking interactions
- core calculations — VERIFIED foundations
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if a legal combat incident occurs
- status lifecycle — PARTIAL if relevant
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL if Moves are permitted
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL family; exact required Feature still BLOCKING unless implemented
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Resolve the race using validated PTU/Caelo Skill checks and world-state timing outside AutoPTU. Open a normal tactical encounter only for a separate legal battle incident.

### Breakwater Dash

FULL version:
- base movement legality — VERIFIED
- complete movement — BLOCKING for collision/interception-rich behavior
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING for mechanical waterfront conditions
- move-specific behavior / abilities / items — PARTIAL when explicitly allowed
- Trainer Features/perks — PARTIAL family but exact effects require proof
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

REDUCED version:
Keep the route and event in overworld state. Use legal Skill checks or authored non-combat resolution. No custom tactical water, collision or timer rules.

### Course Emergency

FULL version:
- complete movement — BLOCKING
- full lifecycle — PARTIAL
- hazards/zones/reactions — BLOCKING
- Trainer Features/perks — PARTIAL family; rescue-specific Features unverified
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

REDUCED version:
Suspend the sporting event. Resolve the emergency through crisis/rescue world state and any conventional static battle that is independently legal. Amend or resume the official event afterward.

## README evidence boundary

The current AutoPTU-Java README still lists these large areas as unfinished:
- core combatant/grid battle state;
- full damage pipeline;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The new perk-registry commit should therefore be treated as bounded progress inside one unfinished family, not completion of that family.

## Conclusion

Pass 39 can safely establish athletic institutions, events, course history, records, practice, public culture and non-combat careers in Ouros now.

Full tactical racing remains beyond current verified engine scope.

The Java head provides enough new direct evidence to move the broad Trainer Features/perks category to PARTIAL infrastructure, but every concrete Feature remains opt-in only after exact parity-backed implementation. The most important blockers for rich sports encounters remain complete movement/interception, terrain/weather/hazards/reactions, tactical AI and Minecraft playback.
