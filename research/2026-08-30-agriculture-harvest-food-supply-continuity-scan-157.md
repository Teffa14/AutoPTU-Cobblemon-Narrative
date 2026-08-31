# Research Scan — Agriculture, Harvest & Food-Supply Continuity — Pass 157

Status: PROVENANCE / NON-CANON RESEARCH. This file records external inspiration and design extraction. It does not establish Ouros canon.
Date: 2026-08-30

## Research question

How can Ouros make farms, orchards, ranches, berry plots, food processors, storehouses and seasonal supply feel like persistent parts of a living region without inventing a universal farming simulator, food law, domestication rule or Pokémon labor system?

The target gap is continuity between production planning, seasonal work, cultivation or husbandry, harvest, post-harvest handling, storage, processing, distribution and recovery after disruption. Existing Ouros layers already own material identity and provenance, ecology, weather, water and infrastructure, workplaces, markets, transport, care, investigations and tactical battle facts. This pass must preserve those authorities.

## Existing-repository gap check

The complete recursive repository tree was inspected before writing and returned without truncation. Focused searches for agriculture, farm, ranch, harvest, crop, orchard, food supply and related terms did not identify a dedicated longitudinal layer with this scope.

Adjacent authority remains separate:

- Material Culture owns item, batch, custody and provenance identity.
- Ecology, conservation, wildlife, water and weather systems own environmental observations and authored ecological facts.
- Infrastructure owns pumps, channels, roads, storage-support assets and service interruptions when those assets are already modeled.
- Workplace systems own staffing, assignments and ordinary work participation.
- Shops, markets and trade systems own transactions and market activity.
- Travel and transport systems own journeys and movement of shipments.
- Care owns illness, treatment and recovery facts.
- Investigation owns causal claims and hypotheses.
- AutoPTU owns tactical facts covered by verified BattleSpec mechanics.
- Minecraft/Cobblemon/Craftics owns presentation and playback only.

The missing layer is the history of production cycles and how food availability changes across stages without collapsing every problem into a single `HARVEST_FAILED` flag.

## Pokémon source patterns

### Jubilife Village farm — Pokémon Legends: Arceus

The Jubilife Village farm provides an unusually clear production loop. The player requests harvests, time or activity passes, and the farm later provides the resulting goods. Separate requests expand the available fields. One expansion uses a Ground-type Pokémon to help plow hard soil.

Reusable structures:

- productive capacity can change historically;
- a field exists before it produces a harvest;
- preparation, cultivation and harvest are separate moments;
- Pokémon can participate in work through a specific authored relationship rather than a universal species rule;
- production continues as ordinary settlement activity between adventures.

Ouros adaptation: record a production site, a cycle, participants, known inputs and an eventual harvest event. Do not infer that every Ground-type Pokémon can plow, that a borrowed Pokémon is owned by the farm, or that a type creates generic labor output.

Source: Bulbapedia, Pokémon Legends: Arceus walkthrough, Request 27 “Help Wanted: Plowing the Fields”; Jubilife Village farm / Colza. Public reference consulted 2026-08-30.

### Kalos Berry fields — Pokémon X/Y

The Berry fields show cultivation as repeated care rather than a one-click resource node. Planting, watering, weeds, hungry Bug Pokémon, compost/mulch and adjacent plantings can affect the production loop. A scientist later studies observed mutations.

Reusable structures:

- cultivation has a history of interventions and observations;
- pests or wildlife can become a production pressure without being villains;
- an unusual result can become a scientific lead rather than instant supernatural lore;
- local production can depend on imported varieties without making the whole system self-sufficient.

Ouros adaptation: preserve interventions and observed outcomes, but never import Pokémon X/Y growth timers, mutation recipes, mulch formulas or species behavior as Ouros rules unless separately approved.

Source: Bulbapedia, Pokémon X and Y walkthrough, Berry fields. Public reference consulted 2026-08-30.

### Moomoo Farm and Paniola Ranch

Moomoo Farm connects a working farm, a sick Miltank, care and a product sold after recovery. Paniola Ranch presents fenced paddocks and Pokémon associated with ranch work and local production.

Reusable structures:

- individual animal/Pokémon health can affect a workplace or household without proving a region-wide shortage;
- production sites can have ordinary routines, caretakers and products long before a quest occurs;
- the same Pokémon species can exist both in managed settings and elsewhere in the wild;
- care, ownership, work role and species ecology remain separate facts.

Ouros adaptation: a ranch can remember which individual Pokémon participates in which role, who cares for it and what production episode was affected. No universal domestication status follows from species alone.

Sources: Bulbapedia, Moomoo Farm; Paniola Ranch. Public references consulted 2026-08-30.

## Food-loss and supply-chain source patterns

### FAO food-loss stage separation

The Food and Agriculture Organization describes food supply through distinct stages including harvest, on-farm post-harvest handling, transport and storage. FAO material also emphasizes that significant loss can happen after a crop has successfully been harvested.

This distinction is highly reusable for Ouros because many narratives incorrectly call every shortage a crop failure.

Reusable sequence:

PRODUCTION -> HARVEST -> ON-SITE HANDLING -> STORAGE/PROCESSING -> TRANSPORT -> MARKET OR USE

A disruption can occur at any stage.

Ouros adaptation: treat this as process grammar only. Do not import real-world loss percentages, agricultural standards, laws, food-safety regimes or technical prescriptions.

Sources: FAO Technical Platform on Food Loss and Waste, FLW Database User Guide; FAO material on economic aspects of post-harvest losses. Public references consulted 2026-08-30.

## PTU community cross-check

Public PTU community discussions repeatedly note that the system’s tactical combat can become lengthy as the number of actors rises. This is useful design evidence for a rural/economic layer: farms and supply chains should create many meaningful scenes that are social, investigative, logistical or environmental, with combat reserved for cases where tactical conflict genuinely matters.

A contemporary GM discussion also recommends open-ended campaign structures where small hooks can expand if players engage with them. Agriculture supports this well because ordinary work can reveal ecology, local relationships, supply pressure, infrastructure dependencies or faction interests without demanding a predetermined main quest.

These community discussions are campaign-practice evidence only. They do not establish PTU mechanics.

Sources: r/PokemonTabletop public discussions on large-party combat and first-time campaign design. Public references consulted 2026-08-30.

## Design extraction for Ouros

### Production and availability require separate state

A good harvest can still fail to reach consumers because storage, processing or transport failed.

A weak harvest does not automatically create a shortage if reserves, substitution or imports cover demand.

A storehouse can be full while a settlement experiences poor access because the route or distribution contract is interrupted.

Therefore production output, stored quantity claims, release/distribution state and local availability should remain separate records.

### Estimates remain claims until measured

Farmers, traders, inspectors and residents can make yield estimates. Those statements should retain speaker, method, date and scope.

An expected bumper crop can later become an ordinary harvest without anyone having lied.

### Seasonal pressure does not equal disaster

A seasonal gap can be routine. A late harvest can be inconvenient. A failed batch can matter to one household. Regional crisis requires evidence of wider consequence.

The system should support ordinary variation so that genuine emergencies feel different.

### Pokémon labor must be explicit and individual

A Pokémon may help plow, herd, carry, locate pests, protect a field or participate in another job when an authored relationship and approved mechanics support that fact.

Species, type or Pokédex flavor alone cannot grant a universal labor capability.

Work participation does not transfer ownership, erase agency or make the Pokémon a BattleSpec combatant.

### Post-harvest history creates strong mysteries

A batch can be harvested successfully and later spoiled, mixed, mislabeled, delayed, damaged or diverted. Material Culture should retain batch identity/provenance while this layer records the production and supply episode.

This supports mysteries where several witnesses honestly say “the harvest was fine” while market shelves are still empty.

## Reusable quest structures

### Five meanings of “the harvest failed”

One speaker means low field yield. Another means produce spoiled before storage. A merchant means the shipment missed its market window. A household means the usual product was unavailable. A processor means one input lot failed quality review.

The investigation resolves scope and stage rather than selecting a single liar.

### The full storehouse

A settlement reports scarcity while a nearby storage building remains visibly full. Possible explanations include reserved stock, inaccessible custody, a distribution interruption, unsuitable contents, an outdated inventory claim or a different owner. None should be assumed in advance.

### The quiet harvest

A no-combat episode follows an ordinary harvest day. The player learns names, routes, work rhythms, care relationships and normal output. Months later those established facts make a disruption legible without exposition.

### The weather everyone blamed

A poor market week is publicly attributed to weather. Investigation may confirm field damage, find post-harvest loss, discover transport delay, or conclude that several small causes combined. Weather remains an observed event rather than an automatic causal verdict.

### The temporary substitute

A shortfall changes what a town cooks, sells or trades for one season. Some substitutions disappear after recovery; others become culturally persistent. The system records adoption history without declaring that temporary emergency food instantly became ancient tradition.

## Environmental-storytelling seeds

- an orchard has old rows, newer replacement rows and one deliberately retained tree;
- a granary has repair marks from several storage eras;
- a farm road shows heavier seasonal wear than nearby residential lanes;
- irrigation markers remain after the source route changed;
- market signage lists a local product that has not been locally produced for years;
- a ranch keeps work equipment sized for Pokémon no longer present there;
- field notebooks show expected and actual harvest dates across decades;
- a packing shed contains labels from several destination markets;
- a village festival uses preserved food from a prior season because the fresh crop is not ready yet.

## Hard provenance safeguards

`YIELD_ESTIMATE != HARVESTED_AMOUNT`

`HARVESTED != SAFE_OR_USABLE`

`HARVESTED != DISTRIBUTED`

`STORED != AVAILABLE_TO_PUBLIC`

`CROP_FAILURE != SHORTAGE`

`SHORTAGE != FAMINE`

`WEATHER_EVENT != CROP_FAILURE`

`PRODUCTION_RESTORED != PRICE_NORMALIZED`

`FOOD_AVAILABLE_REGIONALLY != AVAILABLE_IN_EVERY_SETTLEMENT`

`ONE_BAD_SEASON != PERMANENT_ECOLOGICAL_CHANGE`

`POKEMON_PRESENT_ON_FARM != FARM_OWNED`

`POKEMON_WORK_ROLE != UNIVERSAL_SPECIES_CAPABILITY`

`BATTLE_WON != HARVEST_SAVED`

`IRRIGATION_ACCESS_CLEAR != WATER_DELIVERED`

## PTU/Caelo assumptions that remain UNKNOWN

This scan found no project-approved basis for silently creating:

- a universal farming subsystem;
- crop growth timers or yield formulas;
- generic food-consumption or starvation rules;
- universal domestication status by Pokémon species;
- automatic ranch ownership of resident Pokémon;
- generic plowing, pollination, herding, harvesting or processing capability from type or flavor text;
- universal pest mechanics;
- generic soil fertility statistics;
- crop disease simulation;
- universal irrigation rules;
- food-safety checks or inspection regimes;
- generic spoilage percentages or shelf-life rules;
- universal market-price changes from harvest state;
- Trainer Skill checks that automatically determine crop yield, food safety or causal truth;
- Moves, Abilities or Trainer Features that alter agricultural output without individual source verification.

Any exact PTU/Caelo Skill, Move, Ability, Item or Trainer Feature proposed for agricultural work must be checked individually before canon approval and, if tactical, against current AutoPTU contracts.

## Candidate scope for Pass 157 design

The design layer should own persistent continuity records for production sites, production cycles, harvest episodes, post-harvest handling, storage availability claims, production dependencies, distribution-release state, losses, substitutions and recovery.

It must leave item/batch identity to Material Culture, environmental truth to the relevant environment systems, infrastructure operation to Infrastructure, employment to Workplaces, commerce to Markets, tactical outcomes to AutoPTU and presentation to Minecraft/Cobblemon/Craftics.