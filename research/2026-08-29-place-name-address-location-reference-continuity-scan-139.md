# Ouros Narrative Research — Place Names, Addresses & Location References — Pass 139

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-29

## Scope

This pass examines how a persistent world should preserve the identity of places when names, aliases, street labels, entrances, address descriptions, map editions and institutional records change at different times.

The goal is not to create a universal Ouros addressing authority. The goal is to give existing systems a stable way to refer to the same physical place across history without collapsing name, geometry, access, ownership, routing and public display into one fact.

The full recursive narrative repository tree was inspected before topic selection. Existing Cartography, Public Notices, Courier, Land Parcels, Human Identity, Residential, Public Memory, Travel, Roads, Dispatch and Archives material was checked so this pass stays connective rather than duplicative.

## Existing Ouros boundaries

Cartography already separates authoritative geography from map claims. A map can have a stale label without moving the represented feature.

Public Notices and Signage already separate a physical sign from the state it displays.

Courier already supports `ADDRESS_INCOMPLETE`, recipient relocation and redirect logic, but does not own the identity or history of a destination reference.

Land Parcels already states `ADDRESS_MATCH != LAND_UNIT_IDENTITY` and separates boundaries, residence, ownership and access.

Human Identity already demonstrates the useful pattern that a persistent internal identity can survive changing public names while disclosure remains scoped.

The missing connective layer is place-reference continuity itself.

## Public Pokémon research

### Lumiose City — later naming of already-existing urban geometry

Source:
https://bulbapedia.bulbagarden.net/wiki/Lumiose_City

Bulbapedia documents streets in Pokémon Legends: Z-A that occupy thoroughfares already present in Pokémon X and Y, while some of those thoroughfares were not individually named in the earlier presentation. It also distinguishes plazas, streets, boulevards, avenues and places of interest.

Reusable lesson:

A physical feature can predate the label later used for it. Naming should therefore be an event or record attached to persistent geography, not the birth of the geography itself.

Ouros transformation:

- `PLACE_EXISTS != PLACE_HAS_CURRENT_NAME`;
- a newly standardized name can point to an older feature;
- historical events may legitimately use older unnamed, descriptive or local references;
- later indexing can connect those references without rewriting the event text.

No Lumiose names, layouts, characters or story events are imported into Ouros.

### Castelia City — multiple reference scales inside one settlement

Source:
https://bulbapedia.bulbagarden.net/wiki/Castelia_City

Castelia provides a useful structural example of a large city whose navigation uses named streets, a central plaza, piers, alleys, gates and landmarks. A person can therefore identify the same destination through several nested or adjacent references: city, street, pier, landmark or nearby building.

Reusable lesson:

Location references are composable and purpose-specific. A courier may need an entrance or delivery point. A traveler may only need a district or landmark. An archive may preserve a historical street name. Those references can all resolve to the same persistent place while differing in precision.

Ouros transformation:

Represent location references with scope, type, effective dates and provenance instead of one global display string.

No Castelia locations are copied into Ouros.

## Public operational research

### UNGEGN — standardized and locally used geographical names

Sources:
https://unstats.un.org/unsd/ungegn/about/
https://unstats.un.org/unsd/ungegn/nna/

UNGEGN describes geographical-name standardization as useful for communication, navigation, mapping, data integration and public-service delivery, while also encouraging recording and use of locally used names that reflect language, culture and tradition.

Reusable architecture:

- a standardized name and a locally used name can coexist;
- standardization is an authored institutional process, not a property inherent in geometry;
- names need provenance and responsible authority where an authority exists;
- multilingual or culturally specific forms should not be silently collapsed.

Ouros limitation:

This does not establish a national names authority, official-language regime or naming law anywhere in Ouros. Those remain canon questions.

### USGS GNIS — feature identity, official name, variants and historical names

Sources:
https://www.usgs.gov/us-board-on-geographic-names/what-geographic-names-information-system-gnis
https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data

GNIS separates a feature record from its official name and from variant names. Variants can be historical, unofficial or alternate spellings. Historical information can persist even when a feature no longer exists or no longer serves its original function.

Reusable architecture:

- persistent feature identity can outlive a name;
- one place may have multiple documented variants;
- a historical name remains evidence even when no longer current;
- search/index systems can resolve variants to one feature without displaying every variant as current;
- name data does not imply ownership or driving directions.

Ouros transformation:

Introduce a stable `place_ref_id`, separate `place_name_record` objects, effective ranges, variant relationships and source records. Do not import GNIS policy or its one-official-name rule as universal Ouros canon.

### UPU addressing manual — address, delivery address and delivery point are different concepts

Source:
https://www.upu.int/UPU/media/upu/publications/manualAddressingAddressingAndPostcodeManualEn.pdf

The UPU manual distinguishes an address, a delivery address and a physical delivery point.

Reusable architecture:

A textual destination reference should not be treated as identical to the physical point where a parcel can actually be handed over. A building can keep its identity while its accepted delivery entrance changes. A service can recognize a delivery point without that point defining ownership, residence or the complete identity of the site.

Ouros limitation:

No postal standard, postcode system, required address fields or universal delivery practice is imported.

## Design findings

### 1. Place identity should be stable

A persistent place needs an internal continuity key analogous to `actor_id` for people.

The key is implementation state. It is not automatically visible to NPCs.

### 2. Name records should be append-only

Renaming should create a new name record with an effective period and provenance. The old name remains available for historical records, archives, dialogue memories and search resolution.

### 3. Reference precision must be explicit

Examples of distinct scopes:

- region;
- settlement;
- district;
- street or path;
- named feature;
- site;
- structure;
- entrance;
- service counter;
- berth/platform/gate;
- delivery point;
- approximate landmark reference.

No hierarchy is universal until the local world model establishes it.

### 4. Record systems can update asynchronously

A map may publish the new name first. A sign can lag. A courier directory may update later. An archive catalog can intentionally retain the historical form. None of those facts proves fraud or incompetence by itself.

### 5. Place-name ambiguity can remain unresolved

Two different features may share the same local name. One historical note may be too vague to identify which one it meant. `ACCEPTED_AMBIGUITY` is preferable to fabricated certainty.

### 6. Address and access are separate

An address reference can resolve correctly while the usable entrance is elsewhere. Construction, events, security, accessibility, flooding or service changes can alter an approach or handoff point without changing the site's identity.

### 7. Naming and memory interact without becoming the same system

Public Memory may interpret why a name matters. This layer only preserves what forms were used, when, by whom, and what feature each record is believed to reference.

## PTU / Caelo cross-check

The project source scan confirms that PTU supports sandbox play, Jobs, exploration, persistent locations and mechanically meaningful environmental locations. It does not establish a universal place-name, street-address or navigation-resolution subsystem.

This pass therefore treats the following as UNKNOWN unless a governing PTU/Caelo source is later found:

- universal Survival checks to resolve an address;
- universal General Education checks to identify historical place names;
- universal Perception checks to locate an entrance;
- universal Technology Education checks for geocoding or map databases;
- universal Charm/Command/Guile checks for asking directions;
- fixed travel-time or search penalties for stale names;
- Trainer Features that grant naming or addressing authority;
- species, Types, Moves or Abilities that automatically identify a place or prove a route reference.

Exact Skill or Feature contracts may still be used where the source text specifically supports them. No narrative convenience should be promoted into a PTU rule.

## Copyright and transformation note

This research extracts only high-level structures, state separations and design lessons. No protected dialogue, map layout, distinctive plot, character or prose from Pokémon or community works is copied into Ouros.

## Candidate Ouros consequences

- old street names remain in letters and business records;
- a renamed bridge has both a current public label and a historical local nickname;
- a rebuilt station keeps the same place identity but gains a new entrance;
- a courier reaches the correct structure but the obsolete delivery point;
- a dispatcher receives two reports using different names for the same feature;
- two nearby hills share a colloquial name and must remain ambiguous until evidence disambiguates them;
- a resident continues using a former district name long after public maps change;
- a landmark disappears but its name persists in route instructions and neighborhood memory.

All such examples remain NON-CANON until authored into a specific region.