# Food Safety, Kitchen Operations & Traceability Research — Pass 136

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-23

## Why this pass exists

The existing Food, Agriculture & Hospitality layer already owns ingredients, cultivation, prepared dishes, recipes, venues and meal/service events. Supply Chains owns inventory and freight. Outbreak/Health Surveillance owns clusters of illness. Toxicology owns hazardous-agent exposure. Manufacturing owns repeatable production runs. None of those layers currently owns the operational chain inside a kitchen or food-service venue that answers:

- which physical ingredient lots entered a dish;
- what preparation steps actually occurred;
- what equipment/storage state mattered;
- which servings came from which preparation batch;
- what was held, discarded, withdrawn or recalled;
- how a venue narrows a suspected problem without declaring guilt or diagnosis.

Pass 136 therefore researches a narrow Food Safety / Kitchen Traceability authority that can connect those systems without duplicating them.

## Source scan

### Pokémon official — `A Recipe for Success!`

Source: https://www.pokemon.com/us/animation/seasons/22/episode-29-a-recipe-for-success

Useful structure:

- a restaurant runs out of a specific ingredient;
- staff source that ingredient from another location;
- an existing venue can become unexpectedly busy;
- preparation, customer service and ingredient supply are distinct pressures;
- Pokémon can participate in hospitality as actors rather than generic equipment.

Reusable Ouros lesson:

A kitchen can have service pressure without a combat problem. A shortage can be solved by sourcing, substitution or menu change. The event is still useful world state even if no illness occurs.

Do not copy characters, Tapu Koko reward, restaurant identity or episode plot.

### Pokémon official — `A Seasoned Search!`

Source: https://tv.apple.com/us/episode/a-seasoned-search/umc.cmc.6h4wotk4l5sbvmfkwaiknvcvy

Useful structure:

- a signature dish depends on a particular ingredient;
- substitution can fail for culinary reasons even when the substitute is available;
- ingredient ecology and sourcing can be part of the story;
- a successful recipe can become a seasonal menu item.

Reusable Ouros lesson:

Ingredient identity, culinary suitability, mechanical food definition and safety status are separate. A substitute can be safe and still be wrong for the dish. A rare ingredient can be narratively important without receiving a PTU bonus.

### Pokémon official — `Food Fit for a Kingambit!`

Source: https://www.pokemon.com/us/animation/horizons/2/food-fit-for-a-kingambit

Useful structure:

- menu design, dining experience, staff relationships and Pokémon behavior can all affect a venue;
- a restaurant problem does not need to be a contamination event;
- correcting service design can matter as much as changing the recipe.

Reusable Ouros lesson:

Food safety must not swallow the whole Hospitality layer. A bad service day, menu failure or Pokémon-specific accommodation is not automatically a safety incident.

### PTU community — restaurant/Gym hybrid

Source: https://www.reddit.com/r/PokemonTabletop/comments/qdus3t

The public PTU map discussion describes a Gym Leader who is also a chef and a restaurant that doubles as a Gym/event venue.

Reusable structure:

One physical venue can contain multiple institutional roles. Kitchen operations, public dining, competitive battling and spectators should remain separate authorities even when they share a building.

Do not import the region, Leader, city or event format.

### PTU community — Pokémon Center with kitchen/dining space

Source: https://www.reddit.com/r/PokemonTabletop/comments/mt1qo8

The public map treats a Pokémon Center as more than a healing counter and includes a small dining area and kitchen.

Reusable structure:

Food-service capability can exist inside clinics, stations, schools, shelters and other institutions without making each site a full restaurant. This is useful for emergency feeding, travel canteens and recovery facilities.

### PTU community — Chef mechanical boundary

Sources:

- https://www.reddit.com/r/PokemonTabletop/comments/lkp29b
- https://www.reddit.com/r/PokemonTabletop/comments/1ewm06f

These discussions reinforce that PTU Chef/Food Buff mechanics are specific mechanical contracts. Community answers about poisoning food also point toward separate Chemist/item mechanics rather than treating ordinary cooking as a generic debuff system.

Reusable guardrail:

A narrative cooking error, spoiled ingredient or suspicious dish must never invent Poisoned, Badly Poisoned, Food Buff removal, Digestion Buff behavior or a custom debuff. Mechanical effects require exact PTU/Caelo/AutoPTU validation.

### CDC — outbreak investigation requires multiple evidence streams

Source: https://www.cdc.gov/foodsafety/outbreaks/pdfs/outbreak-infographic.pdf

CDC separates epidemiologic evidence, traceback evidence and food/environmental testing. The source can remain unresolved even when an outbreak is real.

Reusable Ouros lesson:

A shared restaurant visit is an exposure opportunity, not source proof. A suspect ingredient lot is a hypothesis until records, timing, samples and other evidence support it. Multiple diners can become ill for different reasons.

### CDC — restaurant environmental assessment

Sources:

- https://www.cdc.gov/restaurant-food-safety/php/investigations/index.html
- https://www.cdc.gov/restaurant-food-safety/php/investigations/ea-definitions.html
- https://www.cdc.gov/restaurant-food-safety/php/investigations/why-investigators-did-or-did-not-do-environmental-assessments.html

Useful abstractions:

- inspection and outbreak environmental assessment are different activities;
- investigators look for contributing factors and underlying system conditions;
- an investigation can be limited by staffing, access or jurisdiction.

Reusable Ouros lesson:

A venue can pass a routine inspection and later have an incident. An incident review should preserve the actual observations instead of converting every deviation into root cause.

Do not import modern public-health law or jurisdiction structures into Ouros.

### FDA — lot-level traceability

Sources:

- https://www.fda.gov/food/food-safety-modernization-act-fsma/traceability-lot-code
- https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods
- https://www.fda.gov/food/food-safety-modernization-act-fsma/frequently-asked-questions-fsma-food-traceability-rule

Useful abstractions:

- a physical lot can keep a stable lot identity through handling;
- transformation is the point where a new lot/batch relationship may need to be recorded;
- traceability works by linking events and locations rather than by assigning guilt;
- restaurants can receive ingredients whose source information is stored separately from the food itself.

Reusable Ouros lesson:

A kitchen preparation batch should link backwards to ingredient lots and forward to servings. Shipping an ingredient does not create a new ingredient identity. Transforming several lots into one sauce or stew should create a new preparation batch with parent links.

Do not import FSMA regulation, mandatory record fields or enforcement rules into Ouros.

### FDA Food Code — preparation state matters

Source: https://www.fda.gov/media/184685/download

The Food Code distinguishes handling stages such as cooking, cooling, holding and reheating and explains that later handling can introduce new risks even after an earlier cooking step.

Reusable Ouros lesson:

`cooked=true` is insufficient. If Ouros ever tracks safety-relevant preparation state, it should preserve the sequence of preparation/holding events and observations. The narrative layer should remain qualitative unless exact numeric rules are intentionally authored.

### WHO — safer-food process model

Source: https://www.who.int/docs/default-source/food-safety/five-keys-to-safer-food-poster/5keys-en.pdf

WHO separates cleanliness, raw/cooked separation, cooking, temperature control and safe water/raw materials.

Reusable Ouros lesson:

Food safety is a system of multiple barriers. A venue may have one weak point while others function correctly. A single failed observation should not automatically imply every dish is unsafe.

Do not import real-world temperatures, pathogens or mandatory thresholds as Ouros rules without explicit canon/rules decisions.

## PTU / project cross-check

The project Food layer already states that mechanical food definitions belong to PTU/Caelo/AutoPTU, while physical batches, recipes and service events belong to narrative world state. It also already contains `contamination_case_id` as a link point, which is evidence that a dedicated safety layer should reference Food rather than replace it.

AutoPTU data accessible in the current Python repository contains the PTU 1.05 trainer/feature material and Chef-related mechanical content. The existence of Chef/Food Buff mechanics does not establish a generic spoilage, contamination, foodborne-illness or kitchen-hazard subsystem.

The complete Caelo corpus was not recoverable as a reliable invocable source in this run. Super PTU Online Helper was not exposed as a callable capability. No Caelo or Helper output is inferred.

## Design conclusions for Ouros

1. Food safety state should begin with a physical food/ingredient identity, not a diagnosis.
2. Preparation should create a traceable batch with parent ingredient lots.
3. One preparation batch can create many served portions; one service event can include several preparation batches.
4. A complaint is a signal, not proof.
5. A hold, withdrawal or discard is an operational decision, not a criminal finding.
6. A recall should preserve the original lot and transaction history rather than deleting records.
7. Inspection, outbreak investigation, toxicology, care and institutional adjudication remain separate authorities.
8. Routine safe service should compress into background state.
9. Safety incidents are most useful when they expose system relationships: supply chain, water, storage, equipment, staffing, maintenance, traceability or public communication.
10. Pokémon participation must remain individual and capability-grounded. No species becomes a universal thermometer, purifier, sanitizer, poison detector or safe-food guarantor.

## New narrative structures unlocked

- a shared sauce batch connects several meals while unrelated menu items remain unaffected;
- a venue voluntarily withdraws one ingredient before anyone becomes ill;
- a clinic cluster points to a festival, but records show the affected people ate from different stalls;
- a refrigerator outage produces a hold, but later review clears most stock;
- a batch is safe but mislabeled, creating a service/provenance problem rather than illness;
- a water-service interruption forces a kitchen to change its menu without becoming unsafe;
- a restaurant closes for investigation and later reopens with revised workflow;
- a supplier recall reaches institutions at different times because of route and communications state;
- a dish served during an old event becomes important years later because its ingredient provenance was unusually well recorded;
- a suspected Pokémon-caused contamination incident is weakened by timeline evidence showing the relevant Pokémon arrived after the problem began.

## Explicit non-inferences

This research does not authorize:

- foodborne disease mechanics;
- automatic Poisoned/Badly Poisoned;
- spoilage timers;
- pathogen simulation;
- numeric cooking-temperature checks;
- kitchen Skill DCs;
- Chef bonuses beyond exact PTU rules;
- Pokémon-based purification or contamination detection;
- restaurant closure authority;
- criminal liability;
- item destruction without world-state action;
- appetite/hunger systems;
- custom Food Buffs;
- Minecraft block temperature as rules authority.
