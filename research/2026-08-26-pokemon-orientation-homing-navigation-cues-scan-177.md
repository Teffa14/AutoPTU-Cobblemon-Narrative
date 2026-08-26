# Pokémon Orientation, Homing & Navigation Cues — Research Scan 177

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is Ouros canon.
Date: 2026-08-26
Pass: 177

## Why this pass exists

The repository already has authoritative narrative layers for Wildlife Migration, Wayfinding, Pokémon Spatial Ecology, Olfactory Landscapes, Soundscapes, Astronomy, Telemetry and Field Signs. The missing subject is the biological process by which an individual Pokémon may orient toward a goal, return to a familiar site, compensate after displacement, switch between cues, or fail when cues conflict.

This pass does not create route truth, migration episodes, home-range geometry, tracking certainty, battle movement, pathfinding or a universal navigation stat.

## Internal boundary audit

Files inspected before writing included the complete recursive repository tree, README, `design/wildlife-migration-stopovers-corridors-layer.md`, `design/wayfinding-trails-route-guidance-layer.md`, `design/pokemon-spatial-ecology-home-ranges-territoriality-layer.md`, and the current engine evidence.

Existing authorities remain in force:

- Wildlife Migration owns recurring regional movement patterns, annual episodes, corridors and stopovers.
- Pokémon Spatial Ecology owns local home-range, core-use, site-fidelity and territorial assessments.
- Wayfinding owns signs, landmarks, route guidance and actor route knowledge.
- Olfactory Landscapes owns odor sources, fields and scent observations.
- Astronomy owns celestial observations, not animal use of celestial cues.
- Telemetry owns devices, fixes and detected movement segments.
- Pokémon Agency owns persistent individual identity and relationship/custody state.
- PTU/AutoPTU owns mechanical Capabilities, Abilities, movement and battle legality.

No existing file in the recursive tree was found with `orientation`, `homing`, `magnetic navigation` or equivalent as a dedicated authority.

## Research findings

### 1. Navigation should be decomposed into map, compass and implementation

A 2025 review of animal navigation describes map-and-compass navigation as a useful two-step model: first determine a goalward direction from positional information, then orient movement using a directional reference. The review further separates the cues being used, the structure of the learned or inherited map, and the strategy used to combine information.

Source: Morford, Wynn, Lewin & Jaggers, “Map and compass navigation: the mechanism and ontogeny of animal maps,” Animal Behaviour, 2025.
https://pmc.ncbi.nlm.nih.gov/articles/PMC7618438/

Reusable lesson for Ouros: do not store `can_navigate=true`. Store the goal, available cues, evidence of cue use, displacement context, observed orientation and outcome. An individual can have a reliable compass cue but poor positional information, or vice versa.

### 2. Magnetic compass and magnetic map are different claims

A review of magnetic navigation distinguishes directional compass information from positional map information. Evidence exists across several animal groups for using geomagnetic information, including long-distance return toward natal areas, while many details of mechanism and development remain unresolved.

Source: Lohmann et al., “Magnetic maps in animal navigation,” 2022.
https://pmc.ncbi.nlm.nih.gov/articles/PMC8918461/

A related review emphasizes that geomagnetic information is widespread but should not be treated as a single universal sensory implementation.

Source: Wiltschko & Wiltschko, “The discovery of the use of magnetic navigational information,” 2021.
https://pmc.ncbi.nlm.nih.gov/articles/PMC8918449/

Reusable lesson: a Pokémon that appears consistently oriented relative to north may support a magnetic-compass hypothesis. It does not automatically support a magnetic positional map, perfect homing, underground navigation or immunity to local anomalies.

### 3. Animals often combine several cues

The magnetic-map review stresses multimodal navigation. Terrestrial animals may combine visual landmarks, celestial information, odors and magnetic signals. Different cues can dominate at different scales or under different conditions.

The NOAA-hosted study of sea-turtle island finding models a particularly useful pattern: magnetic information may bring an animal into the vicinity of a goal while chemical information helps localize the final destination.

Source: Endres et al., “Multi-Modal Homing in Sea Turtles: Modeling Dual Use of Geomagnetic and Chemical Cues in Island-Finding.”
https://repository.library.noaa.gov/view/noaa/51794

Reusable lesson: Ouros should support `COARSE_ORIENTATION` followed by `LOCALIZATION` without requiring the same cue to solve both tasks.

### 4. Olfactory homing can rely on learned local memories

USGS explains that salmon may use Earth’s magnetic field as a broad compass and then rely on learned odor memories when returning to a natal stream.

Source: USGS, “How do salmon know where their home is when they return from the ocean?” Updated 2026.
https://www.usgs.gov/faqs/how-do-salmon-know-where-their-home-when-they-return-ocean

A 2024 review of olfactory navigation emphasizes that odor signals become intermittent and physically complex at distance; local odor gradients do not always point directly toward the source, so memory and additional directional information can matter.

Source: Emonet & Vergassola, “Olfactory cues and memories in animal navigation,” 2024.
https://pmc.ncbi.nlm.nih.gov/articles/PMC11331761/

Reusable lesson: smelling a familiar cue does not create a straight-line path. Signal loss during a search can be normal. Odor-assisted return must consume Olfactory observations rather than bypassing that layer.

### 5. Celestial cues and artificial light can interact

National Park Service material describes migratory birds using stars, the moon and Earth’s magnetic field as directional information and documents artificial lights as a source of disorientation during nocturnal movement.

Sources:
https://www.nps.gov/articles/000/migration.htm
https://www.nps.gov/orpi/learn/nature/dark-sky.htm

Reusable lesson: a cue conflict can produce a world-state investigation without adding Accuracy penalties, Confusion, Fatigue or forced movement. Lightscape state can be compared with movement observations while the causal conclusion remains a hypothesis.

### 6. Landmarks can be learned, weighted and sometimes overshadow one another

Research on spatial learning shows animals can use landmarks alongside other internal/external cues, and learned cues can compete or dominate under particular conditions.

Source: “Associative Basis of Landmark Learning and Integration in Vertebrates.”
https://pmc.ncbi.nlm.nih.gov/articles/PMC2895939/

Research on scatter-hoarding animals similarly shows small-scale navigation may use beacons, landmarks, compass information and geometry to relocate remembered sites.

Source: “What scatter-hoarding animals have taught us about small-scale navigation.”
https://pmc.ncbi.nlm.nih.gov/articles/PMC2830246/

Reusable lesson: a city redevelopment can remove a familiar landmark and temporarily change observed route efficiency without deleting the Pokémon’s site fidelity or implying cognitive decline.

### 7. Pokémon gives a magnetic-flavor precedent, not a navigation mechanic

The official Pokémon Pokédex classifies Probopass as the Compass Pokémon and states that it emits a powerful magnetic field. Its mechanical Ability `Magnet Pull` has a specific battle meaning involving Steel-type Pokémon.

Source: official Pokémon Pokédex, Probopass.
https://www.pokemon.com/uk/pokedex/probopass

The useful Ouros distinction is strict:

`COMPASS / MAGNETIC LORE != HOMING SYSTEM`

`MAGNET PULL != MAGNETORECEPTION`

`MAGNETIC FIELD EFFECT != POSITIONAL MAP`

A Pokémon can be the subject of an authored orientation study without receiving a new Capability or overworld pathfinding power.

### 8. Pokémon stories can separate disruption from identity

The official episode “Nosing ’Round the Mountain” centers on a Probopass whose behavior is externally disrupted by a device. The reusable structure is not the plot itself, but the distinction between an individual’s normal behavior, an observed deviation, an external-interference hypothesis and restoration of baseline behavior.

Source: Pokémon.com, “Nosing ’Round the Mountain.”
https://www.pokemon.com/us/animation/seasons/11/episode-6-nosing-round-the-mountain

Reusable lesson: when an orientation pattern changes, Ouros should preserve the old baseline and test multiple explanations rather than rewriting the individual’s behavioral profile.

### 9. PTU campaign material supports navigation as adventure texture without supplying new rules

A public PTU campaign log uses route choices between a forest and a visible town after an expedition through hazardous terrain. The reusable structure is travel decision → local information → uncertain route → consequences, while the actual Skill resolution remains PTU-governed.

Source: Giant in the Playground, Pokémon Tabletop United Campaign Log archive.
https://forums.giantitp.com/archive/index.php/t-527075.html

The official PTU retrospective `Tales of Visiwa` likewise describes dangerous wilderness where certified explorers and local knowledge matter to persistent exploration. This supports navigation knowledge as world state, but does not grant a generic homing mechanic.

Source: Pokémon Tabletop RPG, “Tales of Visiwa: A Retrospective.”
https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

### 10. Fan-game navigation supplies an anti-pattern for opaque orientation state

Pokémon Reborn’s Chrysolia Forest uses changing obstacles and route loops. Community reports show that some players can lose the state model and depend on walkthroughs, even though the puzzle has a deterministic structure.

Sources:
https://pokemon-reborn.fandom.com/wiki/Chrysolia_Forest
https://www.reddit.com/r/PokemonReborn/comments/1l2wma3/

Reusable lesson: when orientation itself is the challenge, Ouros should expose enough evidence for the player to form and revise a model. Confusion should come from observable cue conflict or changing world state, not hidden arbitrary path changes.

## Original design deductions for Ouros

1. Biological orientation needs an explicit `goal_ref`. “Heading north” and “heading home” are different observations.
2. A single successful return is evidence of an outcome, not proof of the cue used.
3. Cue-use claims should be versioned and carry confidence.
4. Displacement experiments require Research Ethics authorization and should preserve handling/transport provenance.
5. Landmarks, odors, celestial state and magnetic-anomaly hypotheses should be references to their owning layers.
6. A familiar individual may compensate when one cue disappears by using another; this should be observed, not assumed.
7. Juveniles may have different cue histories from experienced adults, but no species-wide rule should be generated without authored evidence.
8. Return after release can update Rehabilitation/Spatial Ecology only after the relevant observation is accepted; it never restores custody or partnership.
9. Minecraft pathfinding cannot reveal what cue an entity “used.”
10. A navigation failure can be meaningful world history without forcing combat or rescue every time.

## PTU / AutoPTU cross-check

The current AutoPTU repository contains `Magnet Pull` material and Nosepass data in the imported source corpus. Search also surfaces PTR2e/Foundry species data; those files must not be treated as primary PTU/Caelo rules when they conflict with the project’s PTU source priority.

Current AutoPTU-Java search did not surface a generic magnetic-navigation, homing, compass, landmark-learning or path-integration subsystem. The Java README still treats Minecraft/Cobblemon as a future adapter and explicitly leaves full damage, status controller, terrain, hazards, forced movement, reactions, registries, tactical AI and adapter integration incomplete.

Therefore this pass does not add:

- a Navigation Skill;
- a magnetic-sense Capability;
- a homing percentage;
- compass bonuses;
- landmark-memory bonuses;
- automatic pathfinding;
- immunity to being lost;
- species-wide orientation rules from Pokédex flavor;
- Magnet Pull overworld behavior;
- battle LoS as navigational visibility;
- migration speed or movement bonuses.

## Caelo / Super PTU status

The searchable project sources available during this run did not expose a reliable primary Caelo passage defining magnetic navigation, homing, compass use or orientation checks. Super PTU Online Helper was not available as an invocable capability. No result from either source is invented here.

## Canon status

Everything in this research file is provenance or design input. No Pokémon population, navigation ability, landmark tradition, magnetic anomaly, research institution, homing behavior or encounter is canon-approved by this pass.