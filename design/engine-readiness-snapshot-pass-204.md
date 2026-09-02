# Engine Readiness Snapshot — Pass 204

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `75fb24d3ce30ee8f53f162a4dfcef9d1c5749309`

Read-only engines inspected:
- AutoPTU-Java head: `f320aca406e3da87427eca32ab97943062c264ff`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

No engine head changed since pass 203.

AutoPTU-Java remains on `f320aca406e3da87427eca32ab97943062c264ff` — `Freeze forced-movement ability semantic contract (#324)`.

That commit strengthens evidence for selected Ability-family forced-movement prevention semantics, including pinned Python behavior associated with `push_immunity`, Suction Cups and Sumo Stance. It remains evidence for a bounded family, not proof of complete Push/Pull/Knockback/Interception coverage.

AutoPTU remains on `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. The commit message explicitly states the change is presentation-only and does not alter battle rules or outcomes.

No permanent capability category is promoted in pass 204.

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

## Complete movement caution

Still unverified as one complete family:
- all Push paths;
- all Pull paths;
- all Knockback paths;
- Interception;
- collisions;
- partial displacement/stops;
- chained displacement;
- footprint interactions during movement;
- reaction ordering;
- terrain-mediated displacement;
- all Move/Ability/Item/Feature/status combinations;
- end-to-end adapter/playback parity.

A representative prevention semantic contract cannot promote `complete movement` beyond PARTIAL.

## Pass 204 PTU/Caelo boundary

Repository searches across AutoPTU-Java and AutoPTU for `lodging` and `hotel` returned no indexed implementation evidence in this run.

A literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU again returned no indexed source content.

Pass 204 therefore treats residence/lodging as Narrative world-state only and leaves unresolved any Caelo/PTU rules concerning:
- rent;
- tenancy;
- property ownership;
- residential access law;
- household/guardianship status;
- lodging quality;
- relocation cost/time;
- storage capacity;
- accommodation-related bonuses.

PTU rest/healing remains a separate governed mechanic. A bed, room assignment or residential stay cannot heal HP, remove Injuries, restore AP, cure statuses or reset Move frequencies through Narrative authority.

## Residence versus Minecraft state

Pass 204 freezes the implementation boundary:

`CANONICAL_RESIDENCE != MINECRAFT_BED_OR_RESPAWN_STATE`

Minecraft/Cobblemon can project a room, bed, actor and personal props. It cannot create or terminate a residential record because:
- a bed is placed/broken;
- an actor sleeps;
- a spawn point changes;
- a chunk unloads;
- an NPC is duplicated;
- a nameplate changes;
- items happen to be present in a room.

Residential state must persist through stable Narrative IDs and reconcile presentation from that authority.

## Pass 204 rich encounter

Encounter: `Return Route to the Boarding Row`.

Narrative premise:
A persistent resident has legitimate temporary accommodation in Puerto Bruma after a separately established disruption. A bounded recovery trip for personal field equipment encounters a localized wild threat on Sendero del Vidrio. Residence, custody, relocation and destination remain Narrative facts outside BattleSpec.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required if protected withdrawal, Interception, Push, Pull, Knockback or other forced movement matters
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if route conditions become tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL where battle Items participate
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING when actors must prioritize withdrawal, territorial pressure, disengagement or protecting an exit over KO
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful overworld -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

Narrative retains:
- ordinary residence record;
- temporary lodging record;
- relocation/displacement provenance;
- recovered equipment identity/custody;
- noncombatants;
- route context;
- destination after withdrawal;
- any forwarding or room-access state.

Before combat:
- establish a safe Narrative state for noncombatants and semantic objects where appropriate;
- identify the single immediate actor still preventing withdrawal;
- select audited combatants/content;
- use stable geometry;
- omit unverified tactical weather/hazards/zones/reactions;
- avoid displacement objectives unless every selected interaction is independently contract-verified.

Allowed narrow handoffs:
- `IMMEDIATE_RECOVERY_ROUTE_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_RESIDENT_CAN_WITHDRAW`

Battle output cannot determine:
- residence or tenancy;
- room ownership;
- household membership;
- rent/payment;
- relocation motive;
- entitlement to future lodging;
- old-address forwarding;
- family/romantic relationships;
- PTU rest or healing;
- permanent route safety.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI tactical-policy caution

Legal-action infrastructure does not prove policy for:
- protected withdrawal;
- disengagement;
- territorial behavior;
- corridor control;
- choosing not to pursue;
- preserving distance;
- protecting a route exit rather than maximizing damage.

The full version therefore remains dependent on AI tactical policy.

## Terrain/hazard caution

Sendero del Vidrio's canonical seasonal watercourses and exposed shelves remain narrative geography. If a recovery encounter makes slippery ground, current, unstable stone, weather, hazard zones or reactions mechanically relevant, `terrain/weather/hazards/zones/reactions` becomes an explicit dependency and remains BLOCKING as a full family.

The reduced version uses stable geometry or keeps such conditions descriptive.

## Narrative repository state for this pass

Pass 204 writes only to Narrative.

New files:
- `research/2026-09-02-residence-lodging-household-relocation-scan-204.md`
- `design/residence-lodging-household-relocation-continuity-layer.md`
- `proposals/2026-09-02-marea-residence-lodging-relocation-seeds-204.md`
- `design/engine-readiness-snapshot-pass-204.md`

No AutoPTU-Java or AutoPTU write is authorized or performed.

## Implementation recommendation

Prototype `Room Assigned, Room Empty` first.

It requires:
- no battle;
- no new NPC;
- no new institution;
- no new building;
- no new canonical address;
- no price/rent rule;
- no family inference;
- no PTU housing mechanic.

It directly tests the essential persistence invariant: a canonical residence remains assigned while its resident is elsewhere, and Minecraft entity/bed state cannot author a move-out.