# Conservation genetics, population diversity & recovery research — pass 143

Status: research/provenance only. Not Ouros canon.

## Why this pass

The repository already separates wild-population state, breeding/lineage, island biogeography, biosecurity, taxonomy, conservation, migration and research ethics. None of those layers should silently infer genetic health from visible abundance, pedigree, species rarity or Minecraft entity counts. This scan covers the missing bridge: population-level genetic evidence, founder effects, bottlenecks, gene flow and post-reintroduction monitoring.

The intended design rule is conservative: genetics can enrich long-running conservation stories, but it must never become a hidden purity score, breeding-value score or procedural justification for new forms/stats.

## Sources inspected

### Pokémon ecology precedent — Lapras population recovery

Bulbapedia preserves the Pokémon Moon Pokédex entry stating that Lapras had once been near extinction because of poaching and later became overabundant after protection. This is useful as a narrative structure because population recovery can overshoot or create new ecological pressures; conservation success is not equivalent to restoring one frozen historical number.

Source: https://bulbapedia.bulbagarden.net/wiki/Lapras_%28Pok%C3%A9mon%29

A current official Pokémon.com Lapras page was also checked for current species framing and abilities. It does not itself provide the historical near-extinction text in the rendered entry inspected here, so the population-history claim above is attributed to the preserved game Pokédex material rather than to the current page.

Source: https://www.pokemon.com/us/pokedex/lapras

Reusable Ouros lesson: a population can move through scarcity, protection, recovery and new management questions without changing the identity of the species or turning every individual into a conservation asset.

### PTU worldbuilding precedent — sensible ecosystems

The public PTU 1.05 GM material explicitly recommends balancing game progression with sensible ecosystems when populating a region. This supports population structure as worldbuilding context, not as permission to invent new combat mechanics.

Source: https://anyflip.com/qloz/xgfq/basic/401-450

The official Pokémon Tabletop site remains the public PTU resource index and states that PTU resources are rules/game material for GMs and players. External ecology sources therefore remain narrative/research references; PTU/Caelo remains the authority for mechanics.

Source: https://pokemontabletop.com/about/

### USGS — reintroduction can preserve or lose diversity

USGS work on Laysan teal shows that translocation itself can create a management-induced bottleneck because only a subset of a source population is moved. Genetic monitoring can test whether rare variants and diversity persist after reintroduction.

Sources:
- https://www.usgs.gov/publications/microsatellite-variation-and-rare-alleles-a-bottlenecked-hawaiian-islands-endemic
- https://www.usgs.gov/pacific-island-ecosystems-research-center/science/ecology-population-dynamics-and-translocation

Reusable Ouros lesson: `reintroduced_population_established = true` is insufficient. Source composition, follow-up sampling and multi-generation evidence may matter to long-term management.

### USGS — effective population size differs from headcount

A long-term Cumberland Island bobcat study found a small island population whose estimated effective breeding population was smaller than the abundance estimate, while much genetic diversity remained. This is a useful warning against equating census count, visible individuals and genetic diversity.

Source: https://www.usgs.gov/publications/population-and-genetic-outcomes-20-years-after-reintroducing-bobcats-lynx-rufus

Reusable Ouros lesson: use distinct fields for abundance estimates, sampled individuals, relatedness evidence and any population-genetic assessment. Never derive one directly from another.

### USGS — source choice, founder effects and later gene flow

American black bear reintroductions in the Central Appalachians demonstrate that small founder groups can create bottlenecks and that later immigration can alter the genetic trajectory of reintroduced populations.

Source: https://www.usgs.gov/publications/early-genetic-outcomes-american-black-bear-reintroductions-central-appalachians-usa

Reusable Ouros lesson: corridors and immigration can become important years after a release project. Road Ecology, Migration, Island Biogeography and Conservation can therefore affect later genetic assessments without granting any Pokémon a mechanical bonus.

### USGS — combine demographic and genetic monitoring

Brook trout reintroduction work emphasizes combining demographic and genetic data and monitoring more than one source population over time. A restored population can look successful demographically while genetic questions remain open.

Sources:
- https://www.usgs.gov/publications/using-genetic-data-advance-stream-fish-reintroduction-science-a-case-study-brook-trout
- https://pubs.usgs.gov/publication/70253898

Reusable Ouros lesson: survival, abundance, recruitment and genetic diversity are separate evidence channels. A successful release should not collapse them into a single `population_health` score.

### Historical samples can change the baseline

USGS ancient-DNA work on California condors illustrates how museum/historical samples can reveal diversity that is no longer visible in modern populations. This creates a useful handoff to Museums/Collections and Archives.

Source: https://www.usgs.gov/publications/ancient-dna-reveals-substantial-genetic-diversity-california-condor-gymnogyps

Reusable Ouros lesson: an old specimen can revise the inferred historical baseline without rewriting the historical population itself.

## Design conclusions

1. Species identity, individual identity, pedigree and population-genetic diversity must remain separate.
2. A bottleneck is an assessment derived from evidence, not a visual flag on a population.
3. Visible abundance can increase while effective breeding diversity remains limited.
4. A reintroduction can establish successfully while still requiring long-term monitoring.
5. Immigration/gene flow can change a population years after a release.
6. Historical samples can revise estimates of former diversity.
7. Conservation decisions should preserve uncertainty and competing management options.
8. Genetic evidence must not generate new Pokémon forms, Types, Abilities, stats, Natures, Moves, Egg Groups or evolutions.
9. Breeding mechanics from PTU cannot be extrapolated into Mendelian simulation for wild populations.
10. Loaded Cobblemon counts are never a genetic sample or population census.

## PTU/Caelo mechanical guardrails

The project-accessible public PTU material confirms explicit Breeding/Egg Group rules, but this pass found no project-authoritative rule that turns wild-population genetic diversity into combat stats, capture modifiers, breeding bonuses, encounter rarity or evolution changes.

The complete Caelo Player's Guide/rulebook/errata corpus was not recoverable through the available project sources during this run. Super PTU Online Helper was not exposed as an invocable capability. No Caelo-specific genetics rule is claimed.

Before any mechanics are attached to this layer, verify exact project sources for:
- Breeding and Egg Groups;
- offspring species and inheritance;
- Nature/Ability inheritance;
- Breeder/Hatcher/Researcher Features;
- capture/release/relocation rules;
- any Caelo population or conservation rules.

## Originality boundary

External conservation programs supply only abstract structures such as founder groups, monitoring, historical baselines and gene flow. Ouros institutions, populations, places, histories and conflicts must be original. Real endangered-species histories should not be reskinned one-to-one into fictional species narratives.