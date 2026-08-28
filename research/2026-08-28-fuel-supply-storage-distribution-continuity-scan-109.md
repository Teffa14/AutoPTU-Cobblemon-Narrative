# Ouros Narrative Research — Fuel Supply, Storage & Distribution Continuity — Pass 109

Status: RESEARCH / PROVENANCE ONLY. This file creates no Ouros canon and no PTU rules.
Date: 2026-08-28
Baseline inspected: `aebe36f39eafb9d9554d3e302368b28b6de9d426`.

## Repository gap audit

The complete recursive repository inventory was inspected before writing and returned `truncated=false`.

Relevant existing authorities were then checked directly:

- `technology-energy-infrastructure-layer.md` owns generic technical assets, energy networks, faults, maintenance dependencies and fallback plans. It recognizes HEAT networks and consumable-resource dependencies but intentionally does not model a fuel supply chain.
- `infrastructure-outage-restoration-extension.md` owns cross-service outages, backups and staged restoration. It explicitly avoids inventing fuel quantities or reserve duration.
- `procurement-commissions-supplier-fulfillment-extension.md` owns sourcing, ordering, receipt and acceptance.
- `storage-warehousing-inventory-operations-continuity-extension.md` owns general storage location, putaway, picking, staging and inventory reconciliation.
- `courier-delivery-chain-of-custody-extension.md`, Ports, Railway and Road Passenger Transport own their respective transport/custody legs or services.
- `batch-traceability-recall-correction-extension.md` owns batch holds, recalls and quarantine decisions.
- `wildfire-fire-response-incident-continuity-extension.md` owns fire-specific incidents, response and residual verification.
- `waste-sanitation-recycling-pollution-layer.md` owns pollution/cleanup interpretation and response handoffs.
- Finance and Storefront own payment and customer-facing availability.

The uncovered operational seam is narrower: continuity of an authored fuel system after accepted supply enters that system and before a downstream consumer can actually use the supply. This includes terminal/depot identity, operating storage state, allocation, internal transfer, loading/release readiness, local delivery/service-point availability, shortage observations, temporary supply arrangements and staged restoration.

This pass does not define which fuels Ouros uses. Fuel technology remains regional canon.

## Public Pokémon sources

### Outskirt Stand — Pokémon Colosseum / XD

Source: https://bulbapedia.bulbagarden.net/wiki/Outskirt_Stand

Observed reusable structure:

- Orre contains a lonely gasoline stand/diner in a desert travel corridor.
- Travelers stop there during journeys.
- A fuel-service point can therefore be simultaneously infrastructure, commerce, social space and a recurring travel landmark.

Ouros transformation:

A small roadside supply point can matter even when the upstream fuel system is mostly off-screen. Its local stock/service state can change travel plans, worker routines and settlement traffic without turning it into a universal shop mechanic.

Excluded:

- specific characters;
- story sequence;
- dialogue;
- exact layout;
- prices;
- assumption that all Ouros vehicles use gasoline.

### Virbank Complex — Pokémon Black 2 / White 2

Source: https://bulbapedia.bulbagarden.net/wiki/Virbank_Industrial_Complex

Observed reusable structure:

- the industrial complex visibly distinguishes crude-oil processing equipment, gas handling and other industrial functions;
- industrial production and public travel coexist in the same city region;
- workers and production spaces create an ordinary social geography around technical infrastructure.

Ouros transformation:

A region can have several operational stages between source material and local availability. A processing facility, depot, distribution route and service point should remain separate objects with independent states.

Excluded:

- exact industrial process simulation;
- pressure calculations;
- real-world petroleum engineering;
- any assumption that Virbank technology is Ouros canon;
- the worker-battle side task.

### Oil Field Hideout and Sea of Wailord — Pokémon Ranger: Shadows of Almia

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Offshore_Oil_Platform_Hideout
- https://bulbapedia.bulbagarden.net/wiki/Sea_of_Wailord

Observed reusable structure:

- a once-active oil field can be shut down while the physical installation remains present;
- an old industrial site can be repurposed later;
- discarded material and pollution can remain relevant after original operations stop;
- offshore location creates distinct access and logistics constraints.

Ouros transformation:

Decommissioning must preserve industrial history. `source inactive`, `facility decommissioned`, `stock remaining`, `site accessible`, `site repurposed`, `environmental review complete` and `cleanup complete` are separate facts.

Pollution interpretation remains owned by the existing environmental systems. A legacy site does not become contaminated merely because the real inspiration involved contamination.

Excluded:

- Team Dim Sun;
- Miniremo production;
- boss encounters;
- kidnapping plot;
- exact access method;
- specific pollution event;
- any assumption of offshore oil extraction in Ouros.

### Pokémon Tabletop community homebrew — fossil/fuel discussion

Source: https://www.tapatalk.com/groups/pokemon_tabletop/pokemon-fossils-t3473.html

Classification: COMMUNITY HOMEBREW. Not PTU 1.05 authority.

Observed reusable lesson:

The tabletop community has explored petroleum and coal as world resources. The same post also invents prices, revival probabilities and mechanical bonuses. That makes it useful as a provenance boundary: worldbuilding ideas can be separated from unsupported rules.

Ouros transformation:

A region may eventually author fuel resources if canon chooses to. No price, damage bonus, revival rule, Torkoal interaction, extraction yield or fuel efficiency from this thread is imported.

### PTU public downloads page

Source: https://pokemontabletop.com/downloads-and-resources/

The official public resource page continues to identify PTU 1.05 as the downloadable rules corpus. Pass 109 uses the project's already-ingested PTU/Caelo material as governing mechanics evidence and treats community additions separately.

## External operational references

These sources are used only for high-level information architecture. They do not establish Ouros laws, safety procedures, engineering standards, quantities or technology.

### U.S. Department of Energy — local energy emergency planning

Source: https://www.energy.gov/ceser/local-leaders-prepare-energy-emergency

Reusable structure:

- understand where local energy supplies originate;
- distinguish supply sources from distribution paths and end uses;
- identify operators and vulnerable infrastructure;
- preserve contingency relationships instead of treating a shortage as one global boolean.

Ouros transformation:

An authored fuel service can preserve source/import handoff, depot, distribution path, service sector and downstream consumer links while leaving exact engineering out of scope.

### U.S. Department of Energy — Strategic Petroleum Reserve overview

Source: https://www.energy.gov/hgeo/opr/strategic-petroleum-reserve

Reusable structure:

Storage sites connect to pipelines, terminals and downstream facilities through multiple distribution relationships. The useful abstraction is topology and handoff state, not real capacities or national policy.

Ouros transformation:

A supply reserve may be physically present yet unavailable to a specific region until an authorized release and a viable path exist.

Excluded:

- real capacities;
- named companies;
- national reserve policy;
- emergency release law;
- pipeline operating procedures.

## Transformed design lessons

1. Fuel stock, fuel availability and downstream service availability need separate states.
2. A roadside service point can function as a recurring social/travel node even when the upstream network stays abstract.
3. Processing, storage, distribution and retail/service endpoints should not collapse into one facility flag.
4. A supply interruption may affect one sector, route or endpoint while neighboring areas continue operating.
5. Temporary supply can acquire social history and become a future landmark even after normal service returns.
6. Decommissioned infrastructure should preserve identity and provenance for later reuse, ecology, archaeology or cleanup stories.
7. A physical reserve can exist without being released, reachable or appropriate for every downstream use.
8. Shortage reports are scoped observations. They do not prove hoarding, sabotage, theft, price manipulation or technical failure.
9. A fuel-related fire, spill or contamination event must hand off to the systems that own those incident families rather than being simulated by this layer.
10. Pokémon involvement must be individual and evidenced. Species, Type, Ability visuals or proximity never grant extraction, refining, transport, ignition, extinguishing or power-generation competence.

## PTU / Caelo mechanical boundary

The project source scan identifies the following internal governing references:

- PTU Core Rulebook;
- Caelo Player's Guide 1.5;
- Caelo Region Location & Encounter List;
- character creation material;
- errata/extras;
- Pokédex material.

Pass 109 found no project evidence that establishes a universal PTU/Caelo subsystem for:

- fuel extraction;
- refining;
- fuel grade or quality arithmetic;
- tank capacity;
- transfer rate;
- pipeline flow;
- vehicle fuel consumption;
- generator fuel consumption;
- heating-fuel consumption;
- ignition probability;
- explosion or blast rules for generic fuel assets;
- fumes or exposure statuses;
- spill spread;
- environmental contamination from generic fuel blocks;
- fuel-powered Move bonuses;
- Fire-type ignition privilege;
- Water-type extinguishing privilege;
- Poison-type contamination immunity;
- Pokémon species-level fuel handling competence;
- universal technical checks for fuel transfer or terminal operation.

An exact Move, Ability, Item, Trainer Feature, Capability, authored Caelo condition or other governing rule can later provide a specific effect. Each effect still requires implementation evidence in the corresponding permanent engine capability family.

## Engine-facing research consequence

Fuel facilities are mechanically rich locations but should default to REDUCED tactical forms.

The intended full versions could eventually use:

- reviewed restricted/hazard zones;
- generalized reactions;
- protection/withdrawal objectives;
- Intercept or forced movement;
- tactical AI that understands evacuation and route control;
- semantic world-to-battle playback.

Current safe versions should isolate operations before battle, remove workers and fuel-handling equipment from BattleSpec, keep fuel assets noninteractive, and use static reviewed perimeter geometry.

## Provenance and canon policy

Everything in this file is research evidence or transformed design guidance.

No source above establishes:

- an Ouros petroleum industry;
- a specific fuel type;
- combustion-engine prevalence;
- a particular regional technology level;
- an oil field;
- a fuel company;
- a refinery;
- prices;
- extraction rights;
- environmental liability law;
- safety regulation;
- Pokémon labor assignments.

Those remain authored canon questions.
