# Engine Readiness Snapshot — Pass 148

Status: ENGINE EVIDENCE SNAPSHOT. This file records live read-only evidence observed during Pass 148 and the capability dependencies of the boss-dramaturgy encounters. It does not modify AutoPTU-Java or AutoPTU and does not promote a capability from one representative mechanic.

Date: 2026-08-30

## Repositories inspected

### AutoPTU-Java — read only

Observed `main` head:

`6b7a8b111f567bce39102606ff494fdc3dd57c15`

Commit:

`Internalize Intercept check input at spatial boundary (#286)`

The live commit moves Intercept check materialization further inside the server-owned spatial boundary. The runtime receives candidate identity, canonical combatant rule content and an already-resolved legal intercept position, then constructs the PTU check input from authoritative state. Tests cover the server-owned boundary and deterministic spatial-failure fixtures.

The same patch states that successful melee Intercepts reuse the shared forced-movement application for Push 1, collisions and partial stops. That is useful localized evidence for Intercept and shared forced-movement ownership.

It still does not verify the entire permanent family `complete movement including push/pull/knockback/interception/forced movement`. In particular, this commit does not prove every Push/Pull/Knockback source, arbitrary collision cases, escort movement, carried objects, moving platforms, generalized reaction ordering or environmental forced movement.

No capability family is promoted from this commit alone.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit keeps cached Pixi screen dimensions synchronized after viewport resize. Its commit message explicitly identifies the change as presentation-only and states that battle rules and outcomes do not change.

It does not establish Minecraft/Cobblemon/Craftics as battle authority and does not verify the full adapter/playback family.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category changes during Pass 148.

## Boss-specific readiness rule

A narrative phase is not evidence of a runtime phase.

Until exact lifecycle, state carryover and adapter contracts are verified, rich multi-phase bosses should compile to separate BattleSpecs with Ouros state transitions between them. HP, status, initiative, temporary terrain, reaction resources, move-use state, item consumption and Trainer Feature/perk state must not carry between BattleSpecs unless the engine explicitly serializes and restores them.

A static telegraph may be presentation-only. A telegraph that grants an interrupt, dodge, reaction window, changing safe zone or delayed effect depends on `terrain/weather/hazards/zones/reactions` and potentially lifecycle/forced movement as well.

## Encounter dependency matrix

### The Bell Beneath the Quarry — full version

Narrative purpose: survive a territorial confrontation long enough to create a separate window for investigating or disabling a resonant stimulus.

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary targeting, pulse-area geometry if supported separately |
| base movement legality | VERIFIED | ordinary movement through quarry geometry |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | resonance displacement, collision/partial stops |
| core calculations | VERIFIED | ordinary PTU calculations |
| action economy/initiative | VERIFIED | ordinary action structure |
| full turn/round lifecycle | PARTIAL | timed pulse/opening transitions |
| full stateful damage pipeline | PARTIAL | persistent boss combat state |
| status lifecycle | PARTIAL | exact move/status interactions |
| terrain/weather/hazards/zones/reactions | BLOCKING | pulse lanes, temporary unsafe areas, reaction windows |
| move-specific behavior | PARTIAL | exact selected move semantics |
| abilities | PARTIAL | exact selected ability semantics |
| items | PARTIAL | battle items if allowed; apparatus is not a generic battle item |
| Trainer Features/perks | PARTIAL | any feature-driven interrupts or modifiers |
| AI legal-action infrastructure | VERIFIED | legal-choice generation |
| AI tactical policy | BLOCKING | coordinated use of openings/space |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | dynamic arena/playback path incomplete |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- workers and neutral Pokémon leave BattleSpec;
- resonant apparatus is static, invulnerable and noninteractive;
- no pulse zones, reactions or environmental forced movement exist tactically;
- explicit combatants and fixed geometry only;
- AutoPTU may establish `IMMEDIATE_QUARRY_PERIMETER_CLEAR` or a reviewed narrow combat result;
- Ouros may then evaluate whether that result creates `CALMING_WINDOW_CREATED` and handle the apparatus separately.

### The Floodgate Sentinel — full version

Narrative purpose: create physical access to a floodgate while water pressure and a territorial actor change the approach.

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | targeting and spatial checks |
| base movement legality | VERIFIED | ordinary gate-approach movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | channel-edge displacement and rescue/interception |
| core calculations | VERIFIED | ordinary calculations |
| action economy/initiative | VERIFIED | ordinary actions/initiative |
| full turn/round lifecycle | PARTIAL | water-state transitions and timed access windows |
| full stateful damage pipeline | PARTIAL | persistent combat damage |
| status lifecycle | PARTIAL | exact conditions |
| terrain/weather/hazards/zones/reactions | BLOCKING | changing water tiles, hazards, reactive safe areas |
| move-specific behavior | PARTIAL | exact move behavior |
| abilities | PARTIAL | exact ability behavior |
| items | PARTIAL | battle items only |
| Trainer Features/perks | PARTIAL | feature interrupts/modifiers |
| AI legal-action infrastructure | VERIFIED | legal choices |
| AI tactical policy | BLOCKING | positioning around channels/objective |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | changing water/authoritative playback incomplete |

Full version: BLOCKED.

Reduced version: READY.

- gate operator, civilians and semantic infrastructure objects leave BattleSpec;
- Ouros selects one fixed pre-battle water state;
- static blocked geometry represents inaccessible space;
- battle success may establish only `IMMEDIATE_FLOODGATE_APPROACH_CLEAR`;
- crisis/water/utility owners decide gate operation and downstream consequences after combat.

### The Last Carriage — full version

Narrative purpose: confront a major actor around a departing rail vehicle without letting vehicle presentation become PTU authority.

Critical requirements:

- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for carriage boundaries/reactions if dynamic;
- move-specific behavior, abilities, items and Trainer Features/perks — PARTIAL as used;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING;
- moving-platform/vehicle coordinate semantics require an additional reviewed contract and are not inferred from entity motion.

Full version: BLOCKED.

Reduced version: READY.

The train is stopped before BattleSpec. Carriages are static scenery/blockers. Combatants are explicit. Success may establish only `IMMEDIATE_RAILYARD_ROUTE_CLEAR`, `TACTICAL_DEFEAT_CONFIRMED` or another narrow reviewed result. Ouros decides later escape/departure facts.

### The Machine Around the Pokémon — full version

Narrative purpose: separate the Pokémon as actor from an apparatus that may be influencing the confrontation.

Critical requirements:

- full stateful damage pipeline — PARTIAL if apparatus can be damaged;
- full turn/round lifecycle — PARTIAL for timed openings;
- terrain/weather/hazards/zones/reactions — BLOCKING for arena effects;
- move-specific behavior/abilities/items/Trainer Features as used — PARTIAL;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING;
- destructible-object HP/targeting/consequence semantics remain unverified as a generic boss-object contract.

Full version: BLOCKED.

Reduced version: READY.

The machine is non-targetable static scenery. Ouros resolves any pre-battle disablement before generating BattleSpec. AutoPTU resolves only explicit combatants. A reviewed tactical result may create `INTERRUPTION_WINDOW_CREATED`; world systems decide what happens to the machine afterward.

### The Champion Who Won't Finish the Match — full version

Narrative purpose: make a recurring opponent capable of deliberate disengagement or objective-first play.

Core geometry and legality families are usable, but intelligent disengagement/target prioritization depends on `AI tactical policy`, currently BLOCKING. Mid-combat retreat also needs complete movement and encounter-end semantics beyond merely legal base movement.

Full version: BLOCKED for autonomous tactical personality.

Reduced version: READY.

Run an ordinary authoritative battle using legal-action infrastructure. A post-battle authored transition may record withdrawal only from an allowed narrow result. The opponent's future preparation is world-authored between BattleSpecs rather than claimed as learned tactical policy.

## Multi-stage boss reduced contract

A rich boss may be represented as A -> Ouros transition -> B -> Ouros transition -> C.

For each boundary:

- freeze the completed BattleSpec result;
- extract only explicitly allowed combat/world facts;
- discard temporary tactical state unless serialized by a verified contract;
- evaluate the next scene in Ouros;
- construct the next BattleSpec from explicit initial state;
- never ask Minecraft/Cobblemon to infer the transition from animation, entity HP, particles, block changes or despawn.

This structure can preserve boss dramaturgy without pretending that full turn/round lifecycle, terrain phases or adapter playback are complete.

## Rich boss mechanics that remain dependency-sensitive

The following narrative ideas must continue to declare exact families rather than using a generic `boss mechanics` label:

- knockback or pull into arena hazards: complete movement + terrain/hazards/zones/reactions;
- reaction attacks or interrupts: terrain/weather/hazards/zones/reactions and possibly Trainer Features/perks/move-specific behavior;
- weather phase changes: terrain/weather/hazards/zones/reactions + lifecycle;
- delayed effects: lifecycle + relevant move/ability/status family;
- complex status phase: status lifecycle + lifecycle + full damage where damage-over-time matters;
- ability-created terrain: abilities + terrain/weather/hazards/zones/reactions + lifecycle;
- Trainer Feature interrupts: Trainer Features/perks + reaction/lifecycle support;
- scripted reinforcements: lifecycle + action economy/initiative + AI legal actions + tactical policy + playback;
- moving platforms: complete movement + terrain/zones/reactions + adapter/playback;
- destructible boss apparatus: targeting + full stateful damage + lifecycle + object-specific rules + playback.

## PTU / Caelo assumptions kept UNKNOWN

Pass 148 does not invent mechanical support for:

- a universal PTU `Boss` tag;
- universal phase thresholds;
- extra boss turns/actions;
- boss immunity to statuses, capture, forced movement or specific moves;
- generic stagger/break gauges;
- universal enrage rules;
- scripted reinforcements;
- boss-specific damage reduction;
- generic destructible-object HP/Armor/DR;
- universal non-KO objective mechanics;
- generic tactical retreat thresholds;
- cross-BattleSpec HP/status/initiative carryover;
- dynamic weather/terrain phase transitions;
- automatic Trainer Feature boss interactions;
- automatic species/Type/Ability-based boss authority;
- a generic Skill Check that calms, contains or interrupts any boss;
- battle victory as automatic capture, trust, crisis resolution or faction defeat.

## Adapter boundary

Minecraft/Cobblemon/Craftics may present a boss that Ouros has already selected and parameterized. It may display arena geometry, models, animations, particles, sound cues, damage presentation, phase-themed scenery and post-battle world changes that were already decided authoritatively.

It must not choose combatants, decide whether a boss phase begins, infer PTU HP/status from Minecraft entity state, apply collision damage from Minecraft physics, generate tactical reinforcements, choose legal targets, decide retreat legality or author the world consequence of a battle.

Cobblemon BattleState remains outside Ouros battle-state authority.

## Readiness conclusion

Pass 148 adds no new permanent capability promotion.

All proposed rich boss examples remain blocked where they require dynamic terrain/zones/reactions, tactical AI or adapter/playback. The reduced versions are READY because they remove those mechanics from BattleSpec, keep semantic actors and objectives outside tactical state where necessary, and use explicit static combat followed by Ouros-owned consequence transitions.

The current Java Intercept work is meaningful evidence that server ownership of one complicated reaction/movement path is improving. It remains localized evidence inside a broader PARTIAL movement family and does not justify treating phase bosses, moving hazards or generalized reactions as implemented.
