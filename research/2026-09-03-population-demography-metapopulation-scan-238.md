# Population, demography and metapopulation scan — Pass 238

Status: RESEARCH / PROVENANCE
Date: 2026-09-03
Scope: Ouros ecology program Pass 238

## Question

What population model can Ouros use so that wild Pokémon abundance changes through explicit demographic processes rather than through spawn counts, elapsed time or habitat-health shortcuts?

This note is research. It does not change canon by itself.

## Repository context checked before research

The active directive is `design/ecology-development-program.md`. Pass 238 owns population/demography. The prior recovery contract explicitly reserves population arithmetic for Pass 238 and states that habitat recovery must not refill population abundance automatically.

The first canon wild population remains `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`. Its visible deterministic actor is an implementation slot, not an abundance measurement. Redline remains a separate named persistent individual.

The Ouros authority policy remains unchanged: Ouros owns ecological and population truth; Minecraft/Cobblemon projects visible state; AutoPTU adjudicates structured mechanics only after explicit handoff.

## New source findings

### 1. Population change needs separate vital-rate channels

USGS work on structured population dynamics explicitly models abundance together with recruitment, immigration, stage-specific survival and detection. This is useful for Ouros because visible encounters are an observation process, not population arithmetic.

Source:
- Campbell Grant et al. (2014), “Modeling structured population dynamics using data from unmarked individuals”, USGS / Ecology.
- https://www.usgs.gov/publications/modeling-structured-population-dynamics-using-data-unmarked-individuals

Reusable lesson:

```text
observed_count != true_abundance
recruitment != immigration
survival != persistence_of_visible_entity
```

Ouros should track demographic channels separately enough that later observation systems can remain uncertain without corrupting ground truth.

### 2. Recruitment from reproduction and recruitment from immigration are mechanically different causes

Nichols and Pollock describe recruitment as having at least two conceptually distinct sources: immigration and in-situ reproduction. Those causes produce different population dynamics and therefore should not be collapsed into one anonymous `+N` event.

Source:
- Nichols & Pollock (1990), “Estimation of recruitment from immigration versus in situ reproduction using Pollock's robust design”, USGS / Ecology.
- https://www.usgs.gov/publications/estimation-recruitment-immigration-versus-in-situ-reproduction-using-pollocks-robust

Ouros implication:

```text
BIRTH/LOCAL_RECRUITMENT
IMMIGRATION
EMIGRATION
ECOLOGICAL_MORTALITY
CAPTURE_REMOVAL
RELEASE/RETURN
```

should remain provenance-distinct demographic event families even when several events happen in the same update window.

### 3. Density dependence affects survival and recruitment, and its strength can vary by season

A full-annual-cycle black-duck model found density-dependent effects on survival and recruitment and showed that those effects vary by season and through time.

Source:
- Robinson, McGowan & Devers (2017), “Disentangling density-dependent dynamics using full annual cycle models and Bayesian model weight updating”, USGS / Journal of Applied Ecology.
- https://www.usgs.gov/publications/disentangling-density-dependent-dynamics-using-full-annual-cycle-models-and-bayesian

Ouros implication: do not use one global species carrying-capacity constant as the complete demographic law. Site quality, season, life stage, migration phase, resources and disturbance can change effective demographic pressure.

### 4. Habitat quality and abundance can recover on different schedules

Recovery studies show demographic performance can depend on site quality, climate and density. A habitat becoming usable again does not imply that local abundance instantly returns to its previous level.

Source:
- Bruggeman et al. (2015), “Dynamics of a recovering Arctic bird population: the importance of climate, density dependence, and site quality”, USGS / Ecological Applications.
- https://www.usgs.gov/publications/dynamics-a-recovering-arctic-bird-population-importance-climate-density-dependence-and

This directly supports the Pass 237 -> Pass 238 boundary.

### 5. Local extinction and recolonization are patch processes, not entity spawn/despawn events

Metapopulation evidence from the tidewater goby found different local extirpation and recolonization rates among habitat patches; larger patches had lower extirpation rates, and recolonization related to source-population context and distance.

Source:
- Lafferty, Swift & Ambrose (1999), “Extirpation and recolonization in a metapopulation of an endangered fish, the tidewater goby”, USGS / Conservation Biology.
- https://www.usgs.gov/publications/extirpation-and-recolonization-a-metapopulation-endangered-fish-tidewater-goby

Ouros implication: local populations can reach zero while the regional species remains extant. Recolonization needs a plausible source and connectivity path. A generic Cobblemon spawn is not proof of either.

### 6. Environmental stochasticity and landscape heterogeneity affect viability

USGS multi-population viability work shows extinction risk depends on environmental stochasticity, habitat conditions and pressures that can lower carrying capacity. This supports explicit uncertainty and multi-site demographic histories instead of deterministic refill rules.

Source:
- Leasure et al. (2019), “Hierarchical multi-population viability analysis”, USGS / Ecology.
- https://www.usgs.gov/publications/hierarchical-multi-population-viability-analysis

The project does not need a full conservation PVA solver for ordinary gameplay. The reusable design lesson is that population trajectories should preserve causes, patch context and uncertainty rather than forcing every population toward a fixed target each tick.

### 7. Spatial encounter histories can inform density without becoming truth automatically

Spatial capture-recapture research uses encounter histories to estimate density, movement, resource selection and landscape connectivity. For Ouros this is a strong model for the later observation/research system: sightings can update knowledge without directly writing population truth.

Source:
- Royle, Fuller & Sutherland (2017), “Unifying population and landscape ecology with spatial capture-recapture”, USGS / Ecography.
- https://www.usgs.gov/publications/unifying-population-and-landscape-ecology-spatial-capture-recapture

### 8. Pokémon precedent: outbreaks represent unusual concentration/availability, not a general demographic law

Pokémon Legends: Arceus and its Daybreak update expose mass and massive mass outbreaks as unusual, investigable regional phenomena. This is useful presentation precedent but must not be treated as a literal birth burst.

Official source:
- Pokémon Legends: Arceus Daybreak update.
- https://legends.arceus.pokemon.com/en-gb/update/

Ouros interpretation:
- an outbreak may be caused by activity, aggregation, movement, migration, temporary resource response or true recruitment;
- the demographic cause must be authored separately;
- visible concentration must not implicitly manufacture population members.

### 9. PTU community practice favors authored ecological evidence over meaningless random encounters

Public PTU GM discussions recommend using habitat, tracks, territorial markings, behaviour and small authored wild situations rather than treating every route as a stream of unrelated random battles. Another exploration discussion describes wild Pokémon as active environmental actors with their own small interactions.

Sources:
- r/PokemonTabletop, “How do you plan your wild encounters?” (2020): https://www.reddit.com/r/PokemonTabletop/comments/jivcud
- r/PokemonTabletop, “Question for Exploration.” (2024): https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9

Reusable lesson: demographic changes should create visible evidence and encounter opportunities, but population arithmetic should remain independent of whether the player happens to trigger an encounter.

## PTU / Caelo / Kairos cross-check

The project-local Kairos index routes world population/ecosystem guidance to the Kairos core around pp. 437+ and encounter creation to pp. 470+. Kairos also demonstrates a living-world hunting workflow selected by region/biome/level range. These are useful operational references, but Kairos generation workflows do not authorize spawn generation to become Ouros population truth.

The existing canon Fletchling population cites Caelo as comparative evidence for ordinary route/urban Fletchling and territorial/diurnal behaviour. That remains comparative ecology evidence only. No Caelo or Kairos population arithmetic is adopted by this pass without explicit Ouros approval.

`SOURCE_HAS_RULE != OUROS_USES_RULE`

## Proposed high-level model

A local population should have a stable identity independent of visible entities.

Recommended state dimensions:

```text
population_id
species_id
site_or_patch_id
stage_counts
sex_or_breeding_class_counts_if_needed
known_persistent_individual_ids
unresolved_pool_count
local_capacity_context
resource_pressure
shelter_pressure
predation_pressure
disturbance_pressure
connectivity_state
last_demographic_tick
recent_demographic_events
```

A bounded update should resolve explicit events or pressures into auditable deltas:

```text
starting population
+ local recruitment
+ immigration
+ release/return
- ecological mortality
- emigration
- capture/permanent removal
= ending population
```

No term is inferred from Minecraft entity count.

## Stage structure

Do not require the same stage schema for every species. Minimum general categories can be:

```text
DEPENDENT_JUVENILE
INDEPENDENT_JUVENILE
SUBADULT_OR_PREBREEDER
BREEDING_ADULT
NONBREEDING_ADULT
```

Species ecology profiles can collapse or extend these categories. Eggs/nests remain distinct persistent records where reproduction requires them.

## Density and carrying context

Avoid a single hard `capacity` value as the only rule. Use an effective capacity context assembled from authored ecological state:

```text
base habitat suitability
+ current resource availability
+ shelter/nesting availability
+ seasonal context
+ competitor pressure
+ predator pressure
+ disturbance/recovery state
+ connectivity
= demographic pressure context
```

The resolver may use that context to reduce recruitment, increase dispersal pressure or modify mortality risk. It must not automatically kill or create members merely to force abundance back to a target.

## Local extinction and recolonization

`count == 0` can represent local extirpation without declaring species-wide extinction.

Recolonization requires an authored demographic path such as:
- immigration from a connected source population;
- return of known emigrants;
- release/relocation authorized by a world event;
- migration cohort settling and becoming resident.

A generic Cobblemon entity appearing at the site cannot satisfy this requirement.

## Observation boundary

Future Pass 240 should consume demographic truth through evidence and uncertainty:

```text
true population state
-> activity/exposure/projection
-> player/NPC observations
-> estimated abundance/confidence
```

Do not reverse that arrow merely because many entities are visible.

## Battle boundary

Most demographic updates require no battle engine.

A structured encounter can return semantic demographic effects after explicit resolution, for example:
- `CAPTURED_AND_REMOVED_FROM_LOCAL_POPULATION`
- `INJURED_BUT_REMAINS_RESIDENT`
- `FLED_LOCAL_PATCH`
- `RELEASED_TO_ORIGIN_PATCH`

Those outcomes must be produced by verified mechanics plus Ouros world policy. Minecraft death/despawn or visual retreat cannot author them.

## Status of conclusions

PROPOSED:
- event-ledger population arithmetic;
- stage-structured local populations;
- explicit immigration/emigration/recruitment/mortality channels;
- local extirpation/recolonization state;
- density/resource pressure as context, not automatic target refill.

UNCERTAIN:
- exact demographic time step for different species;
- exact breeding/stage schema per species;
- numeric density-dependence functions;
- which mortality sources resolve stochastically versus through authored events;
- how much individual identity is preserved in large populations.

CANON-APPROVED AND UNCHANGED:
- the first Sendero Fletchling population identity and species authorization;
- Ouros/Cobblemon/AutoPTU authority boundaries;
- Redline remains outside the wild population.

## Next design consequence

Pass 238 should now define a deterministic demographic event ledger and a Marea/Sendero fixture that proves:
- habitat recovery alone does not refill abundance;
- births and immigration are different causes;
- death and emigration are different causes;
- local count can reach zero without deleting the population record;
- recolonization requires a valid source/connectivity event;
- visible entity count never writes canonical abundance.
