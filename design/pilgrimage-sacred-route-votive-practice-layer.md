# Pilgrimage, sacred-route and votive-practice layer

Status: DESIGN ARCHITECTURE / NOT CANON
Date: 2026-09-01

Purpose: support recurring journeys to meaningful places, shrine or marker visitation, offerings, vows, commemorative walks and disputed traditions without letting social practice silently author supernatural truth.

## Boundary

This layer composes existing Ouros systems:

- calendar/event recurrence;
- public memory;
- archives and provenance;
- local knowledge and claim propagation;
- language/translation/interpretation;
- memorial and legacy stewardship;
- shared-resource access and closure states;
- route condition/recovery;
- NPC schedules and institutional roles;
- ecology/phenology;
- questline and relationship state.

It does not define a religion engine, Legendary cosmology or universal belief score.

## Core model

A recurring meaningful journey is represented by separate records:

### `practice_id`

Stable identity of the social practice.

Fields:

- display label;
- earliest verified evidence date/range;
- current observed form;
- known historical variants;
- associated route/site IDs;
- organizer/custodian IDs if any;
- public/private participation status;
- recurrence rule if any;
- evidence refs;
- disputed-origin claims;
- active access constraints;
- current edition/version.

### `practice_action`

An observable action such as:

- WALK_ROUTE;
- STOP_AT_MARKER;
- LEAVE_OBJECT;
- RING_BELL;
- READ_TEXT;
- COPY_NAME;
- LIGHT_LAMP;
- SHARE_MEAL;
- OBSERVE_SILENCE;
- RETURN_OBJECT;
- CLEAN_SITE;
- RECORD_TESTIMONY.

No action carries a supernatural effect by default.

### `belief_claim`

Uses existing claim/provenance architecture rather than a new truth system.

Examples:

- “the marker protects travelers”;
- “this path was first walked after a historical rescue”;
- “a certain Pokémon appears when the bell sounds”;
- “leaving food here brings good weather.”

Each remains attributed and confidence-scoped until independently verified.

### `practice_participation_record`

Stores what the player actually did:

- practice ID;
- date/time;
- route version;
- actions completed;
- companions/witnesses;
- interruptions;
- optional notes;
- resulting relationship/public-memory references.

It must not store an inferred belief such as `player_believes=true` unless the player explicitly chooses an authored dialogue position and the product later decides such stance tracking is desirable.

## Epistemic separation

The server must distinguish:

1. physical fact;
2. observed social practice;
3. historical documentation;
4. oral testimony;
5. interpretation;
6. metaphysical claim;
7. verified PTU/Caelo mechanical effect.

Mandatory invariants:

`PRACTICE_OBSERVED != BELIEF_TRUE`

`REPEATED_TRADITION != VERIFIED_ORIGIN`

`RITUAL_ITEM != MECHANICAL_ITEM_EFFECT`

`LEGENDARY_ASSOCIATION_CLAIM != LEGENDARY_PRESENCE`

`PLAYER_PARTICIPATION != PLAYER_BELIEF`

`ROUTE_CUSTOM != ACCESS_AUTHORITY`

## Access composition

A route practice reads the existing access-state layer.

Examples:

- OPEN: normal participation possible;
- OPEN_WITH_CONDITIONS: practice may continue with restrictions;
- OBSERVATION_ONLY: no object placement or removal;
- ESCORT_REQUIRED: participation requires authorized accompaniment;
- TEMPORARILY_CLOSED: ordinary route traversal cannot proceed;
- EMERGENCY_ACCESS_ONLY: ritual purpose does not override closure.

If participants adapt by using a shortened route, remote reading, symbolic stop or deferred date, that becomes a new practice edition or temporary variant. It does not retroactively rewrite the prior form.

## Material offerings and votive objects

All physical items retain ordinary provenance and custody.

Suggested states:

- OFFERED_IN_PLACE;
- TEMPORARY_DISPLAY;
- RETURN_EXPECTED;
- ARCHIVED;
- WEATHER_DAMAGED;
- REMOVED_FOR_SAFETY;
- CLEANUP_PENDING;
- DISPUTED_CUSTODY;
- LOST;
- RETURNED.

Rules:

- leaving an item does not transfer ownership unless the practice/institution explicitly defines transfer;
- food or biological material can create wildlife or sanitation consequences and must interact with ecology/care policy;
- valuable objects require custody rules;
- cleanup cannot silently erase provenance;
- Minecraft despawn cannot author item loss in canon.

## Evolving tradition

Each practice can have editions.

Example:

`practice.v1`: walk full Sendero, stop at three markers.

`practice.v2`: one marker inaccessible after a slide; participants use a documented alternate stop.

`practice.v3`: archive evidence changes the public explanation of marker two; the route continues with corrected signage.

This allows continuity without freezing culture.

## NPC posture

NPCs may have distinct relationships to the same practice:

- PARTICIPANT;
- CUSTODIAN;
- ORGANIZER;
- SKEPTICAL_PARTICIPANT;
- HISTORIAN;
- PRACTICAL_SUPPORT;
- OCCASIONAL_VISITOR;
- NONPARTICIPANT;
- CRITIC;
- UNCERTAIN.

These are social postures, not classes or alignments.

A Researcher can participate. A custodian can be unsure of the origin story. A person can value a tradition culturally without endorsing its supernatural explanation.

## Quest use

Good quest questions include:

- Can a practice continue safely after route damage?
- Which objects should remain, be archived or be returned?
- Why do two families describe the same stop differently?
- Does a public plaque overstate what the archive can prove?
- How should a tradition adapt to a wildlife window?
- Who has authority to close access, and who merely organizes participation?
- What happens when a recurring practice creates litter or attracts Pokémon?

Poor quest questions include:

- “prove the local god is real” unless canon/mechanics already establish that exact premise;
- “win a battle to become spiritually worthy” without explicit setting provenance;
- “collect ten offerings because the quest board needs collectibles.”

## Relationship effects

Participation may affect relationships through ordinary behavior:

- showing up when invited;
- respecting access rules;
- returning borrowed material;
- accurately preserving testimony;
- helping with cleanup;
- declining respectfully;
- challenging unsupported claims without humiliating participants.

There is no universal piety meter.

## Ecology interaction

A meaningful route may cross ecological corridors or seasonal activity windows.

The ecology layer remains authoritative for wildlife facts.

Examples:

- recurring human traffic changes detectability;
- food offerings attract ordinary scavenging behavior;
- a route is rescheduled to avoid a breeding or migration window;
- residents interpret a recurring Pokémon sighting as meaningful while Mirador records only the observation.

`ECOLOGICAL_CORRELATION != SACRED_CAUSATION`

## Battle handoff contract

Battle can occur during a meaningful journey, but the battle result is narrow.

Allowed examples:

- `IMMEDIATE_ROUTE_THREAT_WITHDREW`;
- `IMMEDIATE_CLEARING_SECURED`;
- `AUDITED_MATCH_COMPLETE`.

Forbidden automatic outputs:

- `RITUAL_ACCEPTED_BY_LEGENDARY`;
- `PLAYER_PROVED_WORTHY`;
- `BELIEF_CONFIRMED`;
- `ROUTE_BLESSED`;
- `HISTORICAL_ORIGIN_PROVED`;
- `CLOSURE_LIFTED`.

## Mechanically rich encounter template

### Full form: Procession Under Pressure

Premise: a recurring route event is underway when a localized Pokémon confrontation or panic develops near a narrow section. Participants, route restrictions and the integrity of the practice matter at the same time.

Capability dependencies:

- targeting/footprints/range/LoS: required;
- base movement legality: required;
- complete movement including push/pull/knockback/interception/forced movement: required if crowd protection, interception or displacement is modeled tactically;
- core calculations: required;
- action economy/initiative: required;
- full turn/round lifecycle: required for a sustained escort/protection objective;
- full stateful damage pipeline: required;
- status lifecycle: required if selected content applies statuses;
- terrain/weather/hazards/zones/reactions: required if narrow-route safety, hazards or reaction protection are tactical objects;
- move-specific behavior: exact roster audit required;
- abilities: exact roster audit required;
- items: exact roster audit required;
- Trainer Features/perks: exact roster audit required;
- AI legal-action infrastructure: required;
- AI tactical policy: required for objective-aware retreat/protection/path reasoning;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful in-world projection.

### Reduced form

The public group is moved to a safe world-state position before BattleSpec begins. Route access, ritual objects, crowd behavior and environmental risk remain outside combat authority. If combat is necessary, AutoPTU resolves one ordinary audited battle on stable terrain.

Allowed battle consequence:

`IMMEDIATE_ROUTE_THREAT_WITHDREW`

Afterward the world layer separately decides whether the route stays closed, the practice resumes, postpones or changes edition.

The reduced version preserves the narrative premise: a meaningful community journey was disrupted and had to adapt. It does not require the adapter to simulate an escort objective or the engine to invent unsupported zone/reaction rules.

## Minecraft/Cobblemon projection

Useful visual surfaces:

- route markers;
- lecterns/sign boards;
- temporary ribbons or lanterns;
- scheduled NPC movement;
- physical archive copies;
- cleanup objects;
- location discovery;
- ordinary Pokémon presentation actors when ecology authorizes them.

Authority boundaries:

- visual marker absence after chunk unload does not delete the practice;
- a Pokémon spawn near a marker does not prove a Legendary association;
- an item entity disappearing does not settle custody;
- NPC pathfinding failure does not cancel participation;
- client animation does not author ritual completion.

## Canon promotion checklist

Before any specific Ouros practice becomes canon, resolve:

- stable route/site IDs;
- who currently performs it;
- who organizes or maintains it;
- earliest evidence versus claimed origin;
- current public wording;
- material objects involved;
- cleanup/custody rules;
- access interaction;
- ecology interaction;
- whether any supernatural assertion is merely belief or actually supported by Caelo/PTU canon;
- implementation surfaces;
- reduced encounter path where necessary.

Until those fields are reviewed, all concrete examples remain proposals.