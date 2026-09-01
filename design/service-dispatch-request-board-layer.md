# Ouros Service Dispatch & Request-Board Layer

Status: DESIGN / NON-CANON
Date: 2026-09-01

Purpose: define a reusable layer for small resident/institution requests that stays connected to persistent world state, existing questlines and physical travel.

## Core rule

A request is a projection of an existing world need. It does not create the need.

Request generation order:

`WORLD FACT OR ACTOR NEED -> ISSUER KNOWLEDGE -> POSTING CHANNEL -> PLAYER VISIBILITY -> ACCEPTANCE -> EXECUTION -> WORLD CONSEQUENCE`

If the world fact disappears before acceptance, the request may update or withdraw. If the issuer never learned the fact, the request cannot appear merely because the system knows it.

## Request record

Each authored/generated request should carry:

- `request_id`
- `issuer_actor_id` or `issuer_institution_id`
- `posting_channel_id`
- `created_world_time`
- `affected_site_ids`
- `route_cluster_id` when travel can be bundled
- `need_type`
- `known_fact_refs`
- `claim_refs` when information is unverified
- `prerequisite_fact_refs`
- `urgency_state`
- `expiry_condition` only when justified by world state
- `questline_refs` when the request contributes to a larger thread
- `consequence_targets`
- `mechanical_dependency_contract`
- `privacy_scope`
- `status`

Suggested statuses:
`AVAILABLE`, `ACCEPTED`, `SUPERSEDED`, `WITHDRAWN`, `RESOLVED`, `FAILED_BY_WORLD_CHANGE`.

## Need types

Initial reusable vocabulary:

- DELIVER
- RETRIEVE
- VERIFY
- SURVEY
- REPAIR_COORDINATION
- ESCORT_COORDINATION
- LOCATE
- REPORT
- TRANSPORT_SUPPORT
- SUPPLY_SUPPORT
- DOCUMENT_SUPPORT
- CARE_LOGISTICS
- ECOLOGY_OBSERVATION
- FACILITY_SUPPORT
- COMPETITIVE_NOTICE

These are narrative verbs, not mechanical permissions.

## Channel model

A board is one channel among several.

Examples:
- Field Office dispatch board;
- market service ledger;
- ferry notice slate;
- archive circulation desk;
- cooperative dispatch ledger;
- station operations board;
- personal message/mail when relationship and communications state allow it.

The same underlying request may appear through more than one channel only when information actually propagated there.

## Trip bundling

Requests receive a route cluster derived from actual sites and current route availability.

The UI/journal may suggest compatible work when:
- affected sites share a plausible route;
- both requests are active at the same world time;
- combining them does not violate urgency, custody, privacy or institutional constraints;
- no request requires a mutually exclusive commitment.

Bundling changes presentation and route planning. It does not auto-complete tasks or fabricate travel events.

Example Marea route cluster:

`Puerto Bruma -> Sendero del Vidrio -> Mirador branch -> Loma Clara`

A player carrying archive copies to Mirador may also return a serviced instrument and verify the seasonal crossing if those needs all exist concurrently.

## Relationship to questlines

SERVICE requests may:
- remain one-off settlement texture;
- advance an existing SETTLEMENT, REGION, FACTION, CLASS, CHARACTER, RELATIONSHIP, EXPLORATION or EQUIPMENT thread;
- expose evidence used later by a major quest;
- create a new persistent NPC relationship edge after repeated interactions.

They should not silently become MAIN quests.

A larger questline can emit service requests as consequences. A service request can reveal a larger thread only after its evidence justifies that transition.

## Failure and world change

Failure should distinguish player choice from changed circumstances.

Examples:
- ferry departed before an optional delivery was accepted -> `SUPERSEDED`;
- blocked crossing reopened because another actor repaired it -> `WITHDRAWN/RESOLVED_EXTERNALLY` equivalent through recorded world cause;
- player accepted a time-sensitive pickup and ignored it until goods spoiled only if spoilage/timing is explicitly established by governing world state;
- NPC became unavailable because schedule changed -> request remains possible through another legitimate contact only if the institution supports reassignment.

No arbitrary countdowns.

## Mechanical dependency contract

Every request that can enter a tactical encounter records the intended version and a reduced implementation.

### Example: Stranded Survey Crew

Intended full version:
The player reaches a damaged route while hostile wild Pokémon are agitated around a research crew. The tactical objective is to protect a withdrawal corridor while crew members move toward safety.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if exact statuses appear;
- terrain/weather/hazards/zones/reactions — BLOCKING if unstable ground or weather affects tactics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for objective-aware protection/denial;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING as complete family.

Full version status: BLOCKED.

Reduced version:
The research crew remains outside BattleSpec. The player resolves one audited ordinary battle/encounter at the route edge. On authoritative success, Narrative may write `IMMEDIATE_WITHDRAWAL_CORRIDOR_CLEAR`; crew evacuation then resolves through world-state logic, not tactical NPC movement.

Reduced version status: potentially READY after exact Move/Ability/Item/Feature audit.

### Example: Ferry Manifest Recovery

Intended version:
Locate a dropped waterproof manifest packet along a known shoreline segment and return it to Lia.

Dependencies:
No tactical battle required. Base overworld discovery/search presentation only.

If a battle occurs incidentally, it remains a separate audited encounter and does not mechanically determine whether the packet exists.

Status: READY at narrative layer.

### Example: Battle Yard Fixture Check

Intended version:
Inspect several physical Battle Yard anchors, identify which fixture is damaged, deliver Teo's repair note and later confirm repair completion.

Dependencies:
No tactical PTU mechanics required unless a formal battle is independently scheduled.

Status: READY at narrative layer.

## Marea first implementation mapping

Marea Field Office:
- route verification;
- ecology observation handoff;
- incident follow-up.

Market Hall:
- supplier pickup/delivery;
- substitute ingredient sourcing only as physical supply state, never invented Chef mechanics.

Ferry landing:
- manifest/document movement;
- delayed passenger/package coordination;
- route observation reports.

Tideglass:
- copy delivery;
- source retrieval;
- archive cross-reference errands.

Clinic:
- equipment/supply logistics only on public boards;
- patient identity and clinical details remain private.

Repair row:
- equipment intake/return;
- site inspection before repair;
- parts provenance when authoritative item systems support it.

Loma cooperative:
- lot verification;
- dispatch paperwork;
- delivery coordination.

Mirador:
- instrument transport;
- observation handoff;
- transect verification.

## Anti-filler gate

A request should not be generated unless it changes or exposes at least one durable relation:
- actor knowledge;
- relationship history;
- site/service state;
- route state;
- evidence/case state;
- supply/provenance state;
- ecology observation state;
- faction/institution history;
- questline progression.

Requests whose only output is currency or generic XP should be rejected unless the governing progression/economy design explicitly requires them.
