# Archaeological context and layered-ruin scan — Pass 383

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-09

## Repository-first inspection

Before writing, the current narrative `main` head `48f644e7b22948f085be6b48823197a2fda5c2e8` was inspected together with `CURRENT_FOCUS.md`, `canon/README.md`, the current canon inventory, Pass 382 research/proposal/readiness files, `sources/kairos/KAIROS_SOURCE_INDEX.md`, and repository-wide searches for archaeology, archaeological, excavation, stratigraphy, artifact provenance and ruin-site documentation.

No dedicated archaeological-site evidence/context layer was found. Existing work covers archives, museums, preservation, world evidence, travel interruption, environmental continuity and many site-specific continuity systems, but not the specific distinction between an object, its find context, a nonportable site feature, a later reinterpretation and the effect of excavation itself.

Recent fan-game/PTU anchors were also checked to avoid recycling Pokémon Prisme, Stalactite, Dreamstone Mysteries, Odyssey, Bushido, Valoryn, Infinity, Golurk Rising, PokéTaka, Wastelands and the Pass 382 route-closure material.

## Internal PTU/Kairos routing

`sources/kairos/KAIROS_SOURCE_INDEX.md` identifies relevant internal authority areas without making them Ouros canon:

- Researcher, Paleontologist, Topographer and other utility classes in the Skills/Features/Class material;
- movement and tactical positioning at pp. 382+;
- hazards at p. 401;
- terrain/weather at pp. 404+;
- world population/ecosystem guidance at pp. 437+;
- campaign/session structure at pp. 449+;
- encounter creation at pp. 470+;
- recurring rivals/villains at p. 477;
- boss encounters at pp. 485+;
- gear/items/crafting at pp. 495+.

These page routes are comparison aids only. Any Trainer Feature, Move, Ability, Item, hazard or tactical interaction used by an authored ruin must still be admitted through authoritative PTU/Caelo/AutoPTU evidence.

## Public source 1 — Pokémon Gaia

Source family: fan-made ROM hack / archaeological mystery structure.

Public references:
- https://pokehackdb.com/hacks/pokemon-gaia
- https://pokehackzone.com/hacks/pokemon-gaia

High-level reusable structure:

Pokémon Gaia builds a regional mystery around ancient remains distributed through the overworld rather than isolating all history in one exposition scene. Ruins, monuments, seismic disturbance and exploration remain connected to the present-day journey.

Useful Ouros abstraction:

- historical evidence can be geographically distributed;
- a ruin can be a recurring field site rather than a one-use dungeon;
- later observations can change the interpretation of earlier evidence;
- access methods and route knowledge can be part of discovery without making combat the only progression gate;
- a regional mystery can grow from multiple local sites whose meaning is initially incomplete.

Not imported:

Orbtus, its civilization, Professor Redwood, the New Elders, Reliquia Ruins, its inscriptions, temples, earthquakes, plot beats, characters, maps, puzzles or Pokémon distributions.

## Public source 2 — U.S. National Park Service archaeological documentation guidance

Source: U.S. National Park Service, Archaeological Documentation Guidelines.

URL: https://www.nps.gov/articles/sec-standards-archeo-doc-guidelines.htm

High-level reusable structure:

The guidance treats archaeological specimens and their associated documentation as one documentary record. Maps, photographs, field notes, environmental samples and later curation all preserve information that can be lost if an object is detached from context.

Useful Ouros abstraction:

`FOUND_OBJECT != FULL_SITE_EVIDENCE`

A portable object may matter less than its exact location, surrounding material, orientation, layer, nearby feature and record of who observed or moved it. Removing an item can therefore create information loss even when the item itself remains in inventory.

This supports investigation play in which the player can discover, document, disturb, preserve or revisit evidence. It also creates legitimate disagreement between NPCs who have access to different portions of the record.

No real-world legal, cultural-resource or agency procedure is imported as Ouros law.

## Public source 3 — NPS Mound 7 excavation history

Source: U.S. National Park Service, Salinas Pueblo Missions National Monument, Excavation of Mound 7.

URL: https://www.nps.gov/sapu/learn/historyculture/excavation-of-mound-7.htm

High-level reusable structure:

The account shows a site whose later structure sits over earlier construction, and where excavation, stabilization, backfilling and visitor access change what remains visible while preserving different forms of evidence.

Useful Ouros abstraction:

- one physical site can contain multiple historical phases;
- an apparently single room/path/feature may belong to a later layer over something older;
- exposing a layer can change preservation risk and future accessibility;
- later restoration or backfilling can legitimately make earlier visible evidence inaccessible without erasing the historical record;
- revisiting the same place at a later semantic time can produce a different navigable and interpretable site.

The real site, culture, architecture and history are not transferred into Ouros.

## Public source 4 — NPS archaeological feature findings

Source: U.S. National Park Service, Golden Gate National Recreation Area, Archaeological Feature Findings.

URL: https://www.nps.gov/goga/learn/historyculture/merrie-way-feature-findings.htm

High-level reusable structure:

The source distinguishes portable artifacts from nonportable archaeological features such as built or cut elements that remain part of the site itself.

Useful Ouros abstraction:

`PORTABLE_FIND != SITE_FEATURE`

A puzzle or mystery does not need to reduce every clue to collectible inventory. A drainage cut, sealed doorway, worn floor, foundation alignment, hearth, post hole, channel, stair or altered wall can remain world-state evidence that players must inspect in place.

This is especially valuable for Minecraft projection because the evidence can exist as persistent blocks/entities/markers while interpretation remains in Ouros world state.

## Source synthesis for Ouros

The combined reusable pattern is a layered field site with four independent evidence families:

1. portable finds;
2. fixed features;
3. spatial/context records;
4. interpretations made by actors at specific times.

A robust archaeological mystery should preserve those independently. A later expert may reinterpret a feature without changing the original observation. A player may move an object and preserve the object while damaging contextual evidence. A site may be stabilized, flooded, collapsed, backfilled or restricted later while earlier maps and notes remain valid historical evidence.

## Narrative patterns enabled

### Revisit with changed meaning

The player first visits a ruin as a route obstacle or local curiosity. A later discovery elsewhere changes which details matter. Returning to the original location produces progression through interpretation rather than a newly spawned key.

### Conflicting experts without forced deception

Two researchers can disagree because one saw the site before disturbance and another saw it after stabilization or partial collapse. Both can be sincere.

### Preservation versus extraction

Removing a valuable-looking object can help an immediate objective while reducing future context quality. Documenting it in place can preserve evidence but cost time during a dangerous window.

### Layered construction mystery

A later structure may have reused an older foundation. The mystery advances when alignments, material changes or sealed connections show that apparently contemporary features belong to different phases.

### Environmental re-exposure

Flooding, erosion, burrowing Pokémon, construction work, root growth or a collapse can expose evidence briefly. The field site can therefore produce time-bounded quests without assuming that the environment itself is a tactical hazard unless the engine supports the exact mechanism.

## Mechanics boundary

The reduced archaeological loop is world-agent/world-state only:

- persistent site identity;
- semantic-time observations;
- portable-find identity;
- fixed-feature identity;
- observation records with actor/source/time;
- optional location/context metadata;
- later interpretation records that reference prior evidence;
- access/restriction state;
- ordinary semantic travel and communication.

It requires no AutoPTU combat.

A rich version may add tactical traversal, unstable footing, falling debris, hostile or territorial Pokémon, environmental phases, forced movement, statuses, reactive hazards or timed rescue. Each such addition inherits its exact permanent capability-category dependency and cannot be admitted from narrative intent alone.

## Candidate design rule

Preserve this invariant in future implementation:

`CURRENT_INTERPRETATION != HISTORICAL_OBSERVATION`

and

`OBJECT_IN_INVENTORY != ORIGINAL_FIND_CONTEXT_PRESERVED`

The site should remember what was observed, where and when, even if the later interpretation changes.
