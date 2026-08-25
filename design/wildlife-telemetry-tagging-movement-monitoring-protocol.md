# Wildlife Telemetry, Tagging, and Movement-Monitoring Protocol

Status: PROPOSED / NON-CANON
Pass: 165
Authority type: subordinate observational protocol

## Authority statement

This protocol owns telemetry instrumentation and the provenance chain from device deployment to derived movement evidence. It does not own the ecological, legal, welfare, or tactical conclusions that may later use that evidence.

Existing authorities remain authoritative:

- Pokémon Agency: `pokemon_entity_id`, custody, partnership, release, and individual identity.
- Wild Migration: migration patterns, episodes, corridors, stopovers, and population-level movement interpretation.
- Wildlife Rehabilitation / Conservation: release, relocation, monitoring goals, and outcome assessments.
- Research Ethics: authorization, welfare conditions, permitted methods, and stop conditions.
- Metrology / Timekeeping: calibration, clocks, corrected timestamps, measurement standards, and uncertainty conventions.
- Radio / Wireless: communications infrastructure and propagation where relevant.
- Remote Sensing / Photography / Field Signs: their own observation types.
- Science: hypotheses, analyses, publications, and interpretation.
- Material Culture / Technology: physical recovered devices or institutional equipment where relevant.

Telemetry data may be consumed by those systems. It cannot silently overwrite them.

## Design goal

Represent the evidence produced by tracking devices without turning them into omniscient locators.

The authoritative chain is:

research authorization -> device configuration -> deployment -> observation opportunity -> raw detection -> QC/time correction -> derived fix -> movement-segment derivation -> ecological interpretation by another authority -> deployment end / tag loss / recovery -> archival history.

Every arrow is explicit. No stage proves the next one automatically.

## Primary entities

### `TELEMETRY_DEVICE`

Persistent identity of the physical instrument.

Suggested fields:

- `telemetry_device_id`
- device family / technology profile
- manufacturer/model only when canon defines them
- device serial / institutional identifier
- measurement channels
- nominal transmission/logging mode
- configuration revision
- calibration/reference links
- battery/power state observations
- physical condition observations
- owner/custodian institution
- current lifecycle state
- provenance / created-at / retired-at

The device is not the Pokémon.

### `DEVICE_DEPLOYMENT`

Links one device to one authorized subject for one bounded period.

Suggested fields:

- `deployment_id`
- `telemetry_device_id`
- `pokemon_entity_id` when identity is known
- authorization/protocol reference
- attachment/implant/site description at the level permitted by canon
- deployment start time
- planned retrieval/end conditions
- release-event link where applicable
- deployment status
- observed fit/condition notes
- uncertainty / incomplete metadata flags

A device can have sequential deployments. A Pokémon can have sequential devices.

### `RECEIVER_STATION`

Persistent receiver or listening site.

Suggested fields:

- `receiver_station_id`
- physical location revision
- antenna/sensor configuration revision
- operational history
- power/connectivity history
- clock-source link
- maintenance events
- owning institution
- visibility/public-access policy

### `RECEIVER_COVERAGE_REVISION`

Represents an estimated observation opportunity, not a guaranteed detection radius.

Suggested fields:

- `coverage_revision_id`
- receiver/station reference
- technology/profile
- method used to estimate coverage
- temporal validity
- environmental assumptions
- bearing/sector if directional
- confidence / uncertainty
- known blind zones
- calibration/test links

Never substitute battle range or battle LoS for this object.

### `TELEMETRY_DETECTION`

Immutable raw or minimally normalized detection event.

Suggested fields:

- `detection_id`
- `telemetry_device_id`
- receiver/source identifier
- raw timestamp
- corrected timestamp reference, if later produced
- signal / sensor fields supported by the device
- raw payload provenance
- ingest time
- quality flags
- duplicate / collision / parsing flags

Raw detections remain preserved if later interpretations change.

### `LOCATION_FIX`

Derived spatial estimate produced from one or more observations.

Suggested fields:

- `location_fix_id`
- input detection IDs
- processing revision
- timestamp / interval
- coordinate or coarse area
- uncertainty geometry / confidence class
- derivation method
- quality state
- reviewer / system provenance

A receiver hit may support a coarse area rather than a point.

### `DERIVED_MOVEMENT_SEGMENT`

A conservative relation between validated fixes.

Suggested fields:

- `movement_segment_id`
- subject/deployment reference
- start/end fix IDs
- interval
- inferred direction / minimum displacement when useful
- interpolation policy
- confidence
- explicitly unknown intermediate path

A straight line between fixes is not automatically the traversed path.

### `DEVICE_STATE_REVISION`

Tracks battery, configuration, damage, detachment suspicion, clock status, data backlog, and other device-level changes.

### `TAG_LOSS_CASE`

Supports suspected or confirmed detachment, loss, recovery, or device-subject reassociation problems.

Possible states:

- `SUSPECTED`
- `PROBABLE`
- `CONFIRMED_DETACHED`
- `RECOVERED`
- `UNRESOLVED`

This case can revise movement interpretation without rewriting detections.

### `MONITORING_SERIES`

Groups deployments, stations, detections, fixes, and analysis periods under a defined monitoring objective.

### `LOCATION_PRIVACY_POLICY`

Controls publication precision independently of scientific storage precision.

Examples:

- full institutional coordinates;
- restricted researcher access;
- broad public polygon;
- delayed publication;
- no public location while active;
- release/roost/nest redaction.

## Evidence semantics

### Device identity and subject identity

A tag code proves device identity when decoded correctly. It proves subject identity only through a valid deployment association that has not been superseded, confused, or invalidated.

Never use:

`telemetry_device_id == pokemon_entity_id`.

### Detection

A detection can support:

“device D was observed by receiver R at time T under quality state Q.”

It does not automatically support:

“Pokémon P was standing exactly at coordinate C.”

### Silence

`NO_DETECTION` requires an observation-opportunity context. A silence window should retain:

- which receivers were operational;
- whether their clocks were trustworthy;
- whether data uploads were complete;
- estimated coverage;
- tag battery/device state;
- environmental/propagation context where relevant;
- whether the subject could have moved beyond coverage.

Allowed conclusions include `UNRESOLVED`.

### Stationary signal

Repeated detections from one area may support a stationary-device hypothesis. They do not prove the Pokémon is stationary, injured, dead, nesting, resting, or captured.

### Tagged subset

Telemetry never supplies population abundance directly. `n tagged = n population` is forbidden.

Population and corridor authorities must combine telemetry with their own surveys and evidence.

### Derived movement

The segment between fixes can support displacement and timing bounds. Unless the method provides more, intermediate route geometry remains unknown.

## Quality and correction

Telemetry processing should be versioned.

Examples of later corrections:

- receiver clock offset discovered;
- station coordinates corrected;
- duplicate detections merged;
- erroneous tag association fixed;
- receiver moved without metadata update;
- outlier filter changed;
- coverage model revised;
- recovered tag proves detachment occurred before a supposed movement interval.

Corrections create new derived products. Raw records remain unchanged.

## Welfare and ethics

Deployment is not a neutral administrative action. Research Ethics must authorize methods and define stop conditions.

The protocol can record observations such as:

- device appears loose;
- repeated rubbing near attachment site;
- altered movement suspected;
- no observed issue during defined checks;
- individual refuses handling;
- monitoring was terminated early.

It cannot create a generic burden score or automatic mechanical penalty.

A tagging procedure must not silently grant custody or ownership. A wild Pokémon remains wild unless another authority records a legitimate state change.

## Privacy and sensitive ecology

Public telemetry products may be deliberately degraded. This is especially appropriate for:

- nesting sites;
- roosts;
- rehabilitation release locations;
- rare populations;
- culturally restricted sites;
- vulnerable dens;
- sensitive research stations.

A public map can be less precise than the authoritative scientific record without being false.

## Integration contracts

### Telemetry -> Wild Migration

Allowed handoff:

- tagged-individual detections/fixes;
- timing observations;
- crossings at receiver gates;
- uncertain movement intervals;
- monitoring effort / network coverage.

Migration decides whether this supports a corridor, stopover, wave, route revision, or individual exception.

### Telemetry -> Rehabilitation / Conservation

Allowed handoff:

- post-release detection series;
- last valid detection;
- site fidelity evidence;
- tag loss/device failure hypotheses;
- voluntary-return link;
- monitoring coverage.

Rehabilitation decides outcome assessment. `released + no signal` never equals death or failure.

### Telemetry -> Pokémon Agency

Only persistent identity association and explicit state transitions flow here. Device data cannot create partnership, custody, Loyalty, command authority, or capture eligibility.

### Telemetry -> Research Ethics

Ethics controls deployment authorization, permitted handling, welfare review, removal/termination conditions, and secondary use of sensitive tracking records.

### Telemetry -> Metrology / Timekeeping

Calibration, timing references, drift corrections, and instrument-quality conventions must be referenced rather than reimplemented.

### Telemetry -> Radio / Wireless

If a technology depends on radio infrastructure, the communications layer can provide network/propagation context. A communications coverage map remains distinct from a validated wildlife-detection coverage revision.

### Telemetry -> Remote Sensing / Science

Derived telemetry can be compared with aerial imagery, habitat products, surveys, and hypotheses. Neither system gets automatic causal authority over the other.

## Minecraft / Cobblemon projection

Minecraft is presentation and interaction, not telemetry truth.

Permitted projections:

- visible receiver mast or buoy;
- equipment cabinet;
- broad public monitoring polygon;
- technician interaction;
- recovered tag item representation;
- status indicator derived from server state;
- coarse historical movement visualization.

Forbidden authority inversions:

- loaded Pokémon coordinates become telemetry detections;
- despawn becomes signal loss;
- entity death becomes tag-mortality evidence;
- Minecraft compass/locator becomes scientific fix;
- redstone signal strength becomes radio signal strength;
- battle LoS becomes receiver coverage;
- chunk presence becomes population occupancy;
- client UI can move or fabricate historical fixes.

## PTU boundary

No new PTU rules are introduced by this protocol.

Explicitly forbidden inferences include:

- Tracker -> electronic telemetry range;
- Technology Education -> automatic tag deployment success;
- Perception -> receiver sensitivity;
- Lock-On / Odor Sleuth -> telemetry;
- Electric Terrain -> radio boost/interference;
- Psychic Pokémon -> remote sensing;
- tag attachment -> PTU Item effect;
- a signal -> initiative, Accuracy, surprise, target lock, capture bonus, or combat visibility.

Any exact PTU Feature, Item, Skill, Move, Ability, or Capability used by a future implementation must be verified independently against the project oracle/Caelo material.

## Failure modes the world must support

- battery expiry;
- device detachment;
- receiver power outage;
- receiver clock drift;
- receiver moved without metadata update;
- broken antenna / blocked hydrophone;
- data backlog with later upload;
- identifier collision or wrong deployment association;
- no receiver coverage;
- corrupted record;
- tag recovered far from the subject;
- research program ends while tags still exist;
- subject enters a sensitive location that becomes redacted publicly;
- monitoring finds nothing noteworthy.

None of these requires a villain or a battle.

## Persistence requirements

Telemetry history should survive:

- Pokémon despawn/reload;
- transfer/release where authorized identity persists;
- station rebuilds;
- map revisions;
- server restarts;
- research-program closure;
- public-map redaction changes;
- later discovery of clock or metadata error.

## Canon gate

Before this protocol becomes active canon, Ouros must decide which tracking technologies exist, which institutions can deploy them, what subject-protection rules apply, how precise public data can be, and whether any historical telemetry networks predate the players.

Until then, all devices, receiver arrays, institutions, and scenarios introduced by Pass 165 remain proposed.