# Research Scan — Pass 59: Architecture, Built Environment & Adaptive Reuse

Status: RESEARCH ONLY. Not canon.

Date: 2026-08-20

## Gap identified

The repository already covers homes, neighborhoods, public works, infrastructure, accessibility, settlement growth, archaeology, tourism and adaptive world state. It does not yet treat a building or district as a persistent physical object with version history, changing use, condition, morphology and retained traces of prior states.

This pass focuses on that gap.

## Public sources and reusable lessons

### Lumiose City redevelopment

Official source:
https://legends.pokemon.com/en-au/story-world/lumiose-city

Lumiose is explicitly undergoing redevelopment. Shopping arcades, cafés and restaurants coexist with parks, waterfronts and newer facilities. Prism Tower remains a major landmark while the surrounding city changes.

Reusable structure:

A mature city can accumulate new uses, greener spaces and new facilities without discarding its older spatial identity. Ouros settlements should support incremental change rather than complete replacement.

### Urban wild zones

Official source:
https://legends.pokemon.com/en-us/news/adventure

Wild zones are constructed inside Lumiose as part of redevelopment to give Pokémon places to live.

Reusable structure:

Built form and ecology can share the same spatial system. Courtyards, roofs, drainage edges, vacant structures and parks can become habitat state when world evidence supports it.

### Jubilife Village as a historical predecessor

Official sources:
https://www.pokemon.com/us/pokemon-video-games/pokemon-legends-arceus
https://www.pokemon.com/us/pokemon-news/a-look-at-the-early-days-of-pokemon-research-in-pokemon-legends-arceus

Jubilife Village is presented as the predecessor of later Jubilife City. In the earlier era it is young, guarded and organized around institutions appropriate to its current technology and relationship with wild Pokémon.

Reusable structure:

A place should retain morphology versions. The same settlement can grow into another physical form while preserving historical continuity.

### Ecruteak and architectural memory

Official source:
https://www.pokemon.com/uk/features/remember-the-region-johto-spotlight

Ecruteak remains strongly associated with towers, the Burned Tower and the Dance Theater.

Reusable structure:

A destroyed, altered or surviving building can remain a major part of public identity. Ruin state should not delete a structure from world history.

### Sinnoh locale identity

Official source:
https://www.pokemon.com/us/pokemon-news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-sinnoh-region

Sinnoh differentiates places through strong spatial identities, from dense Jubilife City to Eterna Forest and the Old Chateau.

Reusable structure:

Regional identity should come from spatial grammar and use as well as visual palette. Street shape, density, verticality, courtyards, covered passages and relation to terrain can help settlements feel different.

### Pokémon Tabletop — Mysterious Ruins

PTU source:
https://pokemontabletop.com/campaign-seeds-mysterious-ruins/

The seed explicitly allows a quiet town to expand after major discoveries. The Apparatus also demonstrates a structure functioning simultaneously as settlement, machine, habitat and mystery.

Reusable structure:

A building can remain narratively important for many arcs because its access, interpretation, occupants and physical state evolve.

### Pokémon Tabletop — The Road to Tomorrow

PTU source:
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

The Last Caravan uses surviving structures, recovered technologies and settlement-building as a campaign foundation.

Reusable structure:

Adaptive reuse creates stronger continuity than repeated construction from nothing. Existing structures can acquire new functions while retaining older physical traces.

### Eevee Expo worldbuilding presentation

Source:
https://www.eeveeexpo.com/expo-news/

Eevee Expo's coverage of Pokémon Covenant highlights custom buildings and repeated environmental details as part of maintaining world/story cohesion.

Reusable structure:

Ouros can use recurring material and spatial motifs to create regional identity, but should create original grammars rather than copy a fangame's layouts or distinctive buildings.

### Minecraft settlement generation

Research source:
https://arxiv.org/abs/2307.09777

The paper separates terrain preparation, building layout, route planning and infrastructure placement, and finds different generation strategies suit different terrain.

Reusable structure:

Minecraft settlement generation should be terrain-aware. Do not stamp the same town plan into every biome or slope condition.

### Urban morphology

Research source:
https://arxiv.org/abs/1910.03219

The work uses block size, regularity and neighborhood composition to describe distinctive urban forms.

Reusable structure:

Ouros can define coarse spatial fingerprints such as irregular lanes, regular grids, linear harbor streets, terraced slopes or dispersed compounds.

### Location-based play and public space

Research sources:
https://arxiv.org/abs/1610.08098
https://arxiv.org/abs/1903.12041

These studies show game systems tied to geography can change use of streets and public spaces and can reinforce existing spatial concentration.

Reusable structure:

Do not put every valuable service, activity and point of interest into one optimal district. Settlement layout should preserve multiple useful public spaces and reasonable access paths.

## Derived principles

Physical structure, current use and historical meaning remain separate.

A structure can change from station to market, warehouse to club, school to shelter or industrial hall to habitat/research site while retaining the same persistent identity.

Architectural style is evidence, not identity proof. A visual tradition does not automatically prove builder, owner, occupant, ethnicity or political allegiance.

Damage does not erase provenance. Fire, abandonment, collapse or demolition should produce successor states and retained history.

Landmark identity may survive physical change. A replaced bridge can remain the same named crossing in public memory.

Settlement morphology should constrain navigation and world behavior. It can affect where crowds form, how emergency response reaches a block, where wildlife finds shelter and which public spaces become social hubs.

Adaptive reuse should preserve traces where feasible: old signage, sealed doors, foundations, obsolete service corridors, loading bays, changed rooflines or mismatched construction phases.

## PTU / Caelo boundary

This pass creates no new PTU terrain, cover, falling, climbing, demolition or building-damage rules.

A wall may become a blocker in a tactical projection when supported. A staircase can be walkable geometry when legal. A collapsing balcony cannot deal damage merely because Minecraft animates it.

The project-supplied primary Caelo PDFs were not reliably retrievable in this automation runtime. No new Caelo-specific architecture, urban-terrain, access or structural-hazard rule is asserted.

Python AutoPTU contains terrain-aware behavior and Features, but that is not evidence that Java or Minecraft may invent arbitrary building effects.

## Copyright boundary

This pass reuses high-level structures only: redevelopment, layered growth, adaptive reuse, landmarks, morphology and architecture as evidence.

Do not copy canonical Pokémon building layouts, distinctive fangame buildings, source-specific puzzles, dialogue, characters or plots.

## Conclusion

The built environment should sit between world history and Minecraft geometry.

Important structures need stable IDs, versioned physical states, changing uses, condition records and links to events and institutions. Minecraft renders the current version. Ouros preserves the complete history.