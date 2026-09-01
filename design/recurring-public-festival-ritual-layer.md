# Ouros Recurring Public Festival and Ritual Layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01
Research basis: `research/2026-09-01-festivals-ritual-trials-public-memory-scan-175.md`

Purpose: define how a settlement-scale public event can recur, change, preserve memory and create playable work without introducing duplicate calendar, quest, relationship, communication or public-memory systems.

## Existing systems retained

This layer composes existing ownership:
- calendar/date state: existing world calendar/event systems;
- world facts and claims: existing case/investigation/world-agency systems;
- public communication: `design/media-communications-information-layer.md`;
- local knowledge: `design/local-knowledge-claim-propagation-layer.md`;
- public historical persistence: existing public-memory layer;
- service tasks: existing service-dispatch/request-board layer;
- questline taxonomy: canonical questline taxonomy;
- relationship state: existing persistent relationship systems;
- battle resolution: AutoPTU handoff only.

It owns only the lifecycle and composition rules for recurring public events.

## Event lifecycle

Suggested lifecycle:

`PLANNING -> SETUP -> OPEN -> PEAK -> CLOSING -> CLEANUP -> AFTERMATH -> ARCHIVED -> NEXT_EDITION_PLANNING`

Each phase may expose different locations, NPC routines, postings, public information packets and quests.

A yearly or seasonal recurrence creates a new edition record rather than resetting the previous event.

```yaml
public_event_edition:
  event_series_id: null
  edition_id: null
  calendar_window: null
  phase: PLANNING
  host_institution_ids: []
  participating_actor_ids: []
  active_site_ids: []
  public_program_ids: []
  operations_request_ids: []
  claim_refs: []
  incident_refs: []
  relationship_consequence_refs: []
  public_memory_refs: []
  inherited_from_edition_id: null
  unresolved_changes: []
```

## Series identity vs edition state

The event series is persistent cultural identity.
The edition is one occurrence.

Examples of edition-level change:
- a route is unavailable this year;
- a vendor does not return;
- a resident takes a new role;
- an archive label is revised;
- weather moves one activity indoors;
- a previous accident changes safety procedure;
- a player-created relationship affects access to a behind-the-scenes task.

The event must not silently return to a pristine default after the edition closes.

## Public program model

A program item should have an authored function and operational owner.

```yaml
public_program:
  program_id: null
  event_series_id: null
  program_type: EXHIBITION
  site_id: null
  owner_actor_or_faction_id: null
  participation_mode: OPTIONAL
  prerequisite_refs: []
  claim_refs: []
  service_dependency_refs: []
  battle_handoff_contract_id: null
  completion_outputs: []
```

Suggested program types:
- `EXHIBITION`
- `GUIDED_WALK`
- `PUBLIC_MEAL`
- `ARCHIVE_DISPLAY`
- `SKILL_DEMONSTRATION`
- `NONCOMBAT_TRIAL`
- `AUDITED_BATTLE`
- `STORY_CIRCLE`
- `MARKET_PROGRAM`
- `CARE_OR_SAFETY_STATION`

## Operational reality

A festival is also work.

Possible operational threads:
- supply arrivals and shortages;
- temporary route signs;
- ferry scheduling;
- accessibility accommodations;
- clinic readiness;
- equipment inspection;
- stall allocation;
- archival loan custody;
- cleanup;
- crowd communication;
- weather relocation.

These should reuse service dispatch and existing institutional responsibilities.

A problem becomes a quest only when an actor has knowledge, mandate and a reason to ask the player.

## Cultural-memory model

A program can reference an existing `claim_id`, archive record or public-memory record.

The event never upgrades a remembered story into world truth by repetition.

Possible knowledge states during an edition:
- public version remains current;
- archived correction exists but has not reached program copy;
- hosts disagree about wording;
- old version is retained with an annotation;
- a ceremonial retelling intentionally simplifies a complex event;
- evidence is insufficient to choose between variants.

Required invariant:

`REPEATED_TRADITION != VERIFIED_CAUSAL_HISTORY`

## Ritual objects and replicas

A ceremonial object may be:
- an original artifact;
- a documented replica;
- a teaching model;
- a reconstructed object;
- a symbolic prop.

Its provenance must be explicit.

`CEREMONIAL_IMPORTANCE != HISTORICAL_AUTHENTICITY`

A replica can matter socially without inheriting the mechanical or historical properties of an original.

## Noncombat trial design

Preferred early implementations should use server-observed world state that does not require battle rules.

Examples:
- visit markers in correct sequence;
- compare two archive sources and identify their differing dates;
- deliver sealed items without opening them;
- match route observations to map locations;
- coordinate pickup/dropoff windows;
- inspect temporary structures and report visible defects;
- carry out a guided observation route;
- identify which public claim has been superseded.

These can be audited through quest objective state, location discovery, inventory provenance or interaction logs.

## Audited battle program

A battle exhibition or challenge remains a normal battle handoff.

Full version may require:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if ring-out, push/pull, interception or protected zones matter;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle for round-scored or timed formats;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions if festival arena rules use them;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy if opponents must pursue event-specific objectives;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced implementation:
- no ring-out mechanics;
- no crowd buffs;
- no festival-only combat modifiers;
- no dynamic arena hazards;
- no escort/protected-object objective;
- no tactical AI requirement beyond legal ordinary action selection;
- exact participants and mechanics audited individually;
- AutoPTU result can write only the explicitly contracted exhibition outcome.

## Ritual route encounter

Candidate pattern: a ceremonial route uses part of Sendero del Vidrio. A localized wild Pokémon encounter interrupts passage.

Full version dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if civilians, procession spacing, interception, retreat corridors, push/pull or knockback are represented tactically;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle if safe-passage windows span rounds;
- full stateful damage pipeline;
- status lifecycle for selected Moves;
- terrain/weather/hazards/zones/reactions if route surface or weather affects battle;
- exact Moves, Abilities, Items and Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for corridor blocking/protection behavior;
- adapter/playback.

Reduced version:
- procession members remain outside BattleSpec;
- route observation and evacuation resolve in narrative state;
- if combat is needed, an ordinary audited battle occurs in a cleared encounter area;
- allowed battle output is only `IMMEDIATE_EVENT_ROUTE_CLEAR`;
- victory cannot establish ecological cause, historical meaning or future route safety.

## Current capability posture

Live read-only evidence inspected at AutoPTU-Java `8e5204b19f4aa83d96c573635be52c6e0e9092a3`.

VERIFIED for covered contracts:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING as complete families:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

The latest Java change adds generic candidate-step constraints and Shadow Tag forced-movement execution parity. It strengthens one forced-movement path but does not prove complete movement as a family.

## Relationship consequences

Public events can create relationship consequences through authored interactions:
- accepting or refusing a duty;
- correcting someone publicly or privately;
- helping an NPC recover from an operational failure;
- sharing credit;
- returning a borrowed item;
- choosing whose version of a disputed story to amplify.

Relationship state may change access or later dialogue. It cannot decide historical truth or battle legality.

## Edition-to-edition memory

At close, write an aftermath packet containing only actual observed outcomes:
- attendance/public participation facts if tracked;
- program completions;
- incidents;
- service failures/resolutions;
- archive/public-memory revisions;
- NPC role changes;
- damaged/repaired infrastructure;
- unresolved disputes;
- player relationship consequences.

The next edition may read these refs during planning.

## Validation targets

Future validation should reject:
- edition IDs with missing event series;
- program sites outside the event’s reachable map graph without an explicit transport edge;
- battle programs lacking a handoff contract;
- public historical claims with no provenance refs;
- replicas treated as originals without explicit canon promotion;
- operational requests whose issuer lacks knowledge/mandate;
- next-edition inheritance loops;
- cleanup that deletes history rather than closing active state.

## Promotion boundary

This file creates no festival, holiday, ritual, historical event, artifact or regional calendar fact. Specific event names, dates, meanings and historical referents remain proposals until canon review.
