# Museums, Collections, Exhibitions & Conservation Research — Pass 128

Status: RESEARCH / PROVENANCE ONLY. Not canon. External stories and museum standards are inspiration sources, not PTU/Caelo rules sources.

## Why this pass

The repository already has strong ownership over adjacent domains:

- Material Culture owns persistent object identity, provenance and physical transformation.
- Myth/Archaeology owns archaeological sites, observations and historical interpretations.
- Archives/Public Memory own records, claims and public remembrance.
- Photography owns visual records and derivative copies.
- Supply Chains/Postal/Transport own physical movement.
- Institutional Review owns bounded review decisions.

The missing layer is institutional collections stewardship: accession, cataloguing, location history, conservation, loans, travelling exhibitions, display decisions, deaccession/disposition, label revisions and the distinction between an object physically held by a museum and the public story currently told about it.

## Source scan

### 1. Pokémon Fossil Museum — travelling exhibition and comparative interpretation

Official Pokémon sources:
- https://www.pokemon.com/us/pokemon-news/dig-into-the-pokemon-fossil-museum-exhibition-at-chicagos-field-museum
- https://www.pokemon.com/us/pokemon-news/pokemon-fossil-museum-to-debut-in-north-america-at-chicagos-field-museum

Observed structures:
- the exhibition travels between host institutions;
- objects/models/casts can be displayed together without becoming one collection;
- an exhibit has a curatorial thesis separate from the identity of the individual object;
- comparison is part of the visitor experience rather than a declaration that two objects are equivalent;
- exhibition design can combine specimens, models, illustrations, tools, sound and interpretation;
- a temporary show can build public interest while the underlying collections remain persistent.

Reusable Ouros lesson:

A travelling exhibit should be a versioned project with its own object list, label set, host schedule and handling history. It must not duplicate objects when the show moves. Host custody, ownership and collection membership remain separate.

### 2. Pewter Museum of Science — research, excavation and public museum in one institution

Official sources:
- https://pokemonletsgo.pokemon.com/en-us/kanto-region/
- https://www.pokemon.com/us/animation/seasons/23/episode-38-restore-and-renew

Observed structures:
- fossils are publicly displayed;
- museum staff can also conduct excavation/research;
- field discoveries can enter an institutional workflow;
- a museum can contain specialized equipment without the equipment defining the collection itself;
- a recovered fossil or artifact can be scientifically important before any display decision exists.

Reusable Ouros lesson:

Discovery -> field custody -> preparation/research -> accession review -> collection storage -> possible exhibit is a useful chain. Each stage can be delayed or rejected independently.

Guardrail:

Fossil restoration is a governed Pokémon-world capability. Do not infer that every museum can revive fossils or that every fossil object is eligible for revival.

### 3. Oreburgh Museum — collection object, restoration machine and live Pokémon are different states

Official source:
- https://www.pokemon.com/us/animation/seasons/10/episode-18-oer-the-rampardos-we-watched

Observed structures:
- a fossil and a restoration machine can both be museum assets but have different operational roles;
- theft of a machine and fossil creates separate custody problems;
- restored Pokémon become living actors, not museum objects;
- a museum incident can spill into city-scale consequences.

Reusable Ouros lesson:

Never let `collection_object` survive unchanged after a process that produces a living Pokémon. The original fossil/object history remains in Material Culture, while the living Pokémon must receive persistent Pokémon identity and agency under Pokémon Agency.

### 4. Slateport Sea Museum — a museum can hold newly recovered scientific material before interpretation is settled

Official source:
- https://www.pokemon.com/us/animation/seasons/6/episode-36-the-spheal-of-approval

Observed structures:
- a curator presents a newly recovered volcanic rock from the seafloor;
- cultural stories and scientific interpretation can coexist around the same object;
- a museum can be closed to the public while staff continue work;
- theft can occur during active research rather than only from a polished gallery.

Reusable Ouros lesson:

Public access state and collections/research state must be independent. `MUSEUM_CLOSED` does not mean no staff, no custody or no work is occurring.

### 5. Eterna Historical Museum — provenance/custody incident and false identification

Official source:
- https://www.pokemon.com/us/animation/seasons/10/episode-36-a-secret-sphere-of-influence

Observed structures:
- a specific museum object can be the center of a custody investigation;
- security evidence can be real but misleading;
- resemblance between actors can produce false attribution;
- recovery of the object does not erase the incorrect accusation from history.

Reusable Ouros lesson:

Museum security incidents should use Case/Authority/Custody. The collection system records object status and location history; it should not decide guilt.

### 6. Exceed museum — museum as public front plus deeper institutional archive/infrastructure

Official source:
- https://www.pokemon.com/us/animation/horizons/3/dot-and-pennys-top-secret-mission

Observed structure:
- a museum can coexist with server rooms, corporate records and research holdings;
- public galleries reveal only one subset of institutional knowledge.

Reusable Ouros lesson:

`on_display` is not equivalent to `institution_knows`. Gallery access is not archive/server/research access.

### 7. Pokémon Fossil Museum exhibition fact sheet — why museums collect and how exhibits can expose method

Public Field Museum fact sheet surfaced through official exhibition materials:
- https://www.datocms-assets.com/44232/1746203660-pokemon-fact-sheet-web-2025-05-01.pdf

Observed structures:
- exhibition can teach excavation, cleaning, identification and scientific comparison;
- casts and original specimens have different material status while both can support interpretation;
- exhibition can explicitly explain why collections exist beyond display.

Reusable Ouros lesson:

A museum collection should support research, comparison, preservation and future reinterpretation even when most objects are never on display.

### 8. PTU community encounter — museum boss complication as a capability warning

Public discussion:
- https://www.reddit.com/r/PokemonTabletop/comments/q5kvm1

Observed high-level structure:
- a natural-history museum encounter uses hanging displays, glass cases and exhibits as proposed tactical complications;
- community ideas quickly turn scenery into moving hazards, improvised weapons or effect zones.

Reusable Ouros lesson:

Museums are excellent encounter spaces because they have meaningful geometry and objects. However, the intended full encounter can require forced movement, interactables, hazards, reactions and tactical AI. The Minecraft adapter must not invent those effects because a display visually exists.

Do not import the thread's exact hazards, stats or boss scenario.

### 9. PTU community fossil campaign — collection pressure can shape regional institutions

Public discussion:
- https://www.reddit.com/r/PokemonTabletop/comments/fh59h2

Observed high-level structure:
- fossils can become culturally central to a region;
- dig sites, research, resale, illicit acquisition and restoration technology can form linked institutions;
- the same material can carry scientific, economic and political value.

Reusable Ouros lesson:

Collections can become part of regional identity and contested stewardship without every valuable object becoming loot.

Do not import the homebrew legendary, antagonist, plot or mechanical changes.

## Museum collections-management references

These are architecture references only. Their legal/ethical requirements are not automatically Ouros law.

### 10. Collections Trust / SPECTRUM — cataloguing and location history

Source:
- https://collectionstrust.org.uk/wp-content/uploads/2016/11/Cataloguing_SPECTRUM_4_04_ForDownloadVersionforCLuser-9.pdf

Useful abstractions:
- an object requires enough description to distinguish it from similar objects;
- cataloguing can cross-reference acquisition, conservation, exhibition, loan and location history;
- documentation should preserve an object's historical archive rather than only current state.

Reusable Ouros lesson:

Collection records should point to existing provenance/custody/conservation records instead of duplicating every fact into a single omniscient museum row.

### 11. ICOM accessioning standards — acquisition decision is separate from possession

Source:
- https://icom.museum/wp-content/uploads/2022/02/Accessioning-Standards_EN.pdf

Useful abstractions:
- institutions should consider provenance and ability to care for an object before accession;
- long-term preservation/storage capacity can matter to acquisition decisions;
- accepting physical custody is not identical to permanently adding something to a collection.

Reusable Ouros lesson:

Use `TEMPORARY_CUSTODY`, `PENDING_ACCESSION`, `ACCESSIONED`, `DECLINED`, `RETURN_PENDING` and related states rather than turning every donated/found object into museum property immediately.

No real-world cultural-property law, human-remains policy or national legal framework is imported into Ouros by default.

## Cross-layer conclusions

### Collection membership versus custody

An institution can physically hold an object without owning it or accessioning it. Examples include incoming loans, conservation work, evidence held under a Case, deposits pending review and temporary research custody.

### Collection membership versus display

Most holdings do not need to be visible to players. Storage can still produce research, conservation, loan and future-exhibition content.

### Object versus interpretation

An object remains the same persistent object while labels and interpretations change. Exhibit text belongs to Archives/Language/Public Memory and should be versioned.

### Original versus cast/replica

A cast, replica or reconstruction must receive its own `item_instance_id` and relationship to the source object. A replica can become historically important in its own right.

### Living Pokémon boundary

Pokémon are actors. A museum may preserve records, fossils, photographs, casts, shed material or historical objects related to Pokémon. A living Pokémon is not a `collection_object` simply because the institution houses, studies or publicly presents it.

### Exhibition versus research

A scientifically useful object can remain off display. A display object can support public interpretation without being suitable for destructive research. Exhibit scheduling cannot silently authorize sampling.

### Conservation versus restoration

Conservation records changes made to stabilize/preserve an object. Restoration may alter presentation. Neither process rewrites earlier condition observations or guarantees historical authenticity.

### Loan versus transfer

Outgoing loan changes custody/location for a bounded period. It does not automatically transfer ownership or collection membership.

## Candidate implementation concepts

Potential world-state entities:
- `MUSEUM_OR_COLLECTION_INSTITUTION`
- `COLLECTION_OBJECT_LINK`
- `ACCESSION_CASE`
- `CATALOG_RECORD`
- `OBJECT_LOCATION_EVENT`
- `CONDITION_REPORT`
- `CONSERVATION_TREATMENT`
- `EXHIBITION_PROJECT`
- `EXHIBITION_OBJECT_ASSIGNMENT`
- `EXHIBIT_LABEL_REVISION`
- `LOAN_AGREEMENT_STATE`
- `LOAN_HANDOFF`
- `DEACCESSION_REVIEW`
- `DISPOSITION_EVENT`
- `REPLICA_OR_CAST_RELATIONSHIP`
- `COLLECTION_RESEARCH_ACCESS`

These are orchestration/world-state records. They do not create PTU effects.

## Encounter-design implications

Mechanically rich museum scenes commonly tempt the narrative layer to invent unsupported behavior:
- falling/swinging exhibits;
- shattered cases as hazards;
- moving crowds;
- protected display corridors;
- objectives that require carrying fragile objects;
- live Pokémon retreating through galleries;
- display cases granting cover;
- environmental effects from minerals, fossils or artifacts;
- object damage changing battle state.

Full versions of such scenes may depend on:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback;
- exact item/move/ability behavior if an exhibit has a genuine PTU effect.

Reduced versions should evacuate civilians, secure/relocate fragile objects in world state where appropriate, freeze a safe static arena, and let AutoPTU resolve only the actual combatants.

## PTU/Caelo validation boundary

No primary Caelo corpus was reliably exposed in this runtime. Super PTU Online Helper was not exposed as an invocable capability.

Therefore this pass does not invent:
- fossil-restoration legality;
- Fossil Researcher effects;
- artifact bonuses;
- appraisal DCs;
- collection-value formulas;
- object HP;
- improvised-weapon stats;
- falling-display damage;
- glass hazards;
- museum terrain;
- research sampling mechanics;
- restoration effects on living Pokémon.

Exact PTU mechanics remain governed by the project's primary PTU/Caelo corpus and current AutoPTU implementation.

## Originality note

The resulting Ouros proposals must use only high-level structures from these sources. Do not copy named museums, characters, exhibit scripts, theft plots, fossil lists, dialogue, homebrew artifacts or encounter gimmicks wholesale.
