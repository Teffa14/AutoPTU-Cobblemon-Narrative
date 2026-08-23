# Memorials, Remembrance & Legacy Continuity — Research Scan 129

Status: research/provenance only. Not Ouros canon. No mechanics are authorized by this document.

## Why this scan exists

The repository already has strong authorities for Public Memory, Archives, Museums, Sacred Sites, Families, Identity, Material Culture, Pokémon Agency and recurring Observances. What it does not yet own explicitly is the persistent state between an acknowledged loss/absence/retirement and the ways a community keeps, revises, relocates or stops maintaining a memorial over time.

This scan therefore focuses on memorialization as world continuity rather than on grief simulation. It also establishes a strict rules boundary: PTU battle states such as Fainted or Injury must never be promoted into narrative death without explicit authored evidence.

## Source set and reusable lessons

### 1. Pokémon Tower / Lavender Town — memorial site can change function without erasing remembrance

Source: Bulbapedia, Pokémon Tower — https://bulbapedia.bulbagarden.net/wiki/Lavender_Tower

The Pokémon Tower is established as a burial and remembrance site. Later generations convert the tower to another civic use while the graves are moved to the House of Memories/Soul House.

Reusable structure:

- a memorial institution can move while the remembered subjects remain continuous;
- adaptive reuse does not need to erase commemorative history;
- a former memorial building can retain public memory after its formal function changes;
- relocation should produce a new site/location revision, not delete the old one;
- Ghost-type presence at a memorial site is a separate world fact, not a universal consequence of burial or remembrance.

Ouros transformation: a station, tower, old Gym, hospital wing or bridge can cease to be the physical memorial location while the memorial records, objects and recurring observances move elsewhere.

### 2. Mt. Pyre — remembrance can coexist with ordinary travel and battle spaces

Source: Serebii Pokéarth, Mt. Pyre — https://www.serebii.net/pokearth/hoenn/mt.pyre.shtml

Mt. Pyre combines graves, visitors who come to grieve, ordinary traversal, wild Pokémon and Trainers. The reusable lesson is not its specific plot or protected artifacts. It is that a memorial landscape can remain part of normal regional geography rather than becoming a sealed one-use cutscene.

Ouros transformation:

- a memorial path can remain a working trail;
- visitors, caretakers, researchers and wild Pokémon can occupy the same broad place for different reasons;
- battle may occur near a memorial without the memorial itself becoming a combat mechanic;
- memorial access, sacred access and ordinary travel access can be distinct permissions.

### 3. Lost Tower — a memorial can preserve an individual incident without becoming the whole identity of a region

Source: Bulbapedia, Lost Tower — https://bulbapedia.bulbagarden.net/wiki/Lost_Tower

The Lost Tower is a resting place for deceased Pokémon. It also contains individual mourners whose personal losses connect the location to wider events.

Reusable structure:

- public sites can contain private or small-scale remembrance;
- one marker can preserve a specific historical incident without requiring a region-wide quest;
- the same site can support anonymous, named and disputed records;
- absence of a quest does not make the memorial narratively inert.

### 4. Celestial Tower — remembrance, care and research can share one institution without becoming one system

Source: Bulbapedia, Celestial Tower — https://bulbapedia.bulbagarden.net/wiki/Tower_of_Heaven

Celestial Tower is a resting place and remembrance site. Separate stories also use it for care of a fainted Pokémon and for research into changing Pokémon distribution.

This is a particularly useful rules guardrail. A fainted living Pokémon and a deceased Pokémon can be present in the same location for entirely different reasons. The setting itself does not collapse those states.

Reusable structure:

- `FAINTED` must remain distinct from `DECEASED`;
- a remembrance site can also host care or research without those functions becoming memorial mechanics;
- a bell, marker or ritual action can carry symbolic meaning without automatically producing a supernatural or PTU effect;
- later visitors can attach new meanings to the same place while earlier uses remain historically true.

### 5. PTU Hex Maniac — tomb caretaking can be a practical role, but class mechanics do not come free

Source: PTU community reference, Hex Maniac — https://pturpg.wikidot.com/hex-maniac

The public PTU reference describes caretakers of Pokémon tombs as one plausible background for Hex Maniac expertise and frames grave robbers or dangerous Ghost-types as practical reasons for such training.

Reusable structure:

- memorial caretaking can be an occupation or institutional role;
- caretaking can produce repeated local knowledge and practical responsibilities;
- a caretaker does not automatically possess Hex Maniac Features, Occult Education ranks or combat authority;
- a memorial location does not automatically generate Ghost-type threats.

This source is a PTU reference, not proof that the current Java port executes those Features.

### 6. Persistent game memorials — place, mechanics and memory can reinforce one another

Source: Gibbs, Mori, Arnold & Kohn, “Tombstones, Uncanny Monuments and Epic Quests: Memorials in World of Warcraft,” Game Studies 12(1), 2012 — https://gamestudies.org/1201/articles/gibbs_martin

The paper documents memorials embedded inside a persistent game world and examines how developers use environmental objects and game-world context to support remembrance.

Reusable structure for Ouros:

- remembrance can be expressed by ordinary world objects, routes and spatial practices rather than exposition dumps;
- a memorial gains meaning through accumulated context, not through a mandatory buff or quest marker;
- player familiarity with a place can make later revisions meaningful;
- environmental storytelling works best when the world preserves earlier states or records rather than silently retconning them.

### 7. Virtual memorials are vulnerable to platform change

Source: Thomas Montefiore, “Unstable preservation: memorials in virtual environments,” Phenomenology and the Cognitive Sciences, 2025 — https://link.springer.com/article/10.1007/s11097-025-10091-6

The paper argues that virtual memorials face preservation problems because digital environments can change, disappear or alter the context that gives a memorial meaning.

Reusable structure for a Minecraft-backed Ouros:

- a memorial's world-state identity cannot depend only on loaded blocks;
- relocation, rebuild, server migration or asset replacement should preserve revision history;
- digital memorial records need durable IDs and archival provenance;
- deleting or rebuilding a Minecraft structure must not erase Chronicle history;
- preserving a screenshot alone may be insufficient if the surrounding context changed.

### 8. Digital memorialization can preserve continuity but also creates privacy/representation risks

Source: Fu et al., “Grieving in virtual worlds: emotional processes and generational differences in avatar-based memorials on VRChat,” Frontiers in Psychology 16, published 10 December 2025 — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1669020/full

This work is used only for a system-design caution: virtual remembrance can be meaningful, but participants differ in how they interpret rituals and digital identity.

Ouros design consequence:

- attendance cannot be used to infer private grief, belief, kinship or emotional state;
- a multiplayer memorial should not expose private correspondence, medical history or identity data by default;
- a digital memorial page is a versioned publication, not an omniscient representation of the subject;
- players must retain control over private character beliefs and feelings.

## Cross-source design lessons

### Memorial identity should outlive location

Use a stable memorial ID and version the site, marker, inscription and custodian separately. A bridge can be rebuilt; a plaque can move; a tower can change use; the same commemorative record can continue.

### A memorial is not proof of the event it describes

An inscription is evidence of what someone chose to record. It can be sincere, incomplete, politically contested, translated imperfectly or corrected later. The underlying incident remains under Cases, Archives, Public Memory or other evidence-owning layers.

### Missing is not deceased

A missing Trainer, expedition member or Pokémon can receive a marker of absence without being declared dead. If later evidence changes the status, the memorial receives a revision; the old version remains part of history.

### Commemoration is broader than death

Ouros can commemorate:

- retirement;
- closure of a workplace or institution;
- a successful evacuation;
- a lost route or settlement phase;
- local extirpation of a population;
- a disaster and subsequent rebuilding;
- a living Pokémon or Trainer's long service;
- a vanished expedition whose outcome remains unknown.

This avoids forcing death into the world merely to justify memorial content.

### Public memory is not private emotion

Public Memory owns the evolving social narrative around an event. This proposed layer owns the persistent memorial object/site/practice and its revision history. Neither system may infer what a PC privately feels.

### Sacredness is optional and separate

A memorial can be sacred, civic, familial, institutional, artistic, digital, ecological or purely practical. Sacred Sites owns sacred recognition and religious/spiritual practice where authored. Memorial status alone does not create sacredness.

### Pokémon agency survives memorialization

A living retired, missing, released or former partner can be commemorated without becoming property or losing agency. A memorial to a deceased Pokémon does not transfer ownership or Command authority to another actor. A Pokémon visiting a memorial is an observation, not proof of grief, supernatural perception or kinship unless canon explicitly says so.

## PTU/Caelo mechanical guardrails

This pass must preserve these boundaries:

- `Fainted` is a battle state, not a death declaration.
- Injury history is not death semantics.
- HP reaching a threshold must not be interpreted as death unless the authoritative PTU/Caelo project rules explicitly define that outcome for the relevant context.
- Ghost-type presence does not prove a dead subject's spirit is present.
- Hex Maniac lore does not grant Features to memorial caretakers.
- bells, incense, flowers, songs, candles, masks, offerings or memorial objects do not create buffs, healing, Status effects, Weather, Terrain or Legendary encounters.
- a memorial object has no automatic Item effect.
- remembrance cannot change Loyalty, Command, Friendship or capture eligibility.

The complete primary Caelo corpus was not reliably exposed in this runtime. No Caelo-specific death, burial, inheritance, Ghost or memorial mechanic is asserted here.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output is attributed to it.

## Novel Ouros directions unlocked

The strongest new direction is not “cemeteries as spooky dungeons.” It is memorial continuity as a cross-system history layer:

- an old bridge marker can conflict with later archival evidence;
- a missing-expedition memorial can be revised when one member returns;
- a public plaque can move during accessibility work without losing identity;
- a retired service Pokémon can be honored while still living independently;
- a memorial grove can later conflict with conservation or land-use priorities;
- a digital remembrance page can survive redevelopment of the physical venue;
- a former memorial site can become a café, station or clinic while a smaller remembrance space moves nearby;
- a memorial may simply be maintained for decades with no quest attached.

## Research provenance policy

All structures above are abstractions from public sources. Do not copy source prose, dialogue, named plots, distinctive character arcs, ritual text, sacred practices or memorial inscriptions into Ouros. Any future canon material must be original and should continue to distinguish source attribution from authored Ouros lore.