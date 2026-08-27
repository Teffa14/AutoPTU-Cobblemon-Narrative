# Wildlife Monitoring, Individual Re-identification, Tagging & Telemetry Research — Pass 79

Status: research/provenance only. Nothing in this file is established Ouros canon.

Date: 2026-08-27

## Research question

What reusable narrative and world-simulation structures can support long-term observation of individual wild Pokémon without collapsing research contact into capture, ownership, omniscient tracking, automatic battle participation or a duplicate ecology system?

This pass was selected after enumerating the current repository tree and reviewing the nearest systems. Ouros already has:

- persistent individual Pokémon identity and post-release continuity;
- wild populations, collectives, visible subgroups and exact tactical encounter participants;
- scientific questions, methods, measurements, datasets and research programs;
- protected-area monitoring and stewardship review;
- photography, camera traps and visual re-identification;
- shared equipment, physical technology and digital records;
- travel/expedition logistics;
- Care and Pokémon welfare;
- a strict Cobblemon/AutoPTU authority boundary.

The missing layer is the longitudinal link between those systems: how one wild individual is re-observed across time, how artificial or natural identifiers are recorded, how a tracking device is associated with that individual only for a bounded interval, how detections become a track with gaps and uncertainty, how a device is recovered/reused, and how the resulting evidence changes research or stewardship without becoming omniscient world truth.

## Source classification

Mechanical rules authority remains the project's governing PTU/Caelo source set plus AutoPTU evidence. The sources below are used for narrative structure, field-research workflow and implementation lessons unless explicitly identified as PTU material.

External wildlife-science sources are operational inspiration only. They do not establish Ouros law, ethics policy, permitting institutions, equipment technology, medical procedure or scientific standards.

Community campaigns and fan material are inspiration only. They never establish mechanics or canon.

## Source 1 — New Pokémon Snap official site

Source:
- The Pokémon Company / Nintendo, New Pokémon Snap official website, “Create Your Own Photodex” and “Explore the Lental Region.”
- https://newpokemonsnap.pokemon.com/en-au/create-photodex/
- https://newpokemonsnap.pokemon.com/en-au/explore/

Observed structures:

- Professor Mirror leads ecological research through L.E.N.S.
- The player repeatedly visits research sites rather than consuming each location once.
- Repeated expeditions expose different behaviors and discovery opportunities.
- A record can document behavior without capturing the Pokémon.
- The research loop distinguishes the observed subject, the photograph and the later evaluation of that photograph.

Reusable Ouros lessons:

1. Repeated observation should create longitudinal value. A site can become more informative because researchers revisit it under different times, seasons, disturbances or recovery states.
2. Research interaction with a wild Pokémon does not need to imply ownership or battle.
3. The evidence object and its interpretation should remain separate. This matches the existing Photography and Science layers.
4. Uncommon behavior can become a research lead without becoming a permanent species rule after one sighting.

Do not import:

- Photodex star scores;
- research-level progression;
- Illumina mechanics;
- Fluffruit behavior as a universal research method;
- Professor Mirror, Lental institutions or plot.

## Source 2 — Pokémon Legends: Arceus official site

Source:
- Pokémon Legends: Arceus official website.
- https://legends.arceus.pokemon.com/

Observed structure:

The official game framing asks the player to catch, observe and study the behavior of wild Pokémon while compiling the region's first Pokédex. The useful pattern is repeated field observation rather than a single encounter functioning as complete knowledge.

Reusable Ouros lessons:

- research programs can require repeated observations;
- a behavior claim can gain support through replication across windows rather than one sighting;
- field research can remain a major progression loop even when battles are not the central objective of every excursion.

Do not import:

- Pokédex task counts;
- research-point math;
- mandatory capture quotas;
- Hisui institutions or progression gates.

## Source 3 — PTU 1.05 Survival skill material

Source:
- Pokémon Tabletop United 1.05 Survival skill reference as publicly mirrored at PTU RPG.
- https://pturpg.wikidot.com/skills

Relevant governing pattern:

PTU Survival explicitly covers wilderness scouting and tracking signs through the environment. It can reveal common local Pokémon/resources and can be used to track someone through wilderness conditions.

Ouros implication:

PTU already contains a mechanical avenue for some field tracking. Pass 79 therefore must not invent a parallel “Telemetry Skill,” tracking stat, detection roll or universal research bonus.

Important limit:

A radio/acoustic/satellite-style device, if Ouros eventually canonizes one, does not automatically bypass PTU Skills or grant exact location information. Any mechanical check, modifier, feature interaction or Pokémon-assisted tracking benefit requires exact PTU/Caelo and AutoPTU validation.

## Source 4 — Movebank deployment/reference-data model

Source:
- Movebank, “Deployment Manager.”
- https://www.movebank.org/cms/movebank-content/deployment-manager
- Movebank, “Why use Movebank?”
- https://www.movebank.org/cms/movebank-content/why-use-movebank

Observed structures:

Movebank separates:

- the animal;
- the tag/device;
- the deployment interval associating the two;
- the tracking events produced during that interval.

The deployment period matters because the same device can be tested before attachment, removed, or later deployed on a different animal. Incorrect association would assign data to the wrong individual.

Movebank also supports multiple tracking methods, including GPS, radio/acoustic telemetry, rings and natural markers.

Reusable Ouros lessons:

1. Never store `pokemon_id` permanently inside a tag as though device identity and Pokémon identity were identical.
2. Use an explicit deployment record with start/end provenance.
3. A recovered/reused device creates a new deployment.
4. Data outside a confirmed deployment window must remain unassigned or separately classified.
5. Natural-mark re-identification and artificial tagging can feed one monitoring program without being the same method.

This is a particularly high-value safeguard for persistent Minecraft entities, because a Cobblemon entity UUID, a research tag ID and an Ouros persistent Pokémon ID must never be conflated by convenience.

Do not import:

- Movebank software architecture as mandatory Ouros technology;
- its field names as canon terminology;
- real-world privacy, publication or access policy;
- real species metadata requirements.

## Source 5 — NOAA animal telemetry overview

Source:
- NOAA Ocean Service, U.S. Animal Telemetry Network.
- https://oceanservice.noaa.gov/ocean/animal-telemetry.html
- NOAA Fisheries, “Follow the Whales: How Tagging Supports Whale Research and Rescue.”
- https://www.fisheries.noaa.gov/feature-story/follow-whales-how-tagging-supports-whale-research-and-rescue

Observed structures:

- animal-borne sensors can collect movement, behavior and environmental measurements;
- telemetry may support both long-term research and time-sensitive management/rescue decisions;
- not every individual can be tagged;
- deployments are finite and devices can release/fail;
- attachment requires trained/authorized work in the real-world examples;
- one tagged individual can provide useful evidence without representing an entire population.

Reusable Ouros lessons:

1. Tagged individuals should remain samples, not omniscient representatives of a species or collective.
2. Device silence has several possible explanations: range, battery, obstruction, loss, removal, malfunction, destroyed receiver, data delay, or actual movement away from coverage.
3. A telemetry signal can be evidence for location at a timestamp. It should not be represented as an eternally exact live waypoint.
4. Research contact and device attachment should have a welfare/authorization boundary if Ouros canon later establishes such practices.
5. Tag recovery can be a separate objective from subject observation.

Do not import NOAA permitting law, agency authority, species practice, attachment methods or welfare thresholds into Ouros.

## Source 6 — NOAA passive acoustic monitoring

Source:
- NOAA Fisheries, “Technologies for Passive Acoustic Research.”
- https://www.fisheries.noaa.gov/new-england-mid-atlantic/science-data/passive-acoustic-technologies

Observed structures:

Passive stations can monitor an area for long periods, while animal-borne tags can answer different questions about an individual. Real-time systems and archival systems also differ.

Reusable Ouros lessons:

- station detection and attached-device telemetry are separate methods;
- a receiver network can have gaps and maintenance history;
- a research program can combine several weak evidence streams rather than depend on one perfect sensor;
- passive monitoring is useful for Pokémon that should not be approached directly.

This connects cleanly with Ouros camera stations, Soundscape/Acoustic Ecology and Technology/Infrastructure without duplicating them.

## Source 7 — USGS Motus-style receiver networks

Source:
- U.S. Geological Survey, “Birds, Bats, and Beyond: Networked Wildlife Tracking in the Southern California Bight.”
- https://www.usgs.gov/centers/werc/science/birds-bats-and-beyond-networked-wildlife-tracking-southern-california-bight

Observed structures:

- tiny tags broadcast unique identifiers;
- shared receiver stations detect those identifiers when individuals pass through coverage;
- multiple receivers can improve location inference;
- the network is collaborative and must be maintained;
- a detection is generated by infrastructure availability plus animal movement.

Reusable Ouros lessons:

1. A receiver hit is an observation event, not a continuous global coordinate.
2. Route inference can emerge from several detections across time.
3. Missing detections require checking receiver health before concluding absence.
4. Infrastructure can itself become gameplay: maintenance, outage, relocation and calibration matter.
5. Different institutions may share monitoring infrastructure while preserving separate research questions.

Do not import Motus technology, organizations or coverage assumptions as Ouros canon.

## Source 8 — PTU campaign framing: Social Ecology of Kanto

Source:
- Public StartPlaying listings for “PTU: The Social Ecology of Kanto.”
- https://startplaying.games/adventure/cmnf2v6d70004gw04pk801qil

Observed structure:

The campaign explicitly frames a long-running PTU game around relationships between society and nature, with ecological mysteries coexisting alongside ordinary journey/battle progression. Current public listings show campaigns reaching dozens of sessions, demonstrating that ecology can sustain recurring subplots rather than a single conservation quest.

Reusable Ouros lesson:

A monitoring program should generate repeated intersections with the same region: a missing detection, a migration change, a receiver outage, a public-policy dispute, a re-sighting, a newly observed route, or a subject returning after a long gap. It should not require making every research session a boss encounter.

Do not import the campaign’s factions, political themes, Kanto reinterpretation, house rules or characters.

## Source 9 — PTU campaign framing: Pokémon Astra

Source:
- Public StartPlaying listing for “Pokemon Astra (PTR2).” The listing identifies the system as Pokémon Tabletop United while describing field research into unfamiliar Pokémon and coexistence questions.
- https://startplaying.games/adventure/cm3c67efa0006142b945hsdpv

Observed structure:

Field research is treated as a campaign-scale responsibility tied to coexistence and changing environmental conditions, not merely as flavor between battles.

Reusable Ouros lesson:

A research program can produce operational decisions for settlements, conservation and travel while remaining incomplete and revisable. The characters can contribute evidence without automatically owning institutional conclusions.

Do not import the science-fiction colony premise, factions, weather mystery, species framing or campaign rules.

## Source 10 — Tales of Visiwa retrospective

Source:
- Pokémon Tabletop official site, “Tales of Visiwa: A Retrospective.”
- https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Observed structure:

A long-running PTU campaign can sustain dangerous wilderness, institutional exploration, recurring geography and long-term discoveries for years of play.

Pass 79 reuse:

Monitoring should be attached to persistent geography and repeated expeditions. A tag or re-sighting becomes more valuable when it connects old trips to current world state rather than functioning as a disposable fetch objective.

This source has appeared in earlier Ouros research, so Pass 79 does not re-process its specific campaign arcs. It is retained only as continuity evidence for long-form PTU wilderness play.

## Cross-source design deductions

### A. Identity must survive the sensor

The Pokémon is the persistent subject. A tag, collar, band, visual marking, acoustic signature or camera record is evidence about that subject.

A lost or removed device does not delete the Pokémon entity.

### B. Device identity must survive redeployment

A physical device can have its own provenance, maintenance, custody and recovery history. If reused, the new association needs a new deployment interval.

### C. No detection is an ambiguous fact

Signal silence may indicate movement, device failure, receiver outage, obstruction, data delay, tag loss, or a genuine long absence. The system must keep these hypotheses separate.

### D. Longitudinal monitoring creates revisitable content

High-value callbacks include:

- an individual reappearing after months;
- the same individual using a different route;
- a tag detected somewhere unexpected;
- a receiver going offline exactly when a movement window matters;
- a natural-mark sighting contradicting the automated track;
- a recovered tag without the Pokémon;
- a Pokémon observed after the deployment ended;
- a monitoring method changing because the previous method caused too much disturbance;
- a public map hiding precise coordinates to protect a sensitive site;
- a collective’s assumed route being revised after several individually tracked members diverge.

### E. One tracked Pokémon does not define the collective

Individual evidence can support or challenge a collective-level hypothesis. It never automatically overwrites population or collective state.

### F. Monitoring can be non-invasive

Photography, camera traps, acoustic stations, environmental traces and natural markers should remain valid alternatives to artificial attachment. The game should not make tagging the default “better” method.

## PTU/Caelo mechanical boundary

Pass 79 introduces no new mechanical tracking rules.

Relevant PTU evidence includes wilderness scouting/tracking through Survival, but exact checks, DCs, bonuses, Trainer Feature interactions, Pokémon assistance and equipment effects must be validated against the governing project source set before implementation.

The system must not invent:

- a telemetry Skill;
- automatic tracking advantage;
- exact live coordinates;
- tracking range;
- battery duration;
- tag attachment checks;
- Pokémon-specific tagging resistance;
- status effects from a tag;
- capture modifiers;
- battle bonuses against monitored Pokémon;
- AI knowledge derived from a research database;
- guaranteed encounter generation from a signal.

## Cobblemon implementation boundary

Pass 79 should aggressively reuse Cobblemon/Minecraft for safe presentation:

- persistent overworld Pokémon entities when available;
- species models, forms, textures, animations and cries;
- movement and pose presentation;
- particles/sounds for research-device feedback where appropriate;
- item/block/entity assets for visible stations or devices;
- world positions and chunk/entity observations as inputs to Ouros observation records;
- networking, UI and client synchronization;
- interaction hooks;
- world persistence hooks.

The authority rule remains binding:

`Ouros world/research state -> AutoPTU when battle is required -> adapter -> Minecraft/Cobblemon projection`

Never use Cobblemon battle-state, participant/controller, HP/status, target, initiative or battle-outcome authority to decide an Ouros fact.

A Cobblemon entity’s current physical position can support an overworld observation. It cannot by itself establish an AutoPTU tactical position or make that Pokémon a combatant.

## Originality note

The proposed Ouros content should use the general structures above: deployment intervals, uncertain re-identification, sensor gaps, repeated observation, individual-vs-population inference and revisitable monitoring infrastructure.

It must not reproduce source characters, dialogue, named institutions, exact quests, maps, device designs or plot resolutions.