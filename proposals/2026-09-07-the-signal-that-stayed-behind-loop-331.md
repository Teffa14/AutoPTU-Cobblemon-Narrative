# The Signal That Stayed Behind — Pass 331

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A long-running field study follows a small population of wild Pokémon with non-invasive tracking devices. One tagged individual stops producing ordinary movement fixes near a managed trail corridor.

A field receiver still detects the device. The signal appears strongest from the same drainage for multiple checks.

A public-facing movement map therefore marks the individual as stationary near that feature.

Later, a ranger reports a sighting that appears to place the same individual far outside the mapped area.

The quest begins before anyone decides which report is wrong.

## Narrative function

This loop tests a recurring Ouros principle in a new domain: evidence can be genuine while the interpretation built from it is incomplete.

The player is asked to reconstruct what each observation actually establishes and which later decisions relied on assumptions that were never independently verified.

## Persistent features

The exact region remains unresolved. The loop needs stable feature IDs for:

- a field station or research office;
- a monitored trail corridor;
- a forested or topographically enclosed signal basin;
- two or more receiver observation points;
- a public route or infrastructure feature affected by the movement interpretation;
- a likely device-recovery feature;
- an archive node containing deployment, maintenance and study records;
- at least one independent sighting location.

None of these locations become canon through this proposal.

## Persistent actors

Potential roles:

### Field researcher

Knows deployment identity, scheduled monitoring and the distinction between raw fixes and derived movement tracks.

Does not automatically know every maintenance action or public communication.

### Ranger / habitat steward

Knows local trail conditions, field sightings and safety obligations.

Does not automatically possess the research team's raw telemetry archive.

### Data analyst

Knows filtering rules, timestamp handling and uncertainty fields used to build the public movement product.

May never have visited the actual terrain.

### Infrastructure or land-management representative

Received a summarized corridor recommendation and used it for a planning decision.

May not know the uncertainty behind the map.

### Local recurring observer

Knows repeated place-level patterns and may have seen the same individual or group over time.

Their observation is still an observation with provenance, not automatic species expertise.

## Opening contradiction

The study ledger contains:

- several missing GPS fixes;
- repeated radio detections from the same general direction;
- a derived map showing the tagged individual remaining near one feature;
- a later independent sighting outside that feature;
- no verified direct observation of the subject during the interval represented by the stationary map.

Every record can remain authentic.

## Investigation structure

### First pass: separate device from subject

The player checks whether the records establish that the transmitter was active, that the device was attached, or that the Pokémon itself was present.

These are separate claims.

### Second pass: reconstruct observation geometry

Receiver observations preserve observer location, time and directional result. Multiple observations can constrain a likely signal area without converting one strong bearing into exact position.

### Third pass: inspect device history

Deployment date, expected release interval, maintenance notes, attachment condition and any intervention records are checked.

### Fourth pass: compare the track with independent evidence

The player compares the derived track against sightings, habitat observations, camera or field records if authored, and later device recovery.

### Fifth pass: trace institutional consequence

The movement map may have influenced a temporary closure, construction timing, habitat buffer, patrol route, research priority or public notice. The player identifies which decision remains justified after the evidence is revised.

## Open explanations

The proposal does not preselect one answer.

Possible explanations include:

- the device released normally and remained where it fell;
- the device snagged on vegetation or infrastructure;
- an attachment failed early;
- GPS fixes failed more often in one terrain band while radio detection continued;
- one dataset was delayed and compared against a later field observation;
- the public map used filtered positions that exaggerated apparent stationarity;
- the independent sighting was of the correct individual but the identification confidence was lower than initially reported;
- several of these occurred together.

Deliberate tampering is possible only if later authored evidence supports it. It is not the default explanation.

## Consequences

A strong outcome does more than locate a collar.

The player may cause:

- a public map revision;
- a correction to a habitat-use assumption;
- retrieval of stored data from a detached device;
- a new monitoring protocol requiring uncertainty metadata;
- a revised infrastructure schedule;
- a reopened trail segment while another remains monitored;
- a follow-up study focused on the terrain band where fixes failed;
- changed trust between a field team and a planning institution without reducing either side to incompetence.

A later revisit can show whether the revised interpretation predicted new observations better than the original one.

## NPC knowledge rules

The field researcher does not gain the ranger's sighting until it is communicated.

The analyst does not gain attachment-condition knowledge merely because they have the device ID.

The land-management representative may know only the published corridor map and recommendation.

The local observer does not gain the study's full history because they witnessed the subject.

A correction is a new communicative event with its own recipients.

## Reduced playable version

The reduced version requires no live telemetry simulation.

World state stores:

- `TAGGED_SUBJECT_ID`;
- `DEVICE_ID`;
- attachment state when authoritatively known;
- raw fix observations;
- failed-fix events;
- radio-bearing observations;
- derived track versions;
- independent sightings;
- device recovery;
- publication/revision lineage;
- explicit recipients and belief updates;
- feature-scoped institutional decisions.

Device transmissions and fix attempts happen between scenes through semantic world events.

If combat occurs, it uses an ordinary static tactical map. The combat result cannot decide telemetry truth.

## Full encounter version

A richer optional field encounter could involve reaching a receiver site while wild Pokémon move through the area, protecting equipment, maintaining observation positions, escorting a researcher, or responding to an actual injured subject discovered independently of the telemetry assumption.

Potential mechanical dependencies:

- targeting / footprints / range / LoS for foliage, elevation or intermittent visibility beyond ordinary verified LoS;
- base movement legality for ordinary traversal only;
- complete movement for pushes, falls, rescue, interception or forced displacement;
- core calculations for ordinary deterministic combat math;
- action economy / initiative for ordinary combat sequencing;
- full turn / round lifecycle for timed signal windows, environmental phases or delayed events inside combat;
- full stateful damage pipeline for fall, impact or environmental damage;
- status lifecycle for any persistent exposure or field condition;
- terrain / weather / hazards / zones / reactions for dense cover, storms, unstable ground, moving hazards or reactive protection;
- move-specific behavior for any Move used to alter terrain, sensing, visibility or displacement;
- abilities for any claimed sensing, tracking, terrain or weather interaction;
- items for any tactical tracking or protection device effect;
- Trainer Features / perks for any tracking, research, command or interrupt effect;
- AI legal-action infrastructure for ordinary legal choices;
- AI tactical policy for escort, retreat, protect-equipment, rescue and observation-under-threat behavior;
- Minecraft / Cobblemon / Craftics adapter/playback for presenting authoritative positions, devices and results without becoming the rules authority.

## Canon questions left open

- region and biome;
- tagged species;
- study institution;
- reason the study exists;
- device technology and visual form;
- whether the device stores local data;
- who owns retrieval obligations;
- which infrastructure decision was affected;
- whether the independent sighting is ultimately confirmed;
- final cause of the stationary signal;
- whether any tactical encounter is needed.
