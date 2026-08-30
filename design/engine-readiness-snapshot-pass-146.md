# Engine Readiness Snapshot — Pass 146

Status: ENGINE EVIDENCE SNAPSHOT. This file records live evidence observed during Pass 146 and the implementation dependencies of the new organization/faction continuity encounters. It does not change AutoPTU-Java or AutoPTU and does not promote a capability from one representative mechanic.

Date: 2026-08-30

## Repositories inspected

### AutoPTU-Java — read only

Observed `main` head:

`3b860c37f45afde559533393f8ac78a24cf7df5f`

Commit:

`Own Intercept check distance in PTU geometry (#285)`

The commit moves the Intercept check-distance derivation into server-owned PTU geometry. It derives distance from the interceptor's runtime position/footprint and selected intercept position, uses footprint distance to a Medium anchor, floors overlap to one, and adds contract/runtime tests.

This is concrete evidence for a localized Intercept geometry path and strengthens server authority over rule-critical inputs.

It does not verify:

- every Intercept rule path;
- broad Push/Pull/Knockback;
- every forced-movement source;
- escort movement;
- object carrying;
- generalized reactions or reaction ordering;
- generalized terrain lifecycle;
- weather lifecycle;
- hazards;
- dynamic zones;
- ability-triggered terrain;
- full Trainer Feature interrupt semantics;
- AI tactical policy.

No capability family is promoted on this evidence alone.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit synchronizes cached Pixi screen dimensions after viewport resize so tactical sprite destinations use current renderer geometry. Its own commit message identifies the work as presentation-only and says battle rules/outcomes do not change.

This is not evidence for battle legality or narrative authority.

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

No category changed during Pass 146.

## Why Intercept remains inside a PARTIAL family

The live Java head verifies another server-owned slice of Intercept geometry. The permanent category is deliberately broader: `complete movement including push/pull/knockback/interception/forced movement`.

The category therefore remains PARTIAL until evidence covers the family rather than one path. Organization-lineage encounters must not treat the new distance resolver as proof that escort, carried records, broad forced movement, or generalized reactions are available.

## Encounter dependency matrix

### Branch Archive Withdrawal Corridor — full version

Narrative purpose: clear a withdrawal route while records and people are being removed from a contested site. Organizational succession and record custody remain outside battle.

Capability requirements:

| Capability family | Status | Why the full version may need it |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary targeting and geometry |
| base movement legality | VERIFIED | ordinary movement on the corridor |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | interception, displacement, and escort-adjacent movement if modeled tactically |
| core calculations | VERIFIED | standard PTU calculations |
| action economy/initiative | VERIFIED | standard initiative/action structure |
| full turn/round lifecycle | PARTIAL | timed withdrawal or reinforcement phases |
| full stateful damage pipeline | PARTIAL | normal persistent combat damage state |
| status lifecycle | PARTIAL | conditions affecting movement/timing |
| terrain/weather/hazards/zones/reactions | BLOCKING | reactive doorway control or dynamic access zones |
| move-specific behavior | PARTIAL | exact move semantics |
| abilities | PARTIAL | exact ability semantics |
| items | PARTIAL | battle items only; archive records are not generic battle items |
| Trainer Features/perks | PARTIAL | any feature interrupt or special reaction |
| AI legal-action infrastructure | VERIFIED | generating legal choices |
| AI tactical policy | BLOCKING | choosing good escort/blocking tactics |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative/playback integration remains incomplete |

Reduced version: READY.

Reduction contract:

- archivists leave BattleSpec;
- records and custody objects leave BattleSpec;
- neutral actors leave BattleSpec;
- archive doors/boxes become inaccessible static scenery;
- Ouros selects explicit combatants;
- AutoPTU receives static geometry;
- battle success may emit only `IMMEDIATE_ARCHIVE_WITHDRAWAL_ROUTE_CLEAR`;
- Ouros performs any record movement, custody handoff, succession interpretation, or NPC consequence afterward.

### Assembly Hall Split Perimeter — full version

Narrative purpose: keep a shared hall physically safe while two descendant organizations conduct separate activities. Battle has no role in deciding which descendant is legitimate.

Capability requirements:

| Capability family | Status | Why the full version may need it |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary targeting and geometry |
| base movement legality | VERIFIED | ordinary exterior movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | interception/displacement at exits |
| core calculations | VERIFIED | standard calculations |
| action economy/initiative | VERIFIED | standard initiative/action structure |
| full turn/round lifecycle | PARTIAL | timed arrival, evacuation, or reinforcement phases |
| full stateful damage pipeline | PARTIAL | persistent battle state |
| status lifecycle | PARTIAL | exact condition lifecycle |
| terrain/weather/hazards/zones/reactions | BLOCKING | reactive exits/crowd edges/dynamic perimeter zones |
| move-specific behavior | PARTIAL | exact move semantics |
| abilities | PARTIAL | exact ability semantics |
| items | PARTIAL | exact battle-item semantics |
| Trainer Features/perks | PARTIAL | feature interrupts/reactions |
| AI legal-action infrastructure | VERIFIED | legal choice generation |
| AI tactical policy | BLOCKING | coordinated perimeter tactics |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | full authoritative playback/integration unavailable |

Reduced version: READY.

Reduction contract:

- all meeting participants evacuate before initiative;
- organizational representatives and neutral crowds are outside BattleSpec;
- static exterior geometry is supplied;
- explicit combatants only;
- success may emit only `IMMEDIATE_ASSEMBLY_HALL_PERIMETER_CLEAR`;
- lineage, meeting decisions, leadership, authority, membership, and affiliation remain unchanged unless separate world events change them.

### Shared Depot Handoff Chokepoint — full version

Narrative purpose: protect the physical approach to a depot during an organizational transition. Custody and successor identity remain world-system facts.

Capability requirements:

| Capability family | Status | Why the full version may need it |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | ordinary targeting/geometry |
| base movement legality | VERIFIED | ordinary movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | chokepoint displacement, interception, escort-adjacent behavior |
| core calculations | VERIFIED | standard calculations |
| action economy/initiative | VERIFIED | standard initiative/action structure |
| full turn/round lifecycle | PARTIAL | handoff timing if kept inside initiative |
| full stateful damage pipeline | PARTIAL | persistent battle state |
| status lifecycle | PARTIAL | exact status behavior |
| terrain/weather/hazards/zones/reactions | BLOCKING | dynamic access control/reactions |
| move-specific behavior | PARTIAL | exact move semantics |
| abilities | PARTIAL | exact ability semantics |
| items | PARTIAL | depot assets must not be treated as generic battle items without rules |
| Trainer Features/perks | PARTIAL | interrupts/reactions |
| AI legal-action infrastructure | VERIFIED | legal choice generation |
| AI tactical policy | BLOCKING | coordinated chokepoint tactics |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | full authoritative playback/integration unavailable |

Reduced version: READY.

Reduction contract:

- staff leave BattleSpec;
- controlled assets leave BattleSpec as semantic objects;
- vehicles/equipment may remain visual static scenery only;
- explicit combatants fight over static approach geometry;
- success may emit only `IMMEDIATE_DEPOT_HANDOFF_APPROACH_CLEAR`;
- Ouros resolves custody, contracts, asset assignment, branch/successor relations, and archival consequences afterward.

## Narrative outcomes battle must never author

No current or proposed battle contract may directly assert:

- same organization / different organization;
- branch created or closed;
- successor confirmed;
- successor rejected;
- merger proposed or effective;
- dissolution;
- organizational revival;
- leadership recognition;
- membership;
- resignation;
- authority or mandate transfer;
- contract inheritance;
- debt inheritance;
- archive custody;
- facility ownership;
- coalition formation;
- affiliation start/end;
- legitimacy of a public claim.

Battle may change a narrow physical state. Ouros applies narrative consequences through the relevant owner afterward.

## PTU / Caelo assumptions kept UNKNOWN

Pass 146 does not invent mechanical support for:

- universal organizational registries;
- legal-personhood rules;
- mandatory charters/bylaws;
- universal faction reputation tables;
- generic organization ranks;
- generic membership/expulsion procedures;
- universal leadership succession;
- split/merger/dissolution mechanics;
- generic disguise/infiltration DCs that establish organizational legitimacy;
- Command as automatic organizational authority;
- Guile as automatic proof of membership or deception success outside governed checks;
- Intuition as automatic lineage detection;
- General Education as universal institutional-history authority;
- Technology Education as universal registry access;
- Trainer Classes/Features as automatic office or faction rank;
- Pokémon species, Type, Move, Ability, held item, crest, uniform, or badge as automatic membership proof;
- battle victory as succession, merger, dissolution, ownership, or mandate resolution.

## Adapter boundary

Minecraft/Cobblemon/Craftics may render already-decided organization history through current/old signage, banners, colors, buildings, meeting rooms, archive props, notices, NPC presentation, and environmental layers.

It must not infer organizational identity from entity IDs, scoreboard teams, nametags, skins, banners, blocks, permissions, location, or who wins a local fight.

A despawn does not dissolve an organization. Changing a banner does not rename it. Moving an NPC does not transfer membership. Reusing a scoreboard label does not establish succession.

## Readiness conclusion

All three new Pass 146 encounters have reduced READY versions that preserve the narrative premise with currently verified/basic combat capabilities. Their rich versions remain honestly dependent on the permanent PARTIAL/BLOCKING families where they require interception beyond the pinned path, forced movement, timed lifecycle, generalized reactions/zones, richer statuses, tactical AI, or adapter playback.

The live AutoPTU-Java Intercept geometry improvement is recorded as localized evidence only. No permanent capability category is promoted.
