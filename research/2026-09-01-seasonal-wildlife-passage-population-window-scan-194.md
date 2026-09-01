# Seasonal Wildlife Passage and Population Window Scan — Pass 194

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-01
Canon effect: NONE. This file records sources and transformed design lessons. It does not establish Ouros species, seasons, migration routes, population sizes, encounter tables, breeding behavior, or Caelo ecology.

## Research question

How can Ouros represent wild Pokémon populations that change over time and space without turning ecology into a static spawn table, an omniscient quest marker, or a battle generator?

The target gap is narrower than generic wildlife incidents, field search, route closure, weather, or scientific-record continuity. The missing structure is a persistent ecological window: a temporary concentration, passage, absence, nesting/gathering period, feeding opportunity, or corridor use that can be observed incompletely by different people and that may affect ordinary district life.

## Internal repository overlap check

The repository was inspected before selecting this seam.

Relevant canon already exists:
- Marea Interior contains seasonal watercourses on Sendero del Vidrio.
- Estación Mirador maintains ecological observations, route reports, and specimen records.
- Dr. Nerea Sol maintains a longitudinal district record and explicitly revises conclusions when evidence changes.
- Mara Veyra and Marea Field Office handle wildlife incidents and route observations without owning ecological truth.
- Ema Rey performs transect observations under Mirador protocols.
- Jo Venn teaches practical observation and safe field practice.
- the canonical quest taxonomy requires `POKEMON` questlines grounded in district ecology and already reserves `SERVER_EVENT` for seasonal observations.
- the Thin Delivery Season allows changes in wild-Pokémon presence only when observations support them.

Existing design layers already cover evidence/provenance, field search, closure/access, preparedness, public notices, education, provisioning, visitor continuity, and aftermath. This pass therefore does not create another authority, another closure system, or another generic observation ledger.

Repository-wide indexed searches for `migration`, `habitat`, `nesting`, `breeding`, `swarm`, `outbreak`, `ecology`, `corridor`, and `season` did not surface an existing dedicated continuity layer with the same scope. Search index limitations are still possible, so this is evidence of no indexed duplicate rather than proof that no older prose ever mentions those words.

## Source A — Pokémon Legends: Arceus, Daybreak update

Source: official Pokémon Legends: Arceus website, Daybreak update.
URL: https://legends.arceus.pokemon.com/en-au/update/

Observed structure:
- multiple mass outbreaks can emerge across a region during a limited phenomenon;
- the outbreaks are associated with rainstorms;
- the player investigates the phenomenon with an existing local actor rather than receiving its complete explanation immediately;
- species that are ordinarily difficult to find can become temporarily observable in concentrated numbers.

Reusable lesson for Ouros:
A temporary concentration can be a world condition first and an explanation second. The player may encounter evidence of unusual presence before anyone knows whether the cause is weather, food, route connectivity, reproductive behavior, disturbance, coincidence, or another factor.

Do not import:
- Hisui species distribution;
- the Daybreak plot;
- Warden Mai or Munchlax as characters;
- rainstorms as a universal outbreak cause;
- game-specific catch rates or outbreak generation formulas.

## Source B — New Pokémon Snap ecological survey structure

Sources: official New Pokémon Snap website and official exploration/free-update pages.
URLs:
- https://newpokemonsnap.pokemon.com/en-au/
- https://newpokemonsnap.pokemon.com/en-au/explore/
- https://newpokemonsnap.pokemon.com/pt-pt/free-update/

Observed structure:
- the core activity is repeated ecological survey rather than mandatory battle;
- distinct habitats support different assemblages and observable behavior;
- repeated visits to a route can reveal behaviors that were not visible on earlier visits;
- day/night variants and local environmental features change what can be observed;
- a river can function as a shared ecological concentration point because many Pokémon gather near a sustaining resource;
- some Pokémon remain concealed in terrain and require careful observation rather than direct confrontation.

Reusable lesson for Ouros:
Repeated transects should be able to produce genuinely different evidence without claiming that the world rerolled arbitrarily. Observation conditions, time window, route segment, disturbance level, weather observation, and previous uncertainty can all explain why a population signal appears or disappears.

A longitudinal station such as Mirador should therefore store observations rather than a single canonical `species_present = true` flag whenever ecology is uncertain.

Do not import:
- Photodex scoring;
- research levels as an Ouros stat;
- Illumina phenomenon;
- NEO-ONE;
- Lental species lists or locations.

## Source C — Pokémon Scarlet/Violet mass outbreaks

Sources: official Pokémon news pages describing event mass outbreaks.
Representative URL: https://www.pokemon.com/uk/news/the-fire-type-pokemon-charcadet-vulpix-and-numel-are-appearing-in-mass-outbreaks

Observed structure:
- a mass outbreak is explicitly described as many individuals of the same species appearing in one location;
- event windows can begin and end at explicit times;
- the phenomenon is geographically scoped rather than globally changing every location.

Reusable lesson for Ouros:
Population concentration should have a spatial and temporal envelope. The server may know an authoritative active window for simulation, while NPC knowledge remains observation-based and delayed. A resident who saw many individuals yesterday is reporting a dated observation, not permanent regional truth.

Do not import:
- online-event scheduling logic;
- shiny modifiers;
- portal-news mechanics;
- Paldea/Kitakami/Blueberry distributions.

## Source D — National Park Service migration/corridor guidance

Source: U.S. National Park Service, Grand Teton National Park, “Migrations Need You.”
URL: https://home.nps.gov/grte/learn/nature/migrations-need-you.htm

Observed real-world operational structure:
- wildlife movement depends on connected pathways;
- some areas may be temporarily closed to provide space during sensitive periods such as winter or birthing season;
- visitors are asked to keep distance and respect closures;
- management distinguishes the animal movement itself from the human-access response.

Reusable lesson for Ouros:
An ecological window can affect route use without turning wildlife into an enemy. A settlement may shift a work route, postpone a public field-school session, narrow access, or reroute deliveries while the underlying Pokémon movement remains an ecological fact under observation.

This source is useful for structure only. No U.S. legal standard, distance, agency power, wildlife regulation, or closure doctrine is imported into Caelo.

## Source E — Pokémon Ranger environmental reuse

Source: Bulbapedia summary of Lyra Forest in Pokémon Ranger, used as secondary descriptive reference.
URL: https://bulbapedia.bulbagarden.net/wiki/Lyra_Forest

Observed structure:
- one forest supports ordinary traversal, escorts, a lost-person incident, localized Pokémon behavior, fire response, deeper later exploration, and additional missions;
- the same physical environment supports different tasks at different times rather than being consumed by one quest.

Reusable lesson for Ouros:
A corridor can remain a durable place while its ecological and social use changes. Sendero del Vidrio does not need a new dungeon instance for every population window. The same shelves, crossing, and junction can acquire different temporary observations, access advice, work patterns, and encounter possibilities.

Do not import Ranger capture mechanics, characters, shrine content, mission plots, or species placement.

## PTU / project-source cross-check

Read-only AutoPTU evidence was searched for habitat and wild-Pokémon concepts.

Observed evidence:
- project source material contains species habitat fields in audited Pokédex data;
- Foundry/PTR2E material in the repository includes habitat tables and habitat configuration;
- source indices contain mechanics that can reference whether a Pokémon is standing on terrain related to its natural habitat;
- Trainer content includes mechanics that explicitly distinguish Wild Pokémon in specific effects;
- Survival appears as an existing wilderness-oriented Skill in bundled rules material.

Interpretation boundary:
These pieces prove that habitat, wild status, terrain relationship, and wilderness skills exist in source material. They do not prove a PTU rule that generates seasonal migration, outbreak size, nesting windows, regional abundance, breeding seasons, corridor preference, or ecological causation.

Therefore Narrative must not infer any of those facts from a species habitat tag alone.

`SPECIES_HABITAT_TAG != CURRENT_LOCAL_PRESENCE`
`CURRENT_LOCAL_PRESENCE != ABUNDANCE`
`ABUNDANCE_OBSERVATION != MIGRATION`
`TEMPORARY_CONCENTRATION != BREEDING_EVENT`
`WEATHER_CORRELATION != WEATHER_CAUSATION`

## Caelo source status

No indexed Caelo-specific source was located in Narrative, AutoPTU-Java, or AutoPTU during this pass.

This pass therefore leaves unresolved:
- Caelo seasons and calendar ecology;
- protected species or protected areas;
- regional wildlife-management authority;
- capture restrictions during sensitive periods;
- breeding/nesting doctrine;
- migration knowledge already established in Caelo lore;
- regional scientific terminology;
- whether any species have canon migration routes in Caelo.

No answer is invented here.

## Transformed design principles

1. Store ecological windows separately from observations about them.
2. A concentration needs a location envelope and time envelope.
3. NPCs know dated observations, reports, and hypotheses; they do not automatically read authoritative population state.
4. Repeated absence can be evidence, but one failed sighting is weak evidence.
5. Weather and ecological change can correlate without the simulation declaring causation.
6. A route may remain physically passable while ordinary users voluntarily avoid a segment because wildlife is using it.
7. A route may also receive an actual closure through the existing access/closure layer; ecology does not create a second closure authority.
8. Wild Pokémon can create noncombat gameplay through observation, detours, timing, documentation, education, and work rescheduling.
9. Battle only occurs when an actual immediate confrontation is present and should not be the default proof that a population exists.
10. Minecraft spawn/despawn is presentation/simulation evidence, not canonical population truth by itself.

## Candidate narrative value

This seam can enrich the canonical Thin Delivery Season without solving it. For example, Mirador might document an unusual temporary concentration near a seasonal crossing during the same period as route irregularity. That observation could affect one hypothesis, but it must not silently become the final cause of reduced deliveries.

It can also support independent `POKEMON`, `EXPLORATION`, `SETTLEMENT`, `CLASS`, and `SERVER_EVENT` questlines after the initial arc, using the same durable district geography.
