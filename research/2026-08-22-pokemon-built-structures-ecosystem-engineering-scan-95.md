# Research Scan — Pokémon-Built Structures & Ecosystem Engineering

Status: RESEARCH / PROVENANCE. Not canon. Not a PTU rules source.

Pass: 95
Date: 2026-08-22

## Why this pass exists

The repository already models hydrology, caves, soil, wild collectives, conservation, architecture, road ecology, settlements and Pokémon agency. It did not yet have a dedicated authority for persistent structures created by wild Pokémon themselves.

This matters because a structure can outlive the encounter that created it. A dam can alter water level and wetland extent. A deep nest can intersect infrastructure. A burrow network can remain after its builders leave. A hive or colony site can become a landmark, research site, conflict point or historical object.

The reusable pattern is:

species-authored behavior -> construction event -> persistent physical structure -> environmental consequences -> observations and interpretations -> later maintenance/abandonment/reuse.

Do not collapse this into `Pokémon used Move X and terrain changed` unless PTU/Caelo and AutoPTU explicitly support that mechanic.

## Sources and reusable lessons

### Official Pokémon — Bibarel and Bidoof

Pokémon's official Pokédex says Bibarel makes its nest by damming streams with bark and mud and also builds with branches and roots. The official Bidoof page places Bidoof nests alongside water, while Pokémon's Bidoof Day material explicitly references observing a Bidoof-built dam in New Pokémon Snap.

Sources:
- https://www.pokemon.com/br/pokedex/bibarel
- https://www.pokemon.com/br/pokedex/bidoof
- https://www.pokemon.com/us/news/celebrate-bidoof-day-with-the-bidoof-quiz

Reusable lesson:
A Pokémon-built structure can be normal species behavior rather than a puzzle, attack, villain action or one-time scripted event. Its world consequences can persist after the individual Pokémon are gone.

Do not infer:
- every Bibarel builds a dam;
- every dam is safe or permanent;
- a dam is a PTU barrier/hazard;
- Bibarel can create or destroy water tiles during battle without a verified rule.

### Official Pokémon — Durant

The official Pokédex states that Durant lay eggs deep inside nests and can crunch through rock with their mandibles. Their colony construction and egg protection are persistent spatial behavior rather than merely battle flavor.

Source:
- https://www.pokemon.com/us/pokedex/durant

Reusable lesson:
A colony can create internal zones with different functions. A nest entrance, nursery depth, occupied chamber and abandoned chamber should not be treated as identical space.

Do not infer:
- generic tunneling speed;
- shared initiative or hive-mind AI;
- automatic Pack Mon behavior;
- rock destruction inside AutoPTU from species flavor.

### Official Pokémon — Bunnelby and Excadrill

Bunnelby can dig a deep nest rapidly. Excadrill builds maze-like nests far underground and can accidentally interfere with subway tunnels; its Pokédex also describes it as useful in tunnel construction.

Sources:
- https://www.pokemon.com/us/pokedex/bunnelby
- https://www.pokemon.com/uk/pokedex/excadrill

Reusable lesson:
Wild construction can intersect human infrastructure without malicious intent. A tunnel discovered under a road, railway or building is first a spatial/infrastructure problem; battle is optional.

Do not infer:
- every Ground-type can excavate;
- PTU Burrow equals permanent world excavation;
- an underground Minecraft tunnel proves which Pokémon made it;
- Excadrill flavor grants a general construction Feature.

### Official Pokémon — Combee Wall

An official anime episode describes a Combee Wall as a place where Combee gather and store nectar.

Source:
- https://www.pokemon.com/us/animation/seasons/10/episode-31-the-grass-type-is-always-greener

Reusable lesson:
Some constructed or accumulated sites can be resource stores, colony spaces and cultural landmarks at the same time. Access to the site does not imply ownership of its contents.

### Pokémon fan quest / roleplay discussion

A recent long-running Sinnoh trainer quest discussion explicitly treats Bidoof-built dams, nests, dens and silk bridges as ordinary examples of Pokémon-built homes. This is useful as community evidence that readers accept Pokémon habitat construction as part of everyday world texture rather than only as set-piece spectacle.

Source:
- https://forums.spacebattles.com/threads/to-live-is-to-dream-sinnoh-pokemon-trainer-quest.979188/page-5711

Reusable lesson:
The world feels more inhabited when constructed habitats exist before the player arrives and continue to matter after the immediate scene.

No prose, characters or plot elements from the quest are imported.

### Fanfiction pattern — abandoned structures as later resources

A publicly accessible PMD fan story uses an abandoned Bidoof dam as a source of old wood for a later camp. The exact story is not reused. The high-level pattern is valuable: an abandoned animal structure can become a historical material source, landmark or shelter while retaining provenance.

Source:
- https://m.fanfiction.net/s/12699122/1/Pokemon-Mystery-Dungeon-The-Dreamstone

Reusable lesson:
Abandonment is a state transition, not deletion. A structure can move from active habitat -> abandoned habitat -> salvage candidate -> historical site -> recolonized habitat.

### Real ecology — beavers as ecosystem engineers

NPS/USGS literature documents beaver dams reducing flow velocity, trapping sediment, raising local water tables, expanding riparian areas and creating habitat mosaics. These consequences show why persistent animal-built structures deserve their own causal state rather than a cosmetic prop.

Sources:
- https://www.nps.gov/grte/learn/historyculture/upload/persico_meyer_gye-beav_espl-RED.pdf
- https://pubs.usgs.gov/of/2014/1121/pdf/ofr2014-1121.pdf

Reusable lesson:
One construction can create secondary consequences across hydrology, sediment, vegetation and other species. Those downstream consequences should be represented through existing Ouros layers, not duplicated here.

Important boundary:
Real beaver ecology is a structural reference. Ouros must not assume Bibarel produce identical hydrologic outcomes, construction rates or ecological benefits without authored regional evidence.

### Habitat-construction research

A 2024 review of animal habitat construction emphasizes that animal-built structures can create or modify habitat and that effects must be understood in multi-species context rather than through one species alone.

Source:
- https://www.frontiersin.org/journals/environmental-science/articles/10.3389/fenvs.2023.1133879/full

Reusable lesson:
An ecosystem-engineering effect belongs in an evidence graph: builder observation -> structure -> measured environmental response -> dependent species response. Avoid jumping directly from builder presence to ecosystem conclusion.

## PTU / AutoPTU mechanical boundary

The available PTU-derived Python evidence shows that capabilities and creative actions can participate in battle actions, and Python contains explicit terrain/hazard and movement behavior in particular rules. That is not authority for a generic world-construction subsystem.

A narrative structure may be authored because species lore supports it, while any tactical consequence still requires exact mechanics.

Examples that remain blocked unless separately verified:
- dam tile creation;
- flooding during battle;
- breaking a dam with damage;
- tunnel creation or collapse during combat;
- digging under blockers;
- entering/exiting a burrow as forced movement;
- hive wall cover;
- nursery protection bonuses;
- shared colony reactions;
- structure HP;
- construction actions measured in rounds.

## Design conclusions for Ouros

1. Pokémon-built structures need stable IDs independent of the builder currently being loaded in Minecraft.
2. A structure may have builder attribution with confidence rather than certainty.
3. Construction, maintenance, abandonment, damage and reuse need separate events.
4. Environmental effects should be handed off to Hydrology, Soil, Flora, Wild Collectives, Conservation, Infrastructure and other existing authorities.
5. Removing a structure is a world-state decision with consequences; it is not automatic cleanup after an encounter.
6. Loaded blocks are presentation, not proof of builder, age, function or ecological effect.
7. Species flavor can justify a proposed structure type but never creates PTU combat mechanics by itself.
8. Abandoned structures can become habitats, heritage sites, salvage sources or hazards without losing provenance.
9. Different observers may disagree about who built a structure or whether it is still active.
10. A structure can be useful to humans and disruptive to infrastructure at the same time without making the Pokémon antagonists.
