# Pass 165 — Wildlife telemetry, tagging, and movement-monitoring scan

Status: RESEARCH / NON-CANON
Date: 2026-08-25
Writable repository: AutoPTU-Cobblemon-Narrative only

## Purpose

This pass examines wildlife telemetry and tagging as a provenance problem rather than as a new ecology authority. Existing Ouros design already owns migration, release monitoring, conservation interpretation, individual Pokémon identity, research ethics, metrology, timekeeping, remote sensing, and communications. The missing layer is the instrument chain between a device deployed on an individual and the later scientific claims derived from detections.

The intended Ouros boundary is therefore narrow:

physical device -> deployment -> receiver/network opportunity -> raw detection -> quality/time correction -> location or movement inference -> handoff to the existing ecological authority.

The protocol proposed by this pass must not decide migration corridors, rehabilitation success, population abundance, ownership, custody, cause of death, or battle state.

## Existing-repository audit

The repository was inspected before writing. Relevant existing authorities include:

- Wild Migration: corridor identity, migration episodes, stopovers, movement waves, partial participation, and interannual interpretation.
- Wildlife Rehabilitation / Release Monitoring: release readiness, release attempts, post-release monitoring, voluntary return, and outcome assessment.
- Pokémon Agency: persistent individual identity, custody, partnership, release, and behavioral observations.
- Research Ethics: authorization, welfare stop conditions, site permission, and subject protection.
- Metrology and Timekeeping: instrument calibration, measurement provenance, clock drift, corrected time estimates, and reference revisions.
- Radio/Wireless Propagation: communications infrastructure and coverage, without granting ecological truth.
- Remote Sensing: repeated area acquisitions and spatial products, distinct from individual-device telemetry.
- Photography / Visual Records: image provenance and camera-trap observations.

Telemetry is referenced by several of those systems, but no dedicated authority was found that separates tag identity, receiver identity, deployment state, raw detections, coverage gaps, tag loss, and derived movement fixes. Pass 165 therefore proposes a subordinate protocol instead of a second migration or rehabilitation layer.

## External research findings

### Motus Wildlife Tracking System

Motus uses uniquely coded radio tags and strategically placed receiver stations. A station records a detection when a tagged animal is within usable range; the stored record can include time, signal strength, and receiving antenna. Motus explicitly treats receiver placement and coverage as part of the method. Range depends on configuration and conditions, and the network can preserve detections even when data are uploaded later.

Reusable Ouros lessons:

1. A detection belongs to a tag-receiver interaction, not directly to a perfect map coordinate.
2. Receiver coverage determines what could have been observed. No detection outside useful coverage says little about the animal.
3. Signal strength, antenna, timestamp, and station metadata belong in provenance.
4. Station maintenance and network growth can change apparent movement patterns even when animal behavior is unchanged.
5. Raw detections should remain archived after later interpretation changes.

Sources:
- Motus, “How Motus Works”: https://motus.org/resources/how-motus-works/
- Motus, “Information for Researchers”: https://motus.org/get-involved/information-for-researchers/
- Motus resources / station documentation: https://motus.org/resources/

### NOAA acoustic telemetry

NOAA describes tags attached or implanted in animals and arrays of receivers placed at selected locations. When a tagged animal moves near a receiver, the receiver records that presence. Multiple receiver locations over time can support inferences about migration, site fidelity, and habitat use.

This is useful because the evidence remains discrete. A receiver gate can establish that a tagged individual passed near that array during a time window; it does not reveal every intermediate path. The same tagged animal can also go undetected because it never entered receiver range, because a receiver failed, or because its tag stopped transmitting.

Sources:
- NOAA Fisheries, passive acoustic technologies / transmitting telemetry tags: https://www.fisheries.noaa.gov/new-england-mid-atlantic/science-data/passive-acoustic-technologies
- NOAA Fisheries, Chesapeake Bay acoustic telemetry arrays: https://www.fisheries.noaa.gov/feature-story/tracking-fish-chesapeake-bay-helps-researchers-and-resource-managers
- NOAA Fisheries, “How Do Scientists Know Where the Fish Go?”: https://www.fisheries.noaa.gov/feature-story/how-do-scientists-know-where-fish-go

### Movebank

Movebank’s tracking-data model is a strong architectural precedent because tag identity, animal identity, deployments, sensor type, timestamps, and quality control are distinct. Its live-feed documentation notes that tags must be associated with animals through deployment/reference data before those records become animal tracking data, and it recommends filtering outliers and checking reference metadata.

Reusable Ouros lessons:

- `tag_id` and `pokemon_entity_id` must never be the same field.
- A physical device can have several deployments over its life.
- A single individual can have sequential devices.
- Raw device data can exist before a valid individual association is established.
- Derived fixes should retain the input detections and processing revision that produced them.
- Bad or missing metadata can make a technically valid sensor record scientifically ambiguous.

Source:
- Movebank live data feeds and deployment/reference-data guidance: https://www.movebank.org/cms/movebank-content/live-data-feeds

### Pokémon research structure

New Pokémon Snap provides an official Pokémon precedent for ecological field research in which repeated observations of wild Pokémon and their behavior build a research record. Ouros can reuse the high-level pattern — repeated observation, field revisits, behavior documentation, and later interpretation — without importing its scoring systems or assuming that a camera, tag, or other device grants perfect knowledge.

Source:
- Pokémon, New Pokémon Snap overview: https://www.pokemon.com/us/pokemon-video-games/new-pokemon-snap

Pokémon Ranger material also establishes that Pokémon settings can contain dedicated field organizations and specialized communication devices. That supports authored institutions with field equipment, but the Ranger Capture Styler is not a wildlife telemetry rule and must not be treated as one.

Reference:
- Pokémon Ranger / Capture Styler overview: https://bulbapedia.bulbagarden.net/wiki/Capture_Styler

## PTU / Caelo cross-check

The project evidence still treats PTU 1.05 and the Python AutoPTU oracle as mechanical sources. The accessible project corpus confirms many tracking-adjacent concepts such as Perception, Survival, Technology Education, and the Tracker capability elsewhere in the project history, but this pass did not recover a primary PTU/Caelo rule that defines radio telemetry, GPS collars, acoustic arrays, tag attachment, receiver ranges, or a generic wildlife-monitoring subsystem.

Therefore none of the following are inferred:

- Tracker capability = radio/GPS telemetry.
- Technology Education = automatic telemetry competence.
- Perception = receiver range.
- Lock-On / Odor Sleuth = overworld tracking devices.
- Electric/Psychic Pokémon = signal boosters.
- a tagged Pokémon = owned, captured, commanded, or available for capture.

The full Caelo corpus and Super PTU Online Helper were not available as reliable invocable sources in this run. No output is attributed to either.

## Reusable Ouros design lessons

### Detection is not location truth

A raw receiver hit proves only the scoped event supported by the device/network contract. Depending on technology, that may be “tag X was detected by receiver Y during time T,” not “Pokémon X stood on coordinate Z.” A later derived location must carry method, uncertainty, and provenance.

### No signal has many explanations

A silence window can mean the animal left coverage, the tag failed, the battery expired, the tag detached, receiver power failed, telemetry upload stopped, the clock drifted, environmental propagation changed, or the animal genuinely stopped moving. The system should preserve competing hypotheses instead of converting silence to death or absence.

### Stationary signal is ambiguous

A receiver can repeatedly detect a tag from roughly the same area after the tag detached. “Stationary tag” must remain distinct from “stationary Pokémon.” A recovered tag can retrospectively revise movement interpretations without rewriting the original raw records.

### Tagged animals are a sample

Tagged individuals must never become population counts. Migration and Conservation can consume tagged-individual evidence alongside surveys, field signs, photographs, genetic sampling, and other observations. They decide whether that evidence supports a population-level claim.

### Network history matters

A new receiver can create an apparent new corridor simply because detection coverage improved. A receiver moved five kilometers can change route inference. Every station and coverage revision therefore needs its own history.

### Device burden remains a welfare question

Any claim that a device altered movement, feeding, social behavior, or survival must be evidence-backed. Tagging should route through Research Ethics and Care/Agency where appropriate. The narrative system must support “possible device effect,” “no detected effect,” and “unresolved” without inventing biological penalties.

### Sensitive locations need publication controls

A precise roost, nest, release site, or rare-population location can be scientifically valid while public presentation remains deliberately coarse. Public maps may point to a broad region while authorized researchers retain the detailed record.

## Original Ouros adaptation

Proposed telemetry should support several technology profiles without declaring which is canon:

- fixed radio receiver arrays;
- acoustic receiver gates in rivers/coasts;
- store-on-device loggers requiring recovery;
- near-live networked tags;
- manual directional tracking;
- mixed systems where only some detections are remotely transmitted.

The chosen technology belongs to regional canon and institutional capability. The protocol can represent all of them through device, deployment, receiver, raw detection, derived fix, and quality state.

## Narrative opportunities

Telemetry is strongest when it creates uncertainty rather than omniscience. A signal that disappears after release can trigger a search whose correct ending is “receiver outage.” A migration corridor can become visible only after five years of sparse detections. A famous tagged Pokémon can vanish from the public map because the research team redacted its new breeding site. A recovered collar can reveal that three months of supposed residency were actually the history of a detached device.

These structures generate investigation, institutional learning, callbacks, archive value, and non-combat resolutions while preserving Pokémon agency and scientific uncertainty.

## Copyright / transformation note

No protected Pokémon dialogue, prose, distinctive quest plot, or campaign narrative is reproduced. External sources are used for high-level research patterns and provenance only. All Ouros scenarios and system proposals in Pass 165 are original and NON-CANON until approved.