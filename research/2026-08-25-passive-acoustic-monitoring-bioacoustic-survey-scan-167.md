# Passive Acoustic Monitoring, Bioacoustic Survey, and Automated Detection — Research Scan 167

Status: research/provenance only. Not established Ouros canon.

Date: 2026-08-25

## Scope and repository fit

This scan extends the existing authority in `design/soundscapes-acoustic-ecology-layer.md`. That layer already owns acoustic sources, emitted sound events, auditory observations, recordings, profiles, baselines, anomalies, listening sites and non-mechanical disturbance. Pass 167 does not create a competing sound system.

The narrower gap is passive acoustic monitoring as a scientific workflow: autonomous recorders, recording effort, duty cycles, inaccessible-site bias, data gaps, machine-generated candidate detections, false positives, duplicate detections, human review, coverage revisions and long-term comparability.

Related authorities remain separate:

- Soundscapes owns sound events, recordings and acoustic interpretations.
- Science owns research questions, analyses and publications.
- Metrology owns calibration, instrument traceability and measurement uncertainty.
- Timekeeping owns clock state and timestamp correction.
- Research Ethics owns authorization and subject/site protection.
- Community Science owns public submissions and participatory monitoring.
- Wildlife Telemetry owns tagged-individual detections; passive acoustic monitoring does not create individual identity unless other evidence supports it.
- Diel Activity and Seasonality own interpretation of activity windows.
- Wild Collective Agency owns collective identity.
- Minecraft/Cobblemon remains presentation and cannot manufacture scientific detections.

## New-source findings

### 1. Passive recorders sample detectability, not omniscient presence

USGS tested autonomous AudioMoth recorders against known wolf vocalizations. A recorder placed at the source captured the known events, while remote units detected a much smaller fraction. Chorus and solo vocalizations had different detectability, and wind and temperature affected results.

Reusable Ouros lesson: a valid deployment can produce a non-detection while the caller was genuinely present and vocalizing. Coverage is conditional on source behavior, distance, environment, device placement and recording window. `NOT_DETECTED` must remain a survey result rather than an absence fact.

Source: U.S. Geological Survey, “Testing a new passive acoustic recording unit to monitor wolves,” 2020.
https://www.usgs.gov/publications/testing-a-new-passive-acoustic-recording-unit-monitor-wolves

### 2. Time of day, season and weather change acoustic availability

A USGS autonomous-recorder study of birds found substantial changes in detection probability by time of day, date and weather. The important design lesson is not the specific bird schedule. It is that a recorder can work perfectly while the target simply does not vocalize during the sampled interval.

Reusable Ouros lesson: acoustic sampling needs explicit effort windows. Comparing “five detections this year” with “two detections last year” is unsafe when schedules, seasons, weather or recording effort differ.

Source: U.S. Geological Survey, “Autonomous acoustic recorders reveal complex patterns in avian detection probability,” 2017.
https://www.usgs.gov/publications/autonomous-acoustic-recorders-reveal-complex-patterns-avian-detection-probability

### 3. Automated classifiers require review and model provenance

A 2025 USGS study examined machine-learning classifiers used on more than 9,500 hours of acoustic data. The two tested models produced very different true-positive rates. A second-stage model substantially improved separation of true and false detections.

Reusable Ouros lesson: an automated detector creates a candidate observation, not a species fact. Every detection must preserve detector/model revision, threshold or confidence class, source recording and review state. Updating a classifier can change historical interpretation without changing the raw audio.

Source: U.S. Geological Survey, “Two-stage models improve machine learning classifiers in wildlife research: A case study in identifying false positive detections of Ruffed Grouse,” 2025.
https://www.usgs.gov/publications/two-stage-models-improve-machine-learning-classifiers-wildlife-research-a-case-study

### 4. Deployment logistics can create geographic sampling bias

A July 29, 2026 USGS publication describes drone deployment and retrieval of autonomous recording units in inaccessible wetlands. The underlying problem is broadly reusable: manual installation tends to favor accessible habitat edges, which can restrict coverage and bias monitoring.

Reusable Ouros lesson: absence of data from a marsh interior, cliff, canopy or hazardous ruin may reflect deployment access rather than ecological absence. Program design should preserve why a site was or was not sampled.

This paper is useful as current research inspiration. Ouros must not infer that drone technology exists in canon. Any platform must be authored separately through Technology/Airspace.

Source: U.S. Geological Survey, “Developing a low-cost drone-based method for deploying and retrieving autonomous recording units in inaccessible areas,” July 29, 2026.
https://www.usgs.gov/publications/developing-a-low-cost-drone-based-method-deploying-and-retrieving-autonomous-recording

### 5. Passive acoustic technologies vary by platform and research goal

NOAA documents multiple passive-acoustic approaches including stationary moorings, drifting systems, hydrophones and mobile platforms. Passive systems listen to naturally occurring or externally generated sound rather than sending sound to interrogate the environment.

Reusable Ouros lesson: underwater hydrophones, terrestrial recorders and mobile arrays should share provenance concepts but should not inherit identical range, coverage or maintenance assumptions. Passive monitoring must also remain distinct from active sonar or an authored Pokémon Move.

Source: NOAA Fisheries, “Technologies for Passive Acoustic Research.”
https://www.fisheries.noaa.gov/new-england-mid-atlantic/science-data/passive-acoustic-technologies

### 6. Large monitoring programs need program-level provenance

USGS AMMonitor treats remote biodiversity monitoring as a workflow involving sites, equipment, objectives, deployments and data. The reusable design lesson is organizational: hundreds of recordings without deployment and processing provenance are much less useful than a smaller, well-documented series.

Source: U.S. Geological Survey, “AMMonitor: Remote monitoring of biodiversity in an adaptive framework. Version 2.1.”
https://www.usgs.gov/software/ammonitor-remote-monitoring-biodiversity-adaptive-framework-version-21

## Pokémon-specific inspiration and guardrails

### Chatot — mimicry can confound source attribution

The official Pokédex describes Chatot as capable of learning human words and imitating the cries of other Pokémon. This is unusually useful for Ouros because it creates a natural reason for an acoustic classifier to identify a call pattern correctly while the assumed source species is wrong.

Reusable structures:

- a rare-call alert that turns out to be mimicry;
- a local Chatot repertoire containing sounds learned from infrastructure, people or other Pokémon;
- a detector model that must distinguish sound pattern from source identity;
- an old recording whose interpretation changes after a mimic is documented.

Hard guardrail: Chatot mimicry does not grant automatic language comprehension, Chatter mechanics, perfect copying or a generic deception bonus.

Source: official Pokémon Pokédex — Chatot.
https://www.pokemon.com/us/pokedex/chatot

### Noibat — biologically relevant sound can sit outside human hearing

The official Pokédex describes Noibat using very high-frequency sound and ultrasonic waves while searching for food. That is useful for survey design because a human listener and a recorder may have different detectable frequency ranges.

Reusable structures:

- a cave survey where people hear silence but an authored instrument logs patterned signals;
- recorder hardware revisions that change which calls can be sampled;
- old datasets becoming only partially comparable after equipment upgrades.

Hard guardrail: Noibat lore does not grant Ouros a generic ultrasonic sensing system, exact ranges, sonar geometry, damage or location-finding mechanics.

Source: official Pokémon Pokédex — Noibat.
https://www.pokemon.com/us/pokedex/noibat

## PTU / project-source cross-check

The project PTU source corpus exposes `Blindsense` as a Special Capability. Its rules text explicitly allows echolocation, enhanced hearing, smell or other heightened senses as possible forms while defining its actual mechanical benefit around functioning in darkness and immunity to Blindness. This is important because narrative acoustics must not invent additional range, localization or detection rules from the descriptive example.

Project source: `Teffa14/AutoPTU/audit_sources/Indices and Reference.txt`.

The same project contains concrete PTU concepts such as the Sonic keyword, Soundproof and sound-based Moves/Abilities. These are mechanical objects. Passive acoustic survey state must never invoke them merely because a recording contains a loud call.

AutoPTU Python contains broad ability code references, but its own ability audit says test coverage is partial. AutoPTU-Java remains a parity port in progress. A representative Sonic or Soundproof behavior, even where implemented, cannot promote the whole `abilities`, `move-specific behavior`, `status lifecycle` or reaction families.

## PTU campaign and actual-play design lessons

Public PTU campaign material repeatedly shows that exploration and investigation can carry a session without immediate combat. A 2025 campaign pitch for a long-running “Social Ecology of Kanto” game explicitly centers mysteries in the relationship between society and nature. The reusable lesson for Pass 167 is structural rather than political: monitoring data can expose a relationship between infrastructure and ecology without requiring a villain.

Source: public PTU campaign listing, “PTU: The Social Ecology of Kanto.”
https://startplaying.games/adventure/clnt20u4d000208ma3ty01n49

A long-running public PTU campaign log also shows how field exploration, unusual behavior, damaged habitat and later confrontations can appear in the same session without every ecological observation being reduced to battle. Pass 167 uses only that pacing lesson; it does not reuse its characters, homebrew or plot.

Source: public Pokémon Tabletop campaign logs on r/PokemonTabletop, including session reports such as:
https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv/

## High-value Ouros design lessons

1. Raw audio should survive every later reinterpretation.
2. Recorder uptime and scheduled effort must be explicit.
3. A candidate classifier hit is not a validated detection.
4. A validated detection is not an individual count.
5. Simultaneous detections at several recorders may represent one event.
6. Non-detection is meaningful only relative to actual sampling opportunity and expected detectability.
7. Equipment upgrades can improve present surveys while making historical comparisons harder.
8. Placement accessibility creates spatial bias.
9. Clock drift can create false timing or sequence conclusions.
10. Environmental noise can suppress detection without removing the source.
11. Mimicry can make call identity differ from source identity.
12. Sensitive acoustic records can reveal nest, roost or release locations and may need restricted public coordinates.
13. Long-running recorder arrays can create compelling “nothing happened” baseline years.
14. Acoustic monitoring should create evidence and hooks, not automatic spawns.
15. Scientific disagreement can remain unresolved without generating a combat encounter.

## Candidate Ouros applications

The protocol can support marsh-bird style monitoring, cave ultrasonic surveys, dawn chorus series, migration stopover monitoring, restoration follow-up, urban-noise comparisons, hydrophone surveys, nocturnal wildlife work, long-term soundscape archives and community listening projects.

These applications remain proposed. No specific region, institution, Pokémon population, recorder technology or historical dataset becomes canon through this scan.

## Copyright / transformation note

All external sources above are used for abstract structures, scientific constraints and design lessons. No protected dialogue, narrative prose, distinctive plot, character, encounter sequence or original campaign text is copied into Ouros.

## Open source-mechanics questions

- Which Caelo materials, if any, modify Sonic, Soundproof, hearing, echolocation, Blindsense or recording equipment?
- Which sound-based Moves and Abilities have current parity-backed Java contracts, and which remain only Python evidence?
- Does the setting canon support autonomous recorders, hydrophones, spectrum analysis or automated classifiers?
- What levels of location privacy are required for nests, roosts, releases and rare populations?
- How should acoustic effort be compressed when the world advances offline?
- Which Pokémon call profiles should be authored versus discovered during Chronicle?

Super PTU Online Helper was not available as an invocable capability during this pass, so no output from it is claimed here.