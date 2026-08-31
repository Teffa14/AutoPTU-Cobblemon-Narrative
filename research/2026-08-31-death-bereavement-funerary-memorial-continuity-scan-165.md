# Death, Bereavement, Funerary and Memorial Continuity Scan — Pass 165

Status: RESEARCH ONLY — NON-CANON
Date: 2026-08-31
Narrative head inspected before writing: `9b435d75865b2dd9a1ce5019cb1b15c089b16da0`

## Purpose

This pass investigates a missing continuity surface between health/care, family/kinship, ritual/tradition, material culture, archives and public memory: how Ouros should preserve mortality reports, confirmed deaths, remains status, funerary episodes, resting places and private or community bereavement without treating any one representation as omniscient truth.

The full repository tree was inspected before selecting this gap. Existing files already own public memorial memory, sacred-site interpretation, ritual traditions, archives, family/kinship, physical objects and care. This pass therefore proposes only the mortality/funerary lifecycle and outward links to those authorities.

## Existing authority boundaries

Public Memory remains authoritative for collective remembrance, reputation, event legacies, anniversaries and competing public narratives.

Myth / Archaeology / Sacred Sites remains authoritative for sacred claims, spiritual interpretations, archaeology and uncertain supernatural readings.

Ritual / Tradition remains authoritative for inherited practices, observances, transmission and variation.

Family / Kinship remains authoritative for kin relationships and household consequences.

Material Culture remains authoritative for physical markers, monuments, keepsakes and their object histories.

Archives remains authoritative for preservation and later access to records after those records exist.

Health / Care remains authoritative for injury, treatment, stabilization and care before a canonical mortality fact is established.

Minecraft, Cobblemon and Craftics remain presentation and adapter layers. Entity despawn, faint animation, model replacement, tombstone blocks or visible Ghost Pokémon cannot establish death.

## Public Pokémon sources

### Pokémon Tower / House of Memories / burial grounds

Source family:

- Bulbapedia, Pokémon Tower / death and burial-ground coverage: https://bulbapedia.bulbagarden.net/wiki/Death
- Bulbapedia, House of Memories: https://bulbapedia.bulbagarden.net/wiki/House_of_Memories

Reusable structures:

- burial sites can persist while the surrounding institution changes;
- graves may be moved or rehoused when a building changes function;
- memorial infrastructure can have access rules distinct from public visibility;
- mourning sites can remain socially important long after the underlying death;
- people visit for remembrance even when no quest or battle is occurring.

Excluded:

- named character plots;
- copied dialogue;
- exact geography;
- any assumption that a Ghost-type Pokémon proves the identity or continued agency of a deceased being.

### Mt. Pyre

Source:

- Bulbapedia, Mt. Pyre: https://bulbapedia.bulbagarden.net/wiki/Mt._Pyre

Reusable structures:

- one site can combine graves, caretakers, visitors, ritual behavior, local history and unrelated danger;
- grieving visitors can coexist with Trainers or other actors whose reason for being there is different;
- a funerary landscape can accumulate older structures and later uses;
- visiting a resting place can be an ordinary recurring act rather than a one-time story climax.

Excluded:

- Team Aqua/Magma plots;
- Red/Blue Orb material;
- Phoebe-specific story beats;
- supernatural claims as verified world facts.

### Celestial Tower

Source:

- Bulbapedia, Celestial Tower: https://bulbapedia.bulbagarden.net/wiki/Celestial_Tower

Reusable structures:

- a burial site can include a repeatable remembrance practice such as ringing a bell;
- different mourners may use the same place for different relationships and memories;
- a care episode for a living, fainted Pokémon can occur at the same location as memorial activity for deceased Pokémon, reinforcing that `FAINTED != DEAD`;
- remembrance actions can be recorded without inferring an actor's total internal emotional state.

Excluded:

- copied character arcs;
- supernatural truth claims derived from the bell;
- any rule that a remembrance act grants mechanical effects.

### Death and Ghost-type distinction

Source:

- Bulbapedia, Death in the Pokémon world: https://bulbapedia.bulbagarden.net/wiki/Death

Useful boundary:

The franchise contains explicit deaths and burial grounds, while Ghost-type Pokémon are living Pokémon even where lore sometimes associates species with spirits. Ouros should therefore never equate Type with mortality identity.

Proposed invariant:

`GHOST_TYPE != IDENTIFIED_DECEASED_ENTITY`

## PTU public evidence

Public PTU discussion preserves an important baseline: Fainted is a recoverable rules state. A community rules discussion quotes PTU handling where a Pokémon below 0 HP may be Fainted and can later regain consciousness through healing / revival procedures.

Source:

- Pokémon Tabletop forum, "Some things I've been trying to figure out": https://www.tapatalk.com/groups/pokemon_tabletop/some-things-i-39-ve-been-trying-to-figure-out-t2230.html

A second PTU discussion quotes Features that explicitly modify when a Trainer or Pokémon Faints relative to negative HP and Injuries.

Source:

- Pokémon Tabletop forum, "Gaining Ticks of HP with Injuries": https://www.tapatalk.com/groups/pokemon_tabletop/gaining-ticks-of-hp-with-injuries-t5254.html

Design consequence:

Narrative must not infer canonical death from `Fainted`, negative HP, one failed battle, one Injury threshold or use of a Revive-like recovery mechanic unless the exact project-approved PTU/Caelo source establishes a mortality rule and the engine contract implements it.

Exact PTU/Caelo death thresholds, fatal-injury procedures and any Caelo modifications remain UNKNOWN in this pass because no exact project-source contract was found in the Narrative repository search. No new mortality mechanics are imported from forum paraphrases.

## Cemetery and heritage-design sources

### National Park Service — cemetery preservation

Sources:

- https://www.nps.gov/subjects/nationalcemeteries/publications-and-reports.htm
- https://www.nps.gov/subjects/nationalcemeteries/cemetery-preservation-guidance.htm
- https://www.nps.gov/articles/000/cemetery-preservation-course-documentation.htm
- https://www.nps.gov/grsm/planyourvisit/burial_landscape.htm

Reusable structures:

- burial grounds are landscapes whose physical condition and meaning change over time;
- markers, paths, vegetation, boundaries and access can have independent histories;
- documentation can use photographs, maps, notes and later surveys, each preserving different evidence;
- a cemetery may survive after much of the settlement around it disappears;
- preservation work should preserve historical change instead of flattening a site to one imagined original state.

Excluded:

- United States law;
- federal cemetery eligibility rules;
- military-specific ceremony;
- real-world religious prescriptions;
- real-world conservation specifications as mandatory Ouros mechanics.

## High-level reusable patterns

### Mortality has epistemic stages

A person can be missing, reported dead, presumed dead, confirmed dead, incorrectly reported dead or still unresolved. These stages need separate records.

### A death and its representation have different histories

The underlying event, a notice, a funeral, a grave marker, a public monument, an archive entry and a later legend can each have different dates, sources and confidence.

### Resting place and remains presence must stay separate

A cenotaph, memorial marker, relocated headstone or symbolic grave can exist without remains. Conversely, remains can be held or moved without a public marker.

### Mourning is observable only through evidence

Ouros can record attendance, words, offerings, visits, absences, maintenance and ritual participation. It should not generate an omniscient emotion state merely from those acts.

### Cemeteries can be long-lived locations

A burial landscape may outlive roads, institutions, names, settlements and political boundaries. This makes it useful for multi-generation environmental storytelling.

### Corrections do not erase earlier reports

If a premature death report is corrected, the earlier report remains part of history with a superseded status. Characters who acted on it may still have consequential memories or decisions.

## Explicit non-transfer rules

Do not copy protected dialogue, named plot structures or distinctive character arcs from Pokémon media.

Do not generate exact death mechanics from community discussion.

Do not convert real-world cemetery law into Ouros canon.

Do not infer spiritual truth from burial customs, Ghost-type species, apparition-like presentation or belief.

Do not treat a memorial's heroic inscription as an objective account of the deceased.

Do not treat body/remains custody as ownership unless canon explicitly defines a lawful or cultural relationship.

## Proposed truth boundaries

`DEFEATED != DEAD`

`FAINTED != DEAD`

`DEATH_REPORTED != DEATH_CONFIRMED`

`MISSING != DEAD`

`PRESUMED_DEAD != CONFIRMED_DEAD`

`REMAINS_UNRECOVERED != SURVIVED`

`GRAVE_EXISTS != REMAINS_PRESENT`

`MEMORIAL_EXISTS != DEATH_PROVEN`

`FUNERAL_HELD != PUBLIC_MEMORY_UNIFORM`

`MOURNING_PRACTICE != INNER_EMOTION`

`MEMORIALIZED != CANONICAL_HEROISM`

`SPIRITUAL_CLAIM != WORLD_FACT`

`GHOST_TYPE != IDENTIFIED_DECEASED_ENTITY`

`MINECRAFT_ENTITY_DESPAWN != DEATH`

`COBBLEMON_FAINT != DEATH`

`TOMBSTONE_BLOCK != CANONICAL_GRAVE`

## Engine-aware design observations

Death continuity should be noncombat-first. Most funerary, bereavement and memorial scenes need no BattleSpec at all.

If danger appears around a resting site, procession, search site or records office, the battle contract should resolve only the immediate tactical perimeter. It must not decide death confirmation, remains identity, funeral completion, spiritual peace, bereavement resolution or public legacy.

Mechanically rich versions can require complete movement, escort/withdrawal, hazards/zones/reactions, lifecycle, individual Move/Ability/Item/Feature parity, tactical AI and adapter playback. Reduced versions can pause the social process, remove noncombatants and protected objects from BattleSpec, freeze geometry and return only a local route/perimeter fact.

## Canon status

Everything in this file is research and design extraction. Nothing here establishes that Ouros currently has a particular cemetery, funeral custom, afterlife doctrine, death mechanism, burial law, cremation practice, spiritual institution or memorial tradition.

Those remain authored canon decisions.