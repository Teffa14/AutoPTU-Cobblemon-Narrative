# Engine Readiness Snapshot — Pass 31

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination

## Live Java head inspected

AutoPTU-Java head during this pass:

`5576e433b7b2f9e87fad7c669bd008b992b9bb62`

Commit:
`Add reusable status phase effect registry (#57)`

The commit adds bounded status/lifecycle infrastructure:

- a reusable phase-scoped status effect contract;
- an ordered canonical status phase registry;
- matching against server-owned normalized statuses;
- explicit execution order;
- pending status-skip propagation where the last request wins;
- lifecycle hook integration;
- tests for canonical aliases and registration order.

This is meaningful progress for status/lifecycle architecture.

It does not establish:

- complete status coverage;
- every status trigger and cure rule;
- full status durations;
- all status interactions with Moves/Abilities/Items/Trainer Features;
- reactions;
- terrain/hazard status interactions;
- objective-aware AI;
- Minecraft playback.

A reusable registry is infrastructure. It is not proof that the whole status family has been ported.

## Java README evidence

The current AutoPTU-Java README still states that Python AutoPTU is authoritative while the Java port is incomplete.

Its unfinished families still include:

- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript semantic parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Live Python head inspected

AutoPTU head during this pass:

`4182310d0d5d3b9e320fed681940164ab489dd8b`

Commit:
`Career: harden automatic training across retirements`

The latest observed Python changes concern the Career/UI automatic-training path and retirement-safe candidate selection.

They do not establish new tactical Java capability.

Python remains the source oracle, but Python behavior is not equivalent to Java or Minecraft implementation readiness.

## Permanent capability classification

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

### BLOCKING for mechanically rich encounter design

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Delta from Pass 30

The Java head advanced from:

`957e7eaa0ce056b8fc6f2f66aba7f24440c2c2be`

through pending-status overwrite parity to:

`5576e433b7b2f9e87fad7c669bd008b992b9bb62`.

The new evidence strengthens:

- full turn/round lifecycle: still PARTIAL;
- status lifecycle: still PARTIAL.

Neither category is promoted to VERIFIED because representative infrastructure and registry tests do not establish full family coverage.

No evidence from these commits upgrades:

- full damage pipeline;
- complete movement;
- terrain/weather/hazards/zones/reactions;
- Move coverage;
- Ability coverage;
- Item coverage;
- Trainer Features/perks;
- tactical AI;
- Minecraft playback.

## Pass-31 relevance

The education/academy layer is mostly persistent world and institutional state.

Safe implementation-independent work:

- institutions;
- programs;
- enrollment;
- curricula;
- module dependencies;
- attendance;
- instruction events;
- practicum records;
- competency evidence;
- assessment records;
- field placements;
- supervision levels;
- exchange/transfer state;
- academic-record privacy;
- instructor schedules;
- alumni history.

Those systems should not use battle-turn lifecycle as an overworld academic clock.

## Encounter dependency table

### Field Practicum: Ravine Survey

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if tactical rescue/interception is used
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if environmental danger affects the grid
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when required
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Survey, supervision and hazard state remain in the overworld. Any battle uses a static legal arena. The institution evaluates the field report and authoritative battle result separately.

### Aptitude Battle Workshop

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: only required if the assessment specifically depends on currently unsupported forced/interception movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when used by the assessment
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when used
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:

Use a bounded legal battle that avoids unsupported families. Assessment may reference only observed transcript facts and explicitly authored rubric criteria.

### Emergency Drill: Clear the Exit

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- stateful damage/status/move/ability/item families: PARTIAL when relied upon
- terrain/weather/hazards/zones/reactions: BLOCKING
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- ESCAPE/PROTECT/CLEAR_ZONE objective semantics: not verified

Reduced version:

The evacuation drill resolves outside battle state. A conventional static encounter can block the final route, after which world state records factual response and supervision outcomes.

## Assessment boundary

An AutoPTU transcript can eventually provide evidence that a battle occurred and what legal actions/results were emitted.

It does not by itself establish:

- a grade;
- a PTU Skill increase;
- a Feature;
- a Tutor Move;
- a qualification;
- a license;
- a Badge;
- a school rank;
- institutional authority.

Those are separate systems.

## Education versus Python Career training

The Python Career feature currently includes automatic Pokémon training plans.

That UI/gameplay system must not be treated as proof of Ouros academy mechanics or PTU classroom training.

A narrative course cannot call Career training and claim PTU progression unless the projects deliberately establish that integration later.

## Tutoring boundary

Education content may contain instructors, lessons and practice.

Actual Move tutoring remains dependent on authoritative PTU/Caelo tutoring rules and the eventual Java Trainer Feature/perk/Move infrastructure.

Trainer Features/perks remain BLOCKING as a permanent capability category.

## Schedule boundary

Academic calendars are overworld world-state clocks.

They are independent from:

- battle rounds;
- turn phases;
- status phase hooks;
- move frequencies.

Do not reuse combat lifecycle code as academic timing semantics.

## Minecraft boundary

Verified battle systems do not prove:

- persistent class schedules;
- campus access control;
- dorm allocation;
- enrollment UI;
- field-trip instancing;
- student record privacy;
- instructor schedules;
- classroom populations;
- practicum objective tracking;
- exchange-program state;
- offline academic progression.

These remain narrative/world adapter requirements.

## No-inference rules for Pass 31

- Enrollment does not grant a Trainer Class.
- Passing a course does not grant a Skill Rank.
- Attending Battle Studies does not grant combat bonuses.
- A practical battle does not automatically qualify someone for field authority.
- An instructor title does not prove a particular PTU Feature.
- A school record is an institutional claim, not universal truth.
- A failed assessment does not imply incompetence, expulsion or humiliation.
- A field placement does not grant the host institution's legal powers.
- A dorm assignment does not define personality or social bonds.
- An exchange student has not permanently transferred unless state says so.
- The latest Java status registry does not upgrade the whole status category to VERIFIED.
- Python Career automatic training does not prove Java/PTU academy progression.