# Evolution, Life Stage & Transformation Research — Pass 53

Status: research/provenance only. Not Ouros canon. Not a rules source.

Date: 2026-08-20

## Scope and overlap check

The repository already models persistent Pokémon identity, breeding and Eggs, partnership/release, care, ecology, public memory, seasonality and implementation-aware encounters. It did not yet have a dedicated contract for permanent Evolution, branching paths, delayed Evolution, wild Evolution, post-Evolution continuity or the distinction between permanent Evolution and temporary battle transformations.

Existing files inspected before writing included `pokemon-agency-partnership-release-layer.md`, `breeding-eggs-nursery-lineage-layer.md`, `seasonality-calendar-phenology-layer.md`, `science-research-discovery-layer.md`, `encounter-implementation-contracts.md` and the Pass 52 engine snapshot.

## Official Pokémon research

### Evolution methods vary and can be delayed

Source: https://diamondpearl.pokemon.com/en-au/trainersguide/fundamentals/raising/

The official Brilliant Diamond/Shining Pearl guide treats Evolution as species-dependent. It documents level-based, stone, trade, friendship, time-of-day, gender and Move-related methods, and explicitly allows a Trainer to delay an available Evolution.

Reusable structure for Ouros:

- eligibility is different from resolution;
- one species can have a different trigger from another;
- delaying a change can be a valid state rather than an error;
- Evolution can alter Moves, types and Abilities, so downstream systems need authoritative refresh rather than narrative assumptions.

### A partner can remain unevolved

Sources:
- https://pokemonletsgo.pokemon.com/en-gb/story/
- https://www.pokemon.com/us/animation/seasons/11/episode-20-pika-and-goliath

The Let's Go partner Pokémon are explicitly presented as having no interest in evolving. The Pikachu story in `Pika and Goliath` also revisits an Evolution choice after defeat rather than treating Evolution as mandatory optimization.

Reusable structure:

A loss, available Evolution item or stronger evolved opponent can create social pressure or a decision scene, but none of those facts alone should force an important Pokémon to evolve.

### Place-linked Evolution

Source: https://www.pokemon.com/us/animation/seasons/11/episode-6-nosing-round-the-mountain

The story establishes Mt. Coronet as the relevant location for Nosepass to evolve into Probopass and has the transformation occur during a battle there.

Reusable structure:

A location can be meaningful to eligibility, but the narrative generator must query authoritative rules before treating location presence as sufficient. Place-linked Evolution can connect travel, research, local tradition and ecology without inventing a new mechanic.

### Evolution can occur during battle

Sources:
- https://www.pokemon.com/us/animation/seasons/1/episode-21-abra-and-the-psychic-showdown
- https://www.pokemon.com/us/animation/seasons/16/episode-11-a-unova-league-evolution

Pokémon fiction has used Evolution during active battles. This is useful as a future spectacle but is technically different from recording an Evolution between encounters.

Reusable structure:

Live tactical Evolution should be a separate implementation tier. It can require species/stat rebuild, Move and Ability refresh, footprint changes, state carry-over, event emission and AI re-evaluation inside one battle.

### Temporary transformation is a separate state machine

Sources:
- https://pokemonletsgo.pokemon.com/en-us/story/
- https://mega.pokemon.com/en-us
- https://legends.pokemon.com/en-au/news/adventure

Official material presents Mega Evolution as a temporary transformation that goes beyond regular Evolution and depends on its own requirements.

Reusable structure:

Permanent species history and temporary battle transformation history should never share one field. A temporary form should have start/end state and should not overwrite the Pokémon's persistent Evolution chain.

## PTU source boundary

Official PTU downloads remain available at:
https://pokemontabletop.com/downloads-and-resources/

External Pokémon game/anime methods are not PTU rules for Ouros.

The current Python AutoPTU repository does contain concrete Evolution infrastructure. At inspected head `e4bb0ca38b7018710af476ce365d515a387de4e7`:

- `auto_ptu/career/evolutions.py` loads compiled PTU lineage/minimum-level data, builds immediate Evolution edges, filters by region/level and chooses a deterministic candidate;
- `auto_ptu/career/roster.py` preserves the same `pokemon.id`, replaces `species`, refreshes identity/Abilities and appends an `evolution_history` event.

This is useful implementation evidence for persistent identity. It is not sufficient evidence that all PTU/Caelo Evolution conditions are represented, nor that deterministic branch selection is the desired policy for player-important Pokémon.

## Community and fangame research

Source: https://lakevalor.net/threads/fanfiction-writers-how-do-you-decide-when-to-evolve-a-pokemon.23535/

Use only as community design discussion. Writers place Evolution at different kinds of beats: training milestones, climaxes, ordinary progression and character moments. Ouros should therefore avoid one predictable formula where every Evolution happens at a dramatic boss moment.

Source: https://eeveeexpo.com/threads/9331/

Use only as fangame design discovery. Contemporary fan projects can treat evolution data, regional identity and long-running consequences as part of a larger persistent campaign. Do not copy custom species, Moves, regions, characters or plots.

## Design conclusions

### Persistent identity survives Evolution

`pokemon_entity_id` remains stable. Species history changes. The individual does not become a new entity.

### Eligibility, intention and resolution are separate

Store these separately when relevant:

- authoritative candidate paths;
- conditions currently satisfied;
- options known to the player/actor;
- authored or player-provided intention when one exists;
- authoritative resolved path.

Availability never proves intent.

### Branches require provenance

A branching Pokémon should retain why a path was considered legal, what source established the condition and what event actually resolved it. A deterministic Career helper must not silently decide canon for an important Pokémon when the governing rules leave a meaningful branch.

### Wild Evolution is first-class

A known wild individual, institutional Pokémon, research subject or released former partner may evolve without capture. The same persistent entity can later reappear with a changed species/form and an intact prior history.

### Downstream systems update independently

Evolution may change size, movement, battle build, habitat use, care needs, work suitability, transport assumptions or public recognition. Each linked system must refresh from authoritative data. Species change alone cannot invent a new mount permission, job capability, Loyalty state or environmental effect.

### Evolution aftermath can support noncombat stories

Useful scenes can focus on adapting a home, workplace, equipment, route, team tactics, public records or routines after the change. These should not invent obedience penalties or medical problems.

### Mid-battle Evolution is a separate implementation tier

Between-scene Evolution can exist in world state before live tactical Evolution exists. A live battle transition needs its own Java contract and parity evidence.

## Originality boundary

This pass uses source material only for high-level structural lessons. Do not copy dialogue, named plots, fanfiction prose, fangame characters, custom species or distinctive story sequences.

## Unresolved questions

- What exact PTU/Caelo rules govern minimum levels, branching, items, trade, friendship/Loyalty, time, location and other Evolution triggers?
- Which Caelo overrides apply to regional forms or Evolution methods?
- Which important Pokémon require an explicit player decision when multiple paths are legal?
- Can wild Pokémon evolve during offline world advancement?
- How will Cobblemon preserve the same entity across a species transition?
- Which mechanical data must be recalculated immediately after Evolution?
- Is live mid-battle Evolution in AutoPTU-Java scope, or should the first implementation remain between battles?
