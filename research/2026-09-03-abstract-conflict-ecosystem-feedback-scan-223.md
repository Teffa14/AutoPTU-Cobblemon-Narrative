# Abstract conflict, selective pressure and ecosystem feedback scan — pass 223

Status: RESEARCH / PROVENANCE, NON-CANON
Date: 2026-09-03

## Research question

Pass 222 added dynamic demography, but the world also needs ecological experience and conflict pressure. Wild Pokémon can fight Trainers, compete with other wild Pokémon, prey on each other, survive repeated conflict, be captured, relocate, and change the habitat around them. Most of those off-screen interactions must be resolved as population/world simulation rather than thousands of hidden AutoPTU battles.

The design target is an ecological causal model:

```text
population composition
+ species relations
+ resources
+ Trainer battle/capture pressure
+ abstract wild conflict/predation
+ season/migration
+ management response
-> abundance + strength distribution + behavior + habitat impact
-> later visible world evidence
```

No research source below is treated as Pokémon canon or as a PTU mechanical rule. It only supports reusable ecological structure.

## 1. Predation changes both abundance and behavior

Predator-prey ecology distinguishes consumptive effects from non-consumptive effects. Predators can reduce prey abundance, but predator risk can also alter movement, foraging and habitat use. Those responses can propagate to vegetation and other trophic levels.

Reusable Ouros lesson:

- predation pressure must not be only `prey_count - X`;
- prey can redistribute, reduce exposed activity or change site use under risk;
- those behavioral changes can alter resource pressure even before a kill occurs;
- predator/prey effects should be time- and context-dependent, not a permanent species-wide modifier.

Sources:

- Temporal Variation in Trophic Cascades, Annual Review of Ecology, Evolution, and Systematics 48 (2017): https://doi.org/10.1146/annurev-ecolsys-121415-032246
- Predator diversity dampens trophic cascades, Nature 429 (2004): https://doi.org/10.1038/nature02554

## 2. Population structure matters when members are selectively removed

Harvest/population-management literature shows that removing members from a structured population can alter age/stage composition and produce transient dynamics that differ from a simple reduction in total abundance.

Selective management literature also emphasizes that particular individuals can contribute disproportionately to conflict, while removing or relocating them can produce indirect population effects.

Reusable Ouros lesson:

- capture pressure is not just a count; which life stages/strength bands/behavioral types are repeatedly exposed to Trainers matters;
- removal of strong or conspicuous members can change the future strength distribution;
- removing a dangerous individual should not magically modify every member of its species;
- management should target real members or cohorts and preserve ledger conservation.

Sources:

- Control of structured populations by harvest, Ecological Modelling 196 (2006): https://doi.org/10.1016/j.ecolmodel.2006.02.012
- Ecology of Problem Individuals and the Efficacy of Selective Wildlife Management, Trends in Ecology & Evolution 32 (2017): https://doi.org/10.1016/j.tree.2017.03.011

## 3. Relocation/removal is not a free reset button

Human-wildlife conflict literature warns that translocation can move a problem rather than solve it, and that management effectiveness depends on species, behavior and local context. Non-lethal measures can be preferable in many real-world carnivore conflicts, but there is no universal intervention.

Reusable Ouros lesson:

A managed starter zone should not simply delete over-threshold Pokémon. Potential authority actions include monitoring, warning/closure, deterrence, route management, controlled relocation, escort or other canon-approved interventions. A relocated Pokémon becomes real ecological pressure somewhere else and keeps its identity/state.

Sources:

- IUCN SSC Guidelines on human-wildlife conflict and coexistence (2023): https://portals.iucn.org/library/sites/library/files/documents/2023-009-En.pdf
- Effectiveness of interventions for managing human-large carnivore conflicts worldwide, Science of the Total Environment 838 (2022): https://doi.org/10.1016/j.scitotenv.2022.156195

## 4. Animal abundance can visibly reshape vegetation and future habitat

Reviews of wild ungulate impacts show that browsing and trampling can alter tree regeneration, understorey composition, structure and longer-term forest trajectories. Effects depend on density and context and can have delayed or legacy effects.

Reusable Ouros lesson:

- ecosystem population state can drive persistent vegetation pressure;
- high pressure need not destroy adult trees immediately; it can first appear as fewer saplings, depleted fruit/forage, trail formation or shifted understorey;
- low/intermediate pressure can also create heterogeneity rather than a universal negative effect;
- landscape manifestation should use accumulated pressure and recovery windows rather than one battle creating a biome rewrite.

Sources:

- Effects of wild ungulates on the regeneration, structure and functioning of temperate forests: A semi-quantitative review, Forest Ecology and Management 424 (2018): https://doi.org/10.1016/j.foreco.2018.05.016
- Long-term effects of ungulate browsing on forest composition and structure, Forest Ecology and Management 258 (2009): https://doi.org/10.1016/j.foreco.2009.06.006

## 5. Design derivation: abstract conflict is not an off-screen PTU battle

Ouros needs a separate `ABSTRACT_ECOLOGICAL_CONFLICT` resolver.

It may estimate:

- encounter/conflict frequency;
- predation attempts and successful consumptive events;
- displacement/avoidance pressure;
- competition pressure;
- survivor exposure/progression pressure;
- injury/mortality risk only through an explicit world-level demographic contract;
- habitat/resource disturbance.

It must never invent:

- Move selection;
- initiative order;
- exact HP damage;
- Status Afflictions;
- Ability triggers;
- Items used;
- Trainer Features;
- exact tactical positions;
- a fabricated AutoPTU winner/loser log.

An abstract predation event can author `one anonymous prey member was consumed during this demographic window` when the ecological model resolves that transition. It cannot claim `Move X dealt Y damage and caused Status Z`.

## 6. Design derivation: battle pressure can shift wild strength

The requested game-world rule is stronger than ordinary real-world demography and is therefore Ouros-authored game ecology, not an inference from wildlife literature.

The causal chain can be:

```text
actual resolved Trainer battles
+ estimated wild-vs-wild conflict exposure
+ estimated predator/prey conflict exposure
+ survival/opportunity/resources
-> population combat-exposure pressure
-> gradual shift in population strength distribution
```

Do not use `battle_count * fixed XP = hidden fake battles`.

Instead retain a population-level progression signal such as `combat_exposure_pressure` and resolve bounded changes to a strength distribution once per world window. Persistent individuals can retain their own exposure history where relevant.

The eventual mapping from population strength state to legal PTU Level must be a separate audited generation/progression contract. Pass 223 does not invent PTU XP arithmetic.

## 7. Managed starter-zone paradox

Starter zones should deliberately support:

- high encounter availability;
- high legitimate Trainer battle volume;
- many lower/ordinary-strength wild members;
- enough turnover/recruitment to keep beginner activity available;
- low probability of unmanaged dangerous individuals remaining near children and beginners.

Without management, high battle exposure can make survivor strength drift upward. Therefore safe starter zones require active world institutions rather than static encounter tables.

Possible causal stabilizers:

```text
high battle volume -> strength pressure upward
captures -> real removals
recruitment/immigration -> younger/lower-strength entrants
routine dispersal -> members leave naturally
authority surveillance -> dangerous outliers detected
targeted management -> outlier relocated/deterred/access restricted
```

This preserves both player-facing battle density and ecological continuity.

## 8. World manifestation channels

The abstract simulator should write semantic world state that other systems can render or observe:

```text
POPULATION_STATE
STRENGTH_DISTRIBUTION
PREDATION_PRESSURE
CAPTURE_PRESSURE
CONFLICT_PRESSURE
BEHAVIOR_PRESSURE
RESOURCE_PRESSURE
VEGETATION/HABITAT_PRESSURE
MANAGEMENT_STATE
```

Possible manifestations:

- NPC observations, rumors, field reports and warnings;
- changed wild tolerance/wariness/activity windows;
- changed predator/prey spatial overlap;
- depleted or recovering forage resources;
- browsed saplings or reduced tree recruitment;
- nesting/territorial concentration;
- tracks, trails and disturbed ground;
- temporary route closure or patrol presence;
- relocation events that create pressure in a neighboring ecosystem;
- later quests whose cause can be investigated from accumulated evidence.

Characters should infer these states from evidence unless their institution has legitimate access to authoritative monitoring.

## Research boundary

This scan supports the architecture only. It does not canonize predator-prey pairs, starter-zone jurisdiction, numerical risk thresholds, PTU Level formulas, species diets, tree species, or authority intervention procedures in Marea.