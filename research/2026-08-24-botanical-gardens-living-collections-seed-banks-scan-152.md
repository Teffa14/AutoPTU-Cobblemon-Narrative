# Research Scan — Botanical Gardens, Living Collections & Seed Banks — Pass 152

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Sources below are inspiration and evidence, not imported setting truth.
Date: 2026-08-24

## Why this scan

The repository already has strong authorities for wild vegetation, pollination, seed dispersal, restoration, conservation, museums, taxonomy, biosecurity, science, tourism and institutional infrastructure. The remaining gap is institutional stewardship of living plant material over long periods: accessioning, provenance, propagation, duplicate holdings, seed banking, viability review, curatorial decisions, public display, research use and eventual transfer or deaccession.

This is narrower than `flora-pollination-seed-dispersal-layer.md`. Flora owns ecological vegetation state and wild/restoration processes. The proposed new layer should own institutional living-collection identity and custody.

## Existing repo boundaries checked

- `flora-pollination-seed-dispersal-layer.md`: vegetation units, seed sources, dispersal, recruitment, restoration, plant-Pokémon associations.
- `museums-collections-exhibitions-conservation-layer.md`: accession and stewardship of collection objects, including replicas and loans; living plants need different lifecycle semantics.
- `conservation-protected-areas-stewardship-layer.md`: conservation objectives and protected sites.
- `conservation-genetics-population-diversity-layer.md`: population-level diversity and founder/bottleneck questions.
- `biosecurity-introduced-species-translocation-layer.md`: movement, establishment and introduced-status assessment.
- `taxonomy-species-classification-nomenclature-layer.md`: taxonomic identity and revision history.
- `research-ethics-consent-subject-protection-layer.md`: research authorization and sampling boundaries.
- `technology-energy-infrastructure-layer.md`: greenhouse climate-control, irrigation, refrigeration and monitoring hardware when authored.
- `supply-chains-procurement-inventory-layer.md`: physical movement/storage of material in transit.
- `working-pokemon-institutional-roles-layer.md`: voluntary Pokémon participation in institutional work.

No existing file in the complete design tree is dedicated to botanical-garden living accessions, seed-bank lots or institutional horticultural continuity.

## New external sources

### Botanic Gardens Conservation International — PlantSearch and accessioning

BGCI PlantSearch connects accession-level information from living/viable plants, seeds, pollen and tissues across botanical institutions. BGCI explicitly emphasizes that useful living collections depend on documentation and accession-level data rather than only a taxon list.

Useful abstractions for Ouros:

- accession identity should survive propagation, movement and staff turnover;
- taxon identity and accession identity are different;
- provenance can be wild-origin, garden-origin, derived or unknown;
- stocktaking and deaccession are normal collection operations;
- collection value depends partly on information associated with the material;
- duplicate holdings across institutions can provide continuity without creating a single central collection.

Sources:
- https://www.bgci.org/resources/bgci-databases/plantsearch/
- https://www.bgci.org/news-events/new-guide-to-accessioning-living-collections-published/ — published 2026-08-20.
- https://www.bgci.org/news-events/plantsearch-accessions-is-now-available/ — published 2026-07-23.
- https://www.bgci.org/resources/bgci-databases/plantconnect/

Do not import real-world compliance rules, conservation law, international exchange restrictions or institutional terminology as Ouros law.

### Cambridge University Botanic Garden — living collections as long-lived curated systems

Cambridge treats living collections as a dynamic resource for research, education and conservation. Its strategy tracks qualities including wild origin, provenance, duplication, longevity and sustainability. Its 2026 Living Collections Manual explicitly frames collection management as a continuous institutional process from acquisition through ongoing management and utilization.

Useful abstractions:

- a living collection changes while retaining historical identity;
- horticultural care, curation and recordkeeping are different jobs;
- duplicate material can be strategically useful;
- a plant can remain alive while its label, taxonomic determination or curatorial purpose changes;
- collection strategy can change over decades without rewriting accession history;
- public display is only one possible use of a living accession.

Sources:
- https://www.botanic.cam.ac.uk/cambridge-university-botanic-garden-produces-its-first-ever-living-collections-strategy/
- https://www.botanic.cam.ac.uk/collections/living-collections/living-collections-manual/ — published 2026-03-04.
- https://www.botanic.cam.ac.uk/collections/collectionsportal/
- https://www.botanic.cam.ac.uk/collections/

### Seed collections and viability

Botanical institutions may keep seeds as a separate ex-situ collection supporting propagation, backup and conservation. Stored seed remains a biological sample with provenance and changing viability rather than an infinitely stable inventory item.

Useful abstractions:

- seed bank accession and living display specimen may share ancestry but are separate holdings;
- one seed lot can be split among institutions while retaining provenance links;
- viability checks are observations at a point in time, not permanent guarantees;
- germination success does not prove successful establishment in the wild;
- a failed germination test does not automatically prove every seed in the accession is nonviable;
- collection restrictions or provenance conditions should propagate to derivatives when Ouros canon defines such restrictions.

Source:
- Denver Botanic Gardens Living Collections Strategy: https://www.botanicgardens.org/sites/default/files/file/2022-12/2021LivingCollectionsStrategy100521.pdf

## Pokémon-world precedents

### Florges — authored garden relationship, not a generic healing system

Official Pokédex material states that Florges creates impressive flower gardens in its territory and includes folklore that such gardens can heal body and spirit.

Reusable structure:

A persistent individual can become associated with a cultivated landscape strongly enough that the garden has public memory, caretaking practices and local stories around it.

Guardrail:

The healing statement is species lore and folklore. It does not authorize a universal greenhouse healing zone, HP recovery, status removal or Care effect in Ouros. Any battle effect must come from exact PTU/Caelo/AutoPTU mechanics.

Source:
- https://www.pokemon.com/us/pokedex/florges

### Eldegoss — seed dispersal without institutional authority

Official Pokédex material states that Eldegoss spreads nutritious seeds on the wind.

Reusable structure:

A botanical institution can observe seed movement by a persistent Pokémon and later investigate whether a new patch derives from known accessions or from surrounding wild vegetation.

Guardrail:

Observed dispersal does not authorize staff to treat those seeds as accessioned material, infer parentage, create propagation success, manipulate spawns or claim that Eldegoss performs institutional seed banking.

Source:
- https://www.pokemon.com/us/pokedex/eldegoss

### Flabébé / Flower Veil boundary

Official Pokédex material links Flabébé to preferred flowers and exposes Flower Veil as a defined Ability.

Reusable structure:

A specific Pokémon may have a long-lived relationship with one cultivated plant or bed, creating an observation history around both.

Guardrail:

Flower Veil is a battle Ability with a defined scope. It is not plant health, frost protection, greenhouse protection, conservation status or a passive environmental shield.

Source:
- https://www.pokemon.com/us/pokedex/flabebe

### Combee / Honey Gather boundary

The PTU project data contains Honey Gather as a named mechanic. Botanical abundance must not turn that exact mechanic into a generalized honey-production simulator.

Project evidence:
- AutoPTU contains PTU/ability data entries for Honey Gather and Combee.

Guardrail:

A nectar-rich collection does not itself create Honey, increase Honey Gather frequency, increase crop yield or change encounter rarity.

## PTU community / campaign design source

A public PTU campaign framework in the Something Awful `Fight Clans` thread includes a player-base `Garden` facility that allows Apricorns/Berries to be planted and later expanded. This is homebrew campaign infrastructure, not PTU core law.

Reusable structure:

- player investment can turn a base into a recurring productive/cultural location;
- facilities can create new downtime loops and callbacks;
- the same physical garden can matter to economy, relationships and exploration without needing a combat encounter every visit.

Guardrail:

Do not import its costs, tree limits, ranks, yields, loyalty effects or facility progression.

Source:
- https://forums.somethingawful.com/showthread.php?threadid=3652290

## Design lessons for Ouros

1. Preserve accession identity separately from plant taxon identity.
2. Preserve provenance even when the plant is propagated many times.
3. Keep living specimens, seed lots, pollen/tissue samples and preserved vouchers as distinct objects with handoffs to the correct subsystem.
4. Let institutional collections change purpose across decades: research, display, conservation backup, teaching, restoration source, heritage.
5. Treat duplicate holdings as a network rather than a magical backup flag.
6. Make loss possible without erasing history: a living specimen can die while its accession record, descendants, samples and photographs remain.
7. Treat viability, successful germination and successful field establishment as separate findings.
8. Keep public labels separate from current taxonomic/curatorial interpretation.
9. Keep visitor popularity separate from conservation value.
10. Let routine horticulture compress into Chronicle unless an anomaly, choice, relationship or long-term consequence makes it playable.
11. Do not make every rare plant a quest or every greenhouse a dungeon.
12. Never use Minecraft block duplication/growth as accession propagation authority.

## Candidate Ouros system handoffs

- wild collection event -> Flora / Conservation / Biosecurity / Research Ethics
- accession creation -> Botanical Collection layer
- taxonomic update -> Taxonomy
- greenhouse utility state -> Technology / Water Service
- seed shipment -> Supply Chains / Postal
- duplicate holding -> Botanical Collection network
- seed viability observation -> Science / Metrology
- public display -> Tourism / Education / Public Memory
- preserved voucher -> Museums / Archives
- restoration release -> Conservation / Flora
- live Pokémon participation -> Pokémon Agency / Working Pokémon

## Mechanical boundary

Do not infer any of the following from a botanical collection:

- Grassy Terrain;
- plant HP or cover;
- healing from gardens;
- pollen Status effects;
- Honey production;
- Berry yield modifiers;
- Naturewalk;
- Flower Veil protection of plants;
- Seed Sower environmental state;
- growth timers based on Minecraft ticks;
- greenhouse temperature damage;
- automatic Fire weakness of the site;
- Grass-type encounter bonuses;
- capture bonuses;
- restored population success from germination alone.

## Caelo / helper status

No reliable primary Caelo source defining botanical-garden accessioning, seed banking, institutional horticulture or ex-situ conservation was recovered in this run.

Super PTU Online Helper was not exposed as an invocable capability. No output is invented or attributed to it.
