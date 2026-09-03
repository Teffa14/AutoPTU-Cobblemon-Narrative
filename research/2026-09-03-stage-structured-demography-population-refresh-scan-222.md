# Stage-structured demography and population refresh scan — pass 222

Status: RESEARCH / PROVENANCE, NON-CANON
Date: 2026-09-03

## Research question

Pass 221 established finite ecosystem populations and conservation-preserving Cobblemon projection. This pass asks the next necessary question: how should that finite population change through time as members reproduce, mature, die, are captured or released, and move seasonally between habitat patches and ecosystems?

The goal is a balanced, persistent demographic cycle. The goal is not a fixed population number, an invisible replacement-respawn system, or per-Minecraft-tick simulation of every off-screen animal.

## Internal continuity

This scan extends `design/ecosystem-population-authority-v1.md` rather than replacing it.

Existing invariants remain:

- Cobblemon spawn/despawn is projection, not demography;
- bait changes detectability/redistribution, not population totals;
- a persistent wild identity consumes exactly one population membership;
- ecosystem ownership changes only through explicit authoritative transitions;
- Minecraft biome boundaries are not automatically ecosystem boundaries;
- observations by characters remain separate from population ground truth.

Passes 216, 218, 219, 220 and 221 already provide temporal ecology, migration, dependent sites, provisioning and finite-population authority. This scan only adds the demographic lifecycle that was intentionally left unresolved.

## Public research findings

### 1. Density dependence should constrain recruitment and survival, but a single logistic curve is too crude

Wildlife-management literature treats density dependence as an important regulator of population growth. Empirical work also shows that the simple logistic model is only an approximation and that effects can appear through different vital rates rather than one universal multiplier.

Recent conservation synthesis likewise warns that both negative density dependence at high abundance and positive density dependence at very low abundance can matter. Very small populations can have reduced reproduction or survival because mating, cooperative defense or other processes break down.

Reusable Ouros lesson:

- do not enforce a magical fixed `K` by deleting or spawning Pokémon;
- derive pressure from food, water, shelter, nesting/breeding sites, space, disease/competition context and disturbance;
- let pressure affect specific demographic processes such as recruitment, juvenile survival, dispersal or breeding opportunity;
- allow very small populations to be fragile instead of automatically rebounding to a target number.

Sources:

- Guthery, F.S. & Shaw, J.H. (2013), “Density dependence: Applications in wildlife management,” *Journal of Wildlife Management* 77:33–38. DOI: https://doi.org/10.1002/jwmg.450
- Mills, L.S., Whiteley, A.R. & Tourani, M. (2025), “Density-dependent population change,” in *Conservation of Wildlife Populations*, 3rd ed., Oxford University Press. DOI landing page: https://doi.org/10.1093/oso/9780192898166.003.0007
- Accolla, C. et al. (2024), “Density-dependent population regulation in freshwater fishes and small mammals,” *Integrated Environmental Assessment and Management*. DOI: https://doi.org/10.1002/ieam.4845

### 2. Demography should be stage-structured

Population response commonly differs by age/life stage. Reviews of density dependence report effects on age of first reproduction, juvenile survival, reproductive rate and dispersal rather than one identical effect on every member.

Reusable Ouros lesson:

Anonymous population state should preserve at least the life-stage distinctions that materially affect reproduction, survival and movement. A juvenile becoming an adult is a state transition, not a population increase.

Biological maturation must remain distinct from PTU Level and from Pokémon Evolution. A Pokémon can get older without gaining combat Levels, and a Level increase cannot silently advance biological age.

Source:

- Bonenfant, C. et al. (2009), “Empirical Evidence of Density-Dependence in Populations of Large Herbivores,” *Advances in Ecological Research* 41. DOI: https://doi.org/10.1016/S0065-2504(09)00405-X

### 3. Immigration, emigration and local reproduction must remain separate

Source–sink and metapopulation literature distinguishes reproduction/survival from movement between local populations. A habitat can appear to lose members because they emigrated rather than died; another can persist because immigration offsets poor local recruitment.

Reusable Ouros lesson:

The server must never infer death from disappearance. Cross-ecosystem movement and death are different events. Character-facing surveys can confuse them, but the canonical ledger cannot.

For migratory species, non-breeding stopovers can still be essential even though no reproduction occurs there. Seasonal ownership and transit therefore need explicit semantics rather than treating every location as a breeding population.

Sources:

- Dias, P.C. (1996), “Sources and sinks in population biology,” *Trends in Ecology & Evolution* 11(8):326–330. DOI: https://doi.org/10.1016/0169-5347(96)10037-9
- Runge, J.P., Runge, M.C. & Nichols, J.D. (2006), “The Role of Local Populations within a Landscape Context: Defining and Classifying Sources and Sinks,” *The American Naturalist* 167(6). DOI: https://doi.org/10.1086/503531
- Erickson, R.A. et al. (2018), “Defining and classifying migratory habitats as sources and sinks: The migratory pathway approach,” *Journal of Applied Ecology*. DOI: https://doi.org/10.1111/1365-2664.12952

### 4. Seasonal processes should execute in sequence, not all at once

Ecological work on sequential density dependence shows that conditions in one part of the annual cycle can affect later survival or reproduction. Carry-over effects make a single simultaneous annual population formula misleading.

Reusable Ouros lesson:

Ouros should process demographic windows in authored order. A breeding pulse, juvenile maturation, dry-season resource deficit, migration departure and capture pressure do not have to happen in one calculation. Each transition can consume the state produced by the previous one.

Source:

- Norris, D.R. & Taylor, C.M. (2006/2007 review literature), “When density dependence is not instantaneous: theoretical developments and management implications,” *Ecology Letters*. PubMed: https://pubmed.ncbi.nlm.nih.gov/17979979/

### 5. Seasonal migration can itself be density-dependent and partial

Recent migration literature continues to show that resident/migrant proportions can vary rather than every member following one compulsory route. This supports a population model in which only some members transfer, while others remain resident or use another habitat patch.

Reusable Ouros lesson:

A `migration season` is not `move 100% of species X to biome Y`. Migration propensity belongs to the population/species/context model and can select a subset of eligible members.

Source:

- Liu, M. et al. (2025), “Seasonal density-dependence can select for partial migrants in migratory species,” *Ecological Monographs*. DOI landing page: https://doi.org/10.1002/ecm.70009

## Derived Ouros model

### Population accounting equation

Over an authoritative demographic interval:

```text
N(t+Δt)
= N(t)
+ confirmed_births_or_hatches
+ confirmed_immigration
+ confirmed_releases_or_introductions
- confirmed_deaths
- confirmed_captures
- confirmed_emigration
```

Maturation and movement among habitat patches inside the same ecosystem preserve `N`.

An atomic migration transfer preserves regional/metapopulation membership while changing ecosystem ownership.

### Hybrid identity model

Do not require every invisible wild Pokémon to be a fully materialized persistent actor.

Use:

- persistent individuals for actors with identity/history, tracked state or narrative relevance;
- anonymous demographic cohorts for the rest;
- projection reservations to materialize members without creating new ones.

Candidate cohort dimensions should stay minimal and source-driven:

```text
species/form
life_stage
current_ecosystem
habitat_patch_affinity or seasonal location class when needed
breeding_eligibility when needed
count
```

Do not add sex ratios, family groups, genetics or exact birthdays unless a species/source/quest requires them.

### Biological growth is not PTU progression

Keep separate clocks/contracts for:

```text
chronological age / life stage
PTU Level / XP progression
Evolution eligibility/state
physical growth if species/source requires it
```

A demographic tick can mature a juvenile cohort while leaving PTU Level unchanged. Conversely, battle/training progression can raise Level without moving a Pokémon into another biological stage.

### Resource-limited recruitment

Candidate recruitment inputs:

```text
species reproduction profile (source-backed)
breeding window / season
eligible breeding population
resource sufficiency from source-backed diet + ecosystem resources
suitable dependent/nesting sites when relevant
density pressure
recent disturbance
juvenile survival pressure
migration/residency state
```

No input alone guarantees births.

`food exists` must never become `spawn babies`.

### Dynamic effective capacity

Avoid a single immutable carrying-capacity integer.

Candidate derived state:

```text
effective_capacity_pressure
resource_pressure_by_type
space/shelter pressure
dependent-site pressure
disturbance pressure
competition/predation/disease pressure when authored and evidenced
```

This state can influence vital rates. It cannot directly delete or add members to force the ledger toward a target.

### Stable simulation cadence

Population demography should advance on coarse authoritative windows, not every Minecraft tick.

Possible cadence families, to be selected per species/ecosystem after source review:

- daily state bookkeeping for movement/presence only;
- seasonal breeding/recruitment windows;
- scheduled maturation checks;
- seasonal migration transfer windows;
- explicit real-time capture/release/death events;
- periodic resource-pressure reconciliation.

The runtime should use deterministic/seeded resolution or persisted transition results so multiplayer sessions cannot resolve the same demographic interval differently.

## Balance guardrails

1. No replacement respawn after capture.
2. No automatic return-to-target after mortality.
3. No exponential breeding without maturation delay, breeding windows and resource/density constraints.
4. No silent extinction prevention by fabricating immigrants.
5. No silent extinction caused by chunk unloading or low detectability.
6. No double counting during migration.
7. No migration caused merely by crossing a Minecraft biome boundary inside one ecosystem.
8. No biological maturation inferred from PTU Level alone.
9. No PTU Level gain inferred from biological age alone.
10. No ecosystem population growth from bait, spawn weights, time-of-day eligibility or observation frequency.

## Narrative opportunities

A dynamic population cycle creates stories that a fixed count cannot:

- a strong breeding year can be followed by poor juvenile survival;
- capture pressure can change age structure before characters notice a total decline;
- a population can appear to recover because immigrants arrive while local recruitment remains poor;
- a seasonal resource shift can move members among habitat patches without changing ecosystem abundance;
- an ecosystem can become a temporary sink while a neighboring source supports it;
- a familiar persistent individual can mature while retaining identity without automatically leveling;
- conservation or access decisions can improve one demographic bottleneck while exposing another.

## Canon status

All structures in this scan are PROPOSED / NON-CANON until explicitly promoted. No Marea population number, species breeding rate, lifespan, life stage, migration fraction or carrying capacity is assigned here.