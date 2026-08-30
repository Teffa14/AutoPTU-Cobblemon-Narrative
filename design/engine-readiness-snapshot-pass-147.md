# Engine Readiness Snapshot — Pass 147

Status: ENGINE EVIDENCE SNAPSHOT. This file records live read-only evidence observed during Pass 147 and the capability dependencies of the adjudication/decision-continuity encounters. It does not modify AutoPTU-Java or AutoPTU and does not promote a capability from one representative mechanic.

Date: 2026-08-30

## Repositories inspected

### AutoPTU-Java — read only

Observed `main` head:

`6b7a8b111f567bce39102606ff494fdc3dd57c15`

Commit:

`Internalize Intercept check input at spatial boundary (#286)`

The commit moves more Intercept check materialization behind the server-owned spatial boundary, adds tests for that boundary, makes spatial failure fixtures deterministic and migrates pre-target fixtures to the server-owned check boundary.

This is meaningful evidence that another rule-critical Intercept input is no longer delegated outward. It strengthens server authority for that localized mechanic.

It does not verify the entire permanent family `complete movement including push/pull/knockback/interception/forced movement`. It also does not establish broad Push/Pull/Knockback, every forced-movement source, escort movement, carried-object semantics, generalized reaction ordering, dynamic zones, hazards, weather lifecycle, terrain lifecycle, Trainer Feature interrupts or tactical AI.

No capability family is promoted from this commit alone.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit synchronizes cached Pixi screen dimensions after viewport resize. Its own commit message identifies the change as presentation-only and states that battle rules and outcomes do not change.

This remains presentation evidence only. It gives no authority to the Minecraft/Cobblemon/Craftics adapter over combatants, legality, HP/status, tactical positions, institutional state or world consequences.

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

No permanent category changes during Pass 147.

## Why complete movement remains PARTIAL

The live Java head internalizes another Intercept check input and adds boundary coverage. That is narrower than the permanent family. A rich encounter that needs pushing a protected actor, pulling a carried record, knockback into a controlled zone, escort movement, multiple reaction windows or arbitrary forced movement still depends on unverified portions of the family.

The reduced encounters below therefore avoid all such semantics.

## Encounter dependency matrix

### Hearing Hall Withdrawal Perimeter — full version

Narrative purpose: protect a physical withdrawal route after a hearing or formal meeting is paused. The hearing state stays outside combat.

Capability requirements:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary targeting and spatial checks |
| base movement legality | VERIFIED | movement through hall/exterior geometry |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | interception and displacement near exits |
| core calculations | VERIFIED | ordinary PTU calculations |
| action economy/initiative | VERIFIED | ordinary action structure |
| full turn/round lifecycle | PARTIAL | timed withdrawal or reinforcement phases |
| full stateful damage pipeline | PARTIAL | persistent combat damage state |
| status lifecycle | PARTIAL | conditions affecting movement and timing |
| terrain/weather/hazards/zones/reactions | BLOCKING | dynamic safe zones, reactive exits or environmental control |
| move-specific behavior | PARTIAL | exact move semantics |
| abilities | PARTIAL | exact ability semantics |
| items | PARTIAL | battle items only; hearing records are not tactical items |
| Trainer Features/perks | PARTIAL | interrupts or special reactions |
| AI legal-action infrastructure | VERIFIED | legal-choice generation |
| AI tactical policy | BLOCKING | coordinated blocking/withdrawal tactics |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative presentation/playback path incomplete |

Reduced version: READY.

Reduction contract:

- proceeding pauses before initiative;
- adjudicators, participants, witnesses, records and neutral actors leave BattleSpec;
- all semantic hearing objects are inaccessible static scenery;
- Ouros chooses explicit combatants;
- AutoPTU receives static geometry;
- success may emit only `IMMEDIATE_HEARING_HALL_WITHDRAWAL_ROUTE_CLEAR`;
- Ouros later decides scheduling, notice, resumption and decision state.

### Decision Archive Handoff Chokepoint — full version

Narrative purpose: protect the physical approach used for an archive handoff. Decision validity and record custody remain separate world-system facts.

Capability requirements:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary geometry |
| base movement legality | VERIFIED | ordinary movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | escort-adjacent movement, displacement, interception |
| core calculations | VERIFIED | ordinary calculations |
| action economy/initiative | VERIFIED | ordinary initiative/actions |
| full turn/round lifecycle | PARTIAL | timed handoff phases |
| full stateful damage pipeline | PARTIAL | persistent combat state |
| status lifecycle | PARTIAL | exact condition behavior |
| terrain/weather/hazards/zones/reactions | BLOCKING | dynamic chokepoints/reactions |
| move-specific behavior | PARTIAL | exact move semantics |
| abilities | PARTIAL | exact ability semantics |
| items | PARTIAL | archive record cannot become a generic held/battle item |
| Trainer Features/perks | PARTIAL | feature interrupts/reactions |
| AI legal-action infrastructure | VERIFIED | legal-choice generation |
| AI tactical policy | BLOCKING | coordinated escort/blocking behavior |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | full authoritative playback unavailable |

Reduced version: READY.

Reduction contract:

- record is secured outside tactical state before initiative;
- custodians and couriers leave BattleSpec;
- explicit combatants fight over a static approach;
- success may emit only `IMMEDIATE_DECISION_ARCHIVE_HANDOFF_APPROACH_CLEAR`;
- record transfer/custody is resolved afterward by Case/Authority, Archives and the decision-continuity layer as applicable.

### Compliance Inspection Access Corridor — full version

Narrative purpose: secure access for a later implementation inspection. Combat never verifies compliance.

Capability requirements:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary targeting/geometry |
| base movement legality | VERIFIED | corridor access |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | escort/interception/displacement if inspectors remain tactical |
| core calculations | VERIFIED | ordinary calculations |
| action economy/initiative | VERIFIED | ordinary initiative/actions |
| full turn/round lifecycle | PARTIAL | timed inspection windows |
| full stateful damage pipeline | PARTIAL | persistent combat damage |
| status lifecycle | PARTIAL | exact status semantics |
| terrain/weather/hazards/zones/reactions | BLOCKING | dynamic site hazards/zones/reactions |
| move-specific behavior | PARTIAL | exact move behavior |
| abilities | PARTIAL | exact ability behavior |
| items | PARTIAL | exact battle-item behavior only |
| Trainer Features/perks | PARTIAL | feature interrupts |
| AI legal-action infrastructure | VERIFIED | legal-choice generation |
| AI tactical policy | BLOCKING | coordinated corridor denial/protection |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | full playback/integration unavailable |

Reduced version: READY.

Reduction contract:

- inspection staff remain outside BattleSpec;
- semantic compliance objects are noninteractive scenery;
- static geometry and explicit combatants only;
- success may emit only `IMMEDIATE_IMPLEMENTATION_INSPECTION_APPROACH_CLEAR`;
- later inspection determines observations;
- the responsible institutional/world layer determines whether implementation requirements were met.

### Tournament Protest Perimeter — full version

Narrative purpose: protect venue safety after an authoritative battle result while a separate protest/review process exists.

Capability requirements match the same permanent map. Rich crowd boundaries, evacuation timing, reactions and tactical coordination depend on PARTIAL/BLOCKING families.

Reduced version: READY.

- authoritative AutoPTU battle result is frozen before the new encounter;
- protest/review records and institutional actors remain outside BattleSpec;
- static exterior geometry only;
- success may emit `IMMEDIATE_TOURNAMENT_PROTEST_PERIMETER_CLEAR`;
- match result and review disposition cannot be altered by this combat.

## Institutional outcomes battle must never author

No current encounter contract may directly assert:

- filing accepted/declined;
- hearing scheduled/held/valid;
- notice validity;
- institutional finding;
- decision issued/effective;
- review permission;
- stay, affirmation, amendment, reversal or remand;
- eligibility outside an authoritative governing rule;
- credential suspension/restoration;
- guilt, liability or legal status;
- archive custody;
- organization authority;
- implementation or compliance outside the narrow physical battle result.

AutoPTU resolves combat facts. Ouros routes those facts into the responsible owner afterward.

## PTU / Caelo assumptions kept UNKNOWN

Pass 147 does not invent mechanical support for:

- universal court/tribunal systems;
- criminal/civil/administrative-law categories;
- generic hearing or appeal rights;
- universal notice requirements;
- generic evidence admissibility rules;
- universal burdens or standards of proof;
- sentencing or penalty tables;
- generic filing/review deadlines;
- automatic stays during review;
- universal appeal hierarchy;
- generic institutional-jurisdiction checks;
- Command as automatic adjudicative authority;
- Guile as automatic procedural victory;
- Intuition as automatic truth detection;
- General Education as universal legal knowledge;
- Technology Education as universal archive access;
- Trainer Features/classes as automatic judicial rank;
- badges, uniforms, species, Types, Moves, Abilities or held items as automatic authority proof;
- battle victory as adjudication, appeal, liability or compliance resolution.

## Adapter boundary

Minecraft/Cobblemon/Craftics may render an already-decided procedural state through posted schedules, waiting rooms, public notices, archive shelves, seals, changed signage, NPC presentation and other environmental details.

It must not infer hearing state from NPC co-location, decision validity from a written book item, authority from a scoreboard team, review state from chat, compliance from a block change or institutional outcome from battle/despawn events.

Cobblemon BattleState has zero authority over combatant selection, legality, HP/status, tactical position or adjudication consequences in Ouros.

## Readiness conclusion

Pass 147 introduces no new engine requirement for its reduced forms. All four proposed encounter families can preserve their narrative premise while using the verified/basic combat surface because institutional actors, records and decision semantics remain outside BattleSpec.

The live Java head is meaningful progress toward server-owned Intercept authority, but it remains localized evidence inside the broader PARTIAL movement family. Terrain/weather/hazards/zones/reactions, tactical AI and adapter/playback remain BLOCKING.