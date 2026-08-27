# Libraries, Publications, Editions & Circulation Research — Pass 65

Status: research/provenance only. Nothing in this file is established Ouros canon.
Date inspected: 2026-08-26

## Scope and repository-fit check

The complete repository tree was enumerated before this pass. Relevant existing layers were read directly, especially `design/archives-museums-collections-preservation-layer.md`, `design/media-communications-information-layer.md`, `design/language-translation-symbolic-systems-layer.md`, `design/public-memory-event-legacy-layer.md`, `design/education-academies-field-practice-layer.md`, `design/material-culture-economy-crafting-layer.md`, and the newest engine snapshot.

The existing archive layer already owns deliberate preservation, accession, collection custody, catalog records, reading rooms, exhibit interpretation and conservation. The media layer already owns information packets, publication events and communications channels. The language layer already owns source/transcription/translation/interpretation separation.

The remaining gap is narrower: a work can exist as several editions and many physical/digital copies, move through lending or sale, receive annotations, be corrected without erasing older copies, become temporarily unavailable even while other copies survive, and acquire public significance that differs from its factual accuracy. Pass 65 therefore adds publication-and-circulation continuity rather than another archive or media system.

## New sources inspected

### Canalave Library — public reference material can launch field research and later receive new contributions

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Canalave_Library
- https://bulbapedia.bulbagarden.net/wiki/Canalave_City

Observed high-level structure:
- a public library contains regional myths and philosophical/historical material that can be read directly;
- the same building functions as a meeting point where researchers assign field investigation based on existing knowledge;
- later game state can make additional written material available;
- a contributor can explicitly identify their own theory/contribution rather than the text becoming anonymous truth.

Reusable Ouros lesson:

A library should support a loop of read -> form a question -> investigate elsewhere -> return with evidence -> revise or add a work. New information does not need to overwrite the old shelf. Older texts can remain historically important even after better evidence appears.

Do not copy Sinnoh myths, Arceus cosmology, Rowan, Cynthia, the lake assignment or specific texts.

### Malie Library — access depends on people, old texts and ordinary collection accidents

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Malie_City
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Sun_and_Moon/Part_14
- https://www.thonky.com/pokemon-ultra-sun-ultra-moon/malie-city

Observed high-level structure:
- a character seeks a specific old book because it contains information not otherwise immediately available;
- another knowledgeable person helps locate or interpret the material;
- the library also contains ordinary public readers and unrelated books;
- an old photograph can fall from a shelf and create a small provenance/return-to-owner problem independent of the main plot.

Reusable Ouros lesson:

Libraries can generate low-stakes and high-stakes stories from the same persistent place. A rare reference request, an unidentified insert, a returned photograph, a missing copy and an expert referral can coexist without turning every shelf into a dungeon.

Do not copy Alola's legendary history, named characters or the specific photograph quest.

### Naranja/Uva Academy libraries — one expedition work can coexist with rules, registries and instructional texts

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Naranja_Academy
- https://bulbapedia.bulbagarden.net/wiki/Uva_Academy

Observed high-level structure:
- the academy library/study area contains institutional regulations, student records, instructional references and a famous expedition-derived volume in the same space;
- the expedition work is associated with a named author and an institutionally funded research history;
- the work records mysteries and observations rather than eliminating uncertainty merely because it was printed;
- access to a text can therefore communicate institutional history, research provenance and current policy simultaneously.

Reusable Ouros lesson:

Treat publications as authored claims with provenance. A prestigious book can shape expeditions, public expectations and institutional memory while still containing uncertainty, interpretation or incomplete conclusions.

Do not copy Area Zero, Herba Mystica, the Scarlet/Violet Books, Heath or academy-specific lore.

### Pokémon Insurgence — a library can be a civic identity and a layered exploration space

Sources:
- https://wiki.p-insurgence.com/Utira_Library
- https://wiki.p-insurgence.com/Utira_Town
- https://wiki.p-insurgence.com/Books

Observed high-level structure:
- a large library is central enough to knowledge that the surrounding settlement identifies with it;
- different wings have different access/use states, including an abandoned area;
- ordinary reference books can answer practical local questions;
- a note attached to a book can redirect the reader toward another actor or unresolved thread;
- written lore distributed through the location can deepen the region without requiring every text to be a quest key.

Reusable Ouros lesson:

A library may have spatial state: public wing, staff area, closed stacks, repair zone, overflow storage or temporarily inaccessible section. A copy can also carry an insert, annotation or provenance clue distinct from the published work itself.

This is fangame inspiration only. Do not copy Utira, cult prophecy, characters, book titles, secret-wing geometry or plot beats.

### PTU community design — books can be plot hooks, but reward mechanics must stay authoritative

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/ptu-books-and-book-like-things-t3257.html

Observed high-level structure:
- PTU community discussion treats books/knowledge as possible rewards and plot hooks;
- the discussion explicitly separates valuable knowledge/training rewards from ordinary shop inventory;
- some proposals in the thread are mechanical/homebrew rather than governing PTU rules.

Reusable Ouros lesson:

Knowledge objects can motivate exploration and professional growth, but narrative availability must not silently grant a Skill, Edge, Feature, Tutor Move, AP benefit or other rule effect. If a publication is intended to have a mechanical PTU effect, that effect must be validated against the project's PTU/Caelo source set and current AutoPTU implementation.

This thread is inspiration, not a rules source.

### PTU campaign structure guidance — recurring personal interests should coexist with larger plots

Source:
- https://pokemontabletop.fandom.com/wiki/Campaign_Structure

Observed high-level structure:
- PTU campaign guidance encourages alternating space for personal interests with larger plot pressure;
- organization-based campaigns can sustain mission structures beyond a simple Gym crawl;
- player-directed interests remain meaningful even when a central plot exists.

Reusable Ouros lesson:

Libraries and publications should support optional professional/personal arcs: translation, research, local history, catalog work, authorship, collecting or correcting a reference. These loops should not become mandatory exposition checkpoints for every player.

The wiki is secondary/reference material; supplied project sourcebooks remain authoritative for mechanics.

## New synthesis: the work, edition and copy are different objects

A durable publication model needs at least three layers.

```text
authored work / claim set
        |
        +--> edition A ----> copy A-001 ----> loan history / annotation
        |        |
        |        +----------> copy A-002 ----> lost / later recovered
        |
        +--> edition B ----> correction notes / changed framing
                 |
                 +----------> copy B-001 ----> current public shelf
```

If Edition B corrects a date, Edition A does not disappear from history. A character who read A months ago may still remember the old claim. A scholar can cite A because it documents what people believed at that time. A marginal note in copy A-002 belongs to that copy, not to the authored work.

## Publication continuity principles

### Publication does not establish truth

A printed statement remains a claim. Prestige, rarity, age, named authorship or institutional sponsorship can change how actors treat it, but none of those properties convert it into canonical fact.

### Revision must preserve provenance

Useful revision relations include:
- REVISED_EDITION
- EXPANDED_EDITION
- ABRIDGED_EDITION
- TRANSLATED_EDITION
- FACSIMILE
- ERRATA_SHEET
- RETRACTION_OR_WITHDRAWAL_NOTICE
- ANNOTATED_COPY

These labels are descriptive until implementation/canon review.

### A copy can have a life separate from its text

A copy may be:
- on shelf;
- checked out;
- reserved;
- missing;
- in repair;
- in staff processing;
- transferred;
- sold;
- donated;
- found with an insert;
- personally annotated;
- damaged while the underlying work remains available elsewhere.

Custody and ownership remain separate.

### Access is local and temporal

A work may be publicly known while a specific copy is unavailable. A reading room may require staff handling without implying secrecy. A closed wing may be a maintenance state rather than conspiracy. A restricted item needs an authored access policy; the generator may not invent censorship, police authority or legal prohibition.

### Marginalia is evidence about a reader, not an automatic correction

An annotation can record:
- a question;
- disagreement;
- a cross-reference;
- an observation;
- a date;
- ownership/custody marks;
- later editorial comment.

It does not become true because it is handwritten, old or hidden.

## Reusable story structures

### Read -> investigate -> revise

A current reference contains a gap or claim. Players follow the lead into the world, collect evidence, and later decide whether the outcome supports a correction, appendix, new work, catalog note or unresolved dispute.

### Two editions, one disagreement

Two actors quote the same title but different editions. Their apparent contradiction is resolved by edition history rather than by declaring one actor dishonest.

### The missing copy matters because of its copy-specific history

The published text exists elsewhere, so theft of "secret knowledge" is not the premise. The missing copy matters because it contains provenance marks, annotations, an inserted photograph, a loan history or evidence of who handled it.

### A library changes slowly

After a public event, expedition, restoration or controversy, future visits can show:
- a new reference shelf;
- an errata slip;
- a display copy moved to secure handling;
- an old edition returned to open stacks;
- a waiting list;
- a repaired wing;
- a librarian now able to point toward an older record.

This creates visible world memory without inventing another settlement.

## Mechanical boundary

External stories do not define PTU mechanics.

Reading a work, finding an annotation, borrowing a copy, writing a correction or publishing an edition does not automatically grant:
- Skills or Skill Ranks;
- Edges;
- Features;
- Chronicler effects;
- Researcher effects;
- Tutor Moves;
- Move access;
- Ability changes;
- item effects;
- AP or XP;
- combat bonuses;
- Legendary knowledge as objective truth.

The newest inspected AutoPTU-Java commit is `c5ef1d72c8a997144d215423e2aab60d706905a9` (Port Chronicler Accuracy bonus resolution #226). That is a parity-backed slice of one Trainer Feature/Accuracy interaction. The current Java README still leaves full battle state, damage pipeline, status controller, terrain, hazards, forced movement, reactions, complete hook registries, AI scoring/policy and Craftics/Cobblemon adapter unfinished.

The newest inspected AutoPTU commit is `2976b6047702d2e86d367fdad3d648e35ced4145` (Career: reject coerced recovery decision progress #164). That is persistence validation in the Career UI/runtime and does not add a tactical family.

No capability category is promoted by Pass 65.

## Copyright/transformation boundary

Use only high-level structures: persistent library space, edition drift, provenance, annotations, distributed reading, institutional research, old-copy recovery and public correction.

Do not reproduce protected prose, myths, book text, dialogue, named characters, distinctive puzzles, secret-wing layouts or fangame plots.

## Canon questions deliberately left open

- Which Ouros settlements have libraries, reading rooms or circulating collections?
- Which institutions publish research, manuals, newspapers, field guides or public records?
- What technologies of printing/copying/digital publication exist by region?
- What makes an edition authoritative inside any institution?
- Are lending cards, deposits, membership or other access systems used anywhere?
- Who can authorize restricted access, and for what reasons?
- What correction/retraction conventions exist?
- Which works are already established canon and which remain proposed?
- Which historical traditions are oral rather than written?
- How much copy-level state should Minecraft materialize before shelves become cluttered?

Pass 65 does not answer these by convenience.