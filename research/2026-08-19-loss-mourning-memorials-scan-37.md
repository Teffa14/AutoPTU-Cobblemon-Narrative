# Ouros Research Scan — Loss, Mourning, Memorials & Mortality Boundaries — Pass 37

Status: research/provenance only. Nothing in this file is established Ouros canon.
Date: 2026-08-19

## Why this pass exists

The repository already has dedicated layers for public memory, family continuity, care/recovery, cases and missing actors, archives, myths/sacred sites, crisis response and homes. What it did not yet have was a safe model for what happens when a person or Pokémon is confirmed dead, believed dead, missing for a long period, publicly commemorated, privately remembered, or associated with a burial/memorial site.

This gap matters because Pokémon canon repeatedly treats cemeteries and memorial locations as ordinary parts of the world while also placing Ghost-type Pokémon, folklore, crime, family memory and public ritual around them. Those elements should not be collapsed into one supernatural explanation.

The most important design constraint discovered in this pass is:

`Fainted != dead`

`missing != dead`

`Ghost-type Pokemon != deceased spirit`

`memorial claim != world truth`

`supernatural-looking event != proof of afterlife identity`

Any actual death outcome must come from authored canon or an authoritative PTU/Caelo/AutoPTU resolution path that explicitly establishes death. The narrative generator must not infer it from HP, Fainted state, an Injury, absence, retirement, age, or dramatic context.

## Sources reviewed

### Official Pokémon — Kanto / Pokémon Tower

Source: https://www.pokemon.com/us/pokemon-news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-kanto-region

Pokémon's official Kanto retrospective describes Pokémon Tower as a place containing graves of deceased Pokémon. It also presents the specific Marowak event as a dead parent whose spirit is encountered and eventually calmed.

Reusable high-level structures:
- a memorial/burial institution can be a major explorable location rather than scenery;
- a specific supernatural case can coexist with ordinary Ghost-type encounters in the same place;
- criminal activity can exploit or disturb a memorial site without making the memorial institution itself sinister;
- resolving one restless-spirit case does not establish that every Ghost Pokémon is a dead individual;
- grief, crime, ecology and supernatural uncertainty can overlap in one location.

Do not copy the Marowak/Cubone plot into Ouros.

### Official Pokémon — Hoenn / Mt. Pyre

Source: https://www.pokemon.com/us/pokemon-news/remember-the-region-hoenn-spotlight

The May 29, 2026 Hoenn retrospective describes Mt. Pyre as a place filled with graves where Trainers visit to pay respects. It is also inhabited by Ghost-type Pokémon and becomes relevant to a regional conflict because important objects are protected at its summit.

Reusable high-level structures:
- a memorial site can have several simultaneous functions: burial place, pilgrimage/visitation site, Ghost habitat, stewardship institution and strategic location;
- visitors may come for remembrance while other actors come for research, travel, theft, protection or battle;
- sacred or historically important objects can have custodians without the generator inventing supernatural powers for them;
- a cemetery can remain part of normal regional life rather than being permanently isolated from gameplay.

### Official Pokémon — Lavender Town regional retrospective

Source: https://www.pokemon.com/uk/features/remember-the-region-kanto-spotlight

The 2026 Kanto retrospective again foregrounds Lavender Town and the Pokémon Tower as a persistent cultural landmark associated with Ghost Pokémon and the Marowak incident.

Design lesson: a place can remain regionally famous because of how collective memory, atmosphere, Pokémon ecology and one historical event reinforce each other.

### Pokémon burial-ground overview — discovery reference

Source: https://bulbapedia.bulbagarden.net/wiki/Burial_ground

This community reference indexes burial/memorial examples across several regions, including Pokémon Tower/House of Memories, Memorial Pillar, Mt. Pyre and Lost Tower. It is useful as a discovery map, not as higher authority than official sources or the project's PTU/Caelo corpus.

Reusable high-level structure: memorial practice does not need one universal regional template. Different communities can preserve graves, pillars, towers, houses of memory, summit sites or other forms.

### PTU retrospective — Over There!

Source: https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

The retrospective explicitly describes Pokémon — including Ghost types — as creatures that operate according to their own natural logic inside a believable living world. The campaign also demonstrates that dark themes can exist without every supernatural element needing the same metaphysical explanation.

Important Ouros lesson: Ghost Pokémon should remain ecological entities unless a specific authored rule or event establishes something more. A graveyard containing Ghost Pokémon is not evidence that those Pokémon are the people/Pokémon buried there.

The same retrospective warns indirectly about tone expectations because its campaign was intentionally much darker than a standard badge journey. Ouros should therefore treat death-heavy content as authored/curated rather than casually inserting it into ordinary procedural play.

### Public Pokémon fan work — trainer-loss premise

Source: https://forums.serebii.net/threads/when-a-pokemons-trainer-dies-one-shot.658727/

This public one-shot explores a high-level question useful to Ouros: what happens to a Trainer's Pokémon after the Trainer dies, and who gets to decide? The source is creative work, so no prose, characters, dialogue or plot should be copied.

Reusable design questions only:
- ownership/custody does not automatically answer attachment or residence;
- a deceased Trainer's Pokémon may have their own future state;
- memorial participation can include Pokémon as social actors;
- estate/custody decisions need explicit world rules rather than narrative assumption.

### Game Studies — memorials in persistent online worlds

Source: https://gamestudies.org/1201/articles/gibbs_martin

The paper studies how memorials inside an MMO use world objects, location, text, quests and other game elements to produce remembrance. It supports treating memorialization as something expressed through world state and player practices, not only through exposition.

Reusable design structures:
- memorials can be formal or informal;
- a memorial's meaning emerges from location, repeated visitation, objects and community practice;
- persistent worlds can preserve absence through changed places rather than replacing the missing/deceased actor with exposition.

### Research — death-themed game design

Source: https://research.aalto.fi/en/publications/unraveling-grief-design-space-analysis-of-death-themed-games/

This peer-reviewed work analyzes design questions around games dealing with permanent death and grief. The relevant lesson for Ouros is not to reduce loss to a failure penalty or reward loop.

Reusable principle: mechanically meaningful content around loss should support remembrance, relationship continuity, changed routines, stewardship or unresolved questions instead of requiring the player to "win grief."

### Research — burial and mourning in games

Source: https://research.aalto.fi/en/publications/bittivainajien-pikselikalmistot-hautaamisen-ja-suremisen-rooli-di/

The study separates death, burial/burial sites and mourning as distinct design dimensions. Ouros should use the same separation conceptually:

- mortality outcome is a fact/state;
- disposition/burial is an institutional/material process;
- mourning is a social/personal practice;
- memorialization is public or private representation over time.

### Research — remembrance in Minecraft

Source: https://escholarship.org/uc/item/2mh2c7k5

A 2025 dissertation examines remembrance practices in a private Minecraft community for bereaved youth and describes both formal memorials and informal player-led tributes.

Ouros relevance:
- Minecraft is capable of representing memorial meaning through persistent construction and repeated use;
- not every tribute needs a formal institution;
- player-created memorial spaces need authorship/consent boundaries;
- memorialization can be collaborative and evolve over time.

This research concerns real-world bereavement. Ouros should use only the high-level design insight and must not imitate therapeutic claims or real participants' experiences.

## Structural findings for Ouros

### 1. Mortality needs a truth boundary

The world state needs distinct values for:
- alive/confirmed active;
- missing/whereabouts unknown;
- presumed status claimed by an institution or community;
- mechanically Fainted;
- incapacitated/in recovery;
- retired/out of active story;
- confirmed deceased.

Only the last value authorizes death-specific downstream state.

### 2. Mourning state cannot be inferred from relationship labels

The system may record observable facts such as:
- actor attended a memorial;
- actor placed an item;
- actor visits a grave regularly;
- actor refused to discuss the event;
- actor changed a routine after the event.

It must not autonomously conclude:
- actor is devastated;
- actor has moved on;
- actor feels guilty;
- actor forgave someone;
- actor wants revenge;
- actor considers a memorial spiritually significant.

Those are authored/internal states.

### 3. Ghost ecology and spirit claims must be separate

A site can contain:
- ordinary Ghost-type population records;
- folklore about spirits;
- witness reports of anomalies;
- a confirmed supernatural entity if canon explicitly establishes one;
- completely unrelated Pokémon using the location as habitat.

These fields must not overwrite each other.

### 4. Memorial sites should change over time

Possible persistent changes:
- new names/markers added;
- repaired or weathered structures;
- flowers/offerings/objects accumulated or removed;
- paths become more or less used;
- a caretaker changes;
- a section becomes ecologically important;
- public interpretation changes;
- a memorial is relocated because of erosion or construction;
- old records are corrected;
- a yearly remembrance event changes format.

### 5. Absence can be world state

A character or Pokémon no longer being present can change:
- schedules;
- workplace staffing;
- household composition;
- club rosters;
- rivalries;
- ownership/custody questions;
- public records;
- travel plans;
- ecological relationships;
- responsibilities inherited by institutions.

The system should represent the hole left behind instead of generating a replacement immediately.

### 6. Memorial gameplay should usually be low-pressure

Useful activities include:
- archive research;
- site maintenance;
- escorting an elderly/young visitor only when authored appropriately;
- locating a lost marker;
- resolving conflicting records;
- protecting habitat that developed around an old cemetery;
- returning an object to the correct custodian;
- investigating an anomaly without assuming it is a spirit;
- preparing a commemoration;
- documenting an endangered memorial landscape.

Combat can occur, but it should not be the default expression of grief.

## PTU/Caelo boundary notes

The supplied project corpus already treats Fainted, Injuries, healing/recovery and combat lifecycle as mechanical concepts. Narrative mortality must not reinterpret them.

The current Python AutoPTU contains explicit logic where False Strike can leave a fainted wild target at 1 HP and where Injuries trigger their own Feature interactions. This is further evidence that `fainted`, `HP`, and `injury` are mechanical states with specific rules rather than synonyms for death.

Exact PTU/Caelo death thresholds, lethal-damage procedures, capture/ownership consequences after Trainer death, Ghost-specific Features, Spirit Medium/Aura interactions and any Caelo homebrew concerning mortality still require dedicated source extraction before Ouros implements them.

## Copyright / transformation notes

Do not copy:
- Marowak/Cubone's distinctive tragedy;
- Mt. Pyre's stolen-orb plot;
- fanfiction characters or dialogue;
- named funerary customs from real communities;
- real bereaved players' memorial practices as fictional set dressing.

Reusable material is limited to abstract structures: memorial institutions, layered truth, custody questions, evolving burial sites, ecological overlap, collective remembrance and consent-aware legacy.

## Research gaps for later runs

- Extract the exact PTU 1.05 and Caelo rules that can establish death rather than Fainted/Injury state.
- Determine whether Caelo has explicit policies for PC/Pokémon death in its living-world format.
- Research Ghost-related PTU classes/Features separately from general Ghost Pokémon ecology.
- Decide whether Ouros launch canon permits permanent Trainer death, permanent Pokémon death, both, or neither during normal generated play.
- Define estate/custody rules only after Ouros ownership institutions exist.
- Determine how memorial sites and player-created tributes persist in multiplayer Minecraft without griefing or unauthorized edits.
