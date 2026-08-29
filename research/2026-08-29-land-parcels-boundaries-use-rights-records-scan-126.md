# Ouros Narrative Research — Land Parcels, Boundaries, Use Rights & Records — Pass 126

Status: RESEARCH ONLY. Provenance and design evidence. This file does not establish Ouros property law, land institutions, ownership rules, survey standards, rights of way, easements, leases, titles, or adjudicative authority.
Date: 2026-08-29

## Why this gap was selected

The repository already contains dedicated layers for homes and occupancy, cartography and surveying, ranch operations, conservation stewardship, civic public works, roads, archives, agreements, adjudication, finance and settlement change. The complete current design inventory was checked before this scan.

A remaining continuity gap sits between those systems: persistent identity for land units and boundary claims, the provenance of mapped or physically marked boundaries, recorded interests or use permissions when canon establishes them, later survey corrections, and handoffs when a public work, ranch, residence, reserve or route intersects those records.

Existing Homes/Housing explicitly keeps ownership as a separate claim and forbids inference of property law from residence. Existing Cartography treats maps and surveys as evidence rather than omniscient world truth. Civic Governance grants no land-use mandate unless canon authors it. Adjudication similarly requires an authored deciding body and available outcome. Pass 126 therefore records spatial/legal provenance without filling those canon gaps.

## Public Pokémon material

### Paniola Ranch — managed landscape with internal physical divisions

Source: https://bulbapedia.bulbagarden.net/wiki/Paniola_Ranch

Paniola Ranch is presented as a named managed landscape connected to surrounding routes. Its geography contains multiple areas separated by fences and ramps, including a fenced pasture and operational spaces around the Nursery and farm equipment. Animation material also assigns the ranch to a family and depicts ongoing work there.

Reusable structure for Ouros:
- a named managed property can contain several functional sub-areas;
- fences and paths are useful world landmarks and operational boundaries;
- the same place can connect private/managed activity with public travel links;
- operation, residence, stewardship, ownership claim and exact legal geometry should remain separate records.

Transformation guardrail: a visible fence may represent husbandry, access control, old construction or a convenient physical divider. It does not become an authoritative parcel boundary merely because Minecraft renders it.

### Floccesy Ranch — a boundary created for one purpose can outlive that origin

Source: https://bulbapedia.bulbagarden.net/wiki/Sangi_Ranch

Floccesy Ranch is described as having begun when a fence was made to protect Pokémon. Later it operates as a ranch containing tame and wild Pokémon, river frontage and a forest behind it.

Reusable structure for Ouros:
- a physical boundary can begin as a practical intervention and later become part of local place identity;
- current land use can differ from the original reason a boundary feature was installed;
- Pokémon can cross or disregard human operational limits without changing the human record;
- old boundary features can become evidence in later mysteries while remaining ambiguous about their original authority.

Ouros should preserve the date, purpose claim and source of a fence or marker when known instead of assigning it timeless legal meaning.

### Secret Bases — persistent occupancy/use without a safe ownership-law inference

Source: https://bulbapedia.bulbagarden.net/wiki/Secret_Base

Core-series Secret Bases let a Trainer establish and decorate a persistent personal space at designated spots, relocate to another spot, visit other Trainers' bases and preserve imported representations through record sharing.

Reusable structure for Ouros:
- persistent personal use of a place can be meaningful even when no broad property regime is defined;
- use, customization, public identity and location persistence are distinct dimensions;
- relocation should preserve historical identity and prior-place provenance;
- two actors' records can disagree about current use because they were synchronized at different times.

This material is a strong guardrail against equating occupation with legal ownership. The game mechanic itself should not be converted into Ouros real-estate doctrine.

### Resort Area Villa — transfer of a residence can be an explicit authored event

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Resort_Area
- https://bulbapedia.bulbagarden.net/wiki/Villa

Pokémon Platinum explicitly presents a Villa that can become the player's home after an offer from a previous owner. Other adaptations also depict later sale/purchase of the same residence.

Reusable structure for Ouros:
- where canon explicitly establishes a transfer, former and current claims can coexist in historical records;
- the persistent structure should not lose provenance when its holder changes;
- transfer of a residence does not define the geometry of its parcel, neighboring rights, public access or a universal transaction system.

## Pokémon Tabletop community material

Source: https://www.reddit.com/r/PokemonTabletop/comments/iqxtg0/a_custom_region_map/

A public PTU region-map discussion recommends additional connections, optional towns and non-essential areas instead of a map composed only of required League stops. The discussion treats routes, cities and mountain passages as a connected geography whose usefulness comes from multiple ways through the region.

Reusable lesson for Pass 126: land records should support the living travel graph rather than force the region into a rigid parcel puzzle. A historic corridor, informal path, ranch crossing or public-works route can create story because it intersects several persistent places. The map remains a representation; Travel owns actual journey connections.

The community source is design inspiration only. No fan setting, map, names or geography are copied into Ouros.

## Public cadastral and surveying material

### Tasmanian property-boundary mapping — mapped geometry and surveyed geometry can differ

Source: https://nre.tas.gov.au/land-tasmania/geospatial-infrastructure-surveying/about-cadastral-surveys/property-boundaries-on-listmap

The Tasmanian government explains that spatial cadastral mapping can contain substantial positional error and illustrates cases where mapped parcel lines differ from modern field-survey measurements. It also describes ongoing improvement when new surveyed subdivisions are connected to survey control and accepted into the title system.

Reusable architecture for Ouros:
- `map_geometry_claim` and `survey_measurement` need separate provenance;
- a later survey can supersede geometry without erasing the older map artifact;
- old mapped lines can remain historically important even after correction;
- Minecraft coordinates should never silently become legal geometry because they are visually precise.

No Tasmanian accuracy figures, title process, statutory authority or survey procedure is imported into Ouros.

### National Land Parcel Boundaries — one spatial product can aggregate several classes of land objects

Source: https://link.fsdf.org.au/dataset/national-land-parcel-boundaries

Australia's national parcel dataset aggregates jurisdictional cadastral sources and includes parcel-like information for easements, roads, crossings, rail and water as well as ordinary land parcels. The dataset is sourced from state and territory custodians rather than created as a universal local authority.

Reusable architecture for Ouros:
- persistent land identifiers should link outward to roads, crossings, conservation, waterways and public works instead of duplicating those systems;
- one map product can visualize several kinds of spatial interest while preserving each source owner;
- a corridor or crossing can have a relationship to parcels without implying ownership of every connected place.

No Australian legal category or government structure is imported.

### National Academies parcel-data model — parcel identity, boundary and interests are related but provenance matters

Sources:
- https://www.nationalacademies.org/read/11978/chapter/3
- https://www.nationalacademies.org/read/11978/chapter/6

The 2007 National Research Council study describes parcels as identifiable land units with maintained location/boundary information and histories of recognized interests. Its international review also describes cadastre as an inventory linking separately identified land objects to boundaries, descriptive data, rights and restrictions.

Reusable architecture for Ouros:
- stable `land_unit_id` should survive map editions and ownership/use changes;
- geometry, identifier, descriptive attributes and claims/interests need explicit source links;
- separate institutions may maintain different parts of the record;
- the record should support current and historical states rather than a single overwrite.

This is information-system inspiration. Ouros receives no United States legal definitions, registration doctrine, tax system, zoning regime or presumptive property rights from this source.

## Cross-source synthesis

The combined sources support a high-value continuity pattern:

1. A place exists physically and socially before every detail of its record is known.
2. Physical fences, roads, streams, walls and survey markers provide observations, not automatic authority.
3. Maps provide versioned geometry claims.
4. A survey can provide newer measurements while preserving uncertainty and its own scope.
5. Ownership, occupancy, stewardship, access, maintenance duty and public operational control remain separate relationships.
6. A canon-authored institution may later recognize, revise or decide some of those relationships.
7. Public works or environmental change can alter the physical landscape while the record catches up at another time.
8. Historical discrepancies can produce mysteries without requiring fraud or a hidden villain.

## Narrative patterns extracted

Useful mysteries:
- a fence and registry map disagree because the fence was built for husbandry rather than boundary marking;
- a new survey corrects an old approximate map and reveals that two long-used paths cross different recorded units;
- an address survives after subdivision, consolidation or renaming and is mistaken for a parcel identity;
- an old boundary stone is genuine but belongs to an earlier configuration;
- a river or road moved physically while the governing record did not automatically change;
- two maps are both accurate for their stated purpose but use different geometry or scale;
- an informal shortcut has decades of local use but no canon-authored access-right record;
- a public work completed physically while the associated land-record update remained pending.

Useful character roles, all NON-CANON until authored:
- survey technician or field mapper;
- archive/registry clerk;
- ranch or reserve steward;
- public-works corridor coordinator;
- neighborhood historian;
- cartographer who specializes in old editions;
- mediator or case worker when a dispute is handed to an existing authority.

None of those roles automatically possesses legal power.

## PTU / Caelo cross-check

Existing project source material supports campaign structure, evidence-rich locations, Skill-driven characters and exact authored environmental mechanics when a governing source defines them. It does not establish a universal land-law or cadastral subsystem.

Remain UNKNOWN unless an exact supplied PTU/Caelo rule or later canon source establishes them:
- universal property ownership mechanics;
- deed/title creation by a Skill Check;
- universal survey DCs or exact-boundary discovery checks;
- automatic property-right detection through Perception, Survival, General Education or another Skill;
- Pokémon species that inherently recognize human parcel lines;
- Ground/Rock/Steel typing as surveying authority;
- Dig, Earthquake, Bulldoze, Strength or other Moves creating, moving or validating a legal boundary;
- Trainer Features granting universal authority to define ownership or access rights;
- a physical survey marker receiving combat HP or legal force from its Minecraft block state.

Where an authored story needs a factual field survey, use the existing Cartography layer and only invoke PTU/Caelo checks when the exact governing rule and intended consequence are known.

## Copyright and transformation note

The Pokémon, PTU-community and operational sources above are used only for high-level structures, state separations, provenance lessons and design guardrails. This pass does not reproduce protected dialogue, distinctive characters, complete plots, maps, encounter scripts or setting geography.

## Candidate output

The research supports a new proposed continuity extension for:
- persistent land-unit identity;
- boundary evidence and revision history;
- recorded claims/interests only where canon authors them;
- physical-marker provenance;
- map-versus-survey discrepancies;
- access/corridor handoffs;
- public-works and conservation intersections;
- reduced encounter forms that never let combat decide ownership or legal scope.
