# Engine Readiness Snapshot — Pass 205

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `d7ea892619f831c1c5712e89e8d5a28afb84d5b8`

Read-only engines inspected:
- AutoPTU-Java head: `f320aca406e3da87427eca32ab97943062c264ff`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

No engine head changed since pass 204.

AutoPTU-Java remains at `f320aca406e3da87427eca32ab97943062c264ff` — `Freeze forced-movement ability semantic contract (#324)`.

This continues to strengthen a bounded Ability-family prevention contract. It does not establish complete Push/Pull/Knockback/Interception, collisions, partial stops, chained displacement, footprint interactions, reaction ordering, terrain-mediated displacement or all PTU content combinations.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. Its commit message states the change is presentation-only and does not alter battle rules or outcomes.

No permanent capability category is promoted in pass 205.

## Permanent capability classification

### VERIFIED within currently audited contracts

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

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## PTU death-resolution caution

PTU 1.05 contains explicit Death rules distinct from Fainted/KO state. Public source text states that death in non-friendly combat depends on Injury and extreme negative-HP thresholds, and also notes that campaigns may alter or remove Injury/Death rules.

Repository searches in this run found broad AutoPTU Python use of `fainted`, but did not verify an end-to-end death adjudication contract matching PTU/Caelo authority. A targeted AutoPTU-Java `fainted` search returned no indexed result.

Therefore:

`FAINTED_SUPPORT != DEATH_RESOLUTION_VERIFIED`

Any executable encounter whose narrative outcome depends on a permanent death remains dependent at minimum on:
- full stateful damage pipeline: PARTIAL;
- full turn/round lifecycle: PARTIAL where timing/termination matters;
- status lifecycle: PARTIAL when helpless/fainted/status interactions matter;
- move-specific behavior: PARTIAL;
- abilities/items/Trainer Features as selected content requires;
- authoritative Caelo/PTU death policy, currently unresolved in indexed project sources.

Pass 205 does not authorize Narrative to calculate death independently.

## Caelo search

A literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed source content in this run.

Unresolved:
- whether Caelo keeps or modifies PTU 1.05 death thresholds;
- whether Injury/Death rules are enabled for Ouros;
- any resurrection/resuscitation boundary;
- human/Pokémon remains procedures;
- inheritance or posthumous Pokémon ownership;
- funerary institutions or supernatural doctrine.

No unresolved field is promoted to canon.

## Pass 205 rich encounter

Encounter: `Night Retrieval at the Old Marker`.

Premise:
A memorial object or historical field case has been temporarily secured near a route-maintenance site. A current wild actor blocks immediate safe withdrawal. The object, memorial meaning, death history, custody and public interpretation remain Narrative state outside BattleSpec.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required for protected withdrawal, Interception or displacement
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, route hazards or zones affect tactics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING when the wild actor must prioritize territorial pressure, withdrawal, corridor control or disengagement over KO
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful overworld -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

Narrative retains:
- confirmed memorial/object identity;
- death provenance only if already canon-approved;
- physical location;
- current custody state;
- retrieval purpose;
- noncombatants;
- public/supernatural claims as claims only.

Before combat:
- place noncombatants and semantic objects into safe Narrative state;
- identify one immediate wild obstruction;
- select audited combatants and content;
- use stable geometry;
- omit tactical darkness/weather/hazard mechanics unless independently verified;
- avoid forced-movement objectives unless each selected interaction is contract-verified;
- do not permit the encounter to require a death result.

Allowed handoffs:
- `IMMEDIATE_SITE_APPROACH_CLEAR`
- `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR`
- `IMMEDIATE_WILD_ACTOR_WITHDREW`

Battle output cannot determine:
- spirit identity or afterlife truth;
- death cause;
- ownership/inheritance;
- authority over remains or memorials;
- whether a Ghost is a deceased actor;
- grief resolution;
- public historical interpretation;
- permanent route safety.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## Complete movement caution

Still not verified as one family:
- all Push;
- all Pull;
- all Knockback;
- Interception;
- collisions;
- partial displacement;
- chained displacement;
- footprint interactions;
- reaction ordering;
- terrain-mediated displacement;
- all Move/Ability/Item/Feature/status combinations;
- end-to-end adapter/playback parity.

The current forced-movement semantic contract remains bounded evidence and cannot promote the category.

## Narrative repository writes

Pass 205 writes only to Narrative.

New files:
- `research/2026-09-02-memorial-death-remains-belongings-scan-205.md`
- `design/memorial-death-remains-belongings-continuity-layer.md`
- `proposals/2026-09-02-marea-memorial-death-belongings-seeds-205.md`
- `design/engine-readiness-snapshot-pass-205.md`

No write to AutoPTU-Java or AutoPTU is authorized or performed.

## Recommended first implementation

Prototype `The Label on the Old Field Case` only after a historical deceased actor is explicitly approved for canon or an existing approved historical death becomes available.

Until then, the design can be tested with fixtures but should not silently create a dead Marea resident.

The slice requires:
- no battle;
- no current resident death;
- no inheritance decision;
- no Ghost metaphysics;
- no new institution;
- no new location;
- no PTU reward;
- no modification to established canon.

Its main invariant is provenance:

`FORMER USER CONFIRMED != CURRENT OWNER PROVEN`.