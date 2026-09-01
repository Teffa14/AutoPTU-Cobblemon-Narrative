# Field search, wayfinding and recovery continuity layer

Status: DESIGN ARCHITECTURE / NOT CANON
Date: 2026-09-01

Purpose: support overdue-person reports, field searches, route-finding, clue interpretation, safe contact and recovery while preserving uncertainty and reusing existing Ouros authority systems.

## Boundary

This layer composes existing systems rather than replacing them:

- communications and delivery history;
- local knowledge / claim propagation;
- route condition and aftermath;
- shared-resource access and temporary closure;
- ecological phenology and field observations;
- NPC schedules and institutional delegation;
- archive provenance;
- care and injury consequences;
- relationship/public-memory consequences;
- questline state;
- battle handoff.

It does not create omniscient tracking, a generic Rescue stat, universal Ranger authority, a death inference system or a replacement for PTU Skills/Features/Capabilities.

## Core entities

### `field_presence_expectation`

Represents an expected arrival, return or check-in.

Fields:

- `expectation_id`;
- subject ID;
- issuer/reporter ID;
- expected place or checkpoint;
- expected time/window;
- planned route if actually known;
- stated purpose if known;
- companions/equipment already documented;
- source/provenance;
- status.

Possible status values:

- PLANNED;
- CHECKED_IN;
- OVERDUE_UNVERIFIED;
- CANCELLED_KNOWN;
- SUPERSEDED.

A missed expectation alone does not create `MISSING_CONFIRMED`.

### `field_search_case`

Created only after reasonable verification attempts justify organized follow-up.

Fields:

- stable case ID;
- subject ID;
- reporter(s);
- opened timestamp;
- current coordination authority;
- urgency basis;
- last-known-point version;
- relevant route IDs;
- active access restrictions;
- search sectors;
- observations/claims;
- communications attempted;
- assigned teams/persons;
- current operational status;
- care requirements if contact occurs;
- closure reason;
- archive/public visibility policy.

Suggested status flow:

RECEIVED
-> VERIFYING
-> ACTIVE
-> CONTACT_ESTABLISHED_SAFE | FOUND_ASSISTANCE_REQUIRED | FOUND_ESCORT_REQUIRED | SAFE_SELF_RETURN | FOUND_BY_OTHER_PARTY | SUSPENDED | TRANSFERRED | CLOSED_UNRESOLVED
-> CLOSED

Status transitions require an event or attributed report. They cannot be inferred from an entity loading or unloading in Minecraft.

### `last_known_point_version`

Fields:

- place/segment ID;
- timestamp or interval;
- evidence type;
- source actor/object/system;
- observation confidence;
- capture method;
- contradictions;
- supersedes prior version;
- whether position is exact, bounded, inferred or reported.

Allowed precision labels:

- EXACT_VERIFIED;
- NAMED_SITE_VERIFIED;
- ROUTE_SEGMENT_BOUNDED;
- REPORTED_UNVERIFIED;
- INFERRED_RANGE;
- UNKNOWN.

The UI should not render inferred or bounded evidence as a precise pin unless the visual language clearly preserves uncertainty.

### `search_sector`

A named operational unit of terrain.

Fields:

- sector ID;
- route/site bounds;
- accessibility state;
- method;
- assigned searcher/team;
- start/end time;
- conditions;
- coverage confidence;
- observations found;
- revisit recommendation.

Search result states:

- NOT_STARTED;
- IN_PROGRESS;
- SEARCHED_NO_RELEVANT_TRACE;
- TRACE_REQUIRES_REVIEW;
- ACCESS_BLOCKED;
- CONTACT_ESTABLISHED;
- REVISIT_REQUIRED.

`SEARCHED_NO_RELEVANT_TRACE` does not mean the subject was never present.

### `field_trace_observation`

Uses normal evidence/claim provenance.

Possible categories:

- OBJECT;
- TRACK_OR_PRINT;
- DAMAGE_OR_DISTURBANCE;
- WITNESS_SIGHTING;
- SIGNAL;
- REGISTER_ENTRY;
- INSTRUMENT_RECORD;
- POKEMON_BEHAVIOR;
- ROUTE_MARKER_STATE;
- OTHER_OBSERVATION.

Fields include observed time, observer, location precision, capture method, environmental conditions, possible alternate explanations and claimed subject linkage.

A found object can have high confidence as a physical observation and low confidence as evidence about the subject.

## Operational invariants

`NOT_AT_EXPECTED_LOCATION != MISSING_CONFIRMED`

`MISSING_REPORT != DANGER_CONFIRMED`

`OVERDUE != INJURED`

`TRACE_FOUND != SUBJECT_IDENTIFIED`

`SEARCHED_SECTOR != SUBJECT_NEVER_PRESENT`

`LAST_KNOWN != CURRENT_POSITION`

`MAP_MARKER != WORLD_TRUTH`

`POKEMON_BEHAVIOR != INTENT_OR_IDENTITY_PROOF`

`BATTLE_VICTORY != SEARCH_COMPLETE`

`SUBJECT_FOUND != SAFE_TO_TRAVEL`

`NO_CONTACT != DEATH`

`COBBLEMON_ENTITY_DESPAWNED != SUBJECT_MISSING`

## Verification before escalation

A normal missed check-in should first trigger bounded verification appropriate to the situation:

- confirm the expected time/window was recorded correctly;
- check whether the route or plan changed through an authorized communication;
- contact the expected destination;
- inspect known departure/arrival records where those records legitimately exist;
- verify whether a ferry, closure or weather delay plausibly explains lateness;
- ask the last verified witness without turning rumor into fact.

The design should allow a case to resolve here. Not every overdue event becomes a field deployment.

## Search planning

A search plan should be generated from known geography and evidence.

For Marea's current canon, legitimate named segments already exist:

- Puerto Bruma / south trailhead;
- lower shelf;
- seasonal crossing;
- upper junction;
- Mirador branch / transect trailhead;
- Loma Clara arrival area.

No alternate trail should be invented as canon until a map file establishes it.

A plan can prioritize sectors by:

- last-known evidence;
- planned destination;
- route accessibility;
- time since last verification;
- environmental conditions;
- subject mobility actually known;
- credible witness information.

Do not expose a hidden authoritative subject coordinate to NPC reasoning merely because the server stores it.

## Wayfinding

Wayfinding can use several distinct supports:

- fixed landmarks;
- canonical route graph;
- signs/markers;
- physical maps with edition/provenance;
- compass or instrument mechanics when supported;
- NPC local knowledge;
- verified Pokémon capabilities;
- PTU Skills/Features when exact content supports them.

No one source is automatically perfect. An old Tideglass map can be historically accurate for its edition and operationally obsolete today.

## Pokémon participation

Companion Pokémon may contribute only through explicitly justified behavior.

Examples safe at the narrative layer:

- Kite visibly surveys from above and Mara reports what she observed through ordinary interaction;
- Margin repeatedly turns attention toward a branch, creating an observation to inspect;
- a Pokémon with a verified sensory Capability may mechanically support a search if PTU/Caelo and engine parity confirm the effect.

Forbidden shortcuts:

- every Flying-type provides aerial omniscience;
- every canine Pokémon has automatic scent tracking;
- Telepathy reveals an absent person's coordinates;
- a Cobblemon pathfinding target becomes canonical evidence.

## Autonomous resolution

Search state can change while the player is elsewhere.

Examples:

- the subject self-returns and checks in;
- Lia reports that the subject boarded or disembarked after a delay;
- another resident establishes contact;
- a route closure lifts but the case remains active;
- worsening conditions suspend a sector;
- a correction invalidates an earlier sighting.

The player does not need to be present for NPCs and institutions to act within their existing authority.

## Finding the subject

Contact branches before quest closure.

### Safe contact

The subject can continue or return under their own power. The case can move toward closure after communication and accountability are complete.

### Assistance required

The subject is found but needs ordinary supplies, route help or transport. Care/transport systems determine what happens next.

### Escort required

Movement to safety becomes an operational objective. If modeled tactically, this creates much higher engine requirements and must not be faked in the adapter.

### Medical emergency

Oren/care systems own medical consequences within verified mechanics. Finding the person does not authorize Narrative to invent injury treatment rules.

## Search closure

A closure record stores:

- final operational status;
- who authorized closure;
- contact outcome if known;
- evidence that justified closure;
- unresolved questions;
- route/equipment follow-up;
- communications sent;
- archive retention;
- public wording if any;
- relationship consequences.

Historical uncertainty can remain after operational closure.

Examples:

- person safely returned, reason for route deviation unknown;
- old missing case remains unresolved but search operations are closed;
- found equipment ownership unresolved even though the person was located elsewhere.

## Relationship and institutional consequences

Good consequences come from conduct:

- accurately reporting last-known information;
- respecting a closure;
- checking in on time after accepting a procedure;
- returning borrowed search equipment;
- avoiding rumor amplification;
- documenting a false lead instead of hiding it;
- escalating a real hazard;
- recognizing when conditions make continued searching unsafe.

There is no universal hero score for finding someone.

## Quest patterns

Useful patterns:

- overdue but safely delayed;
- check-in failure caused by communications infrastructure;
- ambiguous trace with multiple owners;
- outdated map versus current route;
- subject found but unable to traverse safely;
- wildlife activity changes search accessibility without being the cause of disappearance;
- historical disappearance re-opened by new provenance;
- two teams have different evidence quality;
- subject self-rescues while searchers are still deployed.

Avoid defaulting to kidnapping, villain factions, death or supernatural disappearance simply to raise stakes.

## Mechanically rich encounter template

### Full form: Search at the Upper Bend

Premise: an overdue field traveler was last reliably seen beyond the lower shelf. A search narrows toward the upper route while a localized wild-Pokémon confrontation and unstable terrain create pressure around searchers and the eventual contact point.

Intended full-version requirements:

- targeting/footprints/range/LoS: required for tactical positioning and visibility;
- base movement legality: required;
- complete movement including push/pull/knockback/interception/forced movement: required if slope displacement, protective interception or forced repositioning is modeled;
- core calculations: required;
- action economy/initiative: required;
- full turn/round lifecycle: required for sustained search/escort objectives;
- full stateful damage pipeline: required;
- status lifecycle: required if the exact roster applies statuses;
- terrain/weather/hazards/zones/reactions: required if unstable cells, weather phases, hazardous corridors or reactive protection are tactical mechanics;
- move-specific behavior: exact roster audit required;
- abilities: exact roster audit required;
- items: exact roster audit required;
- Trainer Features/perks: exact participant audit required;
- AI legal-action infrastructure: required;
- AI tactical policy: required for objective-aware protection, retreat and path decisions;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful projection of the tactical sequence and authoritative results.

The full form remains unavailable until each dependency it uses is verified by current contracts/tests. Representative forced-movement support does not satisfy complete movement.

### Reduced form

The search itself remains world-state gameplay. The player checks named sectors, compares traces and establishes the subject's bounded location through evidence. Searchers and the subject are never tactical escort units.

If an ordinary hostile encounter blocks safe access, civilians and the subject remain outside BattleSpec. AutoPTU receives one audited battle in a stable clearing with content chosen to avoid unsupported terrain, weather phases, forced movement, reaction zones, complex statuses and unverified interrupts.

Allowed battle handoff examples:

- `IMMEDIATE_CLEARING_SECURED`;
- `IMMEDIATE_WILD_THREAT_WITHDREW`.

Forbidden automatic consequences:

- `SUBJECT_FOUND` unless world evidence already established contact;
- `SUBJECT_SAFE`;
- `SEARCH_COMPLETE`;
- `ROUTE_REOPENED`;
- `TRACE_IDENTIFIED`;
- `CAUSE_OF_DELAY_PROVED`.

The world layer decides those outcomes separately.

## Minecraft/Cobblemon projection

Useful near-term surfaces:

- physical check-in board at Field Office or other canon location after approval;
- route markers at existing anchors;
- time-stamped field notes;
- carried map copies with edition metadata;
- search-sector journal entries;
- visible temporary closure notices;
- found-object props linked to server-owned item state;
- NPC movement between known anchors;
- location discovery without hidden target teleport markers.

Authority boundaries:

- entity unload cannot create or resolve a missing case;
- pathfinding failure cannot become evidence of injury;
- a client-side waypoint cannot prove location;
- despawned trace props remain governed by server provenance;
- visual battle playback cannot author recovery outcome beyond its contract.

## Canon promotion checklist

Before a concrete search procedure becomes canon, resolve:

- who can open and coordinate a case in Marea;
- what types of check-in records actually exist;
- which route markers/signs physically exist;
- whether Mirador has a formal field plan/check-in protocol;
- whether ferry records can be used operationally and by whom;
- what emergency signaling PTU/Caelo explicitly supports;
- whether any Pokémon sensory/tracking behavior has exact provenance;
- what care/transport authority follows successful contact;
- privacy/public-memory policy for active and historical cases;
- reduced battle path for any encounter that would otherwise exceed engine readiness.

Until reviewed, concrete procedures and incidents remain proposals.