# Pass 166 — Community science and participatory monitoring scan

Status: RESEARCH / NON-CANON
Date: 2026-08-25
Writable repository: AutoPTU-Cobblemon-Narrative only

## Purpose

This pass examines community science, structured volunteer observations, public biodiversity counts, distributed field reports, and participatory monitoring as a provenance problem rather than as a new ecology authority.

The repository already owns scientific interpretation, research ethics, photography, taxonomy, migration, telemetry, remote sensing, identity, privacy, and many domain-specific monitoring systems. The missing contract is the chain between a voluntary observation effort and the later scientific product that may use it.

Proposed boundary:

participation opportunity -> observation effort -> submission -> source/provenance review -> identification/validation -> quality state -> aggregation -> handoff to the existing scientific/ecological authority.

Pass 166 must not decide species presence at population scale, abundance, migration corridors, taxonomy, capture eligibility, ownership, battle state, or research credentials.

## Existing-repository audit

The complete repository tree was inspected before writing. No dedicated citizen/community-science authority was found.

Relevant existing authorities include:

- Research Ethics: authorization, participant permissions, subject protection, secondary-use limits, sensitive-site protection, and welfare stop conditions.
- Visual Records / Photography: image identity, capture events, derivatives, camera traps, visual observations, and sensitive-location redaction.
- Taxonomy: species/form determinations, classification revisions, synonyms, and uncertainty around identification.
- Metrology / Timekeeping: instrument quality, timestamp correction, calibration, and measurement provenance.
- Wildlife Telemetry: tagged-individual detections and receiver/network provenance.
- Remote Sensing: repeated area acquisitions, processing revisions, spatial products, and change-detection claims.
- Oral History: interviews, testimony, memory, recordings, and source dependency.
- Identity: persistent actor identity, aliases, handles, and record linkage.
- Domain ecological layers: Migration, Wild Nesting, Urban Wildlife, Fisheries, Plant Disease, Fungal Monitoring, Seismic Monitoring, and others retain authority over their own scientific interpretations.

Community science should therefore be a subordinate protocol for collection, validation, coverage, and aggregation of public observations.

## External research findings

### eBird: effort and complete checklists

eBird distinguishes a structured checklist from a highlights-only sighting. A complete checklist records all birds the observer was able to identify during a defined effort, while protocols preserve where, when, duration, distance, and observation type. This makes non-detection interpretable only in relation to effort and protocol.

Reusable Ouros lessons:

- A report of one rare Pokémon is different from a complete survey of everything detected during a route.
- A checklist with zero detections can be useful if effort, place, time, and method are known.
- Observer skill does not have to be perfect for the effort record to remain useful.
- Two records with different protocols should not be treated as directly equivalent without review.

Sources:
- eBird Help, “Complete Checklists and Birding as Your Primary Purpose”: https://support.ebird.org/en/support/solutions/articles/48000967748-birding-as-your-primary-purpose-and-complete-checklists
- eBird Help, “eBird Protocols”: https://support.ebird.org/en/support/solutions/articles/48000950859
- eBird Help, “Get started with eBird”: https://support.ebird.org/en/support/solutions/articles/48001158707-get-started-with-ebird

### eBird: review and data quality

eBird combines automated filters with expert review. Unusual records can be flagged for more documentation, and whole checklists can be withheld from public outputs when location, date, distance, or protocol precision is insufficient. Review is therefore an additional state, not a declaration that the observer lied.

Reusable Ouros lessons:

- A rare observation can be `PENDING_REVIEW` without being rejected.
- Requests for photographs, sounds, notes, or route details should preserve the original submission.
- A technically valid record can remain unsuitable for a particular aggregate map.
- Reviewers can disagree or revise a decision later.
- Public visibility and scientific retention are separate decisions.

Source:
- eBird Help, “The eBird Review Process”: https://support.ebird.org/en/support/solutions/articles/48000795278-the-ebird-review-process

### iNaturalist: sensitive locations and geoprivacy

iNaturalist supports open, obscured, and private geographic information. Sensitive taxa can have locations automatically obscured, while observers can also restrict geographic information for personal privacy.

Reusable Ouros lessons:

- The authoritative location and the public location can be different products.
- A redacted observation is not missing data.
- Sensitive nest, roost, release, or rare-population coordinates should not be published merely because the observation is valid.
- Observer privacy and ecological sensitivity are separate reasons for restricting coordinates.

Sources:
- iNaturalist Help, “How does iNaturalist protect the locations of sensitive species?”: https://help.inaturalist.org/en/support/solutions/articles/151000233080-how-does-inaturalist-protect-the-locations-of-sensitive-species-
- iNaturalist Help, “What is geoprivacy?”: https://help.inaturalist.org/en/support/solutions/articles/151000169938-what-is-geoprivacy-what-does-it-mean-for-an-observation-to-be-obscured-

### National Park Service BioBlitzes

NPS BioBlitz guidance treats a BioBlitz as a short, bounded event where staff, professional scientists, students, teachers, and citizen scientists work together using scientific methods to document species in a defined place and time. The objective and taxa/habitats being surveyed are planned in advance.

Reusable Ouros lessons:

- A large public count can be a designed sampling event rather than a festival minigame.
- Volunteers and professional researchers can contribute to the same project without having identical roles or authority.
- Event coverage and expertise can be uneven across taxa and locations.
- Repeating the event across years can create a Chronicle baseline, but method changes must be versioned.

Sources:
- NPS, “Planning and Conducting a Small-scale BioBlitz Event”: https://home.nps.gov/articles/000/htln-bioblitz-how-to-plan-and-conduct.htm
- NPS, “The NPS/National Geographic Society BioBlitzes”: https://www.nps.gov/subjects/biodiversity/the-nps-national-geographic-society-bioblitzes.htm
- NPS BioDiscovery: https://www.nps.gov/orgs/1103/biodiscovery.htm

### Pokémon: distributed field research

Pokémon GO provides an official Pokémon-world precedent for distributed research participation. Professor Willow assigns Field Research and Special Research, and official character material describes his work as fieldwork supported by Pokémon GO players around the world to understand Pokémon habitats and distribution.

Reusable Ouros lesson: a professor or institution can distribute bounded observation tasks across many Trainers and later synthesize the returned evidence.

Do not import the Pokémon GO reward loop, stamps, encounter rewards, PokéStop delivery mechanism, or automatic research authority. Completing a public research task in Ouros does not grant a Trainer Class, Skill rank, credential, scientific job, or special capture right.

Sources:
- Pokémon, “Master Pokémon GO Research”: https://www.pokemon.com/us/strategy/master-pokemon-go-research
- Pokémon, Meltan / Professor Willow profile: https://pokemonletsgo.pokemon.com/en-ca/new-pokemon/
- Pokémon GO overview, Field and Special Research: https://www.pokemon.com/uk/pokemon-video-games/pokemon-go

### PTU community material

Public Pokémon Tabletop campaign logs regularly use professors, field researchers, expedition work, and characters remaining behind to perform research. These examples support research as a continuing social activity around a campaign rather than a one-off exposition dump. They do not establish a PTU community-science subsystem.

One public campaign log notes a party member staying in town to conduct research with a professor while other characters continue traveling. The reusable pattern is parallel research work and later information handoff, not the specific characters or events.

Reference:
- r/PokemonTabletop campaign log #3, 2021: https://www.reddit.com/r/PokemonTabletop/comments/mfgwzd

## PTU / Caelo cross-check

The read-only AutoPTU project contains structured Trainer Class material including Researcher-related class data. That evidence confirms that formal Trainer progression is a mechanical system with its own prerequisites and effects. It does not authorize Pass 166 to grant Researcher, Pokémon Education, Chronicler, Perception, or any other Skill/Class/Feature because an actor submitted observations.

Pass 166 therefore prohibits:

- participation -> Researcher class;
- observation count -> Pokémon Education rank;
- accepted record -> Trainer Feature;
- reviewer role -> scientific Skill rank;
- public leaderboard -> character advancement;
- observation of a rare Pokémon -> capture eligibility;
- many observations -> automatic population truth.

No primary PTU/Caelo rule for citizen science, crowdsourced biodiversity monitoring, volunteer-review networks, or public observation platforms was recovered during this run.

The complete Caelo corpus and Super PTU Online Helper were not available as reliable invocable sources. No output is attributed to them.

## Reusable Ouros design lessons

### Observation volume is not sampling effort

Fifty reports from one popular plaza can represent less spatial coverage than five structured transects across a valley. Aggregation must retain method, effort, coverage, and source dependence.

### Duplicate reports need provenance, not deletion

A group walk can generate ten uploads of the same Pokémon. A viral photograph can be reposted by hundreds of actors. Those records may be socially important but are not hundreds of independent detections. Preserve the submissions and link them to shared source evidence.

### `NOT_DETECTED` requires an opportunity to detect

A complete checklist or structured count with known effort can support a scoped non-detection. A casual walk with no report cannot.

### Review is not punishment

Flagging a rare record should create a request for documentation or expert review. It must not create wrongdoing, reputation loss, or faction hostility by default.

### Public participation introduces coverage bias

Accessible parks, famous landmarks, weekend events, daylight hours, transit corridors, photography hotspots, and viral rare sightings will attract disproportionate effort. The system should let Science distinguish “more observations” from “more Pokémon.”

### Sensitive discoveries can remain scientifically useful

A rare nesting site can be retained at full precision for authorized research while public dashboards show only a coarse region. Public excitement must never force disclosure of exact coordinates.

### Community science can prevent quests

A mature monitoring network may resolve a rumor before the party arrives. A supposed disappearance can be explained by a coverage outage; a rare-sighting rumor can collapse as duplicate reposts; a seasonal change can be recognized as normal. Institutional competence should sometimes reduce adventure load.

## Original Ouros adaptation

Potential program types, all NON-CANON until approved:

- annual regional BioBlitzes;
- school biodiversity routes;
- harbor or market wildlife counts;
- migration-watch weekends;
- night-sound observation programs;
- public fungi/flower phenology logs;
- urban rooftop nesting reports;
- trail condition and field-sign reporting;
- volunteer camera-trap annotation;
- archive digitization of historical checklists.

A program may accept casual sightings, structured checklists, fixed-point counts, transects, photographs, audio, field signs, or institution-authored tasks. The method must remain explicit.

## Narrative opportunities

Community science works best as a source of imperfect but accumulating knowledge. A famous rare sighting can turn out to be one photograph reposted repeatedly. An overlooked neighborhood can become scientifically important after a school starts a complete weekly count. A veteran volunteer can retire and expose how much an institution depended on one person. Two clubs can disagree about identification while sharing the same raw evidence. An observation network can become better over five years and make later mysteries easier to resolve.

## Copyright / transformation note

No protected Pokémon dialogue, prose, distinctive quest plot, or campaign narrative is reproduced. External sources are used for high-level structures and provenance. All Ouros candidates derived from this scan are original and remain NON-CANON until approved.