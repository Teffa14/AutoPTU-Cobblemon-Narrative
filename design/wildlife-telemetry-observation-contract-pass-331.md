# Wildlife Telemetry Observation Contract — Pass 331

Status: PROPOSED SYSTEMS DESIGN. Not Ouros canon.
Date: 2026-09-07

## Purpose

This contract defines how Ouros can represent tracking-device evidence without turning a transmitter, map marker or Minecraft entity into omniscient world truth.

It supports wildlife research, recurring NPC investigations, institutional decisions and later correction while preserving provenance.

## Core authority chain

`persistent subject identity -> device assignment -> device state -> raw observation -> derived estimate -> analyst interpretation -> explicit recipient -> decision -> consequence -> follow-up evidence`

Each stage is separately queryable.

## Required entities

### Tagged subject

A persistent wild Pokémon identity or population member.

Fields should support:

- stable subject ID;
- species identity when canonized;
- study enrollment state;
- device assignments by semantic time;
- known handling/intervention events;
- last verified direct observation;
- current authoritative world state owned outside Minecraft presentation.

### Tracking device

Fields should support:

- stable device ID;
- device kind;
- assigned subject ID;
- deployment time;
- expected service/release interval if authored;
- attachment state when known;
- operating state when known;
- recovery state;
- provenance for every state change.

### Raw telemetry observation

A raw observation records what the system or observer actually obtained.

Possible kinds:

- `GPS_FIX`;
- `GPS_FIX_FAILED`;
- `RADIO_BEARING`;
- `SIGNAL_STRENGTH_OBSERVATION`;
- `DEVICE_STATUS_PACKET`;
- `DIRECT_DEVICE_RECOVERY`.

Required provenance includes:

- observation ID;
- device ID;
- semantic time;
- observer or receiver identity;
- observer position where relevant;
- raw value;
- uncertainty/quality metadata where available;
- source root;
- ingest time distinct from observation time when delayed delivery is possible.

### Derived location estimate

A triangulation, cleaned GPS point, movement segment or public map feature is derived evidence.

Required fields:

- estimate ID;
- source observation IDs;
- derivation method/version;
- semantic interval represented;
- uncertainty representation;
- analyst or process identity;
- publication lineage if exposed externally.

The source observations remain intact when a derived estimate is revised.

## Invariants

`TAGGED_SUBJECT_ID != DEVICE_ID`

`DEVICE_LOCATION != SUBJECT_LOCATION`

`DEVICE_TRANSMITTING != DEVICE_ATTACHED`

`GPS_FIX_FAILED != SUBJECT_ABSENT`

`RADIO_BEARING != EXACT_LOCATION`

`STRONG_SIGNAL != DIRECT_SIGHTING`

`LAST_KNOWN_POSITION != CURRENT_POSITION`

`DERIVED_TRACK != RAW_OBSERVATION_SET`

`FILTERED_TRACK != COMPLETE_TRACK`

`COLLAR_RECOVERED != SUBJECT_RECOVERED`

`STATIONARY_DEVICE != MORTALITY_CONFIRMED`

`MINECRAFT_ENTITY_POSITION != CANONICAL_STUDY_HISTORY`

## Observation-time and receipt-time separation

Telemetry can arrive late.

A stored fix observed at semantic time `T1` and uploaded at `T3` remains evidence about `T1`.

An NPC receiving the upload at `T3` cannot use it for a decision made at `T2` unless a separate earlier delivery exists.

This must integrate with the existing global information runtime rather than creating a hidden broadcast path.

## Missing-data rule

Missing observations remain missing.

The world layer may store why a fix failed when authoritatively known, but the analyst may not know that cause.

A renderer must never interpolate an authoritative subject route across a data gap unless the world simulation independently owns that movement history.

A visual dotted line may present a derived hypothesis only if labeled as such in the underlying data model.

## Device-detachment rule

Attachment is a stateful relation between subject and device.

Once detached:

- the device may continue transmitting;
- the subject retains persistent identity;
- future device observations describe the device unless another source re-establishes attachment;
- old derived tracks remain historical products with provenance;
- institutions may need corrections, retrieval or revised decisions.

Detachment does not retroactively invalidate fixes obtained while attachment was verified.

## Triangulation rule

Radio bearings are directional observations from specific receiver positions and times.

A derived estimate may combine multiple bearings. The estimate must preserve the source set and the temporal window used.

Bearings collected too far apart in time may be inappropriate for a single moving subject estimate. Whether a specific combination is acceptable is an authored research-policy question, not a PTU combat rule.

## Publication and belief boundary

A movement map, alert or corridor recommendation is a publication event.

Publication does not imply universal receipt.

Receipt does not imply belief.

A corrected map is a new revision with explicit audience expansion through the existing publication system.

NPC belief should be recomputed from the evidence each NPC actually has.

## Institutional decision boundary

A decision should reference the evidence product it used, for example:

- derived track version;
- direct sighting report;
- field-receiver summary;
- device-recovery report;
- study protocol version.

When evidence changes, the prior decision remains historical. A review creates a new decision and lineage rather than silently rewriting the old one.

## World-agent AI integration

The global planner may use telemetry-derived claims only when the actor possesses them through explicit knowledge state.

Potential intents include:

- inspect a receiver site;
- retrieve a device;
- request raw observations;
- compare map revisions;
- verify a sighting;
- notify a land manager;
- postpone a decision pending uncertainty;
- schedule follow-up monitoring.

The planner does not get direct access to hidden subject location merely because a tracking study exists.

## AutoPTU boundary

Telemetry evidence remains outside tactical rule authority.

A battle handoff may include a world-authored subject identity and a static starting position when the subject is actually present and the encounter is triggered.

The handoff must not infer starting position from a stale transmitter location.

Combat results return through the existing semantic result ingress contract. AutoPTU does not rewrite historical telemetry observations.

## Reduced implementation contract

A reduced playable version can ship with:

- authored device assignments;
- between-scene fix/bearing events;
- explicit observation timestamps;
- delayed receipt where useful;
- derived map versions;
- independent direct sightings;
- device recovery;
- NPC knowledge and belief lineage;
- feature-scoped institutional consequences;
- static combat maps when combat is needed.

No live radio propagation, GPS physics, path interpolation or Minecraft tracking simulation is required.

## Full-version capability dependencies

### targeting / footprints / range / LoS

Ordinary verified contracts are usable. Dense foliage, sensor-like target acquisition, intermittent visibility or special concealment require additional verified support.

### base movement legality

Ordinary audited movement remains usable. Specialized climbing, swimming, squeezing or difficult terrain cannot be inferred.

### complete movement

Required for pushes, pulls, knockback, falls, rescue, interception, forced displacement or moving-subject interactions beyond base movement.

Current expectation: PARTIAL.

### core calculations

Ordinary deterministic calculations are usable. Telemetry accuracy is not a combat calculation unless separately authored and verified.

### action economy / initiative

Ordinary audited primitives are usable.

### full turn / round lifecycle

Required for timed observation windows inside combat, delayed events, recurring environmental pulses or scheduled equipment behavior.

Current expectation: PARTIAL.

### full stateful damage pipeline

Required for fall, impact, machinery or environmental damage.

Current expectation: PARTIAL.

### status lifecycle

Required for any persistent tactical exposure or condition.

Current expectation: PARTIAL.

### terrain / weather / hazards / zones / reactions

Required for rich foliage fields, storms, unstable ground, environmental triggers, reactive protection or changing observation areas.

Current expectation: MIXED / PARTIAL / BLOCKING by subfamily.

### move-specific behavior

Every Move used for sensing, terrain alteration, pursuit, concealment, displacement or rescue is individually gated.

### abilities

No Ability gains tracking, signal detection, navigation or sensing authority from flavor alone.

### items

No tracking receiver, collar or research device receives PTU tactical effects without an adopted rules source and implementation evidence.

### Trainer Features / perks

No research, tracking, command or interrupt Feature is inferred from narrative role. Each remains individually gated.

### AI legal-action infrastructure

Ordinary audited legal-action infrastructure remains usable.

### AI tactical policy

Rich escort, rescue, protect-equipment, pursuit, retreat and observation-under-threat behavior remains blocked until policy support is verified.

### Minecraft / Cobblemon / Craftics adapter/playback

May present authoritative devices, field actors, observations and battle playback. It may not become a telemetry, movement, sensory, knowledge or rules engine.

## PTU / Caelo boundary

Current narrative source inventory exposes comparative Kairos material. No adopted `sources/caelo` source was found during Pass 331 inspection.

This contract therefore defines data and provenance only. It does not define tracking checks, device ranges, movement modifiers, sensing bonuses, capture behavior, Moves, Abilities, Items or Trainer Features.
