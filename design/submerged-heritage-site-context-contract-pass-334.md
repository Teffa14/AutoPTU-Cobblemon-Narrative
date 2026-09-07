# Submerged Heritage Site-Context Contract — Pass 334

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-07

## Purpose

Provide a reusable world-state contract for submerged or intertidal material where object identity, site context, historical interpretation, ecological use, access, recovery and custody must remain separable.

The contract supports `The Timber Without a Wreck` and future ruins, wrecks, drowned infrastructure, old landings or detached material without assuming that every such feature is loot, a dungeon or a legal salvage opportunity.

## Authority boundary

World state owns persistent feature/object identity, observations, archive evidence, provenance, interpretations, access decisions, recovery decisions and custody lineage.

AutoPTU owns tactical legality and battle outcomes when a structured encounter is requested.

Minecraft/Cobblemon/Craftics renders authoritative state. A block break, item pickup, despawn, entity path or client-side object interaction cannot establish canonical recovery, destroy an archaeological site, change ownership, prove identity or alter NPC knowledge.

## Core entities

### HeritageObject

Fields should include:

- `object_id`;
- `object_class_observed`;
- `first_authoritative_observation_event_id`;
- `current_world_state`;
- `current_custody_state`;
- `mark_observations[]`;
- `condition_observations[]`;
- `position_observations[]`;
- `relationship_claim_ids[]`;
- `recovery_event_id`, nullable.

`object_class_observed` is descriptive evidence, not automatic historical identity.

### SubmergedSite

Create only when evidence establishes a coherent site feature worth tracking.

Fields:

- `site_id`;
- `site_kind_claims[]`;
- `spatial_extent_revision_ids[]`;
- `component_observation_ids[]`;
- `ecology_observation_ids[]`;
- `hazard_observation_ids[]`;
- `access_decision_ids[]`;
- `survey_event_ids[]`;
- `interpretation_claim_ids[]`.

A detached object can exist indefinitely without a `SubmergedSite` record.

### ObjectSiteRelationshipClaim

Fields:

- `claim_id`;
- `object_id`;
- `candidate_site_id`, nullable;
- `relationship_type` such as `POSSIBLE_COMPONENT_OF`, `LIKELY_COMPONENT_OF`, `DOCUMENTED_REMOVAL_FROM`, `NO_CURRENT_MATCH`;
- `evidence_ids[]`;
- `confidence`;
- `author_actor_id`;
- `semantic_time`;
- `supersedes_claim_id`, nullable.

No relationship claim rewrites object observations.

### SiteSurveyRevision

Fields:

- `survey_revision_id`;
- `site_id`;
- `semantic_time`;
- `method_descriptor`;
- `observed_component_positions[]`;
- `coverage_descriptor`;
- `uncertainty_notes[]`;
- `source_event_ids[]`;
- `author_actor_id`.

A later survey adds a revision. It does not mutate the historical survey into information nobody possessed at the time.

### ArchiveEvidence

Use the repository's existing archive and information boundaries.

A record lookup result should identify:

- searched collection;
- search semantic time;
- returned record IDs;
- failed/no-match result when applicable;
- actor who performed or received the lookup;
- interpretive claims kept separately from the record itself.

`RECORD_MATCH != UNIQUE_OBJECT_IDENTIFICATION`.

### StewardshipDecision

Generic world decision fields:

- `decision_id`;
- `feature_or_site_id`;
- `decision_type`;
- `scope`;
- `evidence_ids[]`;
- `decision_actor_id`;
- `semantic_time`;
- `review_condition`;
- `supersedes_decision_id`, nullable.

Possible authored decision types can include `MONITOR`, `LIMIT_ACCESS`, `ALLOW_NON_INTRUSIVE_SURVEY`, `REQUEST_SPECIALIST_REVIEW`, `RECOVER_SPECIFIC_OBJECT`, `LEAVE_IN_PLACE`, or equivalent future canon vocabulary. Their legal authority must be separately canonized before use as institutional powers.

### RecoveryEvent

Create only after world/canon authority permits recovery.

Fields:

- `recovery_event_id`;
- `object_id`;
- `source_feature_id`;
- `semantic_time`;
- `authorizing_decision_id`;
- `recovery_method_descriptor`;
- `receiver_actor_or_institution_id`;
- `initial_custody_event_id`;
- `condition_before_observation_id`;
- `condition_after_observation_id`, nullable.

`RECOVERY_EVENT != HISTORICAL_INTERPRETATION`.

## Required invariants

`OBJECT_FOUND != WRECK_FOUND`

`OBJECT_AUTHENTICATED != PARENT_SITE_IDENTIFIED`

`DETACHED_OBJECT_LOCATION != ORIGINAL_SITE_LOCATION`

`CURRENT_SITE_MAP != ETERNAL_SITE_GEOMETRY`

`ARCHIVE_MATCH != UNIQUE_IDENTITY`

`SITE_DISCOVERED != SITE_SAFE_TO_ENTER`

`SITE_ACCESSIBLE != OBJECT_RECOVERY_AUTHORIZED`

`OBJECT_RECOVERABLE != OBJECT_SHOULD_BE_RECOVERED`

`ECOLOGICAL_OCCUPANCY != HISTORICAL_INTERPRETATION`

`HAZARD_STATE != HERITAGE_VALUE`

`RECOVERED_OBJECT != CLAIM_PROVEN`

`MINECRAFT_PICKUP != CANONICAL_RECOVERY`

`MINECRAFT_BLOCK_STATE != SITE_INTERPRETATION`

## Knowledge and NPC integration

The global NPC information model remains authoritative.

An NPC can act on:

- direct observation;
- a received survey result;
- a received archive copy;
- a received interpretation;
- an explicit institutional instruction;
- accessible personal memory.

An NPC cannot act on hidden site truth, another NPC's private archive finding or an unpublished survey merely because both belong to the same institution.

Possible world-agent intents:

- `DOCUMENT_OBJECT`;
- `REQUEST_ARCHIVE_LOOKUP`;
- `DELIVER_RECORD_COPY`;
- `COMPARE_SITE_REVISION`;
- `REQUEST_NON_INTRUSIVE_SURVEY`;
- `RESTRICT_FEATURE_ACCESS`;
- `REQUEST_SPECIALIST_RECOVERY`;
- `MONITOR_EXPOSED_COMPONENT`;
- `CORRECT_PUBLIC_IDENTIFICATION`.

These are narrative/world intents unless a structured tactical action is explicitly handed to AutoPTU.

## Site formation and movement history

Detached material can move while retaining identity.

Represent movement as observations/events rather than continuously simulated physics when rich environmental implementation is unavailable:

`OBJECT_AT_A(T1)`

`STORM_OR_TRANSFER_EVENT(T2)`

`OBJECT_AT_B(T3)`

The inference `A -> B because of the storm` remains a claim unless the authored event actually establishes that causal movement.

This prevents current position from silently rewriting source context.

## Ecological overlay

A submerged ruin can acquire ecological functions after abandonment.

Store direct ecological observations separately from historical interpretation. Examples can include observed nesting, sheltering, feeding or vegetation use when species-grounded evidence exists.

No Pokémon behavior, Ability, Move, terrain bonus or encounter modifier follows automatically from the statement that a site is habitat.

## Reduced implementation contract

The reduced implementation requires no underwater tactical simulation.

World layer can author:

- shoreline object discovery;
- persistent object identity;
- timed position/condition observations;
- archive queries and document copies;
- interview evidence;
- non-intrusive remote survey results;
- survey-map revisions;
- ecological observations;
- site access decisions;
- later specialist recovery/conservation events;
- publication and correction events;
- explicit per-NPC receipt and belief changes.

If combat occurs near the investigation, use ordinary static legal geometry and existing verified tactical primitives. Unsafe or unsupported aquatic spaces remain inaccessible geometry.

## Full tactical implementation contract

A physical underwater/site encounter can only activate mechanics supported by current AutoPTU evidence.

Potential rich dependencies:

- water-mediated LoS and visibility: targeting/footprints/range/LoS;
- Swim/Dive or unusual traversal: base movement legality plus exact movement capability evidence;
- currents, dragging, rescue, interception, knockback: complete movement;
- ordinary combat arithmetic: core calculations;
- custom survey/recovery actions: action economy/initiative plus explicit action definitions;
- timed survey windows, environment phases, delayed collapse: full turn/round lifecycle;
- impact/collapse/environmental damage: full stateful damage pipeline;
- persistent restraint/exposure: status lifecycle;
- unstable structure, currents, debris, environmental zones/reactions: terrain/weather/hazards/zones/reactions;
- every structure- or water-interacting Move: move-specific behavior;
- every proposed aquatic/sensing/protection Ability: abilities;
- every dive/survey/recovery tool: items;
- any Researcher/Chronicler/Survivalist or specialist mechanical benefit: Trainer Features/perks;
- ordinary legal battle selection: AI legal-action infrastructure;
- preserve-site, escort, withdraw, protect-specialist and non-defeat objectives: AI tactical policy;
- rendering/playback without rules duplication: Minecraft/Cobblemon/Craftics adapter/playback support.

## Failure boundaries

The system must fail closed when:

- a player attempts to infer a unique wreck identity from a non-unique mark;
- an object is physically picked up in Minecraft without an authorized world recovery event;
- a map revision is treated as omniscient site geometry;
- a renderer despawn is interpreted as artifact loss;
- an NPC receives a summary and is credited with source documents never delivered;
- an underwater encounter requests unsupported movement/hazard mechanics;
- a narrative tool tries to invent salvage ownership, legal powers or item value;
- a Pokémon flavor description is converted into aquatic rescue/sensing mechanics without authoritative rules evidence.

## Reuse targets

This contract can later support wrecks, drowned bridges, submerged settlements, old ferry landings, storm-exposed timbers, lost cargo assemblages, archaeological features, cultural sites and historical waterfront infrastructure.

It should not become a generic ownership/legal system. Those domains need their own canon and authority contracts.