# Wild nesting, parental care & juvenile dispersal research — Pass 146

Status: RESEARCH ONLY. NON-CANON. External material is used as structural inspiration and provenance, never as imported plot or mechanics.

## Why this gap exists

The current Ouros Breeding/Egg/Nursery layer intentionally governs Trainer-directed breeding, Egg provenance/custody, nursery services, hatching and juvenile care after an authoritative mechanical result. It explicitly keeps wild nesting ecology separate. Wild Collectives, Seasonality, Migration, Conservation, Photography and Research Ethics each cover adjacent state, but none owns the full sequence from a wild reproductive site through dependent young to natal dispersal.

This pass therefore studies wild reproductive sites, parental-care observations, colony monitoring, juvenile dependency and the transition from nest departure to post-natal dispersal. It does not add breeding formulas, Egg inheritance, hatch timing, offspring species, fertility, parentage rules or capture rights.

## Pokémon source patterns

### Nidoqueen and Nidorina — care can alter behavior without becoming a combat rule

Official Pokédex material describes Nidoqueen physically sheltering offspring and suppressing poison secretion from its spines while young are present. Nidorina material likewise links a physical trait to safer feeding of young.

Reusable structure: species-authored parental care may be specific, physical and context-dependent. Ouros can record the observed behavior and the young present without translating it into Poison immunity, a protective aura, an Ability rewrite or a universal maternal behavior rule.

Sources:
- Pokémon Pokédex, Nidoqueen: https://www.pokemon.com/uk/pokedex/nidoqueen
- Pokémon Pokédex, Nidorina: https://www.pokemon.com/us/pokedex/nidorina

### Mandibuzz and Vullaby — provisioning can be tied to a nest

Official Mandibuzz Pokédex material describes searching for food for Vullaby and returning prey to its nest.

Reusable structure: a recurring adult route can be associated with a reproductive site and dependent young. The route, the provision event, the nest and any inferred relationship remain separate observations. Ouros must not infer parentage merely because an adult provisioned a juvenile.

Source:
- Pokémon Pokédex, Mandibuzz: https://www.pokemon.com/br/pokedex/mandibuzz

### Durant — colony defense and eggs can coexist with predation pressure

Official Durant Pokédex material describes eggs placed deep inside nests and coordinated defense against threats such as Sandaconda or Heatmor.

Reusable structure: colony architecture, egg presence, predation pressure and group defense can form a persistent ecological system. None of these observations automatically grants Swarm mechanics, shared initiative, tactical coordination bonuses or a custom nest hazard.

Source:
- Pokémon Pokédex, Durant: https://www.pokemon.com/us/pokedex/durant

### Kangaskhan — dependent young need not be represented as separate wild spawns

Official Kangaskhan material consistently treats the pouch-carried young as part of the species' parental context.

Reusable structure: the world may need to represent dependent young as part of a persistent family/reproductive observation rather than requiring one loaded Cobblemon entity per juvenile. Visual representation and authoritative ecological truth must remain separate.

Source:
- Pokémon Pokédex, Kangaskhan: https://www.pokemon.com/uk/pokedex/kangaskhan

## PTU campaign / community pattern

A public Pokémon Tabletop United campaign recap describes a group knocking down a tree, discovering that a nearby Pokémon was protecting eggs, and choosing restoration/de-escalation rather than taking the eggs or forcing a fight. The reusable lesson is not the specific scene. It is the encounter grammar:

world alteration -> protective response -> new ecological information -> non-capture resolution -> persistent restoration consequence.

This is useful for Ouros because a nest encounter should not default to loot, capture or combat.

Source:
- r/PokemonTabletop, public campaign log #24: https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

## Wildlife ecology and monitoring

### Leaving the nest is not independence or dispersal

A long-term USGS study of northern spotted owls found that juveniles could leave the nest and remain in the natal territory for months before beginning natal dispersal, then use temporary ranges before later settlement.

Reusable structure: Ouros must keep `NEST_DEPARTURE`, `DEPENDENCY_END`, `NATAL_DISPERSAL_START` and `SETTLEMENT/RECRUITMENT` distinct. A juvenile seen outside a nest is not automatically independent, abandoned or dispersing.

Source:
- USGS, Natal and breeding dispersal of northern spotted owls: https://pubs.usgs.gov/publication/70024280

### Post-independence habitat can differ from nesting habitat

USGS research on golden-winged warblers found that independent fledglings used habitat differently from breeding adults and nest-site expectations.

Reusable structure: protecting a nesting patch alone may not protect the juvenile phase. Ouros should support `POST_NATAL_USE_AREA` and later juvenile habitat observations without treating them as the nest itself.

Source:
- USGS, Post-independence fledgling ecology in a migratory songbird: https://www.usgs.gov/publications/post-independence-fledgling-ecology-a-migratory-songbird-implications-breeding-grounds

### Dispersal timing can vary with local conditions

A 2024 USGS-linked study of juvenile burrowing owls found wide variation in natal dispersal timing and different responses by juveniles and adults to food, ectoparasites and parental departure.

Reusable structure: juvenile dispersal is not a species-global fixed timer. Local food, health, disturbance, parental presence and habitat can correlate with timing without giving the narrative generator authority to invent mechanical age thresholds.

Source:
- USGS, Experimental changes in food and ectoparasites affect dispersal timing in juvenile burrowing owls: https://www.usgs.gov/publications/experimental-changes-food-and-ectoparasites-affect-dispersal-timing-juvenile-burrowing

### Monitoring itself can change the thing being monitored

NPS monitoring reports for nesting shorebirds document disturbance risk from people, vehicles and dogs and explicitly avoid some close approaches to incubating adults or young. This aligns with the existing Research Ethics layer: observer effort, access method and disturbance history must accompany nest observations.

Source:
- NPS, American Oystercatcher annual report / human disturbance: https://www.nps.gov/articles/caha_amoy2014.htm

## Reusable Ouros design lessons

1. A reproductive site can persist across many annual episodes even when no nest is active this season.
2. `EGGS_OBSERVED` does not establish parentage, ownership or capture rights.
3. Adult absence during one observation does not establish abandonment.
4. Juvenile size or first independent movement does not establish mechanical Level, Evolution eligibility or independence.
5. Nest departure, parental-care termination, natal dispersal and recruitment are separate transitions.
6. A colony can move between nearby sites without becoming a new population automatically.
7. Monitoring effort and disturbance must be stored because absence of observation is not absence of nesting.
8. Human closures, boardwalks, roads, tourism, wildfire, storms, vegetation change and water level can affect nesting without requiring a villain.
9. Wild Eggs remain ecological entities until an authored intervention legitimately creates custody; only then does the existing Egg/Nursery layer take over.
10. Loaded Minecraft entities are projections, never census or kinship truth.

## Mechanical boundary

No source in this scan authorizes Ouros to invent:
- breeding eligibility;
- parent contribution or lineage;
- offspring species;
- Egg Moves, Nature, Ability or gender;
- hatch timing;
- nest-defense buffs;
- parental reaction rules;
- capture bonuses/penalties around nests;
- juvenile stat penalties;
- automatic Loyalty or ownership after rescue;
- terrain/hazard effects from nests;
- swarm or Pack Mon behavior from colony membership.

The project PTU/Caelo corpus remains the authority for any mechanical breeding/hatching rule. A search of currently exposed GitHub sources did not recover a reliable Caelo-specific rule set for wild nesting or juvenile dispersal. Super PTU Online Helper was not available as an invocable capability in this run, so no output is attributed to it.
