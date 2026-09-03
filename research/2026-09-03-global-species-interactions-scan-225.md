# Ouros Narrative Research — Global Species Interaction Graph — Pass 225

Status: RESEARCH ONLY. Provenance and design evidence; not Ouros canon.
Date: 2026-09-03

## Scope

This pass addresses the world-wide ecological interaction layer. It is intentionally global rather than Marea-specific.

The repository already establishes that wild populations can fight, compete, displace and prey on one another off-screen, that these outcomes can change abundance, distribution, behavior and resources, and that predator/prey relationships remained an explicit open implementation detail. This pass researches how to represent those relationships without requiring an all-pairs hand-authored simulation or invisible AutoPTU battles.

## Internal project evidence

### Existing Ouros canon

`canon/ecosystem-conflict-managed-development-foundation.md` establishes:
- off-screen competition, displacement and predation are authoritative ecosystem/world state;
- successful ecological predation may remove real prey membership;
- predator pressure can change prey behavior and habitat use without a kill;
- ecological outcomes may change local composition, vegetation, trails, nesting evidence, NPC reports and institutional responses;
- exact predator/prey relationships were deliberately left open pending species-grounded data.

### Existing wild-collective research

`research/2026-08-18-wild-collectives-territory-scan-11.md` already separates population, persistent collective, visible subgroup and tactical encounter. It also warns that co-location does not prove cooperation and that territoriality, leadership and mixed-species associations need species-grounded or observed evidence.

### PTU/PTR species data available inside AutoPTU

The read-only AutoPTU repository contains structured species records with diet information. Example: the Fletchling line is represented with `diet: ["omnivore"]` in the Foundry species data. This is useful as a coarse trophic constraint but is not sufficient to infer exact prey species.

Rule for Ouros: diet and habitat narrow candidate relationships; they do not automatically create species-to-species facts.

## Public Pokémon species evidence

Primary sources inspected:
- https://www.pokemon.com/us/pokedex/wurmple
- https://www.pokemon.com/uk/pokedex/pidgeotto
- https://www.pokemon.com/us/pokedex/krookodile
- https://www.pokemon.com/us/pokedex/flygon
- https://www.pokemon.com/us/pokedex/ekans
- https://www.pokemon.com/us/pokedex/golbat

These official entries demonstrate several useful relationship patterns.

Wurmple explicitly identifies Swellow as a predator and also describes Wurmple feeding on tree sap. This is unusually strong evidence because it names both a predator/prey pair and a resource relationship.

Pidgeotto searches a large territory for prey. This supports a predator role plus territorial foraging, but does not identify the prey species and therefore cannot justify arbitrary named prey edges.

Krookodile can detect small prey at very long distance, supporting a mobile predator role whose encounter pressure may extend over a wide home range.

Flygon can lure prey into sandstorms. This supports an environmental hunting strategy: habitat/weather context can change encounter risk even when prey abundance is unchanged.

Ekans can swallow large prey whole. This supports predation but not a named prey list.

Golbat feeds on blood and can share gathered blood with hungry conspecifics. This shows that a feeding relationship and a social resource-transfer relationship can coexist but must remain separate edge types.

Reusable conclusion: explicit named interactions deserve higher confidence than general diet or predator language.

## General ecology research

Sources inspected:
- Nature/Scitable overview of lethal and non-lethal predator effects: https://www.nature.com/scitable/knowledge/library/environmental-context-influences-the-outcomes-of-predator-13240808/
- Scientific Reports, predator experience changing later habitat choice: https://www.nature.com/articles/s41598-018-26757-y
- npj Biodiversity, habitat complexity reducing predation pressure: https://www.nature.com/articles/s44185-022-00007-x
- Nature Ecology & Evolution, migratory coupling between predators and migrant prey: https://www.nature.com/articles/s41559-018-0711-3
- Nature Communications 2026 meta-analysis on predator/prey temporal niche shifts under human disturbance: https://www.nature.com/articles/s41467-026-69113-9

High-level lessons relevant to Ouros:

1. Predation has consumptive and non-consumptive effects. A predator can lower prey encounter visibility or shift prey habitat/time use even when no prey member is removed.
2. Habitat complexity can alter encounter success. Dense cover, caves, reefs, canopy, rubble or other refuges should be allowed to lower effective predation pressure without changing the predator's nominal presence.
3. Predator experience can leave temporary behavioral memory in prey. Ouros can represent recent pressure as a population behavior state rather than individual sentience for every wild Pokémon.
4. Migrating prey can pull predator distributions with them. Migration therefore may change more than one species at once.
5. Human activity can alter temporal overlap between predators and prey. Ranger restrictions, busy routes, settlements or heavy Trainer traffic can therefore shift activity windows rather than only raw abundance.

These are ecological design principles only. No scientific numeric model is copied into Ouros.

## Interaction vocabulary proposed for design work

A single generic `relationship` field is too weak. Candidate edges should distinguish at least:

- PREDATES_ON: actor consumes target species.
- AVOIDS: actor actively reduces overlap with target.
- COMPETES_WITH: both consume or defend a materially overlapping resource.
- DISPLACES: actor pressure shifts target spatial use or access.
- TERRITORIAL_AGAINST: actor defends a site/home-range/resource against target.
- SCAVENGES_FROM: actor consumes remains or leftovers associated with target.
- FORAGES_RESOURCE: species uses a non-Pokémon food/resource node.
- FACILITATES: actor creates conditions or resources that benefit target.
- SHELTERS_WITH / ASSOCIATES_WITH: only when direct evidence supports repeated mixed-species association.
- NEUTRAL_OBSERVED: optional observational edge that prevents the generator from inventing a conflict merely because two species co-occur.

Edges are directional except where explicitly stored as paired/symmetric relations.

## Evidence grades

PROVENANCE_EXPLICIT
Direct official or project source names the relationship. Example: Wurmple -> prey_of -> Swellow.

SPECIES_TRAIT_STRONG
Species source gives a strong ecological role but not a named counterpart. Example: Pidgeotto hunts prey over a large territory.

PTU_DERIVED
PTU/PTR Diet, Habitat, size, movement, capabilities or other species data constrain a candidate interaction.

BIOLOGICAL_ANALOGUE
A real-world analogue suggests a candidate relationship. Never sufficient by itself for canon.

OUROS_INFERRED
World simulation creates a context-specific edge from approved traits and co-occurrence. Must remain reversible and provenance-linked.

OUROS_AUTHORED
Human-reviewed original Ouros ecology.

## Global generation rule

Do not author every possible species pair.

For each ecosystem instance:
1. collect species that can actually co-occur there;
2. load PTU/PTR diet, habitat, size/mobility and other approved species traits;
3. apply explicit Pokémon relationship evidence where available;
4. generate only plausible candidate edges for shared resources, predation, avoidance and territorial conflict;
5. score each edge with evidence and ecological context;
6. require human review or an approved inference policy before persistent world use;
7. let population state, season, weather, resource pressure and human disturbance modulate edge intensity through time.

This turns a global all-pairs problem into local interaction graphs per ecosystem.

## Spawn projection lesson

Ecological state should project into Cobblemon availability/weight/activity, while the ecological ledger remains authoritative.

Example:
- predator pressure rises;
- prey abundance may fall after actual demographic losses;
- even without losses, prey may shift toward cover or a different activity window;
- visible spawn weight/eligibility changes accordingly;
- NPC observers may report fewer sightings, changed routes or unusual activity.

Spawn observations do not manufacture population truth.

## NPC knowledge lesson

Ecology should emit observations rather than omniscient dialogue.

Possible observation packets:
- `predator_pressure_rising`
- `prey_sightings_declining`
- `territorial_displacement`
- `migration_followed_by_predators`
- `resource_competition_visible`
- `activity_window_shift`
- `unusual_mixed_species_association`

Rangers, field researchers, explorers, traveling Trainers, farmers, fishers and residents receive different subsets according to location, role, direct observation and communication routes. A report can be incomplete or wrong without changing canonical world truth.

## Copyright/provenance guardrail

No fan plot, dialogue, distinctive character, map or custom species is imported. Official Pokémon descriptions are used only for species ecology facts. General ecology literature contributes abstract modeling principles. PTU/PTR data remains a mechanical/species-data source and does not grant new combat mechanics.
