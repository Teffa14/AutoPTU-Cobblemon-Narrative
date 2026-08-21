# Pass 89 Research — Island Biogeography, Endemism & Dispersal

Status: research/provenance only. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-21

## Why this pass exists

The repository already models maritime travel, open-ocean ecology, biosecurity, introduced species, conservation, regional mobility, coastal change and persistent wild populations. It does not yet have a dedicated contract for island-scale ecological isolation, natural colonization, local extinction, stepping-stone dispersal, endemism, archipelago turnover or ecological differentiation among nearby islands.

The missing distinction matters because several existing systems can otherwise collapse into one incorrect inference:

`species seen on one island only` -> `endemic species`.

That inference is unsafe.

A population may instead be:
- genuinely endemic;
- undersurveyed elsewhere;
- seasonally present;
- recently colonizing;
- recently extirpated from another island;
- maintained by repeated immigration;
- introduced by people;
- displaced by weather;
- represented by one persistent roaming individual;
- split into several locally differentiated populations of one species.

Pass 89 therefore studies how island identity, isolation and connectivity can become persistent world state without inventing speciation mechanics or replacing the existing Biosecurity and Evolution layers.

## Internal overlap check

Relevant existing layers inspected before writing:
- `design/maritime-coasts-depths-layer.md`
- `design/open-ocean-oceanography-pelagic-ecology-layer.md`
- `design/biosecurity-introduced-species-translocation-layer.md`
- `design/interregional-mobility-recognition-layer.md`
- `design/conservation-protected-areas-stewardship-layer.md`
- `design/wild-collective-agency-layer.md`
- `design/interspecies-ecological-relations-layer.md`
- `design/seasonality-calendar-phenology-layer.md`
- `design/evolution-life-stage-transformation-layer.md`
- `design/cartography-survey-wayfinding-layer.md`
- `design/engine-readiness-snapshot-pass-88.md`

Pass 89 should own archipelago/island biogeographic state. Maritime remains authoritative for sea travel. Open Ocean remains authoritative for pelagic water state. Biosecurity remains authoritative for human-assisted introduction/translocation. Evolution remains authoritative for individual Pokémon transformation. Conservation remains authoritative for protection and management actions.

## Source 1 — official Pokémon: Alola as an isolated island region

Official Pokémon Sun/Moon material describes Alola as an island region where some Pokémon adapted to a distinct natural environment and developed regional forms whose ecology differs from forms known elsewhere.

Source:
https://www.pokemon.co.jp/ex/sun_moon/world/160801_03.html

Related Ultra Sun/Ultra Moon material explicitly describes Alola as a warm region made of islands and again connects regional forms to the region's distinctive natural environment.

Source:
https://www.pokemon.co.jp/ex/usum/story/170922_02.html

Reusable design lesson:
- geographic isolation can support durable regional ecological differentiation;
- local difference should be represented as authored or observed state, not invented ad hoc by procedural generation;
- a regional form is a species/mechanical fact that must come from authoritative Pokémon/PTU data, not from the narrative layer deciding that isolation 'should' cause a new form.

Guardrail:
Pass 89 may model the conditions and history around isolated populations. It may not create new Pokémon forms, typings, Abilities, Moves, stats or evolution methods.

## Source 2 — official Pokémon: Oricorio and local resources

The official Pokédex describes Oricorio forms as changing after consuming different nectars.

Source:
https://www.pokemon.com/us/pokedex/oricorio

The animated episode `A Seasoned Search!` also uses Yellow Nectar as a seasonal resource associated with Oricorio and a hidden meadow.

Source:
https://www.pokemon.com/us/animation/seasons/20/episode-18-a-seasoned-search

A secondary reference records that the four Nectar types in Alola are associated with different island locations.

Discovery reference:
https://bulbapedia.bulbagarden.net/wiki/Nectar

Reusable design lesson:
- nearby islands can differ because resources, vegetation, climate, elevation or habitat differ;
- one species can interact differently with local resource patches without becoming a different species;
- local ecological resources can create route-specific observation opportunities and cultural knowledge.

Guardrail:
The known Oricorio/Nectar relationship is specific. Ouros must not infer that arbitrary island foods change Pokémon forms or types.

## Source 3 — PTU living world: Kairos Isles

Kairos Isles is a public PTU living-world campaign. Its public wiki organizes the region explicitly as multiple islands and describes the islands as having distinct biomes.

Sources:
https://kairosptu.wiki.gg/
https://kairosptu.wiki.gg/wiki/Category%3AIslands

Its public encounter tables show different habitat tables across islands and locations rather than one archipelago-wide encounter pool.

Source:
https://kairosptu.wiki.gg/wiki/Pok%C3%A9mon_Encounter_Tables

Reusable design lesson:
- an archipelago should not use one global encounter distribution;
- island identity can be expressed through multiple habitat mosaics inside the island, not only one 'island biome';
- public encounter knowledge can itself be partial or spoiler-sensitive;
- island-scale differentiation can coexist with player-created locations and a living-world structure.

Copyright/originality boundary:
Do not copy Kairos islands, guardians, regional forms, towns, encounter percentages, characters or lore. Use only the structural lesson that island-specific habitat mosaics and public/private knowledge can coexist.

## Source 4 — PTU campaign retrospective: Tales of Visiwa

`Tales of Visiwa` was a long-running PTU campaign set in a tropical island region. The retrospective describes a region where geography, dangerous wilderness, exploration permissions, settlements and local history strongly affected the campaign.

Source:
https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Reusable design lesson:
- island geography can shape institutions and exploration practices;
- a regional campaign can support several personal motivations while geographic isolation remains a constant world constraint;
- islands become stronger campaign spaces when access, settlement, wilderness and history are linked rather than treated as disconnected route maps.

Copyright/originality boundary:
Do not reuse Visiwa's cultures, colonial history, gods, NPCs or plot. The source is useful only as evidence that island geography can sustain a full PTU campaign rather than a short side area.

## Source 5 — National Park Service: basic island-biogeography pattern

NPS summarizes the core island-biogeography idea: island size and distance/isolation can influence colonization and local extinction, helping explain ecological differences among islands.

Source:
https://www.nps.gov/articles/000/travel-blog-the-pacific-islands.htm

A Boston Harbor Islands study found species richness increasing with island area in the surveyed beetles, while dispersal ability influenced colonization patterns. It also observed repeated extinction/recolonization as a plausible source of population turnover.

Source:
https://www.nps.gov/boha/learn/management/research-abstracts-madden.htm

Reusable design lesson:
- island occupancy is a history, not a permanent boolean;
- the same species can disappear locally and later recolonize naturally;
- dispersal capability matters, but should be inferred from authoritative species capabilities/observations rather than narrative convenience;
- larger or better-connected islands can support different population persistence than small isolated patches without requiring hidden 'spawn bonuses'.

Important limitation:
The narrative layer should not implement a literal MacArthur-Wilson equation for Pokémon populations unless the project later chooses a validated simulation model. The principle is enough for world-state causality.

## Source 6 — stepping stones and connectivity

NOAA reports that parts of the Northwestern Hawaiian Islands may function as stepping stones and reservoirs for organisms across an archipelago.

Source:
https://sanctuaries.noaa.gov/science/condition/pmnm/history.html

A NOAA Fisheries feature on Hawaiian hawksbill turtles also discusses the archipelago as a possible historical stepping stone for colonization elsewhere in the Pacific.

Source:
https://www.fisheries.noaa.gov/feature-story/hawksbill-sea-turtles-are-truly-hawaii-locals

A conservation synthesis notes that stepping-stone habitats can maintain movement or recolonization when organisms can cross the gaps between them.

Reference:
https://portals.iucn.org/library/efiles/documents/FR-021.pdf

Reusable design lesson:
- a tiny island may be important even if almost nothing lives there permanently;
- temporary stopovers, feeding sites, roosts, seasonal pools or reefs can maintain regional connectivity;
- losing one stepping stone can change movement between two larger populations without destroying either population immediately.

## Source 7 — endemism and vulnerability

NOAA describes endemic species as native organisms restricted to a geographic location and notes very high levels of endemism in remote Hawaiian marine habitats.

Sources:
https://marinedebris.noaa.gov/cultural-and-ecological-significance-papah-naumoku-kea-marine-national-monument
https://oceanservice.noaa.gov/news/mar14/nwhi-fish-species.html

NPS notes that island populations can be geographically restricted and especially vulnerable to introduced species, habitat change and loss of dispersal opportunities.

Source:
https://www.nps.gov/articles/000/aps-20-2-8.htm

Reusable design lesson:
- `endemic` should be a reviewed biogeographic assessment, not a decorative rarity label;
- a population can be locally important because it is isolated, old, genetically/ecologically distinct or the last known occurrence, but those are separate claims;
- highly restricted populations create strong stakes for conservation, science, biosecurity and public information without needing Legendary Pokémon.

## Source 8 — isolation does not determine every outcome

NPS research across Boston Harbor islands found that area, isolation and dispersal can interact differently for native and non-native species, and that local patterns do not reduce cleanly to one variable.

Source:
https://www.nps.gov/boha/learn/management/research-abstracts-long-1.htm

Reusable design lesson:
- do not reduce archipelago ecology to `farther island = fewer species`;
- habitat quality, disturbance, mobility, human transport, currents, weather and historical contingency can all matter;
- Ouros should preserve competing hypotheses until observation supports one.

## Source 9 — assisted colonization as a high-stakes management choice

A NOAA-hosted paper discusses assisted colonization as a possible response for climate-sensitive island endemics, while emphasizing institutional and practical barriers.

Source:
https://repository.library.noaa.gov/view/noaa/62512

Reusable design lesson:
- moving a population to another island can be a difficult conservation decision rather than a generic 'rescue';
- assisted colonization must pass through Conservation, Biosecurity, custody/provenance and monitoring layers;
- successful release does not prove establishment;
- establishment does not prove the intervention had no downstream ecological effects.

## New Ouros design synthesis

Pass 89 should introduce persistent records for:
- island/archipelago identity;
- survey effort by island and habitat;
- occupancy history for populations;
- colonization observations and competing pathway hypotheses;
- local extirpation assessments;
- recolonization events;
- stepping-stone function;
- endemism assessments with evidence and scope;
- within-archipelago population differentiation claims;
- natural-versus-assisted dispersal uncertainty;
- island-specific ecological baselines;
- cross-island comparison projects.

## Strong non-inferences

Do not infer:
- island-only observation = endemic;
- regional form = caused by isolation alone;
- isolated population = new species;
- different behavior = different species/form;
- rare on one survey = local extinction;
- missing for one season = extirpated;
- first observation = recent colonization;
- same species on two islands = continuous gene flow;
- flight-capable Pokémon = guaranteed inter-island dispersal;
- Swim/Sky movement = open-ocean travel capability;
- ferry presence = human introduction pathway actually used;
- introduced = invasive;
- naturalized = harmless;
- protected island = mechanically restricted capture;
- small island = low encounter level;
- endemic = stronger stats or rarer encounter tier.

## PTU/Caelo boundary

No new mechanical rule was extracted from public web material.

Before a concrete encounter uses capabilities such as Sky, Swim, Teleporter, Mountable, Naturewalk, migratory travel, capture, relocation or release, the exact PTU/Caelo text and current Java support must be checked.

The complete primary Caelo corpus was not reliably accessible in this runtime. No Caelo-specific island, travel, migration or conservation mechanic is asserted here.

## Candidate design direction

The most useful architectural sequence is:

`island geography`
-> `habitat mosaic`
-> `survey effort`
-> `population occupancy history`
-> `dispersal/colonization evidence`
-> `endemism or connectivity assessment`
-> `management/research response`
-> `Minecraft/Cobblemon projection`
-> optional `AutoPTU battle snapshot`.

The server-side graph remains authoritative. Loaded Cobblemon entities must never become the population census.