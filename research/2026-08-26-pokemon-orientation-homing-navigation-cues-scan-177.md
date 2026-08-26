# Pokémon Orientation, Homing & Multimodal Navigation Cues — Research Scan 177

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is Ouros canon.
Date: 2026-08-26
Pass: 177

## Corrected scope after full-tree audit

The first targeted search did not surface Pass 81. The full repository comparison did: `design/geomagnetism-magnetic-navigation-interference-layer.md` already owns magnetic-field state, magnetic observations, magnetic-navigation context, local anomalies, instrument interference and Pokémon magnetic-behavior observations.

Pass 177 therefore does not create a second magnetic-navigation authority. It extends the existing architecture only for multimodal biological orientation and homing: how a persistent Pokémon appears to combine or switch among landmarks, celestial cues, odor, acoustic information, route memory, social following and Pass 81 magnetic context while moving toward a goal.

Existing authorities remain authoritative:

- Geomagnetism Pass 81 owns magnetic field revisions, magnetic navigation profiles, anomaly state and magnetic-behavior observations.
- Wildlife Migration owns recurring regional movement, episodes, corridors and stopovers.
- Pokémon Spatial Ecology owns home ranges, core-use, site fidelity and territoriality.
- Wayfinding owns human guidance assets, route descriptions and actor route knowledge.
- Olfactory Landscapes owns odor sources, fields and scent observations.
- Light/Astronomy owns lightscape and celestial observations.
- Telemetry owns devices, detections, fixes and movement segments.
- Pokémon Agency owns persistent individual identity, custody, partnership and release.
- Research Ethics owns experimental handling and displacement authorization.
- PTU/AutoPTU owns Skills, Capabilities, Abilities, movement and battle legality.

The corrected gap is therefore `multimodal biological orientation / homing assessment`, not geomagnetism itself.

## Research findings

### Map, compass and implementation should remain separate

A 2025 animal-navigation review describes map-and-compass navigation as a useful two-step model: an animal first derives a goalward direction from positional information, then orients movement using a directional reference. The review further separates cue type, map structure and implementation strategy.

Source: Morford, Wynn, Lewin & Jaggers, “Map and compass navigation: the mechanism and ontogeny of animal maps,” Animal Behaviour, 2025.
https://pmc.ncbi.nlm.nih.gov/articles/PMC7618438/

Ouros implication: do not store `can_navigate=true`. Store goal context, observations, available cue conditions, route outcome and a reviewed hypothesis about which information may have contributed.

### Magnetic compass and magnetic map are distinct even inside Pass 81

A review of magnetic maps distinguishes directional compass information from positional map information. Diverse animals can use geomagnetic information, but mechanism, learning and cue integration remain species- and context-dependent.

Source: Lohmann et al., “Magnetic maps in animal navigation,” 2022.
https://pmc.ncbi.nlm.nih.gov/articles/PMC8918461/

A related review emphasizes geomagnetic information as widespread while cautioning against treating all magnetic behavior as one mechanism.

Source: Wiltschko & Wiltschko, “The discovery of the use of magnetic navigational information,” 2021.
https://pmc.ncbi.nlm.nih.gov/articles/PMC8918449/

Ouros implication: Pass 177 references Pass 81’s magnetic context. A north-oriented observation may support a magnetic-compass hypothesis already represented there; it does not prove a positional map, homing ability or immunity to anomalies.

### Real navigation is often multimodal

The magnetic-map literature stresses that animals combine information sources. Terrestrial navigators may use landmarks, celestial information, odors and magnetic cues in different proportions depending on setting.

A NOAA-hosted sea-turtle study provides a useful two-scale model: magnetic information may guide an animal into the vicinity of an island, while chemical cues may assist final localization.

Source: Endres et al., “Multi-Modal Homing in Sea Turtles: Modeling Dual Use of Geomagnetic and Chemical Cues in Island-Finding.”
https://repository.library.noaa.gov/view/noaa/51794

Ouros implication: support `coarse orientation -> local search/localization` without requiring one cue to solve both stages.

### Learned odor memories can support return without acting like a straight-line beacon

USGS explains that salmon are believed to use broad magnetic information and then learned odors to return toward their natal stream.

Source: USGS, “How do salmon know where their home is when they return from the ocean?” Updated 2026.
https://www.usgs.gov/faqs/how-do-salmon-know-where-their-home-when-they-return-ocean

A 2024 review of olfactory navigation notes that odor signals become intermittent and physically complex at distance; local gradients may fail to point toward the source, making memory and additional directional information important.

Source: Emonet & Vergassola, “Olfactory cues and memories in animal navigation,” 2024.
https://pmc.ncbi.nlm.nih.gov/articles/PMC11331761/

Ouros implication: a familiar odor can contribute to a homing hypothesis while Olfactory Landscapes remains owner of odor-field state. The system must not draw an automatic route from source to Pokémon.

### Celestial information can interact with artificial light

National Park Service material describes nocturnal birds using stars and Earth’s magnetic field during migration, while artificial lights can disorient movement around built structures.

Sources:
https://www.nps.gov/articles/000/migration.htm
https://www.nps.gov/orpi/learn/nature/dark-sky.htm

Ouros implication: Lightscape changes can become one input to a cue-conflict investigation. They do not create Confused, Accuracy penalties, Fatigue or forced movement.

### Landmarks can be learned and reweighted

Research on landmark learning shows animals can integrate external landmarks with other navigational information, and cue competition can change which information dominates behavior.

Source: “Associative Basis of Landmark Learning and Integration in Vertebrates.”
https://pmc.ncbi.nlm.nih.gov/articles/PMC2895939/

Research on scatter-hoarding animals likewise shows small-scale relocation can depend on beacons, landmarks, compass information and geometry.

Source: “What scatter-hoarding animals have taught us about small-scale navigation.”
https://pmc.ncbi.nlm.nih.gov/articles/PMC2830246/

Ouros implication: redevelopment can remove a familiar visual cue and change observed route efficiency without deleting site fidelity or implying cognitive decline.

### Pokémon offers magnetic flavor, but Pass 81 already owns that domain

The official Pokédex classifies Probopass as the Compass Pokémon and describes its powerful magnetic field. Its `Magnet Pull` Ability has a specific mechanical battle meaning.

Source: official Pokémon Pokédex, Probopass.
https://www.pokemon.com/uk/pokedex/probopass

The official episode “Nosing ’Round the Mountain” gives a narrative precedent for baseline behavior being externally disrupted by technology, then restored. The reusable structure is baseline -> deviation -> interference hypothesis -> recovery, not the specific plot.

Source: Pokémon.com, “Nosing ’Round the Mountain.”
https://www.pokemon.com/us/animation/seasons/11/episode-6-nosing-round-the-mountain

Pass 177 therefore uses magnetic examples only as handoffs to Pass 81. It does not create new magnetic-region, anomaly or instrument-state objects.

### PTU campaign material supports navigation as world texture without supplying a new mechanic

A public PTU campaign log uses route choices through hazardous travel, while `Tales of Visiwa` describes wilderness where certified explorers and local knowledge matter to persistent exploration.

Sources:
https://forums.giantitp.com/archive/index.php/t-527075.html
https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Reusable lesson: orientation uncertainty can shape expedition structure, callbacks and discovery while exact Skill resolution remains PTU/Caelo-governed.

### Fan-game navigation provides an anti-pattern for hidden state

Pokémon Reborn’s Chrysolia Forest uses changing obstacles and route loops. Community reports show that some players lose the state model and rely on walkthroughs even though the path follows a deterministic gimmick.

Sources:
https://pokemon-reborn.fandom.com/wiki/Chrysolia_Forest
https://www.reddit.com/r/PokemonReborn/comments/1l2wma3/

Reusable lesson: if orientation itself becomes gameplay, Ouros should expose enough changing evidence for players to form and revise a model. Hidden arbitrary route changes should not substitute for ecological uncertainty.

## Design deductions

A biological orientation record needs a goal or goal hypothesis; “faces north” and “returns home” are different claims.

A successful return proves an outcome, not the mechanism.

Cue-use assessments should be versioned and may remain `UNRESOLVED` indefinitely.

Pass 81 supplies magnetic observations and field state. Pass 177 may compare those records with visual, olfactory, celestial or acoustic evidence but may not rewrite the geomagnetic assessment.

Experimental displacement requires Research Ethics authorization and should be rare. Natural returns, historical telemetry and passive observations are valid alternatives.

Known individuals may switch cues after landscape change. That switch must be inferred from evidence, not generated from species flavor.

Minecraft pathfinding can never reveal what cue an entity used.

A navigation failure can become Chronicle state without forcing a battle, rescue mission or permanent impairment.

## PTU / AutoPTU cross-check

AutoPTU search confirms `Magnet Pull` and Nosepass/Probopass material exist in the imported source corpus. Search also surfaces PTR2e/Foundry files; those are not promoted over the project’s PTU/Caelo source priority.

AutoPTU-Java currently has no generic multimodal homing, landmark-learning, biological compass or route-memory subsystem. Its current README still leaves full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining registries, tactical AI and Craftics/Cobblemon integration incomplete.

Pass 177 therefore adds no Navigation Skill, homing percentage, compass bonus, magnetic-sense Capability, landmark-memory modifier, automatic pathfinding, species-wide orientation rule, Magnet Pull overworld effect, battle-LoS navigation rule, migration-speed bonus or capture modifier.

## Caelo / Super PTU status

Searchable project sources did not expose a reliable primary Caelo passage defining homing, multimodal animal navigation or orientation checks. Super PTU Online Helper was not available as an invocable capability. No output from either source is invented here.

## Canon status

Everything in this research file is provenance or design input. No population, navigation behavior, research institution, magnetic phenomenon, landmark dependency, homing ability or encounter becomes canon through Pass 177.