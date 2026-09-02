# Cartography, Survey and Route-Marker Research Scan — Pass 203

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

Nothing in this file is Ouros canon unless separately promoted through `canon/`.

## Why this pass exists

Marea already has canonical physical coordinates, a route graph, Estación Mirador route reports, Tideglass route surveys, actor route knowledge and mutable route state. The missing seam is representational continuity: maps, sketches, survey copies, route-marker observations and annotations can be incomplete, stale, differently scoped or copied from one another without changing the underlying canonical geography.

This pass therefore does not redesign Marea, invent new coordinates or create a navigation subsystem. It studies how exploration games and tabletop practice make maps useful while preserving uncertainty and provenance.

## Repository continuity check

Canon reviewed before writing:
- `canon/README.md`
- `canon/marea-interior-map-resident-network-v2.md`
- `canon/npc-pokemon-dynamic-progression-v1.md`
- `canon/ouros-playable-foundation-v1.md`
- `canon/questline-taxonomy-v2.md`

Adjacent design reviewed:
- `design/travel-transport-expedition-layer.md`
- `design/engine-readiness-snapshot-pass-202.md`
- repository inventory through the current recursive tree

Relevant established facts:
- Sendero del Vidrio is the old survey road connecting Puerto Bruma and Loma Clara and branching toward Estación Mirador.
- Canonical anchor coordinates and the canonical route graph are already frozen in `marea-interior-map-resident-network-v2.md`.
- Estación Mirador maintains route reports and claims with provenance/revision history.
- Tideglass preserves route surveys.
- The Travel layer already separates physical route state from actor route knowledge and explicitly permits maps to be stale.

Pass 203 therefore owns map/survey artifacts and physical marker observations. It does not replace route-state authority, actor route knowledge, archive provenance, observation records or canonical coordinates.

## Source A — Pokémon Legends: Arceus, Survey Corps structure

Public source:
https://legends.arceus.pokemon.com/en-ca/story/

The official site describes Jubilife Village as a base of operations. Survey Corps members leave on assignments to study areas and return after survey work. The useful pattern is institutional fieldwork with an origin, an excursion and a return path through which observations become records.

Reusable design lessons:
- field representation can be produced by a specific survey event rather than appearing omnisciently;
- a survey has a date, author/team, area and purpose;
- returning from the field is a natural point for review, transcription and comparison;
- later survey work can refine an earlier representation without deleting the earlier edition.

Not imported:
- Galaxy Team structure;
- Hisui geography;
- Pokédex progression;
- rank rewards;
- any named character, mission or plot.

## Source B — Pokémon Legends: Arceus, research accumulation

Public source:
https://legends.arceus.pokemon.com/en-gb/gameplay/

The official gameplay material presents research as cumulative work: repeated tasks add information rather than a single observation instantly completing knowledge. Although the examples concern Pokédex research, the high-level structure transfers cleanly to survey records.

Reusable design lessons:
- representation can have completeness and confidence dimensions without becoming binary true/false;
- repeated observations can add coverage;
- a record may become more useful while still retaining unresolved portions;
- access to new field areas should remain a world/access fact, not something a map artifact grants by itself.

## Source C — Etrian Odyssey Nexus, player-built mapping

Public source:
https://atlus.com/etriannexus/

The official site explicitly describes mapping as part of exploration: players draw their own maps while navigating labyrinths, with auto-mapping available as an alternative convenience.

Reusable design lessons:
- a map can be a representation built from traversal rather than a magical reveal of world truth;
- annotation itself can be meaningful gameplay;
- map utility comes from remembered spatial relationships, landmarks and hazards;
- a convenient auto-generated representation should still be treated as a presentation layer rather than authority over world facts.

Not imported:
- Etrian labyrinth layouts;
- iconography;
- progression systems;
- battle mechanics.

## Source D — Pokémon Ranger: Guardian Signs, route obstruction and later access

Public source:
https://www.pokemon.com/it/videogiochi/pokemon-ranger-tracce-di-luce

The official page describes exploration in which currents, rocks and other obstacles can prevent passage, and some previously blocked passages can later become available. The useful lesson is that a representation of connectivity needs a time/version context: a path shown on an older map can remain physically real while its current traversability changes.

Reusable design lessons:
- route existence and current access state must remain separate;
- a marker for a blocked passage is an observation about a time/state, not a permanent rewrite of the route graph;
- maps may need revision after access changes;
- access changes should remain grounded in actual world events.

Not imported:
- Ranger authority;
- Styler mechanics;
- legendary traversal powers;
- Oblivia geography.

## Source E — PTU 1.05 Survival Skill

Public reference:
https://pturpg.wikidot.com/skills

The PTU reference places outdoor navigation, scouting, geology, geography and tracking under Survival. It also describes scouting an area to learn basic information and notes that terrain/environment can affect difficulty.

Mechanical boundary for Ouros:
- Narrative must not invent a separate Cartography Skill.
- Narrative must not invent map-reading DCs, navigation bonuses or automatic success from possessing a map.
- When a contested navigation/scouting action requires mechanics, the authoritative PTU/Caelo rules and current implementation must adjudicate it.
- A survey record may provide narrative information or evidence, but any mechanical modifier requires an explicit governing rule.

## Source F — PTU campaign mapping practice

Public community sources:
https://www.reddit.com/r/PokemonTabletop/comments/1ijdzo3/
https://www.reddit.com/r/PokemonTabletop/comments/1vgj9m3/

These discussions show active PTU GMs building region maps around biomes, routes, settlements and immediately relevant areas. The 2026 discussion is especially useful as evidence that current tabletop practice still treats region/route planning as a distinct authoring problem rather than assuming a complete game-style map exists automatically.

Reusable lesson:
- broad geography and locally detailed route representation can have different scopes;
- not every map needs the same resolution;
- a local field sketch can be useful without being a full regional atlas.

Community advice is not PTU authority and is not imported as rules.

## Source G — PTU battle-map practice distinguishes tactical map from route/region map

Public community source:
https://www.reddit.com/r/PokemonTabletop/comments/j7xrgf/

A long-running PTU GM distinguishes ordinary battle maps from larger route/city set pieces and recommends containing tactical battles within smaller zones even when the visual area is larger.

Reusable implementation lesson:
- an overworld/route map and a tactical BattleSpec map are different artifacts;
- a route sketch cannot automatically become battle geometry;
- a large Minecraft area cannot be assumed to be a legal PTU tactical footprint without conversion and validation.

## Source H — Hexcrawl design: world model versus player-facing representation

Public source:
https://thealexandrian.net/wordpress/17308/roleplaying-games/hexcrawl

The Alexandrian explicitly separates the GM-side geographic structure from what players directly perceive, emphasizing exploration and repeated discovery. The useful idea is representational separation, not the hex procedure itself.

Reusable design lessons:
- the canonical spatial model may contain more than any single actor-facing map;
- exploration should update actor knowledge and map artifacts without requiring the underlying geography to be procedurally invented;
- revisiting a known place can still produce new observations.

Not imported:
- hexcrawl travel rates;
- getting-lost procedures;
- random encounter rules;
- hex size or preparation doctrine.

## Cross-source synthesis

The strongest reusable pattern is a four-layer separation:

1. canonical geography and current physical route state;
2. survey observations produced at a time/place by actors;
3. map/survey artifacts that encode selected observations at a chosen scope and edition;
4. actor knowledge and UI projection derived from some subset of those artifacts and direct experience.

A discrepancy can therefore have several explanations without retconning the world:
- the map is old;
- the marker moved;
- the route state changed after publication;
- two surveys used different scopes or reference points;
- a copy omitted an annotation;
- a landmark has multiple local names;
- the observation was uncertain;
- the Minecraft build drifted from the canonical coordinate registry and requires an implementation fix.

## Proposed vocabulary for design review

`survey_event`: bounded observation work over a defined spatial scope.

`cartographic_artifact`: a persistent representation such as a map, sketch, plan, route diagram or annotated copy.

`cartographic_edition`: one version of an artifact with provenance and supersession links.

`map_feature_assertion`: a claim that a landmark, connection, marker, hazard or access note belongs at a represented location/state.

`route_marker`: a physical world object or durable feature used for orientation. Its physical state is separate from what maps say about it.

`marker_observation`: an observation that a marker was present, absent, damaged, moved or legible at a timestamp.

`spatial_scope`: the area and resolution an artifact claims to represent.

`reference_frame`: the coordinate/landmark basis used by the artifact. Canonical Minecraft anchors remain implementation references and need not be printed in-world.

## Hard boundaries

- `MAP_FEATURE != WORLD_FACT`
- `MAP_EDITION_LATEST != AUTOMATICALLY_CORRECT`
- `OLD_MAP != FALSE_MAP`
- `MARKER_PRESENT != ROUTE_OPEN`
- `MARKER_ABSENT != ROUTE_DESTROYED`
- `ROUTE_EXISTS != CURRENTLY_TRAVERSABLE`
- `PLAYER_MAP_REVEAL != CHARACTER_KNOWLEDGE`
- `CHARACTER_KNOWLEDGE != PUBLIC_KNOWLEDGE`
- `MINECRAFT_TERRAIN != CANONICAL_CARTOGRAPHIC_AUTHORITY`
- `BATTLE_MAP != OVERWORLD_MAP`
- `TACTICAL_LOS != CARTOGRAPHIC_VISIBILITY`
- `SURVEY_COMPLETED != EVERY_FEATURE_DISCOVERED`

## Relationship to existing Ouros layers

Travel owns connection state, journeys and actor route knowledge.

Observation owns observations and evidence quality.

Tideglass/archive provenance owns custody, copies and edition history of documents.

Information circulation owns who received which version.

Identity/delegated authority owns who is allowed to perform or approve a specific institutional action.

Pass 203 adds the spatial representation objects that those systems can reference.

## Caelo check

A literal indexed search for `Caelo` across Narrative, AutoPTU-Java and AutoPTU returned no source content in this run. The repository README still names Caelo Player's Guide, rulebook/errata, character-creation material and Region Location & Encounter List as authoritative inputs that must be consulted when available.

Therefore this pass does not define:
- regional surveying law;
- official map standards;
- legal coordinate systems;
- navigation credentials;
- cartographer licensing;
- route-marker standards;
- formal road-closure signage;
- any Caelo-specific Survival modification.

## Originality note

No protected map, route, character, dialogue, puzzle or plot has been copied. The new Ouros material should use only the abstract structures above: versioned representation, provenance, limited survey scope, physical markers, uncertainty and separation between overworld and tactical geometry.