# Engine Readiness Snapshot — Pass 139

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding place-name, address and location-reference continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 139:

`411ff11bca684e4149a18e62b1239a037e442fe1`

The full recursive repository tree was inspected before topic selection and returned `truncated: false`.

The selected gap was checked directly against:

- `design/cartography-survey-wayfinding-layer.md`;
- `design/public-notices-signage-world-information-extension.md`;
- `design/courier-parcel-last-mile-logistics-extension.md`;
- `design/land-parcels-boundaries-use-rights-records-continuity-extension.md`;
- `design/human-identity-name-record-continuity-extension.md`;
- `research/2026-08-18-source-scan.md`;
- Pass 138 readiness.

The gap is connective: existing systems store geography, map claims, signs, parcel destinations, land identity and record history, but no dedicated layer preserves neutral continuity between a persistent place and changing names, aliases, address descriptors, entrances and service points.

## AutoPTU-Java live evidence

Current head inspected:

`9946f3a46f05ff187e0b04979351e276ab55697e`

Commit:

`Fix terrain oracle helper lexical scope (#281)`

No newer AutoPTU-Java commit was present during this pass.

The commit hardens the Intercept parity exporter so local helper resolution follows Python lexical scope and runtime binding behavior. Dedicated exporter tests are gated in the relevant workflow.

This strengthens confidence in a localized Intercept / `_terrain_skill_check_bonus` contract.

It does not establish:

- generalized terrain state;
- terrain creation or removal;
- weather lifecycle;
- generic hazards or zones;
- generalized reactions or reaction ordering;
- broad Push/Pull/Knockback;
- every forced-movement source;
- escort semantics;
- staged withdrawal semantics;
- tactical AI policy;
- place-name or address resolution;
- semantic Minecraft projection of place-reference state.

No permanent capability category is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during this pass.

The change synchronizes cached Pixi screen dimensions after viewport resize. The commit explicitly states that it is presentation-only and does not change battle rules or outcomes.

It does not establish semantic projection for place identity, names, aliases, map editions, addresses, entrances, delivery points or historical reference linkage.

## Permanent capability map — Pass 139

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and static spatial legality remain sufficient for reduced static encounters.

`base movement legality`

Basic movement remains verified for conventional reviewed BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains verified at its current baseline.

`action economy/initiative`

Baseline tactical action economy and initiative remain verified. Initiative has no authority over location-reference priority or naming decisions.

`AI legal-action infrastructure`

Legal-action enumeration and validation remain verified. This does not provide objective-aware withdrawal, escort, investigation or wayfinding policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The localized Intercept path has strong specific evidence, but the whole family remains partial. Broad Push, Pull, Knockback, every forced-movement source, escort movement and generalized movement reactions are not established.

`full turn/round lifecycle`

Ordinary battle progression exists. Generalized staged civilian withdrawal, moving investigators, timed access changes or escort windows are not verified.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Exact implemented statuses may be used where their source contracts apply. No generic lost, confused, misdirected, access-denied or wayfinding status is created here.

`move-specific behavior`

Representative Moves do not establish full family coverage. No Move automatically resolves an address, authenticates a map, identifies a historical place or authorizes entry.

`abilities`

Representative Ability behavior does not establish the whole family. No Ability creates geographical-name authority or universal navigation competence.

`items`

Items remain partial. Maps, compasses, signs, tickets, badges, radios or documents receive no invented tactical effects.

`Trainer Features/perks`

Exact Features remain source-governed. No Feature automatically grants universal surveying, addressing, archival or naming authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich variants may require protected withdrawal corridors, changing construction access, hazards, dynamically blocked entrances or generalized reactions. The localized Intercept terrain helper is far narrower than this family.

`AI tactical policy`

Rich variants may require PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION, escort-aware behavior or objective-aware avoidance. Legal-action infrastructure alone does not establish those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Current presentation evidence does not provide semantic projection for current/former names, alias resolution, entrance succession, address descriptors, map/sign disagreement or historical linkage.

## Encounter review — Wayfinding Team Withdrawal

Full intended objective:

A noncombat survey, courier or response team is resolving a stale or disputed location reference when an independent tactical threat emerges. Evidence work pauses while the team withdraws.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for staged withdrawal;
- full stateful damage pipeline — PARTIAL if attacks occur;
- status lifecycle — PARTIAL for exact implemented statuses only;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic protected corridors or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Location-reference work pauses before BattleSpec creation.
2. Surveyors, couriers, records and noncombatant Pokémon leave the tactical grid.
3. Ouros selects explicit combatants.
4. AutoPTU receives static reviewed geometry.
5. Tactical resolution may create only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR` or an equivalently narrow physical result.
6. The narrative owner separately resumes, changes or closes the location-resolution task.

`TACTICAL_VICTORY != PLACE_REFERENCE_RESOLVED`.

## Encounter review — Old Entrance Chokepoint

Full intended objective:

Characters reach the correct persistent site through an outdated entrance reference while an independent tactical threat blocks the approach to the currently valid access point.

Dependencies remain identical where escort, forced movement, changing access, hazards or objective-aware AI are active.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Current site identity and valid access-point state are resolved outside BattleSpec.
2. Noncombat staff, visitors and service records remain outside combat.
3. AutoPTU resolves a conventional static encounter at the approach.
4. Victory may create only `IMMEDIATE_APPROACH_CLEAR`.
5. The relevant world owner separately decides access, delivery, reopening or service continuation.

`APPROACH_CLEAR != ACCESS_AUTHORIZED`.

`CORRECT_SITE != CORRECT_ENTRANCE`.

## Encounter review — Same-Name Landmark Perimeter

Full intended objective:

Two reports use the same colloquial landmark name for different candidate places. Investigators reach one candidate location and an independent encounter occurs.

Full version status: BLOCKED only if rich escort/hazard/tactical-policy semantics are desired.

Reduced version status: READY.

Reduced contract:

1. Candidate place references and historical/report linkage remain narrative world state.
2. All evidence handling and noncombat investigators remain outside BattleSpec.
3. AutoPTU receives explicit combatants and static geometry.
4. Tactical victory may secure the immediate site only.
5. Reference linkage remains unresolved unless non-battle evidence resolves it later.

`BATTLE_RESULT != HISTORICAL_PLACE_LINKAGE`.

## PTU / Caelo mechanical guardrails

The project source scan supports persistent locations, exploration, Jobs and authored environmental mechanics where a source defines them. It does not establish a universal place-reference ruleset.

Remain UNKNOWN unless exact source evidence is found:

- universal Survival checks for address resolution;
- universal General Education checks for old place names;
- universal Perception checks for entrance finding;
- universal Technology Education checks for geocoding or map databases;
- universal social-Skill checks for directions;
- fixed stale-map or stale-name penalties;
- generic navigation time costs;
- universal Trainer Features for surveying/naming authority;
- species/Type/Move/Ability based automatic place identification.

No Skill check may replace world evidence simply because it is narratively convenient.

## Minecraft/Cobblemon authority boundary

Minecraft may display current or former signs, entrance markers, old painted names, maps, buildings and landmarks.

Those visuals are projections.

A sign block does not establish a place name. A broken sign does not revoke one. Coordinates do not prove a route exists. A marker does not authorize entry. A Cobblemon entity standing at a landmark does not identify that landmark's historical name.

Ouros remains authoritative for place identity, world facts, combatant selection and narrative consequences. AutoPTU remains authoritative for tactical battle rules. Cobblemon/Minecraft BattleState does not decide either domain.

## Unresolved canon questions

- Which Ouros regions use formal street addressing?
- Which places use landmark-relative directions instead?
- Which institutions can standardize or change names, if any?
- Which local/traditional names coexist with institutional forms?
- Which scripts and languages exist in each region?
- Are building, platform, berth, route or lot numbers common anywhere?
- Which directories are public and which are internal?
- How fast do maps, signs, courier systems, transit records and dispatch directories update?
- Which historical renamings already occurred?
- Which current settlements have same-name collisions?
- Can a place simultaneously have several current names for different communities?

All remain NON-CANON/UNKNOWN until authored.