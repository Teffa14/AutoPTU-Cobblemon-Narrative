# Forest canopy, arboreal habitat & vertical ecology research — pass 74

Status: RESEARCH / PROVENANCE ONLY. Not canon. External sources are inspiration or factual references, not PTU rules authority.

## Why this pass exists

Ouros already models Flora, Decomposition, Wild Collectives, Light, Soundscapes, Wildfire, Soil and Architecture. It does not yet have a dedicated contract for vertical forest structure: canopy, midstory, understory, forest floor, tree cavities, canopy gaps, branch connectivity, epiphytes and arboreal travel.

That omission matters because a forest can change dramatically without changing its species list or ground footprint. A fallen canopy tree can create light at ground level, remove nesting cavities, break an arboreal route, add deadwood and alter encounters at several heights at once.

## Public-source findings

### Fortree City: settlement integrated with tree structure

Pokémon's 2026 Hoenn retrospective describes Fortree City as a treetop city built within trees. An earlier official Hoenn retrospective describes it as a treehouse town with rope bridges.

Sources:
- https://www.pokemon.com/us/pokemon-news/remember-the-region-hoenn-spotlight
- https://www.pokemon.com/uk/news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-hoenn-region

Reusable structure:
- vertical settlement layers can be part of ordinary civic life rather than a one-off dungeon gimmick;
- bridges and elevated access can be transport infrastructure with maintenance history;
- the same forest can support habitation, wildlife and battle spaces without flattening everything into one ground plane.

Do not copy Fortree itself into Ouros.

### Pikipek: tree modification can be species behavior

The official Pokédex states that Pikipek can make holes in hard trees with repeated beak strikes.

Source:
- https://www.pokemon.com/us/pokedex/pikipek

Reusable structure:
- tree cavities, bark disturbance and branch damage can sometimes be produced by known Pokémon behavior;
- a cavity can have provenance and age rather than appearing as generic decoration;
- cavity creation does not imply deliberate construction, ownership or a tactical hazard.

### Passimian: arboreal groups need not be homogeneous encounter blobs

The official Pokédex describes a group structure in which selected members leave to forage/hunt and share food with the rest.

Source:
- https://www.pokemon.com/uk/pokedex/passimian

Reusable structure:
- the subgroup visible in the canopy may be only one working party of a larger collective;
- resource routes can connect canopy fruiting areas to persistent group state;
- group organization must remain species-grounded and must not be generalized to all arboreal Pokémon.

### Forest-top medical encounter: vertical location can change the meaning of an apparent rescue

The official episode summary for "Jump for Joy!" places an ailing Nuzleaf high in a large tree. Characters initially interpret Nurse Joy's disappearance as an abduction, but the situation is actually connected to care.

Source:
- https://www.pokemon.com/us/animation/seasons/6/episode-37-jump-for-joy

Reusable structure:
- reaching an upper layer can reveal that the original interpretation of an incident was wrong;
- vertical traversal can serve investigation and care, not only combat;
- arboreal access should not automatically be a battle puzzle.

### PTU campaign log: tree alteration can have ecological consequences

A public PTU campaign log describes a player knocking down a tree, provoking a nearby Pokémon that was protecting eggs. Replanting trees became part of the resolution.

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Reusable structure:
- player modification of a tree can affect nesting or perceived threat without requiring a scripted villain;
- a single tree can be a persistent habitat object whose history matters later;
- resolution can include restoration or withdrawal rather than capture/KO.

This is a player-written recap. Preserve attribution and do not reuse its characters, dialogue, distinctive scenario details or plot.

### PTU community encounter design: forests work better when behavior and biome context matter

A 2025 community post on forest-route encounter tables argues that Pokémon choices should make sense for the specific biome rather than using one generic forest list.

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/1lt1j9p

Reusable structure:
- canopy composition, tree age, moisture, altitude and disturbance can justify distinct encounter profiles within the same broad forest biome;
- encounter tables should consume authored forest state rather than define it.

### Canopy gaps and regeneration

NPS forest-regeneration material explains that when large trees die, gaps in the canopy allow seedlings and saplings to grow. Other NPS material describes middle-canopy competition for limited light and epiphytes using trees for support.

Sources:
- https://www.nps.gov/articles/000/forest-regeneration-2022.htm
- https://www.nps.gov/articles/000/resilient-forests-initiative-complexity.htm
- https://www.nps.gov/places/carbon-river-rainforest-trail-crowding-out-competition-exhibit-panel.htm

Reusable structure:
- canopy closure should be versioned separately from understory state;
- a canopy gap can create multi-year follow-up content: light change, regeneration, invasive pressure, wildlife use and route changes;
- epiphytes add vertical habitat without implying parasitism.

### Vertical stratification is ecologically real

US Forest Service research summarizes evidence that forest arthropod communities can be strongly stratified by height. Factors include forest age, season, time of day, foliage complexity, cavities, light, temperature, wind, humidity, resources, competition and dispersal ability.

Source:
- https://research.fs.usda.gov/treesearch/37787

Reusable structure:
- upper canopy, middle canopy, understory and floor can have different encounter/ecology profiles even at the same map coordinate;
- time-of-day effects can differ by height;
- one ground-level observation cannot establish whole-forest abundance.

### Forest complexity and cavities

US Forest Service work on uneven-aged hardwood stands documents vertical structural diversity, cavities at different heights, canopy structure, understory and downed wood as distinct habitat features.

Source:
- https://research.fs.usda.gov/treesearch/3756

Reusable structure:
- cavity height and size can matter for habitat identity;
- tree age/structure can be meaningful independent of species;
- a forest should not be reduced to trunk locations plus leaf blocks.

### Gaps can change forest trajectories

NPS restoration material shows that canopy gaps can increase light and regeneration but also create opportunities for undesired or invasive vegetation depending on existing state.

Sources:
- https://www.nps.gov/articles/000/resilient-forests-initiative-complexity.htm
- https://home.nps.gov/seki/learn/historyculture/gfveg.htm

Reusable structure:
- a fallen tree does not have one deterministic consequence;
- restoration proposals should depend on baseline seedlings, disturbance history and surrounding vegetation;
- canopy manipulation belongs in Flora/Conservation world state before it ever becomes a battle effect.

## PTU / Caelo mechanical guardrails

Available project evidence supports a strict separation between ecological verticality and tactical movement.

Python AutoPTU evidence currently visible in the project includes:
- named forest terrain context;
- Naturewalk matching against terrain labels;
- Sky movement and Levitate checks;
- forest-specific temporary effects such as Forest Lord origins in exact rule implementations.

This evidence is narrow. It does not prove generic tree climbing, branch traversal, canopy fall damage, swinging, gliding, perching, arboreal cover, canopy LoS, falling branches, vine movement or 3D combat.

Project Pokédex material contains explicit movement/capability fields. Any Pokémon-assisted traversal must read the actual individual/species capability state rather than infer it from appearance or lore.

The primary Caelo corpus was not reliably retrievable during this pass. No new Caelo-specific climbing, forest, Naturewalk, Sky, Jump or fall rules are asserted here.

## Design lessons for Ouros

1. Give important forests vertical structure that persists independently of Minecraft chunks.
2. Treat canopy gaps, cavities and branch networks as coarse habitat/world-state objects, not per-block simulation.
3. Keep visible subgroup separate from total population and from tactical encounter participants.
4. Use vertical access for investigation, care, observation, social scenes and transport, not only combat.
5. Let a single persistent tree accumulate provenance: growth, cavity creation, nesting, storm damage, repair attempts, fall and decomposition.
6. Do not convert visual height into PTU movement rules automatically.
7. Keep LoS separate from vertical visibility, foliage concealment and perception.
8. Do not treat every arboreal species as having Sky, Wallrunner, Naturewalk or climbing capability.
9. Preserve older map editions when canopy bridges or landmark trees change.
10. Let canopy changes propagate causally into Light, Flora, Wild Collectives, Decomposition, Soil, Soundscape, Travel and Conservation.

## Research gaps

- Exact PTU/Caelo rules for climbing, Jump, Sky, Levitate, Naturewalk (Forest), Wallrunner, falling and vertical LoS.
- Whether Caelo contains authored forest locations with explicit access gates or canopy-specific encounter rules.
- Cobblemon hooks for persistent individual nesting/perching behavior versus generic spawning.
- Minecraft representation strategy for branch connectivity without storing every leaf block as canonical state.
- Whether AutoPTU-Java will eventually use a 2D grid with vertical tags or a true multi-elevation battlefield abstraction.