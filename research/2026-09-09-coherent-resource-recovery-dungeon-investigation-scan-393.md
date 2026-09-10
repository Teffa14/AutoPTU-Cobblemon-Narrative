# Coherent Resource Recovery, Dungeon Investigation and Research-Site Progression Scan — Pass 393

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-09

## Repository review and deduplication

The current recursive repository tree, `CURRENT_FOCUS.md`, repository authority rules, the Pass 391 recovery-manifest work, Pass 392 resource-catalog checkpoint work, relevant tests/tools, current canon index and Kairos source index were inspected before writing.

Recent heavily processed anchors including Pokémon Desolation, Pokémon Gaia, Pokémon Rejuvenation, Pokémon Wastelands, Pokémon Infinity, Pokémon Bushido, Pokémon Odyssey, Pokémon Prisme, Pokémon Stalactite, Valoryn, Pokémon World Tour and the recent archaeology/recovery sources were not reused as primary narrative anchors here.

Repository search found no prior use of Pokémon Empyrean by name. The PTU campaign-log entry used below is also new to this pass's research record.

## Source 1 — Apache Flink consistent checkpoints

Source: Apache Flink, Operations.
URL: https://flink.apache.org/what-is-flink/flink-operations/
Retrieved: 2026-09-09.

Flink describes recovery from consistent checkpoints of application state and treats savepoints as consistent snapshots for stateful applications.

Reusable Ouros structure:

- several valid subsystem snapshots can still be unusable together if they represent different logical moments;
- recovery needs one coherent cut across owners rather than independent "latest" selection;
- the coordinator/manifest should select the generation while each owner remains responsible for validating its own domain state.

This source informs implementation architecture only. Ouros does not import Flink APIs, distributed-computing semantics as game rules, or exactly-once guarantees as fiction.

## Source 2 — PTU campaign log #13: haunted mansion exploration

Source: r/PokemonTabletop campaign log #13.
URL: https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5/
Session date reported by author: 2021-06-06.

The session summary describes a haunted mansion explored as a set of functionally different rooms. Progress includes combat, a riddle, a blocked basement, environmental interaction, captures and directional cues rather than one uninterrupted battle sequence.

Reusable Ouros structure:

- a dungeon can be assembled as evidence-bearing rooms with different interaction verbs;
- one blocked route can preserve mystery while other rooms provide information or optional encounters;
- environmental clues can point toward progression without requiring an omniscient quest marker;
- a location may remain narratively interesting after a combat is resolved because its spatial relationships and inaccessible areas still matter.

No mansion layout, riddle text, characters, captures, dialogue, items or sequence is imported.

## Source 3 — Pokémon Empyrean: investigation nested inside ordinary regional progression

Sources:
- Pokémon Fan Game Wiki, Pokémon Empyrean: https://pokemon-fan-game.fandom.com/wiki/Pok%C3%A9mon_Empyrean
- Pokémon Empyrean Wiki, Sylen City Research Center: https://pokemonempyrean.fandom.com/wiki/Sylen_City_Research_Center
Retrieved: 2026-09-09.

Public summaries describe a regional journey that combines League-style progression with a personal investigation and a broader mystery around artificial berserk Pokémon. The Research Center page also shows story-gated access to deeper floors and disappearing/temporary documentary evidence.

Reusable Ouros structure:

- personal motive, regional travel and institutional investigation can overlap without every quest belonging to one faction track;
- a research building can unlock deeper access as knowledge or story state changes;
- evidence availability can be time-sensitive, so historical observation and current accessibility should remain separate facts;
- returning to an institution after field discoveries can reveal different actionable context without rewriting prior observations.

No Omuran/Deshret lore, father-kidnapping plot, berserk Pokémon concept, characters, floors, rewards, custom types, species variants, mechanics or dialogue is imported.

## Source 4 — PTU/Kairos authority boundary

Internal router checked: `sources/kairos/KAIROS_SOURCE_INDEX.md`.

Relevant routes include Skills/Edges/Features, utility classes, campaign/session structure, encounter creation, recurring rivals, boss encounters, movement, status, hazards, terrain/weather and Items/Gear.

The index explicitly states that it is a routing aid rather than rules acceptance. Therefore this pass introduces no new Skill check, Item effect, Trainer Feature, puzzle bonus, forced-movement rule, hazard damage or tactical interrupt.

## Synthesis for Ouros

The strongest combined pattern is a persistent investigation where three histories can diverge legitimately:

1. an NPC's plan and knowledge history;
2. environmental/evidence history at a site;
3. current resource availability and custody state.

A dungeon or research site can expose those histories through room-by-room evidence. One room can prove a route was previously surveyed. Another can show that equipment was reassigned. A later-access floor can reveal why an earlier team made a decision that looked irrational from current state alone.

Recovery architecture must preserve the same separation after restart. A technically valid but temporally mixed generation could otherwise turn an honest historical contradiction into impossible fiction.

## Capability classification for mechanically rich variants

Targeting/footprints/range/LoS: VERIFIED only within audited scopes. Required if tactical rooms use range/visibility-based placement or interactable zones.

Base movement legality: VERIFIED only within audited scopes. Sufficient for ordinary movement where no richer movement effect is assumed.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for collapsing corridors, dragging, forced displacement, interception or carrier movement affected by combat.

Core calculations: VERIFIED only within audited scopes.

Action economy/initiative: VERIFIED for audited primitives only. Any inspect-console, secure-evidence, transfer-resource or operate-door action inside tactical resolution needs an explicit contract.

Full turn/round lifecycle: PARTIAL. Required for timed locks, delayed shutdowns, phased hazards or round-based access changes.

Full stateful damage pipeline: PARTIAL. Required if damage changes persistent objective state or equipment availability.

Status lifecycle: PARTIAL. Required if lasting statuses affect access, carrying or objective timing.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Required for unstable floors, smoke/dust visibility, triggered doors, flooding, electrical zones or reaction hazards.

Move-specific behavior: individually gated.

Abilities: individually gated. Current Impostor evidence does not verify the family.

Items: individually gated. A narrative field resource is not automatically a PTU Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for investigation-first, protect-evidence, retrieve-resource, escort, split-team search, objective-aware withdrawal and disengage-after-objective unless exact policies gain live evidence.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for persistent room/evidence identity, objective acknowledgement, resource interaction and authoritative non-KO completion playback.

## Reduced-version principle

The same investigation can run without AutoPTU by resolving the dangerous transition between rooms outside structured combat. Semantic time, persistent evidence, private knowledge, resource state, communications, travel/replanning and coherent recovery are enough to preserve the premise.

This reduced version does not give the Minecraft adapter permission to simulate missing PTU rules.
