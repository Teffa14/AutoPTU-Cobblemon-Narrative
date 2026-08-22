# Drinking Water, Treatment & Distribution Research Scan — Pass 113

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.

Date: 2026-08-22.

## Scope

This pass investigates a gap between existing Ouros systems:

- Groundwater owns aquifers, wells, recharge, drawdown and springs.
- Freshwater owns catchments, rivers, reservoirs, lake/river regime and water-control assets.
- Stormwater owns rainfall runoff and drainage.
- Waste/Sanitation owns wastewater, waste streams and treatment of waste.
- Technology owns machines, pumps, power dependencies and technical faults.
- Health Surveillance owns health signals and outbreak investigation.

What was missing was the service chain that takes a raw source and turns it into water available at a household, clinic, market, school, factory or public tap:

`SOURCE -> INTAKE -> TREATMENT -> FINISHED-WATER STORAGE -> DISTRIBUTION -> SERVICE POINT`

The pass therefore focuses on drinking-water supply as infrastructure and institutional state, not on inventing PTU hydration rules.

## Source 1 — Pokémon: “Gotta Catch a Roggenrola!”

Source:
https://www.pokemon.com/us/animation/seasons/14/episode-34-gotta-catch-a-roggenrola

Useful structure:

- a Pokémon Center depends on a specific water source located in a cave;
- the service interruption is initially an observed infrastructure problem;
- a representative of the water company joins the investigation;
- the interruption and the Pokémon problem share a cause but remain distinct facts;
- restoration of service requires fixing the source interruption, not simply winning a battle.

Reusable Ouros lessons:

1. Clinics and other critical facilities should have explicit service dependencies.
2. A source can be geographically distant from the facility that depends on it.
3. Utility staff can be mission stakeholders without being combatants.
4. “No water at the clinic” should create an incident graph, not automatically a combat quest.
5. A battle can remove an obstruction while service restoration remains a separate technical action.

Do not copy the episode’s antagonists, cave layout, Roggenrola plot or dialogue.

## Source 2 — Pokémon: “Take the Lombre Home”

Source:
https://www.pokemon.com/us/animation/seasons/7/episode-23-take-the-lombre-home

Useful structure:

- a village receives water from a stream associated with a culturally significant site;
- residents blame a recently observed Pokémon for the shortage;
- investigation reveals deliberate diversion by a machine;
- cultural interpretation, observed drought, actual infrastructure interference and Pokémon presence are separate layers.

Reusable Ouros lessons:

1. Water-supply failures are good mystery structures because the visible symptom is downstream of the cause.
2. Community beliefs may shape public response without becoming world truth.
3. The same water source can be cultural, ecological and infrastructural at once.
4. Diversion, leakage, blocked intake and low source yield should be separate hypotheses.
5. Restoring flow does not automatically establish long-term reliability.

Do not reuse the shrine, Solrock accusation, Team Rocket device or resolution as Ouros canon.

## Source 3 — Pokémon: “Wake Up, Snorlax!”

Source summary:
https://tv.apple.com/us/episode/episode-41/umc.cmc.6nl4rrn6dz5kn8uspcbon85qb?showId=umc.cmc.721uypshyjjv0u0zbet4rqu71

Useful structure:

- regular rain can coexist with a dry downstream water supply;
- agriculture and food availability fail because water is not reaching users;
- the correct question is not only “is there water in the region?” but “is the service path functioning?”

Reusable Ouros lessons:

1. Regional rainfall is not equivalent to local water availability.
2. Source availability, conveyance and delivery need independent state.
3. A supply failure can propagate into Food, Agriculture, Hospitality and Demography.
4. Infrastructure investigations should follow the chain upstream rather than guessing from the endpoint.

## Source 4 — Pokémon: “Fossil Fools”

Source:
https://www.pokemon.com/us/animation/seasons/4/episode-6-fossil-fools

Useful structure:

- a reservoir flow interruption intersects with scientific activity and unexpected Pokémon presence;
- water infrastructure and research ecology can share a location without sharing the same explanatory model.

Reusable Ouros lessons:

- reservoirs can be simultaneously supply assets, research contexts and habitats;
- changing flow can expose or conceal biological/archaeological information;
- operational interventions should preserve provenance when they uncover scientific evidence.

## Source 5 — Pokémon: “The Young Flame Strikes Back!”

Source:
https://www.pokemon.com/us/animation/seasons/21/episode-26-the-young-flame-strikes-back

Useful structure:

- upstream land/control can affect downstream water access;
- ownership of one parcel does not imply authority over every downstream dependency;
- water-service disputes can intersect with land tenure without becoming a single system.

Reusable Ouros lesson:

Water access should reference boundary/access systems, source ownership/stewardship claims and actual hydraulic dependencies separately.

## Source 6 — EPA: How Does Your Water System Work?

Source:
https://www.epa.gov/sites/default/files/2017-10/documents/epa-ogwdw-publicwatersystems-final508.pdf

Useful architecture:

The public-system flow is presented as source -> treatment -> storage/distribution. The source may be surface water or groundwater and may be far from the end user.

Ouros abstraction:

- `RAW_WATER_SOURCE`
- `INTAKE`
- `TREATMENT_TRAIN`
- `FINISHED_WATER_STORAGE`
- `DISTRIBUTION_ZONE`
- `SERVICE_CONNECTION`

Do not import US regulation, statutory definitions or compliance requirements.

## Source 7 — EPA: Distribution System Pressure Management

Source:
https://www.epa.gov/system/files/documents/2021-12/ds-toolbox-fact-sheets_pressure-management.pdf

Useful architecture:

- pressure loss can be an operational incident in its own right;
- pressure management affects service reliability and potential intrusion risk;
- system state can vary by zone even when source and treatment are functioning.

Ouros abstraction:

A settlement should not use one `water_service = on/off` flag. Distribution zones can be:

- NORMAL
- DEGRADED
- LOW_PRESSURE
- INTERRUPTED
- ISOLATED_FOR_REPAIR
- EMERGENCY_SUPPLY
- UNKNOWN

Exact numeric pressure thresholds are intentionally not imported.

## Source 8 — EPA: Water Availability and Variability Guidance

Source:
https://www.epa.gov/system/files/documents/2021-11/water-availabity-guidance_508_final11921.pdf

Useful architecture:

- leaks and pressure management interact;
- supply reliability depends on infrastructure condition and demand, not only source volume;
- elevation can make service conditions differ across one network.

Ouros abstraction:

Leak detection, pressure-zone history, asset condition and peak-demand episodes should remain distinguishable.

## Source 9 — Drinking-water quality guidance / distribution controls

Source surfaced through EPA-hosted material:
https://www.epa.gov/sites/default/files/2014-03/documents/guidelines_for_drinking_water_quality_3v.pdf

Useful architecture:

- finished-water quality can change after treatment while water is stored or distributed;
- storage condition, stagnation, pressure, backflow and maintenance can matter downstream;
- “treatment plant produced acceptable water” and “water at a service point is acceptable” are different claims.

Ouros abstraction:

Keep treatment observations separate from distribution observations and service-point observations.

Do not import contaminant thresholds, disinfectant chemistry or health rules without project-specific canon/rules work.

## PTU / campaign-design relevance

No new PTU rules source was found that defines a generic potable-water subsystem. That is useful in itself: this pass should remain an overworld institutional/ecological layer.

A current public PTU discussion from November 2025 emphasizes open-ended campaign structure and placing hooks in the world for players to choose rather than requiring one route through a prepared plot:
https://www.reddit.com/r/PokemonTabletop/comments/1oz4e7w/first_time_dm_thinking_of_making_a_ptu_campaign/

Reusable design lesson:

A water-service problem should expose multiple legitimate approaches where world state supports them, for example:

- inspect the intake;
- compare treatment records;
- inspect a pressure zone;
- bring emergency supply;
- find a leak;
- protect technicians;
- reroute service;
- investigate a false contamination rumor;
- repair power to a pump;
- establish a temporary public distribution point.

The narrative should not force battle as the only valid solution.

## Cross-system opportunities

Drinking-water service can connect existing Ouros layers causally:

- Groundwater -> wells/raw source
- Freshwater -> rivers/reservoirs/raw source
- Technology -> pumps, valves, controls, backup power
- Supply Chains -> treatment consumables, spare parts, emergency water
- Workplaces -> operators, technicians, lab staff
- Health Surveillance -> downstream health signals
- Crisis -> outages, emergency distribution, recovery
- Public Information -> advisories and corrections
- Land Tenure -> access to source/intake/pipe easements
- Architecture -> buildings/tanks
- Manufacturing -> replacement parts
- Demography -> peak demand and service expansion
- Tourism/Events -> temporary demand surges
- Wild Ecology -> source/intake habitat conflicts

## Hard design protections derived from the research

Do not infer:

- water visible in Minecraft -> safe to drink;
- source full -> treatment functioning;
- treatment functioning -> distribution functioning;
- distribution functioning -> every endpoint has service;
- low pressure -> contamination occurred;
- contamination report -> contamination confirmed;
- clear water -> safe water;
- bad taste/odor report -> toxic water;
- one negative sample -> whole network safe;
- one positive sample -> source is the cause;
- Water-type Pokémon -> purification capability;
- Water Gun/Hydro Pump -> potable-water production;
- Rain Dance -> municipal supply solution;
- Hydration narrative -> PTU healing or status removal;
- battle victory -> service restored;
- leak -> sabotage;
- unauthorized valve position -> malicious intent;
- emergency water delivery -> permanent repair.

## Original high-level design directions for Ouros

The strongest reusable structures are:

1. Service-chain mysteries where the symptom appears far downstream of the cause.
2. Pressure-zone stories where one district has service and another does not.
3. Treatment-versus-distribution contradictions where plant data and endpoint samples differ.
4. Emergency-supply logistics that become visible before a technical repair is complete.
5. Infrastructure memory: old pipes, abandoned tanks, former wells and superseded maps remain part of Chronicle.
6. Demand-driven changes: festivals, growth, heat, fire response or industry can reveal weak points without any antagonist.
7. False-cause investigations where a Pokémon is blamed because it was visible near the incident.
8. Source protection conflicts where ecological habitat, cultural significance and utility access overlap.
9. Recovery reviews where service returns but the institution still needs to understand why the failure happened.
10. Multi-year capital history where replacement, redundancy and new zones change the same network over time.

## PTU/Caelo validation status

No reliable primary Caelo document or Super PTU Online Helper capability was available in this run.

No PTU mechanic is therefore inferred for:

- drinking;
- dehydration;
- purification;
- contamination;
- pressure;
- pipe breaks;
- treatment;
- emergency water;
- waterborne illness;
- environmental Poisoned;
- Water-type utility work;
- pump/valve operation.

Any such mechanic requires future direct validation against the project’s primary PTU/Caelo source set and the actual AutoPTU implementation.