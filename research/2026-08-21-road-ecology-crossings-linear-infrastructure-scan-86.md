# Ouros Research Scan — Pass 86 — Road Ecology, Wildlife Crossings & Linear Infrastructure

Status: RESEARCH ONLY. Not Ouros canon. External works are used only for high-level structural lessons. Do not copy protected prose, characters, dialogue, plots, maps, mechanics, or distinctive setting elements.

Date: 2026-08-21

## Why this pass exists

The repository already has Travel, Conservation, Public Works, Freshwater, Urban Public Space, Cartography, Crisis, Biosecurity and multiple ecosystem layers. Roads currently exist mainly as human connections, while habitat corridors exist mainly as conservation objects. A missing layer remains between them: how roads, rails, culverts, fences, bridges, utility corridors and similar linear infrastructure alter movement, habitat connectivity and behavior over time.

A road can improve human access while fragmenting a wild population. A culvert can move water successfully while remaining poor passage for some terrestrial or aquatic species. A crossing structure can exist physically but remain unused for years. A fence can reduce road entry while also redirecting movement toward another location. These are persistent world-state problems, not automatic battle hazards.

## Sources and reusable lessons

### Pokémon — Dig Those Diglett!

Source: https://www.pokemon.com/us/animation/seasons/1/episode-30-dig-those-diglett

Official Pokémon material places Trainers at a major construction project where Diglett interfere with the work and the initial human response is to recruit battlers to remove them. The reusable lesson is not the episode plot. It is the conflict structure: infrastructure project + existing Pokémon use of the landscape + incomplete understanding + a proposed combat solution that may be wrong.

Ouros use:
- construction projects should check prior ecological use before labeling Pokémon an obstruction;
- a project delay can become a survey, redesign, mitigation or coexistence problem instead of a mandatory battle;
- contractors, researchers, local residents and conservation actors can hold different but legitimate views.

### Pokémon — The Lost World of Gothitelle!

Source: https://www.pokemon.com/us/animation/seasons/14/episode-21-the-lost-world-of-gothitelle

The construction of Skyarrow Bridge changes transport patterns and makes a previous water-taxi service obsolete. The reusable structure is infrastructure succession: a new connection can solve one mobility problem while ending older livelihoods, routines and relationships.

Ouros use:
- new roads and bridges should change service networks, settlement activity and memory;
- replacing an old route can create stranded infrastructure, unemployed operators, repurposed stations or cultural nostalgia;
- a successful public-works project can still have real losers without being villainous.

### Pokémon — Mind-Boggling Dynamax!

Source: https://www.pokemon.com/us/animation/seasons/23/episode-5-mind-boggling-dynamax

A Pokémon obstructing a rail crossing creates immediate danger to transport. The reusable principle is that infrastructure and wild Pokémon can produce acute conflicts even when neither side is malicious.

Ouros use:
- route safety incidents can emerge from ordinary movement or habitat overlap;
- resolving the immediate danger should remain separate from understanding why the overlap occurred;
- a one-time incident does not prove a persistent corridor problem.

### Pokémon — Mass Hip-Po-Sis

Source: https://www.pokemon.com/uk/animation/seasons/10/episode-44-mass-hip-po-sis

The episode includes a migrating Hippopotas separated from its herd and later reuniting. The reusable pattern is that wild-group movement has destinations and continuity independent of Trainer travel.

Ouros use:
- a route crossing can interrupt a migration without turning the herd into enemies;
- a stranded individual may belong to a larger persistent collective;
- road-crossing observations can feed collective-state and migration-state rather than generate generic spawns.

### Pokémon Tabletop — Campaign Seeds: The Road to Tomorrow

Source: https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

PTU's public campaign-seed material emphasizes reconstruction, institutions, exploration and player choices that alter future society. That supports infrastructure projects whose design creates downstream consequences rather than a static map upgrade.

Ouros use:
- players can influence route alignments, crossing projects or restoration priorities;
- infrastructure decisions can change settlement growth, access, ecology and future jobs;
- a project should leave a historical record of alternatives considered and tradeoffs accepted.

### Pokémon Tabletop — GM Advice: Your First PTU Session

Source: https://pokemontabletop.com/gm-advice-your-first-ptu-session/

Public PTU GM guidance offers encounter motivations such as territorial obstruction, protection and theft instead of assuming every battle begins from random aggression.

Ouros use:
- wildlife near roads may be defending a crossing, nest, feeding site or displaced individual;
- the world-state reason for an encounter should exist before tactical resolution;
- withdrawal, bypass and observation can be valid narrative resolutions even when tactical support for them is not yet implemented.

## Road ecology and wildlife-crossing research

### FHWA / U.S. Fish & Wildlife Service roadway design guidance

Source: https://highways.fhwa.dot.gov/sites/fhwa.dot.gov/files/docs/federal-lands/programs/federal-lands-planning-program/8266/fws-rdg.pdf

The guidance treats roads as both collision risks and fragmentation barriers. Avoidance behavior can matter even when direct collisions are rare. Crossing structures work best when designed for target species and combined with guidance or barrier fencing where appropriate.

Reusable lessons:
- collision frequency and fragmentation are separate metrics;
- a road can damage connectivity even if almost nothing is visibly killed on it;
- mitigation must consider the species or movement behavior involved;
- fencing can redirect movement and therefore creates new spatial state rather than simply deleting risk.

### U.S. Forest Service — Highway Crossing Structures for Wildlife

Source: https://www.fs.usda.gov/psw/publications/documents/psw_gtr271/psw_gtr271_007.pdf

Overpasses can reconnect habitat for many terrestrial species, while underpasses, bridges and culverts can serve terrestrial and aquatic passage. Existing structures can sometimes be retrofitted rather than replaced.

Reusable lessons:
- crossings are infrastructure assets with versions, dimensions and surrounding habitat;
- a bridge or culvert can have a transport role and a wildlife-connectivity role at the same time;
- retrofit projects create good quest structures because they link public works, surveying, construction and ecological monitoring.

### U.S. Forest Service — Wildlife Crossings guidance

Source: https://www.fs.usda.gov/rm/pubs/rmrs_gtr102_2.pdf

Roads are often placed near streams and floodplains that are already natural movement corridors. Crossing structures, bridge design and seasonal road closures can reduce fragmentation and conflict.

Reusable lessons:
- Road Ecology must connect directly to Freshwater and riparian-corridor state;
- a culvert can pass water yet still create an ecological barrier;
- seasonal closure can be an operational tool separate from permanent route state.

### FHWA — Wildlife Crossing Workshop material

Source: https://www.environment.fhwa.dot.gov/env_initiatives/eco-logical/documents/NC_TN_Wildlife_Crossing_Workshop.pdf

Monitoring shows that use of crossings can increase over years as animals learn to use them. Camera observations are useful, but merely seeing animals in a structure does not prove that it meets the target objective.

Reusable lessons:
- crossing success needs a baseline and longitudinal monitoring;
- `used once` is not equivalent to `effective corridor restored`;
- camera records should connect to the existing Photography/Visual Evidence layer;
- crossings can have adoption history and species-specific response.

### FHWA — Fish Passage at Roadway-Stream Crossings

Source: https://www.fhwa.dot.gov/engineering/hydraulics/pubs/07033/07033.pdf

Road-stream crossings can fragment river systems when hydraulic structures are designed only to pass water. Aquatic animals need connectivity for feeding, shelter, reproduction and responses to disturbance.

Reusable lessons:
- a culvert has hydraulic state and biological-passage state separately;
- Freshwater flow, flood capacity and wildlife passage must not collapse into one `culvert_ok` flag;
- road repair can improve human access while worsening passage if ecological constraints are ignored.

## Design conclusions for Ouros

### 1. Linear infrastructure needs persistent ecological state

A road is more than a `travel_connection`. It should reference segments where noise, lighting, fencing, drainage, traffic, bridges and crossings interact with known movement corridors.

### 2. Movement evidence must be versioned

A crossing may be unused initially and heavily used later. A seasonal migration can shift. A road closure can temporarily restore at-grade movement. Historical camera traps can therefore remain correct for their observation window without defining current behavior.

### 3. Crossing effectiveness is not binary

Useful dimensions include:
- target movement supported;
- observed use;
- avoidance near the approach;
- mortality/collision observations;
- fence-end leakage;
- aquatic passage;
- maintenance state;
- seasonal accessibility;
- nearby habitat continuity.

Do not reduce these to one global score unless a UI summary is later needed.

### 4. Roads can create indirect narrative consequences

Possible causal chains:

road opens -> travel improves -> traffic rises -> one collective avoids old route -> crossing pressure concentrates elsewhere -> residents report new sightings -> public works proposes mitigation.

culvert replacement -> water passes normally -> fish passage worsens -> downstream survey changes -> hatchery/restoration project is reconsidered.

seasonal closure -> human detour increases -> old road becomes temporary wildlife corridor -> tourism pattern changes -> local business reacts.

### 5. Route safety and ecological truth stay separate

A collision report does not prove population decline. A lack of collisions does not prove healthy connectivity. A Pokémon standing on a road does not prove migration. A road-crossing sign does not prove current use.

## PTU/Caelo boundary

This pass does not create PTU movement, collision or road-hazard rules.

Do not infer:
- roadway collision damage;
- knockback from vehicles;
- forced movement from fences;
- Rough/Slow Terrain from asphalt, gravel, ditch or culvert;
- interception reactions;
- vehicle initiative;
- herd morale;
- capture restrictions;
- road-crossing Skill DCs;
- automatic Pack Mon or Run Away behavior;
- aquatic current penalties inside culverts.

Exact mechanics remain subject to PTU/Caelo source validation and live AutoPTU-Java implementation evidence.

## Proposed integration targets

This research should feed a dedicated Road Ecology / Linear Infrastructure layer connecting:
- Travel & Transport;
- Conservation & Stewardship;
- Civic/Public Works;
- Freshwater/Hydrology;
- Cartography;
- Photography/Visual Evidence;
- Wild Collectives;
- Biosecurity;
- Urban Public Space;
- Architecture/Infrastructure;
- Cobblemon population projection;
- encounter implementation contracts.

## Copyright / attribution note

No protected dialogue or distinctive story text is copied into Ouros. Pokémon episodes and PTU/community material are used only for abstract conflict structures and design lessons. Government and scientific guidance is used for general ecology/infrastructure design principles. All source URLs are retained here for provenance.