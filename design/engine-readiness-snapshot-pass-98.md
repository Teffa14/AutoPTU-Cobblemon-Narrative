# Engine Readiness Snapshot — Pass 98

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`f3f9884b1142ff1a99dbf647bcf342ba6768bb39`

Latest relevant Java change:
`Expire temporary Trainer AP and reset actions at round start`

Observed narrow evidence:
- temporary Trainer AP grants are runtime-owned;
- deterministic AP consumption and expiry exist for this slice;
- Trainer action budgets reset through ROUND_START lifecycle processing;
- behavior is parity-tested against Python.

No newer Java commit was present during this pass.

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its recent visible work remains Career-oriented and does not change the tactical capability map.

The primary Caelo corpus was not reliably retrievable for universal age, guardianship, starter, novice, travel-supervision or first-journey rules. No Caelo-specific threshold is asserted.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static geometry, footprints, range and geometric LoS remain verified.

Pass 98 non-inference:
- geometric LoS does not prove a novice noticed danger;
- route visibility is not battle LoS;
- a mentor observing from far away is not automatically a valid target/source;
- a home/safe location marker has no tactical effect.

`base movement legality`

Established base Shift/Jump and movement-mode legality remain verified.

Pass 98 non-inference:
- permission to travel is not movement legality;
- a novice cannot enter a closed route because their Pokémon can physically cross it;
- overnight travel is not a movement mode;
- following a mentor is not a special Shift rule.

`core calculations`

Established calculation primitives remain verified.

No novice modifier, starter bonus, supervision bonus or safety scaling is introduced.

`action economy / initiative`

Established action economy/initiative remain verified. The current Java head strengthens Trainer AP/action reset at ROUND_START.

Pass 98 non-inference:
- a beginner acts later because they are inexperienced;
- a mentor grants extra actions by being present;
- a check-in deadline becomes initiative pressure;
- first battles receive hidden action-economy assistance.

`AI legal-action infrastructure`

Deterministic legal-choice generation remains verified.

This does not prove that AI can choose to retreat, protect a novice, preserve a route corridor, avoid escalation or complete a field objective.

### PARTIAL

`full turn / round lifecycle`

Representative phase, initiative, delayed-hit, field progression, temporary-effect and Trainer AP/action-reset slices exist.

Still PARTIAL because complete START/END triggers, durations, interrupts, all delayed effects, Statuses, Abilities, Features and transcript interactions are not proven.

Pass 98 distinction:
world check-ins, curfews, journey clocks and travel-day progression are not battle lifecycle.

`full stateful damage pipeline`

Representative authoritative paths exist.

Still PARTIAL because full damage remains incomplete.

A novice encounter must not receive hidden damage reduction, mercy scaling or beginner protection unless an explicit authored mechanic exists.

`status lifecycle`

Representative status boundaries exist.

Still PARTIAL because the complete controller is unfinished.

Narrative fear, tiredness, homesickness, uncertainty, caution or inexperience cannot create PTU Statuses.

`move-specific behavior`

Representative Move behavior exists.

Still PARTIAL because the complete PTU Move library is not ported.

A first-journey scenario using a particular Move must verify that exact Move behavior rather than assuming family coverage.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

Do not infer:
- Run Away = autonomous safe retreat;
- Pickup = travel scavenging system;
- Illuminate = route lighting permission;
- Friend Guard = generic novice protection;
- Telepathy = unlimited mentor communication.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Map, tent, travel pass, field notebook, loaned kit and emergency beacon are world objects unless exact PTU Item definitions authorize mechanics.

`Trainer Features / perks`

Representative Feature infrastructure exists.

Still PARTIAL.

A mentor, student, graduate, cadet or novice role grants no Feature, Skill Rank, Edge, AP or Order automatically.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a complete family.

Pass 98 impact:
- do not implement escorting through a hostile moving corridor;
- do not rely on interception to protect a novice;
- do not make a wild group physically herd PCs toward an exit;
- do not implement autonomous withdrawal with forced movement;
- do not use cliffs/traffic/doors as forced-movement traps.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 98 impact:
- a stormy first journey cannot invent battlefield Weather;
- darkness cannot invent Accuracy penalties;
- a washed-out route cannot create Rough Terrain automatically;
- a campfire cannot create a hazard zone;
- supervision distance cannot create a protective reaction.

`AI tactical policy`

Still BLOCKING.

No evidence proves goals such as:
- WITHDRAW;
- PROTECT_NOVICE;
- REACH_SAFE_TILE;
- ESCORT;
- AVOID_ESCALATION;
- PRESERVE_PARTNER;
- COMPLETE_FIELD_OBJECTIVE;
- HOLD_CORRIDOR_FOR_RETREAT.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

No verified end-to-end contract currently projects first-journey permissions, support contacts, check-ins, route revisions, starter-partnership state or world objectives into Minecraft and then into authoritative battle snapshots without duplicating PTU rules.

## Pass 98 specific overworld blockers

`FIRST_JOURNEY_STATE`
Persistent journey identity, phase, scope, milestones and completion state.

`NOVICE_AUTONOMY_SCOPE`
Scoped permissions and supervision requirements without a universal numeric autonomy score.

`JOURNEY_SUPPORT_NETWORK`
Mentors, institutions, clinics, lodging, transport and emergency contacts.

`FIRST_PARTNER_EVENT_AND_PROVENANCE`
Persistent Pokémon identity, custody/ownership references and observed relationship events.

`JOURNEY_LEG_STATE`
Planned vs actual route, timing, check-ins and incidents.

`JOURNEY_CHECKIN_STATE`
Due/received/missed/delayed/impossible check-ins linked to Communications.

`JOURNEY_DEBRIEF`
Append-only record of what happened, what changed and what remains unresolved.

`NOVICE_CONTENT_RISK_BUDGET`
Narrative content-selection heuristic based on actual support and capability state; never hidden PTU math.

`MIXED_PARTY_PERMISSION_RESOLUTION`
Each PC's credentials and autonomy remain independent in multiplayer.

`FIRST_JOURNEY_TO_TRAVEL_HANDOFF`
Travel owns route feasibility; first-journey state cannot bypass it.

`FIRST_JOURNEY_TO_CREDENTIALS_HANDOFF`
Formal permission comes from credential/authority state.

`FIRST_JOURNEY_TO_POKEMON_AGENCY_HANDOFF`
Observed partnership events do not become Loyalty or obedience without rules authority.

`FIRST_JOURNEY_TO_MINECRAFT_PROJECTION`
UI may show check-ins, route scope, support contacts and milestones but cannot calculate authority or mechanics.

## Encounter dependency summary

### First Night Route Incident — FULL

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING when used:
- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback.

REDUCED:
Resolve route/weather state before battle; freeze one static safe arena; make continue/wait/reroute/return the post-encounter decision.

### Starter Partnership Field Test — FULL

VERIFIED foundations:
- static targeting;
- base movement;
- core calculations;
- action economy;
- legal-action generation.

PARTIAL:
- exact Move/Ability/Item/Feature dependencies.

BLOCKING:
- objective-aware partner AI when autonomous field goals matter;
- Minecraft/world-object synchronization.

REDUCED:
Resolve field objective in overworld; use a conventional static battle if one occurs; record observed cooperation without assigning Loyalty.

### Return Before Dark — FULL

Main blockers:
- complete movement for pursuit/withdrawal;
- environment family if darkness/weather must affect battle;
- tactical AI for REACH_EXIT/WITHDRAW;
- adapter/playback.

REDUCED:
Resolve time, route, shelter and visibility before battle. Use a frozen arena with no invented darkness, fatigue or curfew effects.

## Overall conclusion

Pass 98 does not change any permanent capability classification.

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

The first-journey system can advance substantially before the blocking battle families exist because most autonomy, support, check-in, departure, return and debrief logic belongs to persistent world state rather than battle mechanics.
